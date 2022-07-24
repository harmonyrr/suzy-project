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

        # logo (row 0)
        logo_img = PhotoImage(file="images/suzy_logo.png")
        self.logo_label = Label(self.start_frame, image=logo_img, width=500)
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

        # distance travelled input (to customer)
        self.distance_travel = IntVar()
        self.distance_travel_label = Label(self.start_frame, font="Arial 15",
                                           text="Distance Travelled", justify=LEFT)
        self.distance_travel_label.grid(row=5, column=0)
        self.distance_travel_entry = Entry(self.start_frame,
                                           font="Arial 15", textvariable=self.distance_travel)
        self.distance_travel_entry.grid(row=5, column=1)
        self.distance_travel_entry.delete(0, END)

        # virus protection input
        self.virus_protection = IntVar()
        self.virus_protection_label = Label(self.start_frame, font="Arial 15",
                                            justify=LEFT, text="Time on Virus Protection")
        self.virus_protection_label.grid(row=6)
        self.virus_protection_entry = Entry(self.start_frame,
                                            font="Arial 15", textvariable=self.virus_protection)
        self.virus_protection_entry.grid(row=6, column=1)
        self.virus_protection_entry.delete(0, END)

        # wof and tune input
        self.general_wof = BooleanVar()
        self.general_wof_label = Label(self.start_frame, font="Arial 15",
                                       text="General WOF and tune service required?")
        self.general_wof_label.grid(row=7)
        self.general_wof_tick = ttk.Checkbutton(self.start_frame, text="Yes",
                                                textvariable=self.general_wof)
        self.general_wof_tick.grid(row=7, column=1)

        # error checking label
        self.error_check_label = Label(self.start_frame, text="")
        self.error_check_label.grid(row=8)

        # enter job button
        self.enter_job_button = Button(self.start_frame,
                                       text="Enter Job", font="Arial 15",
                                       justify=LEFT, command=self.store_input)
        self.enter_job_button.grid(row=8)

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

    def store_input(self):
         #check nothing is blank
        if self.customer_name.get == "" or self.distance_travel.get() == "" or self.virus_protection.get() == "":
            self.error_check_label.config(text="Do not leave any entries blank.")
        else:
            # check customer name is valid
            try:
                customer_name = self.customer_name.get()
                customer_name = ''.join([i for i in customer_name if not i.isdigit()])
                for char in string.punctuation:
                    customer_name = customer_name.replace(char, '')
                customer_name = customer_name.strip()
                if customer_name == "":
                    raise ValueError
            except ValueError:
                # display error message
                self.error_check_label.config(text="Customer name should not include any numbers or special characters.", wrap=275)
                self.error_check_label.grid(row=8, column=1)
            else:
                try:
                    #check distance is a valid number
                    distance_travel = float(self.distance_travel.get())
                    if distance_travel < 0:
                        raise ValueError
                except ValueError:
                    self.error_check_label.config(text="Invalid Distance.")
                    self.error_check_label.grid(row=8, column=1)
                else:
                    # check virus time is a number
                    try:
                        virus_protection = float(self.virus_protection.get())
                        if virus_protection < 0:
                            raise ValueError
                    except ValueError:
                        self.error_check_label.config(text="Invalid Time.")
                        self.error_check_label.grid(row=8, column=1)
                    else:
                        job_number = self.job_number.get()
                        general_wof = self.general_wof.get()

                        # add input to job list
                        self.all_jobs_list.append([job_number, customer_name, distance_travel, virus_protection, general_wof])

                        # success message
                        self.error_check_label.config(text="Job entry successful.")

                        # clear user input
                        self.customer_name.set("")
                        self.distance_travel_entry.delete(0, END)
                        self.virus_protection_entry.delete(0, END)
                        self.general_wof.set(False)

                        # run job charge calculation function
                        self.job_charge_calc()

    def job_charge_calc(self, ):
        distance_travel = self.distance_travel.get()
        fixed_rate = 10
        additional_rate = 0.5

        distance_travel = int(math.floor(distance_travel*fixed_rate + additional_rate / fixed_rate))

        # calculate charge
        virus_protection = self.virus_protection.get()
        virus_rate = 0.8

        if distance_travel > 5:
            self.job_amount = fixed_rate + additional_rate*(distance_travel - 5) + virus_rate * virus_protection
        else:
            self.job_amount = fixed_rate + virus_rate*virus_protection

        general_wof = self.general_wof.get()
        if general_wof:
            self.job_amount += 100

        # add job charge to jobs list
        self.job_number -= 1
        self.all_jobs_list.append(self.job_amount)

        # clear error message & input
        self.customer_name.set("")
        self.distance_travel_entry.delete(0, END)
        self.virus_protection_entry.delete(0, END)
        self.general_wof.set(False)

        # clear the error message
        self.error_check_label.config(text="")

    def view_all_jobs(self, all_jobs_list):
        AllJobs(self, all_jobs_list)



class AllJobs:
    def __init__(self, partner, all_jobs_list):
        self.all_jobs_box = Toplevel()

        # gui frame
        self.show_frame = Frame(self.all_jobs_box, padx=10, pady=10)  # job info display
        self.show_frame.grid(row=0)
        self.button_frame = Frame(self.all_jobs_box, padx=10, pady=10)  # button frame
        self.button_frame.grid(row=1)

        # disable the all jobs button on menu
        partner.view_all_button.config(state=DISABLED)

        # all jobs heading
        self.suzy_mobile_heading = Label(self.show_frame, text="All Jobs Entered",
                                         font="Arial 19 bold", padx=10, pady=10)
        self.suzy_mobile_heading.grid(row=0, pady=5)

        self.all_jobs_list = all_jobs_list

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



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Mobile Service")
    something = JobEnter()
    root.mainloop()
