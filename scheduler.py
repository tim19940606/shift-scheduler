from utils import generate_schedule
import pandas as pd
import os
from datetime import date

def main():
    employees = ['芷芸','婷瑩','冠汝','芬萍','勇得','婉霏','鈺姍','欣怡',
                 '文雄','詣勛','俊穎','琦葳','乙玲','宛淇','惠琳','丁丁']
    sched = generate_schedule(employees, weeks=1)
    df_raw = pd.DataFrame(sched)
    print("📋 原始排班資料（前10筆）：")
    print(df_raw.head(10))
    dupes = df_raw[df_raw.duplicated(subset=['員工', '日期'], keep=False)]
    if not dupes.empty:
        print("⚠️ 發現重複班別（同一人同一日）：")
        print(dupes)

    try:
        df = df_raw.pivot_table(
            index='員工',
            columns='日期',
            values='班別',
            aggfunc=lambda x: ' / '.join(x)
        ).fillna('')
    except Exception as e:
        print("❌ 轉換表格失敗：", e)
        return

    os.makedirs('output', exist_ok=True)
    fname = f"output/schedule_{date.today()}.xlsx"
    df.to_excel(fname)
    print("✅ 排班完成，已輸出檔案：", fname)

if __name__ == "__main__":
    main()
