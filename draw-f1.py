import cv2
import numpy as np
from sklearn.cluster import KMeans
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python import BaseOptions
import urllib.request
import os
helmet_map = { ###edit this dumbassssssss
    assets = {
    "REDBULL": {
        "verstappen": "helmets/rb_max.png",
        "perez": "helmets/rb_checo.png"
    },
    "MERCEDES": {
        "hamilton": "helmets/merc_lewis.png",
        "russell": "helmets/merc_george.png"
    },
    "FERRARI": {
        "leclerc": "helmets/fer_charles.png",
        "sainz": "helmets/fer_carlos.png"
    }
}
}
# Download the face landmarker model if not present
model_path = 'face_landmarker.task'
if not os.path.exists(model_path):
    url = 'https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task'
    urllib.request.urlretrieve(url, model_path)

base_options = BaseOptions(model_asset_path=model_path)
options = vision.FaceLandmarkerOptions(base_options=base_options, num_faces=1)
face_mesh = vision.FaceLandmarker.create_from_options(options)

def run_f1_quiz():
    print("\n🏎️  THE ULTIMATE 2025 F1 TEAM SORTING EXAM  🏎️")
    
    scores = {
        "ferrari": 0, "mercedes": 0, "redbull": 0, 
        "mclaren": 0, "williams": 0, "astonmartin": 0
    }

    # Helper function to make the code cleaner
    def ask(question, options):
        print(f"\n{question}")
        for key, val in options.items():
            print(f"{key}) {val}")
        return input("Choice: ").lower()

    # --- THE 10 QUESTIONS ---

    # 1. Music/Songs
    q1 = ask("What's on your pre-race playlist?", {'a': 'Dramatic Opera', 'b': 'Precision Techno', 'c': 'Aggressive Hip Hop', 'd': 'Upbeat Indie Pop'})
    if 'a' in q1: scores["ferrari"] += 2
    if 'b' in q1: scores["mercedes"] += 2
    if 'c' in q1: scores["redbull"] += 2
    if 'd' in q1: scores["mclaren"] += 2

    # 2. Older Legends
    q2 = ask("Which legend's legacy do you respect most?", {'a': 'Michael Schumacher', 'b': 'Ayrton Senna', 'c': 'Nigel Mansell', 'd': 'Juan Manuel Fangio'})
    if 'a' in q2: scores["ferrari"] += 2
    if 'b' in q2: scores["mclaren"] += 2; scores["williams"] += 1
    if 'c' in q2: scores["williams"] += 2
    if 'd' in q2: scores["mercedes"] += 2

    # 3. Teamwork
    q3 = ask("Your teammate is faster than you. What do you do?", {'a': 'Let them pass (For the team)', 'b': 'Defend like a lion', 'c': 'Wait for strategy to fix it'})
    if 'a' in q3: scores["mercedes"] += 1; scores["williams"] += 1
    if 'b' in q3: scores["redbull"] += 2; scores["astonmartin"] += 2
    if 'c' in q3: scores["ferrari"] += 1

    # 4. Ideal Car Color
    q4 = ask("Choose a livery color:", {'a': 'Rosso Corsa', 'b': 'British Racing Green', 'c': 'Papaya Orange', 'd': 'Silver/Black'})
    if 'a' in q4: scores["ferrari"] += 2
    if 'b' in q4: scores["astonmartin"] += 2
    if 'c' in q4: scores["mclaren"] += 2
    if 'd' in q4: scores["mercedes"] += 2

    # 5. Weekend Activity
    q5 = ask("Non-race weekend activity?", {'a': 'Fashion Show', 'b': 'Sim Racing', 'c': 'Extreme Sports', 'd': 'Restoring a Classic'})
    if 'a' in q5: scores["mercedes"] += 1; scores["ferrari"] += 1
    if 'b' in q5: scores["redbull"] += 1; scores["mclaren"] += 1
    if 'c' in q5: scores["redbull"] += 2
    if 'd' in q5: scores["williams"] += 2

    # 6. Motivation
    q6 = ask("What motivates you?", {'a': 'Glory & History', 'b': 'Data & Results', 'c': 'Winning at any cost', 'd': 'The Underdog Story'})
    if 'a' in q6: scores["ferrari"] += 2
    if 'b' in q6: scores["mercedes"] += 2
    if 'c' in q6: scores["redbull"] += 2; scores["astonmartin"] += 1
    if 'd' in q6: scores["williams"] += 2

    # 7. Preferred Track
    q7 = ask("Favorite Track Type?", {'a': 'Monaco (Glamour)', 'b': 'Silverstone (History)', 'c': 'Spa (Technical)', 'd': 'Interlagos (Chaos)'})
    if 'a' in q7: scores["ferrari"] += 1; scores["mercedes"] += 1
    if 'b' in q7: scores["williams"] += 2; scores["mclaren"] += 1
    if 'c' in q7: scores["redbull"] += 2
    if 'd' in q7: scores["astonmartin"] += 1

    # 8. Handling a Crash
    q8 = ask("You crashed. Your reaction?", {'a': 'Check the data', 'b': 'Angry Radio Message', 'c': 'Apologize to the mechanics', 'd': 'Stare blankly at the wall'})
    if 'a' in q8: scores["mercedes"] += 2
    if 'b' in q8: scores["ferrari"] += 2; scores["astonmartin"] += 2
    if 'c' in q8: scores["williams"] += 2; scores["mclaren"] += 1
    if 'd' in q8: scores["redbull"] += 1

    # 9. Design Style
    q9 = ask("Car design preference?", {'a': 'Bold & Innovative', 'b': 'Safe & Reliable', 'c': 'Aggressive & Risky'})
    if 'a' in q9: scores["redbull"] += 2; scores["mclaren"] += 1
    if 'b' in q9: scores["mercedes"] += 1; scores["williams"] += 2
    if 'c' in q9: scores["ferrari"] += 1; scores["astonmartin"] += 2

    # 10. The 2025 Goal
    q10 = ask("Your goal for 2025?", {'a': 'The Championship', 'b': 'Top 3', 'c': 'Consistent Points', 'd': 'Beating my teammate'})
    if 'a' in q10: scores["redbull"] += 1; scores["ferrari"] += 1; scores["mclaren"] += 1
    if 'b' in q10: scores["mercedes"] += 1; scores["astonmartin"] += 1
    if 'c' in q10: scores["williams"] += 2
    if 'd' in q10: scores["astonmartin"] += 2

    # FINAL RESULT
    sorted_team = max(scores, key=scores.get)
    print(f"\n✨ THE RESULTS ARE IN...")
    print(f"Based on your answers, you are a perfect match for {sorted_team.upper()}!")
    
    return f"helmets/{sorted_team}.png"

def get_driver_assignment(team_name):
    # Extract team name from path
    team = team_name.split('/')[-1].split('.')[0].lower()
    
    print(f"\n🏁 One final question to see whose seat you're taking at {team.upper()}...")
    
    style = input("What is your racing philosophy? (A: Tactical & Experienced, B: Full Attack & Fearless): ").lower()
    
    # Driver Database for 2025
    lineups = {
        "ferrari": ("Lewis Hamilton", "Charles Leclerc"),
        "mercedes": ("George Russell", "Kimi Antonelli"),
        "redbull": ("Max Verstappen", "Sergio Perez"),
        "mclaren": ("Lando Norris", "Oscar Piastri"),
        "williams": ("Carlos Sainz", "Alex Albon"),
        "astonmartin": ("Fernando Alonso", "Lance Stroll")
    }
    
    drivers = lineups.get(team)
    assigned_driver = drivers[0] if 'a' in style else drivers[1]
    
    print(f"\n🔥 IT'S OFFICIAL: You are replacing {assigned_driver} for the 2025 season!")
    return assigned_driver

def overlay_transparent(bg, overlay, x, y):
    #Std opencv logic to overlay a png with transparency onto a bg
    bg_width=bg.shape[1]
    bg_height=bg.shape[0]

    if x>=bg_width or y>= bg_height:
        return bg
    
    #extract over alpha channel(transparency)

    h,w =overlay.shape[0], overlay.shape[1]
    if x+ w> bg_width:w=bg_width-x
    if y+h> bg_height:h=bg_height-y

    overlay_image=overlay[0:h, 0:w, 0:3]
    mask=overlay[0:h, 0:w,3]/255.0 #normalizing alpha to 0.0 from -1.0

def apply_helmet(img, helmet_path):
    # 1. Detect face landmarks
    results = face_mesh.detect(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if not results.face_landmarks:
        print("No face detected!")
        return img

    # 2. Get the head bounding box
    landmarks = results.face_landmarks[0]
    h, w, _ = img.shape
    top = int(landmarks[10].y * h)      # Forehead
    bottom = int(landmarks[152].y * h)   # Chin
    left = int(landmarks[234].x * w)     # Left cheek
    right = int(landmarks[454].x * w)    # Right cheek

    face_width = right - left
    face_height = bottom - top

    # 3. Load the realistic helmet
    helmet = cv2.imread(helmet_path, -1) # Load with alpha
    if helmet is None: return img

    # 4. Resize: We make the helmet ~60% wider than the face to cover the ears/hair
    helmet_resized = cv2.resize(helmet, (int(face_width * 1.6), int(face_height * 2.0)))

    # 5. Position: Offset it so the visor lines up with the eyes
    x_offset = left - int(face_width * 0.3)
    y_offset = top - int(face_height * 0.7)

    return overlay_transparent(img, helmet_resized, x_offset, y_offset)

if __name__ == "__main__":
    team = run_f1_quiz()
    driver = get_driver_assignment(team)
    
    img = cv2.imread('russell.jpg')
    if img is not None:
        h, w, _ = img.shape
        team_display = team.split('/')[-1].split('.')[0].upper()
        # Put the high-def helmet on the high-def photo
        final_img = apply_helmet(img, team)
        
        # Add the 2025 Branding
        cv2.putText(final_img, f"TEAM: {team_display}", (50, h-100), 
                    cv2.FONT_HERSHEY_DUPLEX, 1.2, (255, 255, 255), 2)
        cv2.putText(final_img, f"DRIVER: {driver}", (50, h-50), 
                    cv2.FONT_HERSHEY_DUPLEX, 1.2, (255, 255, 255), 2)

        cv2.imwrite('f1_driver_card.png', final_img)
        print(f"Deployment successful! Welcome to the grid, {driver}.")