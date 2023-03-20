# Results Checker
### Automatically check if results have been announced, instead of refreshing the page like a caveman!

## Installation
`git clone https://github.com/pranftw/results_checker.git`<br>
Create a virtual environment and activate it<br>
`pip install -r requirements.txt`<br>

## Example
```python
from results_checker import BMSChecker

checker = BMSChecker(
  sem=7,
  branch='computer science',
  course=None,
  exam_start_month='feb',
  exam_end_month='mar',
  exam_year=2023,
  exam_type=None,
  refresh_interval=60
)
checker()
```