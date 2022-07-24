from tkinter import *
from tkinter import ttk
import math
from functools import partial  # to prevent unwanted windows
import string


class JobEnter:
    def __init__(self):

        # gui for main menu/new job enter
        # start frame
        self.start_frame = Frame(pady=10, padx=10)
        self.start_frame.grid()

        # logo (row 0)
        logo_img = PhotoImage(file="images/suzy_logo.png")
        self.logo_label = Label(self.start_frame, image=logo_img)
        self.logo_label.image = logo_img
        self.logo_label.grid(row=0, column=0, columnspan=2)

        # program label (row 1)
        self.suzy_mobile_label = Label(self.start_frame, text="New Job Entry",
                                       font="Arial 19 bold",
                                       padx=10, pady=10)
        self.suzy_mobile_label.grid(row=1, columnspan=2)

        # instructions
        self.instructions_label = Label(self.start_frame, font="Arial 15 italic",
                                        text="Please enter the information into the "
                                             "appropriate boxes and press 'Enter Job' "
                                             "when done. Press 'All Jobs' to view "
                                             "all the jobs you have entered. 'All Jobs' will "
                                             "not be available until you have entered at least one job.", bg="#f0f0f0",
                                        wrap=300)
        self.instructions_label.grid(row=2, columnspan=2, padx=10, pady=5)

        # job number input
        self.job_number = IntVar()
        self.job_number.set(1) # automatically sets to 1 when there are no other inputs
        self.job_number_label = Label(self.start_frame, font="Arial 15",
                                      text="Job Number ", justify=LEFT)
        self.job_number_label.grid(row=3, column=0)
        self.job_number_entry = Entry(self.start_frame,
                                      textvariable=self.job_number,
                                      font="Arial 15", justify=LEFT, width=4)
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

        # general wof and tune input
        self.general_wof = BooleanVar()
        self.general_wof_label = Label(self.start_frame, font="Arial 15",
                                       text="General WOF and tune service required?")
        self.general_wof_label.grid(row=7)
        self.general_wof_tick = ttk.Checkbutton(self.start_frame, text="Yes",
                                                variable=self.general_wof)
        self.general_wof_tick.grid(row=7, column=1)

        # error checking label
        self.error_check_label = Label(self.start_frame, text="", font="Arial 15")
        self.error_check_label.grid(row=8, column=1)

        # enter job button
        self.enter_job_button = Button(self.start_frame,
                                       text="Enter Job", font="Arial 15",
                                       justify=LEFT, command=self.store_input)
        self.enter_job_button.grid(row=8, columnspan=2, pady=5)

        # view all jobs button
        self.view_all_button = Button(self.start_frame, text="View All Jobs",
                                      command=lambda:self.view_all_jobs(self.all_jobs_list))
        self.view_all_button.grid(row=9)

         # all jobs list
        self.all_jobs_list = []

        # close menu button
        self.close_button = Button(self.start_frame, text="Close",
                                   font="Arial 15", command=self.close_menu)
        self.close_button.grid(row=9, column=1)


    def close_menu(self):
        root.destroy()

    def store_input(self):
        # check nothing is blank
        if self.customer_name.get == "" or self.distance_travel.get() == "" or self.virus_protection.get() == "":
            self.error_check_label.config(text="Do not leave any entries blank.", font="Arial 15 bold", bg="#faa0b6")
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
                self.error_check_label.config(text="Customer name should not include any numbers or special characters.", wrap=200,
                                              font="Arial 15 bold", bg="#faa0b6")
                self.error_check_label.grid(row=8, column=1)
            else:
                try:
                    # check distance is a valid number
                    distance_travel = float(self.distance_travel.get())
                    if distance_travel < 0:
                        raise ValueError
                except ValueError:
                    self.error_check_label.config(text="Invalid Distance.",
                                                  font="Arial 15 bold", bg="#faa0b6")
                else:
                    # check virus time is a number
                    try:
                        virus_protection = float(self.virus_protection.get())
                        if virus_protection < 0:
                            raise ValueError
                    except ValueError:
                        self.error_check_label.config(text="Invalid Time.",
                                                      font="Arial 15 bold", bg="#faa0b6")
                    else:
                        job_number = self.job_number.get()
                        general_wof = self.general_wof.get()

                        # add input to job list
                        self.all_jobs_list.append([job_number, customer_name, distance_travel, virus_protection, general_wof])

                        # success message
                        self.error_check_label.config(text="Job entry successful.",
                                                      font="Arial 15 bold", bg="#c4c5ff", padx=5)

                        # enable view all jobs button
                        self.view_all_button.config(state=NORMAL)

                        # run job charge calculation function
                        self.job_charge_calc()


    def job_charge_calc(self):
        distance_travel = self.distance_travel.get()
        decimal_point = 0
        multiplier = 10 ** decimal_point
        additional_rate = 0.5

        distance_travel = int(math.floor(distance_travel*multiplier + additional_rate / multiplier))

        # calculate charge
        fixed_rate = 10
        virus_protection = self.virus_protection.get()
        virus_rate = 0.8

        if distance_travel > 5:
            self.job_amount = fixed_rate + additional_rate*(distance_travel - 5) + virus_rate * virus_protection
        else:
            self.job_amount = fixed_rate + virus_rate*virus_protection

        general_wof = self.general_wof.get()
        if general_wof:
            self.job_amount += 100

        # add job charge to jobs list, round charge to 2 places
        job_number = self.job_number.get()
        job_number -= 1
        self.all_jobs_list[job_number].append(round(self.job_amount, 2))

        # clear error message & input
        self.customer_name.set("")
        self.distance_travel_entry.delete(0, END)
        self.virus_protection_entry.delete(0, END)
        self.general_wof.set(False)
        self.error_check_label.config(text="")

        # update job number (+1)
        job_number += 2
        self.job_number.set(job_number)

        print(self.all_jobs_list)

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
                                         font="Arial 19 bold", padx=5, pady=5)
        self.suzy_mobile_heading.grid(row=0, pady=5)

        # all jobs list
        self.all_jobs_list = all_jobs_list

        # set displayed job as the first
        self.job = 0

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
        self.close_button.grid(row=1, column=0, padx=10, pady=10)

    def close_all_jobs(self, partner):
        partner.view_all_button.config(state=NORMAL)
        # close all jobs window
        self.all_jobs_box.destroy()


    def display_input(self, scroll):
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
