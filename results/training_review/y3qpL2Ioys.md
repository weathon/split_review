Here is the consolidated review.

---

## Summary

This paper proposes a hierarchical generative framework for neural architecture search that can navigate an extremely large search space (~10³⁹⁰ designs) without relying on a hand-crafted initial subspace. The approach comprises three levels: (1) a G-VAE with zero-cost (ZC) proxy clustering and Gaussian mixture modeling to organize micro cell designs into families; (2) a Conditional Continuous Normalizing Flow (CCNF) to generate "synonymous" high-performing cell designs given a reference; and (3) a decoder-only transformer (fine-tuned GPT-Neo) trained on evolutionary search history to produce macro architectures under user-defined constraints (FLOPs/parameters). The method achieves strong performance on CIFAR-10/100, ImageNet-1k (78.3% top-1 at ≤450M FLOPs), and NAS-Bench-360.

## Strengths

- **Principled hierarchical factorization of an enormous search space.** The paper quantifies a reduction from ~10³⁹⁰ to ~10⁷⁸ designs by abstracting micro-cell details into cluster-level decisions (Sec. 3.3). This is a novel and technically sound approach to scaling NAS beyond hand-crafted search spaces without making search intractable.

- **Novel use of ZC proxy vectors for relative clustering rather than absolute ranking.** Instead of using ZC proxies to order models (known to be unreliable), the method computes a 4-dimensional ZC vector and clusters designs by L1 distance in this space (Sec. 3.1). The t-SNE visualization (Fig. 2b–c) confirms that triplet-regularized G-VAE preserves this ZC structure, and the ablation (HL-Evo outperforming Evo(T-CET) on the same GraphNet space) demonstrates that this organization provides practical search benefits.

- **CCNF-based synonym generation demonstrably improves over naive latent-space sampling.** Table 1 shows that sampling via the trained CCNF yields ~1 percentage point higher average accuracy, a better best-case design, and narrower variance compared to simple neighbourhood sampling in the G-VAE latent space, using the same reference cell.

- **Competitive performance at low search cost.** On ImageNet-1k (≤450M FLOPs), the method achieves 78.3% top-1 accuracy with 30 GPU hours of one-time pretraining and minutes for generation (Table 3). This is competitive with or exceeds other low-cost NAS methods (DDS, ZiCo, T-CET) and is within 0.2% of GPT-NAS at 33× less compute.

- **Ablation study isolates each component's contribution.** Table 2 progressively adds G-VAE+CCNF (HL-Evo) and then the trained SG, showing consistent improvement over naive evolution in the same large search space (e.g., +0.8% on CIFAR-10 over Evo(T-CET) run on GraphNet), providing clear evidence that each hierarchical element adds value.

## Weaknesses

### Fatal
None.

### Major

- **The foundational assumption that ZC-similarity clusters correspond to similar true performance is unvalidated.** The entire clustering pipeline (GMM partitioning, CCNF cell generation from cluster centers, HL search space factorization) rests on the claim that "we only use it to cluster designs that are likely to train to similar performance" (Sec. 3.1, lines 65–66). Figure 2 validates that the G-VAE preserves ZC distances, but the critical link — showing that architectures in the same ZC cluster have low within-cluster variance in *trained accuracy* — is never established. Without this, the clustering step and the synonym-generation framing lack direct empirical grounding. The paper acknowledges this as a limitation (Sec. 5), but a controlled experiment sampling architectures from a few clusters and training them to convergence would substantially strengthen the core claim. This is a gap, not a fatal flaw, because the overall benchmark results provide indirect validation, but it is the most significant missing piece of evidence.

### Minor

- **Cost comparison in Table 2 and Table 3 presents an asymmetric picture.** The "Cost" column reports 0.1 GPU hours for "Ours," reflecting only the final selection step. The 30 GPU hours of one-time pretraining (G-VAE, CCNF, ES for SG) are disclosed in a separate paragraph (line 155) and legitimately amortized across tasks, but they are not incorporated into the tables where readers naturally compare costs. The baselines' reported costs (2–3 GPU hours) appear to cover their entire search. The paper would benefit from a more transparent total-cost table or a clear breakdown for all methods. The separate "Hidden cost" paragraph on GPT pretraining (lines 157–158) is a fair disclosure and not a weakness.

- **CCNF validation (Table 1) uses a single reference design and one dataset.** The comparison of CCNF vs. neighbourhood sampling uses only the best cell from NATSBench-TSS as a reference and only CIFAR-10. While this is sufficient as a proof-of-concept for the design choice, it does not demonstrate general utility across clusters, tasks, or reference designs.

- **Baseline comparison in Table 2 mixes different search spaces.** ZenNAS, ZiCo, and T-CET are run on ZenNet (a smaller, hand-crafted space), while the authors' method runs on GraphNet (a larger superset). The paper explicitly acknowledges this ("we attribute this simply to the fact that our search space is much larger") and provides a controlled comparison (Evo(T-CET) on GraphNet, where HL-Evo and Ours both outperform it). However, the headline improvements over the ZenNet methods are not directly attributable to the generative approach alone — they partly reflect the larger search space. The controlled comparison on GraphNet is what actually supports the method's claims.

- **No variance or confidence intervals for CIFAR results in Table 2.** The paper reports averaging over 3 runs for ImageNet (Table 3) but not for CIFAR-10/100. Given that many improvements are small (e.g., 97.35% vs. 97.30%), it is unclear whether these differences are statistically significant.

- **The SG training and final selection both use T-CET.** The SG is trained on evolutionary search history that optimizes T-CET, and the final model selection also uses T-CET (Sec. 3.3, line 146). This introduces a degree of circularity. The ablation helps (HL-Evo uses the same T-CET metric and still outperforms Evo(T-CET) on GraphNet), but the paper does not validate that the generated architectures generalize beyond the selection metric — e.g., by comparing T-CET-based selection against final trained accuracy-based selection.

### Trivial
- Minor notation inconsistency in Eq. 5 (the VAE loss formulation double-uses overbraces in a slightly confusing way).

## Nice-to-Haves

- **Within-cluster accuracy variance study:** Sampling 5–10 architectures from 3–5 clusters, training them to convergence on CIFAR-10, and reporting within-cluster vs. between-cluster accuracy variance would directly validate the core ZC-clustering assumption.
- **Ablation on the number of clusters K:** The paper uses BIC/AIC to pick K but never shows how sensitive results are to this choice (e.g., K ranging from 10 to 200).
- **Random sampling baseline from GraphNet:** A simple sanity check — randomly selecting clusters and cells from the GraphNet space and training the top performers — would clarify how much the generative models contribute vs. the raw space size.
- **Pareto-frontier plots for ImageNet** (accuracy vs. FLOPs) comparing Ours to baselines, to contextualize the magnitude of improvements.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Cost comparison is misleading because it omits 910 GPU hours of GPT pretraining"** — The paper explicitly discusses this as a "Hidden cost" (lines 157–158), notes that pretrained GPTs are widely available, and distinguishes this from NAS-specific costs. The criticism is already addressed by the paper.
- **"Parameter count and FLOPs are not zero-cost in the usual sense"** — The paper defines its ZC vector as including these; they are deterministic architectural properties that cost nothing to compute. This is a definitional quibble, not a substantive weakness.
- **"The micro space is still hand-crafted (6 nodes, 28 ops)"** — The paper's goal is to *reduce* dependence on hand-crafted spaces, not eliminate all design choices. The space size (~10¹⁷) far exceeds typical NAS spaces, and the paper explicitly acknowledges this in its limitations.
- **"The method for obtaining reference designs for downstream tasks is unclear"** — The paper explicitly states (line 122–124) that cluster centers (μᵢ) are used as references for new tasks.
- **"Missing related works"** — I cannot verify the existence of missing works without external sources.
- **Various formatting/style nitpicks** — These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel perspective not already articulated in the paper.

## Suggestions

1. **Add a direct validation of the ZC-cluster-to-accuracy correspondence.** Sample architectures from several clusters, train them to convergence, and report within-cluster vs. between-cluster accuracy variance. This is the single most important experiment to strengthen the paper's core claim.
2. **Provide a total-cost table** that includes one-time pretraining alongside per-task search cost, and add a column showing amortized cost over N tasks. This would resolve the cost-transparency concern.
3. **Report variance or confidence intervals for all main results** (CIFAR as well as ImageNet), especially where improvements are small.
4. **Validate the T-CET-based pipeline against final trained accuracy** for at least one setting, to confirm the method is not overfitting to the proxy.
5. **Add a random sampling baseline from GraphNet** — if the method's gains come from the generative models, they should outperform simply randomly sampling from the same large space and selecting by T-CET.

## Score and Decision

The paper presents a novel, well-motivated hierarchical generative framework for NAS with a clever use of ZC proxies for clustering rather than ranking. The experimental evaluation demonstrates competitive performance on standard benchmarks and includes useful ablations. The main gap is the unvalidated link between ZC-cluster membership and true performance similarity — a significant but not fatal omission, as the overall results provide indirect support. The remaining issues (cost presentation, limited CCNF validation, partial search-space misalignment) are addressable. The core contribution is sufficiently novel and the experiments sufficiently supportive to warrant acceptance with the expectation that the authors address the ZC validation gap.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>