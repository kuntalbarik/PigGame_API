# PigGame_API
All API are defined using flask, flask internally install PigGame from "pip install -i https://test.pypi.org/simple/ PigGameVersion-0.1.0"


API Details
----------------

class customGame:

    winScore=100 ###by default the winning score is set to 100. In case winning score need to change call API no- 13

  1)  def createGame(self,gameType):
        if gameType.lower()=='t':
            gameObject=tournament()
            return gameObject
        elif gameType.lower()=='c':
            gameObject=challenge()
            return gameObject
        else:
            return False

   2) def createPlayer(self,noOfPlayers):
        if noOfPlayers==1:
            humanPlayer=human()
            computerPlayer=computer()
            return humanPlayer,computerPlayer

        elif noOfPlayers==2:
            humanPlayer1=human()
            humanPlayer2=human()
            return humanPlayer1,humanPlayer2
        else:
            return False

   3) def createHumanPlayer(self):
        return human()

   4) def createComputerPlayer(self):
        return computer()

   5) def setHumanPlayer(self,humanObject,name:str,tempScore=0,finalScore=0):
        humanObject.Name=name
        humanObject.TempScore=tempScore
        humanObject.FinalScore=finalScore

   6) def setComputerPlayer(self,computerObject,tempScore=0,finalScore=0):
        computerObject.Name="COMPUTER"
        computerObject.TempScore=tempScore
        computerObject.FinalScore=finalScore

   7) def humanPlayOption(self,player):
        playerChoice=" ".join(input(player.Name+' '+data["roll or hold"]).split())
        if (playerChoice.lower()=='r'):
            return 'r'
        else:
            return 'h'

   8) def Roll(self,player):
        return player.role()

   9) def Hold(self,player):
        return player.hold()

   10) def Score(self,player):
        return player.TempScore

   11) def CheckWinner(self,player1,player2):
        if (player1.FinalScore >=winScore):
            return player1.Name

        elif (player2.FinalScore >= winScore):
            return player2.Name

        else:
            return True

   12) def FinalScore(self,playerObject):
        __fs=finalScore()
        playerObject.FinalScore=__fs.calculateScore(playerObject.FinalScore,playerObject.TempScore)
        return playerObject.FinalScore

   13) def GameConfiguration(self,WinningScore):
        winScore=WinningScore
