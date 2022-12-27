from flask import Flask
import utils

app = Flask(__name__)


@app.route('/')
def all_cand():
    return utils.all_cand(utils.load_candidates())


@app.route('/candidates/<x>')
def candidates_page(x):
    candidate = utils.get_by_pk(int(x))
    return  f"<img src={candidate['picture']}>" + utils.all_cand([candidate])


@app.route("/skills/<x>")
def skills_page(x):
    return utils.all_cand(utils.get_by_skill(x))











app.run()