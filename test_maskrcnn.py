import maskrcnn as modellib



class_names = ['BG', 'roadmark', 'car']                            
while True:
    val=input('please input 1 for training,\
                2 for predicting image,\
                3 for predicting video,\
                4 for exit:')
    if val=="1":
        #---train---
        model = modellib.MaskRCNN(
                    mode="training",#mode
                    class_names=class_names)#class names
        modellib.train(
                    model,#contructed model
                    "./datasets/road",#path of dataset
                    35,#epoch
                    0.001)#learning rate
    elif val=="2":
        #---predict image---
        model = modellib.MaskRCNN(
                    mode="inference",#mode
                    class_names=class_names)#class names
        modellib.detect_and_show(
                    model,#contructed model
                    image_path="./road.jpg")#input image
    elif val=="3":
         #---predict video---
        model = modellib.MaskRCNN(
                    mode="inference",#mode
                    class_names=class_names)#class names
        modellib.showvideo(
                    model,#contructed model
                    'road.mp4')#input video
    elif val=="4":
        exit()#exit
    else:
        print("invalid command")#invalid command
               









   