## Summary

This paper pioneers a data-centric task called Candidate Label Set Pruning (CLSP) for deep partial-label learning (PLL): rather than designing better disambiguation strategies *during* training, CLSP filters likely-false candidate labels from each example's candidate set *before* training. The proposed method scores each candidate label by how many of the instance's k-NN neighbors *lack* that label in their own candidate sets (a "down-voting" mechanism) and prunes the highest-scoring fraction. The paper provides theoretical upper bounds on pruning error, analyzes the role of representation quality, and reports extensive experiments: applying CLSP improves test accuracy in 145 out of 149 evaluations (≈97.3%) across 11 PLL methods, 4 datasets, and multiple candidate-generation settings.

## Strengths

- **Near-universal empirical improvement across diverse PLL methods.** The central claim — that CLSP improves existing PLL methods — is supported by a systematic comparison where 145/149 evaluations (≈97.3%) show higher test accuracy on pruned vs. original candidate sets (Section 4.2, line 174). The evaluation covers 11 methods spanning conventional, instance-dependent, and long-tailed PLL approaches, and datasets ranging from CIFAR to real-world PASCAL VOC. This is an unusually thorough empirical sweep for the subfield.

- **Theoretical upper bounds on pruning error.** Theorem 1 (Section 3.3) formalizes an upper bound on the probability of incorrectly pruning the true label under a $(k,\delta_k,\rho_k)$-label distinguishability assumption. Theorem 2 bounds the additional error when pruning more aggressively. These bounds connect representation quality and label ambiguity to a provable guarantee, which goes beyond purely heuristic filtering.

- **Training-free preprocessing is method-agnostic and practical.** The pruning step requires no gradient updates or per-method adaptation — it only needs a feature extractor (any off-the-shelf model) and k-NN search (Faiss). The paper demonstrates this versatility by applying the *same* pruned datasets across 11 different PLL methods and obtaining consistent improvements (Tables 1–3). This is a genuinely useful plug-in contribution.

## Weaknesses

### Major

- **Parameter selection analysis relies on ground-truth labels that are unavailable in PLL.** The paper's analysis for setting $k$ and $\tau$ (Section 4.2, line 188) explicitly computes $\delta_k$ and $\rho_k$ using formulas that require the true label $y_i$ and the set of false candidate labels $Y'_i = Y_i \setminus \{y_i\}$ — exactly the information a PLL practitioner does not have. The paper's suggestion that these quantities "can be estimated on the validation set" (line 106) does not resolve the issue, because a validation set in the PLL setting would also consist of instances with only candidate label sets and no ground truth. While the core pruning *method* operates without ground truth, the parameter analysis that guides selecting $k$ and $\tau$ depends on it. This creates a gap between the evaluation protocol and the practical deployment scenario: a user would need a workable protocol for setting these parameters without access to true labels. The paper does not provide one.

### Minor

- **No uncertainty quantification.** Across 149 experimental conditions, every result is reported as a single number with no standard deviations, confidence intervals, or significance tests. While this is common practice in large-scale PLL benchmarking, the paper describes the improvements as "significant" without statistical backing, and the reader cannot assess whether the improvements are stable across random seeds.

- **Strong independence assumption in the theoretical analysis.** The proof of Theorem 1 (line 93) assumes "the true label and false candidate labels of each PLL example appear in its k-NN examples' candidate label sets independently." This assumption is directly violated in instance-dependent (ID) and label-dependent (LD) candidate generation, where false labels are systematically correlated with features. The paper's own results show $\beta$-coverage drops to 0.08 on CIFAR-100 (ID) — consistent with this violation. The theory therefore provides bounds that may not hold in the most challenging settings, which the paper acknowledges but does not adequately discuss as a limitation.

- **"Training-free" framing is mildly overstated.** The pruning step itself involves no gradient-based training, which is technically correct. However, the method's strong performance depends critically on BLIP-2, a large vision-language model pre-trained on massive labeled and weakly-labeled corpora (ImageNet, image-text pairs). The paper's own results (Table 4) show substantially worse pruning quality with ResNet-based extractors. Calling the approach "training-free" without this important qualifier could mislead readers about what the method actually requires — specifically, access to high-quality pre-trained representations.

- **Explanation for 4/149 degraded cases is speculative.** The paper attributes the small number of degraded cases to overfitting in methods trained for 500–1000 epochs (ABLE, SoLar), but provides no evidence (e.g., running the same methods for fewer epochs on pruned data) to support this claim.

### Trivial

None.

## Nice-to-Haves

- **Random pruning baseline.** The paper compares "PLL on original data" vs. "PLL on pruned data," which conflates the effect of pruning *itself* with the effect of the neighbor-based *selection method*. A control that randomly prunes the same number of candidate labels per instance would cleanly isolate the value of the down-voting mechanism.
- **Computational cost reporting.** The total runtime for feature extraction, k-NN search (Faiss), and voting should be reported, so readers can assess whether the preprocessing overhead is justified relative to the PLL training time.

## Removed Points

These points were flagged for removal; treat them with caution.

- *Tables 1–3 embedded as images, cannot read numbers.* This is a PDF parser artifact; the original submission has readable tables.
- *Transductive accuracy results in Tables 7–9 and Figure 2 cannot be evaluated because the appendix is stripped.* This is a parser artifact — appendices exist in the original submission.
- *Criticism about missing related works.* The system cannot verify whether a reference is missing; this is removed per policy.
- *Reproducibility nitpicks about undisclosed hyperparameters or implementation details.* These are either present in the full submission or too granular to weigh in a review.
- *The claim that "misidentified labels could have profound negative impacts" is generic.* This is a standard motivation in the PLL literature, not a weakness of the paper's contribution.

## Novel Insights

The most interesting insight that emerges from reading the reviews together is that the paper's theoretical apparatus (Theorems 1–2) and its practical contribution are somewhat decoupled. The theory relies on an independence assumption known to be violated in challenging settings, and the paper admits the bounds are "too complicated to perform the mathematical quantitative analysis" — instead resorting to numerical simulation with ungrounded parameter values. Meanwhile, the method's empirical success (97.3% improvement rate) is robust and well-demonstrated. This suggests the paper's true contribution is primarily empirical and methodological rather than theoretical: the down-voting heuristic is simple, intuitive, and works. The formal theory adds mathematical framing but does not drive the experimental design or provide actionable guarantees that practitioners could use. An honest assessment would weigh the empirical contribution heavily and treat the theory as a nice formalization rather than a core proof of correctness.

## Suggestions

- Provide a practical, ground-truth-free protocol for setting $k$ and $\tau$ — for example, a heuristic based on the distribution of down-voting scores $O_{ij}$ across candidate labels, or a sensitivity analysis showing that default parameter choices (e.g., $k \in [5, 20]$, $\tau \in [0.3, 0.6]$) work robustly across settings without fine-tuning.
- Add a random pruning baseline to disentangle the effect of pruning *amount* from pruning *strategy*.
- Report multi-run statistics (mean ± std over 3–5 seeds) for a representative subset of experimental conditions to quantify result stability.
- Qualify the "training-free" label when describing the overall approach, noting that it relies on pre-trained representations.

## Score and Decision

**MY FINAL SCORE:** <score>6.5</score>
**MY FINAL DECISION:** <decision>Accept</decision>