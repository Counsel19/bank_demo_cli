def checkIfUserExists(account_number, user_list):
    user_found = {}
   
    for user in user_list:
        if user["account_number"] == account_number:
            user_found = user
            break  
    return user_found       


def checkIfAmtIsAvailable(user, amount):
    isAmtAvailable = False

    if(int(user["current_balance"]) > int(amount)):
        isAmtAvailable = True
        
    return isAmtAvailable
    