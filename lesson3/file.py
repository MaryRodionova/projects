"Запись в файл "


def main():
    with open('referat.txt','r',encoding='utf-8') as myfile:
        #for line in myfile:
        content  = myfile.read()
        leng_content=len(content)
        count_words=len(content.split())
        content_exclamatory=content.replace(".","!")
        print(leng_content)
        print(count_words)
        print(content_exclamatory)
    with open('referat2.txt','w',encoding='utf-8') as myfile2:
        myfile2.write(content_exclamatory)

if __name__ == "__main__":
    main()