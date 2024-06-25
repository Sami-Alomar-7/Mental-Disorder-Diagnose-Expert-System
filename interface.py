import customtkinter as ctk

app = ctk.CTk()
app.geometry("750x500")
app.title("Mental Disorder Diagnose Expert System")

# Set the theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

questions = [
    "Have you been experiencing symptoms for more than six months?",
    "Have these symptoms significantly affected your ability to work, study, or maintain relationships?",
    "Have you been experiencing any significant changes in your mood or emotions?",
    "Have you been experiencing concentration difficulties?",
    "Do you ever feel detached from yourself, like you're observing your thoughts, feelings, or body from a distance?",
    "Do you describe yourself feeling emotionally numb or like your emotions are muted?",
    "Do you ever feel like there are different 'parts' of you that take control at times?",
    "Have you ever experienced periods where you can't remember important events from your life, especially stressful or traumatic ones?",
    "Do you find yourself missing chunks of memories, like entire days or events, and can't explain why?",
    "Have you been told about things you did or said that you have no memory of?",
    "Do these experiences of detachment or memory loss cause you significant distress or problems in your daily life, or do these experiences affect your relationships, work, or other important areas of functioning?",
    "How long have you been experiencing these feelings of detachment or memory loss?",
    "Do you ever believe things like being watched, followed, or conspired against without clear evidence that others find strange or that you later recognize as unrealistic?",
    "Do you ever hear voices, see things that others do not, or feel any unusual sensory perceptions, like something touching you when nothing is there?",
    "Do you often find that your speech becomes jumbled or incoherent, making it hard for others to understand you, or frequently lose track of your thoughts or find it difficult to follow a conversation?",
    "Do you notice a lack of motivation or a diminished ability to express emotions, or have others mentioned that you seem emotionally flat or withdrawn?",
    "Do you find it difficult to take care of yourself or perform daily tasks compared to before the symptoms started?",
    "Have you experienced mood episodes (depressive or manic) that coincide with these symptoms, and if so, are the mood episodes shorter in duration compared to the psychotic symptoms?",
    "Have you ever been diagnosed with a mood disorder (depression or bipolar disorder) that includes psychotic features?",
    "Have you experienced multiple episodes of these symptoms?",
    "Have you experienced periods of abnormally and persistently elevated, expansive, or irritable mood lasting at least four consecutive days?",
    "During these periods, did you feel more self-confident or grandiose than usual?",
    "Did you notice a decreased need for sleep during these periods (e.g., feeling rested after only a few hours of sleep)?",
    "Were you more talkative than usual or felt pressured to keep talking?",
    "Did you experience racing thoughts or a flight of ideas?",
    "Did you find yourself easily distracted by unimportant or irrelevant things?",
    "Did you engage in activities that are risky or could have painful consequences (e.g., unrestrained spending, or foolish business investments)?",
    "Have you had periods where you felt persistently sad, empty, or hopeless?",
    "During these periods, did you lose interest or pleasure in most activities?",
    "Did you experience significant weight loss or gain, or a change in appetite?",
    "Did you have trouble sleeping (insomnia) or did you sleep excessively (hypersomnia)?",
    "Did you feel unusually tired or had a lack of energy?",
    "Did you have feelings of worthlessness or excessive guilt?",
    "Did you have trouble concentrating or making decisions?",
    "Did you have recurrent thoughts of death or suicide?",
    "Have these mood changes significantly affected your work or social life?",
    "Have you been able to maintain your usual level of functioning during these mood episodes?",
    "Have you experienced four or more mood episodes (manic, hypomanic, or depressive) within a single year?",
    "Do you have a family history of bipolar disorder, depression, or other mood disorders?",
    "Have you felt depressed most of the day, nearly every day, for at least two weeks?",
    "Do you often feel sad, empty, or hopeless?",
    "Have you lost interest or pleasure in most activities that you previously enjoyed?",
    "Have you experienced significant weight loss or weight gain without trying to diet?",
    "Have you noticed a significant decrease or increase in your appetite nearly every day?",
    "Do you have trouble sleeping (insomnia) or do you sleep too much (hypersomnia) nearly every day?",
    "Do you feel fatigued or have a loss of energy nearly every day?",
    "Do you feel worthless or excessively guilty nearly every day?",
    "Do you find it difficult to think, concentrate, or make decisions nearly every day?",
    "Do you have recurrent thoughts of death or suicide?",
    "Have you ever planned or attempted suicide?",
    "Do you often fail to give close attention to details or make careless mistakes in schoolwork, at work, or during other activities (e.g., overlook or miss details, work is inaccurate)?",
    "Do you often have difficulty sustaining attention in tasks or play activities (e.g., difficulty remaining focused during lectures, conversations, or lengthy reading)?",
    "Do you often not seem to listen when spoken to directly (e.g., mind seems elsewhere, even in the absence of any obvious distraction)?",
    "Do you often not follow through on instructions and fail to finish schoolwork, chores, or duties in the workplace (e.g., start tasks but quickly lose focus and get easily sidetracked)?",
    "Do you often have difficulty organizing tasks and activities (e.g., difficulty managing sequential tasks, keeping materials and belongings in order, messy or disorganized work, poor time management, failure to meet deadlines)?",
    "Do you often avoid, dislike, or are reluctant to engage in tasks that require sustained mental effort (e.g., schoolwork or homework; for older adolescents and adults, preparing reports, completing forms, reviewing lengthy papers)?",
    "Do you often lose things necessary for tasks or activities (e.g., school materials, pencils, books, tools, wallets, keys, paperwork, eyeglasses, mobile phones)?",
    "Are you often easily distracted by extraneous stimuli (for older adolescents and adults, this may include unrelated thoughts)?",
    "Are you often forgetful in daily activities (e.g., doing chores, running errands; for older adolescents and adults, returning calls, paying bills, keeping appointments)?",
    "Do you often fidget with or tap your hands or feet, or squirm in your seat?",
    "Do you often leave your seat in situations when remaining seated is expected (e.g., leave your place in the classroom, in the office or other workplace, or in other situations that require remaining in place)?",
    "Are you often unable to play or engage in leisure activities quietly?",
    "Are you often 'on the go,' acting as if 'driven by a motor' (e.g., unable to be or uncomfortable being still for extended time, such as in restaurants, meetings; may be experienced by others as being restless or difficult to keep up with)?",
    "Do you often talk excessively?",
    "Do you often blurt out an answer before a question has been completed (e.g., complete people’s sentences, cannot wait for your turn in conversation)?",
    "Do you often have difficulty waiting your turn (e.g., while waiting in line)?",
    "Do you often interrupt or intrude on others (e.g., butt into conversations, games, or activities; may start using other people’s things without asking or receiving permission; for adolescents and adults, may intrude into or take over what others are doing)?",
    "Do you initiate or respond to social interactions?",
    "Do you share interests or emotions with others?",
    "Have you noticed any difficulties in your initiating or responding to social interactions?",
    "Do you use eye contact, gestures, and facial expressions when communicating?",
    "Are there any abnormalities in your body language or use of gestures?",
    "Do you have difficulties understanding or using nonverbal communication?",
    "Do you have difficulties making or maintaining friendships?",
    "Do you understand and adjust your behavior to suit different social contexts?",
    "Is there an absence of interest in peers or shared imaginative play?",
    "Does your child engage in repetitive motor movements or use objects in a repetitive way (e.g., lining up toys, flipping objects)?",
    "Does your child repeat phrases or use idiosyncratic speech patterns?",
    "Do you insist on following specific routines or get distressed by small changes in your environment?",
    "Are there rigid thinking patterns or ritualized behaviors you adhere to?",
    "Do you have highly restricted interests that are abnormal in intensity or focus?",
    "Is there a strong attachment or preoccupation with unusual objects or topics?",
    "Are you hyper or hypo reactive to sensory input?",
    "Do you often find it difficult to control your emotions?",
    "Do your emotional outbursts often result in aggressive behavior or destruction of property?",
    "Do you frequently have conflicts with authority figures, such as parents, teachers, or supervisors?",
    "Have you engaged in behavior that violates the rights of others, such as aggression or deceit?",
    "Do you find it challenging to adhere to societal norms and rules?",
    "Have your emotional or behavioral issues caused significant problems in your social, educational, or occupational life?",
    "Have you experienced frequent temper outbursts or feelings of anger that are disproportionate to the situation?",
    "Do you often feel misunderstood or that others unfairly blame you for your actions?",
    "Do you often feel irritable or easily annoyed?",
    "Have you engaged in behaviors such as fire setting or stealing to relieve internal tension?",
    "Have you repeatedly engaged in behaviors that you know are harmful to yourself or others?",
    "Do you feel a sense of relief or gratification after engaging in such behaviors?",
    "Have you had difficulty experiencing empathy or understanding the feelings of others?",
    "Have you had difficulty expressing remorse or guilt after harming others?",
    "Have you noticed any changes in your thoughts, such as paranoid or delusional thinking?",
    "Have you felt excessively suspicious or mistrustful of others without justified cause?",
    "Have you had frequent episodes of feeling extremely anxious or fearful in social situations?",
    "Do you avoid social interactions due to fear of being judged, embarrassed, or rejected?",
    "Do you have a persistent fear of being abandoned by people close to you?",
    "Do you often go to extreme lengths to avoid perceived or real abandonment?",
    "Have you experienced rapid changes in mood or unstable relationships?",
    "Do you have a persistent and pervasive pattern of unstable and intense interpersonal relationships?",
    "Do you experience a chronic sense of emptiness or boredom?",
    "Do you engage in impulsive or self-destructive behaviors, such as spending sprees, substance abuse, reckless driving, or self-harm?",
    "Do you experience intense episodes of anger or difficulty controlling your temper?",
    "Do you have a distorted self-image or sense of identity?",
    "Do you often feel disconnected or detached from your surroundings, yourself, or your thoughts?",
    "Do you have difficulty trusting others or forming close relationships?",
    "Do you experience excessive shyness or social inhibition?",
    "Do you have a need for admiration and a lack of empathy for others?",
    "Do you have a grandiose sense of self-importance or believe you are special or unique?",
    "Do you feel entitled to special treatment or expect others to comply with your wishes?",
    "Do you have difficulty recognizing or identifying your own feelings or the feelings of others?",
    "Do you engage in behaviors that seek to gain admiration or attention from others?",
    "Do you have difficulty handling criticism or feel easily hurt by perceived criticism?",
    "Do you often compare yourself to others or feel envious of others?",
    "Do you have a pattern of manipulative or deceitful behavior to achieve your own ends?",
    "Do you experience significant difficulty in regulating your emotions?",
    "Do you have a pervasive distrust and suspicion of others?",
    "Do you often interpret benign actions of others as malicious or threatening?",
    "Do you feel isolated or detached from society?",
    "Do you have an intense fear of criticism, disapproval, or rejection?",
    "Do you have a need for orderliness, perfectionism, and control?",
    "Do you have difficulty making decisions without excessive reassurance from others?",
    "Do you have a pattern of excessive dependency and submissive behavior?",
    "Do you feel a constant need to be taken care of by others?",
    "Do you often have difficulty in expressing disagreement with others due to fear of losing their support or approval?",
    "Do you often volunteer to do things that are unpleasant to gain the approval of others?",
    "Do you feel uncomfortable or helpless when alone, fearing you cannot care for yourself?",
    "Do you have an exaggerated need for others to assume responsibility for most areas of your life?",
    "Do you have difficulty starting projects or doing things on your own due to lack of self-confidence or self-reliance?",
    "Do you feel uncomfortable or helpless when alone due to exaggerated fears of being unable to care for yourself?",
    "Do you urgently seek another relationship as a source of care and support when a close relationship ends?",
    "Do you have an unrealistic preoccupation with fears of being left to take care of yourself?",
    "Do you have a chronic pattern of instability in interpersonal relationships, self-image, and emotions?",
    "Do you frequently engage in impulsive behaviors that are potentially self-damaging?",
    "Do you have a chronic feeling of emptiness or boredom?",
    "Do you have intense and inappropriate anger or difficulty controlling your temper?",
    "Do you experience transient, stress-related paranoid ideation or severe dissociative symptoms?",
    "Do you often feel detached from reality or have feelings of unreality?"
]

global current_question_index
current_question_index = 0


def update_question():
    question_text.set(questions[current_question_index])


# IT's Ofcourse fake
def handle_answer(answer):
    global current_question_index
    print(f"Question: {questions[current_question_index]}")
    print(f"Answer: {answer}\n")
    current_question_index += 1
    if current_question_index < len(questions):
        update_question()
    else:
        label_question.configure(text="Thank you for your responses. Please wait for the diagnosis.")


width_button = 150
height_button = 40
font_button_size = 16
wraplength_label = 700

label_title = ctk.CTkLabel(app, text="Mental Disorder Diagnose Expert System", font=ctk.CTkFont(size=24, weight="bold"))
label_title.pack(pady=20)

question_text = ctk.StringVar()
question_text.set(questions[current_question_index])

label_question = ctk.CTkLabel(app, textvariable=question_text, font=ctk.CTkFont(size=18), wraplength=wraplength_label)
label_question.pack(pady=40)

button_yes = ctk.CTkButton(app, text="Yes", command=lambda: handle_answer("Yes"), width=width_button,
                           height=height_button, font=ctk.CTkFont(size=font_button_size))
button_yes.pack(pady=5)

button_probably = ctk.CTkButton(app, text="Probably", command=lambda: handle_answer("Probably"), width=width_button,
                                height=height_button, font=ctk.CTkFont(size=font_button_size))
button_probably.pack(pady=5)

button_dont_know = ctk.CTkButton(app, text="Don't know", command=lambda: handle_answer("Don't know"),
                                 width=width_button, height=height_button, font=ctk.CTkFont(size=font_button_size))
button_dont_know.pack(pady=5)

button_probably_not = ctk.CTkButton(app, text="Probably not", command=lambda: handle_answer("Probably not"),
                                    width=width_button, height=height_button, font=ctk.CTkFont(size=font_button_size))
button_probably_not.pack(pady=5)

button_no = ctk.CTkButton(app, text="No", command=lambda: handle_answer("No"), width=width_button, height=height_button,
                          font=ctk.CTkFont(size=font_button_size))
button_no.pack(pady=5)

app.mainloop()
