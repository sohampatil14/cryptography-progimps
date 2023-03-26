import re
import copy
import wordEmbedding


def get_map():
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}


def add_mapping(letter_mapping, cipherword, letter):
    for i in range(len(cipherword)):
        if letter[i] not in letter_mapping[cipherword[i]]:
            letter_mapping[cipherword[i]].append(letter[i])


def combine_maps(map1, map2):
    combined_map = get_map()
    for letter in letters:
        # if both maps empty for letter copy other map's letters
        if map1[letter] == []:
            combined_map[letter] = copy.deepcopy(map2[letter])
        elif map2[letter] == []:
            combined_map[letter] = copy.deepcopy(map1[letter])
        else:
            for mapped_letter in map1[letter]:
                if mapped_letter in map2[letter]:
                    combined_map[letter].append(mapped_letter)

    return combined_map


def check_ambiguity(letter_mapping):
    # removes ambiguity by checking double mapping in characters
    # and remmoving the surely solved ones
    flag = True
    while flag:
        flag = False
        solved_letters = []

        for cipher_letter in letters:
            if len(letter_mapping[cipher_letter]) == 1:
                solved_letters.append(letter_mapping[cipher_letter][0])

        for cipher_letter in letters:
            for sl in solved_letters:
                if len(letter_mapping[cipher_letter]) != 1 and sl in letter_mapping[cipher_letter]:
                    letter_mapping[cipher_letter].remove(sl)
                    if len(letter_mapping[cipher_letter]) == 1:
                        # new letter solved, loop again.
                        loopAgain = True
    return letter_mapping


def word_embed(word):
    word = word.upper()
    count = 0
    letter_num = {}
    embedding = []

    for letter in word:
        if letter not in letter_num:
            letter_num[letter] = str(count)
            count += 1
        embedding.append(letter_num[letter])
    return '.'.join(embedding)


def cryptanalysis(ciphertext):
    combined_map = get_map()
    chipher_words = eng_char_patterns.sub('', ciphertext.upper()).split()
    for cipherword in chipher_words:
        letter_map = get_map()
        embedding = word_embed(cipherword)

        if embedding not in wordEmbedding.embeds:
            continue

        for letter in wordEmbedding.embeds[embedding]:
            add_mapping(letter_map, cipherword, letter)

        combined_map = combine_maps(combined_map, letter_map)

    # remove solved letters from the other lists
    return check_ambiguity(combined_map)


def print_plaintext(key, ciphertext):
    plaintext = ''
    for letter in ciphertext:
        if letter.upper() in key:
            index = key.find(letter.upper())
            if letter.isupper():
                plaintext += letters[index].upper()
            else:
                plaintext += letters[index].lower()
        else:
            plaintext += letter

    return plaintext


def decrypt(ciphertext, letter_mapping):

    key = ['*'] * len(letters)
    for cipher_letter in letters:
        if len(letter_mapping[cipher_letter]) == 1:
            index = letters.find(letter_mapping[cipher_letter][0])
            key[index] = cipher_letter
        else:
            ciphertext = ciphertext.replace(cipher_letter.lower(), '_')
            ciphertext = ciphertext.replace(cipher_letter.upper(), '_')
    key = ''.join(key)

    return print_plaintext(key, ciphertext)


letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
eng_char_patterns = re.compile('[^A-Z\s]')
ciphertext = "dkxyvrh 1 - qegt vkr hxccwv keur: xuwdr wn cehrq nwvvwtp et vkr hwsrhcxto gwvk krh nwnvrh, gkrt nkr tevwdrn x vxuowtp, duevkrq gkwvr hxccwv gwvk x yedorv gxvdk hit yxnv. nkr leuuegn wv qegt x hxccwv keur gkrt niqqrtub nkr lxuun x uetp gxb ve x dihwein kxuu gwvk fxtb uedorq qeehn el xuu nwmrn. nkr lwtqn x nfxuu orb ve x qeeh vee nfxuu leh krh ve lwv, civ vkheipk gkwdk nkr nrrn xt xvvhxdvwsr pxhqrt. nkr vkrt qwndesrhn x cevvur uxcruurq 'qhwto fr', vkr detvrtvn el gkwdk dxinr krh ve nkhwto vee nfxuu ve hrxdk vkr orb. x dxor gwvk 'rxv fr' et wv dxinrn krh ve pheg ve nidk x vhrfrtqein nwmr krh krxq kwvn vkr drwuwtp."

letter_mapping = cryptanalysis(ciphertext)

print('\n Ciphertext:\n', ciphertext)
plaintext = decrypt(ciphertext, letter_mapping)
print('\n Obtained Plaintext:\n', plaintext)
