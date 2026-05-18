## Summary

This paper provides a theoretical analysis of when and why contrastive representations from unpaired modalities (A and C) can be meaningfully compared via an intermediate modality (B). It proves that under Assumptions 1–3 (conditional independence, density-ratio encoding, and uniform hyperspherical marginal), the probability ratio p(C|A)/p(C) is a monotonic function of the inner product ϕ(A)ᵀϕ(C) — the "Law of the Unconscious Contrastive Learner." When the marginal uniformity assumption is violated, the paper offers a principled Monte Carlo (LogSumExp) fallback requiring only the first two assumptions. Experiments on synthetic data, pretrained CLIP/CLAP/LanguageBind models, and a language-conditioned RL task validate the theory and demonstrate the practical utility of the Monte Carlo approach.

## Strengths

1. **First rigorous justification of the "direct comparison" heuristic.** Lemma 2 (Section 4.3) proves that under stated assumptions, the dot product between representations of unpaired modalities is a monotonic function of the true probability ratio. Prior work relied on this heuristic without theoretical grounding. The derivation via the von Mises-Fisher distribution is principled, and the form of the result (monotonic function of inner product) precisely captures what practitioners assume.

2. **Principled fallback that drops the strongest assumption.** The Monte Carlo method (Section 5) converts Lemma 1 into a practical LogSumExp algorithm that requires only Assumptions 1–2 (conditional independence and density-ratio encoding) and not the uniformity assumption. This is not merely a theoretical aside — Figure 2 shows a concrete case where the Direct method fails while Monte Carlo succeeds, matching the theory's predictions. The precomputed-representation-matrix trick makes the approach computationally feasible.

3. **Assumption-by-assumption experimental validation.** The synthetic experiments (Figure 2) systematically vary which critic function (L2, dot product, normalized dot product) is used, tracing performance gaps to specific assumption violations. Section 6.2.2 goes further by testing Assumption 3 on real CLIP/CLAP representations using a Kolmogorov-Smirnov test (p-values 0.088 and 0.179). This level of diagnostic validation is rare in multimodal contrastive learning papers.

4. **Zero-shot bridging of mismatched pretrained models.** Using CLIP (vision-language) and CLAP (audio-language) with no additional training, the Monte Carlo method achieves 62% Recall@10 on AudioSet, far above the 14% of direct comparison (Figure 4). This demonstrates that the theory translates to practical utility with off-the-shelf models from different sources — a capability not shown in prior methods requiring joint fine-tuning.

## Weaknesses

### Fatal
None.

### Major
1. **The triangle-inequality argument in Section 4.2 is mathematically incorrect.** The paper claims that for unit vectors, ϕ(A)ᵀϕ(B) + ϕ(B)ᵀϕ(C) ≥ ϕ(A)ᵀϕ(C) follows from the triangle inequality. This is false in general — e.g., with 120° between each pair (ϕ(A)=[1,0], ϕ(B)=[-0.5, √3/2], ϕ(C)=[-0.5, -√3/2]), the left side is -1 while the right side is -0.5, violating the claimed inequality. **However**, this does not affect the main results (Lemmas 1–3 rely on different derivations), and the paper itself notes this is "not the identity that we want" and that "we will need a different proof technique for our main result." The error should be corrected (either removed or replaced with a valid bound), but it does not threaten the core contribution.

2. **The RL experiment lacks quantitative rigor.** The paper claims "20%–30% improvement" in success rates but reports no exact numbers, no table of results, no standard deviations across seeds or environments, and no explicit description of how many Monte Carlo samples were used. For a paper with otherwise careful empirical work, this is a notable gap. A table with means and variances across multiple seeds is needed to evaluate the claim properly.

### Minor
1. **No direct validation of probability-ratio estimates on synthetic data.** The theory (Lemmas 1–2) makes explicit predictions about the form of p(C|A)/p(C), but the synthetic experiments report only Recall@1. A direct comparison of the estimated ratio to the ground-truth ratio (which is available in closed form for the linear-Gaussian setup) would substantially strengthen the link between theory and evidence. Retrieval accuracy can be high even if the estimated ratios are systematically biased, as long as ranking is preserved.

2. **Sensitivity to violations of conditional independence (Assumption 1) is not assessed.** The paper correctly notes this assumption is necessary for identifiability, but the real-world experiments (CLIP/CLAP/LanguageBind, RL) involve modalities where A and C may share information not fully captured by B. The paper would benefit from a synthetic experiment where the assumption is controllably violated (e.g., by adding a direct A→C edge) to quantify how performance degrades.

3. **The Monte Carlo approximation uses a potentially biased sample of B.** For the AudioSet experiment, the intermediate modality distribution is approximated using the AudioSet ontology — a fixed set of class descriptions. The paper does not discuss how representative this set is of the true p(B) or what bias this introduces. A convergence plot (Recall vs. number of Monte Carlo samples) would help assess this.

### Trivial
None.

## Nice-to-Haves
- A practical decision rule: given a new dataset, how should a practitioner decide between Direct and Monte Carlo? The KS test used in Section 6.2.2 is a natural diagnostic — the authors could explicitly recommend it.
- Computational cost analysis: the Monte Carlo method requires evaluating f for N samples per (A,C) pair. A brief complexity note would be helpful.
- Convergence plots for the LanguageBind Monte Carlo gap (currently deferred to appendix).

## Removed Points
- **"Bessel function expression is incomplete/garbled"**: The expression g(x) = (2π)^{p/2} I_{p/2-1}(x) on line 130 is missing the denominator κ^{p/2-1}, but this is a parser/formatting artifact. The correct expression (with κ^{p/2-1} denominator) is standard VMF normalizing constant literature and appears correctly in the VMF definition on lines 134. Not a substantive error.
- **Strength Finder strengths about "importance of the problem" and generic praise**: These are superficial/unspecific and removed. Only strengths with concrete evidence are retained.
- **Criticisms about missing appendix content**: The appendix exists in the original submission; parser stripped it.
- **"Assumption 1 is strong and untested" presented as a critical issue**: The paper explicitly acknowledges this assumption is necessary for identifiability (lines 63–66). Testing sensitivity to violations is a nice-to-have, not a fatal gap. Moved to minor weakness.

## Novel Insights

The harsh critic's observation about the Section 4.2 triangle inequality error is genuinely insightful — it identifies a mathematical mistake in the intuition-building section that the reviewer likely caught by checking the actual inequality rather than accepting it at face value. The critic correctly notes that this error is not propagated to the main lemmas but should be corrected. Beyond this, the reviews converge on the same assessment: the core theory is sound and valuable, the experiments are well-designed but limited in certain ways (no direct ratio validation, incomplete RL reporting). No reviewer identified a flaw that would invalidate the paper's central claims.

## Suggestions
1. Remove or correct Section 4.2. The attempted triangle-inequality bound is mathematically invalid (counterexample with 120° angles). Either replace it with a valid bound (e.g., using the geodesic triangle inequality with the cosine addition formula) or delete the subsection entirely — the main results do not depend on it.
2. Add a direct ratio validation experiment on the synthetic linear-Gaussian data: compare the Monte Carlo estimate and the Bessel-transformed inner product to the ground-truth p(C|A)/p(C). This would close the loop between theory and evidence.
3. Report RL results in a proper table: success rates with standard deviations across multiple seeds, environments, and Monte Carlo sample counts.
4. Add a synthetic experiment with controlled violations of Assumption 1 (direct A→C dependence) to quantify sensitivity.

## Score and Decision

**Calibration anchors (all 5 read in full):**

| Path | Avg Score | Comparison to Current Paper |
|------|-----------|----------------------------|
| Pe3AxLq6Wf (multimodal contrastive theory) | 6.25 | Similar scope; current paper has cleaner theory but fewer real-world benchmarks. Comparable quality. |
| S5yOuNfSA0 (CLIP transfer theory) | 6.50 | Both provide theoretical analysis of contrastive alignment; current paper is more general whereas S5yOuNfSA0 is CLIP-specific. Similar strength. |
| 6EadiKkfgR (contrastive semantic learners) | 5.25 | Weaker experiments and less grounded theory. Current paper is stronger. |
| hLZQTFGToA (InfoNCE = spectral clustering) | 4.50 | Had serious mathematical issues in derivations. Current paper has cleaner proofs and better experiments. Stronger. |
| QCY1WQXTc8 (SimO loss) | 3.00 | Very weak experimental validation (one dataset, one backbone). Current paper is far stronger. |
| ZINaxJyoQr (Barlow Twins theory) | 1.50 | Incomplete paper with no meaningful experiments. Current paper is incomparably stronger. |

Positioned among the high-scoring anchors, the current paper is comparable to the ~6.0–6.5 band. Its theoretical contribution is clean and original, the experiments are systematic and assumption-aware, and the weaknesses (triangle-inequality error in an intuition section, incomplete RL reporting, lack of direct ratio validation) are real but do not undermine the core claims. It is meaningfully stronger than mid-to-low scoring papers in the same topic area.

**MY FINAL SCORE:** <score>6.0</score>
**MY FINAL DECISION:** <decision>Accept</decision>