## Summary
# Final Review Report

## Summary

This paper proposes a graph-based framework (SLW — Spectral Learning with Wild Data) for jointly addressing out-of-distribution (OOD) generalization and OOD detection. The key idea is to construct a graph over labeled ID data and unlabeled wild data (a mixture of ID, covariate-shifted OOD, and semantic-shifted OOD), define edge weights via supervised and self-supervised connectivity, and learn representations through a spectral contrastive loss whose minimizer is equivalent to the top-k eigenvectors of the normalized adjacency matrix. The authors provide closed-form theoretical analysis of linear probing error for OOD generalization and separability for OOD detection on a simplified 5-node toy example. Empirical results on CIFAR-10, ImageNet-100, and Office-Home show competitive performance against existing baselines including SCONE, with an average FPR95 reduction of 8.34% across five OOD datasets.

**Core strengths:** (1) A clean theoretical framing that connects graph spectral decomposition to a trainable contrastive loss; (2) joint treatment of OOD generalization and detection within a single objective, which prior work addressed separately; (3) extensive experiments across multiple datasets and settings.

**Core weaknesses:** (1) The theoretical guarantees are derived from a highly simplified 5-node toy model with discrete class/domain structure, not a general theory; (2) the two-stage training (SLW pre-train + CE fine-tune) confounds attribution of gains to the spectral loss; (3) the closed-form solution assumes neural networks can realize exact spectral eigenvectors — an unverified and likely unrealistic assumption; (4) the method requires 1000-epoch pre-training and per-dataset hyperparameter tuning, limiting practical applicability; (5) no limitations discussion in the conclusion.

## Strengths
**S1. Clean theoretical motivation for a practically relevant problem.** The paper addresses an important real-world challenge: models in deployment encounter both covariate shift (requiring generalization) and semantic shift (requiring detection). The graph-based spectral framing provides an elegant mathematical language for unifying these two objectives within a single optimization framework.

**S2. Equivalence between loss minimization and spectral decomposition.** Theorem 3.1 provides a clean theoretical connection: minimizing the SLW contrastive loss is equivalent to performing spectral decomposition on the normalized adjacency matrix. This is a non-trivial extension of prior spectral contrastive learning results (HaoChen et al. 2021) to the wild data setting with supervised connectivity.

**S3. Comprehensive empirical evaluation.** The experimental section is thorough, covering three complementary settings: CIFAR-10/CIFAR-10-C (main benchmark), ImageNet-100 (large-scale), and Office-Home (open-set domain adaptation). The ablation studies (impact of ID labels, impact of semantic OOD data domain) directly verify the theoretical predictions.

**S4. Competitive detection performance.** SLW achieves state-of-the-art OOD detection results on several benchmarks, particularly on SVHN (FPR95 0.13% vs SCONE's 10.86%) and LSUN-R (FPR95 0.06% vs SCONE's 0.87%). These are substantial improvements that demonstrate the practical value of the approach.

**S5. Strong theoretical motivation for representation geometry.** The theoretical framework predicts a specific representation structure: covariate-shifted OOD data embedded close to ID data, while semantic-shifted OOD data is separated. The t-SNE visualization (Figure 4) confirms this prediction, providing qualitative validation of the theory.

## Weaknesses
**W1. Theory-empirical gap: simplified toy model vs. real benchmarks.** The core theoretical results (Theorem 4.1, 4.2) are derived from a 5-node toy graph with a discrete class-domain structure (Eq. 9) and fixed coefficients (ηu=5, ηl=1). The real experiments use CIFAR-10, ImageNet-100, and Office-Home — none of which satisfy the discrete domain assumption. The paper does not quantify how well the toy theory transfers to these realistic settings or characterize when the 9/8 α > β condition would be satisfied in practice.

**W2. Confounded training pipeline.** The two-stage training (1000 epochs SLW pre-training + 20 epochs CE fine-tuning) makes it impossible to attribute OOD generalization improvements to the spectral loss versus the supervised fine-tuning. The ablation study (Table 5) controls for ID labels during pre-training but not for the CE fine-tuning stage. A direct comparison — SLW pre-train + CE fine-tune vs. random init + CE fine-tune — is missing.

**W3. Realizability assumption.** The closed-form solution Z = D^{-1/2} V_k sqrt(Σ_k) assumes the neural network can exactly represent the top-k eigenvectors of the normalized adjacency matrix. This is an unverified and likely false assumption for Wide ResNet-40 with limited capacity and implicit bias. The theoretical guarantees on E(f) and S(f) do not transfer to the practical setting unless this gap is addressed.

**W4. High computational cost.** The method requires 1000 epochs of pre-training with a batch size of 512, plus 20 epochs of fine-tuning. Training time is not reported, but this is substantially more expensive than post-hoc OOD detection methods and many OOD generalization methods. This limits practical applicability.

**W5. Per-dataset hyperparameter sensitivity.** The ηu, ηl coefficients require per-dataset selection (Table 7), with ηl varying from 0.01 (Office-Home) to 0.50 (CIFAR-10). The validation strategy uses only ID accuracy, which may not generalize to OOD performance (Table 8 shows that higher validation ID Acc does not always correspond to better OOD Acc or FPR).

**W6. Missing limitations section.** The conclusion does not discuss any limitations, failure cases, or boundary conditions, which is unusual for a paper making theoretical claims.

## Key Issues
### Issue 1 (Major): Confounded training pipeline obscures causal attribution

**Evidence.** Page 7 - Implementation details: The model is pre-trained with SLW loss for 1000 epochs, then fine-tuned with cross-entropy loss on labeled ID data for 20 epochs. The final evaluation is on the fine-tuned model.

**Impact.** Any OOD generalization improvement could be attributed to the CE fine-tuning rather than the spectral pre-training. The ablation (Table 5) only compares "with vs without ID labels during pre-training" but does not isolate the effect of pre-training itself. Without a "no pre-training + CE fine-tune" baseline, the paper's core causal claim is unsubstantiated.

**Fix.** Add ablation: (a) random init + CE fine-tune, (b) SLW frozen features + linear probe, (c) SLW pre-train + CE fine-tune (current). Report delta for each.

### Issue 2 (Major): Theoretical analysis rests on unrealistic toy model

**Evidence.** Page 5-6, Section 4.3: The entire closed-form derivation uses a 5-node graph with discrete ρ/α/β/γ augmentation probabilities. The assumption ρ ≫ max(α,β) is strong and domain labels d(x) must be known.

**Impact.** The theoretical guarantees (E(f)=0 condition, S(f) closed form) do not generalize to real benchmarks where domain boundaries are continuous and unknown. The paper leverages these results as "provable error quantification" (abstract) but the proof only covers a highly specific toy case.

**Fix.** Rename Section 4 as "Theoretical Analysis on an Illustrative Example" and clearly state that the general case is future work. Remove "provable" qualifiers from abstract.

### Issue 3 (Major): Realizability gap between theory and practice

**Evidence.** Page 5, Section 4.1: "the closed-form solution for the representations is equivalent to performing spectral decomposition of the adjacency matrix." This assumes the neural network can exactly represent the top-k eigenvectors.

**Impact.** Without verifying this assumption, the claimed alignment between theory and experiments (t-SNE in Figure 4) is merely qualitative. The network may learn a different representation that happens to produce similar geometry but for different reasons.

**Fix.** (a) Measure the approximation error ||Ã - F_k F_k^T||_F for the learned vs. ideal F_k. (b) Replace definitive language with "suggests" or "is consistent with."

### Issue 4 (Minor): Selective empirical reporting

**Evidence.** Page 7-8, Table 1: SLW's OOD Acc on Textures (81.40%) is lower than SCONE (85.56%), and on LSUN-R (Table 2, 79.38%) is similar to SCONE (80.31%). Yet the text claims "excels in both OOD detection and generalization performance."

**Impact.** Overclaiming harms objectivity and invites reviewer skepticism. The method has genuinely strong detection results but generalization is setting-dependent.

**Fix.** Add a balanced sentence: "SLW achieves strong overall performance, though on certain datasets (e.g., Textures) OOD generalization trails SCONE, suggesting a setting-dependent tradeoff."

## Actionable Suggestions
### Suggestion A: Add controlled ablation for training pipeline (Must)

Add experiments isolating the SLW pre-training effect:
- Baseline A: Random initialization → CE fine-tune (20 epochs) [no pre-training]
- Baseline B: SLW pre-train (1000 epochs) → linear probe on frozen features [no fine-tuning]
- Baseline C: SLW pre-train → CE fine-tune (current)
Report OOD-Acc, FPR95, ID-Acc for all three on the CIFAR-10 benchmark.

### Suggestion B: Qualify theoretical scope in abstract and introduction (Must)

Replace: "derive provable error quantifying OOD generalization and detection performance"
With: "derive closed-form expressions for OOD generalization and detection error on a simplified illustrative graph model, providing theoretical intuition for the proposed approach."

### Suggestion C: Add limitations paragraph to conclusion (Must)

Add a dedicated paragraph covering:
1. The toy-model scope of the theoretical analysis
2. The realizability assumption for neural network eigenvectors
3. The computational cost (1000 epochs)
4. The hyperparameter sensitivity (ηu, ηl per-dataset tuning)

### Suggestion D: Add realizability verification experiment (Nice-to-have)

Compute the normalized adjacency matrix Ã for the empirical graph (using training data statistics), then measure $||Ã - F_k F_k^T||_F$ where $F_k$ are the learned representations. Report whether this error decreases during training and how it correlates with OOD performance.

### Suggestion E: Balance empirical claims (Must)

Revise Page 7 claim "our method excels in both OOD detection and generalization performance" to acknowledge texture dataset where OOD Acc trails SCONE (81.40% vs 85.56%).

### Suggestion F: Discuss theory-empirical transfer (Nice-to-have)

Add a paragraph explaining how the discrete toy model (Eq. 9) relates to the continuous corruption setting of CIFAR-10-C. Is there an effective α and β that can be estimated from data? Does the 9/8 α > β condition have a testable prediction for when SLW will outperform SCONE?

### Suggestion G: Add efficiency reporting (Nice-to-have)

Report training time (GPU-hours) for the full pipeline and compare with the strongest baseline (SCONE). This helps readers assess practical tradeoffs.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction has three paragraphs:
- **P1:** Background on OOD generalization vs. detection as separate problems
- **P2:** Bai et al. (2023) wild data formulation and the gap (lack of formalized understanding)
- **P3:** Graph-based framework + spectral analysis as the proposed solution
- **P4:** Summary of contributions

**Strengths of current storyline:** The problem motivation (models face both covariate and semantic shifts) is clear and well-illustrated with Figure 1.

**Weaknesses:** The transition from P2 (gap: lacking formalized understanding) to P3 (propose graph-based framework) jumps too quickly. The reader does not understand *why* a graph-based spectral approach is the natural answer to the wild data problem. The connection between "heterogeneous mixture distribution" and "graph spectral decomposition" is not motivated.

### Recommended Storyline

**Abstract Outline (S1-S5):**
- **S1 (Problem):** "Models deployed in real-world settings must handle both covariate-shifted data (requiring correct classification despite domain change) and semantic-shifted data (requiring rejection of novel classes)."
- **S2 (Challenge):** "Prior work addresses these two challenges separately, and existing wild-data methods lack theoretical characterization of when and why joint learning succeeds."
- **S3 (Gap):** "A unified framework connecting representation learning objectives to both OOD generalization and detection performance is missing."
- **S4 (Method):** "We propose Spectral Learning with Wild Data (SLW), which constructs a graph over labeled and unlabeled data with supervised and self-supervised connectivity, and learns representations via a contrastive loss equivalent to spectral decomposition of the graph's normalized adjacency matrix."
- **S5 (Result):** "On a simplified generative model, our framework yields closed-form expressions for OOD generalization error and ID-OOD separability. Empirically, SLW achieves competitive performance, reducing FPR95 by 8.34% on average over prior state-of-the-art on five OOD datasets."

**Introduction Outline (P1-P5):**

**P1 (Big Picture — 5 sentences):** "Modern ML models deployed in real-world settings face distribution shifts. Two types are critical: covariate shift (input distribution changes, labels remain the same) requiring OOD generalization, and semantic shift (novel classes appear) requiring OOD detection. Current research addresses these separately. However, a reliable model must handle both simultaneously. This paper proposes a unified framework for joint OOD generalization and detection."

**P2 (Prior Work and Gap — 4 sentences):** "Bai et al. (2023) introduced wild data — a mixture of ID, covariate-shifted, and semantic-shifted unlabeled data — as a realistic training resource. While effective, their approach lacks theoretical characterization. In particular, no existing framework explains how the representation geometry should be structured to simultaneously keep covariate-shifted data close to ID clusters while pushing semantic-shifted data apart. This paper fills this gap."

**P3 (Key Insight — 4 sentences):** "Our key insight is that a graph perspective naturally unifies these objectives. By constructing a graph whose vertices are data points and edges encode both supervised (same-class) and self-supervised (same-image) similarity, the problem of learning good representations reduces to spectral decomposition of the graph's adjacency matrix. The top eigenvectors of this matrix are guaranteed to encode class structure while separating semantic outliers — exactly the geometry needed for joint OOD generalization and detection."

**P4 (Method Preview — 3 sentences):** "Building on this insight, we derive a spectral contrastive loss (SLW) whose minimization is equivalent to spectral decomposition. The loss can be optimized end-to-end with neural networks via stochastic gradient descent. This theoretical equivalence allows us to derive closed-form expressions for OOD generalization error and detection separability on a tractable model."

**P5 (Contributions — 4 bullet points):** List the three contributions as in the current paper, but with contribution 3 reframed to emphasize empirical validation of theoretical predictions rather than just "competitive results."

## Priority Revision Plan
### P0 (Critical — must fix before acceptance)

| Priority | Item | Evidence | Expected Impact |
|----------|------|----------|----------------|
| P0.1 | Add controlled ablation (random init + CE fine-tune, SLW frozen + linear probe) | Issue 1 | Establishes causal attribution of gains to SLW pre-training |
| P0.2 | Qualify theoretical scope in abstract and introduction | Issue 2 | Prevents overclaiming, improves scientific honesty |
| P0.3 | Add limitations paragraph to conclusion | Weakness W6 | Essential for a theoretical paper; missing this is a red flag for reviewers |
| P0.4 | Balance empirical claims (acknowledge texture dataset tradeoff) | Issue 4 | Improves objectivity and prevents selective reporting concerns |

### P1 (Major — should fix before final submission)

| Priority | Item | Evidence | Expected Impact |
|----------|------|----------|----------------|
| P1.1 | Discuss the realizability gap and add eigenvector approximation error measurement | Issue 3 | Strengthens theory-empirical connection |
| P1.2 | Add discussion of the sqrt(w_x) scaling factor's practical effect | Annotation 5 | Clarifies a subtle but important implementation detail |
| P1.3 | Add controlled ablation for the CE fine-tuning stage (compare SLW pre-train vs no pre-train) | Issue 1 | Completes the attribution analysis |
| P1.4 | Discuss the finite-sample approximation gap for expected edge weights | Annotation 4 | Improves methodological rigor |

### P2 (Nice-to-have — quality improvement)

| Priority | Item | Evidence | Expected Impact |
|----------|------|----------|----------------|
| P2.1 | Add numerical verification of eigenvector approximation stability in Appendix | Annotation 13 | Strengthens the theoretical derivation |
| P2.2 | Report training time (GPU-hours) | Suggestion G | Helps readers assess practicality |
| P2.3 | Strengthen the related-work differentiation (limit cases of prior work) | Annotation 12 | Clarifies novelty positioning |
| P2.4 | Rewrite introduction with stronger narrative flow (P3 insight paragraph) | Storyline section | Improves readability and motivation |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------|---------|-------------|-----------------|-------------------|
| Main (Table 1) | Compare SLW vs baselines on OOD generalization + detection | CIFAR-10 as Pin, CIFAR-10-C as Pcovariate_out, 5 semantic OOD datasets | OOD-Acc, ID-Acc, FPR95, AUROC | SLW achieves best avg FPR95; OOD-Acc competitive | C1, C3 | Fine-tuning confounds; no significance tests between runs |
| ImageNet-100 (Table 3) | Large-scale validation | ImageNet-100, ImageNet-100-C, iNaturalist | OOD-Acc, ID-Acc, FPR95, AUROC | SLW improves OOD-Acc (72.58% vs SCONE 65.34%) | C3 | Only 3 methods compared; no standard OOD detection baselines |
| Office-Home (Table 4) | Open-set domain adaptation | 4 domains, 12 transfer tasks | OOD-Acc, FPR95 | SLW achieves best avg FPR (12.0% vs Anna 23.3%) | C3 | OOD-Acc slightly below some baselines; tradeoff not discussed |
| ID Label Ablation (Table 5) | Impact of supervised connectivity during pre-training | CIFAR-10, 5 OOD datasets | OOD-Acc, ID-Acc, FPR95, AUROC | ID labels significantly improve both OOD generalization and detection | C2 | Both conditions still include CE fine-tuning |
| Semantic OOD Domain (Table 6) | Impact of same/different domain for semantic OOD | CIFAR-10, known/unknown class split | OOD-Acc | Same domain improves OOD generalization | Theorem B.1 | Small-scale (single experiment variation) |
| Hyperparameter Sensitivity (Table 8) | ηu, ηl sweep | CIFAR-10, Textures | ID-Acc (val), OOD-Acc, FPR, AUROC | Best ID-Acc on val does not always correspond to best OOD performance | — | Missing recommendation for hyperparameter selection |

### Research-Theme Gap Diagnosis

1. **Causal attribution gap.** The current experiments do not isolate whether SLW pre-training causes the OOD improvements. Adding random-init + CE fine-tune as a baseline would establish this.
2. **Theory-empirical bridge.** The closed-form predictions (E(f) condition, S(f) formula) are not quantitatively tested. The paper only provides qualitative t-SNE visualization. A quantitative test would be to create a synthetic dataset matching the toy model assumptions and verify the predicted thresholds.
3. **Robustness characterization.** The method is evaluated on clean benchmarks but not stress-tested with different mixture ratios (πc, πs) or different augmentation strengths. The theory predicts that the 9/8 α > β condition determines success — this could be tested by varying augmentation policies.
4. **Ablation of individual loss terms.** The SLW loss has 5 components (L1-L5). No experiment ablates individual terms to verify each component's contribution.

### Proposed Research Experiments

| Priority | Experiment | Target Claim | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Expected Gain |
|----------|-----------|-------------|----------------|-------------------|---------|-------------------|---------------|
| P0 | Controlled ablation of pre-training | C1: SLW framework improves OOD | (a) random init + CE, (b) SLW frozen + linear probe, (c) SLW + CE | Same architecture, optimizer, epochs | OOD-Acc, FPR95 | SLW pre-train improves over random init by >3% OOD-Acc | Establishes causal link |
| P1 | Synthetic-data verification of theory | C2: Closed-form predictions | Generate 5-class data matching Eq. 9; measure E(f), S(f) vs α,β,ρ | Theoretical predictions vs empirical | E(f) error, S(f) value | Empirical E(f) matches predicted threshold within 10% | Validates theoretical bridge |
| P1 | Loss component ablation | C1: Each L_i contributes | Remove one L_i term at a time, measure performance | Full SLW loss | OOD-Acc, FPR95 | Each removed term causes measurable degradation | Understands mechanism |
| P2 | Mixture ratio sensitivity | C3: Robustness to wild composition | Vary πc ∈ {0.1, 0.3, 0.5, 0.7}, πs ∈ {0.05, 0.1, 0.2} | Fixed πc=0.5, πs=0.1 | OOD-Acc, FPR95 | Performance stable across ratios (std < 5%) | Establishes practical robustness |
| P2 | Augmentation strength variation | Theo: α/β ratio prediction | Vary augmentation strength (weak/medium/strong) | Standard augmentation | OOD-Acc, E(f) | Stronger class-preserving aug (higher α) improves OOD generalization | Tests theoretical 9/8 α > β condition |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

**Rationale:** The paper presents a clean theoretical framework and strong empirical detection results, which are valuable contributions. However, the theoretical guarantees are derived from a highly simplified toy model rather than general settings, and the training pipeline confounds causal attribution of gains to the spectral loss. The computational cost (1000-epoch pre-training) and per-dataset hyperparameter tuning also limit practical impact. The score prioritizes research value (motivating a unified spectral view of OOD generalization and detection) and novelty (extending spectral contrastive learning to heterogeneous wild data mixtures) as primary dimensions, while reflecting concerns about validity (confounded pipeline) and reproducibility (unverifiable realizability assumption).

**Post-Revision Target: [7.0, 8.0]/10**

If the authors address the P0 items (controlled ablation, qualified theoretical scope, limitations paragraph, balanced empirical claims) and at least the P1.1 item (realizability gap discussion), the paper would present a more defensible and scientifically honest contribution. The upper bound of 8.0 reflects the inherent limitation that the theoretical analysis relies on a toy model — this is a structural constraint that cannot be fully removed without a fundamentally different theoretical contribution.

---

### ASCII Diagram — Paper Structure & Evidence Map

```text
[Problem: Joint OOD Gen + Det]
       |
       v
[Wild Data Setup (Bai et al. 2023)]
  Pin, Pcovariate_out, Psemantic_out mixture
       |
       v
[Graph Construction (Sec 3.1)]
  Vertices = data, Edges = w = ηu·w(u) + ηl·w(l)
       |
       v
[Spectral Loss L_SLW (Sec 3.2)]
  L = -2ηuL1 - 2ηlL2 + ηu²L3 + 2ηuηlL4 + ηl²L5
       |
       v
[Equivalence: min L_SLW = top-k SVD(Ã)] (Theorem 3.1)
       |
       v
[Closed-Form Repr: Z = D^{-1/2} V_k sqrt(Σ_k)]
       |
       +-------→ [E(f): Linear probing error on covariate OOD] (Theorem 4.1)
       |              └── Condition: 9/8·α > β → E(f)=0
       |
       +-------→ [S(f): ID vs semantic OOD separability] (Theorem 4.2)
       |              └── Closed-form in α', β'
       |
       v
[Empirical Validation (Sec 5)]
  CIFAR-10, ImageNet-100, Office-Home
       |
       v
[GAP: Confounded by CE fine-tuning stage]
       |
       v
[GAP: Toy model assumptions ≠ real benchmarks]
```

### ASCII Diagram — Revision Strategy Roadmap

```text
[Current Issues]
    |
    +-- P0.1: Confounded pipeline → Add controlled ablation
    |       └── Expected: Clear attribution of SLW gains
    |
    +-- P0.2: Overclaimed theoretical scope → Qualify abstract/intro
    |       └── Expected: Reviewer trust restored
    |
    +-- P0.3: No limitations in conclusion → Add limitations paragraph
    |       └── Expected: Scientific completeness
    |
    +-- P0.4: Selective empirical claims → Balance wording
    |       └── Expected: Objectivity improved
    |
    +-- P1.1: Realizability gap → Discuss + measure approx error
    |       └── Expected: Theory-empirical bridge strengthened
    |
    v
[After Revision: Stronger, more defensible paper]
```

### ASCII Diagram — Related-Work Taxonomy Tree (Layered)

```text
Related Work Taxonomy (Root: Joint OOD Gen + Det)
│
├── Branch 1: OOD Detection Methods
│   ├── Leaf 1.1: Post-hoc (confidence/energy/distance/gradient)
│   │   └── MSP, ODIN, Energy, Mahalanobis, KNN, ASH
│   └── Leaf 1.2: Regularization-based (requires auxiliary OOD data)
│       └── OE, Outlier Exposure variants
│
├── Branch 2: OOD Generalization / Domain Generalization
│   ├── Leaf 2.1: Invariant representation learning
│   │   └── IRM, VREx, GroupDRO
│   ├── Leaf 2.2: Robust optimization
│   │   └── SharpDRO, EQRM, Mixup
│   └── Leaf 2.3: Meta-learning / Augmentation
│       └── MetaReg, MixStyle
│
├── Branch 3: Wild-Data Methods
│   ├── Leaf 3.1: Wild data for OOD detection only
│   │   └── Woods (Katz-Samuels et al. 2022)
│   └── Leaf 3.2: Wild data for joint OOD Gen + Det
│       └── SCONE (Bai et al. 2023)
│       └── SLW (THIS PAPER) — graph-based spectral approach
│
├── Branch 4: Spectral Contrastive Learning
│   ├── Leaf 4.1: Unsupervised (homogeneous unlabeled data)
│   │   └── HaoChen et al. 2021 (SSL)
│   ├── Leaf 4.2: Domain adaptation (covariate-shifted unlabeled)
│   │   └── Shen et al. 2022 (UDA)
│   └── Leaf 4.3: Novel category discovery (semantic-shifted unlabeled)
│       └── Sun et al. 2023 (NCD)
│       └── [THIS PAPER]: Heterogeneous mixture unlabeled data
│
└── This Paper's Position:
    Extends spectral contrastive learning (Branch 4) to the wild-data
    setting (Branch 3), creating the first unified spectral framework
    for joint OOD generalization and detection.
```

### ASCII Diagram — Experiment Upgrade Plan

```text
[Stage 1: Immediate — Fix confounds]
   ┌─────────────────────────────────────────────┐
   │ Add: random init + CE fine-tune (no pre-train) │
   │ Add: SLW frozen + linear probe (no fine-tune) │
   └─────────────────────────────────────────────┘
                        ↓
[Stage 2: This revision — Bridge theory-empirical gap]
   ┌─────────────────────────────────────────────┐
   │ Add: Synthetic data experiment (verify E(f), S(f)) │
   │ Add: Eigenvector approximation error metric      │
   │ Add: Loss component ablation (L1-L5 individually) │
   └─────────────────────────────────────────────┘
                        ↓
[Stage 3: Future work — Robustness characterization]
   ┌─────────────────────────────────────────────┐
   │ Vary: πc, πs mixture ratios                    │
   │ Vary: Augmentation strength (test 9/8 α > β)   │
   │ Add: Training time / GPU-hour reporting        │
   └─────────────────────────────────────────────┘
```

---

### Contribution Novelty Verdict Board

| Claim ID | Author Claim | Verdict | Why | Confidence |
|----------|-------------|---------|-----|------------|
| C1 | Novel graph-based framework for joint OOD generalization and detection via spectral decomposition | Partially overlapping | Prior spectral contrastive works (HaoChen 2021, Shen 2022, Sun 2023) use similar graph-adjacency spectral framing for related but simpler settings. The novelty is in extending to heterogeneous wild data mixtures with supervised connectivity. | Medium |
| C2 | Theoretical insight via closed-form solutions for OOD generalization and detection error | Unclear | Derivation is on a 5-node toy model with strong assumptions (discrete ρ/α/β/γ, known domain labels, ηu=5, ηl=1). General closed-form results are not provided. | Low |
| C3 | Empirical validation showing competitive performance and alignment with theoretical analysis | Partially overlapping | Strong detection results validated, but causal attribution to spectral loss is confounded by CE fine-tuning stage. Qualitative t-SNE alignment is shown but not quantitatively verified. | Medium |

**Contribution-level Novelty Conclusion:** The paper's primary novelty (C1) is incrementally extending spectral contrastive learning to a more complex data setting (heterogeneous wild mixtures) and adding supervised connectivity. This is a valid extension but builds directly on established methodology. The theoretical claims (C2) are overstated relative to their scope. The empirical contribution (C3) is genuine but needs deconfounding.

**Note:** External literature verification was unavailable in this run (Retrieval-Disabled Mode). Novelty verdicts are based on manuscript-internal evidence only and should be verified by manual literature review.