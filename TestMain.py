def find_first_duplicate(arr):  
    seen = set()
 
    for num in arr:
        
        if num in seen:
            return num
      
        seen.add(num)

    return -1

if __name__ == "__main__":
  
    arr = [2, 1, 3, 5, 3, 2]
    result = find_first_duplicate(arr)
    if result != -1:
        print(f"The first duplicate is: {result}")
    else:
        print("No duplicates found.")