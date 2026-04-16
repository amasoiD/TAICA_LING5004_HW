import re, sys
text = open(sys.argv[1], encoding="utf-8").read()
chars = ["paper", "spool", "cut", "fold", "toy"]
for c in chars:
    n = len(re.findall(c, text))
    bar = "█" * (n // 5)
    print(f"{c:<6} {n:4}次  {bar}")
