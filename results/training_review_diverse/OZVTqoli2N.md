Now I have a thorough understanding of the paper and can verify all reviewer claims against the actual text. Let me compose the final review.

## Summary

This paper presents a second-order Taylor approximation framework to understand model compositionality in non-linear deep networks. It derives an upper bound (Jensen inequality) on the composed model's risk under the assumption of local optimality at pre-training weights, and proposes two incremental learning algorithms — ITA (individual training, regularizing each task vector toward pre-training) and IEL (ensemble training, regularizing the composed model directly). Both algorithms feature constant complexity w.r.t. number of tasks and are evaluated on 7 class-incremental benchmarks with comparisons to EWC, LwF, L2P, CODA, SEED, InfLoRA, APT, and TMC. The pool of learned task vectors also supports zero-shot specialization and unlearning.

## Strengths

- **Novel second-order Jensen inequality for non-linear networks (Eq. 3–4, §2.1).** The paper generalizes prior compositionality analyses that were limited to linearized models. The inequality ℓ̂_emp(θ_pool) ≤ Σ w_t ℓ̂_emp(θ_t) applies to *any* fine-tuning strategy (full, LoRA, IA³), which is a genuine theoretical advance over Tangent/linearization-based approaches.

- **Two dual algorithms with practical efficiency (§3).** ITA and IEL are derived from the same second-order formulation but offer complementary trade-offs (individual vs. ensemble training). Both maintain O(1) complexity w.r.t. number of tasks through cached/closed-form gradient computation, making them scalable to long task sequences.

- **Closed-form gradient for the ensemble regularizer (§2.3, Eq. 7–8).** Theorem 1 and the subsequent derivation yield regularization gradients computable analytically without backprop-through-time, a concrete technical contribution that makes IEL lightweight.

- **Comprehensive evaluation on 7 benchmarks (§5).** The paper evaluates on diverse class-incremental settings (ImageNet, CIFAR, CUB, Caltech, MIT-67, RESISC, CropDiseases) with multiple fine-tuning strategies (FFT, LoRA, IA³), comparing against a wide range of existing methods.

- **Demonstration of specialization and unlearning beyond standard metrics (§5, Table 3).** The paper shows that learned task vectors support zero-shot editing (specializing to a subset of tasks, unlearning specific tasks) via simple addition/subtraction, with ITA achieving larger target/control accuracy gaps than TMC.

## Weaknesses

### Fatal
None.

### Major

- **Central theoretical assumption unverified.** The entire theoretical chain (convex quadratic approximation, Jensen inequality, Eq. 4) hinges on θ_0 being a local minimum of the empirical risk across all tasks. The paper's pre-consolidation (linear probing) fine-tunes only the classification head — it does not empirically verify that the resulting θ_0 (backbone + LP head) is a stationary point of the combined-task risk. No gradient norms or Hessian eigenvalue checks are reported. While the paper discusses this in limitations (§6), the gap between assumption and verification is significant enough that the theoretical guarantees (convexity, the bound) rest on unconfirmed ground. The paper's footnote that the condition "can be easily satisfied with over-parameterized deep learning models" is an assertion, not evidence. This weakens, but does not invalidate, the contribution — the algorithms work empirically regardless — and is the most serious issue identified.

### Minor

- **Inconsistent claim about domain shift (§5).** The paper states that ITA/IEL "outperform existing approaches on all datasets except MIT-67 and CropDisease," then immediately says "Considering the good results on SplitRESISC and SplitCropDiseases... [our methods] do not seem affected by large domain shifts." Since CropDisease is one of the two datasets where the methods did *not* outperform baselines, the claim of robustness to domain shift is undercut by the paper's own results. The term "good results" is vague — the paper should clarify what constitutes "good" when SOTA performance was not achieved.

- **O(1) complexity claim for IEL requires clearer exposition (§3).** The regularization term in Eq. 15 involves Σ_{t' < t} τ_t^T Î_θ₀ τ_{t'}. The paper asserts closed-form gradients with constant complexity w.r.t. T, which is achievable by caching accumulated inner products, but this important design detail is deferred to a supplementary section not visible in the main text. Since this claim is central to the method's scalability, a brief explanation in the main text would significantly help readers.

- **Link between theory (quadratic approx) and practice (exact loss) could be more directly validated.** The paper acknowledges (§3) that the algorithms minimize the exact loss ℓ(θ) while the theory uses ℓ̂(θ), which is standard practice. Figure 1 shows that regularization reduces both the exact composed loss ℓ_emp(θ_pool) and the quadratic upper bound Σ w_t ℓ̂_emp(θ_t). However, the paper does not directly verify that the *exact Jensen inequality* (ℓ_emp(θ_pool) ≤ Σ w_t ℓ_emp(θ_t)) holds — it only shows ℓ_emp(θ_pool) ≤ Σ w_t ℓ̂_emp(θ_t). While this is a reasonable sanity check, explicitly comparing ℓ_emp(θ_pool) to Σ w_t ℓ_emp(θ_t) would strengthen the bridge between theory and practice.

- **Hyperparameter sensitivity not reported.** The paper selects α and β via grid search but provides no analysis of how performance varies with these values. Without sensitivity results, it is difficult for practitioners to gauge how robust the methods are to hyperparameter choices.

- **Analysis of why IES (ensemble) fails at specialization is underdeveloped.** The paper notes that IEL "struggles when any of its members are removed" and calls this "sobering," but does not analyze why — e.g., whether IEL task vectors drift farther from θ_0 than ITA vectors, which would directly connect to the paper's central thesis.

### Trivial
None.

## Nice-to-Haves

- **Comparison with additional merging methods.** Adapting approaches like Ties-Merging or DARE to the incremental setting could further strengthen the claim that the proposed algorithms are better suited for incremental composition.
- **Wall-clock time comparison.** The paper claims constant complexity for closed-form gradients but does not demonstrate the computational benefit empirically (e.g., training time vs. number of tasks).
- **Statistical reporting in main table.** While standard deviations are in the appendix, including them in the main table (at least for the proposed methods) would improve readability.
- **Analysis of task vector geometry.** Computing pairwise distances in the Fisher metric for ITA vs. IEL vs. plain fine-tuning would provide mechanistic evidence for why the regularization works.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *"The description of IA³ as a task vector is stated without derivation"* — The paper provides the explicit formula (τ_t = θ_0 ⊙ ((l-𝟙_h) ⊗ 𝟙_h)) on line 159, which is a complete derivation.
- *"The main results table is not shown here"* — This is a parser artifact; the paper uses \input{tables/main_results_cil}, which exists in the original submission.
- *"Standard deviations should at least be mentioned in a footnote in the table"* — The paper explicitly states on line 182 that standard deviations are in the supplementary; this is a presentation choice, not an omission.
- *"The Fisher accumulation glosses over the fact that the Fisher is estimated on the pre-training weights while the actual loss evolves during fine-tuning"* — The paper acknowledges this approximation explicitly in the limitations section (§6: "the approximation may become inaccurate as parameters drift").
- *"Criticism that the Jensen inequality in Eq. 4 pertains to the quadratic approximation rather than the exact loss"* — The paper clearly states this distinction (line 69: "our result pertains to the *second-order* approximation") and Figure 1 shows the exact composed loss improving, which already bridges theory and practice.
- *"Missing comparison with Ties-Merging or DARE as baselines"* — The paper's baseline set (EWC, LwF, DPP, L2P, CODA, SEED, InfLoRA, APT, TMC) is already comprehensive. Adding more merging baselines is a nice-to-have, not a weakness.
- *"The local minimum assumption note about over-parameterized models is hand-wavy"* — While the assumption lacks verification, this criticism is already captured in the Major weakness above. Removing the redundant version.

## Novel Insights

None beyond the paper's own contributions. The reviewer insights are primarily requests for additional validation rather than novel observations about the work.

## Suggestions

1. **Empirically verify the local-minimum assumption.** Report the gradient norm of the empirical risk at θ_0 (after LP) for a few tasks. Even a small gradient norm would substantially validate the theory; a large one would force a refinement of the argument but would not invalidate the empirical results.
2. **Clarify the domain shift claim.** Distinguish between "good results" (competitive accuracy) and "outperforming baselines" when discussing CropDisease, or remove the ambiguous phrasing.
3. **Add a brief explanation of the O(1) complexity for IEL's regularization gradient** in the main text — specifically, that cached sums of Î_θ₀ τ_{t'} enable the sum over previous tasks to be computed in O(1) per gradient step.
4. **Include a hyperparameter sensitivity plot** (e.g., accuracy vs. α for one dataset) to demonstrate robustness.
5. **Analyze why IEL fails at specialization** by measuring whether its task vectors drift farther from θ_0 than ITA's, providing mechanistic insight consistent with the paper's thesis.

## Score and Decision

The paper makes a credible theoretical contribution by extending compositionality analysis to non-linear networks, proposes two practical and well-motivated algorithms with useful efficiency properties, and evaluates them thoroughly. The main weakness — an unverified central assumption — is significant but does not invalidate the contribution; the algorithms work empirically, and the assumption is a common limitation in second-order methods that the paper acknowledges. The work is original, addresses an important question, and provides value to the research community. With revisions addressing the key concern (verifying or softening the assumption), the paper would be a solid contribution.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>