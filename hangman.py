from tkinter import *
from PIL import Image, ImageTk
import random


class HangMan:
    def __init__(self, win):
        self.win = win
        self.word = ""
        self.score = 0

        self.mainWindowStuff()
    def mainWindowStuff(self):
        self.win.title("HangMan Game")
        self.win.wm_state('zoomed')
        self.win.config(bg = "Ghost White")


        title_label = Label(self.win, text = "The HangMan Game", font = (None, 40), fg = "Black", bg = "ghost white")
        title_label.place(x = 400, y = 10)

        self.generateWord()
        self.keyboard()

    def keyboard(self):
        keyFrame = Frame(self.win, width = 1350, height = 300, bg = 'Ghost White', relief = RIDGE, bd = 10)
        keyFrame.place(x = 50, y = 500)
        #
        # row = 1
        # column = 1
        #
        # for i in range(65, 91):   # To get all the alphabets from a-z using ASCII
        #     char = chr(i)
        #     key_button = Button(keyFrame, text = char, font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed('A'), command = lambda: self.keyPressed(key_button["text"]))
        #     key_button.grid(row = row, column = column, sticky = W)
        #
        #     if(column==18):
        #         row += 1
        #         column = 0
        #     column += 1

        a = Button(keyFrame, text = 'A', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(a))
        a.grid(row = 1, column = 1, sticky = W)
        b = Button(keyFrame, text = 'B', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(b))
        b.grid(row = 1, column = 2, sticky = W)
        c = Button(keyFrame, text = 'C', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(c))
        c.grid(row = 1, column = 3, sticky = W)
        d = Button(keyFrame, text = 'D', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(d))
        d.grid(row = 1, column = 4, sticky = W)
        e = Button(keyFrame, text = 'E', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(e))
        e.grid(row = 1, column = 5, sticky = W)
        f = Button(keyFrame, text = 'F', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(f))
        f.grid(row = 1, column = 6, sticky = W)
        g = Button(keyFrame, text = 'G', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(g))
        g.grid(row = 1, column = 7, sticky = W)
        h = Button(keyFrame, text = 'H', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(h))
        h.grid(row = 1, column = 8, sticky = W)
        i = Button(keyFrame, text = 'I', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(i))
        i.grid(row = 1, column = 9, sticky = W)
        j = Button(keyFrame, text = 'J', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(j))
        j.grid(row = 1, column = 10, sticky = W)
        k = Button(keyFrame, text = 'K', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(k))
        k.grid(row = 1, column = 11, sticky = W)
        l = Button(keyFrame, text = 'L', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(l))
        l.grid(row = 1, column = 12, sticky = W)
        m = Button(keyFrame, text = 'M', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(m))
        m.grid(row = 1, column = 13, sticky = W)
        n = Button(keyFrame, text = 'N', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(n))
        n.grid(row = 1, column = 14, sticky = W)
        o = Button(keyFrame, text = 'O', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(o))
        o.grid(row = 1, column = 15, sticky = W)
        p = Button(keyFrame, text = 'P', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(p))
        p.grid(row = 1, column = 16, sticky = W)
        q = Button(keyFrame, text = 'Q', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(q))
        q.grid(row = 1, column = 17, sticky = W)
        r = Button(keyFrame, text = 'R', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(r))
        r.grid(row = 1, column = 18, sticky = W)
        s = Button(keyFrame, text = 'S', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(s))
        s.grid(row = 2, column = 1, sticky = W)
        t = Button(keyFrame, text = 'T', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(t))
        t.grid(row = 2, column = 2, sticky = W)
        u = Button(keyFrame, text = 'U', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(u))
        u.grid(row = 2, column = 3, sticky = W)
        v = Button(keyFrame, text = 'V', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(v))
        v.grid(row = 2, column = 4, sticky = W)
        w = Button(keyFrame, text = 'W', font = (None, 25), padx = 5, pady = 5, command = lambda: self.keyPressed(w))
        w.grid(row = 2, column = 5, sticky = W)
        x = Button(keyFrame, text = 'X', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(x))
        x.grid(row = 2, column = 6, sticky = W)
        y = Button(keyFrame, text = 'Y', font = (None, 25), padx = 12, pady = 5, command = lambda: self.keyPressed(y))
        y.grid(row = 2, column = 7, sticky = W)
        z = Button(keyFrame, text = 'Z', font = (None, 25), padx = 10, pady = 5, command = lambda: self.keyPressed(z))
        z.grid(row = 2, column = 8, sticky = W)


    def keyPressed(self, button):
        #button['state'] = DISABLED
        #print(button["text"])
        txt = button["text"]
        indices = []

        for i in range(len(self.formattedWord)):
            if(self.formattedWord[i] == txt):
                indices.append(i)

        j = list(self.hidden_word)
        for i in indices:
            j[i] = txt

        new_str = ""
        for i in j:
            new_str += i

        self.hidden_word = new_str

        if(len(indices) == 0):
            self.wrongMove()
        else:
            self.score += 5

        self.updateWord(True)



    def wrongMove(self):
        pass



    def generateWord(self):

        wordsList = ['integral', 'earthworm', 'swimsuit', 'terrace', 'alteration', 'verification', 'assault', 'parsley', 'recorder', 'bestseller', 'shelter', 'vulture', 'speedboat', 'nanoparticle', 'collection', 'amazement', 'validity', 'boatload', 'armoire', 'training', 'gingerbread', 'currency', 'marketplace', 'composition', 'interferometer', 'burglar', 'podcast', 'footwear', 'homework', 'decision', 'catalyst', 'doughnut', 'iceberg', 'eyeliner', 'footage', 'vinegar', 'sidewalk', 'opposition', 'editing', 'trustee', 'upstairs', 'stinger', 'grandfather', 'professor', 'parenting', 'jalapeño', 'construction', 'director', 'hypothesis', 'briefing', 'hometown', 'fingerling', 'gateway', 'opportunity', 'trading', 'publisher', 'sauerkraut', 'puritan', 'microphone', 'porthole', 'kumquat', 'aircraft', 'discharge', 'disclosure', 'seashore', 'browser', 'financing', 'imbalance', 'sustenance', 'familiar', 'incubation', 'millennium', 'grenade', 'titanium', 'marriage', 'laundry', 'gasoline', 'endothelium', 'manatee', 'prostanoid', 'clapboard', 'marmalade', 'trouble', 'refectory', 'contour', 'caliber', 'waterfront', 'jewelry', 'business', 'neighbour', 'embarrassment', 'midline', 'shirtdress', 'semester', 'handball', 'strawberry', 'selling', 'hamburger', 'furnace', 'quicksand']

        randomNum = random.randint(0, len(wordsList))

        self.word = wordsList[randomNum].upper()
        self.formattedWord = ""
        self.hidden_word = ""

        for i in self.word:
            self.formattedWord += i + " "
            self.hidden_word += "_" + " "



        self.updateWord(False)

    def updateWord(self, deletePrevious):
        wordFrame = Frame(self.win, height = 10, width = 10, bg = "Ghost White", relief = RIDGE, bd = 10)
        wordLabel = Label(wordFrame, text = self.hidden_word, font = (None, 30))
        wordFrame.place(x = 550, y = 100)
        wordLabel.pack()

        print(self.formattedWord)





if __name__ == "__main__":
    win = Tk()
    runObject = HangMan(win)
    win.mainloop()
