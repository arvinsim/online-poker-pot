from typing import List


def filter_players_from_ids(ids: List[int], players):
    result = []
    for player in players:
        if player['id'] in ids:
            result.append(player)
    return result





