- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3
Now I have verified all claims against the paper text. Let me produce the final consolidated review.

---

## Summary

This paper proposes a backdoor defense that trains per-class normalizing flows on self-supervised (SimCLR) feature embeddings to detect and relabel poisoned training samples. The method distinguishes two poisoning scenarios in feature space — non-disruptive (samples stay near their source class manifold) and disruptive (samples become isolated) — and uses density-based scores per class to identify poisoned classes, flag individual poisoned examples, and reassign their original labels via generative classification. Experiments across CIFAR-10, ImageNet, and VGGFace2 show that the defense reduces attack success rate (ASR) below 1% for most of six attack types, while maintaining competitive clean accuracy.

## Strengths

- **Novel, principled approach using generative modeling on self-supervised features.** The paper is the first to apply per-class normalizing flows on SimCLR embeddings for backdoor defense (Section 4.3). This is a genuinely different strategy from existing discriminative defenses (NAD, ABL, DBD, ASD) and is well-motivated by the finding that generative models of RGB images behave unintuitively on outliers, while generative models in semantic latent spaces are more reliable (Section 3.1, citing Kirichenko et al. 2020).

- **Strong empirical results across diverse attacks and datasets.** Table 1 shows ASR below 1% for the majority of 6 attack types (BadNets, Blend, WaNet, ISSBA, Adap-Patch, Adap-Blend) on all three datasets. Particularly notable is performance on Adap-Patch and Adap-Blend (ASR 0.0–0.06%), which were explicitly designed to defeat latent-separability defenses — this directly validates the paper's claim that self-supervised features resist the intended circumvention (lines 257–258).

- **No clean validation data required.** Unlike NAD and ASD (marked with * in Table 1, requiring a small clean subset per class), the defense operates on the potentially poisoned dataset alone. This is a genuine practical advantage explicitly stated and supported by results.

- **Thoughtful ablation of feature extractor choice.** Table 3 compares SimCLR with supervised features and CLIP, showing both self-supervised approaches greatly outperform supervised ones. The paper also honestly discusses that CLIP could itself be backdoored in practice, avoiding overclaiming (lines 269–270).

- **Transparent handling of limitations at higher poisoning rates.** Table 4 and the accompanying discussion (lines 275) acknowledge a slight ASR increase at higher poisoning rates and offer a plausible explanation, rather than papering over the degradation.

## Weaknesses

### Fatal

None.

### Major

1. **Missing ablation: filtering-only vs. full method with relabeling.** The paper presents relabeling as a central contribution (abstract: "considering the triggers as a kind of augmentation"; contribution 3: "the proposed method can cleanse the dataset by pseudo-labeling the poisoned samples"). However, there is no experiment comparing the full method (detect + remove ambiguous + relabel poisoned) to a variant that simply **removes** the identified poisoned samples (i.e., trains only on \(\hat{\mathcal{D}}_C\) and discards \(\hat{\mathcal{D}}_P\)). Without this ablation, it is impossible to determine whether the relabeling step provides any benefit in clean accuracy without raising ASR — which is precisely what the paper claims it does. If filtering alone already achieves comparable ACC and ASR, the relabeling machinery is unnecessary complexity. This is a structural gap in the experimental design relative to the paper's own framing.

2. **No principled procedure for hyperparameter selection without clean data.** The defense relies on four hyperparameters (β_ND=0.6, β_D=0.05, λ=0.75, α=0.15) that are set "based on early validation experiments" (line 246). Under the paper's stated threat model, the defender has only the potentially poisoned dataset — no clean validation set, no knowledge of attack type, and no ground truth about poisoning. The paper provides no unsupervised procedure for choosing these values, and no sensitivity analysis showing that results are stable across a range of values. For example, β_D is described as "the minimum fraction of poisoned samples per class" (line 191), yet the defender does not know this fraction. This undermines the practical deployability of the method. An unsupervised selection method (e.g., fitting a two-component model to score distributions) or a demonstration that performance is broadly insensitive to hyperparameter values is needed.

### Minor

3. **Missing statistical significance / error bars.** No standard deviations, confidence intervals, or multiple-run averages are reported for any of the main results (Tables 1–4). ASR values near 0% can be dominated by random seed variance. The paper should report at least 3–5 independent runs for the core comparisons.

4. **The disruptive-poisoning detection (Section 4.4) uses an ad-hoc histogram method.** The procedure — constructing a 30-bin histogram, finding the minimum on the left from λ, and thresholding the fraction of samples below that minimum — is not a principled statistical test. The bin count (30) and the λ parameter are arbitrary and may behave differently across datasets with different numbers of classes or score scales. A more principled approach (e.g., Gaussian mixture model) would be more convincing.

5. **Scalability / computational cost not discussed.** The method trains per-class normalizing flows. For CIFAR-10 (10 classes) this is trivial, but VGGFace2 has 8,631 identities and ImageNet has 1,000 classes. The paper does not specify how many classes were used in its ImageNet/VGGFace2 subsets, how long training takes, or whether per-class flows become impractical beyond a certain class count. This is a practical concern for real-world deployment.

6. **No false positive / false negative analysis for detection.** The paper reports ASR and ACC but not how many clean samples were incorrectly removed or relabeled, nor how many poisoned samples were missed. This makes it hard to assess the practical cost of the defense beyond aggregate metrics.

### Trivial

None.

## Nice-to-Haves

- **ImageNet-pretrained supervised features as a baseline in Table 3.** The supervised features in Table 3 are trained on the *poisoned* dataset with poisoned labels, which explains their poor performance. Comparing against features from a cleanly pretrained supervised model (e.g., ImageNet-pretrained ResNet) would better isolate whether the issue is poisoning of the supervised model or a fundamental property of self-supervised representations. The CLIP result partially addresses this, but CLIP is trained on much more data.

- **Failure case analysis for adaptive attacks.** The paper notes that relabeling accuracy is lowest for Adap-Patch and Adap-Blend (Table 2) and attributes this to enhanced similarity between clean and poisoned samples. An analysis of what goes wrong (e.g., confusion matrices or visualizations of misclassified samples) would strengthen the paper and guide future work.

## Removed Points

These points were raised by reviewers but are removed from the main assessment with justification:

- **"Comparison to frequency-domain or spectral defenses like Spectral Signatures / activation clustering."** Removed: the paper already compares against four state-of-the-art defenses (NAD, ABL, DBD, ASD). Requesting additional baselines beyond those is a scope-expansion suggestion, not a weakness of the presented evaluation.

- **"ASD's clean-data requirement may give it an unfair ACC advantage."** Removed: the paper already addresses this (lines 244–245, 255), noting that ASD requires clean data and trades higher ACC for higher ASR. The discussion is sufficient.

- **"The poisoning score mechanism needs formal justification."** Removed as a standalone weakness but absorbed into the minor concern about the method's overall characterization. The paper provides a clear qualitative explanation (Section 4.5) and empirical validation (Figure 4 shows clean/poisoned score separation). Formal proofs are not standard for empirical defense papers; the empirical evidence is the primary support.

- **"UMAP visualization may create spurious structure."** Removed: UMAP visualizations are standard practice in the backdoor defense literature (the paper cites Huang et al. 2022; Chen et al. 2022 using the same methodology). Quantitative measures would strengthen the paper but the lack of them is not a weakness given field conventions.

## Novel Insights

The two independent reviews converge on the same two critical gaps: the missing relabeling-vs-filtering ablation and the lack of an unsupervised hyperparameter selection procedure. Neither reviewer questions the core results or the method's architectural novelty — both acknowledge the ASR results are strong, especially on adaptive attacks. However, both also identify that the paper's central claim about relabeling as value-add over detection-based filtering is untested, and the method's real-world deployability is unclear without a way to choose hyperparameters in the assumed threat model. The combination of these two concerns, rather than either alone, is what prevents the paper from being a complete contribution.

## Suggestions

1. **Add the filtering-only ablation.** Train the deployment model on \(\hat{\mathcal{D}}_C\) alone (discarding \(\hat{\mathcal{D}}_P\) and \(\hat{\mathcal{D}}_0\)) and compare ACC/ASR against the full method that relabels \(\hat{\mathcal{D}}_P\). This directly validates the novelty claim.

2. **Address hyperparameter selection.** Either (a) provide an unsupervised selection criterion (e.g., grid search over β_ND, β_D and choose values that maximize the gap between two modes of the \(v_y\) histogram for disruptive detection), or (b) conduct a sensitivity analysis showing performance is stable across a wide range of values, with guidance for practitioners.

3. **Report standard deviations** for at least 3 runs of the main comparisons (Table 1).

4. **Add false positive / false negative rates** for the detection step, quantifying how many clean samples are discarded and how many poisoned samples are missed per attack and dataset.
