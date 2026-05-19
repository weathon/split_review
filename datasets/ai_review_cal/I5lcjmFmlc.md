- Decision: Reject
- Avg Score: 8.00
- Scores: 8, 8, 8
Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper proposes Robust Diffusion Classifier (RDC), a generative classifier built from a single pre-trained conditional diffusion model. RDC: (1) computes class probabilities via Bayes' theorem using the diffusion loss as a surrogate for conditional log-likelihood; (2) applies Likelihood Maximization (LM) as a pre-optimization step to move inputs toward high-density regions; and (3) introduces multi-head diffusion to reduce computational cost from K×T to T function evaluations. The method achieves 75.67% robust accuracy on CIFAR-10 under ℓ∞ (ε=8/255) with strong adaptive attacks, surpassing prior SOTA, and shows dramatic generalization to unseen threat models (e.g., >53% absolute improvement over baselines on StAdv).

## Strengths

- **State-of-the-art robust accuracy with thorough adaptive attack evaluation.** RDC achieves 75.67% robust accuracy on CIFAR-10 under ℓ∞ (ε=8/255) using AutoAttack with BPDA, surpassing AT-EDM by +4.77% (abstract, lines 267). The authors verify that BPDA yields nearly identical results to exact gradients (Table 2: 69.53% vs 69.92% for N=1, lines 321-323), and explicitly rule out gradient obfuscation through low gradient variance measurements (Fig. 2a, lines 337-338).

- **Exceptional generalization to unseen threat models.** RDC outperforms baselines by >30% on average across ℓ∞, ℓ2, and StAdv threats (line 277). On StAdv, RDC achieves 89.45% robust accuracy vs. the best baseline (DiffPure) at 35.55% — a 53.90% absolute improvement (line 277). This is a practically significant finding since most defenses overfit to a specific threat model.

- **Low gradient variance confirms reliable evaluation.** The paper measures pairwise cosine similarity of gradients across 10 samplings (Fig. 2a, lines 337-338). RDC's gradients have variance comparable to a standard classifier, while DiffPure requires 640× EOT to achieve similar levels. This convincingly demonstrates the robustness is not an artifact of obfuscated or stochastic gradients.

- **Likelihood Maximization as a novel pre-optimization defense.** LM directly maximizes the unconditional diffusion loss ELBO under an ℓ∞ constraint (Section 3.3, Eq. 6). This differs from prior purification approaches (e.g., DiffPure's add-noise-then-denoise) by directly optimizing for likelihood, and the paper provides thoughtful comparison with DiffPure (lines 186-188).

- **Multi-head diffusion for practical efficiency.** Modifying the UNet's final convolutional layer to predict noise for all K classes simultaneously reduces NFEs from K×T to T (Section 3.4, lines 231). This architectural contribution makes the diffusion classifier tractable on datasets like CIFAR-10.

- **Comprehensive ablation studies with clear rationale.** The paper ablates the optimization budget η (Fig. 2b), showing robustness peaks at η=8/255, and sampling timesteps T' (Fig. 2c), showing that reducing timesteps harms robust accuracy while preserving clean accuracy. These provide actionable guidance for practitioners.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The theoretical analysis (optimal classifier) is disconnected from the practical method.** Theorem 2 and Corollary 3.1 show that an optimal diffusion model — one achieving minimal diffusion loss over the full data distribution — yields a classifier with 100% robust accuracy. The paper acknowledges the large gap (optimal: 100%, empirical DC: 35.94%, lines 163), but the theory neither informs the design of the algorithm nor explains why Likelihood Maximization helps. The section serves primarily as motivation, and the paper could either connect it more concretely to the empirical method or move it to the appendix.

- **The source of robustness is not fully disentangled.** RDC's robustness jumps dramatically from DC alone (35.94% ℓ∞) to RDC (75.67% ℓ∞), with LM providing the bulk of the gain. While the paper is transparent about both components (it presents DC, LM, and RDC results separately), the framing attributes robustness to the "generative classifier" without sufficient discussion of how much comes from the purification-like LM step versus the generative density estimates. An ablation adding LM + a standard robust classifier (e.g., AT-EDM) would clarify whether the generative classifier or the LM preprocessing is the main driver of the final robustness.

- **Multi-head diffusion lacks quantitative efficiency comparisons.** The paper states the reduction from K×T to T NFEs and mentions "More details are in Sec. 5.3" (line 231). However, no wall-clock time or practical speedup is reported for the multi-head approach versus the naive per-class loop. Given that this is one of the paper's stated contributions, the absence of concrete timing numbers makes the efficiency claim unsubstantiated beyond the theoretical NFE reduction.

### Trivial
None.

## Nice-to-Haves

- Report wall-clock inference times (seconds per image) for multi-head diffusion vs. the naive K×T loop.
- Add an ablation combining LM with a standard robust classifier (e.g., AT-EDM) as the downstream classifier, to separate the benefits of the purification step from the generative classifier.
- Include a brief discussion or analysis of failure cases — what types of adversarial examples successfully attack RDC, given that the empirical model is far from the optimal (100% robust) regime.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Missing main results table (Harsh Critic #1).** The table is loaded via `\input{tables/generalization}` at line 219 and was stripped by the PDF parser. This is a formatting artifact of the extracted text, not an author error. Key numerical claims are stated in the abstract and text (75.67%, StAdv results, etc.). Removed per rule: remove criticisms about parser artifacts.

2. **Unfair DiffPure comparison (Harsh Critic #2).** The critic claims using PGD-200 (vs. AutoAttack for RDC) weakens comparison fairness. The paper explains the choice is due to DiffPure's memory/randomness issues (lines 263-264). Crucially, if PGD-200 is weaker than AutoAttack, DiffPure's reported numbers would be an overestimate of its true robustness — making RDC's improvement even more impressive. The asymmetry favors the baseline, not the author's method. Removed per rule on asymmetric comparisons favoring baselines.

3. **Missing appendix details for multi-head diffusion (Harsh Critic #5, sub-point).** The critic asks whether fine-tuning is needed for multi-head diffusion. The paper states "More details are in Sec. 5.3" (line 231), which was in the appendix stripped by the parser. Removed per rule: remove weaknesses about missing appendix content.

4. **Lagrange attack criticism (Harsh Critic, Section-by-Section).** The critic argues the Lagrange attack does not backprop through LM. The paper's approach is to craft examples that already have small diffusion loss (surviving LM), which is a different attack philosophy. The paper also evaluates BPDA (which does approximate the full gradient through LM) and exact gradients (for N=1). The criticism is addressed by the paper's existing experiments.

5. **StAdv results not shown in a table (Harsh Critic, Section-by-Section).** The StAdv results are stated in text at line 277 (87.50%, 93.55%, 89.45% for LM, DC, RDC). The table would show them alongside baseline comparisons, but the numbers themselves are provided. The missing table is a parser artifact.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a column to the ablation showing LM + a standard robust classifier (e.g., a pre-trained AT-EDM) to explicitly separate the purification benefit from the generative classifier benefit.
2. Report wall-clock inference times for RDC (both standard and multi-head diffusion) against the K×T naive baseline to substantiate the efficiency claim.
3. Provide a brief discussion connecting the theoretical optimal analysis more concretely to the empirical algorithm — for example, characterizing when the gap d(x,y,θ) is likely to be small vs. large, and how LM reduces this gap.
4. Consider showing the main results table even at a reduced resolution in the main text to avoid dependence on the appendix for the paper's core empirical claims.
