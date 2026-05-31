## Summary

ACSP (Automatic Complementary Separation Pruning) is a structured, activation-based pruning method for CNNs that aims to automate the pruning-ratio decision. For each layer, ACSP constructs a "graph space" where each component (neuron/channel) is embedded via its Jeffries-Matusita (JM) pairwise separability scores across all class pairs. k-Medoids clustering groups components with similar separability; the Mean Simplified Silhouette (MSS) index scores each cluster count k; and the Kneedle algorithm identifies a "knee" to pick the optimal k automatically. Within each cluster, the highest-weight component is retained. Experiments on VGG, ResNet, DenseNet, and MobileNet-V2 across CIFAR-10/100 and ImageNet-1K report competitive accuracy–efficiency tradeoffs.

---

## Strengths

- **Automatic pruning-extent determination** is a genuine and practically useful contribution. Most structured pruning methods require a user-specified compression ratio; ACSP's knee-finding on the MSS curve removes this requirement in a principled, data-driven way.

- **Complementary-diversity principle is well-motivated.** Using k-Medoids to enforce coverage of the separability space (rather than simply keeping high-magnitude filters) is a conceptually sound deviation from standard magnitude-only pruning, and the visualization in Figure 2 makes the intuition clear.

- **Broad empirical coverage.** Results span four architecture families, three datasets at different scales, and include both FLOPs reduction (Table 1) and real wall-clock latency measurements (Table 2). The method consistently achieves competitive or leading tradeoffs.

- **Metric flexibility is acknowledged.** The paper documents that JM distance was selected after comparing Hellinger and Wasserstein alternatives, providing at least partial empirical grounding for that design choice.

---

## Weaknesses

### Fatal
None.

### Major

1. **Unexplained scalability to ImageNet.** The separation matrix for layer $L_i$ has dimensions $N_i \times (p^2 \times \binom{C}{2})$. For ImageNet ($C=1000$), $\binom{C}{2}=499{,}500$ class pairs. For a conv layer with spatial dimension $p=14$ and $N=256$ channels (typical in ResNet-50), this is $256 \times 196 \times 499{,}500 \approx 25\times10^9$ entries. Even at float16, storing this matrix requires ~50 GB per layer—clearly infeasible. For $p=28$ layers, the situation is far worse. The paper explicitly flags class-pair sampling and dimensionality reduction as *future work*, yet presents ImageNet-1K results without explaining what approximation or reduction was actually used. This is a critical gap: readers cannot reproduce the ImageNet experiments as described, and it casts doubt on whether the method as stated was actually applied to ImageNet.

2. **Algorithm 1 is inconsistent with the methodology.** Line 12 reads "optimal\_components ← top-k' components by weight," which describes plain magnitude pruning (select the k' globally highest-weight components). Section 3.4.2, however, specifies selecting *the highest-weight component from each cluster*, which is a fundamentally different operation that enforces diversity. These two rules produce identical results only when each cluster contains exactly one component. The pseudocode should be corrected, and both selection strategies should be ablated.

3. **No ablation of key design choices.** The method stacks several non-trivial decisions—MSS vs. standard Silhouette, knee-finding vs. fixed ratio, weight-based intra-cluster selection vs. medoid selection, JM distance vs. alternatives, and layer-by-layer sequential pruning. No ablation disentangles their contributions. Given that the baseline (top-k by magnitude within each cluster) is itself a reasonable pruning strategy, the paper cannot attribute its empirical gains specifically to the complementarity principle.

4. **Wall-clock speedup is much smaller than the FLOP reduction.** Table 1 claims $2.25\times$ FLOPs on ResNet-50; Table 2 shows 6–8% latency reduction. For VGG-16 (CIFAR-10), a claimed $2.59\times$ FLOP reduction yields only 7–11% latency reduction. The paper acknowledges this gap in one sentence but does not analyze root causes (e.g., memory-bandwidth bottlenecks, residual connections, batch-norm overhead). This means the central claim—"significantly reduces … FLOPs … and results in faster inference time"—is only partially borne out in practice.

### Minor

- The Bhattacharyya distance formula (Eq. 2) assumes Gaussian-distributed activations; this assumption is not stated or justified. Post-ReLU activations are clearly non-Gaussian, and this could affect JM score reliability.
- For ImageNet MobileNet-V2, SANP achieves a +0.14% accuracy gain vs. ACSP's +0.09%, with ACSP's advantage being only a 0.14× larger speedup. The claimed superiority here is marginal and likely within measurement noise.
- The fine-tuning protocol (2 epochs on 25% of data) is very lightweight, but the paper never compares against longer fine-tuning to verify this is not leaving accuracy on the table.

### Trivial

- In Table 1, the ACSP row for CIFAR-10/MobileNet-V2 incorrectly shows the citation "(Gao et al., 2023)" in the Method column, copying SANP's attribution.

---

## Nice-to-Haves

- A clear description of how the separation matrix is actually constructed for ImageNet experiments (whether subsampled class pairs, spatial pooling, or other reduction strategy).
- Reporting total pruning time (including forward passes and k-Medoids sweeps per layer) compared to baseline methods, to establish practical usability.
- An ablation replacing the full ACSP pipeline with a simple per-layer magnitude pruning combined with the same automatic knee-finding, to isolate the value of the separability-based clustering.

---

## Novel Insights

The use of the JM-distance-based class separability space as a proxy for component diversity—embedding each filter as a vector of pairwise discriminabilities rather than as a scalar importance score—is a fresh angle on structured pruning that genuinely differs from prior spectral, magnitude, and gradient-based approaches. Combining this with a cluster-coverage objective (MSS + Kneedle) produces an end-to-end automated pipeline without a user-defined ratio. That said, the ultimate selection rule (highest-L1-norm per cluster) largely reduces to magnitude pruning within local separability neighborhoods, narrowing the gap with simpler baselines and raising the question of how much diversity enforcement actually contributes beyond automatic ratio selection alone.

---

## Suggestions

- Provide a concrete description of how the separation matrix is tractably computed for ImageNet (e.g., spatial global-average-pooling, class-pair subsampling), and quantify the approximation error introduced.
- Fix Algorithm 1 line 12 to match the intra-cluster weight-based selection described in Section 3.4.2.
- Add a minimal three-way ablation: (a) standard magnitude pruning + manual ratio, (b) ACSP clustering + manual ratio, (c) full ACSP including automatic ratio. This isolates the contribution of each ingredient.
- Analyze or profile where the FLOP–latency discrepancy originates (e.g., show which layers are bottlenecked by memory bandwidth vs. compute), to set realistic expectations for practitioners.

---

## Score and Decision

ACSP proposes a genuinely useful automated pruning-ratio mechanism and an interesting separability-based diversity criterion. However, the paper's treatment of scalability to ImageNet is a critical omission: the method as written is computationally infeasible for 1000 classes without approximations that are deferred to future work, yet ImageNet results are presented. Combined with the inconsistency between Algorithm 1 and the text, the absence of ablations for key design choices, and the large gap between claimed FLOP reduction and actual latency improvement, the paper requires significant revision before it can be confidently accepted.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>