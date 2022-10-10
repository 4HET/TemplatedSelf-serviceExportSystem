
from docxtpl import DocxTemplate

tpl = DocxTemplate("test.docx")
if tpl:
    tpl.replace_pic("Picture 1", "test.png")
tpl.save("end.docx")