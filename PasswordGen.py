'''
Created on Jul 07, 2015

@author: Donald MacIntyre
'''
from tkinter import Tk, Label, Checkbutton, Button, W, E, IntVar, StringVar, Scale

import random, string
        
class pwordGUI():
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")
        self.lbl1 = Label(master, text="Include:").grid(row=0, sticky=W)
        self.incLower = IntVar()
        self.incLower.set(1)        
        self.chk1 = Checkbutton(master, text="lower case", variable=self.incLower).grid(row=1, sticky=W)
        self.incUpper = IntVar()
        self.incUpper.set(1)
        self.chk2 = Checkbutton(master, text="UPPER CASE", variable=self.incUpper).grid(row=2, sticky=W)
        self.incNumeric = IntVar()
        self.incNumeric.set(1)
        self.chk3 = Checkbutton(master, text="numeric", variable=self.incNumeric).grid(row=3, sticky=W)
        self.incPunc = IntVar()
        self.chk4 = Checkbutton(master, text="punctuation", variable=self.incPunc).grid(row=4, sticky=W)
        self.b1 = Button(master, text="Generate password", width=20, command=self.genPwd).grid(row=5, sticky=W)
        self.b2 = Button(master, text="Quit", width=20, command=self.exitApp).grid(row=5, column=1, sticky=W)
        self.label_text = StringVar()
        self.lbl2 = Label(master, textvariable=self.label_text).grid(row=6, column=0, columnspan=2, sticky=W + E)
        self.label_text.set("")

        self.numDigits = IntVar()
        self.sc1 = Scale(master, from_=6, to=40, variable=self.numDigits).grid(row=0, rowspan=5, column=1, sticky=E)
        
    def genPwd(self):
        if not (self.incLower.get() or self.incUpper.get() or self.incNumeric.get() or self.incPunc.get()):
            self.label_text.set("Select at least one character type")
        else:
            password = ''
            if self.incLower.get():
                password += string.ascii_lowercase
            if self.incUpper.get():
                password += string.ascii_uppercase
            if self.incNumeric.get():
                password += string.digits
            if self.incPunc.get():
                password += string.punctuation
        
            myrg = random.SystemRandom()
            # Get password and make sure it contains at least one of each desired character type
            goodPwd = False
            while not goodPwd:
                pword = ''.join(myrg.choice(password) for i in range(self.numDigits.get()))
                # Now need to assume password is good and then set it to bad if any test fails
                goodPwd = True
                if self.incLower.get():
                    goodPwd = self.contains_n(string.ascii_lowercase, pword)
                if self.incUpper.get() and goodPwd:  # if password was bad for previous test want to leave it bad
                    goodPwd = self.contains_n(string.ascii_uppercase, pword)
                if self.incNumeric.get() and goodPwd:  # if password was bad for previous test want to leave it bad
                    goodPwd = self.contains_n(string.digits, pword)
                if self.incPunc.get() and goodPwd:  # if password was bad for previous test want to leave it bad
                    goodPwd = self.contains_n(string.punctuation, pword)
            self.label_text.set(pword)
            self.master.clipboard_clear()
            self.master.clipboard_append(pword)

    def contains_n(self, search, password):
        for i in password:
            for j in search:
                if j == i :
                    return True
        return False
    
    def exitApp(self):
        self.master.clipboard_clear()
        # It appears the clipboard doesn't actually clear until you write something new to it.
        # So write a blank line.
        self.master.clipboard_append('')
        self.master.quit()
        
def main():
    app = Tk()
    app.geometry('300x200+200+100')
    pwordGUI(app)
    app.mainloop()
    
if __name__ == '__main__':
    main()
