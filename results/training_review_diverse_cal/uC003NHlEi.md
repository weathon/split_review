I now have sufficient information from the paper to verify all claims. Let me compose the final consolidated review.

## Summary

This paper introduces IBO-HPC, an interactive Bayesian optimization method that uses probabilistic circuits (PCs) — specifically mixed sum-product networks (MSPNs) — as surrogate models to incorporate user knowledge during hyperparameter optimization. The key innovation is that PCs enable exact conditional inference and sampling from a joint distribution over hyperparameters and scores, allowing users to provide feedback (as point values or distributions) at any point during optimization without restarting the process. The paper provides formal definitions of interactive policies, theoretical properties, and an extensive empirical evaluation across NAS and HPO benchmarks.

## Strengths

- **Tractable conditional sampling enables precise reflection of user beliefs**: Unlike weighting-based approaches (πBO, BOPrO) that reshape acquisition functions, IBO-HPC directly conditions its PC surrogate on user-provided values or distributions via exact inference. Figure 1 (Right) demonstrates empirically that IBO-HPC's selected configurations match the user prior distribution, while competitors deviate substantially. This is a clear technical advantage.

- **Flexible anytime interaction without ex-ante constraints**: The method supports both point-value and distributional feedback at any iteration (not just before optimization begins), and handles partial feedback over arbitrary subsets of hyperparameters. This generality surpasses prior interactive HPO methods, which require full prior specification ex ante and often impose constraints on the acquisition function.

- **Recovery mechanism from misleading user feedback**: The Bernoulli-decay mechanism (Eq. 3) gradually reduces the influence of user knowledge over time. Figure 3 shows IBO-HPC reliably recovers from misleading interactions across 4/5 benchmarks, catching up with or outperforming standard HPO methods — something πBO and BOPrO's static priors cannot do.

- **Competitive performance without user interaction**: When no user knowledge is provided, IBO-HPC matches or outperforms strong baselines (SMAC, local search, RF-BO) on 4/5 tasks (Figure 2), demonstrating the effectiveness of HPCs as surrogates and the sampling-based selection policy for standard (non-interactive) HPO.

- **Significant wall-clock speedup from beneficial interactions**: Figure 4(b) reports a median speedup of 2× to 10× in achieving target solution quality when beneficial user knowledge is provided, demonstrating practical resource savings.

- **Extensive evaluation across diverse benchmarks**: Experiments cover four benchmarks (NAS-Bench-101/201, JAHS, HPO-B) spanning image classification, tabular data, neural architecture search, and tree-based models, each with 500 random seeds. This thoroughness strengthens the generality of the claims.

## Weaknesses

### Major

None.

### Minor

- **Tension between the feedback-adhering definition and the Bernoulli-decay mechanism**: Definition 3 requires that "the distribution over Ĥ induced by the selection policy equals the prior q(Ĥ) in the next iteration." However, the algorithm (Line 8–9) only uses user knowledge with probability ρ via a Bernoulli draw; when the draw fails, the knowledge is ignored entirely. The paper describes the algorithm as satisfying Def. 3 (Proposition 1), but the main text does not reconcile this tension. Either the definition should be weakened to "conditionally feedback-adhering" (dependent on the Bernoulli succeeding), or the algorithm should guarantee the knowledge is used in the first iteration. The proof in Appendix B.1 may address this, but the main text is ambiguous, which risks overclaiming.

- **Convergence guarantee (Proposition 3) rests on assumptions disconnected from practice**: The proposition assumes a non-noisy, differentiable, Lipschitz-continuous, convex function on a ball in ℝ^d, with a PC whose Gaussian leaves locally maximize likelihood. These assumptions do not match the paper's intended domain (mixed categorical/continuous search spaces, non-convex objectives, noisy evaluations). The resulting bound is expressed in terms of erf functions and mixture parameters whose practical meaning is unclear. This proposition does not materially strengthen the paper's contributions; it could be removed or replaced with a more grounded discussion of why PCs are sensible surrogates for HPO.

- **Experimental "user knowledge" is derived from oracle-based priors, limiting external validity**: The paper constructs priors by sampling 10k configurations and taking the best/worst, with a 1000× likelihood ratio for those values. While the paper justifies this choice as necessary for fair comparison against πBO/BOPrO (which require strong priors to work well), the setup does not demonstrate how IBO-HPC performs with the kind of partial, uncertain, or noisy feedback a human would actually provide. The speedup claims (2–10×) are relative to the same algorithm without knowledge; they do not quantify the benefit of IBO-HPC's specific mechanism relative to cheaper interaction strategies.

- **No guidance on key hyperparameters (ρ, γ, N, B, L, J) or sensitivity analysis**: The decay mechanism (ρ, γ) is central to robustness, and N and B affect the approximation quality of Eq. 2. The paper notes B=1 "works surprisingly well" but provides no ablation, default values, or guidance for practitioners on how to set these parameters. Some of these may be addressed in the appendix, but the main text should include at least a discussion or recommendation.

- **"Global optimizer" claim (Proposition 2) is stated too strongly without contextualization**: The claim that IBO-HPC "minimizes simple regret" is stated as a one-line proposition with a proof deferred to the appendix. Without assumptions in the main text, "global optimizer" is an overly strong characterization for a sampling-based method with a decaying reliance on user input.

### Trivial

- The paper would benefit from brief summaries of how the PC structure (number of components, depth) is chosen and how J (initial sample size) affects early performance, even if only to refer to appendix details.

## Nice-to-Haves

- A runtime comparison against the most directly related interactive methods (πBO, BOPrO) for the optimization loop itself would be informative, since IBO-HPC involves retraining a PC every L iterations and conditional sampling.
- A concrete illustrative example (perhaps in the introduction) of a realistic user interaction — what a practitioner might say and how IBO-HPC would handle it — would ground the "interactive" framing beyond the oracle-prior experiments.
- An ablation on N and B values (e.g., N=1,5,10, B=1,5,10) on one benchmark would help readers understand sensitivity.

## Removed Points

- **"Formal definitions are used only to state Proposition 1 and do not drive the algorithm design"** — Removed. The definitions serve to formalize the notion of interactivity and ground the contribution; they do not need to "drive" the algorithm design to be valuable. This is a matter of presentation taste, not a weakness.

- **"Missing related work on human-in-the-loop optimization"** — Removed per instructions: I cannot verify existence of missing references.

- **"Proposition 3 proof is in appendix"** — Removed per instructions: parser strips appendix sections from all papers; they exist in the original submission.

- **"Strength: Theoretical convergence analysis (Proposition 3)"** — Removed because this strength conflicts with a verified weakness (Proposition 3 is disconnected from practice). Per rules, when strength and weakness disagree, weakness wins.

## Novel Insights

The reviews surface an interesting tension that goes beyond the paper's own framing: the method's key advantage — exact conditional inference yielding precise reflection of user beliefs — is simultaneously its limitation in that the formal guarantee only holds when the Bernoulli mechanism activates the knowledge. The paper presents the Bernoulli-decay as a robustness feature, but it actually creates a subtle disconnect between the theoretical definition of "feedback adhering" and the practical algorithm. This suggests a deeper design question for interactive HPO: whether it is better to (a) guarantee exact reflection of user beliefs but risk overcommitment to bad input, or (b) introduce stochasticity/decay to trade off fidelity for robustness. IBO-HPC chooses (b) operationally while claiming (a) formally, and resolving this alignment would strengthen both the paper and the broader research direction.

## Suggestions

- **Clarify the feedback-adhering property**: Acknowledge in the main text that the policy is feedback-adhering *conditional on the Bernoulli draw succeeding* (i.e., with probability ρ). Alternatively, modify the algorithm to guarantee use of knowledge when provided by removing the Bernoulli for the first iteration after provision.
- **Remove or substantially rework Proposition 3**: Either drop it entirely (the paper does not lose credibility without it) or replace it with a discussion of why PCs are sensible surrogates for HPO that connects to the actual (mixed, non-convex) setting.
- **Add hyperparameter guidance**: State the default values of ρ, γ, N, B, L, J used in experiments and add a brief sensitivity analysis (even a paragraph) for ρ and γ, which control the crucial recovery mechanism.
- **Soften the framing of speedup claims**: Clarify that the 2–10× speedups are relative to the same algorithm without user knowledge using oracle-derived priors, and discuss what scenarios these results generalize to.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>