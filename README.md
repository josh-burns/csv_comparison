1 - fork the repo
2 - run `python tester.py textfile.txt textfile2.txt`
3 - notice that they are the same 
4 - run `python tester.py sample.csv sample2.csv` 
5 - notice that they are the different 
6 - note the output: 

```
oh no! sample2.csv and sample.csv don't match. Give me a second, I will find which lines
 ...
---
+++
@@ -26 +26 @@
-Line 25,field2,field3,93w
+Line 25,field2,field3,93


See above differences between sample2.csv and sample.csv
```

this can be used to block a build if CSVs (or other filetypes) text content do not match