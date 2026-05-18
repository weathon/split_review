Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper makes a first attempt at pushing fully quantized training (FQT) to an average of 1-bit per gradient element — below the previous 4-bit frontier. The authors propose two key components: Activation Gradient Pruning (AGP), which prunes less informative gradient groups and allocates higher precision to informative ones to reduce quantizer variance, and Sample Channel joint Quantization (SCQ), which uses different quantization strategies for weight vs. activation gradients to enable practical hardware acceleration. Theoretical regret bounds (convex setting) motivate why Adam is more suitable than SGD in low-bitwidth regimes. Experiments on transfer-learning tasks (six vision datasets + object detection + NLP) show convergent training with ~5–6% average accuracy drop from full-precision gradients, and real hardware speedups up to 5.13× on Hygon CPU and 3.72× on Raspberry Pi 5.

## Strengths

- **First demonstration of convergent training at ~1-bit average gradient precision.** Table 1 shows that with b=4, the method achieves 60.53% (ResNet-18) and 69.97% (VGGNet-16) average accuracy across six datasets, substantially outperforming 1-bit PSQ (54.01% and 64.24%). This is genuinely pushing beyond the existing 4-bit FQT frontier.

- **AGP provides a well-motivated mechanism for variance reduction.** The variance bound in Eq. (24) formally shows reduction from \(\frac{D^{(l)}}{4}\sum_{i=1}^N R_i^2\) (1-bit PSQ) to \(\frac{D^{(l)}}{4B^2}\sum_{i=1}^{N/b} R_i^2\). Figure 11 empirically confirms that datasets with lower quantizer variance (Flowers, Pets) correspond to minimal accuracy loss (<1%). The gradient heterogeneity motivation (Figure "dis") is clearly supported.

- **SCQ enables real hardware speedup by solving the dequantization bottleneck.** The paper correctly identifies that PSQ cannot accelerate weight-gradient computation (requires dequantization before multiplication), and SCQ resolves this via per-channel quantization for weight gradients. Table 3 demonstrates meaningful speedups (up to 5.13× on Hygon, 3.72× on Raspberry Pi 5) — not just theoretical FLOP counts.

- **Theoretical analysis connecting optimizer choice to variance sensitivity.** Theorems 1 and 2 show \(\frac{R^{SGD}}{T} = O(\sigma^2) + O(1)\) vs \(\frac{R^{Adam}}{T} = O(\sigma) + O(1)\), providing formal intuition for why Adam dominates SGD in low-bit regimes. Figure 3 empirically validates this — PSQ+SGD fails to converge while the proposed method+SGD still trains.

- **Generalization to multiple architectures and tasks.** Table 2 shows results on Faster R-CNN (detection, 1.66% mAP drop), MLP-Mixer (classification, 3.52% drop), and BERT (NLP, 8.39% drop), suggesting the approach is not limited to CNNs.

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation study separating AGP and SCQ contributions.** The experiments compare the full method against 1-bit PSQ, but do not isolate the individual contributions of AGP and SCQ. The reader cannot tell how much each component contributes to accuracy improvement vs. speedup. This is the single most important missing experiment — without it, attributing the gains to specific design choices remains speculative.

- **Scope limited to transfer learning (fine-tuning pre-trained binary models).** As the paper acknowledges, training from scratch is not demonstrated. While the paper frames this as "the first step," it substantially limits the contribution's generality and practical impact. The limitation is stated in a "Limitations" paragraph but should be more prominently reflected in the abstract and conclusion.

- **Accuracy gaps remain large on harder datasets.** On CIFAR-100 (ResNet-18: QAT 65.82% vs Ours 56.83%, ~9% drop) and Cars (50.81% vs 37.88%, ~13% drop), the degradation is substantial. The paper's headline "approximately 6%" average masks significant variability. The practical utility on such datasets is unclear, and the paper would benefit from more specific guidance about where the method is viable vs. not.

### Minor

- **The "1-bit" framing is technically an average of 1-bit, not uniform 1-bit.** The method retains groups at b-bit precision (b=4 optimal) while pruning others, achieving an *average* of 1-bit per element. The paper is transparent about this in the technical section (Section 5.2: "maintaining an average bitwidth of 1") and Table 5, but the title, abstract, and early discussion use "1-bit FQT" without qualification. This should be clarified upfront to avoid misleading readers about the compute characteristics.

- **Theoretical analysis assumes convex loss functions (Assumption from Zinkevich, 2003).** The regret bounds do not directly apply to the non-convex deep networks used in experiments. This is standard practice in the optimization literature for providing intuition, but the paper does not acknowledge this gap or provide heuristic justification (e.g., local convexity near minima). Bridging this gap would substantially strengthen the theory.

- **The variance reduction analysis conflates two sources of improvement.** Equation (24) shows variance proportional to \(\frac{1}{B^2}\) (where B=2^b-1) times \(\sum_{i=1}^{N/b}\) instead of \(\sum_{i=1}^N\). For b=4, B=15, so B²=225 — the bitwidth increase of retained groups contributes far more to variance reduction than the pruning factor (N→N/b). The paper's narrative emphasizes pruning, but the dominant factor is the increased quantization resolution of retained groups. This should be made explicit.

- **No comparison against 4-bit PSQ (the current FQT frontier).** The paper compares against 8-bit PSQ (for speed) and 1-bit PSQ (for accuracy), but it would be informative to see how much accuracy is sacrificed relative to 4-bit PSQ — the previous state of the art — in a fair comparison.

### Trivial
- The derivation of the \(ND^{(l)}\) factor in Eq. (17) could benefit from a brief explanation (it follows from summing variances across all N×D^(l) elements, each with SR variance ≤ 1/4).

## Nice-to-Haves
- Characterize *when* 1-bit FQT works beyond post-hoc variance analysis — e.g., do easier datasets have fewer gradient outliers, smaller output classes, etc.? This would turn the observation into a predictive guide.
- Statistical significance testing would strengthen the comparison between variants (e.g., b=2 vs b=4), though the three-run means with stddevs are adequate.
- The speedup comparison against 8-bit PSQ (32–45×) is expected since the primary driver is bitwidth difference; this is fine as a demonstration of the benefit of lower precision but should not be oversold as an algorithm-specific advantage.

## Removed Points

**These points are flagged to be removed, treat them with caution:**
- Critique that "the variance bound... specific factor ND^(l) is not derived in the text" — The derivation follows directly from summing per-element SR variance (≤1/4) over N×D^(l) elements and is clear to a reader familiar with basic probability.
- Critique that "the regret bounds are presented without comparing their tightness" — The bounds serve their purpose as scaling-law comparisons (O(σ²) vs O(σ)), which is the paper's goal. Tightness analysis is not necessary for the point being made.
- "The huge speedup ratio is primarily due to the difference in bitwidth, not the specific algorithm" — This is the entire point of pushing to 1-bit. The comparison is valid and informative; it demonstrates the practical benefit of achieving 1-bit FQT.
- "The paper does not conduct significance tests" — Three runs with stddevs is standard practice for this type of work; requesting significance tests for a small number of runs is not standard.
- Strength Finder's claim about "Systematic ablation of the hyperparameter b" — While this is genuine evaluation, calling it an "ablation" is somewhat misleading since it does not ablate the method's components. It is simply a sensitivity study of b.
- Various generic strengths from the Strength Finder ("important problem," "well-written") — These are superficial and carry no weight.

## Novel Insights

The most interesting observation from the reviews is that the variance reduction in AGP is dominated by the increased bitwidth of retained groups (B² = 225 for b=4) rather than the pruning itself (factor of N/b). This suggests that a simpler scheme — keeping all groups but at somewhat higher precision — might achieve similar variance reduction. The paper does not explore this, which would be a natural follow-up. Combined with the finding that performance degrades at b=8 (too much information lost by pruning), this reveals a nuanced trade-off where pruning aggressively enough to fund higher bitwidths is only beneficial up to a point, beyond which information loss dominates over variance reduction.

## Suggestions
1. **Add ablation experiments separating AGP and SCQ** — compare: (a) 1-bit PSQ baseline, (b) PSQ + AGP only, (c) PSQ + SCQ only, (d) full method. Report both accuracy and speedup for each.
2. **Clarify the "average 1-bit" framing** — qualify "1-bit FQT" as "average 1-bit FQT" or "~1-bit FQT" in the title and abstract, stating upfront that uniform 1-bit is not achieved.
3. **Add a 4-bit PSQ accuracy comparison** to calibrate how much is sacrificed relative to the prior frontier.
4. **Acknowledge the convexity limitation** more explicitly in the theory section and discuss how the insights might (or might not) generalize to non-convex settings.
5. **Report per-dataset accuracy drops from QAT** in the abstract and conclusion rather than only the average, to avoid masking variability.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Comparison |
|------|-----------|-----------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/wg1PCg3CUP.md` (Scaling Laws for Precision) | 8.00 | Broader scope, more thorough experiments, broader implications. Current paper is narrower (transfer learning only) and less thorough. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/wJv4AIt4sK.md` (Effective Interplay...) | 7.50 | Stronger theoretical contribution, validated across more model scales. Current paper has weaker (convex) theory. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/LzPWWPAdY4.md` (LoftQ) | 7.33 | Clear practical contribution with stronger experiments. Current paper explores a harder problem but with less complete evaluation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TJo6aQb7mK.md` (Ternary Language Model) | 7.60 | More substantial empirical scale. Current paper is smaller in scale. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/oOwDQl8haC.md` (Lower Bit-Width Accumulators) | 5.75 | Similar score band — useful contribution with clear limitations. Current paper is comparably strong. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Dm4qrBuFKH.md` (Binary Neural Networks in Binary Weight Space) | 4.67 | Insufficient experiments, weak results. Current paper has stronger evidence. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/wJ3GeGLFmc.md` (Sub-8-Bit Integer Training) | 4.50 | Similar topic (low-bit training), rejected partly for unclear contribution and limited novelty. Current paper is more novel (pushing to 1-bit) and has clearer contribution. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TDzAqTqDHV.md` (QCR) | 3.00 | Unconvincing experiments, weak baselines. Current paper is clearly stronger. |

Relative to these anchors, the paper is stronger than the 4.5–4.7 range papers (more novel problem, clearer contribution, better experiments) but falls short of the 7.5+ range papers (more limited scope, weaker theory, missing ablation). It fits naturally alongside papers in the 5.5–6.5 range — a genuine contribution with acknowledged limitations.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>