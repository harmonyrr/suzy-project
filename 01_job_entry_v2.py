from tkinter import *
from tkinter import ttk
# from functools import partial  # to prevent unwanted windows
# import random


class JobEnter:
    def __init__(self):

        # gui for main menu/new job enter
        # start frame
        self.start_frame = Frame(pady=10, padx=10)
        self.start_frame.grid()

        # logo (row 0)
        logo_img = PhotoImage(file="suzy_project/suzy_logo.png")
        self.logo_label = Label(self.start_frame, image=logo_img)
        self.logo_label.grid(row=0, column=0)

        # program label (row 1)
        self.suzy_mobile_label = Label(self.start_frame, text="New Job Entry",
                                       font="Arial 19 bold",
                                       padx=10, pady=10)
        self.suzy_mobile_label.grid(row=1, column=0)

        # instructions
        self.instructions_label = Label(self.start_frame, font="Arial 15 italic",
                                        text="Please enter the information into the "
                                             "appropriate boxes and press 'Enter Job' "
                                             "when done.")
        self.instructions_label.grid(row=2, columnspan=2)

        # job number input
        self.job_number = IntVar()
        self.job_number_label = Label(self.start_frame, font="Arial 15",
                                      text="Job Number ", justify=LEFT)
        self.job_number_label.grid(row=3, column=0)
        self.job_number_entry = Entry(self.start_frame,
                                      textvariable=self.job_number,
                                      font="Arial 15", justify=LEFT)
        self.job_number_entry.grid(row=3, column=1)

        # customer name input
        self.customer_name = StringVar()
        self.customer_name_label = Label(self.start_frame, font="Arial 15",
                                         text="Customer Name", justify=LEFT)
        self.customer_name_label.grid(row=4, column=0)
        self.customer_name_entry = Entry(self.start_frame, font="Arial 15",
                                         textvariable=self.customer_name, justify=LEFT)
        self.customer_name_entry.grid(row=4, column=1)

        # distance travelled input
        self.distance_travel = DoubleVar()
        self.distance_travel_label = Label(self.start_frame, font="Arial 15",
                                           text="Distance Travelled", justify=LEFT)
        self.distance_travel_label.grid(row=5, column=0)
        self.distance_travel_entry = Entry(self.start_frame,
                                           font="Arial 15", textvariable=self.distance_travel)
        self.distance_travel_entry.grid(row=5, column=1)

        # virus protection input
        self.virus_protection = IntVar()
        self.virus_protection_label = Label(self.start_frame, font="Arial 15",
                                            justify=LEFT, text="Time on Virus Protection")
        self.virus_protection_label.grid(row=6)
        self.virus_protection_entry = Entry(self.start_frame,
                                            font="Arial 15", textvariable=self.virus_protection)
        self.virus_protection_entry.grid(row=6, column=1)

        # wof and tune input
        self.general_wof = IntVar()
        self.general_wof_label = Label(self.start_frame, font="Arial 15",
                                       text="General WOF and tune service required?")
        self.general_wof_label.grid(row=7)
        self.general_wof_tick = ttk.Checkbutton(self.start_frame, text="Yes",
                                                textvariable=self.general_wof)
        self.general_wof_tick.grid(row=7, column=1)

        # enter job button
        self.enter_job_button = Button(self.start_frame,
                                       text="Enter Job", font="Arial 15",
                                       padx=5, pady=5, justify=LEFT)
        self.enter_job_button.grid(row=8, columnspan=2)

        # view all jobs button
        self.view_all_button = Button(self.start_frame, text="View All Jobs")
        self.view_all_button.grid(row=9)

        # close menu button
        self.close_button = Button(self.start_frame, text="Close",
                                   font="Arial 15", command=self.close_menu)
        self.close_button.grid(row=9, column=1)

    def close_menu(self):
        self.root.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Mobile Service")
    something = JobEnter()
    root.mainloop()
