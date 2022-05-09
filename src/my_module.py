import re



def get_cheapest_hotel(number):   #DO NOT change the function's name

    #initialize the variables that will accumulate the money amount for every hotel

    lakewood = 0
    bridgewood = 0
    ridgewood = 0

    result = "" #result will store the value of the cheapest hotel in case there's no equal amount among the hotels.
  
    # The following function will get the lowest amount of money and return the corresponding string.

    def sort_cheapest(hotel1, hotel2, hotel3):

      cheapest_hotel = min(hotel1, hotel2, hotel3)
      cheapest_hotel_string = ""
  
      if cheapest_hotel == lakewood:
        cheapest_hotel_string = "Lakewood"
  
      elif cheapest_hotel == bridgewood:
        cheapest_hotel_string = "Bridgewood"
  
      else:
        cheapest_hotel_string = "Ridgewood"
  
      return cheapest_hotel_string

    # the following variable contains the split builtin function which splits the input by a space.
    input_separated_list = number.split(" ")

    #The following variable contains a regex in order to extract from the input the days of the week.
    input_separated_days = re.findall('\(([^)]+)', number)



    

    """The following is a series of conditionals and for loops in order to assign the right values to the declared variables
    according to the specified problem conditions"""
    
    if input_separated_list[0] == "Rewards:": 
      
      for x in input_separated_days:
        
        if x == "mon" or x == "tues" or x== "wed" or x== "thur" or x== "fri":

          lakewood += 80
          bridgewood += 110
          ridgewood += 100

        elif x == "sat" or x == "sun":

          lakewood += 80
          bridgewood += 50
          ridgewood += 40

    if input_separated_list[0] == "Regular:":

      for x in input_separated_days:

        if x == "mon" or x == "tues" or x== "wed" or x== "thur" or x== "fri":

          lakewood += 110
          bridgewood += 160
          ridgewood += 220

        elif x == "sat" or x == "sun":

          lakewood += 90
          bridgewood += 60
          ridgewood += 150

    if lakewood == bridgewood:
      cheapest_hotel = "Bridgewood"

    elif lakewood == ridgewood:
      cheapest_hotel = "Ridgewood"

  
    elif bridgewood == ridgewood:
      cheapest_hotel = "Ridgewood"
      
    elif bridgewood == ridgewood and lakewood == ridgewood and lakewood == bridgewood:
        cheapest_hotel = "Ridgewood"

    else:
       result = sort_cheapest(lakewood, bridgewood, ridgewood)
       cheapest_hotel = result
      
          
        






    
    
    
    return cheapest_hotel
    