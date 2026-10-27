def record_task(name, correct, total):
 accuracy = (correct/total) * 100
 return accuracy

def main():
 print("Accuracy Performance Tracker")

 task_name = input("Task name: ")
 correct = int(input("Correct count: "))
 total = int(input("Total count: "))

 if total == 0:
  print("Total cannot be zero")
  return

 accuracy = record_task(task_name, correct, total)

 if accuracy >= 99.99:
  status = "Excellent"
 elif accuracy >= 99.5:
  status = "Acceptable"
 else:
  status = "Below Standard"

 print("Accuracy: ", accuracy)
 print("Status: ", status)

 with open("data.txt", "a", encoding="utf-8") as file:
  file.write(f"{task_name}, {correct}, {total}, {accuracy}, {status}\n")

if __name__ == "__main__":
 main()
