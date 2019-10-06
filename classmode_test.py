# class Document():
#     welcome_str='welcome the context for this book is {}.'
#     #构造函数，一个对象生成时会自动被调用的函数
#     def __init__(self,title,author,context):
#         print('init fun called')
#         self.title=title
#         self.author=author
#         self.__context=context
#     #类函数,实现不同的__init__的构造
#     @classmethod
#     def create_empty_book(cls,title,author):
#         return cls(title=title,author=author,context='nothing')
#
#     #静态函数
#     @staticmethod
#     def get_welcome(context):
#         return Document.welcome_str.format(context)
#
#     def get_context_length(self):
#         return len(self.__context)
#
#     def intercept_context(self,length):
#         self.__context=self.__context[:length]
#
# #对象
# # harry_potter_book=Document('Harry Potter','J.K.Rowling','...Forever Do not beleve anything is')
# # #属性
# # print(harry_potter_book.title)
# # print(harry_potter_book.author)
# # print(harry_potter_book.get_context_length())
# # harry_potter_book.intercept_context(10)
# # print(harry_potter_book.get_context_length())
# empty_book=Document.create_empty_book('what every man think','professor Sheridan Simove')
# print(empty_book.get_context_length())
# print(empty_book.get_welcome('indeed nothing'))
#
# class Entity():
#     def __init__(self,object_type):
#         self.object_type=object_type
#
#     def get_context_length(self):
#         raise Exception('get_context_length is not implemented')
#
#     def print(self):
#         print(self.title)
#
#
# class Document(Entity):
#     #构造函数，一个对象生成时会自动被调用的函数
#     def __init__(self,title,author,context):
#         print('Document init fun called')
#         Entity.__init__(self,'document')
#         self.title=title
#         self.author=author
#         self.__context=context
#
#     def get_context_length(self):
#         return len(self.__context)
#
# class Video(Entity):
#     #构造函数，一个对象生成时会自动被调用的函数
#     def __init__(self,title,author,video_length):
#         print('Video init fun called')
#         Entity.__init__(self,'document')
#         self.title=title
#         self.author=author
#         self.__video_length=video_length
#
#     def get_context_length(self):
#         return len(self.__video_length)
#抽象类 必须有子类才可以调用,用在多人大型开发任务中
from abc import ABCMeta,abstractmethod
class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass
    @abstractmethod
    def set_title(self):
        pass

class Document(Entity):
    def get_title(self):
        return self.title
    def set_title(self,title):
        self.title=title

document=Document()
document.set_title('harry potter')
print(document.get_title())

