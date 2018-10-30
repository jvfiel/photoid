from Tkinter import *

#https://medium.com/dreamcatcher-its-blog/making-an-stand-alone-executable-from-a-python-script-using-pyinstaller-d1df9170e263

class Window:

    def __init__(self, master):

        self.image = ""
        b = Button(master, text='Browse', command=self.browsefile)
        b.pack()

        b = Button(master, text="2x2 (5r)", command=self.fiveR)
        b.pack()

        b = Button(master, text="2x2 (5r) + Free 1x1", command=self.fiveR_free)
        b.pack()

        b = Button(master, text="1x1 (4r)", command=self.oneByOne)
        b.pack()

        b = Button(master, text="1x1 (5r) + Free", command=self.oneByOne_free)
        b.pack()

        b = Button(master, text="Passport (4r)", command=self.passport)
        b.pack()

        b = Button(master, text="Passport (4r) + Free", command=self.passport_free)
        b.pack()

        b = Button(master, text="Mix 2x2 1x1 (5r)", command=self.mix_twoBytwo_oneByone)
        b.pack()

        b = Button(master, text="Mix Passport 1x1 (5r)", command=self.mix_passport_oneByone)
        b.pack()


    def fiveR(self):
        image = self.image
        # print "click!", self.image
        from fpdf import FPDF
        pdf = FPDF()
        # imagelist is the list with all image filenames
        # for image in imagelist:
        # image = "/home/jvfiel/projects/papa/1533911_10202416925357949_2518432_n.jpg"

        from reportlab.pdfgen import canvas
        from reportlab.lib.units import mm
        from reportlab.lib.units import inch
        # c = canvas.Canvas("hello.pdf", pagesize=(297 * mm, 420 * mm))
        c = canvas.Canvas("fiveR.pdf", pagesize=(5 * inch, 7 * inch))
        # or (420 * mm, 297 * mm) if you want it in portrait format
        # values for inch: 11.69 * inch , 16.53 * inch

        # the following would create an empty page

        size_inch = (2 * inch)+(0.125*inch)
        c.drawImage(image, 0, 0,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch, 0,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, 0, size_inch,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch,size_inch,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, 0, size_inch+size_inch, size_inch/2, size_inch/2)  # Who needs consistency?
        c.drawImage(image, 0+size_inch/2, size_inch+size_inch, size_inch/2, size_inch/2)  # Who needs consistency?

        c.showPage()
        c.save()

    def fiveR_free(self):
        image = self.image
        # print "click!"
        from fpdf import FPDF
        pdf = FPDF()
        # imagelist is the list with all image filenames
        # for image in imagelist:
        # image = "/home/jvfiel/projects/papa/1533911_10202416925357949_2518432_n.jpg"

        from reportlab.pdfgen import canvas
        from reportlab.lib.units import mm
        from reportlab.lib.units import inch
        # c = canvas.Canvas("hello.pdf", pagesize=(297 * mm, 420 * mm))
        c = canvas.Canvas("fiveR_free.pdf", pagesize=(5 * inch, 7 * inch))
        # or (420 * mm, 297 * mm) if you want it in portrait format
        # values for inch: 11.69 * inch , 16.53 * inch

        # the following would create an empty page

        size_inch = (2 * inch)+(0.125*inch)
        c.drawImage(image, 0, 0,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch, 0,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, 0, size_inch,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch,size_inch,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, 0, size_inch+size_inch, size_inch/2, size_inch/2)  # Who needs consistency?
        c.drawImage(image, 0+size_inch/2, size_inch+size_inch, size_inch/2, size_inch/2)  # Who needs consistency?

        c.showPage()
        c.save()


    def oneByOne(self):
        image = self.image
        # print "click!"
        from fpdf import FPDF
        pdf = FPDF()
        # imagelist is the list with all image filenames
        # for image in imagelist:
        # image = "/home/jvfiel/projects/papa/1533911_10202416925357949_2518432_n.jpg"

        from reportlab.pdfgen import canvas
        from reportlab.lib.units import mm
        from reportlab.lib.units import inch
        # c = canvas.Canvas("hello.pdf", pagesize=(297 * mm, 420 * mm))
        c = canvas.Canvas("oneByOne.pdf", pagesize=(4 * inch, 6 * inch))
        # or (420 * mm, 297 * mm) if you want it in portrait format
        # values for inch: 11.69 * inch , 16.53 * inch

        # the following would create an empty page

        size_inch = (1 * inch)+(0.125*inch)
        c.drawImage(image, 0, 0,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch, 0,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch+size_inch, 0,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, 0, size_inch,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch,size_inch,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch+size_inch,size_inch,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, 0, size_inch+size_inch, size_inch, size_inch)  # 3rd row
        c.drawImage(image, size_inch, size_inch+size_inch, size_inch, size_inch)  # Who needs consistency?
        # c.drawImage(image, 0, size_inch+size_inch, size_inch/2, size_inch/2)  # Who needs consistency?
        # c.drawImage(image, 0+size_inch/2, size_inch+size_inch, size_inch/2, size_inch/2)  # Who needs consistency?

        c.showPage()
        c.save()

    def oneByOne_free(self):
        image = self.image
        # print "click!"
        from fpdf import FPDF
        pdf = FPDF()
        # imagelist is the list with all image filenames
        # for image in imagelist:
        # image = "/home/jvfiel/projects/papa/1533911_10202416925357949_2518432_n.jpg"

        from reportlab.pdfgen import canvas
        from reportlab.lib.units import mm
        from reportlab.lib.units import inch
        # c = canvas.Canvas("hello.pdf", pagesize=(297 * mm, 420 * mm))
        c = canvas.Canvas("oneByOne_free.pdf", pagesize=(5 * inch, 7 * inch))
        # or (420 * mm, 297 * mm) if you want it in portrait format
        # values for inch: 11.69 * inch , 16.53 * inch

        # the following would create an empty page

        size_inch = (1 * inch)+(0.125*inch)
        size_inch_free = (2 * inch) + (0.125 * inch)
        c.drawImage(image, 0, 0,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch, 0,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch+size_inch, 0,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, 0, size_inch,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch,size_inch,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch+size_inch,size_inch,size_inch,size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch+size_inch, size_inch+size_inch, size_inch, size_inch)  # 3rd row
        c.drawImage(image, size_inch+size_inch, size_inch+size_inch+size_inch, size_inch, size_inch)  # Who needs consistency?

        c.drawImage(image, 0, size_inch + size_inch, size_inch_free, size_inch_free)  # 2x2
        c.drawImage(image, 0, size_inch + size_inch+size_inch_free, size_inch_free, size_inch_free)  # 2x2

        # c.drawImage(image, 0, size_inch+size_inch, size_inch/2, size_inch/2)  # Who needs consistency?
        # c.drawImage(image, 0+size_inch/2, size_inch+size_inch, size_inch/2, size_inch/2)  # Who needs consistency?

        c.showPage()
        c.save()


    def passport(self):
        image = self.image
        # print "click!"
        from fpdf import FPDF
        pdf = FPDF()
        # imagelist is the list with all image filenames
        # for image in imagelist:
        # image = "/home/jvfiel/projects/papa/1533911_10202416925357949_2518432_n.jpg"

        from reportlab.pdfgen import canvas
        from reportlab.lib.units import mm
        from reportlab.lib.units import inch
        # c = canvas.Canvas("hello.pdf", pagesize=(297 * mm, 420 * mm))
        c = canvas.Canvas("passport.pdf", pagesize=(4 * inch, 6 * inch))
        # or (420 * mm, 297 * mm) if you want it in portrait format
        # values for inch: 11.69 * inch , 16.53 * inch

        # the following would create an empty page

        size_inch_w = (1.37 * inch)+(0.125*inch)
        size_inch_h = (1.77 * inch)+(0.125*inch)
        size_inch_free = (1 * inch)
        c.drawImage(image, 0, 0,size_inch_w,size_inch_h)  # Who needs consistency?
        c.drawImage(image, size_inch_w, 0,size_inch_w,size_inch_h)  # Who needs consistency?
        c.drawImage(image, 0, size_inch_h,size_inch_w,size_inch_h)  # Who needs consistency?
        c.drawImage(image, size_inch_w,size_inch_h,size_inch_w,size_inch_h)  # Who needs consistency?
        # c.drawImage(image, 0,size_inch_h+size_inch_free*2,size_inch_free,size_inch_free)  # Who needs consistency?
        # c.drawImage(image, size_inch_free,size_inch_h+size_inch_free*2,size_inch_free,size_inch_free)  # Who needs consistency?
        # c.drawImage(image, 0, size_inch_h + size_inch_free * 3, size_inch_free, size_inch_free)  # Who needs consistency?
        # c.drawImage(image, size_inch_free, size_inch_h + size_inch_free * 3, size_inch_free,
        #             size_inch_free)  # Who needs consistency?
        c.showPage()
        c.save()


    def passport_free(self):
        image = self.image
        # print "click!"
        from fpdf import FPDF
        pdf = FPDF()
        # imagelist is the list with all image filenames
        # for image in imagelist:
        # image = "/home/jvfiel/projects/papa/1533911_10202416925357949_2518432_n.jpg"

        from reportlab.pdfgen import canvas
        from reportlab.lib.units import mm
        from reportlab.lib.units import inch
        # c = canvas.Canvas("hello.pdf", pagesize=(297 * mm, 420 * mm))
        c = canvas.Canvas("passport_free.pdf", pagesize=(4 * inch, 6 * inch))
        # or (420 * mm, 297 * mm) if you want it in portrait format
        # values for inch: 11.69 * inch , 16.53 * inch

        # the following would create an empty page

        size_inch_w = (1.37 * inch)+(0.125*inch)
        size_inch_h = (1.77 * inch)+(0.125*inch)
        size_inch_free = (1 * inch)
        c.drawImage(image, 0, 0,size_inch_w,size_inch_h)  # Who needs consistency?
        c.drawImage(image, size_inch_w, 0,size_inch_w,size_inch_h)  # Who needs consistency?
        c.drawImage(image, 0, size_inch_h,size_inch_w,size_inch_h)  # Who needs consistency?
        c.drawImage(image, size_inch_w,size_inch_h,size_inch_w,size_inch_h)  # Who needs consistency?
        c.drawImage(image, 0,size_inch_h+size_inch_free*2,size_inch_free,size_inch_free)  # Who needs consistency?
        c.drawImage(image, size_inch_free,size_inch_h+size_inch_free*2,size_inch_free,size_inch_free)  # Who needs consistency?
        c.drawImage(image, 0, size_inch_h + size_inch_free * 3, size_inch_free, size_inch_free)  # Who needs consistency?
        c.drawImage(image, size_inch_free, size_inch_h + size_inch_free * 3, size_inch_free,
                    size_inch_free)  # Who needs consistency?
        c.showPage()
        c.save()

    def mix_twoBytwo_oneByone(self):
        image = self.image
        # print "click!"
        from fpdf import FPDF
        pdf = FPDF()
        # imagelist is the list with all image filenames
        # for image in imagelist:
        # image = "/home/jvfiel/projects/papa/1533911_10202416925357949_2518432_n.jpg"

        from reportlab.pdfgen import canvas
        from reportlab.lib.units import mm
        from reportlab.lib.units import inch
        # c = canvas.Canvas("hello.pdf", pagesize=(297 * mm, 420 * mm))
        c = canvas.Canvas("mix_twoBytwo_oneByone.pdf", pagesize=(5 * inch, 7 * inch))
        # or (420 * mm, 297 * mm) if you want it in portrait format
        # values for inch: 11.69 * inch , 16.53 * inch

        # the following would create an empty page

        size_inch = (1 * inch) + (0.125 * inch)
        size_inch_free = (2 * inch) + (0.125 * inch)
        c.drawImage(image, 0, 0, size_inch, size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch, 0, size_inch, size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch + size_inch, 0, size_inch, size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch + size_inch + size_inch, 0, size_inch, size_inch)  # Who needs consistency?

        c.drawImage(image, 0, size_inch, size_inch, size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch, size_inch, size_inch, size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch + size_inch, size_inch, size_inch, size_inch)  # Who needs consistency?
        c.drawImage(image, size_inch + size_inch + size_inch, size_inch, size_inch, size_inch)  # Who needs consistency?


        # c.drawImage(image, size_inch + size_inch, size_inch + size_inch, size_inch, size_inch)  # 3rd row
        # c.drawImage(image, size_inch + size_inch, size_inch + size_inch + size_inch, size_inch,
        #             size_inch)  # Who needs consistency?

        c.drawImage(image, 0, size_inch + size_inch, size_inch_free, size_inch_free)  # 2x2
        c.drawImage(image, size_inch_free, size_inch + size_inch, size_inch_free, size_inch_free)  # 2x2
        c.drawImage(image, 0, size_inch + size_inch + size_inch_free, size_inch_free, size_inch_free)  # 2x2
        c.drawImage(image, size_inch_free, size_inch + size_inch + size_inch_free, size_inch_free, size_inch_free)  # 2x2

        # c.drawImage(image, 0, size_inch+size_inch, size_inch/2, size_inch/2)  # Who needs consistency?
        # c.drawImage(image, 0+size_inch/2, size_inch+size_inch, size_inch/2, size_inch/2)  # Who needs consistency?

        c.showPage()
        c.save()

    def mix_passport_oneByone(self):
        image = self.image
        # print "click!"
        from fpdf import FPDF
        pdf = FPDF()
        # imagelist is the list with all image filenames
        # for image in imagelist:
        # image = "/home/jvfiel/projects/papa/1533911_10202416925357949_2518432_n.jpg"

        from reportlab.pdfgen import canvas
        from reportlab.lib.units import mm
        from reportlab.lib.units import inch
        # c = canvas.Canvas("hello.pdf", pagesize=(297 * mm, 420 * mm))
        c = canvas.Canvas("mix_passport_oneByone.pdf", pagesize=(5 * inch, 7 * inch))
        # or (420 * mm, 297 * mm) if you want it in portrait format
        # values for inch: 11.69 * inch , 16.53 * inch

        # the following would create an empty page

        size_inch_w = (1.37 * inch)+(0.125*inch)
        size_inch_h = (1.77 * inch)+(0.125*inch)
        size_inch_free = (1 * inch)
        c.drawImage(image, 0, 0,size_inch_w,size_inch_h)  # Who needs consistency?
        c.drawImage(image, size_inch_w, 0,size_inch_w,size_inch_h)  # Who needs consistency?
        c.drawImage(image, size_inch_w+size_inch_w, 0,size_inch_w,size_inch_h)  # Who needs consistency?


        c.drawImage(image, 0, size_inch_h,size_inch_w,size_inch_h)  # Who needs consistency?
        c.drawImage(image, size_inch_w,size_inch_h,size_inch_w,size_inch_h)  # Who needs consistency?


        c.drawImage(image, 0,size_inch_h+size_inch_free*2,size_inch_free,size_inch_free)  # Who needs consistency?
        c.drawImage(image, size_inch_free,size_inch_h+size_inch_free*2,size_inch_free,size_inch_free)  # Who needs consistency?
        c.drawImage(image, size_inch_free * 2,size_inch_h+size_inch_free*2,size_inch_free,size_inch_free)  # Who needs consistency?
        c.drawImage(image, size_inch_free * 3,size_inch_h+size_inch_free*2,size_inch_free,size_inch_free)  # Who needs consistency?

        c.drawImage(image, 0, size_inch_h + size_inch_free * 3, size_inch_free, size_inch_free)  # Who needs consistency?
        c.drawImage(image, size_inch_free, size_inch_h + size_inch_free * 3, size_inch_free,
                    size_inch_free)  # Who needs consistency?
        c.drawImage(image, size_inch_free *2, size_inch_h + size_inch_free * 3, size_inch_free,
                    size_inch_free)  # Who needs consistency?
        c.drawImage(image, size_inch_free * 3, size_inch_h + size_inch_free * 3, size_inch_free,
                    size_inch_free)  # Who needs consistency?

        c.showPage()
        c.save()


    def browsefile(self):
        from tkFileDialog import askopenfilename

        # Tk().withdraw()
        self.image = askopenfilename()
        # print self.image


def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


root = Tk()
window=Window(root)
center(root)
root.title("Cyberbee Photo")
root.geometry("300x250")
root.mainloop()
