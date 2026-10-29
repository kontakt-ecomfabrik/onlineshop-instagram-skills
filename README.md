# EcomFabrik Instagram Skills für Onlineshops

**Neun eigenständige Agent Skills**, um Instagram-Content für Shops und Produktmarken zu planen, zu schreiben und kritisch zu prüfen. Konkrete Produkte, Kundenfragen und Kaufentscheidungen stehen im Vordergrund – kein generischer Business-Coach-Content.

**Keine EcomFabrik-Anmeldung oder Instagram-API nötig.** Für Claude bzw. Codex benötigst du Zugang zum jeweiligen KI-Dienst. Nichts wird automatisch gepostet, und ohne von dir bereitgestellte Daten werden keine Instagram-Insights gelesen.

## Die 9 Skills

| Skill | Wofür? |
| --- | --- |
| [ecom-content](ecom-content/) | Allgemeine Instagram-Aufgabe und passende Formatwahl |
| [ecom-content-strategy](ecom-content-strategy/) | Ziele, Zielgruppe, Customer Journey, Content-Säulen, Messung |
| [ecom-content-ideas](ecom-content-ideas/) | Produktspezifische Ideen aus Kaufbarrieren und Kundenfragen |
| [ecom-reel](ecom-reel/) | Reel-Hooks, Skripte, Szenen und Faceless-Varianten |
| [ecom-carousel](ecom-carousel/) | Karussell-Slides, Produktwissen und Kaufhilfen |
| [ecom-story](ecom-story/) | Story-Sequenzen, FAQs und sinnvolle Interaktionen |
| [ecom-caption](ecom-caption/) | Natürliche Captions, die den Post ergänzen |
| **[ecom-brand-voice](ecom-brand-voice/)** | **Eigene Instagram-Markenstimme entwickeln und festhalten** |
| **[ecom-content-review](ecom-content-review/)** | **Fertigen Instagram-Beitrag vor Veröffentlichung prüfen** |

## Neu: Interaktive Fragen bei zu wenig Informationen

Ein allgemeiner Auftrag wie **„Erstelle mir ein Instagram-Reel“** löst zuerst kurze Fragen aus — beispielsweise zu Produkt, Zielgruppe, Reel-Ziel und vorhandenem Material. **Erst mit ausreichenden Angaben** erstellt der Skill das fertige Ergebnis. Das gilt für **alle neun Skills**.

- **Kein langer Fragebogen:** Im Normalfall ein bis drei kurze Gesprächsfragen, angepasst an das gewählte Format.
- **Keine Wiederholungen:** Informationen aus dem bisherigen Gespräch werden berücksichtigt; nur fehlende entscheidende Angaben werden erfragt.
- **Keine unnötigen Hürden:** Wer alle wichtigen Fakten geliefert hat, erhält direkt den Inhalt. Optionale Details müssen nicht geliefert werden.
- **Ausnahme:** Bei „Zeige mir nur ein Beispiel“ oder „Entscheide selbst“ sind sichtbar markierte Musterentwürfe möglich. Fakten wie Produktherkunft, Wirkung, Material oder Lagerbestand werden weiterhin nicht erfunden.
- **Kompatibel mit Claude und ChatGPT:** Standard sind gewöhnliche Rückfragen im Chat, keine vorausgesetzte besondere Formularfunktion.
- **Kein Zugriff auf fremde Accounts:** Aus einer Instagram-URL allein lässt sich kein überprüftes Markenprofil ableiten, wenn keine echte Kontoanalyse möglich war.

### Beispiel: Reel ohne Briefing

**Nutzer:** „Erstelle mir ein Instagram-Reel.“

**Skill:** „Welches Produkt soll im Mittelpunkt stehen? Wen möchtest du damit erreichen und welche Frage beantworten? Welche Fotos oder Videos hast du bereits?“

**Nutzer:** „Ein kleiner Silberanhänger, für Menschen, die ein persönliches Geschenk suchen. Ich habe nur Produktfotos.“

**Skill:** Erst jetzt konkretisiert er die nachweisbaren Produkteigenschaften, falls sie für die gewählte Aussage benötigt werden, und plant anschließend ein realistisch umsetzbares Reel aus Produktfotos.

## So arbeiten sie zusammen

1. **Einmalig Brand Voice definieren:** Shop und Zielgruppe beschreiben, ggf. echte bisherige Captions einfügen; zwei Stilrichtungen vergleichen. Ergebnis als `brand-voice.md` speichern und bestätigen.
2. **Strategie und Ideen:** Prioritäten, Produkte und Kundenfragen mit `ecom-content-strategy` bzw. `ecom-content-ideas` bestimmen. Fehlende Daten bleiben Hypothesen.
3. **Inhalte erstellen:** Reel, Carousel, Story oder Caption. Das bestätigte **Brand-Voice-Profil als Eingabe einfügen oder hochladen**, wenn es in der aktuellen Umgebung nicht vorhanden ist.
4. **Vor Veröffentlichung prüfen:** Entwurf mit `ecom-content-review` auf verständliche Aussagen, Markenstimme, echte Belege und offene Medien-/Werberechte prüfen. Die endgültige Freigabe bleibt beim Shop.

**Jeder Skill funktioniert einzeln.** Nicht alle neun müssen installiert werden. Die Ausführung anderer Skills oder das dauerhafte Speichern des Markenprofils geschieht **nicht automatisch** durch diese Dateien.

## Beispiele

### Markenstimme entwickeln
```text
Entwickle mit ecom-brand-voice unsere Instagram-Markenstimme.
Shop: [PRODUKTWELT]  Zielgruppe: [KUNDEN]
Hier sind drei bisherige Captions: [TEXTE].
Vergleiche zwei deutlich unterschiedliche Stilrichtungen.
Trenne Beobachtungen von deinen Vorschlägen.
```

### Reel erstellen
```text
Erstelle mit ecom-reel ein 20-Sekunden-Reel für [PRODUKT].
Bestätigte Produktinfos: [DATEN].
Kundenfrage: [FRAGE]. Vorhandene Fotos/Videos: [MATERIAL].
Brand Voice: [BESTÄTIGTES PROFIL].
```

### Content prüfen
```text
Prüfe mit ecom-content-review diese Instagram-Caption: [TEXT].
Bestätigte Fakten: [FAKTEN]. Brand Voice: [PROFIL, FALLS VORHANDEN].
Prüfe konkrete Schwachstellen, mögliche unbelegte Aussagen und Markenpassung.
Schreibe anschließend eine überarbeitete Fassung ohne erfundene Angaben.
```

## Installation und Qualität

[Schritt-für-Schritt-Installation](INSTALLATION.md) für Claude, Claude Code und Codex. Die Skills sind je ein Ordner mit `SKILL.md` und eigenen `references/`. Updates im GitHub-Repository aktualisieren bereits installierte ZIPs **nicht automatisch**.

- `python3 scripts/validate_skills.py` prüft Struktur, Namen, Beschreibungen und lokale Referenzen; ein GitHub-Workflow führt die Prüfung bei Push/PR aus.
- [Manuelle Akzeptanztests](tests/ACCEPTANCE.md) beschreiben reale Testfälle. Der Strukturtest **beweist kein korrektes Modellverhalten** in Claude oder Codex.
- Kein automatisches Veröffentlichen, Auslesen fremder Accounts oder garantierte Reichweite/Umsatz.
- Werbekennzeichnung, kommerzielle Musik, Bild-/UGC-Rechte und sensible Produktclaims sind **Prüfpunkte**, keine Rechtsberatung.

## Offizielle Referenzen

- [Claude: Custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [Claude: Skills nutzen](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [OpenAI: Build Skills](https://learn.chatgpt.com/de-DE/docs/build-skills)
- [Instagram: Lizenzierte Musik](https://www.facebook.com/help/instagram/402084904469945)
- [GEMA: Musik für Reels gewerblich nutzen](https://www.gema.de/de/w/hilfe/musiknutzer/musik-nutzen/social-media-websites/instagrams-musikbibliothek-nutzen-fuer-story-reel)
- [Medienanstalten: Werbekennzeichnung](https://www.die-medienanstalten.de/service/merkblaetter-und-leitfaeden/leitfaden-werbekennzeichnung-bei-online-medien/)

## Autorin

**Dr. Kenanah Shereih – EcomFabrik** · [ecomfabrik.de](https://ecomfabrik.de) · [Instagram @ecomfabrik.de](https://www.instagram.com/ecomfabrik.de/)

Ein öffentliches Repository ohne ausdrückliche Lizenz ist nicht automatisch zur beliebigen Weiterverwendung freigegeben.
