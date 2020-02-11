def split(word): 
    return [char for char in word]
def convert(s):
    
    d = {}
    d[2] = ['A', 'B', 'C']
    d[3] = ['D', 'E', 'F']
    d[4] = ['G', 'H', 'I']
    d[5] = ['J', 'K', 'L']
    d[6] = ['M', 'N', 'O']
    d[7] = ['P', 'Q', 'R', 'S']
    d[8] = ['T', 'U', 'V']
    d[9] = ['W', 'X', 'Y', 'Z']
    con = ""
    for i in d.keys():
        if s in d[i]:
            s = i
    return str(s)

num = int(input())
n = 0
alpha = ["A", "B", "C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R", "S", "T", "U", "V","W","X","Y","Z"]
while n<num:
    phone = input().replace("-", "")

    for i in phone:
            phone = phone.replace(i, convert(i))

    n+=1
    print(phone[0:3] + "-"+phone[3:6]+"-"+phone[6:10])



