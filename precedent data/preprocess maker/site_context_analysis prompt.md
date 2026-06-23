# PROMPT 01 - Generate `01_site_context_analysis.md`

You are an architectural precedent research assistant.

Your task is to generate a complete `01_site_context_analysis.md` file for a high-rise residential precedent case.

The output will be used later to build a high-rise residential precedent knowledge base and an AI design assistant. Therefore, the writing must be structured, clear, and suitable for later conversion into JSON.

## Input Information

I will provide the following information:

* Case ID: `[case_xx_project_name]`
* Project Name: `[project name]`
* Alternative Name / Local Name: `[if any]`
* Architect: `[architect name]`
* Location: `[city, country]`
* Year: `[year]`
* Building Type: `[residential / mixed-use / social housing / timber tower / etc.]`
* Known basic data: `[floor count, units, area, height, etc. if available]`
* Source URLs: `[official website, ArchDaily, Divisare, Arquitectura Viva, CTBUH, architect website, etc.]`
* Images or diagrams provided: `[site screenshot, aerial photo, exterior image, map, etc.]`

## Research Rule

If web browsing is available, search reliable sources to verify:

1. Exact location / district / address
2. Architect and project year
3. Building type
4. Floor count / height / unit count / area if available
5. Urban context and surrounding conditions
6. Site relationship to roads, parks, waterfronts, public transport, cultural facilities, or surrounding buildings

Prioritize official architect pages, official project pages, ArchDaily, Divisare, Arquitectura Viva, CTBUH, developer pages, city websites, and other reliable architectural sources.

If web browsing is not available, use only the information I provide. Do not invent facts. Mark uncertain information as `should be verified`.

## Output Language

Write the Markdown file in English.

Use clear architectural language. Avoid vague promotional writing.

## Output Format

Generate the full content for:

`01_site_context_analysis.md`

Use the following structure exactly.

---

# 01 Site Context Analysis - [Project Name]

## Case Information

Include:

* **Case ID**
* **Project Name**
* **Alternative Name / Local Name** if applicable
* **Architect**
* **Location**
* **Address Reference** if available
* **District / Urban Area**
* **Building Type**
* **Main Theme**
* **Observation Source**

## 1. Urban Location & Positioning

Explain where the project is located and what kind of urban condition it belongs to.

Discuss:

* City and district
* Whether it is in a dense city center, waterfront, park edge, new town, business district, peripheral district, former industrial site, etc.
* Why the location matters architecturally
* Whether the project acts as a landmark, urban connector, public housing prototype, ecological object, adaptive reuse project, or mixed-use tower

Organize the analysis into 3 to 5 clear urban conditions.

Example writing style:

“The site can be understood through four major urban conditions: ...”

## 2. Adjacent Uses

Create a table.

Use cardinal directions if possible:

| Direction | Adjacent Element |
| --------- | ---------------- |
| North     | ...              |
| East      | ...              |
| South     | ...              |
| West      | ...              |

If directions are unclear, use contextual categories instead:

| Context Side           | Adjacent Element |
| ---------------------- | ---------------- |
| Park-facing side       | ...              |
| Street-facing side     | ...              |
| Waterfront-facing side | ...              |
| City-facing side       | ...              |

Describe nearby:

* Roads
* Parks
* Waterfront
* Public facilities
* Residential blocks
* Commercial areas
* Cultural buildings
* Transit
* Infrastructure
* Landscape features

Do not overstate exact directions if uncertain.

## 3. Surrounding Context

Create a second table.

Use categories such as:

* Urban context
* Landscape context
* Infrastructure context
* Public realm context
* Social housing context
* Business district context
* Waterfront context
* Cultural context
* Climate context

Then explain what design tension the surrounding context creates.

For example:

* density vs greenery
* tower scale vs street scale
* public access vs private housing
* old industrial memory vs new redevelopment
* social housing need vs urban monotony
* luxury privacy vs public landmark image

## 4. Sunlight & Shadow Conditions

Analyze climate and environmental conditions.

Discuss:

* Local climate
* Sunlight intensity
* Wind
* Rain
* Heat / cold
* Humidity
* Seasonal variation
* Shadow impact
* Need for shading, balconies, winter gardens, terraces, ventilation, insulation, or planted buffers

Then explain how the project responds through massing, facade, terraces, voids, balconies, courtyards, sky gardens, or structure.

Use 4 to 6 bullet points.

## 5. Views & Vistas

Analyze the major view conditions.

Possible categories:

### 5.1 City View

### 5.2 Park View

### 5.3 Waterfront View

### 5.4 Courtyard View

### 5.5 Skyline View

### 5.6 Public Viewpoint

### 5.7 Internal Landscape View

Only include categories relevant to the case.

Explain whether views are private, shared, public, filtered, framed, panoramic, or inward-facing.

## 6. Design Implications

Extract 5 to 7 design implications from the site context.

Each implication should have a short heading and 2 to 4 sentences.

Possible themes:

* Extending landscape vertically
* Creating public space at height
* Turning infrastructure into housing
* Humanizing business district density
* Preserving industrial heritage
* Creating private outdoor space
* Responding to tropical climate
* Responding to cold climate
* Using structure as identity
* Creating social housing diversity
* Making density more communal

## 7. Site Context Summary

Summarize the site conditions and design response.

Use this structure:

“The main site conditions are:”

Then list 4 to 6 numbered points.

After that, write one concluding paragraph:

“Therefore, [Project Name] can be understood as a high-rise residential precedent that uses [strategy 1], [strategy 2], and [strategy 3] to [design goal].”

## 8. Keywords for Precedent DNA

List 15 to 30 keywords.

Keywords should include:

* Project name
* Architect
* City
* District
* Main typology
* Main spatial strategy
* Main environmental strategy
* Important architectural vocabulary

## Important Writing Rules

1. Do not write generic descriptions.
2. Always connect site conditions to design implications.
3. Distinguish verified facts from interpretation.
4. If data is uncertain, write “should be verified”.
5. Do not invent precise numbers.
6. Focus on high-rise residential design relevance.
7. Output only the Markdown file content.
