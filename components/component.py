class Component(object):
   __name: str
   __desc: str
   __type: str 
   __tag: str

   def __init__(self):
      pass

   def get_name(self) -> str:
      return self.__name

   def get_desc(self) -> str:
      return self.__desc

   def get_type(self) -> str:
      return self.__type

   def get_tag(self) -> str:
      return self.__tag