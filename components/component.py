class Component(object):
   __name: str
   __desc: str
   __type: str 
   __tag: str

   def __init__(self, tag: str, type: str, name: str = "", desc: str = ""):
      self.__tag = tag
      self.__name = name
      self.__desc = desc
      self.__type = type

   def print_information(self):
      print(f'Tag: {self.__tag}')
      print(f'Name: {self.__name}')
      print(f'Type: {self.__type}')
      print(f'Description: {self.__desc}')


   def get_name(self) -> str:
      return self.__name

   def get_desc(self) -> str:
      return self.__desc

   def get_type(self) -> str:
      return self.__type

   def get_tag(self) -> str:
      return self.__tag