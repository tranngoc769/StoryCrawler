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
def numberToText(number, prefix =""):
      range1 = [
        [0, "không", "", ""],
        [1, "một", "mốt"],
        [2, "hai"],
        [3, "ba"],
        [4, "bốn"],
        [5, "năm", "lăm", "lăm"],
        [6, "sáu"],
        [7, "bảy"],
        [8, "tám"],
        [9, "chín"],
        [10, "mười"]
    ]
      range2 = [
            [1000000000, "tỷ"],
            [1000000, "triệu"],
            [1000, "ngàn"],
            [100, "trăm"]
      ]
      if (number < 0):
            number *= -1;
            return numberToText(number, "âm ")
      decTxt = ""
      intPart = number
      if (intPart >= 0 and intPart <= 10):
            r = range1[intPart]
            return prefix + r[1]+decTxt
      # mười -> mười chín
      if (intPart > 10 and intPart < 20):
            r = range1[intPart - 10]
            n = r[1]
            try:
                  n = r[3]
            except:
                  n = r[1]
            return prefix +"mười " + n + decTxt
      if (intPart >= 20 and intPart < 100):
            f = intPart // 10
            l = intPart % 10
            r = range1[f][1] #Bốn
            k = range1[l][1]
            try:
                  k = range1[l][2]
            except:
                  k = range1[l][1]
            return prefix +r +" mươi " + k 
      result = ''
      for i in range(0, len(range2)):
            r = range2[i]
            rVal = int(r[0])
            roundedDiv = intPart // rVal
            if roundedDiv >= 1:
                  remainder = intPart % rVal
                  result += numberToText(roundedDiv)
                  result += " " + r[1]
                  if remainder:
                        if remainder < 10:
                              result+= " lẻ"
                        result+= " " +numberToText(remainder)
                  break
      return prefix + result + decTxt
def checkNumberInSentense(text):
      temp = []
      check = True
      for s in text.split():
            if s.isdigit():
                  s = numberToText(int(s))
                  check = False
            temp.append(s)
      totalWord = len(temp)
      if (totalWord < 3 and check == False):
            totalWord = 0
      return totalWord, " ".join(temp)
def Normalize_File():
      if os.path.isdir(textDir) == False:
            print("Not found folder")
            return False
      listFile = getTextFileInFolder(textDir)
      with open(fileOut, encoding="UTF-8", mode="w") as fOut:
            for filename in listFile:
                  with open(filename, encoding="UTF-8", mode="r") as f:
                        print("File : "+ filename)
                        listString = f.readlines()
                        listString = [x.strip() for x in listString] 
                        content = (" ".join(listString)).split(".")
                        totalLine = len(content)
                        start = 0
                        for text in content:
                              out = normalize_text(text)
                              subTextArr = out.split(".")
                              for subText in subTextArr:
                                    subText = subText.strip()
                                    totalWord, solveString = checkNumberInSentense(subText)
                                    if (totalWord != 0):
                                          fOut.write(solveString.strip() + "\n")
                              start+= 1
                              # print(str(start)+"/"+str(totalLine))
      return True
# import re
# text = "   Bắt~!@#$%^&*()_\\-=+/*<>đầu từ-gà gáy một tiếng, trâu bò lục-tục kéo thợ cầy đến đoạn đường phía trong điếm tuần.... - Mọi ngày, giờ ấy, những con-vật này cũng như những người cổ cầy, vai bừa kia, đã lần-lượt đi mò ra ruộng làm việc cho chủ."
# print(out)
def getTextFileInFolder(folder):
      listFile = []
      for file in os.listdir(folder):
          if file.endswith(".txt"):
            listFile.append(os.path.join(folder, file))
      return listFile
def startNormalize():
      stt = Normalize_File()
      if (stt):
            print("Success")
      else:
            print("Failed")
if __name__ == "__main__":
      startNormalize()
