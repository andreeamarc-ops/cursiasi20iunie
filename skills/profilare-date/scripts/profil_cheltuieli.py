#!/usr/bin/env python3
"""
profil_cheltuieli.py — partea de COD a skill-ului `profilare-date`.

Rulează calcule REALE pe un fișier CSV de cheltuieli (nu estimează): rezumat pe
coloane, totaluri pe categorie, anomalii — și scrie un grafic HTML *interactiv*
(filtrare + sortare) în outputs/.

E aici intenționat ca exemplu de skill care nu e doar un prompt, ci și o bucată
de cod care chiar se rulează (vezi Cursul 7). Folosește doar biblioteca standard.

Utilizare:
    python3 profil_cheltuieli.py <input.csv> <output.html> \\
        [--categorie COL] [--suma COL] [--din-memorie N]
"""
import argparse
import csv
import html
import sys
from collections import defaultdict


def to_number(value):
    """Încearcă să citească un număr dintr-un text (acceptă , sau . zecimal)."""
    if value is None:
        return None
    s = str(value).strip().replace(" ", "")
    if not s:
        return None
    # tratează 1.234,56 (RO) și 1234.56 (EN)
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".")
    else:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def guess_column(headers, candidates, rows, want_numeric):
    """Ghicește coloana de categorie/sumă dacă nu a fost dată explicit."""
    lower = {h.lower(): h for h in headers}
    for cand in candidates:
        if cand in lower:
            return lower[cand]
    # fallback: prima coloană (ne)numerică
    for h in headers:
        sample = [to_number(r.get(h)) for r in rows[:20]]
        numeric = sum(1 for x in sample if x is not None)
        if want_numeric and numeric >= max(1, len(sample) // 2):
            return h
        if not want_numeric and numeric < max(1, len(sample) // 2):
            return h
    return headers[-1] if want_numeric else headers[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path")
    ap.add_argument("html_path")
    ap.add_argument("--categorie", default=None)
    ap.add_argument("--suma", default=None)
    ap.add_argument("--din-memorie", type=float, default=None,
                    help="o cifră «din memorie» de verificat față de totalul real")
    ap.add_argument("--verifica-categorie", default=None,
                    help="dacă e dat, --din-memorie se compară cu totalul ACELEI categorii, nu cu totalul general")
    args = ap.parse_args()

    with open(args.csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)

    if not headers:
        print("CSV gol sau fără antet.", file=sys.stderr)
        sys.exit(1)

    cat_col = args.categorie or guess_column(headers, ["categorie", "category", "tip"], rows, want_numeric=False)
    sum_col = args.suma or guess_column(headers, ["suma", "sumă", "amount", "valoare", "total", "lei"], rows, want_numeric=True)

    totals = defaultdict(float)
    grand_total = 0.0
    anomalies = []
    clean_rows = []
    for i, r in enumerate(rows, start=2):  # +2: antet pe rândul 1
        cat = (r.get(cat_col) or "").strip() or "(fără categorie)"
        amount = to_number(r.get(sum_col))
        if amount is None:
            anomalies.append(f"rândul {i}: suma lipsește sau nu e număr ({r.get(sum_col)!r})")
            amount = 0.0
        elif amount < 0:
            anomalies.append(f"rândul {i}: sumă negativă ({amount:g}) la categoria «{cat}»")
        if (r.get(cat_col) or "").strip() == "":
            anomalies.append(f"rândul {i}: categorie lipsă")
        totals[cat] += amount
        grand_total += amount
        clean_rows.append({**r, "_cat": cat, "_amount": amount})

    by_cat = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)

    # ---- sumar pe stdout (intră în profil-cheltuieli.md) ----
    print(f"Fișier: {args.csv_path}  ({len(rows)} rânduri, {len(headers)} coloane)")
    print(f"Coloană categorie: «{cat_col}» · coloană sumă: «{sum_col}»\n")
    print("Totaluri pe categorie:")
    for cat, val in by_cat:
        print(f"  {cat:<28} {val:>12,.0f}")
    print(f"  {'TOTAL':<28} {grand_total:>12,.0f}\n")
    if args.din_memorie is not None:
        if args.verifica_categorie:
            real = totals.get(args.verifica_categorie, 0.0)
            eticheta = f"categoria «{args.verifica_categorie}»"
        else:
            real = grand_total
            eticheta = "totalul general"
        diff = real - args.din_memorie
        print(f"Verificare cifră din memorie ({eticheta}): din memorie {args.din_memorie:,.0f} → "
              f"în fișier {real:,.0f} → corect e {real:,.0f} "
              f"(diferență {diff:+,.0f}).\n")
    if anomalies:
        print("Anomalii:")
        for a in anomalies:
            print(f"  - {a}")
    else:
        print("Anomalii: niciuna evidentă.")

    write_html(args.html_path, headers, clean_rows, by_cat, grand_total, cat_col, sum_col)
    print(f"\nGrafic interactiv scris în: {args.html_path}")


def write_html(path, headers, rows, by_cat, grand_total, cat_col, sum_col):
    max_val = max((v for _, v in by_cat), default=1) or 1
    bars = "".join(
        f'<div class="bar-row" data-cat="{html.escape(cat)}">'
        f'<span class="bar-label">{html.escape(cat)}</span>'
        f'<span class="bar" style="width:{(val / max_val) * 100:.1f}%"></span>'
        f'<span class="bar-val">{val:,.0f}</span></div>'
        for cat, val in by_cat
    )
    head_cells = "".join(
        f'<th onclick="sortTable({i})">{html.escape(h)} &#x21C5;</th>'
        for i, h in enumerate(headers)
    )
    body_rows = "".join(
        "<tr>" + "".join(f"<td>{html.escape(str(r.get(h, '')))}</td>" for h in headers) + "</tr>"
        for r in rows
    )
    doc = f"""<!DOCTYPE html>
<html lang="ro"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Profil cheltuieli — interactiv</title>
<style>
  body {{ font-family: system-ui, sans-serif; margin: 2rem; color: #3C2814; background:#FCF8EC; }}
  h1,h2 {{ font-weight: 700; }}
  .bar-row {{ display:flex; align-items:center; gap:.5rem; margin:.25rem 0; }}
  .bar-label {{ width: 12rem; font-size:.9rem; }}
  .bar {{ height: 1.1rem; background:#FD483D; border-radius:3px; }}
  .bar-val {{ font-variant-numeric: tabular-nums; }}
  table {{ border-collapse: collapse; width: 100%; margin-top: 1rem; }}
  th, td {{ border: 1px solid #ECDFBD; padding: .4rem .6rem; text-align: left; font-size:.9rem; }}
  th {{ background:#ECDFBD; cursor: pointer; user-select:none; position: sticky; top:0; }}
  tr:nth-child(even) td {{ background: #fff8e7; }}
  input {{ padding:.4rem .6rem; margin: 1rem 0; width: 100%; max-width: 24rem;
           border:1px solid #B5A373; border-radius:6px; }}
  .total {{ margin-top:.5rem; font-weight:700; }}
</style></head>
<body>
  <h1>Profil cheltuieli</h1>
  <h2>Totaluri pe categorie</h2>
  {bars}
  <p class="total">TOTAL: {grand_total:,.0f}</p>

  <h2>Toate rândurile (filtrează &amp; sortează)</h2>
  <input id="filter" placeholder="filtrează… (scrie o categorie, o descriere, o sumă)"
         oninput="filterTable()">
  <table id="t"><thead><tr>{head_cells}</tr></thead><tbody>{body_rows}</tbody></table>

<script>
function filterTable() {{
  var q = document.getElementById('filter').value.toLowerCase();
  var rows = document.querySelectorAll('#t tbody tr');
  rows.forEach(function(r) {{
    r.style.display = r.innerText.toLowerCase().indexOf(q) > -1 ? '' : 'none';
  }});
}}
var sortDir = {{}};
function sortTable(col) {{
  var tb = document.querySelector('#t tbody');
  var rows = Array.prototype.slice.call(tb.querySelectorAll('tr'));
  var dir = sortDir[col] = !sortDir[col];
  rows.sort(function(a, b) {{
    var x = a.cells[col].innerText.trim(), y = b.cells[col].innerText.trim();
    var nx = parseFloat(x.replace(/[^0-9.,-]/g, '').replace('.', '').replace(',', '.'));
    var ny = parseFloat(y.replace(/[^0-9.,-]/g, '').replace('.', '').replace(',', '.'));
    if (!isNaN(nx) && !isNaN(ny)) return dir ? nx - ny : ny - nx;
    return dir ? x.localeCompare(y, 'ro') : y.localeCompare(x, 'ro');
  }});
  rows.forEach(function(r) {{ tb.appendChild(r); }});
}}
</script>
</body></html>"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(doc)


if __name__ == "__main__":
    main()
