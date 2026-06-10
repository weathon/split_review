Now I will produce the final consolidated review.

---

## Summary

This paper proposes Multi-Objective Control (MOC), a method for training a single LLM to generate outputs conditioned on user-specified preference vectors over multiple reward objectives (e.g., humor vs. helpfulness). The key technical idea is to integrate multi-objective optimization min-norm dynamic weighting into PPO, with a surrogate objective that avoids backpropagating through multiple reward models. The method is evaluated on Llama-2 7B using the HH-RLHF dataset for two-objective trade-offs (humor-helpful, harmless-helpful).

## Strengths

- **Novel algorithmic contribution.** Integrating min-norm dynamic weighting (a MOO technique) into PPO to train a single preference-conditioned LLM policy is a genuine and well-motivated idea. The surrogate that reduces the problem to a closed-form quadratic avoids the need for N+1 backpropagations per step, making the computation comparable to single-objective PPO — a practically relevant improvement over prior MOO approaches that are too expensive for LLM-scale training.

- **Clean toy proof-of-concept (Fishwood, Section 3.4).** The illustrative experiment on the fishwood domain where the ground-truth Pareto front is known provides a diagnostic sanity check. The visual comparison with Linear PPO demonstrates exactly why linear scalarization fails (one objective dominates) and confirms that MOC achieves both Pareto-front convergence and preference-vector alignment in a controlled setting before scaling to LLMs.

- **Substantial reported margins on hyper-volume.** In the humor-helpful setting, MOC reportedly achieves a hyper-volume of 12.32 vs. RiC's 6.769 (nearly 2×). The hyper-volume metric jointly captures convergence to the Pareto front and solution diversity, so this gap — if the evaluation holds up to scrutiny — is a meaningful indicator of improved solution quality.

- **Generalization to unseen preferences (Section 4.3).** Testing on four sets of preference vectors not seen during training, with both hyper-volume and local order rate metrics, demonstrates that the conditioning mechanism learns the concept of preference-following rather than memorizing specific vectors. This is a stronger validation than simply evaluating on trained preferences.

## Weaknesses

### Major

- **Reward models are completely unspecified, making the empirical evaluation uninterpretable.** The paper evaluates on reward-model scores for "humor," "helpfulness," and "harmlessness" (Section 4.1), but provides no information about how these reward models were obtained — their architecture, training data, training procedure, or validation accuracy. The HH-RLHF dataset used for policy training does not natively contain humor annotations, so it is entirely unclear where the humor reward model comes from. Since the reward models serve as *both* the optimization target during training *and* the evaluation metric, the reader cannot assess whether the reported results reflect meaningful behavioral control or reward hacking. This is the single most significant gap in the paper.

- **Theorem 1 and the surrogate derivation are not substantiated in the main text.** The paper states "Theorem 1. The upper bound of Equation (8) is" and presents Equation (10), but no proof or proof sketch is provided. More critically, the transition from the claimed bound (Equation 10, which includes a factor of ‖∇_θ π‖²) to the actual surrogate used in practice (Equation 12, which drops this term entirely) is not explained. The justification that the gradient norm "does not depend on c^(i)" is incomplete — the norm of the policy gradient is not constant across training steps, and removing it changes the optimization landscape. The paper claims MOC's surrogate preserves the Pareto improvement properties of the original min-norm approach, but this claim is not substantiated.

- **Nearly all training hyperparameters are missing, preventing reproducibility.** The experimental section reports the model (Llama-2 7B), dataset (HH-RLHF), LoRA rank (64), and GPU type (A6000). It does **not** report: learning rate, batch size, number of PPO steps or epochs, KL penalty coefficient β, clipping parameter ε, the threshold φ (defined in the method but never given a numerical value), the number of preference vectors M and their specific values, the number of training steps, evaluation samples per setting, or random seeds. A methods paper at a top venue should be reproducible from its description; this paper falls far short of that standard.

### Minor

- **Misleading claim: "does not rely on human preference data" (line 14).** The paper states this as an advantage, but the reward models used by MOC are trained on the HH-RLHF dataset, which is human preference data. What the paper likely means is that MOC does not require per-user preference data during training — a weaker and more standard claim. The phrasing as written is misleading.

- **Baseline comparison insufficiently documented.** The paper names MORLHF, Rewarded Soups, and RiC as baselines (Section 4.1), but does not specify: how many separate models Rewarded Soups trains per run, whether baselines were given comparable compute budgets, whether the same reward models were used for all methods, or whether RiC's rejection sampling hyperparameters were tuned. Without these details, the claim that MOC "significantly outperforms all baselines" cannot be fully evaluated.

- **No confidence intervals or error bars.** Given the stochasticity of both PPO training and LLM text sampling, the absence of any variance estimates for local order rate, hyper-volume, or entropy makes it impossible to assess whether reported differences are statistically meaningful. The generalization results state "no significant degradation" without reporting confidence intervals.

### Trivial

- The "sin" in Equation (12) is a parser-level artifact of "min"; this is a formatting issue, not an author error, but should be corrected in revision.

## Nice-to-Haves

- A small-scale human evaluation (even 100-200 comparisons with a few annotators) specifically validating that preference-conditioned outputs reflect the intended trade-offs (e.g., "does p=[1,0] look more humorous than p=[0,1]?") would substantially strengthen the personalization claim, especially since the paper's motivation is about human preferences.

- Specification of the reward models (architecture, training data, validation accuracy) is essential, not merely nice-to-have — but if added, it would resolve the most critical weakness.

- Reporting wall-clock training time for MOC vs. baselines would substantiate the computational efficiency claim.

## Removed Points

These points were raised by one or both reviewers but are removed here for the reasons given:

- **"The appendix might contain the proof" / "missing appendix proofs"**: The appendix was stripped by the parser; this is not an author omission.
- **"The sin/min typo is a weakness"**: Parser artifact from PDF rendering; the original submission uses "min."
- **Speculation about "reward hacking" without evidence**: The harsh critic suggested the results could reflect reward hacking, but this is speculative given what's on the page.
- **Generic concerns about "missing related work"**: I cannot verify whether a given paper is missing or present in the references without external sources.
- **"No limitations section"**: A presentation-level preference, not a methodological weakness.
- **"Table 1 is an image" / "figures are not readable"**: Parser limitation; the original PDF contains these.
- **Strength Finder's claim about Theorem 1 being a core strength**: Since the theorem is stated but not proven, and the surrogate's relationship to the claimed bound is not rigorously established, this is at best a potential strength rather than an established one; it is removed from the strengths list.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fully specify the reward models** — architecture, training data, training procedure, and validation metrics. Without this, the empirical evaluation is uninterpretable.
2. **Provide a proof sketch for Theorem 1 in the main text**, and explicitly discuss the approximation error introduced by dropping the ‖∇_θπ‖² term when moving from the upper bound (Equation 10) to the practical surrogate (Equation 12).
3. **Report all training hyperparameters**: learning rate, batch size, PPO epochs/steps, KL penalty β, clipping ε, threshold φ, number of preference vectors M, number of training steps, and random seeds.
4. **Add variance estimates** (confidence intervals or standard deviations over multiple seeds) to all reported metrics.
5. **Correct the misleading claim** on line 14: MOC does rely on human preference data (to train reward models), just not per-user preference data during policy training.
6. **Clarify baseline experimental setup**: how many models were trained per baseline method, whether compute was normalized, and whether hyperparameters were tuned per method.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>