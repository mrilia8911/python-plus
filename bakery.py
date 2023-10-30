print("barbary = 1$")
print("lavash = 2$")
print("sangak = 3$")
print("bugget = 4$")
print("konjedi = 5$")
one = 0
two = 0
three = 0
four = 0
five = 0

breadRoom ={
"barbary":1,
"lavash":2,
"sangak":3,
"bugget":4,
"konjedi":5
    }

print("do you want breads? yes or no?")
yn = input()
while yn == "yes" :
    print("wich?")
    wich = input()
    if wich == "barbary" :
        print("how many?")
        one = int(input())
        one = one*1
        print("do you want to buy more? yes or no?")
        yn = input()
    elif wich == "lavash" :
         print("how many?")
         two = int(input())
         two = two*2
         print("do you want to buy more? yes or no?")
         yn = input()
    elif wich == "sangak" :
             print("how many?")
             three = int(input())
             three = three*3
             print("do you want to buy more? yes or no?")
             yn = input()
    elif wich == "bugget" :
        print("how many?")
        four = int(input())
        four = four*4
        print("do you want to buy more? yes or no?")
        yn = input()
        
    elif wich == "sangak" :
        print("how many?")
        five = int(input())
        five = five*5
        print("do you want to buy more? yes or no?")
        yn = input()
        
    else :
        print("ok good bye")

print("your bill =",one+two+three+four+five,"$")
    
    
       
    


    


              
 
