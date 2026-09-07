import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'skill', 'scripts'))
import gen_mockups as g

BASE = os.path.dirname(os.path.abspath(__file__))
g.OUT = os.path.join(BASE, 'mockups'); os.makedirs(g.OUT, exist_ok=True)
A = os.path.join(BASE, 'assets')
LOGO = os.path.join(A, 'terra-logo.png'); LOGO_W = os.path.join(A, 'terra-logo-white.png')
MARK = os.path.join(A, 'terra-mark.png')

g.PAL = ("Brand terra, a specialty coffee roastery. Palette: espresso brown #2E201A, "
         "terracotta #C4633C, clay #E2A583, cream #F6EEE3, sage green #7E8C6F. "
         "Aesthetic: earthy, warm, artisanal, minimal. Soft natural light, no people, cream background. ")

JOBS = [
  ("cup",        "A cream paper coffee cup front view on a warm cream surface, the terra logo printed on the cup, a thin terracotta hills motif band near the base, soft natural shadow.", [LOGO]),
  ("bag",        "A terracotta coffee bag (stand up pouch) three quarter view on cream, the cream logo centered, kraft texture, coffee beans scattered near the base, soft shadow.", [LOGO_W]),
  ("storefront", "A warm minimal cafe storefront at golden hour, cream facade, the terra logo as a dimensional sign above the window, terracotta awning, photographic, no people.", [LOGO]),
]
for n, p, refs in JOBS:
    g.gemini(n, p, refs)
g.optimize()
print("TERRA DONE", flush=True)
