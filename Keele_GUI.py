from tkinter import *
import tkinter as tk
from tkinter import ttk
import csv

class Keele:
    
    user_options = ['building/location name','building/location number',
                   'building/location classification']

    save_value = []
    def __init__(self):
        self.keele, self.building_name_list, self.building_classification_list, self.building_number_list = self.get_csv_cols_as_list('Keele Project.csv')
        self.root = tk.Tk()
        self.root.title('Keele Map')
        self.root.geometry("600x600")
        self.user_input = StringVar()
        self.result = StringVar()
        
        self.output_listbox = tk.Listbox(self.root, width=90)
        self.entLab = ttk.Label(self.root,text='Kindly select an option:', font = ('Arial',12))
        self.entLab.grid(row=0,column=0,sticky='W')
        self.scrollbar = ttk.Scrollbar(self.root,orient=VERTICAL)
        self.combo = ttk.Combobox(self.root, textvariable = self.user_input, width=40, value= self.user_options)
        self.combo.current(0)
        self.combo.grid(row=1,column=0,sticky='W')
        self.combo.bind("<<ComboboxSelected>>", self.create_list_box)
        self.label = Label(self.root,font = ('Arial',12),text = 'Options',textvariable=self.user_input).grid(row=2,column=0, sticky='W')
        Button(self.root, text="clear", command=self.clear).grid(row=7,column=0, sticky='W')

        
    def get_csv_cols_as_list(self,path):
        
        header = ['Building_Name', 'Classification', 'Building_Number']
        file = open(path,'r', newline='')
        next(file)
        csv_reader = csv.DictReader(file, fieldnames=header)
        keele_all = []
        keele_columns_dict = {}
          
        for row in csv_reader:
            for header, value in row.items():
                try:
                    keele_columns_dict[header].append(value)
                except KeyError:
                    keele_columns_dict[header] = [value]
            keele_all.append(row)
        return keele_all,tuple(set(keele_columns_dict['Building_Name'])), keele_columns_dict['Classification'],keele_columns_dict['Building_Number']
         
        
    def show_matching_output(self,user_choice):
        
        if self.combo.get() == 'building/location name':
            self.clear()
            for building_info in self.keele:
                if building_info['Building_Name'] == user_choice:
                    self.save_value.append("Building Number: " + str( building_info['Building_Number']) + ' ' +'Building Classification: ' + str(building_info['Classification']) +'\n')
            for i in range(len(self.save_value)):
                self.output_listbox.insert(i, self.save_value[i])
                self.output_listbox.grid(row=6,column=0, sticky='W')
           
        elif self.combo.get() == 'building/location number':
            self.clear()
            for building_info in self.keele:
                if building_info['Building_Number'] == user_choice:
                    self.save_value.append("Building Name: " + str( building_info['Building_Name']) + ' ' +'Building Classification: ' + str(building_info['Classification']) +'\n')
            for i in range(len(self.save_value)):
                self.output_listbox.insert(i, self.save_value[i])
                self.output_listbox.grid(row=6,column=0, sticky='W')

        elif self.combo.get() == 'building/location name':
            self.clear()
            for building_info in self.keele:
                if building_info['Classification'] == user_choice:
                    self.save_value.append("Building Number: " + str( building_info['Building_Number']) + ' ' +'Building Name: ' + str(building_info['Building_Name']) +'\n')
            for i in range(len(self.save_value)):
                self.output_listbox.insert(i, self.save_value[i])
                self.output_listbox.grid(row=6,column=0, sticky='W')

    def create_scroll_bar(self,list_box):
        self.scrollbar.config(command=list_box.yview)
        self.scrollbar.grid(row=3,column=1, columnspan=2,sticky='W')
        
    def create_list_box(self,event):
        if self.combo.get() == 'building/location classification':
            listbox = tk.Listbox(self.root,listvariable=tk.StringVar(value=sorted(self.building_name_list)),selectmode='single')
            listbox.grid(row=3,column=0,sticky='W')
            listbox.bind('<<ListboxSelect>>',self.create_output)
        elif self.combo.get() == 'building/location number':
            listbox= tk.Listbox(self.root,listvariable=tk.StringVar(value=sorted(self.building_number_list)),selectmode='single',yscrollcommand=self.scrollbar.set)
            self.create_scroll_bar(listbox)
            listbox.grid(row=3,column=0,sticky='W')
            listbox.bind('<<ListboxSelect>>',self.create_output)
        else: listbox = tk.Listbox(self.root,width=40,listvariable=tk.StringVar(value=sorted(self.building_classification_list)),selectmode='single');self.create_scroll_bar(listbox);listbox.grid(row=3,column=0,sticky='W');listbox.bind('<<ListboxSelect>>',self.create_output)
        
    def create_output(self,event):
        tk.Label(self.root, text="outcome").grid(row=5,column=0,sticky='W')
        choice = event.widget.curselection()
        try:
            index = choice[0]
            value = event.widget.get(index)
            self.result.set(value)
            self.show_matching_output(self.result.get())
        except IndexError:
            pass

    def clear(self):
        self.output_listbox.delete(0, END)
        self.save_value = []

if __name__ == '__main__':
    app = Keele()
    app.root.mainloop()
