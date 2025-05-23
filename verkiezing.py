class Kandidaat:
    def __init__(self, naam):
        self.naam = naam
        self.stemmen = []

    def geef_stem(self, stem):
        self.stemmen.append(stem)

    def __str__(self):
        return f"{self.naam}"
    
class Stem:
    def __init__(self, kandidaat):
        self.kandidaat = kandidaat

    def __str__(self):
        return f"Stem op {self.kandidaat}"
    
class Kiezer:
    def __init__(self, naam):
        self.naam = naam


    def stem(self, kandidaat):
        stem = Stem(kandidaat)
        kandidaat.geef_stem(stem)
        print(f"{self.naam} heeft gestemd op {kandidaat}")

lijst_van_kandidaten = [
    RectorKandidaat("Eren", "Natuurkunde"),
    RectorKandidaat("Fran", "Wiskunde")
    RectorKandidaat("Barbara", "Scheikunde"),
    RectorKandidaat("Tim", "Biologie"),
    RectorKandidaat("Lander", "Informatica")
]
lijst_kiezers = [
    RectorKiezer("Mama", "Wiskunde"),
    RectorKiezer("Zus", "Natuurkunde")]

for kiezer in lijst_kiezers:
    kandidaatnummer = random.randint(0, len(lijst_van_kandidaten)-1)
    kiezer.stem(lijst_van_kandidaten[kandidaatnummer])
        