
# 함수이름 수정하지 말 것
# don't modify function name

import datetime, time
def your_answer(y,m,d):
        
        day_dic = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN' }
	result= day_dic[datetime.date(y,m,d).weekday()]
	
	return result

#main
