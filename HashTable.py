from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  def create_arr(self, size):
      '''This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.'''

      array = []
      for _ in range(size):
        array.append(LinkedList())
        
      return array


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


  def insert(self, key, value):
    '''This method insert a ey value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared.'''
    new_key_value = (key, value)

    index = self.hash_func(key)
    linked_list = self.arr[index]

    if linked_list.find(key) == -1:
      print(f'{key} was not found.')
      linked_list.append(new_key_value)
    else:
      linked_list.update(key,value)


  def print_key_values(self):
    '''This method traverse through the every Linked List in the table and print the key value pairs.'''

    index = 0
    for linked_list in self.arr:
      print('\n\n')
      print(f'This is the Linked List in the index {index} of the Hash Table')
      linked_list.print_nodes()
      index += 1
