import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# ==============================================================================
# CLINICAL DECISION SUPPORT SYSTEM (CDSS) CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="FERRO-SAFE | Clinical Decision Support System for RLS IV Iron Therapy",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Academic / Clinical Neurology Grade Interface
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }
    .clinical-header {
        background-color: #0f172a;
        color: #f8fafc;
        padding: 1.4rem 1.75rem;
        border-radius: 6px;
        border-left: 6px solid #0284c7;
        margin-bottom: 1.25rem;
    }
    .clinical-header h1 {
        color: #f8fafc;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 1.65rem;
        font-weight: 700;
        margin: 0 0 0.35rem 0;
        letter-spacing: -0.01em;
    }
    .clinical-header p {
        color: #cbd5e1;
        font-size: 0.95rem;
        margin: 0;
        font-weight: 400;
    }
    .panel-title {
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #334155;
        border-bottom: 1px solid #cbd5e1;
        padding-bottom: 0.4rem;
        margin-bottom: 0.8rem;
    }
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #cbd5e1;
        padding: 0.75rem 1rem;
        border-radius: 6px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 2px solid #e2e8f0;
    }
    .stTabs [data-baseweb="tab"] {
        height: 44px;
        background-color: #f1f5f9;
        border-radius: 4px 4px 0 0;
        padding: 0 18px;
        font-weight: 600;
        color: #475569;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0f172a !important;
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================================================================
# SIDEBAR: ACADEMIC METADATA & EVIDENCE PROVENANCE
# ==============================================================================
with st.sidebar:
    st.markdown("### **FERRO-SAFE CDSS (v1.0)**")
    st.caption(
        "Multidisciplinary Clinical Decision Support System for Intravenous Iron Therapy "
        "in Restless Legs Syndrome (Willis–Ekbom Disease)"
    )
    st.divider()

    st.markdown("**Principal Investigator & Developer**")
    st.markdown("**Duc Minh Phan**")
    st.caption(
        "Faculty of Medicine, Hong Bang International University, "
        "215 Dien Bien Phu Street, Gia Dinh Ward, Ho Chi Minh City, Viet Nam"
    )
    st.caption(
        "ORCID: "
        "0009-0006-1985-178X"
    )
    st.markdown(
        "**Correspondence:**\n\n"
        "- `ducpm@hiu.vn`\n"
        "- `tommyphan9911@gmail.com`"
    )
    st.divider()

    st.markdown("**Primary Peer-Reviewed Evidence Base**")
    st.markdown(
        "1. **Phan DM** (2027). Beyond the neurological horizon: A metabolic paradigm shift "
        "in intravenous iron therapy for restless legs syndrome. *Sleep Medicine*, 149, 109324. "
        "[doi:10.1016/j.sleep.2026.109324](https://doi.org/10.1016/j.sleep.2026.109324)\n\n"
        "2. **Phan DM**, Lam MY, Trang MN (2026). Iron therapy & restless legs syndrome: "
        "a narrative review. *Sleep and Breathing*, 30(4), 202. "
        "[doi:10.1007/s11325-026-03738-4](https://doi.org/10.1007/s11325-026-03738-4)"
    )
    st.divider()

    st.caption(
        "**Clinical Governance Notice:** This deterministic, evidence-synthesized clinical decision "
        "support tool is intended for licensed healthcare professionals and clinical researchers. "
        "It does not supersede individualized clinical judgment or institutional protocols."
    )

# ==============================================================================
# MAIN CLINICAL HEADER
# ==============================================================================
st.markdown(
    """
    <div class="clinical-header">
        <h1>FERRO-SAFE: Multidisciplinary Clinical Decision Support for RLS Intravenous Iron Therapy</h1>
        <p>Operationalizing Biomarker-Guided Patient Selection, Intact FGF23 (6-H Syndrome) Metabolic Risk Stratification, and Post-Infusion Diagnostic De-confounding</p>
    </div>
    """,
    unsafe_allow_html=True
)

tab1, tab2, tab3, tab4 = st.tabs([
    "MODULE 1: Indication & Responder Prediction",
    "MODULE 2: 6-H Syndrome Risk & Formulation Triage",
    "MODULE 3: Post-Infusion Diagnostic De-confounder",
    "MODULE 4: Evidence Matrix & In-Silico Validation"
])

# ==============================================================================
# MODULE 1: STEP 1 - BIOMARKER INDICATION & HIDDEN RESPONDER ENGINE
# ==============================================================================
with tab1:
    st.markdown("#### **Step 1: Initiation, Biomarker Gatekeeper, and Therapeutic Response Prediction**")
    st.caption(
        "Evaluates clinical eligibility for intravenous (IV) iron replacement according to AASM 2025 / IRLSSG "
        "directives and identifies functional iron deficiency ('hidden responders') within the serum ferritin "
        "gray zone (75–300 µg/L) via transferrin saturation (TSAT ≤ 35%)."
    )

    col1_a, col1_b = st.columns([1, 1.15], gap="large")

    with col1_a:
        st.markdown('<div class="panel-title">1. Baseline Clinical & Laboratory Parameters</div>', unsafe_allow_html=True)

        irls_score = st.slider(
            "Baseline IRLSSG Severity Rating Scale Score (0–40 points):",
            min_value=0, max_value=40, value=24, step=1,
            help="IRLSSG severity strata: Mild (1–10), Moderate (11–20), Severe (21–30), Very Severe (31–40). "
                 "Clinical trials and guidelines primarily endorse IV iron for moderate-to-severe RLS (IRLS ≥ 15)."
        )

        ferritin = st.number_input(
            "Baseline Serum Ferritin (µg/L):",
            min_value=1.0, max_value=1000.0, value=120.0, step=5.0,
            help="Oral iron absorption is physiologically restricted by hepcidin when serum ferritin exceeds 75 µg/L "
                 "(Allen et al., 2018; Winkelman et al., 2025)."
        )

        tsat = st.number_input(
            "Baseline Transferrin Saturation — TSAT (%):",
            min_value=1.0, max_value=100.0, value=28.0, step=1.0,
            help="Multivariable logistic regression demonstrates %TSAT is an independent predictor of IV iron "
                 "response (OR = 0.955, 95% CI: 0.913–0.998, p = 0.040; Park et al., 2020; Phan et al., 2026)."
        )

        rls_phenotype = st.selectbox(
            "Primary Clinical RLS Etiology / Subpopulation:",
            [
                "Primary / Idiopathic RLS (Baseline responder benchmark: 64.7%–80.8%)",
                "RLS with Iron Deficiency Anemia — IDA (Responder benchmark: 91.3%)",
                "Post-Gastrectomy / GI Malabsorption RLS (Responder benchmark: 90.9%)",
                "Hemodialysis / ESRD-Associated RLS (Responder benchmark: ~78.0%)",
                "Pediatric RLS / PLMD — Age < 18 Years (Responder benchmark: 78.1%)",
                "RLS with Comorbid Lumbosacral Radiculopathy (Responder benchmark: 39.3%)"
            ]
        )

        oral_intolerance = st.checkbox(
            "Documented intolerance, malabsorption, or inadequate response to oral iron / α₂δ ligands",
            value=True
        )
        active_augmentation = st.checkbox(
            "Active dopaminergic augmentation (on chronic pramipexole, ropinirole, or rotigotine)",
            value=False
        )

    with col1_b:
        st.markdown('<div class="panel-title">2. Algorithmic Stratification & Dosing Directives</div>', unsafe_allow_html=True)

        if irls_score == 0:
            severity_str = "Asymptomatic (0 pts)"
        elif irls_score <= 10:
            severity_str = "Mild Severity (1–10 pts)"
        elif irls_score <= 20:
            severity_str = "Moderate Severity (11–20 pts)"
        elif irls_score <= 30:
            severity_str = "Severe RLS (21–30 pts)"
        else:
            severity_str = "Very Severe RLS (31–40 pts)"

        is_pediatric = "Pediatric" in rls_phenotype
        eligible_severity_or_intolerance = (irls_score >= 15) or oral_intolerance

        # Compute Phenotype Responder Rate
        phenotype_map = {
            "Primary / Idiopathic RLS (Baseline responder benchmark: 64.7%–80.8%)": (
                72.8, "64.7% (single 1000 mg infusion; Park et al., 2020) to 80.8% (repeated dosing; Park et al., 2022)"
            ),
            "RLS with Iron Deficiency Anemia — IDA (Responder benchmark: 91.3%)": (
                91.3, "91.3% (single dose; Park et al., 2020) and 81.8% (repeated maintenance; Park et al., 2022)"
            ),
            "Post-Gastrectomy / GI Malabsorption RLS (Responder benchmark: 90.9%)": (
                90.9, "90.9% (single dose; Park et al., 2020) and 80.0% (repeated maintenance; Park et al., 2022)"
            ),
            "Hemodialysis / ESRD-Associated RLS (Responder benchmark: ~78.0%)": (
                78.0, "Significant IRLS reduction with IV Iron Sucrose 1000 mg (-7.38 vs -0.81 placebo, p < 0.001; Deng et al., 2017)"
            ),
            "Pediatric RLS / PLMD — Age < 18 Years (Responder benchmark: 78.1%)": (
                78.1, "78.05% RLS symptom response and significant PLMS reduction (Dye et al., 2017; DelRosso et al., 2021)"
            ),
            "RLS with Comorbid Lumbosacral Radiculopathy (Responder benchmark: 39.3%)": (
                39.3, "39.3% responder rate; attenuated efficacy due to concurrent radicular pathology (Park et al., 2020)"
            )
        }
        base_prob, prob_desc = phenotype_map[rls_phenotype]

        adjusted_prob = base_prob
        if tsat <= 35 and ferritin < 300:
            adjusted_prob = min(96.0, adjusted_prob + 6.5)
        if active_augmentation:
            adjusted_prob = max(25.0, adjusted_prob - 18.0)

        m1_c1, m1_c2 = st.columns(2)
        m1_c1.metric("IRLSSG Clinical Stratum", f"{irls_score}/40 pts", severity_str)
        m1_c2.metric("Predicted IV Iron Responder Rate", f"{adjusted_prob:.1f}%", "≥ 40% IRLS Score Reduction")
        st.caption(f"**Subpopulation Evidence Benchmark:** {prob_desc}.")

        # Decision Logic for Oral vs IV Iron
        if (75 <= ferritin < 300) and (tsat <= 35) and eligible_severity_or_intolerance and (irls_score > 0):
            st.success(
                "**CLINICAL DIRECTIVE: INTRAVENOUS IRON INDICATED — 'HIDDEN RESPONDER' IN FERRITIN GRAY ZONE**\n\n"
                "- **Biomarker Evaluation:** Serum ferritin resides in the borderline 'gray zone' (**75–300 µg/L**), "
                "where reliance on ferritin alone frequently results in clinical undertreatment.\n"
                "- **Secondary Biomarker Trigger:** **TSAT ≤ 35%** confirms functional iron deficiency and "
                "independently predicts a favorable therapeutic response to IV iron (**OR = 0.955, 95% CI: 0.913–0.998, "
                "p = 0.040**; Park et al., 2020; Phan et al., 2026; Phan, 2027)."
            )
            indication_status = "IV Iron Indicated (Hidden Responder)"
        elif (ferritin < 100 or (ferritin < 300 and tsat <= 45)) and eligible_severity_or_intolerance and (irls_score > 0):
            st.success(
                "**CLINICAL DIRECTIVE: STANDARD GUIDELINE INDICATION FOR INTRAVENOUS IRON**\n\n"
                "- **Biomarker Evaluation:** Meets AASM 2025 and IRLSSG consensus thresholds (**Ferritin < 100 µg/L**, "
                "or **Ferritin 100–300 µg/L with TSAT ≤ 45%**) in a patient with moderate-to-severe symptoms "
                "(**IRLS ≥ 15**) or documented intolerance/refractoriness to oral iron (Winkelman et al., 2025; "
                "Allen et al., 2018).\n"
                "- **Predictive Nuance:** If baseline TSAT lies between **36% and 45%**, IV iron remains guideline-supported, "
                "though expected therapeutic magnitude is more pronounced when **TSAT ≤ 35%** (Phan et al., 2026)."
            )
            indication_status = "IV Iron Indicated (Standard Criteria)"
        elif (ferritin <= 75 or (is_pediatric and ferritin < 50)) and (not oral_intolerance) and (0 < irls_score < 15):
            st.info(
                "**CLINICAL DIRECTIVE: FIRST-LINE ORAL IRON SUPPLEMENTATION TRIAL**\n\n"
                "- **Physiological Rationale:** Baseline serum ferritin is **≤ 75 µg/L** (low systemic hepcidin activity, "
                "permitting enterocyte ferroportin transport) with mild-to-low-moderate symptom severity (**IRLS < 15**) "
                "and intact gastrointestinal tolerance.\n"
                "- **Standard Regimen:** Ferrous sulfate **65 mg elemental iron** (325–650 mg/day co-administered with "
                "Vitamin C in adults; **3 mg/kg/day** in pediatric patients) for 12 weeks, followed by repeat iron panel "
                "assessment (Allen et al., 2018; González-Parejo et al., 2024; Dye et al., 2017)."
            )
            indication_status = "Oral Iron First-Line"
        elif (75 < ferritin < 300) and (tsat <= 45) and (not oral_intolerance) and (0 < irls_score < 15):
            st.warning(
                "**CLINICAL DIRECTIVE: ORAL IRON INEFFICIENT (HEPCIDIN BLOCKADE) — SYMPTOM SEVERITY BELOW IV THRESHOLD**\n\n"
                "- **Pathophysiological Rationale:** Because serum ferritin exceeds **75 µg/L**, hepatic hepcidin "
                "upregulation limits intestinal oral iron absorption (Allen et al., 2018). However, mild symptom severity "
                "(**IRLS < 15**) without refractory features does not yet mandate intravenous infusion.\n"
                "- **Clinical Action:** Optimize non-iron therapies or monitor clinically; initiate IV iron if IRLS "
                "progresses to **≥ 15** or if functional iron deficiency (**TSAT ≤ 35%**) is accompanied by refractory symptoms."
            )
            indication_status = "IV Iron Not Indicated"
        else:
            st.warning(
                "**CLINICAL DIRECTIVE: INTRAVENOUS IRON NOT ROUTINELY INDICATED (IRON REPLETE / ASYMPTOMATIC)**\n\n"
                "- **Rationale:** Baseline peripheral iron indices (**Ferritin ≥ 300 µg/L** or **TSAT > 45%**, or IRLS = 0) "
                "do not support empirical intravenous iron administration.\n"
                "- **Clinical Action:** Avoid iatrogenic iron overload. Evaluate secondary neurological mimics or "
                "optimize guideline-directed non-iron pharmacotherapy (e.g., α₂δ ligands)."
            )
            indication_status = "IV Iron Not Indicated"

        if active_augmentation:
            st.error(
                "**DOPAMINERGIC AUGMENTATION WARNING:** Multicenter randomized controlled trial evidence (Earley et al., "
                "2024; Phan et al., 2026) demonstrates attenuated clinical responsiveness to IV iron among patients "
                "experiencing active dopaminergic augmentation. Iron repletion must be paired with a structured, "
                "gradual down-titration of dopamine agonists."
            )

        if "Radiculopathy" in rls_phenotype:
            st.warning(
                "**COMORBID RADICULOPATHY NOTICE:** Observational cohort data (Park et al., 2020) indicate a "
                "significantly lower IV iron responder rate (**39.3%**) in patients with comorbid lumbosacral "
                "radiculopathy. Concurrent management of radicular neuropathy is required."
            )

        st.markdown('<div class="panel-title">3. Minimum Effective Dose Gatekeeper</div>', unsafe_allow_html=True)
        if indication_status == "IV Iron Not Indicated":
            st.info(
                "**Dosing Gate Status:** Inactive. Intravenous iron is not currently indicated based on "
                "baseline biomarker thresholds or clinical severity."
            )
        elif indication_status == "Oral Iron First-Line":
            st.info(
                "**Oral Dosing Protocol:** Administer oral ferrous sulfate **65 mg elemental iron** "
                "(325–650 mg/day with ascorbic acid in adults, or **3 mg/kg/day** in pediatric patients to achieve "
                "target ferritin > 50 µg/L; Allen et al., 2018; Dye et al., 2017)."
            )
        elif is_pediatric:
            st.info(
                "**Pediatric Intravenous Dosing Directive:** Administer **15 mg/kg IV (maximum single dose 750 mg)** "
                "in pediatric RLS/PLMD patients intolerant or refractory to oral iron (DelRosso et al., 2021; "
                "ferritin increased from 14.6 ± 7.01 to 112.4 ± 65.86 µg/L, p < 0.00001)."
            )
        else:
            st.error(
                "**MANDATORY ADULT DOSING GATE: DO NOT PRESCRIBE A SINGLE 500 mg IV DOSE**\n\n"
                "- **RCT Evidence:** Cho et al. (2018, n = 64) demonstrated that a single **500 mg** IV FCM dose "
                "does **not** achieve statistically significant IRLS score reduction compared with placebo "
                "(**-8.3 ± 7.5 vs. -4.8 ± 8.7, p = 0.100**).\n"
                "- **Target Therapeutic Dose:** Prescribe a total dose of **≥ 1,000 mg** (e.g., **1,000 mg** single "
                "infusion or **750 mg × 2** on Day 0 and Day 5), which yields robust IRLS score reductions of "
                "**-8.0 to -11.9 points** (Cho et al., 2016; Earley et al., 2024; Khan et al., 2024) "
                "→ **Proceed to Module 2 to select a metabolically safe IV formulation.**"
            )

# ==============================================================================
# MODULE 2: STEP 2 & 3 - 6-H SYNDROME TRIAGE & FORMULATION PATHWAY
# ==============================================================================
with tab2:
    st.markdown("#### **Step 2 & 3: 'Two-Hit' Osteocyte–FGF23 Risk Stratification and Formulation Selection**")
    st.caption(
        "Quantifies patient susceptibility to intact fibroblast growth factor 23 (iFGF23)-mediated "
        "hypophosphatemia ('6-H Syndrome') driven by osteocyte DMP1–integrin cleavage blockade "
        "(Wagner et al., Blood 2026; Phan, Sleep Medicine 2027) and assigns Pathway A or Pathway B."
    )

    col2_a, col2_b = st.columns([1.05, 1.15], gap="large")

    with col2_a:
        st.markdown('<div class="panel-title">1. Pre-Infusion Metabolic & Pharmacological Profile</div>', unsafe_allow_html=True)

        baseline_po4 = st.number_input(
            "Baseline Serum Phosphate — PO₄ (mg/dL) [Adult Reference Range: 2.5–4.5 mg/dL]:",
            min_value=0.5, max_value=8.0, value=3.2, step=0.1,
            help="Pre-existing hypophosphatemia (< 2.5 mg/dL or < 0.81 mmol/L) is an ABSOLUTE contraindication "
                 "to Ferric Carboxymaltose (Phan, Sleep Medicine 2027, Fig. 1)."
        )

        planned_drug = st.selectbox(
            "Candidate / Formulary-Default IV Iron Formulation (Hit-2 Osteocyte Intensity):",
            [
                "Ferric Carboxymaltose — FCM (+6 pts | 50.0%–75.0% Hypophosphatemia Incidence)",
                "Ferric Derisomaltose — FDI (+1 pt | < 8.5% Risk, 20-min single infusion)",
                "Iron Sucrose — IS (+1 pt | Low Risk, preferred in Hemodialysis cohorts)",
                "Ferumoxytol (0 pts | < 1.0% Risk, 15–30 min infusion)",
                "Low Molecular Weight Iron Dextran — LMW ID (0 pts | ~0.0% Risk, 60-min infusion)"
            ]
        )

        renal_status = st.radio(
            "Glomerular Filtration Profile (The Renal Filtration Paradox):",
            [
                "Normal or Hyperfiltrating Renal Function (eGFR ≥ 60 mL/min/1.73m²) [+2 pts]",
                "Moderate-to-Severe CKD or Hemodialysis (eGFR < 60 mL/min/1.73m²) [0 pts]"
            ],
            help="Paradoxically, normal or hyperfiltrating GFR facilitates massive urinary phosphate wasting "
                 "when proximal tubular NaPi-2a and NaPi-2c cotransporters are downregulated by iFGF23, whereas "
                 "advanced CKD limits filtration-dependent phosphaturia (Phan, 2027; Phan et al., 2026)."
        )

        dosing_history = st.radio(
            "Intravenous Iron Treatment Trajectory:",
            [
                "Recurrent / Maintenance Dosing (≥ 2 infusions; typical relapse every 10–14.5 months) [+3 pts]",
                "First-Time (Index) Intravenous Iron Infusion [0 pts]"
            ],
            help="In relapsing RLS, mean retreatment interval is 14.5 ± 8.0 months after the first dose and "
                 "10–11 months subsequently (Park et al., 2022). Repeated FCM exposure causes cumulative "
                 "bone mineralization defects, osteomalacia, and fractures (Wagner et al., 2026; Schaefer et al., 2016)."
        )

        vitd_bone_risk = st.checkbox(
            "Vitamin D deficiency, low baseline ionized Calcium (iCa), or Osteopenia / Osteoporosis [+2 pts]",
            value=False,
            help="iFGF23 inhibits 1α-hydroxylase (CYP27B1), depleting calcitriol (1,25(OH)₂D), inducing "
                 "hypocalcemia and secondary hyperparathyroidism (PTH surge), which compounds phosphaturia."
        )
        gi_malabsorption = st.checkbox(
            "Gastrointestinal Malabsorption or Malnutrition (IBD, Celiac disease, Post-gastrectomy) [+1 pt]",
            value=("Post-Gastrectomy" in rls_phenotype),
            help="Chronic iron deficiency upregulates baseline bone FGF23 transcription (Hit 1) while "
                 "malabsorption prevents compensatory enteric phosphate uptake."
        )
        heart_failure = st.checkbox(
            "Pre-existing Heart Failure or Cardiomyopathy [+1 pt & Myocardial Safety Alert]",
            value=False,
            help="In the HEART-FID substudy (Nouhravesh et al., 2025), FCM induced phosphate reductions in "
                 "57.6% of heart failure patients vs 10.3% placebo; severe hypophosphatemia impairs myocardial "
                 "contractility (Ishikawa et al., 2025)."
        )
        strict_formulary = st.checkbox(
            "Strict Institutional Formulary / Payer Mandate (FCM is the sole reimbursed formulation available)",
            value=False
        )

    with col2_b:
        st.markdown('<div class="panel-title">2. FERRO-6H-RISK Index & Algorithmic Pathway Assignment</div>', unsafe_allow_html=True)

        drug_pts_map = {
            "Ferric Carboxymaltose — FCM (+6 pts | 50.0%–75.0% Hypophosphatemia Incidence)": 6,
            "Ferric Derisomaltose — FDI (+1 pt | < 8.5% Risk, 20-min single infusion)": 1,
            "Iron Sucrose — IS (+1 pt | Low Risk, preferred in Hemodialysis cohorts)": 1,
            "Ferumoxytol (0 pts | < 1.0% Risk, 15–30 min infusion)": 0,
            "Low Molecular Weight Iron Dextran — LMW ID (0 pts | ~0.0% Risk, 60-min infusion)": 0
        }
        drug_pts = drug_pts_map[planned_drug]
        renal_pts = 2 if "≥ 60" in renal_status else 0
        recurrent_pts = 3 if "Recurrent" in dosing_history else 0
        bone_pts = 2 if vitd_bone_risk else 0
        gi_pts = 1 if gi_malabsorption else 0
        hf_pts = 1 if heart_failure else 0

        host_metabolic_pts = renal_pts + recurrent_pts + bone_pts + gi_pts + hf_pts
        total_6h_score = drug_pts + host_metabolic_pts
        hypothetical_fcm_score = 6 + host_metabolic_pts
        hard_stop_po4 = baseline_po4 < 2.5

        m2_c1, m2_c2, m2_c3 = st.columns(3)
        m2_c1.metric("Host Metabolic Risk", f"{host_metabolic_pts} / 9 pts", "Hit-1 & Renal Susceptibility")
        m2_c2.metric("Formulation Hit-2 Score", f"+{drug_pts} / 6 pts", f"If FCM selected: {hypothetical_fcm_score}/15")
        m2_c3.metric("Composite FERRO-6H-RISK", f"{total_6h_score} / 15 pts", "Pathway A Cutoff: ≥ 6 pts")

        if "Hemodialysis" in rls_phenotype and "≥ 60" in renal_status:
            st.warning(
                "**CROSS-MODULE CONSISTENCY NOTE:** Hemodialysis / ESRD was selected in Module 1, whereas "
                "eGFR ≥ 60 mL/min/1.73m² is currently selected above. Please verify renal filtration status."
            )

        if hard_stop_po4:
            st.error(
                "**HARD-STOP GATEKEEPER TRIGGERED: ABSOLUTE CONTRAINDICATION TO FERRIC CARBOXYMALTOSE**\n\n"
                f"- **Baseline Serum Phosphate:** `{baseline_po4:.1f} mg/dL` (below the **2.5 mg/dL / 0.81 mmol/L** safety threshold).\n"
                "- **Pathophysiological Mechanism (Phan, 2027, Fig. 1):** Administering FCM to a patient with pre-existing "
                "hypophosphatemia induces an unbuffered surge in bioactive intact FGF23 (via osteocyte DMP1–integrin "
                "blockade), precipitating severe hypophosphatemia (**< 1.0 mg/dL**), acute respiratory/proximal myopathy, "
                "and osteomalacia.\n"
                "- **Mandatory Clinical Action:** **ASSIGN PATHWAY A (STRICTLY BYPASS FCM).** Correct baseline phosphate "
                "and Vitamin D deficits prior to infusion and utilize a non-FGF23-inducing formulation (FDI, Ferumoxytol, "
                "or LMW ID)."
            )
        elif total_6h_score >= 6 or host_metabolic_pts >= 3:
            if drug_pts == 6:
                st.warning(
                    "**ASSIGNED ROUTE: PATHWAY A — HIGH METABOLIC RISK / PREFERRED SAFE ROUTE (BYPASS FCM)**\n\n"
                    f"- **Risk Stratification:** High composite iFGF23 cleavage blockade risk (**FERRO-6H-RISK = "
                    f"{total_6h_score}/15 pts**; Host Metabolic Risk = **{host_metabolic_pts}/9 pts**).\n"
                    "- **Clinical Directive (Phan, 2027, Step 3 — Pathway A):** **Do not administer Ferric Carboxymaltose (FCM).** "
                    "Transition to a third-generation alternative that achieves central nervous system iron repletion "
                    "without disrupting the osteocyte–renal phosphate axis:\n"
                    "  1. **Ferric Derisomaltose (FDI):** `1,000 mg` single IV infusion over **20 minutes** "
                    "(IRLS reduction **-8.0 to -11.9 pts**; hypophosphatemia incidence **< 8.5%** vs. **51.0%** with FCM "
                    "in PHOSPHARE-IBD; Zoller et al., 2023).\n"
                    "  2. **Ferumoxytol:** `1,020 mg` single or split IV infusion over **15–30 minutes** "
                    "(IRLS reduction **-7.9 pts**; hypophosphatemia incidence **< 1.0%**; Short et al., 2024; Adkinson et al., 2018. "
                    "*Observe FDA boxed warning precautions regarding hypersensitivity*).\n"
                    "  3. **Low Molecular Weight Iron Dextran (LMW ID):** `1,000 mg` single IV infusion over **60 minutes** "
                    "following a test dose (negligible hypophosphatemia risk **~0.0%**; Glaspy et al., 2020; Wong et al., 2016)."
                    + (
                        "\n  4. **Hemodialysis Subgroup Option — IV Iron Sucrose (IS):** `1,000 mg` total divided across "
                        "dialysis sessions (IRLS reduction **-7.38 pts**, p < 0.001; Deng et al., 2017)."
                        if "Hemodialysis" in rls_phenotype or "< 60" in renal_status else ""
                    )
                )
            else:
                st.success(
                    "**ASSIGNED ROUTE: PATHWAY A VERIFIED — METABOLICALLY SAFE FORMULATION SELECTED**\n\n"
                    f"- **Risk Mitigation Confirmed:** The patient exhibits host metabolic vulnerability (**Host Risk = "
                    f"{host_metabolic_pts}/9 pts**; selecting FCM would have resulted in a high-risk score of "
                    f"**{hypothetical_fcm_score}/15 pts**). By selecting **{planned_drug.split('—')[0].strip()}**, the "
                    f"active composite score is reduced to **{total_6h_score}/15 pts**.\n"
                    "- **Pathophysiological Advantage (Phan, 2027, Fig. 1):** Guarantees neurological iron delivery across "
                    "the blood–brain barrier while avoiding osteocyte DMP1–integrin blockade and iFGF23-driven urinary "
                    "phosphate wasting."
                )

            if strict_formulary:
                st.info(
                    "**FORMULARY RESTRICTION CONTINGENCY (PATHWAY B PROTOCOL):** If institutional or insurance mandates "
                    "strictly prohibit FDI, Ferumoxytol, or LMW ID and compel FCM administration, **Mandatory Pathway B "
                    "Surveillance** must be enforced: obtain **Serum PO₄, ionized Calcium (iCa), and 1,25(OH)₂D** at "
                    "**Weeks 2–3 post-infusion** (the physiological nadir of iFGF23-induced phosphaturia) and prepare "
                    "active **calcitriol (0.25–0.5 µg/day) + oral phosphate supplementation** if 6-H syndrome manifests."
                )
        else:
            st.success(
                "**ASSIGNED ROUTE: LOW COMPOSITE METABOLIC RISK (PATHWAY A PREFERRED / PATHWAY B ELIGIBLE)**\n\n"
                f"- **Clinical Rationale:** Low baseline metabolic risk (**FERRO-6H-RISK = {total_6h_score}/15 pts**) "
                "and normal pre-infusion serum phosphate.\n"
                "- **Clinical Directive:** Third-generation formulations (**FDI, Ferumoxytol, LMW ID**) remain the preferred "
                "standard of care (**Pathway A**). If local formulary constraints mandate **FCM** (**Pathway B**), "
                "proactively monitor **Serum PO₄, iCa, and 1,25(OH)₂D at 2 to 3 weeks post-infusion**."
            )

        if heart_failure:
            st.error(
                "**CARDIOMYOPATHY / HEART FAILURE SAFETY DIRECTIVE (Phan et al., 2026):** Prospective data from the "
                "HEART-FID substudy (Nouhravesh et al., 2025) demonstrated serum phosphate reductions in **57.6%** "
                "of FCM-treated heart failure patients (vs. **10.3%** with placebo). Severe hypophosphatemia depletes "
                "myocardial ATP and can precipitate acute heart failure decompensation and myopathy (Ishikawa et al., 2025). "
                "**FCM should be strictly avoided in this patient.**"
            )

        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=15 if hard_stop_po4 else total_6h_score,
            title={"text": "Active FERRO-6H-RISK Index (0–15 Scale)", "font": {"size": 14, "color": "#1e293b"}},
            number={"font": {"size": 28, "color": "#0f172a"}},
            gauge={
                "axis": {"range": [0, 15], "tickwidth": 1, "tickcolor": "#475569"},
                "bar": {"color": "#991b1b" if (hard_stop_po4 or total_6h_score >= 6 or host_metabolic_pts >= 3) else "#0369a1"},
                "steps": [
                    {"range": [0, 5.9], "color": "#e0f2fe"},
                    {"range": [5.9, 9.5], "color": "#fef3c7"},
                    {"range": [9.5, 15], "color": "#fee2e2"}
                ],
                "threshold": {
                    "line": {"color": "#dc2626", "width": 4},
                    "thickness": 0.8,
                    "value": 6
                }
            }
        ))
        fig_gauge.update_layout(
            height=230,
            margin=dict(l=25, r=25, t=45, b=10),
            paper_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_gauge, use_container_width=True)

# ==============================================================================
# MODULE 3: POST-INFUSION DIAGNOSTIC DE-CONFOUNDER
# ==============================================================================
with tab3:
    st.markdown("#### **Module 3: Post-Infusion Diagnostic De-confounder**")
    st.caption(
        "Resolves post-infusion diagnostic confounding in patients presenting with persistent or worsening "
        "lower-extremity symptoms or fatigue by differentiating: (1) Iatrogenic 6-H Hypophosphatemic Myopathy, "
        "(2) True RLS Relapse / Dopaminergic Augmentation, and (3) Physiological Delayed CNS Iron Repletion "
        "(Phan, Sleep Medicine 2027; Phan et al., Sleep and Breathing 2026)."
    )

    col3_a, col3_b = st.columns([1.05, 1.15], gap="large")

    with col3_a:
        st.markdown('<div class="panel-title">1. Post-Infusion Timeline & Clinical Semiology</div>', unsafe_allow_html=True)

        weeks_post_infusion = st.slider(
            "Time Elapsed Since Last Intravenous Iron Infusion (Weeks):",
            min_value=1, max_value=80, value=3, step=1,
            help="Weeks 1–6: Peak window for both FCM-induced iFGF23 hypophosphatemia AND physiological CNS "
                 "blood–brain barrier transport delay (Trenkwalder et al., 2017). ≥ 40–60 weeks (10–14.5 months): "
                 "Expected window for true RLS iron-depletion relapse (Park et al., 2022)."
        )

        infused_fcm = st.checkbox(
            "Most recent infusion formulation was Ferric Carboxymaltose (FCM)",
            value=True
        )

        post_po4_status = st.selectbox(
            "Post-Infusion Serum Phosphate (PO₄) Laboratory Status:",
            [
                "Not yet measured (Frequent diagnostic blind spot in sleep medicine clinics)",
                "Normal Serum Phosphate (PO₄ ≥ 2.5 mg/dL / ≥ 0.81 mmol/L)",
                "Moderate Hypophosphatemia (PO₄ 1.0–2.4 mg/dL / 0.32–0.80 mmol/L)",
                "Severe Life-Threatening Hypophosphatemia (PO₄ < 1.0 mg/dL / < 0.32 mmol/L)"
            ]
        )

        st.markdown("**Post-Infusion Symptom Semiology Checklist:**")
        sym_proximal_weakness = st.checkbox(
            "Generalized daytime fatigue and proximal muscle weakness (e.g., difficulty rising from a chair or climbing stairs) [+30 pts 6-H]",
            value=True
        )
        sym_bone_pain = st.checkbox(
            "Deep, continuous, non-circadian skeletal pain (pelvic, femoral, or pretibial bone tenderness) [+25 pts 6-H]",
            value=True
        )
        sym_circadian_urge = st.checkbox(
            "Classic evening/nocturnal circadian urge to move the legs, worsening at rest and relieved by ambulation [+30 pts RLS]",
            value=False
        )
        sym_dopamine_aug = st.checkbox(
            "Receiving chronic Dopamine Agonists with paradoxical earlier afternoon symptom onset, increased intensity, or spread to upper limbs [+35 pts Aug]",
            value=False
        )

    with col3_b:
        st.markdown('<div class="panel-title">2. Differential Probability Matrix & Management Protocol</div>', unsafe_allow_html=True)

        score_6h = 0
        score_rls_aug = 0
        score_delayed = 0

        # 1. Iatrogenic 6-H Hypophosphatemic Myopathy Score
        if infused_fcm and (1 <= weeks_post_infusion <= 12):
            score_6h += 30
        elif infused_fcm and weeks_post_infusion > 12:
            score_6h += 10
        if sym_proximal_weakness:
            score_6h += 30
        if sym_bone_pain:
            score_6h += 25
        if "Moderate" in post_po4_status:
            score_6h += 40
        elif "Severe" in post_po4_status:
            score_6h += 65
        elif "Normal" in post_po4_status:
            score_6h = max(0, score_6h - 60)

        # 2. True RLS Relapse / Dopaminergic Augmentation Score
        if sym_circadian_urge:
            score_rls_aug += 15 if weeks_post_infusion < 12 else 30
        if sym_dopamine_aug:
            score_rls_aug += 35
        if weeks_post_infusion >= 40:
            score_rls_aug += 25
        if not sym_proximal_weakness and not sym_bone_pain and sym_circadian_urge:
            score_rls_aug += 7 if weeks_post_infusion < 12 else 15

        # 3. Physiological Delayed CNS Iron Repletion Score (Trenkwalder et al., 2017)
        if weeks_post_infusion < 12:
            score_delayed += 35
            if weeks_post_infusion <= 6:
                score_delayed += 17
        if not sym_proximal_weakness and not sym_bone_pain and ("Normal" in post_po4_status or not infused_fcm):
            score_delayed += 30
        if "Moderate" in post_po4_status or "Severe" in post_po4_status or (sym_proximal_weakness and sym_bone_pain):
            score_delayed = max(5, score_delayed - 32)
        if weeks_post_infusion >= 12:
            score_delayed = 5

        total_raw = max(1, score_6h + score_rls_aug + score_delayed)
        prob_6h = (score_6h / total_raw) * 100
        prob_rls = (score_rls_aug / total_raw) * 100
        prob_delay = (score_delayed / total_raw) * 100

        df_deconf = pd.DataFrame({
            "Differential Etiology": [
                "1. Iatrogenic 6-H Hypophosphatemic Myopathy",
                "2. True RLS Relapse / Dopaminergic Augmentation",
                "3. Physiological Delayed CNS Repletion (< 12 Weeks)"
            ],
            "Relative Likelihood (%)": [round(prob_6h, 1), round(prob_rls, 1), round(prob_delay, 1)]
        })

        fig_bar = go.Figure(go.Bar(
            x=df_deconf["Relative Likelihood (%)"],
            y=df_deconf["Differential Etiology"],
            orientation="h",
            marker_color=["#991b1b", "#b45309", "#0369a1"],
            text=[f"{v:.1f}%" for v in df_deconf["Relative Likelihood (%)"]],
            textposition="auto"
        ))
        fig_bar.update_layout(
            height=220,
            xaxis_title="Relative Diagnostic Probability Share (%)",
            xaxis=dict(range=[0, 100]),
            yaxis=dict(autorange="reversed"),
            margin=dict(l=10, r=10, t=10, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_bar, use_container_width=True)

        if prob_6h >= prob_rls and prob_6h >= prob_delay:
            st.error(
                f"**PRIMARY DIAGNOSTIC CLASSIFICATION ({prob_6h:.1f}%): IATROGENIC 6-H HYPOPHOSPHATEMIC MYOPATHY / OSTEOMALACIA MIMICRY**\n\n"
                "- **Clinical De-confounding Analysis (Phan, 2027; Pozzessere, 2025):** Post-FCM hypophosphatemic "
                "muscle weakness, exhaustion, and deep skeletal pain frequently mimic refractory RLS.\n"
                "- **CRITICAL CONTRAINDICATION:** **Do NOT escalate dopamine agonists or α₂δ ligands, and do NOT "
                "administer repeat FCM infusions.**\n"
                "- **Immediate Therapeutic Protocol:**\n"
                "  1. Obtain urgent **Serum PO₄, ionized Calcium (iCa), intact PTH, 25(OH)D, and 1,25(OH)₂D**.\n"
                "  2. Initiate active **Calcitriol (1,25(OH)₂D; 0.25–0.5 µg/day)** alongside oral/intravenous "
                "phosphate supplementation to counter iFGF23-mediated CYP27B1 inhibition and secondary hyperparathyroidism.\n"
                "  3. Permanently transition future maintenance iron therapy to **Pathway A (FDI, Ferumoxytol, or LMW ID)**."
            )
        elif prob_delay > prob_6h and prob_delay >= prob_rls:
            st.info(
                f"**PRIMARY DIAGNOSTIC CLASSIFICATION ({prob_delay:.1f}%): PHYSIOLOGICAL DELAYED CNS IRON REPLETION WINDOW (< 12 WEEKS)**\n\n"
                "- **Pharmacokinetic Rationale (Trenkwalder et al., 2017; Phan et al., 2026):** In double-blind, "
                "placebo-controlled RCT data, 1,000 mg IV iron demonstrated **non-significant IRLS score reduction "
                "at Week 4 (-2.5 pts, 95% CI: -5.93 to 1.02, p = 0.163)**, but achieved **statistically significant "
                "remission by Week 12 (-4.66 pts, 95% CI: -8.59 to -0.73, p = 0.021)** due to slow transferrin-receptor "
                "transport across the blood–brain barrier and gradual striatal tyrosine hydroxylase restoration.\n"
                "- **Clinical Action:** Counsel and reassure the patient. Avoid premature declaration of treatment "
                "failure or unnecessary medication escalation prior to the **Week 12 clinical evaluation landmark**."
            )
        else:
            st.warning(
                f"**PRIMARY DIAGNOSTIC CLASSIFICATION ({prob_rls:.1f}%): TRUE RLS RELAPSE OR DOPAMINERGIC AUGMENTATION**\n\n"
                "- **Semiological Interpretation:** Symptoms exhibit classic evening/nocturnal circadian rhythmicity "
                "and relief with movement without clinical or biochemical features of hypophosphatemic myopathy.\n"
                "- **Management Protocol:**\n"
                "  1. **If Time Elapsed ≥ 10–14.5 Months Post-Infusion (Park et al., 2022):** Findings reflect "
                "expected physiological depletion of iron stores after initial remission. Re-evaluate serum ferritin "
                "and TSAT; if **TSAT ≤ 35%**, schedule maintenance IV iron exclusively via **Pathway A (FDI 1,000 mg, "
                "Ferumoxytol 1,020 mg, or LMW ID 1,000 mg)** to prevent cumulative osteocyte toxicity.\n"
                "  2. **If Active Dopaminergic Augmentation is Present (Earley et al., 2024):** Perform a structured "
                "cross-taper from dopamine agonists to α₂δ ligands alongside iron optimization."
            )

# ==============================================================================
# MODULE 4: REFERENCE ARSENAL & IN-SILICO VALIDATION VIGNETTES
# ==============================================================================
with tab4:
    st.markdown("#### **Module 4: Comparative Pharmacological Arsenal & In-Silico Validation Suite**")
    st.caption(
        "Synthesizes Table 1 from Sleep Medicine (Phan, 2027) and the 17 core clinical trials/meta-analyses "
        "from Sleep and Breathing (Phan et al., 2026), accompanied by the standardized In-Silico Clinical "
        "Vignette Benchmark Dataset."
    )

    st.markdown('<div class="panel-title">1. Comparative Neurological Efficacy & Metabolic Safety of IV Iron Formulations in RLS</div>', unsafe_allow_html=True)
    df_formulary = pd.DataFrame({
        "IV Iron Formulation": [
            "Ferric Carboxymaltose (FCM)",
            "Ferric Derisomaltose (FDI)",
            "Ferumoxytol",
            "Low Molecular Weight Iron Dextran (LMW ID)",
            "Iron Sucrose (IS) [Hemodialysis Subgroup]"
        ],
        "Standard RLS Dosing Regimen": [
            "1,000 mg (single) or 1,500 mg (750 mg × 2)",
            "1,000 mg (single total dose infusion)",
            "1,020 mg (single or 510 mg × 2 split dose)",
            "1,000 mg (single total dose infusion)",
            "1,000 mg (divided across dialysis sessions)"
        ],
        "Efficacy on IRLS Score (Mean Change)": [
            "High (-8.0 to -11.9 pts; p ≤ 0.03)",
            "High (Comparable to FCM; ~ -8.0 to -11.9 pts)",
            "High (-7.9 pts; comparable to FCM)",
            "High (Comparable to FCM; ~ -8.0 to -11.9 pts)",
            "High in Hemodialysis (-7.38 vs -0.81 placebo; p < 0.001)"
        ],
        "iFGF23-Mediated Hypophosphatemia Risk": [
            "Severe (50.0%–75.0%) [Osteocyte DMP1–integrin blockade]",
            "Low (< 8.5%) [Linear glucose matrix; PHOSPHARE-IBD]",
            "Very Low (< 1.0%) [Superparamagnetic carbohydrate shell]",
            "Negligible (~0.0%) [No osteocyte FGF23 cleavage arrest]",
            "Low (< 5.0% — negligible in anuric ESRD)"
        ],
        "Administration Protocol & Clinical Directives": [
            "15–30 min | Bypass in Pathway A; mandatory Week 2–3 PO₄/iCa/1,25(OH)₂D monitoring in Pathway B",
            "20 min single visit | First-line Pathway A replacement matching FCM administrative convenience",
            "15–30 min | Pathway A alternative; observe FDA Boxed Warning precautions for hypersensitivity",
            "60 min (test dose required) | Pathway A gold-standard long-term metabolic & skeletal safety",
            "Multi-session | Evidence-based option in Hemodialysis / ESRD-associated RLS (Deng et al., 2017)"
        ]
    })
    st.dataframe(df_formulary, use_container_width=True, hide_index=True)

    st.markdown('<div class="panel-title">2. In-Silico Clinical Vignette Stress-Testing Suite (Exportable CSV)</div>', unsafe_allow_html=True)
    df_vignettes = pd.DataFrame({
        "Vignette ID": ["VIG-01", "VIG-02", "VIG-03", "VIG-04", "VIG-05"],
        "Clinical Scenario": [
            "Adult Female, Primary RLS in Ferritin Gray Zone, Normal eGFR",
            "Post-Gastrectomy RLS, Low Baseline PO₄ (2.1 mg/dL), Osteopenia",
            "Recurrent Relapsing RLS (3rd infusion at 12 mos), Hospital Formulary FCM Default",
            "Post-FCM Week 3: Proximal Weakness, Deep Tibial Pain, PO₄ 1.4 mg/dL",
            "Post-FDI Week 4: Persistent Evening RLS, Normal PO₄ (3.4 mg/dL), No Weakness"
        ],
        "Baseline Biomarkers": [
            "IRLS 26 | Ferritin 145 µg/L | TSAT 24% | PO₄ 3.3 mg/dL | eGFR 92",
            "IRLS 31 | Ferritin 42 µg/L | TSAT 14% | PO₄ 2.1 mg/dL | eGFR 85",
            "IRLS 24 | Ferritin 110 µg/L | TSAT 31% | PO₄ 2.9 mg/dL | eGFR 78",
            "3w post-1000mg FCM | PO₄ 1.4 mg/dL | Non-circadian myalgia/fatigue",
            "4w post-1000mg FDI | PO₄ 3.4 mg/dL | Classic evening urge only"
        ],
        "Step 1 Output (Indication & Phenotype)": [
            "IV Iron Indicated ('Hidden Responder' via TSAT ≤ 35%; Expected Response ~79.3%)",
            "IV Iron Indicated (Post-Gastrectomy Phenotype; Expected Response ~90.9%)",
            "IV Iron Indicated (Repeated Dosing Responder Rate ~80.8%; Dose ≥ 1000 mg)",
            "Already Infused -> Routed to Module 3 De-confounder",
            "Already Infused -> Routed to Module 3 De-confounder"
        ],
        "Step 2/3 FERRO-6H-RISK & Pathway": [
            "Host Risk 2 pts (+6 if FCM = 8/15) -> PATHWAY A: Bypass FCM, give FDI 1000 mg (20 min)",
            "HARD-STOP GATE (PO₄ < 2.5) + Score 13/15 -> PATHWAY A: Strictly contraindicate FCM",
            "Host Risk 5 pts (+6 FCM = 11/15) -> PATHWAY A (or Pathway B mandatory Wk 2-3 lab monitor)",
            "Module 3 De-confounder: 86.2% Probability of Iatrogenic 6-H Hypophosphatemic Myopathy",
            "Module 3 De-confounder: 78.8% Probability of Physiological Delayed CNS Repletion (<12w)"
        ],
        "Prevented Clinical Error": [
            "Prevents denying IV iron due to 'normal' ferritin (145 µg/L) & avoids 1st-hit FCM phosphaturia",
            "Prevents life-threatening <1.0 mg/dL hypophosphatemia & pathological fracture",
            "Prevents cumulative osteomalacia from repeated FCM courses every 10-14.5 months",
            "Prevents mistaken dopamine agonist escalation for pseudo-RLS hypophosphatemic myopathy",
            "Prevents premature treatment failure declaration at Week 4 before Week 12 CNS peak"
        ]
    })
    st.dataframe(df_vignettes, use_container_width=True, hide_index=True)

    csv_data = df_vignettes.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download In-Silico Validation Dataset (CSV for Short Communication Manuscript)",
        data=csv_data,
        file_name="FERRO_SAFE_InSilico_Validation_Vignettes.csv",
        mime="text/csv"
    )
