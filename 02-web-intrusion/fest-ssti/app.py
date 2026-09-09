# Source for fest-ssti (synthetic, stdlib-only, no Jinja dependency).
# render = "Hello " + name
# if "{{" in name: inner = between {{ }}; result = str(eval(inner, {"__builtins__": {}, "os": os}))
# This mimics SSTI: {{7*7}} -> 49, {{os.popen('cat /flag').read()}} -> flag
# Real Jinja payloads are similar: {{cycler.__init__.__globals__.os.popen(...)}}
