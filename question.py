class Question:
    def __init__(self,question_text,correct_ans):
        self.question_text=question_text
        self.correct_ans=correct_ans
    


    def check_answer(self,answer):
        return self.correct_ans.upper()==answer.upper()



def get_questions():
    return [
    Question("What is the SI unit of force? (One word)", "Newton"),
    Question("What is the rate of change of velocity called? (One word)", "Acceleration"),
    Question("What type of wave is sound in air? (One word)", "Longitudinal"),
    Question("What is the property of a body that resists any change in its state of motion? (One word)", "Inertia"),
    Question("What is the device that converts mechanical energy into electrical energy? (One word)", "Generator"),
    Question("What is the phenomenon where light bends as it passes through a different medium? (One word)", "Refraction"),
    Question("What is the energy stored in a stretched or compressed spring? (One word)", "Elasticity"),
    Question("What is the smallest particle of an element that retains its properties? (One word)", "Atom"),
    Question("What is the term for the attraction between two masses? (One word)", "Gravity"),
    Question("What is the measure of disorder in a system called? (One word)", "Entropy"),
    Question("What is the phenomenon of splitting white light into its component colors? (One word)", "Dispersion"),
    Question("What is the unit of electric charge? (One word)", "Coulomb"),
    Question("What is the force that opposes motion between two surfaces in contact? (One word)", "Friction"),
    Question("What is the rate of doing work? (One word)", "Power"),
    Question("What is the potential energy stored in an object due to its height? (One word)", "Gravitational"),

           
    ]
