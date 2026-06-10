Now I have all the evidence I need. Here is the final consolidated review.

---

## Summary

This paper introduces Discrete Walk-Jump Sampling (dWJS), a generative modeling framework for discrete sequences that trains a smoothed energy-based model via contrastive divergence and decouples MCMC sampling on the noisy manifold from one-step denoising (the "jump"). The method is evaluated on antibody protein generation, with the key empirical result being wet-lab validation: 270/277 (97.47%) of designed antibody sequences expressed successfully, and 70% of trastuzumab CDR H3 redesigns bound to HER2 — substantially higher than concurrent diffusion-model baselines (LaMBO-2: 25%, AbDiffuser: 22%). The paper also introduces a Distributional Conformity Score (DCS) for benchmarking protein generative models.

## Strengths

- **Wet-lab validation is the paper's strongest asset and genuinely rare in this field.** Out of 277 designed antibody sequences tested in the laboratory, 270 expressed and purified successfully (97.47%, Table 1/line 251). This goes far beyond the typical *in silico* evaluation and directly demonstrates that dWJS generates functional proteins.

- **Highest reported binding rate on a standard therapeutic antibody redesign benchmark.** dWJS achieves 70% binding for trastuzumab CDR H3 redesign without post-hoc filtering, compared to 25% (LaMBO-2) and 22% (AbDiffuser, 57% with filtering) — both concurrent diffusion-model methods reporting wet-lab results on the same task (Section 3.3, Table 2/line 279). This is a direct, quantitative comparison on an identical benchmark.

- **Simplifies EBM training by eliminating standard engineering tricks.** The paper demonstrates that fitting the energy function to *noisy* data removes the need for replay buffers, ℓ₂ norm penalties, simulated annealing, and rejection sampling that are otherwise standard for training EBMs (Conclusions, line 292). This is supported by the ablation: a standard EBM on clean data achieves only 42% expression versus 97%+ for dWJS (Table 2).

- **Introduces and empirically calibrates a new evaluation metric (DCS) to wet-lab outcomes.** The Distributional Conformity Score provides a single scalar measure of sample-to-reference similarity, and the paper reports that methods with DCS > 0.3 yield nearly 100% expressing proteins in the lab (line 178). This gives practitioners a practical *in silico* proxy.

## Weaknesses

### Fatal

None.

### Major

- **The paper presents two distinct variants ("dWJS (energy-based)" and "dWJS (score-based)") under the same method umbrella without clearly committing to which is the core contribution, creating ambiguity about what "dWJS" actually is.** These variants use qualitatively different sampling procedures: the energy-based variant follows gradients of a separately trained EBM (Algorithm 1, line 119), while the score-based variant follows the denoiser's score function directly (line 87). They also perform differently on nearly every metric — the energy-based variant achieves the best Wasserstein distance (0.056) and uniqueness (1.0), while the score-based variant achieves the best edit distance (62.7), internal diversity (65.1), and DCS (0.49) (Table 1, lines 216–217). The score-based variant is essentially the original Walk-Jump Sampling from Saremi et al. (2019); the energy-based variant (training an EBM on the smoothed distribution) is the novel contribution. The paper never clearly states this distinction, leaving readers unsure which variant constitutes "the method" and whether the reported gains stem from the new framework or from standard WJS applied to discrete data. On line 90 the paper says "take advantage of this decoupling to train an EBM," suggesting the energy-based variant is the primary contribution, but the paper continues to present both as "dWJS" throughout the evaluation.

### Minor

- **No quantitative mixing analysis despite a central claim of "fast-mixing MCMC chains."** The abstract and line 28 claim the "first demonstration of long-run fast-mixing MCMC chains where diverse antibody protein classes are visited in a single MCMC chain," and Figure 1 shows samples colored by germline. However, there is no quantitative evidence — no autocorrelation times, effective sample sizes, or Gelman-Rubin diagnostics. The mixing claim rests entirely on visual inspection of one chain.

- **The abstract's binding claim conflates a constrained redesign task with unconditional generation.** The abstract states "70% of functional designs show equal or improved binding affinity," but this result is specifically from the constrained CDR H3 redesign of trastuzumab (Section 3.3), not from unconditional *ab initio* generation. An unqualified reader would assume this is a binding rate for unconditional discovery. The paper should clearly scope this claim.

- **No breakdown of how many of the 277 tested sequences came from each variant.** The paper reports 270/277 expressed (line 251) and separately reports that the score-based variant achieved 100% expression and the energy-based variant 97% (Table 2), but never states how many sequences each variant contributed to the aggregate. This makes it impossible to assess whether the aggregate is dominated by one variant.

- **The 1D-CNN classifier used to compute binding probabilities has 86% accuracy, but no precision/recall is reported, and the impact on reported binding rates is unexplored.** The classifier screens 1000 samples and the binding probabilities (p_bind in Table 2) are used as a headline result. At 86% accuracy, if the base rate of binders is modest, the classifier's precision/recall trade-off could substantially distort the reported probabilities. The paper should acknowledge this limitation and report precision/recall (line 277).

- **Missing implementation details for critical parameters.** Algorithm 1 defines step size δ and number of MCMC steps T, but neither is specified anywhere in the paper. These are not trivial settings — they control the trade-off between sampling quality and compute cost. Similarly, the contrastive divergence inner MCMC loop parameters are not discussed. While detailed hyperparameter tables may reside in the stripped appendix, these parameters are central to reproducibility.

- **No discussion of failure cases or limitations.** The paper reports uniformly positive results. The 7 non-expressing sequences and the 30% non-binding trastuzumab redesigns are not analyzed. What structural or sequence features distinguish failures from successes? Understanding failure modes would strengthen the method's credibility and guide future improvements.

### Trivial

- The acronym "SDS" (Smoothed Discrete Sampling) is introduced on line 15 as a "new formalism," but is barely used after the introduction and the paper focuses entirely on "dWJS." It adds unnecessary terminology.

## Nice-to-Haves

- Clarify the metric hierarchy: DCS measures proximity to the reference distribution, while metrics like IntDiv and edit distance measure diversity. The paper correctly notes this tradeoff (line 247) but the presentation would benefit from an explicit statement that good performance requires both adequate DCS and adequate diversity — no single metric suffices. A Pareto-style analysis (DCS vs. IntDiv) would be informative.
- Provide full wall-clock sampling speed comparison with methodology, accounting for MCMC burn-in, number of samples, and hardware details, to substantiate the 43× speed claim.
- Report precision and recall of the 1D-CNN classifier used for binding prediction.

## Removed Points

These points were raised by reviewers but are flagged as removed after verification against the paper; treat them with caution:

- *DCS evaluation contradiction*: The paper does not discard DCS when it favors IgLM. The paper explicitly acknowledges IgLM's high DCS (line 247) and interprets it correctly — high DCS paired with low diversity means IgLM samples are very close to the reference but lack diversity. This is standard multi-metric evaluation. (HARD RULE: factually wrong criticism removed.)
- *Unfair baseline comparisons*: ESM2 is included transparently as a non-generative baseline with acknowledged limitations (line 247). GPT 3.5/4 are standard general-purpose LLM baselines. The EBM baseline on clean data is a meaningful ablation, not a straw opponent. (HARD RULE: factually wrong criticism removed.)
- *Overstated simplicity claim*: The paper's claim of "single hyperparameter choice: σ" refers to the hyperparameter specific to dWJS, not to standard Langevin MCMC parameters (δ, T) that any MCMC method requires. The claim is defensible in context. (Removed as not a genuine weakness.)
- *σ_c derivation mixing dimensionalities*: The paper transparently acknowledges the dimensionality issue (line 148) and provides a sparsity justification. The derivation is presented as intuition/guidance, not a rigorous proof. (Removed as not a genuine weakness.)
- *Fast-mixing MCMC as strength*: The strength finder's claim about fast-mixing is noted but no quantitative analysis exists to support it beyond visual inspection. Moved here because the evidence is insufficient to stand as a strength. (Strength/weakness conflict resolution.)
- *43× faster sampling as strength*: The claim is stated (line 247) but cannot be verified from the paper content as the profiling methodology (referenced Table 4) is absent. Moved here for lack of verifiability.

## Novel Insights

One interesting observation emerges from cross-referencing the two variants' performance. The energy-based variant achieves better Wasserstein distance (0.056 vs. 0.065) and perfect uniqueness (1.0), while the score-based variant achieves better diversity (IntDiv 65.1 vs. 55.3) and DCS (0.49 vs. 0.38). This suggests that the explicit EBM energy landscape on the smoothed manifold may constrain samples more tightly (producing more "typical" sequences at the cost of diversity), while score-based Langevin following the denoiser gradient explores more freely. This tradeoff — which the paper notes but does not analyze — implies that the choice between variants depends on the goal: tight distribution approximation (energy-based) versus exploration and diversity (score-based). Future work could probe whether interpolation between the two gradients yields better Pareto-optimal points.

## Suggestions

1. Commit to a primary method. The clearest framing is: the energy-based variant (EBM trained on noisy data + separate denoiser) is the core contribution; the score-based variant is the existing WJS baseline applied to discrete data. Rewrite the paper around this distinction.
2. The abstract should scope the binding claim: "70% of trastuzumab CDR H3 redesigns bound to HER2" rather than the current unqualified phrasing.
3. Add a limitations paragraph discussing failure modes (e.g., why did 7/277 sequences fail to express? What distinguishes the 30% non-binders?).
4. Add quantitative mixing diagnostics (autocorrelation time, effective sample size) for the single-chain mixing claim.
5. Report how many of the 277 wet-lab sequences were drawn from each variant, and ideally report expression rates per variant with sample sizes.
6. Provide the key implementation parameters (δ, T) in the main text; the community standard for this venue requires central hyperparameters to be in the paper body, not deferred to an appendix.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>