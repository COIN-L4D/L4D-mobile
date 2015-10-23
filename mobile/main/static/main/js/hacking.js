(function(){

  var self = {
    game: undefined,
    mini_game_block: undefined,
    current_game: undefined,
    end_form: undefined,
    result_input: undefined,
  }

  function startGame(){
    self.game.easyStart(self.mini_game_block, function(){
      self.result_input.value = "success"
      self.end_form.submit()
    })
  }

  function initialize(){

    self.mini_game_block = document.getElementById('mini-game-block')
    self.end_form = document.getElementById('end-form')
    self.result_input = document.getElementById('result-input')
    self.current_game = hacking_current_game

    function loadGame(obj){
      if (typeof obj === 'undefined'){
        console.error("Could not load the game named '"+ self.current_game.name +"'")
        return false
      }
      else {
        self.game = obj
        return true
      }
    }

    function makeStartEasier(settings){
      self.game.easyStart = function(node, callback){
        settings.node = node
        settings.callback = callback
        return self.game.start(settings)
      }
    }


    if (self.current_game.name == 'Hack'){
      // load and congifgure mgHack
      loadGame(mgHack)
      makeStartEasier({
        alphabet: '0123456789',
        size: 4,
      })
    }
    else if (self.current_game.name == 'Fire'){
      loadGame(fire)
      var w = window.innerWidth
      || document.documentElement.clientWidth
      || document.body.clientWidth;

      var h = window.innerHeight
      || document.documentElement.clientHeight
      || document.body.clientHeight;
      makeStartEasier({
        canvasWidth: w,
        canvasHeight: h,
        mapWidth: 20,
        mapHeight: 15,
        scoreToWin: 10,
        maxFiresNumber: 10,
        maxWatersNumber: 3,
        fireSpawnProba: 0.01,
        waterSpawnProba: 0.05,
        startFiresNumber: 10
      })
    }

    startGame()
  }

  window.addEventListener('load', initialize)
})()
