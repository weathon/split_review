Now I have thoroughly verified all the reviewer claims against the paper. Let me compose the final consolidated review.

## Summary

This paper introduces Multi-Source Diffusion Models (MSDM), a score-based generative model that learns the joint distribution of multiple musical sources (stems). By training a single model on the joint prior, the authors demonstrate that it can perform three distinct inference tasks: total generation (synthesizing full mixtures), partial generation/source imputation (generating some stems conditioned on others), and source separation (recovering individual stems from a mixture). A novel Dirac-likelihood inference procedure is proposed for the separation task, showing consistent gains over a Gaussian likelihood baseline. Experiments on Slakh2100 show competitive separation results (16.48 dB SI-SDR_I overall with correction, vs. 17.73 for the top supervised baseline) while simultaneously enabling generative tasks that no single prior model could perform.

## Strengths

- **First unified model for both music generation and source separation.** The paper demonstrates that a single model (MSDM) trained once on the joint source distribution can perform total generation, partial generation (source imputation), and source separation — tasks previously addressed by separate specialized models. This is well-supported: Table 1 shows MSDM's total generation quality (FAD 6.55) is comparable to a mixture-only model (FAD 6.67), while Table 3 shows it can also separate sources competitively.

- **Novel Dirac-likelihood inference yields consistent improvements.** The Dirac-based separation method (Algorithm 1) shows clear gains over the Gaussian likelihood used in prior work (NCSN-BASIS). Table 3 documents this across settings: e.g., ISDM Dirac + correction achieves 19.36 dB on Bass vs. 14.27 dB for ISDM Gaussian + correction, and overall SI-SDR_I rises from 14.58 to 17.27 dB. The same trend holds for MSDM (14.54 → 16.48 dB overall).

- **Introduction and evaluation of source imputation (partial generation).** The paper defines a new task — generating a subset of musical sources conditioned on fixed ones — and provides both subjective ratings (quality 6.3±2.7, density 6.1±2.6 out of 10) and objective sub-FAD metrics across all 14 combinations of four instrument classes, establishing baselines for a problem no prior model addressed.

## Weaknesses

### Fatal
None.

### Major

- **Insufficiently justified connection between the Dirac likelihood and the inference algorithm.** The paper defines the likelihood as a Dirac delta: $p(\mathbf{y}(t)\mid\mathbf{x}(t)) = \mathbb{1}_{\mathbf{y}(t)=\sum_n \mathbf{x}_n(t)}$, yet the algorithm (Algorithm 1, lines 161 and 167) sets $\mathbf{x}_N(t) = \mathbf{y}(0) - \sum_{n=1}^{N-1}\mathbf{x}_n(t)$, substituting the *clean* mixture $\mathbf{y}(0)$ where the likelihood formulation calls for the *noisy* mixture $\mathbf{y}(t)$. The paper states this "models the limiting case $\gamma(t)\to0$" of the Gaussian likelihood, but this does not explain why $\mathbf{y}(0)$ replaces $\mathbf{y}(t)$: at time $t>0$, the perturbation kernel means $\sum_n \mathbf{x}_n(t)$ is a noisy mixture, not the clean one. The algorithm works empirically (Table 3 confirms this), but the presented derivation does not bridge this gap. The authors could reframe the procedure as a constrained/projection-based sampler and drop the Dirac likelihood language, or provide a proper derivation showing how the algorithm follows from Bayes' rule under a stated approximation. As presented, the core methodological novelty rests on shaky theoretical ground.

- **Subjective evaluation lacks statistical rigor.** The listening tests (Tables 1 and 2) report mean ratings with standard deviations but provide no significance testing, no information about the number of subjects, and no inter-rater agreement metrics. The reported variances are large relative to the mean differences: e.g., MSDM quality 6.51±2.19 vs. mixture model 6.15±2.47 in Table 1, and partial generation quality 6.3±2.7 in Table 2. With standard deviations of ~2.2–2.7 on a 1–10 scale and mean differences of ~0.3–0.8, it is unclear whether the apparent advantages are statistically significant or merely noise. The paper claims MSDM's generation quality is "comparable" or better than the mixture model, but the evidence is too weak to distinguish meaningful improvement from chance variation. This is especially important because the generation results are central to establishing that learning the joint distribution does not sacrifice generative quality.

### Minor

- **Material gap to top supervised separation baseline under-discussed.** MSDM Dirac + correction achieves 16.48 dB overall SI-SDR_I vs. 17.73 dB for Demucs+Gibbs (Table 3) — a gap of ~1.25 dB. The paper accurately notes MSDM can also perform generation, but the discussion of this accuracy/flexibility trade-off is too brief. Given that Demucs+Gibbs is the state-of-the-art supervised separator on Slakh2100, the paper would benefit from a more direct discussion of how much separation accuracy is sacrificed for the generative capability.

- **Silent-chunk filtering threshold unspecified.** The paper states it filters "silent chunks and chunks consisting of only one source, given the poor performance of SI-SDR_I on such segments" (line 306) but does not specify the threshold for "silent" or report the fraction of data discarded. This affects the representativeness of the evaluation set and is needed for reproducibility.

### Trivial
None.

## Nice-to-Haves

- An analysis of why sub-FAD varies so widely across instrument combinations in Table 2 (0.11 for Guitar alone vs. 4.90 for BGP) would provide insight for future work and strengthen the contribution.
- A direct comparison of computational cost (ODE steps, wall-clock time) between MSDM separation and regression baselines would help contextualize the practical trade-offs.

## Removed Points

- **Hyperparameter values for Algorithm 1 (I, R, S_churn, noise schedule) not specified:** The paper references "Section \ref{sec:sampler}" for these details, which was likely part of a section removed by the parser. Per policy, this is not a valid criticism.
- **Model architecture details insufficient:** The paper states it follows the U-Net design of Moûsai. Architecture specifics were likely in a removed appendix section. The reference to an existing architecture is standard practice.
- **Claim about "no model can perform both tasks" needs qualification:** The harsh critic acknowledges this is "fine" and not actually a weakness. Removed.
- **Partial generation sub-FAD range not analyzed:** While worth discussing, this is a scope-expansion wishlist item, not a flaw in the presented work. Moved to Nice-to-Haves.
- **Strength about "rigorous evaluation combining subjective and objective metrics":** Conflicts with the verified weakness about subjective evaluation lacking statistical rigor. Removed per policy (when strength and weakness disagree, weakness wins).

## Novel Insights

None beyond the paper's own contributions. The reviews do not identify a genuinely novel interpretation that the authors themselves did not articulate.

## Suggestions

1. **Clarify the Dirac inference derivation.** Either provide a rigorous derivation showing how the algorithm follows from Bayes' rule with the Dirac likelihood approximation, or reframe the algorithm as a constrained/projection-based sampling procedure that does not rely on the Dirac likelihood language. The empirical evidence supports the method; the presentation needs to catch up.
2. **Add statistical significance testing** to the subjective evaluation (e.g., bootstrap confidence intervals, Mann–Whitney U tests) and report the number of subjects and inter-rater agreement. If the ratings are from a small number of subjects, acknowledge this as a limitation.
3. **Specify the silent-chunk filtering threshold** and report the fraction of discarded data in the separation evaluation.
4. **Discuss the separation/generation accuracy trade-off** more directly, quantifying how much separation performance is sacrificed for multi-task capability.
5. Report the computational cost of MSDM separation vs. regression baselines.

## Score and Decision

This paper makes a genuine contribution by demonstrating that a single score model of the joint source distribution can unify music generation and separation — a direction that is timely and valuable. The Dirac likelihood inference, while theoretically under-motivated, shows consistent empirical gains. The source imputation task is novel and well-defined.

The two major weaknesses — the incompletely justified Dirac inference and the statistically under-powered subjective evaluation — are both fixable with revisions. They do not invalidate the paper's core contribution (which is supported by multiple forms of evidence), but they do weaken the presentation of the key methodological novelty and the strength of the generation claims.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>