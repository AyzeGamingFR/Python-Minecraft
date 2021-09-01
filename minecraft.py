import keyboard

class player :
    
    def playerDatas() :
        
        playerXCord = 2
        playerYCord = 0
        playerZCord = 0
        playerCameraXCord = 2
        playerCameraYCord = 0
        playerCameraZCord = 0
        def playerSettings() :
            
            playerForwardButton = "z" AND "Z"
            playerLeftButton = "q" AND "Q"
            playerRightButton = "d" AND "D"
            playerBackButton = "s" AND "S"
            playerShiftButton = ""
            
    def move(key) :
        
        if key == playerDatas.playerSettings.playerForwardButton :
            
            
            
        if key == playerDatas.playerSettings.playerLeftButton :
            
            
            
        if key == playerDatas.playerSettings.playerRightButton :
            
            
            
        if key == playerDatas.playerSettings.playerBackButton :
            
            
            
        if key == playerDatas.playerSettings.playerShiftButton :
            
            game.animations.shift
            playerCameraXCord = playerXCord -0.5
            
class game :
    
    def animations() :
        
        def forward() :
            
            
            
        def backward() :
            
            
            
        def left() :
            
            
            
        def right() :
            
            
            
        def shift() :
            
            
            
        def jump() :
            
            
            
        def punch() :
            
            
            
        def useTool() :
            
            
            
    def blocks() :
        
        dirtBlock = {"name": "dirt", "id": 0, "images": {"topImage": {"img": "", "size": {"x": "64", "y": "64"}}, "bottomImage": {"img": "", "size": {"x": "64", "y": "64"}}, "forwardImage": {"img": "", "size": {"x": "64", "y": "64"}}, "backImage": {"img": "", "size": {"x": "64", "y": "64"}}, "leftImage": {"img": "", "size": {"x": "64", "y": "64"}}, "rightImage": {"img": "", "size": {"x": "64", "y": "64"}}}}
        cobbleBlock = {"name": "cobble", "id": "", "images": {"topImage": {"img": "", "size": {"x": "64", "y": "64"}}, "bottomImage": {"img": "", "size": {"x": "64", "y": "64"}}, "forwardImage": {"img": "", "size": {"x": "64", "y": "64"}}, "backImage": {"img": "", "size": {"x": "64", "y": "64"}}, "leftImage": {"img": "", "size": {"x": "64", "y": "64"}}, "rightImage": {"img": "", "size": {"x": "64", "y": "64"}}}}
        cobblestoneBlock = {"name": "cobble stone", "id": "", "images": {"topImage": {"img": "", "size": {"x": "64", "y": "64"}}, "bottomImage": {"img": "", "size": {"x": "64", "y": "64"}}, "forwardImage": {"img": "", "size": {"x": "64", "y": "64"}}, "backImage": {"img": "", "size": {"x": "64", "y": "64"}}, "leftImage": {"img": "", "size": {"x": "64", "y": "64"}}, "rightImage": {"img": "", "size": {"x": "64", "y": "64"}}}}
        lightBlock = {"name": "light", "id": "", "images": {"topImage": {"img": "", "size": {"x": "64", "y": "64"}}, "bottomImage": {"img": "", "size": {"x": "64", "y": "64"}}, "forwardImage": {"img": "", "size": {"x": "64", "y": "64"}}, "backImage": {"img": "", "size": {"x": "64", "y": "64"}}, "leftImage": {"img": "", "size": {"x": "64", "y": "64"}}, "rightImage": {"img": "", "size": {"x": "64", "y": "64"}}}}
