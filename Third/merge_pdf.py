import os
from PyPDF2 import PdfFileMerger

target_path = os.getcwd() + r'/tmp/output'
pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

print(pdf_lst)
if os.path.exists("{}/merge.pdf".format(target_path)):
    os.remove("{}/merge.pdf".format(target_path))

file_merger = PdfFileMerger()
for pdf in pdf_lst:
    file_merger.append(pdf)     # 合并pdf文件

file_merger.write("{}/merge.pdf".format(target_path))