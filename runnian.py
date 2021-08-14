year_str = input("请输入要判断的年份：")

year = int(year_str)

if year % 4 == 0 and year % 100 != 0:
    print(str(year) + "是闰年")
else:
    print(str(year) + "不是闰年")

    
        
    
    
