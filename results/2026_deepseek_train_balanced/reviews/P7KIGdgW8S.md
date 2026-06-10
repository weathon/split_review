## Summary

This paper introduces a *Hölder stability in expectation* framework for analyzing the separation *quality* (not just binary separation) of parametric permutation-invariant functions and MPNNs. It proves that sum-based ReLU MPNNs have a lower-Hölder exponent that degrades linearly with depth, smooth-activation MPNNs degrade exponentially, and proposes SortMPNN — the first MPNN with provable bi-Lipschitz guarantees in expectation. The theoretical analysis is paired with adversarial ε-Tree examples where sum-based MPNNs fail completely while SortMPNN succeeds, plus experiments on TUDatasets, LRGB, and ZINC.

## Strengths

1. **Novel "Hölder in expectation" framework (Definition 1, Section 2.1):** The paper proposes a principled probabilistic relaxation of lower-Hölder stability that resolves a known tension: ReLU-sum networks are never injective for any fixed parameter (Amir et al. 2023) yet empirically separate well when wide. The framework explains this by showing they are lower-Hölder *in expectation* with α=3/2, even though no single parameter choice achieves separation.

2. **First characterization of depth-dependent deterioration of MPNN separation quality (Theorem 4):** Theorem 4 proves that ReluMPNN's lower-Hölder exponent degrades as 1+(K+1)/p and SmoothMPNN's as 2^{K+1} with depth K. The exponential degradation for smooth activations is a new quantitative finding — prior work had not analyzed how the exponent scales with MPNN depth.

3. **SortMPNN as the first MPNN with provable bi-Lipschitz guarantees (Theorem 5):** SortMPNN is shown to be lower Lipschitz in expectation (α=1) even with width 1, while also being uniformly upper Lipschitz. The paper explicitly contrasts this with prior work and the empirical results on five TUDatasets and ESAN-ZINC12K consistently place SortMPNN at or near the top.

4. **Quantitative adversarial examples connecting theory to practical failure (ε-Trees, Section 4, Table 1):** The ε-Tree construction provides graphs separable by 3 WL iterations that cannot be learned by any sum-based MPNN tested (GIN, GCN, GAT, ReluMPNN, SmoothMPNN all achieve exactly 0.5 accuracy), while SortMPNN and AdaptMPNN achieve 1.0. This goes beyond prior work which only proved that WL-separable graphs *can* be separated in principle.

5. **Empirical verification of predicted exponents on synthetic data (Figure 4, Section 5):** The plots of embedding distance vs. TMD for ε-Trees across varying ε show that ReluMPNN and SmoothMPNN exponents deteriorate with depth consistent with the predicted bounds, while SortMPNN's plot is linear — directly validating Theorem 4.

6. **Robustness advantage in low-parameter regimes (Figure 5, Section 5):** SortMPNN and AdaptMPNN outperform GCN on peptides-struct when the parameter budget drops to 1K, consistent with the width-1 lower-Lipschitz guarantee — a clean connection from theory to a practical advantage.

## Weaknesses

### Fatal
None.

### Major

1. **The connection between initialization analysis and trained models is a conjecture, not a result (line 101).** The Hölder in expectation definition is with respect to the *initialization* distribution. The paper states: "we conjecture that bad separation at initialization will be difficult to overcome during training." The ε-Tree experiments (Table 1) are consistent with this conjecture but do not constitute a proof or a general characterization. The paper presents no analysis of how training alters the Hölder exponents, nor any study isolating whether poor initialization separation is the causal mechanism for training failure. This matters because the paper's practical claims about preferring SortMPNN partly draw on this connection. To be clear, this is honestly presented as a conjecture, but the paper's narrative occasionally suggests a stronger link than is established (e.g., the ε-Tree experiments are described as "proof of the importance of separation quality analysis" at line 310, which conflates correlation with causation).

### Minor

2. **AdaptMPNN lacks theoretical guarantees despite being presented as a main contribution (line 266).** The paper states: "While we don't formally analyze the lower-Hölder properties of AdaptMPNN, we conjecture its worst-case behavior will be similar to ReluMPNN." This means one of the two proposed architectures has no proven guarantees. On ZINC/ESAN (Table 4), AdaptMPNN underperforms GIN in 5 of 8 subgraph-aggregation variants and is notably worse than SortMPNN, yet the paper does not discuss why. The paper is transparent about the gap, but it weakens AdaptMPNN as a contribution.

3. **Real-world empirical gains are modest and often within statistical noise.** On TUDatasets (Table 2), SortMPNN's improvements over GIN are within one standard deviation on all five datasets (e.g., Mutag: 90.99±6.2 vs. 89.4±5.6; Proteins: 76.46±3.68 vs. 76.2±2.8). On LRGB (Table 3), SortMPNN's AP on peptides-func (0.6940) barely exceeds GCN (0.6860), and on peptides-struct, GCN outperforms SortMPNN. On ZINC/ESAN (Table 4), SortMPNN outperforms GIN in 5/8 settings but underperforms in the DSS-GNN variants with EGO and EGO+ policies. The strongest evidence remains the ε-Tree synthetic data.

4. **AdaptMPNN's poor ZINC/ESAN results are not discussed.** While SortMPNN performs well in the ESAN experiments, AdaptMPNN underperforms GIN in most settings. Since AdaptMPNN is presented as a co-contribution alongside SortMPNN, this warrants analysis or at least acknowledgement.

### Trivial

- The augmented Wasserstein metric definition uses the notation W₁ but the proof and exponents reference W_p for general p≥1 (lines 122–130). This notation slight is consistent with the literature but could be confusing on first reading.
- Table 1 reports accuracy for the ε-Tree task without standard deviation across runs, though the 0.5 vs. 1.0 gap makes this inconsequential.

## Nice-to-Haves

- **Matching upper bound for smooth activations (Theorem 3):** Theorem 3 gives α ≥ n for smooth-sum multiset functions but provides no matching upper bound. The paper correctly flags this as future work (line 407), but a concrete construction achieving α = n would complete the analysis.
- **Tracking Hölder exponents during training** across epochs would substantially strengthen the claim that initialization separation predicts trainability.
- **Statistical significance tests** for the TUDataset results would clarify which improvements are meaningful.

## Removed Points

The following points from inputs were removed under the filtering rules:

- **Alleged definitional ambiguity (Critical Issue 1 from Harsh Critic):** The critic claimed a mismatch between Definition 1 and the ±ε proof. The definition reads: `c^p ≤ E_{w~μ} { d_Y / d_X^α }^p`, where `^p` is inside the expectation (applied to the fraction), i.e., `E[(d_Y/d_X^α)^p]`. The ±ε proof computes `E[|Δ|^p] / W_p^{αp} = E[(|Δ|/W_p^α)^p]`, which is exactly the left side of the definition. The notation is consistent. This is a misreading by the reviewer.
- **Missing experimental details / code link concerns:** Removed per hard rules — criticisms about reproducibility details and code hosting are excluded.
- **Variance on ε-Tree experiments:** Removed — 0.5 vs. 1.0 for binary classification makes variance irrelevant.
- **||x||<B assumption:** Removed — the paper explicitly addresses this with Adaptive ReLU.
- **No matching upper bound for smooth activations:** Moved to Nice-to-Haves; the paper acknowledges it as future work.
- **ε-Tree construction lacks pseudocode:** Removed — acceptable for a theory paper.

## Novel Insights

The most striking finding beyond the paper's own stated contributions is that the ε-Tree adversarial construction — where all sum-based MPNNs achieve exactly random-guess accuracy (0.5) while sorting-based MPNNs achieve 1.0 — is essentially independent of width. Standard accounts (Xu et al. 2018, Morris et al. 2019) emphasize that wider MPNNs are more expressive. The Hölder analysis reveals a complementary failure mode: even arbitrarily wide sum-based MPNNs can fail catastrophically on certain WL-separable pairs because their separation *quality* is poor, not because they lack separation *capability*. This suggests that the WL hierarchy, while necessary for separation, is insufficient to characterize learnability.

## Suggestions

1. Clarify the notation in Definition 1 by explicitly writing `E[ (d_Y(f(x;w), f(x';w)) / d_X(x,x')^α)^p ]` to preempt the ambiguity the reviewer encountered.
2. Acknowledge more prominently that the initialization-to-trainability link is conjectural, and consider adding an experiment that tracks the Hölder exponent during training.
3. Discuss AdaptMPNN's mixed ZINC/ESAN results and why it underperforms GIN in several settings despite strong ε-Tree performance.
4. Report whether the TUDataset improvements are statistically significant.

## Score and Decision

This is a strong theoretical paper with a novel framework, non-trivial proofs, and a compelling new architecture (SortMPNN) that follows naturally from the analysis. The weaknesses — the conjectural initialization-to-training link, the unproven AdaptMPNN, and modest real-world gains — are real but do not undermine the core theoretical contributions, which stand on their own. The theoretical results (linear vs. exponential degradation with depth, SortMPNN's Lipschitz guarantee, the ε-Tree lower bounds) are the paper's main value, and the honest treatment of limitations (the previous error in proof acknowledged at line 249, the AdaptMPNN gap, the future work items) is commendable.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>