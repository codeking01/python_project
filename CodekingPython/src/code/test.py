from CodekingPython.Deal_Excel import Basic_Excle

exceldata=Basic_Excle.DoExcel(read_path=r'C:\Users\king\Desktop\CAS_ALL.xlsx')
exceldata=exceldata.Read_Data()
print(exceldata.cas_list)