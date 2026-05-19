## Summary
This paper proposes a graph-based framework for jointly addressing out-of-distribution (OOD) generalization and detection using heterogeneous wild data. The authors introduce Spectral Learning with Wild Data (SLW), a spectral contrastive loss derived from the factorization of a graph adjacency matrix that combines supervised and self-supervised connectivity signals. Theoretically, the paper establishes an equivalence between minimizing the SLW loss and performing spectral decomposition on the data graph, yielding closed-form error bounds for OOD generalization and separability metrics for OOD detection. Empirically, SLW demonstrates competitive performance against strong baselines, including the state-of-the-art SCONE method, across multiple benchmarks (CIFAR-10, ImageNet-100, Office-Home). The work provides a unified perspective on OOD learning, bridging spectral graph theory with modern contrastive representation learning.

## Strengths
1. **Unified Theoretical Framework:** The paper successfully bridges OOD generalization and detection under a single graph-based spectral framework, providing a novel perspective on how heterogeneous wild data can be leveraged jointly.
2. **Rigorous Theoretical Analysis:** The derivation of closed-form solutions for linear probing error and separability metrics based on graph eigenvectors is mathematically sound and offers clear insights into the conditions for perfect generalization ($9/8 \alpha > \beta$).
3. **Strong Empirical Performance:** SLW demonstrates competitive results across multiple datasets (CIFAR-10, ImageNet-100, Office-Home), effectively balancing the trade-off between OOD accuracy and FPR compared to strong baselines like SCONE.
4. **Clear Problem Formulation:** The introduction clearly defines the wild data mixture distribution and motivates the need for a framework that handles both covariate and semantic shifts simultaneously.

## Weaknesses
1. **Limited Theoretical Generalization Conditions:** The theoretical analysis relies on a highly simplified 5-node toy example with specific augmentation probability assumptions ($\rho \gg \max(\alpha, \beta) \ge \min(\alpha, \beta) \gg \gamma \ge 0$). While illustrative, it is unclear how these closed-form bounds extend to complex, high-dimensional real-world datasets where augmentation connectivity is not easily parameterized.
2. **Lack of Causal Ablation for Graph Components:** The empirical gains are attributed to the combination of supervised and self-supervised graph connectivities. However, the paper lacks a matched-capacity ablation study isolating the contribution of the spectral decomposition versus standard contrastive learning, making it difficult to causally attribute performance improvements to the graph-based mechanism.
3. **Computational Scalability Concerns:** Constructing and factorizing the adjacency matrix for large-scale datasets (e.g., ImageNet) is computationally expensive. The paper does not discuss approximation techniques or scalability limits, which may hinder practical deployment in large-scale settings.
4. **Overclaiming SOTA Performance:** The introduction and abstract claim "significant reduction in FPR95" and "competitive performance" without explicitly bounding these claims to the specific evaluated settings and mixture ratios ($\pi_c=0.5, \pi_s=0.1$), potentially overstating generalization to other wild data regimes.

## Key Issues
1. **Theoretical-to-Empirical Gap:** The closed-form error bounds derived in Section 4 rely on a highly constrained 5-node graph with explicit augmentation probabilities. The manuscript does not provide a clear bridge explaining how these theoretical conditions map to the high-dimensional neural network representations learned in practice, limiting the practical utility of the theoretical guarantees.
2. **Missing Matched-Control Ablation:** Without a matched-capacity baseline that uses standard contrastive learning without spectral graph factorization, it remains unclear whether the performance gains stem from the novel graph-based spectral mechanism or simply from the specific combination of supervised and self-supervised positive/negative pair sampling.
3. **Scalability and Implementation Opacity:** The adjacency matrix construction and factorization are $O(N^2)$ in complexity. The paper lacks discussion on how SLW scales to large datasets (e.g., ImageNet-1K) and omits critical implementation details regarding graph sparsification or approximate spectral decomposition, raising reproducibility concerns for large-scale applications.

## Actionable Suggestions
1. **Add Matched-Control Ablation:** Introduce a baseline that uses the same supervised/self-supervised pair sampling but optimizes a standard contrastive loss (e.g., InfoNCE) without spectral graph factorization. Report the performance delta to causally isolate the contribution of the spectral mechanism.
2. **Clarify Theoretical-to-Empirical Bridge:** Add a discussion paragraph explaining how the theoretical condition $9/8 \alpha > \beta$ translates to practical hyperparameter tuning ($\eta_u, \eta_l$) and augmentation choices. Provide empirical validation showing how varying $\eta_u/\eta_l$ affects the balance between OOD accuracy and FPR.
3. **Address Scalability:** Discuss computational complexity and propose or evaluate graph sparsification techniques (e.g., k-NN graph construction) to make SLW feasible for large-scale datasets. Include a complexity analysis in the appendix.
4. **Bound Empirical Claims:** Revise the abstract and introduction to explicitly bound performance claims to the evaluated settings and mixture ratios. Replace "state-of-the-art" with "competitive performance under reported settings" to maintain scientific objectivity.

## Storyline Options + Writing Outlines
### Abstract Outline (S1-S5)
- **S1 (Problem & Domain):** Models deployed in real-world scenarios encounter heterogeneous data shifts, challenging both OOD generalization (covariate shifts) and detection (semantic shifts).
- **S2 (Significance/Challenge):** While critical for robustness, these tasks are often addressed separately or under simplifying assumptions of homogeneous unlabeled data, leaving a gap in leveraging naturally arising wild data.
- **S3 (Prior Gap):** Existing methods struggle to balance the trade-off between preserving semantic structure for detection and maintaining domain invariance for generalization.
- **S4 (Proposed Method):** We formalize a graph-based framework and introduce Spectral Learning with Wild Data (SLW), showing equivalence between minimizing our objective and spectral decomposition on the data graph.
- **S5 (Key Result & Implication):** This yields closed-form error bounds quantifying OOD performance. Empirically, SLW achieves competitive results, reducing FPR95 by an average of 8.34% compared to SCONE across five datasets.

### Introduction Outline (P1-P4)
- **P1 (Big Picture & Problem):** Define closed-world limitations and introduce OOD generalization vs. detection using concrete examples (seabirds vs. deer). Highlight that robust models must excel in both, but current research addresses them in isolation.
- **P2 (Gap & Wild Data):** Introduce Bai et al. (2023) wild data mixture $P_{wild}$. Emphasize the challenge of heterogeneity and the lack of formalized understanding of how this mixture impacts joint OOD tasks, motivating a unified framework.
- **P3 (Solution & Graph Intuition):** Propose the graph-based framework where vertices are data points and edges combine supervised/self-supervised signals. Explain how this dual-signal construction naturally aligns covariate OOD with ID while separating semantic OOD.
- **P4 (Evidence & Contributions):** Preview the spectral contrastive loss, theoretical equivalence to graph factorization, and empirical gains. Summarize contributions: (1) unified graph framework, (2) closed-form theoretical insights, (3) competitive empirical validation.

## Priority Revision Plan
**P0 (Critical - Validity & Causal Attribution):**
- Add matched-control ablation: Compare SLW against a standard contrastive baseline using identical supervised/self-supervised pair sampling but without spectral graph factorization. This isolates the contribution of the spectral mechanism.
- Clarify theoretical-to-empirical bridge: Add a discussion linking the theoretical condition $9/8 \alpha > \beta$ to practical hyperparameter tuning ($\eta_u, \eta_l$) and provide empirical validation of this trade-off.

**P1 (Major - Reproducibility & Scalability):**
- Address computational complexity: Discuss $O(N^2)$ graph construction costs and propose/evaluate sparsification techniques (e.g., k-NN graphs) for large-scale datasets. Include complexity analysis in the appendix.
- Bound empirical claims: Revise abstract/introduction to explicitly bound performance claims to evaluated settings and mixture ratios, replacing "state-of-the-art" with "competitive performance under reported settings".

**P2 (Minor - Writing & Clarity):**
- Tighten abstract structure: Restructure into compact 4-5 sentence logic (Problem -> Gap -> Method -> Theory -> Empirical Outcome).
- Enhance conclusion: Add brief acknowledgment of limitations (e.g., augmentation assumptions) and future directions (adaptive graph construction).

## Experiment Inventory & Research Experiment Plan
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | SLW vs. OOD detection/generalization baselines | CIFAR-10, CIFAR-10-C, SVHN/LSUN/Textures | OOD Acc, ID Acc, FPR, AUROC | SLW outperforms SCONE in FPR, competitive in Acc | C3 (Empirical) | Limited to specific mixture ratios |
| E2 | Large-scale validation | ImageNet-100, ImageNet-100-C, iNaturalist | OOD Acc, ID Acc, FPR, AUROC | SLW balances detection/generalization better than Woods/SCONE | C3 | ResNet-34 backbone only |
| E3 | Open-set domain adaptation | Office-Home (4 domains) | OOD Acc, FPR | SLW outperforms Anna in FPR by 11.3% | C3 | Special case of wild data |
| E4 | Impact of ID labels | CIFAR-10 with/without labels | OOD Acc, FPR | Labels significantly improve both tasks | C2 (Theory) | Ablation only, no causal isolation |
| E5 | Impact of semantic OOD domain | CIFAR-10 same/diff domain | OOD Acc | Same domain improves generalization | C2 | Theoretical verification only |

### Proposed Research Experiments
1. **Matched-Control Contrastive Baseline (P0):**
   - *Target Claim:* Spectral graph factorization drives gains.
   - *Design:* Standard InfoNCE loss with identical supervised/self-supervised pair sampling.
   - *Metrics:* OOD Acc, FPR delta vs. SLW.
   - *Success Criterion:* SLW shows statistically significant improvement over matched baseline.
2. **Hyperparameter Sensitivity & Trade-off Analysis (P1):**
   - *Target Claim:* $\eta_u/\eta_l$ controls generalization/detection balance.
   - *Design:* Sweep $\eta_u \in [0.5, 5.0], \eta_l \in [0.01, 1.0]$ on CIFAR-10.
   - *Metrics:* Pareto frontier of OOD Acc vs. FPR.
   - *Success Criterion:* Clear trade-off curve aligning with theoretical $9/8 \alpha > \beta$ intuition.
3. **Scalability & Sparsification Study (P1):**
   - *Target Claim:* SLW is feasible for large datasets.
   - *Design:* Apply k-NN graph sparsification ($k=10, 50, 100$) on ImageNet-100.
   - *Metrics:* Training time, memory usage, performance drop.
   - *Success Criterion:* <10% performance drop with $k=50$, feasible training time.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper presents a theoretically grounded and empirically competitive framework for joint OOD generalization and detection. The unified graph-based perspective and closed-form error bounds are significant contributions. However, the score is moderated by the limited generalizability of the theoretical analysis (reliance on a simplified 5-node toy example), the lack of matched-control ablations to causally isolate the spectral mechanism's contribution, and scalability concerns for large-scale datasets. Addressing these issues would substantially strengthen the paper's validity and impact.

**Post-Revision Target:** [7.5, 8.5]/10

**Path to Target:** Adding a matched-control contrastive baseline, clarifying the theoretical-to-empirical bridge, and discussing graph sparsification for scalability would resolve the core validity and reproducibility concerns, elevating the paper to a strong acceptance candidate.