import difflib

def generate_diff(text1, text2):
    diff = difflib.HtmlDiff().make_file(
        text1.splitlines(),
        text2.splitlines(),
        fromdesc='Model 1 Summary',
        todesc='Model 2 Summary'
    )
    return diff
