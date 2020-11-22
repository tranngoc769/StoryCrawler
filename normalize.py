# Tool convert danh sách các file text trong thư mục thành 1 file duy nhất đã qua chuẩn hóa : dòng, kí tự,... --> làm language model
# Hướng dẫn sử dụng : python main.py -i|--textdir [TEXTDIR] -o|--output [FILEOUT]
import  re
import sys
import  os
import argparse
parser = argparse.ArgumentParser(description='Huong dan su dung')
parser.add_argument('-i','--textdir', help='Folder of text files', required=True)
parser.add_argument('-o','--output', help='Path of output text file', required=True)
# args = vars(parser.parse_args())
# textDir =  args['textdir']
# fileOut = args['output']
textDir = "txtdir"
fileOut = "output.txt"
def normalize_text(text):
      text = text.strip()
      text = re.sub(r'[/\\~@#$%^&*()_\--/*<>,“”;"]',' ', text)
      text = text.replace("="," ")
      text = text.replace("+"," ")
      text = re.sub(' +', ' ',text)
      text = re.sub('\?+', '.',text)
      text = re.sub(':+', '.',text)
      text = re.sub('!+', '.',text)
      out = re.sub('\.+', '.',text)
      out = out.replace("…",".")
      return out
