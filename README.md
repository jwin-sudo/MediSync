# MediSync

1. Have the text file as CSV format
2. Create a function to open CSV file
3. Split the text in CSV so there are no new lines
4. Since it return an array of strings, return the array so can call in a different function

5. create a function to get the names from CSV file
6. call function that opened the CSV file
7. loop through the array and find where it starts with Patient
8. extract the names 
9. create a separate array to store the names
10. append the names 
11. return the array of names

12. create a function to get the number of treatments from CSV file
13. call the function that open the CSV file
14. call the function that give the patient names
15. set counter equal to 0
16. create an array for treatment
17. loop through the array of names and array of strings from CSV file
18. check to see if the name exist in the array of strings and if there's "Treatment" keyword exist 
19. append the number of treatments into the array
20. increment the counter by 1
21. return the treatment array 

22. create a function to calculate the time patients stay 
23. call the function that open the CSV file
24. call the function that get the names of patients
25. create an array to store the date and time 
26. create an array to store just the date
27. create an array to store just the time
28. create an array to store the final hours that the patients stay

29. set start equal to 0 and end equal to 1 to calculate the difference
30. loop through the list of names and list of strings 
31. check when the patient is intake and discharge to get the time
32. store it into an array arr
33. loop through the array arr to split the date and time
34. store the date into date_arr
35. store the time into time_arr
36. use while loop to get the date and time in each position
37. convert the date object into correct format 
38. convert the time object into correct format
39. find the diffence between the two dates and two times
40. get the final time in hours minutes seconds and append to the final array arr
41. increment the start and end by 2 since it's consecutive for each patient 

42. call the function extractPatient(), countTreatment(), and timeStayed()
43. since it's return a value, I set it equal to a variable
44. set i = 0 so I can start a while loop
45. while 0 is less than the length of the array 
46. concatenate the patient name, hours stay, and treatments receive 
47. increment the i by 1
48. break out of the loop once it reaches the max length of the array


Unit Test

Test the file if it return correct output 
test the patient function if there's no data
test the treatment function if there's no data
test the timestayed function if there's no data
