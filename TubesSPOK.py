def take_input():
    print("This program only accepts subjects: aku, dia, mereka, kita, kamu")
    print("This program only accepts Predicates: membaca, membeli, menonton, menggambar, menulis")
    print("This program only accepts Objects: buku, komik, novel, film, pantun")
    print("This program only accepts Adverbs: di kamar, kemarin, di rumah, tadi, sekarang")
    
    sentence = input("\n\nType the sentence that you want to check:\n")
    
    return sentence.lower()

def subject(sentence):
    def change_state(early_state, character):
        last_state = "reject"

        if early_state == "q0":
            if character == "a":
                last_state = "q1"
            elif character == "k":
                last_state = "q3"
            elif character == "d":
                last_state = "q6"
            elif character == "m":
                last_state = "q8"

        if early_state == "q1":
            if character == "k":
                last_state = "q2"
        
        if early_state == "q2":
            if character == "u":
                last_state = "q12"

        if early_state == "q3":
            if character == "a":
                last_state = "q4"
            elif character == "i":
                last_state = "q5" 

        if early_state == "q4":
            if character == "m":
                last_state = "q2"
        
        if early_state == "q5":
            if character == "t":
                last_state = "q7"
        
        if early_state == "q7":
            if character == "a":
                last_state = "q12"
        
        if early_state == "q6":
            if character == "i":
                last_state = "q7"
            
        if early_state == "q8":
            if character == "e":
                last_state = "q9"

        if early_state == "q9":
            if character == "r":
                last_state = "q10"

        if early_state == "q10":
            if character == "e":
                last_state = "q11"

        if early_state == "q11":
            if character == "k":
                last_state = "q7"       
        return last_state
    
    state = "q0"
    word = ""
    i = 0

    while state != "reject" and i < len(sentence):
        state = change_state(state, sentence[i])
        word += sentence[i]
        i += 1
    
    if state == "q12":
        isSubject = True
    else:
        isSubject = False

    return word, isSubject

def predicate(sentence):
    def change_state(early_state, character):
        last_state = "reject"
        
        if early_state == "q0":
            if character == "m":
                last_state = "q3"

        if early_state == "q3":
            if character == "e":
                last_state = "q8"

        if early_state == "q8":
            if character == "m":
                last_state = "q2"
            elif character == "n":
                last_state = "q7"
        
        if early_state == "q2":
            if character == "b":
                last_state = "q4"

        if early_state == "q4":
            if character == "a":
                last_state = "q5"
            elif character == "e":
                last_state = "q11"

        if early_state == "q5":
            if character == "c":
                last_state = "q6"

        if early_state == "q6":
            if character == "a":
                last_state = "q10"

        if early_state == "q11":
            if character == "l":
                last_state = "q12"

        if early_state == "q12":
            if character == "i":
                last_state = "q10"
        
        if early_state == "q7":
            if character == "g":
                last_state = "q19"
            elif character == "o":
                last_state = "q9"
            elif character == "u":
                last_state = "q16"

        if early_state == "q19":
            if character == "g":
                last_state = "q20"

        if early_state == "q20":
            if character == "a":
                last_state = "q21"

        if early_state == "q21":
            if character == "m":
                last_state = "q22"

        if early_state == "q22":
            if character == "b":
                last_state = "q23"

        if early_state == "q23":
            if character == "a":
                last_state = "q24"

        if early_state == "q24":
            if character == "r":
                last_state = "q10"  

        if early_state == "q9":
            if character == "n":
                last_state = "q13"
        
        if early_state == "q13":
            if character == "t":
                last_state = "q14"
        
        if early_state == "q14":
            if character == "o":
                last_state = "q15"
        
        if early_state == "q15":
            if character == "n":
                last_state = "q10"
        
        if early_state == "q16":
            if character == "l":
                last_state = "q17"
        
        if early_state == "q17":
            if character == "i":
                last_state = "q18"

        if early_state == "q18":
            if character == "s":
                last_state = "q10"  
        return last_state     

    state = "q0"
    word = ""
    i = 0

    while state != "reject" and i < len(sentence):
        state = change_state(state, sentence[i])
        word += sentence[i]
        i += 1

    if state == "q10":
        isPredicate = True
    else:
        isPredicate = False
    
    return word, isPredicate

def object(sentence):
    def change_state(early_state, character):
        last_state = "reject"

        if early_state == "q0":
            if character == "b":
                last_state = "q1"
            elif character == "f":
                last_state = "q4"
            elif character == "n":
                last_state = "q7"
            elif character == "k":
                last_state = "q11"
            elif character == "p":
                last_state = "q15"
            
        if early_state == "q1":
            if character == "u":
                last_state = "q2"
        
        if early_state == "q2":
            if character == "k":
                last_state = "q3"
        
        if early_state == "q3":
            if character == "u":
                last_state = "q20"
        
        if early_state == "q4":
            if character == "i":
                last_state = "q5"
        
        if early_state == "q5":
            if character == "l":
                last_state = "q6"
        
        if early_state == "q6":
            if character == "m":
                last_state = "q20"
        
        if early_state == "q7":
            if character == "o":
                last_state = "q8"
        
        if early_state == "q8":
            if character == "v":
                last_state = "q9"
            
        if early_state == "q9":
            if character == "e":
                last_state = "q10"

        if early_state == "q10":
            if character == "l":
                last_state = "q20"
        
        if early_state == "q11":
            if character == "o":
                last_state = "q12"

        if early_state == "q12":
            if character == "m":
                last_state = "q13"

        if early_state == "q13":
            if character == "i":
                last_state = "q14"
        
        if early_state == "q14":
            if character == "k":
                last_state = "q20"

        if early_state == "q15":
            if character == "a":
                last_state = "q16"
        
        if early_state == "q16":
            if character == "n":
                last_state = "q17"
        
        if early_state == "q17":
            if character == "t":
                last_state = "q18"
        
        if early_state == "q18":
            if character == "u":
                last_state = "q19"

        if early_state == "q19":
            if character == "n":
                last_state = "q20"
        return last_state
    
    state = "q0"
    word = ""
    i = 0

    while state != "reject" and i < len(sentence):
        state = change_state(state, sentence[i])
        word += sentence[i]
        i += 1

    if state == "q20":
        isObject = True
    else:
        isObject = False

    return word, isObject

def adverb(sentence):
    def change_state(early_state, character):
        last_state = "reject"

        if early_state == "q0":
            if character == "d":
                last_state = "q1"
            elif character == "t":
                last_state = "q10"
            elif character == "k":
                last_state = "q13"
            elif character == "s":
                last_state = "q19"

        if early_state == "q1":
            if character == "i":
                last_state = "q2"

        if early_state == "q2":
            if character == "k":
                last_state = "q3"
            elif character == "r":
                last_state = "q6"

        if early_state == "q3":
            if character == "a":
                last_state = "q4"

        if early_state == "q4":
            if character == "m":
                last_state = "q5"

        if early_state == "q5":
            if character == "a":
                last_state = "q27"
        
        if early_state == "q27":
            if character == "r":
                last_state = "q26" 

        if early_state == "q6":
            if character == "u":
                last_state = "q7"

        if early_state == "q7":
            if character == "m":
                last_state = "q8"

        if early_state == "q8":
            if character == "a":
                last_state = "q9"

        if early_state == "q9":
            if character == "h":
                last_state = "q26"

        if early_state == "q10":
            if character == "a":
                last_state = "q11"
        
        if early_state == "q11":
            if character == "d":
                last_state = "q12"
        
        if early_state == "q12":
            if character == "i":
                last_state = "q26"

        if early_state == "q13":
            if character == "e":
                last_state = "q14"

        if early_state == "q14":
            if character == "m":
                last_state = "q15"

        if early_state == "q15":
            if character == "a":
                last_state = "q16"

        if early_state == "q16":
            if character == "r":
                last_state = "q17"

        if early_state == "q17":
            if character == "i":
                last_state = "q18"

        if early_state == "q18":
            if character == "n":
                last_state = "q26"

        if early_state == "q19":
            if character == "e":
                last_state = "q20"

        if early_state == "q20":
            if character == "k":
                last_state = "q21"

        if early_state == "q21":
            if character == "a":
                last_state = "q22"

        if early_state == "q22":
            if character == "r":
                last_state = "q23"

        if early_state == "q23":
            if character == "a":
                last_state = "q24"

        if early_state == "q24":
            if character == "n":
                last_state = "q25"

        if early_state == "q25":
            if character == "g":
                last_state = "q26"

        return last_state

    state = "q0"
    word = ""
    i = 0

    while state != "reject" and i < len(sentence):
        state = change_state(state, sentence[i])
        word += sentence[i]
        i += 1

    if state == "q26":
        isAdverb = True
    else:
        isAdverb = False

    return word, isAdverb

def structure(sentence):
    structure_list = []
    check_word = ""
    i = 0

    while i < len(sentence):
        while i < len(sentence) and sentence[i] != " ":
            check_word += sentence[i]
            i += 1
        i += 1  # Skip the space

        subj_word, is_subj = subject(check_word)
        if is_subj:
            structure_list.append('S')
        else:
            pred_word, is_pred = predicate(check_word)
            if is_pred:
                structure_list.append('P')
            else:
                obj_word, is_obj = object(check_word)
                if is_obj:
                    structure_list.append('O')
                else:
                    adv_word, is_adv = adverb(check_word)
                    if is_adv:
                        structure_list.append('K')
                    else:
                        structure_list.append('UNKNOWN')
        
        check_word = ""  # Reset the check_word for the next word

    return structure_list

def cfg_valid_structure(structure_list):
    list_length = len(structure_list)
    if list_length > 1:
        if structure_list[0] != "S" or structure_list[1] != "P":
            return False
        elif list_length == 2:
            return True
        elif structure_list[2] == "O":
            if list_length == 3:
                return True
            elif structure_list[3] == "K" and list_length == 4:
                return True
            return False
        elif structure_list[2] == "K" and list_length == 3:
            return True
    return False

sentence = take_input()
print(f'This sentence is: {sentence}')

structure_list = structure(sentence)
print(f'The structure we got is: {structure_list}')

valid = cfg_valid_structure(structure_list)
if valid:
    print("The sentence is valid")
else:
    print("The sentence is invalid")