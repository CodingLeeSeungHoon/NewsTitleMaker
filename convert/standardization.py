import json
from os import write
import csv


class Convert:
  def __init__(self):
    self.valid_filepath = "data/vaild_original.json"
    self.standard_valid_filepath = "data/standard_vaild_original.json"
    self.standard_valid_filecsv = "data/standard_vaild_original.csv"
  def convert_data(self):
    news_data = self.openfile()
    documents = news_data['documents']

    self.data = []
    for document in documents:
      data_dic = {}
      data_dic['category'] = document['category']
      data_dic['title'] = document['title']
      data_dic['abstractive'] = document['abstractive'][0]

      main_text = ''
      for text in document['text']:
        main_text += text[0]['sentence'] + ' '
      data_dic['text'] = main_text

      self.data.append(data_dic)

    self.writefile()

  def openfile(self):
    with open(self.valid_filepath, "rt", encoding='UTF-8') as file:
      json_data = json.load(file)
    return json_data

  def writefile(self):
    with open(self.standard_valid_filepath, "wt", encoding='UTF-8') as file:
      json.dump(self.data, file, indent=4, ensure_ascii=False)

  def json_to_csv(self):
    with open(self.standard_valid_filepath, 'rt', encoding='UTF-8', newline="") as input_file, \
    open(self.standard_valid_filecsv, "w", encoding='UTF-8', newline="") as output_file:

      standard_data = json.load(input_file)
  
      f = csv.writer(output_file)

      f.writerow(['category', 'title', 'abstractive', 'text'])

      for datum in standard_data:
        f.writerow([datum["category"], datum["title"], datum["abstractive"], datum["text"]])