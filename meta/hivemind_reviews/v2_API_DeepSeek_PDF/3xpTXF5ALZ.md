## Summary
# Final Review Report

## Summary

This paper proposes AI2TALE, a deep learning method for phishing attack localization — the task of identifying which specific sentences in an email cause it to be classified as phishing. The method combines mutual information maximization (to select label-relevant sentences) with information bottleneck regularization (to avoid selecting supersets of sentences) under a weakly supervised setting where only document-level vulnerability labels are available. Experiments on seven email datasets with ~40,000 samples show that AI2TALE achieves 99.33% Label-Accuracy and 98.95% Cognitive-True-Positive, outperforming five intrinsic interpretability baselines (L2X, INVASE, ICVH, VIBI, AIM) by margins of 1.39–3.32% on the combined average metric. A human evaluation (N=25) finds that 81% of participants agree the top-1 selected sentences are persuasive.

The paper addresses a practically important problem (explainable phishing detection), proposes a technically sound framework combining variational mutual information bounds with information bottleneck theory and a data-distribution mechanism, and provides extensive experiments across seven datasets. The main weaknesses are: (1) the claimed 1.5–3.5% improvement requires careful framing since individual metric gains are ~0.85–0.93% and no variance/statistical significance is reported; (2) the human evaluation lacks a baseline comparison and has a small sample; (3) the Related Work section is a flat citation list rather than a structured comparison; (4) the conclusion lacks concrete limitations and failure-case discussion; (5) novelty verification is deferred due to external retrieval being unavailable in this run.

## Strengths
1. **Practically motivated problem formulation.** Phishing attack localization — identifying which specific sentences cause an email to be classified as phishing — addresses a genuine gap in explainable cybersecurity. The weakly supervised setting (using only document-level labels) is realistic since ground-truth sentence-level phishing annotations are rarely available in practice.

2. **Technically sound framework combining multiple information-theoretic principles.** The method integrates three well-motivated components: (a) a variational lower bound on mutual information for selection learning, (b) an information bottleneck regularizer to prevent trivial superset selections, and (c) a data-distribution mechanism to decouple the classifier from the selector. This architectural combination goes beyond individual existing methods (L2X, VIBI, ICVH) and is a genuine technical contribution.

3. **Extensive evaluation across seven diverse email datasets with ~40,000 samples.** The datasets cover multiple sources (IWSPA-AP, Nazario, Miller Smiles, Cornell Phish Bowl, Fraud emails, Cambridge, Enron) and writing styles. This diversity strengthens external validity claims.

4. **Two complementary evaluation metrics.** Label-Accuracy measures whether the top-1 selected sentence alone predicts the correct label, while Cognitive-True-Positive measures alignment with known psychological persuasion triggers. This dual-metric design is more informative than using either metric alone.

5. **Human evaluation provides initial evidence of practical usefulness.** 81% of 25 participants rated the selected sentences as persuasive, suggesting the method identifies intuitively meaningful phishing content.

6. **Reproducibility commitment.** The authors provide publicly available source code and data references, which is good practice for verifiable research.

7. **Honest threat-to-validity discussion (Appendix 6.9).** The paper includes construct, internal, and external validity analyses, which is more transparent than many papers that omit such self-critique.

## Weaknesses
1. **Missing statistical significance and variance reporting (Major).** Table 1 reports point estimates without standard deviations, confidence intervals, or significance tests. The individual metric gains (~0.85–0.93%) could be within noise range. This is the most critical weakness because the paper's main empirical claim depends on these small margins.

2. **Overstated improvement framing (Major).** The abstract and results sections claim "1.5% to 3.5%" improvement over SOTA baselines. This range refers to the *combined average* of two metrics, not individual metrics. The individual Label-Accuracy gain is ~0.93% and Cognitive-True-Positive gain is ~0.85%. The combined-average framing inflates the perceived improvement and could mislead readers.

3. **Human evaluation lacks baseline comparison and has limited sample size (Major).** The evaluation (N=25, 10 emails) only tests AI2TALE's selected sentences. Without showing sentences from baseline methods or random selections, the claim that AI2TALE selects *more useful* sentences is unsupported. No inter-rater reliability metric (e.g., Fleiss' kappa) is reported.

4. **Related Work is a flat citation list rather than structured comparison (Moderate).** The section lists 13+ phishing detection papers and 10+ interpretability papers without grouping by approach type or comparison axes. Readers cannot quickly assess the novelty gap or understand how AI2TALE differs from the strongest prior work.

5. **Data-distribution mechanism interaction with joint training is underspecified (Moderate).** Algorithm 1 alternates between updating the classifier on random masks (Step 4) and jointly updating selector+classifier (Step 5). The paper does not explain why the Step 5 update does not overwrite the effect of Step 4, nor does it provide ablation evidence for the claimed data augmentation benefit.

6. **Cognitive-True-Positive metric relies on ChatGPT-generated keyword lists (Minor).** The metric's reliability depends on the completeness of cognitive trigger keyword lists generated via ChatGPT (Appendix 6.3). This introduces potential measurement bias that is not quantified.

7. **Conclusion lacks concrete limitations and actionable future work (Minor).** The conclusion is purely positive and does not summarize the limitations acknowledged in Appendix 6.9, nor does it provide prioritized future research directions beyond webpage phishing extension.

8. **Novelty verification deferred (Deferred).** Due to external retrieval being unavailable in this run, the novelty claims (C1: problem formalization, C2: AI2TALE method, C3: evaluation metrics) cannot be verified against the full literature. The claim that "automated ML/DL techniques for this problem have not yet been well studied" requires manual literature verification.

## Key Issues
### Issue 1: Missing statistical significance in main quantitative results (Critical)

**Location:** Page 8 - Section 4.4 Quantitative Results, Table 1
**Evidence:** Table 1 reports point estimates without standard deviations, confidence intervals, or significance tests. The individual metric improvements are modest: Label-Accuracy 99.33% vs 98.40% (AIM) = +0.93%; Cognitive-True-Positive 98.95% vs 98.10% (ICVH) = +0.85%.
**Impact:** Without variance information, readers cannot assess whether these differences are statistically reliable or within noise range. The paper's core empirical claim — that AI2TALE outperforms baselines — is weakened.
**Fix (Must):** Report mean±std over ≥3 random seeds for all methods. Add paired significance tests (McNemar's or bootstrap) for AI2TALE vs. the strongest baseline on each metric. Provide effect sizes (Cohen's d or similar).

### Issue 2: Improvement framing inflates perceived gains (Major)

**Location:** Page 1 (Abstract), Page 8 (Section 4.4), Page 9 (Section 4.4)
**Evidence:** The abstract and results repeatedly state "1.5% to 3.5%" improvement. This refers to the *combined average* of Label-Accuracy and Cognitive-True-Positive. The range is computed as 99.14% (AI2TALE) minus 95.82–97.75% (baseline combined averages).
**Impact:** Readers may infer that individual metrics improve by 1.5–3.5%, which is not true. Individual gains are ~0.85–0.93%. The framing is technically correct but potentially misleading.
**Fix (Must):** State the combined-average improvement transparently and report individual metric gains separately. Example: "On the combined average, AI2TALE achieves 99.14%, outperforming baselines by 1.39–3.32 percentage points. Individually, Label-Accuracy improves by ~0.93% and Cognitive-True-Positive by ~0.85%."

### Issue 3: Human evaluation lacks baseline control and has methodological gaps (Major)

**Location:** Page 10 - Section 4.4 Human Evaluation
**Evidence:** 25 participants evaluated only AI2TALE's top-1 sentences for 10 phishing emails. No baseline method sentences or random sentences were shown. No inter-rater reliability metric is reported. The 5-point Likert scale is collapsed to 3 categories.
**Impact:** The evaluation shows that AI2TALE's sentences are perceived as persuasive, but it does not demonstrate that they are *more persuasive* than alternatives. The claim of "effectiveness" is unsupported without a comparative design.
**Fix (Must):** Add a within-subjects or between-subjects comparison condition showing sentences from at least one baseline method. Report Fleiss' kappa for inter-rater agreement. Report full Likert distribution (not collapsed percentages). Expand sample size justification with a power analysis.

### Issue 4: Related Work lacks structured comparison (Moderate)

**Location:** Pages 2-3 - Section 2 Related Work
**Evidence:** Two paragraphs list 13+ phishing detection citations and 10+ interpretability citations with minimal grouping, no comparison axes, and no explicit statement of how AI2TALE differs from the strongest prior work.
**Impact:** Readers cannot efficiently assess the novelty gap. The paper does not build a clear case for why existing intrinsic interpretability methods are insufficient for phishing localization.
**Fix (Must):** Restructure into at least three organized paragraphs: (1) Phishing detection method families with key limitations, (2) Intrinsic vs. post-hoc interpretability with representative methods, (3) Explicit gap: why existing intrinsic methods (L2X, INVASE, etc.) may select supersets or encode labels via selection patterns — and how AI2TALE's IB regularization + data-distribution mechanism addresses this.

### Issue 5: Data-distribution mechanism training dynamics underspecified (Moderate)

**Location:** Page 6, Algorithm 1 (Page 7)
**Evidence:** Step 4 updates classifier on random masks (Eq. 9). Step 5 jointly updates both selector and classifier (Eq. 8). The paper does not explain why the joint update does not overwrite the classifier parameters learned in Step 4. The "data augmentation" claim for generalization is stated without ablation evidence.
**Impact:** Readers cannot fully understand or reproduce the training dynamics. The effectiveness of the data-distribution mechanism vs. simply training on full emails is unverified.
**Fix (Must):** Add a paragraph explaining the alternating training rationale. Provide an ablation study comparing three variants: (a) no data-distribution mechanism, (b) data-distribution mechanism with random masks, (c) data-distribution mechanism with full emails instead of random masks.

## Actionable Suggestions
### Suggestion 1: Add variance reporting and statistical tests (Must, P0)

**Location:** Table 1 (Page 8) and accompanying text
**Action:**
- Run each method with 3 different random seeds and report mean ± std for both Label-Accuracy and Cognitive-True-Positive.
- Add a bootstrapped paired significance test (or McNemar's test for matched samples) comparing AI2TALE against the strongest baseline on each metric.
- Report effect sizes (Cohen's d or similar) to quantify practical significance.
- Update Table 1 to include variance columns (e.g., "Label-Acc (mean±std)") and a significance marker (e.g., †p<0.05 vs. best baseline).
**Expected benefit:** Provides statistical grounding for the claimed improvements and allows readers to assess reliability.

### Suggestion 2: Restructure the improvement claims (Must, P0)

**Location:** Abstract (Page 1), Section 4.4 (Page 8), Conclusion (Page 10)
**Action:**
- Rewrite the abstract improvement sentence to clearly distinguish combined-average vs. individual metric gains.
- In Section 4.4, report and discuss individual metric gaps first, then the combined average.
**Mentor Revised Text (Abstract extract):**
"Notably, under a weakly supervised setting, our approach achieves a combined average of 99.14% on Label-Accuracy and Cognitive-True-Positive, outperforming the compared baselines by 1.39–3.32% on this combined measure. On individual metrics, AI2TALE improves Label-Accuracy by ~0.93% and Cognitive-True-Positive by ~0.85% over the strongest baseline in each."

### Suggestion 3: Improve human evaluation design (Must, P0)

**Location:** Page 10 - Human Evaluation
**Action:**
- Add a within-subjects comparison: show participants sentences from AI2TALE AND from at least one baseline method (e.g., AIM or ICVH) for the same emails, randomized order.
- Compute Fleiss' kappa to measure inter-rater agreement.
- Report full 5-point Likert scale distribution (not collapsed to 3 categories).
- Add a brief power analysis or at least acknowledge the small sample limitation.
**Expected benefit:** Transforms the evaluation from "AI2TALE sentences seem persuasive" to "AI2TALE sentences are more persuasive than baselines."

### Suggestion 4: Restructure Related Work by comparison axes (Must, P1)

**Location:** Pages 2-3 - Section 2
**Action:**
Organize into three thematic paragraphs:
1. **Phishing detection methods** grouped by approach (feature-based URL analysis, visual similarity, NLP-based content analysis, LLM-based). Conclude with shared limitation: no sentence-level explanation.
2. **Interpretable ML methods** with explicit distinction between post-hoc (LIME, SHAP) and intrinsic (L2X, INVASE, VIBI, ICVH, AIM). Describe each intrinsic method's core mechanism and limitation.
3. **Gap statement:** Why existing intrinsic methods are insufficient — they may select supersets, or encode labels via selection patterns rather than semantic content. How AI2TALE addresses each gap.
**Expected benefit:** Readers can quickly assess novelty positioning.

### Suggestion 5: Clarify data-distribution mechanism training dynamics (Nice-to-have, P1)

**Location:** Page 6 - Section 3.2.2, Algorithm 1 (Page 7)
**Action:**
- Add 2-3 sentences explaining the alternating optimization rationale: "Step 4 updates the classifier on randomly masked inputs to learn label-relevant representations independent of the current selector policy. Step 5 then jointly fine-tunes selector and classifier so the selector learns which sentences are predictive. This alternation prevents the degenerate equilibrium where the selector simply encodes the label through arbitrary selection patterns."
- Add an ablation experiment comparing: (a) no data-distribution mechanism, (b) with mechanism, (c) with mechanism but using full emails instead of random masks.
**Expected benefit:** Clarifies training dynamics and validates the claimed benefit.

### Suggestion 6: Revise Cognitive-True-Positive metric description (Nice-to-have, P2)

**Location:** Page 8 - Section 4.2, Appendix 6.3
**Action:**
- Add a sentence acknowledging: "The Cognitive-True-Positive metric relies on keyword matching against cognitive trigger lists; this serves as a proxy measure and may not capture all psychological persuasion techniques used in phishing."
- Report the keyword list size and coverage statistics (e.g., what fraction of phishing emails in the test set contain at least one keyword from each principle).
**Expected benefit:** Improves transparency about metric limitations.

### Suggestion 7: Restructure Conclusion to include limitations (Must, P1)

**Location:** Page 10 - Section 5
**Action:**
Adopt a three-part structure: (1) validated findings with bounded claims, (2) limitations (including proxy evaluation metrics, small human evaluation sample, no statistical significance, L=100 truncation), (3) prioritized future work (ground-truth annotation collection, webpage phishing extension, LLM embedding investigation).
**Mentor Revised Framework:**
"AI2TALE achieves strong results on seven email datasets under the compared metrics. Key limitations include: (a) proxy-based evaluation without ground-truth sentence annotations, (b) no statistical significance reporting, (c) small-scale human evaluation without baseline comparison. Future work should prioritize collecting sentence-level ground-truth annotations for direct selection quality evaluation, statistically rigorous evaluation."

## Storyline Options + Writing Outlines
### Current Storyline Diagnosis

The current introduction (Pages 1-2) uses the following structure:
- P1: Background on phishing attacks and cognitive triggers (defines problem, establishes stakes).
- P2: AI successes + phishing detection methods + LLM phishing work (dense citation list, mixed roles).
- P3: Gap statement + research question + problem definition + contribution list (most effective paragraph).

**Strengths of current structure:** The gap is clearly stated (lack of intrinsic explainability). The research question is explicit. The distinction between detection and localization is well-motivated.

**Weaknesses:** P2 tries to cover too much (general AI → phishing detection → LLMs) without a clear argumentative arc. The transition from general AI successes to phishing detection is abrupt. The contribution list uses vague language ("important problem," "innovative").

### Proposed Storyline Option A (Recommended): Problem-Gap-Solution-Evidence

**Abstract Outline (complete):**
- S1: Phishing attacks remain a critical security challenge; existing AI detection lacks sentence-level explainability.
- S2: We introduce AI2TALE, a method combining mutual information maximization and information bottleneck regularization to localize phishing-triggering sentences using only document-level labels.
- S3: Experiments on seven datasets (~40K emails) show AI2TALE achieves 99.33% Label-Accuracy and 98.95% Cognitive-True-Positive.
- S4: Individual metric improvements are ~0.85-0.93% over strongest baselines; combined-average improvement is 1.39-3.32%.
- S5: A human evaluation suggests the selected sentences align with perceived persuasion triggers.

**Introduction Outline (complete):**
- P1 (Motivation): Phishing email threats are growing; detection accuracy is high but explainability remains poor. Cite statistics from FBI/APWG reports. Define phishing attack localization as the missing capability.
- P2 (Prior Work Gap): Existing phishing detection methods (ML-based, LLM-based) predict labels but do not identify which specific sentences cause the classification. Existing interpretability methods (L2X, INVASE, VIBI, ICVH, AIM) can select informative features but lack two properties needed for this task: (i) they may select supersets rather than minimal subsets, and (ii) they may encode labels via selection patterns rather than semantic content.
- P3 (Proposed Solution): We propose AI2TALE, which addresses both gaps through (a) an information bottleneck regularizer that penalizes over-selection, and (b) a data-distribution mechanism that decouples classifier learning from selector patterns. The method works in a weakly supervised setting requiring only document-level labels.
- level labels.
- P4 (Contribution Summary + Roadmap): Four contributions — problem formalization, method, dual-metric evaluation design, extensive experiments. Brief preview.

### Proposed Storyline Option B: Application-First (Emphasis on Practical Deployability)

- P1: Same phishing background.
- P2: Focus on why explainability matters in practice (user trust, security training, compliance).
- P3: Existing solutions and their practical limitations (black-box detection, post-hoc explanations are insufficient).
- P4: AI2TALE as a practical solution with weakly supervised training.
This option is less recommended because it delays the technical gap too long.

### Alignment Checks for Option A

1. **Problem alignment:** The stated challenge (black-box detection lacks explanations) matches the proposed solution (sentence-level localization).
2. **Variable alignment:** Core concepts from introduction (phishing-relevant sentences, weakly supervised, mutual information, information bottleneck) all appear in the method section.
3. **Contribution-evidence alignment:** Contribution 1 (problem formalization) is supported by Section 3.1. Contribution 2 (method) is supported by Sections 3.2.1-3.2.3 and Algorithm 1. Contribution 3 (metrics) is supported by Section 4.2. The evidence is present but statistical reliability is weak (Issue 1).


### Title Revision Suggestion

**Current:** "AI2TALE: An Innovative Information Theory-Based Approach for Learning to Localize Phishing Attacks"
**Suggestion:** "AI2TALE: Weakly-Supervised Phishing Attack Localization via Information Bottleneck Sentence Selection"
**Rationale:** Replaces the promotional "innovative" with the method's key property (weakly-supervised) and specifies the technical approach (information bottleneck sentence selection). This is more informative for readers.

## Priority Revision Plan
### Ranked Error Board (Top 5)

| Rank | Issue | Severity | Validity Risk | Fixability | Confidence |
|------|-------|----------|---------------|------------|------------|
| 1 | No statistical significance/variance in Table 1 | Critical | High (core empirical claim unsupported) | High | High |
| 2 | Inflated improvement framing (1.5%-3.5% claim) | Major | Medium (misleading) | High | High |
| 3 | Human evaluation lacks baseline comparison | Major | Medium (overclaims usefulness) | High | High |
| 4 | Related Work is flat citation list | Moderate | Low (quality, not validity) | High | High |
| 5 | Data-distribution mechanism dynamics underspecified | Moderate | Low-Medium | High | High |

### P0 (Pre-submission critical — Must fix)

| Action | Location | Effort | Impact |
|--------|----------|--------|--------|
| Add variance/std over 3 seeds to Table 1 | Page 8, Table 1 | 1-2 days (re-runs) | Validates core empirical claim |
| Add significance tests (McNemar/bootstrap) | Page 8, Section 4.4 | 0.5 day (compute) | Statistical grounding |
| Rewrite improvement claims to distinguish individual vs. combined | Abstract, Section 4.4, Conclusion | 0.5 day (writing) | Prevents misleading readers |
| Add baseline comparison to human evaluation | Page 10, Section 4.4 | 2-3 days (new survey) | Transforms evaluation from suggestive to comparative |

### P1 (High priority — Strongly recommended)

| Action | Location | Effort | Impact |
|--------|----------|--------|--------|
| Restructure Related Work by comparison axes | Pages 2-3 | 0.5 day (writing) | Clear novelty positioning |
| Clarify alternating training dynamics in Algorithm 1 | Page 6-7 | 0.5 day (writing) | Reproducibility |
| Restructure Conclusion with limitations | Page 10 | 0.5 day (writing) | Balanced scientific messaging |
| Move E1D vs BERT comparison to main text | Section 4.4 | 0.5 day (writing) | Full disclosure |

### P2 (Quality improvement — Nice to have)

| Action | Location | Effort | Impact |
|--------|----------|--------|--------|
| Ablation study for data-distribution mechanism | Appendix 6.8 | 1-2 days (runs) | Validates claimed benefit |
| Cognitive-True-Positive metric transparency | Section 4.2, Appendix 6.3 | 0.5 day (writing) | Metric credibility |
| Report Likert distribution without collapsing | Page 10 | 0.5 day (analysis) | Transparent reporting |
| Title revision | Page 1 | 0.5 day | Reader engagement |

### Revision Sequencing

```
Phase A (P0 — before re-submission):
  1. Re-run Table 1 with 3 seeds, compute std + significance tests
  2. Draft and run improved human evaluation with baseline condition
  3. Rewrite improvement claims in Abstract, Results, Conclusion
  4. Restructure Conclusion to include limitations

Phase B (P1 — concurrent with Phase A):
  5. Restructure Related Work section
  6. Clarify data-distribution mechanism in Section 3.2.2
  7. Add E1D vs BERT discussion to main text

Phase C (P2 — if time permits):
  8. Run ablation experiments for data-distribution mechanism
  9. Improve Cognitive-True-Positive metric transparency
  10. Revise title
```

### Expected Impact After Fixes

- **P0 fixes alone:** Core empirical claim becomes statistically grounded; human evaluation becomes comparative. Validity risk drops from High to Low-Medium.
- **P0+P1:** Novelty positioning becomes clear; method description is reproducible; conclusion is balanced. Overall paper quality improves substantially.
- **P0+P1+P2:** Full methodological validation with ablation evidence; metric transparency; polished narrative.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Main comparison: AI2TALE vs 5 baselines (Label-Accuracy + Cognitive-TP) | 7 datasets, ~40K emails, 80/10/10 split, 10 epochs, E1D embeddings, Adam lr=1e-3 | Label-Acc, Cognitive-TP, combined avg | AI2TALE achieves 99.33% Label-Acc, 98.95% Cognitive-TP | C2 (method effective), C3 (metrics useful) | No variance/std; no significance tests; metric gains small |
| E2 | F1-score comparison (two scenarios) | Same as E1, but F1 on (i) phishing only (ii) both classes | F1-score, FPR, FNR | AI2TALE best F1=99.32%, FPR=0.451%, FNR=0.899% | C2 | Same variance limitation |
| E3 | BERT vs E1D embedding comparison | Same task with BERT encoder (EBERT) instead of E1D | Label-Acc, Cognitive-TP, FPR, FNR | E1D (99.33%) substantially outperforms EBERT (97.25%) | C2 (E1D variant) | Only one LLM tested (BERT); no analysis of why BERT underperforms |
| E4 | Information bottleneck + data-distribution ablation | Same setup, w/ and w/o IB term and data-distribution | Label-Acc, Cognitive-TP, FPR, FNR | With both: best across all metrics; without: matches second-best baseline | C2 (both components contribute) | Ablation partial (only reported in appendix 6.8); no separate analysis of each component's independent contribution |
| E5 | Hyperparameter sensitivity (λ, σ) | λ ∈ {0.1, 0.01, 0.001}, σ ∈ {0.1, 0.2, 0.3} | Label-Acc, Cognitive-TP, F1 | Low variance (Label-Acc: 0.0124, Cognitive-TP: 0.0852) | C2 (robustness) | Only two hyperparameters tested; no learning rate or temperature τ sensitivity |
| E6 | Human evaluation of top-1 sentence persuasiveness | N=25, 10 phishing emails, 5-point Likert scale | % Agree+Strongly Agree | 81% agreement | C2 (selected sentences are persuasive) | No baseline comparison; small sample; no inter-rater reliability |

### Research-Theme Gap Diagnosis

| Research Value Dimension | Current Support | Gap | Required Evidence |
|-------------------------|----------------|-----|-------------------|
| New knowledge (methodological) | Moderate — IB regularization + data-distribution mechanism is a novel combination | Statistical reliability unverified; comparison limited to 5 baselines | Variance reporting, significance tests, broader baseline comparison |
| Reproducibility | Good — code/data provided | Training dynamics of alternating optimization underspecified | Clearer Algorithm 1 explanation, hyperparameter sensitivity analysis |
| Impact on practice | Weak — human evaluation shows promise but limited design | No evidence that selected sentences improve end-user security outcomes vs alternatives | Comparative user study measuring actual phishing avoidance behavior |

### Proposed Research Experiments (P0/P1/P2)

**P0 Experiment: Statistical Validation of Main Results**
- **Target Claim:** "AI2TALE outperforms baselines on Label-Accuracy and Cognitive-TP"
- **Hypothesis:** AI2TALE achieves statistically significant improvement over the strongest baseline
- **Minimal Design:** Run all methods (AI2TALE + 5 baselines) with 3 random seeds each, same 80/10/10 split. Record mean±std for all metrics.
- **Controls/Baselines:** Same as current Table 1.
- **Metrics:** Label-Acc, Cognitive-TP, F1, mean±std, Cohen's d, paired bootstrap p-value.
- **Success Criterion:** AI2TALE shows p<0.05 (or bootstrap CI excludes zero) against the strongest baseline on at least one metric.
- **Estimated Cost/Time:** 1-2 GPU-days (6 methods × 3 seeds × ~4h each).
- **Expected Paper-Quality Gain:** Transforms core empirical claim from suggestive to statistically grounded.

**P0 Experiment: Comparative Human Evaluation**
- **Target Claim:** "AI2TALE provides more persuasive explanations than compared baselines for humans"
- **Hypothesis:** Top-1 sentences from AI2TALE are rated as more persuasive than those from the strongest baseline (AIM or ICVH).
- **Minimal Design:** Within-subjects: each participant sees sentences from AI2TALE AND a baseline method for 10 phishing emails (20 total, randomized order). Rate each on a 5-point persuasiveness scale.
- **Controls/Baselines:** AIM or ICVH (whichever has highest Cognitive-TP).
- **Metrics:** Mean persuasiveness rating (paired t-test), Fleiss' kappa for inter-rater agreement.
- **Success Criterion:** AI2TALE sentences rated significantly higher (p<0.05) than baseline.
- **Estimated Cost/Time:** 3-5 days (survey design + recruitment of N≥30).
- **Expected Paper-Quality Gain:** Converts the human evaluation from a single-arm pilot to a rigorous comparative study.

**P1 Experiment: Ablation of Data-Distribution Mechanism Components**
- **Target Claim:** "Data-distribution mechanism prevents degeneracy and improves generalization"
- **Hypothesis:** Each component of the mechanism contributes to final performance.
- **Minimal Design:** Compare 4 variants:
  1. Full AI2TALE (joint training + data-distribution mechanism)
  2. Without data-distribution mechanism (only Eq. 8, no Eq. 9)
  3. Data-distribution mechanism with full emails (r=1 vector instead of r~B(0.5))
  4. Data-distribution mechanism with different masking rates (p=0.3, 0.7)
- **Controls/Baselines:** Variant 1 = current AI2TALE; Variant 2 = ablation.
- **Metrics:** Label-Acc, Cognitive-TP, F1, FPR, FNR, selection sparsity (avg # sentences selected per email).
- **Success Criterion:** Variant 1 outperforms Variant 2 significantly; Variant 3 underperforms Variant 1 (confirming random masking matters).
- **Estimated Cost/Time:** 1-2 GPU-days.
- **Expected Paper-Quality Gain:** Validates the claimed benefit of the data-distribution mechanism.

**P1 Experiment: Beyond Top-1 Sentence**
- **Target Claim:** "Top-1 sentence provides concise explanation"
- **Hypothesis:** Using top-k sentences (k=2,3,5) improves Label-Accuracy over top-1.
- **Minimal Design:** Re-run evaluation using top-2, top-3, and top-5 sentences instead of top-1.
- **Controls/Baselines:** Current top-1 results.
- **Metrics:** Label-Accuracy at each k.
- **Success Criterion:** Characterize the trade-off between conciseness (k=1) and accuracy (k>1).
- **Estimated Cost/Time:** No new training needed; only inference modification.
- **Expected Paper-Quality Gain:** Provides practical guidance for deployment (users can choose conciseness vs. completeness).

### ASCII Diagram — Experiment Upgrade Plan

```text
Stage 1 (P0 — Pre-submission critical)
├── E1a: Re-run Table 1 with 3 seeds + std + significance tests
├── E6a: Redesign human eval with baseline comparison
└── Writing: Rewrite improvement claims + Conclusion

Stage 2 (P1 — High priority)
├── E4a: Full ablation of data-distribution components
├── E7: Top-k sentence evaluation (k=2,3,5) evaluation
└── Writing: Restructure Related Work + clarify training dynamics

Stage 3 (P2 — Quality improvement)
├── E3a: Investigate BERT underperformance (LR sweep, fine-tuning depth)
├── E5a: Learning rate and temperature τ sensitivity
└── E8: Error analysis — which emails are falsely positive/negative?
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

**Rationale:** The paper addresses a practically important problem with a technically sound method combining mutual information, information bottleneck regularization, and a data-distribution mechanism. The evaluation across seven datasets is extensive. However, the core empirical claim is weakened by the absence of statistical significance and variance reporting — the individual metric gains (~0.85-0.93%) could be within noise range. The improvement framing (1.5%-3.5%) inflates perceived gains by using a combined average. The human evaluation lacks a baseline comparison. Novelty verification is deferred due to external retrieval being unavailable. These issues collectively limit confidence in the paper's central claims.

**Score breakdown:**
- Research value / Contribution: 7/10 (practically important problem, technically sound method, but novelty unverified)
- Validity / Soundness: 5/10 (missing statistical significance, small-margin gains, human evaluation design gaps)
- Novelty: 6/10 (method combination appears novel but external verification deferred)
- Reproducibility: 7/10 (code/data provided, but training dynamics underspecified)
- Presentation / Clarity: 6/10 (Related Work is flat list, improvement framing misleading, conclusion lacks limitations)

**Post-Revision Target: [7.5, 8.5] / 10**

**Rationale:** If the authors address the P0 items (add variance/significance to Table 1, redesign human evaluation with baseline comparison, restructure improvement claims, add limitations to conclusion), the paper's validity and clarity would substantially improve. The P1 items (restructured Related Work, clarified training dynamics) would further strengthen positioning and reproducibility. The upper bound of 8.5 assumes all P0+P1 items are addressed and the method's superiority is statistically confirmed. The lower bound of 7.5 assumes only P0 items are addressed.