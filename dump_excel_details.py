import openpyxl
import sys

sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.load_workbook('Day22-AI-Product-GTM-Monetization-Model.xlsx', data_only=False)

for name in wb.sheetnames:
    ws = wb[name]
    print(f"\n{'='*30} SHEET: {name} {'='*30}")
    for r in range(1, ws.max_row + 1):
        row_str = []
        for c in range(1, ws.max_column + 1):
            cell = ws.cell(r, c)
            if cell.value is not None:
                # check if cell has yellow fill or formula
                fill_color = ""
                if cell.fill and cell.fill.start_color and cell.fill.start_color.rgb:
                    fill_color = f"[{cell.fill.start_color.rgb}]"
                val = str(cell.value)
                row_str.append(f"{cell.coordinate}{fill_color}={val}")
        if row_str:
            print(f"Row {r:2d}: " + " | ".join(row_str))
