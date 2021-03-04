from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # 1️⃣ TODO: Complete the create_arr method.

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):
    '''This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.'''

    array = []
    for _ in range(size):
      array.append(LinkedList())
      
    return array




  # 2️⃣ TODO: Create your own hash function.

  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

  def hash_func(self, key):
    '''This hash function will count how manny vowels are in a string. An return the count to be use as an index.'''

    vowels = "AaEeIiOoUu"
    count = 0
    for vowel in vowels:
      for character in key:
        if vowel == character:
          count += 1

    index = count % self.size
    return index


  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):
    
    new_key_value = (key, value)

    index = self.hash_func(key)
    linked_list = self.arr[index]

    if linked_list.find(key) == -1:
      print(f'{key} was not found.')
      linked_list.append(new_key_value)
    else:
      linked_list.update(key,value)





  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    '''This method traverse through the every Linked List in the table and print the key value pairs.'''

    index = 0
    for linked_list in self.arr:
      print('\n\n')
      print(f'This is the Linked List in the index {index} of the Hash Table')
      linked_list.print_nodes()
      index += 1


if __name__ == '__main__':
  ht = HashTable(6)
  # print(ht.arr)
  print(ht.hash_func('Eric Morales'))
  print("---")
  print(ht.hash_func('Javier Morales'))
  print("---")
  print(ht.hash_func('Ana Morales'))
  ht.insert("Eric Morales", 1)
  ht.insert("Javier Morales", 1)
  ht.insert("Eric Morales", 2)
  print("---")
  ht.insert("Ana Morales", 1)
