import json
# import logg_proggram as lg

def change_details():
    name_search = input("\033[1mВведите имя контакта, который хотите изменить:\033[0m ")
    sur_name_search = input("\033[1mВведите имя контакта, который хотите изменить:\033[0m ")
    with open('BD.json', encoding='utf8') as openfile:
        data = json.load(openfile)
        # lg.logging.info('Open file')

    for i in data["phone_book"]:
        if i["name"] == name_search and i["surname"] == sur_name_search:
            print(f'name: {i["name"]} {i["surname"]}')
            
            print(f'phone: {i["phone"]}')
            print(f'mail: {i["E-mail"]}')
            
            number = i["phone"]
            email = i["E-mail"]
            surname = i["surname"]
            print("\033[1mкакие данный хотите изменить?\033[0m(ФИО, номер, почту): ")
            answer = int(input("\033[1m1 - ФИО, 2 - номер, почту - 3, 0 - выход в меню:\033[0m "))
            if answer == 0:
                        print("\033[1mвыходим в меню\033[0m")
            if answer == 1:
                answer_name = int(input("1 - имя, 2 - фамилию: "))
                if answer_name == 1:
                    change_name = input(f"\033[1mМеняем имя {name_search} на:\033[0m ")
                    i["name"] = change_name
                    # lg.logging.info('Change name')
                    print("Имя изменено")
                elif answer_name == 2:
                    change_name = input(f"Меняем фамилию {surname} на: ")
                    i["surname"] = change_name
                    # lg.logging.info('Change surname')
                    print("Фамилия изменена")
            elif answer == 2:
                change_phone = input(f"Меняем номер {number} на: ")
                i["phone"] = change_phone
                # lg.logging.info('Change phone number')
                print(f'Теперь номер контакта {i["name"]}: {i["phone"]}')
            elif answer == 3:
                change_email = input(f"Меняем почту контакта {name_search} {surname} с почтой {email} на: ")
                i["E-mail"] = change_email
                # lg.logging.info('Change E-mail')
        else:
            continue
            # i = i + 1
    with open('BD.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)
        # lg.logging.info('Data recording')

