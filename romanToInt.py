def romanToInt(s):
    result = 0
    dictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    s = list(s)
    for i in range(len(s)):
        if i == len(s)-1 and s[i] != '':
            result += dictionary.get(s[i])
        elif s[i] == 'I':
            if s[i+1] == 'V' or s[i+1] == 'X':
                result += (dictionary.get(s[i + 1]) - dictionary.get(s[i]))
                s[i + 1] = ''
            else:
                result += dictionary.get(s[i])
        elif s[i] == 'X':
            if s[i+1] == 'L' or s[i+1] == 'C':
                result += (dictionary.get(s[i + 1]) - dictionary.get(s[i]))
                s[i + 1] = ''
            else:
                result += dictionary.get(s[i])
        elif s[i] == 'C':
            if s[i+1] == 'D' or s[i+1] == 'M':
                result += (dictionary.get(s[i + 1]) - dictionary.get(s[i]))
                s[i + 1] = ''
            else:
                result += dictionary.get(s[i])
        elif s[i] == '':
            pass
        else:
            result += dictionary.get(s[i])

    return result

print(romanToInt('MMCCCXCIX'))