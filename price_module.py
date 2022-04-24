class Pricing_module:
    def __init__(self):
        self.current_price = 1.5 # default price that the distrivutor gets from refinery
        self.company_profit_factor = 0.1 # for the company profit factors which is always 10%
        self.price_p_gallon = 0 # default value


    def calcPrice(self, location, hist, gal_requested):
        location_factor = 0
        gal_req_factor = 0

        if location.lower() == 'tx': # set the default loction factor for the price at 4% for texas
            location_factor = 0.02

        if location.lower() != 'tx': # if the customer is located in a different place other than tx charge at 4%
            location_factor = 0.04

        hist_factor = 0 # rate history factor on default is zero

        if hist == 'yes': # sets the value to 0.01/1% if the customer has ordered before
            hist_factor = 0.01

        if gal_requested<1000:
            gal_req_factor = 0.03# set the gallons requested to 3% and since most users are less than a 1000 this is the defaut value

        if gal_requested > 1000: # if the value is greater than 1000 set it to 2 percent
            gal_req_factor = 0.02

        margin = self.current_price * (location_factor - hist_factor + \
                gal_req_factor + self.company_profit_factor) # given formula for calulating the margin

        self.price_p_gallon = self.current_price + margin # the total price is current+margin

        return self.price_p_gallon
