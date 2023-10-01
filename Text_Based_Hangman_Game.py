while attempts > 0:

        failed = 0

        for char in word: 
            if char in guessed_letters: 
                print(char, end = '')
            else: 
                print('_', end = '')
                failed += 1