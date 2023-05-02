from back import *
import os

if __name__ == '__main__':

    pdf.set_author('Gerbovics Tamás - CV')
    pdf.addpage()

    pdf.about_me(1, 'About me', r'src/about_me.txt')
    pdf.about_me_picture(1, 'Contact', r'src/contact.txt')
    pdf.professional_skills(1, 'Knowledges', r'src/about_me.txt')
    pdf.contact(1, 'Contact', r'src/contact.txt')
    pdf.addpage()

    pdf.mutlicell_work1(2, 'Work experience:', r'src/work_1.txt')
    pdf.mutlicell_work2(2, 'Work experience:', r'src/work_2.txt')
    pdf.mutlicell_work3(2, 'Work experience:', r'src/work_3.txt')
    pdf.mutlicell_work4(2, 'Work experience:', r'src/work_4.txt')
    pdf.mutlicell_work5(2, 'Work experience:', r'src/work_5.txt')
    pdf.mutlicell_work6(2, 'Work experience:', r'src/work_6.txt')
    pdf.addpage()

    pdf.mutlicell_school1(3, 'Schools:', r'src/school_1.txt')
    pdf.mutlicell_school2(3, 'Schools:', r'src/school_2.txt')
    pdf.mutlicell_school3(3, 'Additional studies:', r'src/school_3.txt')

    pdf.output(r'out/Gerbovics_Tamás-CV.pdf', 'F')

    def open_travel_pdf():
        fileName = "out/Gerbovics_Tamás-CV.pdf"
        os.system("start " + fileName)

    open_travel_pdf()


