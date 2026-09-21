
from time import sleep
import random
import peremens as gs

def location1():
    print("\n1 - заглянуть под камень")
    print("2 - добыть камень")
    print("3 - полежать на камне")
    print("4 - вернуться назад")
    gs.answer = input()

    if gs.answer == "1":
        if gs.flag_kitchen == 0:
            gs.qcoins = random.randint(5, 20)
            print(f"Под камнем лежит кирка и {gs.qcoins} монет")
            gs.coins += gs.qcoins
            gs.inventory.append("кирка")
            gs.flag_kitchen = 1
            print(f"У вас теперь {gs.coins} монет")
        else:
            print("Вы уже заглядывали под этот камень, там ничего нет")
        location1()

    elif gs.answer == "2":
        if "кирка" in gs.inventory:
            if gs.flag_kitchen == 1:
                gs.qcoins = random.randint(20, 50)
                print(f"Вы нашли тайник! В нём алмаз и {gs.qcoins} монет")
                gs.coins += gs.qcoins
                gs.inventory.append("алмаз")
                gs.flag_kitchen = 2
                print(f"У вас теперь {gs.coins} монет")
            else:
                print("В тайнике уже ничего нет")
        else:
            print("Вы сломали себе палец и выбились из сил")
        location1()

    elif gs.answer == "3":
        if random.random() < 0.4:
            print("Что-то коснулось вашей ноги. Это пауки")
            sleep(2)
            print("Следовать за пауками?")
            gs.answer = input()
            if gs.answer.lower() == "да":
                print("Паук привёл вас к маленькой щели")
                if gs.flag_kitchen < 3:
                    print("В ней лежит сокровище! Вы нашли рубин!")
                    gs.inventory.append("рубин")
                    gs.flag_kitchen = 3
                else:
                    print("В щели уже ничего нет")
            else:
                print("Вы остались на месте")
            location1()
        else:
            print("вы полежали и отдохнули")
            location1()
    elif gs.answer == "4":
        from hub import hub
        hub()
    else:
        print("Неверный ввод")
        location1()

def location2():
    print("\n1 - идти по тропинке")
    print("2 - свернуть в чащу")
    print("3 - прислушаться")
    print("4 - вернуться назад")
    gs.answer = input()

    if gs.answer == "1":
        if gs.flag_hut == 0:
            print("Вы нашли старую хижину")
            print("Внутри лежит сундук с 30 монетами")
            gs.coins += 30
            gs.inventory.append("ключ")
            gs.flag_hut = 1
            print(f"У вас теперь {gs.coins} монет")
        else:
            print("Вы уже были в этой хижине, там пусто")
        location2()

    elif gs.answer == "2":
        if random.random() < 0.5:
            print("Вы наткнулись на волков! Быстро убегайте!")
            sleep(2)
            if random.random() < 0.1:
                print("вы чудом убежали")
                location2()
            else:
                print("вы чпокнулись")
                print("вы проиграли")
                quit()
        else:
            if gs.flag_hut < 2:
                print("Вы нашли поляну с грибами")
                print("Вы собрали 15 монет")
                gs.coins += 15
                gs.flag_hut = 2
            else:
                print("Вы уже собирали грибы на этой поляне")
        print(f"У вас теперь {gs.coins} монет")
        location2()

    elif gs.answer == "3":
        if gs.flag_waterfall == 0:
            print("Вы слышите шум воды неподалёку")
            print("Это ведёт к водопаду, где спрятан клад!")
            print("Вы нашли золотой слиток!")
            gs.inventory.append("золотой слиток")
            gs.flag_waterfall = 1
        else:
            print("Вы уже нашли клад у водопада")
        location2()

    elif gs.answer == "4":
        from hub import hub
        hub()
    else:
        print("Неверный ввод")
        location2()

def location3():
    print("\n1 - войти внутрь мельницы")
    print("2 - осмотреть снаружи")
    print("3 - заглянуть под колесо")
    print("4 - вернуться назад")
    gs.answer = input()

    if gs.answer == "1":
        print("Внутри темно и пыльно")
        if gs.flag_mill_inside == 0:
            if "ключ" in gs.inventory:
                print("Вы открыли старый сундук ключом!")
                print("Внутри 50 монет и древний амулет!")
                gs.coins += 50
                gs.inventory.append("амулет")
            else:
                print("Внутри ничего интересного")
            gs.flag_mill_inside = 1
        else:
            print("Вы уже осмотрели всё внутри")
        print(f"У вас теперь {gs.coins} монет")
        location3()

    elif gs.answer == "2":
        if gs.flag_mill_outside == 0:
            print("Снаружи вы нашли тайник под крыльцом")
            print("В нём 25 монет")
            gs.coins += 25
            gs.flag_mill_outside = 1
        else:
            print("Вы уже осмотрели всё снаружи")
        print(f"У вас теперь {gs.coins} монет")
        location3()

    elif gs.answer == "3":
        if gs.flag_mill_wheel == 0:
            print("Под колесом вы нашли старую монету")
            gs.coins += 5
            gs.flag_mill_wheel = 1
        else:
            print("Под колесом уже ничего нет")
        print(f"У вас теперь {gs.coins} монет")
        location3()

    elif gs.answer == "4":
        from hub import hub
        hub()
    else:
        print("Неверный ввод")
        location3()

def location4():
    print("\n1 - пойти налево")
    print("2 - пойти направо")
    print("3 - пойти прямо")
    print("4 - вернуться назад")
    gs.answer = input()

    if gs.answer == "1":
        if gs.flag_dungeon_left == 0:
            print("Вы нашли комнату с сокровищами!")
            gs.coins += 40
            gs.inventory.append("бриллиант")
            gs.flag_dungeon_left = 1
        else:
            print("В этой комнате уже всё забрали")
        print(f"У вас теперь {gs.coins} монет")
        location4()

    elif gs.answer == "2":
        print("Вы попали в ловушку!")
        print("Потеряно 15 монет и вы сломали факел")
        gs.coins = max(0, gs.coins - 15)
        print(f"У вас теперь {gs.coins} монет")
        location4()

    elif gs.answer == "3":
        if gs.flag_dungeon_straight == 0:
            print("Вы нашли выход из подземелья")
            print("Перед вами сундук с 60 монетами!")
            gs.coins += 60
            gs.flag_dungeon_straight = 1
        else:
            print("Сундук уже пуст")
        print(f"У вас теперь {gs.coins} монет")
        location4()

    elif gs.answer == "4":
        from hub import hub
        hub()
    else:
        print("Неверный ввод")
        location4()

def location5():
    print("\n1 - искупаться")
    print("2 - порыбачить")
    print("3 - поискать на берегу")
    print("4 - вернуться назад")
    gs.answer = input()

    if gs.answer == "1":
        if gs.flag_lake_swim == 0:
            print("В воде вы нашли жемчужину!")
            gs.inventory.append("жемчужина")
            gs.coins += 20
            gs.flag_lake_swim = 1
        else:
            print("Вы уже нашли жемчужину в этом озере")
        location5()

    elif gs.answer == "2":
        if random.random() < 0.4:
            print("Вы поймали золотую рыбку!")
            print("Она дала вам 35 монет")
            gs.coins += 35
        else:
            print("Вы поймали старый ботинок...")
        location5()

    elif gs.answer == "3":
        if gs.flag_lake_shore == 0:
            print("На берегу вы нашли клад!")
            gs.coins += 45
            gs.inventory.append("коралл")
            gs.flag_lake_shore = 1
        else:
            print("На берегу уже всё обыскано")
        print(f"У вас теперь {gs.coins} монет")
        location5()

    elif gs.answer == "4":
        from hub import hub
        hub()
    else:
        print("Неверный ввод")
        location5()

def hamam():
    print("в хамаме вас встречает Меллстрой")
    sleep(2)
    print("Попросить у меллстроя денег?")
    gs.answer = input()
    if gs.answer == "да":
        print("вы просите у Меллстроя денег")
        if gs.kotost == 0:
            print("Меллстрой говорит: Ну Братан...")
            sleep(1)
            print("я могу дать тебе денег, но для этого ты должен найти котость")
            print("отправляйся в зачекшье и найди её")
            print("отправться в зачекушье?")
            gs.answer = input()
            if gs.answer == "да":
                print("Перемещаемся в Зачекушье")
                print("вы оказались в зачекушье")
                sleep(1)
                print("перед вами стоит чекушка")
                sleep(1)
                zachekushe()
            elif gs.answer == "нет":
                print("вы вернулись назад")
                from hub import hub
                hub()
        elif gs.kotost == 1:
            print("ты уже получил свои деньги")
    elif gs.answer == "нет":
        print("Меллстрой говорить: Ну ещё посидим, ещё посидим")
        from hub import hub
        hub()
    else:
        print("некоректный ввод")
        hamam()

def zachekushe():
    print("Будешь ловить котость?")
    gs.answer = input()
    if gs.answer == "да":
        print("вы ловите котость")
        sleep(0.5)
        if random.random() < 0.001:
            print("ВЫ ПОЙМАЛИ КОТОСТЬ!!!")
            print("возвращаемся к меллстрою")
            sleep(2)
            print("Вас вчречает меллстрой в хамаме")
            print("Ого ты реально поймал котость")
            sleep(1)
            print("держи твой 1000000")
            gs.coins += 1000000
            gs.kotost = 1
            from hub import hub
            hub()
        else:
            print("котость ускользнула")
            zachekushe()
    elif gs.answer == "нет":
        print("вы вернулись к меллстрою")
        print("мелстрой говорит: эх жаль что ты не поймал её")
        from hub import hub
        hub()
    else:
        print("Некоректный ввод")
        zachekushe()

def trader():
    print(f"ваш инвентарь: {gs.inventory}")
    print("\nСкупщик может обменять ваши сокровища на монеты:")
    print("1 - алмаз (50 монет)")
    print("2 - рубин (40 монет)")
    print("3 - золотой слиток (30 монет)")
    print("4 - амулет (20 монет)")
    print("5 - жемчужина (25 монет)")
    print("6 - бриллиант (60 монет)")
    print("7 - коралл (15 монет)")
    print("8 - уйти")
    gs.answer = input()

    items_prices = {
        "1": ("алмаз", 50),
        "2": ("рубин", 40),
        "3": ("золотой слиток", 30),
        "4": ("амулет", 20),
        "5": ("жемчужина", 25),
        "6": ("бриллиант", 60),
        "7": ("коралл", 15)
    }

    if gs.answer in items_prices:
        item, price = items_prices[gs.answer]
        if item in gs.inventory:
            gs.inventory.remove(item)
            gs.coins += price
            print(f"Вы продали {item} за {price} монет!")
            print(f"У вас теперь {gs.coins} монет")
        else:
            print(f"У вас нет {item}!")
        trader()
    elif gs.answer == "8":
        from hub import hub
        hub()
    else:
        print("Неверный ввод")
        trader()

def boss():
    print("\nВы попали в тронный зал к королю")
    sleep(2)
    price = random.randint(500, 600)
    print(f"Король требует плату в {price} монет")
    if gs.coins >= price:
        print(f"Вы заплатили королю {price} монет")
        sleep(1)
        print("Игра пройдена!")
    else:
        print("У вас недостаточно монет")
        sleep(4)
        print("Король скидывает вас в бездну. Вы проиграли :(")