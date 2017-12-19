from ..model import *
from .. import app
from ..logic.poll_service import find_poll,votes_per_day
from ..logic.census_service import census_count
from flask import render_template
from flask import jsonify

@app.route('/visres/data/day/<poll_id>')
def votes_per_day_data(poll_id):
    poll = find_poll(poll_id)
    vpd = votes_per_day(poll_id);
    res= jsonify(
        len=poll.votos_actuales,
        labels=vpd[0],
        data=vpd[1]
    )
    return res

@app.route('/visres/data/census/<poll_id>')
def participation(poll_id):
    poll = find_poll(poll_id)
    participantsN = census_count(poll.census.id);
    res= jsonify(
        participation=participantsN/poll.votos_actuales
    )
    return res

