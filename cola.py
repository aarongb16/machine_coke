amount_due = 50

while amount_due > 0 :
    print('amount dude:', amount_due)
    coin = int(input('insert coin:')) 
    if coin != 10 and coin != 25 and coin != 5:
        amount_due = amount_due + 0
    else:
        amount_due = amount_due - coin 
        if amount_due == 0: print('change: 0')
        elif amount_due < 0:
            print('change:', abs(amount_due))


    
# amount_due = 50

# while amount_due > 0:
#     coin = int(input('insert coin:'))
#     if coin != 25 and coin != 10 and coin != 5:
#         print('amount:due',amount_due)
#         coin = int(input('insert coin:'))
#     amount_due = amount_due - coin
#     print('amount dude:', amount_due)
#     if amount_due == 0:
#         print('change: ',amount_due)

