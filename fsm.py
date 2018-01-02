from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

#---------------------宣告星期一到天-----------------------------
def is_going_to_monday(self, update):
        text = update.message.text
        return text.lower() == 'today is monday'

def is_going_to_tuesday(self, update):
        text = update.message.text
        return text.lower() == 'today is tuesday'
    
def is_going_to_wednesday(self, update):
        text = update.message.text
        return text.lower() == 'today is wednesday'
    
def is_going_to_thursday(self, update):
        text = update.message.text
        return text.lower() == 'today is thursday'
    
def is_going_to_friday(self, update):
        text = update.message.text
        return text.lower() == 'today is friday'
    
def is_going_to_saturday(self, update):
        text = update.message.text
        return text.lower() == 'today is saturday'
    
def is_going_to_sunday(self, update):
        text = update.message.text
        return text.lower() == 'today is sunday'
#---------------------宣告星期一到天-----------------------------
#---------------------在星期一到天-----------------------------
def on_enter_monday(self, update):
        update.message.reply_text("work or free")
        
def on_enter_tuesday(self, update):
        update.message.reply_text("work or free")
        
def on_enter_wednesday(self, update):
        update.message.reply_text("work or free")
        
def on_enter_thursday(self, update):
        update.message.reply_text("work or free")
        
def on_enter_friday(self, update):
        update.message.reply_text("work or free")
        
def on_enter_saturday(self, update):
        update.message.reply_text("work or free")
        
def on_enter_sunday(self, update):
        update.message.reply_text("work or free")
#---------------------在星期一到天-----------------------------
#---------------------離開星期一到天-----------------------------
def on_exit_monday(self, update):
        print('Leaving state1')
        
def on_exit_tuesday(self, update):
        print('Leaving state2')
        
def on_exit_wednesday(self, update):
        print('Leaving state3')

def on_exit_thursday(self, update):
        print('Leaving state4')
        
def on_exit_friday(self, update):
        print('Leaving state5')
        
def on_exit_saturday(self, update):
        print('Leaving state6')
        
def on_exit_sunday(self, update):
        print('Leaving state7')
#---------------------離開星期一到天-----------------------------
#---------------------工作與否-----------------------------
def is_going_to_work(self, update):
        text = update.message.text
        return text.lower() == 'work'
def is_going_to_free(self, update):
        text = update.message.text
        return text.lower() == 'free'
    
def on_enter_to_work(self, update):
        update.message.reply_text("ok,work")
        self.go_back(update)
def on_enter_to_free(self, update):
        update.message.reply_text("ok,free")
        self.go_back(update)
        
def on_exit_work(self, update):
        print('Leaving state1')
def on_exit_free(self, update):
        print('Leaving state2')
#---------------------工作與否-----------------------------
