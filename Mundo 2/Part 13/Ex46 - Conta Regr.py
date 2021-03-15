from time import sleep
import emoji

print(f"{' CONTAGEM REGRESSIVA ' :=^50}")

for i in range(1, 11, 1):
    print(f"==>{i}")
    sleep(1)

print(emoji.emojize(":confetti_ball: " * 10))
