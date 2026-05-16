Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper studies client-side detectability of malicious server (MS) attacks in federated learning. It introduces D-SNR, a metric to detect example-disaggregation attacks in gradient space, and shows that all prior MS attacks are detectable via principled checks. The paper then proposes HIPS, a novel MS attack framework that uses a secret decoder (disaggregator + reconstructor) jointly trained with the shared model via SGD on auxiliary data, avoiding handcrafted modifications and operating in a hidden space rather than original gradient space. Experiments demonstrate successful data reconstruction from batches up to 512 and under secure aggregation, with D-SNR values in the natural range.

## Strengths

1. **Novel D-SNR metric provides a principled basis for detecting example-disaggregation attacks.** The metric is well-defined (Eq. 1) and grounded in the observation that effective disaggregation must leave a detectable signature in the gradient space. Figure 1 shows a clear separation between successful attacks (high D-SNR) and natural networks (low D-SNR), and the paper correctly notes that D-SNR detects *vulnerability* rather than *maliciousness* — which is desirable behavior.

2. **HIPS is a genuinely novel attack design that sidesteps both forms of detectability identified in prior work.** The key insight — disaggregating data in a secret decoder's hidden space rather than the original gradient space — is a clean fix to the fundamental limitation of prior example-disaggregation attacks. Jointly training the shared model, disaggregator, and reconstructor with SGD on auxiliary data also avoids the weight-space-detectable handcrafted modifications of boosted-analytical attacks. Figure 1 confirms HIPS operates at low D-SNR values indistinguishable from natural networks.

3. **Strong experimental results under realistic, previously challenging settings.** HIPS achieves high reconstruction success (up to 98.6% on CIFAR10/100 with PSNR up to 30) for batch sizes up to 512 — settings where honest attacks fail entirely. Under secure aggregation (C=4 or C=8 clients), it still obtains average PSNR >25. The ImageNet results (PSNR-All 21.9, 82.1% Rec, B=64) are significant since stealing single ImageNet images is impossible for honest attacks without restrictive assumptions.

4. **Systematic formulation of necessary requirements for practical MS attacks.** The paper's categorization of prior attacks into "boosted analytical" and "example disaggregation" classes, identification of root-cause detectability (weight-space vs. gradient-space), and distillation into four necessary requirements (Section 3) provides a conceptual framework for the field that goes beyond the specific attack.

5. **Local property mechanism substantially improves single-image isolation probability.** The local (in-batch) property setting achieves P(|I_rec|=1) > 0.9 for batches up to 512, a large improvement over the 1/e bound of prior work. This enables single-round data theft most of the time, an important practical improvement.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core contributions — the detection analysis, the HIPS attack framework, and the experimental validation — are all present and supported. The weaknesses below are addressable and do not threaten the paper's central claims.

### Minor

1. **Detectability evidence for HIPS could be more quantitative.** The paper relies on Figure 1 to show that HIPS-trained networks have low D-SNR values, but provides no summary statistics (mean, variance, or statistical test comparing HIPS to natural networks) in the main text. While the visual evidence is useful, reporting mean ± std D-SNR across multiple runs would be more convincing. Additionally, the weight-space detectability argument (that SGD-trained weights avoid handcrafted modifications) is conceptually sound but lacks empirical verification (e.g., showing weight distributions, filter norms, or correlation statistics are within normal ranges). Adding such analysis would strengthen the paper's central detectability claim.

2. **The local property mechanism could be explained more clearly.** The paper states (Section 4.1) that BN intertwines the computational graphs of images, enabling local property selection, but does not fully explain the mechanism by which the server's disaggregator can reliably identify which gradient component corresponds to the image satisfying the property at attack time. The server trains on auxiliary data where it knows which image satisfies P, and the model learns to encode gradients such that the disaggregator can extract the right example — but the causal chain from "BN intertwines the batch" to "disaggregator isolates the target" is left implicit. A brief algorithmic illustration or concrete example would resolve this.

3. **Comparative claim about ImageNet PSNR lacks direct baseline numbers in the main text.** The paper states (Section 5) that HIPS's ImageNet PSNR "is higher than the state-of-the-art attack in Fishing" but does not show Fishing's reported PSNR in the main paper for side-by-side comparison. (The appendix, which was stripped by the PDF parser, contains this comparison via `\input{src/app_fishing_compare_exp}`.) Including the baseline numbers in the main text — even as a brief parenthetical — would make the comparison self-contained.

4. **No hyperparameter sensitivity analysis in the main text.** The tradeoff parameter α (balancing reconstruction and nullification losses) and the disaggregator dimension n_d are not ablated in the main body (deferred to appendix). Given that the two losses are at odds, some sense of α sensitivity in the main text would help readers assess the method's robustness.

5. **Rec threshold (PSNR > 19) is on the low side.** While the paper cites a reference for this threshold, 19 PSNR corresponds to perceptually lossy reconstructions. Reporting complementary metrics (SSIM/LPIPS) alongside in the main text (currently deferred to appendix) would give a more complete picture of reconstruction quality.

6. **The claim about detecting "all future" example-disaggregation attacks is somewhat speculative.** The conceptual argument (disaggregation must happen in gradient space, hence D-SNR will detect it) is reasonable, but the paper acknowledges this limitation implicitly by noting D-SNR detects *vulnerability* rather than *maliciousness*. The wording could be slightly softened without losing impact.

### Trivial

- The dimensionality n_d of the secret linear map is not specified in the main text; a typical value would help.
- The claim that HIPS "does not require restrictive assumptions such as... knowledge of batch normalization data" is slightly incomplete — it does rely on BN being present in the architecture, which is a mild but real assumption that should be explicitly acknowledged as such.

## Nice-to-Haves

- An ablation showing attack performance vs. auxiliary data quantity in the main text (currently in appendix referenced as `sec:app_size_data`).
- Visual reconstructions for CIFAR (Figure 2 right shows ImageNet; CIFAR examples are referenced but not shown as a figure).
- A more thorough threat-model discussion of other potential gradient-space checks (e.g., gradient norm distributions across layers, covariance patterns) that might detect HIPS-like attacks, to contextualize the strength of the D-SNR-based argument.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"No direct comparison to prior attack methods in main text"** — The paper includes `\input{src/app_fishing_compare_exp}` in the appendix, which the PDF parser strips. The appendix comparison exists in the original submission. The main text makes a comparative claim (ImageNet PSNR higher than Fishing) — the only issue is that the Fishing baseline numbers are not in the main body, which is a minor presentation point (addressed above as Weakness #3). The paper's primary comparison to prior work is on *detectability*, which is done in Figure 1, not on raw reconstruction quality, so the "critical omission" framing is overstated.

2. **"D-SNR is always ∞ for Fishing attacks... unclear whether modified attack is representative"** — The paper explicitly acknowledges modifying Fishing and explains why this is necessary (D-SNR is always ∞ for the unmodified attack). This is a standard methodological approach (using a controlled variant to probe the decision boundary) and is clearly explained. No weakness here.

3. **"CIFAR-100 and ImageNet numbers not tabulated"** — These are described in text, which is standard practice for supplementary results. The table in the main text focuses on CIFAR-10; full results are in the appendix.

4. **"Secure aggregation results without a baseline with the same setting"** — The paper's comparison is against the theoretical 1/e success probability of prior global-property approaches, which is the appropriate baseline for the property-selection component. The absolute reconstruction quality (PSNR > 25) speaks for itself.

5. **"No sensitivity analysis for key hyperparameters... in main text"** — This is a common and acceptable pattern for conference papers; hyperparameter studies go in the appendix due to space constraints. Acknowledged as a minor weakness above (#4) but not a structural flaw.

6. **Various section-by-section stylistic nitpicks** about what "should" be included — these are either addressed in the appendix (which is stripped) or represent scope-creep demands.

## Novel Insights

Beyond the paper's own contributions, the reviews surface the point that the paper cleanly identifies *why* prior MS attacks are detectable at a principled level: they all depend on the server having no informational advantage over the client in the gradient space (for disaggregation attacks) or on making handcrafted modifications (for analytical attacks). The key insight — that a secret decoder operating in a low-dimensional null-space projection can break this symmetry — is a genuinely new design principle for MS attacks. The reviews also highlight that the local-property trick exploiting BN intertwining is clever but undertheorized; a formal analysis of why BN enables this would be a useful follow-up.

## Suggestions

1. Add a short quantitative statement about HIPS detectability: mean ± std D-SNR for HIPS vs. natural networks vs. prior attacks, and optionally a statistical test (e.g., Kolmogorov-Smirnov).
2. Expand the explanation of the local property mechanism by adding one paragraph or a brief algorithm step showing how BN intertwining enables the disaggregator to learn which example in the batch satisfies P, using the auxiliary training data.
3. Include the Fishing baseline PSNR numbers in the main ImageNet discussion (even as a parenthetical).
4. Add a brief α sensitivity study to the main text (e.g., a small table or a sentence summarizing the appendix findings).

## Score and Decision

This paper presents a novel MS attack framework with sound methodology, a principled detection analysis, and strong experimental results under challenging settings. The weaknesses are addressable and do not undermine the core contributions. The paper makes a meaningful contribution to the FL security literature.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>