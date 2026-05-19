- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6
Now I have all the information I need. Let me synthesize my final consolidated review.

## Summary
This paper proposes **SelMix**, a selective mixup-based fine-tuning technique to optimize non-decomposable objectives (e.g., min recall, H-mean, G-mean, coverage-constrained metrics) for pre-trained models. The core idea is to compute a gain matrix \(G_{ij}\) approximating how much mixing class \(i\) with class \(j\) would improve the target objective, then sample mixup pairs from a softmax distribution over this gain matrix. The method fine-tunes both the linear layer (primarily) and backbone (at a lower learning rate) of a pre-trained classifier. Experiments on CIFAR-10/100 LT (semi-supervised and supervised), STL-10, ImageNet-100/1k show consistent improvements over prior empirical methods (DASO, ABC, CoSSL) and theoretical methods (CSST) across multiple non-decomposable metrics.

## Strengths
- **Consistent and large empirical improvements across diverse settings.** Table 1 shows SelMix improves Min Recall on CIFAR-10 LT (semi-supervised) from 55.9 (FixMatch(LA), the same pre-trained starting point) to 79.1, and on CIFAR-100 from 34.6 to 57.8. It also achieves the best Mean Recall (85.4), H-mean (85.1), and G-mean (85.3) simultaneously — outperforming both empirical and theoretical baselines on their own reported metrics. Tables 2 and 3 extend these gains to supervised learning and large-scale datasets (ImageNet-1k LT: Min HT Recall from 29.7 → 45.1).

- **Ability to optimize non-linear non-decomposable objectives.** Unlike prior theoretically principled methods (CSST, Narasimhan et al. 2021) that are restricted to linear-in-the-confusion-matrix objectives, SelMix directly optimizes non-linear objectives like H-mean and G-mean and achieves the best results on these metrics (e.g., H-mean 85.1 vs. 76.9 for CSST on CIFAR-10). This is a genuine capability extension.

- **Robustness to mismatched label distributions.** Under the practical scenario where labeled and unlabeled class distributions differ (\(\rho_l \neq \rho_u\)), Figure 2/3 shows SelMix significantly outperforms all baselines on CIFAR-10 (balanced and inverted unlabeled distributions) and achieves a 12.7% improvement in min recall over CSST on STL-10 where the unlabeled distribution is unknown. This validates the adaptive nature of the method.

- **Generality across training paradigms.** SelMix is demonstrated in semi-supervised learning (fine-tuning FixMatch(LA)), supervised learning (fine-tuning MiSLAS), and large-scale settings (ImageNet-1k), showing it is not narrowly tailored to one setup.

## Weaknesses

### Fatal
None. The paper's core claims are supported by valid evidence — especially the dramatic improvement of SelMix over FixMatch(LA) (the same starting pre-trained model), which directly attributes gains to the SelMix fine-tuning procedure.

### Major
- **Missing controlled fine-tuning ablations.** The paper compares SelMix (fine-tuning from FixMatch(LA)) against full pre-training baselines (DASO, ABC, CSST, etc.). While FixMatch(LA) is included as a direct baseline and the improvement over it is substantial (55.9→79.1 Min Rec), the paper does **not** compare SelMix against other *fine-tuning* strategies applied on top of the *same* pre-trained model: (a) standard fine-tuning on labeled data without mixup, (b) uniform/random mixup fine-tuning (non-selective), (c) fine-tuning with logit-adjustment only, (d) fine-tuning with CSST's loss. Without these ablations, it is difficult to isolate how much of the gain comes from the *selective* nature of the mixup vs. simply additional training with mixup. This is the single most important missing experiment for establishing the method's distinctive contribution.

### Minor
- **The gain approximation (Theorem 1) is not directly validated.** The paper asserts "this approximation works well in practice" (line 208) but provides only end-task metric results as indirect evidence. A direct empirical validation — e.g., measuring the correlation (Spearman or Pearson) between the approximate gain \(G_{ij}\) from Eq. (9) and the actual change in \(\psi\) after one SGD step — would significantly strengthen confidence in the method's core mechanism.
- **Convergence analysis (Theorem 2) relies on an unrealistic concavity assumption.** The theorem assumes \(\psi\) as a function of \(W\) is concave (line 273), which does not generally hold for neural network objectives even when only the linear layer is updated. The convergence guarantee therefore does not apply to the actual setting studied. This limits the practical relevance of the theoretical contribution.
- **Tension between gain approximation and backbone fine-tuning.** The gain approximation assumes the feature extractor \(g\) is fixed (line 135: "fixed feature extractor \(g\)"), but the algorithm fine-tunes the backbone at a lower learning rate (line 236). The paper acknowledges this but provides no analysis of whether the approximation error remains controlled as \(g\) drifts.

### Trivial
- An "appendix" reference for limitations is present in the text but the limitations section is not in the main paper (per the parser limitation). This should be integrated into the main paper.
- Table 3 (large-scale results) reports single numbers without variance estimates across seeds.

## Nice-to-Haves
- Study of the sensitivity to the softmax temperature parameter \(s\) (which controls how greedy vs. exploratory the mixup distribution is).
- Study of the gain matrix update frequency \(n\) as a hyperparameter.
- Wall-clock time comparison of total training between SelMix fine-tuning and full-training baselines.
- Ablation comparing frozen backbone vs. fine-tuned backbone for the SelMix method itself.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"CSST already optimizes non-linear objectives"** — Removed as factually incorrect. CSST, based on Narasimhan et al. (2021), optimizes linear-in-the-confusion-matrix objectives (min over linear combinations). H-mean and G-mean are non-linear functions of recall and cannot be directly optimized by the CSST framework. The paper correctly identifies this as a limitation of prior work.
- **"Low variance for CSST (std=0.2) may indicate single run"** — Removed as a nitpick. A standard deviation of 0.2 across 3 seeds is perfectly plausible for a stable method and does not indicate any problem.
- **"No total training time reported"** — Removed as the paper states "~2 min extra compute" and references a computation time table in the appendix.
- **"Not clear if pre-training uses same unlabeled data"** — Removed because the training details (line 361) clearly describe the pre-training setup using the same unlabeled data with logit-adjusted FixMatch.
- **"Missing appendix content"** — Removed per instructions: the parser strips appendix sections; they exist in the original submission.
- **"Update frequency n is a hyperparameter that could affect performance"** — Removed from weaknesses (moved to Nice-to-Haves); it is a reasonable design choice following prior work (Narasimhan et al.) and not a flaw.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Add controlled fine-tuning baselines.** Starting from the same pre-trained FixMatch(LA) model, compare against: standard fine-tuning (no mixup), uniform/random mixup fine-tuning, and CSST-style fine-tuning. This will cleanly isolate the benefit of the *selective* mixup mechanism.
2. **Directly validate the gain approximation.** Report the rank correlation between approximate \(G_{ij}\) and the actual measured change in \(\psi\) after one SGD step on a held-out set. This is a straightforward experiment that would significantly increase confidence in the method's core theoretical component.
3. **Add variance bars to Table 3** (large-scale experiments) to match the reporting standard of the main tables.
4. **Discuss the concavity assumption** more honestly in the main text, clarifying that the convergence guarantee applies under an idealized setting and that empirical evidence (not theory) supports the method's effectiveness for deep networks.
