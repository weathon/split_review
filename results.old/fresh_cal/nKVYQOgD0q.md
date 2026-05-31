Now I have all the information I need. Let me carefully cross-check every claim and produce the consolidated review.

---

## Summary

This paper introduces Merged Preference Dimensions (MPD), a method for personalizing LLMs by learning a lightweight Preference Control Model (PCM) that dynamically weights the token-level output distributions of frozen expert models (each specialized for a single preference dimension). Unlike prior weight-merging approaches (e.g., Personalized Soup) that average model parameters statically and require white-box access, MPD operates in black-box settings, uses only output logits/probabilities, and can batch across shared preference dimensions during inference. Training uses online RL (REBEL/PPO) with per-dimension reward models and Bradley-Terry normalization. Experiments on Koala and UltraFeedback benchmarks show MPD achieves higher win rates than Personalized Soup and preference prompting across both GPT-4 and human evaluations.

## Strengths

1. **Novel and well-motivated method architecture** — Learning a lightweight PCM (160M params, ≈2% of the 7B base model) to dynamically merge expert outputs at the token level is a clean and creative idea. The method cleanly addresses the key limitation of prior work (Jang et al., 2023): that weight merging is context-independent and can wash out individual preferences. The black-box requirement (only top logits/probabilities) is a genuine practical advantage over parameter-merging approaches.

2. **Consistent empirical advantage over relevant baselines** — Table 2 shows MPD achieves a 66.28% average pairwise win rate across all baselines, outperforming Personalized Soup (61.28%) and Preference Prompting (56.09%). Table 3 confirms this on a second dataset (UltraFeedback). The consistent direction of improvement across two datasets and 8 preference combinations is a meaningful signal.

3. **Ablation study validates key design choices** — Table 4 ablates merging space (probability > logit space), reward modeling (BT normalization improves over direct averaging), and RL algorithm (REBEL works; PPO is viable). These ablations demonstrate that each component of MPD meaningfully contributes to the final performance.

4. **Human evaluation confirms results with statistical significance** — Table 5 reports human evaluation on 200 response pairs: MPD achieves 67.5% win rate vs Preference Prompting and 64.5% vs Personalized Soup, both significant at p<0.05 (binomial test). This provides direct evidence that the GPT-4 judge results are not an artifact of LLM-as-judge bias.

5. **Efficiency analysis reveals an non-obvious advantage** — Under batched inference (32 simultaneous requests), MPD averages 10.48s per request vs Personalized Soup's 13.25s, because output merging can batch across shared preference dimensions while parameter merging cannot. This is a genuinely useful practical insight.

## Weaknesses

### Fatal
None.

### Major

1. **Small evaluation set limits statistical confidence in the main results.** The main experiments use only 100 unique instructions (50 from Koala + 50 from UltraFeedback), scaled to 800 evaluations across 8 preferences. Following the protocol of Jang et al. (2023) is understandable, but the claim of state-of-the-art personalization would benefit from evaluation on substantially more diverse prompts. With only 100 unique instructions, results could be driven by idiosyncrasies of the specific prompts selected.

2. **No statistical significance reported for the primary GPT-4 evaluation (Table 2).** The main win-rate comparisons (66.28% vs 61.28% vs 56.09%) are presented as point estimates without confidence intervals, error bars, or significance tests. Given the limited instruction count, the variance across instructions could be meaningful. The paper only reports a binomial test for the 200-pair human evaluation subset; the primary GPT-4 evaluation lacks any such analysis. This makes it difficult to assess whether the observed differences are reliable.

3. **No per-dimension win-rate breakdown.** The evaluation aggregates scores across all three preference dimensions into a single win/loss decision, but never reports per-dimension win rates. This is a significant omission for a method that claims to dynamically balance multiple preference dimensions. Without per-dimension breakdowns, it is impossible to know whether MPD genuinely satisfies all specified dimensions simultaneously or sacrifices one dimension to improve another. The qualitative examples (Table 6) are helpful but are not a substitute for systematic quantitative per-dimension reporting.

### Minor

1. **The preference dimensions tested (elementary/knowledgeable, concise/informative, friendly/unfriendly) are limited to three manually chosen axes.** Generalization to other dimensions (humor, safety, creativity, technical depth) is untested. Section 4.6 acknowledges this as a limitation, which is good, but the paper's empirical claims remain scoped to these specific axes.

2. **Preference Control Model (PCM) input encoding is underspecified.** The paper states that the PCM takes "the instruction x, the partial response y\<t, and the preference vector ξ" as input (Section 3.1), but does not specify how ξ is encoded — is it a one-hot vector, a learned embedding, or text? The model is described as "LLaMA-based" with 160M parameters, but the input fusion mechanism is unclear. This affects immediate reproducibility from the main text.

3. **Baseline coverage is reasonable for the setting but somewhat narrow.** The paper compares against Personalized Soup (the most directly relevant baseline) and Preference Prompting, plus an untrained MPD (Uniform). These are appropriate, but additional comparisons would strengthen the paper. A learned linear combination (trained on a validation set without the full PCM/RL machinery) would help isolate the value of the REBEL training. However, the critic's request for comparisons to reward-ranked tuning (Lu et al., 2022) or SFT-DPO pipelines (Guo et al., 2024) is scope creep — those methods operate in different training paradigms (full model fine-tuning, not black-box merging).

4. **GPT-4-as-judge is used for the primary evaluation with acknowledged but limited mitigation.** The paper is aware of this limitation and includes a human evaluation on 200 pairs, which helps. However, inter-rater reliability for the human evaluation is not reported, and the human subset covers only 200 of the 800 response pairs.

### Trivial
None.

## Nice-to-Haves

- **Analyze the learned PCM weights.** Showing one or two examples where the weight assigned to a specific expert (e.g., "concise") shifts across token positions in response to the generation context would provide direct evidence that the PCM is actually adapting dynamically, not just learning a fixed preference weighting.
- **Report accuracy or agreement of the individual reward models.** Since the PCM training depends on reward model quality, a brief validation note would help.
- **Clearly state the single-user inference trade-off.** The efficiency comparison (batch of 32) correctly identifies the batched advantage, but for the single-user case parameter merging requires one forward pass while MPD requires n forward passes. A brief acknowledgment of this trade-off would improve completeness.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The example about the humorous expert generating a poem about tulips is speculative — no concrete evidence provided."** — This example is illustrative framing in the introduction, not a claimed experimental result. It motivates the problem clearly and is reasonable as an intuitive example.
- **"No prior work applies output interpolation to MORL is plausible but unverified."** — The paper appropriately uses "to the best of our knowledge" language (Section 2, line 36). This is standard practice.
- **"Comparison to [Lu 2022, Guo 2024, Wang 2024a, Dognin 2024] is missing."** — These methods involve full model fine-tuning or SFT-DPO pipelines, not black-box output merging. The comparison would not be apples-to-apples. The most relevant baseline (Personalized Soup) is included.
- **"Missing hyperparameters (learning rate, batch size, number of REBEL iterations, value of η)."** — The paper states there is an implementation details section (Section 6). The PDF parser strips such sections from all papers; they exist in the original submission.
- **"No tokenizer compatibility discussion."** — The paper explicitly addresses this in Section 2: "applicable to both white-box and black-box models and to different model architectures as long as the tokenizer is the same."
- **"The scaling issue of enumerating exponentially many preferences is not discussed."** — The paper *does* discuss this in Section 4.6 as a limitation: "The training of preference control module in MPD requires enumerating on all preference combinations."
- **"The 50-instruction subsets are inherited from Jang et al. (2023) but the paper does not justify why this sample size is adequate."** — The paper follows the prior work's protocol and adds an additional 50 instructions from UltraFeedback. The justification is that this is the standard in the sub-area. The evaluation size is retained as a Major weakness above (it's a real limitation), but the "no justification" framing is removed since the paper cites prior work.
- **"GPT-4's own preferences could bias the results."** — This is a known field-wide limitation, not specific to this paper. The paper mitigates it with human evaluation. Kept as Minor weakness 4 but weakened.
- **"No discussion of the cost of acquiring reward models for new dimensions."** — This is noted in Limitations (Section 4.6) as an area for future work. The paper acknowledges that retraining is needed.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface insights about the method or results that the paper itself does not already provide or clearly imply.

## Suggestions

- **Expand evaluation to substantially more unique instructions** (200–500+) drawn from a broader distribution, to strengthen the statistical basis of the win-rate comparisons.
- **Add confidence intervals or significance tests to the main GPT-4 evaluation** in Table 2 and Table 3. Bootstrapping over instructions is a straightforward approach.
- **Report per-dimension win rates** alongside the aggregate. Include a simple table showing, for each method, the per-dimension win/tie/loss breakdown, to demonstrate that MPD is genuinely satisfying all specified dimensions rather than trading off.
- **Clarify the PCM input encoding** in the main text: specify how the preference vector ξ is represented (one-hot, learned embedding, text concatenation, etc.).
- **Include a visualization or quantitative analysis of the learned PCM weights** across tokens to demonstrate the dynamic adaptation behavior that is central to the method's claimed advantage.

## Score and Decision

The paper presents a genuinely novel method for black-box personalized LLM alignment with a clear motivation, sound design, and consistently positive results across both automated and human evaluations. The contributions are real and practically relevant. However, the empirical evidence has notable gaps: a small evaluation set (100 unique instructions), no statistical significance reporting for the primary GPT-4 results, and no per-dimension breakdown of win rates. These weaken the strength of the conclusions but do not invalidate them. With the suggested improvements to evaluation rigor, this could be a strong contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>