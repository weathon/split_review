Now let me finalize the review and score.

## Summary

The paper proposes Medix, a framework for OOD detection that uses median-based gradient filtering to extract outlier candidates from unlabeled wild data. The method has two stages: (1) a greedy iterative algorithm that removes samples from wild data based on leave-one-out deviations from the element-wise median (EWM) of gradients, and (2) training a binary OOD detector on the identified outliers plus labeled InD data. The paper provides theoretical bounds on misclassification rates and reports strong empirical results across multiple benchmarks, outperforming 20 baselines.

## Strengths

1. **Novel median-centric filtering algorithm (Algorithm 1)** — The use of the element-wise median of gradients to identify outliers from unlabeled mixtures is a well-motivated and non-trivial methodological contribution. The algorithm's greedy leave-one-out procedure is clearly described and the motivation from Figure 1 (monotonic increase in EWM deviation as OOD samples are added) is empirically grounded.

2. **Provable two-sided error bounds (Theorems 4.1, 4.2)** — The paper derives upper bounds on both inlier misclassification and outlier misclassification rates, analyzing contamination, concentration, and separation effects. The symmetry between the two bounds (contamination term for InD vs. reverse contamination term for OOD) is a nice theoretical property. The paper also provides a looser version (Theorem C.3) that removes the sub-Gaussian assumption, showing robustness even under only bounded second moments.

3. **State-of-the-art empirical results (Tables 1, 2)** — Medix outperforms 20 baselines across 5 OOD datasets on both CIFAR-10 and CIFAR-100. The improvements are substantial: on CIFAR-100, average FPR95 of 5.42% vs. WOODS' 6.74%; on CIFAR-10, average FPR95 of 0.80% vs. WOODS' 3.40%. Improvements over the best InD-only methods (KNN+) are even larger (40.98% FPR95 reduction). Standard deviations are reported across 5 runs.

4. **Handles realistic dataset-level mixing** — The paper explicitly notes that prior work (e.g., WOODS, Du et al.) assumes batch-level mixing ratios, while Medix works without this requirement, which is more practical for real-world deployment.

5. **Empirical verification of key theoretical assumptions (Remark 4.3, Figure 4)** — The paper provides gradient histograms and Q-Q plots supporting the sub-Gaussian assumption, strengthening the credibility of the theoretical analysis.

## Weaknesses

### Major

1. **Theory-algorithm disconnect** — Theorems 4.1 and 4.2 analyze properties of EWM-based filtering under distributional assumptions on InD and OOD gradients. However, they provide no proof that the *greedy iterative procedure* (Algorithm 1, with its leave-one-out deviation criterion and k-at-a-time removal) converges to a subset that achieves these bounds. The theorems analyze a one-shot EWM filter, while the deployed algorithm is an iterative greedy method. The convergence criterion ($|\delta_{\max}| > \epsilon$) is described but never connected to the theoretical bounds. The paper states "the bounds analyze the EWM filtering rule" without specifying whether this rule corresponds to the algorithm's output. This disconnect means the theoretical guarantees do not directly apply to what is actually implemented.

2. **Undefined variables in Theorem 4.1** — The bound uses $m_{\text{in}}$ and $m_{\min}$ without definition in the main paper. $m = |\mathcal{S}_{\text{wild}}|$ and $\pi$ are defined, so $m_{\text{in}} = (1-\pi)m$ is a natural interpretation, and $m_{\min}$ likely refers to $\min(m_{\text{in}}, m_{\text{out}})$ or similar, but neither is stated. Since the theorem is presented in the main text (not just the appendix), readers need these definitions to interpret the bound.

3. **Wild-to-test distribution match in main experiments** — The primary evaluation uses the *same* OOD distribution for constructing the wild mixture and the test set (e.g., Places365 is both in the wild data and the test set). The paper describes this as evaluating in "open-world settings," which overstates the generality. The paper does include "complex unseen OOD" experiments in Appendix A.4 (where $\mathbb{P}_{\text{out}}^{\text{test}} \neq \mathbb{P}_{\text{out}}$), which partially addresses this, but the limitation is not acknowledged in the abstract, introduction, or conclusions. The headline claims of general OOD superiority are calibrated to a setting where test OOD matches wild OOD.

### Minor

1. **Missing critical ablation: filtered vs. unfiltered wild data** — The paper compares Medix against WOODS and OE, which use different training paradigms. It does not compare training the Medix detector on the *unfiltered* wild mixture vs. the *filtered* outliers using the same detector architecture and loss. This makes it impossible to isolate whether the filtering stage adds independent value beyond what the detector could learn from the raw mixture. Since filtering is the paper's primary contribution (C1), this ablation is essential.

2. **Trivial synthetic validation (Figure 2)** — The 2D synthetic example places OOD centers ~18 units from the nearest InD cluster center (≈36 standard deviations separation given variance 0.25 per coordinate). Claiming "only 12.5% error rate" as corroboration of theoretical guarantees is not meaningful — any reasonable method would achieve near-perfect separation at this distance. This experiment tests nothing about the algorithm's ability to handle realistic OOD scenarios.

3. **Hyperparameter selection may benefit from test distribution knowledge** — Hyperparameters $\epsilon$ and $k$ are selected from specific sets "with the objective of maximizing OOD performance." Since the same OOD distributions are used for both wild data construction and testing, and the wild data composition determines what "maximizing OOD performance" means, hyperparameter tuning may inadvertently benefit from knowledge of the test distribution. The paper should clarify whether a held-out validation set was used.

### Trivial

1. **Algorithm 1 initialization** — $d_t$ is initialized to 0 (line 1) but is checked in the while condition (line 2) before being computed (line 4) on the first iteration. The condition also checks $|\delta_{\max}| > \epsilon$, and $\delta_{\max}$ is initialized to $\infty$, so the first iteration proceeds. But the initial $d_t = 0$ is never used before being overwritten.

## Nice-to-Haves

- Study sensitivity of filtering quality to InD classifier accuracy (the reference gradient $\bar{\nabla}_{\text{in}}$ depends on classifier quality)
- Systematic study varying contamination proportion $\pi$ beyond 0.5 to test the theoretical prediction that contamination terms blow up near boundaries
- Computational cost analysis for large-scale wild datasets

## Removed Points

- Criticism about "dimensional inconsistency" in Theorem 4.2's $2\epsilon$ term: this is debatable and may be resolved in the appendix (which is stripped). The term is a rate, not a dimension — this is not clearly an error.
- Criticism that the contamination term provides a "weak guarantee" for large $\pi$: the bound is not tight but the paper openly states the condition $\pi < 0.5$. This is a limitation of the bound, not an error.
- Claim that Paper "does not show that filtering improves over raw wild data": kept as Minor weakness 1 above (missing ablation).
- Generic "reproducibility concerns" about undisclosed hyperparameters: most implementation details are provided.
- "No analysis of sensitivity to InD classifier quality" and "Phase mixing in pre-training": these are speculative concerns without clear evidence from the paper that they would qualitatively change results.
- Strengths that are generic/superficial: "addressed an important problem," "demonstrated effectiveness" — removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Connect the theoretical analysis to the actual algorithm** — Either prove bounds for the greedy leave-one-out procedure, or (failing that) clearly articulate which simplified version of the algorithm the theorems apply to and acknowledge the gap. Defining $m_{\text{in}}$ and $m_{\min}$ explicitly in the main text is a minimum requirement.

2. **Add the filtered vs. unfiltered ablation** — Train the Medix detector on the raw (unfiltered) wild mixture using the same detector architecture and loss, and compare to the filtered version. This would isolate the value of the filtering stage.

3. **Calibrate claims about "open-world" evaluation** — Acknowledge in the abstract and conclusions that the main experiments use the same OOD distribution for wild data and testing (matched setting), while the unseen-OOD experiments in Appendix A.4 provide initial evidence for generalization.

4. **Provide a more informative synthetic experiment** — Vary the separation distance systematically across a range (not just near-perfect separation) to demonstrate when filtering starts to fail, providing practical guidance and connecting to theoretical bounds.

## Score and Decision

### Calibration

**Round 1 bracket (3.5–7.5):**
- Low band (< 3.5): Anchors at 2.0–3.4; papers on OOD detection with unlabeled data that are clearly weaker (poor evaluation, weak methodology)
- Middle band (3.5–7.5): Anchors at 4.75–6.5
- High band (> 7.5): Anchors at 8.0; clearly stronger papers

**Round 2 narrowing:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| SAL (Du et al., 2024a) `jlEjB8MVGa` | 6.5 | R2 | Most directly comparable: same two-stage filtering for wild OOD detection with theory. Medix has better empirical results but weaker theory-algorithm connection. Medix is slightly weaker overall. |
| Gradient Norm `bcWwhF8cTZ` | 5.5 | R2 | Uses gradients for OOD; weaker novelty and empirical results than Medix. Medix is clearly stronger. |
| SPADE `kwCHcaeHrf` | 5.5 | R2 | Theory-driven OOD detection with good experimental validation. Medix has stronger empirical results and a more practical setting. Comparable quality. |
| Double Descent `eN0RyRVbSm` | 6.5 | R2 | Strong theoretical contribution but weaker practical relevance. Medix has stronger empirical grounding. |
| TOOD `Zww4Xqmk38` | 4.75 | R2 | Tree-based OOD detection; less related, weaker empirical results. Medix is stronger. |
| GROD `zUrdd5NRLH` | 5.0 | R2 | OOD with transformers; less related setting. Medix is comparable or stronger. |

**Final placement:** Medix sits between the 5.5 anchors (SPADE, Gradient Norm) and the 6.5 anchors (SAL, Double Descent). It is empirically stronger than all 5.5 anchors but has a theory-algorithm disconnect that SAL does not appear to share. The paper's contribution is real — the median-based filtering is novel and achieves strong results — but the theoretical claims (C2) are not fully supported as presented. Score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>