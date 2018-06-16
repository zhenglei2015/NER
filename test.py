def write_nll():
    right = []
    guess = []
    fi = open("result.txt", "r")
    for line in fi:
        guess.append(line)
    fi.close()

    fi = open("dev.eval", "r")
    for line in fi:
        right.append(line)
    fi.close()
    fi = open("nll.txt", "w")
    for i in range(min(len(guess), len(right))):
        s1 = right[i].split(" ")
        s2 = guess[i].split(" ")
        if len(s1) > 1:
            if s1[0] != s2[0]:
                print i, s1[0], s2[0]
            fi.write(s1[0] + " " + s1[1].strip() + " " + s2[1])
        else:
            fi.write("\n")

def split_file():
    fi = open("dev.eval", "r")
    word = open("predict.txt", "w")
    for line in fi:
        s = line.split(" ")
        if len(s) < 2:
            word.write("\n")
        else:
            word.write(s[0] + " ")
    fi.close()
    word.close()

if __name__ == '__main__':
    split_file()
