## Summary
This paper introduces Ablated Learned Temperature Energy (AbeT), an out-of-distribution (OOD) detection method for deep neural networks. The core idea is to combine two existing techniques — a learned (input-conditional) temperature and an energy-based OOD score — and then remove a counterproductive scaling term. The resulting score is simple: AbeT(x) = -log Σ_c exp(g_c(x) / T_learned(x)), where T_learned is learned via a lightweight single-layer head. The method requires no OOD training data, no test-time backward passes, and no multi-stage training.

The paper reports strong empirical results across three tasks: (a) classification (CIFAR-10, CIFAR-100, ImageNet-1k), where AbeT reduces FPR@95 by 45–78% over single-stage baselines; (b) semantic segmentation (Cityscapes → LostAndFound/RoadAnomaly), with FPR@95 reduction of 78% on LostAndFound; and (c) object detection (PASCAL VOC ID / COCO OOD), with AUROC +4.69 points. The paper also provides t-SNE-based analysis suggesting that AbeT learns to detect OOD inputs through exposure to misclassified ID examples during training.

The technical contribution (combining learned temperature with energy score and identifying the conflicting scaling term) is conceptually clean and the ablation study confirms the marginal benefit of the removal. However, the paper has several weaknesses: (1) the main comparison table has architecture mismatches for some baselines; (2) multi-seed statistical variance is not reported; (3) the mechanistic analysis of OOD detection is correlational, not causal; and (4) novelty claims cannot be fully verified without external literature (deferred to manual verification in this run). Overall, the paper presents a practically useful and conceptually simple method, but the empirical comparisons and mechanistic evidence need strengthening.

## Strengths
**1. Conceptually clean and simple method.** The core idea — replacing the scalar temperature in the energy score with a learned input-conditional temperature, then removing a counterproductive multiplication term — is elegantly simple. The final score is a one-line formula, and the architectural change requires only a single additional layer before training. This simplicity is a genuine strength for reproducibility and practical adoption.

**2. Consistent improvements across three task domains.** Unlike many OOD detection papers that focus solely on classification, AbeT demonstrates gains in classification, semantic segmentation, and object detection using the same core idea. The segmentation results on LostAndFound (FPR@95 reduction of 78.02%) are particularly compelling, as they validate the method's applicability to per-pixel dense prediction.

**3. Honest limitations discussion.** Section 7 candidly acknowledges that AbeT degrades when few misclassified ID examples exist and that most tested OOD methods share this failure mode. This transparency is rare and adds credibility.

**4. Ablation study confirms the marginal benefit of the core contribution.** Appendix B.1 quantifies that the Forefront Temperature Constant ablation alone reduces FPR@95 by 28.76% (CIFAR-10), 59.00% (CIFAR-100), and 24.81% (ImageNet). This directly ties the claimed contribution to measured improvement.

**5. No OOD data, no multi-stage training, no extra hyperparameters.** The method satisfies the hardest constraints in practical OOD detection: it requires no exposure to OOD examples, no test-time backward passes (like ODIN's input perturbation), no multiple training stages, and no dataset-specific hyperparameter tuning. This makes it potentially attractive for deployment.

## Weaknesses
**1. Comparison fairness concerns in Table 1 (Page 6).** Several baselines (Energy+ReAct, Energy+DICE) use a different backbone architecture (ResNet-50) than AbeT (ResNetv2-101). The authors state they could not reproduce results with ResNet-101, which raises concerns about implementation fidelity. Without matched-architecture reproduction, the reported improvements may partly reflect implementation differences.

**2. Missing multi-seed statistical variance (Pages 6, 8, 9).** All reported standard deviations are computed across OOD datasets, not across independent training runs. Since deep learning experiments exhibit non-trivial run-to-run variance (especially on smaller datasets like CIFAR-10), the reported improvements could fall within noise for some settings. This is critical for Table 1, where some improvements are modest (e.g., CIFAR-100 AUROC: 94.0±1 for AbeT vs 89.6±12 for Energy+ASH).

**3. Mechanistic analysis is correlational, not causal (Page 7).** Section 5 provides t-SNE visualizations and two hypotheses to explain AbeT's OOD detection ability. However, t-SNE distorts global geometry, and the claim "misclassified ID exposure drives OOD performance" is not tested with controlled experiments (e.g., training on a near-perfect classifier with few misclassified examples). An equally plausible alternative is that the cosine logit head + learned temperature jointly separate all low-confidence inputs without requiring misclassified ID as a specific training signal.

**4. Overclaim on "contradiction" terminology (Page 4).** The paper frames the Forefront Temperature Constant as a "contradiction" in the energy score. In reality, it creates an opposing directional effect — which is a design conflict, not a logical contradiction. The current wording inflates the perceived novelty of the ablation.

**5. Abstract and introduction narrative could be clearer (Pages 1-2).** The abstract lacks a structured problem-gap-solution-evidence flow. The introduction's first paragraph opens with a 10-reference laundry list rather than a focused motivation. Contribution bullets are clear but do not adequately separate the two distinct technical steps (combination vs. ablation).

**6. Limitations section too brief (Page 9).** The limitation on "few misclassified ID examples" is not quantified. The interesting finding that all tested methods fail on misclassified ID examples is relegated to the appendix and should be elevated to the main text.

**7. Novelty verification deferred (Retrieval-Disabled Mode).** Because external literature search was not possible in this run, the novelty of combining learned temperature with energy score and the claimed advantage over existing methods cannot be independently verified. Manual verification by the authors/reviewers is required.

## Key Issues
**Issue 1 (Major): Comparison fairness in Table 1 — mismatched backbones for key baselines.**
- *Severity:* High. The claim of "state of the art" depends on fair comparisons.
- *Evidence:* Energy+ReAct and Energy+DICE on ImageNet-1k use ResNet-50 (from original papers), while AbeT uses ResNetv2-101. Asterisk note states "our inability to reproduce their results with ResNet-101."
- *Impact:* Without matched-architecture reproduction, the reported improvements may partly come from different model capacities, not method superiority.
- *Fix:* Either (a) reproduce all methods on the same architecture, or (b) add a note explicitly quantifying the performance gap expected from architecture difference alone, and (c) add the "unablated AbeT" row so readers can see the ablation benefit directly.

**Issue 2 (Major): No multi-seed variance for core experimental results.**
- *Severity:* High. Statistical significance of reported gains cannot be assessed.
- *Evidence:* All ± values in Tables 1-3 are standard deviations across OOD datasets, not across training seeds.
- *Impact:* For small-improvement cases (e.g., CIFAR-100 AUROC: AbeT 94.0 vs Energy+ASH 89.6±12), the large std of the competitor suggests high variability — but without multi-seed variance for AbeT, the gap's reliability is unclear.
- *Fix:* Report mean±std over ≥3 random seeds for the main setting (at least CIFAR-10 and CIFAR-100 with plain AbeT and the strongest competitor).

**Issue 3 (Major): Understanding Section claims overextend correlational evidence.**
- *Severity:* Medium-High. The paper's mechanistic narrative could mislead readers into thinking the causal mechanism is established.
- *Evidence:* t-SNE plots + two hypotheses + appendix reference to non-dimensionality-reduction evidence. No counterfactual experiment (e.g., training on a near-perfect classifier to eliminate misclassified ID examples).
- *Impact:* The paper claims to "provide intuition as to why our model learns to distinguish" — this is accurate (intuition, not proof), but the section heading "Understanding AbeT" implies mechanistic insight.
- *Fix:* Add explicit causal disclaimer in Section 5. Report the results of a controlled experiment with high-accuracy models. Consider moving the mechanistic claim to a hypothesis rather than a conclusion.

**Issue 4 (Medium): Terminology overclaim — "contradiction" vs "counterproductive scaling."**
- *Severity:* Medium. Affects scholarly precision.
- *Evidence:* Page 4, second contribution claim: "resolve a contradiction in the energy score." The Forefront Temperature Constant has an opposing effect, not a logical contradiction.
- *Impact:* The inflated term strengthens the perceived novelty of the contribution beyond what the technical content justifies.
- *Fix:* Replace "contradiction" with "counterproductive scaling effect" or "conflicting directional effect."

**Issue 5 (Medium): Limitations section lacks actionable specificity.**
- *Severity:* Medium. Hinders reproducibility of failure modes.
- *Evidence:* Page 9, Section 7: "our method does not perform well in cases where there are few misclassified ID examples" — no quantification, no threshold.
- *Impact:* Readers cannot determine whether their specific setting would trigger this limitation.
- *Fix:* Add a plot or table showing OOD metrics vs training accuracy or misclassification rate. State a clear threshold (e.g., "when training accuracy exceeds 99%, FPR@95 increases by X%").

## Actionable Suggestions
### S1 (Must): Fix comparison fairness in Table 1
- **Action:** Reproduce Energy+ReAct and Energy+DICE on ResNetv2-101 (the same architecture used for AbeT). If reproduction fails, report the reproduced numbers (even if lower) with a clear note and move the asterisk explanation to a full subsection.
- **Also:** Add an "AbeT (unablated)" row to Table 1 — this is the combined learned temperature + energy score without the Forefront Temperature Constant ablation. This directly shows the marginal benefit of the core contribution in the same comparison context.
- **Location:** Page 6, Table 1.

### S2 (Must): Report multi-seed variance
- **Action:** Run each experiment (at least CIFAR-10, CIFAR-100 main settings) with 3 random seeds and report mean ± std across seeds in addition to the current OOD-dataset-standard-deviation.
- **Location:** Page 6, Table 1 caption and main text.

### S3 (Must): Add causal disclaimer and controlled experiment for mechanistic claim
- **Action:** 
  (a) Add a sentence to Section 5: "These findings are correlational; a controlled experiment with a high-accuracy classifier (few misclassified ID examples) is needed to confirm the causal role of misclassified ID exposure."
  (b) Run one targeted experiment: train a model with stronger data augmentation or larger capacity to achieve >99% training accuracy on CIFAR-100; measure whether AbeT's OOD detection degrades as predicted.
- **Location:** Page 7, Section 5.

### S4 (Must): Replace "contradiction" with precise terminology
- **Action:** In the second contribution bullet (Page 2) and Section 3 discussion (Page 4), replace "resolve a contradiction" with "remove a counterproductive scaling effect" or "eliminate a conflicting directional effect."
- **Location:** Pages 2 and 4.

### S5 (Should): Quantify the "few misclassified ID examples" limitation
- **Action:** Add a figure showing OOD detection performance (FPR@95) as a function of training set misclassification rate. State a practical threshold (e.g., "AbeT's FPR@95 increases by >10% relative when training accuracy exceeds 99%").
- **Location:** Page 9, Section 7.

### S6 (Should): Restructure abstract and introduction narrative
- **Action:** Rewrite the abstract using the 5-sentence structure (problem → significance → prior gap → method → key result). For the introduction, replace the 10-reference laundry list with a focused 2-3 sentence problem motivation, then introduce learned temperature and energy score as complementary approaches, then state the paper's combination + ablation insight.
- **Location:** Pages 1-2.

### S7 (Should): Move the "all methods fail on misclassified ID" finding to main text
- **Action:** The observation that "all tested OOD detection methods' failures were concentrated on misclassified ID examples" (currently in Appendix A.1) is potentially impactful. Elevate a 2-sentence summary to Section 5 or 7.
- **Location:** Page 7 or 9.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows this paragraph structure:
1. **(P1, Page 1)** Broad motivation: ML models perform well on fixed distributions but fail under distribution shift → OOD detection is important for AI safety.
2. **(P2, Page 1)** Briefly mentions learned temperature and energy score as existing approaches → states this paper combines them → announces code availability.

**Problems with current storyline:**
- Problem and gap are not clearly separated. The motivation paragraph blends distribution shift, miscalibration, and OOD detection into one continuous flow without a clear "prior work limitation" statement.
- The "gap" is implicit — readers must infer what is missing in prior work from the statement that this paper "combines these methods." The specific limitation of each individual method is not articulated.
- The transition from Introduction to Method (Section 2, Preliminaries) is abrupt, with no forward-looking statement.

### Recommended Storyline (Candidate A — Best)

**Abstract (5-sentence structure):**
- S1 (Problem): Deep neural networks in high-stakes domains must detect OOD inputs to avoid miscalibrated high-confidence predictions.
- S2 (Gap): Existing single-stage OOD scores — learned-temperature-based and energy-based — each have individual limitations: the former lacks a principled separation mechanism, the latter uses a fixed scalar temperature.
- S3 (Solution): We propose AbeT, which combines a learned input-conditional temperature with the energy score, then removes a counterproductive scaling term identified through analysis.
- S4 (Key Result): AbeT reduces FPR@95 by 45–78% on standard classification benchmarks and shows consistent gains in segmentation and detection.
- S5 (Limitation/Bound): Analysis suggests that exposure to misclassified ID examples drives this performance, though the mechanism remains correlational.

**Introduction Outline:**

**P1 (Problem + Stakes):** "Deep neural networks achieve high accuracy when test data matches the training distribution, but under distribution shift, both accuracy degrades and confidence estimates become miscalibrated. Users can be misled by high-confidence predictions on OOD inputs. Detecting such inputs is therefore critical for reliable deployment."
→ *Transition:* "Existing methods address OOD detection through scoring functions that separate ID from OOD inputs, but key design choices remain underexplored."

**P2 (Prior Work + Gap):** "Two prominent families of OOD scores are learned-temperature methods, which adaptively reduce confidence on uncertain inputs, and energy-based scores, which use the log partition function as a separation metric. Each has complementary strengths: learned temperatures provide input-adaptivity, while energy scores offer a principled thermodynamic interpretation. However, they have not been combined, and the interaction between learned temperature scaling and energy scoring has not been analyzed."
→ *Transition:* "In this paper, we show that combining them reveals a previously unrecognized design conflict, and resolving it yields a simple but effective OOD score."

**P3 (Solution + Contributions):** "We propose AbeT, which (1) replaces the scalar temperature in the energy score with a learned input-conditional temperature, and (2) identifies and removes a term — the Forefront Temperature Constant — that counteracts the desired score separation. This yields a single-line score: AbeT(x) = -log Σ_c exp(g_c(x)/T_learned(x))."
→ *Transition:* "We validate AbeT across classification, semantic segmentation, and object detection."

**P4 (Evidence Preview):** "On standard benchmarks, AbeT reduces FPR@95 by 45–78% over comparable single-stage methods, with consistent gains across three tasks and multiple architectures. We also provide visual and quantitative evidence consistent with the hypothesis that AbeT learns to separate OOD inputs through exposure to misclassified ID examples during training."

### Alternative Storyline (Candidate B — Application-first)

**P1:** Start with a concrete deployment scenario (autonomous driving, medical diagnosis) where OOD inputs cause safety failures.
**P2:** Introduce learned temperature and energy scoring as technical solutions, then state their limitations in this deployment context.
**P3:** Present AbeT as a method that resolves these limitations.
**P4:** Show deployment-relevant results across detection, segmentation, and classification.

*Verdict:* Candidate A is stronger because it establishes the technical gap more precisely before discussing contributions. Candidate B may be better for an application-oriented venue.

### Alignment Checks for Candidate A

- **(a) Problem alignment:** The problem (OOD detection under distribution shift) → solution (AbeT score) chain is direct and consistent.
- **(b) Variable alignment:** The core concepts (learned temperature, energy score, Forefront Temperature Constant, ablation) appear consistently in the introduction, method section, and experiments.
- **(c) Contribution-evidence alignment:** The three contributions map directly to experiments: combination → Table 1 main results, ablation → Appendix B.1, mechanistic analysis → Section 5.

## Priority Revision Plan
```text
ASCII Diagram — Revision Strategy Roadmap

[Current manuscript state]
    │
    ├── P0 (Critical — Before Resubmission)
    │   ├── Fix Table 1 architecture mismatch
    │   │   └── Reproduce ReAct/DICE on ResNetv2-101
    │   ├── Add multi-seed variance (3 seeds)
    │   │   └── Report mean±std across seeds
    │   └── Tone down "contradiction" claims
    │       └── Replace with "counterproductive scaling"
    │
    ├── P1 (High Priority — Next Revision)
    │   ├── Add controlled experiment for mechanistic claim
    │   │   └── High-accuracy model → measure OOD degradation
    │   ├── Quantify "few misclassified ID examples" limitation
    │   │   └── Plot OOD metric vs training misclassification rate
    │   ├── Add "AbeT (unablated)" row to Table 1
    │   └── Move "all methods fail on misclassified ID" to main text
    │
    ├── P2 (Medium Priority — Quality Improvement)
    │   ├── Restructure abstract (5-sentence structure)
    │   ├── Restructure introduction (P1-P4 per outline)
    │   ├── Add explicit score direction to Problem Statement
    │   └── Clarify PEBAL comparison in Table 2
    │
    └── Deferred
        └── Novelty verification (requires external literature search)
            └── Manual verification by authors/reviewers
```

### P0 Items (Critical, Before Resubmission)

| ID | Task | Effort | Impact | Location |
|---|---|---|---|---|
| P0.1 | Reproduce ReAct/DICE on ResNetv2-101 or report reproduced numbers | Medium | High (comparison fairness) | Page 6, Table 1 |
| P0.2 | Add multi-seed variance (±std across 3 seeds) for main results | Low | High (statistical reliability) | Page 6, Table 1 |
| P0.3 | Replace "contradiction" with precise terminology | Low | Medium (scholarly accuracy) | Pages 2, 4 |

### P1 Items (High Priority, Next Revision)

| ID | Task | Effort | Impact | Location |
|---|---|---|---|---|
| P1.1 | Controlled experiment: high-accuracy model → measure OOD degradation | Medium | High (mechanistic claim validation) | Page 7, Section 5 |
| P1.2 | Quantify "few misclassified ID examples" threshold | Low-Medium | Medium (actionable limitation) | Page 9, Section 7 |
| P1.3 | Add "AbeT (unablated)" row to Table 1 | Low | Medium (direct ablation visibility) | Page 6, Table 1 |
| P1.4 | Elevate "all methods fail on misclassified ID" to main text | Low | Medium (interesting finding) | Page 9 or 7 |

### P2 Items (Medium Priority, Quality Improvement)

| ID | Task | Effort | Impact | Location |
|---|---|---|---|---|
| P2.1 | Restructure abstract to 5-sentence flow | Low | Medium (readability) | Page 1 |
| P2.2 | Restructure introduction per Candidate A outline | Medium | Medium (narrative clarity) | Pages 1-2 |
| P2.3 | Add explicit score direction to Problem Statement | Low | Low (clarity) | Page 3 |
| P2.4 | Add visual separator for PEBAL in Table 2 | Low | Low (presentation) | Page 8 |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | OOD detection: classification | CIFAR-10 (ID) → 4 OOD datasets; ResNet-20 | FPR@95, AUROC | AbeT: 12.5±2 FPR@95, 97.8±1 AUROC | C1 (combination) + C2 (ablation) | No multi-seed variance; single architecture |
| E2 | OOD detection: classification | CIFAR-100 (ID) → 4 OOD datasets; ResNet-20 | FPR@95, AUROC | AbeT: 31.1±12 FPR@95, 94.0±1 AUROC | C1 + C2 | No multi-seed variance |
| E3 | OOD detection: classification | ImageNet-1k (ID) → 4 OOD subset; ResNetv2-101 | FPR@95, AUROC | AbeT: 40.0±11 FPR@95, 91.8±3 AUROC | C1 + C2 | Baseline architecture mismatch for ReAct/DICE |
| E4 | Ablation: Forefront Temp. Constant | Same as E1-E3, compare unablated vs ablated | FPR@95 reduction | 28.76%, 59.00%, 24.81% reduction per ID dataset | C2 (ablation value) | Not in main table; only in appendix |
| E5 | Cosine vs Inner Product head | CIFAR-10/100, ImageNet-1k | FPR@95, AUROC | Reaffirms Hsu et al. (2020) finding | Supports architectural choice | Not a new finding |
| E6 | Gradient Input Perturbation | ODIN perturbation applied to AbeT | FPR@95, AUROC | "Harmed our method" | Negative result | No details on perturbation magnitude tuning |
| E7 | Mechanistic analysis | CIFAR-10, LSUN OOD; t-SNE | Visual + empirical | OOD points near misclassified ID points; scores higher on misclassified ID | C3 (intuition) | Correlational; t-SNE distorts global distances |
| E8 | Semantic segmentation | Cityscapes → LostAndFound, RoadAnomaly | mIOU, FPR@95, AUPRC, AUROC | FPR@95 3.42 (LostAndFound), AUPRC 31.12 (RoadAnomaly) | Generalizability | Small ID mIOU drop (80.56 vs 81.39) |
| E9 | Object detection | PASCAL VOC → COCO | AP, FPR@95, AUROC, AUPRC | AUROC 65.34, AUPRC 91.76 | Generalizability | No variance; VOS uses non-native OOD scoring |
| E10 | AbeT + post-hoc methods (ReAct/DICE/ASH) | CIFAR-10/100, ImageNet-1k | FPR@95, AUROC | Consistent improvements with each post-hoc method | Complementarity | Post-hoc method parameters may need tuning |

### Research-Theme Gap Diagnosis

**New Knowledge:** The paper's key potential contribution is identifying that the learned temperature appears in two roles in the combined energy score, and that one role (Forefront Temperature Constant) counteracts separation. This is a new analysis insight. However, the novelty cannot be fully assessed without external literature verification.

**Reproducibility:** The method architecture is simple (one extra fully-connected layer + BatchNorm + sigmoid) and well-described. However, the missing multi-seed variance and the architecture mismatch in Table 1 weaken reproducibility confidence. The code availability statement is positive.

**Impact on Practice/Understanding:** If validated, the method could be practically useful due to its simplicity (single-line architectural change, no OOD data, no hyperparameters). The understanding section (Section 5) provides plausible intuition but does not rise to the level of established mechanism.

### Proposed Research Experiments

**P1-ExpA: High-accuracy degradation test (P1 Priority)**
- *Target Claim:* C3 — Misclassified ID exposure drives OOD detection.
- *Hypothesis:* When training accuracy approaches 100% (few misclassified ID examples), AbeT's OOD detection degrades.
- *Minimal Design:* Train on CIFAR-100 with (a) standard augmentation, (b) stronger augmentation (TrivialAugment), (c) larger model (ResNet-110). Measure training misclassification rate and OOD FPR@95 on the 4-test-dataset average.
- *Controls/Baselines:* Same experiment with standard Energy score (no learned temperature) to isolate the temperature-driven effect.
- *Metrics:* FPR@95, training misclassification count.
- *Success Criterion:* Strong negative correlation (ρ < -0.7) between training misclassification rate and OOD detection performance for AbeT, and weaker correlation for Energy baseline.
- *Estimated Cost/Time:* ~2 GPU-days (3 training runs).
- *Expected Gain:* Either validates or refutes the mechanistic claim.

**P1-ExpB: Multi-seed variance suite (P0/P1 Priority)**
- *Target Claim:* All classification claims.
- *Hypothesis:* AbeT's improvements are statistically significant across random seeds.
- *Minimal Design:* Repeat E1, E2, and E3 × 3 seeds each. Report mean ± std.
- *Controls/Baselines:* Same 3 seeds for strongest competitor (Energy+ASH).
- *Metrics:* Mean ± std FPR@95, AUROC; paired t-test vs competitor.
- *Success Criterion:* AbeT outperforms competitor with p < 0.05 in at least 2 of 3 ID datasets.
- *Estimated Cost/Time:* ~4 GPU-days.
- *Expected Gain:* Statistical credibility for main empirical claims.

**P1-ExpC: Architecture-matched baselines for ImageNet (P0 Priority)**
- *Target Claim:* SOTA on ImageNet-1k.
- *Hypothesis:* Reproducing ReAct/DICE on ResNetv2-101 yields comparable or lower performance than reported.
- *Minimal Design:* Implement ReAct and DICE using author-provided code on ResNetv2-101 with identical training setup.
- *Metrics:* FPR@95, AUROC.
- *Success Criterion:* Reproducibility established or honest reporting of reproduced numbers.
- *Estimated Cost/Time:* ~6 GPU-days (fine-tuning + evaluation).
- *Expected Gain:* Comparison fairness.

**P2-ExpD: OOD detection as function of training misclassification rate (P2 Priority)**
- *Target Claim:* Limitation quantification (Section 7).
- *Hypothesis:* A quantitative relationship exists between training accuracy and OOD detection performance.
- *Minimal Design:* Train multiple checkpoints with varying training accuracy (via early stopping or data fraction) and measure AbeT's FPR@95.
- *Metrics:* Plot training misclassification rate vs FPR@95.
- *Success Criterion:* Clear monotonic relationship, enabling a practical "caution threshold."
- *Estimated Cost/Time:* ~2 GPU-days.
- *Expected Gain:* Actionable limitation for practitioners.

```text
ASCII Diagram — Experiment Upgrade Plan

P0 (Before Resubmission)
├── ExpC: Architecture-matched baselines (ReAct/DICE on ResNetv2-101)
└── ExpB (partial): 3-seed variance for main settings

P1 (Next Revision)
├── ExpA: High-accuracy model → test mechanistic claim
├── ExpB (complete): Full multi-seed suite + significance tests
└── ExpC (complete): Full reproduction report

P2 (Before Final Submission)
└── ExpD: Training accuracy vs OOD performance curve
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6/10**

This score reflects the paper's strengths (conceptually clean method, consistent cross-domain results, honest limitations) balanced against its weaknesses (comparison fairness concerns, missing statistical variance, correlational mechanistic evidence, and deferred novelty verification).

**Score breakdown:**
- **Research value (primary):** 6/10 — The method is simple and practically useful, but the mechanistic contribution is correlational and the novelty relative to existing work cannot be verified in this run.
- **Validity/Soundness:** 6/10 — Core method derivation is sound, but the main comparison table has architecture mismatches and no multi-seed variance.
- **Novelty:** N/A (deferred — external literature verification unavailable).
- **Reproducibility:** 7/10 — Method architecture is simple and well-described; code is promised. Missing training hyperparameter details in main text and no multi-seed reporting.
- **Clarity:** 7/10 — Generally well-written but abstract and introduction could be more structured.

**Post-Revision Target: [7, 8]/10**

If the authors address the P0 and P1 items (fix architecture matching, add multi-seed variance, add controlled experiment for mechanistic claim, quantify limitations, restructure abstract/intro), the paper could reach 7-8/10. The upper bound of 8 assumes that novelty holds up under external verification and that the ablation benefit remains robust under matched comparisons. The lower bound of 7 assumes that only the P0 items are addressed before resubmission.