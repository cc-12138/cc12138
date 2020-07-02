import turtle as t
#计算应得工资
def total_money(h,m):
    all_money=0
    if(h<=40):
        all_money=m*h
        return all_money
    else:
        all_money=h*m*1.5-20
        return all_money
#打印支票题目，年月日以及银行等相关信息
def title():
    t.setup(width=600,height=300,startx=100,starty=100)
    t.penup()
    t.goto(-280,100)
    t.write('X X 银行 支票',move=False,align="left",font=("Arial",30,"normal"))
    t.goto(200,120)
    t.write('B G',move=False,align="left",font=("Arial",10,"normal"))
    t.goto(200,112)
    t.write('- -',move=False,align="left",font=("Arial",15,"normal"))
    t.goto(200,106)
    t.write('0  2',move=False,align="left",font=("Arial",10,"normal"))
    t.goto(-280,85)
    t.write('出票日期  X年  X月  X日      付款行名称：XX银行',move=False,align="left",font=("Arial",10,"normal"))
#打印收款人以及收款金额
def mainmassage(name,money):
    #打印姓名
    t.goto(-280,68)
    t.write('收款人：                       出票人姓名：XXX',move=False,align="left",font=("Arial",10,"normal"))
    t.goto(-215,68)
    t.write(name,move=False,align="left",font=("Arial",10,"normal"))
    #绘制金额外方框
    t.goto(-280,68)
    t.pendown()
    t.fd(540)
    t.right(90)
    t.fd(50)
    t.right(90)
    t.fd(540)
    t.right(90)
    t.fd(50)
    #绘制内方框
    t.penup()
    t.goto(-220,65)
    t.right(90)
    t.color("pink")
    t.begin_fill()
    t.pendown()
    t.fd(200)
    t.right(90)
    t.fd(30)
    t.right(90)
    t.fd(200)
    t.right(90)
    t.fd(30)
    t.end_fill()
    t.penup()
    t.color("black")
    #绘制金额表格
    t.right(180)
    num_list=["亿","仟","百","十","万","千","百","十","元","角"]
    for i in range(10):
        t.penup()
        t.goto(10+i*25,68)
        t.pendown()
        t.fd(25)
        t.write(num_list[i],move=False,align="left",font=("Arial",15,"normal"))
        t.fd(25)
    t.penup()
    t.goto(10,43)
    t.pendown()
    t.left(90)
    t.fd(252)
    #打印金额
    t.penup()
    t.goto(-280,40)
    t.write('人民币',move=False,align="left",font=("Arial",15,"normal"))
    t.goto(-220,40)
    t.write(money,move=False,align="left",font=("Arial",15,"normal"))
    m_str=str(money)
    for i in range(11-len(m_str)):
        t.goto(10+i*25,18)
        t.write("0",move=False,align="left",font=("Arial",15,"normal"))
    for i in range(11-len(m_str),9):
        t.goto(10+i*25,18)
        t.write(m_str[i+len(m_str)-11],move=False,align="left",font=("Arial",15,"normal"))
    t.goto(240,18)
    t.write(m_str[len(m_str)-1],move=False,align="left",font=("Arial",15,"normal"))
#打印结尾落款
def ending():
    t.goto(-280,0)
    t.write("用途：工资结算",move=False,align="left",font=("Arial",10,"normal"))
    t.goto(150,0)
    t.write("科目（借）：否",move=False,align="left",font=("Arial",10,"normal"))
    t.goto(-280,-15)
    t.write("上列款项请从",move=False,align="left",font=("Arial",10,"normal"))
    t.goto(150,-15)
    t.write("对方账目（贷）：否",move=False,align="left",font=("Arial",10,"normal"))
    t.goto(-280,-30)
    t.write("我账户内支付",move=False,align="left",font=("Arial",10,"normal"))
    t.goto(150,-30)
    t.write("复核          记账",move=False,align="left",font=("Arial",10,"normal"))
    t.goto(-280,-45)
    t.write("出票人盖章：",move=False,align="left",font=("Arial",10,"normal"))
#打印印章
def seal():
    t.goto(-145,-45)
    t.color("Red")
    t.begin_fill()
    t.pendown()
    for i in range(4):
        t.right(90)
        t.fd(80)
    t.end_fill()
    t.penup()
    t.goto(-150,-50)
    t.color("White")
    t.begin_fill()
    t.pendown()
    for i in range(4):
        t.right(90)
        t.fd(70)
    t.end_fill()
    t.penup()
    t.color("Red")
    t.goto(-220,-80)
    t.write("四川省",move=False,align="left",font=("Arial",18,"normal"))
    t.goto(-220,-100)
    t.write("X  X有",move=False,align="left",font=("Arial",18,"normal"))
    t.goto(-220,-120)
    t.write("限公司",move=False,align="left",font=("Arial",18,"normal"))
#主函数
if __name__ == "__main__":
    name=input("输入你的名字:")
    hour=input("输入你的工作时长:")
    money=input("输入每小时工资：")
    allmoney=total_money(int(hour),int(money))
    title()
    mainmassage(name,allmoney)
    ending()
    seal()
    t.mainloop()
