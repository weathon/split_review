Now I have sufficient calibration data. Let me write the final consolidated review.

---

## Summary

Thoughtbubbles introduces a transformer variant that learns to fork (duplicate) or delete residual streams during pretraining, enabling dynamic allocation of parallel computation in latent space. The architecture uses cumulative scores to decide which tokens get extra parallel residual streams, with attention and residual updates attenuated by these scores to train the allocation. Experiments across 150M–772M parameters on OpenWebText and peS2o show consistent perplexity improvements over parameter-matched and computation-matched baselines, including the striking result that a 319M Thoughtbubbles model achieves lower perplexity than a 772M baseline transformer.

## Strengths

- **Novel architecture for unsupervised dynamic parallel computation during pretraining.** The core idea — learning to fork/delete residual streams using cumulative scores trained via attention attenuation, with no supervision beyond the language modeling loss — is genuinely novel. This is the first architecture that enables dynamic allocation of parallel latent computation from pretraining, as opposed to CoT/pause-token methods that insert serial computation at inference time. (Abstract, Section 2)

- **Consistent and substantial perplexity improvements across all scales and datasets.** Table 1 shows Thoughtbubbles (κ=4L) beating both the baseline transformer and the computation-matched Copy-5 baseline on every dataset/scale combination for perplexity. The 772M model achieves 19.74 vs. 21.22 for the baseline on OpenWebText. More strikingly, the 319M model (20.23) outperforms the 772M baseline (21.22), a cross-scale result that directly demonstrates the benefit of dynamic forking beyond simply scaling parameters. (Table 1, Figure 3)

- **Outperforms non-adaptive computation-matched baselines.** The Copy-3 and Copy-5 baselines (which naïvely duplicate every input residual) provide a controlled test: the gap between Thoughtbubbles (κ=4L) and Copy-5 on OpenWebText 772M (19.74 vs. 20.90) shows that adaptive allocation — pruning low-importance streams while allocating extra streams to important tokens — is more effective than blindly duplicating all streams. (Table 1)

- **Interpretable allocation pattern emerges without supervision.** Figure 5 shows that the model allocates more forks to tokens with higher output entropy, measured both by the forking model itself and by an independent baseline LM. This non-trivial, interpretable pattern (concave parabolic relationship) emerges purely from the language-modeling loss. (Section 5, Figure 5)

- **Attention analysis confirms forks actively participate in parent token computation.** Figure 4 shows the parent ("og") token attends to its child forks with scores an order of magnitude higher than to sibling tokens or other context tokens, validating that the forked residuals meaningfully influence the parent's residual update. (Section 5, Figure 4)

## Weaknesses

### Major

- **Gradient flow through discrete forking decisions is underspecified.** The method uses a hard top-*k* operation to select which streams survive (Eq. 5–6), creating a non-differentiable boundary. The paper describes the attention attenuation mechanism (Eq. 8–10) for training the scores but never explicitly states how gradients pass through the discrete selection. The scores of surviving streams do receive gradients through the differentiable attention computation (Eq. 8 uses log(*P*) as a softmax bias and *P* to scale *V*, both differentiable), and the limitation section acknowledges the "Top-K Gradient Bottleneck" for dropped streams. However, the paper should clearly state that: (a) the training signal flows through the attenuated attention mechanism, not through the top-*k* itself, and (b) streams dropped by top-*k* receive no gradient (an acknowledged limitation). Without an explicit description, the method's training soundness requires inference from equations rather than being clearly stated.

- **Forking layer positions are manually chosen (layers 3, 7, 11), constraining the adaptivity claim.** The paper places forking layers at fixed depths and notes that "for models with more layers, the majority of the latter half of transformer will contain no forking" (Section 3.1). This means the model cannot learn *where* to allocate extra computation — only *how many* streams to fork at predetermined locations. This does not invalidate the contribution (the dynamism is about per-token allocation, not per-layer placement), but the paper's framing of "dynamic allocation" and its critique of pause tokens (which require manual insertion locations) would be more appropriately qualified. The paper defers justification to Appendix B (not available in the review text).

- **No confidence intervals or variance reported.** All results in Table 1 are single numbers. Several zero-shot gains are small (e.g., HellaSwag 30.6→31.1 for 772M OWT), and tasks like BLiMP and PIQA show inconsistent results where baselines sometimes outperform Thoughtbubbles. Without variance estimates, it is unclear which improvements are reliable and which may reflect training noise. While single-run pretraining is common at this scale due to cost, the lack of any uncertainty quantification weakens the evidence for the smaller-magnitude claims.

### Minor

- **No experimental comparison against pause-token baselines.** The related work section discusses pause tokens (Goyal et al., 2024; Herel & Mikolov, 2024; Sun et al., 2025) and critiques their limitation of inserting computation "prior to computation." However, no experimental comparison against any pause-token baseline is provided. The Copy-3/5 baselines serve as computation-matched controls but do not test the specific claim about forking *within* the forward pass vs. pre-pended pause tokens.

- **Zero-shot gains are inconsistent across tasks; BLiMP and PIQA often underperform baselines.** On OpenWebText 772M, Thoughtbubbles (κ=4L) achieves 81.6 on BLiMP vs. 81.2 for Copy-3 and 79.6 for baseline — a small gain. On some configurations (e.g., 319M OWT), baseline (79.0) and Copy-3 (80.5) outperform Thoughtbubbles (78.8). PIQA results are mixed, with baseline often comparable or better. The paper attributes this to "short training" (Section 4), but the same training was sufficient for consistent perplexity and LAMBADA/HellaSwag gains, making this explanation incomplete.

### Trivial

- The conclusion claims "our method at 319M outperformed baselines at 772M scale" without noting that this applies to perplexity only — zero-shot gains at 319M are much smaller than the parameter scaling gap would suggest.
- The paper states that "all scores (keep, fork, cumulative) are implemented in log-space for stability" (Section 2.3) but presents all equations in probability space, making the exact training procedure slightly ambiguous.

## Nice-to-Haves

- An ablation comparing adaptive vs. non-adaptive (fork every token to max budget) Thoughtbubbles would directly test the value of the adaptivity mechanism.
- A discussion of sensitivity to the choice of forking layer positions (3, 7, 11) and whether these positions matter.

## Removed Points

- **Harsh critic's point about gradient issue being "fatal" / "structural flaw."** This is downgraded to Major because the paper *does* describe a training mechanism: the attention attenuation (Eq. 8–10) provides gradients to surviving scores. The paper never says "no mechanism for training" — it just does not frame the mechanism in explicit gradient-flow terms. The limitation section also acknowledges and discusses the gradient bottleneck for dropped streams.
- **"The method as described cannot learn the forking scores."** This overstates the problem. Scores receive gradients through the differentiable attenuation mechanism. The paper describes this implicitly through the equations, though it should be more explicit.
- **Strength Finder's generic strengths about "important problem" and "well-written."** These are superficial and do not add specific evidence.
- **Request for "more models" or "larger dataset."** The current scale (150M–772M, 2.5B tokens) is adequate for demonstrating the method's viability.

## Novel Insights

None beyond the paper's own contributions. The review triangulation surfaces no genuinely new observation about the method that the paper itself does not already make.

## Suggestions

1. **Explicitly describe gradient flow in the main text.** State that the attention attenuation mechanism (Eq. 8) provides differentiable gradients to the cumulative scores of surviving streams, that the top-*k* is non-differentiable but only gates which streams continue, and that dropped streams receive no gradient signal (the "Top-K Gradient Bottleneck" acknowledged in limitations). A brief training pseudocode or gradient flow diagram would help.

2. **Report confidence intervals or multiple-seed runs for the main zero-shot results**, especially given the small-magnitude and inconsistent gains on BLiMP and PIQA.

3. **Add a pause-token baseline** or at minimum discuss why the Copy baselines are the more appropriate comparison. If adding baselines is infeasible, qualify the related-work critique accordingly.

4. **Ablate the adaptivity** by comparing against a "fork-all" version where every token receives the maximum budget. This would directly test whether the score-based pruning is beneficial beyond simply having more streams.

5. **Add a comparison of standard transformer vs. Thoughtbubbles at matched FLOPs** (rather than matched parameters). The paper uses Copy-5 as a FLOPs-matched baseline, but showing the parameter-matched transformer at comparable inference FLOPs (via larger width/depth) would strengthen the scaling claims.

## Score and Decision

**Round 1 bracketing:** The paper sits between weak anchors (avg ~3.0, rejected papers with vague or undersupported claims) and strong anchors (avg ~8.0, papers like Differential Transformer with clean innovations and thorough evaluations). Initial bracket: between 5.5 and 7.5.

**Round 2 narrowing:** 
- CoTFormer (5.75): similar adaptive-computation goal but weaker empirical results. Thoughtbubbles shows more consistent perplexity gains and a more novel mechanism.
- Hyper-Connections (6.25): clean architectural improvement with strong results. Thoughtbubbles has higher novelty in its core mechanism but less polished exposition.
- Selective Attention (6.75): simple, well-executed modification with strong efficiency claims. Thoughtbubbles is architecturally more ambitious but less thoroughly evaluated.
- KAT (6.80): KAN-based architecture with solid evaluation. Thoughtbubbles is comparably novel but has more significant methodological ambiguities.

Final score: **6.5**. The paper is carried by a genuinely novel idea and consistent perplexity improvements, including the striking cross-scale result. However, the underspecified gradient flow, manually chosen forking positions, absent variance reporting, and inconsistent zero-shot gains hold it back from the 7+ range.

**Decision: Accept**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>