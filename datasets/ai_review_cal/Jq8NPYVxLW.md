- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6
Now I have enough information. Let me write the consolidated final review.

## Summary

This paper proposes a membership inference attack (MIA) that progressively removes features from inputs (via pixel removal) and uses the trajectory of model output changes as a membership signal. The key insight is that member samples reside in higher-density regions of the learned feature space, so their confidence drops more gradually under feature removal compared to non-members. The method comes in two variants — random removal (resource-efficient, only needs one shadow model and a few dozen queries) and guided removal (trains a U-net mask predictor for principled feature selection). Experiments on classification models (CIFAR-10/100, CINIC-10, ResNet/WideResNet) and diffusion models (DDPM on CIFAR-10/100) show consistent improvements in TPR at low FPR over existing methods.

## Strengths

- **Novel membership signal validated with controlled evidence**: Figure 1 directly shows that for samples with nearly identical loss (<0.01), member and non-member confidence trajectories diverge under progressive pixel removal. This demonstrates a genuinely new discriminative signal beyond loss-based metrics.

- **Strong and consistent empirical gains across multiple settings**: The paper reports large TPR-at-low-FPR improvements across diverse datasets and architectures. For instance, on CIFAR-100 + ResNet-18 in the standard setting, the guided variant achieves markedly higher TPR@0.1%FPR than existing methods, and this advantage carries over to the large-supplementary-dataset setting and the many-shadow-models setting. The random removal variant alone (no mask predictor, one shadow model) often outperforms methods using 64 shadow models (Table 2).

- **Resource efficiency demonstrated quantitatively**: Table 5 (removal step ablation) shows that even 5–10 removal steps produce strong results (e.g., 20.7% TPR@0.1%FPR with 10 steps vs. 24.4% with 50 steps), confirming the claim that only "a few dozen queries" suffice. The random variant requires no additional model training beyond one shadow model.

- **Generalization to diffusion models**: Table 3 shows the method nearly doubles the best prior diffusion-model MIA (SecMI-NNs) on CIFAR-100 (18.4% vs. 9.7% TPR@0.1%FPR), demonstrating applicability beyond classifiers.

- **Robustness to distribution shift**: Figure 5 shows that when shadow and target data come from disjoint distributions (CINIC-10 ImageNet vs. CIFAR-10), the method remains effective while baseline ROC curves collapse.

## Weaknesses

### Fatal
None.

### Major
- **No variance/error bars reported for any result**: All reported TPR@0.1%FPR, AUC, and balanced accuracy are point estimates (single seed). MIA experiments — especially those involving shadow model training, mask predictor training, and multiple queries — are subject to nontrivial randomness from data splits and training stochasticity. The absence of any measure of dispersion (standard deviation, min/max over N≥3 runs) makes it impossible to assess whether the reported improvements are statistically reliable. This is the most significant threat to the paper's quantitative claims.

- **Table 1 (standard setting) benchmarks against weak baselines**: The standard-setting comparison in Table 1 includes only Yeom (2018), Shokri (2017), Salem (2018), and Song & Mittal (2021) — methods not designed for low-FPR performance. LiRA with 1–2 shadow models and RMIA with 1 shadow model (which are the relevant low-resource comparisons) appear only in Table 2 (CIFAR-10/WideResNet, the many-shadows setting). Since the paper's core claim is resource efficiency, the main table should include these stronger low-resource baselines. While Table 2 partially fills this gap, it covers only one dataset/architecture combination.

### Minor
- **Conceptual gap between "feature density" and pixel removal is not directly validated**: Section 3.2 formulates feature-space density $p(\phi(x))$ as a theoretical motivation, but the attack operates on input pixels. The paper acknowledges that pixel removal only *approximates* feature removal (line 65), but no experiment directly verifies that (a) members actually have higher feature-space density, or (b) confidence changes under pixel removal correlate with feature-space density. The empirical success of the method is not in doubt, but the "exploiting feature density" narrative remains an untested post-hoc explanation rather than a validated mechanism.

- **Reproducibility details missing for the guided removal component**: The mask prediction U-net training details (optimizer, learning rate, batch size, number of epochs, the C&W loss parameter $k$) are not specified. Only $\alpha=2$ and $\beta=0.02$ for the combined loss are given. This makes independent reproduction of the guided variant unnecessarily difficult.

- **Hyperparameter sensitivity of mask prediction loss is unexamined**: The loss function parameters $\alpha$ (total variation weight) and $\beta$ (L1 weight) are fixed at 2 and 0.02 with no sensitivity analysis to show that results are stable across a reasonable range.

- **Diffusion model experiments use only random removal (not guided) and only CIFAR-10/100 with DDPM**: The guided variant is not applied to diffusion models, and no experiments on higher-resolution datasets (e.g., LSUN, ImageNet) are conducted. This limits the generality claim.

### Trivial
- The abstract should explicitly note that the guided variant requires training an additional mask prediction model (U-net), not just a shadow model. Currently it only says "does not rely on large auxiliary datasets or the training of numerous shadow models," which is accurate but understates the guided variant's overhead.
- The C&W loss parameter $k$ in Equation 2 is referenced but never specified.

## Nice-to-Haves

- A direct validation experiment correlating feature-space density (computed via the nearest-neighbor formula in Section 3.2) with the confidence drop under pixel removal would strengthen the paper's conceptual framing.
- A plot of TPR@0.1%FPR as a function of total query count (across varying numbers of removal steps) would more directly characterize the query-efficiency frontier.
- A brief discussion of scalability to higher-resolution images (e.g., 256×256) — especially for the guided variant's U-net optimization — would be helpful context.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing related works (Selbst et al. 2023, others)"**: Removed per rule — missing-related-work criticisms cannot be verified without external sources and are excluded by policy.
- **"No ethical considerations/limitations discussion about improved MIAs"**: Removed as a non-standard request that does not reflect a flaw in the paper's technical contribution; moved to nice-to-have territory implicitly.
- **"The formulation 'exploiting feature density' in title/abstract is an overstatement"**: This is editorial framing, not a technical weakness. The paper provides empirical evidence for the behavioral divergence it claims, regardless of whether the density mechanism is fully proven.
- **"Table 1 formatting confusion between settings"**: The paper's text descriptions clearly delineate which setting each row corresponds to (standard setting rows vs. large supplementary dataset rows). The table organization is standard and interpretable.
- **"Density equation does not specify how many neighbors k"**: The equation is theoretical motivation only; the method never computes this quantity. Specifying k is irrelevant to the actual attack. Removed as a nitpick.
- **Several severity downgrades**: The harsh critic's points about "weak baseline selection" and "variance" are kept but classified correctly below Fatal. The critic's framing of the baseline issue as a "critical issue" and "fatal" is too strong given that Table 2 does include the stronger baselines (LiRA, RMIA) on a representative dataset/architecture.

## Novel Insights

None beyond the paper's own contributions. The two notable synthesized observations are: (1) the random removal variant's strength is particularly surprising — it requires no mask predictor yet still beats methods using 64 shadow models in Table 2, suggesting the progressive-removal trajectory is a fundamentally richer signal than pointwise loss; (2) the method's consistent advantage under distribution mismatch (Figure 5) hints that the removal-trajectory signal may be rooted in model behavior properties (e.g., confidence calibration near training data) that persist even when the shadow distribution is imperfect, which is a practically valuable robustness property.

## Suggestions

1. **Report variance**: Run the full pipeline (target model + shadow model + mask predictor for guided) at least 3 times with different random seeds and report mean ± std for the key metrics (TPR@0.1%FPR, AUC) in Tables 1–3. This single change would dramatically increase confidence in the results.

2. **Add LiRA/RMIA with 1 shadow model to Table 1**: Since the paper's core strength is low-resource MIA, the main comparison table should include LiRA (1 shadow) and RMIA (1 shadow) alongside the older baselines. If these are already present in the image tables, make this explicit in the table caption and text.

3. **Validate the density hypothesis directly**: Compute feature-space density (using the nearest-neighbor formula with a reasonable $k$) for a subset of members vs. non-members and show a scatter plot or correlation with the observed confidence drop. This would either confirm the claimed mechanism or reveal the true cause — either outcome strengthens the paper.

4. **Provide missing training details for the U-net mask predictor**: Specify the optimizer, learning rate, batch size, number of epochs, and the C&W loss $k$ parameter to enable independent reproduction.

5. **Add a hyperparameter sensitivity study** for $\alpha$ and $\beta$ in the mask loss (or state that results are stable and move on).
