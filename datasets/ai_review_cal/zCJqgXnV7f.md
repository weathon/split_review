- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper studies PAC best-item identification from subset-wise relative feedback under the Plackett-Luce model. It contributes two algorithms: **Dynamic Elimination (DE)**, which prunes suboptimal items dynamically during subset play rather than evaluating static subsets (achieving \(O(\frac{n}{\epsilon^2}\ln(\frac{n}{n_s\delta}))\) sample complexity), and **DEBC**, which extends DE by leveraging item correlation information to perform probabilistic "inferred updates" on unplayed items. Experiments on synthetic datasets show order-of-magnitude improvements over prior baselines (TTB, DAB, DKWT).

## Strengths

1. **Dynamic elimination is a clean and motivated algorithmic innovation (Section 5, Algorithms 1–2).** Prior work (Saha & Gopalan 2019a,b; Haddenhorst et al. 2021) evaluates static subsets and waits for a winner to emerge, wasting plays on items already known to be suboptimal. DE eliminates items as soon as they are provably non-Condorcet with high probability. The running-winner inheritance mechanism (Alg. 2 lines 8–11) addresses the technical challenge of what happens when a running winner is eliminated. Experiments confirm this design yields large practical gains.

2. **Formalization of inferred updates from item correlations (Section 6, Theorem 2–3).** The paper introduces a principled Bayesian framework for probabilistically updating pairwise win-ratio estimates of unplayed items using correlation information. Theorem 2 derives a closed-form expression for \(p_{jk|ik}\) under a latent-embedding cosine-similarity model (Eq. 1). Theorem 3 claims the combined empirical+inferred sequence yields an unbiased estimator. This is a novel extension beyond standard rank-breaking and is conceptually interesting.

3. **DEBC item-selection strategy (Section 7.1).** The principled selection of poorly-correlated initial subsets and least-correlated replacements to maximize coverage of the item space is a well-reasoned departure from the random selection in prior work. It directly connects to the effectiveness of inferred updates.

4. **Consistent and large empirical improvements across multiple settings (Section 8, Figures 1–3).** Experiments cover three distinct vector-distribution scenarios (weakly correlated Gaussian vectors, well-separated clusters, overlapping clusters), vary \(\epsilon\), \(n_s\), and \(n\), and include ablation on correlation noise and short-term performance. Both DE and DEBC consistently exceed 95% accuracy while requiring orders of magnitude fewer samples than TTB, DAB, and DKWT. The improvement is sustained across all scenarios tested.

## Weaknesses

### Fatal
None.

### Major

1. **Theorem 4 uses undefined quantities, making it unverifiable.** The theorem's sample complexity bound (line 248) depends on \(w_{\min}^{\text{in}}\) which is never defined. Condition 4 of the theorem (line 254) invokes \(\text{Info}(\cdot)\) and \(\lambda\) without definition. Additionally, condition 2 uses both \(\varepsilon\) and \(\epsilon\) (line 254) without clarifying whether these are distinct parameters. A central theoretical result that cannot be parsed by a knowledgeable reader is a significant presentation gap.

2. **No pseudocode or algorithmic box is provided for DEBC (Section 7.1).** While DE is specified by Algorithms 1 and 2, DEBC's item selection strategy ("least correlated to items that have already been played") is described only in prose. The selection metric, tie-breaking, and initialization procedure are underspecified. This makes the precise algorithm ambiguous and the experimental results harder to reproduce or build upon.

3. **Missing ablation: the contribution of inferred updates vs. item selection is confounded.** DEBC differs from DE in two ways: (a) correlation-based item selection, and (b) inferred updates. The experiments compare DEBC directly to DE, but the performance gap could be driven primarily by better item selection alone. An ablation running DE with DEBC's selection (without inferred updates), or DEBC with random selection (without correlation-based selection), is needed to attribute the gains correctly.

4. **Unbiasedness claim for inferred updates (Theorem 3) is not adequately justified.** The proof sketch (2 sentences) states that combining empirical and inferred sequences yields a Beta mixture whose mean is the sample mean. However, the inferred updates are functions of the same empirical data that informed the prior — the independence required for the standard unbiasedness argument is not established, and the proof sketch does not address this. Given that Theorem 3 is one of the paper's four headline contributions, this gap is significant.

### Minor

1. **No error bars or variance information reported despite 100 trials.** The paper states "each setting is run for 100 trials" (line 268), but Figures 1–3 are described only as line plots. Without confidence intervals, quartiles, or any measure of variance, it is impossible to assess the statistical significance of the reported improvements.

2. **DKWT modification is not described.** The paper says "we consider a modified version of DKWT... We compare both algorithms under this equivalence" (line 264), but neither the modification nor "this equivalence" is explained in the main text. This makes the primary baseline comparison uninterpretable on its face.

3. **No evaluation on real-world datasets.** The paper claims applications in recommender systems, search, and NLP (Section 1) but evaluates only on synthetic data (N¹⁶, DIM, G2). While synthetic experiments are acceptable for a theory-driven paper, the claimed practical relevance would be strengthened by at least one realistic benchmark.

4. **Uniform query distribution assumption is implicit but not discussed.** The derivation of \(p_{jk|ik}\) (Theorem 2) relies on query vectors being uniformly distributed on the unit sphere (implied by the geometric area-of-hemisphere-intersection argument). This assumption is not stated explicitly, nor is its practical plausibility discussed or tested.

5. **Proof sketches in the main text are very brief.** Each theorem is accompanied by a 2–5 sentence sketch. While full proofs may reside in the appendix, the main-text sketches for the central claims (particularly Theorems 3 and 4) are too vague for a reviewer to assess the logic without the supplementary material.

### Trivial
- TTB and DAB are mentioned as having sample complexities "orders of magnitude larger" (line 272) but are not plotted in Figures 1–3. Including them (even on a separate scale or as annotations) would improve verifiability.
- Algorithm 2, line 10's weighted-average update (\(P_{ij} \gets P_{i^*j} \times N_{i^*j} + P_{ij} \times N_{ij}\)) is described but the normalization post-update could be clarified.

## Nice-to-Haves
- A small simulation validating the unbiasedness of the inferred-update estimator on known PL data would substantially strengthen the theoretical claim.
- Reporting the sharpness values used in experiments and showing sensitivity (the paper mentions Figure 1.4 which appears to vary sharpness, but the values are not stated in text).
- A discussion of whether and how the method extends to settings where item correlations are estimated from data rather than known a priori.

## Removed Points

- **"Sharpness parameter gives unfair advantage to proposed method"** — The paper explicitly states sharpness "induces faster convergence across all instance optimal algorithms (DE, DEBC, DKWT)" (line 268), meaning it is applied uniformly. The critic's concern about tuning asymmetry is not supported by the text.
- **"Missing related work: Yang & Feng (2023) not compared"** — This work operates in a different setting (variable-size subsets), which the paper notes. Not comparing against a method in a different problem setting is not a weakness.
- **"No code release, no hyperparameter tables"** — These are standard reproducibility concerns but the instruction removes nitpicks about reproducibility artifacts impractical to include.
- **Claims about stripped appendix content** — References to Lemma 5, Lemma 10, and footnotes (".1." artifacts) are parser-stripped content that exists in the original submission.
- **"Evaluation fairness" as a general claim** — The critic's broad assertion that the comparison is unfair lacks specific anchor points beyond the DKWT modification (kept) and sharpness (removed above).
- **Strength Finder's generic strengths** — "This paper addressed an important problem" and similar generic statements are removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Define every symbol used in Theorem 4 (\(w_{\min}^{\text{in}}\), \(\text{Info}(\cdot)\), \(\lambda\), clarify \(\varepsilon\) vs \(\epsilon\)) and show that condition 4 is satisfiable for reasonable parameter values.
2. Provide a pseudocode box for DEBC that specifies the item selection and replacement procedure precisely.
3. Add an ablation experiment: DE with DEBC's item selection (without inferred updates) vs. DEBC with random selection (without correlation-based selection) to disentangle the two contributions.
4. Add confidence intervals or quartiles to all figures reporting sample complexity over 100 trials.
5. Describe the DKWT modification explicitly so the baseline comparison is interpretable.
6. Expand the proof sketches in the main text, especially the unbiasedness argument for Theorem 3, to at least sketch the handling of dependence between inferred and empirical sequences.
