from experta import *
import customtkinter as ctk
##########################################################################
#                                 GUI                                    #
##########################################################################
app = ctk.CTk()
app.geometry("900x600")
app.title("Mental Disorder Diagnose Expert System")

# Set the theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

width_button = 150
height_button = 40
font_button_size = 16
wraplength_label = 700

label_title = ctk.CTkLabel(
    app, 
    text="Mental Disorder Diagnose Expert System", 
    font=ctk.CTkFont(size=24, weight="bold")
)
label_title.pack(pady=20)

question_text = ctk.StringVar()

new_window = None

##########################################################################
#                           Expert System                                #
##########################################################################
class Question(Fact):
    id = Field(int, mandatory=True)
    content = Field(str, mandatory=True)
    characteristics = Field(list, mandatory=True)
    certaintyFactor = Field(float, mandatory=True)
    isAsked = Field(bool, mandatory=True, default=False)

class Characteristic(Fact):
    label = Field(str, mandatory=True)
    significance = Field(float, mandatory=True)

class Disorder(Fact):
    label = Field(str, mandatory=True)
    number_of_asked_question = Field(int, default=0)

class MyKnowledgeEngine(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.display_intro = True
        self.question_number = 0
        self.super_certainty = 1.0
        self.chars = []
        self.is_main_question = True
    
    @DefFacts()
    def initialize(self):
        yield Disorder(label="Dissociative Disorders")
        yield Disorder(label="Schizophrenia")
        yield Disorder(label="Bipolar Disorder")
        yield Disorder(label="Depressive Disorders")
        yield Disorder(label="ADHD")
        yield Disorder(label="Autism")
        yield Disorder(label="Anxiety Disorders")
        yield Disorder(label="OCD")
        yield Disorder(label="Somatic Disorders")
        yield Disorder(label="Feeding Disorders")
        yield Disorder(label="Disruptive, Impulse-Control, and Conduct Disorders")
        yield Disorder(label="ASPD (Antisocial Personality Disorder)")
        yield Disorder(label="Borderline Personality Disorder")
        yield Disorder(label="Narcissistic Personality Disorder")

        # Dissociative Disorders
        yield Characteristic(id=1, label='Loss of identity', significance=0.0)
        yield Characteristic(id=2, label='Acting without awareness and forgetting actions', significance=0.0)
        yield Characteristic(id=3, label='Emotional coldness or detachment', significance=0.0)
        yield Characteristic(id=4, label='Multiple personalities', significance=0.0)
        yield Characteristic(id=5, label='Memory loss', significance=0.0)
        yield Characteristic(id=6, label='Daily life problems', significance=0.0)
    
        # Schizophrenia
        # yield Characteristic(id=7, label='Emotional coldness or detachment', significance=0.0)
        yield Characteristic(id=8, label='Delusional beliefs', significance=0.0)
        yield Characteristic(id=9, label='Hallucinations', significance=0.0)
        # yield Characteristic(id=10, label='Memory loss', significance=0.0)
        # yield Characteristic(id=11, label='Daily life problems', significance=0.0)
        yield Characteristic(id=12, label='Neglect of self-care', significance=0.0)
        yield Characteristic(id=13, label='Mood fluctuations', significance=0.0)
    
        # Bipolar Disorder
        # yield Characteristic(id=14, label='Daily life problems', significance=0.0)
        yield Characteristic(id=15, label='Mood swings', significance=0.0)
        yield Characteristic(id=16, label='Overconfidence', significance=0.0)
        yield Characteristic(id=17, label='Reduced need for sleep', significance=0.0)
        # yield Characteristic(id=18, label='Excessive talking', significance=0.0)
        yield Characteristic(id=19, label='Distractions and irrelevant thoughts', significance=0.0)
        yield Characteristic(id=20, label='Impulsivity', significance=0.0)
        yield Characteristic(id=21, label='Emptiness and sadness', significance=0.0)
        yield Characteristic(id=22, label='Loss of pleasure and interest', significance=0.0)
        yield Characteristic(id=23, label='Insomnia', significance=0.0)
        yield Characteristic(id=24, label='Loss of appetite and weight', significance=0.0)
        yield Characteristic(id=25, label='Loss of energy', significance=0.0)
        yield Characteristic(id=26, label='Suicidal thoughts', significance=0.0)
        yield Characteristic(id=27, label='Feelings of guilt', significance=0.0)
        yield Characteristic(id=28, label='Low self-worth', significance=0.0)
        yield Characteristic(id=29, label='Indecisiveness', significance=0.0)
        yield Characteristic(id=30, label='Poor concentration', significance=0.0)
        # yield Characteristic(id=31, label='Family history of mood disorders', significance=0.0)
    
        # Depressive Disorders
        yield Characteristic(id=32, label='Life problems', significance=0.0)
        # yield Characteristic(id=33, label='Emptiness and sadness', significance=0.0)
        # yield Characteristic(id=34, label='Loss of pleasure and interest', significance=0.0)
        # yield Characteristic(id=35, label='Insomnia', significance=0.0)
        # yield Characteristic(id=36, label='Loss of appetite and weight', significance=0.0)
        # yield Characteristic(id=37, label='Loss of energy', significance=0.0)
        # yield Characteristic(id=38, label='Suicidal thoughts', significance=0.0)
        # yield Characteristic(id=39, label='Feelings of guilt', significance=0.0)
        # yield Characteristic(id=40, label='Low self-worth', significance=0.0)
        # yield Characteristic(id=41, label='Indecisiveness', significance=0.0)
        # yield Characteristic(id=42, label='Poor concentration', significance=0.0)
        yield Characteristic(id=43, label='Family history of mood disorders', significance=0.0)
    
        # ADHD
        yield Characteristic(id=44, label='Difficulty focusing', significance=0.0)
        yield Characteristic(id=45, label='Hyperfocus', significance=0.0)
        yield Characteristic(id=46, label='Daydreaming', significance=0.0)
        yield Characteristic(id=47, label='Difficulty following instructions', significance=0.0)
        yield Characteristic(id=48, label='Losing important items', significance=0.0)
        yield Characteristic(id=49, label='Forgetfulness in daily activities', significance=0.0)
        # yield Characteristic(id=50, label='Impulsivity', significance=0.0)
        yield Characteristic(id=51, label='Difficulty engaging in quiet activities', significance=0.0)
        yield Characteristic(id=52, label='Constant activity', significance=0.0)
        yield Characteristic(id=53, label='Excessive talking', significance=0.0)
        yield Characteristic(id=54, label='Interrupting others', significance=0.0)
        yield Characteristic(id=55, label='Difficulty waiting', significance=0.0)
    
        # Autism
        yield Characteristic(id=56, label='Problems with social interactions', significance=0.0)
        yield Characteristic(id=57, label='Difficulty sharing emotions', significance=0.0)
        yield Characteristic(id=58, label='Issues with eye and physical contact', significance=0.0)
        yield Characteristic(id=59, label='Social relationship problems', significance=0.0)
        yield Characteristic(id=60, label='Repetitive movements or speech', significance=0.0)
        yield Characteristic(id=61, label='Insistence on routine', significance=0.0)
        yield Characteristic(id=62, label='Stubbornness', significance=0.0)
        yield Characteristic(id=63, label='Attachment to unusual objects or interests', significance=0.0)
        yield Characteristic(id=64, label='Sensory sensitivities', significance=0.0)
    
        # Anxiety Disorders
        yield Characteristic(id=65, label='Excessive anxiety in certain situations', significance=0.0)
        yield Characteristic(id=66, label='Physical symptoms', significance=0.0)
        yield Characteristic(id=67, label='Difficulty concentrating', significance=0.0)
        yield Characteristic(id=68, label='Avoidance of anxiety-inducing situations', significance=0.0)
        # yield Characteristic(id=69, label='Life problems', significance=0.0)
        yield Characteristic(id=70, label='Inability to control anxiety', significance=0.0)
        yield Characteristic(id=71, label='Sleep disturbances', significance=0.0)
        yield Characteristic(id=72, label='Irritability', significance=0.0)
        yield Characteristic(id=73, label='Family history of anxiety disorders', significance=0.0)
    
        # OCD
        yield Characteristic(id=75, label='Obsessions', significance=0.0)
        yield Characteristic(id=76, label='Compulsions', significance=0.0)
        # yield Characteristic(id=77, label='Life problems', significance=0.0)
        yield Characteristic(id=78, label='Avoidance of situations that trigger obsessions and compulsions', significance=0.0)
    
        # Somatic Disorders
        # yield Characteristic(id=79, label='Physical symptoms', significance=0.0)
        yield Characteristic(id=80, label='Overthinking these symptoms', significance=0.0)
        yield Characteristic(id=81, label='Frequent doctor visits', significance=0.0)
        yield Characteristic(id=82, label='Dissatisfaction with medical advice', significance=0.0)
    
        # Feeding Disorders
        yield Characteristic(id=83, label='Extreme weight loss', significance=0.0)
        yield Characteristic(id=84, label='Eating-related issues', significance=0.0)
        yield Characteristic(id=85, label='Reliance on dietary supplements', significance=0.0)
        # yield Characteristic(id=86, label='Life problems', significance=0.0)
        yield Characteristic(id=87, label='Avoidance or attraction to food based on appearance, smell, taste, and temperature', significance=0.0)
        yield Characteristic(id=88, label='Fear of choking or vomiting', significance=0.0)

        # Disruptive, Impulse-Control, and Conduct Disorders
        yield Characteristic(id=89, label='Difficulty controlling emotions', significance=0.0)
        yield Characteristic(id=90, label='Hostile behaviors', significance=0.0)
        yield Characteristic(id=91, label='Property destruction', significance=0.0)
        yield Characteristic(id=92, label='Issues with authority figures', significance=0.0)
        yield Characteristic(id=93, label='Difficulty conforming to social norms', significance=0.0)
        # yield Characteristic(id=94, label='Life problems', significance=0.0)
        yield Characteristic(id=95, label='Irrational reactions', significance=0.0)
        yield Characteristic(id=96, label='Feeling misunderstood', significance=0.0)
        yield Characteristic(id=97, label='Easily annoyed', significance=0.0)
        yield Characteristic(id=98, label='Engaging in fire-setting or theft to relieve internal feelings', significance=0.0)

        # ASPD (Antisocial Personality Disorder)
        yield Characteristic(id=99, label='Engaging in criminal activities', significance=0.0)
        yield Characteristic(id=100, label='Pathological lying', significance=0.0)
        yield Characteristic(id=101, label='Impulsive decision-making', significance=0.0)
        yield Characteristic(id=102, label='Physical fights and assaults', significance=0.0)
        yield Characteristic(id=103, label='Reckless disregard for safety of self or others', significance=0.0)
        yield Characteristic(id=104, label='History of irresponsibility', significance=0.0)
        yield Characteristic(id=105, label='Lack of guilt', significance=0.0)
        yield Characteristic(id=106, label='Early behavioral problems', significance=0.0)

        # Borderline Personality Disorder
        yield Characteristic(id=107, label='Fear of abandonment', significance=0.0)
        yield Characteristic(id=108, label='Pattern of idealization and devaluation of others', significance=0.0)
        yield Characteristic(id=109, label='Unstable self-image', significance=0.0)
        yield Characteristic(id=110, label='Emotional instability', significance=0.0)
        yield Characteristic(id=111, label='Suicidal ideation', significance=0.0)
        yield Characteristic(id=112, label='Self-harming behaviors', significance=0.0)
        # yield Characteristic(id=113, label='Mood swings', significance=0.0)
        yield Characteristic(id=114, label='Chronic feelings of emptiness', significance=0.0)
        yield Characteristic(id=115, label='Episodes of intense anger', significance=0.0)

        # Narcissistic Personality Disorder
        yield Characteristic(id=116, label='Grandiose sense of self-importance', significance=0.0)
        yield Characteristic(id=117, label='Fantasies of unlimited power, brilliance, and ideal love', significance=0.0)
        yield Characteristic(id=118, label='Need for excessive admiration', significance=0.0)
        yield Characteristic(id=119, label='Sense of entitlement', significance=0.0)
        yield Characteristic(id=120, label='Manipulative behaviors', significance=0.0)
        yield Characteristic(id=121, label='Lack of empathy', significance=0.0)
        yield Characteristic(id=122, label='Envy of others and belief that others are envious of them', significance=0.0)
        yield Characteristic(id=123, label='Arrogance', significance=0.0)

        ####################################################################################################################################################################################################################

        # main questions
        yield Question(
            id=1, 
            content="Have you been experiencing symptoms for more than six months?", 
            characteristics=[], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=2, 
            content="Have these symptoms significantly affected your ability to work, study, or maintain relationships?", 
            characteristics=[], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=3, 
            content="Have you been experiencing any significant changes in your mood or emotions?", 
            characteristics=[], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=4, 
            content="Have you been experiencing concentration difficulties?", 
            characteristics=[], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        
        # Dissociative Disorders
        yield Question(
            id=12, 
            content="How long have you been experiencing these feelings of detachment or memory loss?", 
            disorder="Dissociative Disorders",
            characteristics=[
                Characteristic(label='Loss of identity', significance=0.95),
                Characteristic(label='Emotional coldness or detachment', significance=0.84),
                Characteristic(label='Memory loss', significance=1.0),
                Characteristic(label='Daily life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=11, 
            content="Do these experiences of detachment or memory loss cause you significant distress or problems in your daily life, or do these experiences affect your relationships, work, or other important areas of functioning?", 
            disorder="Dissociative Disorders",
            characteristics=[
                Characteristic(label='Loss of identity', significance=0.84),
                Characteristic(label='Emotional coldness or detachment', significance=0.84),
                Characteristic(label='Memory loss', significance=0.84),
                Characteristic(label='Daily life problems', significance=1.0)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=10, 
            content="Have you been told about things you did or said that you have no memory of?", 
            disorder="Dissociative Disorders",
            characteristics=[
                Characteristic(label='Acting without awareness and forgetting actions', significance=1.0),
                Characteristic(label='Multiple personalities', significance=0.84),
                Characteristic(label='Memory loss', significance=0.84),
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=9, 
            content="Do you find yourself missing chunks of memories, like entire days or events, and can't explain why?", 
            disorder="Dissociative Disorders",
            characteristics=[
                Characteristic(label='Loss of identity', significance=0.84),
                Characteristic(label='Acting without awareness and forgetting actions', significance=0.95),
                Characteristic(label='Memory loss', significance=1.0),
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=8, 
            content="Have you ever experienced periods where you can't remember important events from your life, especially stressful or traumatic ones?", 
            disorder="Dissociative Disorders",
            characteristics=[
                Characteristic(label='Loss of identity', significance=0.84),
                Characteristic(label='Acting without awareness and forgetting actions', significance=0.84),
                Characteristic(label='Memory loss', significance=1.0),
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=7, 
            content="Do you ever feel like there are different 'parts' of you that take control at times?", 
            disorder="Dissociative Disorders",
            characteristics=[
                Characteristic(label='Loss of identity', significance=0.84),
                Characteristic(label='Acting without awareness and forgetting actions', significance=0.84),
                Characteristic(label='Multiple personalities', significance=1.0),
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=6, 
            content="Do you describe yourself feeling emotionally numb or like your emotions are muted?", 
            disorder="Dissociative Disorders",
            characteristics=[
                Characteristic(label='Loss of identity', significance=0.84),
                Characteristic(label='Emotional coldness or detachment', significance=1.0),
                Characteristic(label='Daily life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=5, 
            content="Do you ever feel detached from yourself, like you're observing your thoughts, feelings, or body from a distance?", 
            disorder="Dissociative Disorders",
            characteristics=[
                Characteristic(label='Loss of identity', significance=0.95),
                Characteristic(label='Emotional coldness or detachment', significance=0.84),
                Characteristic(label='Multiple personalities', significance=0.84),
                Characteristic(label='Memory loss', significance=0.84),
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )

        # Schizophrenia
        yield Question(
            id=20, 
            content="Have you experienced multiple episodes of these symptoms?", 
            disorder="Schizophrenia",
            characteristics=[
                Characteristic(label='Memory loss', significance=0.84),
                Characteristic(label='Delusional beliefs', significance=0.95),
                Characteristic(label='Hallucinations', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=19, 
            content="Have you ever been diagnosed with a mood disorder (depression or bipolar disorder) that includes psychotic features?", 
            disorder="Schizophrenia",
            characteristics=[
                Characteristic(label='Mood fluctuations', significance=1.0),
                Characteristic(label='Delusional beliefs', significance=0.95),
                Characteristic(label='Hallucinations', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=18, 
            content="Have you experienced mood episodes (depressive or manic) that coincide with these symptoms, and if so, are the mood episodes shorter in duration compared to the psychotic symptoms?", 
            disorder="Schizophrenia",
            characteristics=[
                Characteristic(label='Mood fluctuations', significance=1.0),
                Characteristic(label='Delusional beliefs', significance=0.95),
                Characteristic(label='Hallucinations', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=17, 
            content="Do you find it difficult to take care of yourself or perform daily tasks compared to before the symptoms started?", 
            disorder="Schizophrenia",
            characteristics=[
                Characteristic(label='Neglect of self-care', significance=1.0),
                Characteristic(label='Daily life problems', significance=0.95),
                Characteristic(label='Memory loss', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=16, 
            content="Do you notice a lack of motivation or a diminished ability to express emotions, or have others mentioned that you seem emotionally flat or withdrawn?", 
            disorder="Schizophrenia",
            characteristics=[
                Characteristic(label='Emotional coldness or detachment', significance=1.0),
                Characteristic(label='Neglect of self-care', significance=0.84),
                Characteristic(label='Daily life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=15, 
            content="Do you often find that your speech becomes jumbled or incoherent, making it hard for others to understand you, or frequently lose track of your thoughts or find it difficult to follow a conversation?", 
            disorder="Schizophrenia",
            characteristics=[
                Characteristic(label='Daily life problems', significance=0.84),
                Characteristic(label='Mood fluctuations', significance=0.84),
                Characteristic(label='Memory loss', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=14, 
            content="Do you ever hear voices, see things that others do not, or feel any unusual sensory perceptions, like something touching you when nothing is there?", 
            disorder="Schizophrenia",
            characteristics=[
                Characteristic(label='Hallucinations', significance=1.0),
                Characteristic(label='Delusional beliefs', significance=0.95),
                Characteristic(label='Emotional coldness or detachment', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=13, 
            content="Do you ever believe things like being watched, followed, or conspired against without clear evidence that others find strange or that you later recognize as unrealistic?", 
            disorder="Schizophrenia",
            characteristics=[
                Characteristic(label='Delusional beliefs', significance=1.0),
                Characteristic(label='Emotional coldness or detachment', significance=0.84),
                Characteristic(label='Mood fluctuations', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )

        # Bipolar Disorder
        yield Question(
            id=37, 
            content="Have you been able to maintain your usual level of functioning during these mood episodes?", 
            disorder="Bipolar Disorder",
            characteristics=[
                Characteristic(label='Daily life problems', significance=1.0),
                Characteristic(label='Mood swings', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=35, 
            content="Did you have recurrent thoughts of death or suicide?", 
            disorder="Bipolar Disorder",
            characteristics=[
                Characteristic(label='Suicidal thoughts', significance=0.95),
                Characteristic(label='Emptiness and sadness', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=34, 
            content="Did you have trouble concentrating or making decisions?", 
            disorder="Bipolar Disorder",
            characteristics=[
                Characteristic(label='Poor concentration', significance=0.95),
                Characteristic(label='Indecisiveness', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=33, 
            content="Did you have feelings of worthlessness or excessive guilt?", 
            disorder="Bipolar Disorder",
            characteristics=[
                Characteristic(label='Feelings of guilt', significance=0.95),
                Characteristic(label='Low self-worth', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=32, 
            content="Did you feel unusually tired or had a lack of energy?", 
            disorder="Bipolar Disorder",
            characteristics=[
                Characteristic(label='Loss of energy', significance=0.95),
                Characteristic(label='Daily life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=31, 
            content="Did you have trouble sleeping (insomnia) or did you sleep excessively (hypersomnia)?", 
            disorder="Bipolar Disorder",
            characteristics=[
                Characteristic(label='Insomnia', significance=0.95),
                Characteristic(label='Daily life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=30, 
            content="Did you experience significant weight loss or gain, or a change in appetite?", 
            disorder="Bipolar Disorder",
            characteristics=[
                Characteristic(label='Loss of appetite and weight', significance=0.95),
                Characteristic(label='Daily life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=28, 
            content="Have you had periods where you felt persistently sad, empty, or hopeless?", 
            disorder="Bipolar Disorder",
            characteristics=[
                Characteristic(label='Emptiness and sadness', significance=0.95),
                Characteristic(label='Daily life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=27, 
            content="Did you engage in activities that are risky or could have painful consequences (e.g., unrestrained spending, or foolish business investments)?", 
            disorder="Bipolar Disorder",
            characteristics=[
                Characteristic(label='Impulsivity', significance=0.95),
                Characteristic(label='Mood swings', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=26, 
            content="Did you find yourself easily distracted by unimportant or irrelevant things?", 
            disorder="Bipolar Disorder",
            characteristics=[
                Characteristic(label='Distractions and irrelevant thoughts', significance=0.95),
                Characteristic(label='Impulsivity', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=25, 
            content="Did you experience racing thoughts or a flight of ideas?", 
            disorder="Bipolar Disorder",
            characteristics=[
                Characteristic(label='Distractions and irrelevant thoughts', significance=0.95),
                Characteristic(label='Mood swings', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=24, 
            content="Were you more talkative than usual or felt pressured to keep talking?", 
            disorder="Bipolar Disorder",
            characteristics=[
                Characteristic(label='Excessive talking', significance=0.95),
                Characteristic(label='Overconfidence', significance=0.95),
                Characteristic(label='Mood swings', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=23, 
            content="Did you notice a decreased need for sleep during these periods (e.g., feeling rested after only a few hours of sleep)?", 
            disorder="Bipolar Disorder",
            characteristics=[
                Characteristic(label='Reduced need for sleep', significance=0.95),
                Characteristic(label='Mood swings', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=22, 
            content="During these periods, did you feel more self-confident or grandiose than usual?", 
            disorder="Bipolar Disorder",
            characteristics=[
                Characteristic(label='Overconfidence', significance=0.95),
                Characteristic(label='Mood swings', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=21, 
            content="Have you experienced periods of abnormally and persistently elevated, expansive, or irritable mood lasting at least four consecutive days?", 
            disorder="Bipolar Disorder",
            characteristics=[
                Characteristic(label='Mood swings', significance=0.95),
                Characteristic(label='Daily life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )

        # Depressive Disorders
        yield Question(
            id=50, 
            content="Have you ever planned or attempted suicide?", 
            disorder="Depressive Disorders",
            characteristics=[
                Characteristic(label='Suicidal thoughts', significance=1.0),
                Characteristic(label='Low self-worth', significance=1.0),
                Characteristic(label='Emptiness and sadness', significance=0.95),
                Characteristic(label='Loss of pleasure and interest', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=49, 
            content="Do you have recurrent thoughts of death or suicide?", 
            disorder="Depressive Disorders",
            characteristics=[
                Characteristic(label='Suicidal thoughts', significance=1.0),
                Characteristic(label='Low self-worth', significance=1.0),
                Characteristic(label='Emptiness and sadness', significance=0.95),
                Characteristic(label='Loss of pleasure and interest', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=48, 
            content="Do you find it difficult to think, concentrate, or make decisions nearly every day?", 
            disorder="Depressive Disorders",
            characteristics=[
                Characteristic(label='Poor concentration', significance=1.0),
                Characteristic(label='Indecisiveness', significance=0.95),
                Characteristic(label='Life problems', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=47, 
            content="Do you feel worthless or excessively guilty nearly every day?", 
            disorder="Depressive Disorders",
            characteristics=[
                Characteristic(label='Feelings of guilt', significance=1.0),
                Characteristic(label='Low self-worth', significance=1.0),
                Characteristic(label='Emptiness and sadness', significance=0.84),
                Characteristic(label='Loss of pleasure and interest', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=46, 
            content="Do you feel fatigued or have a loss of energy nearly every day?", 
            disorder="Depressive Disorders",
            characteristics=[
                Characteristic(label='Loss of energy', significance=1.0),
                Characteristic(label='Emptiness and sadness', significance=0.84),
                Characteristic(label='Life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=45, 
            content="Do you have trouble sleeping (insomnia) or do you sleep too much (hypersomnia) nearly every day?", 
            disorder="Depressive Disorders",
            characteristics=[
                Characteristic(label='Insomnia', significance=1.0),
                Characteristic(label='Emptiness and sadness', significance=0.84),
                Characteristic(label='Life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=44, 
            content="Have you noticed a significant decrease or increase in your appetite nearly every day?", 
            disorder="Depressive Disorders",
            characteristics=[
                Characteristic(label='Loss of appetite and weight', significance=1.0),
                Characteristic(label='Emptiness and sadness', significance=0.84),
                Characteristic(label='Life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=43, 
            content="Have you experienced significant weight loss or weight gain without trying to diet?", 
            disorder="Depressive Disorders",
            characteristics=[
                Characteristic(label='Loss of appetite and weight', significance=1.0),
                Characteristic(label='Emptiness and sadness', significance=0.84),
                Characteristic(label='Life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=42, 
            content="Have you lost interest or pleasure in most activities that you previously enjoyed?", 
            disorder="Depressive Disorders",
            characteristics=[
                Characteristic(label='Loss of pleasure and interest', significance=1.0),
                Characteristic(label='Emptiness and sadness', significance=0.84),
                Characteristic(label='Life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=41, 
            content="Do you often feel sad, empty, or hopeless?", 
            disorder="Depressive Disorders",
            characteristics=[
                Characteristic(label='Emptiness and sadness', significance=1.0),
                Characteristic(label='Low self-worth', significance=0.84),
                Characteristic(label='Feelings of guilt', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=40, 
            content="Have you felt depressed most of the day, nearly every day, for at least two weeks?", 
            disorder="Depressive Disorders",
            characteristics=[
                Characteristic(label='Emptiness and sadness', significance=1.0),
                Characteristic(label='Loss of pleasure and interest', significance=0.95),
                Characteristic(label='Life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )

        # ADHD
        yield Question(
            id=67, 
            content="Do you often interrupt or intrude on others (e.g., butt into conversations, games, or activities; may start using other people’s things without asking or receiving permission; for adolescents and adults, may intrude into or take over what others are doing)?", 
            disorder="ADHD",
            characteristics=[
                Characteristic(label='Interrupting others', significance=0.95),
                Characteristic(label='Impulsivity', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=66, 
            content="Do you often have difficulty waiting your turn (e.g., while waiting in line)?", 
            disorder="ADHD",
            characteristics=[
                Characteristic(label='Difficulty waiting', significance=0.95),
                Characteristic(label='Impulsivity', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=65, 
            content="Do you often blurt out an answer before a question has been completed (e.g., complete people’s sentences, cannot wait for your turn in conversation)?", 
            disorder="ADHD",
            characteristics=[
                Characteristic(label='Impulsivity', significance=0.95),
                Characteristic(label='Interrupting others', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=64, 
            content="Do you often talk excessively?", 
            disorder="ADHD",
            characteristics=[
                Characteristic(label='Excessive talking', significance=0.95),
                Characteristic(label='Impulsivity', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=63, 
            content="Are you often 'on the go,' acting as if 'driven by a motor' (e.g., unable to be or uncomfortable being still for extended time, such as in restaurants, meetings; may be experienced by others as being restless or difficult to keep up with)?", 
            disorder="ADHD",
            characteristics=[
                Characteristic(label='Constant activity', significance=0.95),
                Characteristic(label='Impulsivity', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=62, 
            content="Are you often unable to play or engage in leisure activities quietly?", 
            disorder="ADHD",
            characteristics=[
                Characteristic(label='Difficulty engaging in quiet activities', significance=0.95),
                Characteristic(label='Constant activity', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=61, 
            content="Do you often leave your seat in situations when remaining seated is expected (e.g., leave your place in the classroom, in the office or other workplace, or in other situations that require remaining in place)?", 
            disorder="ADHD",
            characteristics=[
                Characteristic(label='Impulsivity', significance=0.95),
                Characteristic(label='Constant activity', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=60, 
            content="Do you often fidget with or tap your hands or feet, or squirm in your seat?", 
            disorder="ADHD",
            characteristics=[
                Characteristic(label='Constant activity', significance=0.95),
                Characteristic(label='Impulsivity', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=59, 
            content="Are you often forgetful in daily activities (e.g., doing chores, running errands; for older adolescents and adults, returning calls, paying bills, keeping appointments)?", 
            disorder="ADHD",
            characteristics=[
                Characteristic(label='Forgetfulness in daily activities', significance=1.0),
                Characteristic(label='Difficulty focusing', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=58, 
            content="Are you often easily distracted by extraneous stimuli (for older adolescents and adults, this may include unrelated thoughts)?", 
            disorder="ADHD",
            characteristics=[
                Characteristic(label='Easily distracted', significance=0.95),
                Characteristic(label='Difficulty focusing', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=57, 
            content="Do you often lose things necessary for tasks or activities (e.g., school materials, pencils, books, tools, wallets, keys, paperwork, eyeglasses, mobile phones)?", 
            disorder="ADHD",
            characteristics=[
                Characteristic(label='Losing important items', significance=1.0),
                Characteristic(label='Difficulty focusing', significance=0.95),
                Characteristic(label='Forgetfulness in daily activities', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=56, 
            content="Do you often avoid, dislike, or are reluctant to engage in tasks that require sustained mental effort (e.g., schoolwork or homework; for older adolescents and adults, preparing reports, completing forms, reviewing lengthy papers)?", 
            disorder="ADHD",
            characteristics=[
                Characteristic(label='Difficulty focusing', significance=1.0),
                Characteristic(label='Avoidance of tasks requiring mental effort', significance=0.95),
                Characteristic(label='Difficulty organizing tasks', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=55, 
            content="Do you often have difficulty organizing tasks and activities (e.g., difficulty managing sequential tasks, keeping materials and belongings in order, messy or disorganized work, poor time management, failure to meet deadlines)?", 
            disorder="ADHD",
            characteristics=[
                Characteristic(label='Difficulty organizing tasks', significance=1.0),
                Characteristic(label='Difficulty focusing', significance=0.95),
                Characteristic(label='Forgetfulness in daily activities', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=54, 
            content="Do you often not follow through on instructions and fail to finish schoolwork, chores, or duties in the workplace (e.g., start tasks but quickly lose focus and get easily sidetracked)?", 
            disorder="ADHD",
            characteristics=[
                Characteristic(label='Difficulty following instructions', significance=1.0),
                Characteristic(label='Difficulty focusing', significance=1.0)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=53, 
            content="Do you often not seem to listen when spoken to directly (e.g., mind seems elsewhere, even in the absence of any obvious distraction)?", 
            disorder="ADHD",
            characteristics=[
                Characteristic(label='Daydreaming', significance=1.0),
                Characteristic(label='Difficulty focusing', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=52, 
            content="Do you often have difficulty sustaining attention in tasks or play activities (e.g., difficulty remaining focused during lectures, conversations, or lengthy reading)?", 
            disorder="ADHD",
            characteristics=[
                Characteristic(label='Difficulty focusing', significance=1.0),
                Characteristic(label='Hyperfocus', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=51, 
            content="Do you often fail to give close attention to details or make careless mistakes in schoolwork, at work, or during other activities (e.g., overlook or miss details, work is inaccurate)?", 
            disorder="ADHD",
            characteristics=[
                Characteristic(label='Difficulty focusing', significance=1.0),
                Characteristic(label='Forgetfulness in daily activities', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )

        # Autism
        yield Question(
            id=83, 
            content="Are you hyper or hypo reactive to sensory input?", 
            disorder="Autism",
            characteristics=[
                Characteristic(label='Sensory sensitivities', significance=1.0),
                Characteristic(label='Attachment to unusual objects or interests', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=82, 
            content="Is there a strong attachment or preoccupation with unusual objects or topics?", 
            disorder="Autism",
            characteristics=[
                Characteristic(label='Attachment to unusual objects or interests', significance=1.0),
                Characteristic(label='Insistence on routine', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=81, 
            content="Do you have highly restricted interests that are abnormal in intensity or focus?", 
            disorder="Autism",
            characteristics=[
                Characteristic(label='Attachment to unusual objects or interests', significance=1.0),
                Characteristic(label='Insistence on routine', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=80, 
            content="Are there rigid thinking patterns or ritualized behaviors you adhere to?", 
            disorder="Autism",
            characteristics=[
                Characteristic(label='Insistence on routine', significance=0.95),
                Characteristic(label='Stubbornness', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=79, 
            content="Do you insist on following specific routines or get distressed by small changes in your environment?", 
            disorder="Autism",
            characteristics=[
                Characteristic(label='Insistence on routine', significance=0.95),
                Characteristic(label='Stubbornness', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=78, 
            content="Do you repeat phrases or use idiosyncratic speech patterns?", 
            disorder="Autism",
            characteristics=[
                Characteristic(label='Repetitive movements or speech', significance=0.95),
                Characteristic(label='Insistence on routine', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=77, 
            content="Does your child engage in repetitive motor movements or use objects in a repetitive way (e.g., lining up toys, flipping objects)?", 
            disorder="Autism",
            characteristics=[
                Characteristic(label='Repetitive movements or speech', significance=1.0),
                Characteristic(label='Insistence on routine', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=76, 
            content="Is there an absence of interest in peers or shared imaginative play?", 
            disorder="Autism",
            characteristics=[
                Characteristic(label='Problems with social interactions', significance=0.95),
                Characteristic(label='Social relationship problems', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=75, 
            content="Do you understand and adjust your behavior to suit different social contexts?", 
            disorder="Autism",
            characteristics=[
                Characteristic(label='Problems with social interactions', significance=0.95),
                Characteristic(label='Social relationship problems', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=74, 
            content="Do you have difficulties making or maintaining friendships?", 
            disorder="Autism",
            characteristics=[
                Characteristic(label='Social relationship problems', significance=1.0),
                Characteristic(label='Problems with social interactions', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=73, 
            content="Do you have difficulties understanding or using nonverbal communication?", 
            disorder="Autism",
            characteristics=[
                Characteristic(label='Issues with eye and physical contact', significance=0.95),
                Characteristic(label='Problems with social interactions', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=72, 
            content="Are there any abnormalities in your body language or use of gestures?", 
            disorder="Autism",
            characteristics=[
                Characteristic(label='Issues with eye and physical contact', significance=0.95),
                Characteristic(label='Problems with social interactions', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=71, 
            content="Do you use eye contact, gestures, and facial expressions when communicating?", 
            disorder="Autism",
            characteristics=[
                Characteristic(label='Issues with eye and physical contact', significance=0.95),
                Characteristic(label='Problems with social interactions', significance=0.84),
                Characteristic(label='Social relationship problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=70, 
            content="Have you noticed any difficulties in your initiating or responding to social interactions?", 
            disorder="Autism",
            characteristics=[
                Characteristic(label='Problems with social interactions', significance=0.95),
                Characteristic(label='Social relationship problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=69, 
            content="Do you share interests or emotions with others?", 
            disorder="Autism",
            characteristics=[
                Characteristic(label='Difficulty sharing emotions', significance=0.95),
                Characteristic(label='Problems with social interactions', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=68, 
            content="Do you initiate or respond to social interactions?", 
            disorder="Autism",
            characteristics=[
                Characteristic(label='Problems with social interactions', significance=1.0),
                Characteristic(label='Social relationship problems', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )

        # Anxiety Disorders
        yield Question(
            id=98, 
            content="Do you have trouble sleeping because of your anxiety?", 
            disorder="Anxiety Disorders",
            characteristics=[
                Characteristic(label='Sleep disturbances', significance=1.0),
                Characteristic(label='Excessive anxiety in certain situations', significance=0.95),
                Characteristic(label='Inability to control anxiety', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=97, 
            content="Do you experience other symptoms such as irritability, restlessness, or feeling on edge?", 
            disorder="Anxiety Disorders",
            characteristics=[
                Characteristic(label='Irritability', significance=1.0),
                Characteristic(label='Physical symptoms', significance=0.95),
                Characteristic(label='Excessive anxiety in certain situations', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=96, 
            content="Does your anxiety feel uncontrollable?", 
            disorder="Anxiety Disorders",
            characteristics=[
                Characteristic(label='Inability to control anxiety', significance=0.95),
                Characteristic(label='Excessive anxiety in certain situations', significance=0.95),
                Characteristic(label='Life problems', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=95, 
            content="Does anxiety affect your daily life and activities, such as work, school, or relationships?", 
            disorder="Anxiety Disorders",
            characteristics=[
                Characteristic(label='Life problems', significance=1.0),
                Characteristic(label='Excessive anxiety in certain situations', significance=0.95),
                Characteristic(label='Inability to control anxiety', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=93, 
            content="Do you avoid certain situations or activities because they make you anxious?", 
            disorder="Anxiety Disorders",
            characteristics=[
                Characteristic(label='Avoidance of anxiety-inducing situations', significance=1.0),
                Characteristic(label='Excessive anxiety in certain situations', significance=0.95),
                Characteristic(label='Life problems', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=92, 
            content="Do you worry excessively about various things?", 
            disorder="Anxiety Disorders",
            characteristics=[
                Characteristic(label='Excessive anxiety in certain situations', significance=1.0),
                Characteristic(label='Inability to control anxiety', significance=0.95),
                Characteristic(label='Life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=91, 
            content="Do you find it difficult to concentrate or does your mind often go blank when anxious?", 
            disorder="Anxiety Disorders",
            characteristics=[
                Characteristic(label='Difficulty concentrating', significance=1.0),
                Characteristic(label='Excessive anxiety in certain situations', significance=0.95),
                Characteristic(label='Inability to control anxiety', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=90, 
            content="Do you experience gastrointestinal issues like nausea or stomach discomfort when anxious?", 
            disorder="Anxiety Disorders",
            characteristics=[
                Characteristic(label='Physical symptoms', significance=1.0),
                Characteristic(label='Excessive anxiety in certain situations', significance=0.95),
                Characteristic(label='Inability to control anxiety', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=89, 
            content="Do you experience physical symptoms like increased heart rate, sweating, trembling, or shortness of breath when anxious?", 
            disorder="Anxiety Disorders",
            characteristics=[
                Characteristic(label='Physical symptoms', significance=1.0),
                Characteristic(label='Excessive anxiety in certain situations', significance=0.95),
                Characteristic(label='Inability to control anxiety', significance=0.95),
                Characteristic(label='Life problems', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=88, 
            content="Do certain events or thoughts make your anxiety worse?", 
            disorder="Anxiety Disorders",
            characteristics=[
                Characteristic(label='Excessive anxiety in certain situations', significance=1.0),
                Characteristic(label='Inability to control anxiety', significance=0.95),
                Characteristic(label='Life problems', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=87, 
            content="Are there specific situations or activities that trigger your anxiety?", 
            disorder="Anxiety Disorders",
            characteristics=[
                Characteristic(label='Excessive anxiety in certain situations', significance=1.0),
                Characteristic(label='Avoidance of anxiety-inducing situations', significance=0.95),
                Characteristic(label='Life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=86, 
            content="Can you recall when your anxiety first started?", 
            disorder="Anxiety Disorders",
            characteristics=[
                Characteristic(label='Excessive anxiety in certain situations', significance=0.95),
                Characteristic(label='Family history of anxiety disorders', significance=0.95),
                Characteristic(label='Life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=85, 
            content="Do your periods of anxiety typically last for extended periods?", 
            disorder="Anxiety Disorders",
            characteristics=[
                Characteristic(label='Excessive anxiety in certain situations', significance=1.0),
                Characteristic(label='Inability to control anxiety', significance=0.95),
                Characteristic(label='Life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=84, 
            content="Do you feel anxious or worried often?", 
            disorder="Anxiety Disorders",
            characteristics=[
                Characteristic(label='Excessive anxiety in certain situations', significance=1.0),
                Characteristic(label='Inability to control anxiety', significance=0.95),
                Characteristic(label='Life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )

        # OCD
        yield Question(
            id=109, 
            content="Do you have a distressing sense of 'incompleteness' or uneasiness until things look, feel, or sound 'just right'?", 
            disorder="OCD",
            characteristics=[
                Characteristic(label='Obsessions', significance=0.95),
                Characteristic(label='Compulsions', significance=0.84),
                Characteristic(label='Life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=108, 
            content="Do you experience marked anxiety, recurrent panic attacks, or strong feelings of disgust when confronted with situations that trigger obsessions and compulsions?", 
            disorder="OCD",
            characteristics=[
                Characteristic(label='Obsessions', significance=0.95),
                Characteristic(label='Compulsions', significance=0.84),
                Characteristic(label='Avoidance of situations that trigger obsessions and compulsions', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=107, 
            content="Do you avoid people, places, or things that trigger your obsessions and compulsions?", 
            disorder="OCD",
            characteristics=[
                Characteristic(label='Avoidance of situations that trigger obsessions and compulsions', significance=0.95),
                Characteristic(label='Obsessions', significance=0.95),
                Characteristic(label='Compulsions', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=106, 
            content="Do your obsessions or compulsions cause significant distress or impairment in social, occupational, or other important areas of functioning?", 
            disorder="OCD",
            characteristics=[
                Characteristic(label='Obsessions', significance=0.95),
                Characteristic(label='Compulsions', significance=0.95),
                Characteristic(label='Life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=105, 
            content="Do your obsessions or compulsions take more than 1 hour per day?", 
            disorder="OCD",
            characteristics=[
                Characteristic(label='Obsessions', significance=0.95),
                Characteristic(label='Compulsions', significance=0.95),
                Characteristic(label='Life problems', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=104, 
            content="Are these behaviors or mental acts aimed at preventing or reducing anxiety or distress, or preventing some dreaded event or situation?", 
            disorder="OCD",
            characteristics=[
                Characteristic(label='Compulsions', significance=0.95),
                Characteristic(label='Obsessions', significance=0.84),
                Characteristic(label='Avoidance of situations that trigger obsessions and compulsions', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=103, 
            content="Do you attempt to ignore or suppress these thoughts, urges, or images, or neutralize them with some other thought or action?", 
            disorder="OCD",
            characteristics=[
                Characteristic(label='Obsessions', significance=0.95),
                Characteristic(label='Compulsions', significance=0.84),
                Characteristic(label='Avoidance of situations that trigger obsessions and compulsions', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=102, 
            content="Do you experience recurrent and persistent thoughts, urges, or images that are intrusive and unwanted, causing marked anxiety or distress?", 
            disorder="OCD",
            characteristics=[
                Characteristic(label='Obsessions', significance=1.0),
                Characteristic(label='Life problems', significance=0.95),
                Characteristic(label='Avoidance of situations that trigger obsessions and compulsions', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )

        # Somatic Disorders
        yield Question(
            id=122, 
            content="Do you frequently check your body for abnormalities or repeatedly seek medical help and reassurance?", 
            disorder="Somatic Disorders",
            characteristics=[
                Characteristic(label='Frequent doctor visits', significance=1.0),
                Characteristic(label='Overthinking these symptoms', significance=0.95),
                Characteristic(label='Physical symptoms', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=121, 
            content="Do you worry excessively about illness and fear that physical activity may damage your body?", 
            disorder="Somatic Disorders",
            characteristics=[
                Characteristic(label='Overthinking these symptoms', significance=1.0),
                Characteristic(label='Physical symptoms', significance=0.95),
                Characteristic(label='Life problems', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=120, 
            content="Do you focus excessively on bodily symptoms and attribute normal bodily sensations to physical illness?", 
            disorder="Somatic Disorders",
            characteristics=[
                Characteristic(label='Overthinking these symptoms', significance=1.0),
                Characteristic(label='Physical symptoms', significance=0.95),
                Characteristic(label='Life problems', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=119, 
            content="Do you feel that your medical assessments and treatments have been inadequate?", 
            disorder="Somatic Disorders",
            characteristics=[
                Characteristic(label='Dissatisfaction with medical advice', significance=1.0),
                Characteristic(label='Frequent doctor visits', significance=0.95),
                Characteristic(label='Overthinking these symptoms', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=118, 
            content="Are you unusually sensitive to medication side effects?", 
            disorder="Somatic Disorders",
            characteristics=[
                Characteristic(label='Physical symptoms', significance=0.95),
                Characteristic(label='Overthinking these symptoms', significance=0.95),
                Characteristic(label='Life problems', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=115, 
            content="Have you been experiencing somatic symptoms for more than six months?", 
            disorder="Somatic Disorders",
            characteristics=[
                Characteristic(label='Physical symptoms', significance=0.95),
                Characteristic(label='Overthinking these symptoms', significance=0.95),
                Characteristic(label='Life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=114, 
            content="Do you devote excessive time and energy to your symptoms or health concerns?", 
            disorder="Somatic Disorders",
            characteristics=[
                Characteristic(label='Overthinking these symptoms', significance=1.0),
                Characteristic(label='Physical symptoms', significance=0.95),
                Characteristic(label='Life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=113, 
            content="Do you experience a persistently high level of anxiety about your health or symptoms?", 
            disorder="Somatic Disorders",
            characteristics=[
                Characteristic(label='Overthinking these symptoms', significance=1.0),
                Characteristic(label='Physical symptoms', significance=0.95),
                Characteristic(label='Life problems', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=112, 
            content="Do you have persistent and disproportionate thoughts about the seriousness of your symptoms?", 
            disorder="Somatic Disorders",
            characteristics=[
                Characteristic(label='Overthinking these symptoms', significance=1.0),
                Characteristic(label='Physical symptoms', significance=0.84),
                Characteristic(label='Life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=116, 
            content="Have you frequently sought medical help for your symptoms?", 
            disorder="Somatic Disorders",
            characteristics=[
                Characteristic(label='Frequent doctor visits', significance=1.0),
                Characteristic(label='Overthinking these symptoms', significance=0.95),
                Characteristic(label='Physical symptoms', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=117, 
            content="Do you feel that medical interventions rarely alleviate your concerns?", 
            disorder="Somatic Disorders",
            characteristics=[
                Characteristic(label='Dissatisfaction with medical advice', significance=0.95),
                Characteristic(label='Frequent doctor visits', significance=0.95),
                Characteristic(label='Overthinking these symptoms', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=111, 
            content="Are your somatic symptoms predominantly related to pain?", 
            disorder="Somatic Disorders",
            characteristics=[
                Characteristic(label='Physical symptoms', significance=1.0),
                Characteristic(label='Overthinking these symptoms', significance=0.95),
                Characteristic(label='Life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=110, 
            content="Do you experience one or more somatic symptoms that are distressing or result in significant disruption of your daily life?", 
            disorder="Somatic Disorders",
            characteristics=[
                Characteristic(label='Physical symptoms', significance=1.0),
                Characteristic(label='Life problems', significance=0.95),
                Characteristic(label='Overthinking these symptoms', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )

        # Feeding Disorders
        yield Question(
            id=131, 
            content="Do you avoid or restrict food intake due to a fear of aversive consequences like choking or vomiting?", 
            disorder="Feeding Disorders",
            characteristics=[
                Characteristic(label='Fear of choking or vomiting', significance=1.0),
                Characteristic(label='Avoidance or attraction to food based on appearance, smell, taste, and temperature', significance=0.95),
                Characteristic(label='Eating-related issues', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=130, 
            content="Do you avoid or restrict food intake due to sensory characteristics such as appearance, color, smell, texture, temperature, or taste?", 
            disorder="Feeding Disorders",
            characteristics=[
                Characteristic(label='Avoidance or attraction to food based on appearance, smell, taste, and temperature', significance=1.0),
                Characteristic(label='Eating-related issues', significance=0.95),
                Characteristic(label='Life problems', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=129, 
            content="Is your eating disturbance not attributable to a concurrent medical condition or another mental disorder?", 
            disorder="Feeding Disorders",
            characteristics=[
                Characteristic(label='Eating-related issues', significance=0.95),
                Characteristic(label='Life problems', significance=0.84),
                Characteristic(label='Avoidance or attraction to food based on appearance, smell, taste, and temperature', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=128, 
            content="Is your eating disturbance not better explained by anorexia nervosa or bulimia nervosa, and there is no evidence of a disturbance in how you perceive your body weight or shape?", 
            disorder="Feeding Disorders",
            characteristics=[
                Characteristic(label='Eating-related issues', significance=0.95),
                Characteristic(label='Life problems', significance=0.84),
                Characteristic(label='Avoidance or attraction to food based on appearance, smell, taste, and temperature', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=127, 
            content="Is your eating disturbance not explained by a lack of available food or cultural practices?", 
            disorder="Feeding Disorders",
            characteristics=[
                Characteristic(label='Eating-related issues', significance=0.95),
                Characteristic(label='Life problems', significance=0.84),
                Characteristic(label='Avoidance or attraction to food based on appearance, smell, taste, and temperature', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=126, 
            content="Does your eating behavior cause marked interference with your social or psychological functioning?", 
            disorder="Feeding Disorders",
            characteristics=[
                Characteristic(label='Eating-related issues', significance=1.0),
                Characteristic(label='Life problems', significance=0.95),
                Characteristic(label='Avoidance or attraction to food based on appearance, smell, taste, and temperature', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=125, 
            content="Are you dependent on enteral feeding or oral nutritional supplements to meet your nutritional needs?", 
            disorder="Feeding Disorders",
            characteristics=[
                Characteristic(label='Reliance on dietary supplements', significance=0.95),
                Characteristic(label='Eating-related issues', significance=0.95),
                Characteristic(label='Life problems', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=124, 
            content="Do you have a significant nutritional deficiency that impacts your health?", 
            disorder="Feeding Disorders",
            characteristics=[
                Characteristic(label='Eating-related issues', significance=1.0),
                Characteristic(label='Reliance on dietary supplements', significance=0.95),
                Characteristic(label='Life problems', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=123, 
            content="Have you experienced a significant weight loss or failure to gain weight as expected for your age and growth?", 
            disorder="Feeding Disorders",
            characteristics=[
                Characteristic(label='Extreme weight loss', significance=1.0),
                Characteristic(label='Eating-related issues', significance=1.0),
                Characteristic(label='Life problems', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )

        # Disruptive, Impulse-Control, and Conduct Disorders
        yield Question(
            id=141, 
            content="Have you engaged in behaviors such as fire setting or stealing to relieve internal tension?", 
            disorder="Disruptive, Impulse-Control, and Conduct Disorders",
            characteristics=[
                Characteristic(label='Engaging in fire-setting or theft to relieve internal feelings', significance=1.0),
                Characteristic(label='Difficulty controlling emotions', significance=0.95),
                Characteristic(label='Hostile behaviors', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=140, 
            content="Do you often feel irritable or easily annoyed?", 
            disorder="Disruptive, Impulse-Control, and Conduct Disorders",
            characteristics=[
                Characteristic(label='Easily annoyed', significance=1.0),
                Characteristic(label='Difficulty controlling emotions', significance=0.95),
                Characteristic(label='Hostile behaviors', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=139, 
            content="Do you often feel misunderstood or that others unfairly blame you for your actions?", 
            disorder="Disruptive, Impulse-Control, and Conduct Disorders",
            characteristics=[
                Characteristic(label='Feeling misunderstood', significance=1.0),
                Characteristic(label='Difficulty controlling emotions', significance=0.95),
                Characteristic(label='Hostile behaviors', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=138, 
            content="Have you experienced frequent temper outbursts or feelings of anger that are disproportionate to the situation?", 
            disorder="Disruptive, Impulse-Control, and Conduct Disorders",
            characteristics=[
                Characteristic(label='Irrational reactions', significance=1.0),
                Characteristic(label='Difficulty controlling emotions', significance=0.95),
                Characteristic(label='Hostile behaviors', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=137, 
            content="Have your emotional or behavioral issues caused significant problems in your social, educational, or occupational life?", 
            disorder="Disruptive, Impulse-Control, and Conduct Disorders",
            characteristics=[
                Characteristic(label='Life problems', significance=1.0),
                Characteristic(label='Difficulty controlling emotions', significance=0.95),
                Characteristic(label='Hostile behaviors', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=136, 
            content="Do you find it challenging to adhere to societal norms and rules?", 
            disorder="Disruptive, Impulse-Control, and Conduct Disorders",
            characteristics=[
                Characteristic(label='Difficulty conforming to social norms', significance=1.0),
                Characteristic(label='Hostile behaviors', significance=0.95),
                Characteristic(label='Difficulty controlling emotions', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=135, 
            content="Have you engaged in behavior that violates the rights of others, such as aggression or deceit?", 
            disorder="Disruptive, Impulse-Control, and Conduct Disorders",
            characteristics=[
                Characteristic(label='Hostile behaviors', significance=1.0),
                Characteristic(label='Difficulty conforming to social norms', significance=0.95),
                Characteristic(label='Difficulty controlling emotions', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=134, 
            content="Do you frequently have conflicts with authority figures, such as parents, teachers, or supervisors?", 
            disorder="Disruptive, Impulse-Control, and Conduct Disorders",
            characteristics=[
                Characteristic(label='Issues with authority figures', significance=1.0),
                Characteristic(label='Hostile behaviors', significance=0.95),
                Characteristic(label='Difficulty controlling emotions', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=133, 
            content="Do your emotional outbursts often result in aggressive behavior or destruction of property?", 
            disorder="Disruptive, Impulse-Control, and Conduct Disorders",
            characteristics=[
                Characteristic(label='Hostile behaviors', significance=1.0),
                Characteristic(label='Property destruction', significance=0.95),
                Characteristic(label='Difficulty controlling emotions', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=132, 
            content="Do you often find it difficult to control your emotions?", 
            disorder="Disruptive, Impulse-Control, and Conduct Disorders",
            characteristics=[
                Characteristic(label='Difficulty controlling emotions', significance=1.0),
                Characteristic(label='Irrational reactions', significance=0.95),
                Characteristic(label='Life problems', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )

        # ASPD (Antisocial Personality Disorder)
        yield Question(
            id=149, 
            content="Did you exhibit symptoms of conduct disorder before the age of 15?", 
            disorder="ASPD (Antisocial Personality Disorder)",
            characteristics=[
                Characteristic(label='Early behavioral problems', significance=0.95),
                Characteristic(label='Engaging in criminal activities', significance=0.95),
                Characteristic(label='Pathological lying', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=148, 
            content="Do you often show a lack of remorse by being indifferent to or rationalizing the harm you have caused to others?", 
            disorder="ASPD (Antisocial Personality Disorder)",
            characteristics=[
                Characteristic(label='Lack of guilt', significance=1.0),
                Characteristic(label='Pathological lying', significance=0.95),
                Characteristic(label='Engaging in criminal activities', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=147, 
            content="Do you have a history of consistent irresponsibility, such as not honoring financial obligations or maintaining steady work?", 
            disorder="ASPD (Antisocial Personality Disorder)",
            characteristics=[
                Characteristic(label='History of irresponsibility', significance=1.0),
                Characteristic(label='Impulsive decision-making', significance=0.95),
                Characteristic(label='Reckless disregard for safety of self or others', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=146, 
            content="Do you show a reckless disregard for your own safety or the safety of others?", 
            disorder="ASPD (Antisocial Personality Disorder)",
            characteristics=[
                Characteristic(label='Reckless disregard for safety of self or others', significance=1.0),
                Characteristic(label='Impulsive decision-making', significance=0.95),
                Characteristic(label='Physical fights and assaults', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=145, 
            content="Have you been involved in repeated physical fights or assaults?", 
            disorder="ASPD (Antisocial Personality Disorder)",
            characteristics=[
                Characteristic(label='Physical fights and assaults', significance=1.0),
                Characteristic(label='Engaging in criminal activities', significance=0.95),
                Characteristic(label='Reckless disregard for safety of self or others', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=144, 
            content="Do you often make impulsive decisions without planning ahead?", 
            disorder="ASPD (Antisocial Personality Disorder)",
            characteristics=[
                Characteristic(label='Impulsive decision-making', significance=1.0),
                Characteristic(label='Reckless disregard for safety of self or others', significance=0.95),
                Characteristic(label='History of irresponsibility', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=143, 
            content="Do you frequently lie, use aliases, or con others for personal profit or pleasure?", 
            disorder="ASPD (Antisocial Personality Disorder)",
            characteristics=[
                Characteristic(label='Pathological lying', significance=1.0),
                Characteristic(label='Impulsive decision-making', significance=0.95),
                Characteristic(label='Engaging in criminal activities', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=142, 
            content="Have you repeatedly engaged in behaviors that are grounds for arrest, such as destroying property, harassing others, or stealing?", 
            disorder="ASPD (Antisocial Personality Disorder)",
            characteristics=[
                Characteristic(label='Engaging in criminal activities', significance=1.0),
                Characteristic(label='Physical fights and assaults', significance=1.0),
                Characteristic(label='Reckless disregard for safety of self or others', significance=0.95)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )

        # Borderline Personality Disorder
        yield Question(
            id=157, 
            content="Do you frequently express inappropriate, intense anger or have difficulty controlling your anger (e.g., frequent displays of temper, constant anger, recurrent physical fights)?", 
            disorder="Borderline Personality Disorder",
            characteristics=[
                Characteristic(label='Episodes of intense anger', significance=1.0),
                Characteristic(label='Emotional instability', significance=0.95),
                Characteristic(label='Unstable self-image', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=156, 
            content="Do you have chronic feelings of emptiness?", 
            disorder="Borderline Personality Disorder",
            characteristics=[
                Characteristic(label='Chronic feelings of emptiness', significance=1.0),
                Characteristic(label='Unstable self-image', significance=0.95),
                Characteristic(label='Emotional instability', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=155, 
            content="Do you experience affective instability due to a marked reactivity of mood (e.g., intense episodic dysphoria, irritability, or anxiety usually lasting a few hours and only rarely more than a few days)?", 
            disorder="Borderline Personality Disorder",
            characteristics=[
                Characteristic(label='Emotional instability', significance=1.0),
                Characteristic(label='Mood swings', significance=0.95),
                Characteristic(label='Unstable self-image', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=154, 
            content="Do you display recurrent suicidal behavior, gestures, or threats, or self-mutilating behavior?", 
            disorder="Borderline Personality Disorder",
            characteristics=[
                Characteristic(label='Suicidal ideation', significance=1.0),
                Characteristic(label='Self-harming behaviors', significance=0.95),
                Characteristic(label='Emotional instability', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=153, 
            content="Do you engage in impulsivity in at least two areas that are potentially self-damaging (e.g., spending, substance abuse, reckless driving, binge eating)?", 
            disorder="Borderline Personality Disorder",
            characteristics=[
                Characteristic(label='Impulsive decision-making', significance=1.0),
                Characteristic(label='Emotional instability', significance=0.95),
                Characteristic(label='Unstable self-image', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=152, 
            content="Do you experience a markedly and persistently unstable self-image or sense of self?", 
            disorder="Borderline Personality Disorder",
            characteristics=[
                Characteristic(label='Unstable self-image', significance=1.0),
                Characteristic(label='Emotional instability', significance=0.95),
                Characteristic(label='Chronic feelings of emptiness', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=151, 
            content="Do you have a pattern of unstable and intense interpersonal relationships characterized by alternating between extremes of idealization and devaluation?", 
            disorder="Borderline Personality Disorder",
            characteristics=[
                Characteristic(label='Pattern of idealization and devaluation of others', significance=1.0),
                Characteristic(label='Emotional instability', significance=0.95),
                Characteristic(label='Unstable self-image', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=150, 
            content="Do you make frantic efforts to avoid real or imagined abandonment?", 
            disorder="Borderline Personality Disorder",
            characteristics=[
                Characteristic(label='Fear of abandonment', significance=1.0),
                Characteristic(label='Emotional instability', significance=0.95),
                Characteristic(label='Unstable self-image', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )

        # Narcissistic Personality Disorder
        yield Question(
            id=166, 
            content="Do you frequently show arrogant, haughty behaviors or attitudes?", 
            disorder="Narcissistic Personality Disorder",
            characteristics=[
                Characteristic(label='Arrogance', significance=1.0),
                Characteristic(label='Grandiose sense of self-importance', significance=0.95),
                Characteristic(label='Need for excessive admiration', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=165, 
            content="Are you often envious of others or do you believe that others are envious of you?", 
            disorder="Narcissistic Personality Disorder",
            characteristics=[
                Characteristic(label='Envy of others and belief that others are envious of them', significance=1.0),
                Characteristic(label='Grandiose sense of self-importance', significance=0.95),
                Characteristic(label='Arrogance', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=164, 
            content="Do you lack empathy (e.g., are you unwilling to recognize or identify with the feelings and needs of others)?", 
            disorder="Narcissistic Personality Disorder",
            characteristics=[
                Characteristic(label='Lack of empathy', significance=1.0),
                Characteristic(label='Manipulative behaviors', significance=0.95),
                Characteristic(label='Sense of entitlement', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=163, 
            content="Are you interpersonally exploitative (e.g., do you take advantage of others to achieve your own ends)?", 
            disorder="Narcissistic Personality Disorder",
            characteristics=[
                Characteristic(label='Manipulative behaviors', significance=1.0),
                Characteristic(label='Sense of entitlement', significance=0.95),
                Characteristic(label='Lack of empathy', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=162, 
            content="Do you have a sense of entitlement (e.g., do you have unreasonable expectations of especially favorable treatment or automatic compliance with your expectations)?", 
            disorder="Narcissistic Personality Disorder",
            characteristics=[
                Characteristic(label='Sense of entitlement', significance=1.0),
                Characteristic(label='Grandiose sense of self-importance', significance=0.95),
                Characteristic(label='Arrogance', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=161, 
            content="Do you require excessive admiration from others?", 
            disorder="Narcissistic Personality Disorder",
            characteristics=[
                Characteristic(label='Need for excessive admiration', significance=1.0),
                Characteristic(label='Grandiose sense of self-importance', significance=0.95),
                Characteristic(label='Arrogance', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=160, 
            content="Do you believe that you are 'special' and unique and can only be understood by, or should associate with, other special or high-status people (or institutions)?", 
            disorder="Narcissistic Personality Disorder",
            characteristics=[
                Characteristic(label='Grandiose sense of self-importance', significance=1.0),
                Characteristic(label='Sense of entitlement', significance=0.95),
                Characteristic(label='Arrogance', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=159, 
            content="Are you preoccupied with fantasies of unlimited success, power, brilliance, beauty, or ideal love?", 
            disorder="Narcissistic Personality Disorder",
            characteristics=[
                Characteristic(label='Fantasies of unlimited power, brilliance, and ideal love', significance=1.0),
                Characteristic(label='Grandiose sense of self-importance', significance=0.95),
                Characteristic(label='Need for excessive admiration', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )
        yield Question(
            id=158, 
            content="Do you have a grandiose sense of self-importance (e.g., do you exaggerate your achievements and talents, or expect to be recognized as superior without commensurate achievements)?", 
            disorder="Narcissistic Personality Disorder",
            characteristics=[
                Characteristic(label='Grandiose sense of self-importance', significance=1.0),
                Characteristic(label='Arrogance', significance=0.95),
                Characteristic(label='Need for excessive admiration', significance=0.84)
            ], 
            certaintyFactor=0.0, 
            isAsked=False
        )

    # passed on the user answer construct it to a float value
    def construct_answer_to_float(self, answer: str) -> float:
        if answer.lower() == 'yes':
            return 1 
        elif answer.lower() == 'probably':
            return 0.85
        elif answer.lower() == 'do not know':
            return 0.65
        elif answer.lower() == 'probably not':
            return 0.35
        elif answer.lower() == 'no':
            return 0
    
    def ask(self, question):
        print(f'\t\tQ.{self.question_number}  {question} \n')
        self.question_number += 1
        question_text.set(question)
    
    # takes the characteristic list from the question, and the user answer certainty factor 
    # then update the facts (the actual facts those in the working memory not in the question list)
    def update_characteristics(self, characteristics, answer_cf):
        # make the question characteristic as a dictionary
        labels_to_update = {char['label']: char['significance'] for char in characteristics}
        # for all the characteristics facts in the working memory check if this characteristic is in the question list if it was then save it to the new list (characteristic_to_update)
        characteristics_to_update = [char for char in self.facts.values() if isinstance(char, Characteristic) and char['label'] in labels_to_update]
        # iterate over the characteristics_to_update list (which has all the FACTS which is mentioned in the question list too) and update it with in the approbriate way
        for characteristic in characteristics_to_update:
            if characteristic['label'] in labels_to_update:
                new_significance = self.super_certainty * answer_cf * labels_to_update[characteristic['label']]
                self.modify(characteristic, significance=new_significance)
        self.run()
    
    # update the super certainty which affects how much the following answer would be taken seriously
    def update_super_certainty(self, answer_cf):
        if answer_cf >= 0.85:
            answer_cf = 0.95
        elif answer_cf >= 0.65:
            answer_cf = 0.75
        elif answer_cf >= 0.35:
            answer_cf = 0.55
        self.super_certainty *= answer_cf
        self.run()
    
    def result(self, disorder:str):
        global new_window
        new_window = ctk.CTkToplevel(app)
        new_window.geometry("700x200")
        new_window.title("Diagnosed Disorder")
        label_message = ctk.CTkLabel(
            new_window, 
            text=disorder, 
            font=ctk.CTkFont(size=20)
        )
        label_message.pack(pady=20)
        self.halt()

    ##################################################################################################
    #                                        Main Questions                                          #
    ##################################################################################################
    @Rule(
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, isAsked=MATCH.isAsked),
        TEST(lambda id, isAsked: (0 < id < 5) and (not isAsked)),
        salience=100
    )
    def main_questions(self, question_instance, question_content):
        self.ask(question_content)
        # Set the question as asked
        self.modify(question_instance, isAsked=True)
        self.halt()
    
    ##################################################################################################
    #                                     Ask Two From Each                                          #
    ##################################################################################################
    @Rule(
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda num_asked: num_asked < 2),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def ask_two_questions_from_each_disorder(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.is_main_question = False
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as asked
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        # ask one question at a time
        self.halt()

    ##################################################################################################
    #                                      Dissociative Disorders                                    #
    ##################################################################################################
    @Rule(
        Characteristic(label=L('Emotional coldness or detachment'), significance=GE(0.4)),
        Characteristic(label=L('Loss of identity'), significance=GE(0.35)),
        Characteristic(label=L('Memory loss'), significance=GE(0.3)),
        Characteristic(label=L('Multiple personalities'), significance=GE(0.35)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda num_asked, disorder_name: num_asked < 5 and disorder_name == 'Dissociative Disorders'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def little_sus_about_Dissociative_Disorders(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as asked
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        # ask one question at a time
        self.halt()
    @Rule(
        Characteristic(label=L('Emotional coldness or detachment'), significance=GE(0.6)),
        Characteristic(label=L('Acting without awareness and forgetting actions'), significance=GE(0.5)),
        Characteristic(label=L('Loss of identity'), significance=GE(0.45)),
        Characteristic(label=L('Memory loss'), significance=GE(0.6)),
        Characteristic(label=L('Multiple personalities'), significance=GE(0.5)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda disorder_name: disorder_name == 'Dissociative Disorders'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def real_sus_about_Dissociative_Disorders(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as asked
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Emotional coldness or detachment'), significance=GE(0.55)),
        Characteristic(label=L('Acting without awareness and forgetting actions'), significance=GE(0.6)),
        Characteristic(label=L('Loss of identity'), significance=GE(0.6)),
        Characteristic(label=L('Memory loss'), significance=GE(0.5)),
        Characteristic(label=L('Multiple personalities'), significance=GE(0.65)),
        Characteristic(label=L('Daily life problems'), significance=GE(0.5)),
    )
    def it_is_Dissociative_Disorders(self):
        print('you have Dissociative Disorders')
        self.result('you have Dissociative Disorders')
        self.halt()
    
    ##################################################################################################
    #                                          Schizophrenia                                         #
    ##################################################################################################
    @Rule(
        Characteristic(label=L('Hallucinations'), significance=GE(0.4)),
        Characteristic(label=L('Delusional beliefs'), significance=GE(0.4)),
        Characteristic(label=L('Mood fluctuations'), significance=GE(0.35)),
        Characteristic(label=L('Emotional coldness or detachment'), significance=GE(0.35)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda num_asked, disorder_name: num_asked < 5 and disorder_name == 'Schizophrenia'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def little_sus_about_Schizophrenia(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as askedy
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Hallucinations'), significance=GE(0.5)),
        Characteristic(label=L('Delusional beliefs'), significance=GE(0.5)),
        Characteristic(label=L('Neglect of self-care'), significance=GE(0.5)),
        Characteristic(label=L('Daily life problems'), significance=GE(0.4)),
        Characteristic(label=L('Emotional coldness or detachment'), significance=GE(0.4)),
        Characteristic(label=L('Mood fluctuations'), significance=GE(0.4)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda disorder_name: disorder_name == 'Schizophrenia'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def real_sus_about_Schizophrenia(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as asked
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Hallucinations'), significance=GE(0.55)),
        Characteristic(label=L('Delusional beliefs'), significance=GE(0.55)),
        Characteristic(label=L('Neglect of self-care'), significance=GE(0.55)),
        Characteristic(label=L('Daily life problems'), significance=GE(0.55)),
        Characteristic(label=L('Emotional coldness or detachment'), significance=GE(0.6)),
        Characteristic(label=L('Mood fluctuations'), significance=GE(0.5)),
        Characteristic(label=L('Memory loss'), significance=GE(0.5)),
    )
    def it_is_Schizophrenia(self):
        print('you have Schizophrenia')
        self.result('you have Schizophrenia')
        self.halt()

    ##################################################################################################
    #                                       Bipolar Disorder                                         #
    ##################################################################################################
    @Rule(
        Characteristic(label=L('Mood swings'), significance=GE(0.4)),
        Characteristic(label=L('Overconfidence'), significance=GE(0.4)),
        Characteristic(label=L('Daily life problems'), significance=GE(0.4)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda num_asked, disorder_name: num_asked < 5 and disorder_name == 'Bipolar Disorder'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def little_sus_about_Bipolar_Disorder(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as askedy
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Mood swings'), significance=GE(0.45)),
        Characteristic(label=L('Overconfidence'), significance=GE(0.55)),
        Characteristic(label=L('Excessive talking'), significance=GE(0.55)),
        Characteristic(label=L('Reduced need for sleep'), significance=GE(0.55)),
        Characteristic(label=L('Distractions and irrelevant thoughts'), significance=GE(0.55)),
        Characteristic(label=L('Daily life problems'), significance=GE(0.4)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda disorder_name: disorder_name == 'Bipolar Disorder'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def real_sus_about_Bipolar_Disorder(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as asked
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Mood swings'), significance=GE(0.5)),
        Characteristic(label=L('Overconfidence'), significance=GE(0.55)),
        Characteristic(label=L('Excessive talking'), significance=GE(0.6)),
        Characteristic(label=L('Reduced need for sleep'), significance=GE(0.55)),
        Characteristic(label=L('Distractions and irrelevant thoughts'), significance=GE(0.6)),
        Characteristic(label=L('Daily life problems'), significance=GE(0.5)),
        Characteristic(label=L('Emptiness and sadness'), significance=GE(0.55)),
        Characteristic(label=L('Suicidal thoughts'), significance=GE(0.55)),
        Characteristic(label=L('Poor concentration'), significance=GE(0.55)),
        Characteristic(label=L('Indecisiveness'), significance=GE(0.55)),
        Characteristic(label=L('Low self-worth'), significance=GE(0.55)),
        Characteristic(label=L('Feelings of guilt'), significance=GE(0.5)),
        Characteristic(label=L('Loss of energy'), significance=GE(0.55)),
        Characteristic(label=L('Insomnia'), significance=GE(0.55)),
        Characteristic(label=L('Loss of appetite and weight'), significance=GE(0.55)),
        Characteristic(label=L('Distractions and irrelevant thoughts'), significance=GE(0.55)),
    )
    def it_is_Bipolar_Disorder(self):
        print('you have Bipolar Disorder')
        self.result('you have Bipolar Disorder')
        self.halt()
    
    ##################################################################################################
    #                                      Depressive Disorders                                      #
    ##################################################################################################
    @Rule(
        Characteristic(label=L('Emptiness and sadness'), significance=GE(0.45)),
        Characteristic(label=L('Loss of pleasure and interest'), significance=GE(0.5)),
        Characteristic(label=L('Low self-worth'), significance=GE(0.45)),
        Characteristic(label=L('Feelings of guilt'), significance=GE(0.4)),
        Characteristic(label=L('Life problems'), significance=GE(0.4)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda num_asked, disorder_name: num_asked < 5 and disorder_name == 'Depressive Disorders'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def little_sus_about_Depressive_Disorders(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as askedy
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Emptiness and sadness'), significance=GE(0.5)),
        Characteristic(label=L('Loss of pleasure and interest'), significance=GE(0.5)),
        Characteristic(label=L('Loss of appetite and weight'), significance=GE(0.5)),
        Characteristic(label=L('Low self-worth'), significance=GE(0.5)),
        Characteristic(label=L('Feelings of guilt'), significance=GE(0.4)),
        Characteristic(label=L('Life problems'), significance=GE(0.4)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda disorder_name: disorder_name == 'Depressive Disorders'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def real_sus_about_Depressive_Disorders(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as asked
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Emptiness and sadness'), significance=GE(0.6)),
        Characteristic(label=L('Suicidal thoughts'), significance=GE(0.6)),
        Characteristic(label=L('Poor concentration'), significance=GE(0.6)),
        Characteristic(label=L('Indecisiveness'), significance=GE(0.5)),
        Characteristic(label=L('Loss of energy'), significance=GE(0.6)),
        Characteristic(label=L('Insomnia'), significance=GE(0.6)),
        Characteristic(label=L('Loss of pleasure and interest'), significance=GE(0.6)),
        Characteristic(label=L('Loss of appetite and weight'), significance=GE(0.6)),
        Characteristic(label=L('Low self-worth'), significance=GE(0.5)),
        Characteristic(label=L('Feelings of guilt'), significance=GE(0.5)),
        Characteristic(label=L('Life problems'), significance=GE(0.5)),
    )
    def it_is_Depressive_Disorders(self):
        print('you have Depressive Disorders')
        self.result('you have Depressive Disorders')
        self.halt()
    
    ##################################################################################################
    #                                             ADHD                                               #
    ##################################################################################################
    @Rule(
        Characteristic(label=L('Difficulty focusing'), significance=GE(0.5)),
        Characteristic(label=L('Hyperfocus'), significance=GE(0.4)),
        Characteristic(label=L('Forgetfulness in daily activities'), significance=GE(0.4)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda num_asked, disorder_name: num_asked < 5 and disorder_name == 'ADHD'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def little_sus_about_ADHD(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as askedy
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Difficulty focusing'), significance=GE(0.5)),
        Characteristic(label=L('Hyperfocus'), significance=GE(0.5)),
        Characteristic(label=L('Forgetfulness in daily activities'), significance=GE(0.5)),
        Characteristic(label=L('Difficulty following instructions'), significance=GE(0.5)),
        Characteristic(label=L('Daydreaming'), significance=GE(0.6)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda disorder_name: disorder_name == 'ADHD'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def real_sus_about_ADHD(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as asked
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Difficulty focusing'), significance=GE(0.5)),
        Characteristic(label=L('Hyperfocus'), significance=GE(0.5)),
        Characteristic(label=L('Forgetfulness in daily activities'), significance=GE(0.5)),
        Characteristic(label=L('Difficulty following instructions'), significance=GE(0.5)),
        Characteristic(label=L('Daydreaming'), significance=GE(0.6)),
        Characteristic(label=L('Interrupting others'), significance=GE(0.6)),
        Characteristic(label=L('Difficulty waiting'), significance=GE(0.6)),
        Characteristic(label=L('Excessive talking'), significance=GE(0.6)),
        Characteristic(label=L('Constant activity'), significance=GE(0.6)),
        Characteristic(label=L('Difficulty engaging in quiet activities'), significance=GE(0.6)),
        Characteristic(label=L('Losing important items'), significance=GE(0.6)),
        Characteristic(label=L('Impulsivity'), significance=GE(0.5)),
    )
    def it_is_ADHD(self):
        print('you have ADHD')
        self.result('you have ADHD')
        self.halt()
    
    ##################################################################################################
    #                                           Autism                                               #
    ##################################################################################################
    @Rule(
        Characteristic(label=L('Difficulty sharing emotions'), significance=GE(0.5)),
        Characteristic(label=L('Problems with social interactions'), significance=GE(0.4)),
        Characteristic(label=L('Social relationship problems'), significance=GE(0.4)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda num_asked, disorder_name: num_asked < 5 and disorder_name == 'Autism'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def little_sus_about_Autism(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as askedy
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Difficulty sharing emotions'), significance=GE(0.55)),
        Characteristic(label=L('Issues with eye and physical contact'), significance=GE(0.55)),
        Characteristic(label=L('Problems with social interactions'), significance=GE(0.45)),
        Characteristic(label=L('Social relationship problems'), significance=GE(0.45)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda disorder_name: disorder_name == 'Autism'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def real_sus_about_Autism(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as asked
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Difficulty sharing emotions'), significance=GE(0.6)),
        Characteristic(label=L('Issues with eye and physical contact'), significance=GE(0.6)),
        Characteristic(label=L('Problems with social interactions'), significance=GE(0.6)),
        Characteristic(label=L('Social relationship problems'), significance=GE(0.6)),
        Characteristic(label=L('Sensory sensitivities'), significance=GE(0.6)),
        Characteristic(label=L('Insistence on routine'), significance=GE(0.6)),
        Characteristic(label=L('Stubbornness'), significance=GE(0.5)),
        Characteristic(label=L('Repetitive movements or speech'), significance=GE(0.6)),
        Characteristic(label=L('Social relationship problems'), significance=GE(0.6)),
        Characteristic(label=L('Social relationship problems'), significance=GE(0.6)),
        Characteristic(label=L('Attachment to unusual objects or interests'), significance=GE(0.6)),
    )
    def it_is_Autism(self):
        print('you have Autism')
        self.result('you have Autism')
        self.halt()
    
    ##################################################################################################
    #                                      Anxiety Disorders                                         #
    ##################################################################################################
    @Rule(
        Characteristic(label=L('Excessive anxiety in certain situations'), significance=GE(0.5)),
        Characteristic(label=L('Inability to control anxiety'), significance=GE(0.4)),
        Characteristic(label=L('Life problems'), significance=GE(0.4)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda num_asked, disorder_name: num_asked < 5 and disorder_name == 'Anxiety Disorders'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def little_sus_about_Anxiety_Disorders(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as askedy
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Excessive anxiety in certain situations'), significance=GE(0.6)),
        Characteristic(label=L('Inability to control anxiety'), significance=GE(0.5)),
        Characteristic(label=L('Life problems'), significance=GE(0.4)),
        Characteristic(label=L('Avoidance of anxiety-inducing situations'), significance=GE(0.55)),
        Characteristic(label=L('Family history of anxiety disorders'), significance=GE(0.5)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda disorder_name: disorder_name == 'Anxiety Disorders'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def real_sus_about_Anxiety_Disorders(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as asked
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Excessive anxiety in certain situations'), significance=GE(0.6)),
        Characteristic(label=L('Inability to control anxiety'), significance=GE(0.6)),
        Characteristic(label=L('Life problems'), significance=GE(0.5)),
        Characteristic(label=L('Avoidance of anxiety-inducing situations'), significance=GE(0.55)),
        Characteristic(label=L('Family history of anxiety disorders'), significance=GE(0.55)),
        Characteristic(label=L('Physical symptoms'), significance=GE(0.6)),
        Characteristic(label=L('Irritability'), significance=GE(0.55)),
        Characteristic(label=L('Difficulty concentrating'), significance=GE(0.6)),
        Characteristic(label=L('Sleep disturbances'), significance=GE(0.6)),
    )
    def it_is_Anxiety_Disorders(self):
        print('you have Anxiety Disorders')
        self.result('you have Anxiety Disorders')
        self.halt()
    
    ##################################################################################################
    #                                            OCD                                                 #
    ##################################################################################################
    @Rule(
        Characteristic(label=L('Obsessions'), significance=GE(0.5)),
        Characteristic(label=L('Compulsions'), significance=GE(0.4)),
        Characteristic(label=L('Avoidance of situations that trigger obsessions and compulsions'), significance=GE(0.4)),
        Characteristic(label=L('Life problems'), significance=GE(0.45)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda num_asked, disorder_name: num_asked < 5 and disorder_name == 'OCD'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def little_sus_about_OCD(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as askedy
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Obsessions'), significance=GE(0.6)),
        Characteristic(label=L('Compulsions'), significance=GE(0.6)),
        Characteristic(label=L('Avoidance of situations that trigger obsessions and compulsions'), significance=GE(0.5)),
        Characteristic(label=L('Life problems'), significance=GE(0.5)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda disorder_name: disorder_name == 'OCD'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def real_sus_about_OCD(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as asked
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Obsessions'), significance=GE(0.6)),
        Characteristic(label=L('Compulsions'), significance=GE(0.55)),
        Characteristic(label=L('Avoidance of situations that trigger obsessions and compulsions'), significance=GE(0.6)),
        Characteristic(label=L('Life problems'), significance=GE(0.55)),
    )
    def it_is_OCD(self):
        print('you have OCD')
        self.result('you have OCD')
        self.halt()

    ##################################################################################################
    #                                        Somatic Disorders                                       #
    ##################################################################################################
    @Rule(
        Characteristic(label=L('Physical symptoms'), significance=GE(0.55)),
        Characteristic(label=L('Overthinking these symptoms'), significance=GE(0.5)),
        Characteristic(label=L('Life problems'), significance=GE(0.4)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda num_asked, disorder_name: num_asked < 5 and disorder_name == 'Somatic Disorders'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def little_sus_about_Somatic_Disorders(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as askedy
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Overthinking these symptoms'), significance=GE(0.55)),
        Characteristic(label=L('Dissatisfaction with medical advice'), significance=GE(0.55)),
        Characteristic(label=L('Frequent doctor visits'), significance=GE(0.55)),
        Characteristic(label=L('Physical symptoms'), significance=GE(0.5)),
        Characteristic(label=L('Life problems'), significance=GE(0.5)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda disorder_name: disorder_name == 'Somatic Disorders'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def real_sus_about_Somatic_Disorders(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as asked
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Overthinking these symptoms'), significance=GE(0.6)),
        Characteristic(label=L('Dissatisfaction with medical advice'), significance=GE(0.6)),
        Characteristic(label=L('Frequent doctor visits'), significance=GE(0.6)),
        Characteristic(label=L('Physical symptoms'), significance=GE(0.6)),
        Characteristic(label=L('Life problems'), significance=GE(0.6)),
    )
    def it_is_Somatic_Disorders(self):
        print('you have Somatic Disorders')
        self.result('you have Somatic Disorders')
        self.halt()

    ##################################################################################################
    #                                     Feeding Disorders                                          #
    ##################################################################################################
    @Rule(
        Characteristic(label=L('Eating-related issues'), significance=GE(0.5)),
        Characteristic(label=L('Extreme weight loss'), significance=GE(0.5)),
        Characteristic(label=L('Reliance on dietary supplements'), significance=GE(0.45)),
        Characteristic(label=L('Life problems'), significance=GE(0.4)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda num_asked, disorder_name: num_asked < 5 and disorder_name == 'Feeding Disorders'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def little_sus_about_Feeding_Disorders(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as askedy
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Eating-related issues'), significance=GE(0.5)),
        Characteristic(label=L('Extreme weight loss'), significance=GE(0.5)),
        Characteristic(label=L('Reliance on dietary supplements'), significance=GE(0.45)),
        Characteristic(label=L('Life problems'), significance=GE(0.4)),
        Characteristic(label=L('Avoidance or attraction to food based on appearance, smell, taste, and temperature'), significance=GE(0.5)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda disorder_name: disorder_name == 'Feeding Disorders'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def real_sus_about_Feeding_Disorders(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as asked
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Eating-related issues'), significance=GE(0.6)),
        Characteristic(label=L('Extreme weight loss'), significance=GE(0.6)),
        Characteristic(label=L('Reliance on dietary supplements'), significance=GE(0.6)),
        Characteristic(label=L('Life problems'), significance=GE(0.6)),
        Characteristic(label=L('Avoidance or attraction to food based on appearance, smell, taste, and temperature'), significance=GE(0.6)),
        Characteristic(label=L('Fear of choking or vomiting'), significance=GE(0.6)),
    )
    def it_is_Feeding_Disorders(self):
        print('you have Feeding Disorders')
        self.result('you have Feeding Disorders')
        self.halt()

    ##################################################################################################
    #                        Disruptive, Impulse-Control, and Conduct Disorders                      #
    ##################################################################################################
    @Rule(
        Characteristic(label=L('Hostile behaviors'), significance=GE(0.5)),
        Characteristic(label=L('Property destruction'), significance=GE(0.5)),
        Characteristic(label=L('Irrational reactions'), significance=GE(0.5)),
        Characteristic(label=L('Difficulty controlling emotions'), significance=GE(0.4)),
        Characteristic(label=L('Life problems'), significance=GE(0.4)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda num_asked, disorder_name: num_asked < 5 and disorder_name == 'Disruptive, Impulse-Control, and Conduct Disorders'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def little_sus_about_Disruptive_Impulse_Control_and_Conduct_Disorders(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as askedy
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Hostile behaviors'), significance=GE(0.55)),
        Characteristic(label=L('Property destruction'), significance=GE(0.6)),
        Characteristic(label=L('Irrational reactions'), significance=GE(0.6)),
        Characteristic(label=L('Difficulty controlling emotions'), significance=GE(0.55)),
        Characteristic(label=L('Issues with authority figures'), significance=GE(0.6)),
        Characteristic(label=L('Difficulty conforming to social norms'), significance=GE(0.6)),
        Characteristic(label=L('Life problems'), significance=GE(0.5)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda disorder_name: disorder_name == 'Disruptive, Impulse-Control, and Conduct Disorders'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def real_sus_about_Disruptive_Impulse_Control_and_Conduct_Disorders(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as asked
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Hostile behaviors'), significance=GE(0.6)),
        Characteristic(label=L('Property destruction'), significance=GE(0.6)),
        Characteristic(label=L('Irrational reactions'), significance=GE(0.6)),
        Characteristic(label=L('Difficulty controlling emotions'), significance=GE(0.6)),
        Characteristic(label=L('Issues with authority figures'), significance=GE(0.6)),
        Characteristic(label=L('Difficulty conforming to social norms'), significance=GE(0.6)),
        Characteristic(label=L('Life problems'), significance=GE(0.6)),
        Characteristic(label=L('Easily annoyed'), significance=GE(0.6)),
        Characteristic(label=L('Engaging in fire-setting or theft to relieve internal feelings'), significance=GE(0.6)),
        Characteristic(label=L('Feeling misunderstood'), significance=GE(0.6)),
    )
    def it_is_Disruptive_Impulse_Control_and_Conduct_Disorders(self):
        print('you have Disruptive, Impulse-Control, and Conduct Disorders')
        self.result('you have Disruptive, Impulse-Control, and Conduct Disorders')
        self.halt()

    ##################################################################################################
    #                        ASPD (Antisocial Personality Disorder)                                  #
    ##################################################################################################
    @Rule(
        Characteristic(label=L('Pathological lying'), significance=GE(0.5)),
        Characteristic(label=L('Physical fights and assaults'), significance=GE(0.5)),
        Characteristic(label=L('Impulsive decision-making'), significance=GE(0.5)),
        Characteristic(label=L('Engaging in criminal activities'), significance=GE(0.4)),
        Characteristic(label=L('Engaging in criminal activities'), significance=GE(0.4)),
        Characteristic(label=L('Reckless disregard for safety of self or others'), significance=GE(0.4)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda num_asked, disorder_name: num_asked < 5 and disorder_name == 'ASPD (Antisocial Personality Disorder)'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def little_sus_about_ASPD(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as askedy
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Pathological lying'), significance=GE(0.6)),
        Characteristic(label=L('Physical fights and assaults'), significance=GE(0.6)),
        Characteristic(label=L('Impulsive decision-making'), significance=GE(0.6)),
        Characteristic(label=L('Engaging in criminal activities'), significance=GE(0.55)),
        Characteristic(label=L('Reckless disregard for safety of self or others'), significance=GE(0.6)),
        Characteristic(label=L('History of irresponsibility'), significance=GE(0.6)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda disorder_name: disorder_name == 'ASPD (Antisocial Personality Disorder)'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def real_sus_about_ASPD(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as asked
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Pathological lying'), significance=GE(0.6)),
        Characteristic(label=L('Physical fights and assaults'), significance=GE(0.6)),
        Characteristic(label=L('Impulsive decision-making'), significance=GE(0.6)),
        Characteristic(label=L('Engaging in criminal activities'), significance=GE(0.55)),
        Characteristic(label=L('Reckless disregard for safety of self or others'), significance=GE(0.6)),
        Characteristic(label=L('History of irresponsibility'), significance=GE(0.6)),
        Characteristic(label=L('Lack of guilt'), significance=GE(0.6)),
    )
    def it_is_ASPD(self):
        print('you have ASPD (Antisocial Personality Disorder)')
        self.result('you have ASPD (Antisocial Personality Disorder)')
        self.halt()

    ##################################################################################################
    #                               Borderline Personality Disorder                                  #
    ##################################################################################################
    @Rule(
        Characteristic(label=L('Fear of abandonment'), significance=GE(0.5)),
        Characteristic(label=L('Pattern of idealization and devaluation of others'), significance=GE(0.5)),
        Characteristic(label=L('Emotional instability'), significance=GE(0.45)),
        Characteristic(label=L('Unstable self-image'), significance=GE(0.4)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda num_asked, disorder_name: num_asked < 5 and disorder_name == 'Borderline Personality Disorder'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def little_sus_about_Borderline_Personality_Disorder(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as askedy
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Fear of abandonment'), significance=GE(0.6)),
        Characteristic(label=L('Pattern of idealization and devaluation of others'), significance=GE(0.6)),
        Characteristic(label=L('Emotional instability'), significance=GE(0.5)),
        Characteristic(label=L('Unstable self-image'), significance=GE(0.5)),
        Characteristic(label=L('Self-harming behaviors'), significance=GE(0.6)),
        Characteristic(label=L('Suicidal ideation'), significance=GE(0.6)),
        Characteristic(label=L('Chronic feelings of emptiness'), significance=GE(0.55)),
        Characteristic(label=L('Impulsive decision-making'), significance=GE(0.6)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda disorder_name: disorder_name == 'Borderline Personality Disorder'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def real_sus_about_Borderline_Personality_Disorder(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as asked
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Fear of abandonment'), significance=GE(0.65)),
        Characteristic(label=L('Pattern of idealization and devaluation of others'), significance=GE(0.65)),
        Characteristic(label=L('Emotional instability'), significance=GE(0.65)),
        Characteristic(label=L('Unstable self-image'), significance=GE(0.55)),
        Characteristic(label=L('Self-harming behaviors'), significance=GE(0.6)),
        Characteristic(label=L('Suicidal ideation'), significance=GE(0.65)),
        Characteristic(label=L('Chronic feelings of emptiness'), significance=GE(0.55)),
        Characteristic(label=L('Impulsive decision-making'), significance=GE(0.65)),
        Characteristic(label=L('Mood swings'), significance=GE(0.6)),
        Characteristic(label=L('Episodes of intense anger'), significance=GE(0.65)),
    )
    def it_is_Borderline_Personality_Disorder(self):
        print('you have Borderline Personality Disorder')
        self.result('you have Borderline Personality Disorder')
        self.halt()
    
    ##################################################################################################
    #                               Narcissistic Personality Disorder                                #
    ##################################################################################################
    @Rule(
        Characteristic(label=L('Fantasies of unlimited power, brilliance, and ideal love'), significance=GE(0.6)),
        Characteristic(label=L('Grandiose sense of self-importance'), significance=GE(0.55)),
        Characteristic(label=L('Arrogance'), significance=GE(0.55)),
        Characteristic(label=L('Need for excessive admiration'), significance=GE(0.5)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda num_asked, disorder_name: num_asked < 5 and disorder_name == 'Narcissistic Personality Disorder'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def little_sus_about_Narcissistic_Personality_Disorder(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as askedy
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Fantasies of unlimited power, brilliance, and ideal love'), significance=GE(0.6)),
        Characteristic(label=L('Grandiose sense of self-importance'), significance=GE(0.55)),
        Characteristic(label=L('Arrogance'), significance=GE(0.55)),
        Characteristic(label=L('Need for excessive admiration'), significance=GE(0.55)),
        Characteristic(label=L('Grandiose sense of self-importance'), significance=GE(0.6)),
        AS.disorder_instance << Disorder(label=MATCH.disorder_name, number_of_asked_question=MATCH.num_asked),
        TEST(lambda disorder_name: disorder_name == 'Narcissistic Personality Disorder'),
        AS.question_instance << Question(id=MATCH.id, content=MATCH.question_content, disorder=MATCH.disorder_name, characteristics=MATCH.characteristics, isAsked=MATCH.isAsked),
        TEST(lambda isAsked: not isAsked)
    )
    def real_sus_about_Narcissistic_Personality_Disorder(self, disorder_instance, num_asked, question_instance, question_content, characteristics):
        self.ask(question_content)
        self.chars = characteristics
        # Set the question as asked
        self.modify(question_instance, isAsked=True)
        # increase the number of asked question for this disorder (to prevent keep asking question in the same domain)
        self.modify(disorder_instance, number_of_asked_question=num_asked+1)
        self.halt()
    @Rule(
        Characteristic(label=L('Fantasies of unlimited power, brilliance, and ideal love'), significance=GE(0.65)),
        Characteristic(label=L('Grandiose sense of self-importance'), significance=GE(0.65)),
        Characteristic(label=L('Arrogance'), significance=GE(0.65)),
        Characteristic(label=L('Need for excessive admiration'), significance=GE(0.55)),
        Characteristic(label=L('Grandiose sense of self-importance'), significance=GE(0.65)),
        Characteristic(label=L('Manipulative behaviors'), significance=GE(0.65)),
        Characteristic(label=L('Lack of empathy'), significance=GE(0.65)),
        Characteristic(label=L('Sense of entitlement'), significance=GE(0.55)),
    )
    def it_is_Narcissistic_Personality_Disorder(self):
        print('you have Narcissistic Personality Disorder')
        self.result('you have Narcissistic Personality Disorder')
        self.halt()

engine = MyKnowledgeEngine()
engine.reset()
engine.run()

label_question = ctk.CTkLabel(
    app, 
    textvariable=question_text,
    font=ctk.CTkFont(size=18),
    wraplength=wraplength_label
)
label_question.pack(pady=40)

def update(answer:str):
    if engine.is_main_question:
        engine.update_super_certainty(engine.construct_answer_to_float(answer))
    else:
        engine.update_characteristics(engine.chars, engine.construct_answer_to_float(answer))

button_yes = ctk.CTkButton(
    app, 
    text="Yes", 
    command=lambda: update("Yes"), 
    width=width_button,
    height=height_button, 
    font=ctk.CTkFont(size=font_button_size)
)
button_yes.pack(pady=5)

button_probably = ctk.CTkButton(
    app, 
    text="Probably", 
    command=lambda: update("Probably"),
    width=width_button,
    height=height_button, 
    font=ctk.CTkFont(size=font_button_size)
)
button_probably.pack(pady=5)

button_dont_know = ctk.CTkButton(
    app, 
    text="Don't know", 
    command=lambda: update("Do not know"),
    width=width_button, 
    height=height_button, 
    font=ctk.CTkFont(size=font_button_size)
)
button_dont_know.pack(pady=5)

button_probably_not = ctk.CTkButton(
    app, 
    text="Probably not", 
    command=lambda: update("Probably not"),
    width=width_button, 
    height=height_button, 
    font=ctk.CTkFont(size=font_button_size)
)
button_probably_not.pack(pady=5)

button_no = ctk.CTkButton(
    app, 
    text="No", 
    command=lambda: update("No"),
    width=width_button, 
    height=height_button,
    font=ctk.CTkFont(size=font_button_size)
)
button_no.pack(pady=5)

app.mainloop()