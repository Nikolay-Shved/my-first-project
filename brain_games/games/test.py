

def calculation(NUM_1, NUM_2, NUM_3):

    if NUM_3 == '+':
        result = NUM_1 + NUM_2
    elif NUM_3 == '-':
         result = NUM_1 - NUM_2
    else:
        result = NUM_1 * NUM_2
    
    print(f'Question: {NUM_1} {NUM_3} {NUM_2}')