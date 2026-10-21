"""원본 CSV → 호흡기(J코드) 청구 데이터 추출 → dashboard_template.html 에 내장 → 청구_대시보드.html
실행: python build_dashboard.py  (같은 폴더에 CSV 10개 필요)
"""
import json
from pathlib import Path
import pandas as pd

HERE = Path(__file__).parent
rd = lambda n: pd.read_csv(HERE / f'{n}.csv', dtype=str)

claim, pat, inst = rd('claim'), rd('patient'), rd('institution')
rx, drug, sick = rd('claim_rx'), rd('drug_ingredient'), rd('sick_master')
codes, sido = rd('code_table'), rd('sido_code')

# 호흡기 = 주상병이 J로 시작
c = claim[claim.main_sick.str.startswith('J')].copy()
for k in ['rvd_rpe_tamt_amt', 'rvd_slf_brdn_amt', 'rvd_insup_brdn_amt', 'recu_ddcnt']:
    c[k] = pd.to_numeric(c[k])
c = c.merge(pat, on='jid').merge(inst, on='yid', suffixes=('', '_i'))
c['year'] = c.recu_fr_dd.str[:4].astype(int)
c['month'] = (c.year - 2024) * 12 + c.recu_fr_dd.str[5:7].astype(int) - 1
age = c.year - c.birth_yr.astype(int)
c['age'] = pd.cut(age, [-100, 6, 18, 64, 200], labels=[0, 1, 2, 3]).astype(int)
c['form'] = (c.fom_tp_cd == '021').astype(int)

CL = ['01', '11', '21', '31']
c['cl'] = c.cl_cd.map({k: i for i, k in enumerate(CL)})
sido = sido.sort_values('sido_cd')
SIDO = sido.sido_cd.tolist()
c['sido'] = c.sido_cd.map({k: i for i, k in enumerate(SIDO)})
# 소득층: 0=의료급여(5분위 없음), 1~5=보험료 5분위
c['q'] = pd.to_numeric(c.prem_quintile).fillna(0).astype(int)
DEPT = sorted(c.dgsbjt_cd.unique())
c['dept'] = c.dgsbjt_cd.map({k: i for i, k in enumerate(DEPT)})


def sub_of(code):
    n = int(code[1:3])
    if n <= 6: return 0
    if 9 <= n <= 18: return 1
    if 20 <= n <= 22: return 2
    if 30 <= n <= 39: return 3
    if 40 <= n <= 47: return 4
    return 5


SUB = ['급성 상기도(J00–J06)', '인플루엔자·폐렴(J09–J18)', '급성 하기도(J20–J22)',
       '알레르기비염 등 상기도(J30–J39)', '만성 하기도(J40–J47)', '기타 호흡기']
SICK = sorted(c.main_sick.unique())
c['sub'] = c.main_sick.map(sub_of)
c['sick'] = c.main_sick.map({k: i for i, k in enumerate(SICK)})

# 청구별 처방
c = c.reset_index(drop=True)
idx = dict(zip(c.mid, c.index))
r = rx[rx.mid.isin(idx)].copy()
r['amt'] = pd.to_numeric(r.amt)
r = r.merge(drug[['gnl_cd', 'gnl_nm', 'class_no']], on='gnl_cd', how='left')
GNL = sorted(r.gnl_cd.unique())
r['g'] = r.gnl_cd.map({k: i for i, k in enumerate(GNL)})
r['ci'] = r.mid.map(idx)
c['rxamt'] = c.index.map(r.groupby('ci').amt.sum()).fillna(0).astype(int)
c['hasrx'] = c.index.isin(r.ci).astype(int)

cn = lambda t: dict(codes[codes.code_type == t][['code', 'code_nm']].values)
cols = ['year', 'month', 'age', 'dept', 'form', 'cl', 'region_cd', 'sido', 'q', 'sub', 'sick',
        'rvd_rpe_tamt_amt', 'rvd_slf_brdn_amt', 'rvd_insup_brdn_amt', 'rxamt', 'hasrx', 'recu_ddcnt']
gname = drug.set_index('gnl_cd')
data = {
    'cols': ['year', 'month', 'age', 'dept', 'form', 'cl', 'reg', 'sido', 'q', 'sub', 'sick',
             'tot', 'slf', 'ins', 'rx', 'hasrx', 'days'],
    'rows': c[cols].astype(int).values.tolist(),
    'rx': r[['ci', 'g', 'amt']].astype(int).values.tolist(),
    'cl': [cn('종별코드')[k] for k in CL],
    'dept': [cn('진료과목코드')[k] for k in DEPT],
    'sido': sido.sido_nm.tolist(),
    'sidoReg': sido.region_cd.astype(int).tolist(),
    'region': {int(k): v for k, v in sido.drop_duplicates('region_cd')[['region_cd', 'region_nm']].values},
    'sub': SUB,
    'sick': [[k, sick.set_index('sickcd').krnm.get(k, k)] for k in SICK],
    'gnl': [[k, gname.gnl_nm[k], gname.class_no[k]] for k in GNL],
    'total_claims': len(claim),
    'total_amt': int(pd.to_numeric(claim.rvd_rpe_tamt_amt).sum()),
}
payload = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
html = (HERE / 'dashboard_template.html').read_text(encoding='utf-8').replace('/*__DATA__*/null', payload)
out = HERE / '청구_대시보드.html'
out.write_text(html, encoding='utf-8')
print(f'호흡기 청구 {len(c):,}건, 처방 {len(r):,}줄 → {out.name} ({out.stat().st_size/1024:.0f} KB)')
