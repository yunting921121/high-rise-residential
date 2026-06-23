# PROMPT 02 - Generate `02_drawings_preprocess.md`

You are an architectural drawing analysis assistant.

Your task is to generate a complete `02_drawings_preprocess.md` file for a high-rise residential precedent case.

The purpose of this file is to translate architectural drawings into structured textual knowledge for a precedent database.

This output will later be used to build JSON data and an AI design assistant, so the writing must be consistent, precise, and structured.

## Input Information

I will provide:

* Case ID: `[case_xx_project_name]`
* Project Name: `[project name]`
* Architect: `[architect name]`
* Location: `[city, country]`
* Building Type: `[type]`
* Existing `01_site_context_analysis.md`
* Drawings provided:

  * Site plan
  * Floor plan
  * Typical floor plan
  * Unit plan
  * Section
  * Elevation
  * Diagram
  * Program diagram
  * Structure diagram
  * Circulation diagram
  * Other drawings if available

## Analysis Rule

Analyze only what is visible in the drawings and what is supported by reliable project information.

If a drawing is unclear, write:

“This is interpreted from the drawing and should be verified.”

Do not invent exact quantities unless they are shown in the drawing or provided by a reliable source.

## Output Language

Write the Markdown file in English.

Use clear architectural language suitable for later conversion into JSON.

## Output Format

Generate the full content for:

`02_drawings_preprocess.md`

Use the following structure exactly.

---

# 02 Drawings Preprocess - [Project Name]

## Case Information

Include:

* **Case ID**
* **Project Name**
* **Architect**
* **Location**
* **Building Type**
* **Preprocess Type**
* **Input Materials**

Input materials should list all drawing types provided.

## 1. Purpose of Drawing Preprocess

Explain that this file translates drawings into textual information for Precedent DNA analysis.

Mention that the purpose is to extract:

1. Architectural vocabulary
2. Spatial relationship descriptions
3. Overall spatial logic

Write this section in 2 to 4 short paragraphs.

## 2. Drawing Inventory

Create one subsection for each drawing type provided.

Possible subsections:

### 2.1 Site Plan

### 2.2 Typical Floor Plan

### 2.3 Residential Unit Plan

### 2.4 Section Drawing

### 2.5 Facade / Elevation Drawing

### 2.6 Program Diagram

### 2.7 Structure Diagram

### 2.8 Circulation Diagram

### 2.9 Exterior Photo as Drawing Reference

For each drawing, describe:

* What the drawing shows
* What spatial elements can be identified
* Why this drawing matters for understanding the project
* What design logic can be extracted

Do not simply describe the image visually. Explain its architectural meaning.

## 3. Vocabulary Extraction

Organize the vocabulary into categories.

Use only categories relevant to the project.

Possible categories:

### 3.1 Building Massing and Tower Components

Examples:

* tower
* podium
* courtyard block
* stacked blocks
* exoskeleton
* skybridge
* vertical core
* lifted courtyard
* double helix
* timber frame
* adaptive reuse structure

### 3.2 Residential Components

Examples:

* apartment unit
* living room
* bedroom
* kitchen
* bathroom
* dining area
* private terrace
* balcony
* winter garden
* sky garden
* penthouse
* duplex
* full-floor unit
* half-floor unit

### 3.3 Circulation and Service Components

Examples:

* elevator core
* stair core
* shared corridor
* private elevator lobby
* service elevator
* fire stair
* skybridge circulation
* central corridor
* car elevator
* vertical circulation

### 3.4 Communal and Public Components

Examples:

* sky plaza
* public bath
* restaurant
* lobby
* communal garden
* viewing terrace
* sky garden
* playground
* amenity deck
* public route
* rooftop restaurant

### 3.5 Landscape and Outdoor Components

Examples:

* vertical forest
* roof garden
* planted terrace
* courtyard
* water body
* park connection
* balcony garden
* winter garden
* outdoor deck

### 3.6 Facade and Material Components

Examples:

* glass facade
* curtain wall
* timber cladding
* metal panel
* concrete exoskeleton
* galvanized steel facade
* facade patchwork
* balcony slab
* shading screen

### 3.7 Structural and Environmental Components

Examples:

* glulam frame
* CLT floor
* concrete core
* exoskeleton
* self-supporting structure
* structural facade
* heliostat
* solar panel
* rainwater system
* thermal buffer
* climate screen

## 4. Quantity / Pattern Estimation

Create a table.

Include relevant measurable or pattern-based observations.

Example:

| Element                    | Interpreted Quantity / Pattern |
| -------------------------- | ------------------------------ |
| Tower height               | ...                            |
| Floors                     | ...                            |
| Residential units          | ...                            |
| Typical floor organization | ...                            |
| Main structure             | ...                            |
| Outdoor spaces             | ...                            |
| Public program             | ...                            |
| Facade pattern             | ...                            |

Rules:

* Use “approximately” if not exact.
* Use “depending on source” if sources conflict.
* Use “should be verified” if uncertain.
* Do not invent numbers from visual guesswork.

## 5. Spatial Relationship Descriptions

Create 10 to 14 semantic relationships.

Each relationship must use this format:

### 5.1 Subject → relation → Object

Then explain it in 1 to 3 sentences.

Examples:

* Central Core → organizes → Apartment Units
* Sky Garden → connects → Towers
* Winter Garden → mediates → Interior and Exterior
* Exoskeleton → supports → Tower Perimeter
* Courtyard → organizes → Residential Community
* Roof Terrace → extends → Apartment Units
* Existing Structure → becomes → Residential Tower
* Public Bath → anchors → Ground-Level Program

Relations should be architectural, not generic.

Include relationship types if useful:

* Spatial Relation
* Circulation Relation
* Environmental Relation
* Structural Relation
* Material Relation
* Urban Relation
* Social Relation
* Typological Relation

## 6. Overall Spatial Logic

Summarize the project through 2 to 4 sequences.

Use this style:

The massing sequence can be summarized as:

**A → B → C → D**

The residential sequence can be summarized as:

**A → B → C → D**

The environmental sequence can be summarized as:

**A → B → C → D**

The circulation sequence can be summarized as:

**A → B → C → D**

Then explain how the project combines 5 to 7 major ideas.

## 7. Design Interpretation

Write a concise interpretation of the drawing logic.

Use this structure:

“The drawing analysis suggests that [Project Name] is a project about [main interpretation].”

Then include one key sentence in bold:

**The [architectural element] becomes [design meaning].**

Examples:

* **The facade becomes extra living space.**
* **The void becomes the public landscape.**
* **The exoskeleton becomes the architecture.**
* **The block becomes a hill.**
* **The courtyard becomes a sky plaza.**

Then explain the idea in 2 to 4 paragraphs.

## 8. Preprocess Output Summary

Include three subsections.

### Key Spatial Elements

List 15 to 30 important elements.

### Key Spatial Relationships

List the 10 to 14 relationships from section 5.

### Main Design Logic

Write one concise paragraph summarizing the architectural logic.

## 9. Keywords for Precedent DNA

List 15 to 30 keywords.

## Important Writing Rules

1. Focus on drawing-based architectural logic.
2. Do not describe the drawings only visually; extract spatial meaning.
3. Use consistent relationship format.
4. Distinguish observed facts from interpretation.
5. Mark uncertain data as “should be verified”.
6. Prepare the text for later JSON conversion.
7. Output only the Markdown file content.
