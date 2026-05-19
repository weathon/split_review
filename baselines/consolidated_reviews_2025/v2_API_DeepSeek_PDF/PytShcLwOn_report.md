## Summary
# Final Review Report

## Summary

This paper introduces SIGHT (Single-Image Conditioned Generation of Hand Trajectories), a new task: given a single image of an object (either with an interacting hand or standalone), generate a realistic 3D hand trajectory that completes the implied manipulation action. The authors propose SIGHT-Fusion, a system combining (1) VISOR-HOS for hand-object detection, (2) CLIP for object-level and part-level visual feature extraction, and (3) a diffusion-based motion generator adapted from MDM to produce 17-joint right-hand trajectories conditioned on visual features. Training does not require action labels. Evaluation on FPHAB and HOI4D datasets uses ACC (action classifier accuracy), Diversity (FID-based), and Fidelity (FID) metrics, plus a physics simulation (MuJoCo) hit-rate metric for four manipulation tasks.

**Core Assessment:** The paper proposes a genuinely new task that bridges static hand-object understanding and dynamic motion generation, which is timely and relevant for robotics, AR/VR, and animation. The SIGHT-Fusion pipeline is well-motivated and the evaluation is reasonably comprehensive given the novelty of the task. However, several methodological concerns reduce the strength of the claims: (1) test-set leakage via FID-based checkpoint selection, (2) action-merging on FPHAB that may conflate object-specific trajectory variations, (3) limited simulator evaluation (4 of 45 tasks) with unexplained GT outperformance, (4) grammatical errors and misplaced paragraphs in the manuscript, and (5) a conclusion that omits limitations. Novelty/comparison conclusions are deferred to manual verification due to external literature search being unavailable in this run.

## Strengths
1. **Novel task formulation.** The SIGHT task — generating 3D hand trajectories from a single image — is genuinely new and bridges static hand-object understanding with dynamic motion generation. This is a well-motivated problem with clear applications in robotics, embodied AI, character animation, and AR/VR.

2. **Clean pipeline design.** SIGHT-Fusion follows a logical two-stage architecture: feature extraction (VISOR-HOS + CLIP) and conditional diffusion generation (adapted MDM). The use of foundation model features (CLIP) for cross-instance generalization is sensible, and the part-feature ablation (Section 4.5) provides a clear demonstration of the value of contact-region features.

3. **Comprehensive evaluation framework.** The paper establishes benchmarks on two datasets (FPHAB and HOI4D) with multiple metrics (ACC, Diversity, FID) and multiple baselines (T2M-T, MDM-T, MDM-I). The introduction of a physics simulation hit-rate metric for downstream task success is a noteworthy methodological contribution.

4. **Generalization evaluation.** The HOI4D instance split (Table 2) provides a meaningful test of cross-instance generalization, showing that object-centered features improve ACC from 0.734 (MDM-I) to 0.909 (ours, obj.). The location split further tests robustness to unseen backgrounds.

5. **Part-feature analysis.** The disambiguation experiment (Table 3) cleanly demonstrates that part-level features improve action classification accuracy on multi-action objects (ACC from 0.359 to 0.450), providing mechanistic insight into why the proposed feature extraction pipeline works.

## Weaknesses
1. **Test-set leakage via checkpoint selection (Major).** The authors select the checkpoint achieving the lowest FID on the test set (Page 7 - Implementation details). This violates standard ML practice and optimistically biases all reported FID/ACC/Diversity metrics. The claim that this is "consistent with the human motion generation literature" does not make it methodologically sound.

2. **FPHAB action merging conflates object-specific trajectories (Major).** Merging all actions by verb (e.g., "pour juice," "pour milk," "pour salt" → "pour") ignores object-specific trajectory variations. The ACC classifier operates on this merged label space, potentially penalizing methods that generate correct but object-appropriate diverse trajectories. The paper does not analyze per-verb accuracy or the impact of this merging.

3. **Simulator evaluation limited in scope (Major).** Only 4 of 45 FPHAB activities are tested in simulation. The counterintuitive finding that generated trajectories outperform ground-truth ones on juice (84.4% vs 78.1%) and milk (65.6% vs 64.1%) tasks is not adequately explained — if GT human trajectories are ground truth, why are they worse at pouring? This may indicate retargeting artifacts or object-shape mismatch rather than genuine trajectory quality.

4. **Loss function ambiguity (Moderate).** The velocity loss operates in 6D rotation representation space rather than Cartesian joint space, which may not correspond to physically meaningful velocities. The hyperparameters λ_pos and λ_velocity are not specified in the main text.

5. **Missing limitations section (Moderate).** The conclusion (Page 10) omits any discussion of limitations. A new task paper should explicitly bound its contributions: right-hand-only, only two datasets, limited simulator tasks, test-set leakage in checkpoint selection.

6. **Grammatical errors and misplaced content (Minor).** "Motion in simulator" paragraph (Page 4) has multiple typos ("with to much speed," "is a challenging as," "RL learning") and is placed under Related Work rather than Experiments. The method overview paragraph (Page 2) has a subject-verb agreement error: "Using a general-purpose vision foundation models... effectively generalize."

7. **Related Work reads as a list (Minor).** The Whole-Body Motion Generation paragraph (Page 3) is a chronological list of VAEs and diffusion models without organizing by comparison axes relevant to this paper (e.g., conditioning modality, body part granularity, evaluation protocol).

8. **Novelty claims unverifiable without external literature (Deferred).** Due to external paper search being unavailable in this run, claims such as "first to evaluate physical realism of generated trajectories in a simulator" and "novel task" cannot be independently verified against the literature. These are marked as deferred manual verification.

## Key Issues
### Issue 1 (Must Fix): Test-set FID checkpoint selection
**Location:** Page 7 - Implementation Details
**Risk:** Invalidates the reported FID, ACC, and Diversity as unbiased estimates.
**Fix:** Switch to a held-out validation set for checkpoint selection. Re-report all metrics.
**Severity:** Major

### Issue 2 (Must Fix): FPHAB action merging
**Location:** Page 6 - FPHAB paragraph
**Risk:** ACC metric may penalize correct object-specific trajectory variations.
**Fix:** (a) Report per-verb accuracy breakdown, (b) Analyze whether methods with higher ACC also generate more object-appropriate trajectories, (c) Consider verb+object label space for FPHAB.

### Issue 3 (Must Fix): Simulator evaluation limitations
**Location:** Page 10 - Section 4.6
**Risk:** Claims of "physical realism" and "downstream usefulness" are based on only 4 tasks, with unexplained GT outperformance.
**Fix:** (a) Hit rates need confidence intervals, (b) Analyze why GT underperforms on some tasks, (c) Expand to at least 8-10 tasks, (d) Acknowledge as explicit limitation.

### Issue 4 (Should Fix): Missing limitations in conclusion
**Location:** Page 10 - Conclusion
**Risk:** Reader cannot judge the scope of claims.
**Fix:** Add a dedicated limitations paragraph.

### Issue 5 (Should Fix): Loss function ambiguity
**Location:** Page 5-6 - Equation (1)
**Risk:** Reduced reproducibility. Velocity computed in 6D space may not be physically meaningful.
**Fix:** Clarify variable definitions, report λ values, add note on velocity representation.

## Actionable Suggestions
### S1. Fix test-set checkpoint selection (Must, P0)
**Current:** "select the checkpoint achieving the lowest FID metric on the test set" (Page 7).  
**Action:** Hold out 10% of training data as validation split. Select checkpoint with lowest FID on validation. Re-run evaluation on test set with this single checkpoint. Report both old (biased) and new (unbiased) metrics for transparency.

### S2. Analyze FPHAB action merging impact (Must, P0)
**Current:** All "pour*" actions merged into one class (Page 6).  
**Action:** Train the ACC classifier on verb+object labels instead of verb-only. Report a confusion matrix showing which specific actions are confused. Compare part-feature model vs object-feature model on per-object accuracy for multi-action objects (e.g., juice bottle: open vs close vs pour). This would strengthen the disambiguation claim in Section 4.5.

### S3. Address simulator evaluation limitations (Must, P0)
**Current:** 4 tasks, no confidence intervals, GT outperformance unexplained.  
**Action:**  
- Add bootstrap confidence intervals for all hit rates (1000 resamples).  
- Analyze the retargeting pipeline: does the human-to-robotic hand retargeting introduce systematic errors that affect GT more than generated trajectories? If so, report retargeting fidelity.  
- Expand to at least 8 tasks covering diverse action types (e.g., stirring, screwing, cutting from FPHAB).  
- Add a "random trajectory" baseline to establish floor performance.

### S4. Fix grammatical errors and paragraph placement (Nice-to-have, P1)
**Action:**  
- Rewrite "Motion in simulator" paragraph (Page 4) and move to Section 4.6.  
- Fix "a general-purpose vision foundation models" → "a general-purpose vision foundation model" or "general-purpose vision foundation models" (Page 2).  
- Fix "effectively generalize" → "effectively generalizes" (Page 2).  
- Fix "is a challenging as" → "are challenging, as" (Page 4).  
- Fix "with to much speed" → "with too much speed" (Page 4).  
- Fix "RL learning" → "RL" (Page 4).

### S5. Restructure Related Work (Nice-to-have, P1)
**Action:** Reorganize the whole-body motion generation paragraph by comparison axes: (a) conditioning modality (text/audio/label vs image), (b) output granularity (whole-body vs hand-only), (c) evaluation protocol (FID/ACC vs simulation). This would make the positioning of SIGHT-Fusion clearer.

### S6. Add limitations and rewrite conclusion (Must, P0)
**Action:** See the Mentor Revised Version in Annotation 14 (Page 10 - Conclusion). Include right-hand-only, limited datasets, action merging, test-set leakage, and limited simulator evaluation.

### S7. Clarify loss function (Nice-to-have, P1)
**Action:** Add explicit variable definitions linking r/ˆr to x0/G(xt,t,c). Report λ_pos and λ_velocity values. Add a note that velocity loss operates in 6D rotation representation space and is complemented by L_pos in Cartesian space.

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The current introduction has 5 paragraphs with the following roles:
- P1 (Page 1): Motivation + gap (implicit) — opens with an engaging example but lacks explicit gap statement
- P2 (Page 1): Task definition — clear but partially redundant with abstract
- P3 (Page 2): Literature gap — reads as a paper list rather than organized comparison
- P4 (Page 2): Challenges — well-structured but missing prioritization
- P5 (Page 2): SIGHT-Fusion overview — vague insight statement with grammatical errors

The three alignment checks show partial issues:
- (a) **Problem alignment:** The stated challenge (ambiguous trajectory generation) matches the solution (image-conditioned diffusion), but the gap is not stated until P3.
- (b) **Variable alignment:** Key concepts in the introduction (object features, part features, diffusion) appear in the method, but the "visual features" mentioned in P5 are not defined until Section 3.2.
- (c) **Contribution-evidence alignment:** The contribution list (Page 3) claims "superior performance" but this is only supported in Tables 1-3 much later.

### Recommended Storyline (Option A: Best)
Follow a clear Big Picture → Gap → Solution → Evidence → Contribution arc:

P1: **Big picture + Stakes.** "When a human hand grasps an object, the brain immediately plans a manipulation trajectory. For AI systems to interact with the physical world naturally, they need a similar ability: given a single image, infer the most likely future hand trajectory. This capability would benefit robotics, character animation, and human intent prediction." [Same as current but shorter]

P2: **Explicit gap.** "Existing work falls short in two ways. First, hand-object interaction research has focused on static analysis (detection, segmentation, 3D reconstruction) without generating temporal trajectories. Second, human motion generation has concentrated on whole-body movements conditioned on text or action labels — hand-specific trajectory generation from a single image remains unexplored." [New — replaces current P3-style listing]

P3: **Our solution.** "We propose SIGHT-Fusion, which combines VISOR-HOS for object detection, CLIP for visual feature extraction, and a conditional diffusion model adapted from MDM to generate 17-joint right-hand trajectories. The core insight is that part-level features from the hand-object contact region help disambiguate which action to perform when the same object supports multiple uses." [Replaces current P5]

P4: **Evidence preview.** "On FPHAB, SIGHT-Fusion achieves 0.417 ACC (+5.9% over MDM-I). On HOI4D unseen object instances, it reaches 0.909 ACC (+17.5% over MDM-I). Physics simulation on 4 manipulation tasks yields hit rates comparable to or exceeding ground-truth trajectories on 3 of 4 tasks."

P5: **Contributions.** [Same as revised contribution list in Annotation 7]

This ordering ensures the reader knows what is missing (P2) before learning about the solution (P3), making the contribution clearer.

### Abstract Outline (Complete)
S1 (Problem): "We introduce SIGHT, a task for generating realistic 3D hand trajectories from a single image — either a hand-object interaction scene or a standalone object."

S2 (Challenge): "This is challenging because the model must infer the intended action from visual cues alone, without action labels, and must handle object ambiguity (multiple possible interactions per object)."

S3 (Method): "Our SIGHT-Fusion system combines VISOR-HOS for hand-object detection, CLIP for object-level and part-level feature extraction, and a conditional diffusion model to generate 17-joint right-hand trajectories."

S4 (Key results): "On FPHAB, SIGHT-Fusion achieves 0.417 ACC (+0.059 over image-only MDM). On HOI4D instance split (unseen objects), ACC reaches 0.909 (+0.175). Physics simulation on 4 tasks yields hit rates of 54.6-84.4%."

S5 (Bounded claim): "These results demonstrate the viability of single-image-conditioned hand trajectory generation. Limitations include right-hand-only evaluation and action-label merging on FPHAB."

### Introduction Outline (Complete)
P1 (Motivation + Stakes): Opening paragraph establishing the practical importance of trajectory generation from a single image. Replace the generic "could benefit immensely" with concrete application scenarios. End with: "In this paper, we investigate this problem."

P2 (Research Gap): Explicitly state that prior work does not generate trajectories (static analysis only for HOI) or conditions on text/labels (not images). Use comparison axes, not paper lists.

P3 (Proposed Solution): State the SIGHT-Fusion pipeline with clear architecture preview. Define "object features" and "part features" at a high level.

P4 (Evidence Preview): Give 2-3 key quantitative results from Tables 1, 2, and 4 to orient the reader.

P5 (Contributions): Revised contribution list (4 items) from Annotation 7.

## Priority Revision Plan
### P0 — Critical (Must fix before resubmission)

| # | Item | Effort | Impact | Annotation Ref |
|---|------|--------|--------|---------------|
| 1 | **Test-set checkpoint selection** — Use validation split instead of test set for model selection | Medium | High | Ann. 12 |
| 2 | **FPHAB action merging analysis** — Report per-verb accuracy; consider verb+object labels | Medium | High | Ann. 11 |
| 3 | **Simulator evaluation** — Add CI, analyze GT outperformance, expand tasks | High | High | Ann. 13 |
| 4 | **Add limitations section** — Right-hand only, dataset scope, simulator scope, checkpoint bias | Low | High | Ann. 14 |

### P1 — Important (Should fix)

| # | Item | Effort | Impact | Annotation Ref |
|---|------|--------|--------|---------------|
| 5 | **Rewrite conclusion** with quantitative evidence and limitations | Low | Medium | Ann. 14 |
| 6 | **Restructure introduction** following the recommended storyline | Medium | Medium | Ann. 2,4,5,6 |
| 7 | **Clarify loss function** — variable definitions, λ values, velocity representation note | Low | Medium | Ann. 10 |
| 8 | **Fix grammatical errors** — "a general-purpose vision foundation models," "with to much speed," etc. | Low | Low | Ann. 6, 9 |

### P2 — Nice-to-have (Improve quality)

| # | Item | Effort | Impact | Annotation Ref |
|---|------|--------|--------|---------------|
| 9 | **Restructure Related Work** by comparison axes | Medium | Medium | Ann. 8 |
| 10 | **Move "Motion in simulator" paragraph** to Section 4.6 | Low | Low | Ann. 9 |
| 11 | **Tighten contribution list** — replace "superior performance" with specific claims | Low | Medium | Ann. 7 |

### Revision Order
1. Fix test-set checkpoint selection (P0#1) — affects all metrics
2. Add limitations and rewrite conclusion (P0#4, P1#5) — immediate scope control
3. Analyze FPHAB action merging (P0#2) — may change result interpretation
4. Expand simulator evaluation (P0#3) — strengthens claims
5. Clarify loss function and fix grammar (P1#7, P1#8) — reproducibility
6. Restructure introduction and Related Work (P1#6, P2#9) — narrative quality
7. Move paragraph, tighten claims (P2#10, P2#11) — manuscript polish

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Main comparison (Table 1) | FPHAB subject split + HOI4D location split vs T2M-T, MDM-T, MDM-I | ACC, DIV, FID | Ours part achieves 0.417 ACC on FPHAB (+0.059 over MDM-I); 0.885 ACC on HOI4D loc. | Image features improve ACC/FID; part>object | Test-set leakage (FID selection) |
| E2 | Generalization (Table 2) | HOI4D instance split: Ours obj vs MDM-I | ACC, DIV, FID | Ours obj: 0.909 ACC vs 0.734 MDM-I | Object-centered features generalize to unseen instances | Only one baseline; only HOI4D |
| E3 | Part-feature disambiguation (Table 3) | FPHAB subset: 3 objects with 3 actions each | ACC, DIV, FID | Ours part: 0.450 ACC vs Ours obj: 0.359 | Part features help disambiguate multi-action objects | Only 3 objects; only FPHAB |
| E4 | Physics simulation (Table 4) | MuJoCo: 4 tasks, retarget to Adroit hand | Hit rate (%) | Ours: 84.4% juice, 65.6% milk, 54.6% salt, 60.1% soap | Generated trajectories achieve physical task success | Only 4/45 tasks; GT outperformance unexplained; no CI |

### Research-Theme Gap Diagnosis

1. **New Knowledge (Partially supported):** The claim that part-level features disambiguate actions is supported by Table 3 but only tested on 3 objects. The generalization claim (Table 2) is strong but uses only one baseline.

2. **Reproducibility (Partially supported):** The method is described in reasonable detail, but missing hyperparameters (λ values), ambiguous variable definitions in the loss function, and test-set leakage reduce reproducibility.

3. **Impact on Practice/Understanding (Weakly supported):** The simulator evaluation is the strongest evidence for downstream applicability, but limited to 4 tasks. The counterintuitive GT outperformance undermines confidence.

### Proposed Research Experiments

**P0-Exp1: Validation-set-based re-evaluation**
- **Target Claim:** Main comparison results (Table 1)
- **Hypothesis:** Re-evaluating with validation-set checkpoint selection will yield similar or slightly lower metrics
- **Minimal Design:** Hold out 10% of training data, select checkpoint by validation FID, re-report Table 1
- **Controls/Baselines:** Same baselines
- **Metrics:** ACC, DIV, FID
- **Success Criterion:** ACC within 0.02 of reported values
- **Estimated Cost/Time:** 2-3 days (re-training with validation split)
- **Expected Paper-Quality Gain:** High — removes a major methodological concern

**P0-Exp2: FPHAB per-object accuracy breakdown**
- **Target Claim:** Part features disambiguate actions (Table 3)
- **Hypothesis:** Per-object accuracy (e.g., "pour juice" vs "pour milk") will show larger part-feature advantage than verb-level accuracy
- **Minimal Design:** Report confusion matrix over verb+object labels for Table 3 setting
- **Controls/Baselines:** Object-only model
- **Metrics:** Per-class ACC, confusion matrix
- **Success Criterion:** Part model shows higher per-object accuracy on all 3 objects
- **Estimated Cost/Time:** 1-2 days (re-running evaluation with new labels)
- **Expected Paper-Quality Gain:** High — strengthens the core disambiguation claim

**P1-Exp3: Simulator expansion to 8+ tasks**
- **Target Claim:** Physical realism and downstream usefulness (Table 4)
- **Hypothesis:** Method maintains competitive hit rates across diverse action types
- **Minimal Design:** Select 4 additional FPHAB tasks (e.g., stirring, screwing, cutting, opening), build MuJoCo environments, evaluate all methods
- **Controls/Baselines:** GT, MDM-I, MDM-T
- **Metrics:** Hit rate, bootstrap CI
- **Success Criterion:** Method achieves top-1 or top-2 hit rate on at least 6/8 tasks
- **Estimated Cost/Time:** 2-3 weeks (environment design + simulation)
- **Expected Paper-Quality Gain:** High — transforms simulator evaluation from proof-of-concept to robust benchmark

**P1-Exp4: Biomechanical plausibility check**
- **Target Claim:** Generated trajectories are "smooth, natural and anatomically plausible" (Page 2, challenges)
- **Hypothesis:** Generated trajectories have similar joint-angle velocity profiles and range-of-motion distributions as GT
- **Minimal Design:** Compute joint-angle acceleration (jerk) and range-of-motion histograms for Ours, MDM-I, MDM-T, and GT
- **Controls/Baselines:** MDM-I, MDM-T, GT
- **Metrics:** Mean jerk, joint-angle range, PCA-based motion naturalness score
- **Success Criterion:** Ours trajectories are closer to GT distribution than baselines on these biomechanical metrics
- **Estimated Cost/Time:** 3-5 days (analysis code + evaluation)
- **Expected Paper-Quality Gain:** Medium — adds a missing evaluation dimension

### ASCII Diagram — Experiment Upgrade Plan

```text
P0 Experiments (Must)
├── Exp1: Validation-set re-evaluation [Effort: Low, Impact: High]
│   └── Removes test-set leakage concern
└── Exp2: Per-object accuracy breakdown [Effort: Low, Impact: High]
    └── Strengthens part-feature disambiguation claim

P1 Experiments (Should)
├── Exp3: Simulator expansion to 8+ tasks [Effort: High, Impact: High]
│   └── Transforms simulator from proof-of-concept to robust benchmark
└── Exp4: Biomechanical plausibility [Effort: Medium, Impact: Medium]
    └── Addresses missing "smooth, natural" evaluation

Timeline: Exp1+Exp2 (1 week) → Exp4 (1 week) → Exp3 (2-3 weeks)
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5/10**

**Rationale:** The paper proposes a genuinely new and interesting task (SIGHT) with a well-motivated pipeline (SIGHT-Fusion). The evaluation is reasonably broad with two datasets, multiple metrics, and physics simulation. However, the score is limited by:

- **Research value (Primary dimension):** Moderate. The task is novel and relevant, but the methodological contribution is primarily an adaptation of existing components (VISOR-HOS + CLIP + MDM). The core technical novelty over the sum of its parts is incremental.
- **Validity:** Reduced by test-set leakage in checkpoint selection (major concern), action-merging artifacts, and limited simulator evaluation.
- **Novelty:** Deferred to manual verification due to unavailability of external literature search in this run. If the SIGHT task is indeed new (which seems plausible), novelty is a strength.
- **Reproducibility:** Partially supported. Described adequately but missing λ values and ambiguous loss function definitions.
- **Presentation:** Competent but with grammatical errors, misplaced paragraphs, and a conclusion lacking limitations.

**Post-Revision Target: [6.5, 7.5]/10**

If all P0 and P1 items are fixed (validation split, per-object accuracy, simulator expansion, limitations, loss clarification, grammar fixes), the paper would address its main validity concerns and present a stronger case. The upper bound is limited by the incremental nature of the technical contribution.

---

### ASCII Diagram — Paper Structure & Evidence Map

```text
[Problem: Generate 3D hand trajectories from a single image]
    │
    ├── [C1: New task (SIGHT)]  ← Evidence: Task definition (P1-P2)
    │   └── Gap: Prior work only does static detection/reconstruction
    │
    ├── [C2: Feature extraction pipeline]  ← Evidence: VISOR-HOS + CLIP (Sec 3.2)
    │   ├── Object features: cropped CLIP embedding
    │   └── Part features: contact-region CLIP grid average
    │
    ├── [C3: Conditional diffusion model]  ← Evidence: Adapted MDM (Sec 3.3)
    │   └── Replaces text encoder with CLIP visual encoder
    │
    └── [C4: Evaluation framework]  ← Evidence: Tables 1-4
        ├── ACC/DIV/FID on FPHAB + HOI4D
        └── MuJoCo hit-rate on 4 tasks
[RISK: Test-set leakage → all metrics potentially biased]
[RISK: FPHAB verb merging → ACC may not measure object-specific correctness]
```

### ASCII Diagram — Revision Strategy Roadmap

```text
Current State
    │
    ├── [Test-set leakage]              → Fix: Validation split [P0, High Impact]
    │   └── Metric validity at risk
    │
    ├── [Action merging]               → Fix: Per-object accuracy [P0, High Impact]
    │   └── ACC interpretation unclear
    │
    ├── [Limited simulator scope]       → Fix: Expand to 8+ tasks [P0, High Impact]
    │   └── Claims of "physical realism" weakly supported
    │
    ├── [Missing limitations]          → Fix: Add limitations paragraph [P0, Low Effort]
    │   └── Reader cannot judge scope
    │
    └── [Grammatical errors]           → Fix: Proofread [P1, Low Effort]
        └── Presentation quality

After P0 fixes: Methodologically sound, scope bounded, claims defensible
After P1 fixes: Ready for resubmission
```

### ASCII Diagram — Related-Work Taxonomy Tree (Layered)

```text
Related Work Taxonomy (Root: Hand-Object Interaction & Motion Generation)
├── Branch 1: Hand-Object Analysis (Static)
│   ├── Leaf 1.1: Detection & Segmentation
│   │   ├── Faster-RCNN + hand/object detection [Shan 2020]
│   │   ├── EgoHOS [Zhang 2022a]
│   │   └── COHESIV [Shan 2021]
│   └── Leaf 1.2: 3D Reconstruction
│       ├── HOLD [Fan 2024]
│       ├── ObMan [Hasson 2019]
│       └── What's in Your Hands [Ye 2022]
│
├── Branch 2: Motion Generation (Temporal)
│   ├── Leaf 2.1: Whole-body + Text/Label Conditioning
│   │   ├── MDM [Tevet 2022]
│   │   ├── T2M [Guo 2022]
│   │   ├── GMD [Karunratanakul 2023]
│   │   └── TEMOS [Petrovich 2022]
│   └── Leaf 2.2: Hand-specific Motion
│       ├── Affordance Diffusion [Ye 2023b] (static only)
│       ├── HMP [Duran 2023] (pose estimation, not generation)
│       └── Bao et al. 2023 (VR/AR coarse prediction)
│
└── Branch 3: Physics Simulation for Evaluation
    ├── Leaf 3.1: Static Grasp Stability
    │   ├── CPF [Yang 2021]
    │   └── DeepSimHO [Wang 2024]
    └── Leaf 3.2: Dynamic Trajectory Evaluation
        └── SIGHT-Fusion Simulator (this paper, 4 tasks)
            └── [Note: Authors claim 'first' — deferred verification]

Manuscript Positioning:
  SIGHT-Fusion sits at the intersection of Leaf 1.1 (uses VISOR-HOS),
  Leaf 2.1 (adapts MDM), and Leaf 3.2 (proposes simulator evaluation).
  The primary novelty is the task (SIGHT) and the image-conditioning
  mechanism, not the individual components.
```

### Page Coverage Audit

| Page | Annotation Count | Coverage Status | Notes |
|------|-----------------|-----------------|-------|
| 1 (Abstract + Intro P1-P2) | 3 | Covered | Abstract, Intro P1 (motivation), Intro P2 (task def) |
| 2 (Intro P3-P5) | 3 | Covered | Literature gap, Challenges, SIGHT-Fusion overview |
| 3 (Contributions + Related Work) | 2 | Covered | Contribution list, Hand motion generation RW |
| 4 (Fig 2 + Misplaced paragraph + Task def) | 1 | Covered | "Motion in simulator" paragraph |
| 5 (Method: Features + Diffusion) | 1 | Covered | Loss function equation audit |
| 6 (FPHAB + datasets) | 1 | Covered | FPHAB action merging issue |
| 7 (Metrics + Implementation details) | 1 | Covered | Test-set FID checkpoint selection |
| 8 (Results) | 0 | Skipped (boilerplate) | Results text is brief and largely descriptive of tables/figures |
| 9 (Tables + Part features + Sim setup) | 0 | Skipped | Tables 1-3 are data; related discussion is covered in other annotations |
| 10 (Sim results + Conclusion) | 2 | Covered | Simulator scope, Conclusion rewrite |
| 11-14 (References) | 0 | Skipped (non-substantive) | Reference list |
| **Total** | **14** | | |

### Contribution Novelty Verdict Board (Deferred)

Due to external literature search being unavailable in this run (Retrieval-Disabled Mode active), all novelty verdicts are marked as `unclear` with deferred manual verification. The following provisional analysis is provided for guidance:

| Claim ID | Author Contribution Claim | Novelty Verdict | Why | Confidence |
|----------|-------------------------|----------------|-----|-----------|
| C1 | New task (SIGHT): single-image conditioned hand trajectory generation | Unclear (deferred) | Plausibly new — requires literature verification on trajectory generation from static images | Medium |
| C2 | Feature extraction pipeline (VISOR-HOS + CLIP + part features) | Unclear (deferred) | Combination of existing components; novelty depends on whether similar pipelines exist | Medium |
| C3 | SIGHT-Fusion: conditional diffusion model for hand trajectories | Unclear (deferred) | Adaptation of MDM with CLIP visual encoder; novelty is in the adaptation, not the architecture | Medium |

**Contribution-level Novelty Conclusion:** External literature verification unavailable in this run (paper_search not started). Novelty/comparison conclusions are intentionally deferred for manual verification. The authors should conduct a thorough comparison with existing hand trajectory prediction methods (e.g., Bao et al. 2023, Affordance Diffusion) and motion generation approaches to clearly delineate their contribution boundaries.