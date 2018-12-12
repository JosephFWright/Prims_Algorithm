# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:32:12 2018

@author: Joseph Wright
"""
from Prims import Prims

def main():

    choice ='0'
    while choice =='0':
        print("MST Theory:")
        print("Choose 1 for Prims")
        print("Choose 2 for Kruskals*")
        choice = input("Please make a choice: ")
    if choice == "1":
        submenu()
    elif choice == "2":
        print("*Kruskals is not available right now.")
    else:
        print("Not a valid choice!")
def submenu():
     file = input("Please enter the filename of your graph file: ")
     start = input("Choose a starting vertex: ")
     graph = input("Would you like the graph to be drawn for you? (Y/N) ")
     if graph == "Y" or graph == "y":
         Prims(str(file), int(start), True)
     elif graph == "N" or graph == "n":
         Prims(str(file), int(start),)
     else:
         print("You didn't choose yes or no. Going back to main menu...")
         main()

main()