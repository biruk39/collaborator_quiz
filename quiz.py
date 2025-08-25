

print("===================================")
print("   Quiz Question     " )
def run_quiz():
    print("===================================")
    print("       Welcome to the  Quiz     ")
    print("===================================")

    
    name = input("Enter your full name: ").strip()
    student_id = input("Enter your ID number: ").strip()
    print(f"\nWelcome {name} (ID: {student_id})!")
    print("You will answer 20 questions per subject.")
    print("Each correct answer = 1 mark. Marks are shown immediately.\n")

    
    quiz = {
        "Physics": [
            {"question": "What is the speed of light in vacuum (m/s)?\n(a) 3x10^8\n(b) 3x10^6\n(c) 3x10^5\n(d) 3x10^7", "answer": "a"},
            {"question": "Force = mass x ?\n(a) Velocity\n(b) Acceleration\n(c) Momentum\n(d) Energy", "answer": "b"},
            {"question": "Unit of electric current?\n(a) Ampere\n(b) Volt\n(c) Ohm\n(d) Watt", "answer": "a"},
            {"question": "Who formulated the law of gravitation?\n(a) Newton\n(b) Einstein\n(c) Galileo\n(d) Faraday", "answer": "a"},
            {"question": "SI unit of power?\n(a) Joule\n(b) Watt\n(c) Newton\n(d) Pascal", "answer": "b"},
            {"question": "Acceleration due to gravity on Earth?\n(a) 9.8 m/s^2\n(b) 10 m/s^2\n(c) 9 m/s^2\n(d) 8 m/s^2", "answer": "a"},
            {"question": "Unit of frequency?\n(a) Hz\n(b) Nm\n(c) Pascal\n(d) Tesla", "answer": "a"},
            {"question": "Light year is a measure of?\n(a) Time\n(b) Distance\n(c) Energy\n(d) Mass", "answer": "b"},
            {"question": "Which color has highest wavelength?\n(a) Violet\n(b) Blue\n(c) Red\n(d) Green", "answer": "c"},
            {"question": "What is Ohm's Law?\n(a) V=IR\n(b) P=VI\n(c) F=ma\n(d) E=mc^2", "answer": "a"},
            {"question": "Unit of pressure?\n(a) Pascal\n(b) Watt\n(c) Joule\n(d) Volt", "answer": "a"},
            {"question": "Energy possessed by a body due to motion?\n(a) Potential\n(b) Kinetic\n(c) Thermal\n(d) Chemical", "answer": "b"},
            {"question": "Unit of work?\n(a) Newton\n(b) Joule\n(c) Watt\n(d) Pascal", "answer": "b"},
            {"question": "Formula for density?\n(a) Mass/Volume\n(b) Volume/Mass\n(c) Mass x Volume\n(d) Mass + Volume", "answer": "a"},
            {"question": "Which particle has negative charge?\n(a) Proton\n(b) Neutron\n(c) Electron\n(d) Photon", "answer": "c"},
            {"question": "Unit of magnetic field?\n(a) Tesla\n(b) Newton\n(c) Ampere\n(d) Ohm", "answer": "a"},
            {"question": "Who discovered X-rays?\n(a) Rutherford\n(b) Roentgen\n(c) Maxwell\n(d) Newton", "answer": "b"},
            {"question": "Unit of electric charge?\n(a) Coulomb\n(b) Volt\n(c) Ampere\n(d) Ohm", "answer": "a"},
            {"question": "Wave that can travel in vacuum?\n(a) Sound\n(b) Light\n(c) Water\n(d) Seismic", "answer": "b"},
            {"question": "SI unit of temperature?\n(a) Celsius\n(b) Kelvin\n(c) Fahrenheit\n(d) Joule", "answer": "b"}
        ],
        #this part is done by biruk daniel
 "Chemistry": [
            {"question": "Chemical symbol for gold?\n(a) Au\n(b) Ag\n(c) Go\n(d) Gd", "answer": "a"},
            {"question": "pH of pure water?\n(a) 7\n(b) 0\n(c) 14\n(d) 1", "answer": "a"},
            {"question": "Atomic number of Hydrogen?\n(a) 1\n(b) 2\n(c) 3\n(d) 4", "answer": "a"},
            {"question": "Chemical formula of water?\n(a) H2O\n(b) CO2\n(c) O2\n(d) H2", "answer": "a"},
            {"question": "Gas in balloons?\n(a) Oxygen\n(b) Nitrogen\n(c) Helium\n(d) Carbon dioxide", "answer": "c"},
            {"question": "NaCl is?\n(a) Acid\n(b) Base\n(c) Salt\n(d) Sugar", "answer": "c"},
            {"question": "Periodic table is by?\n(a) Newton\n(b) Mendeleev\n(c) Einstein\n(d) Bohr", "answer": "b"},
            {"question": "Solvent in salt water?\n(a) Salt\n(b) Water\n(c) Sugar\n(d) Alcohol", "answer": "b"},
            {"question": "HCl is?\n(a) Acid\n(b) Base\n(c) Salt\n(d) Alcohol", "answer": "a"},
            {"question": "NaOH is?\n(a) Acid\n(b) Base\n(c) Salt\n(d) Sugar", "answer": "b"},
            {"question": "O2 is?\n(a) Oxygen\n(b) Carbon dioxide\n(c) Nitrogen\n(d) Hydrogen", "answer": "a"},
            {"question": "C6H12O6 is?\n(a) Glucose\n(b) Salt\n(c) Water\n(d) Alcohol", "answer": "a"},
            {"question": "Strongest acid?\n(a) HCl\n(b) H2SO4\n(c) HNO3\n(d) HF", "answer": "b"},
            {"question": "Noble gases are?\n(a) Reactive\n(b) Inert\n(c) Acidic\n(d) Basic", "answer": "b"},
            {"question": "Atomic mass unit?\n(a) kg\n(b) amu\n(c) g\n(d) m", "answer": "b"},
            {"question": "Chemical reaction of photosynthesis?\n(a) CO2 + H2O → O2 + Glucose\n(b) O2 + H2 → H2O\n(c) C + O2 → CO2\n(d) HCl + NaOH → NaCl + H2O", "answer": "a"},
            {"question": "Boiling point of water?\n(a) 100°C\n(b) 90°C\n(c) 110°C\n(d) 120°C", "answer": "a"},
            {"question": "Mol is unit of?\n(a) Mass\n(b) Amount of substance\n(c) Volume\n(d) Pressure", "answer": "b"},
            {"question": "Acid + Base = ?\n(a) Water\n(b) Salt\n(c) Both\n(d) None", "answer": "c"},
            {"question": "Electrolytes conduct?\n(a) Heat\n(b) Electricity\n(c) Sound\n(d) Light", "answer": "b" }
 ],
        #this part is done by nesiha nurselam

        "Math": [
            {"question": "What is 5 + 3?\n(a) 6\n(b) 7\n(c) 8\n(d) 9", "answer": "c"},
            {"question": "What is 9 - 4?\n(a) 3\n(b) 5\n(c) 6\n(d) 7", "answer": "b"},
            {"question": "What is 6 × 2?\n(a) 12\n(b) 10\n(c) 14\n(d) 8", "answer": "a"},
            {"question": "What is 15 ÷ 3?\n(a) 4\n(b) 5\n(c) 6\n(d) 3", "answer": "b"},
            {"question": "What is the square of 4?\n(a) 8\n(b) 12\n(c) 16\n(d) 20", "answer": "c"},
            {"question": "What is 10 + 5?\n(a) 15\n(b) 14\n(c) 13\n(d) 16", "answer": "a"},
            {"question": "What is 7 × 3?\n(a) 21\n(b) 24\n(c) 18\n(d) 27", "answer": "a"},
            {"question": "What is 20 - 8?\n(a) 10\n(b) 11\n(c) 12\n(d) 13", "answer": "c"},
            {"question": "What is 9 + 6?\n(a) 14\n(b) 15\n(c) 16\n(d) 17", "answer": "b"},
            {"question": "What is 12 ÷ 4?\n(a) 2\n(b) 3\n(c) 4\n(d) 6", "answer": "b"},
            {"question": "What is 3 squared?\n(a) 6\n(b) 9\n(c) 12\n(d) 3", "answer": "b"},
            {"question": "What is 8 + 7?\n(a) 14\n(b) 15\n(c) 16\n(d) 17", "answer": "b"},
            {"question": "What is 14 - 9?\n(a) 3\n(b) 4\n(c) 5\n(d) 6", "answer": "c"},
            {"question": "What is 2 × 5?\n(a) 10\n(b) 12\n(c) 8\n(d) 6", "answer": "a"},
            {"question": "What is 18 ÷ 2?\n(a) 9\n(b) 8\n(c) 10\n(d) 7", "answer": "a"},
            {"question": "What is 11 + 4?\n(a) 14\n(b) 15\n(c) 16\n(d) 13", "answer": "b"},
            {"question": "What is 16 - 7?\n(a) 8\n(b) 9\n(c) 10\n(d) 11", "answer": "b"},
            {"question": "What is 5 × 5?\n(a) 20\n(b) 25\n(c) 30\n(d) 35", "answer": "b"},
            {"question": "What is 6 + 9?\n(a) 14\n(b) 15\n(c) 16\n(d) 17", "answer": "b"},
            {"question": "What is 10 ÷ 2?\n(a) 4\n(b) 5\n(c) 6\n(d) 7", "answer": "b"}
        ],
# this part is done by hikma mohammed

"Biology": [
            {"question": "The powerhouse of the cell?\n(a) Nucleus\n(b) Mitochondria\n(c) Ribosome\n(d) Chloroplast", "answer": "b"},
            {"question": "Human blood type universal donor?\n(a) O+\n(b) AB+\n(c) O-\n(d) A+", "answer": "c"},
            {"question": "Largest organ in human body?\n(a) Heart\n(b) Skin\n(c) Liver\n(d) Brain", "answer": "b"},
            {"question": "Basic unit of life?\n(a) Atom\n(b) Cell\n(c) Tissue\n(d) Organ", "answer": "b"},
            {"question": "Which vitamin is from sunlight?\n(a) A\n(b) B\n(c) C\n(d) D", "answer": "d"},
            {"question": "Humans have how many chromosomes?\n(a) 46\n(b) 44\n(c) 48\n(d) 42", "answer": "a"},
            {"question": "Process of making food in plants?\n(a) Respiration\n(b) Photosynthesis\n(c) Digestion\n(d) Fermentation", "answer": "b"},
            {"question": "What carries oxygen in blood?\n(a) Plasma\n(b) Red blood cells\n(c) Platelets\n(d) WBC", "answer": "b"},
            {"question": "Smallest blood vessels?\n(a) Veins\n(b) Arteries\n(c) Capillaries\n(d) Venules", "answer": "c"},
            {"question": "Where is DNA found?\n(a) Ribosome\n(b) Nucleus\n(c) Cytoplasm\n(d) Cell membrane", "answer": "b"},
            {"question": "Humans have how many senses?\n(a) 4\n(b) 5\n(c) 6\n(d) 7", "answer": "b"},
            {"question": "Which blood cells fight infection?\n(a) RBC\n(b) WBC\n(c) Platelets\n(d) Plasma", "answer": "b"},
            {"question": "Plant cells have?\n(a) Cell wall\n(b) Chloroplast\n(c) Vacuole\n(d) All", "answer": "d"},
            {"question": "Largest bone in human body?\n(a) Femur\n(b) Tibia\n(c) Humerus\n(d) Skull", "answer": "a"},
            {"question": "Human heart has how many chambers?\n(a) 2\n(b) 3\n(c) 4\n(d) 5", "answer": "c"},
            {"question": "Process of cell division?\n(a) Mitosis\n(b) Meiosis\n(c) Fertilization\n(d) Both a and b", "answer": "d"},
            {"question": "Organ for respiration?\n(a) Heart\n(b) Lungs\n(c) Kidney\n(d) Liver", "answer": "b"},
            {"question": "Smallest unit of an element?\n(a) Atom\n(b) Molecule\n(c) Cell\n(d) Electron", "answer": "a"},
            {"question": "Blood clotting cells?\n(a) RBC\n(b) WBC\n(c) Platelets\n(d) Plasma", "answer": "c"},
            {"question": "Process of breaking down food?\n(a) Digestion\n(b) Photosynthesis\n(c) Respiration\n(d) Excretion", "answer": "a"}
        ],
