l=["a", "b", "c", "d", "e", "f", "g"]
def skip_elements(elements):
  new_list = []
  for i in range(len(elements)):
      if i % 2 == 0:
          new_list.append(elements[i])

  return new_list

print(skip_elements(l)) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) #should be ['orange,'strawberry','Peach']