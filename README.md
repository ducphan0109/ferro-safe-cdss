# 🧬 FERRO-SAFE v1.0: Multidisciplinary Clinical Decision Support System for Intravenous Iron Therapy in Restless Legs Syndrome

**FERRO-SAFE** is an open-source, evidence-synthesized Clinical Decision Support System (CDSS) designed to operationalize biomarker-guided patient selection, **6-H Syndrome** (*intact FGF23-mediated hypophosphatemia*) risk stratification, and post-infusion diagnostic de-confounding in patients with Restless Legs Syndrome (RLS) receiving intravenous (IV) iron therapy.

## 📚 Foundational Evidence Base
This clinical software directly operationalizes the translational frameworks established in:
1. **Phan DM** (2027). *Beyond the neurological horizon: A metabolic paradigm shift in intravenous iron therapy for restless legs syndrome*. **Sleep Medicine**, 149, 109324. https://doi.org/10.1016/j.sleep.2026.109324
2. **Phan DM**, Lam MY, Trang MN (2026). *Iron therapy & restless legs syndrome: a narrative review*. **Sleep and Breathing**, 30(4), 202. https://doi.org/10.1007/s11325-026-03738-4

## ⚙️ Three-Stage Algorithmic Architecture
* **Module 1 (Step 1 — Initiation & Hidden Responder Engine):** Evaluates IRLSSG severity, scans the serum ferritin "gray zone" ($75\text{--}300\ \mu\text{g/L}$) using transferrin saturation ($\text{TSAT} \le 35\%$), predicts phenotype-specific responder probabilities, and enforces the minimum effective adult IV iron dose gate ($\ge 1000\text{ mg}$).
* **Module 2 (Step 2 & 3 — `FERRO-6H-RISK` Triage & Formulation Pathway):** Enforces a hard-stop contraindication gate for baseline hypophosphatemia ($\text{PO}_4 < 2.5\text{ mg/dL}$), calculates the 0–15 point composite `FERRO-6H-RISK` index based on osteocyte DMP1-integrin blockade intensity and the renal eGFR filtration paradox, and routes patients to **Pathway A** (FDI, Ferumoxytol, LMW ID) or **Pathway B** (mandatory Weeks 2–3 surveillance).
* **Module 3 (Post-Infusion Diagnostic De-confounder):** Differentiates iatrogenic 6-H hypophosphatemic myopathy/osteomalacia from true RLS relapse/dopaminergic augmentation and physiological delayed CNS iron repletion ($< 12\text{ weeks}$).

## 👨🔬 Author & Affiliation
Duc Minh Phan

Faculty of Medicine, Hong Bang International University, Ho Chi Minh City, Viet Nam

Email: ducpm@hiu.vn

## 🚀 Local Installation & Execution
```bash
pip install -r requirements.txt
streamlit run app.py


