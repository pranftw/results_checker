import time
from thefuzz import fuzz
from .scraper import BMSScraper


class Checker:
  def __init__(self, scraper, refresh_interval):
    self.scraper = scraper
    self.refresh_interval = refresh_interval
  
  def __call__(self):
    self.checker()

  def run(self, *fns):
    while True:
      has_been_announced, result_link = self.check(fns)
      if has_been_announced:
        print(f'\n!!!!!!!RESULTS ANNOUNCED!!!!!!!\n\nCheck at: {result_link}')
        break
      time.sleep(self.refresh_interval)

  def check(self, fns):
    results = self.scraper.scrape()
    if results is not None:
      for result_text, result_link in results:
        if all([fn(result_text.lower()) for fn in fns]):
          return True, result_link
    return False, None


class BMSChecker(Checker):
  def __init__(self, sem, branch, course, exam_start_month, exam_end_month, exam_year, exam_type, refresh_interval=60):
    self.sem = sem
    self.branch = branch
    self.course = course
    self.exam_start_month = exam_start_month
    self.exam_end_month = exam_end_month
    self.exam_year = exam_year
    self.exam_type = exam_type
    super().__init__(BMSScraper(), refresh_interval)

  def checker(self):
    self.run(
      self.check_sem,
      self.check_branch,
      self.check_course,
      self.check_month,
      self.check_year,
      self.check_exam_type
    )
  
  def check_sem(self, result_text):
    return str(self.sem) in result_text
  
  def check_branch(self, result_text):
    return fuzz.partial_ratio(self.branch.lower(), result_text)>=70
  
  def check_course(self, result_text):
    if self.course is not None:
      return self.course.lower() in result_text
    return True

  def check_month(self, result_text):
    return (self.exam_start_month.lower() in result_text) or (self.exam_end_month.lower() in result_text)
  
  def check_year(self, result_text):
    return str(self.exam_year) in result_text
  
  def check_exam_type(self, result_text):
    if self.exam_type is not None:
      return self.exam_type.lower() in result_text
    return True