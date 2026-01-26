class student:
  name = "Narendra"
  def __len__(self):
    i = 0
    for c in self.name:
      i = i + 1
    return i
s = student()
print(len(s))