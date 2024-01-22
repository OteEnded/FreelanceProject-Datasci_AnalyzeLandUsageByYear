from txtmanager import TXTManager

test_txt = TXTManager("2565.csv")
txtData = test_txt.getData()
print(txtData)
split_replace = txtData.split(" ")
txtData = "".join(split_replace)
print(txtData)
test_txt.setData(txtData)
test_txt.save()

# print(len(txtData))
# test_txt.save()