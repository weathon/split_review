Now I have all the information I need. Let me compile the final consolidated review by carefully cross-referencing each claim against the paper.

**Verified facts from the paper:**

1. **Line 117**: "The tree system produced by this construction has a chain-like tree structure" — the paper **does** acknowledge the chain structure.
2. **Line 230**: "The splitting maps α will be selected either as a trainable constant vector or a random vector" — no ablation of α is presented.
3. **Lines 247-249**: "Over 2500 timesteps, we evaluate the Wasserstein distance between source and target distributions" — "Wasserstein distance" is the generic name; the paper does not specify whether this is the true Wasserstein-2 or each method's own metric.
4. **Line 263**: "We report the Wasserstein distances at the final time step along with the corresponding transferred images from various baselines Figure 5" — quantitative results ARE reported for color transfer.
5. **Lines 269-270, 277-279**: GAN experiments use FID/IS (independent metrics); diffusion experiments use FID.
6. **Line 230**: The paper explicitly states "focusing mainly on comparing TSW-SL with the original SW, without expecting TSW-SL to outperform more recent SW variant."

---

## Summary

This paper proposes Tree-Sliced Wasserstein distance on Systems of Lines (TSW-SL), which generalizes Sliced Wasserstein (SW) by replacing one-dimensional projection lines with tree-structured systems of lines. The authors define tree systems as connected collections of lines with a tree metric, develop a Radon transform on systems of lines, prove its injectivity, and derive a closed-form Wasserstein computation at SW-equivalent cost. Experiments on gradient flows, color transfer, GANs, and denoising diffusion models show consistent improvements over standard SW.

## Strengths

- **Novel theoretical framework generalizing SW to tree-structured domains.** The paper formally defines tree systems (connected systems of lines with tree metrics — Theorem 3.2), introduces a Radon transform on systems of lines (Definition 4.1), and proves its injectivity (Theorem 4.2). This provides a principled generalization of the one-dimensional line in SW to richer geometric structures while preserving closed-form OT computation via the tree-metric Wasserstein formula (Equation 12).

- **Closed-form Wasserstein computation at SW-equivalent cost.** The paper derives a closed-form expression for the Wasserstein distance on tree systems and shows the time complexity is O(L k n log n + L k d n), matching SW when using the same total number of projection directions (Remark after Equation 12). This is a concrete advantage over methods that sacrifice closed-form tractability.

- **Consistent empirical outperformance in generative settings with independent metrics.** TSW-SL achieves substantially better FID/IS scores in GANs (Table 3: CelebA FID 12.84 vs. 17.97 for SW with 500 directions) and improves FID in denoising diffusion (Table 4: CIFAR-10 FID 9.23 vs. 12.66 for SW). These improvements are measured with standard independent metrics (FID, IS), not the proposed distance itself, providing credible evidence of practical value.

- **Theoretical properties: injectivity and reduction to SW.** Theorem 4.2 proves the Radon transform on systems of lines is injective for any splitting map — a fundamental property ensuring TSW-SL is a valid metric (Theorem 5.2). The framework reduces to standard SW when k=1 (Remark after Theorem 5.2), showing it is a natural generalization.

## Weaknesses

### Fatal
None.

### Major

- **No ablation of the splitting map α.** The splitting map α ∈ C(R^d, Δ_{k-1}) determines how mass at each point is distributed across the k lines. In practice, α is either a trainable constant vector or a random vector (Section 6, first paragraph). This introduces a degree of freedom absent from SW baselines. Since no experiment compares TSW-SL with a fixed uniform α against TSW-SL with a learned α, the contribution of the tree structure per se is not disentangled from the tuning of α. The empirical improvements could partly stem from this additional flexibility rather than from the tree geometry. An ablation controlling for α is needed to attribute gains to the tree structure.

- **Uncertainty estimates are missing across all experiments.** Tables 1–2 report averages over 10 runs but no standard deviations. Table 3 reports averages over 3 runs but no standard deviations. Given the known variance of GAN and diffusion training, this omission makes it difficult to assess whether the reported improvements are statistically significant.

### Minor

- **Gap between the general theoretical framework and the restricted practical construction.** The paper's theory (Sections 3–5) discusses general tree systems with arbitrary topologies, but Algorithm 1 generates only chain-like tree systems (line 117: "chain-like tree structure"). While the paper acknowledges this explicitly, it does not discuss whether the metric property (Theorem 5.2) — which depends on the distribution σ over tree systems — is guaranteed to hold for this restricted class. The injectivity of the Radon transform (Theorem 4.2) concerns the operator over ALL systems of lines (L_k^d), but the metric claim for TSW-SL depends on whether the sampled space T (chain systems only) has sufficient support to separate measures. The paper should either (i) prove that chain systems suffice for the metric property, (ii) provide a more general sampling algorithm, or (iii) qualify the metric claim for the implemented subclass.

- **Ambiguity about the evaluation metric in gradient flow experiments.** Tables 1–2 report "Average Wasserstein distance" but do not specify whether this is the true Euclidean Wasserstein-2 distance (an independent evaluation metric) or each method's own loss. If each method is evaluated on its own loss, the comparison is circular — each method would naturally achieve the lowest value on its own metric. Given standard practice, it is likely the true W_2 is reported, but the paper should clarify this explicitly.

- **No wall-clock runtime comparison.** The paper claims equivalent complexity to SW but does not report actual wall-clock times. Given the additional steps (mass splitting, tree-metric summation), a practical runtime comparison would confirm that the theoretical complexity bound translates to practice.

### Trivial
- The paper uses "Wasserstein distance" generically without specifying the exponent (p=1 or p=2) in the gradient flow evaluation, which would help reproducibility.

## Nice-to-Haves

- **Ablation with uniform α.** Fix α(x)_l = 1/k for all x and repeat the main experiments to isolate the effect of the tree structure from the effect of the learnable α.
- **Comparison against tree Wasserstein on a single fixed tree.** This would isolate whether the benefit comes from using multiple tree systems versus the tree structure itself.
- **Sensitivity analysis for k** (number of lines per tree system). The experiments use k=4 or k=5 without justification; a sweep over different k values would illuminate the role of tree system size.
- **Proving injectivity or metric property for chain-like tree systems specifically**, if not already done in the deferred appendix.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The paper never acknowledges this gap [chain vs. tree]."** — Removed. The paper explicitly states at line 117: "The tree system produced by this construction has a chain-like tree structure." The paper does acknowledge the limitation. The deeper concern about the metric property is preserved in Minor above.

2. **"The metric property is unlikely to hold for the restricted set of tree systems used in practice."** — Removed as stated. This is a speculative claim made without proof. The paper's proof is deferred to the appendix (Theorem B.1), which we cannot evaluate. The critic does not demonstrate that the claim is false. The legitimate concern about the theory-practice gap is preserved in Minor.

3. **"No quantitative metric [for color transfer]."** — Removed. The paper states at line 263: "We report the Wasserstein distances at the final time step." Quantitative results are reported, contradicting this criticism.

4. **"Gradient flow evaluation uses the loss value itself (circular)."** — Removed as stated. The paper says "evaluate the Wasserstein distance" (line 247) without specifying which Wasserstein distance, but standard practice in the SW literature is to evaluate the true Euclidean Wasserstein-2 as an independent metric. The ambiguity concern is preserved in Minor.

5. **"GAN comparison incomplete — missing MaxSW, SWGG, LCVSW baselines."** — Weakened to a Nice-to-Have. The paper explicitly scopes itself (line 230): "focusing mainly on comparing TSW-SL with the original SW, without expecting TSW-SL to outperform more recent SW variant." This is a defensible scope choice, not a methodological gap.

6. **"Diffusion baselines comparison is vague."** — Removed. The paper references "baselines in (Nguyen et al., 2024b)" which is standard citation practice.

7. Various formatting/style/strawman nitpicks from the critic's section-by-section notes that do not affect the core contribution.

## Novel Insights

The most interesting observation emerging from the reviews is that the theory-practice gap in this paper is the reverse of the usual direction: the theory is genuinely general (arbitrary tree topologies, arbitrary k lines), but the implemented sampling algorithm (Algorithm 1) only generates chain-like structures. This raises the question of whether the chain subclass is already sufficient for the metric property — a question the paper does not address but which, if answered affirmatively, would make the paper's contribution more impactful (because it would show that a very simple construction suffices for the full theoretical benefit). Conversely, if chain systems are insufficient, the paper needs a new algorithm. This tension, and the missing α ablation, are the paper's two most actionable improvement points.

## Suggestions

1. **Ablate the splitting map:** Run the main experiments with α fixed to uniform (1/k) and compare against the trainable/random α version. Report both in the same table.
2. **Clarify the evaluation metric in gradient flows:** State explicitly that the reported "Wasserstein distance" is the Euclidean Wasserstein-2 distance, computed independently of the loss.
3. **Add standard deviations** to all tables reporting averages over multiple runs (Tables 1–3).
4. **Discuss the chain limitation directly** in the main text (currently it is mentioned only in passing at line 117). Specifically, address whether the metric property (Theorem 5.2) is proven for T as defined (chain systems from Algorithm 1) or only for the unrestricted space L_k^d.
5. **Report wall-clock times** for TSW-SL vs. SW to verify the complexity claim empirically.

## Score and Decision

This paper makes a genuinely novel theoretical contribution — generalizing SW to tree-structured systems of lines with an injective Radon transform and closed-form computation — and provides empirical validation across multiple tasks. The GAN and diffusion results (using standard independent metrics FID/IS) are credible evidence of practical value. However, two issues prevent stronger confidence: (1) the splitting map α is not ablated, leaving the source of empirical gains unclear, and (2) the evaluation metric in gradient flows needs clarification to rule out circularity. The theory-practice gap (chain-only construction vs. general tree theory) is acknowledged but its implications for the metric property are not discussed. These are all addressable in revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>