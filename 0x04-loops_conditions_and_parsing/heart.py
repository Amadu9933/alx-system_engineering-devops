#Heart shape filled with alphabets

n = 6
for i in range(n//2, n, 2):
     
        for j in range(1, n-i, 2):
                    print(" ", end="")
                       
                           for j in range(i):
                                       print(chr(65 + j), end="")
                                           
                                               for j in range(1, n-i+1, 1):
                                                           print(" ", end="")
                                                              
                                                                  for j in range(i):
                                                                              print(chr(65 + j), end="")
                                                                                  print()


                                                                                  for i in range(n, 0, -1):
                                                                                          for j in range(i, n):
                                                                                                      print(" ", end="")
                                                                                                          for j in range(i*2):
                                                                                                                      print(chr(65 + j), end="")
                                                                                                                          print()
