# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 11:25:29 2019

@author: flavien
"""
# Datasruct Diane Du Peloux, Flavien Galbez

# Partie 3

# Question 1

""" Une recherche naive et gloutonne """
def naifSearch (unsortedListe, researched_number): 
  
    # On regarde toute les cases 
    for i in range (0,len(unsortedListe)):
        if unsortedListe[i]==researched_number: 
            return i
    # si aucunes des cases sont egales a notre nombre alors on retourne -1
    return -1


# Question 2


""" La fonction reccurcive de divideAndConquerSearch """
def divideAndConquerSearchRec (unsortedListe, l, r, researched_number): 
  
    # Si nous n'avons pas parcouru l'ensemble des elements
    if r >= l: 
        mid = l + (r - l)//2
        # Si le milieu est notre element recherche 
        if unsortedListe[mid] == researched_number: 
            return mid
        else:
            # On regarde des deux cotes car la liste n'est pas triee 
            return max(divideAndConquerSearchRec(unsortedListe, mid + 1, r, researched_number),divideAndConquerSearchRec(unsortedListe, l, mid-1, researched_number))
    else: 
        # Si notre element n'est pas present on retourne -1
        return -1
    
""" Une recherche naive et gloutonne mais en divise pour regner sur une liste non triee """  
def divideAndConquerSearch (sorterdListe, researched_number):
    return divideAndConquerSearchRec (sorterdListe, 0, len(sorterdListe)-1, researched_number)


# Question 3

""" Un quicksort afin de trier notre liste de maniere plutot efficace """
def quicksort(unsortedListe):
    if unsortedListe == []:
        return []
    else:
        pivot = unsortedListe[0]
        l1 = []
        l2 = []
        for x in unsortedListe[1:]:
            if x<pivot:
                l1.append(x)
            else:
                l2.append(x)
    return quicksort(l1)+[pivot]+quicksort(l2)

""" La fonction reccurcive de divideAndConquerSearch """
def dichotomieSearchRec (sorterdListe, l, r, researched_number): 
  
    # Si nous n'avons pas parcouru l'ensemble des elements succeptible d'etre notre valeur
    if r >= l: 
  
        mid = l + (r - l)//2
  
        # Si le milieu est notre element recherche 
        if sorterdListe[mid] == researched_number: 
            return mid 
          
        # Si l'element est plus grand que le milieu alors il ne peut que se situer a droite 
        elif sorterdListe[mid] < researched_number: 
            return dichotomieSearchRec(sorterdListe, mid + 1, r, researched_number) 
  
        # Si l'element est plus petit que le milieu alors il ne peut que se situer a gauche
        else: 
            return dichotomieSearchRec(sorterdListe, l, mid-1, researched_number) 
    else: 
        # Si notre element n'est pas present on retourne -1
        return -1
    
""" Une recherche dichotomique pour une liste triee """  
def dichotomieSearch (sorterdListe, researched_number):
    return dichotomieSearchRec (sorterdListe, 0, len(sorterdListe)-1, researched_number)


# Question 4
# Test array 
    
""" On cree la base de donnee de facon aleatoire"""
import random
dtb3=[]
i=0
while (i<100):
    randint=random.randrange(0,10000)
    if randint not in dtb3 :
        dtb3.append(random.randrange(0,10000))
        i=i+1
        
x_in = dtb3[4]
x_not_in = 12256
print (naifSearch(dtb3, x_in))
print (naifSearch(dtb3, x_not_in))
print (divideAndConquerSearch(dtb3, x_in))
print (divideAndConquerSearch(dtb3, x_not_in))
print (dichotomieSearch(dtb3, x_in))
print (dichotomieSearch(dtb3, x_not_in))
dtb3Sorted=quicksort(dtb3)
print(dtb3)
print(dtb3Sorted)
print (dichotomieSearch(dtb3Sorted, x_in))
print (dichotomieSearch(dtb3Sorted, x_not_in))
print (naifSearch(dtb3Sorted, x_in))
print (naifSearch(dtb3Sorted, x_not_in))
print (divideAndConquerSearch(dtb3Sorted, x_in))
print (divideAndConquerSearch(dtb3Sorted, x_not_in))


# Partie 4
""" On cree la base de donnee de facon aleatoire """
import random
dtb4=[]
i=0
while (i<100):
    randint=random.randrange(0,10000)
    if randint not in dtb4 :
        dtb4.append(random.randrange(0,10000))
        i=i+1

    
""" Class definissant les Binary Serarch Tree """
class NodeBRT(object):

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = NodeBRT(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = NodeBRT(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
# findval method to compare the value with nodes
    def valIsInBRT(self, researchedValue):
        if researchedValue < self.data:
            if self.left is None:
                return False
            return self.left.valIsInBRT(researchedValue)
        elif researchedValue > self.data:
            if self.right is None:
                return False
            return self.right.valIsInBRT(researchedValue)
        else:
            return True
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
    
    def affichageRec(self, i):
        if self.left!= None :
            self.left.affichageRec(i+1)
        print(str(i)+"| "+str(self.data))
        if self.right!= None :
            self.right.affichageRec(i+1)
    
    def affichage(self):
        self.affichageRec(0)
        
""" Remplir l'arbre BRT avec la dtb et tester les recherches """

TreeBRT=NodeBRT(dtb4[0])
for val in dtb4[1:]:
    TreeBRT.insert(val)
print(dtb4)
print(TreeBRT.valIsInBRT(dtb4[4]))
print(TreeBRT.valIsInBRT(12097))
TreeBRT.affichage()

#Question 2

""" Class definissant les AVL Tree """
class NodeAVL(object):

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
        self.height = 1
    
    
    def insert(self,insertedValue):
        if self.data:
            if insertedValue < self.data:
                if self.left is None:
                    self.left = NodeAVL(insertedValue)
                else:
                    self.left.insert(insertedValue)
            elif insertedValue > self.data:
                if self.right is None:
                    self.right = NodeAVL(insertedValue)
                else:
                    self.right.insert(insertedValue)
        else:
            self.data = insertedValue
        #self.balance()
        
    def valIsInAVL(self, researchedValue):
        if researchedValue < self.data:
            if self.left is None:
                return False
            return self.left.valIsInAVL(researchedValue)
        elif researchedValue > self.data:
            if self.right is None:
                return False
            return self.right.valIsInAVL(researchedValue)
        else:
            return True
    
    def affichageRec(self, i):
        if self.left!= None :
            self.left.affichageRec(i+1)
        print(str(i)+"| "+str(self.data))
        if self.right!= None :
            self.right.affichageRec(i+1)
    
    def affichage(self):
        self.affichageRec(0)

""" Remplir l'arbre AVL avec la dtb et tester les recherches """

TreeAVL=NodeAVL(dtb4[0])
for val in dtb4[1:]:
    TreeAVL.insert(val)
TreeAVL.affichage()
print(TreeAVL.valIsInAVL(dtb4[4]))
print(TreeAVL.valIsInAVL(12097))

#Question 3

""" Class definissant les B-Tree """
class BTree(object):

    class BNode(object):

        def __init__(self):
            self.keys = []
            self.children = []
            self.leaf = True

        def split(self, parent, payload):
            new_node = self.__class__()

            mid_point = len(self.keys)//2
            split_value = self.keys[mid_point]
            parent.add_key(split_value)

      # Add keys and children to appropriate nodes
            new_node.children = self.children[mid_point + 1:]
            self.children = self.children[:mid_point + 1]
            new_node.keys = self.keys[mid_point+1:]
            self.keys = self.keys[:mid_point]

      # If the new_node has children, set it as internal node
            if len(new_node.children) > 0:
                new_node.leaf = False

            parent.children = parent.add_child(new_node)
            if payload < split_value:
                return self
            else:
                return new_node

        def add_key(self, value):
            self.keys.append(value)
            self.keys.sort()

        def add_child(self, new_node):
            i = len(self.children) - 1
            while i >= 0 and self.children[i].keys[0] > new_node.keys[0]:
                i -= 1
            return self.children[:i + 1]+ [new_node] + self.children[i + 1:]
        
        def affichageRec(self, i):
            print(str(i)+"| "+str(self.keys))
            for nodei in self.children:
                if nodei!= None :
                    nodei.affichageRec(i+1)

    def __init__(self):
        self.root = self.BNode()

    def insert(self, payload):
        node = self.root
    # Root is handled explicitly since it requires creating 2 new nodes instead of the usual one.
        if len(node.keys) == 2*5-1:
            new_root = self.BNode()
            new_root.children.append(self.root)
            new_root.leaf = False
      # node is being set to the node containing the ranges we want for payload insertion.
            node = node.split(new_root, payload)
            self.root = new_root
        while node.leaf == False:
            i = len(node.keys) - 1
            while i > 0 and payload < node.keys[i] :
                i -= 1
            if payload > node.keys[i]:
                i += 1

            next = node.children[i]
            if len(node.keys) == 2*5-1:
                node = next.split(node, payload)
            else:
                node = next
    # Since we split all full nodes on the way down, we can simply insert the payload in the leaf.
        node.add_key(payload)

    def valIsInB(self, value, node=None):
        if node is None:
            node = self.root
        if value in node.keys:
            return True
        elif node.leaf:
      # If we are in a leaf, there is no more to check.
            return False
        else:
            i = 0
        while i < len(node.keys) and value > node.keys[i]:
            i += 1
        return self.valIsInB(value, node.children[i])

  
    def affichage(self):
        self.root.affichageRec(0)    
""" Remplir l'arbre AVL avec la dtb et tester les recherches """

TreeB=BTree()
for val in dtb4:
    TreeB.insert(val)
    
    
print(TreeB.valIsInB(dtb4[4]))
print(TreeB.valIsInB(12097))  

TreeB.affichage()
        