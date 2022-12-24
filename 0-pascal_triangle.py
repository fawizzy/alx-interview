#!/usr/bin/python3

def pascal_triangle(n): 
  triangle = []
  for i in range(n): 
    row = [1] 
    if i > 0: 
      last_row = triangle[i-1] 
      for j in range(1, i): 
        row.append(last_row[j-1] + last_row[j]) 
      row.append(1) 
    triangle.append(row) 
  return triangle 