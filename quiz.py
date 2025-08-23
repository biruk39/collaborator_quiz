

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
    }

