from fpdf import FPDF

header_image= r'src/header.png'
profile_image = r'src/profile image.jpg'
skill_image = r'src/skill_picture.png'

title = "Gerbovics Tamás - CV"

class PDF(FPDF):
    def __init__(self, **kwargs):
        super(PDF,self).__init__(**kwargs)
        self.add_font('delo', "", r"src\Roboto-Regular.ttf",
                      uni=True)

    def header(self):
        self.image(header_image,0,0,210,60)
        self.ln(55)

    def addpage(self):
        self.add_page()

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 12)
        self.set_text_color(52, 73, 94 )
        self.cell(0, 22,'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, label):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(52, 73, 94)
        self.set_text_color(244, 246, 247 )
        self.cell(0, 6, '%s' % (label), 0, 1, 'C', 1)
        self.ln(3)

    def chapter_body(self, name):
        with open(name, 'rb') as fh:
            txt = fh.read().decode('utf-8')
        self.set_font('delo',"", size=14)
        self.multi_cell(0, 5, txt)
        self.ln()
        self.set_font('delo',"", size=14)
        self.cell(0, 5, ' ')

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title (title)
        self.chapter_body(name)

    def chapter_image(self,num,title,name):
        self.add_page()
        self.chapter_title(title)
        self.image(name,0,90,210,190)

    def about_me(self,num, title, name):
        self.chapter_title(title)

        self.set_draw_color(40, 116, 166)
        with open(name, 'rb') as fh:
            txt = fh.read().decode('utf-8')
        self.set_font('delo',"", size=12)
        self.set_text_color(244, 246, 247)#253, 254, 254
        self.set_fill_color(25, 118, 210 )

        self.multi_cell(135, 5, txt,1,'J',True)
        self.ln(1)

    def about_me_picture(self,num, title, name):
        self.image(profile_image,150, 74, 50, 80)
        #self.multi_cell(0, 8, txt, 1, 'L', True)
        self.ln()

    def professional_skills(self,num, title, name):
        self.chapter_title(title)
        self.ln(65)
        self.image(skill_image,1, 170, 210, 70)
        self.ln()

    def contact(self,num, title, name):
        self.chapter_title(title)
        with open(name, 'rb') as fh:
            txt = fh.read().decode('utf-8')
        self.set_font('delo',"", size=11)
        self.set_text_color(244, 246, 247)
        self.set_fill_color(25, 118, 210 )
        self.multi_cell(0, 8, txt,1,'L',True)
        self.ln()

    def mutlicell_work1(self,num, title, name):
        self.chapter_title(title)
        with open(name, 'rb') as fh:
            txt = fh.read().decode('utf-8')
        self.set_fill_color(13, 71, 161)
        self.set_text_color(255, 255, 255)
        self.set_font('delo',"", size=12)
        self.multi_cell(0, 5, txt,1,'C',True)
        self.ln()

    def mutlicell_work2(self,num, title, name):
        with open(name, 'rb') as fh:
            txt = fh.read().decode('utf-8')
        self.set_fill_color(21, 101, 192)
        self.set_text_color(255, 255, 255)
        self.set_font('delo',"", size=12)
        self.multi_cell(0, 5, txt,1,'C',True)
        self.ln()

    def mutlicell_work3(self,num, title, name):
        with open(name, 'rb') as fh:
            txt = fh.read().decode('utf-8')
        self.set_fill_color(25, 118, 210 )
        self.set_text_color(255, 255, 255)
        self.set_font('delo',"", size=12)
        self.multi_cell(0, 5, txt,1,'C',True)
        self.ln()

    def mutlicell_work4(self,num, title, name):
        with open(name, 'rb') as fh:
            txt = fh.read().decode('utf-8')
        self.set_fill_color(30, 136, 229)
        self.set_text_color(255, 255, 255)
        self.set_font('delo',"", size=12)
        self.multi_cell(0, 5, txt,1,'C',True)
        self.ln()

    def mutlicell_work5(self,num, title, name):
        with open(name, 'rb') as fh:
            txt = fh.read().decode('utf-8')
        self.set_fill_color(33, 150, 243)
        self.set_text_color(255, 255, 255)
        self.set_font('delo',"", size=12)
        self.multi_cell(0, 4, txt,1,'C',True)
        self.ln()

    def mutlicell_work6(self,num, title, name):
        with open(name, 'rb') as fh:
            txt = fh.read().decode('utf-8')
        self.set_fill_color(66, 165, 245)
        self.set_text_color(255, 255, 255)
        self.set_font('delo',"", size=12)
        self.set_text_color(253, 254, 254 )
        self.multi_cell(0, 4, txt,1,'C',True)

    def mutlicell_school1(self,num, title, name):
        self.chapter_title(title)
        with open(name, 'rb') as fh:
            txt = fh.read().decode('utf-8')
        self.set_font('delo',"", size=13)
        self.set_text_color(244, 246, 247)
        self.set_fill_color(33, 97, 140 )
        self.multi_cell(0, 8, txt,1,'L',True)
        self.ln()

    def mutlicell_school2(self,num, title, name):
        with open(name, 'rb') as fh:
            txt = fh.read().decode('utf-8')
        self.set_font('delo',"", size=13)
        self.set_text_color(244, 246, 247)
        self.set_fill_color(40, 116, 166)
        self.multi_cell(0, 8, txt,1,'L',True)
        self.ln()

    def mutlicell_school3(self,num, title, name):
        self.chapter_title(title)
        with open(name, 'rb') as fh:
            txt = fh.read().decode('utf-8')
        self.set_font('delo',"", size=13)
        self.set_text_color(244, 246, 247)
        self.set_fill_color(46, 134, 193)
        self.multi_cell(0, 8, txt,1,'L',True)
        self.ln()


pdf = PDF()
