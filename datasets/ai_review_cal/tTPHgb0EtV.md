- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8
Now I have all the information to cross-check the reviews against the paper. Let me construct the final review.

## Summary

This paper identifies "harmful perturbation" (a gradient step on harmful data) as the root cause of alignment breakdown during fine-tuning, and proposes Booster — an alignment-stage regularizer that minimizes the reduction in harmful loss before/after a simulated harmful gradient step. The method requires three forward/backward passes per alignment step and is evaluated on Llama2-7B, Gemma2-9B, and Qwen2-7B across multiple attack ratios and fine-tuning datasets, consistently reducing harmful scores by large margins over baselines including Vaccine, RepNoise, and Lisa.

## Strengths

- **Clear empirical demonstration of the mechanism**: Section 3.2 and Figure 1 provide a controlled experiment showing that fine-tuning on pure harmful data steadily increases harmful score and reduces harmful loss, while fine-tuning on benign SST2 data does not. This directly motivates the paper's design choice to attenuate harmful perturbation.

- **Strong and consistent harmful-score reduction across diverse settings**: Tables 1–4 show that Booster achieves the lowest average harmful score among all baselines under every tested harmful ratio (p=0.05 to p=0.2), sample count (n=500 to n=2500), fine-tuning dataset, and model architecture. For example, in Table 1 Booster's average HS is 10.94% vs. SFT's 33.58% and the next-best Vaccine's 28.20%; in Table 4 the average HS across three models is 7.03% vs. SFT's 41.17%.

- **Statistical evidence directly validating the proposed mechanism**: Figure 3 plots harmful training/testing loss over fine-tuning steps, showing that Booster's aligned model starts with lower harmful loss and decreases it much more slowly than SFT. This directly confirms that the regularizer achieves its intended effect of attenuating the harmful loss reduction rate.

- **Practical one-time overhead justified**: Table 6 reports Booster's alignment stage takes 1.86h (vs. Vaccine's 1.06h and RepNoise's 2.69h) with 57.86 GB GPU memory. The paper correctly notes this is a one-time cost for an alignment-stage solution that serves many downstream fine-tuning requests, unlike fine-tuning-stage defenses that pay overhead per request.

- **Thorough hyperparameter analysis**: Tables 5–7 examine λ (regularizer intensity), α (inner step size), and the number of harmful samples, identifying optimal ranges (λ≈10–20, α≈0.01, ≥50 harmful samples) and showing predictable degradation when parameters are set too small or too large.

- **Compatibility with existing defenses**: Table 9 shows Vaccine+Booster further reduces average harmful score compared to either method alone, demonstrating integrability with prior alignment-stage solutions.

## Weaknesses

### Fatal
None.

### Major
None. The paper makes a clearly stated contribution with a well-motivated method, and the experimental design supports the core claims. The issues below are limitations worth addressing but do not threaten the validity of the central results.

### Minor

- **Same-distribution evaluation for harmful data**: The harmful data used during alignment, the harmful samples mixed into user fine-tuning data, and the test set used to compute harmful score all come from the BeaverTails distribution. The paper acknowledges they are different instances from the same distribution (line 141), but does not evaluate on out-of-distribution harmful data (e.g., different harm categories, adversarial reformatting, or a different harmful dataset). This limits the strength of generalization claims beyond BeaverTails-style harms.

- **AlpacaEval underperformance**: On the AlpacaEval fine-tuning task (Table 3), Booster's harmful score is 36.70, which is considerably worse than Lisa's 14.30 and only modestly better than SFT's 40.70. The paper reports this result but offers no analysis of why Booster struggles on this particular task. This is a notable failure case that should be discussed.

- **Default hyperparameters (λ, α) not explicitly stated in main experiments**: The setup section (line 141) states the default attack settings (p=0.1, n=1000) but does not specify the default values of λ and α used in Tables 1–4. Cross-referencing the hyperparameter tables (λ=5 → HS=8.30, α=0.1 → HS=8.30) with the main results (HS=8.30 at p=0.1) suggests λ=5 and α=0.1 are the defaults, but this is never stated. The paper should report these defaults explicitly and justify the choice.

- **No error bars or multiple-run statistics**: All reported results in Tables 1–4, 7–9 are single values without standard deviations, confidence intervals, or any measure of variance. While single runs are common for 7B+ models in this literature, the absence of any variance information makes it difficult to assess whether the performance gaps between methods are statistically reliable.

- **No ablation on the harmful answer requirement**: Booster's regularizer requires the harmful dataset to contain harmful *answers* (y'), not just harmful prompts. The paper acknowledges this assumption (line 66) and notes it is shared with RepNoise and TAR, but never tests whether the method would still work if refusal/safe answers were substituted for the harmful answers in the harmful dataset. Such an ablation would clarify whether the regularizer actually needs harmful responses or simply any data conditioned on harmful prompts.

### Trivial

- **Clean (p=0) harmful score is slightly elevated**: In Table 1, Booster's clean HS is 1.90 vs. SFT's 1.30 and Lisa's 0.90. While all three values are low, this suggests the regularizer introduces a small safety cost even when no attack occurs. The paper discusses clean FA but does not comment on clean HS.

## Nice-to-Haves

- Evaluate Booster on out-of-distribution harmful data (e.g., Anthropic's HH-RLHF harmful prompts, adversarial jailbreak prompts) to test whether the defense generalizes beyond the BeaverTails distribution.
- Run a small-scale experiment with full fine-tuning (non-LoRA) to verify the method applies beyond the LoRA setting.
- Ablate the effect of gradient normalization (step bound used in the inner step) to justify its inclusion.
- Re-run main experiments with 3 seeds and report means ± standard deviations for the headline tables.

## Removed Points

These points from the reviewers were not included in the main weaknesses; they are listed here for completeness but should not be weighed in the final evaluation:

1. **"Second-order information" labeling is imprecise** (Harsh Critic): The paper's characterization of ∇(w − α∇h/‖∇h‖) as containing second-order information is standard in meta-learning (MAML-style approximations). The term does involve the Hessian, and the paper correctly identifies this. Not a valid criticism.

2. **"Harmful response data requirement is unrealistic"**: The paper explicitly discusses this assumption (line 66) and notes it is shared with prior work (RepNoise) and available in existing open datasets (BeaverTails). The criticism is overstated, though the lack of ablation is a valid related point (kept above).

3. **"Hyperparameter sensitivity makes headline numbers hinge on careful tuning"**: Even with the inferred defaults (λ=5, α=0.1), Booster achieves HS=8.30 at p=0.1, compared to the next-best Lisa at 23.70. The improvements do not "hinge" on optimal tuning — they are large even with suboptimal defaults. The valid sub-issue about non-explicit reporting is kept above.

4. **"Novelty claim is overstated relative to Vaccine"**: The paper's "harmful perturbation" (a gradient step over harmful weights) is conceptually distinct from Vaccine's "harmful embedding drift" (drift of alignment-data embeddings). The paper correctly positions its contribution relative to prior work.

## Novel Insights

None beyond the paper's own contributions. Both reviews largely validate the paper's claims and suggest specific extensions rather than offering fundamentally new perspectives on the problem.

## Suggestions

1. **State default λ and α explicitly in the setup section** and briefly justify why those values were chosen (e.g., "we use λ=5 and α=0.1 as defaults because they provide robust defense without excessive tuning").
2. **Add a brief analysis or ablation for the AlpacaEval case** — why does Booster underperform Lisa on this task, and is this fixable?
3. **Include an ablation comparing harmful answers vs. refusal answers** in the harmful dataset to clarify whether the regularizer's effectiveness depends on the presence of harmful responses.
4. **Report main results with error bars** (at least 3 runs) or state that results are from a single fixed seed and acknowledge the limitation.
