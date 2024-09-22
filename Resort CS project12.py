def Main_menu():
     print("WELCOME to INFINITY RESORT")
     print("1 for Customer Registration ")
     print("2 for  Hotel Management " )
     x=input("Pls tell what you want to know :")
Main_menu()
#Customer Registration
if x==1 :
          def register() :
               print('0:Addition of Record ')
               print('1:Modification of Record ')
               print('2:Deletion of Record ')
               print('3:Main Menu ')
               opt=int(input("Enter the option:"))
               if opt==0 :
                    Add_File()
               elif opt==1 :
                    Modify_File
               elif opt==2 :

               elif opt==3:
                    Main_menu()               
              
          def Add_File() :
                Name=str(input('Customer Name:'))
                Address=input('Customer Permanent Address:')
                Contact No.=int(input('Customer Mobile:'))
                Aadhar ID=int(input('Customer ID no. :'))
                CheckIn = input('Date of Check in :')
                CheckOut = input('Date of Check out :')
                Numroom = input('Number of room :')
                Regst Id = int(input('Registration No. of customer :'))
          Add_File()

          def Modify_File() :
               print('Editting Part')
               Name=str(input('Customer Name:'))
               Address=input('Customer Permanent Address:')

               Contact No.=int(input('Customer Mobile:'))
               Aadhar ID=int(input('Customer ID no. :'))
               CheckIn = input('Date of Check in :')
               CheckOut = input('Date of Check out :')
          Modify_File()
#HotelManagment,Customer info
     '''elif x==2 :
          c=Regist Id
          f1=open(file of rooms type )
          r= room type
          rp=room price
          d=dine file
          dp=dine price{d1+d2}
          sig=open(sig file)
          sp=sig price {s1+game+tax}
          print("Bill = sum(rp+dp+sp-offer")
          
          
          
          
          
          
          





          
