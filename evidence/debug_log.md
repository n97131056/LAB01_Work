# Traceback and Repair Log
Traceback (most recent call last):
  File "D:\python_game\lab01_student_starter\lab01-work\src\lab01.py", line 37, in <module>
    print(format_student_record("Lin", "eighty"))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\python_game\lab01_student_starter\lab01-work\src\lab01.py", line 34, in format_student_record
    classification = classify_score(score)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "D:\python_game\lab01_student_starter\lab01-work\src\lab01.py", line 10, in classify_score
    raise TypeError
TypeError
## Observation and exception type
TypeError
## First relevant frame in my code
第37行
## Smallest reproducible case
 type, value error
## Hypothesis and evidence
應該是數字而不是字串
## Minimal repair and verification command
score 必須是 int

