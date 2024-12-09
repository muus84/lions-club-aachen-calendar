import requests
from datetime import datetime
import argparse
from bs4 import BeautifulSoup

def get_gewinnzahlen(tag):
    """
    Ruft die Gewinnzahlen für einen bestimmten Tag ab.

    :param tag: Der Tag, für den die Gewinnzahlen abgerufen werden sollen (1-24).
    :return: Eine Liste der Gewinnnummern für den angegebenen Tag.
    """
    url = f"https://carolina.lions-aachen.de/advent2024/html/Today.php?day={tag}"
    try:
        response = requests.get(url)
        response.raise_for_status()

        # HTML parsen
        soup = BeautifulSoup(response.text, 'html.parser')

        # Alle Elemente mit dem Attribut 'data-sheets-value' finden
        data_elements = soup.find_all(attrs={"data-sheets-value": True})

        gewinnzahlen = []

        # Gewinnzahlen aus jedem gefundenen Element extrahieren
        for element in data_elements:
            gewinnzahlen_text = element["data-sheets-value"]
            # Gewinnzahlen sind durch ' - ' getrennt
            zahlen = [num.strip() for num in gewinnzahlen_text.split(" - ")]
            gewinnzahlen.extend(zahlen)

        return gewinnzahlen
    except requests.RequestException as e:
        print(f"Fehler beim Abrufen der Gewinnzahlen für Tag {tag}: {e}")
        return []

def check_gewinn(gewinn_nummer, alle_tage):
    """
    Überprüft, ob die angegebene Gewinnnummer gewonnen hat.

    :param gewinn_nummer: Die zu überprüfende Gewinnnummer als String.
    :param alle_tage: Boolean, ob alle Tage (1-24) überprüft werden sollen.
    """
    heutiger_tag = datetime.now().day
    tage = range(1, 25) if alle_tage else [heutiger_tag]
    gewinne = []

    for tag in tage:
        gewinnzahlen = get_gewinnzahlen(tag)
        if gewinn_nummer in gewinnzahlen:
            gewinne.append(tag)

    if gewinne:
        if alle_tage:
            tage_str = ', '.join(str(t) for t in gewinne)
            print(f"Herzlichen Glückwunsch! Deine Gewinnnummer {gewinn_nummer} hat an folgenden Tagen gewonnen: {tage_str}.")
        else:
            print(f"Herzlichen Glückwunsch! Deine Gewinnnummer {gewinn_nummer} hat heute (Tag {heutiger_tag}) gewonnen.")
    else:
        if alle_tage:
            print(f"Leider hat Deine Gewinnnummer {gewinn_nummer} an keinem Tag (1-24) gewonnen.")
        else:
            print(f"Leider hat Deine Gewinnnummer {gewinn_nummer} heute nicht gewonnen.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prüfe Adventskalender-Gewinnnummer.")
    parser.add_argument("gewinn_nummer", type=str, help="Die zu überprüfende Gewinnnummer.")
    parser.add_argument("--alle_tage", action="store_true", help="Überprüfe alle Tage (1-24), nicht nur den heutigen Tag.")

    args = parser.parse_args()
    check_gewinn(gewinn_nummer=args.gewinn_nummer, alle_tage=args.alle_tage)
