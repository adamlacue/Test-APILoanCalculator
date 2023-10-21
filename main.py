from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask('app')
CORS(app)


@app.post('/calculate')
def calculation():
  data = request.json
  price = float(data.get("price") or 0) 
  trade = float(data.get("trade"))
  accessory = float(data.get("accessory"))
  subtotal = price - trade + accessory
  tax_rate = float(data.get("tax_rate"))
  tax = round((tax_rate * subtotal), 2)
  title = float(data.get("title"))
  payoff = float(data.get("payoff"))
  total = subtotal + tax + title + payoff
  down = float(data.get("down"))
  financed = total - down
  term = int(data.get("term"))
  interest_rate = float(data.get("interest_rate"))
  rate = interest_rate / 12
  factor = rate * ((1 + rate) ** term) / (((1 + rate) ** term) - 1)
  payment = round(financed * factor, 2)

  response = {
    'price': price,
    'trade': trade,
    'accessory': accessory,
    'subtotal': subtotal,
    'tax': tax,
    'title': title,
    'payoff': payoff,
    'total': total,
    'down': down,
    'financed': financed,
    'term': term,
    'interest_rate': interest_rate,
    'payment': payment
    }

  return jsonify(response)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
