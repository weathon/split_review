Now let me assemble the final consolidated review.

## Summary

This paper introduces WI3D (Weakly Incremental 3D object Detection), a new task where a 3D detector learns novel object classes using only 2D visual prompts (from off-the-shelf 2D detectors) rather than costly 3D annotations. The authors propose a framework with three components: (1) a class-agnostic Pseudo-label Refinement (PRF) module that denoises coarse 3D pseudo labels generated from 2D predictions, (2) Cross-modal Knowledge Transfer (CKT) using bipartite matching for feature-level representation learning of novel classes, and (3) Reweighting Knowledge Distillation (RKD) to selectively preserve base-class knowledge. Experiments on SUN RGB-D and ScanNet show consistent improvements over baselines including a prior class-incremental 3D detection method (SDCoT).

---

## Strengths

- **Novel and practically significant task formulation.** The paper defines WI3D, a setting that removes the need for expensive 3D annotations on novel classes by leveraging 2D visual prompts. This is clearly distinguished from prior class-incremental 3D detection (Fig. 1, Sec. 3.1) and addresses a realistic deployment scenario where 3D annotation is the bottleneck.

- **PRF module demonstrably improves novel-class pseudo labels.** The class-agnostic design, trained on base classes and applied to novel classes, yields +3.25% mAP_novel (Tab. 3). Ablations (Tab. 4) confirm that both box-coordinate and point-cloud-context inputs are needed for best performance, and the Binary Classification Header adds +0.96%.

- **CKT with bipartite matching outperforms naive one-to-many assignment.** The ablation in Tab. 6 shows CKT yields +1.43% mAP_novel, while the one-to-many strategy actually hurts (−0.35%), demonstrating the value of the Hungarian-style matching for clean cross-modal feature alignment.

- **RKD provides a clear improvement over standard distillation strategies.** Tab. 7 shows that RKD outperforms both KL-divergence and L2-distillation on both base and novel class mAP, validating the intuition that objectness-weighted distillation is more selective and effective.

- **Robustness across different 2D teachers.** Tab. 5 shows consistent gains with Faster R-CNN, Ground Dino, and human 2D annotations (+3.74% mAP_base, +9.49% mAP_novel for Ground Dino), demonstrating the framework is not tied to a specific 2D detector.

- **Comprehensive experimental validation.** Results are reported on two datasets (SUN RGB-D and ScanNet) under multiple incremental splits, with the method consistently outperforming all baselines.

---

## Weaknesses

### Major

- **SDCoT adaptation is described in insufficient detail.** The paper states it "modif[ies] the training of SDCoT to fit our weakly incremental learning setting" (line 161) but provides zero specifics about what was changed. SDCoT (Zhao & Lee, 2022) was designed for class-incremental 3D detection with 3D ground-truth annotations for novel classes; the modifications needed to run it without those annotations are non-trivial. Without knowing which losses were kept, how pseudo labels were fed in, or whether the co-teaching structure was preserved, the comparison in Tables 1–2 is hard to interpret. This does not invalidate the paper — the method still outperforms the other baselines (fine-tuning, freeze-and-add, base-training) by large margins — but it weakens the claim of surpassing prior class-incremental 3D methods specifically. The authors should fully describe the adaptation in a revision.

### Minor

- **CKT cost function in Equation (2) is written incorrectly.** The equation states: minimize ∑_i ∑_j m_{ij} * IoU(...), with ∑_i m_{ij}=1. Minimizing the *sum of IoU* would preferentially match 3D proposals to 2D boxes with the *least* overlap — the opposite of the intended behavior. The correct formulation should either maximize IoU or minimize (1 − IoU). The ablation results (Tab. 6) confirm the implementation works as intended (+1.43%), so this is a presentation typo rather than a methodological flaw. Nevertheless, the equation as printed is mathematically inconsistent with the stated goal and must be corrected.

- **No analysis of PRF generalization across diverse novel-class geometries.** PRF is trained on base classes and applied to novel classes that may differ in scale, shape, and point density. The paper provides ablation evidence that it helps (+3.25%), and the class-agnostic design is plausible, but there is no analysis of whether refinement quality degrades as the gap between base and novel distributions widens. A simple decomposition of PRF's per-class IoU improvement on base vs. novel classes would address this.

- **No sensitivity analysis for loss weights.** The weights β₁, β₂, β₃ = 1, 10, 5 are selected "heuristically" (line 135) and differ by an order of magnitude. A brief grid or at minimum a justification for these values would be useful for reproducibility.

- **No quantitative evaluation of pseudo label quality.** The paper shows mAP gains but does not report direct metrics on the pseudo labels themselves (e.g., IoU before/after PRF, recall of novel-class pseudo labels). This would directly support the claim that denoising is effective.

### Trivial

- **Results are reported from a single run without variance.** The reviewer notes this is "common practice in this subarea." Reporting variance across seeds would increase confidence but is not a structural flaw.
- **The number/order of incremental steps is not explicitly stated** for the main experiments (whether |C_novel|=5 classes are added all at once or sequentially). This could be clarified.

---

## Nice-to-Haves

- A small experiment or analysis showing PRF refinement accuracy (e.g., box IoU improvement) separately for novel vs. base classes.
- Sensitivity analysis or ablation on the β loss weights (1, 10, 5) used in the overall objective.
- Clarifying whether the incremental setting involves single-step or multi-step novel class addition.

---

## Removed Points

These points were flagged by reviewers but are removed or downgraded per the verification guidelines:

1. **"Keoi eoi" garbled phrase in Equation (5):** This is a parser artifact from PDF extraction, not a paper error. The original submission contains proper mathematical notation.
2. **BCH threshold not specified:** The paper explicitly states "the bounding box is considered valid only when the probability of presence exceeds the probability of absence" — this is a clear threshold criterion (effectively 0.5). The concern is unfounded.
3. **Criticism about "not yet released" or "cannot be independently verified":** Any such phrasing would be removed per the hard rules — cited references and entities are assumed to exist.
4. **Pure formatting/style nitpicks:** Removed per the hard rules — these are parser artifacts, not author errors.

---

## Novel Insights

The most interesting observation emerging across the reviews is the tension between the paper's two main knowledge transfer mechanisms: CKT (for novel-class learning via cross-modal feature alignment) and RKD (for base-class retention via selective distillation). The paper correctly identifies that naive feature-level supervision can actually hurt (−0.35% in the one-to-many variant in Tab. 6) and shows that bipartite matching resolves this by filtering noisy correspondences. This suggests that in weakly-supervised cross-modal 3D learning, *which* proposals get aligned matters as much as the alignment objective itself — a finding that extends beyond the incremental learning framing.

---

## Suggestions

1. **Fix the CKT cost function** in Equation (2) — it should minimize (1 − IoU) or maximize IoU. Clarify this is a bipartite matching formulation consistent with Hungarian matching conventions.
2. **Fully describe the SDCoT adaptation** — which losses were kept/modified, the source of pseudo labels used, and whether architectural changes were made.
3. **Add a PRF generalization analysis** showing per-class IoU improvement on base vs. novel classes to confirm the refinement transfers without degradation.
4. **Add pseudo label quality metrics** (IoU before/after PRF, recall) to directly support the denoising claim.
5. **Report results with standard deviation** over at least 3 random seeds for the main tables.

---

## Score and Decision

The paper addresses a well-motivated and underexplored problem, proposes a sensible framework with sound ablations, and shows consistent empirical gains across two datasets and multiple settings. The two most significant weaknesses — the CKT equation typo and the underspecified SDCoT adaptation — are correctable in revision and do not invalidate the core contribution. The equation error is a presentation issue (the ablation confirms the implementation works), and the SDCoT comparison, while important, is only one of several baselines the method outperforms.

The paper makes a genuine contribution: defining the WI3D task and providing a working framework with clear, ablated components. The current form requires clarification on two points before acceptance, but the technical core is solid.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>