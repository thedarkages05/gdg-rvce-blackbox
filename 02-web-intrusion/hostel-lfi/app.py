# Source for hostel-lfi. Vulnerable logic:
# page = query?page, then page = page.replace("../", "")  # single pass only
# path = os.path.join("/challenge/pages", page); open(path)
# Bypass: ....// -> after one strip -> ../
