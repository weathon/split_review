Now I have all the information needed to synthesize the review. Let me write the final consolidated review.

## Summary
This paper identifies a trade-off: reducing the Lipschitz constant of individual models (via spectral norm clipping) improves per-model robustness but increases the transferability rate of adversarial examples across ensemble members, harming ensemble-level robustness. To address this, the authors propose LOTOS (Layer-wise Orthogonalization for Training rObust enSembles), which orthogonalizes the top singular subspaces of corresponding affine layers across models, reducing transferability while retaining the benefits of Lipschitzness. The method is shown to be efficient for convolutional layers (k=1 suffices theoretically and empirically), achieves 4–6 p.p. improvement over clipping alone, scales well with ensemble size, and can be combined with TRS (prior SOTA) for additional gains (up to 10.7 p.p. on CIFAR-10/DLA).

## Strengths
1. **Identifies a novel and practically relevant trade-off.** The paper shows—empirically and via Proposition 3.3 (as a motivating heuristic)—that decreasing the Lipschitz constant increases the transferability rate among ensemble members, creating a tension between individual robustness and ensemble diversity. Figure 1 provides clean empirical evidence of this effect across multiple clipping values.

2. **Introduces LOTOS, a principled and efficient method for reducing transferability.** The idea of orthogonalizing the top singular subspaces of corresponding layers across models is both novel and elegant. Theorem 4.1 shows that for convolutional layers, even k=1 provides a bound on the output when applied to remaining singular vectors, and Figure 3 (Left) empirically confirms that k=1 performs nearly identically to k=15 (<1% difference), making the overhead negligible.

3. **Strong empirical validation across multiple settings.** Table 1 shows consistent improvements (4–6 p.p.) over clipping alone across two datasets (CIFAR-10/100) and two architectures (ResNet-18, DLA). Table 2 demonstrates that LOTOS leverages increasing ensemble size much more effectively than baselines (10.3 p.p. improvement from 3→9 models vs. ~2 p.p. for Orig or C=1).

4. **Compatibility with prior SOTA methods.** Table 3 shows that combining LOTOS with TRS yields robust accuracy improvements of up to 10.7 p.p. over TRS alone, and the ablation chain (TRS → TRS+C=1 → TRS+LOTOS) confirms that LOTOS adds value beyond clipping.

5. **Extensive ablation studies on design choices.** The paper systematically ablates k (number of singular vectors), ensemble size, and the number of orthogonalized layers (finding the first layer suffices, Figure 3 Right), providing practical guidance for deployment.

6. **Cleaner definition of transferability rate.** The conditional probability formulation (Definition 3.2) improves on prior joint-probability definitions by isolating the property of interest from confounding factors like model accuracy and attack success rates.

## Weaknesses

### Major
1. **Missing black-box robust accuracy for heterogeneous ensembles (§5.4).** The paper claims LOTOS is uniquely applicable to heterogeneous architectures (where prior methods cannot be used). However, the heterogeneous experiment (ResNet-18, ResNet-34, DLA) reports only transferability trends and individual model robust accuracy—not the ensemble's robust accuracy against black-box attacks. Without this, the key claim that LOTOS "is an effective method for training robust ensembles of heterogeneous architectures" (Introduction) is only partially supported. The reader cannot assess whether the reduced T_rate actually translates to improved ensemble robustness in this scenario.

2. **Theorem 4.1 is proven only for a restricted setting that does not match practical networks.** The theorem assumes 1D convolution with a single input/output channel and circular padding. The paper uses this to justify that k=1 suffices for general convolutional layers, but no formal argument bridges the gap to 2D multi-channel convolutions with zero-padding used in standard architectures (ResNet, DLA). While the empirical evidence (Figure 3 Left) partially fills this gap, the theoretical grounding is narrower than claimed. This over-claim should be acknowledged and the gap discussed.

### Minor
1. **Proposition 3.3 provides only heuristic motivation, not a rigorous link to transferability.** The proposition bounds the difference in population losses on adversarial examples, which the paper uses as a proxy for transferability. The paper acknowledges this is a "conjecture" and the reasoning is heuristic, but the narrative in §3.2 could more clearly distinguish the formal bound from the hypothesized connection to transferability rates.

2. **No ensemble robust accuracy reported for different `mal` values.** Figure 2 shows how `mal` affects transferability and individual robust accuracy, but the paper does not report ensemble-level black-box robust accuracy for different `mal` values. This makes it unclear whether the transferability improvements at strict orthogonalization (mal=0) translate to optimal ensemble robustness, or whether a small positive `mal` might yield a better trade-off.

3. **k-ablation (§5.3.2) measures only T_rate, not ensemble robust accuracy.** Figure 3 (Left) shows that k=1 through k=15 yield nearly identical T_rate, but the paper does not verify that this translates to equivalent ensemble robust accuracy. While T_rate is the direct target of LOTOS, robust accuracy is the ultimate metric of interest.

4. **`w_i` in Equation (3) is not defined in the main text.** The weights in the S_k loss term are introduced without explanation. (This may be addressed in a footnote or appendix stripped by the PDF parser, but it should be defined in the main body for clarity.)

5. **No discussion of limitations (§6).** The conclusions would benefit from explicitly acknowledging: the need for similar architectures for full-layer LOTOS, sensitivity to the `mal` hyperparameter, the computational cost of SVD at each iteration, and the scope gap in Theorem 4.1.

### Trivial
- None that survive filtering.

## Nice-to-Haves
- **Confidence intervals or variance estimates for T_rate measurements.** As noted by a reviewer, the conditional probability definition of T_rate requires many samples where both models are correct and the attack fools the source, which could yield high variance. Reporting confidence intervals would strengthen the reliability claims.
- **Causal disentanglement experiment.** The increased transferability from clipping (Figure 1) could partly stem from reduced model capacity rather than Lipschitzness per se. An experiment controlling for capacity (e.g., smaller networks without clipping) would strengthen the causal argument.
- **Reporting gradient cosine similarity or prediction disagreement** as complementary diversity metrics to further corroborate that LOTOS increases diversity beyond what T_rate captures.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Criticism about "first to study" claim being overstated.** The paper qualifies this with "To the best of our knowledge," which is appropriate for novelty claims. Removed as a generic nitpick.
- **Criticism that Table 3 comparison is "unfair" or that the 10.7 p.p. improvement is not backed.** The paper provides TRS+C=1 as a controlled baseline, and TRS+LOTOS outperforms it (49.3 vs 42.5 on DLA CIFAR-10), confirming LOTOS adds value beyond clipping. The claim is properly supported. Removed as factually incorrect about the data.
- **Criticism that other SOTA methods are relegated to the appendix.** This is standard practice; the paper mentions DVERGE in the appendix and focuses on TRS (the current SOTA) in the main paper. Removed as a scope-creep formatting preference.
- **Criticism about "motivation conflating" the narrative.** The paper clearly describes a trade-off with both sides supported by data. Removed as a misreading.
- **Criticism about missing detail on whether TRS+LOTOS uses adversarial training.** TRS inherently uses adversarial training; TRS+LOTOS uses TRS's training procedure as stated. Removed as a misunderstanding.
- **Criticism about Theorem 4.1 bound looseness.** Already subsumed by the major weakness about restricted setting. Removed as redundant.

## Novel Insights
The reviewers' critiques center on a genuine gap between the paper's ambitions and its evidence in two specific areas (heterogeneous ensemble evaluation and Theorem 4.1 scope), but both areas are partially addressed by strong empirical results. The most interesting tension revealed across reviews is that the paper's core strength—a simple, principled, computationally cheap method (k=1, first layer only) that cleanly addresses a previously unrecognized trade-off—is also where the reviewers push hardest for formal rigor. This suggests the community would benefit most from a version of this work that either (a) extends Theorem 4.1 to practical 2D conv settings, or (b) is more explicit about treating it as an empirical finding supported by the theorem for a simplified case. The missing heterogeneous ensemble evaluation is a straightforward experimental gap that the authors can fill in a rebuttal.

## Suggestions
1. **Add black-box robust accuracy for heterogeneous ensembles** to §5.4. This is the most critical missing experiment and directly supports a major claimed advantage of LOTOS.
2. **Acknowledge the scope of Theorem 4.1** explicitly: state that it holds for 1D single-channel convolutions with circular padding, and note that the empirical results (Figure 3) validate the same conclusion for practical 2D multi-channel settings.
3. **Report ensemble robust accuracy for at least 2–3 values of `mal`** (e.g., mal=0, 0.4, 0.8) to justify the choice of mal=0 in the main experiments.
4. **Add a limitations paragraph** to the conclusions discussing the Theorem 4.1 scope gap, the need for similar architectures for full-layer LOTOS, and sensitivity to `mal`.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>