def bubble_sort(values):
    if (len(values) <= 1):
        return values
    elif (len(values) == 2):
        if values[0] <= values[1]:
            return values
        else:
            return values[::-1]
            
    elif (len(values) > 2):
        activate = True
        c = 0
        while(activate):
            for pre in range(0, len(values)-1):
                if values[pre+1] < values[pre]:
                        c += 1
                        temp = values[pre+1]
                        values[pre+1] = values[pre]
                        values[pre] = temp
            if(c == 0):
                return values
            else:
                c = 0
        

# Driver code
if __name__ == '__main__':
    print("Bubble sort.")
    a = [2]
    b = [2, 1]
    c = [2, 9, 3, 4, -1]
    
    print("a: ", bubble_sort(a) )
    print("b: ", bubble_sort(b) )
    print("c: ", bubble_sort(c) )