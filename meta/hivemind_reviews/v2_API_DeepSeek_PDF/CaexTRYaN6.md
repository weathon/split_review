## Summary
This paper proposes CONCORD (CONCept-infORmed Diffusion), a method that enhances instance-level conceptual completeness in diffusion-based dataset distillation by incorporating fine-grained concepts retrieved from large language models. The key idea is to use LLM-generated visual attribute descriptions (e.g., "otter-shaped head," "thick leg fur") as explicit guidance signals during the denoising process, steering generated images toward better object detail fidelity. A contrastive matching objective (Eq. 12) aligns generated samples with positive concepts from the target class while repelling negative concepts from similar categories. The method is designed as a training-free plug-in for existing diffusion-based DD pipelines such as Minimax and Stable Diffusion unCLIP. Experiments on ImageNet-1K, ImageNet-100, ImageWoof, and Food-101 show consistent improvements over baselines across multiple architectures and image-per-class settings.

The paper addresses a genuine and under-explored problem in generative-prior DD: the lack of instance-level control during synthesis. The empirical results are reasonably consistent, with 17 ablation/analysis experiments. However, the manuscript contains several significant issues, including: (1) a critical hyperparameter inconsistency (λ=1 vs λ=2.0 across sections), (2) a mathematical ambiguity in how the guided noise estimate integrates with DDIM sampling (Algorithm 1 vs Eq. 7-8), (3) an unfair comparison between classifier guidance and concept informing, (4) a factual contradiction about computational cost reduction, and (5) unsubstantiated SOTA and interpretability claims. External literature verification was unavailable in this review, so novelty and positioning claims are deferred for manual verification.

## Strengths
1. **Well-motivated problem.** The paper identifies a genuine limitation in generative-prior DD methods—the lack of instance-level control leading to conceptual incompleteness (missing/incorrect object details). This is a practically relevant issue, especially under the tight per-class storage budgets typical of DD benchmarks.

2. **Clean, training-free design.** CONCORD operates at inference time without requiring additional fine-tuning of diffusion models. This makes it a practical plug-in enhancement for existing diffusion-based DD pipelines.

3. **Comprehensive empirical evaluation.** The paper evaluates on 4 datasets (ImageNet-1K, ImageNet-100, ImageWoof, Food-101), 2 base diffusion pipelines (Minimax, Stable Diffusion unCLIP), 3 architectures (ConvNet, ResNet-18, ResNet-101), and multiple IPC settings (1, 10, 50, up to 200). The ablation study (Tab. 4-6, Fig. 4-5) systematically investigates prompt design, negative selection strategies, objective forms, and hyperparameter sensitivity.

4. **Consistent improvement pattern.** Across nearly all settings, applying CONCORD yields positive gains over the baseline (Minimax or unCLIP). The improvement is most pronounced at higher IPC values, where conceptual completeness has more room to contribute.

5. **Transparent limitation disclosure.** The paper acknowledges the increased inference cost (Table 8) and the incompatibility with few-step diffusion, which is commendable for practical deployment awareness.

## Weaknesses
1. **Critical hyperparameter inconsistency (λ).** Sec 4.1 states λ=1, Sec 4.4 concludes λ=2.0, and Appendix B states λ=1. This contradiction makes the reported results non-reproducible without clarification.

2. **Mathematical ambiguity in guided DDIM sampling.** Algorithm 1 replaces ϵθ with ˆϵ (Eq. 9) for the denoising step but does not specify whether ˆx(0) (Eq. 8) is recomputed with ˆϵ. If not, the DDIM step uses inconsistent noise estimates, which could affect the validity of the results.

3. **Unfair comparison with classifier guidance.** The ablation sets classifier guidance weight to 0.05 while CONCORD uses λ=1 or 2.0—a 20-40x difference. Without evaluating classifier guidance across a comparable range of weights, the claim that "contrastive objective offers more detailed guidance" is not convincingly supported.

4. **Computational cost claim contradicts data.** The Introduction claims the method "reduces the required computational consumption," but Table 8 shows CONCORD increases inference time by 1.4-2.5x over baselines.

5. **SOTA and interpretability claims overstretched.** "State-of-the-art" cannot be verified without external literature comparison. "Explicit interpretability" is claimed but never evaluated (no concept attribution, no user study, no quantitative interpretability metric).

6. **Unsubstantiated core motivation.** The central claim that "conceptual incompleteness" degrades DD quality is intuitive but never directly measured. No metric quantifies conceptual completeness, and no controlled experiment isolates its causal effect.

7. **Food-101 baseline concern.** At IPC=50, both unCLIP (61.3%) and unCLIP^C (62.5%) underperform random selection (64.0%), suggesting generative-prior DD may not be universally advantageous—a point that requires deeper analysis.

8. **Related Work is list-like.** Both the Dataset Distillation and Diffusion Models paragraphs read as chronological/categorical summaries without explicit comparison axes or differentiation from CONCORD.

9. **Introduction narrative is front-loaded with generic background** rather than immediately establishing the specific gap that CONCORD addresses.

## Key Issues
**Issue 1 (Critical) — λ inconsistency prevents reproducibility.**
- Location: Page 6 (Sec 4.1) vs Page 10 (Sec 4.4) vs Page 16 (Appendix B).
- Problem: λ is stated as 1, 2.0, and 1 in different sections.
- Impact: All experimental results are non-reproducible without resolution.
- Fix: Unify to single value, correct conflicting sections, and justify choice relative to Fig. 4b.

**Issue 2 (Major) — Algorithm 1 / Eq. 7-9 mathematical gap.**
- Location: Page 5 (Algorithm 1, Eq. 9) combined with Eq. 7-8 (Page 4).
- Problem: Algorithm replaces ϵθ with ˆϵ for DDIM step but does not recompute ˆx(0) consistently.
- Impact: The actual generation behavior may differ from what is described, weakening causal claims.
- Fix: Clarify or restructure the update rule for full mathematical consistency.

**Issue 3 (Major) — Unfair classifier guidance comparison.**
- Location: Page 8 (Optimization ablation, Tab. 6).
- Problem: Classifier guidance weight=0.05 vs CONCORD λ=1/2.0.
- Impact: Superiority claim of CONCORD over classifier guidance is confounded by unequal tuning.
- Fix: Sweep classifier guidance across multiple weights and report best result.

**Issue 4 (Major) — Computational cost contradiction.**
- Location: Page 2 (Introduction) vs Page 17 (Table 8, Appendix).
- Problem: Claims "reduces computational consumption" but data shows 1.4-2.5x increase.
- Impact: Misleading readers about the method's practical efficiency.
- Fix: Rewrite cost claim to accurately reflect the accuracy-cost trade-off.

**Issue 5 (Major) — SOTA and interpretability claims overreach.**
- Location: Abstract, Page 2 (Introduction), Page 10 (Conclusion).
- Problem: "State-of-the-art" unverifiable without external retrieval; "interpretability" never evaluated.
- Impact: Overclaims reduce scientific credibility.
- Fix: Replace SOTA with bounded comparative wording; remove or substantiate interpretability claims.

**Issue 6 (Major) — Core motivation concept untested.**
- Location: Page 2 (Introduction), throughout.
- Problem: "Conceptual completeness" is never directly measured or causally isolated.
- Impact: The paper's central hypothesis remains untested; observed gains could stem from other factors (CLIP regularization, embedding alignment).
- Fix: Propose and compute a "concept completeness score" (e.g., CLIP alignment with reference descriptions) and show it correlates with downstream accuracy.

**Issue 7 (Major) — Food-101 baseline concern.**
- Location: Page 7 (Sec 4.2, Tab. 3).
- Problem: Both unCLIP and unCLIP^C underperform random selection at IPC=50.
- Impact: Raises questions about when generative DD is beneficial.
- Fix: Add analysis explaining the underperformance and discuss practical boundary conditions.

## Actionable Suggestions
### S1 — Fix λ inconsistency (Must)
- Unify the informing weight λ across Sec 4.1, Sec 4.4, and Appendix B. If λ=1 was used for main results, correct Sec 4.4's conclusion. If λ=2.0 is optimal, update Sec 4.1 and Appendix B. Add a sentence explaining the choice: "Based on the parameter analysis in Fig. 4b, λ=2.0 yields the best accuracy-CLIP similarity balance for the contrastive objective, and this value was used for all main experiments."

### S2 — Resolve Algorithm 1 / Eq. 7-9 derivation gap (Must)
- Option A (recommended): Modify Algorithm 1 to recompute ˆx(0) using ˆϵ before the DDIM step. Add: "Compute ˆx(0) ← x(t)/√α_t − √(1−α_t)/√α_t · ˆϵ" after line "Update the predicted noise ˆϵ according to Eq. 9."
- Option B: If ˆx(0) is not recomputed, provide a mathematical justification or adopt the classifier-guidance style (Eq. 6) which operates on the mean directly.

### S3 — Fair classifier guidance comparison (Must)
- Report classifier guidance at λ ∈ {0.01, 0.05, 0.1, 0.5, 1.0, 2.0} on at least one dataset (e.g., ImageWoof IPC=10).
- Include the best result in Tab. 6. If the gap persists, the superiority claim is valid; if the gap closes, adjust the claim accordingly.

### S4 — Revise computational cost claim (Must)
Replace the sentence in Introduction (Page 2): "It reduces the required computational consumption, and thereby enhances the practicality of our approach" with: "While CONCORD increases per-sample generation time by ~1.4-2.5x due to the additional CLIP similarity computation at each denoising step, it eliminates the need for training task-specific classifiers, shifting the computational burden from training to inference."

### S5 — Bound SOTA and remove unsubstantiated claims (Must)
- Replace "state-of-the-art performance" with "improves upon selected baselines under reported settings" throughout.
- Remove or substantiate "interpretability" claims. If kept, provide quantitative evidence (e.g., concept activation maps, ablation studies showing that certain descriptions drive specific visual features and downstream accuracy).

### S6 — Add concept completeness metric (Nice-to-have)
Propose a metric: For each generated image, compute the average CLIP cosine similarity between the image and the top-5 retrieved concepts for its target class. Report this metric across baselines and CONCORD to directly verify that "conceptual completeness" is indeed improved.

### S7 — Analyze Food-101 underperformance (Nice-to-have)
Add a paragraph analyzing why unCLIP underperforms random at IPC=50 on Food-101. Possible angles: (a) domain shift between LAION-2B training data and food imagery, (b) concept granularity mismatch, (c) soft-label training dynamics. Include a practical recommendation for when to use generative DD vs random selection.

## Storyline Options + Writing Outlines
### Abstract Outline (complete, 5-sentence structure)

**S1 (Problem):** Dataset distillation aims to condense large-scale datasets into small surrogate sets for efficient model training, but generative-prior methods lack instance-level control, leading to missing or incorrect object details.

**S2 (Gap):** Existing approaches match dataset-level distributions without explicitly verifying conceptual completeness at the instance level, causing information loss that degrades downstream task performance.

**S3 (Proposed method):** We propose CONCORD (CONCept-infORmed Diffusion), which retrieves fine-grained visual attributes from large language models and uses them as explicit guidance during the denoising process, steering each generated sample toward better object detail fidelity.

**S4 (Key result):** On ImageNet-1K and its subsets, CONCORD consistently improves over Minimax and Stable Diffusion baselines across multiple architectures and image-per-class settings, with gains of up to 2-3 percentage points at high IPC values.

**S5 (Impact):** The method enhances the quality and controllability of distilled datasets without requiring task-specific classifier training, at the cost of moderate increases in per-sample generation time.

### Introduction Outline (complete, paragraph-by-paragraph)

**P1 (Establish territory → identify gap):** Open with the specific limitation of generative-prior DD: generated samples may lack essential object details because instance-level control is absent. Replace the current generic data-abundance framing with a focused problem statement. *Transition: "This gap motivates our investigation into instance-level concept enhancement."*

**P2 (Prior work survey → limitations):** Briefly categorize DD methods (meta-learning, metric matching, generative prior) and highlight that all three paradigms operate at the dataset-distribution level. Contrast with classifier guidance in diffusion models, which provides category-level but not attribute-level control. *Transition: "We thus ask: can we inject fine-grained concept information directly into the denoising process?"*

**P3 (Proposed method intuition):** Present CONCORD: LLM-retrieved descriptive attributes → CLIP similarity guidance → noise prediction modification. Highlight key design choices: (a) distinctiveness emphasis in concept retrieval, (b) contrastive matching with negative concepts, (c) training-free inference. *Transition: "The resulting method improves sample quality without additional training."*

**P4 (Evidence preview + contributions):** Summarize key results: consistent improvements on ImageNet-1K subsets, ablation validating each component, analysis of concept effectiveness. List 2-3 concrete contributions concisely. *Transition: "We detail the method in Sec. 3."*

### Current Storyline Critique

The current introduction (Paragraph 1-3, Page 1-2) starts with broad statements about "vast volumes of data" and "strong neural networks often demand days or even months of training" before arriving at the DD context. This delays the paper's focus. A tighter opening would directly state: "Dataset distillation aims to create small surrogate datasets that preserve training efficacy. Recent generative-prior methods achieve this efficiently but lack instance-level control, causing conceptual incompleteness. We address this gap by introducing concept-informed diffusion."

### Alternative Storyline Options

**Option A (Problem-first):** Open with a concrete failure case (e.g., Fig. 1's beagle with unrealistic legs) → generalize to the conceptual incompleteness problem → contrast with existing DD methods that cannot fix this → propose CONCORD → evidence. This is more engaging than the current abstract-first approach.

**Option B (Gap-driven):** Start with the question "Does distribution-level matching guarantee effective individual samples?" → show evidence it does not → derive the need for instance-level control → introduce CONCORD as the solution. This aligns with the existing rhetorical question on Page 2 but places it at the very beginning.

**Recommended:** Option A combines visual grounding with clear problem motivation, and the existing Fig. 1 already supports this narrative.

## Priority Revision Plan
### P0 — Publication-critical (Must fix before acceptance)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P0.1 | λ inconsistency (Sec 4.1 vs 4.4 vs Appendix) | Unify to single value; correct all sections | Restores reproducibility |
| P0.2 | Algorithm 1 / Eq. 7-9 derivation gap | Clarify or restructure the update rule | Ensures mathematical validity |
| P0.3 | Computational cost contradiction | Rewrite cost claim to reflect actual 2x increase | Restores factual accuracy |
| P0.4 | SOTA / interpretability overclaims | Replace with bounded wording throughout | Improves scientific credibility |
| P0.5 | Unfair classifier guidance comparison | Sweep weights {0.01-2.0} and report best | Fairly establishes superiority |

### P1 — High priority (Should fix for strong revision)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P1.1 | Core motivation concept untested | Add concept completeness metric | Directly validates central hypothesis |
| P1.2 | Food-101 underperformance unexplained | Add analysis paragraph | Clarifies boundary conditions |
| P1.3 | Classifier guidance limitation unsubstantiated | Soften claim or add evidence | Strengthens motivation |
| P1.4 | Introduction narrative too generic | Restructure to problem-first format | Improves reader engagement |

### P2 — Quality improvement (Nice-to-have)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P2.1 | Related Work list-like | Reorganize by comparison axes | Better positioning |
| P2.2 | Abstract CLIP dependence contradiction | Acknowledge CLIP as pre-trained model | Removes internal inconsistency |
| P2.3 | "Personalization" overclaim | Remove unsubstantiated claim | Tightens contribution scope |
| P2.4 | Typo "replying" → "relying" | Fix | Language quality |

### ASCII Diagram — Revision Strategy Roadmap

```text
[P0 Issues: Reproducibility + Validity Risks]
    |
    +--> Fix λ inconsistency        -> Reproducible results
    +--> Fix Algorithm 1 gap        -> Mathematically sound
    +--> Fix cost contradiction     -> Factually accurate
    +--> Bound SOTA claims          -> Scientifically credible
    +--> Fair classifier comparison -> Valid superiority claim
    |
    v
[P1 Issues: Motivation + Boundary Conditions]
    |
    +--> Add concept completeness metric -> Core hypothesis testable
    +--> Analyze Food-101 gap            -> Practical guidance
    +--> Soften classifier criticism     -> Balanced motivation
    +--> Restructure Introduction        -> Clearer narrative
    |
    v
[P2 Issues: Polish + Positioning]
    |
    +--> Reorganize Related Work    -> Better field positioning
    +--> Fix abstract inconsistency -> Internal consistency
    +--> Trim overclaims            -> Tighter contribution
    |
    v
[Expected Outcome: Stronger, reproducible, defensible paper]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------|---------|--------------|-----------------|--------------------|
| E1 | Main results (ImageWoof) | Tab 1, IPC={1,10,50}, baselines={MTT,SRe2L,RDED,DiT,Minimax,unCLIP} | Top-1 accuracy | CONCORD improves over baselines across architectures | C1 (improved quality) | SOTA claim unverifiable |
| E2 | Main results (ImageNet-100/1K) | Tab 2, IPC={1,10,50} | Top-1 accuracy | Consistent improvement, less gain at larger class count | C1 | λ inconsistency affects all |
| E3 | Food-101 custom DD | Tab 3, IPC={1,10,50} | Top-1 accuracy | CONCORD improves over unCLIP, but underperforms random at IPC=50 | C1 (partial) | Baseline quality concern |
| E4 | Prompt design | Tab 4, GPT-3.5 vs GPT-4 vs classification prompt | Top-1 accuracy | GPT-4 + custom prompt best | C1 (concept quality) | Only tested on ImageWoof |
| E5 | Negative selection | Tab 5, {Random,Similar-#,Weighted} | Top-1 accuracy | Weighted sampling best | C1 (negative design) | Limited analysis of why |
| E6 | Objective form | Tab 6, {None,Classifier,Cosine,Contrastive} | Top-1 accuracy | Contrastive > Cosine > Classifier > None | C1 (contrastive design) | Unfair classifier tuning |
| E7 | λ parameter | Fig 4b, λ∈{0,0.1,0.5,1,2,3,4,6} | Top-1 accuracy | Best at λ=2 | C1 (control strength) | Inconsistent with λ=1 claim |
| E8 | Negative sample count | Fig 4c, |C|∈{0,2,5,10,20,50} | Top-1 accuracy | Best at 10 | Limited analysis |
| E9 | Denoising steps | Fig 5, steps∈{25,50,100} | Top-1 accuracy | 50 steps optimal | C1 (practicality) | Moderate effect |
| E10 | Combination (classifier + concept) | Tab 7, {None,Classifier,Contrastive,Combination} | Top-1 accuracy | Combination underperforms individual | C1 (design independence) | Mechanism unexplained |
| E11 | Inference time | Tab 8, Minimax vs MinC, unCLIP vs unCLIP^C | Seconds/sample | ~1.4-2.5x increase | C2 (training-free) | Cost claim contradicts Intro |
| E12 | Extended baselines | Tab 9, Random/K-Center/Herding/IDM | Top-1 accuracy | CONCORD outperforms all | C1 | No significance test |
| E13 | Feature distribution | Fig 6, t-SNE visualization | Qualitative | CONCORD preserves distribution while improving quality | C1 | Qualitative only |

### Research-Theme Gap Diagnosis

1. **New knowledge (partial):** The paper demonstrates that instance-level concept guidance improves DD quality, but the mechanism is not isolated from CLIP embedding regularization effects. The core construct ("conceptual completeness") remains unmeasured.

2. **Reproducibility (threatened):** The λ inconsistency and Algorithm 1 ambiguity directly threaten reproducibility. These must be resolved before the paper is verifiable.

3. **Impact on practice/understanding (mixed):** The consistent improvement pattern across settings supports practical value, but the Food-101 underperformance relative to random selection and the increased inference cost constrain the practical scope.

### Proposed Research Experiments (P0/P1/P2)

**Exp-P0a: λ consistency verification**
- Target Claim: All experimental results (C1)
- Hypothesis: Using λ=2.0 (optimal per Fig 4b) reproduces reported results
- Minimal Design: Rerun ImageWoof IPC=10 with both λ=1 and λ=2.0, report both
- Metric: Top-1 accuracy
- Success Criterion: One λ value matches original results; the other is either reported as correction or analysis
- Expected Gain: Resolves reproducibility crisis (P0 critical)

**Exp-P0b: Algorithm 1 clarification experiment**
- Target Claim: C1 (method validity)
- Hypothesis: The two interpretations (recomputing ˆx(0) with ˆϵ vs not) produce different results
- Minimal Design: Implement both versions and compare on ImageWoof IPC=10
- Success Criterion: Identify which version was actually used and report results accordingly
- Expected Gain: Mathematical validity and reproducibility

**Exp-P1a: Concept completeness metric**
- Target Claim: C1 (conceptual completeness)
- Hypothesis: CONCORD improves CLIP-image-to-concept similarity
- Minimal Design: Compute average CLIP similarity between generated images and their top-5 target concepts, for baseline vs CONCORD
- Metric: Average CLIP cosine similarity
- Success Criterion: CONCORD shows statistically significant higher concept similarity
- Expected Gain: Directly validates the core hypothesis

**Exp-P1b: Fair classifier guidance sweep**
- Target Claim: C1 (superiority over classifier guidance)
- Hypothesis: At matched guidance strength, the gap may change
- Minimal Design: Sweep classifier λ ∈ {0.01, 0.05, 0.1, 0.5, 1.0, 2.0} on ImageWoof IPC=10
- Success Criterion: Best classifier guidance result is reported in Tab. 6
- Expected Gain: Fair comparison establishes true superiority

**Exp-P2a: Food-101 failure analysis**
- Target Claim: C1 (general applicability)
- Hypothesis: unCLIP underperforms random due to domain shift for food categories
- Minimal Design: Compute CLIP image-text similarity for Food-101 categories and compare with ImageNet categories
- Success Criterion: Identify a quantitative predictor of when CONCORD helps vs hurts
- Expected Gain: Practical deployment guidance

### ASCII Diagram — Experiment Upgrade Plan

```text
[Current Evidence Base]
    |
    +-- Strong: consistent gains across 4 datasets, 3 architectures
    +-- Weak: λ inconsistent, Algorithm 1 ambiguous, SOTA unverified
    |
    v
[P0 Fixes (Week 1)]
    +-- Fix λ -> Rerun affected tables if needed
    +-- Fix Algorithm 1 -> Clarify update rule
    +-- Verify all numerical claims
    |
    v
[P1 Strengthening (Week 2)]
    +-- Concept completeness metric (Exp-P1a)
    +-- Fair classifier sweep (Exp-P1b)
    +-- Food-101 analysis (Exp-P2a)
    |
    v
[P2 Polish (Week 3)]
    +-- Restructure Introduction
    +-- Reorganize Related Work
    +-- Add coverage audit paragraph
    |
    v
[Expected: Defensible SOTA claim with bounded scope, reproducible results]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 5/10

**Rationale:** The paper addresses a well-motivated problem (instance-level control in generative-prior DD) and provides consistent empirical evidence of improvement across multiple datasets and architectures. However, the manuscript faces several major validity and reproducibility concerns: (1) a critical hyperparameter inconsistency (λ=1 vs λ=2.0) across sections that prevents reproduction of all reported results, (2) a mathematical ambiguity in how the guided noise modification integrates with DDIM sampling (Algorithm 1 vs Eq. 7-8), (3) an unfair comparison between classifier guidance and CONCORD that weakens the claimed superiority, (4) a factual contradiction about computational cost, and (5) overclaimed SOTA and interpretability statements. Additionally, external literature verification was unavailable, so novelty positioning is deferred. The paper's research value is genuine but the presentation and verification gaps reduce confidence in the current form.

**Scoring breakdown:**
- Research value / novelty: 5/10 (good problem, but mechanism not isolated; SOTA unverifiable)
- Methodological soundness: 4/10 (λ inconsistency + Algorithm 1 gap are fixable but currently serious)
- Empirical evidence: 6/10 (comprehensive but with unaddressed confounds)
- Reproducibility: 3/10 (critical λ inconsistency prevents reproduction)
- Writing and clarity: 5/10 (overclaims dilute otherwise clear technical writing)

**Post-Revision Target:** [6.5, 7.5]/10

**Rationale:** If all P0 issues (λ consistency, Algorithm 1 clarification, computational cost correction, bounded claim scope, fair classifier comparison) and P1 issues (concept completeness metric, Food-101 analysis) are addressed, the paper would present a solid, reproducible empirical contribution. The core idea is sound, the experiments are broad, and the ablation study is thorough. The ceiling is limited by the intrinsic constraint that novelty positioning requires external literature verification and that the method's improvement over baselines, while consistent, is modest in absolute terms (1-3 percentage points in most settings).