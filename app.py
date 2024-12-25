
while True:
    print('欢迎进入B站用户信息查询系统\n1.查询用户信息\n2.查询直播间状态\n3.查询舰队数据\n4.分析舰队数据\n5.退出')
    choice = input('请输入您的选择:')
    if choice == '1':
        from user import get_user_info
        uid = input('请输入用户UID:')
        user_info = get_user_info(uid)
        print(f"用户名: {user_info['用户名']}")
        print(f"性别: {user_info['性别']}")
        print(f"等级: {user_info['等级']}")
        print(f"VIP类型: {user_info['VIP类型']}")
        print(f"官方认证类型: {user_info['官方认证类型']}")
    elif choice == '2':
        from live_info import livedata
        room_id = input('请输入直播间ID:')
        livedata(room_id)
        
    elif choice == '3':
        from ship import shipdata
        room_id = input('请输入直播间ID:')
        ruid = input('请输入主播UID:')
        ship = shipdata(room_id, ruid)
    elif choice == '4':
         while True:
            choice = input('请选择分析类型\n0.返回上一级\n1.请输入文件名')
            
            if choice == '0':
                    break
                    
            elif choice == '1':
                    filename = input('请输入文件名:')
                    while True:
                        print('请选择分析类型\n0.返回上一级\n1.分析性别\n2.分析等级\n3.分析VIP类型\n4.分析官方认证类型\n5.分析陪伴天数\n6.分析粉丝牌等级')
                        choice = input('请输入您的选择:')
                        if choice == '1':
                            from countsex import countsex
                            
                            countsex(filename)
                        elif choice == '2':
                            from countLv import countLv
                        
                            countLv(filename)
                        elif choice == '3':
                            from countVIP import countVIP
                            
                            countVIP(filename)
                        elif choice == '4':
                            from countOfficial import countOfficial
                            
                            countOfficial(filename)
                        elif choice == '0':
                            break
                        elif choice == '5':
                            from countaccompany import countaccompany
                        
                            countaccompany(filename)
                        elif choice == '6':
                            from countfanlv import countfanlv
                            
                            countfanlv(filename)
                        else:
                            print('输入错误，请重新输入')
            else:
                print('输入错误，请重新输入')
    elif choice == '5':
        break
    else:
        print('输入错误，请重新输入')
        continue