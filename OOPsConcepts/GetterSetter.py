class Phone:
  def __init__(self):
    self.__passward = "naren7788" #PIN is not used for mathematics  won’t add or subtract it So we keep it as string

  def get_passward(self):
    return self.__passward

  def set_passward(self , old_pass , new_pass):
    if old_pass == self.__passward:
      self.__passward = new_pass
      print("Passward is change ")
    else:
      print("Old passward is Incorrect")

user = Phone()

# getter
print(user.get_passward())

# setter
user.set_passward("naren7788","hello123")

user.set_passward("naren123","hello123")
    
  
    