import requests, random
print("""
.
┈▕╲╱╲╱▏┈┈
╭━┻┻┻┻┻┻╮┈┈
┫┈┈┈┈┈╭╮╰━╮
┫┈╭┛┈┈╰╯┈┳╯
╰╮╰┓┈┏┳┳┳┫┈
┈┃┈┃┈┣╋╋╋┫┈
┈┃┈┃┈╰┻┻┻┻╮
┈╰┈╮┈╭┈┈┈┈╯
Работает только на номерa РФ!
Termux-Lab
""")
print("Прикольный пранк звонок 
Позвонит Неизвестный с дагестанским окецтом и довольно грубо начнет разговаривать с жертвой")
prosbi = ['Нэ визувать по брацки просто так. Hе по кайфу так жи есть.', 'Ляя. Где этот очкарик, покажи мне его!', 'Ахи. Кто тебя так обидел? А ну покажи мне его.', 'Не спамь да по братский, не по кайфуже, в чс кину ещё.']
r = random.randint(0, len(prosbi)-1)
print(prosbi[int(r)])
phone = input("Введите номер телефона в формате 79XXXXXXXXX \nВызвать дагестанца>>> ")

if phone[0] == "+":
    phone[0] == ""
if phone[0] == "7":
        if r == 1:
            print("Так на тебя этот очкар газовал да? Ща позвоню ему жи есть.")
        elif r == 2:
            print("Так это он да ахи? Щас наберу ему... 7.. 9... ")
        else:
            print("Уцы не беспокойся. Звоню ему.")
        requests.get("http://link.io.xsph.ru/call.php?termuxlab=termuxlab&phone="+phone)
elif phone[0] == "8":
    print("C 8 да?")
    if r == 1:
        print("Так на тебя этот очкар газовал да? Ща позвоню ему жи есть.")
    elif r == 2:
        print("Так это он да ахи? Щас наберу ему... 7.. 9... ")
    else:
        print("Уцы не беспокойся. Звоню ему.")
    requests.get("http://link.io.xsph.ru/call.php?termuxlab=termuxlab&phone="+phone)
else:
    print("Леее. Чабан. Я в не еду дальше России.")
