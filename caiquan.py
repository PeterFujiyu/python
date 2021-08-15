while True:
    player = input("请出拳(石头/剪刀/布)")
    print("玩家出拳："+player)
    import random
    list = ["石头","剪刀","布"]
    computer = random.choice(list)
    print("计算机出拳："+computer)
    if player in list:
        if player == computer:
            print("平局了")
        elif  (player=="石头" and computer=="剪刀") or (player=="布" and computer=="石头") or (player=="剪刀" and computer=="布"):
            print("恭喜你，你赢了")
        else:
            print("你输了，再接再厉")
    else:
        print("输入错误")



    

