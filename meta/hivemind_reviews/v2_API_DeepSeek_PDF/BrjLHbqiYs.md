## Summary
# Final Review Report

## Summary

This paper studies the problem of quantifying multimodal interactions (redundancy, uniqueness, synergy) in a semi-supervised setting where only labeled unimodal data D1, D2 and unlabeled multimodal data DM are available. The authors derive two lower bounds on synergy (SR based on redundancy, SU based on modality disagreement) and one upper bound (S based on min-entropy couplings). They validate these bounds on 100,000 synthetic binary distributions and 10 real-world datasets from MultiBench. The bounds track true synergy directionally (e.g., increasing from MOSEI to MUStARD), though gaps remain — the lower bounds are reasonably tight (average gap 0.18 bits) while the upper bound is looser (average gap 0.62 bits). The paper further applies these bounds to estimate optimal multimodal model performance before training and to guide data collection and model selection decisions.

**Core strength:** The theoretical framework connecting PID, modality disagreement, and min-entropy couplings is novel and well-motivated. The semi-supervised setting is practically relevant.

**Major weaknesses:** (1) Estimated upper bounds on accuracy exceed 1.0 (up to 163%) in Table 3, which is not a valid probability — this undermines the quantitative reliability of the performance estimation pipeline. (2) The gap between theoretical guarantees (proven for exact discrete distributions) and empirical practice (clustering-based approximation) is not theoretically bounded. (3) The performance estimation interval is often too wide (e.g., [52%, 107%]) to provide precise actionable guidance, and the midpoint heuristic lacks theoretical justification. (4) The correlation evidence for data collection guidance (ρ=0.21 on n=6 datasets) is too weak to support strong conclusions. (5) Novelty claims cannot be fully verified in this run (Retrieval-Disabled Mode active), but the paper's contribution as presented relies on well-known PID definitions and information-theoretic bounds applied to a new setting — the incremental contribution should be carefully scoped.

## Strengths
1. **Well-motivated problem formulation.** The semi-supervised multimodal interaction quantification setting (labeled unimodal data + unlabeled multimodal data) is realistic and addresses an important gap: prior work either requires fully labeled multimodal data (supervised) or measures interactions only through trained model attributions. The paper's framing of "data-level" vs "model-level" interactions is a clean distinction.

2. **Rigorous theoretical foundation.** The paper builds on a principled PID framework (Bertschinger et al., 2014) and provides four theorems with complete proofs (including an NP-hardness reduction from RTT). The connections drawn between synergy, redundancy, disagreement, and min-entropy couplings are mathematically sound and represent genuine theoretical synthesis.

3. **Empirical validation across diverse datasets.** The experiments cover 10 real-world datasets spanning sentiment analysis, sarcasm detection, humor detection, medical prediction, VQA, and UI classification — totaling over 700,000 datapoints. This breadth strengthens the empirical claims about the bound properties.

4. **Practical applications.** The downstream applications (performance estimation, data collection guidance, model selection) are clearly motivated and the results, while mixed in precision, show directional consistency. The practical utility of computing bounds before training any model is a real value proposition.

5. **Transparency about limitations.** The paper acknowledges three specific limitations (cluster preprocessing errors, difficulty with ENRICO-like datasets, unknown data generation process) and discusses failure cases honestly. This scientific candor is commendable.

## Weaknesses
1. **Probability bounds exceeding 1.0 (Major).** The estimated upper bounds on accuracy in Table 3 exceed 1.0 for all datasets (e.g., 1.07 on MOSEI, 1.63 on MUStARD). Since accuracy is a probability in [0,1], these values are not interpretable as accuracy bounds. The formula from Theorem 5 does not enforce the natural cap at 1, and the paper does not apply a min(1,·) truncation. This inflates the "estimated average" PM and may mislead readers about the tightness of the bounds.

2. **Theory-practice gap for continuous modalities (Major).** The lower and upper bound theorems (Theorems 1-4) are proven for exact distributions over finite discrete spaces. When applied to continuous real-world data, the paper uses clustering (PCA + K-means with 20 clusters) to discretize. The error introduced by this discretization is not theoretically bounded, and the claimed "bounds always hold" (Page 5, line 38-39) applies only to the clustered distribution, not the original continuous one. This gap between theory and empirical application is under-discussed.

3. **Performance estimation interval is too wide for practical use.** The interval [lower, upper] for performance has a typical width of 0.55 (e.g., MOSEI: [0.52, 1.07], width=0.55). The midpoint heuristic is not theoretically justified — the paper proposes it as a practical summary (Page 9, line 18: "estimated average PM = (P_acc + P̅_acc)/2") without formal guarantees. The claim that estimates "closely predict actual model performance" (Abstract, Page 1) overstates what the interval-width evidence supports.

4. **Weak statistical evidence for data collection guidance (Minor).** The correlation between estimated PM and multimodal-unimodal gain is ρ=0.21 (Page 9, Figure 3 left), rising to 0.53 when excluding MIMIC. With n=6 datasets, neither value is statistically meaningful. The paper acknowledges this implicitly but still presents it as actionable guidance. A caveat about sample size is needed.

5. **Novelty scope cannot be fully assessed (Deferred).** Due to Retrieval-Disabled Mode in this run, external literature comparison is unavailable. The paper builds on established PID definitions (Bertschinger et al., 2014) and known bounds (Feder & Merhav, 1994; Fano, 1968). The primary novelty is applying these to the semi-supervised setting and connecting them to disagreement and min-entropy couplings. The incremental nature of these connections needs external verification.

## Key Issues
### Issue 1 (Major): Upper bounds on accuracy exceed 1.0
- **Location:** Page 8 - Table 3, Page 9 - Theorem 5
- **Problem:** Estimated upper bound values of 1.07, 1.21, 1.29, 1.63, 1.27 are presented as accuracy values but exceed the maximum possible value of 1.0.
- **Root cause:** Theorem 5's bound (P_acc ≤ (Ip + 1)/log|Y|) does not enforce the probability constraint P_acc ≤ 1. When Ip is large relative to log|Y|, the bound exceeds 1.
- **Impact:** (1) The midpoint (lower+upper)/2 becomes inflated. (2) Readers may question the entire estimation framework's reliability. (3) The claim of "tight bounds" is undermined.
- **Fix:** Apply min(1, ·) truncation to the upper bound. Revise text to state the effective bound. Update Table 3 to cap at 1.00.

### Issue 2 (Major): Theory-practice gap in bound guarantees
- **Location:** Page 4 - Remark on high-dimensional continuous modalities, Page 7 - Table 1
- **Problem:** Theorems 1-4 provide formal bounds for exact discrete distributions. The empirical pipeline uses PCA + clustering to estimate these distributions, introducing uncontrolled approximation error.
- **Root cause:** The bound proofs rely on exact marginals p(x1,y), p(x2,y), p(x1,x2). Clustering replaces these with estimates whose quality depends on K, cluster algorithm, and feature representation.
- **Impact:** The claim "bounds always hold" (Page 5) applies strictly only to the theoretical quantities, not the empirical estimates. The error magnitude is not characterized.
- **Fix:** Add explicit acknowledgment that empirical bounds are estimates, not theoretical guarantees, when using clustering. Consider sensitivity analysis over cluster count K.

### Issue 3 (Major): Quantitative overclaim on performance estimation accuracy
- **Location:** Page 1 - Abstract, Page 9 - RQ1 paragraph
- **Problem:** The abstract claims bounds "accurately track true interactions" and "closely predict multimodal model performance," but the intervals are very wide (e.g., [52%, 107%] for MOSEI).
- **Root cause:** The midpoint average lacks theoretical justification — it is a heuristic.
- **Impact:** Overclaiming can mislead readers about the practical precision of the method.
- **Fix:** Replace "accurately track" and "closely predict" with "directionally track" and "provide useful qualitative guidance." Report interval width as an uncertainty measure.

### Issue 4 (Minor): Weak statistical basis for data collection guidelines
- **Location:** Page 9 - RQ2, Figure 3
- **Problem:** Correlation ρ=0.21 on n=6 datasets is not statistically meaningful.
- **Fix:** Add explicit caveat about small sample size. Recommend future validation on more datasets.

### Issue 5 (Minor): Introduction gap-framing can be sharper
- **Location:** Page 1 - Introduction paragraphs 1-2
- **Problem:** The introduction presents supervised advances before clearly stating the semi-supervised gap.
- **Fix:** Restructure to: Big Picture → Open Problem (semi-supervised) → Prior Work Gap → Solution → Evidence Preview.

## Actionable Suggestions
### S1 (Must, High Impact): Cap upper bounds at 1.0 in Table 3 and Theorem 5
- **What:** Apply min(1, ·) to the upper bound in Theorem 5 and Table 3. Replace values >1 with 1.00.
- **Where:** Page 8 - Table 3, Page 9 - Theorem 5.
- **Why:** Ensures bounds are valid probabilities and avoids misleading interpretations.
- **Revised Theorem 5 text:** Add: "Since P_acc ≤ 1 by definition, the effective upper bound is min(1, (Ip({X1, X2}; Y) + 1)/log|Y|)."

### S2 (Must, High Impact): Acknowledge the theory-practice gap explicitly
- **What:** Add a paragraph after the clustering Remark (Page 4) clarifying that clustering converts theoretical bounds into empirical estimates, and the "bounds always hold" claim applies to the exact discrete formulation, not the clustered estimates.
- **Where:** Page 4 - Remark on high-dimensional continuous modalities.
- **Revised text:** "Importantly, the bounds in Theorems 1-4 are proven for exact distributions over discrete spaces. When clustering is used to approximate continuous modalities, the computed quantities are empirical estimates of these bounds. The approximation error depends on clustering quality and granularity; we study empirical robustness in Appendix C.4."

### S3 (Must, Medium Impact): Calibrate performance estimation claims
- **What:** Rephrase "closely predict" and "accurately track" throughout the paper to reflect the actual interval widths and uncertainty.
- **Where:** Page 1 - Abstract, Page 9 - RQ1.
- **Revised abstract sentence:** "We validate these estimated bounds on synthetic and real-world datasets; the lower bounds track true synergy from below (average gap 0.18 bits) while the upper bound is looser (average gap 0.62). The bounds provide useful qualitative guidance for performance estimation, data collection, and model selection."
- **Revised RQ1 text (Page 9):** "The estimated interval [52%, 107%] encompasses the true model performance range (82-88%), providing directional guidance rather than precise quantitative prediction."

### S4 (Nice-to-have, Medium Impact): Add caveat about small-sample correlations
- **What:** Add a sentence in RQ2 (Page 9) noting that correlations are based on only 6 datasets.
- **Revised text:** "Given the limited number of datasets (n=6), these correlations should be interpreted as qualitative trends rather than statistically validated relationships. Expanding to more datasets would strengthen this analysis."

### S5 (Nice-to-have, Low Impact): Strengthen limitation 2 in Conclusion
- **What:** Replace the generic second limitation with a more specific future direction.
- **Where:** Page 10 - Conclusion.
- **Revised text:** "2. It is harder to quantify interactions when multiple interaction types (R, U1, U2, S) are all significant simultaneously, as on ENRICO. Future work could explore combined lower bounds that jointly leverage redundancy and uniqueness constraints rather than taking their max."

## Storyline Options + Writing Outlines
### Current Introduction Structure
| Paragraph | Role | Issue |
|-----------|------|-------|
| P1 | Establish supervised multimodal interaction research | Gap (semi-supervised) is not stated until P2 |
| P2 | Define semi-supervised setting with Di, DM | Good concrete scenario, but follows rather than leads |
| P3 | List contributions | Clear but uses "naturally yield" overstatement |

### Recommended Abstract Outline (4-5 sentences)
S1 (Problem): "Understanding how modalities interact — through shared, unique, and synergistic information — is a core challenge in multimodal learning, but most approaches require labeled multimodal data that is often unavailable."

S2 (Gap): "In many real-world settings, only labeled unimodal data and unlabeled multimodal data are available, making direct interaction quantification infeasible."

S3 (Solution): "We derive lower and upper bounds on multimodal synergy using only these semi-supervised resources, based on redundancy, modality disagreement, and min-entropy couplings."

S4 (Evidence): "Experiments on synthetic and 10 real-world datasets show the lower bounds track true synergy from below (average gap 0.18 bits), with the upper bound tighter for high-synergy data."

S5 (Implications): "These estimates enable performance prediction, data collection guidance, and model selection without training multimodal models."

### Recommended Introduction Outline (5 paragraphs)
P1 — **Big Picture and Open Problem** (revised from current P1):
"State the core challenge (multimodal interactions). Immediately state that most existing methods require fully labeled multimodal data. Define the realistic semi-supervised setting with Di and DM as the focus of this paper."

P2 — **Prior Work and Gap** (revised from current P2 first half):
"Review prior work on model-level interaction quantification (Shapley values, integrated gradients, Hessel & Lee). Identify gap: these measure interactions captured by models, not interactions in data. Data-level quantification enables pre-training analysis."

P3 — **PID Foundation** (short bridge paragraph):
"Introduce PID as the formal framework for defining R, U1, U2, S. Note that R, U1, U2 can be computed from Di alone, but S requires the full joint distribution — motivating our bounds."

P4 — **Technical Approach** (revised from current P3):
"State contributions as: (1) lower bound SR via redundancy, (2) lower bound SU via modality disagreement, (3) upper bound S via min-entropy couplings. Mention NP-hardness and approximation."

P5 — **Summary of Results and Applications**:
"Preview empirical validation on 10 datasets. Describe three applications: performance estimation before training (Theorem 5), data collection guidance, and model selection."

### Alternative Storyline Option (for a more applied audience)
Restructure the paper to lead with the applications rather than the theory. The current order (Theory → Applications) is appropriate for ICLR; for a more applied venue, consider:
- Start with the practical question: "Can I estimate multimodal model performance without training any multimodal model?"
- Present the bounds as the answer to this question
- Defer the PID details and NP-hardness to later sections

## Priority Revision Plan
| Priority | Action | Location | Expected Impact | Effort |
|----------|--------|----------|----------------|--------|
| **P0** | Cap upper bounds at 1.0 and revise Theorem 5 | Table 3, Theorem 5 | Eliminates invalid probability values; fixes a factual error | Low (text + math edit) |
| **P0** | Acknowledge clustering approximation gap explicitly | Page 4 Remark | Prevents over-claiming of theoretical guarantees for empirical estimates | Low (one paragraph) |
| **P1** | Calibrate "accurately track" / "closely predict" language throughout | Abstract, RQ1, Conclusion | Improves scientific defensibility; aligns claims with evidence | Medium (multi-location edits) |
| **P1** | Add caveat about small-n correlations in RQ2 | Page 9 RQ2 paragraph | Prevents over-interpretation of weak statistical evidence | Low (one sentence) |
| **P2** | Revise introduction narrative order: gap-first | Page 1 Introduction | Improves reader engagement and clarity | Medium (restructure) |
| **P2** | Strengthen limitation 2 with future direction | Page 10 Conclusion | Turns weakness into research opportunity | Low (rephrase) |

### Revision Strategy Roadmap (ASCII Diagram)
```text
[Current paper: solid theory, mixed empirical precision]
    |
    ├── P0 Fixes (must-do before resubmission)
    |   ├── Cap accuracy bounds at 1.0 (Table 3, Theorem 5)
    |   └── Acknowledge clustering approximation gap (Page 4)
    |   └── Expected: no invalid probability values; honest theory-practice framing
    |
    ├── P1 Improvements (should-do)
    |   ├── Calibrate claim language (Abstract, RQ1, Conclusion)
    |   └── Add small-n caveat for correlations (Page 9)
    |   └── Expected: claims match evidence strength
    |
    └── P2 Enhancements (nice-to-have)
        ├── Restructure introduction for gap-first narrative
        └── Strengthen limitation discussion
        └── Expected: improved narrative flow and completeness
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Verify lower/upper bounds track true synergy on synthetic data | 100,000 binary (0/1) distributions from 8-dim simplex | S - SR, S - SU, S - S gaps, | Lower bounds track from below (avg gap 0.18), upper bound looser (avg gap 0.62) | C1 (bounds track synergy) | No structure/parameter sweep on distribution types |
| E2 | Validate bounds on real-world data | 10 MultiBench datasets; PCA + K-means clustering (K=20) for discretization | SR, SU, S vs true S (oracle) | Lower bounds track trends on MOSEI→MUStARD; ENRICO failure case identified | C1 (bounds track synergy) | Clustering quality not varied; only K=20 tested |
| E3 | Compare bounds to other interaction measures | Synthetic generative model data (R-only, U-only, S-only tasks) | R, U1, U2, S estimates | PID-based estimates more consistent with ground truth than I-min, WMS, CI | C1 (PID definition advantageous) | Only synthetic tasks; no real-world comparison |
| E4 | Robustness to imperfect unimodal classifiers | UR-FUNNY, MOSI; label noise 0.0-0.8 | S - lower bound, upper bound - S | Bounds stable under noise | C1 (bounds robust) | Only two datasets; only label noise tested |
| E5 | Estimate multimodal model performance | MOSEI, UR-FUNNY, MOSI, MUStARD, MIMIC, ENRICO | P_acc(lower), P_acc(upper), PM | Intervals contain true performance; directional ordering correct | C3 (performance estimation) | Upper bound >1; midpoint heuristic unjustified |
| E6 | Data collection guidance (RQ2) | Same 6 datasets as E5 | ρ(PM, multimodal-unimodal gain) | ρ=0.21 (0.53 w/o MIMIC) | C3 (data collection) | Only 6 datasets; weak correlation |
| E7 | Model selection guidance (RQ3) | Same 6 datasets as E5 | ρ(PM, complex-simple gap) | ρ=0.77 | C3 (model selection) | Only 6 datasets; complex fusion models not exhaustive |
| E8 | Self-supervised learning via disagreement (Appendix E) | Social-IQ; MERLOT Reserve pretraining | Accuracy | Disagreement-aware loss improves over agreement-only baseline | C2 (disagreement→synergy) | Limited to one pretraining framework |

### Research-Theme Gap Diagnosis
- **New knowledge:** The theoretical connections (synergy↔redundancy, synergy↔disagreement) are genuinely novel. The main research value gap is in *quantifying* these connections' practical precision — the bounds are directionally correct but quantitatively loose.
- **Reproducibility/reusability:** Code is available. The bound computation is simple (<1 min for clustered data). However, the clustering preprocessing step (PCA + K-means with K=20) introduces experimenter degrees of freedom that should be justified.
- **Impact on practice:** The data collection and model selection guidelines are currently based on weak statistical evidence (n=6, ρ=0.21). Strengthening this evidence is essential for practical adoption.

### Proposed Research Experiments

| Exp ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Quality Gain |
|--------|-------------|------------|---------------|-------------------|---------|------------------|-----------|-------------|
| PE1 (P0) | C3: Performance estimation | Bounds with min(1,·) cap provide valid probability guidance | Recompute Table 3 with upper bound = min(1.0, (Ip+1)/log|Y|); recompute PM | Original unbounded version | Valid probability range | All PM values ∈ [0,1] | Low (recompute only) | Eliminates numerical error |
| PE2 (P1) | C1: Clustering robustness | Bound trends are stable across K | Vary cluster count K ∈ {5, 10, 20, 50}; recompute bounds | K=20 baseline | Rank correlation of bound ordering | Same dataset ordering for K≥10 | Low (script change) | Strengthens empirical reliability |
| PE3 (P1) | C3: Data collection value | Bounds predict gains on more datasets | Add 4+ datasets from MultiBench not currently tested (e.g., TVQA, Social-IQ) | Current 6-dataset baseline | ρ(PM, gain) with significance test | ρ > 0.5 with p < 0.05 | Medium (model training) | Critical for statistical credibility |
| PE4 (P2) | C2: Disagreement → synergy | Bounds improve when combining SR and SU | Derive combined lower bound S_joint = max(SR, SU, f(SR, SU)) for mixed-interaction datasets | ENRICO case | Gap between S_joint and true S | Closer to S than max(SR, SU) alone | High (theoretical derivation) | Addresses ENRICO failure mode |

```text
ASCII Diagram — Experiment Upgrade Plan

[Current experiments: 8 completed (E1-E8)]
    |
    ├── P0 Fix (immediate)
    |   └── PE1: Cap upper bounds at 1.0 → valid probability bounds
    |
    ├── P1 Strengthen (next submission)
    |   ├── PE2: Cluster count sensitivity (K=5,10,20,50)
    |   ├── PE3: Expand to 4+ more datasets
    |   └── Expected: robust bound ordering + statistical significance
    |
    └── P2 Research extension (future work)
        └── PE4: Combined lower bound SR+SU for mixed interactions
        └── Expected: tighter bounds on ENRICO-like datasets
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

*Rationale:* The paper presents a well-motivated theoretical framework with rigorous derivations, connecting PID-based interaction quantification to semi-supervised settings. The experimental validation across 10 datasets demonstrates directional consistency. However, the score is constrained by several validity-critical weaknesses: (1) estimated accuracy upper bounds exceeding 1.0 (a numerical error that undermines quantitative interpretation), (2) a significant theory-practice gap between the discrete-space bound theorems and the clustering-based empirical pipeline, and (3) overclaimed performance prediction accuracy that does not match the actual interval width. The novelty (applying PID to the semi-supervised setting and connecting to disagreement/min-entropy couplings) is conceptually sound but the incremental contribution relative to existing PID literature cannot be fully verified in this run. The primary scoring dimension is research value — the framework enables useful qualitative guidance (dataset ordering, model selection trends) but does not yet provide the quantitative precision that the paper's language sometimes implies.

**Post-Revision Target: [7.0, 7.5]/10**

*Rationale:* If the authors (1) cap upper bounds at 1.0, (2) explicitly acknowledge the theory-practice gap from clustering, (3) calibrate claim language to match evidence strength, and (4) add cluster-count sensitivity analysis (PE2) and more datasets for statistical credibility (PE3), the paper could reach 7.0-7.5. This target assumes the core theoretical contribution remains valid and the incremental novelty is confirmed by external literature review. Without external novelty verification, the upper bound of the target is 7.0 rather than 7.5.