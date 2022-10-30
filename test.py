from porridge import Porridge
porridge = Porridge('myfirstkey:myfirstsecret')
boiled_password = porridge.boil('password')
a = porridge.verify('password', boiled_password)

b = porridge.verify('notmypassword', boiled_password)

print(a)
print(b)
