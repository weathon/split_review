Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

This paper proposes Regression-based Test-Time Adaptation (RTA), a method that trains a lightweight regression tree on pseudo-labeled images to predict cross-entropy loss from logits, then uses those predictions to select high-confidence augmented views during test-time adaptation of CLIP. The key insight is that a regression mapping from logits to label cross-entropy loss can be learned offline from diverse unlabeled data and applied to any downstream domain without retraining.

## Strengths

- **Ceiling TTA experiment provides compelling motivation.** Tables 1 and 2 show that selecting augmented views via oracle label cross-entropy loss ($H_{\text{LCE}}$) yields massive gains over entropy-based selection — e.g., ViT-B/16 on IN-1k reaches 89.0% with LCE-guided selection vs 70.6% with entropy-based selection. This clearly demonstrates the potential of loss-based view selection and justifies the paper's direction.

- **Consistent improvements across diverse benchmarks and architectures.** RTA achieves state-of-the-art results on single-label ImageNet variants (Table 3: RN50 average 51.85% vs BCA 49.94%), cross-domain datasets (Table 4: RN50 average 61.78% vs BCA 61.44%), and multi-label tasks (Tables 5–6: ViT-B/16 MSCOCO mAP 58.95% vs ML-TTA 57.52%). The method works for both ResNet-50 and ViT-B/16 backbones and across single-label and multi-label settings.

- **Method is simple and computationally lightweight.** RTA uses only 1,000 pseudo-labeled samples to train a LightGBM decision tree (depth 5, max 16 leaves), which adds negligible cost at test time compared to methods requiring gradient updates or memory banks.

- **Visual and statistical evidence supports the logits–loss relationship.** t-SNE visualizations (Figure 2) show clear color clustering with label loss, and Spearman rank correlation analyses (Figure 3) reveal significant monotonic relationships between top logit features and cross-entropy loss across multiple datasets.

## Weaknesses

### Fatal

None.

### Major

- **The core regression mechanism is never directly validated.** The paper never measures how well the learned decision tree actually predicts cross-entropy loss. There is no scatter plot, rank correlation, or MSE report comparing the tree's predicted loss against true LCE on any held-out labeled set, nor on the augmented views it is meant to score. The downstream classification results serve as indirect validation — the method does improve accuracy — but the reader cannot assess whether the tree is genuinely approximating CE loss or functioning as an opaque feature selector whose success is tied to the specific training data distribution. This is the central claim of the paper and it goes unevaluated.

### Minor

- **Marginal improvements for ViT-B/16 on cross-domain benchmarks.** On the 10 cross-domain datasets (Table 4, ViT-B/16), RTA achieves 68.70% average accuracy vs BCA's 68.59% — a difference of only 0.11%. On several datasets (Pets, Flowers, DTD, EuroSAT) RTA actually underperforms BCA. This weakens the claim of consistent superiority, especially since ViT-B/16 is the more modern and practically relevant backbone. The RN50 results and multi-label results are stronger, but the cross-domain ViT-B/16 performance does not clearly separate RTA from prior work.

- **The paper overclaims generalization to "arbitrary test distributions."** The abstract, introduction (line 82), and conclusion (line 502) all state that RTA adapts to "arbitrary test distributions." This is not supported: the regression tree is trained on ImageNet validation data and tested on domains that, while diverse, share the ImageNet class vocabulary and are standard CLIP benchmarks. Without experiments on truly unrelated domains or class vocabularies, the "arbitrary" claim is unjustified.

- **Large unexplained gap between oracle LCE performance and RTA.** Table 2 shows oracle LCE(64) on ViT-B/16 IN-1k reaches 89.0%, while RTA achieves 71.13% (Table 3) — an 18 percentage-point gap. This suggests the learned regression mapping is a substantially degraded proxy for true loss, yet the paper offers no analysis of where the degradation comes from (pseudo-label noise, limited feature coverage of the tree, training on original vs augmented views).

- **The regression tree is trained on original (unaugmented) images but applied to augmented views.** Section 4.2 trains the tree on original images with pseudo-labels to avoid augmentation costs, but at test time it scores augmented views. The paper asserts that "the original image itself can actually be regarded as a view," which hand-waves the potential distribution shift between original-image logits and augmented-view logits. This design choice is not empirically tested.

- **No baseline using maximum softmax probability for view selection.** A simple baseline that selects views by the maximum predicted-class probability would directly test whether the learned regression tree adds value beyond a cheap, label-free confidence proxy. Its absence makes it harder to attribute gains specifically to the regression mechanism.

- **No error bars or run-to-run variability reported.** The ViT-B/16 cross-domain average improvement of 0.11% is almost certainly within experimental noise, but without any measure of variance the reader cannot judge reliability. This is particularly important given that many reported margins are small.

### Trivial

- The t-SNE visualizations and Spearman analyses in Section 4.1 use *true* labels, while the actual method uses *pseudo-labels*. The paper should acknowledge this gap between the motivating evidence and the practical regime.

## Nice-to-Haves

- A direct diagnostic of the learned mapping: scatter plot of predicted vs. actual LCE on a held-out labeled set, with correlation coefficient and MSE, would transform the reader's confidence in the method.

- A transfer experiment where the regression tree is trained on a dataset with no class overlap to the test tasks (e.g., Places365) would test whether the learned mapping captures a universal view–loss relationship or depends on domain proximity.

- Discussion of failure modes: when does the regression tree make poor predictions, and what types of views does it systematically misrank?

- Reporting the computational cost of the offline training stage (wall-clock time, GPU requirements, data volume) to help practitioners assess practicality.

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **"The regression relationship is presented as a discovery, but is largely tautological"** — REMOVED. The paper's contribution is not discovering that logits relate to loss (which is definitional), but learning this mapping from pseudo-labeled data and deploying it for view selection without labels. The framing could be toned down but the core novelty is real.

- **"The method requires collecting a suitably diverse unlabeled image set, which may not be available in deployment"** — REMOVED. This is scope creep. Many TTA-adjacent methods require some form of offline preparation (e.g., cache initialization, prompt bank construction). The paper is explicit about this requirement and uses only 1,000 samples, which is modest.

- **"Multi-label adaptation details are not specified — input structure and preprocessing for multi-label logits are unclear"** — REMOVED. The paper states it follows the ML-TTA framework for multi-label settings (line 390: "the TTA process follows the settings of Zero and ML-TTA"). While more detail would be welcome, the claim that this harms reproducibility is overstated given the reference to established frameworks.

- **"Statistical error bars or multiple-run averages should be reported" (as a Major/Fatal concern)** — DEMOTED to Minor (already listed above under Minor). In the TTA-for-CLIP literature, single-run evaluation is the norm (TPT, Zero, BCA, TDA, ML-TTA all report single-run numbers). Demanding error bars elevates a community-wide convention into an individual-paper weakness. The point is valid but belongs in Minor/Nice-to-Have, not as a fatal or major objection.

## Novel Insights

The harsh critic rightly identifies that the paper's strongest contribution — the idea that a regression mapping from logits to loss can be learned offline and reused across domains — is never directly validated: we don't know whether the tree actually predicts loss well or merely acts as a domain-specific feature selector. This is an unusually sharp lens for evaluating TTA methods: many papers in this area rely entirely on downstream accuracy as the validation signal, but here the method makes a specific mechanistic claim (regression predicts CE loss) that would benefit from a direct probe. The tension between the compelling ceiling experiments and the unevaluated learned mapping is the paper's central unresolved question.

## Suggestions

- Add a scatter plot of predicted loss vs. actual LCE on a held-out subset of ImageNet validation data (or any labeled dataset), reporting Spearman correlation and MSE. This is a single figure that would address the largest gap in the evaluation.

- Tone down "arbitrary test distributions" to "diverse test distributions" or similar, and acknowledge the limitation that RTA has only been tested on domains sharing CLIP's pretraining vocabulary.

- For ViT-B/16 cross-domain results, explicitly note that the improvement is marginal and discuss why RN50 benefits more from RTA than ViT-B/16.

- Discuss the oracle–RTA performance gap: where does the 18% go, and what would it take to close it?

---

## Score and Decision

### Calibration anchors across all rounds:

**Round 1 (bracketing):**
- `pdzHpQbGrn` — Active test-time prompt learning (avg 2.50, weak anchor). RTA is substantially stronger: cleaner methodology, broader evaluation, clearer motivation.
- `ZaudLwn0Hm` — Prototypical evaluation for few-shot (avg 2.50). RTA is clearly stronger.
- `HfJxXbXlYJ` — LLM2CLIP (avg 3.00). Different problem setting; RTA is more targeted and better evaluated.
- `j1FLTvgyAh` — Multi-Vision Multi-Prompt (avg 2.50). RTA is clearly stronger.
- `75PhjtbBdr` — ML-TTA (avg 6.25, accepted). Direct baseline; RTA outperforms it but ML-TTA's core contribution is more thoroughly analyzed within its scope.
- `kIP0duasBb` — RLCF (avg 6.67, accepted). Broader task coverage (3 tasks); RTA is somewhat narrower in scope.
- `KNtcoAM5Gy` — BaFTA (avg 5.50, rejected). RTA is stronger — cleaner methodology, no fatal flaws.
- `yD2JMeKumt` — DOTA (avg 6.00, rejected). Comparable evaluation scope; RTA has a more novel mechanism but similar gaps in direct validation.
- `5Ca9sSzuDp` — Interpreting CLIP (avg 8.00). Clearly stronger paper with more thorough analysis.
- `1aF2D2CPHi` — Open-vocabulary customization (avg 8.00). Stronger.
- `3i13Gev2hV` — Compositional entailment (avg 8.00). Stronger.
- `uAFHCZRmXk` — Modality gap analysis (avg 8.00). Stronger.

**Round 2 (narrowing, 4.5–7.0):**
- `z7PhIgVmZU` — BAT-CLIP (avg 5.50, rejected). Had fatal methodological issues (using ground truth labels). RTA is stronger — no comparable fatal flaws.
- `iGbuc9ekKK` — Duoduo CLIP (avg 5.75). Different task; not directly comparable.
- `PxL35zAxvT` — TTA with auxiliary tasks (avg 4.67). RTA is stronger.
- `VLuJL8cnGk` — Novel view synthesis (avg 5.00). Different task.
- `TD3SGJfBC7` — Few-shot TTA for CLIP (avg 6.25, accepted). RTA is comparable in quality.

### Round 1 bracket: 5.0–6.5

**Round 2 narrowing:** RTA is clearly stronger than BAT-CLIP (5.50), comparable to ML-TTA (6.25) and DOTA (6.00) in terms of contribution clarity and experimental thoroughness, but somewhat below RLCF (6.67) in breadth of validation.

RTA has a genuinely novel idea, compelling ceiling experiments, comprehensive benchmarks, and consistent improvements. However, the core mechanism is never directly validated, the ViT-B/16 cross-domain gains are marginal, and the "arbitrary distributions" claim overreaches. These issues are addressable but prevent the paper from being a clear accept. The paper is comparable to DOTA (6.00, rejected) and ML-TTA (6.25, accepted) in overall quality — slightly better motivation than DOTA, but with a similar gap in validating its central mechanism.

**Final score: 6.0.** The paper is a solid contribution with a novel idea and good experimental coverage, but the missing direct validation of the regression mechanism and the marginal ViT-B/16 cross-domain results keep it from being a clear accept.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>