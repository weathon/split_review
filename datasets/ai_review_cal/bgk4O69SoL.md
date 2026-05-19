- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 5, 6, 6
Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual content. Let me synthesize the final review.

---

## Summary

This paper introduces Latent Preference Coding (LPC), a framework that models the multifaceted nature of human preferences through discrete latent codes learned via variational inference. LPC integrates with offline alignment algorithms (DPO, SimPO, IPO) by conditioning the policy on a latent variable drawn from a learned prior (inference) or posterior (training), where each latent code is intended to capture an underlying preference factor. The framework automatically discovers these factors from holistic preference data without requiring pre-defined sub-rewards or hand-crafted combination weights. Experiments across three base LLMs and three alignment algorithms show consistent improvements over vanilla methods on downstream benchmarks, preference accuracy, and AlpacaEval win rates.

## Strengths

- **Consistent improvement across diverse configurations.** Table 1 shows LPC improves performance over vanilla baselines in 33 out of 36 evaluated configurations (3 base models × 3 algorithms × 4 benchmarks), spanning Mistral-7B, Llama3-8B, and Llama3-8B-Instruct. This breadth demonstrates that the benefit is not idiosyncratic to one setup.

- **Generality to multiple offline alignment objectives.** The paper derives explicit LPC variants for DPO (Eq. 7), SimPO (Eq. 12), and IPO (Eq. 13). Each integrated version improves over its vanilla counterpart, showing the framework is not tied to a single algorithm. The authors honestly acknowledge that the IPO extension "sacrifices some mathematical rigor" (line 159) but works in practice.

- **Empirical evidence that latent codes capture meaningful structure.** The T-SNE visualization (Figure 2, Right) shows instances from different data sources cluster when projected from the latent representation. The label-flipping experiment (Figure 2, Bottom Left) demonstrates that LPC maintains a larger advantage over vanilla DPO when 50% of preference labels are deliberately corrupted, suggesting the discrete codes help disentangle conflicting preference signals.

- **Systematic codebook size analysis.** Section 4.3 sweeps over codebook sizes {8, 16, 32, 64, 128, 256}, showing a clear peak in preference accuracy at 32–64 codes. This provides practical guidance and shows the model is not trivially sensitive to this hyperparameter.

- **Preference accuracy and independent judge evaluation.** Table 2 shows LPC improves held-out preference accuracy in 8/9 configurations. Table 3 reports AlpacaEval 2 win rates (judged by GPT-4) for Llama3-8B-Instruct, where LPC improves both length-controlled and raw win rates over all three base algorithms, corroborating downstream results with an independent evaluation.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison against multi-objective/multi-reward baselines.** Section 2.3 reviews multi-objective alignment methods (reward model combination, policy model combination, combination-aware learning) and positions LPC as an alternative that "automatically infer[s] both the implicit factors and their relative importance from holistic feedback data, without relying on pre-defined objective weights or explicit reward models." Yet the experimental evaluation (Section 4) compares only against single-objective baselines (vanilla DPO, SimPO, IPO) and the raw base model. No method that *does* handle multiple objectives is tested — e.g., linearly combining two reward models trained on separate aspects of UltraFeedback, or the conditioned-policy approach from Dong et al. (2023). This gap means the paper's central framing claim — that LPC's *unsupervised* discovery of factors offers advantages over explicit multi-objective approaches — is not directly supported by the evidence. The experiments convincingly show LPC improves over single-objective methods, but they do not isolate *why* (the latent structure vs. added model capacity, the conditioning mechanism, or the variational training). This does not invalidate the paper's contribution but substantially narrows what the evidence can claim.

### Minor

- **Unexplained theoretical inconsistency between Eq. 6 and Eq. 7.** In Eq. 6 (line 97), the derivation writes $\pi_{\mathrm{ref}}(y_w|x,z)$ — the reference model conditioned on the latent variable $z$. But in Eq. 7 (line 105), the actual training loss uses $\pi_{\mathrm{ref}}(y_w|x)$ without $z$ conditioning. The paper does not discuss this change or its theoretical implications (e.g., what the resulting implicit reward $r(x,y,z) = \beta\log(\pi_\theta(y|x,z)/\pi_{\mathrm{ref}}(y|x))$ means, how the partition function behaves, or why the KL penalty against the unconditional reference is the correct design). This choice is likely mathematically consistent, but the paper presents the derivation as cleaner than it is.

- **Small effect sizes and no statistical significance reporting.** In Table 1, several improvements are within 0.5 absolute points (e.g., ARC-c: 50.43→50.66, GSM8K: 62.24→62.28 for Llama3-8B with DPO). No confidence intervals, standard errors, or statistical tests are reported. While the overall trend across 33/36 comparisons is positive, it is unclear which individual improvements reflect genuine gains vs. evaluation noise. The paper would benefit from at least stating whether greedy decoding was used (which would reduce variance) and providing some measure of dispersion.

- **Non-standard negative sampling for preference pairs.** The paper constructs $y_l$ by randomly sampling from the remaining completions (line 176), rather than using a more informative strategy (e.g., selecting the lowest-scored completion). Random $y_l$ may produce many pairs where the preference signal is weak (the random completion could be nearly as good as $y_w$), which could dilute the training signal. The flipping experiment partially mitigates concerns about noise robustness, but the main results should be interpreted with this design choice in mind.

- **Limited demonstration of latent code interpretability.** The paper motivates discrete latent codes as "more interpretable" (Section 2.1) but provides no qualitative analysis of what individual codes represent. The T-SNE visualization (Figure 2, Right) shows clustering by data source, which could reflect surface-level domain differences (writing style, topic) rather than meaningful preference factors (e.g., helpfulness vs. safety vs. conciseness). No human annotation or code-level analysis is provided to substantiate the interpretability claim.

### Trivial
None.

## Nice-to-Haves

- **Ablation of $\lambda$ (KL weight) and the $g$ scheduling strategy.** The paper searches $\lambda$ over {0.01, 0.05, 0.1} and sets $g$ to linearly increase from 0 to 1, but neither is ablated. Understanding sensitivity to these design choices would help practitioners and strengthen the method's justification.

- **Qualitative analysis of individual latent codes.** Even a small study — e.g., top-5 prompts activating each code, with human labeling of the common theme — would substantially strengthen the interpretability claim that motivates discrete codes over continuous alternatives.

- **Empirical comparison with the concurrent continuous latent variable approach (Poddar et al., 2024).** The paper cites this work in §2.1 but does not compare. A direct comparison would help position the contribution relative to the closest latent-variable alignment method.

## Removed Points

*These points were raised by reviewers but are removed because they are either factually incorrect, speculative without paper evidence, or not substantive weaknesses.*

1. **"The evaluation tasks (ARC, GSM8K, TruthfulQA) are only tangentially related to preference alignment."** — The paper also includes direct preference accuracy (Table 2) and AlpacaEval win rates (Table 3). Capability benchmarks are standard supplementary evaluation in alignment papers. Removed as overblown.

2. **"AlpacaEval only uses GPT-4 for Llama3-8B-Instruct, not other models."** — AlpacaEval is designed for instruction-tuned models; evaluating the instruct variant is the appropriate choice. Removed as not a weakness.

3. **"No limitations section."** — Many papers lack a separate limitations section; this is a formatting preference, not a substantive weakness. Removed.

4. **"No λ sensitivity analysis." / "No g scheduling ablation."** — These are nice-to-haves, not weaknesses. Moved to Nice-to-Haves.

5. **"Comparison with Poddar et al. (2024) not done."** — This is concurrent work cited in §2.1. Empirical comparison would be valuable but its absence is not a weakness of the paper as submitted. Moved to Nice-to-Haves.

6. **"The paper never verifies whether the resulting implicit reward $r(x,y,z)$ has a well-defined preference interpretation across different $z$ values."** — This is a speculative theoretical concern ("never verifies") about something that is not standard practice to verify. The paper's empirical evaluation (preference accuracy, downstream tasks) implicitly validates the model's behavior. Removed as speculative.

## Novel Insights

The most interesting observation from the reviews is not about specific weaknesses but about the tension between the paper's framing and its evidence. The paper is *motivated* by the limitations of multi-objective methods (which need explicit sub-rewards and weights), and it *claims* that LPC's automatically discovered latent codes provide a superior alternative. But the experiments only compare against single-objective methods, creating a mismatch between motivation and validation. This suggests a clear path for strengthening the paper — directly comparing against a multi-reward baseline — that would either confirm the advantage of unsupervised factorization or reveal that the observed gains come from the variational conditioning mechanism rather than the latent structure itself. Either outcome would be informative.

## Suggestions

1. **Add a multi-objective/multi-reward baseline.** The simplest version: train two reward models on UltraFeedback using its per-aspect scores (e.g., helpfulness, honesty), then either combine their scores linearly or use the conditioned-policy approach from Dong et al. (2023). This directly tests whether LPC's unsupervised discovery offers advantages over explicit factor specification.

2. **Add standard errors or confidence intervals to the main tables**, or at minimum state that evaluation was conducted with greedy/deterministic decoding. Given the small effect sizes in many cells, readers need to assess reliability.

3. **Explain the $\pi_{\text{ref}}$ design choice.** Add a brief paragraph discussing why the reference model is not conditioned on $z$ and what the resulting implicit reward $r(x,y,z)$ represents theoretically. This addresses the discrepancy between Eq. 6 and Eq. 7.

4. **Provide qualitative evidence for code interpretability** — e.g., pick the top-5 prompts activating each of the top-4 codes and have a human label the common theme. Even a small table would substantially strengthen the claim.

5. **Consider ablating the $g$ scheduling strategy** (e.g., fixed $g=1$, fixed $g=0$, linear schedule) and the $\lambda$ hyperparameter to help practitioners understand which components drive the improvements.
