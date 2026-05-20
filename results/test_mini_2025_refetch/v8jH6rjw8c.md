Now I have sufficient calibration. Let me write the final consolidated review.

**Round 1 bracket**: The paper sits between the weak anchors (~2.5-3.4 for clearly rejected papers) and the strong anchors (~8.0 for spotlight/oral papers). The most topically-similar anchors in the middle band (3.5-7.5) ranged from 4.25 to 6.25. My initial bracket: **4.5–6.0**.

**Round 2 narrowing**: I examined anchors within that bracket. The paper is weaker than "Why is SAM Robust to Label Noise?" (6.0, poster) and "Rethinking Classifier Re-Training" (6.25, poster), both of which have stronger experiments and theoretical depth. It is stronger than "IKL" (4.67, reject) and "Learning a Reusable Meta Denoiser" (4.25, reject). The most comparable anchor is "Robust Classification via Regression" (6.0, poster, with scores 5,5,8,6) — that paper had mixed reviews with noted weaknesses similar to this one's, but stronger empirical support.

**Final score**: This paper's contributions (problem framing, empirical observations of disparate impacts) are genuine and the experiments are broad. However, the lack of variance reporting, absence of comparison to joint-method baselines, marginal real-world gains, and the proxy concern all weigh against it. The paper is **below the acceptance threshold in its current form**. Score: **5.0**.

---

## Summary

This paper studies the underexplored joint setting of long-tailed distributions and label noise. It empirically demonstrates that existing robust methods have disparate impacts on different sub-populations (Section 3), then proposes a Fairness Regularizer (FR) that penalizes absolute differences in average prediction probability across sub-populations. FR is a simple plug-in regularizer applicable to any base loss. Experiments on CIFAR-10/100 and Clothing1M show that adding FR improves accuracy over six standard baselines (CE, LS, NLS, Focal, PL, Logit-adj) in many configurations, with a paired t-test indicating statistical significance for FR(G2) in most settings.

## Strengths

1. **Well-motivated, timely problem framing.** The paper identifies that the coupling of long-tailed distributions and label noise — common in practice but rarely studied jointly — creates disparate impacts across sub-populations. Section 3 (Figures 2, 4, 5) provides empirical evidence that existing robust methods help some sub-populations while hurting others, which is a genuine observation that motivates the work. This problem diagnosis is a contribution in itself.

2. **Simple, accessible method.** FR is conceptually straightforward (a single regularizer added to any loss), requires no noise-rate estimation or special architectures, and works with two coarse sub-population separation strategies (KNN clustering and a pre-trained model split into two groups). The λ sensitivity study on Clothing1M (Table 3) shows the method is not brittle.

3. **Broad experimental evaluation.** The paper tests 6 base methods × 2 noise models (Imb, Sym) × 2 noise rates × 3 imbalance ratios × 2 FR variants on CIFAR, plus Clothing1M. This is a large configuration space. The paired t-test across 12 configurations (Table 2) provides aggregated evidence that FR(G2) significantly improves performance in 11/12 cases.

## Weaknesses

### Fatal
None.

### Major

1. **No within-configuration variance reported.** Every entry in Table 1 is a single number with no standard deviation, number of seeds, or mention of how many runs were performed. Given the stochasticity of neural network training — especially under label noise and heavy class imbalance — single-run results are uninterpretable for individual comparisons. Many reported improvements are 0.1–1.0 percentage points (e.g., LS+FR(KNN) on CIFAR-100 Imb noise ρ=0.2 r=10: 47.80→48.27, a 0.47% gain), which could easily fall within random variation. The paired t-test in Table 2 aggregates across configurations but does not address within-configuration variance. Without replication, the main empirical claim is not supported at the level of individual configurations.

2. **No comparison to existing methods that jointly handle long-tail and label noise.** The related work (Section 1.1) explicitly cites Zhong et al. (2019), Wei et al. (2021c), and Karthik et al. (2021) as addressing precisely this joint setting. The paper evaluates FR only on simple baselines (CE, LS, Focal, etc.) that were not designed for the joint problem. Demonstrating that FR improves these baselines is a valid starting point, but without comparison to existing joint-method baselines, the practical significance of the contribution cannot be gauged. The gap may be small, or FR may already be inferior to existing dedicated solutions.

3. **Real-world improvements on Clothing1M are marginal.** Table 3 shows that FR improves CE from 72.68 to 72.99 (+0.31%), NLS from 74.46 to 74.49 (+0.03%), and PL from 73.00 to 73.08 (+0.08%). These differences are within the noise floor of a single training run and are not accompanied by variance estimates. While real-world benchmarks often yield small gains, the paper does not discuss whether these improvements are practically meaningful or statistically distinguishable from zero given the lack of replication.

### Minor

4. **The regularizer uses prediction probability on the noisy label as a proxy for accuracy, which is a valid relaxation but is not analyzed under noise.** The paper correctly uses the model's prediction probability on the noisy label (Eq. 3) as a standard differentiable relaxation of the 0-1 indicator. However, under **noisy** labels, high confidence on a noisy label does not imply correct prediction. The regularizer could theoretically encourage confident wrong predictions on certain sub-populations. The paper claims theoretical treatment of this issue (Observation 4.1, deferred to appendix), but the main text provides no analysis or empirical evidence that this proxy reliably tracks clean accuracy under noise. An ablation comparing FR to an identical regularizer computed on a clean validation set would help validate the proxy.

5. **The claim of "consistent" improvement is overstated.** The paper states that "FR (KNN) consistently improves the baseline methods on the class-imbalanced CIFAR-10 dataset" (Section 5.2). However, Table 2 shows FR(KNN) does **not** produce statistically significant improvements on CIFAR-10 for LS, Focal, and Logit-adj (p > 0.1). The paper's own t-test undermines the "consistent" claim. Similarly, the abstract's claim that existing methods "fail to consistently improve the learning" is a framing that would benefit from more precise qualification.

6. **The "G2" sub-population separation method is underspecified.** The paper says G2 "separates features into a head and a tail sub-population" using "the direct prediction made by a (ImageNet) pre-trained model" (Section 5.2) with a ratio of ≈5:1. It is unclear how the pre-trained model's predictions are used to create exactly two groups — by confidence threshold? By class prediction? This detail matters for reproducibility and for understanding when G2 would work.

### Trivial
None.

## Nice-to-Haves
- Report results with standard deviations over multiple seeds (at least 3–5) for all main configurations.
- Compare FR to at least one existing joint long-tail+noise method (e.g., from Wei et al. 2021c or Karthik et al. 2021).
- Analyze the effect of FR on worst-group accuracy explicitly, not just overall accuracy, since that is the paper's stated motivation.
- Ablate the number of sub-populations K (beyond K=#classes and K=2) to study sensitivity to this design choice.
- Report how λ was selected (e.g., using a held-out clean validation set) rather than mentioning only that λ=1.0 was the default.

## Removed Points

- **"The regularizer is not a relaxation of a non-differentiable quantity — it is a different quantity."** This is factually incorrect. The prediction probability f(x)[ỹ] is exactly the standard differentiable relaxation of the indicator 1{f(x)=ỹ}. This is textbook material used throughout ML (knowledge distillation, soft targets, etc.). Removed for being factually wrong.

- **Detailed table formatting confusion (e.g., "some entries are not bolded when they should be").** The bold/markup inconsistencies are likely PDF parser artifacts, not author errors. The core claim (FR does not always improve) is retained in its corrected form (Weakness 5). Removed the parser-dependent formatting analysis.

- **"G2 is unclear: how exactly are samples split into two groups?"** Partially retained (Weakness 6) but the critic's framing as a critical flaw was exaggerated. The description, while terse, gives enough information to understand the approach.

- **"No validation split mentioned; risk of overfitting test set."** The paper reports "best-achieved averaged accuracy," which could imply test-set overfitting, but this is standard in many benchmark papers and not unique to this work. The critic's framing was too strong for the evidence available.

- **"Observation 4.1 is deferred to appendix; argument is incomplete."** Per the hard rules, criticisms about missing appendix content (stripped by the parser) must be removed. The paper claims theoretical analysis exists in the appendix; we cannot penalize for its absence.

- **"Lack of analysis on why FR works (loss curve, gradient analysis)."** This is a reasonable suggestion but more of a nice-to-have than a weakness. The paper provides some theoretical insight (Observation 4.1) and empirical validation (t-test, per-class plots). Relocated to Nice-to-Haves.

- **"The t-test sample size is 12; normality is doubtful."** The paired t-test is a standard method for aggregated comparisons; the normality assumption with n=12 is debatable but widely accepted in ML evaluations. This concern is too technical for a major weakness without a concrete demonstration of violation.

- **Generic strengths from Strength Finder removed:** "Addresses the coupling... a valuable contribution to the problem definition" (retained in Strengths 1, but the Strength Finder's phrasing was sycophantic) and "Rigorous experimental evaluation" (conflicts with Weakness 1).

## Novel Insights

The merged reviews do not surface a genuinely novel observation about the paper beyond what the paper itself claims. The interplay between fairness regularization and learning under noise is underexplored, and the paper's diagnosis of disparate impacts (Section 3) is the clearest contribution. The core technical insight — that a regularizer on prediction-probability gaps between sub-populations improves overall accuracy — is plausible but the evidence is not airtight in the current submission.

## Suggestions

1. **Address the variance reporting gap as the top priority.** Re-run all Table 1 configurations with 3–5 random seeds and report mean ± std. If computational cost is a concern, select a representative subset of configurations (e.g., one noise type, three base methods) for full replication and report variance for those.
2. **Include at least one joint-method baseline** (e.g., from Wei et al. 2021c or Karthik et al. 2021) to calibrate whether FR's improvements are competitive with dedicated approaches.
3. **Tone down "consistent" language** to match the t-test results, which show significance in most but not all settings.
4. **Clarify the G2 separation procedure** in a few sentences so the method is reproducible.
5. **Provide an ablation comparing the noisy-label proxy against a clean-validation-set accuracy regularizer** to validate the proxy, or at minimum discuss the limitation explicitly.

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| MDXfiEpEEP.md | 3.40 | R1-Bracket | Weaker — rejected LNL paper with unclear contribution |
| 6PGT9OJX5N.md | 3.00 | R1-Bracket | Weaker — rejected noisy data pruning paper |
| tC1b9DBWww.md | 2.50 | R1-Bracket | Weaker — rejected bias analysis paper |
| AL4tS0HhJT.md | 2.50 | R1-Bracket | Weaker — rejected confidence calibration paper |
| OeKp3AdiVO.md | 6.25 | R1/R2 | Stronger — accepted poster with SOTA on clean long-tailed benchmarks, better experiments |
| toWEwcbldw.md | 4.50 | R1-Bracket | Comparable — withdrawn, but with theoretical results this paper lacks |
| dW7FRwi1eA.md | 4.25 | R1-Bracket | Comparable — rejected, similar experimental gaps (no variance, small gains) |
| wfgZc3IMqo.md | 6.00 | R1/R2 | Stronger — accepted poster on label noise, stronger empirical support despite mixed reviews |
| ta26LtNq2r.md | 8.00 | R1-Bracket | Much stronger — accepted spotlight, deeper theory and experiments |
| TjhUtloBZU.md | 8.50 | R1-Bracket | Much stronger — accepted spotlight on label noise in pre-training |
| Lbx9zdURxe.md | 6.00 | R2 | Stronger — accepted poster with more thorough ablations |
| SRn2o3ij25.md | 4.67 | R2 | Weaker — rejected; similar "simple regularizer" approach with unconvincing results |
| 3aZCPl3ZvR.md | 6.00 | R2 | Stronger — accepted poster with analytical depth this paper lacks |
| HXWTXXtHNl.md | 5.75 | R2 | Slightly stronger — accepted poster on label noise, better experiments |
| yiQCeXdPvs.md | 3.75 | R2 | Weaker — withdrawn; similar setting but different approach |
| 6vtGG0WMne.md | 4.50 | R2 | Comparable — rejected; similar regularizer approach with moderate evidence |
| QgMaqtB444.md | 4.33 | R2 | Weaker — withdrawn; adversarial training with imbalance |

**Round 1 bracket:** [4.5, 6.0]  
**Round 2 narrowing:** The paper is clearly weaker than the 6.0 anchors (which had stronger empirical methodology and analytical depth) and stronger than the 4.25–4.67 anchors (which had weaker experiments or smaller scope). Final score positioned between the weaker rejected papers and the accepted poster papers.

The paper identifies a genuine problem and proposes a clean solution, but the evaluation lacks the rigor (no variance reporting, no joint-method baselines, marginal real-world gains) needed to support the core claims. The contribution is real but the evidence is insufficient.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>