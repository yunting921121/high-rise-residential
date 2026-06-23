# High-Rise-Residential: Building a Case-Based Knowledge System and Applying it in Design Practice
# 組員名單 
王韻婷<br>于皓<br>莊書豪
# 案例主題 
高層集合住宅
## Project Overview
本專案旨在建構一套專為「高層集合住宅」量身打造的 AI 設計輔助工作流。透過結構化分析 20 個經典建築案例，將非結構化的圖紙與文本轉化為機器可讀的知識庫，並將其封裝為自訂的 AI 設計助理 (Gem)。該助理的核心目標並非直接生成最終的建築專案提案，而是協助設計者釐清設計概念，將其解構為具備層級化的空間策略、設計規則與組織邏輯，作為設計推進過程中的智慧副駕駛。

## Project Workflow

### Part 1. Establishing the AI Consultant

#### Step 1 — Build the AI knowledge base
蒐集與初步建檔：人為蒐集 20 個高層集合住宅的指標性案例。針對每個案例，手動彙整其基本資料、建築平立剖圖面、外觀與室內照片，以及相關的文字敘述說明，並將這些原始資料初步結構化整理於 Excel 檔案中（如 `高層集合住宅案例整理.xlsx`），作為後續 AI 處理的原始素材。

#### Step 2 — Write prompts to instruct the AI
多層次 AI 案例萃取**：撰寫三段式、遞進式的 AI Prompts，引導語言模型將前一步驟的圖文資料轉化為結構化的建築知識，並輸出為 Markdown 檔案：
* Prompt 01 (Site Context Analysis)：解析都市涵構與基地環境特徵。
* Prompt 02 (Drawings Preprocess)：解析建築平立剖面圖等圖紙中的空間語彙與組織邏輯。
* Prompt 03 (Photos & Renders Preprocess)：詮釋視覺圖像中的空間氛圍、材質構築與設計意圖。

#### Step 3 — Define the expected output format
資料庫結構化與打包：確保 AI 萃取的 Markdown 分析內容格式統一後，於 VS Code 開啟終端機，執行 Python 腳本（例如 `python scripts/merge_cases.py`）。此步驟將 20 個獨立案例的分析結果，編譯並整合為單一且機器可讀的 JSON 格式資料庫（`highrise_precedent_database.json`），完成底層知識庫的建置。

---

### Part 2. Building the AI Co-designer

#### Step 1 — Set up all required AI consultants
建立專屬 AI 設計助理：在 Gemini 平台中建立一個全新的自訂 Gem（High-Rise Residential Design Assistant）。將 Part 1 完成的 JSON 案例資料庫作為該助理的核心背景知識。

#### Step 2 — Define Logic and Constraints
匯入系統指令與推導邏輯：撰寫並匯入 `gem_instructions.md` 系統指令檔案。此指令嚴格規範了 AI 的角色邊界與思考路徑，確保 AI 能夠準確檢索 `Gene_A` 到 `Gene_D` 的案例基因結構。系統指令要求 AI 在給予反饋時，必須從建築設計推理的角度出發，提供策略與規則，而非單純的資料羅列。

#### Step 3 — Empirical Verification and Application
實務對話與驗證：透過實際啟動對話進行測試。使用者可上傳設計草圖、平面圖或提出特定的設計挑戰（如：如何處理高密度環境下的垂直綠化），AI 助理將根據底層的案例知識庫進行比對，並回饋具體的空間策略建議與設計參考，正式完成高層住宅設計輔助工作流的閉環。