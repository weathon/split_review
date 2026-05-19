- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 5, 6, 6
Now I have all the information I need. Let me verify the specific claim about batch-size confounding, since the harsh critic said "the batch size differs (4096 vs 2048), which confounds the comparison":

Looking at Table 2: SimCLR 100-epoch uses batch 2048, SimCLR 1000-epoch uses batch 4096. The comparison is baseline vs LDReg **at the same batch size** — batch size is not confounded since LDReg and its baseline share the same batch size. The reviewer misinterpreted the table. This criticism is factually wrong.

Let me now produce the final consolidated review.

## Summary

The paper identifies **local dimensional collapse** as a distinct failure mode in SSL (representations can have high global effective rank yet low local intrinsic dimensionality), and proposes **LDReg**, a regularizer that maximizes the geometric mean of sample-wise LIDs. The regularizer is motivated by a theoretical derivation of an asymptotic Fisher-Rao metric for local distance distributions, which yields the insight that LID should be compared and aggregated on a logarithmic scale. Experiments across SimCLR, BYOL, and MAE on ImageNet linear evaluation, transfer learning, and COCO detection show consistent improvements.

## Strengths

1. **Identification of local dimensional collapse as a distinct phenomenon.** The paper demonstrates empirically (Table 1, Fig. 2c–d) that BYOL representations have high effective rank (~584) but low geometric mean LID (~15.9), showing that global and local collapse are separable. This goes beyond prior work that only considered global dimensional collapse.

2. **Theoretically grounded regularizer.** Lemma 1 derives a closed-form asymptotic Fisher-Rao distance \(d_{\AFR}(F,G)=|\ln(\IDstar_G/\IDstar_F)|\) for smooth growth distributions, and Theorem 1 shows the Fréchet mean corresponds to the geometric mean of LID values. This gives a principled justification for using log-LID and the geometric mean — insights that apply beyond SSL.

3. **Consistent improvements across diverse SSL methods and tasks.** LDReg improves linear evaluation on ImageNet for SimCLR (+0.5%), BYOL (+0.9%), and MAE (+0.6%) with ResNet-50/ViT-B (Table 1). The transfer learning gains are more substantial (e.g., SimCLR 1000-epoch: +3.5% on CIFAR-100, +6.3% on Cars in Table 2), and COCO detection improves for BYOL (+0.52 AP\(^\text{bb}\)) and long-trained SimCLR (+0.67 AP\(^\text{bb}\)). The breadth of the positive results (across contrastive, non-contrastive, and generative SSL) strengthens the empirical case.

4. **Empirical link between augmentation strength and local dimensionality.** Figure 2b shows that stronger color jitter monotonically increases LID and correlates with linear evaluation accuracy, providing a mechanistic explanation for why data augmentation helps avoid collapse beyond global decorrelation arguments.

5. **Demonstration that global rank and local LID capture complementary information.** Table 1 shows SimCLR+LDReg and SimCLR-Tuned have similar effective ranks (~526–562) but different accuracies (64.8% vs. 67.2%) and different LIDs (20.0 vs. 26.1), supporting the paper's central claim that local dimensionality provides information not captured by global effective rank.

## Weaknesses

### Fatal
None.

### Major

1. **No uncertainty quantification.** All results are reported as single runs without standard deviations, confidence intervals, or significance tests. The headline ImageNet linear evaluation improvements are small (0.1%–0.9%), and without variance estimates these could be within random seed variation. The broader pattern across many settings is suggestive, but the lack of multiple runs is a significant evidential gap, especially for a paper whose core empirical claim is that LDReg "consistently improves" SSL methods.

### Minor

1. **Within-batch LID estimation is not validated against a global reference.** The LID estimator computes pairwise distances within a single batch of 2048 (or 4096) augmented views. Since batch neighbors are drawn from the augmentation distribution rather than the full data geometry, it is unclear whether these estimates reliably approximate the true LID that would be computed over a large reference set. The paper provides indirect validation (coherent patterns with augmentation strength, training curves), but a direct comparison — e.g., computing LID on a fixed large reference set at selected checkpoints — would substantiate the methodology.

2. **No ablation of the core design choice.** The Fisher-Rao derivation motivates using log-LID rather than raw LID, but the paper does not test whether a simpler linear penalty on estimated LID (without the log transform) produces different results. This makes it impossible to attribute the empirical gains specifically to the Fisher-Rao formulation versus the general idea of encouraging higher LID.

3. **Claim that FR is "preferable" to KL is unsubstantiated.** The paper states (lines 402–405) that "the asymptotic Fisher-Rao metric is preferable (in theory) to the asymptotic KL distance" but provides no proof, reference, or argument for this claim. This does not affect the main contribution but is an unsubstantiated assertion.

4. **Choice of L1 vs L2 regularization variant is unspecified.** The paper defines both an L1-style loss and an L2-style loss (Eq. 6) but does not state which variant was used in any of the experiments. This is an easily fixable clarity issue.

5. **No hyperparameter sensitivity analysis.** Results are reported at a single setting (k=64, one β per method), with no exploration of how performance varies with neighborhood size k, the regularization weight β, or the choice between L1 and L2 forms.

### Trivial

1. **No discussion of computational overhead.** Computing pairwise distances within a batch (O(N²d)) is non-trivial for large batches, but the paper does not report wall-clock time or relative training cost compared to baselines.

## Nice-to-Haves

- **Comparison to alternative regularizers:** Adding a Barlow Twins-style redundancy-reduction term or VICReg variance term to the same SSL baselines would clarify whether LDReg's local approach provides benefits that global decorrelation regularizers do not.
- **Validation of within-batch LID estimation:** A simple experiment comparing within-batch LID estimates to LID computed over a large fixed reference set (e.g., a subsampled training set) for a few checkpoints would address the main methodological concern.
- **Ablation of log vs. linear LID penalty:** Testing whether a raw LID penalty (without the log transform) performs similarly would isolate the value added by the Fisher-Rao theoretical framework.

## Removed Points

These points from the reviewers are removed and should be treated with caution; they do not appear in the final assessment:

- **"Batch size differs (4096 vs 2048), which confounds the comparison"** (Harsh Critic, regarding Table 2). Factually wrong: the comparison is always baseline vs. LDReg at the **same** batch size. The different batch sizes are across different experimental settings (100-epoch vs. 1000-epoch SimCLR), which are not compared against each other.
- **Generic characterizations of gains as "tiny" or "minimal" without distinguishing between settings.** The ImageNet linear eval gains are small (0.1-0.9%), which is acknowledged in the Major weakness above. However, the transfer learning gains (Table 2: CIFAR-100 +3.5%, Cars +6.3%) and COCO detection gains (BYOL: +0.52 AP\(^\text{bb}\)) are non-trivial. Painting all results as "minimal" is misleading.

## Novel Insights

The harsh critic's observation that the paper's theoretical apparatus (Fisher-Rao metric, log-scale comparison) is tested only as a whole, without isolating the contribution of each component, is a genuinely valuable critique. The paper would be substantially stronger if it ablated (a) log-LID vs. raw LID regularization and (b) within-batch vs. reference-set LID estimation. Additionally, the contrast between the careful theoretical development and the thin empirical reporting (single runs, no validation of the LID estimator) is a structural gap that the paper should address.

None beyond the paper's own contributions.

## Suggestions

1. Report each main result (Tables 1–3) with at least 3 random seeds and include means ± standard deviations, or provide evidence that single-run variability is negligible.
2. Add a direct empirical comparison between the proposed log-LID regularizer and a simple linear penalty on raw estimated LID, to isolate the benefit of the Fisher-Rao formulation.
3. Validate the within-batch LID estimator by comparing it against LID computed over a large fixed reference set (e.g., the full training set subsampled once per epoch) for a subset of checkpoints.
4. State explicitly whether L1 or L2 regularization was used in each experiment, and include a brief sensitivity analysis over k (e.g., {16, 32, 64, 128}) and β.
5. Provide a brief discussion of computational overhead (wall-clock time per epoch with and without LDReg) to help practitioners assess the cost-benefit trade-off.
