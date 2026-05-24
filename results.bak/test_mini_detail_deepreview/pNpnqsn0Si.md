Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper introduces **Thoughtbubbles**, a transformer variant that learns to fork (clone) or delete residual streams during pretraining using only the language-modeling objective. The core idea is that each residual stream carries a learned cumulative score; tokens with high scores get forked into additional parallel streams ("bubbles") for extra computation, while low-scoring streams are pruned. Attention and residual updates are attenuated by these scores (Eqs 8–10), providing a training signal. The paper evaluates Thoughtbubbles at 150M–772M parameter scales on two pretraining corpora (OpenWebText, peS2o) and reports perplexity improvements along with zero-shot scores on LAMBADA, HellaSwag, BLiMP, and PIQA.

## Strengths

1. **Novel architectural mechanism for adaptive parallel computation.** The forking-and-attenuation design is genuinely novel. Unlike pause-token methods that insert predefined thinking tokens, Thoughtbubbles dynamically grows and shrinks the set of residual streams based on learned scores. This is a creative architectural contribution that differs from both recurrent-depth methods (Universal Transformers) and explicit token-insertion methods.

2. **Consistent empirical improvements across scales and metrics.** Table 1 shows that Thoughtbubbles (κ=4L) achieves the lowest validation perplexity on both OpenWebText and peS2o at all three model scales (150M, 319M, 772M), and improves LAMBADA and HellaSwag over both the parameter-matched baseline and the computation-matched copy-5 baseline in nearly every setting (e.g., OpenWebText 772M: perplexity 19.74 vs. baseline 21.22; LAMBADA 29.4 vs. 23.9). The improvements are consistent across 6 model-scale/dataset combinations, not cherry-picked.

3. **Interpretable computation allocation.** Section 5 provides evidence that forked tokens are meaningfully used: Figure 4 shows the parent token attends to its child forks with attention scores an order of magnitude higher than to unrelated tokens, and Figure 5 shows a correlation between output-distribution entropy and fork count (both measured from the forking model and an independent baseline LM). This demonstrates that the learned allocation is qualitatively sensible and driven by token difficulty.

4. **Parameter efficiency demonstrated.** The 319M Thoughtbubbles (κ=4L) achieves lower perplexity on OpenWebText (20.23) than the 772M vanilla baseline (21.22), suggesting that adaptive parallel computation can partially substitute for additional parameters — an interesting practical finding.

## Weaknesses

### Fatal
None.

### Major

1. **No variance reporting or multiple seeds.** All results in Table 1 are single-run numbers without error bars, confidence intervals, or multiple seeds. For a paper making empirical claims of superiority across multiple tasks and scales, this absence is significant. Given the modest gaps in some settings (e.g., HellaSwag differences of 0.3–1.0 points), it is not possible to assess whether the reported gains are reliable or within noise. Multi-seed experiments (at least 3) for the main settings (319M and 772M on OpenWebText) are needed to substantiate the claimed improvements.

2. **Gradient flow through the forking decision is only partially explained.** The scores are trained through the attenuation mechanism (Eqs 8–10), which provides a gradient signal: the cumulative scores modulate attention probabilities and residual updates, so gradients from the LM loss flow back to the scores. However, the top‑k decision itself (Eqs 5–6) that determines *which* token streams survive is a hard, discrete operation with no explicit differentiability. The paper acknowledges this as a "Top‑K Gradient Bottleneck" in the Limitations section (lines 382), noting it can cause deep‑layer dropout effects. While the scores do receive training signal via attenuation, a clearer explanation of how the model learns to make *correct forking decisions* (beyond just having high scores) would substantially strengthen the paper. A control experiment comparing against random forking with the same budget would directly test whether the *learned allocation* (rather than just having extra streams) drives the improvement.

### Minor

3. **The 319M vs. 772M comparison needs contextualization.** The paper highlights that "our approach at a 319M parameter scale has lower perplexity on OpenWebText than the baseline approach at the 772M scale" as evidence of scaling superiority. All models were trained for only 2.5B tokens — far below the Chinchilla-optimal ~15B tokens for a 772M model, and below the ~6B for a 319M model. The 772M baseline is thus more severely undertrained relative to its capacity. This does not invalidate the comparison (both models face the same data constraint), but the framing as a "scaling advantage" overstates the result. The paper should acknowledge this confound and present the result as a parameter-efficiency observation under data-limited conditions.

4. **Mixed performance on BLiMP and PIQA.** Thoughtbubbles frequently *underperforms* the copy-3 baseline on BLiMP (e.g., peS2o 772M: 67.4 vs. 73.3; peS2o 319M: 68.6 vs. 71.8). Results on PIQA are often comparable or slightly worse than the baseline. The paper notes this briefly ("pruned dynamic parallel computation may not be as helpful for syntax"), but does not analyze why. This limits the generality of the claim that adaptive parallel computation is broadly beneficial.

5. **Evaluation scale is modest.** Models are trained up to 772M parameters for only 2.5B tokens, limiting the conclusions that can be drawn about scaling behavior. The paper acknowledges this for hard reasoning tasks (GSM8k, etc.), but the overall scope constrains the impact of the empirical findings. Wall-clock times, FLOPs counts, and memory usage are not reported despite the efficiency motivation in the introduction.

### Trivial
None.

## Nice-to-Haves

- An ablation comparing the learned forking against random forking with the same budget would directly isolate whether the *learned allocation* is responsible for improvements, rather than simply the availability of extra streams.
- Reporting variance over 3 seeds for the main experimental conditions (319M and 772M on OpenWebText) would substantially increase confidence in the results.
- A FLOPs or wall-clock comparison alongside the perplexity results would strengthen the practical motivation.

## Removed Points

These points from the input reviews are excluded for the following reasons:

- Harsh Critic's claim that the forking decision has "no gradient path" and "undermines the core contribution" — **Overstated.** The paper describes a clear gradient path through the attenuation mechanism (Eqs 8–10). The scores do receive gradients. The top‑k bottleneck is acknowledged in the Limitations section. The criticism is downgraded from fatal to major above.
- Harsh Critic's criticism of the "first-known" claim — **Not a valid weakness.** The claim is specifically about "unsupervised dynamic allocation of latent *parallel* computation," which differs from Universal Transformers (recurrent depth) and pause-token methods (manual insertion). The paper's claim is appropriately scoped.
- Harsh Critic's complaint about forking layer placement (3, 7, 11) being deferred to appendix — **Parser artifact.** This is a design choice discussed in the deferred appendix, common in conference papers.
- Harsh Critic's complaint about missing appendix/hyperparameters — **Parser artifact.** These sections exist in the original submission.
- Harsh Critic's characterization of copy baselines as "weak" and the BLiMP analysis being insufficient — These are retained (merged into the minor weaknesses above) but downgraded from the harsh critic's framing.
- Strength Finder's generic strengths ("important problem", "interesting question") — Removed as they lack specific, concrete content tied to evidence in the paper.
- Strength Finder's claim about "Parameter-efficiency" — Retained as it is supported by Table 1.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation that the authors have not already made.

## Suggestions

1. **Add multi-seed results** for at least the main comparison settings (319M and 772M on OpenWebText) with mean and std. This single change would significantly strengthen the empirical claims.

2. **Include a random-forking control.** Forking with the same budget but using randomly assigned scores would test whether the *learned* allocation (rather than just having extra computational streams) drives the improvements. This experiment is the cleanest way to address doubts about the training signal for forking decisions.

3. **Acknowledge the undertraining confound** when comparing the 319M Thoughtbubbles against the 772M baseline. Add a brief discussion of how the comparison changes under Chinchilla-optimal training.

4. **Add efficiency metrics.** Report wall-clock time, FLOPs, or memory usage for at least one representative setting to support the efficiency motivation in the introduction.

## Score and Decision

### Calibration Summary

**Round 1 (Bracketing):** I queried three bands on topics related to transformer architecture, adaptive computation, and pretraining:
- Low band (avg < 3.5): returned papers scoring 2.0–3.25 (e.g., decentralized training, PDE simulation) — Thoughtbubbles is clearly stronger.
- Middle band (3.5 < avg < 7.5): returned papers scoring 4.5–6.67 (DyST 6.67, Hyper-UT 5.0, CoTFormer 5.75) — Thoughtbubbles sits in this band.
- High band (avg > 7.5): returned papers scoring 7.6–8.0 (DEPT 8.0, SAR diffusion 8.0) — Thoughtbubbles is clearly weaker on experimental rigor.

**Initial bracket: [4.5, 7.5].**

**Round 2 (Narrowing):** I queried inside the bracket with more specific queries. Key anchors:
- **CoTFormer** (5.75, scores: 6,5,6,6): Most thematically similar (adaptive computation architecture). CoTFormer had concerns about insufficient empirical comparison to standard transformers and limited scale. Thoughtbubbles has more thorough evaluation (3 scales × 2 datasets × multiple tasks) and greater architectural novelty, but shares similar concerns about single runs and limited scale. **Thoughtbubbles is slightly stronger.**
- **Zoology** (6.33, scores: 8,3,8): More rigorous (multiple runs, theoretical analysis) but different topic. Thoughtbubbles is less rigorous experimentally. **Thoughtbubbles is weaker.**
- **Hyper-UT** (5.00): Related topic (adaptive computation) but weaker experimental validation. **Thoughtbubbles is clearly stronger.**

The paper is between CoTFormer (5.75) and Zoology (6.33) — closer to CoTFormer on experimental rigor but closer to Zoology on novelty. Given the genuine architectural contribution but significant gaps in experimental methodology, the score lands at **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>