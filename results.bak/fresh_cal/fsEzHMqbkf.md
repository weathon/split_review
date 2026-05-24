Now I have a thorough understanding of the paper and can construct an authoritative final review. Let me synthesize everything.

---

## Summary

This paper introduces the Conditional Density Ratio (CDR) score for post-hoc OOD detection. The key insight is to estimate the marginal density p(z) without marginalizing over classes by using the ratio p(z|y)/p(y|z) — combining a class-conditional generative model in latent space with a pretrained discriminative classifier. The paper also proposes a temperature tuning method that requires only ID validation data (no OOD samples). Experiments on CIFAR10, CIFAR100, and ImageNet with Mahalanobis and KDE density estimators show strong performance.

## Strengths

1. **Novel and principled alternative to marginalization** — The CDR derivation from the law of conditional probability (Section 3.2, Equation 1) is clean and theoretically grounded. The decomposition into CDR = Energy + average GCR (Equation 2) provides genuine insight into why the method works, and the histograms in Figure 2 empirically validate that the GCR correction is near zero for inliers.

2. **OOD-free temperature tuning that demonstrably works** — Algorithm 1 and Figures 3–4 show that both temperatures can be tuned using only a small ID validation set. The ablation confirms that tuned CDR significantly outperforms untuned CDR, and the AUROC is relatively flat near the optimum, indicating robustness. This is a practical contribution — prior post-hoc methods that use temperature (e.g., ODIN) require OOD data for tuning, which is unavailable in the paper's setup.

3. **Robustness to classifier degradation** — The paper shows (Section 4.1) that Energy's average AUROC drops from 91.99% (CIFAR10) to 77.20% (CIFAR100, lower classifier accuracy), while CDR_Maha only drops from 97.41% to 95.66%. This is a large (≈18 pp) gap on CIFAR100 and convincingly demonstrates that CDR is less dependent on classifier quality than marginalization-based methods.

4. **Strong empirical results across backbones and density estimators** — CDR achieves the highest average AUROC among all hyperparameter-free post-hoc baselines on all three tested datasets (Tables 1–3), with both Mahalanobis and KDE variants. The method works across different architectures (DenseNet, WideResNet) and dataset scales.

5. **Practical setup with transparent limitations** — The paper honestly addresses the challenging setup (no training data, small validation set, no OOD samples). Limitations are discussed in Section 6, including cases where CDR underperforms Energy (hard OOD for CIFAR-100).

## Weaknesses

### Fatal

None.

### Major

1. **Imbalanced comparison: tuned CDR vs. fixed-T=1 baselines** — The paper states (lines 142, 155) that baselines use T=1 while CDR tunes two temperatures. This conflates the benefit of the CDR formulation with the benefit of temperature tuning. The critic's suggestion to show all methods with T=1 as a control is well-founded. The paper does show CDR(untuned) in Figure 3, which helps, but does not report tabular results for CDR(T=1) alongside baselines(T=1). Without this control, readers cannot cleanly attribute the reported gains to the CDR formula versus the tuning procedure. Since the tuning method is itself a contribution, this does not invalidate the results, but it weakens the headline claim that "CDR outperforms baselines" as a statement about the density ratio itself. The authors should provide a direct comparison at shared T=1 and transparency about what fraction of the gain comes from tuning.

2. **Disconnect between stated principle and actual T_φ loss** — The paper says its guiding principle is "maximizing the likelihood of the density functions" (line 117), but the T_φ loss (Equation 3: margin-based term + regularization R) is not a standard negative log-likelihood nor derived from a probabilistic model. The margin loss and the regularization that matches log-scales are reasonable heuristics, but the paper over-claims on the principled nature of this specific loss. This matters because without a clear likelihood interpretation, the tuning method's generalization beyond the tested benchmarks is uncertain. The paper could either derive the loss from a proper probabilistic objective or explicitly reframe it as a heuristic with an analysis of its sensitivity.

### Minor

3. **"Hyperparameter-free" claim is overstated** — The paper calls CDR "hyperparameter-free" (lines 17, 198), but the user must still choose: (a) which density estimator to use (Gaussian vs. KDE), (b) covariance structure (tied vs. full), and (c) the grid range for temperature search. The temperature values themselves are automatically tuned, which is valuable, but the meta-choices remain. This is a presentational overreach rather than a methodological flaw.

4. **Aggregation by averaging is not justified or ablated** — The paper averages CDR scores across K classes (Section 3.2, line 94) with the comment "we adopt a simple solution" but does not discuss alternatives (max, weighted average, learned combination) or provide an ablation. Since different classes may produce very different CDR estimates when the generative model is inaccurate, this design choice deserves justification.

5. **No analysis of sensitivity to validation set size** — The paper uses 10% of training data (CIFAR) or 25 samples/class (ImageNet). It would strengthen the practicality claims to show how performance degrades with even fewer samples (e.g., 5 or 1 sample per class), especially since the setup emphasizes data scarcity.

### Trivial

None.

## Nice-to-Haves

- Report results with **all methods at T=1** as a control experiment, to isolate the contribution of the CDR formula from the tuning procedure.
- Provide an **aggregation ablation** (max, median, weighted average across classes) to justify the averaging choice.
- Show **sensitivity to validation set size** (e.g., vary N from 1 to 100 per class) to support the claim of practicality under data scarcity.
- Include **inference time comparison** between CDR_Maha, CDR_KDE, and baselines.

## Removed Points

The following points from the input reviews are removed with justification:

1. **"Missing Table 4 (self-supervised results) and additional ablations"** — The parser strips table images and appendix content from the text extraction; these exist in the original submission. Per instructions, criticisms about missing appendix-content are removed.

2. **"Missing comparison with Ren et al. 2019 / likelihood ratios"** — The paper scopes itself to post-hoc methods requiring no additional training. The reviewer's suggested methods require separate generative model training. Per the soft rule on scope creep, removed.

3. **"CDR requires nearly same computational cost as GEM/Mahalanobis"** — This is equally true of all generative baselines (Mahalanobis, GEM all need validation-set statistics). It is not a weakness specific to CDR and reflects a misunderstanding.

4. **"Not compared with CSI-based scores, graded features"** — The paper explicitly excludes methods requiring training/retuning (line 142). This is a scope choice, not an omission.

5. **"Statistical significance not reported"** — Single-run evaluation is standard practice in the OOD detection literature. This is a nice-to-have, not a weakness. Moved to Nice-to-Haves.

6. **"The CDR score aggregates by averaging, which is also done in GEM (via log-sum-exp)"** — GEM uses log-sum-exp (softmax aggregation), not averaging. The mathematical forms are different. Removed as factually inaccurate.

7. **"Related work omission of self-supervised methods"** — The paper does cover self-supervised methods in Section 2 (lines 30: "transformation-based self-supervised methods have also shown improved performance"). Removed as factually incorrect.

8. **Generic strengths** (e.g., "the paper addressed an important problem") — Removed per filtering instructions to retain only concrete, evidence-grounded strengths.

## Novel Insights

The harsh critic made a point that, while somewhat overstated, is genuinely insightful: the imbalance between tuned CDR and fixed-T baselines is the paper's most significant methodological limitation, and addressing it would substantially strengthen the contribution. The relationship between CDR and Energy (Equation 2) as an additive correction is nicely articulated in the paper itself. Beyond this, the reviews do not surface novel observations beyond what the paper already states.

## Suggestions

1. **Add a controlled experiment** — Report all methods at T=1 as a table (or a column in the existing tables). Then show the gain from CDR's tuning separately. This cleanly isolates the CDR formulation from the tuning benefit and would silence the most serious criticism.

2. **Reframe the T_φ loss** — Either derive it from a proper likelihood (e.g., as a lower bound on log-marginal-likelihood) or explicitly call it a heuristic and analyze sensitivity to its form (vary the regularization weight, compare with alternative objectives like direct margin maximization).

3. **Tone down the "hyperparameter-free" language** — Replace with "automatically-tuned temperature parameters" or "requires no manual hyperparameter tuning of its core temperature parameters." This is more accurate and avoids overclaiming.

4. **Add an aggregation ablation** — Show max, median, and weighted-average aggregation across classes for CDR on at least one benchmark to justify the averaging choice.

## Score and Decision

The paper presents a clean, theoretically-motivated framework for post-hoc OOD detection with strong empirical results across multiple datasets and backbones. The temperature tuning method using only ID data is practically valuable. The main weaknesses — an imbalanced comparison between tuned CDR and fixed-T baselines, and a heuristic (rather than truly likelihood-based) T_φ loss — are addressable and do not invalidate the core contribution. The performance margins over baselines are substantial enough (5–18 pp AUROC) that tuning alone cannot explain them. On balance, this is a solid paper with genuine contributions to the OOD detection literature.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>