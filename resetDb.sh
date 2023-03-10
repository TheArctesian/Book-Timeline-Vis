python3 ./DB/GoodReads/cleanGoodReads.py
python3 ./DB/LetterBox/cleanLetterBox.py
python3 ./DB/cleanOut.py
rm ./webapp/src/Data/merged_file.json
cp ./DB/merged_file.json ./webapp/src/Data/
