Now I have all the information I need. Let me synthesize the final consolidated review.

## Summary

This paper proposes MiniLLM, a white-box knowledge distillation method for LLMs that minimizes reverse KLD between the student and teacher distributions, replacing the standard forward KLD objective. The authors derive a policy-gradient-based optimization with three stabilization strategies (single-step decomposition, teacher-mixed sampling, length normalization) and evaluate across GPT-2, OPT, and LLaMA families (120M to 13B) on instruction-following tasks with Rouge-L, GPT-4 feedback, and human evaluation. Results consistently favor MiniLLM over SFT, word-level KD, and SeqKD.

## Strengths

- **Principled motivation and clear theoretical framing for reverse KLD**: The paper correctly identifies that forward KLD is suboptimal for generative LLM KD because it forces under-capacity students to overestimate low-probability regions of the teacher distribution. The toy Gaussian-mixture illustration (Figure 1) and the connection to policy gradient optimization provide a strong conceptual foundation that goes beyond simply swapping the divergence direction.

- **Novel, well-designed optimization with three empirically validated stabilization strategies**: The single-step decomposition (reducing variance by summing over the vocabulary), teacher-mixed sampling (addressing reward hacking via importance-sampled mixing with the teacher), and length normalization (countering length bias) are individually motivated and their necessity is confirmed by ablation (Table 2/Figure 3). Table 2 shows catastrophic drops without Length Norm (27.4→17.4 R-L) and Teacher-Mixed (27.4→22.3), establishing these as critical to making reverse-KLD training practical.

- **Consistent, large-margin improvements across model families, sizes, and metrics**: In Table 1, MiniLLM outperforms all baselines in 47 out of 48 setting–metric combinations across GPT-2 (120M–760M), OPT (1.3B–6.7B), and LLaMA-7B on five datasets using two automatic metrics. The improvements are often substantial (e.g., OPT-1.3B GPT4 score on SelfInst: 47.0 vs next-best 37.7; GPT-2 760M on S-NI: 29.3 vs next-best 26.1). The scaling plot (Figure 2) shows this holds across 5 student sizes, and human evaluation on SelfInst (Figure 1) confirms the trend holds for human judges.

- **Exposure bias and calibration analyses provide mechanistic support beyond raw scores**: Figure 4 shows that MiniLLM's excess error (ExAccErr) stays flat with generation length while baselines grow linearly, directly validating the claim that on-policy self-generated samples reduce train-test mismatch. The calibration analysis (Table 3), though limited to classification tasks, shows large ECE improvements over KD and SeqKD (e.g., SST-2 ECE: 0.099 vs 0.191 vs 0.243), indicating the method meaningfully improves confidence alignment.

## Weaknesses

### Major

- **No confidence intervals or significance tests for any result**: All numbers in Table 1 are reported as averages over 5 random seeds, but no standard deviations, standard errors, or significance tests are provided. Several comparisons involve small margins (e.g., GPT-2 340M on DollyEval GPT4: MiniLLM 52.2 vs SFT 51.9 — a 0.3 point gap). Given that GPT-4 feedback as a metric is inherently noisy, and reported variations across seeds are not quantified, the central claim that MiniLLM "consistently outperforms" baselines cannot be fully evaluated. This is the single most impactful weakness because it affects the entire empirical contribution.

- **Diversity evaluation is insufficient to support the claim that diversity is "preserved"**: The paper reports only Dist-4 (within-generation n-gram repetition) and language modeling loss (Table 4). Dist-4 measures repetition within a *single* generated response, not diversity *across* multiple responses to the same prompt. Language modeling loss on the test set measures distributional fit, not response diversity. The paper acknowledges this gap in its own discussion (lines 341–342) by noting that for many applications "one correct response is sufficient," but this is a scope argument, not evidence. The claim that "MiniLLM preserves generation diversity" is not supported by the metrics provided.

### Minor

- **The importance-sampling approximation bias is acknowledged but unanalyzed**: The approximation $w_t \approx q_\theta(y_t)/\tilde{p}(y_t)$ replaces the full product of per-token importance weights to reduce variance (line 105), but the bias this introduces is not characterized. A correctly weighted estimator would be unbiased but high-variance; the approximation trades unbiasedness for lower variance. The ablation (Table 2) shows teacher-mixed sampling is critical, but does not isolate whether the benefit comes from improved sampling or from the optimization itself. This affects the theoretical grounding—whether the learned student actually minimizes reverse KLD is unclear.

- **The calibration analysis switches to classification tasks without explaining the protocol**: Table 3 evaluates ECE on SST-2 and BoolQ, but the paper does not describe how the generation models are adapted to produce classification logits. Are probabilities obtained via prompt engineering, scoring class-label tokens, or some other method? Without this detail, the relevance of these calibration numbers to generation quality is unclear. The teacher ECE on SST-2 (0.025) is suspiciously low and suggests either overfitting or a mismatch in evaluation setup.

- **The dataset size is small for instruction tuning**: Only ~12.5K training examples remain after filtering by context length (Section 3.1). The teacher is fine-tuned on this same small dataset, so the teacher's distribution may be narrow. This setup may amplify the apparent advantage of mode-seeking reverse KLD, as there are fewer modes for the student to miss. An experiment with larger datasets (e.g., full self-instruct data) would strengthen the generality claims.

### Trivial

- Figure 3 caption says "reverse KLD between the teacher and the students during training" — the y-axis would be clearer if labeled directly rather than inferred from the caption.

## Nice-to-Haves

- A side-by-side human evaluation on long-form generation (>100 tokens) would directly support the exposure bias analysis (Figure 4), which currently only uses automatic metrics.
- Evaluating on datasets with multiple valid references (e.g., MS MARCO, or a summarization dataset with multiple ground-truth summaries) would directly test whether reverse KL's mode-seeking harms quality when multiple answers are acceptable.
- Computing cosine similarity between gradients from the full importance weight vs the approximation on a small sample of prompts would quantify the bias-variance trade-off of the approximation.

## Removed Points

These points from the source reviews are removed or weakened after verification against the paper:

1. **"Evaluation favors the method's mode-seeking property" (Harsh Critic, Critical Issue 1)**: The paper explicitly acknowledges the diversity trade-off (lines 341–342) and argues within its scope that "one correct response is sufficient" for instruction-following. The remaining concern (limited diversity evidence) is kept in the Major section above but without the framing that the evaluation is *biased*. The paper's evaluation metrics (Rouge-L, GPT-4) are standard for this setting.

2. **"Missing comparison with diversity-promoting baselines"**: This would strengthen the paper but is a nice-to-have, not a core defect. The paper's scope is white-box KD from LLM distributions, and the baselines (SFT, KD, SeqKD) are the standard ones.

3. **"Synthetic experiment with known teacher distribution"**: Requesting this goes beyond what is standard for empirical NLP papers. The toy Gaussian example is acknowledged by the critic themselves as "trivial" and not representative of text — this is a scope-expanding request.

4. **"Apply method to LLaMA-65B teacher"**: This is an obvious extension but not a weakness of the current paper, which already scales to 13B teachers.

5. **"Calibration analysis should be replaced with generation-relevant analysis"**: A good suggestion, but the calibration analysis is still informative even if imperfect. The paper is not required to replace it.

6. **Strength Finder claim about diversity**: "MiniLLM maintains similar distinct-4-gram ratios and language modeling loss as the teacher, refuting the concern." This claim conflicts with the verified weakness (Dist-4 measures within-generation repetition, not cross-generation diversity). The strength is removed as it overstates what the evidence shows.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same core tension: the paper makes a principled argument for reverse KL and backs it with extensive experiments, but lacks the statistical rigor (error bars) and diversity evaluation needed to fully substantiate its claims. This tension is inherent to the method's design — mode-seeking *by construction* trades diversity for precision, and the paper's evaluation is designed to show the upside of that trade.

## Suggestions

1. **Add standard deviations or confidence intervals to Table 1 and all main results**. Even reporting the range across the 5 seeds would meaningfully improve interpretability. For GPT-4 feedback scores, bootstrapping over per-prompt scores is feasible and would let readers judge which improvements are reliable.

2. **Add a genuine cross-response diversity metric**: For a set of prompts, sample multiple responses per prompt (temperature > 0) and report self-BLEU, distinct n-grams across responses, or number of semantically distinct clusters per prompt (using sentence embeddings). This would directly address whether mode-seeking loses important modes.

3. **Describe the calibration evaluation protocol**: State how generation models were adapted to produce classification logits on SST-2 and BoolQ. If classification prompts were used, provide an example. This is a one-paragraph addition that would resolve reviewer confusion.

4. **Add a brief discussion of the importance-sampling bias**: Even a qualitative discussion of the bias-variance trade-off, or an empirical check (gradient cosine similarity on a small batch between the full product and the approximation), would strengthen the theoretical framing.

## Score and Decision

### Calibration Anchors

| Anchor Path | Avg. Human Score | Comparison to This Paper |
|---|---|---|
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/Wv9Gl1bFbc.md (Dynamic Self-Distillation) | 3.00 | Much weaker — incremental adaptation of a CV method with thin experiments |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/nh5tSrqTpe.md (Don't Pre-train, Teach) | 3.00 | Much weaker — CV distillation with novelty/reproducibility concerns |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/8wjWm5jr1w.md (Multi-Granularity Semantic Revision) | 6.00 | Comparable domain but weaker empirical results (<1 R-L improvement over MiniLLM as baseline); MiniLLM has stronger margins |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/FJWT0692hw.md (SequenceMatch) | 6.00 | Similar quality — well-motivated but with comparable evidential gaps (limited tasks, estimator properties unanalyzed) |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/tJHDw8XfeC.md (MiniPLM) | 6.40 | Similar quality — principled pre-training KD with comparable empirical scope and some of the same rigor gaps |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/cqsw28DuMW.md (TAID) | 7.33 | Slightly stronger — better evaluation of the diversity trade-off and more thorough analysis |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/xsx3Fpo3UD.md (Advantage-Guided Distillation) | 7.50 | Slightly stronger — cleaner experimental design and more focused evaluation |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/1aF2D2CPHi.md (Open-Vocabulary Customization from CLIP) | 8.00 | Stronger — more complete empirical validation including rigorous baselines and ablations |

This paper presents a well-motivated, principled approach to white-box LLM distillation with a clear contribution (reverse KLD + practical optimization), supported by broad experiments across model families, sizes, and metrics including human evaluation. The weaknesses — absence of error bars, insufficient diversity measurement, unanalyzed approximation bias, and a small training dataset — are real but fixable and do not invalidate the core contribution. The paper's empirical scope and the consistency of its improvements substantially exceed what the lower-scoring anchors achieve, and it is competitive in quality with the accepted papers in the 6–7 range.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>