import re

# findall() - 찾은 문자열을 리스트로 반환
text = "오늘은 2026-09-02입니다. 내일은 2026-09-03입니다"
reg_exp = r"\d{4}-\d{2}-\d{2}"

dates = re.findall(reg_exp, text)
print("날짜 목록: ", dates) #['2026-09-02', '2026-09-03']
# print(dates[0])
for date in dates:
    print(date)

# sub() - 마스킹 처리
pattern = r"\d{3}-\d{4}-\d{4}"
text = "내 전화번호는 010-1234-5678입니다."
masked_text = re.sub(pattern, "xxx-xxxx-xxxx", text)
print(masked_text)

# 주민번호 뒷자리 마스킹 예제
ssn = "950101-3234567"
ssn_pattern = r"(\d{6})-(\d)\d{6}"
masked_ssn = re.sub(ssn_pattern, r"\1-\2******", ssn)
print("주민번호 마스킹:", masked_ssn)  # 950101-1******

# 예제
print(re.sub('\d', '*', 'a1b2c3')) #a*b*c*