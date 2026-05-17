from flask import Flask, render_template, request
import logging
from datetime import datetime

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


@app.route('/travel-insurance')
def travel_insurance_redirect():
    gclid    = request.args.get('gclid', '')
    utm_src  = request.args.get('utm_source', '')
    utm_med  = request.args.get('utm_medium', '')
    utm_camp = request.args.get('utm_campaign', '')
    utm_term = request.args.get('utm_term', '')

    logging.info(
        "[TRAVEL REDIRECT] %s | gclid=%s | source=%s | medium=%s | campaign=%s | term=%s",
        datetime.utcnow().isoformat(),
        gclid, utm_src, utm_med, utm_camp, utm_term
    )

    return render_template('travel_redirect.html')


@app.route('/health')
def health():
    return 'ok', 200


if __name__ == '__main__':
    app.run(debug=False)
