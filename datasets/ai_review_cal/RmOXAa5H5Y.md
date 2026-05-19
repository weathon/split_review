- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have thoroughly cross-checked all claims against the paper. Let me produce the consolidated review.

## Summary

This paper empirically studies combinations of Tree-Wasserstein Distance (TWD) variants (total variation and ClusterTree) with several probability models (softmax, ArcFace variants, simplicial embedding) for self-supervised simplicial representation learning using SimCLR. It proposes a Jeffrey divergence (JD) regularization to stabilize the L1-based TWD training. The key empirical finding is that with the right combination (ArcFace(DCT)+JD with TV), TWD-based simplicial learning can match or outperform the standard cosine similarity baseline on small-scale datasets (STL10, CIFAR10, SVHN), while CIFAR100 remains challenging.

## Strengths

1. **Systematic empirical comparison of design choices.** The paper evaluates multiple probability models (softmax, AF, AF(PE), AF(DCT), SEM) across two TWD variants (TV, ClusterTree) with and without JD regularization. This provides concrete guidance for practitioners choosing configurations for simplicial SSL — a previously unstudied design space.

2. **JD regularization dramatically stabilizes training.** The paper provides clear evidence (Figure 2, Table 1) that JD regularization rescues naive softmax+TWD from severely degraded performance (e.g., TV+Softmax on STL10 jumps from ~43% to ~66% accuracy), and consistently improves all TWD configurations. Proposition 2 provides a theoretical upper-bound justification connecting TWD² to Jeffrey divergence.

3. **Best TWD configuration beats the cosine similarity baseline on 3/4 datasets.** The text reports that AF(DCT)+JD(TV) achieves the highest classification accuracy, comparable to or exceeding cosine similarity on STL10, CIFAR10, and SVHN. This supports the paper's claim that an appropriate TWD-simplicial combination can outperform standard cosine similarity on small-scale problems.

4. **Honest reporting of limitations.** Unlike many papers that only report favorable results, this paper explicitly notes that on CIFAR100 the TWD methods underperform, and that the simple softmax+TWD combination produces poor results. This integrity increases the value of the empirical study.

## Weaknesses

### Fatal

None. The harsh critic's claim of a central contradiction between the abstract and Section 5.2 is based on a misreading. The abstract says *"appropriate choice... outperformed"* (qualified, about the best configuration). The sentence in Section 5.2 about simplicial models with cosine similarity tending toward lower error describes the general trend across *all* configurations — these are different statements about different quantities and are not contradictory. The paper's main empirical claim (best TWD config outperforms cosine baseline on 3 datasets) is supported by the evidence as described in the text.

### Major

1. **Missing baselines: no comparison to other Wasserstein approximations.** The paper motivates TWD as computationally cheaper than Sinkhorn and related to sliced Wasserstein, but never compares TWD against these alternatives (sliced Wasserstein, Sinkhorn, or even plain L1 without tree embedding) in the same SSL setup. Without these baselines, the paper cannot attribute any observed effects specifically to the *tree* structure versus using any L1-based Wasserstein distance.

2. **No variance or confidence reporting.** The paper runs three trials and reports only averages (line 256). Given that many reported differences are plausibly small (e.g., 74.08 vs 73.91 on CIFAR10), standard deviations are essential to assess whether the claimed outperformance is meaningful or within noise. This undermines the strength of the paper's main quantitative claim.

3. **Unjustified temperature discrepancy.** The baseline cosine similarity uses τ=0.07 while all TWD methods use τ=0.1 (line 251). No explanation or sensitivity analysis is provided for this difference. In InfoNCE, temperature strongly affects results; this discrepancy confounds the comparison between TWD and cosine methods.

### Minor

1. **RTWD contribution is overstated.** Proposition 1 shows that the robust TWD variant equals total variation. The paper itself cites Raginsky et al. (2013, Proposition 3.4.1) establishing that 1-Wasserstein with Hamming distance equals total variation. The result follows directly and is listed as a core contribution (item 2 in the Introduction), which inflates the paper's novelty.

2. **No comparison of JD vs KL regularization.** The paper acknowledges Frogner et al. (2015) used KL-based regularization for Wasserstein loss, and notes JD subsumes KL (line 242), but never empirically compares JD against KL regularization. Without this comparison, the specific advantage of JD over a simpler KL regularizer is not established.

3. **No ablation or sensitivity analysis on the JD regularization parameter λ.** The regularization parameter is set to λ=0.1 across all experiments without any tuning or sensitivity study (line 256). It is unclear how robust the results are to this choice.

4. **ClusterTree construction details are missing.** The paper does not describe how many clusters are used, how they are defined, or any implementation details of the ClusterTree — yet this is one of only two tree structures evaluated. This hurts reproducibility.

5. **Evaluation uses only KNN (K=50); no linear probing results reported.** Linear probing is the more standard evaluation protocol for self-supervised learning. Reporting only KNN limits comparability with the broader SSL literature.

### Trivial

1. Minor typo: "adn" instead of "and" (line 251).
2. The sentence "all the simplicial model performances with the cosine similarity combination tended to result in a lower classification error than the combination with TWD and simplicial models" (line 271) is ambiguously worded and could benefit from clarification.

## Nice-to-Haves

- An analysis of *why* CIFAR100 degrades — is it the tree structure, the simplicial constraint, the L1 geometry, or the number of classes? Ablations on tree depth and ClusterTree granularity would be illuminating.
- A visualization or qualitative analysis of the learned simplicial embeddings (e.g., what structure does the tree-embedded space capture that cosine similarity does not?).
- A comparison with Sinkhorn-based or sliced Wasserstein SSL to isolate the effect of the tree structure itself.

## Removed Points

These points from inputs are removed with justification:
- **"Central claim contradiction" (Harsh Critic Point 1)**: The abstract says "appropriate choice outperformed" while Section 5.2 describes the general trend across all configurations. These are different claims about different quantities; no contradiction exists in the paper. The harsh critic misread the sentence.
- **"JD derivation is trivial" (Harsh Critic Point 4)**: Whether it's "trivial" is subjective. The bound in Proposition 2 is a straightforward but non-trivial connection, and the paper's main contribution is empirical (showing it works in practice). The critic's claim that it follows from Pinsker's inequality in a single step is an oversimplification — the bound connects TWD² to JD of tree-embedded vectors, not directly to L1. Demoting from the harsh critic's framing.
- **"No comparison to other SSL frameworks"**: Criticizing the paper for not testing Barlow Twins is scope creep. The paper is explicitly about SimCLR; it mentions Barlow Twins only as a possible extension. The paper should be evaluated on whether it does its stated task well.
- **"No ablation of tree structure"**: The paper tests two qualitatively different trees (TV depth-1 and ClusterTree). For an empirical study, this is a reasonable range. The critic's demand for varying tree depth and construction method is a nice-to-have, not a core weakness.
- **Strength Finder's generic strength about "Proposition 1 (RTWD = total variation)"**: This is a known result that the paper itself acknowledges is known. Listing it as a core strength is misleading. Moved here.
- **"Missing related works"**: Not verifiable; excluded per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface standard methodological concerns (missing baselines, variance reporting, temperature discrepancy) rather than novel observations about the paper's approach or results.

## Suggestions

1. **Reframe the paper as a frank empirical study with positive and negative findings.** The paper already does this in parts but could make the balanced framing more central. Consider titling it "An Empirical Study of..." (as it already is) and explicitly state in the abstract that TWD outperforms cosine on small datasets but underperforms on CIFAR100, with analysis of why.

2. **Add standard deviations** to all reported results (from the three runs) and comment on whether the best-vs-baseline differences are statistically meaningful.

3. **Justify or align the temperature parameters** between TWD (τ=0.1) and cosine (τ=0.07) settings, or add a sensitivity study showing that the comparison is robust to temperature choice.

4. **Compare against at least one alternative Wasserstein approximation** (e.g., sliced Wasserstein with simplicial models) in the same SSL framework to isolate whether the tree structure specifically matters.

5. **Add linear probing results** as a second evaluation protocol alongside KNN.

6. **Ablate the JD regularization parameter λ** or at minimum show results for a few values (e.g., λ ∈ {0.01, 0.1, 1.0}).

7. **Provide ClusterTree construction details** (number of clusters, method) and consider sharing code to aid reproducibility.
