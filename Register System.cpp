/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <bits/stdc++.h> 
#include <cctype>
using namespace std;

void NewRegister();
bool validEmail(string);
bool validFirst(string);
bool validLast(string);
bool validPass(string);
//void verificationCode();
//void login();



int main()
{
    cout<<"Hello " << endl;
    cout << "Welcome to the website" << endl;
    cout << "Let our Journey begin..." << endl;
    
    NewRegister();

    return 0;
}



void NewRegister() {
    string NewRegister, Username, Password, firstname, lastname, email;
    
    cout << "New register? \n (Note: if you are a new user type Yes, else type No) \n" ;
    cin >> NewRegister;
    cin.ignore();
    
         if (NewRegister == "Yes" || NewRegister == "yes"){
             
            cout << "firstname:";
            cin >> firstname;
            
                while (validFirst (firstname) == false){
                    cout << "Invalid firstname";
                    cin >> firstname;
                }
            
             
            cout << " Valid First Name." <<endl;
     
            //---------------------------------//
            
            cout << "lastname:";
            cin >> lastname;
            
                while (validLast (lastname) == false){
                    cout << "Invalid lastname";
                    cin >> lastname;
                }
            
             
            cout << " Valid Last Name." <<endl;
           
            
            // --------------------------------- //
            
              
            cout << "email:";
            cin >> email;
            
                while (validEmail (email) == false){
                    cout << "Invalid email";
                    cin >> email;
                }
            
             
            cout << " Valid email Name." <<endl;
           
            
            //---------------------------------//
            
            
             cout << "Password: \n (Note:: your password must be at least one digit,one special character, one uppercase letter, and one lowercase letter) \n"; // enter password
             cin >> Password;
         
            
                while (validPass (Password) == false){
                    cout << "Invalid Password";
                    cin >> Password;
                }
            
             
            cout << " Valid Password." <<endl;
          
              cout << "Registration completed! \n" << endl;
            
           
         }
        //-------------------------------------------------------//
        
        else if (NewRegister == "no" || NewRegister == "No")
        {
            string Username, Password;
            
            cout << endl << "  Login  " << endl <<endl;
            
            cout << "Enter your username" << endl;
            getline(cin, Username);
            
              cout << "Enter your password :" << endl;
              cin >> Password;

             cout << endl
            << "Login success!" << endl;
        }
        
         
}

bool validFirst(string firstname) 
{
    // Start a range-based for loop to iterate over each character in the string lastname
    for (char c : firstname) 
    {
        // Check if the current character is not a letter
        if (!isalpha(c)) 
        {
            // If any character is not a letter, return false
            return false;
        }
    }
    // If all characters are letters, return true
    return true;
}

bool validLast(string lastname) 
{
    // Start a range-based for loop to iterate over each character in the string lastname
    for (char c : lastname) 
    {
        // Check if the current character is not a letter
        if (!isalpha(c)) 
        {
            // If any character is not a letter, return false
            return false;
        }
    }
    // If all characters are letters, return true
    return true;

}


bool validPass (string Password)
{
    int digit = 0, uppercase = 0, specialC = 0, lowercase = 0;
        if (Password.length() >= 8)
        {
            if (Password.find(" ") == std::string::npos)
            {
                for (int i = 0; i < Password.length(); i++)
                {
                    if (Password[i] >= '0' && Password[i] <='9')
                    {
                        ++digit;
                    }
                    
                    else if (Password[i]>= 'a' && Password[i] <= 'z')
                    {
                        ++lowercase;
                    }
                    else if (Password[i]>= 'A' && Password[i] <= 'Z')
                    {
                        ++uppercase;
                    }
                    else if (Password[i] == '@' || Password[i] == '!' || Password[i] == '_' )
                    {
                        ++specialC;
                    }
                    
                }
            }
           
        }
    
    
     return (digit > 0 && lowercase > 0 && uppercase > 0 && specialC > 0);
    
}

bool validEmail(string email) {
    // Simple email validation
    size_t atPos = email.find('@');
    size_t dotPos = email.find('.', atPos);
    return atPos != string::npos && dotPos != string::npos && atPos < dotPos;
}

