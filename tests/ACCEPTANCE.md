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
