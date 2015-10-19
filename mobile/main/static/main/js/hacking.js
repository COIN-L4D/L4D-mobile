(function(){

  var self = {
    games: {},
    mini_game_block: undefined,
    current_game: undefined,
    end_form: undefined,
    result_input: undefined,
  }

  function startGame(name){
    self.games[name].easyStart(self.mini_game_block, function(){
      self.result_input.value = "success"
      self.end_form.submit()
    })
  }

  function initialize(){

    self.mini_game_block = document.getElementById('mini-game-block')
    self.end_form = document.getElementById('end-form')
    self.result_input = document.getElementById('result-input')
    self.current_game = hacking_current_game

    function loadGame(name, obj){
      if (typeof obj === 'undefined'){
        console.error("Could not load the game named '"+ name +"'")
        return false
      }
      else {
        self.games[name] = obj
        return true
      }
    }

    function makeStartEasier(name, settings){
      self.games[name].easyStart = function(node, callback){
        settings.node = node
        settings.callback = callback
        return self.games[name].start(settings)
      }
    }

    // load and congifgure mgHack
    loadGame('Hack', mgHack)
    makeStartEasier('Hack', {
      alphabet: '01',
      size: 2,
    })


    startGame(self.current_game.name)
  }

  window.addEventListener('load', initialize)
})()
