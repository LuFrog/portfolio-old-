import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from capture_img import open_webcam,open_webcam_yolo
from reconnaissance.fonction_yolo import reconnaissance_d




class RecyclotronGUI(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.display_image = tk.StringVar(value="")
        self.input_image = tk.StringVar(value="")
        self.use_yolo = tk.StringVar(value="")
        self.create_widgets()
        self.pack()
    
    '''
    Create all the graphical elements (widgets) in the window.
    '''
    def create_widgets(self):
        # Add a title to the main window.
        self.parent.title("Recyclotron")
        
        # Create the notebook (tabbed panel) inside the main window.
        self.create_notebook()



    '''
    Create the notebook (tabbed pane) inside the main window
    '''
    def create_notebook(self):
        ttk.Style().configure("TButton", padding=6, relief="flat",background="#ccc")
        # Create in the main window a notebook (panel with different tabs)
        nb = ttk.Notebook(self.parent)
    
        # Create the student tab.
        self.create_from_file(nb)

        # The registration tab.
        self.create_from_webcam(nb)  

        #self.create_settings(nb)  

        nb.pack(expand=1, fill="both")

    '''
    Create the from_file tab
    '''
    def create_from_file(self, nb):
        first_tab = ttk.Frame(nb)
        nb.add(first_tab, text='Select from file')

        ttk.Label(first_tab, text="Image path :").grid(row=1, column=0, padx=10, pady=10, sticky='W')
        
        ttk.Label(first_tab, text="Corresponding bin :").grid(row=3, column=0, padx=10, pady=10, sticky='W')


        def select_waste_from_computer():
            main_window.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
            print(main_window.filename)
            self.input_image.set(main_window.filename)
            return()

        ttk.Label(first_tab, text="Select your waste :").grid(row=0, column=0, padx=10, pady=10, sticky='W')
        add_file_button = ttk.Button(first_tab, text="search your computer", command=select_waste_from_computer)
        add_file_button.grid(row=0, column=1)


        def update_path(event):
            self.input_image.get()
        
        def find_out_which_bin():
            try:
                ttk.Label(first_tab, text=reconnaissance_d(self.input_image.get())).grid(row=3, column=1, padx=10, pady=10, sticky='W')
            except:
                ttk.Label(first_tab, text='incorrect path').grid(row=3, column=1, padx=10, pady=10, sticky='W')
        
        input_image_path_entry = ttk.Entry(first_tab, textvariable=self.input_image)
        input_image_path_entry.grid(row=1, column=1, padx=10, pady=10, sticky='W') 
        
        input_image_path_entry.bind("<FocusOut>", update_path)
        bin_button = ttk.Button(first_tab, text="Let's find out!", command=find_out_which_bin)
        bin_button.grid(row=2,column=0)





    def create_from_webcam(self,nb):
        second_tab = ttk.Frame(nb)
        nb.add(second_tab, text='Take a picture with your webcam')
        ttk.Label(second_tab, text="To take the picture, press space when your webcam is opened").grid(row=3, column=0, padx=10, pady=10, sticky='W')
        ttk.Label(second_tab, text="To close your webcam, press x for 3 seconds").grid(row=4, column=0, padx=10, pady=10, sticky='W')
        add_webcam_button = ttk.Button(second_tab, text="Open your webcam", command=open_webcam)
        add_webcam_button.grid(row=1, column=0)
        add_webcam_button = ttk.Button(second_tab, text="Open your webcam with object recognition", command=open_webcam_yolo)
        add_webcam_button.grid(row=2, column=0)


        def update_yolo(event):
            if self.use_yolo.get() == 'No':
                open_webcam_mutable = open_webcam
                print('No')
            elif self.use_yolo.get() == 'Yes':
                open_webcam_mutable = open_webcam_yolo
                print('Yes')
            else:
                print('Debug')
            return
        
        add_webcam_button.bind("<Enter>",update_yolo)

    def create_settings(self,nb):
        third_tab = ttk.Frame(nb)
        nb.add(third_tab, text='Settings')
        ttk.Label(third_tab, text="Use object recognition ?").grid(row=0, column=0, padx=10, pady=10, sticky='W')
        my_combobox = ttk.Combobox(third_tab, values=['Yes','No','Maybe'])
        my_combobox.grid(row=0, column=1, sticky='W')
        ttk.Label(third_tab, text="Please press return to confirm").grid(row=1, column=0, padx=10, pady=10, sticky='W')

        def update_settings(event):
            self.use_yolo.set(my_combobox.get())
            print('debug')
        
        my_combobox.bind("<Return>",update_settings)
    

main_window = tk.Tk()
app = RecyclotronGUI(parent=main_window)
app.mainloop()

#PhotoImage