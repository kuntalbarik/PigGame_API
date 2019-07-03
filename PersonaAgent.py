from flask import Flask,request
import jsonpickle
import PigGame.PROVIDER.mainClass as P
app = Flask(__name__)

@app.route('/Game/CreateGame/<gametype>',methods=['GET'])
def createGame(gametype):
    customGame = P.customGame()
    game=customGame.createGame(gametype)
    myGame=jsonpickle.encode(game)
    return myGame

@app.route('/Game/CreatePlayer/<playerNumber>',methods=['GET'])
def createPlayer(playerNumber):
    customGame=P.customGame()
    p1,p2=customGame.createPlayer(playerNumber)
    return p1,p2

@app.route('/Game/SetHumanPlayer/<humanObject>/<name>/<tempScore>/<finalScore>',methods=['POST'])
def setHumanPlayer(humanObject,name,tempScore):
    customeGame=P.customGame()
    customeGame.setHumanPlayer(humanObject,name,tempScore,finalScore)

@app.route('/Game/SetComputerPlayer/<computerObject>/<tempScore>/<finalScore>',methods=['POST'])
def setComputerPlayer(computerObject,tempScore,finalScore):
    customeGame=P.customGame()
    customeGame.setComputerPlayer(computerObject,tempScore,finalScore)

@app.route('/Game/PlayerAction/Roll/<PlayerObject>',methods=['GET'])
def roll(PlayerObject):
    customGame=P.customGame()
    score=customGame.Roll(PlayerObject)
    return score

@app.route('/Game/PlayerAction/Hold/<PlayerObject>',methods=['GET'])
def hold(PlayerObject):
    customGame = P.customGame()
    score = customGame.Roll(PlayerObject)
    return score

@app.route('/Game/Score/<PlayerObject>',methods=['GET'])
def score(PlayerObject):
    customGame = P.customGame()
    score = customGame.Score(PlayerObject)
    return score

@app.route('/Game/CheckWinner/<playerObject1>/<playerObject2>',methods=['GET'])
def checkWinner(playerObject1,playerObject2):
    customGame=P.customGame()
    winner=customGame.CheckWinner(playerObject1,playerObject2)
    return winner

@app.route('/Game/FinalScore/<palyerObject>',methods=['POST'])
def finalScore(palyerObject):
    customGame=P.customGame()
    finalScore=customGame.finalScore(palyerObject)
    return finalScore
#
# @app.route('/Game/StartGame',methods=['GET'])
# def checkWinner(playerObject1,playerObject2):
#     customGame=P.customGame()
#     winner=customGame.CheckWinner(playerObject1,playerObject2)
#     return winner
#
# @app.route('/stop game',methods=['GET'])
# def checkWinner(playerObject1,playerObject2):
#     customGame=P.customGame()
#     winner=customGame.CheckWinner(playerObject1,playerObject2)
#     return winner

@app.route('/Game/GameConfig/<maxScore>',methods=['POST'])
def gameConfiguration(maxScore):
    customGame=P.customGame()
    customGame.GameConfiguration(maxScore)

@app.route('/Game/HumanPlayOption/<playerObject>',methods=['GET'])
def HumanPlayOption(playerObject):
    customGame=P.customGame()
    playersChoiche=customGame.humanPlayOption(playerObject)
    return playersChoiche

if __name__=='__main__':
    app.run()
