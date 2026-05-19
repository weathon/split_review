Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper tackles Continual Test-Time Adaptation (CTTA) by proposing to *control the direction* of feature-space shifts rather than just suppressing their magnitude. The method (C-CoTTA) adapts Concept Activation Vectors (CAVs) from interpretable ML to represent domain-level and class-level shift directions from prototype differences, then applies two losses: Control Domain Shift (CDS), which reduces model sensitivity along the domain shift direction, and Control Class Shift (CCS), which prevents any class's shift direction from pointing toward other classes. Experiments on CIFAR10-C, CIFAR100-C, and ImageNet-C across standard, gradual, corruption-loop, and random-order scenarios claim state-of-the-art results.

## Strengths

- **Novel problem framing that challenges the dominant paradigm.** The paper explicitly argues that suppressing shift magnitude (the common approach in CTTA) is insufficient, and instead proposes *guiding the direction* of shifts to preserve class separability. This is clearly articulated (Section 1) and opens a new axis for CTTA research.

- **Principled adaptation of CAVs for online shift representation.** The paper derives domain-level and class-level shift directions via prototype differences (Eq. 1→2, Eq. 22, Eq. 20), adapting signal-pattern-based CAVs from interpretable ML to the unsupervised online CTTA setting. The derivation showing equivalence to a simple prototype-difference form (Eq. 2) is clean and well-motivated.

- **Two complementary loss components with ablation evidence.** CDS (Eq. 7) constrains model sensitivity along the overall domain shift direction, while CCS (Eq. 5) prevents class-specific shifts from pointing toward other classes. The ablation study (Table 4) shows that each component individually reduces error rates across all three benchmarks and their combination yields further gains.

- **Comprehensive evaluation across diverse scenarios.** Beyond standard CTTA, the method is tested on gradual adaptation, 10-cycle corruption loops, and random-order sequences. The corruption-loop results (Figure in appendix) show the error rate gap widening over cycles — strong evidence for long-term robustness.

- **Quantitative analysis supporting the proposed mechanism.** The inter-class distance analysis (Figure 5a) shows C-CoTTA maintains larger class separation, and the inter-domain distance analysis (Figure 5b) shows reduced sensitivity to domain shift. These directly back the claim that controlling shift directions is beneficial.

## Weaknesses

### Fatal
None.

### Major
- **Single-run results with no statistical significance.** The paper reports only single-run error rates on all benchmarks. CTTA involves randomness from pseudo-labels, data ordering, teacher model updates, and entropy-based sample selection. A single run cannot separate the method's contribution from random variation. This is especially concerning for small margins (e.g., 0.4% over SATA on CIFAR100-C). At least 3–5 runs with standard deviations are needed for the results to be credible as benchmark numbers. *Verified: the paper states "All experiments are conducted on a single RTX 4090" and mentions no multiple runs anywhere.*

- **O(c²) computational cost of CCS is unexamined.** Equation (5) sums over all C×(C−1) class pairs. For ImageNet-C (1000 classes), this is ~1M dot products per batch. The paper provides no approximation strategy, no sampling scheme, no wall-time comparison, and no discussion of whether this cost affects practical deployment or whether the reported results required any unstated optimization (e.g., only computing a subset of pairs). This is a structural gap for large-class datasets. *Verified: Eq. (5) shows the double sum over all class pairs; Algorithm 1 confirms per-batch computation; no discussion of cost or approximation appears anywhere in the paper.*

- **Hyperparameter values λ₁ and λ₂ not specified.** The overall loss (Eq. 9) uses λ₁ and λ₂ to weight CDS and CCS, but their chosen numeric values are never stated in the paper. The appendix shows hyperparameter analysis figures (which are not readable from the extracted text) but does not report the selected values. This impedes exact reproducibility. *Verified: λ₁ and λ₂ appear only in Eq. (9) and the appendix description; no numeric values are stated.*

### Minor
- **Core motivation relies on t-SNE visualization.** Figure 1 uses t-SNE to claim that CoTTA "blurs boundaries" while C-CoTTA maintains class separability. t-SNE is a non-linear embedding where visual distances do not correspond to actual feature-space distances. The paper partially addresses this with quantitative inter-class distance analysis (Figure 5a), but the primary motivation figure remains qualitative.

- **CDS optimizes against a moving target.** The domain shift direction **v**^{s→t} in CDS (Eq. 7) is recomputed from each batch, changing every iteration as the model adapts. The loss is therefore minimizing against a changing target. The paper does not discuss whether this causes instability or whether momentum-based smoothing of prototypes (e.g., EMA) could help.

- **Ablation not explicitly linked to the RMT baseline.** The ablation table's "None" row (removing CCS+CDS) corresponds to the RMT framework (SCE + mean teacher), and the paper compares against RMT as a separate baseline in the main tables. However, this equivalence is never explicitly stated, requiring the reader to infer it. Direct confirmation would improve clarity.

- **Entropy threshold (E₀) sensitivity analysis limited to CIFAR10-C.** The appendix shows sensitivity for E₀ only on CIFAR10-C; no similar analysis is provided for CIFAR100-C or ImageNet-C, where the threshold formula (0.4 × ln C) would give different values.

### Trivial
- The inter-class relative directions **v**^{s}_{i→j} (Eq. 21) are precomputed once from source prototypes and assumed to capture the relative geometry of classes under domain shift. If source-domain geometry differs substantially from target-domain geometry, the orthogonality constraint in CCS may be misaligned. This assumption is not empirically tested.

## Nice-to-Haves
- **Wall-time comparison** Would help address the O(c²) concern. Reporting seconds per batch for each method on CIFAR100-C and ImageNet-C would clarify practical feasibility.
- **Direct directional ablation** Comparing CCS against a control condition (e.g., gradient penalty along random directions) would strengthen the claim that the *specific* computed directions matter, not just any regularization.
- **Prototype smoothing via EMA** Using exponential moving averages of prototypes instead of per-batch estimates could stabilize **v**^{s→t} and **v**^{s→t}_i. The authors could report whether this changes results.
- **Class-wise error rates** The main tables are not visible in the extracted text, but if the paper reports per-corruption breakdowns in camera-ready form, that is already sufficient. If not, adding them would help identify where gains come from.

## Removed Points

These points from the inputs are flagged to be removed; treat them with caution.

- **"Tables not visible due to \include commands"** (Harsh Critic): The PDF extraction strips `\include`-d tables; the original submission contains them. This is a parser artifact, not an author error.
- **"The paper does not state the entropy threshold E₀"** (Harsh Critic — "Missing hyperparameter values"): The paper *does* state E₀: "set as 0.4 × ln C based on [EATA]" (Appendix, Section "Reliable Sample Selection Analysis"). The critic overlooked this.
- **"RMT baseline concern" framed as structural weakness** (Harsh Critic, point 3): The critic claims the paper's evidence for the proposed components is weakened because RMT is not explicitly confirmed as the ablation "None" row. This is a minor clarity issue, not a structural weakness — the paper clearly compares against RMT in the main tables, and the ablation shows CCS+CDS improve over the SCE+teacher base. Demoted to Minor above.
- **Strengths removed:** Generic/superficial strength descriptions (e.g., "addressed an important problem") omitted. Strength Finder's claim that the paper has "state-of-the-art quantitative results" kept, but the compliment about "honest discussion of limitations" is generic and conflicts with the paper's own admission that prototype contamination is a significant unresolved issue.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report results with 3–5 random seeds** and include standard deviations (or 95% CIs) for all main tables. This is the single most impactful fix for the paper's credibility.
2. **Address the O(c²) cost of CCS explicitly.** Either: (a) propose a sampling strategy over class pairs (e.g., only the top-K nearest classes per category), (b) provide wall-time measurements showing it is feasible on modern hardware for C=1000, or (c) discuss why the double-sum formulation does not create a bottleneck in practice.
3. **State λ₁ and λ₂ values** explicitly in the main paper or a reproducibility table.
4. **Clarify the ablation baseline** by confirming that the "None" row equals the RMT framework with the same architecture and training setup.
5. **Consider an EMA-based prototype update** for **v**^{s→t} to reduce batch-level instability, and report the effect.

## Score and Decision

The paper proposes a genuinely novel perspective on CTTA (controlling shift directions rather than suppressing shift magnitude), provides a clean CAV-based formulation, and evaluates across diverse scenarios. However, three systemic gaps — single-run results with no statistical rigor, an O(c²) loss left unexamined for large-class datasets, and missing hyperparameter values — collectively prevent the empirical claims from being fully trusted and the method from being reproducible. The paper is a solid contribution in need of substantial strengthening before it meets publication standards.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>