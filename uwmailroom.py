import os
import operator
from tabulate import tabulate


def main():
    while True:
        response = input("Please choose either 'Send a Thank You', 'Create a Report', or 'Quit'")
        
        response = response.lower()
        
        if response == "send a thank you":
            send_a_thank_you()
            

        elif response == "create a report":
            create_a_report()

        elif response == "quit":
            os._exit(0)
            

        else:
            print("idk")
            




class Donor:
    def __init__(self,name="",number_of_donations=0,donations_list=None):
        self.name = name
        self.number_of_donations = number_of_donations
        if donations_list is None:
            donations_list = []
        self.donations_list = donations_list
        total = 0
        for x in donations_list:
            total+= x
        self.total_contributed = total

    def donor_name(self):
        return(self.name)
    def donor_total(self):
        return(self.total_contributed)
    def donor_number_of_donations(self):
        return(self.number_of_donations)
    def donor_list_donations(self):
        return(self.donations_list)
    def donor_total_contributed(self):
        return(self.total_contributed)
    def donor_average_donation(self):
        return((self.total_contributed/self.number_of_donations))

    def add_donation(self,x):
        self.donations_list.append(x)
        self.total_contributed += int(x)

p1 = Donor("Ralphie Peterson",2,[350,75])
p2 = Donor("Kourtney Ruiz",1,[27])
p3 = Donor("Jarred Clarkson",3,[1000,500,500])
p4 = Donor("Celia Rawlings",1,[666])
p5 = Donor("Davey Cuevas",2,[314,117])
master_list = []
master_list.extend((p1,p2,p3,p4,p5))

def printout(x,y):
    print("Thank you {} for your generous donation of ${:,.2f} dollars. Your contribution to our endeavour will surely enable our enterprises.".format(x,y))

def thank_you_list():
    for _ in master_list:
        print(_.donor_name())




def send_a_thank_you():
    while True:
        response = input("Please enter a name or 'list' for a list of registered donors. You can also enter return or quit.  ")
        if response == "return":
            break
        if response == "quit":
            os._exit(0)
        if response == "list":
            thank_you_list()
            continue
        a = 0
        b = 0
        for i in master_list:
            if i.name == response:
                response2 = input("Please enter a donation amount ")
                i.add_donation(response2)
                printout(i.name,i.donations_list[-1])

                a = 1
                break
        if a == 0:
            while True:
                response2 = input("New donor, please add donation amount")
                try:
                    master_list.append(Donor(response,1,[float(response2)]))
                    printout(master_list[-1].name,master_list[-1].donations_list[-1])
                    b = 1
                    break 
                    
                except ValueError:
                    print("Please enter a number")
                    continue
                break
        if b == 1:
            break
        
def create_a_report():
    sorted_master_list = sorted(master_list,key=operator.attrgetter('total_contributed'),reverse=True)
    
    report_table = []
    
    for _ in sorted_master_list:
        report_table.append([_.donor_name(),_.donor_total(),_.donor_number_of_donations(),_.donor_average_donation()])

    print(tabulate(report_table,headers=["Donor Name","Total Given","Num Donations","Average Donation"],tablefmt="orgtbl"))        










if __name__ == "__main__":
    main()
