from csvmanager import CSVManager

test_csv = CSVManager("2565.csv")
csvData = test_csv.getData()
for i in csvData:
    real_loc_id = csvData[i]["document_number"].split("(")[1]
    real_loc_id = real_loc_id.split(")")[0]
    csvData[i]["location_id"] = real_loc_id
    csvData[i]["document_number"] = csvData[i]["document_number"].split("(")[0]
print(csvData)

test_write = CSVManager("test2.csv", True, False)
test_write.setHeader(test_csv.getHeader())
test_write.setData(csvData)
test_write.save()