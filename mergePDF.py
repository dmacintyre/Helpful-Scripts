'''
Created on Apr 20, 2016

@author: Don MacIntyre
'''

from tkinter import Tk, Button, filedialog, Listbox
from PyPDF2 import PdfFileMerger, PdfFileReader

class mergeGUI():
    def __init__(self, master):
        self.master = master
        master.title("Merge PDF Files")
        self.filesSelected = []

        self.lstbox = Listbox(master)
        self.button_browse = Button(master, text="Select File", command=self.browse_file)
        self.button_merge = Button(master, text="Merge Files", command=self.merge_files)
        self.button_quit = Button(master, text="Quit", command=self.quit)
        self.lstbox.pack()
        self.button_browse.pack()
        self.button_merge.pack()
        self.button_quit.pack()

    def browse_file(self):
        self.filename = filedialog.askopenfilename(filetypes=[("pdffiles","*.pdf")],multiple=True)
        for i in range(len(self.filename)):
            self.lstbox.insert(i,self.filename[i])
        self.filesSelected.append(self.filename)

    def merge_files(self):
        if len(self.filesSelected) < 2:
            print("Error need at least 2 files to merge files")
        else:    
            merger = PdfFileMerger()
            for fname in self.filesSelected:
                merger.append(PdfFileReader(open(fname, 'rb')))
            
            self.filename = filedialog.asksaveasfilename(title="Enter filename", filetypes=[("pdffiles","*.pdf")])
            merger.write(self.filename + ".pdf")
        
    def quit(self):
        self.master.destroy()

def main():

    app = Tk()
    app.geometry('600x400+200+100')
    mergeGUI(app)
    app.mainloop()

if __name__ == '__main__':
    main()
