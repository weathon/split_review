## Summary

This paper develops a rigorous high-dimensional statistical framework for data curation, deriving exact scaling laws for test error under label-agnostic and label-aware pruning strategies. Using random matrix theory (RMT), the authors characterize when keeping only a subset of data (via "keep hard" or "keep easy" strategies) outperforms full-dataset training. The central result—that strong generators favor "keep hard" while weak generators favor "keep easy"—is validated on ImageNet and used as a lens to reconcile seemingly contradictory findings in LLM mathematical reasoning (LIMO, s1 vs. standard scaling).

## Strengths

- **Exact analytical results with rigorous derivations.** Theorems 1–3 provide precise, non-asymptotic-in-quality formulae for test error via Stieltjes transforms of deformed Marchenko-Pastur laws. This is more than upper/lower bounds—the results are exact in the proportional scaling limit, building on well-established RMT machinery (Couillet & Liao, 2022). The framework unifies label-agnostic (Eq. 5) and label-aware (Eq. 6) pruning in a single model.

- **Clean, interpretable characterization of optimal strategy.** Theorem 2 establishes a clean binary: in the data-rich unregularized regime, strong generators (ρ→1) benefit from "keep hard," while weak generators (ρ<1) benefit from "keep easy." This qualitative insight is sharp, actionable, and directly tied to measurable geometric quantities (cosine alignments between generator, pruner, and ground-truth vectors).

- **Empirical validation confirms predicted crossover on ImageNet.** Figure 2 demonstrates the theoretically predicted crossover: a model trained on 160K images (weak generator) benefits from "keep easy," while a model trained on 1.2M images (strong generator) benefits from "keep hard." The crossover is not cherry-picked—it follows directly from the theory's prediction about generator quality.

- **Connection to model collapse is rigorous and useful.** The paper extends the same framework to multi-round pseudo-labeling (Figure 3), showing that principled curation prevents the degradation observed when training on all pseudo-labels. Figure 3 shows error rate stabilizing at ~30% vs. rising to ~52% without curation, a practically significant result.

- **Timely and well-motivated topic.** The "less is more" vs. "more is more" paradox (LIMO, s1, Sun et al. 2025) is a central open question in modern ML data practice. Providing a formal framework for this at ICLR is highly valuable to the community.

## Weaknesses

### Fatal
None.

### Major

- **Theoretical gap to practice is substantial.** The core theory assumes high-dimensional Gaussian features, linear predictors, squared loss, and binary classification. Real applications involve deep nonlinear networks, non-Gaussian structured data, cross-entropy or RL-based losses, and multi-class settings. The paper acknowledges this but does not bridge it. While this is standard in RMT-based ML theory, a reader looking for direct guidance on how to curate datasets for transformers or LLMs cannot apply Theorems 1–3 quantitatively—only qualitatively.

- **The LLM reasoning interpretation (Section 4.2) is qualitative and unfalsifiable as stated.** The framework is mapped to Tables 1–2 post-hoc: "for average performance, ρ is large; for hard performance, ρ is small." There is no formal way to estimate ρ for an LLM on AIME, no quantitative prediction of error rates, and the categorization of a model as "strong" or "weak generator" for a given task slice is determined by the outcome rather than an independent measure. This section reads more as narrative justification than scientific validation.

### Minor

- **Theorem 2 is limited to the joint limit φ→0 and λ→0.** The optimal strategy characterization only applies in the data-rich, unregularized regime. In finite-sample or regularized regimes, the paper provides Theorem 1 but does not give general optimality conditions. For the regime where "less is more" is most practically relevant (finite, large datasets), the boundaries of validity are not fully characterized in the main text.

- **The multi-round model collapse analysis (Figure 3) relies on empirical results on ImageNet but the theoretic treatment of iterative training is limited.** The paper applies Theorem 2's logic (weak generator → keep easy; but here it uses "keep hard") somewhat informally in this section. A formal stability theorem for iterative pseudo-labeling would strengthen this claim.

### Trivial

- The distributional derivative formulas for β and β̃ in Eq. (13) are deferred to the appendix without a sketch; a brief remark on their magnitude/behavior relative to the label-agnostic case would aid intuition.

## Nice-to-Haves

- A simulation verifying that the exact phase-transition curves predicted by Theorem 1 match empirical results quantitatively (not just qualitatively) for finite d/n, with labeled axes matching the theoretical predictions, would substantially strengthen trust in the exact nature of the result.
- Even a kernel-regime extension (infinite-width NTK) for nonlinear models, as mentioned in Future Directions, would partially bridge the gap to practice and is likely achievable with the existing RMT toolkit.

## Novel Insights

The paper's most genuinely novel contribution is the formal, exact characterization of the phase transition between "keep hard" and "keep easy" as a function of generator quality ρ, encoded through the geometric alignments (ρ, ρ*, ρ_g) between the generator, oracle, and ground truth. The insight that the alignment parameter τ = ρ_g/√(1−ρ*²) enters directly into the deformed Marchenko-Pastur law is non-trivial and would not emerge from naive intuition. Equally novel is the unification of label-agnostic and label-aware curation under a single analytical framework, and the formal demonstration that model collapse can be averted by shifting the curation criterion—a result that goes beyond the prior work of Feng et al. (2025) and Firdoussi et al. (2024), which analyzed only label-correction oracles without difficulty-based pruning.

## Suggestions

- Add a quantitative comparison between the exact test error curve predicted by Theorem 1 and empirical results on the synthetic Gaussian experiments, with explicit numbers for ρ, ρ*, ρ_g, and n/d.
- Provide even a brief semi-rigorous argument connecting the Gaussian linear theory to the nonlinear/ImageNet setting (e.g., via linearization near initialization or kernel approximation) to help practitioners understand when the theory's predictions can be trusted.
- Operationalize the LLM interpretation more concretely: propose a proxy measure for ρ (e.g., pass@1 of the base model on a held-out difficulty slice) that could be used to select the curation strategy ahead of time, rather than retrospectively.

## Score and Decision

The paper makes genuine, mathematically rigorous contributions to understanding data curation. The optimal strategy characterization (Theorem 2) is clean and important, the ImageNet validation confirms the predicted crossover, and the model collapse prevention result is practically significant. The primary limitation—the Gaussian linear model assumption—is real but is standard in this line of work and acknowledged clearly. The LLM interpretation is qualitative but serves as a plausibility check. Overall, this is a solid theoretical contribution on a timely and important problem, above the average quality of submissions.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>