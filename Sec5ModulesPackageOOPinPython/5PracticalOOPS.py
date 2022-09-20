class Shortner:
    def __init__(self,item):
        self.original_items = item

    def printOriginalItems(self):
        print(self.original_items)

class ListAndCharShortner(Shortner):
    def printShortendItems(self):
        print(self.original_items[0:3])

class DictionaryShortner(Shortner):
    def printShortendItems(self):
        dic = self.original_items
        counter = 0
        # for item in dic:
        #     print(item)
        #     counter += 1
        # print(counter)
        res_dic = {}
        for (k,v) in dic.items():
            if counter<3:
                counter +=1
                res_dic.update({k:v})
        print(res_dic)

short = ListAndCharShortner("This is my Mohammad")
short.printShortendItems()

# Also the subclass will have the access to baseclass methods
short.printOriginalItems()

org_items = {1: 'Mohammad',2:'Surayj',3:'Yaseen',4: "Khadar", 5: "Jani"}
shortDic = DictionaryShortner(org_items)
shortDic.printShortendItems()
shortDic.printOriginalItems()