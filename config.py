API_KEY ='uU9Bi5uIPxGLgLrZ9crX1vcVp3sEKGbrsQLvwKUrMcKc4UhS52KYNrCHlVDW2SGY'
API_SECRET ='wy6y3wjqSclen1AZPrHyrBbPh1CjyJaVA8bm1UZV9a6tMypArD5kMS2BZJ7ANG6P'

#FUNCTIONS
def truncate(number, digits) -> float:
    startCounting = False
    if number < 1:
      number_str = str('{:.20f}'.format(number))
      resp = ''
      count_digits = 0
      for i in range(0, len(number_str)):
        if number_str[i] != '0' and number_str[i] != '.' and number_str[i] != ',':
          startCounting = True
        if startCounting:
          count_digits = count_digits + 1
        resp = resp + number_str[i]
        if count_digits == digits:
            break
      return float(resp)
    else:
      return round(number)
