Now I have all the information I need. Let me compile the final consolidated review.

---

## Summary

This paper introduces Dynamic Noise Preference Optimization (DNPO), a framework for iterative LLM self-improvement via synthetic data. DNPO has two components: (1) Dynamic Sample Labeling (DSL), which replaces the rigid assumption that human-annotated data is always preferable with GPT-4o-mini-based quality evaluation to form preference pairs, and (2) Noise Preference Optimization (NPO), which injects trainable noise into the reference model's logits for negative samples to prevent the stagnation that occurs when the margin between positive and negative samples becomes too large. Experiments on Zephyr-7B (Mistral-7B) show that DNPO improves over the SPIN baseline across three iterations, with average benchmark gains of 2.6% and a 29.4 percentage-point win-rate gap against SPIN in GPT-4o-mini evaluations.

## Strengths

1. **Identifies two genuine, specific problems in iterative self-improvement.** The paper offers concrete evidence for both: (a) ~30% of model-generated responses are equal or better than human annotations (Figure 1, verified on the paper's setup), and (b) the model's log-probability distributions stagnate across SPIN iterations (Figure 2). These are well-motivated, measurable issues.

2. **Ablation design cleanly decomposes the contribution of each component.** Figure 8 shows that NPO provides the largest gain in iteration 1 (when stagnation is most acute) and DSL provides the largest gain in iteration 2 (when the model generates high-quality data that would otherwise be mislabeled). This division of labor is exactly what the paper claims, lending credibility to both mechanisms.

3. **Consistent improvement over SPIN across iterations on both benchmarks and GPT-4o-mini evaluations.** DNPO's average benchmark score rises from ~0.586 to 0.612 across three iterations while SPIN stalls (Figure 5). The win-rate analysis (Figure 7) shows DNPO achieving 57.51% vs. 28.07% in iteration 3, a large gap that independently validates that DNPO produces preferred outputs.

4. **The noise mechanism is designed to not affect inference.** The paper deliberately adds noise only to the reference model's logits for negative samples (Section 4.3, Obj. 4 analysis), so the trained model at inference time is identical in architecture to the base model. This is a practical and principled design choice.

## Weaknesses

### Major

1. **The core training objective is presented in a confused and under-specified manner, and the paper contradicts itself on how training proceeds.**

   There are two distinct problems here:

   *First, Eq. 10 (lines 160–166) uses a prime (′) on the first term's denominator (`p_{θ_t,θ_σ}^{noise}(y_i^-|x_i)'`) that is absent in the second term, but this prime is never defined anywhere in the paper.* Without knowing whether the prime denotes a stop-gradient, a different forward pass, frozen noise parameters, or something else, the objective is ambiguous. The derivative of the two-term loss with respect to θ and θ_σ depends entirely on what the prime means — and this is the paper's core algorithmic contribution.

   *Second, the paper describes two incompatible training procedures.* Figure 3's caption says: "the model is frozen and the noise component is trained to minimize the margin... In the following step, the noise is frozen while optimizing the model to maximize this margin" — a clearly **alternating** procedure. But the text around Eq. 10 says "we update both θ and θ_σ in a single iteration by minimizing" — a **simultaneous** procedure. These are different algorithms and produce different gradients. The paper does not resolve the discrepancy.

   The specific claim by the harsh reviewer that the two terms in Eq. 10 are "identical" and would cancel is **incorrect** — the prime differentiates them — but the underlying concern about clarity is valid and serious. The derivation from Eq. 8 (bi-level optimization) through Eq. 9 (min-max) to Eq. 10 (single minimization) skips crucial details about how the approximation is justified. This needs major revision.

2. **No statistical significance or variance reporting on any experimental result.**

   All results in Tables 1, Figures 5–8 are reported from what appears to be a single run. The improvements are modest on average (2.6% over SPIN), and on several individual benchmarks the difference is 1–2 percentage points. Without error bars, confidence intervals, or multiple seeds, the reader cannot determine whether the reported gains reflect genuine improvement or random variation. The paper claims "consistent improvement over iterations," but this claim requires at minimum 3 independent runs with standard deviations to be credible. This is a standard expectation for empirical ML papers.

3. **Limited baseline comparison.** The paper compares only against SPIN and a basic SFT model. While SPIN is the most directly relevant prior work, the paper frames its contribution broadly ("addresses key challenges in LLM self-improvement"). Without comparison to at least one other self-improvement method of comparable complexity — e.g., iterative DPO with an explicit reward model, or self-rewarding LMs — it is difficult to assess whether DNPO's advantage is specific to the SPIN comparison or reflects a general capability.

### Minor

4. **The "promoting method" used with the evaluation model is never defined.** Section 4.2 says "using a more powerful evaluation model M_eval with promoting method" (line 97), but "promoting method" is never explained. If this is a specific prompting technique (e.g., chain-of-thought scoring, few-shot examples, rubric-based evaluation), it must be described for reproducibility.

5. **Evaluation prompts for GPT-4o-mini are not specified.** The paper uses GPT-4o-mini for both DSL labeling (Section 4.2) and for generating the scores in Figure 6, but the exact prompt or scoring rubric is omitted. This is a reproducibility gap — different prompts can produce substantially different scores.

6. **Dataset selection criteria for the 20k UltraChat subset are not stated.** The paper trains on "a 20k sample from the UltraChat dataset" (Section 5.1) without explaining whether this is a random subset, stratified, or curated. Selection bias matters for reproducibility.

7. **Noise generator overhead is not discussed.** The noise generator is a 4096×32000 linear layer (~131M parameters for a 7B model, ~1.9% of model size). The paper does not discuss training/inference overhead, memory cost, or whether a lower-rank approximation would suffice.

### Trivial

8. **Figure 10 axes are unlabeled.** The caption describes "log probability distributions" but the axes are not labeled, making the distributions harder to interpret than necessary.

## Nice-to-Haves

- **Analysis of learned noise patterns.** The paper shows that noise loss decreases (Figure 9) but does not examine what the learned σ_i values look like. Are they large for certain input types? Do they correlate with model uncertainty? Visualizing or analyzing the learned variances would strengthen the claim that the noise is learning something principled.
  
- **Sensitivity of DSL to the choice of evaluator.** The paper uses GPT-4o-mini exclusively. Testing GPT-4 or Claude would clarify whether the method depends on a specific evaluator's biases.

- **Comparison with Self-Rewarding LM (Yuan et al., 2024)** or iterative DPO with a reward model would strengthen the claim that DNPO broadly outperforms self-improvement methods, not just SPIN.

- **The claim that "synthetic data can outperform human-annotated data in about 30% of cases"** is correctly qualified to the paper's setup (Zephyr-7B, UltraChat), but could benefit from an explicit caveat that this result may not generalize to other models or datasets.

## Removed Points

These points have been removed from the main review with justification:

- **"The two sums in Equation 10 are identical and would cancel out"** — Factually incorrect. The first term has a prime (′) on the noise probability that the second term lacks, so they are not identical. However, the notation is unclear (see Major weakness 1), which is the valid concern beneath this criticism.
  
- **"The claim that 'both SFT and DNPO are trained on the same dataset' contradicts typical self-play setups"** — Overly pedantic. The paper's meaning is clear: the *prompts* come from the same dataset; DNPO uses self-generated responses constructed from those prompts. No actual contradiction.

- **Missing related works** — Per policy, I cannot confirm which works are missing without external knowledge.

- **Formatting/typo criticisms** — Parser artifacts, not author errors.

## Novel Insights

Beyond the paper's own contributions, the most striking observation from the reviews is that the ablation study (Figure 8) reveals a **phase-dependent benefit**: NPO matters most in early iterations (when the model is far from convergence and the stagnation problem is acute), while DSL matters most in later iterations (when the model generates high-quality data that would otherwise be mislabeled as negative). This temporal decomposition is more granular than the paper's headline claims and suggests that self-improvement methods may need different mechanisms at different training stages — a potentially general design principle.

## Suggestions

1. **Fix Eq. 10.** Define the prime notation explicitly, or if it denotes a stop-gradient / separate forward pass, state this. Resolve the contradiction between the alternating procedure (Figure 3) and the simultaneous minimization (Eq. 10) — which one is actually implemented, and why?

2. **Run experiments with at least 3 seeds** and report means with standard deviations (or confidence intervals). This is essential given the modest average improvement and the paper's central claim of "consistent improvement."

3. **Add at least one more baseline** of comparable complexity. The most informative comparison would be SPIN + DSL without NPO, which would directly test whether NPO provides benefit beyond relabeling alone (the existing ablation partially does this, but a full comparison with an established method would be stronger).

4. **Specify the evaluation prompts and scoring method** used with GPT-4o-mini, and define what "promoting method" means in Section 4.2.

5. **Describe how the 20k UltraChat subset was selected** (random, stratified, etc.).

## Score and Decision

This paper identifies real problems in LLM self-improvement and proposes a two-component solution that is supported by a well-designed ablation study and consistent experimental signals. However, the paper has two significant weaknesses that prevent acceptance in its current form: (1) the core training objective (Eq. 10) uses unexplained notation and contradicts the described training procedure, making the central algorithmic contribution ambiguous, and (2) all experimental results come from a single run without any measure of variance, which is insufficient to support claims of "consistent improvement" given the modest effect sizes. These issues are fixable with major revision, and the underlying ideas have merit.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>