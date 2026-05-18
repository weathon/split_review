Now I have all the information I need to write the consolidated review.

---

## Summary

This paper studies the counterintuitive phenomenon that difficult-to-learn examples (samples near decision boundaries) can hurt unsupervised contrastive learning. It develops a similarity-graph theoretical model where cross-class similarity takes three values (α, β, γ), derives linear probing error bounds showing that difficult examples strictly worsen generalization (Theorems 3.1–3.2), and proves that removal, margin tuning, and temperature scaling each improve the bound under the model (Corollary 4.1, Theorems 4.3, 4.5). Empirically, it proposes a cosine-similarity-based selection mechanism for identifying difficult pairs and validates that the three mitigation strategies on selected pairs improve linear probing accuracy across CIFAR-10/100, STL-10, and TinyImagenet.

## Strengths

1. **Novel theoretical framework with explicit error bounds.** The similarity-graph model (Section 3.2) formalizes difficult-to-learn examples via inflated cross-class similarity (γ > β) and yields provable linear probing error bounds. Theorem 3.1 vs. Theorem 3.2 rigorously shows that difficult examples strictly worsen generalization — a result that formalizes empirical observations from prior work.

2. **Unified analysis of three mitigation strategies under one model.** The paper theoretically explains removal, margin tuning, and temperature scaling within the same similarity-graph framework (Corollary 4.1, Theorem 4.3, Theorem 4.5), showing how each modifies the graph to recover a bound comparable to the no-difficult-example case. This provides a coherent perspective on techniques previously studied in isolation.

3. **Empirical validation across multiple datasets with consistent improvements.** Experiments on CIFAR-10, CIFAR-100, STL-10, and TinyImagenet (Tables 1–4) show that the proposed methods improve linear probing accuracy over the SimCLR baseline. The combined method achieves up to +15.0% on TinyImagenet (Table 4), demonstrating that the theoretical insights translate to practical gains.

4. **Practical selection mechanism without pretrained models.** The cosine-similarity-based selection (Section 5.1) is simple to implement, avoids requiring a separate pretrained model, and is shown to be robust to parameter choices (Figure 4a,b). Figure 4(c) validates that selected pairs are predominantly cross-class, aligning with the theoretical definition.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between oracle-based theoretical optimal parameters and practical scalar heuristics.** Theorems 4.3 and 4.5 derive per-pair optimal margins m_{x,x'} and temperatures τ_{x,x'} as explicit functions of the unknown parameters α, β, γ, n, n_d, r (equations 7 and 9). The practical implementations (Sections 5.3–5.4) instead use a single scalar σ or ρ, tuned on a validation set and applied uniformly to all selected difficult pairs. The paper never explains how a single global scalar relates to the per-pair formulas, nor does it analyze how much of the theoretical bound improvement is preserved under this approximation. The theory shows what *oracle-aware* tuning could achieve, but the practical methods are heuristics whose connection to the optimal formulas is unexamined. This gap does not invalidate the theoretical contribution, but it weakens the claim that the theory *explains* the empirical success of these specific implementations.

2. **The selection mechanism is heuristic with only correlational validation.** The practical selector (Section 5.1) identifies difficult pairs via cosine-similarity percentile thresholds (posHigh/posLow). The theoretical definition of difficult-to-learn examples is based on proximity to the decision boundary with cross-class similarity γ > β. The paper validates the selector only by showing that the selected region increasingly contains cross-class pairs during training (Figure 4c). This is correlational evidence, not a guarantee that the selected samples are the ones that degrade the bound. The paper would benefit from discussing sensitivity to selection quality — what happens when some non-difficult pairs are mistakenly included or genuinely difficult pairs are missed.

### Minor

1. **The theoretical model is highly stylized and the paper overstates its scope.** The core theorems rely on a similarity graph where cross-class similarity takes exactly two values (β, γ) and same-class similarity is uniformly α (Section 3.2). Real augmentation graphs are far more complex. The paper mentions a relaxation in Section B.3 (appendix) but the main body does not discuss the gap between the clean model and realistic settings. Calling it a "unified theoretical framework" (title, line 105) overstates the scope — it is an *illustrative* model that captures a plausible mechanism under strong idealizations. A more measured characterization would strengthen the paper's credibility.

2. **Empirical results lack variance information.** All accuracy tables report three-run averages without standard deviations or error bars. Given that improvements are modest on several datasets (0.6–2.2% on CIFAR-10/100 for removal and margin tuning), it is impossible to assess statistical reliability. While the paper frames experiments as secondary validation of theory, variance reporting is standard practice and would substantially improve interpretability.

3. **Key assumptions from prior work are not explained.** The bounds depend on the label recoverability parameter δ and the realizability assumption from HaoChen et al. (2021), mentioned only in one sentence (line 82). A reader unfamiliar with that work cannot gauge the tightness or brittleness of the bounds. Since the paper's main theoretical claim rests on relative comparisons of these bounds, a brief intuitive explanation of δ and its role would improve accessibility.

4. **No comparison against prior methods for handling hard negatives/difficult examples.** The paper does not empirically compare against existing approaches such as hard negative mixing (Kalantidis et al., 2020), importance sampling, or dynamic temperature schedules, even though these address related phenomena. While the paper's primary contribution is theoretical, the practical value of the proposed techniques is hard to assess without situating them among existing alternatives.

### Trivial

1. Computational overhead of the selection mechanism is described only qualitatively as "efficient" (Section 5.1). A wall-clock time comparison with the baseline would substantiate this claim.
2. The mixing-image experiment (Section 2) creates artificially difficult examples via pixel-level blending. While presented as a proof-of-concept, the generalizability of this synthetic difficulty to natural data is not discussed.

## Nice-to-Haves

- The paper could directly test the predictions of the bound comparisons by estimating proxies for α, β, γ during training and checking whether the ordering predicted by the theory (ε_{w.d.} > ε_{w.o.}, ε_R, ε_M, ε_T) holds empirically.
- Ablation studies where margin or temperature is deliberately set *away* from the theory-suggested direction (e.g., scaling up temperature for difficult pairs) would increase confidence that the mechanisms identified are the operative ones.
- A discussion of whether the spectral-InfoNCE equivalence (Johnson et al., 2022) holds at finite samples or during training dynamics would help connect theory to practice.

## Removed Points

- **Criticism that "appendix not seen" (Section B.3 reference):** Removed per rule — the parser strips appendix sections; they exist in the original submission.
- **Criticism that "no comparison against prior methods that handle hard negatives" as a major weakness:** Downgraded to minor — the paper's contribution is primarily theoretical, and extensive empirical comparison is not the core expectation for this class of paper.
- **Criticism about missing δ explanation being a "fatal" omission:** Downgraded to minor — it is a presentation gap, not a flaw in the technical content.

## Novel Insights

The harsh critic's most valuable observation is the disconnect between the oracle-perfect per-pair optimal parameters in the theory and the single-scalar heuristics in practice. This is an insightful structural criticism that raises an interesting question: is the benefit of these methods coming from the correct directional alignment (applying positive margins / lower temperatures to difficult pairs) despite the scalar approximation being far from optimal, or would a per-pair adaptive scheme yield larger gains? The reviewer's suggestion to test the bound orderings empirically (rather than just reporting accuracy gains) would transform the experiments from validation-by-correlation to genuine falsification of the theory's predictions.

## Suggestions

1. **Bridge the theory-practice gap for margins and temperatures.** Either (a) analyze how much of the theoretical bound improvement is preserved under a uniform scalar approximation, or (b) design an experiment that estimates α, β, γ from the data and computes the per-pair optimal values to compare against the scalar-tuned results.

2. **Add error bars / standard deviations to all accuracy tables.** Even three-run standard deviations would greatly increase confidence in the modest gains on CIFAR-10/100.

3. **Tone down the generality claims** ("unified theoretical framework") and more explicitly discuss the idealizations in the similarity-graph model within the main paper, not only in the appendix.

4. **Provide wall-clock overhead measurements** for the selection mechanism to substantiate the claim of efficiency.

## Score and Decision

This paper makes a genuine theoretical contribution by introducing a tractable similarity-graph model that explains why difficult-to-learn examples harm contrastive learning, and it connects this theory to three mitigation strategies with consistent empirical validation. The core insights are novel and clearly communicated. The main weaknesses are the gap between oracle-optimal theoretical parameters and practical scalar heuristics, and the stylized nature of the model. However, these weaknesses are typical of theory papers that bridge to practice and do not invalidate the theoretical contribution. The paper would benefit from addressing the theory-practice gap and adding variance information, but in its current form it represents a solid contribution appropriate for a top venue.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>