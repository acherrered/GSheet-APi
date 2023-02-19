from flask import Flask, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Fonction pour récupérer les informations d'identification du fichier JSON
def get_credentials(): 
    credentials_dict = { # to generate from google console API 
        "type": "service_account",
        "project_id": "dynamic-sun-351814",
        "private_key_id": "c0aedb4961166e97318bf7633110a32a25f7fb15",
	"private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDgFGxIJF68xNPC\np4VxGlkhxKCXOFX1clPkRpVDZpF+MlpzFHy5Zah3F3O+/JlnUNg/o/xs1pAlKWm0\nYgGHjaKctv9AP5Tfm1cZSLaBTs74V8Qo3CIuGSjHsDqSdgiUgjNxFZFNBSyQ5pgn\ns21/oYYdHyVZqvbYJ/RgApDA5yA4DQG3bdXU5rxOtBH9sCr3s5BkoHpJcLJnUxUL\nKcfd2QLZEeLxyXhuuf7P+3Au4ZUrgkFx+8ViiaHTmse+l5eGOYfe93AjHGNNKFpU\nilTB8Ervi/tSTxvBcW6ZcrTKeXHPUhOAO2eA8P9PvPTE0LY8VOyJqoANkaTxHBBR\nKBZ/72IhAgMBAAECggEAOlznZRTf/f+v/gOe7HoF3Bc4EprwPJkWA59ksiTtYTah\nO1cLM0ioi7g2g/iLxg6W/GBsVza9XYh/SSW7q0A3KeU571SAJItzsJixPFW375QA\nefn4BxSze+tJHiuTCYct+da5vRtLY8RDvhdsPjFmWoBpvIScfWlOq5EPfcbVK/Ou\nZGuW/oOdr4pekYlFpgqKz5Y2C6wotMGloW0+wV7CMlXHwdD9ob1yoRuKFezbdIDy\ngwPz0ZKiI19jRAqzdZ7D7dsycZ3iBvF924lCEgIK5m7nuU097qokYaF32vCwvfuQ\nmrqBAlfRZp1u9t0tfVnkVTPAl36bKzlwuKcMzQp1TwKBgQD7fUQGmlssejncQuxK\nSP8Q6gHCBlOa3HkdAnWdquaNf2nY8vXty0BiUeELuyOLOJvfk2jOO/oBzOFPw6XA\nsHs1jojXLbWpvbWNcwI2S2spZHFolfGBku7CIapm5VqmyN+wup6E3aULfGtkYg8u\nycyINF7JBmLboGq3mTD5LwpOewKBgQDkGU3VtMAvYtr8t8pgVigrIYypKVKFvOSQ\n+j2TqOb95rF+XBHTteIfl63HC9kS3APjwYRWfUrX5j86uVasyNtyKsV5O/HVBBGc\np/Rcp1XSoHh+JCBdKmwpaHb5FeBivMZCEq0IuAadhAtUWKVA5CQEsVG3kHO2ZfzS\nhP3/wxT9EwKBgChiaTYWO2XdCsWQCZm0NyFkMnwRwAMyPFCoQHLdKsC2IS0xdsSE\nywX+2ACmQILuyDkS1tWnU/JOEDBa3pcev+pNxTOop29mg2z/du95FPBErOF6kpmY\nGrcZ6N81HWWDBEjA7wuu+/3oMOahyIZe6XVF06K8X8uc6wYol3CsWR9ZAoGBALEP\nt2zRz3G5QhZ0sOMRXkME2wShMA7ir2ae6dfKf+zN/DADVk9KXAp8GohteQb7xQUy\nPgFJZySq9aAnKNIdZMN90iam0rWxX96EPdsChktnB8GbV4gamzWVgu0d/z2GHjxB\n9RHUkEYLryO9YCI8Nn1yC+X7euc2yge89tJn484DAoGBAKuTArvsPANPG/u/pl4i\n5dOswt0JfNvKZRsL8/xqDXfjgCHwuGEaUuZa06e/r5A/eAvP9aUW+AB57wSdKsf6\nghviyRpsa/L8ce/AOrFPfmjGSOHxeCM20DsriKQV/PWJZBl2Qr/VmRD06aysBHLf\nK32WLokWOXNK70bfzoSdqesH\n-----END PRIVATE KEY-----\n",
        "client_email": "mitrust-316@dynamic-sun-351814.iam.gserviceaccount.com",
        "client_id": "105906344729950900523",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
	      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/mitrust-316%40dynamic-sun-351814.iam.gserviceaccount.com"

    }

    # Load credentials
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict)
    return credentials

# Access to googlesheet
def open_spreadsheet():
    credentials = get_credentials()
    gc = gspread.authorize(credentials)
    # Remplacez "Nom de votre feuille de calcul" par le nom de votre propre feuille de calcul
    sh = gc.open_by_key("10PEVSrnO1fW9YdmeCbRCh3KJeF4ZcRmuAQJ7NY9pEXY")
    return sh

# Route to send data to the googlesheet
@app.route('/send_data', methods=['POST'])
def send_data():
    sh = open_spreadsheet()
    # Define Sheet name and column name
    worksheet = sh.worksheet("aaa")
    data = request.json
    #worksheet.append_row([data["A"], data["B"]])
    worksheet.append_row([data["A"]])
    return "Données envoyées avec succès à Google Sheet!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

  #send data
  #curl -X POST -H "Content-Type: application/json" -d '{"A": "Valeur 1"}' https://GSheet-APi.aminecherrered.repl.co/send_data
