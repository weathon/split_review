Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes RISE (eRror-Injected Self-Editing), a preference learning framework that constructs hard negative pairs by prompting an LLM to inject predefined subtle errors (miscalculations, incorrect substitutions, omission of terms) into a few tokens of its own correct step-level solutions. These self-edited step pairs are combined with standard full-solution correct/incorrect pairs for step-wise DPO training, augmented with an NLL loss for stability. Experiments on Qwen2 and Llama-3.1 families (7B–72B) across multiple math benchmarks show consistent improvements over base models, with RISE-Qwen2-7B achieving +7.9% on MATH and +3.0% on GSM8K.

## Strengths

- **Novel hard-negative construction via self-editing.** The idea of using the model itself to inject controlled, subtle errors into correct solutions—creating preference pairs that differ by only a few tokens—is conceptually appealing and avoids expensive external annotations. This provides a principled way to generate hard negatives targeting specific error types.

- **Consistent improvements across model families and scales.** RISE improves both Qwen2 and Llama-3.1 at 7B/8B and 70B/72B scales. For example, RISE-Qwen2-7B improves from 52.2% to 59.9% on MATH and from 85.4% to 88.4% on GSM8K; RISE-Llama-3.1-8B improves from 48.3% to 51.0% on MATH and from 84.0% to 87.9% on GSM8K. At the 70B scale, RISE-Llama-3.1-70B reaches 95.1% on GSM8K.

- **Error analysis validates targeted error mitigation.** The paper provides an error-type breakdown (Figure 3) using GPT-4o-based detection (92% human-verified accuracy on 50 samples), showing that RISE reduces predefined subtle errors (calculation, substitution, omission) compared to both the base model and standard DPO, while standard DPO actually increases substitution errors.

- **Thorough experimental exploration.** The paper includes ablation studies (Table 3), hyperparameter sweeps on the number of self-edited pairs (Figure 4) and sampling attempts (Figure 5), analysis of different error-injection combinations (Table 5), and out-of-domain evaluation on SVAMP, AIME24, and Odyssey-MATH.

## Weaknesses

### Fatal
None.

### Major

1. **The core novelty (self-edited pairs) contributes a modest portion of the reported gains.** The ablation study (Table 3) shows that removing self-edited pairs (i.e., training only on full-solution pairs + NLL loss) yields 88.3 GSM8K / 58.2 MATH for Qwen2-7B, compared to full RISE's 88.4 / 59.9. The incremental gain from the claimed key component is **+0.1% on GSM8K and +1.7% on MATH**. For Llama-3.1-8B, the gains are +1.1% on GSM8K and +1.1% on MATH. Meanwhile, the combination of full-solution DPO + NLL (without self-edited pairs) already accounts for the vast majority of the improvement over the base model (e.g., +6.0% of the +7.7% MATH gain for Qwen). The paper's framing consistently emphasizes error injection as the key contribution, but the evidence suggests that most of the headline improvements come from standard DPO components, not the self-editing mechanism. This is a significant gap between the paper's narrative and the data.

2. **The claim of "focus[ing] on predefined errors and their tokens" / "targeting a few error tokens" is not validated by the implementation.** The step-wise DPO loss (Equation 3, \(\mathcal{L}_{\text{DPO-Edit}}\)) is standard step-level DPO—it contrasts entire steps, treating all tokens within a step equally, with no token-level weighting or attention mechanism. While the *pairs* differ only in error tokens (making them harder negatives), the loss itself does not specifically "focus on" or "target" those tokens any more than any DPO loss does. The paper lacks any token-level analysis (e.g., showing that the model's probability changes more on injected error tokens than on surrounding tokens) to support the claim that RISE achieves "subtle error-aware" learning beyond what standard step-wise DPO with hard negatives would provide. This is a gap between the stated mechanism and the actual implementation.

### Minor

1. **Comparison with Step-DPO is not fully controlled.** Step-DPO results are cited from its original paper. While the paper states "We adopt mathematical problems used by Step-DPO," differences in initialization, optimizer hyperparameters, training steps, and sampling procedures could affect the comparison. The ablation shows that even the "w/o self-edited pairs" condition (full-solution DPO + NLL) already outperforms Step-DPO on MATH (58.2 vs. 55.8), suggesting the claimed advantages over Step-DPO may not stem from the error-injection innovation. This weakens the competitive claims.

2. **The Levenshtein filter threshold \(\alpha\) is not specified.** The paper defines \(\alpha\) as a similarity filter for self-edited pairs (Equation 1) but never reports its value or analyzes its sensitivity. Similarly, the selection of \(N\) (number of self-edited pairs per problem) varies across models (1 for Qwen, 3 for Llama) with limited justification beyond post-hoc observations.

3. **About 50% of training problems (4.5K out of 9K) are discarded** because they lack both a correct and incorrect sample within \(K=5\) attempts. These discarded problems are not analyzed—are they systematically harder or easier? Could this introduce selection bias? With more sampling attempts (Figure 5), more problems become usable but performance degrades, suggesting a trade-off that is noted but not fully explained.

4. **The quality of injected errors is not validated.** The paper assumes the self-editing prompt reliably produces realistic, "hard" errors, but no human evaluation or systematic check is performed on the edited steps to verify that the injected errors are plausible mistakes a strong model would make.

### Trivial
None.

## Nice-to-Haves

- **Token-level analysis**: Showing that after RISE training, the model assigns lower probability specifically to injected error tokens (e.g., the wrong number in a substitution) compared to a baseline DPO model would directly validate the "error token focusing" claim.
- **Fair re-implementation of Step-DPO** under identical training conditions (same backbone, data, sampling, steps) would strengthen the competitive claims.
- **Controlled ablation isolating error injection**: A comparison of (a) full-solution DPO + NLL, (b) full-solution DPO + NLL + random step pairs (not error-injected), and (c) full-solution DPO + NLL + self-edited pairs would isolate whether the benefit comes from having any step-level hard negatives or specifically from error-injected ones.
- **Human evaluation of error realism** for a sample of self-edited steps.

## Removed Points

The following points from the source reviews were removed or moved here per the meta-review instructions:

1. *Strength Finder's generic strengths* ("this paper addressed an important problem," "this paper targeted an interesting question") — these are superficial and lack specific evidence; removed.
2. *Critic's claim that "the paper's contribution is not convincingly established" and "cannot recommend acceptance as-is" as a blanket dismissal* — the paper does demonstrate real (if modest) contributions and the evidence supports the method working, just not as strongly as framed; this is addressed in the Major weaknesses above with balanced assessment.
3. *Critic's claim that "random combination works best, suggesting that the specific error types don't matter—any injection does"* — the paper's interpretation (diverse errors help learning) is equally valid; the data supports both views but neither undermines the method.
4. *Critic's claim that the method "does not actually focus on error tokens" as a structural flaw* — this is kept as a major weakness (item #2) but reframed as a gap between claim and evidence rather than a structural flaw, since the pairs do differ in error tokens and the DPO signal is implicitly concentrated on those differing tokens.
5. *Critic's request for "more comprehensive controlled study" with random step pairs* — moved to Nice-to-Haves as a reasonable extension, not a required experiment.
6. *Critic's missing-appendix/proof comments* — the parser strips appendix content from all papers; these concerns are not valid.

## Novel Insights

None beyond the paper's own contributions. The key insight—constructing preference pairs by self-editing correct solutions to inject specific error types—is the paper's main novelty. The reviews confirm this is a promising direction but surface the important nuance that the empirical gains from this specific mechanism are more modest than the paper's narrative suggests.

## Suggestions

1. **Better calibrate the claims.** The paper should explicitly state the incremental contribution of self-edited pairs (1–2% on MATH, 0–1% on GSM8K) rather than attributing the entire 3.0%/7.9% improvement to the error-injection mechanism. A more measured narrative would better match the evidence.

2. **Add token-level analysis.** Compute the per-token probability change on injected error tokens versus surrounding tokens to validate the claim that the model learns specifically about error locations.

3. **Report the \(\alpha\) threshold value and its sensitivity.** This is a control knob in the data construction pipeline; leaving it unspecified is a reproducibility gap.

4. **Acknowledge and discuss the selection bias from discarding 50% of problems.** Analyze the characteristics of discarded vs. used problems.

## Score and Decision

**Originality**: Good — the self-editing idea for constructing hard preference pairs is novel.

**Importance of research question**: High — improving mathematical reasoning in LLMs and mitigating subtle errors is practically important.

**Claims well supported**: Moderate — the overall method works, but the central claim about error injection being the key driver is not well supported by the ablation data.

**Soundness of experiments**: Adequate — the ablation is present and the analysis is thorough, but the Step-DPO comparison is uncontrolled.

**Clarity of writing**: Good — the method is clearly described and the motivation is well-framed.

**Value to the research community**: Moderate — the idea could inspire follow-up work on targeted hard-negative construction, but the current evidence for its effectiveness is limited.

The paper presents a novel idea and a thorough experimental study. However, the central weakness—that the core novelty (self-edited pairs) contributes modestly relative to standard DPO components, and that the "error token focusing" claim is not validated—means the evidence does not fully support the paper's framing. The method works, but the claimed mechanism is not convincingly isolated. This is a borderline paper: the idea is worthwhile, but the current evidence does not rise to the level of a strong acceptance.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>