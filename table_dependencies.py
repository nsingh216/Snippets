import os

path = 'C:\Users\...'
str_from = "FROM"
str_join = "JOIN"
tables = []
other = []

def find_word(file_content, word):
     after_words = file_contents.upper().split(word)
     for i in range(0, len(after_words)):
          if i > 1:
               tab = after_words[i].split()[0]
               if len(tab.split(".")) > 1:  # looking for db.table_name syntax
                    tables.append(tab)
               else:  # these look to be cte names
                    other.append(tab)


for filename in os.listdir(path):
    # print(filename)
    with open(path +"\\" + filename) as f:
        file_contents = f.read()  # read whole file
        find_word(file_contents, str_from)
        find_word(file_contents, str_join)
        find_word(file_contents, "TABLE")

tables = sorted(set(tables))
# print(tables)

with open(".\\" + "table_names.txt", 'w') as f:
     for i in tables:
          f.write(i + "\n")

other = sorted(set(other))
with open(".\\" + "other_names.txt", 'w') as f:
    for i in other:
        f.write(i + "\n")
