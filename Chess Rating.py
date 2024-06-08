# -*- coding: utf-8 -*-
"""

Chess Rating 

Created on Sat Jun  8 02:11:13 2024

@author: Lenovo
"""

Players = { 
    "Player A": 1400,
    "Player B": 1400

               
    }


#Simulate the match

"""

Mafeeesh OD. ma nos w nossss
"""

def Simulate_Match ():
    
    result = input("Wnter the Winner (A/B) or 'draw':").strip().lower()
    
    if result == 'a':
         OA, OB= 1, 0
    elif result == 'b': 
        OA, OB = 0, 1
    elif result == 'draw':
        OA, OB = 0.5, 0.5
    else: 
        print("invalid")
        return Simulate_Match()
    return OA, OB
    
         
    
# OA = Simulate_Match['OA']
# OB = Simulate_Match['OB']
# OD = Simulate_Match['OD']

# Calculate Expected Scores
#RA′​=RA​+K×(SA​−EA​)


def Expected_Score (Ra, Rb):

    return  1/(1+10**((Rb-Ra)/400))

def Rating_Update (Ra, Rb, OA, OB, K=32):
  
      exp_a = Expected_Score(Ra, Rb)
      new_rating_a = Ra + K * (OA - exp_a)
      
      exp_b = Expected_Score(Rb, Ra)
      new_rating_b = Rb + K * (OB - exp_b)
  
      return new_rating_a, new_rating_b
  
    
def main():
    players = { 
        "Player A": 1400,
        "Player B": 1400
    }
    
    while True:
        OA, OB = Simulate_Match()
        
        Ra = players["Player A"]
        Rb = players["Player B"]
        
        new_Ra, new_Rb = Rating_Update(Ra, Rb, OA, OB)
        
        players["Player A"] = new_Ra
        players["Player B"] = new_Rb
        
        print(f"Updated Ratings:\nPlayer A: {new_Ra}\nPlayer B: {new_Rb}")
        
        another_match = input("Do you want to simulate another match? (yes/no): ").strip().lower()
        if another_match != 'yes':
            break

# Call the main function to start the program
main()

    