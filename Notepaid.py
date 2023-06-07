import string
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import  webbrowser as web


def update(data, l):
    l.delete(0, END)

    for item in data:
        l.insert(END, item)


def fillout(e):
    my_entry1.delete(0, END)
    my_entry1.insert(0, l1.get(ACTIVE))


def check(e):
    typed = my_entry1.get()
    if typed == ' ':
        data = list_fonts
    else:
        data = []
        for item in list_fonts:
            if typed.lower() in item.lower():
                data.append(item)
    update(data, l1)


def fillout2(e):
    my_entry2.delete(0, END)
    my_entry2.insert(0, l2.get(ACTIVE))


def check2(e):
    typed = my_entry2.get()
    if typed == ' ':
        data = Style
    else:
        data = []
        for item in Style:
            if typed.lower() in item.lower():
                data.append(item)
    update(data, l2)


def fillout3(e):
    my_entry3.delete(0, END)
    my_entry3.insert(0, l3.get(ACTIVE))


def check3(e):
    typed = my_entry3.get()
    if typed == ' ':
        data = size
    else:
        data = []
        for item in size:
            if typed.lower() in item.lower():
                data.append(item)
    update(data, l3)


def NEW_FILE(e=""):
    global file
    root.title("Untitled - Notepad")
    file = NONE
    TextArea.delete(1.0, END)


def OPEN_FILE(e=""):
    global file
    if e:
        pass
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def SAVE_FILE(e=""):
    global file
    if e:
        pass
    if file == NONE:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            NONE
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "- Notepad")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def EXIT_FILE(e=""):
    exit_function()


def CUT(event=""):
    global Selected
    if event:
        if root.clipboard_get() == "":
            pass
        else:
            Selected = root.clipboard_get()
    else:
        if TextArea.selection_get():
            if TextArea.selection_get() == " ":
                pass
            else:
                Selected = TextArea.selection_get()
                TextArea.delete("sel.first", "sel.last")


def PASTE(event=""):
    global Selected
    if event:
        Selected = root.clipboard_get()
    else:
        if Selected:
            position = TextArea.index(INSERT)
            TextArea.insert(position, Selected)


def COPY(event=""):
    global Selected
    if event:
        Selected = root.clipboard_get()
    else:
        if TextArea.selection_get():
            Selected = TextArea.selection_get()
            root.clipboard_clear()
            root.clipboard_append(Selected)


def FIND(e=""):
    new_window = Toplevel(root)
    new_window.geometry("200x200")
    new_window.title("FIND")
    new_window.config(bg='#F0F0F0')
    Word = StringVar()
    label1 = Label(new_window, text="Entry The Word")
    label1.pack()
    find_word = Entry(new_window, textvariable=Word)
    find_word.pack()

    def GO_1():
        TEXT_1 = str(TextArea.get(1.0, END)).lower()
        a = TEXT_1.count(str(find_word.get()).lower())
        if a == 0:
            showinfo("NOT FOUND", f"{str(find_word.get())} is not present")
        else:
            COUNT = Entry(new_window)
            COUNT.insert(0, a)
            label2 = Label(new_window, text="Number of time the Word Found")
            label2.pack()
            COUNT.pack()

    button_1 = Button(new_window, text="Find", command=GO_1, padx=10)
    button_1.pack(pady=10)


def Replace(e=""):
    new_window = Toplevel(root)
    new_window.geometry("400x250")
    new_window.title("FIND & REPLACE")
    new_window.config(bg='#F0F0F0')
    l1 = Label(new_window, text="Entry The Word to Find")
    l1.grid(row=1, column=1, padx=5)
    Word = StringVar()
    find_word = Entry(new_window, textvariable=Word)
    find_word.grid(row=1, column=2)
    a = 1
    l_3 = Label(new_window, text="Entry The Word to Replace")
    l_3.grid(row=2, column=1, padx=5)

    Word_1 = StringVar()
    find_word1 = Entry(new_window, textvariable=Word_1)
    find_word1.grid(row=2, column=2)
    COUNT = Entry(new_window)

    def GO_1():
        TEXT_1 = str(TextArea.get(1.0, END)).lower()
        a = TEXT_1.count(str(find_word.get()).lower())
        COUNT.insert(0, a)
        COUNT.grid(row=3, column=2)
        l2 = Label(new_window, text="No of Count")
        l2.grid(row=3, column=1)
        a = int(str(COUNT.get()))

    button_1 = Button(new_window, text="FIND ", command=GO_1)
    button_1.grid(row=1, column=3, padx=10, pady=10)

    def GO_2():
        TEXT_1 = str(TextArea.get(1.0, END))
        b = int(COUNT.get())
        if b > a:
            showinfo("Limit ", "YOU ARE OVER THE RANGE")
        else:
            TEXT_1 = TEXT_1.replace(str(find_word.get()).lower(), str(find_word1.get()).lower(), b)
            TEXT_1 = TEXT_1.replace(str(find_word1.get()).lower(), str(find_word1.get()), b)
            TextArea.delete(1.0, END)
            TextArea.insert(1.0, TEXT_1)
            COUNT.delete(0, END)

    button_2 = Button(new_window, text="REPLACE", command=GO_2)
    button_2.grid(row=2, column=3, padx=10, pady=10)


def White_Mood():
    global theme_count
    if theme_count % 2 == 0:
        root.config(bg="white")
        TextArea.config(bg="white", fg="black")
    if theme_count % 2 != 0:
        root.config(bg="black")
        TextArea.config(bg="#282A36", fg="#43CA63")
    theme_count = theme_count + 1


def FONT():
    new_window = Toplevel(root)
    new_window.geometry("450x300")
    new_window.title("FONT")
    new_window.config(bg='#F0F0F0')
    global l1, l2, l3, my_entry1, my_entry2, my_entry3, list_fonts, Style, size
    label1 = Label(new_window, text="Fonts:")
    label1.grid(row=0, column=0, padx=10)

    label2 = Label(new_window, text="Font Style:")
    label2.grid(row=0, column=1, padx=10)

    label3 = Label(new_window, text="Size:")
    label3.grid(row=0, column=2, padx=10)

    my_entry1 = Entry(new_window)
    my_entry1.insert(0, "Consolas")
    my_entry1.grid(row=1, column=0, padx=10)
    l1 = Listbox(new_window)
    l1.grid(row=2, column=0)

    my_entry2 = Entry(new_window)
    my_entry2.insert(0, "Regular")
    my_entry2.grid(row=1, column=1)
    l2 = Listbox(new_window)
    l2.grid(row=2, column=1, padx=10)

    my_entry3 = Entry(new_window)
    my_entry3.insert(0, "11")
    my_entry3.grid(row=1, column=2)
    l3 = Listbox(new_window)
    l3.grid(row=2, column=2, padx=10)

    list_fonts = ['System', 'Terminal', 'Fixedsys', 'Modern', 'Roman', 'Script', 'Courier', 'MS Serif', 'MS Sans Serif',
                  'Small Fonts', 'Bell Gothic Std Black', 'Bell Gothic Std Light', 'Eccentric Std', 'Stencil Std',
                  'Tekton Pro', 'Tekton Pro Cond', 'Tekton Pro Ext', 'Trajan Pro', 'Rosewood Std Regular',
                  'Prestige Elite Std', 'Poplar Std', 'Orator Std', 'OCR A Std', 'Nueva Std Cond', 'Minion Pro SmBd',
                  'Minion Pro Med', 'Minion Pro Cond', 'Mesquite Std', 'Lithos Pro Regular', 'Kozuka Mincho Pro R',
                  '@Kozuka Mincho Pro R', 'Kozuka Mincho Pro M', '@Kozuka Mincho Pro M', 'Kozuka Mincho Pro L',
                  '@Kozuka Mincho Pro L', 'Kozuka Mincho Pro H', '@Kozuka Mincho Pro H', 'Kozuka Mincho Pro EL',
                  '@Kozuka Mincho Pro EL', 'Kozuka Mincho Pro B', '@Kozuka Mincho Pro B', 'Kozuka Gothic Pro R',
                  '@Kozuka Gothic Pro R', 'Kozuka Gothic Pro M', '@Kozuka Gothic Pro M', 'Kozuka Gothic Pro L',
                  '@Kozuka Gothic Pro L', 'Kozuka Gothic Pro H', '@Kozuka Gothic Pro H', 'Kozuka Gothic Pro EL',
                  '@Kozuka Gothic Pro EL', 'Kozuka Gothic Pro B', '@Kozuka Gothic Pro B', 'Hobo Std', 'Giddyup Std',
                  'Cooper Std Black', 'Charlemagne Std', 'Chaparral Pro', 'Brush Script Std', 'Blackoak Std',
                  'Birch Std', 'Adobe Garamond Pro', 'Adobe Garamond Pro Bold', 'Adobe Kaiti Std R',
                  '@Adobe Kaiti Std R', 'Adobe Heiti Std R', '@Adobe Heiti Std R', 'Adobe Fangsong Std R',
                  '@Adobe Fangsong Std R', 'Adobe Caslon Pro', 'Adobe Caslon Pro Bold', 'Adobe Arabic',
                  'Adobe Devanagari', 'Adobe Hebrew', 'Adobe Ming Std L', '@Adobe Ming Std L', 'Adobe Myungjo Std M',
                  '@Adobe Myungjo Std M', 'Adobe Song Std L', '@Adobe Song Std L', 'Kozuka Gothic Pr6N B',
                  '@Kozuka Gothic Pr6N B', 'Kozuka Gothic Pr6N EL', '@Kozuka Gothic Pr6N EL', 'Kozuka Gothic Pr6N H',
                  '@Kozuka Gothic Pr6N H', 'Kozuka Gothic Pr6N L', '@Kozuka Gothic Pr6N L', 'Kozuka Gothic Pr6N M',
                  '@Kozuka Gothic Pr6N M', 'Kozuka Gothic Pr6N R', '@Kozuka Gothic Pr6N R', 'Kozuka Mincho Pr6N B',
                  '@Kozuka Mincho Pr6N B', 'Kozuka Mincho Pr6N EL', '@Kozuka Mincho Pr6N EL', 'Kozuka Mincho Pr6N H',
                  '@Kozuka Mincho Pr6N H', 'Kozuka Mincho Pr6N L', '@Kozuka Mincho Pr6N L', 'Kozuka Mincho Pr6N M',
                  '@Kozuka Mincho Pr6N M', 'Kozuka Mincho Pr6N R', '@Kozuka Mincho Pr6N R', 'Letter Gothic Std',
                  'Minion Pro', 'Myriad Hebrew', 'Myriad Pro', 'Myriad Pro Cond', 'Myriad Pro Light',
                  'Rosewood Std Fill', 'Marlett', 'Arial', 'Arabic Transparent', 'Arial Baltic', 'Arial CE',
                  'Arial CYR', 'Arial Greek', 'Arial TUR', 'Batang', '@Batang', 'BatangChe', '@BatangChe', 'Gungsuh',
                  '@Gungsuh', 'GungsuhChe', '@GungsuhChe', 'Courier New', 'Courier New Baltic', 'Courier New CE',
                  'Courier New CYR', 'Courier New Greek', 'Courier New TUR', 'DaunPenh', 'DokChampa',
                  'Estrangelo Edessa', 'Euphemia', 'Gautami', 'Vani', 'Gulim', '@Gulim', 'GulimChe', '@GulimChe',
                  'Dotum', '@Dotum', 'DotumChe', '@DotumChe', 'Impact', 'Iskoola Pota', 'Kalinga', 'Kartika',
                  'Khmer UI', 'Lao UI', 'Latha', 'Lucida Console', 'Malgun Gothic', '@Malgun Gothic', 'Mangal',
                  'Meiryo', '@Meiryo', 'Meiryo UI', '@Meiryo UI', 'Microsoft Himalaya', 'Microsoft JhengHei',
                  '@Microsoft JhengHei', 'Microsoft YaHei', '@Microsoft YaHei', 'MingLiU', '@MingLiU', 'PMingLiU',
                  '@PMingLiU', 'MingLiU_HKSCS', '@MingLiU_HKSCS', 'MingLiU-ExtB', '@MingLiU-ExtB', 'PMingLiU-ExtB',
                  '@PMingLiU-ExtB', 'MingLiU_HKSCS-ExtB', '@MingLiU_HKSCS-ExtB', 'Mongolian Baiti', 'MS Gothic',
                  '@MS Gothic', 'MS PGothic', '@MS PGothic', 'MS UI Gothic', '@MS UI Gothic', 'MS Mincho', '@MS Mincho',
                  'MS PMincho', '@MS PMincho', 'MV Boli', 'Microsoft New Tai Lue', 'Nyala', 'Microsoft PhagsPa',
                  'Plantagenet Cherokee', 'Raavi', 'Segoe Script', 'Segoe UI', 'Segoe UI Semibold', 'Segoe UI Light',
                  'Segoe UI Symbol', 'Shruti', 'SimSun', '@SimSun', 'NSimSun', '@NSimSun', 'SimSun-ExtB',
                  '@SimSun-ExtB', 'Sylfaen', 'Microsoft Tai Le', 'Times New Roman', 'Times New Roman Baltic',
                  'Times New Roman CE', 'Times New Roman CYR', 'Times New Roman Greek', 'Times New Roman TUR', 'Tunga',
                  'Vrinda', 'Shonar Bangla', 'Microsoft Yi Baiti', 'Tahoma', 'Microsoft Sans Serif', 'Angsana New',
                  'Aparajita', 'Cordia New', 'Ebrima', 'Gisha', 'Kokila', 'Leelawadee', 'Microsoft Uighur', 'MoolBoran',
                  'Symbol', 'Utsaah', 'Vijaya', 'Wingdings', 'Andalus', 'Arabic Typesetting', 'Simplified Arabic',
                  'Simplified Arabic Fixed', 'Sakkal Majalla', 'Traditional Arabic', 'Aharoni', 'David', 'FrankRuehl',
                  'Levenim MT', 'Miriam', 'Miriam Fixed', 'Narkisim', 'Rod', 'FangSong', '@FangSong', 'SimHei',
                  '@SimHei', 'KaiTi', '@KaiTi', 'AngsanaUPC', 'Browallia New', 'BrowalliaUPC', 'CordiaUPC',
                  'DilleniaUPC', 'EucrosiaUPC', 'FreesiaUPC', 'IrisUPC', 'JasmineUPC', 'KodchiangUPC', 'LilyUPC',
                  'DFKai-SB', '@DFKai-SB', 'Lucida Sans Unicode', 'Arial Black', 'Calibri', 'Cambria', 'Cambria Math',
                  'Candara', 'Comic Sans MS', 'Consolas', 'Constantia', 'Corbel', 'Franklin Gothic Medium', 'Gabriola',
                  'Georgia', 'Palatino Linotype', 'Segoe Print', 'Trebuchet MS', 'Verdana', 'Webdings',
                  'Haettenschweiler', 'MS Outlook', 'Book Antiqua', 'Century Gothic', 'Bookshelf Symbol 7',
                  'MS Reference Sans Serif', 'MS Reference Specialty', 'Bradley Hand ITC', 'Freestyle Script',
                  'French Script MT', 'Juice ITC', 'Kristen ITC', 'Lucida Handwriting', 'Mistral', 'Papyrus',
                  'Pristina', 'Tempus Sans ITC', 'Garamond', 'Monotype Corsiva', 'Agency FB', 'Arial Rounded MT Bold',
                  'Blackadder ITC', 'Bodoni MT', 'Bodoni MT Black', 'Bodoni MT Condensed', 'Bookman Old Style',
                  'Calisto MT', 'Castellar', 'Century Schoolbook', 'Copperplate Gothic Bold',
                  'Copperplate Gothic Light', 'Curlz MT', 'Edwardian Script ITC', 'Elephant', 'Engravers MT',
                  'Eras Bold ITC', 'Eras Demi ITC', 'Eras Light ITC', 'Eras Medium ITC', 'Felix Titling', 'Forte',
                  'Franklin Gothic Book', 'Franklin Gothic Demi', 'Franklin Gothic Demi Cond', 'Franklin Gothic Heavy',
                  'Franklin Gothic Medium Cond', 'Gigi', 'Gill Sans MT', 'Gill Sans MT Condensed',
                  'Gill Sans Ultra Bold', 'Gill Sans Ultra Bold Condensed', 'Gill Sans MT Ext Condensed Bold',
                  'Gloucester MT Extra Condensed', 'Goudy Old Style', 'Goudy Stout', 'Imprint MT Shadow', 'Lucida Sans',
                  'Lucida Sans Typewriter', 'Maiandra GD', 'OCR A Extended', 'Palace Script MT', 'Perpetua',
                  'Perpetua Titling MT', 'Rage Italic', 'Rockwell', 'Rockwell Condensed', 'Rockwell Extra Bold',
                  'Script MT Bold', 'Tw Cen MT', 'Tw Cen MT Condensed', 'Tw Cen MT Condensed Extra Bold', 'Algerian',
                  'Baskerville Old Face', 'Bauhaus 93', 'Bell MT', 'Berlin Sans FB', 'Berlin Sans FB Demi',
                  'Bernard MT Condensed', 'Bodoni MT Poster Compressed', 'Britannic Bold', 'Broadway',
                  'Brush Script MT', 'Californian FB', 'Centaur', 'Chiller', 'Colonna MT', 'Cooper Black',
                  'Footlight MT Light', 'Harlow Solid Italic', 'Harrington', 'High Tower Text', 'Jokerman',
                  'Kunstler Script', 'Lucida Bright', 'Lucida Calligraphy', 'Lucida Fax', 'Magneto',
                  'Matura MT Script Capitals', 'Modern No. 20', 'Niagara Engraved', 'Niagara Solid',
                  'Old English Text MT', 'Onyx', 'Parchment', 'Playbill', 'Poor Richard', 'Ravie', 'Informal Roman',
                  'Showcard Gothic', 'Snap ITC', 'Stencil', 'Viner Hand ITC', 'Vivaldi', 'Vladimir Script',
                  'Wide Latin', 'Century', 'Wingdings 2', 'Wingdings 3', 'Arial Unicode MS', '@Arial Unicode MS',
                  'Arial Narrow', 'Rupee Foradian', 'Rupee', 'DevLys 010', 'Calibri Light', 'Monoton', 'Ubuntu Medium',
                  'Ubuntu', 'Ubuntu Light', 'Yatra One', 'HelvLight', 'Lato', 'Great Vibes']

    size = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
            57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
            84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    Style = ['bold', 'italic', 'bold italic', 'Regular']
    update(list_fonts, l1)
    update(Style, l2)
    update(size, l3)
    l1.bind("<<ListboxSelect>>", fillout)
    my_entry1.bind("<KeyRelease>", check)

    l2.bind("<<ListboxSelect>>", fillout2)
    my_entry2.bind("<KeyRelease>", check2)

    l3.bind("<<ListboxSelect>>", fillout3)
    my_entry3.bind("<KeyRelease>", check3)

    def GO_2():
        if str(my_entry2.get()) == 'Regular':
            my_entry2.delete(0, END)
            my_entry2.insert(0, " ")
            TextArea.config(font=f"{str(my_entry1.get())} {str(my_entry3.get())} {str(my_entry2.get())}")
            new_window.destroy()
        else:
            my_entry2.delete(0, END)
            my_entry2.insert(0, " ")
            TextArea.config(font=f"{str(my_entry1.get())} {str(my_entry3.get())} {str(my_entry2.get())}")
            new_window.destroy()

    button_1 = Button(new_window, text="APPLY", command=GO_2)
    button_1.grid(row=3, columns=3, pady=10)


def ZOOM_IN(e=""):
    global Size
    Size = Size + 1
    TextArea.config(font=f"{Font} {str(Size)} {Font_Style}")
    Size = Size


def ZOOM_OUT(e=""):
    global Size
    if Size >= 9:
        Size = Size - 1
        TextArea.config(font=f"{Font} {str(Size)} {Font_Style}")
        Size = Size
    else:
        TextArea.config(font=f"{Font} {str(Size)} {Font_Style}")


def Bar():
    global count_status
    if count_status % 2 == 0:
        status_bar.pack(side=BOTTOM, fill=X)

    if count_status % 2 != 0:
        status_bar.pack_forget()

    count_status = count_status + 1


def ABOUT():
    new_window1 = Toplevel(root)
    new_window1.geometry("320x400")
    new_window1.title("ABOUT NOTEPAD")
    new_window1.config(bg='#F0F0F0')
    TextArea_1 = Text(new_window1, font="InformalRoman 13", bg='#F0F0F0')
    TextArea_1.insert(1.0, 'Notepad is a generic text editor included with all versions of Microsoft Windows that '
                           'allows you to create, open, and read plaintext files. If the file contains special '
                           'formatting or is not a plaintext file, it cannot be read in Notepad. The image is a small '
                           'example of what the Notepad may look like while running.Based on the powerful editing '
                           'component Scintilla, Notepad++ is written in C++ and uses pure Win32 API and STL which '
                           'ensures a higher execution speed and smaller program size. By optimizing as many routines '
                           'as possible without losing user friendliness, Notepad++ is trying to reduce the world '
                           'carbon dioxide emissions. When using less CPU power, the PC can throttle down and reduce '
                           'power consumption, resulting in a greener environment.')
    TextArea_1.pack(expand=True, fill="both")
    new_window1.resizable(FALSE, FALSE)
def Short():
    new_window1 = Toplevel(root)
    new_window1.geometry("320x400")
    new_window1.title("ABOUT NOTEPAD")
    new_window1.config(bg='#F0F0F0')
    TextArea_1 = Text(new_window1, font="InformalRoman 13", bg='#F0F0F0')
    TextArea_1.insert(1.0, '<COPY Control-c> \n'
                           '<COPY Control-C> \n'
                           '<CUT Control-x> \n'
                           '<CUT Control-X> \n'
                           '<PASTE Control-v \n>'
                           '<PASTE Control-V> \n'
                           '<NEW_FILE Control-n> \n '
                           '<NEW_FILE Control-N> \n'
                           '<OPEN_FILE Control-o> \n'
                           '<OPEN_FILE Control-O> \n'
                           '<SAVE_FILE Control-s> \n'
                           '<SAVE_FILE Control-S> \n'
                           '<EXIT Control-e> \n'
                           '<EXIT Control-E> \n'
                           '<FIND Control-f> \n '
                           '<FIND Control-F> \n'
                           '<ZOOM IN Control-i> \n'
                           '<ZOOM IN Control-I> \n'
                           '<ZOOM OUT Control-t> \n '
                           '<ZOOM OUT Control-T> \n'
                           '<White_Mood Control-w> \n'
                           '<White_Mood Control-W> \n'
                           '<Replace Control-r> \n'
                           '<Replace Control-R> \n'
                      )
    TextArea_1.pack(expand=True, fill="both")
    new_window1.resizable(FALSE, FALSE)
def BINDING():
    root.bind('<Control-c>', COPY)
    root.bind('<Control-C>', COPY)
    root.bind('<Control-x>', CUT)
    root.bind('<Control-X>', CUT)
    root.bind('<Control-v>', PASTE)
    root.bind('<Control-V>', PASTE)
    root.bind('<Control-n>', NEW_FILE)
    root.bind('<Control-N>', NEW_FILE)
    root.bind('<Control-o>', OPEN_FILE)
    root.bind('<Control-O>', OPEN_FILE)
    root.bind('<Control-s>', SAVE_FILE)
    root.bind('<Control-S>', SAVE_FILE)
    root.bind('<Control-e>', EXIT_FILE)
    root.bind('<Control-E>', EXIT_FILE)
    root.bind('<Control-f>', FIND)
    root.bind('<Control-F>', FIND)
    root.bind('<Control-i>', ZOOM_IN)
    root.bind('<Control-I>', ZOOM_IN)
    root.bind('<Control-T>', ZOOM_OUT)
    root.bind('<Control-t>', ZOOM_OUT)
    root.bind('<Control-w>', White_Mood)
    root.bind('<Control-W>', White_Mood)
    root.bind('<Control-r>', Replace)
    root.bind('<Control-R>', Replace)


def on_enter(e):
    e.widget['background'] = '#F0FFFF'


def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'
def web_1():
    web.open('https://www.bing.com/search?q=get+help+with+notepad+in+windows+10&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA',new=2, autoraise=True)

class OptionDialog(Toplevel):
    """
        This dialog accepts a list of options.
        If an option is selected, the results property is to that option value
        If the box is closed, the results property is set to zero
    """

    def __init__(self, parent, title, question, options):
        Toplevel.__init__(self, parent, bg="white")
        self.title(title)
        self.geometry("350x100")
        self.question = question
        self.transient(parent)
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.options = options
        self.result = '_'
        self.createWidgets()
        self.grab_set()
        ## wait.window ensures that calling function waits for the window to
        ## close before the result is returned.
        self.wait_window()



    def createWidgets(self):
        frmQuestion = Frame(self)
        Label(frmQuestion, text=self.question, bg="white",fg='#7393B3',pady=10).pack()
        frmQuestion.pack()
        frmButtons = Frame(self)

        frmButtons.pack(side=BOTTOM, fill="both")
        column = 0
        for option in self.options:
            btn = Button(frmButtons, text=option, command=lambda x=option: self.setOption(x), padx=5,bd=0)
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)

            btn.pack(anchor="nw", side=RIGHT, pady=10, padx=3)
            column += 1

    def setOption(self, optionSelected):
        self.result = optionSelected
        self.destroy()

    def cancel(self):
        self.result = None
        self.destroy()


if __name__ == '__main__':
    count_status = 0
    theme_count = 0
    Font = "Consolas"
    Font_Style = ""
    Size = 11
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad.ico")
    root.geometry("1000x500")
    root.config(bg="black")
    TextArea = Text(root, font=f"{Font} {str(Size)} {Font_Style}", bg="#282A36", fg="#43CA63")
    TextArea.pack(expand=True, fill="both")
    file = NONE
    MenuBar = Menu(root, activebackground='#004c99', activeforeground='white')

    # FILE
    filemenu = Menu(MenuBar, tearoff=0)
    filemenu.add_command(label="New    <Control-n>", command=NEW_FILE)
    filemenu.add_command(label="Open   <Control-o>", command=OPEN_FILE)
    filemenu.add_command(label="Save   <Control-s>", command=SAVE_FILE)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT   <Control-e>", command=EXIT_FILE)
    MenuBar.add_cascade(label="File", menu=filemenu)
    # Edit
    Edit = Menu(MenuBar, tearoff=0)
    Edit.add_command(label="Cut      <Control-x>", command=CUT)
    Edit.add_command(label="Paste    <Control-v>", command=PASTE)
    Edit.add_command(label="Copy     <Control-c>", command=COPY)
    Edit.add_command(label="Find     <Control-f>", command=FIND)
    Edit.add_command(label="Replace  <Control-r>", command=Replace)
    MenuBar.add_cascade(label="Edit", menu=Edit)
    # Format
    Format = Menu(MenuBar, tearoff=0)
    Format.add_command(label="White Theme <Control-w>", command=White_Mood)
    Format.add_command(label="Font.. ", command=FONT)
    MenuBar.add_cascade(label="Format", menu=Format)
    # View
    View = Menu(MenuBar, tearoff=0)
    submenu = Menu(View, tearoff=0)
    submenu.add_command(label="ZOOM IN    <Control-i>", command=ZOOM_IN)
    submenu.add_command(label="ZOOM OUT   <Control-u>", command=ZOOM_OUT)
    View.add_cascade(label="ZOOM", menu=submenu, underline=0)
    View.add_command(label="Status Bar", command=Bar)
    MenuBar.add_cascade(label="View", menu=View)
    # Help
    Help = Menu(MenuBar, tearoff=0)
    Help.add_command(label="View Help", command=web_1)
    Help.add_command(label="Short Cuts", command=Short)
    Help.add_separator()
    Help.add_command(label="About Notepad", command=ABOUT)
    MenuBar.add_cascade(label="Help", menu=Help)

    root.config(menu=MenuBar)
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    Scroll1 = Scrollbar(TextArea, orient=HORIZONTAL,cursor="arrow")
    Scroll1.pack(side=BOTTOM, fill=X)
    Scroll1.config(command=TextArea.xview)
    TextArea.config(xscrollcommand=Scroll.set)
    BINDING()

    status_bar = Label(root, text="|Window(CRLF)" + "    " + "  |UTF-8" + "  ", relief=SUNKEN, anchor="e")
    status_bar.pack(side=BOTTOM, fill=X)


    def exit_function():
        # Put any cleanup here.
        if TextArea.compare("end-1c", "==", "1.0"):
            root.destroy()
        else:
           values = ['CANCEL', 'Dont SAVE', 'SAVE']
           dlg = OptionDialog(root, 'Notepad', "DO YOU WANT TO SAVE CHANGES INTO Untitled ?", values)
           if dlg.result == 'SAVE':
               SAVE_FILE()
           if dlg.result == 'Dont SAVE':
              root.destroy()
           if dlg.result == 'CANCEL':
               dlg.destroy()


    root.protocol('WM_DELETE_WINDOW', exit_function)

    root.mainloop()
