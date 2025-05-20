from ultralytics import YOLO
import os
import supervision as sv
import moduls_for_works_with_video as mv

class Tracking:
    
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
    
    model = YOLO("yolov8x.pt")
    box_annotator = sv.BoxAnnotator(thickness=2)
    
    def __init__(self, source_video:str):
        
        if type(source_video) != str:
            print(f"ERROR: INCORECT FORMAT VIDEO WAS GIVEN")
        else:
            self.souce_video = source_video
        
        self.frameBox = []
        
        for result in self.model.track(source= self.souce_video, show= False, stream=False):
            
            frame = result.orig_img
            detections = sv.Detections.from_ultralytics(result)
            
            if result.boxes.id is not None:
                
                detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)
            
            frame = self.box_annotator.annotate(
                scene = frame,
                detections = detections
            )
            
            self.frameBox.append(frame)
            print(f'Frame box size is {len(self.frameBox)} frame/es')
    
    def save_tracking_video(self):
        
        mv.SaveNewVideo(
                        newvideoname= 'trackin_mp4_with_zoom.mp4',
                        videowriter_fourcc= 'mp4v',
                        fps = 30,
                        frames= self.frameBox
                        )

"""
OMP: Hint This means that multiple copies of the OpenMP runtime have been linked into the program. 
That is dangerous, since it can degrade performance or cause incorrect results. 
The best thing to do is to ensure that only a single OpenMP runtime is linked into the process, 
e.g. by avoiding static linking of the OpenMP runtime in any library. 
As an unsafe, unsupported, undocumented workaround you can set the environment variable 
KMP_DUPLICATE_LIB_OK=TRUE to allow the program to continue to execute, 
but that may cause crashes or silently produce incorrect results. For more information, please see http://www.intel.com/software/products/support/.
"""                
                
            
    
 