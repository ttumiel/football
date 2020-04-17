from . import *

first_team_pos = [
  [-1.000000, 0.000000, e_PlayerRole_GK],
  [-0.267574, 0.000000, e_PlayerRole_CM],
  [0.000000, -0.020000, e_PlayerRole_CF],
  [-0.500000, -0.06356, e_PlayerRole_CB],
  [-0.500000, 0.063559, e_PlayerRole_CB],
  [0.000000,  0.020000, e_PlayerRole_RM],
  [-0.422000, -0.19576, e_PlayerRole_LB],
  [-0.422000, 0.195760, e_PlayerRole_RB],
  [-0.184212, -0.10568, e_PlayerRole_CM],
  [-0.184212, 0.105680, e_PlayerRole_CM],
  [-0.010000, -0.21610, e_PlayerRole_LM],
]

second_team_pos = [
  [-1.000000, 0.000000, e_PlayerRole_GK],
  [-0.267574, 0.000000, e_PlayerRole_CM],
  [-0.010000, 0.216102, e_PlayerRole_CF],
  [-0.500000, -0.06356, e_PlayerRole_CB],
  [-0.500000, 0.063559, e_PlayerRole_CB],
  [-0.050000, 0.000000, e_PlayerRole_RM],
  [-0.422000, -0.19576, e_PlayerRole_LB],
  [-0.422000, 0.195760, e_PlayerRole_RB],
  [-0.184212, -0.10568, e_PlayerRole_CM],
  [-0.184212, 0.105680, e_PlayerRole_CM],
  [-0.010000, -0.21610, e_PlayerRole_LM],
]

def build_scenario(builder):
  builder.config().deterministic = False
  if builder._config['duration'] is not None:
    builder.config().game_duration = builder._config['duration']
  else:
    builder.config().game_duration = 500

  if builder._config['difficulty'] is not None:
    builder.config().right_team_difficulty = builder._config['difficulty']
    builder.config().left_team_difficulty = builder._config['difficulty']
  else:
    builder.config().right_team_difficulty = 0.10
    builder.config().left_team_difficulty = 0.10

  if builder.EpisodeNumber() % 2 == 0:
    first_team = Team.e_Left
    second_team = Team.e_Right
  else:
    first_team = Team.e_Right
    second_team = Team.e_Left

  builder.SetTeam(first_team)
  for i in range(builder._config['left_players']):
    builder.AddPlayer(*first_team_pos[i])

  builder.SetTeam(second_team)
  for i in range(builder._config['right_players']):
    builder.AddPlayer(*second_team_pos[i])
