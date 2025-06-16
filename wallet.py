class  Wallet :
   def __init__ (self, deposit=0):
      self.deposit = deposit

   def  add_cash( self, value ):
      self.deposit += value

   def  spend_cash(self, value):
      if value > self.deposit :
         raise InsufficientAmount('Not enough available money to spend {}'.format(value))
      self.deposit -= value

class InsufficientAmount(Exception):
   pass
