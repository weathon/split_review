Now I have everything I need to write the consolidated review.

## Summary

This paper proposes SBGC, an unsupervised framework for change detection in heterogeneous remote sensing images. The method combines (1) self-supervised contrastive learning via pseudo-Siamese networks to extract features from image patches, and (2) bidirectional graph comparison (BGC) that maps KNN graph structures between modalities and compares them bidirectionally to capture change information. Experiments on three heterogeneous datasets (NIR+MS, SAR+MS, MS+SAR) show competitive OA and KC against seven unsupervised baselines, with particularly strong efficiency gains.

## Strengths

- **Bidirectional graph comparison is a principled extension of prior graph-based methods.** Prior work (NPSG, INLPG, SRGCAE) performs a one-way comparison between the mapped graph and the post-event graph. SBGC adds a second comparison term between the original pre-event graph and the mapped graph, which is conceptually motivated and supported by the ablation: going from one-way to bidirectional (with SSL fixed) improves KC on all three datasets (e.g., Sardinia: 80.32% → 86.21%).

- **State-of-the-art or competitive results with significantly lower computation time.** On the California dataset, SBGC achieves 88.94% KC in 42.78s, compared to the second-best INLPG at 86.65% KC in 278.39s—a ~6.5× speedup. The method obtains the highest KC on all three datasets, often by a meaningful margin (e.g., +14.38% KC over the second-best PMBCN on Sardinia).

- **Ablation study isolates both SSL and BGC contributions.** The three-condition design (raw+one-way → SSL+one-way → SSL+BGC) separates the benefit of learned features from the benefit of bidirectional comparison, confirming each component contributes positively across all datasets.

- **Hyperparameter analysis for patch size.** Fig. 4 systematically varies patch size p and identifies a principled trade-off (too large introduces redundancy, too small misses object detail), with p=9 providing good performance across datasets.

## Weaknesses

### Fatal
None. The paper's core claims are supported by the ablation and comparative experiments.

### Major

- **The self-supervised learning loss in Eq. (1) lacks standard collapse-prevention mechanisms, and the paper provides no evidence that the learned feature space is meaningful.** The loss
  $$\mathcal{L}_{\mathrm{CL}}^{\chi}=-\sum_{i=1}^{M}\log\frac{d_{\Theta}(z_{x^{i}},p_{x^{i}})}{\sum_{j=1}^{M}d_{\Theta}(z_{x^{j}},p_{x^{j}})}$$
  contains only positive pairs (different augmentations of the same patch) in both numerator and denominator, with no negative pairs from different patches. Critically, the paper does not mention a stop-gradient, EMA, or any explicit collapse-prevention mechanism that methods like BYOL or SimSiam rely on. A collapsed solution where all patch representations are identical would yield d(z,p)=1 for all pairs and a finite loss—the loss provides no gradient pressure to separate different patches' representations. While the ablation shows SSL improves over raw pixels (Table 3), this only demonstrates that *any* learned feature extractor beats raw pixel values; it does not validate that the specific SSL objective produces discriminative or meaningful representations. The paper should include feature-space analysis (e.g., cosine similarity distributions, t-SNE visualization) and compare against a proper SSL method (SimCLR, BYOL with stop-gradient, or even a supervised baseline) to demonstrate that the learned features carry useful structure beyond random or trivial representations.

### Minor

- **Weak baseline for the SSL ablation.** The "basic framework" in the ablation (condition 1) uses raw pixel values as patch features. This is an extremely weak comparator—essentially any learned representation (including a randomly initialized network) is likely to outperform raw pixels. The improvement from condition 1 to condition 2 therefore does not specifically validate the paper's SSL design; it only shows that learned features are better than no learned features. A condition using features from a proper contrastive method or even random network features would be needed to isolate what the specific SSL loss contributes.

- **Single-run evaluation without error bars.** All experiments report a single run (Table 2). While single-run evaluation is common in remote sensing CD papers, the absence of any variance estimate makes it impossible to assess whether the reported improvements (especially small margins like the 1.47% KC gap over SRGCAE on Shuguang) are statistically significant.

### Trivial

- **Notation inconsistency.** The loss in Eq. (1) uses subscript $\Theta$, while the text earlier refers to $d_{\theta}(\cdot)$. This is a minor presentational issue.

- **The adaptive K formula** $\lceil(\sqrt{M}+\sqrt{M}/10)/2\rceil$ is stated without intuitive justification in the paper (though it is adopted from Sun et al., 2021a, which provides context).

## Nice-to-Haves

- **Explore stronger augmentations.** The paper uses only horizontal/vertical flipping. Standard SSL methods benefit from color jitter, cropping, and rotation. While some of these may be inappropriate for CD, a brief discussion or ablation would strengthen the work.
- **Provide a theoretical intuition for why the specific two-term formula in Eq. (4) captures change information.** An illustrative synthetic example or geometric intuition would help readers understand why the combination of the two absolute differences is more informative than a one-way comparison.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The graph mapping is critically underspecified and not reproducible."** — The paper states the mapped graph $G_{x^i}^Y$ is "constructed using the spatial coordinates of the $K$ patches most similar to $x^i$." This follows the standard approach in the graph-based heterogeneous CD literature (Sun et al., 2021b, 2022): take the KNN neighbor indices from modality X and use those same spatial coordinates to index features from modality Y. The description, while concise, is clear enough for reproducibility by readers familiar with the field. Removed for being an overstatement.

2. **"The ablation does not isolate SSL contributions (conditions conflate changes)."** — The ablation actually has three conditions: (1) raw+one-way, (2) SSL+one-way, (3) SSL+BGC. This properly isolates SSL (1→2) and BGC (2→3). The critic themselves corrected this later in their "Missing Experiments" section. Removed as factually incorrect in its original form.

3. **"Sub-ResNet18 modifications not specified."** — The paper states: "modifying the stride of the first layer from 1 to 2 and removing the third and fourth layers." This is specific enough. Removed.

4. **Various missing hyperparameter details (batch norm, learning rate schedule, weight decay).** — These are practical implementation details that go beyond what is expected in a short paper; the key hyperparameters (learning rate 5e-2, batch size 2048, epochs 50, SGD optimizer) are reported. Removed per nitpick rule.

5. **"The loss is mathematically invalid and not salvageable."** — While the loss is non-standard and lacks theoretical guarantees, it does encourage augmentation invariance. Calling it "invalid" or "unsalvageable" is not supported by the paper's empirical results (which show SSL helps). The concern about collapse is real (kept above), but the characterization is too strong. Recharacterized as a major weakness with appropriate nuance.

6. **Strength from Strength Finder: "Ablation studies provide clear causal evidence for each contribution."** — This conflicts with the verified weakness that the SSL baseline (raw pixels) is too weak to properly validate the specific SSL design. The ablation is well-structured but the baseline choice undermines the causal claim for SSL. Demoted.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a meaningful tension: the paper's high-level approach (learned features + bidirectional graph comparison) is empirically validated and shows clear gains, but the specific SSL formulation raises unanswered questions about feature quality and collapse. This gap between empirical results and methodological rigor is common in applied remote sensing papers that borrow SSL tools without fully engaging with the self-supervised learning literature's theoretical requirements.

## Suggestions

1. **Fix the SSL loss or justify it empirically.** Either (a) replace Eq. (1) with a proper contrastive loss (e.g., NT-Xent) that includes negative pairs, or (b) add a stop-gradient to one branch (making it closer to BYOL/SimSiam), or (c) at minimum provide empirical evidence that the learned features are not collapsed—show distribution of pairwise cosine similarities across patches, or compare against a randomly initialized network to demonstrate that the SSL training actually produces structured representations.

2. **Add error bars or multi-run statistics.** Run each experiment 3-5 times with different random seeds and report mean ± std for OA and KC to establish reliability of the results, especially for the smaller-margin comparisons.

3. **Strengthen the SSL ablation baseline.** Add a condition using a randomly initialized network or a proper contrastive method (SimCLR, BYOL) as the feature extractor, with the same one-way graph comparison, to isolate whether the proposed SSL design is responsible for the improvement or whether any learned features would achieve the same gain.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>