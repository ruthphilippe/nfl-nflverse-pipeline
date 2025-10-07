import polars as pl

def clean_schedules(df: pl.DataFrame) -> pl.DataFrame:
    keep = [
        "game_id", "season", "week", "gameday", "home_team", "away_team",
        "home_score", "away_score", "result"
    ]
    return df.select([c for c in keep if c in df.columns])

def clean_team_stats(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns([
        pl.col("offensive_plays").cast(pl.Float64, strict=False)
        if "offensive_plays" in df.columns else None
    ])
def passthrough(df: pl.DataFrame) -> pl.DataFrame:
    return df