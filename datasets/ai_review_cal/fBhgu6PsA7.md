- Decision: Reject
- Avg Score: 5.83
- Scores: 6, 6, 6, 6, 6, 5
Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes MoFO (Momentum-Filtered Optimizer), a fine-tuning algorithm that mitigates catastrophic forgetting in LLMs by updating only the parameters with the largest momentum magnitudes in each parameter block at each iteration. MoFO requires neither pre-training data (unlike replay methods) nor loss function modifications (unlike regularization methods). The authors provide convergence analysis of a simplified GD variant, present experiments on instruction fine-tuning (MetaMathQA, Code-Alpaca with Llama-2-7B) and continual fine-tuning (TRACE benchmark with TinyLlama-1.1B), and demonstrate that MoFO achieves comparable fine-tuning performance to full-parameter training while better preserving general capabilities.

## Strengths

1. **Clear motivation grounded in empirical observation.** The paper first demonstrates (Figures 1–2, Pythia-160m) that different optimizers converge to minima at different distances from initialization, and that closer minima better preserve pre-training knowledge. This observation directly motivates the design of a BCD-style method that constrains parameter movement — a clean and compelling argument.

2. **Momentum-based selection empirically outperforms gradient-based and random selection.** Table \ref{gradient_mask_exp} shows MoFO achieving 45.4 GSM8K vs. gradient-filtered BCD (40.2) and randomized BCD (35.0) at the same 10% update fraction, while all three BCD variants show comparable forgetting. This directly validates the paper's core algorithmic choice and is the strongest piece of evidence for the method.

3. **Consistent forgetting mitigation across settings.** MoFO shows the smallest average general-capability degradation on MetaMathQA (+0.4%, the only method with positive average), Code-Alpaca (–1.1%, the smallest decline), and superior BWT on the TRACE continual learning benchmark (–5.4 vs. –10.3 for Full FT). The pattern is consistent across diverse tasks and model sizes.

4. **Orthogonality to replay methods.** Table \ref{trace_exp} shows that MoFO + Replay achieves 47.0 OP vs. Replay alone at 45.5, demonstrating that MoFO's benefits are additive to existing continual learning techniques. This is practically valuable as MoFO can be combined with other approaches rather than replacing them.

## Weaknesses

### Fatal
None.

### Major

1. **No experimental comparison to LoRA or other PEFT methods.** The paper discusses LoRA in the related work (line 585), noting it "forgets less but learns less," yet never compares against it experimentally. LoRA is the most widely used approach for mitigating forgetting during LLM fine-tuning — a method specifically designed to preserve pre-trained knowledge via low-rank adapters. The paper's evaluation compares MoFO against Full FT, HFT, and L₁/L₂ regularization, none of which are the de facto standard for forgetting mitigation. Since LoRA shares both advantages that MoFO claims (no pre-training data needed, no loss modification), its absence from the experiments means the paper's practical significance cannot be assessed. The claim that "MoFO still allows for high-rank updates to achieve better fine-tuning performance" (line 585) is asserted without evidence — a direct comparison with LoRA at standard ranks (e.g., 8, 16, 64) on the same tasks is needed.

### Minor

2. **The convergence analysis analyzes a different algorithm than what is used.** Theorem 1 proves convergence at rate O(T^{-1/2}) for a GD variant of MoFO that uses gradient magnitudes for filtering (not momentum magnitudes) and lacks momentum, bias correction, and second-order statistics. The paper acknowledges this (line 241: "rather non-trivial") and frames it as "theoretical support for the strong performance of MoFO." This is overstated — the analyzed algorithm differs in both the selection criterion and the optimizer structure. A theorem about gradient-filtered GD does not directly support a momentum-filtered Adam variant. The paper would benefit from framing this as a limited first step rather than as evidence for the proposed method.

3. **Single-run results without error bars or seed information.** All reported numbers come from single runs with no discussion of variance. Many comparisons involve differences of ≤1–2% (e.g., MoFO's average change on MetaMathQA: +0.4% vs. HFT: –0.1%). The paper does not report which random seeds were used or whether results were stable across initialization/data ordering. Given typical variance in LLM fine-tuning, it is unclear whether the reported gaps are meaningful. Adding multiple seeds (even 2–3) would substantially increase confidence.

4. **The α hyperparameter lacks principled selection guidance.** MoFO uses α=15% for MetaMathQA and 10% for Code-Alpaca, and the ablation (Figure 4) shows performance degrades sharply beyond ~20% update fraction. The paper provides no validation-set procedure or heuristic for choosing α on a new task, raising the question of whether α was tuned on test metrics. The observation that "MoFO avoids forgetting... when the parameter update fraction is below 20%" (line 468) provides only a rough bound, not a selection method.

5. **No per-task breakdown for the TRACE continual learning benchmark.** Table \ref{trace_exp} reports only aggregate OP and BWT scores across 8 diverse tasks. This hides potential trade-offs — MoFO might improve some tasks while harming others. Reporting per-task accuracies (even in an appendix) would improve transparency.

### Trivial
None.

## Nice-to-Haves
- A wall-clock time or memory comparison against Full FT and LoRA would clarify practical trade-offs.
- A diagnostic connecting momentum magnitude to actual parameter movement (e.g., tracking |Δθ| for selected vs. non-selected parameters during training) would strengthen the mechanistic explanation.
- The toy example in Section 5 is illustrative but could be shortened or moved to an appendix.

## Removed Points

- **"Convergence analysis does not cover the actual algorithm" framed as a fatal/structural flaw.** Removed from Fatal because the paper is transparent about the limitation (explicitly calling it "non-trivial" and leaving full proof to future work). Kept as Minor (point 2 above) because the overclaim of "theoretical support" is a real but limited issue.

- **Criticism that L₁/L₂ baselines lacked grid search.** Removed — the paper gives fixed λ values (1e-3, 1e-6), which is standard practice when these are not the main comparison. The harsh critic's inference that they "could easily make them underperform" is speculative without evidence that other values would change conclusions.

- **Various section-by-section presentation notes** (e.g., "the introduction ignores architecture-based methods," "Section 5 could be shortened"). These are stylistic preferences or scope disagreements, not concrete weaknesses of the paper's substance.

- **Strength Finder's claim #3 (convergence guarantee as strength).** Downgraded because the theorem analyzes a GD variant with gradient-based filtering, not the actual MoFO algorithm. This is an overclaim, not a genuine strength.

## Novel Insights

Neither the reviewer inputs nor my analysis surfaced genuinely novel insights beyond what the paper already provides. The paper's own contribution — that momentum magnitude is an effective selection criterion for BCD in LLM fine-tuning — is the key insight, and it is well-supported by the comparison against gradient-filtered and randomized BCD.

## Suggestions

1. **Add LoRA to the experimental comparison.** This is the single highest-leverage improvement. Compare MoFO against LoRA (ranks 8, 16, 64) on both MetaMathQA and Code-Alpaca with the same evaluation protocol. If MoFO matches or beats LoRA on both fine-tuning accuracy and forgetting, the contribution is clearly validated. If not, the paper should honestly characterize the trade-off.

2. **Report results from 2–3 seeds with standard deviations** for at least the main instruction fine-tuning tables. If this is computationally prohibitive, state this explicitly and report a single seed with its value identified.

3. **Provide guidance for choosing α.** Describe a validation-set procedure (e.g., "tune α on a held-out subset of the fine-tuning data using the general capability average as a monitoring metric") or provide a default recommendation (e.g., "α=10% is a safe starting point based on our experiments").

4. **Reframe the convergence result more honestly.** Explicitly state that Theorem 1 applies to a gradient-filtered GD variant and should be viewed as a preliminary theoretical step rather than as direct support for the full MoFO algorithm.
