import string
from tkinter import *
from tkinter import ttk
import math
from functools import partial  # to prevent unwanted windows


class JobEnter:
    def __init__(self):

        # gui for main menu/new job enter
        # start frame
        self.start_frame = Frame(pady=10, padx=10)
        self.start_frame.grid()


        # view all jobs button
        self.view_all_button = Button(self.start_frame, text="View All Jobs",
                                      command=self.view_all_jobs)
        self.view_all_button.grid(row=9)

        # close menu button
        self.close_button = Button(self.start_frame, text="Close",
                                   font="Arial 15", command=self.close_menu)
        self.close_button.grid(row=9, column=1)

        # all jobs list
        self.all_jobs_list = []

    def close_menu(self):
        root.destroy()

    def view_all_jobs(self):
        AllJobs(self)



class AllJobs:
    def __init__(self, partner):
        self.all_jobs_box = Toplevel()

        # gui frame
        self.show_frame = Frame(root, padx=10, pady=10)  # job info display
        self.show_frame.grid(row=0)
        self.button_frame = Frame(root, padx=10, pady=10)  # button frame
        self.button_frame.grid(row=1)

        # disable the all jobs button on menu
        partner.view_all_button.config(state=DISABLED)

        # all jobs heading
        self.suzy_mobile_heading = Label(self.show_frame, text="All Jobs Entered",
                                         font="Arial 19 bold", padx=10, pady=10)
        self.suzy_mobile_heading.grid(row=0, pady=5)

        self.all_jobs_list = [[1, 'Harmony', 10, 2, False, 39.7],
                              [2, 'Sally', 54, 60, True, 43.1],
                              [3, 'Anna', 154, 20, True, 92.2]]  # substitutes for now

        # job number label
        self.job_number = IntVar()
        self.job_number.set(self.all_jobs_list[0][0])
        self.job_number_label = Label(self.show_frame, text="Job Number:")
        self.job_number_label.grid(row=1)
        self.show_job_number = Label(self.show_frame, textvariable=self.job_number)
        self.show_job_number.grid(row=1, column=1)

        # customer name label
        self.customer_name = StringVar()
        self.customer_name.set(self.all_jobs_list[0][1])
        self.customer_name_label = Label(self.show_frame, text="Customer Name:")
        self.customer_name_label.grid(row=2)
        self.show_customer_name = Label(self.show_frame, textvariable=self.customer_name)
        self.show_customer_name.grid(row=2, column=1)

        # job amount label
        self.job_amount = DoubleVar()
        self.job_amount.set(self.all_jobs_list[0][5])
        self.job_amount_label = Label(self.show_frame, text="Job Amount: $")
        self.job_amount_label.grid(row=3)
        self.show_job_amount = Label(self.show_frame, textvariable=self.job_amount)
        self.show_job_amount.grid(row=3, column=1)

        # 'previous' button
        self.prev_button = Button(self.button_frame, text="Previous",
                                  command=lambda:self.display_input("prev"))
        self.prev_button.grid(row=0)

        # 'next' button
        self.next_button = Button(self.button_frame, text="Next",
                                  command=lambda:self.display_input("next"))
        self.next_button.grid(row=0, column=1)

        # 'close' button
        self.close_button = Button(self.button_frame, text="Close",
                                   command=partial(self.close_all_jobs, partner))

    def close_all_jobs(self, partner):
        partner.view_all_button.config(state=NORMAL)

        # close all jobs window
        self.all_jobs_box.destroy()

    def display_input(self, scroll):
        self.job = 1
        # change displayed job info
        if scroll == "next":
            self.job += 1
            self.job_number.set(self.all_jobs_list[self.job][0])
            self.customer_name.set(self.all_jobs_list[self.job][1])
            self.job_amount.set(self.all_jobs_list[self.job][5])
        elif scroll == "prev":
            self.job -= 1
            self.job_number.set(self.all_jobs_list[self.job][0])
            self.customer_name.set(self.all_jobs_list[self.job][1])
            self.job_amount.set(self.all_jobs_list[self.job][5])

        if self.job == 0:
            self.prev_button.config(state=DISABLED)
        else:
            self.prev_button.config(state=NORMAL)

        if self.job == len(self.all_jobs_list) - 1:
            self.next_button.config(state=DISABLED)
        else:
            self.next_button.config(state=NORMAL)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Mobile Service")
    something = JobEnter()
    root.mainloop()
