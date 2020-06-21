class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행(야시장 투어 ) 50만원")
if __name__== "__main__" :
    print("thailand 모듈 직접실행")
    print("이 문장은 직접실행 될때만 적용됩니다.")
    trip_to =ThailandPackage()
    trip_to.detail()
else :
    print('thailand 외부에서 호출 ')
