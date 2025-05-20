import cv2
import numpy as np
import os

class GetVideo:
    
    PATH = os.path.abspath(os.getcwd())
    
    def __init__(self, video_name):
        
        self.video_name = f'\\' + video_name
        video_path = self.PATH + self.video_name
        
        try:
            self.video = cv2.VideoCapture(video_path)
        
        except Exception as e:
            print(f'ERROR IN <GETVIDEO.LOAD_VIDEO>: {e}')

        print(f'Video: {self.video} was succeful loaded.\nViedeo type == {type(self.video)}')
    
    def frame_reader(self):
        
        self.frames = []
        
        while self.video.isOpened():
            
            try:
                ret, frame = self.video.read()
                
            except Exception as e:
                print(f'ERROR IN <FRAMEREADER.READ_FRAME>: {e}')
            
            self.frames.append(frame)
                
            if not ret:
                break
        
        print(f'Was succeful write {len(self.frames)} frame from video')
        
        return self.frames
    
    def save_video_to_object(self):
        if self.video != None:
            print(f'Video was succeful writing to object, object type {type(self.video)}')
            return self.video
        else:
            print('ERROR IN <GETVIDEO.SAVE_VIDEO_TO_OBJECT>: EMPTY VIDEO OBJECT')

class SaveNewVideo:
    def __init__(
                self, 
                newvideoname:str, 
                videowriter_fourcc:str, 
                fps:int, 
                frames:list
                ):
        
        if (
            type(newvideoname) != str or 
            type(videowriter_fourcc) != str or 
            type(fps) != int or 
            type(frames) != list
            ):
            
                print('ERROR IN <SAVENEWVIDEO>: INCORRECT DATA TYPE SENT AS ARGUMENT')
            
        else:
            
            if len(videowriter_fourcc) != 4:
                
                print('ERROR IN <SAVENEWVIDEO>: VIDEOWRITER_FOURCC MUST CONTAIN 4 SYMBOLS')
            
            else:
                self.newvideoname = newvideoname
                self.videowriter_fourcc = videowriter_fourcc
                self.fps = fps
                self.frames = frames
            
                SaveNewVideo.save_new_video(self)
            
    def save_new_video(self):
        
        frame = self.frames[0]
        HIGHT,WIDTH = frame.shape[:2]
        
        out = cv2.VideoWriter(
            self.newvideoname,
            cv2.VideoWriter_fourcc(*self.videowriter_fourcc),
            self.fps,
            (WIDTH, HIGHT)
        )
        
        for frame in self.frames:
            out.write(frame)
            
class ShowVideo:
    def __init__(
                self, 
                frames:list, 
                window_name:str, 
                video: cv2.VideoCapture
                ):
        
        if (
            type(frames) != list or 
            type(window_name) != str or 
            type(video) != cv2.VideoCapture
            ):
            
            print('ERROR IN <SHOWVIDEO> INCORECT TYPE OF VARIABLES WAS GIVEN')
            
        else:
            
            self.frames = frames
            self.window_name = window_name
            self.video = video
            
            ShowVideo.show_video(self)
    
    def show_video(self):
        
        for frame in self.frames:
            if frame is not None:
                cv2.imshow(self.window_name, frame)
                
            else:
                print(f"ERROR: frame is Empty:\n{frame}")
                continue
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        self.video.release()
        cv2.destroyAllWindows()
        
        

        








                
               
        


