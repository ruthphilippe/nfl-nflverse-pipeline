import extract as ex
import transform as tr
import load as ld
from config import NFL_S3_BUCKET

def run_pipeline(season=2024):
    if not NFL_S3_BUCKET:
        raise ValueError("S3 bucket not configured in .env")
    
    print(f"Starting NFL pipeline for season {season}")

    #Extract
    sched = ex.fetch_schedules(season)
    team_stats = ex.fetch_team_stats(season)
    player_stats = ex.fetch_player_stats(season)
    injuries = ex.fetch_injuries(season)

    #Transform
    sched_clean = tr.clean_schedules(sched)
    team_clean = tr.clean_team_stats(team_stats)
    player_clean = tr.passthrough(player_stats)
    inj_clean = tr.passthrough(injuries)

    #Load to S3
    ld.upload_df(sched_clean, "schedules", season)
    ld.upload_df(team_clean, "team_stats_week", season)
    ld.upload_df(player_clean, "player_stats_week", season)
    ld.upload_df(inj_clean, "injuries", season)

    print("All uploads complete!")

if __name__ == "__main__":
    run_pipeline(2024)