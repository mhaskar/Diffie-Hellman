#!/usr/bin/python

from termcolor import cprint

g = 5 #Primitive root
p = 23 #Prime number

AliceSecret = 5655 #random number by alice
BobSecret = 95666  #random number by bob

AliceA = g ** AliceSecret % p #generate the unique value for Alice
BobA   = g ** BobSecret   % p #generate the unique value for Bob

AliceSharedSecret = BobA ** AliceSecret % p #calculate the shared secret based on AliceA
BobSharedSecret   = AliceA ** BobSecret % p #calculate the shared secret based on BobA

cprint("Alice Secret is : %s"%AliceSecret,"green")
cprint("Bob   Secret is : %s"%BobSecret,"yellow")
print "*" * 25
cprint("Alice unique value is %s"%AliceA,"green")
cprint("Bob   unique value is %s"%BobA,"yellow")
print "*" * 25
cprint("The Final Secret Key For Alice is : %s"%AliceSharedSecret,"green")
cprint("The Final Secret Key for Bob   is : %s"%BobSharedSecret,"yellow")


