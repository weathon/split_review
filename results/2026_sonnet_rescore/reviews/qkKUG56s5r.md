## Summary

ACSP (Automatic Complementary Separation Pruning) is a structured, activation-based CNN pruning method that builds a graph space encoding each component's class-pair separability (via Jeffries-Matusita distance), clusters components with k-Medoids scored by the Mean Simplified Silhouette (MSS) index, applies the Kneedle algorithm to identify the automatic knee point in the MSS curve (eliminating user-specified pruning ratios), and then retains the highest-weight component from each cluster. Results are reported across VGG-16/19, ResNet-56/50, DenseNet-40, and MobileNet-V2 on CIFAR-10, CIFAR-100, and ImageNet-1K.

---

## Strengths

- **Fully automated pruning volume selection.** The use of Kneedle on the MSS curve (Section 3.4.1, Algorithm 1 line 11) removes all manual pruning-ratio tuning. The experiments deliberately report only speed-up factors, not user-specified targets, substantiating the automation claim.
- **Competitive accuracy across diverse architectures.** ACSP matches or exceeds baselines in ΔAccuracy on most benchmarks in Table 1 (e.g., VGG-19 CIFAR-100: +0.62%, ResNet-50 ImageNet: tying CCP at 76.98% while achieving higher FLOP reduction). This breadth of results strengthens the generality claim.
- **Inclusion of actual latency measurements.** Table 2 provides real wall-clock latency numbers (batch and single inference, averaged over 100 runs), which is more honest than purely reporting FLOPs, even if those numbers reveal a gap discussed below.
- **Lightweight fine-tuning regime.** Section 4.1 specifies 2–3 fine-tuning epochs on a 25% data subset per layer, a practical and reproducible choice.

---

## Weaknesses

### Fatal

None.

---

### Major

**1. The core contribution (graph-space complementary selection) is never ablated against a simpler automatic baseline.**

Algorithm 1 line 12 and Section 3.4.2 explicitly state that the final component selection picks "the component with the largest weight from each cluster," not the cluster medoid. The entire graph-space construction—JM distances, the N_i × (p × p × C(C-1)/2) separability matrix, k-Medoids traversal—serves only to partition components into diversity-inducing clusters; the actual component chosen from each cluster is determined by L1 weight norm. The obvious ablation—automatic k selection via Kneedle on some simpler MSS surrogate, followed by top-k weight-magnitude selection with no graph-space clustering—is entirely absent. The paper does compare JM vs. Hellinger vs. Wasserstein distances (Section 3.3.1), but this is a sensitivity sweep within the same framework, not an ablation of the framework's necessity. Without this comparison, the expensive graph-space step has no demonstrated marginal contribution to the final accuracy or speed-up numbers.

**2. Computational feasibility of the ImageNet-1K experiments is unresolved.**

Section 3.1 and Figure 1 define the separation matrix as N_i × (p × p × C(C-1)/2). For ImageNet (C = 1000), C(C-1)/2 = 499,500. For a ResNet-50 layer with N_i = 2048 and spatial resolution p = 7, the separation matrix has 2048 × (49 × 499,500) ≈ 50 billion entries—roughly 200 GB in float32 for a single layer. Running k-Medoids from k=2 to k=N_i on this matrix is not merely costly; it requires intermediate representations infeasible on any standard GPU cluster. The paper's own conclusion acknowledges "building the separation graph requires comparing all class pairs, so cost scales with classes C and may bottleneck for large C," and defers all solutions to "future work." But the ImageNet-1K results are already in Table 1. If class-pair sampling or dimensionality reduction was applied, it is part of the method as actually run and must be described. As written, the ImageNet experiments are not reproducible—the reader has no mechanism to replicate the exact procedure that generated Table 1's ResNet-50 or MobileNet-V2 rows.

**3. The headline efficiency claim is substantially overstated by the FLOP metric.**

The abstract promises "faster inference time" and the introduction uses hardware-friendly speedups to motivate structured pruning. Table 1 reports FLOP-based speedups of 1.5–2.59×. Table 2 reports actual measured latency reductions of 2.62%–20.39% (batch) and 2.62%–8.07% (single inference). For ResNet-56 on CIFAR-10, the 2.15× FLOP speedup yields only –2.95% single-inference improvement—roughly a 10× discrepancy between the headline claim and the measured result. All competitor comparisons in Table 1 are FLOP-based; no baseline wall-clock latency is provided. If ACSP's FLOP reductions translate less efficiently to hardware than competitors', the advantage shown in Table 1 may not hold in wall-clock terms. Section 4.5 notes "hardware utilization is not perfectly linear with FLOP count" but provides no analysis of whether this non-linearity affects ACSP differently than it would affect the baselines.

---

### Minor

**1. The "N_i ≤ 256" runtime bound in Section 3.2 is incorrect for ResNet-50.**

Section 3.2 states: "with N_i ≤ 256 the wall-clock cost is below 0.1 s on an RTX 6000." ResNet-50 has convolutional layers with N_i up to 2048. The bound is factually wrong for the exact architectures the paper tests on, and the runtime estimate therefore does not apply to those experiments.

**2. Arithmetic error in Table 1 for ResNet-50 ΔAccuracy.**

Table 1 reports ACSP base accuracy 76.32%, pruned accuracy 76.98%, ΔAccuracy = +0.59. The correct difference is 76.98 − 76.32 = 0.66, which Section 4.4 correctly states as "+0.66%." The table entry is arithmetically wrong, though the text gives the correct value.

---

### Trivial

None beyond what is categorized above.

---

## Nice-to-Haves

- The paper would benefit from reporting baseline latency (Table 2-style) for at least two or three competitors, to verify whether ACSP's wall-clock improvement is genuinely superior to what baselines achieve at comparable FLOP ratios.
- Figure 2 shows a 2D projection of the graph space and marks medoids vs. highest-weight components, but does not quantify how often these differ or what the accuracy delta is when medoids are used instead of highest-weight components. A small table or curve would directly visualize the justification for weight-based override.
- Adding standard deviation or confidence intervals across multiple pruning runs (Kneedle and k-Medoids are both sensitive to initialization) would allow readers to assess whether small ΔAccuracy margins (e.g., +0.13% vs. +0.24% for ResNet-56) are meaningful.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"ACSP (Gao et al., 2023)" citation label in Table 1 (MobileNet-V2 CIFAR-10).** The harsh critic identifies this as a formatting error that conflates ACSP's result with a baseline citation. This is a parser/formatting artifact per the review guidelines and should not be held against the authors.
- **Varying base accuracy across compared methods making ΔAccuracy incomparable.** The critic notes that, e.g., ResNet-56 baselines range from 92.80% (AMC) to 93.71% (ResRep). This is a real but generic concern with structured-pruning comparison tables industry-wide; it does not specifically disadvantage ACSP versus any one baseline, and the authors did not choose competitors' base models. Removing as scope creep.
- **"Consistent improvements" wording overstating the 2.62%–20.39% range.** The harsh critic flags Section 4.5's use of "consistent." While the word choice is loose, this is a presentation nitpick rather than a substantive flaw.
- **Strength: "broad empirical validation demonstrates generality and scalability."** This was flagged by the Strength Finder as a general strength. Kept only in weakened form—the breadth of results is genuine, but the scalability claim for large-C datasets is directly undermined by Major Weakness 2 above.

---

## Novel Insights

The combination of MSS-scored k-Medoids traversal with Kneedle knee-finding as a fully automatic pruning ratio selector is a technically elegant solution to the manual-tuning problem; it operates without any validation-set accuracy feedback. The insight that diversity-in-graph-space can be separated from importance-in-weight-space—and that these two signals can be combined (cluster via graph, select via weight) rather than conflated—is a genuine conceptual contribution, even though it currently lacks the ablation needed to confirm that both signals are necessary.

---

## Suggestions

1. **Provide an explicit description of how the separation graph was computed for ImageNet-1K.** If class-pair sampling or PCA-based dimensionality reduction was used, add it to Section 3.3.1 or an appendix subsection. This is not optional for reproducibility.
2. **Add a direct ablation:** run the full pipeline but replace the graph-space cluster partitioning with random assignment of components to k' equal-sized bins, then select the highest-weight component from each bin. If graph-space clustering outperforms this, the contribution is demonstrated; if not, the method reduces to automatic-k weight-magnitude pruning and the paper should reframe accordingly.
3. **Fix the N_i ≤ 256 runtime claim** to reflect the actual maximum layer widths in the tested architectures, and provide runtime breakdowns or estimates for layers with N_i = 512, 1024, 2048.
4. **Correct the ΔAccuracy entry for ResNet-50** in Table 1 from +0.59 to +0.66.
5. **Report latency for at least 2–3 baselines** using the same timing setup (RTX 6000, 100 runs, same batch sizes) so that the inference efficiency comparison is not FLOP-only.

---

## Score and Decision

**Originality:** The graph-space complementary selection with MSS-based automatic k is novel; the final weight-override step partially undermines originality by reducing the selection to a known criterion. (3/5)
**Importance:** Automated structured pruning for edge deployment is an important practical problem. (4/5)
**Claims supported:** The automation claim is well-supported; the inference-acceleration claim is overstated given the FLOP-vs-latency gap; the feasibility for ImageNet is unresolved. (2/5)
**Soundness:** Missing the critical ablation and the ImageNet feasibility explanation weaken the experimental soundness significantly. (2/5)
**Clarity:** Writing is generally clear; the algorithm description is well-organized. (3/5)
**Community value:** The complementary-selection framing and MSS application are of interest; the gaps reduce immediate impact. (3/5)

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>