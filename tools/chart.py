"""results.csv에서 외부 라이브러리 없이 SVG 비교 그래프를 만든다."""

import csv
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "report"
COLORS = {
    "insertion_sort": "#d95f02",
    "merge_sort": "#1b9e77",
    "heap_sort": "#7570b3",
}


def load_results():
    with (REPORT / "results.csv").open(encoding="utf-8", newline="") as file:
        return [
            {
                "input_type": row["input_type"],
                "n": int(row["n"]),
                "algorithm": row["algorithm"],
                "median_ms": float(row["median_ms"]),
            }
            for row in csv.DictReader(file)
        ]


def line_chart(rows, title, output):
    width, height = 920, 520
    left, right, top, bottom = 92, 28, 65, 72
    plot_width = width - left - right
    plot_height = height - top - bottom
    sizes = sorted({row["n"] for row in rows})
    values = [max(row["median_ms"], 0.001) for row in rows]
    low = math.floor(math.log10(min(values)))
    high = math.ceil(math.log10(max(values)))
    high = max(high, low + 1)

    def x_position(n):
        return left + sizes.index(n) * plot_width / (len(sizes) - 1)

    def y_position(value):
        ratio = (math.log10(max(value, 0.001)) - low) / (high - low)
        return top + plot_height * (1 - ratio)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<style>text{font-family:DejaVu Sans,Arial,sans-serif;fill:#222}.grid{stroke:#ddd}.axis{stroke:#333;stroke-width:1.5}</style>',
        f'<text x="{width / 2}" y="32" text-anchor="middle" font-size="20" font-weight="bold">{title}</text>',
    ]

    for exponent in range(low, high + 1):
        value = 10**exponent
        y = y_position(value)
        svg.append(f'<line class="grid" x1="{left}" y1="{y:.1f}" x2="{width-right}" y2="{y:.1f}"/>')
        svg.append(f'<text x="{left-10}" y="{y+4:.1f}" text-anchor="end" font-size="12">{value:g}</text>')
    for n in sizes:
        x = x_position(n)
        svg.append(f'<line class="grid" x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{height-bottom}"/>')
        svg.append(f'<text x="{x:.1f}" y="{height-bottom+24}" text-anchor="middle" font-size="12">{n:,}</text>')

    svg.extend([
        f'<line class="axis" x1="{left}" y1="{top}" x2="{left}" y2="{height-bottom}"/>',
        f'<line class="axis" x1="{left}" y1="{height-bottom}" x2="{width-right}" y2="{height-bottom}"/>',
        f'<text x="{width/2}" y="{height-20}" text-anchor="middle" font-size="14">Input size (n)</text>',
        f'<text x="20" y="{height/2}" text-anchor="middle" font-size="14" transform="rotate(-90 20 {height/2})">Median time (ms, log scale)</text>',
    ])

    for index, algorithm in enumerate(COLORS):
        selected = sorted(
            (row for row in rows if row["algorithm"] == algorithm),
            key=lambda row: row["n"],
        )
        points = [
            f'{x_position(row["n"]):.1f},{y_position(row["median_ms"]):.1f}'
            for row in selected
        ]
        color = COLORS[algorithm]
        svg.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{color}" stroke-width="3"/>')
        for point in points:
            x, y = point.split(",")
            svg.append(f'<circle cx="{x}" cy="{y}" r="4" fill="{color}"/>')
        legend_x = left + index * 180
        svg.append(f'<line x1="{legend_x}" y1="{height-48}" x2="{legend_x+24}" y2="{height-48}" stroke="{color}" stroke-width="3"/>')
        svg.append(f'<text x="{legend_x+31}" y="{height-43}" font-size="13">{algorithm}</text>')

    svg.append("</svg>")
    output.write_text("\n".join(svg), encoding="utf-8")


def main():
    rows = load_results()
    for input_type in ("random", "sorted", "reversed", "few_unique"):
        selected = [row for row in rows if row["input_type"] == input_type]
        line_chart(selected, f"Sorting time: {input_type} input", REPORT / f"time_{input_type}.svg")


if __name__ == "__main__":
    main()
