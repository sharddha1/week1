import numpy as np
class Car:
  def __init__(self,n1,n2):
      self.n1=n1
      self.n2=n2
  def seat(self):
      if self.n1<5 :
         print("Alloted seat in car 1")

      elif self.n1+self.n2>=5 and self.n1+self.n2<10 :
         print("Alloted seat in car 2")

      else :
         print("There is no seat in the cars")

class Bus:
            def __init__(self, m):
                self.m = m

            def seat(self):
                if self.m < 25:
                    print("Alloted sitting space in the bus")
                elif self.m >=25 and self.m <40:
                    print("Alloted standing space in the bus")
                else:
                    print("There is no space in the bus")

n1=0
n2=0
m=0
while True:
    a=input("Enter A if u want car and B if u want bus and C if u want to remove a person")
    if a=='A':
      x=Car(n1,n2)
      x.seat()
      if n1<5:
          n1+=1

      elif n1==5 and n2<5:
          n2+=1
          n1+=0
      elif n1==5 and n2==5:
          n1+=0
          n2+=0
      print(f"no.of empty spaces in car1 ={5-n1}")
      print(f"no.of empty spaces in car2 ={5-n2}")
      print(f"no.of empty spaces in bus ={40-m}")


    elif a=='B':
      x=Bus(m)
      x.seat()
      if m<40:
          m+=1
      else:
          m+=0
      print(f"no.of empty spaces in car1 ={5-n1}")
      print(f"no.of empty spaces in car2 ={5-n2}")
      print(f"no.of empty spaces in bus ={40-m}")
    elif a=='C':

     x = np.random.rand()
     if x < 0.6:
        if m > 25 and m <= 40:
            m = m - 1
            print("standing person is removed from bus")

        elif m > 0 and m <= 25:
            m = m - 1
            print("sitting person is removed from bus")

        else:
            print("you cannot remove a person from bus")



     elif x < 0.8:
        if n1!=0:
            n1-=1
            print("person is removed from car 1")
        else:
            n1 -=0
            print("you cannot remove a person from car1")


     else:
        if n2 != 0:
            n2 -= 1
            print("person is removed from car 2")

        else:
            n2 -= 0
            print("you cannot remove a person from car2")
     print(f"no.of empty spaces in car1 ={5-n1}")
     print(f"no.of empty spaces in car2 ={5-n2}")
     print(f"no.of empty spaces in bus ={40-m}")

    else:
        break




