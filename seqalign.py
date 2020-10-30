import sys

# minimum alignment takes into account gap and mismatch values
def retrace(a, b, str1, str2, A, x, y):
    if x == 1 and y == 1:
        return str1, str2
    else:
        temp = min(A[x-1][y-1], A[x][y-1], A[x-1][y])
        if temp == A[x][y-1]:
            y -= 1
            str1 = insert(str1, "-", x)
        elif temp == A[x-1][y]:
            x -= 1
            str2 = insert(str2, "-", y-1)
        else:
            x -= 1
            y -= 1

        return retrace(a, b, str1, str2, A, x, y)

def insert(str, letter, index):
    return str[:index] + letter + str[index:]

def alignment(a, b):
    a = "-" + a
    b = "-" + b
    # In the current version of the program, "optimal" is defined as same letter > both vowel/consonant > gap > not both vowel/consonant.
    same_type, delta, diff_type = 1, 2, 3
    a_type, b_type = [], []
    len_a, len_b = len(a), len(b)
    a.lower(), b.lower()

    for letter in a:
        if letter in ("a","e","i","o","u"):
            a_type.append(1)
        else:
            a_type.append(0)
    for letter in b:
        if letter in ("a","e","i","o","u"):
            b_type.append(1)
        else:
            b_type.append(0)

    A = []
    path = []
    for n in range(0, len_a):
        temp = []
        for m in range(0, len_b):
            if m == 0:
                temp.append(n * delta)
            elif n == 0:
                temp.append(m * delta)
            else:
                temp.append(0)
        A.append(temp)

    for i in range(1, len_a):
        for j in range(1, len_b):
            if a_type[i] == b_type[j]:
                A[i][j] = min(same_type + A[i-1][j-1], delta + A[i-1][j], delta + A[i][j-1])
            else:
                A[i][j] = min(diff_type + A[i-1][j-1], delta + A[i-1][j], delta + A[i][j-1])
            if i < len_a and j < len_b:
                if a[i] == b[j]:
                    # print i, j, a[i], A[i-1][j-1]
                    A[i][j] = A[i-1][j-1]
    for i in A:
        print i

    return retrace(a[1:], b[1:], a[1:], b[1:], A, len(a[1:]), len(b[1:]))



if __name__ == "__main__":
    try:
        print alignment(sys.argv[1], sys.argv[2])
    except:
        print "You must run the program in the following format:\npython seqalign 'string1' 'string2'"
