import streamlit as st
import time
from PIL import Image
import pandas as pd
from sklearn.linear_model import LogisticRegression

x_data = pd.read_csv("E:/STUDY/medicine/train_dataset_stroke.csv")
y_data = pd.read_csv("E:/STUDY/medicine/target_dataset_stroke.csv")
x_train = x_data[
    ['age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi', 'Male', 'Govt_job', 'Private', 'Self-employed',
     'children', 'Urban', 'formerly smoked', 'never smoked', 'smokes', 'Married']]
y_train = y_data['stroke']
Method = LogisticRegression(C=1.0, max_iter=1200, penalty='l1', solver='liblinear')
Method.fit(x_train, y_train)
score1 = Method.score(x_train, y_train)


def predictions(age, hypertension, heart_disease, avg_glucose_level, bmi, male, govt_job, private, selfemployed,
                children, urban, formerly_smoked, never_smoked, smokes, married):
    prediction = Method.predict(
        [[age, hypertension, heart_disease, avg_glucose_level, bmi, male, govt_job, private, selfemployed,
          children, urban, formerly_smoked, never_smoked, smokes, married]])
    return prediction


bp = 0
heart = 0
glucose = 0
BODY_M_I = 0
gender = 0
gov = 0
privat = 0
self = 0
child = 0
loc = 0
F_smoke = 0
N_smoke = 0
smoke = 0
even = 0
st.sidebar.title("BODY MASS INDEX (BMI)")
H = st.sidebar.text_input("HEIGHT(m)", '1.82')
try:
    H = float(H)
except ValueError as e:
    st.sidebar.error("please enter valid input")

W = st.sidebar.text_input("WEIGHT(Kg)", '76')
try:
    W = float(W)
except ValueError as e:
    st.sidebar.error("please enter valid input")

B = float(W) / float(H) ** 2
BMI = st.sidebar.write("Your Body Mass Index is : ", B)
if B <= 18.5:
    st.sidebar.error("You are UnderWeight")
elif (B >= 18.5) and (B <= 24.9):
    st.sidebar.success("You have Normal Weight")
elif (B >= 25) and (B <= 29.9):
    st.sidebar.warning("You are Overweight")
elif (B >= 30) and (B <= 34.9):
    st.sidebar.error("You are Obese")
else:
    st.sidebar.error("You are Extremely Obese")
st.markdown("<h1 style='text-align: center; color:#F8FE08 ;'>STROKE</h1>", unsafe_allow_html=True)
img = Image.open("E:/STUDY/medicine/5 Foods That Can Trigger a Stroke.jpg")
col4, col5, col6 = st.beta_columns(3)
col5.image(img, width=200)
st.markdown("<h3 style='text-align: center; color: #FE0813;'>DISCLAIMER</h3>", unsafe_allow_html=True)
st.write("This prediction is done on the basics of data set which has taken from kaggle.com."
         "The information provided herein is accurate, updated and complete as per the best practices of the project. "
         "Please note that this information should not be treated as a replacement for physical medical consultation or"
         " advice.")
st.markdown("<h2 style='text-align: center; color:#D35400 ;'>FILL THIS FORM </h2>", unsafe_allow_html=True)
age = st.slider("AGE", 0, 110)
age = int(age)
Gender = st.selectbox("GENDER", ['MALE', 'FEMALE'])
if Gender == 'MALE':
    gender = 1
elif Gender == 'FEMALE':
    gender = 0
Locality = st.selectbox("LOCATION", ['URBAN', 'RULER'])
if Locality == 'URBAN':
    loc = 1
elif Locality == 'RULER':
    loc = 0
Occupation = st.selectbox("OCCUPATION",
                          ['CHILD', 'STUDENT', 'GOVERNMENT JOB', 'PRIVATE JOB', 'SELF-EMPLOYED'])
if Occupation == 'CHIlD':
    child = 1
    gov = 0
    privat = 0
    self = 0
elif Occupation == 'STUDENT':
    child = 1
    gov = 0
    privat = 0
    self = 0
elif Occupation == 'GOVERNMENT JOB':
    child = 0
    gov = 1
    privat = 0
    self = 0
elif Occupation == 'PRIVATE JOB':
    child = 0
    gov = 0
    privat = 1
    self = 0
elif Occupation == 'SELF-EMPLOYED':
    child = 0
    gov = 0
    privat = 0
    self = 1
Smoke = st.selectbox("SMOKE", ['SMOKE', 'FORMAL SMOKE', 'NEVER SMOKE', 'UNKNOWN'])
if Smoke == 'SMOKE':
    smoke = 1
    F_smoke = 0
    N_smoke = 0
elif Smoke == 'FORMAL SMOKE':
    smoke = 0
    F_smoke = 1
    N_smoke = 0
elif Smoke == 'NEVER SMOKE':
    smoke = 0
    F_smoke = 0
    N_smoke = 1
elif Smoke == 'UNKNOWN':
    smoke = 0
    F_smoke = 0
    N_smoke = 0
BP = st.radio("HYPERTENSION", ('YES', 'NO'))
if BP == 'YES':
    bp = 1
elif BP == 'NO':
    bp = 0
Heart = st.radio("HEART DISEASE", ("YES", "NO"))
if Heart == str('YES'):
    heart = 1
elif Heart == str('NO'):
    heart = 0
Married = st.radio("MARRIED", ('YES', 'NO'))
if Married == 'YES':
    even = 1
else:
    even = 0
bmi = st.text_input("BMI(you can calculate your bmi in sidebar)", B)
try:
    BODY_M_I = float(bmi)
except ValueError as e:
    st.error("Please enter valid input")
Glucose = st.text_input("AVERAGE GLUCOSE LEVEL", "120.7")
try:
    glucose = float(Glucose)
except ValueError as e:
    st.error("Please enter valid input")
col1, col2, col3 = st.beta_columns(3)
if col2.button('Get the Result'):
    with st.spinner("Analysing your Data........................"):
        time.sleep(5)
    pre = predictions(age, bp, heart, glucose, BODY_M_I, gender, gov, privat, self, child, loc,
                      F_smoke, N_smoke, smoke, even)
    if pre == [0]:
        st.success("you are having less chance to get Stroke")
        st.balloons()
    elif pre == [1]:
        st.error("there is higher chance to have Stroke")
st.title("FEW POINTS YOU SHOULD KNOW ABOUT THE STROKE")
img = Image.open("E:/STUDY/medicine/7 Symptoms of Strokes in Women.jpg")
col4, col5, col6 = st.beta_columns(3)
col5.image(img, width=300, caption="Download from @pinterest")
st.write(
    "According to the [World Health Organization "
    "(WHO)](https://www.who.int/news-room/fact-sheets/detail/the-top-10-causes-of-death)"
    " stroke is the 2nd leading cause of death globally, responsible for approximately 11% of total deaths.")
st.title("What is Stroke?")
st.write(
    "A stroke occurs when a blockage or bleed of the blood vessels either interrupts or reduces the supply of blood"
    " to the brain. When this happens, the brain does not receive enough oxygen or nutrients, and brain cells start"
    " to die.Stroke is a cerebrovascular disease. This means that it affects the blood vessels that feed the brain"
    " oxygen. If the brain does not receive enough oxygen, damage may start to occur.This is a medical emergency."
    " Although many strokes are treatable, some can lead to disability or death.")
st.title("Symptoms")
st.write(" \n ")
img1 = Image.open("E:/STUDY/medicine/Is it fatigue – or a stroke_ Women shouldn't ignore these warning signs.jpg")
col4, col5, col6 = st.beta_columns(3)
col4.image(img1, width=400, caption="Download from @pinterest")
st.write("The symptoms of a stroke often appear without warning. Some of the main symptoms include:")
st.write(''' 1.)***Balance difficulty*** \n
2.)***Vertigo (spinning sensation)***\n
3.)***Dizziness***\n
4.)***Double vision***\n
5.)***Loss of coordination***\n
6.)***Swallowing difficulty***\n
7.)***Difficulty articulating words***\n
8.)***Numbness***\n
9.)***Loss of sensation***\n
10.)***Weakness in one half of the body***\n
11.)***Nausea***\n
Learning the acronym “FAST” is a good way to remember the symptoms of stroke. This can help a person seek prompt treatment.
 \n**FAST** stands for:\n
\n
**Face drooping**: If the person tries to smile, does one side of their face droop?\n
**Arm weakness**: If the person tries to raise both their arms, does one arm drift downward?\n
**Speech difficulty**: If the person tries to repeat a simple phrase, is their speech slurred or unusual?\n
**Time to act**: If any of these symptoms are occurring, contact the emergency services immediately.\n
''')
st.title("Causes and risk factors")
st.write('''Each type of stroke has a different set of potential causes. Generally, however, stroke is more likely to 
affect a person if they:\n

1.)***have overweight or obesity***\n
2.)***are 55 years of age or older***\n
3.)***have a personal or family history of stroke***\n
4.)***have high blood pressure***\n
5.)***have diabetes***\n
6.)***have high cholesterol***\n
7.)***have heart disease, carotid artery disease, or another vascular disease
are sedentary***\n
8.)***consume alcohol excessively***\n
9.)***smoke***\n
10.)***use illicit drugs***\n
''')
st.title("Prevention")
st.write("\n")
img2 = Image.open("E:/STUDY/medicine/What Is A Massive Stroke_.jpg")
col4, col5, col6 = st.beta_columns(3)
col4.image(img2, width=500, caption="Download from @pinterest")
st.write('''The best way to prevent a stroke is to address the underlying causes. People can achieve this by making 
lifestyle changes such as:\n

1.)***eating a healthful diet***\n
2.)***maintaining a moderate weight***\n
3.)***exercising regularly***\n
4.)***not smoking tobacco***\n
5.)***avoiding alcohol, or only drinking moderately***\n
Eating a nutritious diet means including plenty of:\n
1.)***fruits***\n
2.)***vegetables***\n
3.)***whole grains***\n
4.)***nuts***\n
5.)***seeds***\n
6.)***legumes***\n
Be sure to limit the amount of red and processed meat in the diet, as well as cholesterol and saturated fats. 
Also, moderate salt intake to support healthy blood pressure levels.

Other measures a person can take to help reduce the risk of stroke include:

1.)**controlling their blood pressure levels**\n
2.)**managing diabetes**\n
3.)**getting treatment for heart disease
As well as**\n 
''')
st.title("Diagnosis")
st.write('''Diagnosis of a pontine stroke requires a thorough neurologic examination. Some diagnostic imaging tests, 
such as brain magnetic resonance imaging (MRI) and brain magnetic resonance angiography (MRA) or computerized tomography 
(CT) angiogram, can help confirm the diagnosis of a pontine stroke.
''')
st.title("Treatment")
st.write('''Stroke treatment depends on getting medical attention as soon as possible. Treatment with the clot-dissolving 
drug tissue plasminogen activator (tPA) can be effective for the treatment of ischemic stroke only if it is administered 
within three hours of the onset of stroke symptoms.\n
During recovery after a stroke, there are several stroke treatments that can help maximize improvement, including blood 
thinners, fluid management, treatment of heart problems, and maintaining adequate nutrition
''')
st.title("Conclusion")
st.write('''
Recovery from a pontine stroke is possible. If you have experienced a pontine stroke, once your symptoms stabilize over 
time, the focus of your recovery will be based on preventing complications such as choking and preventing further strokes 
from happening.\n

Strokes in the brain stem do not affect language ability, and this makes it easier to participate in rehabilitation therapy. 
Vertigo and double vision typically resolve if the stroke is mild or moderate. Physical therapy and rehabilitation are 
important components of stroke recovery\n
\n
\n
\n
''')
st.write("for more information [click here........](https://www.medicalnewstoday.com/articles/7624)")
