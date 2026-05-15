Now I have a thorough understanding of the paper and the reviewer's claims. Let me produce the consolidated review.

## Summary

Re-Debias proposes a framework that combines a Residual-Energy score (energy of non-target classes used to reweight a mixture-of-softmaxes) with a Debias estimator (inverse-class-frequency weighting derived via a causal-inference framing) for long-tailed classification. The method is evaluated on CIFAR-10/100-LT, ImageNet-LT, and iNaturalist18, achieving competitive to state-of-the-art results.

## Strengths

- **Consistent strong empirical performance across benchmarks.** Re-Debias achieves top-1 accuracy of 63.9% on ImageNet-LT (200 epochs), 79.5% on iNaturalist18 (400 epochs), and 83.9% on iNaturalist18 with ViT fine-tuning, outperforming or matching strong baselines including RIDE, DeiT-LT, and LGLA across Many/Medium/Few splits (Tables 1–3).  

- **Useful problem decomposition.** The paper explicitly decomposes the long-tailed problem into (a) improving individual prediction precision and (b) ensuring unbiased aggregate evaluation, and identifies that existing methods can improve overall metrics at the cost of performance in specific classes (Figure 1). This framing is conceptually clear and motivated.

- **Novel use of non-target energy for prediction quality.** The Residual-Energy score \(E(x,\overline{y}) = -\log\sum_{j\neq y} e^{f_j(x)}\) naturally captures information from non-target logits that softmax-based scores discard. The motivating example in Figure 2 shows two samples with nearly identical softmax scores but clearly separated residual-energy scores (−4.39 vs. −8.48), providing a concrete intuition for the approach.

## Weaknesses

### Fatal
None.

### Major

- **The Debias estimator is not novel; it reduces to known logit adjustment (Menon et al., 2021).** The paper derives adjusted logits \(g_y(x) = f_y(x) + \log(C\cdot\pi_y)\). Because the factor \(\log(C)\) is class-independent, it cancels in the softmax normalization, leaving exactly \(f_y(x) + \log(\pi_y)\) — the logit adjustment of Menon et al. (2021). The paper cites Menon et al. for Fisher consistency (line 179) but presents the Debias estimator as Contribution 3 ("develop a novel framework") without acknowledging that the resulting loss is a known method. This overclaims novelty and means the paper's theoretical contribution to aggregate evaluation is a re-derivation, not a new estimator.

- **The propensity derivation is mathematically imprecise and the unbiasedness claim is unjustified.** The paper defines \(\widetilde{P}_{i,c} = C \cdot \pi_c = C \cdot n_c / |\mathcal{O}|\) as a "propensity" (Eq. 14). For any head class with \(n_c > |\mathcal{O}|/C\) — which is common in long-tailed datasets — this exceeds 1, violating the definition of a propensity (a probability in \([0,1]\)). The derivation connecting Eq. 12–14 never verifies that \(\widetilde{P}_{i,c}\) is a valid probability, and the step from Eq. 12 to Eq. 14 implicitly assumes \(|\mathcal{O}| = C\cdot n\) without justification. While the resulting weighting scheme \(1/(C\cdot\pi_c)\) is a reasonable heuristic (inverse class-frequency weighting), the paper's claim that the Debias estimator is "unbiased" in the causal-inference sense is not supported by the derivation as presented.

### Minor

- **No isolation of the Residual-Energy score's effect.** All reported experiments use the full Re-Debias loss (Eq. 20), which jointly applies the mixture-of-softmaxes, residual-energy weighting, and the Debias/logit-adjustment term. Without ablations such as (i) logit adjustment alone, (ii) logit adjustment + standard softmax, (iii) logit adjustment + vanilla mixture-of-softmaxes (without residual-energy weighting), it is impossible to attribute observed gains to the Residual-Energy score specifically. (Note: Section 5.4 is truncated in the parsed copy; if ablation studies exist in the original submission in that section, this criticism should be downweighted.)

- **Value of K (number of mixture components) is not reported.** The mixture-of-softmaxes (Eq. 9) depends on a hyperparameter \(K\) that is never stated in the paper. Without specifying \(K\), the method is not fully reproducible, and the trade-off between expressiveness and computation is unexplored.

- **Uneven training budgets in a key comparison.** On CIFAR-100-LT (imbalance 100), Re-Debias underperforms LGLA, and the paper notes LGLA was trained for 400 epochs versus its own 200 epochs. This is transparently acknowledged, but it leaves open the question of whether Re-Debias would match or surpass LGLA with equal training length.

- **"After just 90 epochs" claim is imprecisely framed.** The paper states that after 90 epochs the method "surpasses previous state-of-the-art results" on ImageNet-LT. However, the baselines in Table 1 are reported at their full training epochs (typically 200), so the comparison at 90 epochs is between the proposed method's intermediate result and other methods' final results. This is still notable if true, but the phrasing could mislead readers into thinking a direct per-epoch comparison was shown.

### Trivial

- Typo: "tipycal" → "typical" (line 116)
- Typo: "socres" → "scores" (line 27)
- Typo: "traning" → "training" (line 199)

## Nice-to-Haves

- Reporting standard deviations or confidence intervals (from multiple seeds) would strengthen the reliability of the reported numbers, though single-run reporting is the prevailing norm in this benchmark setting.
- An explicit comparison against Menon et al. (2021) logit adjustment under identical backbone, schedule, and epochs would clarify whether the residual-energy mixture adds measurable benefit beyond the known baseline.

## Removed Points

**These points are flagged to be removed, treat them with caution:**

- *"No variance or significance reporting"* — Single-run evaluation is the norm across most baselines in this benchmark suite; singling out this paper for a practice that is standard in the field is not substantive.
- *"MNAR connection is a conceptual stretch"* — The MNAR analogy is imperfect but not invalid: in long-tailed learning, the "missingness" of balanced-data samples is indeed correlated with class (the unobserved part), which is structurally analogous to MNAR. The critique overstates the issue.
- *"Table/Figure formatting" complaints* — These are parser artifacts, not author errors.
- *"Equations 12–14 step eliminating n is not explained"* — Already subsumed by the Major weakness above; the derivation issue is captured more precisely by the propensity-bounds argument.
- *Strength Finder's "Principled derivation of the training loss from causal inference principles"* — This conflicts with the verified weakness that the derivation is imprecise and the unbiasedness claim is unsupported; strength and weakness disagree, and the weakness wins.
- *"Missing ablation studies" from the human finder / Strength Finder generic claims* — Not applicable here; no such claims were made in those inputs that needed filtering.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs surface a genuine tension: the paper's theoretical framing (causal inference + unbiased estimation) is more elaborate than what the math ultimately delivers (logit adjustment + inverse class-frequency weighting), and the claimed novelty of the Debias estimator does not survive comparison with Menon et al. (2021). The practical value of the paper therefore rests on whether the residual-energy-weighted mixture-of-softmaxes provides a meaningful improvement over standard logit adjustment — a question the current experiments do not directly answer because the necessary ablations are absent from the visible text.

## Suggestions

1. **Acknowledge the relationship to Menon et al. (2021) explicitly.** Reframe Contribution 3 as an alternative derivation or connection, not a new estimator. Show that the \(C\cdot\pi_y\) factor collapses to \(\pi_y\) in practice, and position the novelty in the *combination* with residual-energy weighting, not in the debiasing mechanism itself.

2. **Fix the propensity derivation.** Either (a) provide a clean proof that the weighting scheme yields an unbiased estimator under clearly stated assumptions, with propensity bounded in \([0,1]\); or (b) abandon the causal-inference framing and present the class weighting directly, avoiding the "propensity" terminology that implies a probability.

3. **Add ablation studies** that isolate the Residual-Energy score: compare (i) logit adjustment only, (ii) logit adjustment + standard softmax, (iii) logit adjustment + vanilla mixture-of-softmaxes (uniform weights), (iv) full Re-Debias. Report on at least one dataset (e.g., CIFAR-100-LT).

4. **Report K** (number of mixture components) and include a sensitivity analysis (e.g., K ∈ {1,2,4,8}) on a small-scale dataset.

5. **Run Re-Debias for 400 epochs** on CIFAR-100-LT (im100) for a fair comparison with LGLA, or temper the state-of-the-art claim accordingly.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>