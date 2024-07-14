# ++++++++++++++++++++++++++++++++++++ #
# Codédex - Python Challenge           #
# Control Flow - Food Rating           # 
# Author: Frederick Pellerin           #
# X/GitHub: @TheRealFredP3D            #
# ------------------------------------ #
# A five-star restaurant review system #
# ++++++++++++++++++++++++++++++++++++ #
"""
Evaluates a restaurant rating and prints a corresponding review.

The rating is a float value between 0.0 and 5.0, where 5.0 is the highest rating.
The review text is determined by the following criteria:
- Rating > 4.5: 'Extraordinary'
- Rating > 4.0: 'Excellent' 
- Rating > 3.0: 'Good'
- Rating > 2.0: 'Fair'
- Rating <= 2.0: 'Poor'
"""
rating = float(2.0)

if rating > 4.5:
  print('Extraordinary')
elif rating > 4:
  print('Excellent')
elif rating > 3:
  print('Good')
elif rating > 2:
  print('Fair')
else:
  print('Poor')