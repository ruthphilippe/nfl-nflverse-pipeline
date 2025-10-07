import nflreadpy as nfl
import polars as pl

def fetch_schedules(seasons=None):
    return nfl.load_schedules(seasons=seasons)

def fetch_team_stats(seasons=None):
    return nfl.load_team_stats(seasons=seasons, summary_level="week")

def fetch_player_stats(seasons=None):
    return nfl.load_player_stats(seasons=seasons, summary_level="week")

def fetch_injuries(seasons=None):
    return nfl.load_injuries(seasons=seasons)