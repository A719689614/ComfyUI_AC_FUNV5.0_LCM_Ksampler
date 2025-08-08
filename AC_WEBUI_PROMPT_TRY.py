from .AC_FUN_CateGory import ac_category
def prompt_expander(text, cur_step, steps, handle_escape_character=True):
    ret = ''
    escaping = False
    depth = 0

    substitution_parameters = []
    substitution_str = ''
    for i, c in enumerate(text):
        if not escaping:
            if handle_escape_character and c == '\\':
                escaping = True
                continue
            elif c == '[':
                if depth == 0:
                    substitution_parameters = []
                    substitution_str = ''
                    depth += 1
                    continue
                depth += 1
            elif c == ']':
                depth -= 1
                if depth < 0:
                    raise Exception(f"Prompt Error: Extra closing bracket at index {i}")
                elif depth == 0:
                    substitution_parameters.append(substitution_str)
                    substitution_str = ''
                    if len(substitution_parameters) == 3 and substitution_parameters[2].replace('.','',1).isdigit():
                        threshold = round(float(substitution_parameters[2])*steps)
                        ret += prompt_expander(substitution_parameters[0] if cur_step < threshold else substitution_parameters[1], cur_step, steps, False)
                    else:
                        ret += prompt_expander(substitution_parameters[cur_step%len(substitution_parameters)], cur_step, steps, False)
                    continue
            elif depth == 1 and c == '|':
                substitution_parameters.append(substitution_str)
                substitution_str = ''
                continue

        if depth == 0:
            ret += c
        else:
            substitution_str += c
        escaping = False
    if depth != 0:
        raise Exception("Prompt Error: Missing closing bracket at the end of prompt")
    return ret

class AC_WEBUI_Prompt:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"text": ("STRING", {"multiline": True}), "clip": ("CLIP", ),
                              "cur_step": ("INT", {"default": 0, "min": 0, "max": 10000}),
                                "steps": ("INT", {"default": 5, "min": 1, "max": 10000}),
                                }}
    RETURN_TYPES = ("CONDITIONING", )
    FUNCTION = "encode"

    CATEGORY = ac_category()

    def encode(self, clip, text, cur_step, steps):
        tokens = clip.tokenize(prompt_expander(text,cur_step,steps))
        cond, pooled = clip.encode_from_tokens(tokens, return_pooled=True)
        return ([[cond, {"pooled_output": pooled}]],)





