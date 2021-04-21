# 기본 룰 설명하는 타이밍이 있어야함
# 돈을 다 잃을 때까지 진행
# 딜러와 플레이어가 동시에 버스트가 되어도 플레이어 패배
# 딜러는 17미만일 경우 카드를 더 뽑아야함
# 스플릿 없음
# 컴퓨터의 랜덤 함수는 일반적으로 완벽하게 랜덤할 수가 없다고 생각함

import random

deck = ['1', '1', '1', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4',
        '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8',
        '9', '9', '9', '9', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K',
        'A', 'A', 'A', 'A']

myMoney = 1000
count_card = 51
# 딜러가 A를 갖는 경우의 수 모두를 계산해주기 위해 총합 계산하는 결과값은 2가지를 줌
D_total_Sum1ver = 0
D_total_Sum11ver = 0
finaldealerDeck = []
# 플레이어 덱 총합 변환 코드
def checkCard(define):
    if define == 'J':
        return 10
    elif define == 'Q':
        return 10
    elif define == 'K':
        return 10
    elif define == 'A':
        print("A를 1과 11 둘중 하나로 사용할 수 있습니다\n 어느쪽으로 사용하시겠습니까?")
        ans = int(input())
        if ans == 1:
            return 1
        else:
            return 11

    else: return int(define)

# 딜러와 플레이어는 서로 한장씩 카드를 번갈아 가며 뽑아야 공평하다
def playerAndDealer():
    global myMoney, count_card, D_total_Sum1ver, D_total_Sum11ver, finaldealerDeck


    print("현재 보유 금액 >>>", myMoney)
    print("<System> 베팅 금액을 입력하십시오 >>> ", end='')
    playerDeck = []
    dealerDeck = []
    finaldealerDeck = []

    betMoney = int(input())


    def dealerDraw():
        global count_card
        D_card = deck[random.randint(0, count_card)]
        deck.remove(D_card)
        dealerDeck.append(D_card)
        finaldealerDeck.append(D_card)
        count_card -= 1


    def playerDraw():
        global count_card
        P_card = deck[random.randint(0, count_card)]
        deck.remove(P_card)
        playerDeck.append(P_card)
        count_card -= 1


    # 카드 드로우 순서는 플레이어 - 딜러 순으로 번갈아가며 2번 뽑는다
    # 첫번째 드로우
    playerDraw()
    dealerDraw()

    # 두번째 드로우
    playerDraw()
    dealerDraw()

    print("※현재 플레이어 카드 >>>", playerDeck)
    print("※현재 딜러의 첫번째 카드 >>>", dealerDeck[0], '\n')
    print("※현재 딜러의 두번째 카드 >>>", dealerDeck[1], '\n')

    # 블랙잭 실제 플레이 영상을 참고했는데 플레이어의 카드를 보고나서 플레이어가 더 먹을지 말지 선택을 함
    # 딜러가 추가 드로우하는 타이밍은 따로 있었음
    # 또한 딜러의 카드 한장을 볼 수 있음
    # 플레이어 추가 드로우 while문
    while True:
        print("<System> 더 뽑으시겠습니까?\n (1) 예 / (2) 아니오")
        ans = int(input())

        if ans == 1:
            playerDraw()
            print("현재 플레이어 카드 >>>", playerDeck)

        elif ans == 2: break

    blackjack = 0
    # 플레이어 점수 변환
    playerTotal = 0
    for card in playerDeck:
        cardToScore = checkCard(card)
        playerTotal += cardToScore

    print("<System> 플레이어의 총합 >>>", playerTotal)

    if playerTotal == 21:
        print("<System> 블랙잭입니다!\n") # 블랙잭이면 1.5배를 바음
        blackjack = 1
        betMoney = int(betMoney * 1.5)

    elif playerTotal > 22:
        print("<System> 플레이어 버스트\n")


    D_total_Sum1ver, D_total_Sum11ver = 0, 0
    def checkCardForDealer(define):
        global D_total_Sum1ver, D_total_Sum11ver

        if define == 'J':
            D_total_Sum1ver += 10
            D_total_Sum11ver += 10
            return [D_total_Sum1ver, D_total_Sum11ver]

        elif define == 'Q':
            D_total_Sum1ver += 10
            D_total_Sum11ver += 10
            return [D_total_Sum1ver, D_total_Sum11ver]

        elif define == 'K':
            D_total_Sum1ver += 10
            D_total_Sum11ver += 10
            return [D_total_Sum1ver, D_total_Sum11ver]

        elif define == 'A':
            D_total_Sum1ver += 1
            D_total_Sum11ver += 11
            return [D_total_Sum1ver, D_total_Sum11ver]

        else:
            trnas = int(define)
            D_total_Sum1ver += trnas
            D_total_Sum11ver += trnas
            return [D_total_Sum1ver, D_total_Sum11ver]

    print("딜러 카드 체크", dealerDeck)
    for card in dealerDeck:
        checkCardForDealer(card)


    tempList = [D_total_Sum1ver, D_total_Sum11ver]

    print("더해진 값 체크", tempList)
    # 딜러 추가 드로우

    for score in tempList:
        break

    # 딜러는 항상 17 미만일 경우 추가 드로우를 해야한다
    # 이떈 직접 하나 드로우
    transToScore = []
    while True :
        if score >= 17:
            fir = tempList[0]
            sec = tempList[1]
            break

        elif score < 17:

            D_card = deck[random.randint(0, count_card)]
            print(D_card)
            deck.remove(D_card)
            finaldealerDeck.append(D_card)
            count_card -= 1
            transToScore = checkCardForDealer(D_card)

            m1 = transToScore[0]
            m2 = transToScore[1]
            transToScore.clear()

            transToScore.append(m1)
            transToScore.append(m2)

            # if 17 <= transToScore[0] or transToScore[1] <= 21:
            #     print(transToScore)
            #     fir = transToScore[0]
            #     sec = transToScore[1]
            #     break
            if transToScore[0] >= 17:
                print(transToScore)
                fir = transToScore[0]
                sec = transToScore[1]
                break
            elif 17 <= transToScore[1] <= 21:
                print(transToScore)
                fir = transToScore[0]
                sec = transToScore[1]
                break




    dealerTotal = 0
    print("딜러의 패 >>>", finaldealerDeck)
    if fir > 21:
        print("딜러의 총합 >>>", fir)
        dealerTotal = fir
    elif fir <= 21:
        if fir == sec:
            print("딜러의 총합 >>>", fir)
            dealerTotal = fir
        else:
            if sec > 21:
                print("딜러의 총합 >>>", fir)
                dealerTotal = fir
            else:
                print("딜러의 총합 >>>", sec)
                dealerTotal = sec


    if playerTotal > 21:
        print("<<플레이어 버스트, 패배했습니다>>")
        myMoney -= betMoney
    elif playerTotal <= 21 and dealerTotal > 21:
        print("<<플레이어의 승리>>")
        myMoney += betMoney
    elif playerTotal <= 21:
        if playerTotal == dealerTotal:
            print("<<무승부, 베팅한 금액을 돌려받습니다>>")
        elif playerTotal > dealerTotal:
            print("<<플레이어의 승리>>")
            myMoney += betMoney
        elif playerTotal < dealerTotal:
            print("<<딜러의 승리>>")
            myMoney -= betMoney

    print()
    print("현재 잔액 >>>", myMoney)
    print(count_card)


#플레이 시작
while True:
    print("<System> 엔터를 치면 새 게임을 시작합니다")
    input()
    playerAndDealer()
    count_card = 51
    deck = ['1', '1', '1', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4',
            '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8',
            '9', '9', '9', '9', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K',
            'A', 'A', 'A', 'A']
    if myMoney == 0:
        print('<System> 당신은 파산하였습니다')
        break
    else: pass
