"""Génère les figures SVG du chapitre « lois continues » à partir des vraies fonctions (pas de dessin à la main)."""
import math

W, H, L, R, T, B = 360, 210, 40, 340, 20, 180


def sx(x, x0, x1):
    return L + (x - x0) / (x1 - x0) * (R - L)


def sy(y, y0, y1):
    return B - (y - y0) / (y1 - y0) * (B - T)


def path(f, a, b, x0, x1, y0, y1, n=160):
    pts = [(sx(a + (b - a) * i / n, x0, x1), sy(f(a + (b - a) * i / n), y0, y1)) for i in range(n + 1)]
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)


def area(f, a, b, x0, x1, y0, y1, n=120):
    d = path(f, a, b, x0, x1, y0, y1, n)
    return f"{d} L{sx(b, x0, x1):.1f},{sy(0, y0, y1):.1f} L{sx(a, x0, x1):.1f},{sy(0, y0, y1):.1f} Z"


def axes(x0, x1, y0, y1, xticks, yticks, xlabel, ylabel):
    out = [f'<line x1="{L}" y1="{sy(0, y0, y1):.1f}" x2="{R + 8}" y2="{sy(0, y0, y1):.1f}" class="stroke"/>',
           f'<line x1="{sx(max(x0, 0) if x0 >= 0 else 0, x0, x1):.1f}" y1="{B}" x2="{sx(max(x0, 0) if x0 >= 0 else 0, x0, x1):.1f}" y2="{T - 6}" class="stroke"/>']
    for v, lab in xticks:
        out.append(f'<text x="{sx(v, x0, x1):.1f}" y="{sy(0, y0, y1) + 15:.1f}" text-anchor="middle" font-size="11">{lab}</text>')
    for v, lab in yticks:
        out.append(f'<line x1="{L}" y1="{sy(v, y0, y1):.1f}" x2="{R}" y2="{sy(v, y0, y1):.1f}" class="muted" stroke-dasharray="2 4"/>')
        out.append(f'<text x="{L - 6}" y="{sy(v, y0, y1) + 4:.1f}" text-anchor="end" font-size="11">{lab}</text>')
    out.append(f'<text x="{R + 10}" y="{sy(0, y0, y1) + 4:.1f}" font-size="12">{xlabel}</text>')
    out.append(f'<text x="{L + 6}" y="{T - 4}" font-size="12">{ylabel}</text>')
    return "".join(out)


def svg(label, body):
    return f'<svg viewBox="0 0 {W} {H + 10}" role="img" aria-label="{label}">{body}</svg>'


def density_3x2():
    f = lambda x: 3 * x * x
    x0, x1, y0, y1 = 0, 1.1, 0, 3.2
    body = axes(x0, x1, y0, y1, [(0, "0"), (0.5, "0,5"), (1, "1")], [(1, "1"), (2, "2"), (3, "3")], "x", "f(x)")
    body += f'<path d="{area(f, 0.5, 1, x0, x1, y0, y1)}" class="venn-fill"/>'
    body += f'<path d="{path(f, 0, 1, x0, x1, y0, y1)}" class="accent" stroke-width="2"/>'
    body += f'<line x1="{sx(1, x0, x1):.1f}" y1="{sy(3, y0, y1):.1f}" x2="{sx(1, x0, x1):.1f}" y2="{sy(0, y0, y1):.1f}" class="accent" stroke-dasharray="3 3"/>'
    body += f'<text x="{sx(0.78, x0, x1):.1f}" y="{sy(0.55, y0, y1):.1f}" text-anchor="middle" font-size="12">7/8</text>'
    return svg("Densité 3x² et l'aire P(X ≥ 1/2)", body)


def cdf_x3():
    F = lambda x: 0 if x < 0 else (x ** 3 if x <= 1 else 1)
    x0, x1, y0, y1 = -0.3, 1.4, 0, 1.15
    body = axes(x0, x1, y0, y1, [(0, "0"), (0.5, "0,5"), (1, "1")], [(0.5, "0,5"), (1, "1")], "x", "F(x)")
    body += f'<path d="{path(F, -0.3, 1.4, x0, x1, y0, y1, 200)}" class="accent" stroke-width="2"/>'
    m = 2 ** (-1 / 3)
    body += f'<line x1="{sx(m, x0, x1):.1f}" y1="{sy(0.5, y0, y1):.1f}" x2="{sx(m, x0, x1):.1f}" y2="{sy(0, y0, y1):.1f}" class="ok" stroke-dasharray="3 3"/>'
    body += f'<text x="{sx(m, x0, x1):.1f}" y="{sy(0, y0, y1) + 28:.1f}" text-anchor="middle" font-size="11">médiane ≈ 0,79</text>'
    return svg("Fonction de répartition x³", body)


def exponential():
    x0, x1, y0, y1 = 0, 6, 0, 2.1
    body = axes(x0, x1, y0, y1, [(i, str(i)) for i in range(0, 6)], [(0.5, "0,5"), (1, "1"), (2, "2")], "t", "f(t)")
    for lam, cls, dash in [(2, "accent", ""), (1, "ok", ' stroke-dasharray="6 3"'), (0.5, "ko", ' stroke-dasharray="2 3"')]:
        body += f'<path d="{path(lambda t, l=lam: l * math.exp(-l * t), 0, 6, x0, x1, y0, y1)}" class="{cls}" stroke-width="2"{dash}/>'
    body += f'<text x="{sx(0.55, x0, x1):.1f}" y="{sy(1.55, y0, y1):.1f}" font-size="11">λ = 2</text>'
    body += f'<text x="{sx(1.1, x0, x1):.1f}" y="{sy(0.55, y0, y1):.1f}" font-size="11">λ = 1</text>'
    body += f'<text x="{sx(3.1, x0, x1):.1f}" y="{sy(0.18, y0, y1):.1f}" font-size="11">λ = 0,5</text>'
    return svg("Densités exponentielles pour trois valeurs de lambda", body)


def normal95():
    phi = lambda x: math.exp(-x * x / 2) / math.sqrt(2 * math.pi)
    x0, x1, y0, y1 = -3.6, 3.6, 0, 0.45
    body = axes(x0, x1, y0, y1, [(-1.96, "−1,96"), (0, "0"), (1.96, "1,96")], [(0.1, "0,1"), (0.2, "0,2"), (0.3, "0,3"), (0.4, "0,4")], "x", "φ(x)")
    body += f'<path d="{area(phi, -1.96, 1.96, x0, x1, y0, y1)}" class="venn-fill"/>'
    body += f'<path d="{area(phi, -3.6, -1.96, x0, x1, y0, y1)}" class="ko-fill"/>'
    body += f'<path d="{area(phi, 1.96, 3.6, x0, x1, y0, y1)}" class="ko-fill"/>'
    body += f'<path d="{path(phi, -3.6, 3.6, x0, x1, y0, y1)}" class="accent" stroke-width="2"/>'
    body += f'<text x="{sx(0, x0, x1):.1f}" y="{sy(0.15, y0, y1):.1f}" text-anchor="middle" font-size="12">95 %</text>'
    body += f'<text x="{sx(-2.7, x0, x1):.1f}" y="{sy(0.05, y0, y1):.1f}" text-anchor="middle" font-size="11">2,5 %</text>'
    body += f'<text x="{sx(2.7, x0, x1):.1f}" y="{sy(0.05, y0, y1):.1f}" text-anchor="middle" font-size="11">2,5 %</text>'
    return svg("Densité normale centrée réduite et intervalle à 95 %", body)


FIGURES = {
    "{{SVG_DENSITY}}": density_3x2,
    "{{SVG_CDF}}": cdf_x3,
    "{{SVG_EXP}}": exponential,
    "{{SVG_NORMAL}}": normal95,
}

if __name__ == "__main__":
    import sys
    path_md = sys.argv[1]
    text = open(path_md, encoding="utf-8").read()
    for key, fn in FIGURES.items():
        text = text.replace(key, fn())
    open(path_md, "w", encoding="utf-8").write(text)
    print("figures insérées :", ", ".join(k for k in FIGURES))
