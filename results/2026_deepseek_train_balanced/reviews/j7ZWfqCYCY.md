## Summary

This paper proposes (1) an Intra-Entropy Gap algorithm for detecting non-stealthy jailbreak attacks on VLMs, (2) a stealthiness-aware jailbreak attack using diffusion models that filters its own outputs through the entropy gap checker, and (3) an information-theoretic framing of the jailbreakability-stealthiness trade-off via Fano's inequality. Experiments evaluate detection across three attack methods on five VLMs (white-box and black-box settings).

## Strengths

- **Detection algorithm performs well on non-target attacks.** Algorithm 1 achieves AUROC 0.96–0.99 on HADES and 0.79–0.96 on MMSafetyBench (Table 1, lines 350–355), demonstrating that entropy-gap-based detection is effective for non-stealthy jailbreak attacks from prior work.

- **The proposed attack produces images with near-natural entropy distributions against the design-target detector.** Against Algorithm 1, the attack achieves AUROC 0.45–0.62 (near-random) across five scenarios, compared to 0.96–0.99 for HADES (Table 1). This empirically shows it is possible to generate jailbreak images whose entropy gap statistics match natural ImageNet images under this specific detection scheme.

- **Evaluation across multiple models and settings.** The paper tests on LLaVA, MiniGPT-4, InstructBLIP (white-box), Gemini, and ChatGPT 4o (black-box) (lines 263, 429–433), providing reasonable coverage of model types and access levels.

- **Attack does not require gradients.** Unlike several baselines (e.g., VisualAE, line 364), the proposed attack operates without gradient access yet achieves competitive white-box ASR — a practically relevant property for black-box threat models.

## Weaknesses

### Major

1. **The information-theoretic contribution is disconnected from empirical measurements.** Theorem 1 (lines 219–229) restates standard Fano's inequality without novel derivation, and the variables $X$, $Y_1$, $Y_2$ are never instantiated with measurable quantities from the experiments. Section 5.3 (lines 456–458) plots the inequality using *hypothetical* values of $H(X)$ (2–10 bits, chosen arbitrarily) against a profanity wordlist ($|\mathcal{X}| = 1730$) — no mutual information, entropy, or error probability is measured from any actual attack or VLM response. Corollary 1 (lines 233–235) claims that minimizing inter-partition entropy differences minimizes mutual information, but this claim is stated without proof or justification and does not follow from any standard information-theoretic identity. The paper's third contribution — positioned as "most importantly" (line 59) — therefore remains a decorative formula appended to the paper rather than a substantive, empirically grounded analysis.

2. **Attack success rates are marginal, especially against deployed models.** On LLaVA (Table 2, lines 372–384), ASR is 0.39 versus a "No Attack" baseline of 0.34 — a 5-percentage-point improvement over *doing nothing*. On several categories (Financial Advice, Health Consultation) ASR is 0.00, identical to baseline. On Hate Speech (0.24 vs 0.26) and Pornography (0.26 vs 0.28), the attack performs *worse* than no attack. On ChatGPT 4o (Table 5, line 448), ASR is 0.01 — essentially zero. The "No Attack" baseline itself is high (0.34 on LLaVA, 0.80 on Malware Generation), which suggests the model is poorly aligned to begin with, further weakening the comparison. The paper frames this as a principled trade-off, but does not demonstrate that the attack constitutes a meaningful practical threat.

3. **Stealthiness is evaluated only against the same detector the attack is designed to evade.** The attack pipeline includes an "entropy gap checker" (line 210) that directly applies Algorithm 1 to filter out high-gap images and trigger regeneration. The stealthiness evaluation (Table 1) then tests whether Algorithm 1 can distinguish the attack's output from natural images — i.e., whether the filter succeeded. This is close to circular: the attack is literally using the detector as a rejection criterion during generation. The paper claims the attack is "indistinguishable from the Nature dataset" (line 271), yet provides no evidence against alternative detection methods (perplexity filters, other entropy-based detectors, or learned classifiers). Without such evidence, the claim of general stealthiness is unsupported.

4. **The attack pipeline is critically under-specified for reproducibility.** The following details are absent: (a) which diffusion model (family, variant, checkpoint) is used — line 208 says only "a diffusion model"; (b) whether typography integration used image-to-image diffusion or watermark blending, and with what parameters — line 202 lists two options without specifying which was used in experiments; (c) the entropy gap checker's acceptance/rejection threshold (line 210); (d) the number of random trials $K$ in Algorithm 1 (line 115); (e) which partitioning method was actually employed (pixel-based, block-based, line-based, Voronoi — line 136 lists all without selection); (f) whether RAKE or LLM-based keyword extraction was used (line 198); (g) the identity and prompt template of the LLM-as-judge evaluator (line 265). These omissions prevent independent reproduction.

### Minor

1. **No statistical tests for stealthiness comparisons.** The claim that the attack's entropy distribution is "indistinguishable" from Nature (line 271, Figure 3) rests solely on visual histogram inspection. No quantitative test (KL divergence, Kolmogorov-Smirnov, etc.) is reported.

2. **Toxicity metrics are floor-level and uninformative.** Tables 3–4 report Detoxify and Perspective API scores in the range of $10^{-4}$ to $10^{-2}$ for all methods including "No Attack." At these magnitudes, differences of $10^{-4}$ are not interpretable and do not support meaningful comparison between methods.

3. **"No Attack" baseline is not defined.** The paper reports ASR for the "No Attack" condition (Table 2) but does not specify what input is provided — e.g., is the text prompt given alone, with a neutral image, or with no image? This makes the baseline difficult to interpret or reproduce.

4. **LLM-as-judge evaluation is under-described.** The paper states "we instruct the LLM to generate an unsafe score between 0 and 1" (line 265) without specifying which LLM, the prompt template, or temperature settings — critical details given that the evaluation metric itself is a model-based judgment.

### Trivial
- None.

## Nice-to-Haves
- Test the attack against multiple detectors (perplexity filters, learned classifiers) to substantiate the general stealthiness claim.
- Compute empirical mutual information or error probabilities from actual attack data to ground the Fano analysis.
- Vary the entropy gap threshold and measure the empirical ASR-vs-detectability Pareto frontier against multiple detectors.
- Report confidence intervals or statistical significance for ASR comparisons.
- Specify all implementation details (diffusion model, partition method, $K$, threshold, LLM-as-judge prompt) in a reproducibility statement.

## Removed Points
These points are flagged to be removed per filtering rules; treat them with caution.

- **Missing algorithms (perplexity_gap, entropy_gap_rot):** The harsh critic noted that Algorithms \ref{alg:perplexity_gap} and \ref{alg:entropy_gap_rot} are referenced (line 237) but absent from the extracted text. Per the hard rules, content that may have been stripped by the PDF parser (including algorithmic pseudocode present in the original submission) should not be counted as a weakness. This is a plausible parser artifact, not an author error.

- **"Fano's inequality is standard textbook material":** The critic argued the theory is not novel because Fano's inequality is a known identity. However, applying standard theory to a new problem setting is a legitimate form of contribution when properly grounded. The actual problem (retained as Major weakness 1) is the lack of empirical connection, not that the inequality itself is standard.

- **Strength: "Explicit connection drawn between jailbreak detection and AIGC detection":** This claimed strength is too generic — the paper mentions the link in passing (lines 4, 59, 509) but does not develop it. Removed per filtering guidelines.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Ground the Fano analysis empirically: compute $I(X;Y_1,Y_2)$ from actual jailbreak data and verify whether the bound is informative. Without this, the theory section is ornamental.
2. Evaluate the attack against at least 2–3 alternative detectors (perplexity-based, learned classifier) to support the general stealthiness claim beyond the design-target detector.
3. Generate an empirical Pareto frontier by varying the entropy gap rejection threshold and measuring both ASR and detectability — this would directly demonstrate the claimed trade-off.
4. Provide complete implementation specifications covering the diffusion model, partitioning method, $K$, threshold, and LLM-as-judge details.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>