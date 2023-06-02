import pickle

filepath = 'score.bin'

def input_scores():
    s = []
    i = 1
    while True:
        n = int(input(f'#{i}? '))
        
        if n < 0:
            break
        s.append(n)
        i += 1
    return s

def get_average(s):
    total = 0
    for n in s:
        total += n
    return total / len(s)

def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

def save_data(scores, filepath):
    with open(filepath, 'wb') as file:
        pickle.dump(scores, file)

def load_data(filepath):
    with open(filepath, 'rb') as file:
        scores = pickle.load(file)
    return scores

# Check if the file exists and load scores if it does
try:
    scores = load_data(filepath)
    print("[파일읽기]")
    show_scores(scores)
    print("평균:", get_average(scores))
except FileNotFoundError:
    scores = input_scores()
    print("[점수 입력]")
    save_data(scores, filepath)

print("[점수 출력]")
show_scores(scores)
print("평균:", get_average(scores))

   
