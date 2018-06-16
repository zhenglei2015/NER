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
    for i in range(len(guess)):
        s1 = right[i].split(" ")
        s2 = guess[i].split(" ")
        print right[i], guess[i]
        if len(s1) > 1:
            if s1[0] != s2[0]:
                print i, s1[0], s2[0]
            fi.write(s1[0] + " " + s1[1].strip() + " " + s2[1])
        else:
            fi.write("\n")

if __name__ == '__main__':
    write_nll()