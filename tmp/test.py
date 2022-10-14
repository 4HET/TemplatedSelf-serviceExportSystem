from docx2pdf import convert

xywj_path = r"test.docx"

inputFile = xywj_path
outputFile = r"./output/{}_xywj.pdf".format(2020416089)
file = open(outputFile, "w")
file.close()

convert(inputFile, outputFile)