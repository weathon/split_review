- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 3, 5, 5
Now I have a thorough understanding of the paper and can evaluate each reviewer claim against the actual text. Let me compose the final consolidated review.

## Summary

This paper tackles the plasticity problem in incremental segmentation learning. The core idea is that instead of freezing old knowledge representations (which causes feature overlap and limits learning of new classes), the method dynamically adjusts feature distributions through two principles: **compression** (shrinking and dimension-reducing old feature representations) and **sparsity** (maximizing the separation between Gaussian mixture peaks of different classes). The paper provides a mathematical motivation (Section 3.2), describes an implementation with learnable feature reconstruction constraints and a contrastive/knowledge-transfer loss, and reports strong empirical gains — most notably 11.7% MIoU improvement on the incremental stage of the VOC 10‑1 setting.

---

## Strengths

1. **Clear, well-motivated core idea with strong empirical support (Tables 1, 2).** The paper identifies a genuine limitation of existing incremental segmentation methods — that freezing old feature representations causes overlapping subspaces that hurt plasticity — and proposes a sensible remedy (compression + sparsity). The experimental results are striking: up to 11.7% MIoU improvement on the 10‑1 VOC setting and consistent gains across multiple configurations and datasets (VOC, ADE20K). These results directly support the paper's central claim.

2. **Ablation study disentangling compression and sparsity components (Table 3).** The paper systematically ablates compression (C) and sparsity (S) in both 19‑1 and 10‑1 settings. The ablation shows that removing either component degrades performance, confirming that both are necessary and that the method is not a one-trick solution. This is the right kind of evidence for a two-component method.

3. **Empirical comparison of fusion strategies (Table 4) and sensitivity analysis (Table 5).** The paper compares attention-based fusion against weighted fusion over five incremental settings and provides a sensitivity analysis for α/β. This gives the reader a clear picture of design choices and their robustness.

---

## Weaknesses

### Fatal
None. The paper's core contribution (the compression-sparsity approach and its empirical validation) survives scrutiny, though significant issues exist.

### Major

1. **The theoretical derivation (Section 3.2) does not convincingly support the method and contains logical gaps.**
   - The transition from Eq. (1) to Eq. (2) requires an assumption that X₁ and X₂ are independent (given θ or marginally), which is neither stated nor justified. In the paper's own framing, X₁ and X₂ are datasets from different learning steps — the required independence is not obvious.
   - The claim that "log P(θ|X₁) follows a Gaussian mixture distribution" (Eq. 3) is presented as fact without motivation or reference; it is at best an approximation.
   - Eq. (6) introduces Nₖ, λₖᵖ, and σₖᵖ without proper definition (only N and F(θ*) are defined in the surrounding text). The reference to prior work (Martens, 2014; Huszár, 2017) does not rescue the notation.
   - The leap from Eq. (7) ("P(X₂|θ)=∏P(Cₖ|θ,Pₓ,Pᵧ)") to the conclusion that "class features should demonstrate substantial differentiation and minimal positional coupling" is an intuitive assertion, not a logical consequence of the equation.
   
   **Why it matters**: The paper presents Section 3 as a "mathematical structural analysis" and claims it demonstrates the benefit of compression-sparsity. As written, it does not provide a valid derivation; it offers loose motivation at best. This overclaiming weakens the paper's intellectual framing, though it does not invalidate the method (which can stand on its empirical merits).

2. **The method description is under-specified in ways that compromise reproducibility from the paper alone.**
   - How "high-dimensional knowledge is transformed into a three-dimensional Gaussian mixture distribution" is never specified. What is the feature space? How are the GMM parameters estimated? The paper states only that the three dimensions are "horizontal pixel position, vertical position, and pixel feature response" — a description, not an algorithm.
   - "After calculating convex points in feature space" — "convex points" are not defined, and no procedure is given for computing them.
   - Equations (9)–(10) state hard constraints on γ and τ ("subject to..."), but the paper never specifies how these constraints are enforced during optimization. Are they Lagrangian constraints? Penalty terms? Projected gradient updates? This is a critical omission: the core mechanism of the method (feature reconstruction subject to diameter and distance constraints) cannot be implemented from the description.
   - The loss function (unnumbered equation after Eq. 13) has notation that is difficult to parse: the first term mixes P̃ₜⁱ and Pₜ₋₁ⁱ with norms and inner products in a contrastive form, and the second term appears to have a redundant denominator (exp P̃ₜⁱ cancels). This makes the loss ambiguous without the supplementary code.
   
   **Why it matters**: A reader should be able to understand and anticipate the algorithm from the paper. Here, the key implementation details (how constraints are enforced, how the GMD/convex points are handled) are missing. While "code is available in the supplementary materials" mitigates this somewhat, the paper should be largely self-contained.

### Minor

3. **No variance or confidence intervals are reported for any experimental result.** The claimed improvements (up to 11.7%) are large and would be more convincing with multi-run statistics. Single-run results leave open the question of whether the gains are stable.

4. **Baseline implementation details are only partially described.** The paper states that "publicly available codes and training strategies" are used for MiB and LGKD, and Coinseg is retrained with "the same backbone and memory sampling strategy." However, no information is provided about whether baselines were tuned, what hyperparameters were used, or whether the same data ordering/memory buffer was employed. This makes it difficult to assess whether the comparisons are apple-to-apple.

5. **The α/β reporting choice is somewhat inconsistent.** The paper notes that α=0.2/β=0.8 gives better VOC results but uses α=0.8/β=0.2 for reported comparisons (to maintain a consistent setting across datasets). This is acknowledged and explained, but it means the main-table VOC results understate what the method could achieve on that dataset. A simple additional row showing the optimal α/β per dataset would clarify this.

6. **The knowledge transfer confidence threshold (0.7) in Eq. (13) is stated without any justification or sensitivity analysis.** It is unclear how critical this value is to performance.

7. **Training hyperparameters (learning rates, batch size, number of epochs, exact split ordering) are deferred to the supplementary.** While common, including at least the key values in the main paper would improve self-containedness.

### Trivial

8. LaTeX typo in the running text: "$1\bar{1}.8\%$" (the `\bar{1}` produces a rendering artifact; should likely be "$11.8\%$").

---

## Nice-to-Haves

- A single clean algorithmic pseudo-code block would dramatically improve clarity and replace the current scattered description.
- Reporting results over 3–5 random seeds with mean±std would substantiate the claimed gains.
- An analysis of where the method underperforms (failure cases) would strengthen the empirical narrative.
- A runtime/efficiency comparison would help, since the method involves computing GMM peaks and distances per step.

---

## Removed Points

These points are flagged by reviewers but are removed from the main review because they do not hold up against the paper as written:

- **"The mathematical analysis is incoherent/fatal."** The derivation is weak and non-rigorous but not incoherent — it follows a recognizable structure (Bayes → GMM approximation → Taylor expansion → intuitive conclusion). Called "fatal" this is overblown; the paper's contribution is primarily empirical, and the theory serves as loose motivation. **Reason**: Overstated severity; demoted to Major.

- **"Unfair comparison / credibility concerns due to large gains."** Large improvements alone are not evidence of unfairness. The paper describes using public baseline code and retraining with the same backbone. **Reason**: Speculative without concrete evidence.

- **"Missing comparison with dynamic adjustment methods."** The paper explicitly cites Kim et al. 2024 and Wuerkaixi et al. 2024 in the introduction as related dynamic adjustment works. An area-chairs cannot verify whether additional related works are missing without external sources. **Reason**: Not verifiable.

- **"Method not implementable at all."** The paper promises code in supplementary materials; the core idea is intuitive even if details are missing. The issue is under-specification, not impossibility. **Reason**: Demoted from fatal to major under-specification.

- **Various formatting and garbled-text criticisms.** These are parser artifacts, not author errors. **Reason**: Parser issue per hard rules.

- **Strength Finder's claim about "mathematical derivation" being a core strength.** This conflicts with the verified weakness about the derivation being non-rigorous. **Reason**: Contradicted by verified weakness.

- **Strength Finder's claim about "principled fusion" being a major strength.** Comparing two fusion methods and selecting the better one is standard practice, not a principled innovation. **Reason**: Overclaimed as strength; it is a routine design choice.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the method or results that the paper itself does not articulate.

---

## Suggestions

1. **Drop or substantially rewrite Section 3.** Either provide a clean, logically coherent argument (e.g., based on information theory or capacity) or present the method as empirically motivated and drop the pretense of mathematical proof. The current derivation hurts more than it helps.

2. **Specify the constraint enforcement mechanism.** Add one sentence explaining whether γ, τ are optimized with a penalty/Lagrangian term or a projection step. This is the single largest gap in reproducibility.

3. **Define "convex points"** and describe how peaks are extracted from the GMM. Without this, the sparsity mechanism is underspecified.

4. **Clarify the loss function notation** and ensure it is unambiguous. Pseudo-code would help.

5. **Report standard deviations** over multiple runs (at least 3 seeds) for the main results.

6. **Provide a supplementary breakdown** with the optimal α/β per dataset alongside the consistent-setting results, so readers can see both.

---
