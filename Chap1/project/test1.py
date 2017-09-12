# 先把weather_info.txt这个文档进行拆解，变成相互独立的一对对值

weather_dic = {}

# open 里面的文档需要打上引号，with *** as ***语句后需要加：
with open('weather_info.txt') as file:
    balala = file.readlines()
    
    # ！忘记了循环语句，没有办法穷举文档中的内容
    for line in balala:
        # ！split语句的标准写法还是没有搞清楚
        a = line.split(',')[0]
        b = line.split(',')[1].rstrip('\n')
    
        weather_dic[a] = b
        
# ！忘记关掉文档       
file.closed
    
user_weather_dic = {}
    
while True:
    print ("欢迎使用天气通软件，请键入城市查询天气，如需帮助请键入help")
    user_city = input(">>>")
    
    #if user_city in a:
    if user_city in weather_dic:
        
        #weather_dic[user_city] = user_weather
        user_weather = weather_dic[user_city]
        print(user_city + "的天气是：" + user_weather)
        
        #忘记写user_weather_dict的赋值语句
        user_weather_dic[user_city] = user_weather
        
    elif user_city == "history":
        # !忘记打引导词
        print ("这是你的搜索记录：")
        
        #user_weather_dic[user_city] = user_weather
        for user_city in user_weather_dic:       
        #print(user_city, user_weather_dic[user_city])
            print(user_city, user_weather_dic[user_city])    
              
    elif user_city == "help":
        print(
            '''
            如需查询天气，请直接输入城市，
            如需帮助，请键入help，
            如需查询历史记录，请键入history，
            如需退出程序，请键入quit。
            ''')
              
    elif user_city == "quit":
        break
              
    else:
        print("输入有误，请重新输入")
              
              
              
              