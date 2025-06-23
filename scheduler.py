from utils import generate_schedule
import pandas as pd
import os
from datetime import date

def main():
    df_raw = pd.DataFrame(sched)
dupes = df_raw[df_raw.duplicated(subset=['員工', '日期'], keep=False)]
if not dupes.empty:
    print("⚠️ 發現重複班別資料：")
    print(dupes)
    employees = ['芷芸','婷瑩','冠汝','芬萍','勇得','婉霏','鈺姍','欣怡','文雄','詣勛','俊穎','琦葳','乙玲','宛淇','惠琳','丁丁']
    sched = generate_schedule(employees, weeks=1)
    df = pd.DataFrame(sched).pivot_table(
    index='員工',
    columns='日期',
    values='班別',
    aggfunc=lambda x: ' / '.join(x)  # 把同一天的班別合併起來
).fillna('')
    fname = f"output/schedule_{date.today()}.xlsx"
    df.to_excel(fname)
    print("✅ 排班完成，檔案：", fname)

if __name__ == "__main__":
    main()
