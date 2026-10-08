import openpyxl

wb = openpyxl.load_workbook('Day22-AI-Product-GTM-Monetization-Model.xlsx', data_only=False)

def eval_cell(sheet, coord):
    cell = wb[sheet][coord]
    return cell.value

print("=== VERIFYING FORMULAS & INPUTS ===")
print("Tab 1:")
print("B5 (Job def):", eval_cell('1_Cost_Job', 'B5'))
print("B6 (HITL Var):", eval_cell('1_Cost_Job', 'B6'))
print("B9 (Jobs tried):", eval_cell('1_Cost_Job', 'B9'))
print("B10 (Containment):", eval_cell('1_Cost_Job', 'B10'))
print("B11 (Completed formula):", eval_cell('1_Cost_Job', 'B11'))
print("B12 (Escalated formula):", eval_cell('1_Cost_Job', 'B12'))
print("B27 (LLM cached formula):", eval_cell('1_Cost_Job', 'B27'))
print("B38 (Speech formula):", eval_cell('1_Cost_Job', 'B38'))
print("B43 (Infra formula):", eval_cell('1_Cost_Job', 'B43'))
print("B47 (Retry formula):", eval_cell('1_Cost_Job', 'B47'))
print("B56 (HITL formula):", eval_cell('1_Cost_Job', 'B56'))
print("B66 (Cost/Job formula):", eval_cell('1_Cost_Job', 'B66'))

print("\nTab 2:")
print("B5 (Cost/job ref):", eval_cell('2_Pricing', 'B5'))
print("B7 (Floor price formula):", eval_cell('2_Pricing', 'B7'))
print("B19 (Proposed price):", eval_cell('2_Pricing', 'B19'))
print("B20 (Multiple formula):", eval_cell('2_Pricing', 'B20'))
print("B21 (Gross Margin formula):", eval_cell('2_Pricing', 'B21'))
print("B33 (Breakeven formula):", eval_cell('2_Pricing', 'B33'))

print("\nTab 3:")
print("B10 (Attribution sum):", eval_cell('3_Value_Metric', 'B10'))
print("B18 (Autonomy sum):", eval_cell('3_Value_Metric', 'B18'))
print("B21 (Suggested metric formula):", eval_cell('3_Value_Metric', 'B21'))
print("B30 (Chosen metric):", eval_cell('3_Value_Metric', 'B30'))

print("\nTab 4:")
print("B5 (ARPU):", eval_cell('4_Channel_Fit', 'B5'))
print("B9 (CAC Budget formula):", eval_cell('4_Channel_Fit', 'B9'))
print("B16 (Deals/AE/day formula):", eval_cell('4_Channel_Fit', 'B16'))
print("B22 (CAC actual formula):", eval_cell('4_Channel_Fit', 'B22'))
print("B23 (Multiple formula):", eval_cell('4_Channel_Fit', 'B23'))
print("B34-D34 (Scores):", eval_cell('4_Channel_Fit', 'B34'), eval_cell('4_Channel_Fit', 'C34'), eval_cell('4_Channel_Fit', 'D34'))
print("B35 (Best channel formula):", eval_cell('4_Channel_Fit', 'B35'))
print("B38 (Chosen channel):", eval_cell('4_Channel_Fit', 'B38'))
print("B39 (Partner name):", eval_cell('4_Channel_Fit', 'B39'))

print("\nTab 5:")
print("B5 (Pain time):", eval_cell('5_90Day_Plan', 'B5'))
print("B8 (Integration point):", eval_cell('5_90Day_Plan', 'B8'))

print("\nTab 6:")
print("B3 (Date checked):", eval_cell('6_Benchmarks', 'B3'))
