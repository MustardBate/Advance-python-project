from tkinter import *
from tkinter import messagebox

class BateInternet:
    def __init__(self):
        self.root = Tk()
        self.root.title("B.A.T.E Internet")
        self.root.geometry("700x520")
        self.root.resizable(FALSE,FALSE)

        self.create_options_frame()
        self.create_buy_product_frame()
        self.create_mobile_frame()
        # Set current frame to mobile frame
        self.current_frame = self.mobile_frame

    # Function to create the menu selections
    def create_options_frame(self):
        self.options_frame = Frame(self.root, width=160, bg="light cyan")
        self.options_frame.pack(side=LEFT, fill="y")
        self.options_frame.pack_propagate(FALSE)
        self.title = Label(self.options_frame, text="---Menu Select---", font=("Bodoni",14,"bold"), bg="light cyan")
        self.title.place(x=2, y=10)

        # Creating buttons for the 3 options
        self.select_mobile_plans = Button(self.options_frame, text="Mobile Plans", font=("Bodoni",12,"bold"), bg="light cyan", width=14, height=2, command=self.go_to_mobile, state=DISABLED)
        self.select_mobile_plans.place(x=4, y=80)
        self.select_vps_packages = Button(self.options_frame, text="VPS Packages", font=("Bodoni",12,"bold"), bg="light cyan", width=14, height=2, command=self.go_to_vps)
        self.select_vps_packages.place(x=4, y=160)
        self.select_vpn_packages = Button(self.options_frame, text="VPN Packages", font=("Bodoni",12,"bold"), bg="light cyan", width=14, height=2, command=self.go_to_vpn)
        self.select_vpn_packages.place(x=4, y=240)
        self.select_domain = Button(self.options_frame, text="Domain", font=("Bodoni",12,"bold"), bg="light cyan", width=14, height=2, command=self.go_to_domain)
        self.select_domain.place(x=4, y=320)

        # Creating the return button
        self.return_button = Button(self.options_frame, text="Return", bg="light cyan", width=5, command=self.root.quit)
        self.return_button.place(x=55, y=480)


    # Creating a function for the purchase button
    def purchase_item(self):
        # MISSING CODE HERE, NEED TO ADD THE PURCHASE FUNCTIONALITY ASAP
        # Creating a messagebox to ask for user conformation
        # After confirming, the purchase will be made and the "Purchase" button will be disabled, replaced with "Purchased"
        return


    def go_to_mobile(self):
        # Disable the "Mobile Plans" button and enable the rest of the buttons
        self.select_mobile_plans.config(state=DISABLED)
        self.select_vps_packages.config(state=NORMAL)
        self.select_vpn_packages.config(state=NORMAL)
        self.select_domain.config(state=NORMAL)
        # Erasing the current frame
        self.current_frame.pack_forget()
        # Adding the Mobile Plans page
        self.create_mobile_frame()
        # Assigning current frame with mobile frame
        self.current_frame = self.mobile_frame
    

    def go_to_vps(self):
        # Disable the "VPS Packages" button and enable the rest of the buttons
        self.select_vps_packages.config(state=DISABLED)
        self.select_mobile_plans.config(state=NORMAL)
        self.select_vpn_packages.config(state=NORMAL)
        self.select_domain.config(state=NORMAL)
        # Erasing the current frame
        self.current_frame.pack_forget()
        # Adding the VPS Packages page
        self.create_vps_frame()
        # Assigning current frame with vps frame
        self.current_frame = self.vps_frame


    def go_to_vpn(self):
        # Disable the "VPN Packages" button and enable the rest of the buttons
        self.select_vpn_packages.config(state=DISABLED)
        self.select_mobile_plans.config(state=NORMAL)
        self.select_vps_packages.config(state=NORMAL)
        self.select_domain.config(state=NORMAL)
        # Erasing the current frame
        self.current_frame.pack_forget()
        # Creating a new frame for the VPN Packages page
        self.create_vpn_frame()
        # Assigning current frame with vpn frame
        self.current_frame = self.vpn_frame


    def go_to_domain(self):
        # Disable the "Domain" button and enable the rest of the buttons
        self.select_domain.config(state=DISABLED)
        self.select_mobile_plans.config(state=NORMAL)
        self.select_vps_packages.config(state=NORMAL)
        self.select_vpn_packages.config(state=NORMAL)
        # Erasing the current frame
        self.current_frame.pack_forget()
        # Creating a new frame for the Domain page
        self.create_domain_frame()
        # Assigning current frame with domain frame
        self.current_frame = self.domain_frame

    # Function to create the frame for the purchase page
    def create_buy_product_frame(self):
        self.buy_product_frame = Frame(self.root, width=540, bg="light blue")
        self.buy_product_frame.pack(side=LEFT, fill="y")
        self.buy_product_frame.pack_propagate(FALSE)


    # Function to create the frame for the Mobile Plans page
    def create_mobile_frame(self):
        # Creating the frame for the Mobile Plans page
        self.mobile_frame = Frame(self.buy_product_frame, bg="light blue", width=540)
        self.mobile_frame.pack(side=LEFT, fill="y")
        self.mobile_frame.pack_propagate(FALSE)
        self.mobile_title = Label(self.mobile_frame, text="---Mobile Plans---", font=("Bodoni",20,"bold"), bg="light blue").pack(pady=12)
        # Creating the items of Mobile Plans
        
        # Bronze Plan
        self.Mobile_Item1 = Frame(self.mobile_frame, width=180, height=132, bg="cyan")
        self.Mobile_Item1.place(x=30, y=100)
        self.Mobile_Item1.pack_propagate(FALSE)
        self.Mobile_Item1_title = Label(self.Mobile_Item1, text="Bronze", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.Mobile_Item1_text = Label(self.Mobile_Item1, text="30GB/month", font=("Helvetica",13,"italic"), bg="cyan").pack()
        self.Mobile_Item1_price = Label(self.Mobile_Item1, text="150,000 VND", font=("Helvetica",14,"italic","bold"), bg="cyan").pack()

        # Silver Plan
        self.Mobile_Item2 = Frame(self.mobile_frame, width=180, height=132, bg="cyan")
        self.Mobile_Item2.place(x=290, y=100)
        self.Mobile_Item2.pack_propagate(FALSE)
        self.Mobile_Item2_title = Label(self.Mobile_Item2, text="Silver", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.Mobile_Item2_text = Label(self.Mobile_Item2, text="50GB/month", font=("Helvetica",13,"italic"), bg="cyan").pack()
        self.Mobile_Item2_price = Label(self.Mobile_Item2, text="250,000 VND", font=("Helvetica",14,"italic","bold"), bg="cyan").pack()

        # Gold Plan
        self.Mobile_Item3 = Frame(self.mobile_frame, width=180, height=132, bg="cyan")
        self.Mobile_Item3.place(x=30, y=300)
        self.Mobile_Item3.pack_propagate(FALSE)
        self.Mobile_Item3_title = Label(self.Mobile_Item3, text="Gold", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.Mobile_Item3_text = Label(self.Mobile_Item3, text="100GB/month", font=("Helvetica",13,"italic"), bg="cyan").pack()
        self.Mobile_Item3_price = Label(self.Mobile_Item3, text="500,000 VND", font=("Helvetica",14,"italic","bold"), bg="cyan").pack()

        # Diamond Plan
        self.Mobile_Item4 = Frame(self.mobile_frame, width=180, height=132, bg="cyan")
        self.Mobile_Item4.place(x=290, y=300)
        self.Mobile_Item4.pack_propagate(FALSE)
        self.Mobile_Item4_title = Label(self.Mobile_Item4, text="Diamond", font=("Bodoni",15,"bold"), bg="cyan").pack()
        self.Mobile_Item4_text = Label(self.Mobile_Item4, text="500GB/month", font=("Helvetica",13,"italic"), bg="cyan").pack()
        self.Mobile_Item4_price = Label(self.Mobile_Item4, text="2,000,000 VND", font=("Helvetica",14,"italic","bold"), bg="cyan").pack()

        # Creating a button to purchase selected item
        for Mobile in [self.Mobile_Item1, self.Mobile_Item2, self.Mobile_Item3, self.Mobile_Item4]:
            self.purchase_button = Button(Mobile, text="Purchase", bg="light cyan", width=10, state="normal" ,command=self.purchase_item).place(x=50, y=90)


    # Function to create the frame for the VPS Packages page
    def create_vps_frame(self):
        self.vps_frame = Frame(self.buy_product_frame, bg="light blue", width=540)
        self.vps_frame.pack(side=LEFT, fill="y")
        self.vps_frame.pack_propagate(FALSE)
        self.vps_title = Label(self.vps_frame, text="---VPS Packages---", font=("Bodoni",20,"bold"), bg="light blue").pack(pady=12)
        # Creating the items of VPS Packages
        # Basic Package
        self.VPS_Item1 = Frame(self.vps_frame, width=180, height=132, bg="cyan")
        self.VPS_Item1.place(x=30, y=65)
        self.VPS_Item1.pack_propagate(FALSE)
        self.VPS_Item1_title = Label(self.VPS_Item1, text="Basic", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.VPS_Item1_text = Label(self.VPS_Item1, text="Ram: 01 GB\nHDD: 50 GB", font=("Helvetica",12,"italic"), bg="cyan").pack()
        self.VPS_Item1_price = Label(self.VPS_Item1, text="500,000 VND", font=("Helvetica",13,"bold","italic"), bg="cyan").pack()

        # Advanced Package
        self.VPS_Item2 = Frame(self.vps_frame, width=180, height=132, bg="cyan")
        self.VPS_Item2.place(x=290, y=65)
        self.VPS_Item2.pack_propagate(FALSE)
        self.VPS_Item2_title = Label(self.VPS_Item2, text="Advanced", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.VPS_Item2_text = Label(self.VPS_Item2, text="Ram: 02 GB\nHDD: 100 GB", font=("Helvetica",12,"italic"), bg="cyan").pack()
        self.VPS_Item2_price = Label(self.VPS_Item2, text="700,000 VND", font=("Helvetica",13,"bold","italic"), bg="cyan").pack()

        # High End Package
        self.VPS_Item3 = Frame(self.vps_frame, width=180, height=132, bg="cyan")
        self.VPS_Item3.place(x=30, y=215)
        self.VPS_Item3.pack_propagate(FALSE)
        self.VPS_Item3_title = Label(self.VPS_Item3, text="High End", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.VPS_Item3_text = Label(self.VPS_Item3, text="Ram: 04 GB\nHDD: 200 GB", font=("Helvetica",12,"italic"), bg="cyan").pack()
        self.VPS_Item3_price = Label(self.VPS_Item3, text="1,000,000 VND", font=("Helvetica",13,"bold","italic"), bg="cyan").pack()

        # VIP Package
        self.VPS_Item4 = Frame(self.vps_frame, width=180, height=132, bg="cyan")
        self.VPS_Item4.place(x=290, y=215)
        self.VPS_Item4.pack_propagate(FALSE)
        self.VPS_Item4_title = Label(self.VPS_Item4, text="VIP", font=("Bodoni",15,"bold"), bg="cyan").pack()
        self.VPS_Item4_text = Label(self.VPS_Item4, text="Ram: 08 GB\nHDD: 400 GB", font=("Helvetica",12,"italic"), bg="cyan").pack()
        self.VPS_Item4_price = Label(self.VPS_Item4, text="1,300,000 VND", font=("Helvetica",13,"bold","italic"), bg="cyan").pack()

        # VIP+ Package
        self.VPS_Item5 = Frame(self.vps_frame, width=180, height=132, bg="cyan")
        self.VPS_Item5.place(x=158, y=365)
        self.VPS_Item5.pack_propagate(FALSE)
        self.VPS_Item5_title = Label(self.VPS_Item5, text="VIP+", font=("Bodoni",15,"bold"), bg="cyan").pack()
        self.VPS_Item5_text = Label(self.VPS_Item5, text="Ram: 16 GB\nHDD: 800 GB", font=("Helvetica",12,"italic"), bg="cyan").pack()
        self.VPS_Item5_price = Label(self.VPS_Item5, text="1,600,000 VND", font=("Helvetica",13,"bold","italic"), bg="cyan").pack()

        # Creating a button to purchase selected item
        for VPS in [self.VPS_Item1, self.VPS_Item2, self.VPS_Item3, self.VPS_Item4, self.VPS_Item5]:
            self.purchase_button = Button(VPS, text="Purchase", bg="light cyan", width=10, state="normal" ,command=self.purchase_item).place(x=50, y=100)


    # Function to create the frame for the VPN Packages page
    def create_vpn_frame(self):
        self.vpn_frame = Frame(self.buy_product_frame, bg="light blue", width=540)
        self.vpn_frame.pack(side=LEFT, fill="y")
        self.vpn_frame.pack_propagate(FALSE)
        self.vpn_title = Label(self.vpn_frame, text="---VPN Packages---", font=("Bodoni",20,"bold"), bg="light blue").pack(pady=12)
        # Creating the items of VPN Packages
        # Basic Package
        self.VPN_Item1 = Frame(self.vpn_frame, width=180, height=132, bg="cyan")
        self.VPN_Item1.place(x=30, y=65)
        self.VPN_Item1.pack_propagate(FALSE)
        self.VPN_Item1_title = Label(self.VPN_Item1, text="Basic", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.VPN_Item1_text = Label(self.VPN_Item1, text="100,000 VND", font=("Helvetica",14,"italic","bold"), bg="cyan").pack(pady=22)

        # Advanced Package
        self.VPN_Item2 = Frame(self.vpn_frame, width=180, height=132, bg="cyan")
        self.VPN_Item2.place(x=290, y=65)
        self.VPN_Item2.pack_propagate(FALSE)
        self.VPN_Item2_title = Label(self.VPN_Item2, text="Advanced", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.VPN_Item2_text = Label(self.VPN_Item2, text="150,000 VND", font=("Helvetica",14,"italic","bold"), bg="cyan").pack(pady=22)

        # High End Package
        self.VPN_Item3 = Frame(self.vpn_frame, width=180, height=132, bg="cyan")
        self.VPN_Item3.place(x=30, y=215)
        self.VPN_Item3.pack_propagate(FALSE)
        self.VPN_Item3_title = Label(self.VPN_Item3, text="High End", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.VPN_Item3_text = Label(self.VPN_Item3, text="200,000 VND", font=("Helvetica",14,"italic","bold"), bg="cyan").pack(pady=22)

        # VIP Package
        self.VPN_Item4 = Frame(self.vpn_frame, width=180, height=132, bg="cyan")
        self.VPN_Item4.place(x=290, y=215)
        self.VPN_Item4.pack_propagate(FALSE)
        self.VPN_Item4_title = Label(self.VPN_Item4, text="VIP", font=("Bodoni",15,"bold"), bg="cyan").pack()
        self.VPN_Item4_text = Label(self.VPN_Item4, text="300,000 VND", font=("Helvetica",14,"italic","bold"), bg="cyan").pack(pady=22)

        # VIP+ Package
        self.VPN_Item5 = Frame(self.vpn_frame, width=180, height=132, bg="cyan")
        self.VPN_Item5.place(x=158, y=365)
        self.VPN_Item5.pack_propagate(FALSE)
        self.VPN_Item5_title = Label(self.VPN_Item5, text="VIP+", font=("Bodoni",15,"bold"), bg="cyan").pack()
        self.VPN_Item5_text = Label(self.VPN_Item5, text="500,000 VND", font=("Helvetica",14,"italic","bold"), bg="cyan").pack(pady=22)

        # Creating a button to purchase selected item
        for VPN in [self.VPN_Item1, self.VPN_Item2, self.VPN_Item3, self.VPN_Item4, self.VPN_Item5]:
            self.purchase_button = Button(VPN, text="Purchase", bg="light cyan", width=10, state="normal" ,command=self.purchase_item).place(x=50, y=90)


    # Function to create the frame for the Domain page
    def create_domain_frame(self):
        self.domain_frame = Frame(self.buy_product_frame, bg="light blue", width=540)
        self.domain_frame.pack(side=LEFT, fill="y")
        self.domain_frame.pack_propagate(FALSE)
        self.domain_title = Label(self.domain_frame, text="---Domain---", font=("Bodoni",22,"bold"), bg="light blue").pack(pady=4)

        # Creating the Domain Registration explanation frame
        self.domain_creation_note = Label(self.domain_frame, text="-Welcome to the Domain Registration Menu!-\nTo register a Domain, please enter your domain name (must be unique)\nand press the 'Register' button.\nThe price for one domain is:", font=("Helvetica",12,"italic"), bg="light blue").pack()
        self.domain_cost = Label(self.domain_frame, text="200,000 VND", font=("Helvetica",15,"bold","italic"), bg="light blue").pack()
        self.domain_creation_note2 = Label(self.domain_frame, text="You'll have: 1 newly registered Domain, 1 unique IP", font=("Helvetica",13,"italic"), bg="light blue").pack()
        self.text = Label(self.domain_frame, text="-----------------------------", font=("Helvetica",13,"bold"), bg="light blue").pack()

        # Creating the Domain creation frame
        self.domain_creation_frame = Frame(self.domain_frame, bg="cyan", width=420, height=240).pack(pady=40)
        self.domain_creation_title = Label(self.domain_creation_frame, text="Domain Registration", font=("Bodoni",14,"bold"), bg="cyan").pack()


    # Function to run the program
    def run(self):
        self.root.mainloop()



bate = BateInternet()
bate.run()