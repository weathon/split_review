I now have a thorough understanding of the paper and all reviewer claims. Let me write the consolidated review.

## Summary

This paper establishes the first scaling law for masked diffusion models (MDMs), showing they scale at a rate comparable to autoregressive models (ARMs) with a ~16× compute gap — significantly smaller than the ~64× gap for continuous diffusion models. The authors train MDMs up to 1.1B parameters, propose an unsupervised classifier-free guidance (CFG) method that leverages unpaired data, and evaluate on zero-shot language understanding, conditional generation, and two tasks where ARMs struggle (reverse curse and temporal degradation). The paper argues MDMs are a viable large-scale alternative to ARMs.

## Strengths

1. **First scaling law for masked diffusion models.** The IsoFLOP analysis (Sec. 3, Figs. 1–2) across compute budgets from 6×10¹⁸ to 10²⁰ FLOPs is systematic and follows established methodology (Chinchilla). The finding that MDMs have a comparable scaling rate to ARMs with only a 16× compute gap (vs. 64× for continuous diffusion models) is a genuinely novel and useful quantitative result that did not exist before. This provides a principled foundation for future MDM scaling efforts.

2. **Unsupervised CFG is a principled and well-explained contribution.** The idea of using a dummy mask sequence to convert unconditional distributions into conditional format (Eq. 6) is clever and correctly grounded in the MDM's probabilistic formulation. The method improves performance across all eight zero-shot benchmarks (Table 1, e.g., +7.2% on OpenBookQA, +4.99% on LAMBADA) and, when fine-tuned on paired data (Table 4), unsupervised CFG (1.60) outperforms both the no-CFG baseline (1.32) and standard CFG (1.53) on MT-Bench.

3. **Controlled architecture comparison.** The paper keeps the Transformer architecture nearly identical between MDMs and ARMs (only adding a mask token embedding and removing the causal mask), isolating the effect of the diffusion formulation from architectural confounds. This strengthens the validity of the scaling law and downstream comparisons.

4. **Broad, multi-task evaluation.** Unlike prior MDM work limited to unconditional generation or perplexity, this paper evaluates on 8 zero-shot benchmarks, MT-Bench for conditional generation, and two ARM-specific challenges (reverse curse, temporal degradation). This breadth demonstrates MDMs' viability as general-purpose language models, not just generative models.

## Weaknesses

### Fatal
None.

### Major

1. **Unfair comparison in the reverse curse experiment (Sec. 7.1).** The MDM is fine-tuned on the training split of the reverse curse dataset, while the comparison baselines (GPT-3 175B, Llama-2 13B) are evaluated zero-shot or few-shot — as sourced from Berglund et al. (2023) and Lv et al. (2023). This confounds architecture with exposure to task data: a same-size ARM fine-tuned on the same training data is a missing control. The paper's headline claim — that a 1.1B MDM "breaks the reverse curse encountered by much larger ARMs … such as Llama-2 (13B) and GPT-3 (175B)" — is prominently featured in the abstract, introduction, and conclusion, and is not supported by the evidence as presented. *Why this matters:* The reverse curse is a central narrative device in the paper ("MDMs address challenging tasks for ARMs"). If the advantage is due to fine-tuning rather than the MDM architecture, the claim is misleading. *Qualification:* Berglund et al. (2023) do show that fine-tuned ARMs (GPT-2) also suffer from the reverse curse, so the MDM's bidirectional advantage is likely real; but the specific comparison to GPT-3/Llama-2 using reported numbers does not control for fine-tuning, making it impossible to assess from this paper alone. A fine-tuned ARM baseline of comparable size on the same data should be added.

2. **Likelihood evaluation method selected per-task on test data (Sec. 5).** The paper uses two different likelihood evaluation methods (chain rule vs. Monte Carlo) and picks the better one per task, reporting this choice post-hoc: "We observed that the chain rule … results in higher accuracy for OpenBookQA and PIQA, while Monte Carlo … for ARC-Easy, Hellaswag, RACE, and SIQA." This constitutes test-set-based method selection, which inflates reported accuracy. The ARM evaluation is deterministic (standard left-to-right likelihood). *Why this matters:* The comparison is not uniform — the MDM effectively gets a per-task best-of-two advantage. A principled approach would pre-commit to one method or use a validation split.

### Minor

1. **Unvalidated 16× scaling factor at the target model size.** The scaling law is fit on models up to ~220M parameters (10²⁰ FLOPs) and used to justify giving the 1.1B MDM 16× more pre-training compute in downstream comparisons (Table 2, Sec. 6). This extrapolation is standard practice in scaling law work but is not verified at the 1.1B scale. The paper presents no validation losses for the 1.1B models to confirm the 16× gap holds. If the true gap is different, the "fair" comparison collapses. Direct evidence (e.g., validation losses for both the 1.1B ARM and MDM) would strengthen the claim considerably.

2. **MT-Bench results lack external calibration and confidence intervals.** The reported MT-Bench scores (1.40–1.60 for MDM, 1.57 for ARM) are very low in absolute terms. While the comparison to the same-size ARM is fair, the paper provides no external reference point (e.g., a widely-used small model like fine-tuned OPT-1.3B or GPT-2 1.5B under identical conditions) to help readers interpret whether a 1.6 score is meaningful for models of this size. Additionally, timing results come from a single A100 run with no confidence intervals.

3. **No ablation or sensitivity analysis of the CFG scale.** The paper searches the CFG scale in {0.4, 0.6, 0.8, 1} and reports only the best scores. No sensitivity analysis or calibration curves are provided, making it unclear how robust the improvements are to this hyperparameter choice. The gains in Table 1 are modest for some tasks (e.g., +0.05 on PIQA) and may not be significant without error bars.

4. **Temporal degradation experiment (Sec. 7.2) is not compute-matched.** The MDM gets 16× more pre-training compute than the ARM, as the paper acknowledges ("MDMs require 16 times more computation to reach this performance level"). The result is still informative — better robustness with higher validation loss is noteworthy — but the confound means the advantage cannot be cleanly attributed to the MDM architecture rather than to the additional training. A compute-matched comparison (higher-validation-loss MDM vs. lower-validation-loss ARM, both on same compute budget) would be cleaner.

### Trivial

1. **FLOPs calculation for MDM training is underspecified.** The paper uses $C = 6ND$ for MDMs, but the MDM loss integral (Eq. 4) may be approximated with one or more Monte Carlo timestep samples per token. The FLOPs per token depend on this choice. Clarifying the number of timestep samples would remove ambiguity about the exact 16× factor.

## Nice-to-Haves

- A fine-tuned ARM baseline (same size, same data) for the reverse curse experiment, allowing direct head-to-head comparison.
- Validation losses for the 1.1B ARM and MDM models to verify the 16× scaling factor at scale.
- Confidence intervals or standard deviations for all reported metrics.
- A held-out validation set for selecting the likelihood evaluation method (chain rule vs. Monte Carlo), rather than post-hoc test-set selection.
- A compute-matched temporal degradation comparison where both models receive the same training budget.

## Removed Points

The following weaknesses from the Harsh Critic are removed or downgraded:

- **"Weak absolute performance in conditional generation — the trade-off is hollow"** (Harsh Critic #2 first half): The paper compares MDM to a same-size ARM (1.57 vs 1.40-1.60). The trade-off claim is about *relative* performance and speed, not absolute quality. The low absolute scores are a function of model size (1.1B), not a flaw in the method, and the comparison to a same-scale ARM is valid. The criticism about missing external reference is kept (Minor #2); the stronger version claiming the trade-off is "hollow" is removed.

- **"Not mentioning whether ARM uses greedy or sampling"** (part of Harsh Critic #2): The paper states for the reverse curse that it uses "greedy sampling" (Sec. 7.1). For MT-Bench, the NFEs of 325.94 for the ARM are consistent with standard autoregressive decoding. This is a minor specification gap, not a substantive weakness.

- **"The paper would be likely to mislead readers about the nature of the MDM advantage"** (Harsh Critic final paragraph): Overly strong editorializing. The paper makes genuine contributions and the reverse curse claim, while overstated, is directionally correct based on prior literature (Berglund et al. showed fine-tuned ARMs also fail).

- **"Ambiguity in training FLOPs for MDM"** (Harsh Critic Other Observations third point): Moved to Trivial. This is a minor clarification.

- **Strength Finder Strength #2 (MDMs break reverse curse):** The strength is partially valid but the unfairness of the comparison undermines it. I have kept a weakened version of this as observation rather than a core strength, given the major weakness above.

## Novel Insights

The most interesting observation that emerges from reading the reviews together is the asymmetry between the paper's strongest contribution (the scaling law, which is clean, careful, and addresses a genuine gap in the literature) and its weakest claim (the reverse curse, which is prominent but methodologically confounded). The scaling law results — that MDMs have a 16× compute gap vs. ARMs (not 64× as for continuous diffusion) and that optimal MDM size is about half that of ARMs — are genuinely useful design heuristics that will influence future MDM research. The unsupervised CFG method is also sound and well-motivated. The paper would be stronger if it deemphasized the reverse curse result or added a proper baseline, letting the scaling law and unsupervised CFG carry the main narrative. None beyond the paper's own contributions.

## Suggestions

1. **For the reverse curse:** Add a fine-tuned ARM baseline of comparable size (1.1B) trained on the same reverse curse data. If it also achieves low reverse-direction accuracy, the claim is well-supported. If it achieves comparable accuracy to the MDM, the claim should be retracted or substantially softened. Alternatively, cite Berglund et al.'s fine-tuned GPT-2 results explicitly and reframe the comparison as "MDMs overcome a known ARM architectural limitation that persists even after fine-tuning."

2. **For the scaling law:** Report validation losses for the 1.1B models (both ARM and MDM) in a brief table or footnote. This would confirm the 16× extrapolation at the target scale and address the most common objection to scaling law extrapolation.

3. **For the likelihood evaluation:** Add a sentence explaining that the choice of chain rule vs. Monte Carlo was validated on a held-out subset, or commit to one method for all tasks. Even a brief sensitivity comparison showing both methods on all tasks would help.

4. **For MT-Bench:** Include a simple reference point — the MT-Bench score of a widely-available small model (e.g., fine-tuned OPT-1.3B or Pythia-1.4B) evaluated under identical conditions — to help readers interpret absolute quality.

5. **For CFG:** Report scores for each CFG scale in {0.4, 0.6, 0.8, 1.0} rather than only the best, to demonstrate robustness.

## Score and Decision

The paper makes genuine contributions — the first scaling law for MDMs, a novel unsupervised CFG method, and a broad evaluation showing MDMs are competitive with ARMs across multiple dimensions. The primary weakness is the confounded reverse curse comparison and the test-set-based likelihood evaluation selection, both of which are addressable. The scaling law, unsupervised CFG, and most evaluation results are solid and advance the field. However, the reverse curse claim as presented is misleading and cannot be accepted at face value; given its prominence, this weakens the paper's overall credibility. The paper is suitable for conditional acceptance if the reverse curse claim is corrected with proper baselines, or for a stronger venue after revisions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>