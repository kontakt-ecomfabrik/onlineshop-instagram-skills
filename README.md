# Instagram-Skills für Onlinehändler

Sieben wiederverwendbare Agent Skills für Onlineshops, Produktmarken, Etsy-Seller, Shopify- und WooCommerce-Shops, Amazon-Händler sowie Hersteller.

Die Skills helfen bei Instagram-Strategie, Content-Ideen, Reels, Carousels, Stories und Captions. Im Mittelpunkt stehen Produkte, Kundenfragen, Kaufbarrieren und die Customer Journey – nicht allgemeiner Coach-Content.

**Keine Anmeldung, kein API-Schlüssel und keine Instagram-Verbindung erforderlich.**

> **Nichts wird automatisch veröffentlicht.** Die Skills erstellen Strategien und Content-Entwürfe. Du prüfst, gestaltest und veröffentlichst selbst.

## Was dieses Paket besonders macht

- Inhalte werden aus realen Produkten, Anwendungen und Kundenfragen entwickelt.
- Produktmerkmale werden in nachvollziehbare Nutzung und Entscheidungshilfe übersetzt.
- Fehlende Fakten werden als Annahme oder Platzhalter gekennzeichnet.
- Jeder Inhalt erhält eine klare Aufgabe: Reichweite, Vertrauen, Abwägung, Kauf, Nutzung oder Kundenbindung.
- Reels, Carousels, Stories und Captions folgen jeweils einem eigenen Workflow.
- Generische Marketingfloskeln und austauschbarer Coach-Content werden vermieden.
- Die vorgeschlagene Frequenz richtet sich nach den tatsächlich verfügbaren Ressourcen.

## Installation

Die vollständige Schritt-für-Schritt-Anleitung findest du in **[INSTALLATION.md](INSTALLATION.md)**.

### Claude – Kurzfassung

1. Gewünschten Skill-Ordner einzeln als ZIP-Datei verpacken.
2. In Claude **Customize → Skills** öffnen.
3. **+ → Create skill → Upload a skill** wählen.
4. ZIP-Datei hochladen und den Skill aktivieren.

Die ZIP-Datei muss den vollständigen Skill-Ordner enthalten:

```text
ecom-reel.zip
└── ecom-reel/
    ├── SKILL.md
    └── references/
```

### Claude Code – alle Skills installieren

```bash
git clone https://github.com/kontakt-ecomfabrik/onlineshop-instagram-skills.git
mkdir -p ~/.claude/skills
cp -R onlineshop-instagram-skills/ecom-* ~/.claude/skills/
```

### Codex – alle Skills installieren

```bash
git clone https://github.com/kontakt-ecomfabrik/onlineshop-instagram-skills.git
mkdir -p ~/.agents/skills
cp -R onlineshop-instagram-skills/ecom-* ~/.agents/skills/
```

Bei einem privaten Repository ist ein angemeldeter GitHub-Zugang erforderlich.

## Die sieben Skills

| Skill | Aufgabe |
| --- | --- |
| [`ecom-content`](ecom-content/) | Zentraler Content-Router für gemischte Anfragen. Wählt den passenden Workflow und verbindet Produkt, Zielgruppe, Kaufphase und Content-Ziel. |
| [`ecom-content-strategy`](ecom-content-strategy/) | Entwickelt realistische Instagram-Strategien mit Zielen, Customer Journey, Content-Säulen, Prioritäten, Frequenz und Messung. |
| [`ecom-content-ideas`](ecom-content-ideas/) | Erstellt konkrete, nicht generische Ideen aus Produkten, Kundenfragen, Einwänden, Bewertungen und Kaufphasen. |
| [`ecom-reel`](ecom-reel/) | Erstellt produktbezogene Reels mit Hooks, Skript, Szenen, gesprochenem Text, On-Screen-Text, CTA und Faceless-Variante. |
| [`ecom-carousel`](ecom-carousel/) | Erstellt kompakte Carousels für Produktwissen, Vergleiche, FAQs, Einwände, Kaufhilfen und Checklisten. |
| [`ecom-story`](ecom-story/) | Erstellt kurze Story-Sequenzen für Produkte, Launches, Umfragen, FAQs, Social Proof, Angebote und Behind-the-Scenes. |
| [`ecom-caption`](ecom-caption/) | Schreibt natürliche Captions, die einen Post ergänzen, statt sichtbare Inhalte nur zu wiederholen. |

## Welchen Skill soll ich verwenden?

| Wenn du … | Nutze … |
| --- | --- |
| noch nicht weißt, welches Format sinnvoll ist | `ecom-content` |
| eine langfristige Richtung oder einen Monatsplan brauchst | `ecom-content-strategy` |
| zuerst konkrete Themen und Hooks sammeln möchtest | `ecom-content-ideas` |
| ein Kurzvideo erstellen möchtest | `ecom-reel` |
| Wissen oder Vergleiche auf Slides erklären möchtest | `ecom-carousel` |
| eine kurze tägliche oder interaktive Sequenz brauchst | `ecom-story` |
| bereits einen Post hast und die Caption fehlt | `ecom-caption` |

**Empfehlung:** Installiere alle sieben Skills. Verwende `ecom-content` als Einstieg, wenn du das passende Format noch nicht festgelegt hast.

## Beispiel-Prompts

Die folgenden Beispiele verwenden den direkten Aufruf in **Claude Code** mit `/`. In **Codex** ersetzt du den Schrägstrich durch `$`, zum Beispiel `$ecom-reel`. In Claude im Browser aktivierst du den Skill und verwendest den restlichen Prompt ohne die erste Befehlszeile.

### Strategie

```text
/ecom-content-strategy

Ich betreibe einen Onlineshop für [PRODUKT/KATEGORIE].
Meine Zielgruppe ist [ZIELGRUPPE].
Mein wichtigstes Ziel für die nächsten 30 Tage ist [ZIEL].

Entwickle eine realistische Instagram-Strategie.
Frage nur nach Informationen, die das Ergebnis wesentlich verändern.
Kennzeichne Annahmen deutlich.
```

### Content-Ideen

```text
/ecom-content-ideas

Erstelle zehn konkrete Instagram-Ideen für [PRODUKT].
Berücksichtige Kundenfragen, Kaufbarrieren, Nutzung und Kundenbindung.
Vermeide austauschbare Tipps, die genauso für Coaches passen würden.
```

### Reel

```text
/ecom-reel

Erstelle ein 20-sekündiges Reel für [PRODUKT].
Zielgruppe: [ZIELGRUPPE]
Kundenfrage oder Einwand: [FRAGE]
Verfügbares Material: [PRODUKTVIDEO/FOTOS/TALKING HEAD]
Ziel: [REICHWEITE/VERTRAUEN/KAUF]

Liefere drei Hooks, das finale Skript, On-Screen-Text,
eine Szenenliste und einen passenden CTA.
```

### Carousel

```text
/ecom-carousel

Erstelle ein Instagram-Carousel mit maximal fünf Slides zum Thema [THEMA].
Nutze höchstens drei kurze Zeilen pro Slide.
Die letzte Slide soll eine klare Handlung oder Frage enthalten.
```

### Story

```text
/ecom-story

Erstelle eine Story-Sequenz mit drei bis fünf Frames für [PRODUKT/ANLASS].
Ziel: [ZIEL]
Verfügbares Bildmaterial: [MATERIAL]
Nutze nur dann einen Sticker, wenn die Antwort wirklich weiterverwendet wird.
```

### Caption

```text
/ecom-caption

Schreibe eine natürliche Caption für diesen bestehenden Post:
[INHALT DES POSTS]

Die Caption soll einen neuen Gedanken ergänzen und den Post nicht wiederholen.
Ton: ehrlich, direkt, ruhig und fachlich.
```

## Wie die Skills arbeiten

1. Der Shop, das Produkt und die Zielgruppe werden eingeordnet.
2. Die relevante Kundenfrage oder Kaufbarriere wird bestimmt.
3. Der Inhalt erhält eine klare Aufgabe innerhalb der Customer Journey.
4. Nur passende Fakten und verfügbare Belege werden verwendet.
5. Das Ergebnis wird im geeigneten Format ausgegeben.
6. Annahmen, fehlende Nachweise oder offene Produktinformationen werden transparent gekennzeichnet.

## Was die Skills nicht tun

- Sie veröffentlichen nicht automatisch auf Instagram.
- Sie liken, kommentieren, folgen oder versenden keine automatischen DMs.
- Sie erfinden keine Produkteigenschaften, Bewertungen, Zahlen oder Kundenergebnisse.
- Sie ersetzen keine fachliche, rechtliche oder werbliche Prüfung.
- Sie garantieren weder Reichweite noch Verkäufe.
- Sie greifen ohne zusätzliche Tools nicht auf Instagram-Konten oder Shop-Daten zu.

## Ordnerstruktur

```text
onlineshop-instagram-skills/
├── ecom-content/
│   ├── SKILL.md
│   └── references/
├── ecom-content-strategy/
│   ├── SKILL.md
│   └── references/
├── ecom-content-ideas/
│   ├── SKILL.md
│   └── references/
├── ecom-reel/
│   ├── SKILL.md
│   └── references/
├── ecom-carousel/
│   ├── SKILL.md
│   └── references/
├── ecom-story/
│   ├── SKILL.md
│   └── references/
├── ecom-caption/
│   ├── SKILL.md
│   └── references/
├── INSTALLATION.md
└── README.md
```

Jeder Skill besteht aus einer `SKILL.md` mit Anweisungen und einem Ordner `references/` mit den dazugehörigen Arbeitsgrundlagen.

## Hinweise zur Nutzung

Gute Ergebnisse hängen von guten Ausgangsinformationen ab. Hilfreich sind insbesondere:

- Produkt und nachweisbare Merkmale
- Zielgruppe und Nutzungssituation
- häufige Kundenfragen oder Einwände
- vorhandene Bilder, Videos und Bewertungen
- aktuelles Geschäftsziel
- bereits veröffentlichte Inhalte

Wenn Informationen fehlen, fragen die Skills gezielt nach oder arbeiten mit klar gekennzeichneten Annahmen.

## Autorin

Erstellt von **Dr. Kenanah Shereih** für **EcomFabrik**.

- Website: [ecomfabrik.de](https://ecomfabrik.de)
- Instagram: [@ecom_fabrik.de](https://www.instagram.com/ecom_fabrik.de/)

Für Onlineshops mit Vision – Content, SEO, Ads und KI strategisch nutzen.
