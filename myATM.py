def startUp(f):
    """Read accounts from file and create dictionary with secret code as key and user info in a list as value.
       Returns True if successful, False otherwise, returns dictionary as well"""
    myDictionary = {}
    try:
        infile = open(f)
    except:
        print('We are very sorry. This ATM is current uder maintainance.\nPlease try later.')
        return (False, myDictionary)
    for line in infile:
        if len(line) > 1:
            lineList = line.split()
            myDictionary[lineList[0]] = lineList[1:3]+[ float(lineList[3])]#need to make sure the balance is a float
    infile.close()
    return (True, myDictionary)
    
 
def getUser(wish, myDictionary):
    """obtain secret code and validate account. Returns user name if successful and a boolean to indicate successful retrieval"""
    try:
        user = input('Welcome to the CSC401 Bank ATM\nPlease enter your secret code:\n')
        if len(user) == 4 and user in myDictionary:
            return (user, wish)
        else:
            print('Secret code incorrect. Goodbye.')
            return (None, False)
    except:
        print('Secret code incorrect. Goodbye.')
        return (None, False)

def menu(name):
    choices = [1,2,3,4]
    choice = 0
    while choice not in choices:
        try:
            choice = eval(input(80*'_' +'\n' + 80*'_' +'\n'+
                       'Welcome '+ name + '.\nPlease select your transaction:\n\t'+
                        '1: DEPOSIT\n\t'+
                        '2: WITHDRAW\n\t'+
                        '3: GET BALANCE\n\t'+
                        '4: QUIT\n'))
        except:
            continue
    return choice 

def deposit(balance):
    balance+= getAmount('deposit')
    print('Your transaction was successful')
    return balance

def withdraw(balance):
    amount = getAmount('withdraw')
    while  amount > balance:
        print('You do not have sufficient funds to complete this transaction.')
        amount = getAmount('withdraw')
    balance-=amount
    print('Your transaction was successful')
    return(balance)
        
    
def getAmount(mode):
    amountBad = True
    while amountBad:
        try:
            amount = float(input('\nPlease enter the amount you wish to '+ mode + ' :\n'))
            amountBad = False
        except:
            print('You entered an incorrect amount.\nPlease try again')
    return amount


def balance(name, balance):
    print(name +', your current balance is ${}'.format(balance))

def wrapUp(myDictionary, file):
    outfile = open(file, 'w')
    for key in myDictionary:
        outfile.write(key + ' ')
        for i in range (3):
            outfile.write(str(myDictionary[key][i] )+ ' ')
        outfile.write('\n')
    outfile.close()
    print(80*'_'+'\n'+
          80*'_' + '\n'+
          'Thank you for using the CSC241 Bank ATM.\nGoodbye')


userIntent = True
success, accts = startUp('accounts.txt')#reads file and sets up a dictionary of accounts,
#first item returned indicates succes in opening file to read accounts.
#secodn item returned is a dictionary with secret code (user) as key and a list as value.
# list contains [first name, last name, balance]
if success:
    user, userIntent = getUser(userIntent, accts)
    while userIntent:
        choice = menu(accts[user][0])
        if choice == 1:
            accts[user][2] = deposit(accts[user][2])
        elif choice == 2:
            accts[user][2] = withdraw(accts[user][2])
        elif choice == 3:
            balance(accts[user][0],accts[user][2])
        else:
            wrapUp(accts, 'accounts.txt')
            userIntent = False
