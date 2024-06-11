quest = ["\nQ1.What is the 1 tallest building in the world ?"]
opt = [["Burj Khalifa", "Shanghai Tower", "Merdeka", "Abraj Al-Bait Clock Tower"]]
ans = ["Burj Khalifa"]

print(quest[0])
print(f"A.{opt[0][0]} B.{opt[0][1]} C.{opt[0][2]} D.{opt[0][3]}")

optAns = input("\nEnter correct option: ").lower()

if optAns == "a" and opt[0][0] in ans[0]:
    print("True")
else:
    print("False")
