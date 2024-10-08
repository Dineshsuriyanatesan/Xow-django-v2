
# # import re
# # from django.shortcuts import render
# # import pyrebase
# # import requests
# # from django.contrib import auth
# # import os
# # import moviepy.video.io.ffmpeg_tools
# # from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# # from django.conf.urls.static import static


# # from django.shortcuts import render
# # from django.http import JsonResponse, HttpResponse


# # from django.core.wsgi import get_wsgi_application

# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro1.settings')

# # application = get_wsgi_application()

# # import os

# # import easyocr


# # import cv2



# # from django.conf.urls.static import static


# # config = {

# # 'apiKey': "AIzaSyDfStYg1oybMuNWma1-4KGJynjrPwIfyhU",
# #   'authDomain': "exhibiton-ce35a.firebaseapp.com",
# #   'databaseURL': "https://exhibiton-ce35a-default-rtdb.firebaseio.com",
# #   'projectId': "exhibiton-ce35a",
# #   'storageBucket': "exhibiton-ce35a.appspot.com",
# #   'messagingSenderId': "241695038706",
# #   'appId': "1:241695038706:web:91fe325c99c663f7f4c46b",
# #   'measurementId': "G-Z9LMLY6ZK8"
# #   }


# # firebase = pyrebase.initialize_app(config)
# # database=firebase.database()
# # authe = firebase.auth()

# # def landing(request):

# #     return render(request, "signIn.html")

# # def singIn(request):

# #     return render(request, "signIn.html")


# # def postsign(request):
# #     email=request.POST.get('email')
# #     passw = request.POST.get("pass")
# #     try:
# #         user = authe.sign_in_with_email_and_password(email,passw)
# #     except:
# #         message = "invalid cerediantials"
# #         return render(request,"signIn.html",{"msg":message})
# #     # print(user)
# #     session_id = user['idToken']
# #     request.session['uid'] = str(session_id)
# #     idtoken = request.session['uid']
# #     a = authe.get_account_info(idtoken)
# #     a = a['users']
# #     a = a[0]
# #     a = a['localId']
# #     name = database.child('users').child(a).child('details').child('name').get().val()

# #     return render(request, "upload.html",{"name":name})

# # def logout(request):
# #     auth.logout(request)
# #     return render(request,'signIn.html')


# # def postsignup(request):
# #     name = request.POST.get('name')
# #     email = request.POST.get('email')
# #     passw = request.POST.get('pass')
# #     try:
# #         user = authe.create_user_with_email_and_password(email, passw)
# #         uid = user['localId']
# #         data = {"name": name, "status": "1"}
# #         database.child("users").child(uid).child("details").set(data)
# #         authe.send_email_verification(user['idToken'])

# #     except:
# #         message = "Weak Password, Use Some Special Characters"
# #         return render(request, "signIn.html", {"messg": message})


# #     return render(request, "signIn.html",{"messg": "Check Your Mail!"})


# # def create(request):
# #     idtoken = request.session['uid']
# #     a = authe.get_account_info(idtoken)
# #     a = a['users']
# #     a = a[0]
# #     a = a['localId']
# #     name = database.child('users').child(a).child('details').child('name').get().val()
# #     return render(request,'upload.html',{"name":name})

# # def post_create(request):


# #     millis = "videourls"
# #     # print("mili"+str(millis))
# #     url = request.POST.get('url')
# #     urlcsv = request.POST.get('csvurl')
# #     idtoken= request.session['uid']
# #     a = authe.get_account_info(idtoken)
# #     a = a['users']
# #     a = a[0]
# #     a = a['localId']
# #     # print("info"+str(a))
# #     data = {
# #         'url':url

# #     }
# #     database.child('users').child(a).child('reports').child(millis).set(data)


# #     idtoken = request.session['uid']
# #     a = authe.get_account_info(idtoken)
# #     a = a['users']
# #     a = a[0]
# #     a = a['localId']

# #     img_url = database.child('users').child(a).child('reports').child('videourls').child('url').get().val()
# #     # print(img_url)
    



# #     return render(request,'Csvupload.html', {'i':img_url})
# # def load_file(filepath):
# #     response = requests.get(filepath)
# #     if response.status_code == 200:
# #         filepath1=os.path.join('static', 'files/sheets.csv')
# #         with open(filepath1, "wb") as file:
# #             file.write(response.content)
# #             print("Excel File has been Fetched and written Successfully!")
# #         return True
# #     else:
# #         return False

# # def post_createcsv(request):
# #     millis = "csvurls"
# #     # print("mili" + str(millis))
# #     url = request.POST.get('url')
# #     idtoken = request.session['uid']
# #     a = authe.get_account_info(idtoken)
# #     a = a['users']
# #     a = a[0]
# #     a = a['localId']
# #     # print("info" + str(a))
# #     data = {
# #         'csvurl': url

# #     }
# #     database.child('users').child(a).child('reports').child(millis).set(data)

# #     idtoken = request.session['uid']
# #     a = authe.get_account_info(idtoken)
# #     a = a['users']
# #     a = a[0]
# #     a = a['localId']

# #     video_url = database.child('users').child(a).child('reports').child('videourls').child('url').get().val()
# #     csv_url = database.child('users').child(a).child('reports').child('csvurls').child('csvurl').get().val()
# #     # print("csvurl")
# #     # print(csv_url)
# #     load_file(csv_url)

# #     os.environ['KMP_DUPLICATE_LIB_OK']='True'
# #     # Replace 'path/to/your/video.mp4' with the actual path to your video file
# #     video_path = video_url
    
# #     # Create an EasyOCR Reader
# #     reader = easyocr.Reader(['en'])
    
# #     # Open the video file
# #     cap = cv2.VideoCapture(video_path)
# #     # Get total frames and frame rate
# #     total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# #     fps = int(cap.get(cv2.CAP_PROP_FPS))

# #     # Calculate video duration in seconds
# #     video_duration_seconds = int(total_frames / fps)
# #     print("Video Duration = ",video_duration_seconds)
# #     # Process the frames
# #     #stop_processing = False
# #     # Define the time pattern
    
# #     #regex_str = r'Date:\s(\d{4}-\d{2}-\d{2})\sTime:\s(\d{2}\:\d{2}\:\d{2}\s(?:AM|PM))\sFrame:\s(\d{2}:\d{2}:\d{2}:\d{2})'
# #     time_pattern = re.compile(r'\b\d{2}\:\d{2}\:\d{2}\b')
# #     def time_to_seconds(time_str):
# #         hours, minutes, seconds = map(int, time_str.split(':'))
# #         total_seconds = hours * 3600 + minutes * 60 + seconds
# #         return total_seconds
# #     for frame_count in range(100):
# #         # Read the frame
# #         ret, frame = cap.read()
# #         x, y, w, h = 0, 0, 850, 50
# #         timestamp_crop = frame[y:y+h, x:x+w]
# #         # Perform OCR on the frame
# #         results = reader.readtext(timestamp_crop, detail = 0)
        
# #         """
# #         # Print OCR results
# #         # Extract time-like strings from the result
# #         text = [time for time in result if re.match(time_pattern, time)]

# #         # Print extracted times
# #         print("Extracted times:", text)
# #         """
# #         if any(results):
            
# #             text = results[3]
# #             if "AM" in text or "PM" in text:
# #                 text = text.replace("AM", "").replace("PM", "")
# #              # Check if the desired time pattern is found
# #             if "." in text :
# #                 text = text.replace(".", ":")
# #             if time_pattern.search(text):
# #                 print("Desired time pattern found. Stopping processing.")
# #                 # Set the flag to stop processing
# #                 #stop_processing = True
# #                 break
        
# #     total_seconds = time_to_seconds(text)
# #     time1= text.split(":")
# #     hours = time1[0]
# #     minutes = time1[1]
# #     seconds = time1[2]
# #     print(f'Total seconds: {total_seconds}')
# #     # Release the video capture object
# #     cap.release()
    

# #     return render(request, 'videopage.html', {'i': video_url,'e':csv_url,'time':int(total_seconds),'hr':int(hours),'min':int(minutes),'sec':int(seconds),'duration':int(video_duration_seconds),})

# # def crop(request):

# #     idtoken = request.session['uid']
# #     a = authe.get_account_info(idtoken)
# #     a = a['users']
# #     a = a[0]
# #     a = a['localId']
# #     video_url = database.child('users').child(a).child('reports').child('videourls').child('url').get().val()

# #     return render(request,'crop.html', {'i': video_url,})
# # def crop_video(request):
# #     if request.method == 'POST':
# #         try:
# #             start_time_str = request.POST.get('start_time')
# #             end_time_str = request.POST.get('end_time')

# #             # Convert start and end times from HH:MM:SS to seconds
# #             start_time = sum(x * int(t) for x, t in zip([3600, 60, 1], start_time_str.split(':')))
# #             end_time = sum(x * int(t) for x, t in zip([3600, 60, 1], end_time_str.split(':')))

# #             if start_time >= end_time:
# #                 return HttpResponse("Invalid time range", status=400)

# #             input_video_path = "Trial with 5MP camera (1).mp4"  # Replace with your input video path
# #             output_video_path = "output_cropped_video.mp4"

# #             ffmpeg_extract_subclip(input_video_path, start_time, end_time, targetname=output_video_path)

# #             with open(output_video_path, 'rb') as video_file:
# #                 response = HttpResponse(video_file.read(), content_type='video/mp4')
# #                 response['Content-Disposition'] = 'attachment; filename="cropped_video.mp4"'
# #                 return response

# #         except Exception as e:
# #             return HttpResponse(str(e), status=500)
# #     else:
# #         return HttpResponse("Invalid request method", status=405)
# def extract_timestamp(frame, x=0, y=0, w=1000, h=100):
#     try:
#         timestamp_crop = frame[y:y+h, x:x+w]
#         timestamp_grey = cv2.cvtColor(timestamp_crop, cv2.COLOR_BGR2GRAY)
#         _, timestamp_thresh = cv2.threshold(timestamp_grey, 127, 255, cv2.THRESH_BINARY)
#         candidate_str = pytesseract.image_to_string(timestamp_thresh, config='--psm 6')
        
#         regex_str = r'Date:\s(\d{4}-\d{2}-\d{2})\sTime:\s(\d{2}:\d{2}:\d{2}\s(?:AM|PM))\sFrame:\s(\d{2}:\d{2}:\d{2}:\d{2})'
#         match = re.search(regex_str, candidate_str)
        
#         if match:
#             date_str, time_str, frame_str = match.groups()
#             return date_str, time_str, frame_str
#     except Exception as e:
#         print(f"Error extracting timestamp: {e}")
#     return None, None, None

# def get_video_timestamp(video_path, frame_position):
#     cap = cv2.VideoCapture(video_path)
#     cap.set(cv2.CAP_PROP_POS_FRAMES, frame_position)
#     ret, frame = cap.read()
#     cv2.imwrite("frame_2.jpg",frame)
#     cap.release()
#     if ret:
#         return extract_timestamp(frame)
#     return None, None, None

# def get_initial_time(video_path):
#     date_str, time_str, _ = get_video_timestamp(video_path, 0)
#     return time_str if time_str else "00:00:00 AM"

# def get_video_end_time(video_path):
#     cap = cv2.VideoCapture(video_path)
#     frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#     date_str, time_str, _ = get_video_timestamp(video_path, frame_count - 1)
#     cap.release()
#     return time_str if time_str else "00:00:00 AM"

# def parse_time(time_str):
#     try:
#         return datetime.strptime(time_str, '%I:%M:%S %p')
#     except ValueError:
#         pass
    
#     try:
#         return datetime.strptime(time_str, '%H:%M:%S')
#     except ValueError:
#         return None

# def time_to_seconds(time_str):
#     dt = parse_time(time_str)
#     if dt:
#         return dt.hour * 3600 + dt.minute * 60 + dt.second
#     return 0

# def seconds_to_time(seconds):
#     return str(timedelta(seconds=seconds))

# def download_video(video_path):
#     response = requests.get(video_path, stream=True)
#     if response.status_code != 200:
#         raise Exception("Failed to download video file")
    
#     input_video_path = os.path.normpath(os.path.join(os.getcwd(), 'downloaded_video.mp4'))
#     with open(input_video_path, 'wb') as f:
#         for chunk in response.iter_content(chunk_size=1024):
#             f.write(chunk)
    
#     return input_video_path

# def crop_video_req(input_video_path, start_time_sec, end_time_sec):
    
#     output_video_path = os.path.normpath(os.path.join(os.getcwd(), 'output_cropped_video.mp4'))
    
#     ffmpeg_cmd = [
#         ffmpeg_path,
#         '-y',
#         '-i', input_video_path,
#         '-ss', str(start_time_sec),
#         '-to', str(end_time_sec),
#         '-c:v', 'libx264',
#         '-crf', str(VIDEO_QUALITY),
#         '-preset', VIDEO_PRESET,
#         '-c:a', 'aac',
#         '-strict', 'experimental',
#         output_video_path
#     ]
    
#     try:
#         subprocess.run(ffmpeg_cmd, check=True)
#     except subprocess.CalledProcessError as e:
#         raise Exception(f"FFmpeg error: {str(e)}")
    
#     if not os.path.exists(output_video_path):
#         raise Exception("Failed to crop video")
    
#     return output_video_path

# def crop_video(request):
#     idtoken = request.session['uid']
#     a = authe.get_account_info(idtoken)
#     a = a['users']
#     a = a[0]
#     a = a['localId']
#     video_url = database.child('users').child(a).child('reports').child('videourls').child('url').get().val()
#     video_path=video_url
#     initial_time_str=get_initial_time(video_path)
#     input_video_path=download_video(video_path)

#     if request.method != 'POST':
#         return HttpResponse("Invalid request method", status=405)
    
#     try:
#         data = json.loads(request.body)
#         start_time_str = data.get("start_time")
#         end_time_str = data.get("end_time")
#         print(f"Hi its start time-->{start_time_str}")
#         print(f"Hi its end time-->{end_time_str}")
        
#         start_time_sec = time_to_seconds(start_time_str)
#         end_time_sec = time_to_seconds(end_time_str)
#         initial_time_sec = time_to_seconds(initial_time_str)
        
#         start_time_sec -= initial_time_sec
#         end_time_sec -= initial_time_sec
#         print(f"Hi its start time-->{start_time_sec}")
#         print(f"Hi its End time-->{end_time_sec}")
        
        
#         if start_time_sec >= end_time_sec:
#             return HttpResponse("Invalid start or end time", status=400)
        
#         cropped_video_path = crop_video_req(input_video_path, start_time_sec, end_time_sec)
        
#         return serve_cropped_video(cropped_video_path)
    
#     except Exception as e:
#         return HttpResponse(f"Error: {str(e)}", status=500)

# def serve_cropped_video(output_video_path):
#     with open(output_video_path, 'rb') as video_file:
#         response = HttpResponse(video_file.read(), content_type='video/mp4')
#         response['Content-Disposition'] = 'attachment; filename="cropped_video.mp4"'
#         return response