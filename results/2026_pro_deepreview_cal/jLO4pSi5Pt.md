Now I have a thorough understanding of the paper and the calibration landscape. Let me synthesize the final review.

---

## Summary

This paper introduces L-TTA, the first test-time adaptation method for vision-language models (VLMs) specifically designed for long-tailed test streams. It identifies two failure modes of existing TTA under class imbalance (text-induced tail erosion and modality-bias amplification) and proposes three cooperative components: Synergistic Prototypes (deterministic and exclusionary) to enrich tail-class representations, learnable Rebalancing Shortcuts with a class re-allocation loss for dynamic adaptation, and Balanced Entropy Minimization (BEM) — a theoretically grounded variant of entropy minimization that reduces the optimization gap between head and tail classes. Extensive experiments across 15 datasets, three imbalance ratios, and multiple backbones demonstrate consistent gains in both accuracy and macro-F1 over 12 baselines.

## Strengths

- **Novel problem formulation with clear motivation**: The paper is the first to systematically study long-tailed test-time adaptation for VLMs. The two identified failure modes (text-induced tail erosion, modality-bias amplification) are illustrated with concrete evidence (Figure 1) and provide a clear rationale for the method's design. This fills a genuine gap — existing TTA methods are evaluated on balanced benchmarks but degrade severely under realistic long-tailed distributions.

- **Comprehensive and consistent empirical validation**: Tables 1–3 evaluate 12 baselines across OOD, Cross-Domain, and Corruption benchmarks under three imbalance ratios (10, 20, 50). L-TTA achieves the best accuracy and macro-F1 on nearly every dataset. The macro-F1 gains are particularly substantial (e.g., +2.20% on Cross-Domain average over the next best method, Table 2), directly validating the class-rebalancing claim. The superiority persists across four additional backbones (ViT-L/14, ViT-H/14, SigLIP-L/16, MetaCLIP-BigG, Table 5) and under corruption noise (Table 3), where prior prototype-based methods degrade substantially while L-TTA maintains its lead.

- **Effective synergistic component design**: Ablation studies (Table 6) demonstrate that each component contributes meaningfully — removing either Deterministic Prototypes or Exclusionary Prototypes causes macro-F1 drops of ~3.95% and ~3.22% respectively on ResNet-50, and adding Rebalancing Shortcuts and BEM further improves performance. This validates that the three components work synergistically rather than being redundant.

- **Theoretical grounding for Balanced Entropy Minimization**: Propositions 1 and 2 (Section 3.2) formally characterize how standard entropy minimization biases head classes in long-tailed settings and prove that BEM reduces the gradient gap between head and tail logits. This provides principled justification beyond heuristics for the core optimization objective.

- **Favorable efficiency–performance trade-off**: Table 4 shows L-TTA uses 1.45h runtime and 1.89G memory while achieving the highest harmonic mean of accuracy and macro-F1, outperforming heavier methods like WATT (27.7h) and RLCF (18.3h). The method's computational efficiency is a practical strength.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **No error bars reported despite multiple runs**: The paper states that 5 runs were conducted for each experiment, yet Tables 1–3 report only point estimates without standard deviations. Given that some accuracy margins are modest (e.g., 0.7% on OOD average at imb=20 over DPE in Table 1), reporting variance is important for assessing the significance and stability of the gains. This is addressable in a rebuttal by providing the relevant statistics.

- **Class Re-Allocation (CRA) loss motivation is somewhat ad-hoc**: The CRA loss (Eq. 7) is inspired by load-balancing losses for mixture-of-experts in LLMs. While the ablation shows RS contributes ~0.7% macro-F1, the paper's argument that minimizing the dot product of attention scores and top-1 counts "results in discernable feature clustering and reduces dominance of head-class prototypes" is asserted rather than demonstrated. A more direct analysis — e.g., showing that CRA actually makes hyper-class attention more uniform or that it correlates with improved tail-class separation — would strengthen this component's justification. The current motivation reads as an analogy rather than a derived design.

- **No discussion of limitations**: The paper lacks a limitations section. Potential failure modes (e.g., extremely severe imbalance where pseudo-label counts become completely unreliable, datasets with very large numbers of classes, or scenarios where text-encoder biases overwhelm the prototype mechanism) should be acknowledged. This is a straightforward addition that would improve completeness.

- **Sensitivity to early-stream prior estimates not analyzed**: BEM relies on class priors updated from pseudo-labels during adaptation (Eq. 9). In the early data stream, when few samples have been seen, these prior estimates may be noisy. The paper does not analyze sensitivity to this initialization or study the effect of the momentum parameter in prior updates. While the strong empirical results suggest this is not a practical problem, the analysis would be informative.

### Trivial

- The definition of "rich classes" in the failure mode analysis (Section 1, Figure 1b.1) relies on a single t-SNE visualization. A quantitative breakdown showing that certain classes persistently outperform others regardless of head/tail status would make this motivational claim more rigorous.

## Nice-to-Haves

- **A simple class-balanced TTA baseline** (e.g., TPT or TDA augmented with online logit-adjusted entropy minimization or balanced softmax using pseudo-label counts) would directly test whether the full L-TTA pipeline is necessary or whether a simpler reweighting scheme could approach its performance. The paper argues theoretically (near Eq. 9) that naive logit adjustment can exacerbate bias under EM, and Appendix G apparently compares BEM with classic LT methods; a full pipeline comparison would nonetheless strengthen the claim of non-triviality.

- A quantitative stability analysis of Exclusionary Prototypes — e.g., measuring EP class-separation over time or tracking whether they genuinely encode anti-class semantics — would make the EP design principle more convincing beyond the ablation.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"Training-free methods like ZERO, MTA and TDA are sensitive to data quality" is misleading** — The critic claimed this statement in the efficiency discussion is misleading. The statement appears at line 312 of the paper and is supported by the Corruption Benchmark results (Table 3), where MTA, ZERO, and TDA indeed show degradation under noise. The claim is a reasonable interpretation of the paper's own experimental data, not misleading. Removed.

- **CRA loss could push attention toward degenerate configurations** — The critic speculated that the product-of-averages loss "could push attention weights toward degenerate configurations (e.g., all prototypes assigning equal attention to all experts)." This is speculative and not supported by evidence in the paper or any external analysis. The ablation shows RS helps, which is evidence against this claim. Removed.

- **"Rich classes" definition needs more rigorous support than a single t-SNE visualization** — Kept as Trivial rather than removed (see above), as it's a valid observation about presentation rigor but carries no weight in evaluation.

- **Various "Strengthening the Paper on Its Own Terms" suggestions** — Moved to Nice-to-Haves where appropriate.

## Novel Insights

None beyond the paper's own contributions. The identification of text-induced tail erosion — where text embeddings carry pre-training biases that interact with head classes to amplify imbalance — is the paper's own contribution and a genuinely novel observation about how the multi-modal nature of VLMs creates unique challenges for long-tailed TTA beyond what unimodal methods face.

## Suggestions

- Report standard deviations in the main tables (Tables 1–3) given the 5-run setup. This is the single most impactful improvement to the paper's rigor.
- Include a brief limitations paragraph discussing scenarios where L-TTA might struggle (very large class counts, extremely severe imbalance, etc.).
- Provide a more direct empirical justification for CRA — e.g., visualize attention uniformity across hyper-class vectors with and without CRA, or show that CRA correlates with improved tail-class feature separation.
- Consider a small case study measuring the gradient gap from Propositions 1–2 on a representative dataset to anchor the theoretical motivation empirically.

---

**Calibration Report:**

Round 1 bracketing placed the paper between ~5.0 and 8.0.
- Low band (<3.5): Anchors at ~2.5 (clearly rejected papers with significant flaws). L-TTA is substantially stronger.
- Middle band: `b20VK2GnSs` (7.00, Accept) — concept drift + long-tailed VLMs, similar domain but with clarity concerns. `lF9QXpfNHm` (4.67, Reject) — open-world TTA with significant contribution and methodology concerns. L-TTA is stronger than both.
- Upper band: `TPZRq4FALB` (8.00, Accept) — near-perfect TTA paper with new benchmarks, all 8s. L-TTA has more minor issues (no error bars, weaker CRA motivation).

Round 2 narrowed to the 6.0–8.0 range:
- `9w3iw8wDuE` (7.00, Accept) — DeYO, a TTA paper with theoretical grounding and strong empirical results. Has its own weaknesses (missing baselines in key tables, unclear motivation for some design choices). L-TTA is comparable: both identify a TTA problem, provide theory, and demonstrate empirical gains. L-TTA's experimental scope is larger (15 datasets vs typical TTA benchmarks). 
- `75PhjtbBdr` (6.25, Accept) — multi-label TTA with entropy minimization. Weaker overall. L-TTA is clearly stronger.
- `kIP0duasBb` (6.67, Accept) — TTA with CLIP reward. L-TTA is stronger.
- `TD3SGJfBC7` (6.25, Accept) — few-shot TTA for CLIP. L-TTA is stronger.

L-TTA sits closest to `b20VK2GnSs` (7.00) and `9w3iw8wDuE` (7.00) in quality — a solid Accept with minor addressable issues. The missing error bars and somewhat ad-hoc CRA motivation prevent it from reaching 8.0 territory. Final score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>