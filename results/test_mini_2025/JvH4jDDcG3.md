Now I have sufficient calibration anchors. Let me write the consolidated review.

## Summary

This paper introduces CDC (Calibrated Deep Clustering), the first framework to address the overconfidence problem in deep clustering. The core idea is a dual-head architecture: a clustering head produces cluster assignments while a calibration head refines confidence estimates using a novel region-aware penalty based on K-means mini-clusters on features. The calibration head's calibrated confidences are then used by the clustering head for dynamic, per-class pseudo-label selection. Additional contributions include a prototype-based network initialization strategy. The method achieves state-of-the-art clustering accuracy and dramatically lower expected calibration error (ECE) across six benchmarks.

## Strengths

1. **First calibrated deep clustering framework with a well-motivated dual-head design.** The paper identifies an underexplored problem—overconfidence in deep clustering—and proposes a clean architectural solution. The dual-head structure cleanly decouples the conflicting goals of high-confidence clustering and calibrated confidence estimation. Ablation results confirm this: the single-head variant (Clu+Cal) on CIFAR-20 achieves ECE 21.2% vs. CDC-Cal's 4.9% (Table 2-IV).

2. **Confidence-aware dynamic pseudo-label selection with clear empirical benefit.** Eq. (4) uses the calibration head's well-calibrated confidence to determine per-class thresholds adaptively. Table 2-II shows that fixing the threshold at any value (0.99, 0.95, 0.90, 0.80) consistently yields lower ACC than CDC-Cal (e.g., CIFAR-20: best fixed threshold 54.9% vs. CDC-Cal 61.7%), demonstrating the value of the dynamic strategy.

3. **Dramatically lower calibration error on 5 of 6 benchmarks.** CDC-Cal achieves ECE of 1.1% on CIFAR-10 (best prior: 4.9%), 4.9% on CIFAR-20 (best prior: 13.1%), 0.9% on STL-10 (best prior: 6.3%), 0.8% on ImageNet-10 (best prior: 1.5%), and 7.7% on ImageNet-Dogs (best prior: 19.3%). These improvements are substantial and consistently demonstrated across diverse datasets.

4. **Feature prototype-based initialization with striking empirical effect.** The proposed initialization transfers discriminative ability from the pre-trained backbone to the MLP heads. The ablation in Table 2-I shows ACC jumping from 19.1% to 87.2% on CIFAR-10 after applying the proposed initialization—a 4.6× improvement. Proposition 1 provides theoretical grounding.

5. **Competitive failure rejection ability.** Figure 3 shows CDC-Cal achieves AUROC 77.9% (next best: 68.4%), AURC 20.4% (next best: 31.0%), and FPR95 73.4% (next best: 75.7%) on CIFAR-20, indicating better separation of correct and wrong predictions—directly supporting reliable pseudo-label selection.

## Weaknesses

### Fatal

None.

### Major

1. **Overstated "5× average ECE improvement" claim.** The paper claims "surpassing the state-of-the-art deep clustering methods by 5× on average in terms of expected calibration error" (abstract, line 21; introduction, line 43). Computing the ratio of best-prior ECE to CDC-Cal ECE across datasets yields: CIFAR-10 (4.9/1.1 ≈ 4.5×), CIFAR-20 (13.1/4.9 ≈ 2.7×), STL-10 (6.3/0.9 = 7.0×), ImageNet-10 (1.5/0.8 ≈ 1.9×), ImageNet-Dogs (19.3/7.7 ≈ 2.5×). The average across these five is ~3.7×, not 5×. Moreover, **on Tiny-ImageNet, CDC-Cal's ECE (11.0%) is worse than CC's (3.2%)** (Table 1). Including Tiny-ImageNet or using a fair baseline average invalidates the "5×" claim. This is a significant presentation issue—the empirical results are still strong, but the claim should be honestly characterized with the full distribution, including the negative case.

### Minor

1. **Undefined baseline variants (SCAN-2, SCAN-3, SPICE-2, SPICE-3) in the main text.** Table 1 reports multiple variants of SCAN and SPICE, but the main text does not specify what distinguishes SCAN-2 from SCAN-3, or SPICE-2 from SPICE-3 (e.g., different backbones, number of neighbors, threshold settings). The paper references "More details are shown in B.1" (Section 4.1), but leaving readers without even a brief characterization in the main body makes it difficult to assess whether baselines are configured optimally and fairly.

2. **Theoretical analysis relies on an idealized partition assumption.** Theorem 1 proves that confidence penalties occur only in "unreliable regions" *assuming* K-means partitions features into regions that correctly separate reliable from unreliable samples (those that cross clustering decision boundaries). The paper does not establish or test this assumption empirically—e.g., by analyzing which samples fall into which mini-clusters and whether they correspond to actual decision-boundary regions. The theoretical framing over-promises; the method's strength is empirical, not from these conditional guarantees.

3. **Single-run results without variance estimates.** Table 1 reports single numbers for each method and metric. Clustering results, especially ECE, can be noisy due to initialization, batch sampling, and dataset splits. Reporting means and standard deviations over multiple runs would strengthen the evidence and is standard practice for robust experimental evaluation.

4. **No discussion of failure cases or limitations.** The paper does not discuss when the method may not improve calibration (e.g., why CDC-Cal underperforms CC's ECE on Tiny-ImageNet). Adding a limitations section that characterizes when the approach works and when it might not would strengthen the paper.

### Trivial

None.

## Nice-to-Haves

- **Variance reporting:** Adding standard deviations over multiple runs to the main results.
- **Computational cost comparison:** Reporting training time relative to baselines would be useful for practitioners.
- **Ablation on calibration loss variants within the dual-head framework:** The paper compares against LS, FL, L1 added as regularizers to the clustering head. A cleaner ablation keeping the dual-head structure but varying the calibration loss (e.g., standard CE vs. mini-cluster averaging) would better isolate the benefit of the proposed calibration loss.
- **Practical guidance on selecting K:** While K shows robustness to ±20% variation, the absolute K varies widely (40–1000) across datasets, and a clearer selection heuristic or sensitivity study would help adoption.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"Theorem 1 is not sufficiently grounded" (Harsh Critic's point about idealized assumptions):** Kept in Minor above, but the harsh critic's framing as "over-promising" is too strong. Many papers include idealized theoretical analysis; the empirical results validate the method. Retained at Minor level.
- **"FL trade-off in failure rejection" (Harsh Critic):** The paper already acknowledges this trade-off explicitly ("Although Focal Loss (FL) may produce a lower ECE than our method, its clustering ACC is much worse"). This is already addressed. Removed.
- **"Strengthening the Paper on Its Own Terms" section points:** These are nice-to-have suggestions, not weaknesses. Moved to Nice-to-Haves.
- **Missing related works:** Removed per rule (cannot verify external sources).
- **Formatting/style nitpicks:** Removed per rule.
- **Generic/superficial strengths from Strength Finder** (e.g., "this paper addressed an important problem"): Removed.

## Novel Insights

The harsh critic and strength finder both independently identify a key tension: the paper's core claim (5× improvement) is quantitatively unsupported while its underlying methodology is genuinely strong. This tension is illuminating — it suggests a paper that is empirically solid but undermines itself through presentation choices. A more honest framing (e.g., "3-7× improvement on 5 of 6 benchmarks, one negative case") would strengthen rather than weaken the paper, because the actual results are already competitive. The deeper pattern across both reviews is that the paper's most distinctive contribution — the dual-head design with region-aware calibration — is what makes possible both the accuracy gains (via better pseudo-label selection) and the calibration gains (via targeted confidence penalty). This two-way symbiosis is the paper's real novelty, not the precise ECE reduction factor.

## Suggestions

1. Replace the "5× on average" claim with an honest summary: report the range of improvements and explicitly note the Tiny-ImageNet case where ECE does not improve.
2. Define SCAN-2/3 and SPICE-2/3 variants in the main text or a brief table (even one sentence each).
3. Add standard deviations to the main results table and discuss failure cases/limitations.
4. Consider adding an empirical analysis (e.g., scatter plots or t-SNE) showing whether the K-means mini-clusters correspond to reliable vs. unreliable regions as assumed in Theorem 1.

## Score and Decision

**Calibration Summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Post-prediction confidence training | AL4tS0HhJT.md | 2.5 | 1 (low) | Much weaker; withdrawn, unclear contribution |
| Automatic Calibration Diagnosis | p79lnC36CO.md | 2.0 | 1 (low) | Much weaker; reject, limited scope |
| The Map Equation goes Neural | F8l0llkMk0.md | 3.33 | 1 (low) | Weaker; reject, different subfield |
| Optimizing Calibration (CA loss) | 34xYxTTiM0.md | 5.5 | 1 (mid) | Weaker; reject, incremental post-hoc calibration in supervised setting |
| Unlocking Calibration in FL (NUCFL) | Osr0KZJeTX.md | 6.0 | 1 (mid) | Similar quality; accept poster, less novel methodology |
| Pseudo-Calibration (UDA) | USWkUOfxOO.md | 5.5 | 2 (mid) | Weaker; reject, heuristic mixup approach |
| PRO-DSC (Deep Subspace Clustering) | 7psWohxvxp.md | 6.25 | 2 (mid) | Comparable; accept poster, theory+experiments |
| URLOST (Unsupervised Repr Learning) | MBBRHDuiwM.md | 6.4 | 2 (mid) | Comparable; accept poster, wider score spread |
| M3C (Graph Matching/Clustering) | AXC9KydyZq.md | 7.0 | 2 (mid) | Slightly stronger; accept poster, theory+clustering |
| Emergence of meta-stable clustering | eBS3dQQ8GV.md | 7.8 | 1 (high) | Stronger; oral, deep theory paper |
| Candidate Label Set Pruning | Fk5IzauJ7F.md | 8.0 | 1 (high) | Stronger; oral, broader impact |

**Round 1 bracket:** Between 3.5 and 7.5 (clearly above rejected calibration papers, below top-tier oral papers).

**Round 2 narrowing:** Compared against anchors in (4.5, 7.5) range. The paper is stronger than the 5.5-level rejected calibration papers (which are incremental or heuristic) and comparable to/slightly stronger than the 6.0-6.4 accepted papers. It does not quite reach the 7.0+ level due to the overstated claim, lack of variance reporting, and undefined baseline variants — but its core contribution (first calibrated deep clustering framework) is novel and well-supported.

**Final Score:** 6.5

This paper makes a genuine contribution to an underexplored problem with a well-designed method and strong empirical results, but presentation issues (overclaimed improvement rate, undefined baselines, missing variance/limitations) prevent it from achieving the highest tier.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>