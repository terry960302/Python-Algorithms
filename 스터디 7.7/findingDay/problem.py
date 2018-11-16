import datetime
import solution

def checking_answer(y,m,d,user_answer):
	day_dic = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN' }#요일을 숫자로 표현
	day_num = datetime.date(y,m,d).weekday() #년,월,일 입력하면 숫자로 요일나옴
	print(day_dic[day_num],user_answer) #만든 함수와 당신의 답을 출력
	if day_dic[day_num] == user_answer:
		return 1   #서로 답이 같으면 1출력
	else:
		return 0    # 틀리면 0출력

if __name__ == '__main__':
	problem_list = [[1,1,2],[1900,2,28],[505,10,11],[2100,2,28],[8888,2,29],[1000,9,12],[4008,1,30],[9999,7,22],[2018,7,6],[1234,4,30]]
	score = 0
	for i in range(10):
		if checking_answer(problem_list[i][0],problem_list[i][1],problem_list[i][2],solution.your_answer(problem_list[i][0],problem_list[i][1],problem_list[i][2])) == 1:
                                #문제리스트에 있는 거 년,월,일 입력했을 때 정답인지
			print(str(i+1)+"번 문제 통과 (number",str(i+1),"problem success)")

			score += 10 #다맞으면 100
		else:
			print(str(i+1)+"번 문제 실패 (number",str(i+1),"problem fail)")
			
	print("점수:",str(score),"(score:",str(score)+")")
