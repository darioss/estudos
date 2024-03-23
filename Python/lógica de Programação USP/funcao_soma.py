def main():
    def soma(x,y,z):
        return x+y+z

    print(soma(10,20,15))
    print(soma(-20,100, 20))

    def multiplica(x, y, z):
        return(x*y*z)

    print(multiplica(2,3,1))
    print(soma(multiplica(2,3,1),soma(100,200,300),multiplica(3,2,2)))
    
main()
