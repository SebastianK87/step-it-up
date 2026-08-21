#!/usr/bin/env python3
"""
Erzeugt lila/index.html aus index.html.

Die Lila-Fassung ist kein zweites Dokument, sondern eine Ableitung. Alle Inhalte
stehen nur einmal, naemlich in index.html. Hier liegen ausschliesslich Farben,
Schriften und die laute Schicht.

Aufruf:  python3 build-lila.py
"""
import pathlib
import re
import sys

HIER = pathlib.Path(__file__).parent
QUELLE = HIER / "index.html"
ZIEL = HIER / "lila" / "index.html"


LAUT = """
/* ============================================================
   ENTWURF LILA, die laute Schicht.
   Regel fuer die Signalfarbe: nur auf Dunkel oder als Flaeche
   mit dunkler Schrift. Nie als Text auf Hell.
   ============================================================ */
body{letter-spacing:-.005em}
h2{font-size:clamp(34px,6.6vw,84px)}

/* Lila auf Dunkel immer aufgehellt, sonst zu wenig Kontrast */
.deep em.s,.dark em.s{color:var(--terra-lift)}
.deep .kicker,.dark .kicker{color:var(--signal)}
.deep .kicker::before,.dark .kicker::before{background:var(--signal)}
.deep .ico [pathLength],.dark .ico [pathLength]{stroke:var(--signal)}
.deep .step .when,.dark .step .when{color:var(--signal)}
.deep .step ul li::before,.dark .step ul li::before{background:var(--signal)}
.deep .big .v,.dark .big .v,.deep .band .n,.dark .band .n{color:var(--signal)}
.deep .step.in::before,.dark .step.in::before{background:var(--signal);border-color:var(--signal)}
.negations span:last-child{color:var(--signal)}
.logo .wm span:nth-child(3){color:var(--signal)}
.logo .mark i{background:var(--signal)}
.rings a.on i{background:var(--signal);border-color:var(--signal)}
.dark .path .p::before,.deep .path .p::before{color:var(--signal)}
.dark .rule .note,.deep .rule .note{color:var(--signal)}
.dark .plan .m,.deep .plan .m{color:var(--signal)}
.tl-fill{background:linear-gradient(var(--signal),var(--terra-lift))}
#bar{background:linear-gradient(90deg,var(--signal),var(--terra-lift))}

/* Der Signal-Knopf */
.btn{font-family:'Syne',sans-serif;font-weight:800;letter-spacing:.02em;border-radius:0}
.btn-p{background:var(--signal);color:var(--ink);font-weight:800}
.btn-p:hover{background:#E4FF66}
.btn-g{border-color:var(--on-dark-20)}

/* Kapitelzahlen groesser und kantiger */
.chapter .num{font-family:'Syne',sans-serif;font-weight:800;-webkit-text-stroke-width:2px}
.deep .chapter .num,.dark .chapter .num{-webkit-text-stroke-color:var(--signal)}
.chapter .lbl{font-family:'Syne',sans-serif;font-weight:800;letter-spacing:.16em}
.deep .chapter .lbl,.dark .chapter .lbl{color:var(--signal)}

/* Hero */
.hero h1 .l3{color:var(--signal)}
.hero .veil{background:linear-gradient(180deg,rgba(24,4,37,.82) 0%,rgba(24,4,37,.4) 32%,rgba(24,4,37,.9) 78%,var(--plum-deep) 100%)}
.hero .veil2{background:radial-gradient(120% 80% at 76% 16%,rgba(123,44,245,.55),transparent 62%)}
.hero video{filter:saturate(.72) contrast(1.08) hue-rotate(-12deg)}
.hero .by{color:var(--on-dark)}
.hero .claim{font-family:'Syne',sans-serif;font-weight:800;letter-spacing:-.03em}

/* Laufband, der lauteste Ton der Seite */
.ticker{background:var(--signal);color:var(--ink);overflow:hidden;padding:15px 0;
  border-top:3px solid var(--ink);border-bottom:3px solid var(--ink)}
.ticker div{display:flex;width:max-content;animation:roll 34s linear infinite}
.ticker span{font-family:'Syne',sans-serif;font-weight:800;text-transform:uppercase;
  font-size:clamp(17px,2.3vw,27px);letter-spacing:-.02em;white-space:nowrap;padding-right:34px}
.ticker i{font-style:normal;padding-right:34px;font-size:clamp(17px,2.3vw,27px);opacity:.5}
@keyframes roll{from{transform:translateX(0)}to{transform:translateX(-50%)}}
@media(prefers-reduced-motion:reduce){.ticker div{animation:none}}

/* Aussagen und Karten haerter */
.statement{font-family:'Syne',sans-serif;font-weight:800;letter-spacing:-.038em}
.card{border-radius:0}
.tint .card{background:#fff;border:1px solid var(--hair)}
.negations span{font-family:'Syne',sans-serif;font-weight:700}
.nav .logo,.rings a{font-family:'Syne',sans-serif;font-weight:800}
</style>"""

TICKER = """</header>
<div class="ticker" aria-hidden="true"><div>
  <span>Bewegung muss man sich nicht verdienen.</span><i>/</i><span>Step it up.</span><i>/</i><span>Ganz Deutschland tanzt.</span><i>/</i><span>Fang du an.</span><i>/</i>
  <span>Bewegung muss man sich nicht verdienen.</span><i>/</i><span>Step it up.</span><i>/</i><span>Ganz Deutschland tanzt.</span><i>/</i><span>Fang du an.</span><i>/</i>
</div></div>"""


def ersetze(text, alt, neu, was):
    if alt not in text:
        sys.exit(f"ABBRUCH: '{was}' nicht in index.html gefunden. Vorlage geaendert?")
    return text.replace(alt, neu, 1)


def main():
    t = QUELLE.read_text(encoding="utf-8")

    # --- Schriften: Syne (Display), Space Grotesk (Text), Allura (Signatur) ---
    t = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?[^"]*" rel="stylesheet">',
        '<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800'
        '&family=Space+Grotesk:wght@400;500;700&family=Instrument+Serif:ital@1'
        '&family=Allura&display=swap" rel="stylesheet">',
        t, count=1)

    t = ersetze(t, "<title>STEP IT UP by Nikeata Thompson</title>",
                "<title>STEP IT UP by Nikeata Thompson, Entwurf Lila</title>", "Titel")
    t = ersetze(t, "<rect width='80' height='80' fill='%233A1B30'/><g fill='%23E2542B'>",
                "<rect width='80' height='80' fill='%23180425'/><g fill='%23D8FF33'>", "Favicon")

    # --- Farbtoken ---
    t = ersetze(t, """:root{
  --cream:#F9F4EE; --blush:#F3DED3; --blush-2:#EBCEC0;
  --ink:#1E1418; --ink-64:rgba(30,20,24,.64); --ink-38:rgba(30,20,24,.38); --hair:rgba(30,20,24,.13);
  --plum:#3A1B30; --plum-2:#4E2440; --plum-deep:#25101F;
  --terra:#E2542B; --rose:#C9556E;
  --on-dark:#F6EBE3; --on-dark-62:rgba(246,235,227,.62); --on-dark-20:rgba(246,235,227,.2);""",
""":root{
  /* Entwurf 2: Lila und Signal. Lauter, frecher, juengerer Ton. */
  --cream:#F5F0FF; --blush:#E7DCFB; --blush-2:#D6C4F5;
  --ink:#190A28; --ink-64:rgba(25,10,40,.66); --ink-38:rgba(25,10,40,.4); --hair:rgba(25,10,40,.14);
  --plum:#2C0A47; --plum-2:#3D1263; --plum-deep:#180425;
  --terra:#7B2CF5;            /* das Lila, auf hellem Grund lesbar, 5,4:1 */
  --terra-lift:#A96BFF;       /* dasselbe Lila aufgehellt, fuer dunklen Grund, 5,0:1 */
  --signal:#D8FF33;           /* Signalfarbe, nur auf Dunkel oder als Flaeche */
  --rose:#FF2E88;
  --on-dark:#F3ECFF; --on-dark-62:rgba(243,236,255,.66); --on-dark-20:rgba(243,236,255,.22);""",
        "Farbtoken")

    # --- Schriftfamilien ---
    t = ersetze(t, """  font-family:'Archivo',system-ui,sans-serif;font-variation-settings:'wdth' 100;
  font-size:17px;line-height:1.62;""",
                """  font-family:'Space Grotesk',system-ui,sans-serif;
  font-size:17px;line-height:1.6;""", "Body-Schrift")

    t = ersetze(t, "h1,h2,h3{font-variation-settings:'wdth' 118,'wght' 900;text-transform:uppercase;line-height:.9;letter-spacing:-.028em}",
                """h1,h2,h3{font-family:'Syne',system-ui,sans-serif;font-weight:800;font-variation-settings:normal;
  text-transform:uppercase;line-height:.88;letter-spacing:-.035em}""", "Display-Schrift")

    t = ersetze(t, "h3{font-size:clamp(17px,1.7vw,21px);font-variation-settings:'wdth' 112,'wght' 800;line-height:1.1;",
                "h3{font-size:clamp(17px,1.7vw,21px);font-weight:700;line-height:1.12;", "h3")

    t = ersetze(t, """em.s{font-family:'Fraunces',Georgia,serif;font-style:italic;font-variation-settings:'SOFT' 45,'WONK' 1,'opsz' 90;
  font-weight:400;text-transform:none;letter-spacing:-.005em;color:var(--terra)}""",
                """em.s{font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-variation-settings:normal;
  font-weight:400;text-transform:none;letter-spacing:-.01em;color:var(--terra)}""", "Serif-Akzent")

    t = t.replace("'Archivo',sans-serif", "'Space Grotesk',sans-serif")
    t = t.replace("'Archivo',system-ui", "'Space Grotesk',system-ui")
    # Variable-Achsen, die Syne und Space Grotesk nicht haben
    t = re.sub(r"font-variation-settings:'wdth' \d+,'wght' \d+", "font-weight:700", t)

    # Inline-Lila auf dunklem Grund
    t = t.replace('<h3 style="color:var(--terra)">Founder Member</h3>',
                  '<h3 style="color:var(--signal)">Founder Member</h3>', 1)

    # --- Die laute Schicht und das Laufband ---
    t = ersetze(t, "</style>", LAUT, "Style-Ende")
    t = ersetze(t, "</header>", TICKER, "Header-Ende")

    t = t.replace('<p class="datum">Arbeitsstand &middot; August 2026</p>',
                  '<p class="datum">Entwurf 2 &middot; Lila und Signal</p>', 1)

    # --- Pfade eine Ebene hoeher ---
    t = t.replace('"assets/', '"../assets/')
    t = t.replace('href="boutique/"', 'href="../boutique/"')
    t = t.replace('href="moodboards/"', 'href="../moodboards/"')
    t = t.replace('href="logo/"', 'href="../logo/"')
    t = t.replace('href="lila/">Entwurf Lila</a>', 'href="../">Entwurf 1</a>')

    ZIEL.parent.mkdir(exist_ok=True)
    ZIEL.write_text(t, encoding="utf-8")
    print(f"lila/index.html erzeugt, {len(t)} Zeichen")


if __name__ == "__main__":
    main()
