class Student(object):

    def __init__(self, name, score):
        self.name = name #可以把变量变成__name和__score这样就变成私有变量外部无法改变
        self.score = score

    def print_score(self):
        print('%s: %d' % (self.name, self.score)) 
Tom=Student('Tom',89)
Tom.print_score()

 #  def __init__(self, name, score):#括号里是三个形参，self必不可少，必须位于其他形参的前面。当py调用这个__init__()方法来创建实例时，将自动传入self，其本身是一个指向实例本身的引用，让实例能够访问类中的属性和方法。self会自动传递，我们不需要传递他，每当我们根据Student类创建实例时，只需要给最后两个形参（name和score）提供值
    #    self.name = name
     #   self.score = score
        #这定义的两个变量都有前缀self，以self为前缀的变量都可供类中的所有方法使用，我们可通过类中的任何实例来访问这些变量。self.name=name获取储存在形参name中的值，并将其储存到变量name中，然后该变量被关联到当前创建的实例。
        #类似上面这样通过实例访问的变量称为“属性”