Now I have all the information I need. Let me synthesize the final consolidated review.

## Summary

The paper proposes the Look, Remember, Reason (LRR) framework, which trains a language model end-to-end with a video encoder and low-level surrogate tasks (object detection, re-identification, tracking) to improve visual reasoning in videos. The approach is evaluated across four diverse benchmarks (ACRE, Something-Else, CATER, STAR) and shows consistent improvements over prior task-specific methods on most tasks.

## Strengths

1. **Consistent performance gains across diverse video reasoning benchmarks.** On ACRE compositional split, LRR achieves 98.2% vs ALOE's 91.7% (+6.5%); on Something-Else compositional split, 62.0% vs STIN+OIE+NL's 56.2% (+5.8%); on CATER moving camera, 80.4% vs ALOE's 59.7% (+20.7%); and on STAR, 70.5% vs SeViLA's 64.9% (+5.6%). The paper is evaluated on four benchmarks that test different reasoning capabilities (causal induction, compositional action recognition, tracking, situated reasoning), which is more comprehensive than most prior work.

2. **Ablations demonstrate the practical importance of both surrogate tasks and the spatiotemporal encoder.** Removing surrogate tasks consistently hurts performance across all datasets (e.g., ACRE compositional: 98.2% → 38.1%; CATER static: 84.1% → 68.5%; STAR overall: 70.5% → 48.2%). Removing the two-stream encoder also degrades performance (e.g., Something-Else compositional Top-1: 62.0% → 53.6%; CATER static: 84.1% → 81.4%). These controlled experiments show both components contribute meaningfully to the model's success.

3. **The approach works across LM backbone sizes with minimal degradation.** The model achieves nearly identical performance with OPT-125M and OPT-1.3B on both ACRE (98.2% vs 98.2% compositional) and Something-Else (62.0% vs 61.3% Top-1 compositional), demonstrating the framework is robust and not dependent on a particular scale.

4. **Strong results on motion-heavy, long-term reasoning tasks.** The 20.7% improvement over ALOE on CATER moving camera and the 8.4% gap between the two-stream and single-stream encoders on Something-Else compositional split demonstrate that the spatiotemporal attention mechanism effectively captures motion cues.

## Weaknesses

### Major

1. **The central claim that surrogate tasks provide "grounding" in low-level visual details is not convincingly supported by the evidence.** The w/o Surrogate ablation removes the surrogate task text tokens from the training sequence, but this does not isolate whether the model learns low-level *visual skills* or simply benefits from additional token-level supervision that forces better attention to visual features. The mechanism could be as simple as having more training tokens per example. The paper:
   - **Never quantitatively evaluates whether the model actually performs surrogate tasks correctly** (e.g., accuracy on detection, re-identification, tracking). The qualitative examples (figures) show plausible outputs but provide no evidence of how well the surrogate tasks are solved or whether surrogate accuracy correlates with final task accuracy.
   - **Does not explain the drastically different ablation gaps across datasets.** On ACRE, removing surrogate tasks drops accuracy from 98.2% to 38.1% (a 60%+ absolute drop); on Something-Else compositional, the drop is from 62.0% to 50.1% (~12%); on CATER static, from 84.1% to 68.5% (~16%). If surrogate tasks were teaching essential "low-level visual capabilities," one would expect a more consistent pattern. The extreme ACRE collapse in particular suggests the w/o Surrogate model may not have been properly trained or converged — possibly because the cross-attention layers receive insufficient gradient signal when surrogate tokens are absent.
   - **Does not ablate what type of extra text supervision matters.** A control experiment replacing object-level surrogate tasks with random text completions would help distinguish the effect of "any extra tokens" from "grounded object-level content."
   
   *Why this matters:* The paper's core contribution is that surrogate tasks "endow the model with low-level visual capabilities" and "ground" the LM. Without evidence that (a) the model actually performs these tasks well, (b) the specific content of surrogate tasks drives improvements (rather than extra token budget), and (c) the mechanism involves genuine grounding rather than auxiliary supervision, this core claim remains unsubstantiated.

2. **The "two-stream video encoder" terminology is misleading and overstates architectural novelty.** The paper describes its encoder as "two-stream" (cited to Simonyan & Zisserman 2014), suggesting separate processing pathways for static and motion information (e.g., RGB + optical flow). In reality, the encoder is a **single** Vision Transformer with divided space-time attention (TimeSformer-style, properly cited to Bertasius et al. 2021) — alternating spatial and temporal attention within the same stream. There are no separate pathways. The term "two-stream" is used more than a dozen times throughout the paper (lines 10, 38, 55, 110, 113, 114, 125, 135, 155, 252, 258, 314, 420) and listed as Contribution (ii). While the technical architecture is clearly described and properly cited, the repeated "two-stream" framing is factually imprecise and inflates the architectural differentiation from standard video transformers.

### Minor

1. **Blanket "state-of-the-art across tasks" claim is overstated for CATER static camera.** On CATER static camera, the paper achieves 84.1% Top-1 while Loci (cited as abs-2205-13349) achieves 90.7%. The paper acknowledges Loci's result in text (line 385) and dismisses it as "not applicable to the moving camera split," but this does not change the fact that Loci outperforms LRR on the static split. The abstract's claim of "surpassing state-of-the-art task-specific methods across tasks by a large margin" is not accurate for CATER static camera.

2. **The STAR experiment is not a clean comparison.** The LRR model's training on STAR leverages additional data (Kinetics, Moments in Time, Something-Else surrogate tasks, text regularization) that the compared baselines may not use. The headline 5.6% improvement over SeViLA could partly reflect this additional training data rather than the LRR framework alone. An ablation that uses the same additional data without the LRR framework would be needed to isolate the framework's contribution.

3. **Random prompting probability (30%) is not ablated.** The choice of 30% is stated but never systematically varied. The ratio of surrogate-to-answer tokens during training is not reported, and the w/o Surrogate ablation does not control for total training tokens or sequence length, making it unclear whether the baseline is disadvantaged by a shorter effective sequence.

4. **Varying but unexplained ablation gaps across datasets.** The w/o Surrogate ablation causes a 60-point drop on ACRE but only a ~12-point drop on Something-Else compositional and ~16-point drop on CATER static. The paper offers no analysis of why the effect is so dataset-dependent, which weakens the claim that surrogate tasks instill a general low-level visual capability.

### Trivial

- The paper says ground-truth annotations for surrogate tasks are "readily obtained using off-the-shelf vision models" (line 172) but does not specify which models were used or the quality/noise level of these annotations, affecting reproducibility.
- The "top-down cross-attention" framing (Eq. 5-8) is essentially standard Flamingo-style gated cross-attention, which the paper properly cites. The framing is fine but the reviewer's confusion suggests the novelty of this mechanism is overstated.

## Nice-to-Haves

- Report quantitative accuracy on the surrogate tasks themselves (detection, re-identification, tracking) to establish that the model genuinely learns low-level visual skills.
- Replace object-level surrogate tasks with random text completions as a control to distinguish "grounded content" from "extra supervision."
- For the w/o Surrogate ablation, control for total training tokens (pad with generic text tokens) and train for more steps to rule out training under-convergence.
- Probe the cross-attention mechanism to show what visual features are extracted with vs. without surrogate training.
- Include Loci in the CATER static camera table for full transparency.

## Removed Points

*These points were flagged to be removed; treat them with caution.*

- **Criticism about leaderboard being "unverifiable from the paper":** The paper provides a URL to the STAR leaderboard (line 414). Per review guidelines, cited entities are assumed to exist; this criticism reflects a reviewer knowledge gap, not an author error.
- **Claim that comparing to Video-ChatGPT and OpenFlamingo is "unfair":** The paper's primary baselines are task-specific methods (ALOE, STIN+OIE+NL). The Video-ChatGPT and OpenFlamingo comparisons are secondary context showing that general video QA models fail without grounding. The main conclusions do not rest on these comparisons.
- **Criticism about missing ORViT or scene-graph baselines in related work:** Per review guidelines, "missing related works" should not be flagged without external confirmation of their existence.
- **Claim that the paper "does not specify how ground-truth annotations are obtained":** The paper states annotations are "readily obtained using off-the-shelf vision models" (line 172) and provides citations. This is standard practice for this type of work.
- **Claim that the cross-attention mechanism is unoriginal (just Flamingo-style):** The paper properly cites Flamingo for cross-attention layers. The contribution is not the cross-attention mechanism itself but its integration with surrogate task training.
- **Strength from Strength Finder about "ablations isolate causal contribution":** This strength conflicts with verified weakness #1 (the ablation does not isolate grounding vs. token-level supervision). When strength and weakness disagree, the weakness wins.

## Novel Insights

The most interesting pattern across the four benchmarks is the highly variable impact of removing surrogate tasks — from a catastrophic 60-point drop on ACRE to a moderate 12-point drop on Something-Else. This suggests the surrogate tasks may serve different functions depending on the dataset: on ACRE (causal induction from static images), the re-identification surrogate may essentially be doing most of the "reasoning" work (matching objects across context trials), while on Something-Else (compositional action recognition from videos), the tracking surrogate provides a smaller marginal benefit because motion features are also captured by the spatiotemporal encoder. If this interpretation is correct, it would mean surrogate tasks are most valuable when the visual reasoning problem can be substantially decomposed into the surrogate's output — which is a more modest claim than "instilling low-level visual capabilities." The paper would benefit from engaging with this interpretation.

## Suggestions

1. **Rename the encoder.** Drop the "two-stream" terminology and describe it as a "divided space-time attention encoder" or "spatiotemporal video encoder." This would align the description with the actual architecture and avoid misleading readers.

2. **Add quantitative surrogate task evaluation.** Report the model's accuracy on detection, re-identification, and tracking tasks. Show that these correlate with final reasoning accuracy (e.g., by binning examples by surrogate accuracy).

3. **Run a token-count-controlled ablation.** When removing surrogate tasks, pad with an equal number of generic text tokens to control for sequence length and training budget. Train the w/o Surrogate model for more steps to verify convergence.

4. **Add a "random text" ablation.** Replace object-level surrogate content with random text completions (e.g., "the quick brown fox jumps over the lazy dog") to test whether the specific content of surrogate tasks matters or whether any extra token-level supervision suffices.

5. **Acknowledge the CATER static camera gap honestly.** Add Loci to Table 3 and note that LRR is second-best on this split. Revise the abstract to say "surpasses task-specific methods on most tasks" rather than "across tasks."

6. **Add a STAR data-controlled ablation.** Train a version of the model with the same additional data (Kinetics, Moments in Time, Something-Else) but without surrogate tasks to isolate the LRR framework's contribution from the benefit of additional training data.

7. **Report multiple seeds and learning curves** for the w/o Surrogate ablation, especially on ACRE where the collapse is extreme.

## Score and Decision

The paper proposes an interesting and practically-motivated framework, with strong empirical results across multiple challenging benchmarks. However, its central claim — that surrogate tasks provide "grounding" in low-level visual capabilities — is not adequately supported by the evidence. The key ablation is confounded (it removes tokens, not grounding), surrogate task accuracy is never measured, and the widely varying ablation gaps across datasets are unexplained. Combined with the overstated "two-stream" terminology and selective baseline presentation, these issues prevent the paper from fully establishing its claimed contributions in its current form. The empirical results suggest the approach has genuine value, but the evidence does not yet support the specific mechanism the paper proposes.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>