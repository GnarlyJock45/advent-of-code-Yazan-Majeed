def main():
    s_idx = ""
    counter = 0
    
    with open('textFiles/official.txt', 'r') as file:
        for line in file:
            # how much "^" without first and last exampel .^.^.^...^. = 2, this number x2 it means 2*2=4, 4- from the interpretation
            # how much "." between ^.^ if it'1 1- if it's 2 0 if it's 3+ =3+
            # exampel .^.^.^...^.= 2- and 1+ = 7