from tkinter import *
from myapi import API
from mydb import Database
from tkinter import messagebox


class NLPApp:

    def __init__(self):
        self.apio = API()
        self.dbo = Database()
        self.root = Tk()                                    # Tk is main class of tkinter
        self.root.title('NLP Application')                  # title
        self.root.iconbitmap('resources/favicon.ico')       # add image to GUI
        self.root.geometry('400x600')
        self.root.configure(bg = 'grey')

        self.login_gui()
        self.root.mainloop()                                # holds GUI on screen


    def login_gui(self):

        self.clear()

        login_heading = Label(self.root , text = 'NLP Application', bg = 'grey' , fg = 'white')
        login_heading.pack(pady = (30,30))
        login_heading.configure(font = ('Borel',20))

        label_1 = Label(self.root , text = 'email' , bg = 'grey' , fg = 'white')
        label_1.pack(pady = (10,10))
        label_1.configure(font = ('Borel',20))

        self.email_input = Entry(self.root , width= 40)                         # entry is used to take inputs
        self.email_input.pack(pady = (10,10), ipady = 3)

        label_2 = Label(self.root , text = 'password' , bg = 'grey' , fg = 'white')
        label_2.pack(pady = (10,10))
        label_2.configure(font = ('Borel' , 20))

        self.password_input = Entry(self.root , width = 40 , show='*')
        self.password_input.pack(pady = (10,10) , ipady = 3)

        login_symbol = Button(self.root , text = 'Login', width=7 , command=self.perform_login)                                              # used to make button
        login_symbol.pack(pady = (10,10), ipady = 2)

        label_3 = Label(self.root , text = 'New User ? Register Now' , bg = 'grey' , fg = 'white')
        label_3.pack(pady = (10,10))
        label_3.configure(font = ('Borel' , 10))

        register_symbol = Button(self.root , text = 'Register' , width=7 , command=self.register_gui)
        register_symbol.pack(pady = (10,10) , ipady = 2)



    def register_gui(self):
        self.clear()

        register_heading = Label(self.root , text = 'Register Yourself' , bg = 'grey' , fg = 'white')
        register_heading.pack(pady = (30,30))
        register_heading.configure(font = ('Borel' , 20))

        label_1 = Label(self.root , text = 'enter your name', bg = 'grey' , fg = 'white')
        label_1.pack(pady = (10,10))
        label_1.configure(font = ('Borel' , 15))

        self.name_input = Entry(self.root , width =30)
        self.name_input.pack(pady = (10,10) , ipady= 4)

        label_2 = Label(self.root, text='enter your email', bg='grey', fg='white')
        label_2.pack(pady=(10, 10))
        label_2.configure(font=('Borel', 15))

        self.email_input = Entry(self.root, width=40)
        self.email_input.pack(pady=(10, 10), ipady=4)

        label_3 = Label(self.root, text='Create Your password', bg='grey', fg='white')
        label_3.pack(pady=(10, 10))
        label_3.configure(font=('Borel', 14))

        self.password_input = Entry(self.root, width=40, show='*')
        self.password_input.pack(pady=(10, 10), ipady=3)

        Register_symbol = Button(self.root , text = 'Register' , command= self.perform_registration)
        Register_symbol.pack(pady=(10, 10), ipady=2)

        Login_symbol = Button(self.root , text = 'Login Now !!' , command= self.login_gui)
        Login_symbol.pack(pady = (10,10), ipady = 2)


    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name , email , password)

        if response:
            messagebox.showinfo('success','registration successful !! You can proceed')
        else:
            messagebox.showerror('error','email already exists !!')

    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email , password)
        if response:
            messagebox.showinfo('success','login successful !! ')
            self.homePage()
        else:
            messagebox.showerror('error','login again !!')


    def homePage(self):

        self.clear()

        login_heading = Label(self.root, text='NLP Application', bg='grey', fg='white')
        login_heading.pack(pady=(30, 30))
        login_heading.configure(font=('Borel', 20))

        ner_btn = Button(self.root, text='NER' , width=20 , height=3, command= self.ner_gui)
        ner_btn.pack(pady=(40, 40))

        language_btn = Button(self.root, text='Language Detection' , width=20 , height=3, command= self.language_gui)
        language_btn.pack(pady=(40, 40))

        sentiment_btn = Button(self.root, text='Sentiment Analysis' , width=20 , height=3 , command=self.sentiment_analysis)
        sentiment_btn.pack(pady=(40, 40))

        logout_btn = Button(self.root , text = 'Logout' , command= self.login_gui)
        logout_btn.pack(pady = (20,20))


    def sentiment_analysis(self):

        self.clear()

        login_heading = Label(self.root, text='NLP Application', bg='grey', fg='white')
        login_heading.pack(pady=(30, 30))
        login_heading.configure(font=('Borel', 20))

        heading2 = Label(self.root , text = 'Sentiment Analysis', bg = 'grey' , fg = 'white')
        heading2.pack(pady = (30,30))
        heading2.configure(font =('Borel' , 20))

        para = Label(self.root, text='enter the paragraph', bg='grey', fg='white')
        para.pack(pady=(10, 10))
        para.configure(font=('Borel', 12))

        self.para_input = Entry(self.root , width = 40)
        self.para_input.pack(pady = (20,20) , ipady = 10)

        sentiment_btn = Button(self.root , text = 'analyze sentiment' , command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady = (10,10))

        self.sentiment_res = Label(self.root , text ='')
        self.sentiment_res.pack(pady = (10,10))

        goback_btn = Button(self.root , text = 'Go Back' , command=self.homePage)
        goback_btn.pack(pady = (10,10))


    def do_sentiment_analysis(self):

        text = self.para_input.get()
        result = self.apio.sentiment_analysis(text)
        print(result)

        self.sentiment_res['text'] = result

    def ner_gui(self):
        self.clear()

        heading = Label(self.root, text='NER', bg='grey', fg='white', font=('Borel', 20))
        heading.pack(pady=(30, 30))

        para = Label(self.root, text='Enter text for NER:', bg='grey', fg='white', font=('Borel', 12))
        para.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=40)
        self.ner_input.pack(pady=(10, 10), ipady=10)

        ner_btn = Button(self.root, text='Extract Entities', command=self.do_ner)
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='', bg='grey', fg='white', wraplength=380, justify='left')
        self.ner_result.pack(pady=(10, 10))

        back_btn = Button(self.root, text='Go Back', command=self.homePage)
        back_btn.pack(pady=(10, 10))

    def do_ner(self):
        text = self.ner_input.get()
        entities = self.apio.ner(text)

        if not entities:
            self.ner_result['text'] = "No entities found."
            return

        result_lines = []
        for ent in entities:
            word = ent['word']
            label = ent['entity_group']
            score = ent['score']
            # Clean word formatting (removes ## from subwords if any)
            clean_word = word.replace("##", "")
            result_lines.append(f"{clean_word} → {label} ({score:.2f})")

        result_text = '\n'.join(result_lines)
        self.ner_result['text'] = result_text

    def language_gui(self):
        self.clear()

        heading = Label(self.root, text='Language Detection', bg='grey', fg='white', font=('Borel', 20))
        heading.pack(pady=(30, 30))

        para = Label(self.root, text='Enter text to detect language:', bg='grey', fg='white', font=('Borel', 12))
        para.pack(pady=(10, 10))

        self.lang_input = Entry(self.root, width=40)
        self.lang_input.pack(pady=(10, 10), ipady=10)

        lang_btn = Button(self.root, text='Detect Language', command=self.do_language_detection)
        lang_btn.pack(pady=(10, 10))

        self.lang_result = Label(self.root, text='', bg='grey', fg='white')
        self.lang_result.pack(pady=(10, 10))

        back_btn = Button(self.root, text='Go Back', command=self.homePage)
        back_btn.pack(pady=(10, 10))

    def do_language_detection(self):
        text = self.lang_input.get()
        lang = self.apio.detect_language(text)
        self.lang_result['text'] = f"Detected Language: {lang}"

    def clear(self):
        for i in self.root.pack_slaves():
            print(i.destroy())





nlp = NLPApp()