#스타크래프트 테란 으로 비유
class Unit:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage
        print('{} 유닛이 생성되엇습니다.'.format(self.name))
        print('체력 {}, 공격력 {}'.format(self.hp ,self.damage))

class atkUnit:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage

    def attack(self, location):
        print('{0}:{1} 방향으로 공격합니다.[공격력{2}]'\
        .format(self.name,location,self.damage))

    def damaged(self,damage):
        print('{}:{}데미지를 입엇습니다.'.format(self.name,damage))
        self.hp-=damage
        if self.hp <= 0:
            print('유닛이 파괴되엇습니다. :/')

marine1 = Unit("marine",50,14)
tank = Unit("tank",200,30)

# 객체 임의확장
wraith=atkUnit("빼앗은 레이스",200,14)
wraith.clocking= True

## wraith 값에만 clocking 이라는 매게변수가 추가됨

firebat1 = atkUnit("파이어뱃",50,16)
firebat1.damaged(50)
