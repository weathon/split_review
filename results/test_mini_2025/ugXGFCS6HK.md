Now let me write the final consolidated review.

## Summary

This paper introduces "principal distortions," a method for comparing the local geometries of multiple (N ≥ 2) image representations by optimizing a pair of stimulus distortions that maximize the variance of the models' log sensitivity ratios under a novel pseudometric on Fisher information matrices. The method extends prior eigen-distortion work (N = 1) and generalized eigen-distortions (N = 2) to arbitrary N. Experiments on early visual models and deep neural networks (AlexNet, ResNet50, with standard, Stylized-ImageNet, and adversarial training) produce interpretable distortions that reveal differences in local sensitivity architecture versus training type.

## Strengths

1. **Clean mathematical generalization to N > 2 models.** The paper extends existing eigen-distortion and generalized eigen-distortion methods by defining a variance-maximization objective (Eq. 4) over a well-motivated pseudometric (Eq. 3). This is a principled and non-trivial extension of prior pairwise-only methods, and the connection to Fisher–Rao distance (Appx. A) gives it a firm information-geometric grounding.

2. **Consistent, cross-validated DNN findings.** The core DNN results (AlexNet vs. ResNet50 separation by architecture; standard vs. adversarial separation by training type) are replicated across 100 base images with error bars (Fig. 3E, 4A, 5A), across multiple random initializations (Supp. Fig. SI.5), and across controlled image manipulations (Supp. Fig. SI.6, SI.8). This reproducibility demonstrates that the optimization produces reliable patterns rather than noise.

3. **Novel empirical observations.** The finding that local geometric differences between AlexNet and ResNet50 are driven by architecture (not training data), while standard vs. adversarial training differences dominate architectural ones, is genuinely interesting and has not been documented in prior eigen-distortion literature. The spatial-frequency interpretation (high-frequency vs. low-frequency sensitivity) is a concrete, interpretable characterization.

4. **Efficiency argument is theoretically grounded.** The paper correctly identifies that prior methods scale as O(N) or O(N²) stimuli for N models, while principal distortions require only 2 stimuli per base image (plus an iterative elimination procedure scaling as O(log N)). This practical advantage is clearly stated and would be important for psychophysics applications.

5. **Honest about limitations.** The Discussion explicitly acknowledges the local linear approximation, the Gaussian noise assumption, and the qualitative nature of the human-perception comparisons, which inspires confidence in the authors' assessment of their method's scope.

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative comparison against alternative baselines for N > 2.** The paper's central claim is that principal distortions "optimally differentiate" multiple models, but the only baseline is random distortions (Fig. 2A), which is trivially beaten by construction. Neither of the two natural alternatives is tested: (a) eigen-distortions of a pooled/average FIM across models, or (b) aggregated pairwise generalized eigen-distortions (e.g., the two that maximize average disagreement across all pairs). Without such comparisons, the reader cannot assess whether principal distortions provide meaningful benefits over simpler approaches. Since the paper is positioned as a methods contribution, this gap substantially weakens the empirical case.

2. **Early visual model experiment lacks evidentiary value.** Section 4.1 presents a "qualitative comparison" that amounts to the authors visually inspecting images and declaring which models appear human-like (Fig. 2C). There are no human subjects, no psychophysical measurements, no forced-choice data, and no statistical test. The paper acknowledges this limitation but nonetheless uses the exercise to draw conclusions (e.g., "LGN model was the best"), and the legibility of the distortions is presented as a strength of the method. This section does not provide evidence for the method's utility; at best it illustrates a protocol for future psychophysics.

### Minor

1. **No quantitative measure of separation quality for the DNN claims.** The paper claims that principal distortions "organize the networks by architecture" (Fig. 3) and that "differences in local sensitivities depend more on differences in training procedure than architecture" (Fig. 5). These claims are supported only by visual inspection of log-ratio plots. A simple quantitative measure (e.g., between-group vs. within-group variance ratio, silhouette score, or ANOVA) would substantially strengthen the conclusions without requiring new data.

2. **Efficiency claim assumes sufficiency of two distortions.** The dramatic reduction to 2(N = 2) vs. O(N) / O(N²) stimuli is presented as a key advantage, but it assumes that two principal distortions capture enough variance to differentiate the models. If they do not, additional distortion pairs would be needed, eroding the efficiency gain. The paper does not report the fraction of variance captured or test whether two distortions are sufficient for the model sets studied.

3. **Practical optimization details are not discussed.** The gradient-based optimization procedure (referenced to Appx. B) is not characterized in the main text: no discussion of sensitivity to initialization, local minima, number of iterations, or computational cost (Jacobian computation across all models per iteration). For practitioners considering applying the method, these details matter.

### Trivial
None.

## Nice-to-Haves

- A computational cost analysis (runtime, memory) for the DNN experiments would help practitioners gauge scalability.
- Comparing principal distortions to global similarity measures (CKA, RSA, Procrustes) to show cases where local and global measures disagree would strengthen the motivation.
- A stability analysis showing the optimization converges to similar solutions across random seeds would address a natural concern.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The metric is image-specific, so averaging across images hides this issue"** (from Harsh Critic). The method is explicitly designed for local (per-image) comparison. Averaging across 100 images to show the pattern is robust across natural images is a strength, not a weakness. The paper never claims the metric is global. **Reason: misunderstands the paper's scope.**

2. **"The optimization algorithm is not described"** is raised as a major concern. The paper references "Appx. B" which was stripped by the PDF parser. The original submission contained this content. **Reason: parser artifact, not an author error.**

3. **Various style/formatting nitpicks** (typos, grammar) from the harsh critic's "Minor details" sections. These are all parser artifacts. **Reason: parser artifacts.**

4. **Missing related works / cannot verify existence of cited models.** We are instructed to assume all cited references exist. **Reason: violates hard rules.**

## Novel Insights

The most valuable insight from the reviews is that the paper's central weakness (lack of quantitative baselines) is directly addressable without changing the method: comparing principal distortions against eigen-distortions of a pooled FIM or aggregated pairwise generalized eigen-distortions would either confirm the method's value or reveal its limitations. The reviews also highlight that the early visual model experiment is currently a placeholder—converting it into a real psychophysical protocol (as the paper itself suggests for future work) would dramatically strengthen the contribution, but even a model-based surrogate (e.g., using one model as a "human proxy" and ranking the others) would be more informative than visual inspection.

## Suggestions

1. **Add baseline comparisons.** Compute log-sensitivity-ratio variance for (a) principal distortions, (b) top two eigen-distortions of the average FIM, and (c) two most-divergent pairwise generalized eigen-distortions. Show that principal distortions capture more model variance. This single addition would address the paper's most significant gap.

2. **Quantify separation.** Report a silhouette score, ANOVA F-statistic, or between-group/within-group variance ratio for the log-sensitivity-ratio patterns in Figs. 3–5. This would convert visual claims about "architecture drives differences" into measured claims.

3. **Report variance explained.** Report how much of the total pairwise variance is captured by the two principal distortions. If the fraction is high, the efficiency claim is supported; if low, this is important information for users.

4. **Remove or reframe the early visual model "comparison."** Either strip the human-perception claims and present Fig. 2 purely as a method illustration, or add even a simple computational oracle (e.g., treat one model as ground truth) to provide quantitative evidence.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing (topic: "Fisher information matrix distortion model comparison neural networks")**
- Weak anchors (score < 3.5): scores 1.50–3.00 — mostly rejected papers with fundamental flaws. Current paper is clearly stronger.
- Middle anchors (3.5 < score < 7.5): scores 4.25–6.25 — includes accepted and rejected papers with mixed evidence. Current paper fits here.
- Strong anchors (score > 7.5): scores 8.00–8.50 — oral/spotlight papers with extensive quantitative validation. Current paper is substantially weaker.

**Initial bracket: 4.5–6.5**

**Round 2 — Narrowing (topic: "local geometry comparison of neural network representations Fisher information" and "comparison of visual models psychophysics qualitative distortions")**
- Anchors in 4.5–6.5 range: scores 5.00 (×3), 5.25 (×2), 5.50, 6.00, 6.25, 6.33, 6.67
- Key comparison anchors read in full:
  - *"Differentiable Optimization of Similarity Scores Between Models and Brains"* (6.25, Accept Poster) — Had quantitative experiments, code release, and systematic analysis. Current paper has a cleaner mathematical contribution but much weaker empirical validation. Current paper is weaker.
  - *"Disentangling the Link Between Image Statistics and Human Perception"* (5.25, Reject) — Also used proxies for human perception and had qualitative results. Current paper has a stronger methodological contribution but similar validation gaps. Current paper is slightly stronger.
  - *"Assessing Visually-Continuous Corruption Robustness"* (5.50, Reject) — Had extensive human experiments (7,718 participants) but suffered presentation issues. Current paper has less quantitative evidence but a more novel methodology. Comparable.

**Final calibration:** The paper sits near the upper end of the rejected-anchor range but below the accepted-anchor threshold. Its mathematical contribution is genuine and the DNN findings are reproducible and interesting, but the lack of quantitative validation against baselines prevents it from reaching the acceptance standard for a methods paper. Score 5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>