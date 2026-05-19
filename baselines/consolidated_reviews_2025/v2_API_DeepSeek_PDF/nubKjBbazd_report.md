## Summary
# Final Review Report

## Summary

This paper proposes Adversarial Perturbation Dropout (APD), a method to improve the transferability of adversarial examples across deep neural network models. The core idea is to break the "synergy" between perturbation regions by dropping (resetting to clean values) square regions of the perturbation during the attack optimization process. At each iteration, multiple masked versions of the adversarial example are generated (varying in dropped region center and size), their gradients are averaged, and the update proceeds on the averaged gradient. Class activation maps (CAM) are used to guide the selection of dropped regions toward attention-critical areas.

The paper evaluates APD on ImageNet across multiple source/target model pairs (Inc-v3, Inc-v4, IncRes-v2, Res-101) including adversarially trained defenses and diverse architectures (ViT, Sequencer, MnasNet). Integrated with baselines such as MI-FGSM, DIM, TIM, SIM, AAM, and AA-TI-DIM, APD shows consistent improvements, with average gains of 9-15 percentage points in attack success rate.

**Overall assessment:** The paper tackles a genuine problem (improving adversarial transferability) with a conceptually clean idea. The experimental results are positive across many settings. However, the manuscript has several substantial weaknesses: (1) the central "synergy" concept lacks formal definition and quantification, (2) the empirical evaluation lacks statistical significance testing, (3) claim language frequently overstates the evidence (SOTA claims without sufficient comparison scope), (4) the related work section is organized as a flat citation list rather than a structured comparison, and (5) the algorithm description contains inconsistencies between text and pseudocode. The novelty of perturbation dropout relative to existing masking/ensemble methods needs clearer positioning. External literature verification is unavailable in this run (Retrieval-Disabled Mode); novelty/comparison conclusions are marked as deferred manual verification.

## Strengths
**S1. Clear problem motivation and intuitive solution.** The paper identifies a genuine limitation of existing transferability methods — that joint optimization of perturbations creates dependencies (synergy) between regions, which hurts transfer when the target model attends to only a subset. The proposed solution of dropping perturbation regions is intuitively appealing and clearly explained. This problem-solution alignment is the paper's strongest conceptual asset.

**S2. Consistent and sizable empirical gains.** Across all four source models and seven target models, APD consistently improves ASR over baseline methods. The improvements are particularly notable on normally trained models (average +12.7 pp) and on diverse architectures like Seq2d LSTM (+13.3 pp) and ViT-B/16 (+11.3 pp). The consistency of improvement across settings supports the robustness of the method.

**S3. Seamless integration with existing methods.** APD can be integrated with multiple existing attack methods (MI-FGSM, DIM, TIM, SIM, AAM, AA-TI-DIM) with consistent improvements. This modularity enhances the practical utility of the approach — practitioners can add APD to their preferred attack pipeline without redesigning the attack.

**S4. Ablation studies on key hyperparameters.** The paper provides ablation experiments for block size β, number of centers, and number of scales, showing the sensitivity of the method to these parameters. The finding that performance saturates at reasonable values (e.g., 3-4 centers, 5-7 scales) helps guide practical usage.

**S5. Evaluation on defended models and diverse architectures.** Beyond standard ImageNet classifiers, APD is tested on feature denoising (FD), purification defense (NRP), and architectures including ViT and MnasNet. This broad evaluation strengthens the claim of general applicability.

## Weaknesses
**W1. Undefined "synergy" concept.** The paper's central conceptual contribution — that perturbation "synergy" harms transferability — is never formally defined or quantified. The concept is used throughout as an intuitive explanation but lacks: (a) a mathematical definition (e.g., gradient correlation, mutual information, or alignment metric), (b) a direct measurement in experiments, and (c) a controlled test that isolates synergy from confounding factors (e.g., region size, gradient magnitude). The selective noise removal experiment (Figure 1b) provides correlational but not causal evidence. This weakens the paper's fundamental claim.

**W2. Missing statistical significance and variance reporting.** All results in Tables 1-4 are point estimates without standard deviations, confidence intervals, or significance tests. Given that many improvements are modest (e.g., 6.8 pp for AA-TI-DIM, 1.5 pp on NRP defense), readers cannot assess whether these gains are statistically reliable. Multiple seeds are standard practice in adversarial attack research; their absence is a significant methodological limitation.

**W3. Overclaimed and imprecise language throughout.** The manuscript uses numerous overclaims: "outperforms state-of-the-art methods" (no comprehensive SOTA comparison provided), "high attack efficiency" (no efficiency metric measured), "significant margin" (undefined), "robust perturbations" (robust to what?), "great inspiration" (speculative). The abstract claims SOTA status without specifying comparison methods or conditions. This pattern of overclaiming reduces scientific credibility.

**W4. Related work is a flat citation list.** Sections 2.1-2.2 list references without categorization, comparison, or critical analysis. The eight methods cited in a single parenthetical block are not grouped by approach type (momentum, input transformation, ensemble, region-based). The paper does not differentiate APD from the most relevant prior work (e.g., PI-FGSM for patch-based attacks, Wu et al. 2022 for guided masking, Cutout-based methods). This weakens the novelty positioning.

**W5. Algorithm description inconsistencies.** (a) Algorithm 1 (line 5) limits n to "less than 3" (i.e., ≤2), while the main text (Page 6) says "limit it to 3." (b) Algorithm 1 line 18 uses "Update xadv_{t+1} by ??" — an unresolved placeholder. (c) The main equation uses notation xdrop_{tjk} but does not specify whether gradients are computed with respect to xdrop or x^{adv}_t — a critical implementation detail.

**W6. Narrow novelty positioning relative to existing methods.** The paper does not clearly distinguish APD from existing approaches that also modify gradient computation via masking/ensembling. The Cutout comparison (Appendix A.2) is relegated to the appendix but should be front-and-center in the main evaluation. The paper does not discuss how APD relates to the large body of work on input diversity, gradient smoothing, and ensemble-based attacks.

**W7. Computational cost not properly analyzed.** APD requires nm forward passes per iteration (e.g., 3 centers × 5 scales = 15 forward passes vs. 1 for standard I-FGSM). While Appendix A.3 provides a control (MI-FGSM with 15× iterations), this does not fully address the cost concern because the 15× iteration baseline uses the same total compute but a different optimization trajectory. A proper cost-vs-benefit analysis is needed.

**W8. Limited defense evaluation scope.** The defense models section (4.3) only compares APD against a single baseline (AA-TI-DIM). Gains are modest (2.6% average) and no analysis is provided for why APD helps less against defenses than against undefended models. The NRP defense results (1.5-1.9 pp gain) are particularly weak.

**W9. Language quality issues.** Multiple grammatical errors reduce readability: "behide" → "behind", "outperform" → "outperforms", "are demonstrate" → "are demonstrated", "dissatisfactory transferability" → "unsatisfactory transferability". Redundant phrasing and awkward constructions occur throughout.

## Key Issues
### Issue 1 (Major): Algorithm inconsistency — unresolved placeholder and conflicting constraints
**Location:** Page 6 - Method: update equation; Page 13 - Algorithm 1
**Evidence:** Algorithm 1 line 18 says "Update xadv_{t+1} by ??" — a clear placeholder. Line 5 limits n to "less than 3" (≤2) but main text says "limit it to 3." The main equation lacks clarity on gradient computation reference variable.
**Impact:** These issues collectively break reproducibility. A reviewer or practitioner cannot implement APD from the manuscript without guessing critical details.
**Fix:** Replace "??" with the correct equation. Align n limit between text and algorithm (use "at most 3"). Clarify that gradients are computed w.r.t. x^{adv}_t (not xdrop). See annotation ID 7eaa4159.

### Issue 2 (Major): Overclaimed SOTA and efficiency language
**Location:** Page 1 - Abstract; Page 3 - Contribution list; Page 7 - Results analysis; Page 9 - Conclusion
**Evidence:** Abstract says "outperforms state-of-the-art methods" without specifying comparison scope. "High attack efficiency" is never measured. Conclusion claims "superior performance" and "great inspiration." No confidence intervals or variance reported.
**Impact:** Overclaiming invites reviewer skepticism and may lead to rejection at top venues where rigorous claim-evidence alignment is required.
**Fix:** Replace SOTA claims with bounded statements: "APD achieves competitive or superior results against evaluated baselines under tested settings." Remove "efficiency" claims unless efficiency metrics are provided. Add statistical significance testing.

### Issue 3 (Major): Undefined "synergy" concept without formal quantification
**Location:** Throughout — Pages 1-5, especially Introduction and Motivation paragraphs
**Evidence:** The term "synergy" is used ~15 times but never formally defined. The only supporting experiment (selective vs random noise removal, Fig 1b) shows correlation but not causation. No synergy metric is computed.
**Impact:** The paper's central conceptual contribution rests on an intuitive but unverified claim. If synergy cannot be measured, the improvement mechanism of APD is not empirically established.
**Fix:** (a) Provide a mathematical definition (e.g., gradient agreement between regions). (b) Compute synergy scores before and after APD. (c) Add a controlled experiment isolating synergy from confounds.

### Issue 4 (Major): Missing statistical significance and variance
**Location:** Pages 7-8 - Experiment Results (Tables 1-4)
**Evidence:** All ASR values are single-run point estimates. Standard deviations, confidence intervals, and significance tests are absent. Many improvements are small (1.5-6.8 pp on defense models).
**Impact:** Without variance estimates, readers cannot distinguish genuine improvement from random variation. This is a fundamental methodological gap for an empirical paper.
**Fix:** Report mean and std over ≥3 random seeds. Add paired significance tests (e.g., McNemar's test) against strongest baseline. Indicate statistically insignificant results.

### Issue 5 (Major): Related work organized as flat list rather than structured comparison
**Location:** Pages 3-4 - Sections 2.1 and 2.2
**Evidence:** Section 2.1 lists 8 references in a single parenthetical block without categorization. No method family grouping. No explicit differentiation between APD and the most relevant prior methods (PI-FGSM, guided masking, Cutout-based attacks).
**Impact:** Readers cannot quickly situate APD within the literature. The novelty positioning is unclear, and the paper misses opportunities to highlight its differentiation.
**Fix:** Restructure into method families (gradient modification, input transformation, region-based masking). Add explicit comparison table: method | mechanism | key difference from APD.

## Actionable Suggestions
### Suggestion A (Must fix): Fix algorithm inconsistency and unresolved placeholder
- **Action:** Replace "Update xadv_{t+1} by ??" in Algorithm 1 line 18 with the correct gradient ascent update equation from the main text. Change "n is limited to less than 3" to "n is limited to at most 3" to match the main text.
- **Location:** Page 13 - Algorithm 1, lines 5 and 18
- **Expected benefit:** Reproducibility restored.

### Suggestion B (Must fix): Add statistical significance and variance reporting
- **Action:** Re-run all experiments with at least 3 random seeds. Report ASR as mean ± std. Add paired significance tests (McNemar's test or paired t-test) comparing APD-augmented methods against their baselines. In Table 1, indicate statistically insignificant improvements.
- **Location:** Pages 7-8 - All result tables and analysis paragraphs
- **Expected benefit:** Scientific credibility of empirical claims.

### Suggestion C (Must fix): Define "synergy" formally and measure it
- **Action:** (a) Provide a mathematical definition of perturbation synergy, e.g., the average cosine similarity between gradient contributions of different image regions: Synergy = (1/|R|²) Σ_{i,j∈R} cos(g_i, g_j) where g_i is the gradient restricted to region i. (b) Compute synergy scores for APD-generated vs. baseline perturbations and show that APD reduces synergy. (c) Add a controlled experiment where region size is held constant to isolate the synergy effect.
- **Location:** Pages 2-3 - Introduction/Motivation; Page 5 - Method
- **Expected benefit:** The paper's central claim becomes testable and falsifiable.

### Suggestion D (Must fix): Revise all overclaims to match evidence scope
- **Action:** (a) Replace "state-of-the-art" with "competitive with or surpassing evaluated baselines under tested settings." (b) Remove "high attack efficiency" unless compute time/latency is measured and reported. (c) In conclusion, replace "superior performance" with "consistent improvements in ASR." (d) Add a limitations paragraph acknowledging: single dataset (ImageNet), no variance estimates, limited defense evaluation.
- **Location:** Pages 1, 3, 7, 9
- **Expected benefit:** Claim-evidence alignment improved; reduced reviewer skepticism.

### Suggestion E (Must fix): Restructure related work into method families
- **Action:** Reorganize Section 2 into: (a) Gradient modification (momentum, Nesterov), (b) Input transformation (DIM, TIM, SIM, AAM), (c) Region-based and masking methods (PI-FGSM, guided mask, Cutout). For each family, state 2-3 representative methods and how APD differs. Add a short comparison table.
- **Location:** Pages 3-4 - Section 2
- **Expected benefit:** Clear novelty positioning; readers can quickly understand APD's place in the literature.

### Suggestion F (Nice-to-have): Broaden defense evaluation and add failure-mode analysis
- **Action:** (a) Evaluate APD integrated with multiple baselines (not just AA-TI-DIM) against defense models. (b) Analyze where APD helps most (e.g., large architecture gap between source and target) and least (e.g., near-saturated ASR, NRP defense). Add a paragraph discussing this heterogeneity.
- **Location:** Page 8 - Section 4.3
- **Expected benefit:** Richer understanding of APD's strengths and limitations.

### Suggestion G (Nice-to-have): Compare APD against Cutout-based attacks in main experiments
- **Action:** Move the Cutout comparison from Appendix A.2 to the main ablation study (Section 4.4). This comparison directly tests the claim that retaining semantic information (by resetting to clean values) is better than zeroing out perturbations. Add an analysis paragraph explaining the mechanism.
- **Location:** Page 8-9 - Ablation section
- **Expected benefit:** Strengthens the evidence for the design choice.

### Suggestion H (Nice-to-have): Add computational cost-benefit analysis
- **Action:** Report average wall-clock time per image for each method (baseline vs APD) under identical hardware. Add a sentence: "APD requires nm forward passes per iteration (here, 3×5=15), resulting in approximately 15× higher computation than I-FGSM. However, as shown in Appendix A.3, the gain cannot be attributed to computation alone."
- **Location:** Page 7 - Experimental setup or Page 9 - Discussion
- **Expected benefit:** Transparent cost discussion.

## Storyline Options + Writing Outlines
### Abstract Outline (4-5 sentence structure)

**S1 (Problem & Domain):** "Adversarial transferability — the ability of a perturbation crafted for one model to mislead another — is critical for black-box attacks in security-sensitive applications."

**S2 (Prior Gap):** "Existing methods improve transferability by spreading perturbations across the entire image, but this creates mutual dependencies between regions that harm cross-model effectiveness."

**S3 (Method):** "We propose Adversarial Perturbation Dropout (APD), which breaks these dependencies by resetting random square perturbation regions to clean values and averaging gradients across masked variants at each iteration."

**S4 (Design choice):** "We use class activation maps (CAM) to focus dropout on attention-critical regions, further improving transferability."

**S5 (Key Result):** "On ImageNet, APD improves attack success rates by up to 19.6 percentage points over baselines and shows consistent gains across defended models and diverse architectures (ViT, Sequencer, MnasNet)."

### Introduction Outline (Complete, paragraph-by-paragraph)

**P1 (Role: Establish stakes and domain context)**
- Target claim: Black-box adversarial attacks are important; transferability is the key enabler.
- Key sentence: "Adversarial transferability — the ability of a perturbation to transfer from a known source model to an unknown target model — is the foundation of black-box attacks and a critical challenge for deploying robust DNNs in security-sensitive settings."
- Transition to P2: "However, existing methods for improving transferability have a key limitation."

**P2 (Role: Identify the gap — flat citations → structured limitation)**
- Target claim: Extending perturbations across the whole image is suboptimal because different models attend to different regions.
- Key sentence: "Recent transferability methods fall into two families: gradient modification (momentum, Nesterov) and input transformation (diversity, translation, scale, mixing). Both families share the same limitation — they optimize perturbations jointly across all image regions, creating dependencies that harm transfer when the target model attends to a different subset."
- Transition to P3: "This observation motivates a different approach."

**P3 (Role: Introduce the synergy hypothesis with motivating experiment)**
- Target claim: Perturbation synergy exists and hurts transferability.
- Key sentence: "Consider two categories of perturbations: those in the source model's attention region, and those outside it. When attention-region perturbations are selectively removed, the attack success rate drops significantly more than when random regions are removed (Fig. 1b). This suggests that perturbations in attention-critical regions have synergistic dependencies with other regions."
- Transition to P4: "Breaking this synergy could improve transferability."

**P4 (Role: Propose APD and explain intuition)**
- Target claim: APD breaks perturbation synergy via dropout-style gradient averaging.
- Key sentence: "We propose Adversarial Perturbation Dropout (APD), which at each iteration creates multiple masked versions of the adversarial example — each with a different square region reset to clean values — and averages their gradients before updating the perturbation."
- Transition to P5: "To maximize effectiveness, we use CAM to guide region selection."

**P5 (Role: Contribution summary and roadmap)**
- Bullet-style contribution list (revised as suggested in annotation):
  - C1: Identify perturbation synergy as a cause of limited transferability; propose perturbation dropout as a solution.
  - C2: Use CAM guidance for effective region selection.
  - C3: Empirical validation with up to 19.6 pp improvement across 7 models and 4 defenses.

### Alternative Storyline Candidates

**Candidate A (Current approach — synopsis):** Black-box transferability → existing methods spread perturbations → this creates synergy → synergy hurts transfer → break synergy via dropout → use CAM for guidance → experiments confirm.

**Candidate B (Gap-first approach — recommended):** Start with the concrete limitation (different models attend to different regions) → show that this makes joint optimization fragile → propose region dropout as a direct solution → derive the CAM guidance as a natural extension → experiments.

**Candidate C (Mechanism-first approach):** Start with the analogy to neuron dropout → explain how dropout prevents co-adaptation in neural networks → propose applying the same principle to perturbation regions → formalize synergy as gradient correlation → show that APD reduces gradient correlation → experiments confirm the mechanism.

**Recommended:** Candidate B (Gap-first). It leads with the clearest problem statement, which is currently buried in paragraph 3 of the Introduction. The gap (attention mismatch between source and target models) is well-established and easy to understand. From this gap, the solution (region dropout) follows naturally.

## Priority Revision Plan
### P0 (Critical — Must fix before resubmission)

| Priority | Issue | Action | Effort | Expected Impact |
|----------|-------|--------|--------|----------------|
| P0-1 | Algorithm inconsistency (placeholder "??") | Fix Algorithm 1 line 18 and align n limit | Low (5 min) | Reproducibility restored |
| P0-2 | Missing statistical significance | Re-run with ≥3 seeds, add std and significance tests | Medium (compute cost) | Core methodological validity |
| P0-3 | Overclaimed SOTA/efficiency language | Revise abstract, contributions, conclusion to bounded wording | Low (30 min) | Claim-evidence alignment |
| P0-4 | Undefined "synergy" | Add formal definition and measurement metric | Medium (analysis) | Central claim becomes testable |

### P1 (High priority — Should fix)

| Priority | Issue | Action | Effort | Expected Impact |
|----------|-------|--------|--------|----------------|
| P1-1 | Flat related work | Restructure into method families with comparison table | Medium (writing) | Clearer novelty positioning |
| P1-2 | Cutout comparison in appendix | Move to main ablation study | Low (text move) | Stronger design-choice evidence |
| P1-3 | Missing cost-benefit analysis | Report wall-clock time per image | Low (measurement) | Transparency on computation |
| P1-4 | Grammar and language errors | Fix ~10 grammar issues | Low (editing) | Professional presentation |

### P2 (Nice to have)

| Priority | Issue | Action | Effort | Expected Impact |
|----------|-------|--------|--------|----------------|
| P2-1 | Single-baseline defense evaluation | Add APD integrated with multiple baselines vs defenses | Medium (compute) | Stronger defense claims |
| P2-2 | Failure-mode analysis | Analyze when/why APD helps most vs least | Medium (analysis) | Deeper insight |
| P2-3 | Introduction narrative restructuring | Rewrite intro using Candidate B (Gap-first) | Medium (writing) | Reader engagement |

```text
ASCII Diagram — Revision Strategy Roadmap

[P0-1: Algorithm fix] -> [Reproducibility] -> Gate: Reviewer can implement from text
     ↓
[P0-2: Statistical tests] -> [Credibility] -> Gate: Gains are statistically significant
     ↓
[P0-3: Bound claims] -> [Defensibility] -> Gate: Claims match evidence scope
     ↓
[P0-4: Define synergy] -> [Testability] -> Gate: Central claim is measurable
     ↓
[P1: Structure + analysis] -> [Positioning] -> Gate: Novelty is clear
     ↓
[P2: Depth experiments] -> [Insight] -> Gate: Rich failure-mode understanding
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective / Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|----------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Single-model APD vs baseline attack methods | Inc-v3/4/IncRes-v2/Res-101 as source → 7 target models; ϵ=16, T=10, α=1.6 | ASR (%) | APD consistently improves all baselines by 6.8-12.7 pp avg | C3 (empirical validation) | No variance/statistical tests; single run per setting |
| E2 | Ensemble-model APD | Ensemble of 4 CNNs → 7 target models | ASR (%) | APD improves by avg 15.62 pp | C3 | Same as E1 |
| E3 | APD vs defense models (FD, NRP) | Ensemble attack → ResNeXtDA, Res152D, NRP, NRPresG | ASR (%) | +2.6 pp avg improvement | C3 | Only AA-TI-DIM baseline; modest gains |
| E4 | APD on diverse architectures | Ensemble attack → Seq2d LSTM, ViT-B/16, MnasNet | ASR (%) | +13.3 / +11.3 / +1.8 pp | C3 | No analysis of why gains differ |
| E5 | CAM vs Random dropout | Inc-v3/4/Res-101 as source → 6 targets | ASR (%) | CAM-guided outperforms random | C2 | Only one random baseline; no statistical test |
| E6 | Hyperparameter β sensitivity | Inc-v3/Res-101 → 6 targets; β=3..33 | ASR (%) | β=27 near-optimal | C1 (design) | Single source models only |
| E7 | Number of centers/scales | Inc-v3/Res-101 → 6 targets | ASR (%) | 3-4 centers, 5-7 scales sufficient | C1 (design) | No interaction analysis |
| E8 | Computational cost control | MI(1x), MI(15x), APD-MI | ASR (%) | APD > MI(15x) despite same cost order | C1 | 15x iterations ≠ same optimization dynamics |
| E9 | Cutout vs APD (Appendix A.2) | Inc-v3/4/IncRes-v2/Res-101 → 6 targets | ASR (%) | APD > Cutout | C1 (design choice) | In appendix, should be in main text |

### Research-Theme Gap Diagnosis

**New Knowledge (partially supported):** The identification of perturbation synergy as a mechanism limiting transferability is a novel conceptual claim, but without a formal definition or direct measurement, it remains a hypothesis rather than validated knowledge. The empirical demonstration that APD improves transferability is solid, but the mechanism (synergy reduction) is inferred rather than directly observed.

**Reproducibility (partially supported):** The algorithm description has inconsistencies (placeholder "??", conflicting n values) that prevent exact reproduction. The missing variance reporting further limits reproducibility.

**Impact on Practice/Understanding (moderate):** APD's modularity (integration with existing methods) is practically useful. However, the computational overhead (15× forward passes) may limit adoption without cost-benefit analysis.

### Proposed Research Experiments

```text
ASCII Diagram — Experiment Upgrade Plan (P0/P1/P2 sequencing)

P0: Statistical validation
  ├── E10: Multi-seed ASR (3 seeds, mean±std for Tables 1-4)
  └── E11: Paired significance tests (McNemar's test for each baseline vs APD)
       ↓
P1: Mechanism validation  
  ├── E12: Synergy metric computation (gradient correlation before/after APD)
  ├── E13: Controlled synergy isolation (fix region size, vary dropout strategy)
  └── E14: Full Cutout comparison in main ablation (move from appendix)
       ↓
P2: Robustness & analysis
  ├── E15: APD with multiple baselines against defense models (not just AA-TI-DIM)
  ├── E16: Failure-case analysis (when ASR gain < 2 pp, what common pattern?)
  └── E17: Cost-adjusted benchmark (wall-clock time per image for all methods)
```

**P0 Experiment: E10 — Multi-seed statistical validation**
- Target Claim: C3 (empirical gains are reliable)
- Hypothesis: APD gains are statistically significant across seeds
- Design: Re-run Table 1 experiments with 3 random seeds
- Controls: Same data split, seed control for model stochasticity
- Metrics: Mean ± std ASR; Cohen's d effect size
- Success Criterion: ASR improvement is > 0 with p < 0.05 for majority of settings
- Estimated Cost: ~3× current compute (3 seeds × current experiments)
- Expected Quality Gain: Core methodological validity

**P1 Experiment: E12 — Synergy metric computation**
- Target Claim: C1 (synergy reduction is the mechanism)
- Hypothesis: APD reduces gradient correlation between perturbation regions compared to baselines
- Design: Compute Synergy = avg pairwise cosine similarity of region gradients for APD vs. MI-FGSM examples. Report synergy reduction ratio.
- Controls: Same attack budget, same number of iterations
- Metrics: Synergy score (defined above), correlation with ASR gain
- Success Criterion: APD shows significantly lower synergy (p < 0.05) and synergy reduction correlates with ASR gain across model pairs (r > 0.5)
- Estimated Cost: Low (analysis of existing gradients)
- Expected Quality Gain: Central claim becomes empirically testable and validated

**P2 Experiment: E16 — Failure-case analysis**
- Target Claim: Understanding APD's scope
- Hypothesis: APD helps most when source/target models have dissimilar attention patterns; helps least when ASR is already saturated
- Design: For each source-target pair, compute attention similarity (CAM correlation). Plot ASR gain vs. attention similarity. Identify outlier pairs.
- Controls: Baseline AA-TI-DIM ASR as reference
- Metrics: ASR gain vs. CAM correlation, per-pair analysis
- Success Criterion: Identifiable pattern (e.g., negative correlation between attention similarity and ASR gain)
- Estimated Cost: Low (analysis of existing data)
- Expected Quality Gain: Rich understanding of method's适用范围

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

**Rationale:** The paper proposes a clean, intuitive idea (perturbation dropout) and demonstrates consistent empirical improvements across many settings. However, the score is constrained by several significant weaknesses:

1. **Research value (5/10):** The conceptual contribution (synergy reduction) is plausible but not formally defined or directly measured. The empirical contribution is solid but limited by the absence of statistical significance testing. Without these, the paper's core value proposition remains partially unsubstantiated.

2. **Novelty (5/10 — deferred):** External literature verification is unavailable in this run (Retrieval-Disabled Mode). Based on internal evidence, the perturbation dropout idea appears incremental over existing masking/ensemble methods. The CAM guidance is a practical enhancement rather than a conceptual novelty. The Cutout comparison (Appendix A.2) suggests differentiation, but the paper does not make this case strongly in the main text. **Novelty verdicts are deferred for manual verification.**

3. **Validity/Soundness (5/10):** The algorithm has documented inconsistencies (placeholder "??", conflicting constraints). The experimental methodology lacks variance reporting and significance testing. The central "synergy" mechanism is asserted but not validated. These issues materially affect confidence in the conclusions.

4. **Reproducibility (4/10):** The unresolved placeholder "??" in Algorithm 1 is a clear reproducibility blocker. The missing implementation details (gradient computation reference variable, handling of masked regions) and single-run results further reduce reproducibility.

5. **Presentation (6/10):** The paper is generally readable but suffers from overclaimed language, flat related-work organization, and ~10 grammatical errors. The figures are informative. The contribution list needs restructuring.

**Post-Revision Target: [6.5, 7.5] / 10**

If the authors complete the P0 and P1 revision items (fix algorithm inconsistency, add statistical tests, define/measure synergy, revise overclaims, restructure related work), the paper could achieve a score of 6.5-7.5/10. The upper bound (7.5) assumes that the synergy definition and measurement convincingly validate the central claim, and that the related work restructuring clearly positions APD's novelty. The lower bound (6.5) reflects the incremental nature of the contribution over existing masking methods, which even with perfect execution will still be a solid but not breakthrough contribution.