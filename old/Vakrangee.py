while True:
    close = str((input('What is the closing price of vakrangee today?\n')))
    amt = float(input('Enter the amount'))
    if close == 'exit':
        break
    elif close != 'exit':
        close = float(close)
        low = close - (close*4.9)/100
        high = close + (close*4.97)/100
        change = (close*4.97)/100
        print(f'Tommorrow low will be {low}\nand high will be {high}\nand change is {change}\n\n')
        bsl =low + 0.1
        amount = amt - ((amt/bsl)*change)
        quantity = round(amount/bsl)
        ssl = close-0.5
        print(f'Put Buy stop loss at: {bsl}')
        print(f'put sell stopp loss at: {ssl}')
        print(f'Quantity You can buy: {quantity}')
        continue