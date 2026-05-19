- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 6, 5
Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper proposes SelfEval, an automated method for evaluating text-to-image diffusion models that uses the generative model itself to estimate likelihoods of real images given text prompts, thereby avoiding reliance on external discriminative models (CLIP, LLMs) for evaluation. The method converts the diffusion model into a classifier for image-text matching tasks on standard recognition benchmarks (TIFA, ARO, CLEVR) and shows that the resulting accuracy rankings correlate with human pairwise evaluations of generated images.

## Strengths

1. **Novel evaluation paradigm that eliminates external-model dependency and biases**: The paper systematically documents how existing metrics (CLIPScore, MID, VPEval, LLMScore) are sensitive to the choice of external model — e.g., Table 2 shows MID rankings reverse when using ViT-B/32 vs ViT-L/14 backbones, and Figure 1 (left) shows CLIP-score rankings of two LDMs flip depending on the CLIP model used. SelfEval avoids these issues by using only the generative model itself, and this is a clean, principled motivation.

2. **Demonstrates agreement with human evaluations across multiple model types and tasks**: Figure 2 shows that for four different diffusion models (pixel vs latent, CLIP vs T5 encoders), the relative ordering given by SelfEval's accuracy aligns with pairwise human evaluation results. Figure 6 (Spearman correlation) shows SelfEval is the only metric among five that exhibits positive correlation with human ratings for *both* pixel diffusion models (PDM) and latent diffusion models (LDM), while all other metrics show negative correlation on at least one model type.

3. **Achieves non-zero image-score on Winoground where a competing likelihood-estimation method fails**: Table 1 shows that the ELBO-based approach of Li et al. (2023) obtains 0 image score on Winoground, whereas SelfEval obtains 7.25 (LDM-CLIP) and up to 14.00 (PDM-CLIP). This demonstrates a concrete improvement over the prior method with the same goal of using diffusion models for image-text matching.

4. **Enables fine-grained diagnostic evaluation**: SelfEval constructs a six-task benchmark covering attribute binding, color, counting, shape, spatial relationships, and text corruption. The results in Tables 3–4 and Figure 2 reveal fine-grained patterns — e.g., CLIP-encoder models perform near-random on counting while T5-encoder models do not, and pixel vs. latent diffusion models differ systematically — providing a level of diagnostic detail that single-score metrics like CLIPScore cannot offer.

## Weaknesses

### Fatal
None.

### Major

1. **The claimed likelihood lower bound (Eq. 5) is not justified by the stated reasoning.** The paper writes (lines 178–181):
   
   `log(∑_{n=1}^{N} a_n) ≥ ∑_{n=1}^{N} log(a_n)`
   
   and attributes this to Jensen's inequality for concave functions. A correct application of Jensen (with log as a concave function, sampling a_n with probability 1/N) would yield:
   
   `log(∑ a_n) ≥ (1/N) ∑ log(a_n) + log(N)`
   
   The paper's inequality differs by both a missing 1/N factor on the sum of logs and a missing additive log(N) term. As a result, the claimed lower bound on `log p(x₀|c)` does not hold in general under the reasoning provided. This means the theoretical foundation of the method — that the computed quantity is a principled lower bound on the likelihood — is not valid as written. 
   
   **Why it matters but is not fatal**: The practical method involves computing `s(c) = ∑_{n} (log p(x_T^n) + ∑_t log p(x_{t-1}^n | x_t^n, c))` and using it for relative comparison (ranking captions). Since N is constant across all captions for a given image, the missing 1/N factor and log(N) additive term would affect all captions equally, so the ranking could still be correct. However, the paper frames the method as theoretically grounded, and this framing requires correction. The authors should either (a) provide a correct derivation of a likelihood bound for the specific Monte Carlo scheme used, or (b) explicitly reframe the score as a heuristic and provide alternative justification for why it works.

2. **The Spearman correlation evidence (Figure 6) is based on very few data points**. The Spearman correlation between metrics and human ratings is computed across only 5 tasks (5 data points per metric × 2 model types). With n=5, Spearman's ρ is extremely noisy (the critical value for p<0.05 one-tailed is approximately ±0.9). The paper's claim that "all metrics except Ours have a negative correlation" would be much more reliable with more tasks or per-task replication. The per-task binary agreement shown in Tables 1–2 (green/red cells) is more robust and is the stronger evidence in the paper.

### Minor

1. **Evaluation uses real images while the claimed target is text fidelity of generated images.** SelfEval computes classification accuracy on *real* image-text pairs from COCO, CLEVR, etc., while human evaluation (the gold standard) is performed on *generated* images. The paper argues that "text faithfulness inherently measures vision-language reasoning" (line 192–193), so discriminative performance on real images is a proxy. This is a reasonable but unproven assumption, and the gap is not directly closed — the paper validates that SelfEval rankings correlate with human rankings, but never runs SelfEval on generated images to test whether the metric works *because* it measures text faithfulness or because both tasks happen to rank models similarly. An experiment applying SelfEval to generated images (from the same prompts used in the human study) would directly address this concern.

2. **Derivation of the Monte Carlo estimate (Eq. 4) is missing a 1/N factor.** The Monte Carlo estimate of the integral in Eq. (3) should be `(1/N) ∑ ...` rather than `∑ ...` (lines 164–166). While this does not affect ranking (the 1/N factor is constant across captions for a given image), it is a technical inaccuracy that should be corrected alongside the Jensen issue.

### Trivial
None.

## Nice-to-Haves

- An analysis of how the bound tightness varies with N (number of noise samples) and T (diffusion steps) would help characterize when the approximation is reliable. The supplement is referenced but the main paper would benefit from a brief sensitivity note.
- Reporting CLIPScore evaluated on real images (not generated images) for the same benchmark would isolate whether SelfEval's advantage comes from using the generative model or simply from using real images.

## Removed Points

- *Harsh critic's claim that "the comparison with human evaluation is not properly calibrated" (no confidence intervals, vote normalization).* The paper reports per-task binary agreement (green/red cells) in Tables 1–2 and overall Spearman correlation in Figure 6. The vote tallies are used only to determine which model humans preferred per task — the actual comparison is the ranking agreement, not the vote magnitudes. This is a standard presentation. Removed as factually incorrect in its characterization of the evidence.

- *Harsh critic's claim that the paper overstates novelty ("first automated metric to show agreement").* The paper supports this claim: SelfEval agrees in 8/10 comparisons and is the only metric with positive Spearman for both PDM and LDM. CLIPScore agrees in 7/10 but has negative Spearman on LDM. This is a substantiated claim. Removed.

- *Harsh critic's section-by-section notes about missing appendix content, missing implementation details, and related work omissions.* Per instructions: appendix exists in original, missing related works cannot be verified.

- *Strength Finder's generic/delusional strengths (e.g., "addressed an important problem") or strengths that conflict with verified weaknesses.* Several such items filtered.

## Novel Insights

Beyond the paper's own contributions, the most interesting emergent observation from the reviews is the *asymmetry between PDM and LDM evaluation*. Existing metrics (CLIPScore, MID, VPEval, LLMScore) all show negative Spearman correlation with human ratings on latent diffusion models while being positively or weakly correlated on pixel diffusion models. SelfEval uniquely maintains positive correlation on both. This suggests that the distributional properties of latent-space representations affect external metrics in ways that are not yet understood, and that using the generative model itself for evaluation inherently avoids this confound. The paper documents this phenomenon but does not deeply explore *why* this asymmetry occurs.

## Suggestions

1. **Fix the mathematical derivation.** The most impactful fix is to either (a) correctly derive the lower bound using the standard ELBO or a valid Jensen inequality, or (b) reframe the computed quantity as a tractable score/approximation rather than a provable bound, and validate it empirically against alternatives.

2. **Directly address the real-vs-generated gap.** Re-run SelfEval on the images *generated* by each model for the same prompts used in the human evaluation. If SelfEval's ranking of its own model's generations matches human rankings, this would be the cleanest possible validation of the method.

3. **Add statistical confidence to the Spearman analysis.** With only 5 tasks, reporting bootstrap confidence intervals for the Spearman ρ would help the reader assess whether the observed correlations are reliable or within noise.

4. **Correct the Monte Carlo estimate** by adding the missing 1/N factor in Eq. (4) for technical accuracy.
