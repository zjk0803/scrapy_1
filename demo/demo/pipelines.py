import pymysql

#import sys
#import importlib
#importlib.reload(sys)
#sys.setdefaultencoding('utf-8')
class Pipeline(object):
    def open_spider(self,spider):
        print("opened")
        try:
            self.con = pymysql.connect(host = "127.0.0.1",port = 3306,user = "root",passwd = "123456",db = "MyDB")
            self.cursor = self.con.cursor(pymysql.cursors.DictCursor)
            self.cursor.execute("delete from PyTitle")
            self.opened = True
            self.count = 0
        except Exception as err:
            print(err)
            self.opened = False
    def close_spider(self,spider):
        if self.opened:
            self.con.commit()
            self.con.close()
            self.opened = False
        print("close")
        print("总共爬取",self.count,"个标题")
    def process_item(self,item,spider):
        try:
            print(item["id"])
            print(str(item["title"]))
            print(item["author"])
            print()
            if self.opened:
                self.cursor.execute("insert into PyTitle(id,title,author)values (%s，%s,%s)",(item["id"],item["title"],item["author"]))
                self.count += 1
        except Exception as err:
            print(err)
        return item


