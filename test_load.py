import openpyxl

wb = openpyxl.load_workbook('Day22-AI-Product-GTM-Monetization-Model.xlsx')

ws1 = wb['1_Cost_Job']
ws2 = wb['2_Pricing']
ws3 = wb['3_Value_Metric']
ws4 = wb['4_Channel_Fit']
ws5 = wb['5_90Day_Plan']
ws6 = wb['6_Benchmarks']

print("Loaded successfully")
