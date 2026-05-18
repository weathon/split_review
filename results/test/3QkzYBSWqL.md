Now I have a comprehensive understanding of the paper and can verify all reviewer claims against the actual text. Here is the consolidated review:

---

## Summary

This paper introduces Universal Backdoor Attacks — the first data-poisoning backdoor method that is many-to-many, enabling an attacker to cause misclassifications into *any* target class rather than a single predetermined class. The key innovation is using LDA on a surrogate model's latent space to generate class-specific binary trigger encodings that share structure across classes, creating "inter-class poison transferability." The method achieves >80% ASR on ImageNet-1K with only 0.16% poisoned data, scales to 6,000 classes, and resists four standard defenses.

## Strengths

- **First demonstration of a many-to-many backdoor attack at low poisoning rates.** Prior backdoor attacks (BadNets, Blended, etc.) are many-to-one; this paper shows a single universal backdoor can achieve >80% ASR across all 1,000 ImageNet-1K classes with 0.16% poisoning (Table 1, Section 4.2). Naïvely composing many-to-one attacks would require vastly more poisoned samples.

- **Discovery and empirical validation of inter-class poison transferability.** The paper demonstrates that poisoning one set of classes increases ASR on a disjoint set (Section 3.2, Figure 4). By fixing one poison per class in set B and varying poisons in set A, ASR on B rises from negligible to >70%. This shows that protecting a single class requires protecting the entire dataset — a practically important finding.

- **Scaling to datasets with thousands of classes.** The attack is evaluated on ImageNet-2K, ImageNet-4K, and ImageNet-6K (up to 7.8M samples, 6,000 classes) with only 0.15% poisoning, achieving 47.31% ASR on ImageNet-6K (Table 2, Section 4.3). The baseline collapses on larger datasets, demonstrating a meaningful robustness advantage.

- **Robustness against multiple defenses.** The universal backdoor resists fine-tuning, fine-pruning, Neural Cleanse, and Neural Attention Distillation, with ASR dropping by at most 2.6% (Table 3, Section 4.5). The paper also shows that ~40% clean data is needed to fully remove the backdoor via fine-tuning (Figure 5), which is impractical at web scale.

- **Trigger-agnostic methodology.** The method works with both patch and blend triggers (Figure 2, Section 3.4), showing the core LDA-based encoding approach is not tied to a specific trigger pattern.

## Weaknesses

### Fatal
None.

### Major

1. **Surrogate model shares the same architecture as the victim for the flagship experiments.**  
   For ImageNet-1K (the main effectiveness results in Table 1, defense evaluations in Table 3, and the transferability experiment in Figure 4), the surrogate is a pre-trained ResNet-18 — *the same architecture trained from scratch as the victim* (Section 4.1, lines 106–108). This is a very favorable condition: the attacker essentially has access to a model that already knows the relevant feature space. While the scaling experiments (ImageNet-2K through 6K) do use a CLIP ViT surrogate with a ResNet-101 victim, the victim is still a ResNet, so cross-architecture mismatch is tested only in one direction. The paper acknowledges in Limitations (line 194) that it "assume[s] that the attacker can access similarly accurate surrogate classifiers," but does not test scenarios where the surrogate is from a genuinely different architecture family (e.g., ViT surrogate → ResNet-18 victim on ImageNet-1K) or trained on a different data distribution. Without this, the generality of the attack's effectiveness is incompletely validated for the settings emphasized most in the paper.

2. **Lack of per-class ASR distribution information.**  
   ASR is reported only as the mean across all classes (Section 3.1, Eq. 1). With 2,000 poisons and 1,000 classes, the paper does not specify how target classes are selected for poisoning in Algorithm 1 (shown as an image, not text), nor does it report any per-class statistics (e.g., quantiles, worst-case ASR, fraction of classes with near-zero ASR). If some classes receive few or no poison samples directly, their ASR depends entirely on transferability — a finding that would *strengthen* the paper, but the data to assess this is not provided. The mean could conceal substantial per-class variation that matters for the practical threat assessment of a "universal" backdoor.

### Minor

1. **Incomplete isolation of the transferability mechanism.**  
   Section 4.4 demonstrates inter-class poison transferability and shows the baseline (randomly colored square triggers) does not exhibit it. However, the paper does not include a control using *random binary strings of the same length* (n=30) that are *not* derived from the surrogate's latent LDA space. Such a control would isolate whether the transferability is specifically due to the LDA-based encoding of salient features, or whether any structured binary encoding would suffice. The baseline uses randomly colored squares (Section 4.1, line 97), which differ in structure from binary encodings in multiple ways. As written, the central explanatory mechanism remains suggestive rather than fully isolated.

2. **Overclaim of "comprehensive" defense evaluation.**  
   Contribution (3) claims the attack is "robust against a comprehensive set of defenses" (line 22), but only four defenses are evaluated (Table 3), all with hyperparameters optimized for BadNets rather than universal backdoors. While the results are valid for the tested set, the coverage is not truly comprehensive, and the paper's conclusion that "existing defenses are ineffective" (line 201) is appropriately tempered by the acknowledgment of this limitation in Section 4.5. This is a presentation issue rather than a technical flaw.

### Trivial
None.

## Nice-to-Haves

- **Sweep over the number of LDA components *n*.** The paper uses n=30 for all experiments and notes this is too small to uniquely encode all 1,000 classes. A sweep (e.g., n = 10, 30, 50, 100) with fixed total poisons would clarify the trade-off between encoding precision and poison efficiency.

- **Sensitivity analysis for the number of images used to estimate class means.** The paper uses 25 images per class for LDA (Section 4.1, line 108). A brief note on how this affects encoding quality would improve reproducibility.

- **Soften "first to study" claim.** The paper states "we are the first to study many-to-many backdoors" (line 97). Rephrasing to "the first data-poisoning backdoor that simultaneously targets all classes" (line 192 already uses this more precise wording) would avoid potential scrutiny from work on multi-target attacks in adjacent threat models.

## Removed Points

The following criticisms raised by reviewers are removed per policy:

- **"Linear Discriminate Analysis" typo.** Per policy, potential parser/formatting artifacts are removed — the original submission likely has the correct spelling.
- **Concerns about missing appendix content or footnoted references (marked ¹, ², ³).** These sections are stripped during PDF parsing; they exist in the original submission.
- **Criticisms about the existence or release status of models/datasets cited.** All cited entities are assumed to exist as of the current date.

## Novel Insights

Beyond the paper's own contributions, a key insight that emerges from the reviews is that the universal backdoor reframes the threat model from *class-level* to *dataset-level* integrity. In traditional many-to-one attacks, a defender can prioritize protecting a few high-value classes. This paper shows that because inter-class transferability allows poisons in any class to reinforce attacks on all others, the defender must protect the entire dataset uniformly — a fundamentally different and more difficult defense problem. The finding that ~40% clean data is needed to remove the backdoor (Figure 5) underscores this shift: at web scale, validating even 1% of data is already impractical, and 40% is essentially impossible.

## Suggestions

1. **Run a surrogate architecture swap on ImageNet-1K.** Use a pre-trained ViT (or VGG, or ConvNeXt) as the surrogate with a ResNet-18 victim to verify that the attack's effectiveness on ImageNet-1K does not rely on surrogate-victim architectural similarity. This is the single most impactful additional experiment for strengthening the paper's claims.

2. **Report per-class ASR statistics for the flagship setting.** At minimum, report the 10th, 50th, and 90th percentiles of per-class ASR, along with the fraction of classes achieving >50% ASR. Clarify in the text how target classes for poisoning are selected (uniformly, weighted, or otherwise) in Algorithm 1.

3. **Add a random-binary-string control for the transferability experiment.** Replace the LDA-derived encodings with random 30-bit strings (same length, same structure) and repeat the Figure 4 measurement to confirm that the latent structure — not just any binary encoding — drives transferability.

4. **Tone down "comprehensive" in contribution (3)** to "a suite of state-of-the-art defenses," which more accurately reflects the evaluation scope.

## Score and Decision

This paper addresses a genuinely novel and important problem — many-to-many backdoor attacks — and provides a clever, effective solution with impressive empirical results. The three major/minor issues identified (surrogate architecture overlap in flagship experiments, missing per-class ASR statistics, incomplete mechanistic control) are substantive but all addressable with additional experiments; none invalidates the core contribution. The paper's originality and potential impact are high.

**MY FINAL SCORE:** <score>6.5</score>  
**MY FINAL DECISION:** <decision>Accept</decision>