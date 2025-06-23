import random
from datetime import date, timedelta

WEEK_SHIFTS = {
    0: ['A3','H5','D6','D7','S2','N','D**','D**','D**','D*','M台','T台','W7','E6','E*'],
    1: ['A3','P5','D6','D7','S2','N','D**','D**','D**','D*','M台','T台','W7','E6','E*'],
    2: ['A3','H5','D6','D7','S2','N','D**','D**','D**','D*','M台','T台','W7','E6','E*'],
    3: ['A3','H5','D6','D7','S2','N','D**','D**','D**','D*','M台','T台','W7','E6','E*'],
    4: ['A3','P5','D6','D7','S2','N','D**','D**','D**','D*','M台','T台','W7','E6','E*'],
    5: ['A3','I3','D6','Y7','D*','E6','E*','N'],
    6: ['D6','D*','E6','E*','N']
}

def generate_schedule(employees, weeks=1):
    def legal(assign, emp, day_idx):
        if sum(1 for d,s,e in assign if e==emp and abs((d-day_idx).days)<=6)==7:
            return False
        return True

    result = []
    today = date.today()
    history = {emp:[] for emp in employees}

    for w in range(weeks):
        for weekday in range(7):
            day = today + timedelta(days=w*7+weekday)
            shifts = WEEK_SHIFTS[weekday].copy()
            random.shuffle(shifts)
            for shift in shifts:
                for emp in employees:
                    if emp in [e for d,s,e in result if d==day and s==shift]:
                        continue
                    if weekday>=5 and emp in history and any(d.weekday()>=5 and e==emp for d,s,e in result if d==day):
                        continue
                    if not legal(result, emp, day):
                        continue
                    if shift in ('E6','E*'):
                        slots = len([1 for d,s,e in result if s==shift])
                        if slots >= (len(employees)*weeks)//2:
                            continue
                    result.append((day, shift, emp))
                    history[emp].append(day)
                    break
    return [{'日期': rec[0].strftime("%Y-%m-%d"), '班別': rec[1], '員工': rec[2]} for rec in result]
