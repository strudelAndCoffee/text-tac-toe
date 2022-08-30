grid = [
  ['.', '.', '.'],
  ['.', '.', '.'],
  ['.', '.', '.']
]
gridVals = {
  'TL': 0,
  'TC': 0,
  'TR': 0,
  'ML': 0,
  'MC': 0,
  'MR': 0,
  'BL': 0,
  'BC': 0,
  'BR': 0
}

class Moves:
  def __init__(self, sym):
    self.sym = sym
    self.rowMove = 'Player ' + sym + ': pick a row__ '
    self.colMove = 'Player ' + sym + ': pick a column__ '

playerX = Moves('X')
playerO = Moves('O')

spots = {
  'X': [],
  'O': []
}
togglePlayer = True
gameOn = True
gameResult = ''

def print_grid():
  print(grid[0][0], grid[0][1], grid[0][2])
  print(grid[1][0], grid[1][1], grid[1][2])
  print(grid[2][0], grid[2][1], grid[2][2])

def player_move_prompt(player):

  rowPrompt = player.rowMove
  colPrompt = player.colMove
  sym = player.sym

  rowMove = input(rowPrompt)

  if rowMove == '1':
    colMove = input(colPrompt)

    if colMove == '1' and grid[0][0] == '.':
      grid[0][0] = sym
      gridVals['TL'] = 1
      spots[sym].append('TL')
    elif colMove == '2' and grid[0][1] == '.':
      grid[0][1] = sym
      gridVals['TC'] = 1
      spots[sym].append('TC')
    elif colMove == '3' and grid[0][2] == '.':
      grid[0][2] = sym
      gridVals['TR'] = 1
      spots[sym].append('TR')
    else:
      print("Invalid answer")
      player_move_prompt(player)

  elif rowMove == '2':
    colMove = input("Player X: pick a column__ ")

    if colMove == '1' and grid[1][0] == '.':
      grid[1][0] = sym
      gridVals['ML'] = 1
      spots[sym].append('ML')
    elif colMove == '2' and grid[1][1] == '.':
      grid[1][1] = sym
      gridVals['MC'] = 1
      spots[sym].append('MC')
    elif colMove == '3' and grid[1][2] == '.':
      grid[1][2] = sym
      gridVals['MR'] = 1
      spots[sym].append('MR')
    else:
      print("Invalid answer")
      player_move_prompt(player)

  elif rowMove == '3':
    colMove = input("Player X: pick a column__ ")
    
    if colMove == '1' and grid[2][0] == '.':
      grid[2][0] = sym
      gridVals['BL'] = 1
      spots[sym].append('BL')
    elif colMove == '2' and grid[2][1] == '.':
      grid[2][1] = sym
      gridVals['BC'] = 1
      spots[sym].append('BC')
    elif colMove == '3' and grid[2][2] == '.':
      grid[2][2] = sym
      gridVals['BR'] = 1
      spots[sym].append('BR')
    else:
      print("Invalid answer")
      player_move_prompt(player)

  else:
      print("Invalid answer")
      player_move_prompt(player)

def check_spots(player):
  allSpots = {
    'TL': 0,
    'TC': 0,
    'TR': 0,
    'ML': 0,
    'MC': 0,
    'MR': 0,
    'BL': 0,
    'BC': 0,
    'BR': 0
  }
  sym = player.sym
  playerSpots = spots[sym]

  for spot in playerSpots:
    if spot in allSpots:
      allSpots[spot] = 1

  topRow = allSpots['TL'] == 1 and allSpots['TC'] == 1 and allSpots['TR'] == 1
  midRow = allSpots['ML'] == 1 and allSpots['MC'] == 1 and allSpots['MR'] == 1
  btmRow = allSpots['BL'] == 1 and allSpots['BC'] == 1 and allSpots['BR'] == 1
  lftCol = allSpots['TL'] == 1 and allSpots['ML'] == 1 and allSpots['BL'] == 1
  cntCol = allSpots['TC'] == 1 and allSpots['MC'] == 1 and allSpots['BC'] == 1
  rgtCol = allSpots['TR'] == 1 and allSpots['MR'] == 1 and allSpots['BR'] == 1
  lftDgn = allSpots['TL'] == 1 and allSpots['MC'] == 1 and allSpots['BR'] == 1
  rgtDgn = allSpots['TR'] == 1 and allSpots['MC'] == 1 and allSpots['BL'] == 1
  wins = [
    topRow,
    midRow,
    btmRow,
    lftCol,
    cntCol,
    rgtCol,
    lftDgn,
    rgtDgn
  ]

  gridValues = gridVals.values()

  # check for draw
  if True not in wins and 0 not in gridValues:
    global gameResult
    global gameOn
    gameOn = False
    gameResult = 'Cat wins'
  else:
    for win in wins:
      if win:
        gameOn = False
        gameResult = 'Player ' + sym + ' wins the game!'

def run_game(player):
  print_grid()
  player_move_prompt(player)
  check_spots(player)

if __name__ == '__main__':
  while gameOn:
    if togglePlayer:
      run_game(playerX)
      togglePlayer = False
    else:
      run_game(playerO)
      togglePlayer = True
  else:
    print_grid()
    print(gameResult)