#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kočičí Věštírna - Webová aplikace v Pythonu
Věštna jako by to říkala kočka!
"""

from flask import Flask, render_template_string, jsonify
import random

app = Flask(__name__)

# Kočičí věštby
FORTUNES = [
    "Vidím tě... Vidím, že ses dnes nechal léňoví. To se kočce líbí! Více spánku a méně prací! 💤",
    "Tvoje budoucnost je jasná - budeme spolu relaxovat na slunci! Není na tom nic špatného! ☀️",
    "Vrhaná kostka mluví: Zítra si dáš rybu. Je to věstba nebo přání? Já vím! 🐟",
    "Moje kočičí instinkty vidí nebezpečí! Psy se blíží! Utíkej na stůl! 🏃",
    "Věda hovoří: Jsi přesně tam, kde bys měl být - místo, kde se můžu koukat z okna. 🪟",
    "Čtu ti z lesklých očí: Dnes bude den plný překvapení a mnoho vrčení! 😸",
    "Hlasitě si mňoukám věštbu: MRŇAU! To znamená, že bys měl koupit rybu. Nebo pamlsky. Nebo oboje! 🐾",
    "Moje osmá barva vidí budoucnost: Budeš kouřit s lehkou studenou a čekat... Čekat na co? Na mě! 😻",
    "Věští se mi, že někdo chce koukat do mé duše. Ale kočka nemá duši, má jen kozy! Mrrr! 🐱",
    "Podle staré kočičí pověsti: Když se oči lesknou v noci, znamená to velkou změnu. Buď připraven! ✨",
    "Vidím v tě dřímající potenciál. Pojď se koukat se mnou! Může to trvat pár hodin... Nebo dní! 😴",
    "Moje věštba je jednoznačná: Kal na botě? Nakopu to co nejdál! Tak budoucnost vypadá! 👢",
    "Slyším hlasy z kočičích dimenzí: Budeš mít štěstí! Nebo smůlu. Záleží, jestli si mě dáš pomazlit! 🐾",
    "Hmm, teď vidím zvláštní symbol... Je to... Misky s jídlem! To není věstba, to je jen můj hlad! 🍽️",
    "Věšticí kočka věští: Budeš koukat do mobilní obrazovky a cítit se viňový. Jako vždycky! 📱",
    "Moje třetí oko vidí: V příštím týdnu se stane něco nekočičího. Patrně normální lidská věc. 🙄",
    "Podle mě? Máš přesně tolik štěstí, kolik je chlupů na mém ocasu - a to je SPOUSTY! 🐈",
    "Věšticí instinkt mi říká: Cokoliv se chystáš dělat - zpomal a línej se na to! 😼",
    "Vidím tě v zrcadle budoucnosti... Kouješ tam a jesteš spokojený. To je všechno, co potřebuješ! 🪞",
    "Moje věštba: Něco kouklíčího se v tobě probouzí. Gratuluji! Jsi half-kočka! 🎉"
]

# Kočičí zvuky
CAT_SOUNDS = ["Mňau!", "Mrrr!", "Prr!", "Myáu!", "Chrup!", "Frrr!"]

# HTML/CSS/JavaScript šablona
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kočičí Věštírna</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #FF8C42 0%, #9B59B6 25%, #E8E8E8 50%, #2C3E50 75%, #FF8C42 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            background: linear-gradient(135deg, #FFE5CC 0%, #F0E6FF 50%, #E8F4F8 100%);
            border-radius: 30px;
            padding: 50px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3),
                        inset 0 0 30px rgba(255, 255, 255, 0.5);
            max-width: 600px;
            text-align: center;
            border: 3px solid #FF8C42;
        }

        .cat-head {
            font-size: 100px;
            margin-bottom: 20px;
            animation: headBob 2s ease-in-out infinite;
        }

        @keyframes headBob {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }

        h1 {
            color: #2C3E50;
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }

        .subtitle {
            color: #FF8C42;
            font-size: 1.2em;
            font-style: italic;
            margin-bottom: 30px;
        }

        .paws {
            display: flex;
            justify-content: space-around;
            margin: 30px 0;
            opacity: 0.7;
        }

        .paw {
            font-size: 60px;
            animation: pawWave 1s ease-in-out infinite;
        }

        .paw:nth-child(1) { animation-delay: 0s; }
        .paw:nth-child(2) { animation-delay: 0.2s; }
        .paw:nth-child(3) { animation-delay: 0.4s; }
        .paw:nth-child(4) { animation-delay: 0.6s; }

        @keyframes pawWave {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-15px) rotate(15deg); }
        }

        .fortune-box {
            background: linear-gradient(135deg, #FFF8DC 0%, #FFE5CC 100%);
            border-radius: 20px;
            padding: 30px;
            margin: 30px 0;
            border: 2px solid #FF8C42;
            min-height: 120px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .fortune-text {
            color: #2C3E50;
            font-size: 1.3em;
            font-style: italic;
            font-weight: bold;
            line-height: 1.6;
        }

        .button-container {
            margin: 30px 0;
        }

        button {
            background: linear-gradient(135deg, #FF8C42 0%, #E74C3C 100%);
            color: white;
            border: none;
            padding: 18px 40px;
            font-size: 1.2em;
            border-radius: 50px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        button:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
            background: linear-gradient(135deg, #FFB366 0%, #FF6B5B 100%);
        }

        button:active {
            transform: translateY(-1px);
        }

        .shine {
            animation: shine 0.5s ease-in-out;
        }

        @keyframes shine {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }

        .footer {
            margin-top: 30px;
            color: #7F8C8D;
            font-size: 0.9em;
        }

        .cat-eyes {
            font-size: 50px;
            margin: 20px 0;
            animation: eyeBlink 3s ease-in-out infinite;
        }

        @keyframes eyeBlink {
            0%, 95%, 100% { opacity: 1; }
            97% { opacity: 0.2; }
        }

        .loading {
            opacity: 0.5;
            pointer-events: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="cat-head">🐱</div>
        <h1>Kočičí Věštírna</h1>
        <p class="subtitle">Tajná moudrost kočiček čeká na tebe...</p>
        
        <div class="cat-eyes">👀</div>
        
        <div class="paws">
            <div class="paw">🐾</div>
            <div class="paw">🐾</div>
            <div class="paw">🐾</div>
            <div class="paw">🐾</div>
        </div>

        <div class="fortune-box">
            <div class="fortune-text" id="fortune">
                Klikni na tlačítko a nechej věštit jedinou opravdovou věštkyni - kočku! 🔮
            </div>
        </div>

        <div class="button-container">
            <button id="fortuneBtn" onclick="getFortuneFromCat()">Věštět mě! 🐱✨</button>
        </div>

        <div class="footer">
            <p>© 2026 Kočičí Věštírna | Powered by Python & Flask | Všechna práva vyhrazena kočkám 🐾</p>
        </div>
    </div>

    <script>
        async function getFortuneFromCat() {
            const button = document.getElementById('fortuneBtn');
            button.classList.add('shine', 'loading');
            
            try {
                const response = await fetch('/api/fortune');
                const data = await response.json();
                
                // Animace - oči blikají
                const eyes = document.querySelector('.cat-eyes');
                eyes.style.animation = 'none';
                setTimeout(() => {
                    eyes.style.animation = '';
                }, 10);
                
                const fortuneText = document.getElementById('fortune');
                
                // Animace zmizel/objevil se text
                fortuneText.style.opacity = '0';
                setTimeout(() => {
                    fortuneText.textContent = data.sound + " " + data.fortune;
                    fortuneText.style.opacity = '1';
                    fortuneText.style.transition = 'opacity 0.5s ease-in-out';
                }, 300);
                
            } catch (error) {
                console.error('Chyba:', error);
                document.getElementById('fortune').textContent = 'Něco se pokazilo! Kočka se zlobila! 😾';
            } finally {
                setTimeout(() => {
                    button.classList.remove('shine', 'loading');
                }, 500);
            }
        }

        // Tlačítko se dá aktivovat i entrem
        document.getElementById('fortuneBtn').addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                getFortuneFromCat();
            }
        });
    </script>
</body>
</html>"""


@app.route('/')
def index():
    """Hlavní stránka - vrací HTML"""
    return render_template_string(HTML_TEMPLATE)


@app.route('/api/fortune')
def get_fortune():
    """API endpoint - vrací náhodnou věštbu a zvuk"""
    fortune = random.choice(FORTUNES)
    sound = random.choice(CAT_SOUNDS)
    return jsonify({
        'fortune': fortune,
        'sound': sound
    })


def main():
    """Spuštění Flask aplikace"""
    print("=" * 60)
    print("🐱 KOČIČÍ VĚŠTÍRNA - Python & Flask Edition 🐱")
    print("=" * 60)
    print("\n✨ Aplikace běží na: http://127.0.0.1:5000")
    print("✨ Otevři si ji v prohlížeči a nechej se věštit!\n")
    print("Kočka je připravena věštit... 🔮\n")
    print("Stiskni Ctrl+C pro vypnutí.\n")
    print("=" * 60 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)


if __name__ == '__main__':
    main()
