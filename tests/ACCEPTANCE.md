# Manuelle Funktionstests für Instagram Skills v2

Dies sind **Testfälle**, keine ausgeführten Modelltests. Ergebnis in Claude/Codex samt Modell, Datum, Bestanden/Nicht bestanden und Fehler dokumentieren.

| Fall | Skill | Testeingabe / Erwartung |
| --- | --- | --- |
| BV1 | brand-voice | Schmuckshop mit 3 echten Captions: beobachtete vs. vorgeschlagene Stimme unterscheiden; 2 konkret unterschiedliche Versionen, keine erfundenen Materialangaben |
| BV2 | brand-voice | Kosmetikshop ohne alte Posts: **vorläufige** Stimme liefern, keine erfundenen Wirkungen, keine behauptete Instagram-Analyse |
| BV3 | brand-voice | 2 Shops unterschiedlicher Positionierung: nachweisbar andere Wortwahl und CTAs, keine EcomFabrik-Einheitsstimme |
| RV1 | content-review | "Unser Serum entfernt alle Falten garantiert" ohne Beleg: Blocker nennen, kein Freigabesiegel |
| RV2 | content-review | Nur Reel-Skript ohne Video: ausschließlich Textprüfung, nicht Musik und Bildqualität behaupten |
| RV3 | content-review | UGC mit fehlender Zustimmung: Rechte und ggf. Kennzeichnung markieren |
| RV4 | content-review | Gute Schmuck-Caption + bestätigte Markenstimme: minimal korrigieren |
| ST1 | content-strategy | Shop ohne Insights und nur 3 Produktfotos: realistische Startannahmen statt Benchmarks und unrealistischer Postingpflicht |
| ID1 | content-ideas | Ein Produkt, 10 Ideen: neue konkrete Kauf-/Nutzungsfragen, keine Paraphrasen |
| RE1 | reel | Silberkette, nur Material bekannt: keine Aussagen zu Allergie, Haltbarkeit oder Duschen, Rechtecheck für Musik |
| CA1 | carousel | Thema mit 3 sinnvollen Slides: keine künstlichen Füllslides |
| SO1 | story | Unbekannter Lagerbestand: keine erfundenen "nur noch 2 Stück" |
| CP1 | caption | Caption zu vorhandenem Carousel: ergänzen statt Slides wiederholen |
| RO1 | content router | Auftrag "Prüfe diese Caption": Review-Workflow bevorzugen; kein angeblicher Aufruf eines nicht aktiven Skills |

**Freigabe-Check:** Alle Fälle im tatsächlichen Zielprodukt ausführen, kritische Verstöße korrigieren und erneut testen. `scripts/validate_skills.py` prüft ausschließlich die Dateistruktur, nicht das Modellverhalten.

## Interaktive Intake-Tests (Claude **und** ChatGPT)

Diese Fälle nach Installation in beiden Zielumgebungen **als neue Konversation** testen. Nicht nur das Vorhandensein der Regeln in `SKILL.md`, sondern das **tatsächlich beobachtete Modellverhalten** entscheidet.

| Fall | Skill | Eingabe | Erwartete **erste** Reaktion |
| --- | --- | --- | --- |
| IN-CONTENT | ecom-content | „Erstelle Instagram-Content.“ | Fragt nach Aufgabe/Format, Shop/Produkt, Zielgruppe/Ziel; **kein vollständiger Post** |
| IN-STRATEGY | ecom-content-strategy | „Erstelle meine Instagram-Strategie.“ | Fragt nach Shop/Produkten, Zielgruppe, Geschäftsziel/Umsetzungskapazität; **keine fertige Strategie** |
| IN-IDEAS | ecom-content-ideas | „Gib mir zehn Instagram-Ideen.“ | Fragt nach Produkt, Kundschaft und Ziel; **keine generische Liste** |
| IN-REEL | ecom-reel | „Erstelle mir ein Instagram-Reel.“ | Fragt nach Produkt, Kundschaft/Ziel, verfügbarem Material; **kein vollständiges Skript** |
| IN-CAROUSEL | ecom-carousel | „Mach ein Instagram-Carousel.“ | Fragt nach Thema/Kundenfrage, Zielgruppe, belegbaren Informationen; **keine Slides** |
| IN-STORY | ecom-story | „Erstelle Instagram-Stories.“ | Fragt nach Produkt/Anlass, Ziel und verfügbarem Material; **keine Story-Sequenz** |
| IN-CAPTION | ecom-caption | „Schreib meine Instagram-Caption.“ | Fragt nach Post-Inhalt, Produkt und Ziel; **keine Caption ausgedacht** |
| IN-VOICE | ecom-brand-voice | „Erstelle meine Brand Voice.“ | Fragt nach Shop/Produkten, Zielkunden, Sprachpräferenzen; **kein fertiges Profil** |
| IN-REVIEW | ecom-content-review | „Prüfe meinen Instagram-Beitrag.“ | Fragt nach **dem konkreten Inhalt**, statt einen erfundenen Post zu bewerten |
| IN-PARTIAL | ecom-reel | „Reel für Silberschmuck, Zielgruppe Geschenkekäufer.“ | Fragt **nur fehlendes Ziel/Material/Produktdetails**, keine Wiederholung der Zielgruppe |
| IN-COMPLETE | ecom-reel | Vollständige Produkteigenschaften + konkrete Kundengruppe + Kaufhürde + verfügbare Aufnahmen + Ziel | **Direktes Skript**, keine Standard-Rückfragen |
| IN-EXAMPLE | ecom-caption | „Zeige ein frei erfundenes, eindeutig als Muster gekennzeichnetes Caption-Beispiel, keine Rückfragen.“ | Liefert Muster mit neutralen Platzhaltern; **keine erdachten Produktfakten als Belege** |
| IN-FOLLOWUP | ecom-brand-voice | Antworten auf die ersten drei Fragen in Folgemeldung | Verwendet bisherige Angaben, fragt nicht erneut dieselben Punkte |
| IN-REVIEW-PARTIAL | ecom-content-review | Vollständiger Caption-Text, aber keine Brand-Voice-Datei | Macht **Textprüfung**, bezeichnet individuellen Brand-Voice-Abgleich als nicht überprüfbar; kein Blockieren |

**Fehlerkriterium:** Fertiges Artefakt trotz fehlender Pflichtangaben, Halluzination von Shopdaten, redundante Rückfragen, Pflichtangabe optionaler Daten, vorgetäuschte Formulare/Accountzugriffe oder Nachfragen trotz vollständiger Angaben.

**Hinweis:** Diese Tabelle dokumentiert erwartetes Verhalten, **keine ausgeführten Claude-/ChatGPT-Testläufe**.
