"""Build the README figures: the header and Table 1, each in a light and a dark variant.

    python3 assets/build.py

Standard library only. The fonts in assets/fonts are subsets (Basic Latin plus a little
punctuation) and get embedded in each SVG, because an SVG shown through an <img> tag cannot
load fonts from anywhere else. Edit ROWS to change the table, then rerun.
"""

import base64
from pathlib import Path

HERE = Path(__file__).parent

# GitHub's own foreground, muted, and border colors, so the figures sit in the page.
THEMES = {
    "light": {"ink": "#1f2328", "muted": "#59636e", "faint": "#d1d9e0", "accent": "#d9480f"},
    "dark": {"ink": "#f0f6fc", "muted": "#9198a1", "faint": "#3d444d", "accent": "#ff7b45"},
}

FONTS = {
    "serif": ("Instrument Serif", "normal", "InstrumentSerif-Regular.woff2"),
    "serif-italic": ("Instrument Serif", "italic", "InstrumentSerif-Italic.woff2"),
    "mono": ("DM Mono", "normal", "DMMono-Regular.woff2"),
}

SERIF = "'Instrument Serif', Georgia, serif"
MONO = "'DM Mono', ui-monospace, Menlo, monospace"

# Human ubiquitin, 76 residues.
UBIQUITIN = "MQIFVKTLTGKTITLEVEPSDTIENVKAKIQDKEGIPPDQQRLIFAGKQLEDGRTLSDYNIQKESTLHLVLRLRGG"

# Table 1. (where, what, status)
ROWS = [
    ("Lewis Lab, UC Berkeley", "peptide design for a mitochondrial RNA-degradation complex", "learning"),
    ("CAHL Lab, UC Berkeley", "accessible math figures in a Bayesian knowledge-tracing tutor", "building"),
    ("Berkeley Lab", "microbe traits across disease studies, on KG-Microbe", "analysis"),
    ("Scope Tutor-1", "does QLoRA on tutoring dialogues beat a good prompt?", "training"),
    ("Scope", "Lectra, Polya, and the extension, used by 400+ students", "shipping"),
]
TABLE_DATE = "October 2026"


def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def font_css(keys):
    rules = []
    for key in keys:
        family, style, filename = FONTS[key]
        data = base64.b64encode((HERE / "fonts" / filename).read_bytes()).decode()
        rules.append(
            f"@font-face{{font-family:'{family}';font-style:{style};font-weight:400;"
            f"src:url(data:font/woff2;base64,{data}) format('woff2')}}"
        )
    return "\n".join(rules)


def svg(width, height, title, style, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" role="img">\n'
        f"<title>{esc(title)}</title>\n<style>\n{style}\n</style>\n{body}\n</svg>\n"
    )


# ---------------------------------------------------------------- header


def attention_heads():
    """Four toy heads as (label, [(i, j, weight)]), residues 0-indexed."""
    n = len(UBIQUITIN)
    previous = [(i, i - 1, 0.25 + 0.75 * ((i * 37) % 11) / 10) for i in range(1, n)]

    helix = []  # the alpha helix, residues 23-34, and the short 3-10 helix at 56-59
    for i in range(22, 31):
        helix.append((i, i + 4, 0.95 if i % 2 else 0.6))
        helix.append((i, i + 3, 0.45))
    helix.append((55, 58, 0.8))

    strands = []  # the N-terminal hairpin, and the first strand against the last
    for k, i in enumerate(range(0, 7, 2)):
        strands.append((i, 16 - i, 0.95 - 0.1 * k))
        strands.append((i, 64 + i, 0.85 - 0.1 * k))
    strands += [(40, 48, 0.7), (42, 46, 0.55), (44, 68, 0.6), (43, 66, 0.45)]

    # Ubiquitin chains link through M1 or one of seven lysines. Let them all look at K48.
    linkage = [(i, 47, 0.95 if i in (0, 62) else 0.6) for i in (0, 5, 10, 26, 28, 32, 62)]

    return [
        ("head 1 / previous residue", previous),
        ("head 2 / i+3, i+4 in the helix", helix),
        ("head 3 / strand pairing", strands),
        ("head 4 / chain linkage sites", linkage),
    ]


def header(theme):
    c = THEMES[theme]
    width, height = 1000, 404
    x0, x1, baseline = 6, 994, 334
    pitch = (x1 - x0) / (len(UBIQUITIN) - 1)
    foot = baseline - 14
    cycle, heads = 16, attention_heads()
    slot = cycle / len(heads)

    def x(i):
        return x0 + i * pitch

    def arc(i, j):
        a, b = sorted((x(i), x(j)))
        h = 9 + 84 * (abs(i - j) / (len(UBIQUITIN) - 1)) ** 0.62
        lift = foot - h * 4 / 3
        return f"M{a:.1f} {foot}C{a:.1f} {lift:.1f} {b:.1f} {lift:.1f} {b:.1f} {foot}"

    ghost, live, marks, labels = [], [], [], []
    for n, (label, pairs) in enumerate(heads):
        start = n * slot - 1.2
        if n:  # the previous-residue bumps would turn the faint layer into a coil
            ghost += [f'<path d="{arc(i, j)}"/>' for i, j, _ in pairs]
        ordered = sorted(pairs, key=lambda p: min(p[0], p[1]))
        for k, (i, j, w) in enumerate(ordered):
            live.append(
                f'<path class="a" pathLength="1" stroke-opacity="{w:.2f}" d="{arc(i, j)}" '
                f'style="animation-delay:{start + k * 1.1 / len(ordered):.2f}s"/>'
            )
        touched = sorted({i for i, j, _ in pairs} | {j for i, j, _ in pairs})
        if len(touched) < len(UBIQUITIN) - 4:
            letters = "".join(
                f'<text x="{x(i):.1f}" y="{baseline}">{UBIQUITIN[i]}</text>' for i in touched
            )
            marks.append(f'<g class="m" style="animation-delay:{start:.2f}s">{letters}</g>')
        labels.append(
            f'<text class="m" x="{x1}" y="{foot - 104}" text-anchor="end" '
            f'style="animation-delay:{start:.2f}s">{esc(label)}</text>'
        )

    residues = "".join(
        f'<text x="{x(i):.1f}" y="{baseline}">{r}</text>' for i, r in enumerate(UBIQUITIN)
    )

    style = f"""{font_css(["serif", "serif-italic", "mono"])}
.eyebrow{{font:12.5px {MONO};letter-spacing:2.4px;fill:{c['muted']}}}
.name{{font:92px {SERIF};fill:{c['ink']};letter-spacing:-0.5px}}
.tag{{font:italic 28px {SERIF};fill:{c['muted']}}}
.seq text{{font:11.5px {MONO};fill:{c['muted']};text-anchor:middle;opacity:.55}}
.marks text{{font:11.5px {MONO};fill:{c['accent']};text-anchor:middle}}
.ghost{{fill:none;stroke:{c['faint']};stroke-width:1;opacity:.55}}
.live{{fill:none;stroke:{c['accent']};stroke-width:1.35;stroke-linecap:round}}
.label{{font:11.5px {MONO};fill:{c['muted']}}}
.fig{{font:11.5px {MONO};fill:{c['muted']}}}
.a{{stroke-dasharray:1;stroke-dashoffset:1;opacity:0;animation:draw {cycle}s cubic-bezier(.3,.1,.2,1) infinite both}}
.m{{opacity:0;animation:show {cycle}s ease-in-out infinite both}}
@keyframes draw{{0%{{stroke-dashoffset:1;opacity:0}}3%{{opacity:1}}13%{{stroke-dashoffset:0}}22%{{stroke-dashoffset:0;opacity:1}}27%,100%{{stroke-dashoffset:0;opacity:0}}}}
@keyframes show{{0%{{opacity:0}}4%,22%{{opacity:1}}27%,100%{{opacity:0}}}}
@media (prefers-reduced-motion:reduce){{.a,.m{{animation:none}}}}"""

    body = f"""<text class="eyebrow" x="2" y="58">UC BERKELEY  ·  MOLECULAR &amp; CELL BIOLOGY + DATA SCIENCE  ·  2028</text>
<text class="name" x="-3" y="146">Noel Sason</text>
<text class="tag" x="0" y="194">How do you know a model does what its number says?</text>
<g class="ghost">{''.join(ghost)}</g>
<g class="live">{''.join(live)}</g>
<g class="seq">{residues}</g>
<g class="marks">{''.join(marks)}</g>
<g class="label">{''.join(labels)}</g>
<text class="fig" x="1" y="378">Fig. 1. Toy attention heads over human ubiquitin, 76 residues. Illustrative, not from a trained model.</text>"""

    title = "Noel Sason. UC Berkeley, Molecular & Cell Biology + Data Science, 2028."
    return svg(width, height, title, style, body)


# ---------------------------------------------------------------- table 1


def table(theme):
    c = THEMES[theme]
    width = 1000
    left, what_x, status_x, right = 1, 254, 868, 999
    top, head_y, mid, first, step = 58, 84, 98, 136, 42
    bottom = first + step * (len(ROWS) - 1) + 20
    height = bottom + 12

    rows = []
    for k, (where, what, status) in enumerate(ROWS):
        y = first + step * k
        rows.append(
            f'<text class="where" x="{left}" y="{y}">{esc(where)}</text>'
            f'<text class="what" x="{what_x}" y="{y}">{esc(what)}</text>'
            f'<circle class="dot" cx="{status_x + 4}" cy="{y - 5}" r="3.6" '
            f'style="animation-delay:{k * 0.45:.2f}s"/>'
            f'<text class="status" x="{status_x + 16}" y="{y}">{esc(status)}</text>'
        )

    style = f"""{font_css(["serif", "serif-italic", "mono"])}
.tlabel{{font:12.5px {MONO};letter-spacing:2.4px;fill:{c['ink']}}}
.tcap{{font:italic 22px {SERIF};fill:{c['muted']}}}
.th{{font:11px {MONO};letter-spacing:1.8px;fill:{c['muted']}}}
.where{{font:23px {SERIF};fill:{c['ink']}}}
.what{{font:13.5px {MONO};fill:{c['muted']}}}
.status{{font:13.5px {MONO};fill:{c['ink']}}}
.rule{{stroke:{c['ink']}}}
.dot{{fill:{c['accent']};animation:pulse 2.8s ease-in-out infinite both}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
@media (prefers-reduced-motion:reduce){{.dot{{animation:none}}}}"""

    body = f"""<text class="tlabel" x="{left + 1}" y="30">TABLE 1</text>
<text class="tcap" x="{left + 94}" y="31">What I am working on, {esc(TABLE_DATE)}.</text>
<line class="rule" x1="{left}" x2="{right}" y1="{top}" y2="{top}" stroke-width="1.4"/>
<text class="th" x="{left}" y="{head_y}">WHERE</text>
<text class="th" x="{what_x}" y="{head_y}">WHAT</text>
<text class="th" x="{status_x}" y="{head_y}">STATUS</text>
<line class="rule" x1="{left}" x2="{right}" y1="{mid}" y2="{mid}" stroke-width="0.7"/>
{''.join(rows)}
<line class="rule" x1="{left}" x2="{right}" y1="{bottom}" y2="{bottom}" stroke-width="1.4"/>"""

    title = f"Table 1. What I am working on, {TABLE_DATE}. " + " ".join(
        f"{where}: {what} ({status})." for where, what, status in ROWS
    )
    return svg(width, height, title, style, body)


def main():
    for theme in THEMES:
        (HERE / f"header-{theme}.svg").write_text(header(theme))
        (HERE / f"table-{theme}.svg").write_text(table(theme))
    for path in sorted(HERE.glob("*.svg")):
        print(f"{path.relative_to(HERE.parent)}  {path.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
