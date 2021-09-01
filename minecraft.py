import keyboard
import socket

class game :
    
    mainServers = []
    def animations() :
        
        def forward() :
            
            
            
        def backward() :
            
            
            
        def left() :
            
            
            
        def right() :
            
            
            
        def shift() :
            
            
            
        def jump() :
            
            
            
        def punch() :
            
            
            
        def useTool(toolId, usedButton) :
            
            self.usedButton = usedButton
            if toolId == 1 :
                
                """ if a sword is used, the sword anim is started """
                if self.usedButton == 1 :
                    
                    """ if the left button of a mouse is used, the attack anim is used """
                    
                elif self.usedButton == 2 :
                    
                    """ if the right button of a mouse is used, the defense anim is used """
                    
                else :
                    
                    print ("Error during the usage of the sword !")
                    
            if toolId == 2 :
                
                """ if a pickaxe is used, the pickaxe anim is started """
                if self.usedButton == 1 :
                    
                    
                    
                elif self.usedButton == 2 :
                    
                    
                    
                else :
                    
                    print ("Error during the usage of the pickaxe !")
                    
            if toolId == 3 :
                
                """ if an axe is used, the axe anim is started """
                
            if toolId == 4 :
                
                """ if a shovel is used, the shovel anim is started """
                
            if toolId == 5 :
                
                
                
    def blocks() :
        
        dirtBlock = {"name": "dirt", "id": 0, "images": {"topImage": {"img": "", "size": {"x": "64", "y": "64"}}, "bottomImage": {"img": "", "size": {"x": "64", "y": "64"}}, "forwardImage": {"img": "", "size": {"x": "64", "y": "64"}}, "backImage": {"img": "", "size": {"x": "64", "y": "64"}}, "leftImage": {"img": "", "size": {"x": "64", "y": "64"}}, "rightImage": {"img": "", "size": {"x": "64", "y": "64"}}}}
        cobbleBlock = {"name": "cobble", "id": "", "images": {"topImage": {"img": "", "size": {"x": "64", "y": "64"}}, "bottomImage": {"img": "", "size": {"x": "64", "y": "64"}}, "forwardImage": {"img": "", "size": {"x": "64", "y": "64"}}, "backImage": {"img": "", "size": {"x": "64", "y": "64"}}, "leftImage": {"img": "", "size": {"x": "64", "y": "64"}}, "rightImage": {"img": "", "size": {"x": "64", "y": "64"}}}}
        cobblestoneBlock = {"name": "cobble stone", "id": "", "images": {"topImage": {"img": "", "size": {"x": "64", "y": "64"}}, "bottomImage": {"img": "", "size": {"x": "64", "y": "64"}}, "forwardImage": {"img": "", "size": {"x": "64", "y": "64"}}, "backImage": {"img": "", "size": {"x": "64", "y": "64"}}, "leftImage": {"img": "", "size": {"x": "64", "y": "64"}}, "rightImage": {"img": "", "size": {"x": "64", "y": "64"}}}}
        lightBlock = {"name": "light", "id": "", "images": {"topImage": {"img": "", "size": {"x": "64", "y": "64"}}, "bottomImage": {"img": "", "size": {"x": "64", "y": "64"}}, "forwardImage": {"img": "", "size": {"x": "64", "y": "64"}}, "backImage": {"img": "", "size": {"x": "64", "y": "64"}}, "leftImage": {"img": "", "size": {"x": "64", "y": "64"}}, "rightImage": {"img": "", "size": {"x": "64", "y": "64"}}}}
        
    def tools() :
        
        swords = { "vanillaSwords": { 1: { "name": "Wood sword", "images": {  }, "model": "" }, 2: { "name": "Cobble sword", "images": {  }, "model": "" }, 3: { "name": "Iron sword", "images": {  }, "model": "" }, 4: { "name": "Gold sword", "images": {  }, "model": "" }, 5: { "name": "Diamond sword", "images": {  }, "model": "" }, 6: { "name": "Emerald sword", "images": {  }, "model": "" }, 7: { "name": "Netherite sword", "images": {  }, "model": "" }, 8: { "name": "Obsidian sword", "images": {  }, "model": "" } }, "moddedSwords": {  } }
        pickaxes = { "vanillaPickaxes": { 1: { "name": "Wood pickaxe", "images": "", "model": "" }, 2: { "name": "Cobble pickaxe", "images": "", "model": "" }, 3: { "name": "Iron pickaxe", "images": "", "model": "" }, 4: {  }, 5: {  }, 6: {  }, 7: {  }, 8: {  } } }
        axes = {  }
        shovels = {  }
        hoes = {  }
        
    def gui() :
        
        
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
            playerDatas.playerCameraXCord = playerXCord -0.5
            
class internet :
    
    def internetClient() :
        
        icsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        icsocket.connect(mainServers, 15000)
        while True :
            
            icsocket.send()
