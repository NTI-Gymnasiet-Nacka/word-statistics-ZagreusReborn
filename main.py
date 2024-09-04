# Ordstatistik
# Din uppgift är att läsa in text från filen som är angiven.
# Därefter ska ditt program räkna ut följande:
# - Antal ord
# - Mest frekventa ord
# - Genomsnittlig ordlängd
# Gör en funktion för varje.

# Bonus, gör en i taget, skapa en funktion för varje: 
# - Längsta och kortaste ordet - om det finns flera, bestäm själv om du skriver ut ett eller flera
# - Räkna antalet unika ord (alltså ord som bara förekommer en gång)
from collections import Counter

def read_from_file(path: str):
    """Reads a file with the given parameter path and returns the file as a list of strings, split on newline (\n).

    Args:
        path (str): the path of the readable file

    Returns:
        list(str): list of strings
    """
    with open(path, "r" ,encoding="utf-8") as f:
        return f.readlines()

def words(sentences: list):
    word = []
    for i in sentences:
        i=i.replace(' ','_').replace('\n','').replace('.','').replace('-','').replace(',','').split('_')
        for w in i:
            if w!='':
                word.append(w)
    return word

def frequent_words(word: list):
    common_words=Counter(word).most_common(1)
    return common_words[0][0]

def average_length(word: list):
    l=0
    for i in word:
        l+=len(i)
    return f'{l/len(word):.2f}'

def longest_and_shortest_words(word: list):
    word_length=[]
    for i in range(0,len(word)):
        word_length.append(len(word[i]))
    longest=max(word_length)
    shortest=min(word_length)
    return f'{word[word_length.index(longest)]}, {word[word_length.index(shortest)]}'
def main():
    
    sentences = read_from_file("en_resa_genom_svenska_skogen.txt") # Här har du nu en lista av strängar från den inlästa filen.

    word = words(sentences)
    print(len(word))
    print(frequent_words(word))
    print(average_length(word))
    print(longest_and_shortest_words(word))

if __name__ == "__main__":
    main()