import install_lib as lib

libs = lib.Libs()
libs.install()
libs.check()

import moduls_for_works_with_video as mv
import tracking_yolo_v8 as tracking
import MovingZoom as mz

class MovingZoomMain:
    
    def __init__(self, video_name:str): #original video
        
        if type(video_name) != str:
            print("ERROR: INCORECT VIDEO NAME FORMAT WAS GIVEN")
        else:
            self.video_name = video_name    
    
    def realise(self):
        
        moving_zoom_realese = mz.MovingZoomRealese(self.video_name)
        frame_moving_zoom = moving_zoom_realese.renderMovingZoom()
        
        mv.ShowVideo(
            frames= frame_moving_zoom,
            window_name= "new",
            video = moving_zoom_realese.orig_video
        )
        
        mv.SaveNewVideo(
            newvideoname= "movingZoomN.mp4",
            videowriter_fourcc= "mp4v",
            fps = 60,
            frames= frame_moving_zoom
        )
        
class YoloTracking:
    
    def __init__(self, video_name:str): #zoomed moved video
        
        if type(video_name) != str:
            print("ERROR: INCORECT VIDEO NAME FORMAT WAS GIVEN")
        else:
            self.video_name = video_name
            
    def realise(self):
        tracking_video = tracking.Tracking(self.video_name)
        tracking_video.save_tracking_video()
        
        
        

            
    

    

    
    



