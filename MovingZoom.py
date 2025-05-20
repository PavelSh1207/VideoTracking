import moduls_for_works_with_video as mv
import numpy as np
import cv2
import os

#main part
class VidoInit:
    def __init__(self, video_name:str):
        
        if type(video_name) != str:
            print("ERROR: INCORECT VIDEO NAME FORMAT WAS GIVEN")
        else:
            self.video_name = video_name
        
        self.init_video = mv.GetVideo(self.video_name)
        self.orig_video = self.init_video.save_video_to_object()
        self.orig_frames = self.init_video.frame_reader()
        
    def showOrigVideo(self):
        mv.ShowVideo(
            frames= self.orig_frames,
            window_name= "Original Video (that video whose to take to <VideoInit> Class",
            video = self.orig_video
        )

class MovingZoomRealese:
    
    def __init__(self, video_name):
        
        if type(video_name) != str:
            print("ERROR: INCORECT VIDEO NAME FORMAT WAS GIVEN")
        else:
            self.video_name = video_name        
        
        #init satrt field of parameters
        self.original_video_init = VidoInit(self.video_name)
        self.orig_video = self.original_video_init.orig_video
        self.orig_frames = self.original_video_init.orig_frames
        self.frames_full = self.orig_frames
        
    
        #initialisation satart constant
        self.SCALE  = np.float16(1.8)
        self.ROTATION_SPEED = 1
        
        #coeffict aix change for 10 degree camera rotation is 0.05
        #sugest rotation speed for test is 10
        self.COEFFICENT = np.float16(0.05)
    
    def inform(self):
        
        print(f"\n{"="*10} FRAMES INFORMATION {"="*10}\n")
        print(f"FRAMES WAS TAKEN.\nFRAMES TOOK LENGT IS: {len(self.orig_frames)}\n")
        
        
        
        print(f"INFORMATION ABOUT <orig_frames>:\nTYPE {type(self.orig_frames)}\nTYPE FIRST FRAME {type(self.orig_frames[0])}\n")
        
        HEIGH, WIDTH = np.int16(self.orig_frames[0].shape[:2])
        print(f"h = {HEIGH}\nw = {WIDTH}\n")
    
    def generate_x_coordinates(self):
        coordinates = []
        cord_x = []
        frames = self.orig_frames
        frames.pop()
        iteration = 0
        
        
        for frame in frames:
            
            HEIGH, WIDTH = frame.shape[:2]
            
            frame_zoomed = cv2.resize(
                frame,
                (np.int16(WIDTH * self.SCALE), np.int16(HEIGH * self.SCALE))
            )
            
            CENTER_X = frame_zoomed.shape[1]//2
            coordinates.append(CENTER_X)           

        START_X = np.int16(CENTER_X - (CENTER_X * self.COEFFICENT))
        END_X = np.int16(CENTER_X + (CENTER_X * self.COEFFICENT))
        
        coordinates_coeficent = START_X
        
        while iteration <= len(coordinates) - 1:
            if coordinates_coeficent <= END_X:
                for cord in range(START_X, END_X+self.ROTATION_SPEED + 1, self.ROTATION_SPEED):
                    if cord < END_X or cord == END_X:
                        cord_x.append(cord)
                    else:
                        print("ELSE WORKED")
                        coordinates_coeficent = cord
                        break
            else:
                for cord in range(END_X, START_X-self.ROTATION_SPEED + 1, -self.ROTATION_SPEED):
                    if cord >= START_X:
                        cord_x.append(cord)
                    else:
                        coordinates_coeficent = cord
                        break
                    
            iteration += 1
               
        return cord_x
    
    def renderMovingZoom(self):
        
        frames_zoom = []
        cord_x = self.generate_x_coordinates()
        i = 0
        """
        print(cord_x[0:250])
        
        print(len(self.frames_full))
        """
        for frame in self.frames_full:
            
            crop_x = cord_x[i]
            i += 1
            
            HEIGH, WIDTH = frame.shape[:2]
            
            frame_zoomed = cv2.resize(
                frame,
                (np.int16(WIDTH * self.SCALE), np.int16(HEIGH * self.SCALE))
            )
            
            
            CENTER_X, CENTER_Y   = crop_x, frame_zoomed.shape[0]//2
            crop_x1 = CENTER_X - WIDTH//2
            crop_x2 = CENTER_X + WIDTH//2
            crop_y1 = CENTER_Y - HEIGH//2
            crop_y2 = CENTER_Y + HEIGH//2
            
            print(crop_x, crop_x1, crop_x2, i)
            
            frame_zoomed = frame_zoomed[crop_y1:crop_y2, crop_x1:crop_x2]
            #print(f'frame zoom was created type = {type(frame_zoomed)}, len = {len(frame_zoomed)}')
            
            frames_zoom.append(frame_zoomed)
            
        return frames_zoom              
                
#test part 
class TestVideoInit:
    
    def __init__(self):
        
        try:
            test_VideoInit = VidoInit()
            test_VideoInit.showOrigVideo()
            print(test_VideoInit.orig_video, test_VideoInit.orig_frames)
            
        except Exception as e:
            print(f"ERROR IN VIDEOINIT: {e}")
            
        else:
            print("TEST PASSED SUCCEFULL")

#realese part  
if __name__ == "__main__":
    
    """
    #test <VideoInit> class
    test_VideoInit = TestVideoInit()
    """
    moving_zoom_realese = MovingZoomRealese("input_video.mp4")
    frame_moving_zoom = moving_zoom_realese.renderMovingZoom()
    
    mv.ShowVideo(
        frames= frame_moving_zoom,
        window_name= "new",
        video = moving_zoom_realese.orig_video
    )
    
    mv.SaveNewVideo(
        newvideoname= "movingZoom.mp4",
        videowriter_fourcc= "mp4v",
        fps = 60,
        frames= frame_moving_zoom
    )
    
    
    
    
   
    