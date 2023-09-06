ABBREVIATIONS = ['Dr', 'Prof', 'Mr', 'Mrs', 'Ms', 'St', 'Jr', 'Co', 'Ltd', 'Inc', 'Capt', 'Cpt', 'Lt', 'ft']
DELIMITERS = ['.', '?', '!', ':', ';', '\n']


class TextPreprocessing:

    @classmethod
    def get_sentences(cls, text: str):
        words_temp = text.split(' ')
        words = []

        for word in words_temp:
            words += word.split('\n')

        words = ['\n' if word == '' else word for word in words]

        sentences = []
        sentence = ''
        for word in words:
            sentence += word + ' '
            if word[-1] in DELIMITERS:
                if word[:-1] in ABBREVIATIONS:
                    continue
                elif word[:-1].isnumeric() and len(sentence) > 0:
                    if sentence[0].isnumeric():
                        sentences.append(' '.join(sentence.split()[:-1]))
                        sentence = word + ' '
                    else:
                        sentences.append(' '.join(sentence.split()))
                        sentence = ''
                else:
                    sentences.append(' '.join(sentence.split()))
                    sentence = ''

        if sentence != '':
            sentences.append(sentence)

        while '' in sentences:
            sentences.remove('')

        return sentences
