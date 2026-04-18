class SozUzunligi:
    def __init__(self, matn):
        self.matn = matn
        self.sozlaringiz = matn.split()

    def eng_uzun_soz(self):
        sozlar_uzunligi = [len(soz) for soz in self.sozlaringiz]
        maks_uzunlik = max(sozlar_uzunligi)
        eng_uzun_soz = [soz for soz in self.sozlaringiz if len(soz) == maks_uzunlik]
        return eng_uzun_soz, maks_uzunlik

    def eng_qisqa_soz(self):
        sozlar_uzunligi = [len(soz) for soz in self.sozlaringiz]
        min_uzunlik = min(sozlar_uzunligi)
        eng_qisqa_soz = [soz for soz in self.sozlaringiz if len(soz) == min_uzunlik]
        return eng_qisqa_soz, min_uzunlik

    def chiqarish(self):
        eng_uzun_soz, eng_uzun_uzunlik = self.eng_uzun_soz()
        eng_qisqa_soz, eng_qisqa_uzunlik = self.eng_qisqa_soz()
        print("Matn:", self.matn)
        print("Eng uzun so'z(lar):", eng_uzun_soz)
        print("Eng uzun so'zlar uzunligi:", eng_uzun_uzunlik)
        print("Eng qisqa so'z(lar):", eng_qisqa_soz)
        print("Eng qisqa so'zlar uzunligi:", eng_qisqa_uzunlik)


def main():
    matn = input("Matn kiriting: ")
    soz_uzunligi = SozUzunligi(matn)
    soz_uzunligi.chiqarish()


if __name__ == "__main__":
    main()

class SozUzunligiTest:
    def __init__(self):
        self.test_matn = "Bu bir test matni"

    def run_test(self):
        test_soz_uzunligi = SozUzunligi(self.test_matn)
        test_soz_uzunligi.chiqarish()


if __name__ == "__main__":
    main()
    test = SozUzunligiTest()
    test.run_test()