Now I have a thorough understanding of the paper. Let me produce the consolidated review.

---

## Summary

The paper proposes **Duet**, a certified robust training method that uses a pre-trained vanilla model as a "guide" to preserve clean accuracy. It performs SVD on the vanilla model's weight matrices, extracts rotation matrices ($U$, $V^T$), and enforces a similarity loss ($L_{sim}$) between these and the certification model's rotation matrices during certified robust training. A low-rank approximation is used for efficiency. Experiments on CIFAR-10 with a 6Conv+2FC architecture claim a 3.76% clean accuracy improvement over global-Lipschitz regularization, with only a 0.93% certified accuracy decrease.

## Strengths

- **Quantified clean-accuracy improvement with controlled certified-accuracy cost**: The paper reports concrete numbers — a 3.76% improvement in clean accuracy (vs. global-Lipschitz regularization) with a 0.93% decrease in certified accuracy (Abstract and Section 1). This provides a direct, testable claim that the method delivers on its core promise.

- **Explicit mechanism via rotation-matrix similarity loss**: The paper defines a dedicated loss term $L_{sim}$ (Section 4.4, Eq. 10) that enforces alignment between the SVD rotation matrices of the vanilla guide model and the certification model. Experiments then show a measured increase in rotation-matrix similarity from 77.8% (standard certified training) to 95.6% (Duet) — linking the proposed mechanism to the observed outcome.

- **Low-rank approximation to reduce computational overhead**: The method uses rank-constrained approximations of the rotation matrices (Section 4.3), selecting only dominant orthogonal unit vectors. This is a practical engineering choice that controls the cost of the additional SVD-based computations.

## Weaknesses

### Fatal

None. The paper's core idea is coherent and the method is described, albeit incompletely. The weaknesses below are major but reparable.

### Major

- **Critically thin experimental evaluation**: The paper reports results on only **one dataset** (CIFAR-10), **one architecture** (6Conv+2FC), and **one perturbation radius** (36/255 $l_2$). No results are given in a **table** — the only quantitative claims are the two numbers (3.76%, 0.93%) in the abstract, with no absolute clean or certified accuracy values for Duet or either baseline. The paper explicitly promises comparisons "in terms of model accuracy, computation time, and memory consumption" (Section 5, line 165), but no computation time or memory numbers are presented anywhere. There are **no ablation studies** on the rank parameter $r$, the weight of $L_{sim}$, or any component variants. This level of evidence is insufficient to substantiate a new method.

- **Key similarity metric left undefined**: The paper reports that rotation-matrix similarity rose from 77.8% to 95.6% (Section 5, "Rotation matrix similarity") but **never defines the similarity metric**. The reader cannot tell whether this is cosine similarity, Frobenius-norm-based alignment, angular distance, or something else — so these numbers are uninterpretable and cannot be independently verified or reproduced.

- **No variance or statistical significance reported**: No standard deviations, no multiple random seeds, no indication of how many runs were performed. Single-run results on a small-scale setup do not establish reliability.

- **Loss function presented without justification or derivation**: The $L_{sim}$ formula (Section 4.4) uses the scaling factors $\frac{\|\sigma_{cer}\|}{\|\sigma_{van}\|}$ and its reciprocal, which appear ad hoc. The paper does not explain why this particular form is correct, why the ratios are necessary, or what geometric interpretation underpins them. This makes the method harder to motivate or extend.

### Minor

- **Section 4.2 analysis is hand-wavy**: The explanation of why certified robust training reduces clean accuracy ("the certification model finds it difficult to rotate the values in a vector to the appropriate positions for varying scales") is informal and lacks formal grounding. While the intuition (that Lipschitz regularization forces singular values to be similar, limiting rotation flexibility) is directionally plausible, it is not supported by any analysis, empirical evidence, or reference.

- **Narrow baseline set**: The paper only compares against global Lipschitz regularization (BCP-type) and local Lipschitz bounds. Several relevant methods (e.g., approaches using different activation functions, weight normalization, or pre-training to improve clean accuracy in certified models) are not discussed or compared.

### Trivial

- Inconsistent capitalization ("certification model" vs. "Certification model"), some odd word spacing caused by PDF extraction artifacts (noted but not held against the paper).
- The SVD definition equation (Section 2) has a formatting mismatch with the surrounding text.

## Nice-to-Haves

- An ablation study on the rank $r$ used for low-rank approximation, and on the weight of $L_{sim}$ relative to the certified robustness loss, would directly test whether the proposed components drive the observed improvement.
- A comparison on a second dataset (e.g., CIFAR-100) or a larger architecture would significantly strengthen the generality claim.
- Reporting computation time and memory usage would support the claim that the method is "practical."
- A theoretical or geometric justification for the specific form of $L_{sim}$ would improve the paper's foundation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The method cannot be understood or reproduced; loss function is not clearly defined"** (from Harsh Critic): Overstated. The equations for $Rota_{van}$, $Rota_{cer}$, and $L_{sim}$ are all present in Section 4.4. The method is describable and would be reproducible with the given equations, even if the justification is thin. Removed as factually incorrect — the definition exists.

- **"Figures not available in extracted text"**: This is a PDF-extraction artifact, not a paper flaw. Removed per hard rules.

- **"Missing appendix, proofs in appendix, absent references"**: Parser-stripped content; the original submission contains these. Removed per hard rules.

- **"Formatting issues, broken equations, typos"**: Parser artifacts. Removed per hard rules.

- **"The paper lacks theoretical analysis"**: Nice-to-have for an empirical paper, not a core weakness. Moved to Nice-to-Haves.

- **Strength: "Principled analysis of why certified training hurts clean accuracy"** (from Strength Finder, Section 4.2): This section is actually vague and informal, not "principled." Removing this strength as it conflicts with the verified weakness above.

- **Strength: "Algorithmic presentation (Algorithm 1)"** (from Strength Finder): Algorithm 1 is shown only as an image and cannot be verified from the text. Its content is opaque to the reader. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that meaningfully reframes or extends the paper's idea beyond what the authors state. The core insight — using SVD rotation matrices from a pre-trained vanilla model as a distillation target during certified robust training — is the paper's own contribution and is not deepened by the reviewer commentary.

## Suggestions

1. **Add a results table** with absolute clean accuracy, certified accuracy, and their standard deviations (over ≥3 runs) for Duet, global-Lipschitz, and local-Lipschitz baselines. Without this table, the claimed improvements are unverifiable.
2. **Define the rotation-matrix similarity metric** used to produce the 77.8%/95.6% numbers. Without this definition those numbers are meaningless.
3. **Conduct ablation studies** on (a) the low-rank parameter $r$, (b) the weight of $L_{sim}$, and (c) a version without $L_{sim}$ to establish that the proposed component is responsible for the improvements.
4. **Provide a justification** — even a brief geometric or optimization-based one — for the specific form of the scaling ratios in $L_{sim}$.
5. **Report computation time and memory** as promised in Section 5.
6. **Extend to at least one more dataset** (e.g., CIFAR-100) to demonstrate generality.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>