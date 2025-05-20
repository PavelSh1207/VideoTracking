import moduls_for_works_with_video as mv
import numpy as np
import cv2

class Zoom:
    
    video_init =  mv.GetVideo('input_video.mp4')
    frames = video_init.frame_reader()
    video = video_init.save_video_to_object()
    
    frames[len(frames) -1] = np.zeros(frames[0].shape)
    print(f'The last NoneType frame np.zeros was succesfully rewriting frame np.zeros type: {frames[len(frames) -1]}\n{type(frames[len(frames) - 1])}')
    
    def __init__(self):
        
        self.frames_zoom = []
        self.SCALE = np.float16(1.8)
        Zoom.zoom_video(self)
            
    def zoom_video(self):
        
        for frame in self.frames:
            
            print('loop is working')
        
            HEIGH, WIDTH = frame.shape[:2]
            
            frame_zoomed = cv2.resize(
                frame,
                (np.int16(WIDTH * self.SCALE), np.int16(HEIGH * self.SCALE))
            )
            
            CENTER_X, CENTER_Y   = frame_zoomed.shape[1]//2, frame_zoomed.shape[0]//2
            crop_x1 = CENTER_X - WIDTH//2
            crop_x2 = CENTER_X + WIDTH//2
            crop_y1 = CENTER_Y - HEIGH//2
            crop_y2 = CENTER_Y + HEIGH//2
            
            frame_zoomed = frame_zoomed[crop_y1:crop_y2, crop_x1:crop_x2]
            print(f'frame zoom was created type = {type(frame_zoomed)}, len = {len(frame_zoomed)}')
            
            self.frames_zoom.append(frame_zoomed)
        
        print(f'zoom frames was created len = {len(self.frames_zoom)}, type = {type(self.frames_zoom)}')

    def save_zoom(self):
        
        mv.SaveNewVideo(
            newvideoname= 'zoomed_video.mp4',
            videowriter_fourcc='mp4v',
            fps = 30,
            frames= Zoom().frames_zoom
        )

if __name__ == "__main___":
    
    zoom_video_object = Zoom()
    zoom_video_object.zoom_video()
    
    zoom_show = mv.ShowVideo(
        frames= zoom_video_object.frames_zoom,
        window_name= "Zoom",
        video = zoom_video_object.video
        )
    zoom_show.show_video()
        

    


            

            
        
        
     
        
    
    