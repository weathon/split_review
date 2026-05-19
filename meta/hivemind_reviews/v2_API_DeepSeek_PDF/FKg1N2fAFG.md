## Summary
# Final Review Report

## Summary

This paper addresses architecture overfitting in dataset distillation — the problem that synthetic data distilled by a shallow training network (e.g., 3-layer CNN) performs poorly when used to train deeper test networks with different architectures. The authors propose a combination of four complementary techniques applied to the test-network training side: (1) a DropPath variant with a three-phase keep-rate scheduler and improved shortcut connections, (2) reversed knowledge distillation (small teacher → large student), (3) periodic learning-rate resets with the Lion optimizer, and (4) multi-operation (k-fold) data augmentation. Extensive experiments on CIFAR-10, CIFAR-100, and Tiny-ImageNet with two distillation algorithms (FRePo and MTT) across ResNet18/50, AlexNet, and VGG11 demonstrate that the full method substantially reduces the architecture accuracy gap — for example, improving MTT-distilled ResNet50 on CIFAR-10 (IPC=10) from 28.1% (baseline) to 63.8% (+35.7 points). The same techniques also improve deep network training on limited real data with ≥100 samples. The paper is clearly written with thorough ablation studies; however, the overall novelty is incremental (each component is established), the main results lack variance reporting, several claims overstate the evidence scope, and the cross-architecture comparison with factorization-based distillation methods is deferred without rigorous justification.

## Strengths
1. **Well-defined and practically important problem**: Architecture overfitting is a recognized limitation in dataset distillation that limits downstream applicability. Targeting the test-network training side (rather than the distillation algorithm) is a practical choice that makes the approach orthogonal to future DD improvements.

2. **Comprehensive empirical evaluation**: The paper evaluates on three datasets (CIFAR-10, CIFAR-100, Tiny-ImageNet), two distillation methods (FRePo, MTT), four test architectures (ResNet18, ResNet50, AlexNet, VGG11), and three IPC settings (1, 10, 50), with 5-way ablation comparisons. This breadth is a genuine strength and provides reasonable evidence of generality within the tested scope.

3. **Thorough ablation studies**: Section 4.3 systematically isolates the contribution of each component (DropPath min/final keep rate, period of decay, improved shortcut, KD weight/temperature, periodical LR, Lion optimizer, augmentation strength). The hyperparameter sensitivity analyses (Figures 4 and 8) show the method is reasonably robust within practical ranges.

4. **Interesting DropPath single-branch extension**: The virtual shortcut variant for VGG-like architectures (Figure 2b) is a technically clean adaptation that opens DropPath to non-residual networks. This is one of the more novel technical contributions in the paper.

5. **Honest identification of teacher capacity ceiling**: The paper acknowledges in Section 4.2 that performance gain saturates when the teacher model is weak (Figure 3, fraction >0.05) and shows in Appendix B.5 that a stronger teacher (ResNet18) can continue to improve ResNet50. This transparency is commendable and suggests the authors understand the boundary conditions of their method.

## Weaknesses
The paper has several weaknesses that affect its scientific rigor, novelty positioning, and contribution strength:

1. **Incremental novelty with limited conceptual contribution**: Each component — DropPath, knowledge distillation, Lion optimizer, cosine annealing with warmup, k-fold augmentation — is a known technique. The paper's novelty lies in the specific composition and the reversed KD framing, which is a valid but incremental contribution. No new training algorithm, theoretical insight, or architectural innovation is introduced. The DropPath variant for single-branch networks is the most novel element, but it is a relatively small engineering adaptation.

2. **Missing variance reporting in main results**: Table 2 (the paper's central evidence table) reports single-run test accuracies without standard deviations or confidence intervals. Appendix B.3 acknowledges that standard deviation increases at low IPC (up to ±2.5 for IPC=1), which means some of the claimed gains may be within noise range. For a paper making strong comparative claims between ablation settings, this omission is significant.

3. **Overclaimed generality and efficiency**: The paper states methods are "generic" and "introduce negligible overhead" without evidence. Only CNN-family architectures on three small-scale image datasets are tested. The efficiency claim is not supported by any FLOP, latency, or parameter count comparison. These overstatements reduce the paper's scientific defensibility.

4. **Exclusion of relevant cross-architecture methods without rigorous justification**: Factorization-based distillation methods (Kim et al. 2022, Deng & Russakovsky 2022, Liu et al. 2022, Lee et al. 2022a) are excluded based on an IPC claim ("at least 5 times larger") that may not hold for all IPC=50 settings used in this paper. Since these methods directly address cross-architecture transfer, their exclusion weakens the novelty and comparison positioning of the paper's core claim.

5. **Causal mechanism for DropPath not validated**: The paper argues DropPath helps via ensemble averaging of shallower subnetworks, but does not provide diagnostic evidence (e.g., effective depth distribution) to support this causal pathway. The observed gains could alternatively come from the increased training stochasticity acting as an implicit regularization.

6. **Conclusion lacks limitations**: The four-sentence conclusion has no dedicated limitations paragraph, introduces an unsupported real-world deployment claim, and omits a quantitative summary of key results.

7. **Teacher-student reversal justification is incomplete**: The paper claims small models perform better on distilled data, but this conflates the training network's privileged position (data optimized for it) with general small-model capability.

## Key Issues
### Issue 1 — Missing variance in main results (High Severity)
The central evidence table (Table 2, Page 7) reports single-run test accuracies without standard deviations. Appendix B.3 (Table 8) shows that IPC=1 results have standard deviations up to ±2.5, and some inter-ablation differences are as small as 0.1-1.0 points (e.g., FRePo IPC=50, ResNet18: w/o KD 74.5 vs Full 74.5 — exactly tied). Without variance bounds, readers cannot judge whether ablation differences are meaningful. The paper's strongest claims (e.g., "+18.5% for ResNet18") are presented without confidence intervals. **Fix**: Move variance reporting into Table 2 or add a supplementary significance analysis table in the main text. Report mean±std for all settings with at least 3 seeds.

### Issue 2 — Overclaimed generality and efficiency (High Severity)
The paper claims the proposed methods are "generic" (Page 2) and "introduce negligible overhead" (Page 2) without evidence. Tested scope is limited to CNN-family architectures (ResNet, AlexNet, VGG) on three small image datasets (CIFAR-10/100, Tiny-ImageNet). No vision transformers, no NLP/speech tasks, no large-scale ImageNet-1K experiments. The efficiency claim has zero quantitative support — no training FLOPs, wall-clock time, memory usage, or parameter count comparisons. **Fix**: Replace absolute claims with bounded wording. Add an efficiency table showing training time per epoch with/without each component.

### Issue 3 — Exclusion of factorization methods weakens cross-architecture novelty claim (High Severity)
The Related Work section (Page 3) excludes factorization-based dataset distillation methods (Kim et al. 2022, Deng & Russakovsky 2022, Liu et al. 2022, Lee et al. 2022a) because their IPC is "at least 5 times larger." However, the paper tests IPC=50, which overlaps with factorization method regimes. The factorization approaches directly address cross-architecture transfer — the paper's central concern. Their exclusion means the paper does not benchmark against the most relevant prior work in cross-architecture dataset distillation. **Fix**: Add a qualitative comparison table in the main text or appendix showing the tradeoffs (IPC, cross-architecture accuracy, compute cost) between the proposed approach and factorization methods. Revise the IPC justification to be numerically precise for each cited factorization method.

### Issue 4 — DropPath causal mechanism not validated (Medium Severity)
The paper attributes DropPath's benefit to ensemble averaging of shallower subnetworks (Page 7), but provides no diagnostic evidence (e.g., effective depth distribution, subnetwork accuracy correlation with keep rate) to confirm this mechanism. An alternative explanation — increased stochasticity acting as implicit regularization — is not ruled out. **Fix**: Add a diagnostic experiment measuring effective depth during training and its correlation with architecture gap reduction.

### Issue 5 — Conclusion lacks limitations and overreaches (Medium Severity)
The four-sentence conclusion (Page 9) has no limitations section and introduces an unsupported "real-world scenarios" claim. **Fix**: Add a three-part limitations paragraph: (a) scope limited to CNN architectures on small-scale image datasets, (b) teacher capacity ceiling bounds the gain, (c) increased sensitivity at low IPC. Remove the real-world claim or mark it as speculation.

## Actionable Suggestions
### S1: Add standard deviations to Table 2 (Must)
Move the variance data from Appendix B.3 (Table 8) into the main result table. At minimum, report mean ± std for IPC=1 and IPC=10 settings where variance is highest. Add a footnote: "Results averaged over 3 random seeds." Add a paired one-sided significance test (e.g., Wilcoxon signed-rank) comparing Full vs Baseline for the primary setting (ResNet18, IPC=10, CIFAR-10).

### S2: Tighten generality claims (Must)
Replace "generic" (Abstract, Introduction) with bounded wording: "Our methods are evaluated on CNN-family architectures (ResNet18/50, AlexNet, VGG11) and small-scale image datasets (CIFAR-10/100, Tiny-ImageNet). Extension to transformer architectures and larger-scale settings remains future work." Add a similar bound to the efficiency claim or provide an efficiency table.

### S3: Add factorization method comparison (Must)
Include a qualitative comparison table in the main text or a new appendix section that contrasts the proposed approach with factorization-based cross-architecture methods (Kim et al. 2022, Deng & Russakovsky 2022, Liu et al. 2022, Lee et al. 2022a). Columns: Method, Paradigm, IPC Range, Cross-Architecture Acc, Training Cost. This is critical because the paper's core claim (mitigating architecture overfitting) competes directly with these methods. If IPC or cost differences prevent fair comparison, explicitly state the gap and why the proposed method is preferable in the small-IPC regime.

### S4: Add DropPath mechanism diagnostic (Nice-to-have)
Add a small diagnostic experiment: for a fixed minimum keep rate p_min, record the distribution of effective depths (number of active layers at each training step) and plot it against the accuracy gap with the 3-layer CNN. This would validate the claim that DropPath helps by reducing effective depth rather than by generic stochastic regularization.

### S5: Add limitations paragraph in conclusion (Must)
Replace the four-sentence conclusion with a structured ending containing:
- **Validated findings**: 1-2 sentences summarizing the key quantitative gain (e.g., "On MTT CIFAR-10 IPC=10, our method improves ResNet50 by 35.7 points, nearly closing the architecture gap.")
- **Bounded limitations**: 2-3 sentences on scope, teacher ceiling, and IPC sensitivity.
- **Future work**: 1 sentence on concrete next steps (e.g., transformer architectures, larger-scale distillation, dynamic teacher selection).

### S6: Revise knowledge distillation equation (Nice-to-have)
Add the softmax-with-temperature definition to Eq. (2) for reproducibility. See Page 5 annotation for the corrected formulation.

### S7: Report cross-architecture variance (Nice-to-have)
Add a row in the results summary or a supplementary figure showing the standard deviation of accuracy across the 4 test architectures for each setting. This would directly quantify claims about "decreasing the performance difference among different test network architectures" (Page 7).

## Storyline Options + Writing Outlines
### Abstract Outline (Revised)

The current abstract (Page 1) is too vague — it uses 3 sentences for problem definition and lacks quantitative anchoring. Recommended 5-sentence structure:

**S1 (Problem)**: Define architecture overfitting in dataset distillation: the distilled data, synthesized by a specific training network (e.g., 3-layer CNN), performs poorly when used to train test networks with different architectures.

**S2 (Gap)**: Existing methods either suffer from this problem or require large IPC budgets that cancel the advantages of distillation.

**S3 (Solution)**: We propose four complementary test-network training techniques — three-phase DropPath with improved shortcuts, reversed knowledge distillation, periodic LR/Lion optimizer, and k-fold augmentation — that together mitigate this gap.

**S4 (Key Result)**: On MTT CIFAR-10 IPC=10, our method improves ResNet50 from 28.1% to 63.8% (+35.7 points), nearly closing the architecture gap. Consistent gains are observed on CIFAR-100 and Tiny-ImageNet.

**S5 (Bounded Implication)**: The same approach improves deep network training on limited real data with ≥100 samples. These findings establish that architecture overfitting can be substantially mitigated by modifying the test network's training procedure without altering the distillation algorithm.

### Introduction Outline (Paragraph-by-Paragraph)

**P1 — Motivation and Problem Setup** (replace current literature-list style):
- Role: Establish stakes (large DNNs need big data), introduce dataset distillation as a solution, then immediately state its critical weakness.
- Key claim: Dataset distillation is valuable but suffers from architecture overfitting that limits practical use with larger networks.
- Evidence anchor: No results needed; conceptual framing.
- Transition: "In this work, we show that..."

**P2 — Architecture Overfitting Mechanism** (strengthen current P2):
- Role: Explain what architecture overfitting is and why it occurs (shallow training network embeds its inductive biases into distilled data).
- Key claim: The gap grows with architectural distance and is especially severe at small IPC.
- Evidence anchor: Reference to Table 2 baseline numbers (e.g., ResNet50 is 18.6% worse than 3-layer CNN on FRePo CIFAR-10 IPC=10).
- Transition: "To recover the advantage of deeper networks, we propose..."

**P3 — Proposed Approaches Overview** (similar to current P3):
- Role: Introduce the four methodological categories: DropPath variant, KD, optimization, augmentation.
- Key claim: These are complementary and can be combined.
- Evidence preview: Figure 1.
- Transition: "We summarize our contributions as follows."

**P4 — Contribution list** (revise from current):
- Role: State 3 contributions: (1) the combined approach, (2) the DropPath+KD synergy mechanism, (3) generalization to limited real data with identified teacher ceiling.
- Key claim: Each contribution should be a conceptual advancement, not an experiment plan.
- Transition to Section 2.

### Alternative Storyline Candidates

**Candidate A — Problem-First (Recommended)**:
Big Picture (data bottleneck) → Precise gap (architecture overfitting) → Why it matters (deeper networks are unusable) → Solution overview (four complementary techniques) → Evidence preview (Figure 1 + key numbers) → Contribution summary. This is the structure recommended above.

**Candidate B — Method-First**:
Start with the DropPath + KD synergy insight, then derive the problem it solves. This would be more distinctive but risks confusing readers who are not familiar with architecture overfitting in DD.

**Candidate C — Negative-Result Framing**:
Lead with the striking fact that ResNet50 (28.1%) performs worse than a 3-layer CNN (63.6%) on MTT CIFAR-10 IPC=10. Then ask: Why? What can we do? This creates immediate reader engagement.

**Comparison**: Candidate A is safest and most aligned with reviewer expectations. It passes all three alignment checks (Problem: yes — architecture overfitting is clearly stated; Variable: yes — key method components appear as named sections; Contribution-evidence: yes — contribution list maps to experimental results). Candidate C is more engaging but risks appearing too narrative-driven for a technical paper.

## Priority Revision Plan
### P0 — Publication-Critical (Must do before acceptance)

| ID | Action | Related Issue | Effort | Expected Impact |
|----|--------|--------------|--------|----------------|
| P0.1 | Add standard deviations (±std, 3 seeds) to Table 2 for all settings, or add a significance test table in the main text | Issue 1 (missing variance) | Low (data already exists in Table 8) | High — fixes reproducibility concern |
| P0.2 | Bound generality and efficiency claims in Abstract, Introduction, and Conclusion | Issue 2 (overclaim) | Low (text revision) | High — improves scientific defensibility |
| P0.3 | Add a limitations paragraph to Conclusion, remove unsupported "real-world" claim | Issue 5 (conclusion) | Low (text revision) | Medium — completes scientific closure |
| P0.4 | Add a qualitative comparison table with factorization-based cross-architecture methods, or provide a clear data-driven justification for exclusion | Issue 3 (exclusion) | Medium (literature review + table) | High — addresses the strongest novelty risk |

### P1 — High Priority (Strongly recommended)

| ID | Action | Related Issue | Effort | Expected Impact |
|----|--------|--------------|--------|----------------|
| P1.1 | Add DropPath diagnostic experiment (effective depth distribution vs architecture gap) | Issue 4 (causal mechanism) | Medium (one additional training run per setting) | Medium — strengthens the paper's mechanistic argument |
| P1.2 | Revise Eq. (2) to include softmax-with-temperature definition for KD | Suggestion from annotation | Low (text revision) | Low-Medium — improves reproducibility |

### P2 — Quality Improvement (Recommended)

| ID | Action | Related Issue | Effort | Expected Impact |
|----|--------|--------------|--------|----------------|
| P2.1 | Add cross-architecture variance metric (std across 4 test architectures) | DropPath+KD synergy claim (Page 7 annotation) | Low (computable from Table 2) | Medium — quantifies the "decreased performance difference" claim |
| P2.2 | Report training time/epoch for each method to support efficiency claim, or remove the claim | Issue 2 (overclaim) | Low (log existing runs) | Low-Medium — supports an existing claim |
| P2.3 | Revise contribution list to remove Contribution 2 (experiment plan) and add mechanism-level contribution (DropPath+KD synergy) | Contribution list (Page 2 annotation) | Low (text revision) | Medium — reframes novelty positioning |

### Execution Order

1. **Day 1**: P0.1 (add std to Table 2), P0.2 (bound claims), P0.3 (rewrite conclusion)
2. **Day 2**: P0.4 (factorization comparison table), P1.2 (KD equation revision)
3. **Day 3**: P1.1 (DropPath diagnostic), P2.1 (cross-architecture variance)
4. **Day 4**: P2.2 (efficiency numbers), P2.3 (contribution list reframing)

### ASCII Diagram — Revision Strategy Roadmap

```text
[Problem: incremental novelty perception]
  -> P0.4: Add factorization comparison table
  -> P2.3: Reframe contribution list with mechanism
  -> Expected: stronger novelty positioning

[Problem: missing variance → reliability concerns]
  -> P0.1: Add std to Table 2
  -> Expected: readers can assess statistical reliability

[Problem: overclaimed generality]
  -> P0.2: Bound all scope claims
  -> P0.3: Rewrite conclusion with limitations
  -> Expected: improved scientific defensibility

[Problem: DropPath mechanism unknown]
  -> P1.1: Diagnostic effective-depth experiment
  -> Expected: causal claim validated
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|---------------------------------------|---------|-------------|-----------------|-------------------|
| E1 | Evaluate architecture overfitting mitigation on CIFAR-10 | FRePo, MTT distillation; IPC=1,10,50; 4 test architectures (RN18, AlexNet, VGG11, RN50); 5-way ablation (Baseline, w/o DP&KD, w/o DP, w/o KD, Full) | Test accuracy (%) | Full method achieves biggest gains at IPC=10; e.g., MTT RN50 IPC=10: 28.1→63.8 (+35.7) | C1 (mitigation approach) | Single-run variance unreported; IPC=1 variance high |
| E2 | Evaluate on additional datasets | CIFAR-100, Tiny-ImageNet; same DD methods and architectures | Test accuracy (%) | Consistent gains across datasets | C1, C2 (generality) | Only small-scale image datasets; no ImageNet-1K |
| E3 | Real-data limited training | CIFAR-10 random fractions (0.002 to 1.0); RN18, RN50 vs 3-layer CNN | Test accuracy (%) | RN18/RN50 + DP+KD surpasses CNN at 100+ samples | C3 (real data) | Teacher capacity ceiling at 0.05 fraction; variance at low fractions |
| E4 | DropPath hyperparameter ablation | Vary p_min, p_final, period of decay (T) | Test accuracy (%) | p_min=0.5, T=500 gives best balance of performance and efficiency | Component effectiveness | No diagnostic on effective depth distribution |
| E5 | KD hyperparameter ablation | Vary α (0.1-0.9), τ (0.5-10) | Test accuracy (%) | Method robust in α∈[0.5,0.8], τ∈[1,10] | Component robustness | Limited to one setting (FRePo IPC=10 RN18) |
| E6 | Optimization/data augmentation ablation | Replace Lion→AdamW, periodic LR→cosine, 2-fold→1-fold | Test accuracy (%) | Each component contributes; Lion gives +2.9% | Component effectiveness | No interaction analysis between components |
| E7 | Lion vs AdamW Hessian analysis | Power iteration for top-20 eigenvalues; loss landscape visualization | Eigenvalues, loss landscape curvature | Lion finds flatter minima (smaller eigenvalues) | Component justification | Only 1 setting; flatter-minima claim is correlation, not causation |

### Research-Theme Gap Diagnosis

1. **Cross-architecture novelty positioning**: The paper does not quantitatively compare against the most relevant prior work in cross-architecture distillation (factorization methods). This is the most significant gap in research-value demonstration.

2. **Mechanistic understanding**: The paper attributes DropPath's effect to ensemble averaging of shallower subnetworks but provides no diagnostic verification. Without understanding the mechanism, the method becomes a bag of tricks rather than a principled approach.

3. **Scope limitations for practical impact**: All experiments use small-scale datasets (CIFAR-10/100 at 32×32, Tiny-ImageNet at 64×64). The paper cannot claim practical impact without evidence on larger-scale settings (e.g., ImageNet-1K subsets) or modern architectures (ViT, ConvNeXt).

4. **Teacher capacity ceiling**: The real-data experiments show saturation at 0.05 fraction due to the weak 3-layer CNN teacher. The paper mentions a stronger teacher can help (Appendix B.5) but does not explore how to select the optimal teacher capacity.

### Proposed Research Experiments

**P0 Experiment — Cross-Architecture Comparison with Factorization Methods**

| Field | Description |
|-------|-------------|
| Target Claim | C1 (mitigation) and novelty positioning |
| Hypothesis | The proposed approach achieves competitive cross-architecture accuracy at lower IPC than factorization methods |
| Minimal Design | Train proposed method + reproduce 1-2 factorization method results (e.g., Kim et al. 2022) on CIFAR-10 IPC=50 with RN18 as test network; compare cross-architecture accuracy and compute cost |
| Controls/Baselines | Same distilled data budget (IPC) when feasible; same test architectures |
| Metrics | Per-architecture test accuracy, cross-architecture variance, training time |
| Success Criterion | Proposed method matches or exceeds factorization method accuracy at same or lower IPC |
| Estimated Cost/Time | 2-3 GPU-days (reproducing factorization methods is the bottleneck) |
| Expected Paper-Quality Gain | High — directly addresses the strongest novelty risk |

**P0 Experiment — Variance-Controlled Significance Analysis**

| Field | Description |
|-------|-------------|
| Target Claim | All comparative claims |
| Hypothesis | Reported gains are statistically significant |
| Minimal Design | Run all Table 2 settings (subset: IPC=10, all architectures) with 5 seeds; report mean±std and paired t-test for Full vs Baseline |
| Controls/Baselines | Same random seeds across methods |
| Metrics | Mean±std, p-value |
| Success Criterion | p < 0.05 for Full vs Baseline at IPC=10 for all architectures |
| Estimated Cost/Time | 1-2 GPU-days (reuse existing checkpoints) |
| Expected Paper-Quality Gain | High — addresses the central reproducibility concern |

**P1 Experiment — DropPath Diagnostic (Effective Depth Analysis)**

| Field | Description |
|-------|-------------|
| Target Claim | DropPath causal mechanism (ensembles shallower subnetworks) |
| Hypothesis | As p_min decreases, the distribution of effective depths shifts closer to the 3-layer CNN's depth |
| Minimal Design | For p_min ∈ {0.2, 0.5, 0.8}, log the number of active layers at each training step; plot the distribution and correlate with final accuracy gap vs 3-layer CNN |
| Controls/Baselines | No DropPath (p=1 throughout) |
| Metrics | Effective depth histogram, accuracy gap |
| Success Criterion | Clear monotonic relationship: lower p_min → lower effective depth → smaller architecture gap |
| Estimated Cost/Time | 0.5 GPU-day (logging overhead only) |
| Expected Paper-Quality Gain | Medium — strengthens the paper's mechanistic argument |

**P2 Experiment — Teacher Capacity Cascade**

| Field | Description |
|-------|-------------|
| Target Claim | C3 (real-data generalization) and teacher ceiling |
| Hypothesis | Cascading to a larger teacher (RN18→RN50) continues to improve the student beyond the 0.05 saturation point |
| Minimal Design | Repeat Figure 3b (RN50 student) with RN18 teacher instead of 3-layer CNN at fractions 0.05 to 0.20 |
| Controls/Baselines | 3-layer CNN teacher, no teacher |
| Metrics | Test accuracy, gain over no-teacher baseline |
| Success Criterion | RN50+KD(RN18) continues to outperform RN50+KD(CNN) at fractions >0.05 |
| Estimated Cost/Time | 0.5 GPU-day |
| Expected Paper-Quality Gain | Medium — demonstrates practical utility and boundary-aware optimization |

### ASCII Diagram — Experiment Upgrade Plan

```text
P0 Priority (Before Resubmission)
├── P0.1: Add std/significance to Table 2 [1 GPU-day]
│   └── Expected: statistical reliability established
└── P0.2: Factorization method comparison [2-3 GPU-days]
    └── Expected: novelty positioning resolved

P1 Priority (Strengthen Core Claims)
├── P1.1: DropPath effective-depth diagnostic [0.5 GPU-day]
│   └── Expected: causal mechanism validated
└── P1.2: Teacher capacity cascade experiment [0.5 GPU-day]
    └── Expected: practical utility demonstrated

P2 Priority (Scope Extension)
└── P2.1: Larger-scale validation (e.g., ImageNet subset, ViT) [5+ GPU-days]
    └── Expected: generality claim expanded
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score**: 5.5 / 10

**Rationale**: The paper addresses a well-motivated problem with a clear empirical demonstration. The experiments are broad in coverage (3 datasets, 2 DD methods, 4 architectures, 3 IPC settings) and the ablation studies are thorough. However, the overall novelty is incremental — each component is an existing technique, and the main contribution is the specific composition. The paper's scientific rigor is weakened by the absence of variance reporting in the main results, overclaimed generality and efficiency statements, and the exclusion of the most directly relevant prior work (factorization-based cross-architecture methods) without rigorous comparison. The conclusion lacks a limitations section and introduces an unsupported claim. The paper has solid empirical grounding but needs substantial revision in novelty positioning, statistical rigor, and claim boundary setting to be publication-ready at a top venue.

**Post-Revision Target**: [6.5, 7.5] / 10

If the P0 and P1 revision items are addressed (variance reporting, claim bounding, factorization comparison table, limitations section, DropPath diagnostic), the paper's score would increase to the 6.5-7.5 range. This assumes the factorization comparison does not reveal substantial overlap — if it does, the score target should be lowered to [5.5, 6.5]. The paper would then be a solid borderline-to-accept paper with clear strengths in empirical breadth and practical relevance, despite incremental novelty.