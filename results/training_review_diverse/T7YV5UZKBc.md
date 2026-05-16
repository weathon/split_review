Now I have all the verification I need. Let me produce the final consolidated review.

## Summary

This paper proposes Neural Fine-Tuning Search (NFTS), a NAS-based approach that automatically discovers the optimal adaptation strategy for few-shot learning. Given a pre-trained backbone (ResNet or ViT), NFTS determines per-layer whether to fine-tune, insert a parameter-efficient adapter, both, or neither. The approach uses a two-phase search: (1) training-time evolutionary search over a SPOS-trained supernet to pre-select a diverse set of candidate architectures, and (2) a lightweight per-episode selection at test time among those candidates. The method achieves state-of-the-art results on Meta-Dataset and Meta-Album benchmarks.

## Strengths

- **First systematic AutoML approach to adaptation strategy search for few-shot learning**: Prior work (PMF, TSA, ETT, FLUTE) makes heuristic choices about which layers to fine-tune or where to insert adapters. NFTS is the first to treat this as a search problem. The ablation study (Table 3) confirms that the searched architecture outperforms all four corner-case heuristics (e.g., +4.4% over the best heuristic for ResNet-18 single domain), providing direct evidence that search adds value beyond any single hand-designed strategy.

- **State-of-the-art performance on two major benchmarks**: The method achieves new best results on Meta-Dataset (Tables 1–2) and Meta-Album (Figure 3). On Meta-Dataset, margins over prior SOTA are substantial (+1.9% over TSA on ResNet-18 single domain, +2.3% multi-domain, +1.6% over ETT on ViT-S single domain). On Meta-Album, improvement exceeds 5% at the 5-way/5-shot operating point. Importantly, the paper shares pre-trained backbones with its closest competitors (TSA, ETT), controlling for pre-training quality as a confound.

- **Generic search space applicable to both CNNs and Transformers**: The adaptation search space is defined in an architecture-agnostic manner, with specific adapter modules (TSA for ResNet, prefix-tuning/ETT for ViT) as configurable choices. The method achieves SOTA on both ResNet-18 and ViT-S (Tables 1–2), confirming generality.

- **Novel two-phase search design with empirical justification**: The paper identifies a genuine tension in applying NAS to FSL—a single fixed architecture may not suit all novel domains, but per-episode search from scratch risks overfitting to tiny support sets. The proposed solution (training-time pre-selection of diverse candidates + test-time selection among them) is well-motivated and the ablation (Table 3) shows the deferred episode-wise selection (N=3) consistently outperforms fixing the top-1 architecture (+1.6% for ResNet-18 single domain, +0.6% multi-domain).

- **Empirical demonstration that different architectures suit different datasets**: Table 4 shows that the three diverse candidate architectures have different per-dataset rankings (e.g., Path 3 best on CIFAR-10, Path 1 best on CIFAR-100 and MNIST). The shading confirms that the episode-wise selection frequency correlates with per-dataset performance, validating the diversity constraint and the need for per-dataset adaptation.

## Weaknesses

### Fatal

None.

### Major

None. The core claim—that a searched adaptation strategy systematically outperforms hand-designed heuristics—is well-supported by the top-1 results (which do not depend on the test-time selection mechanism) and the ablation. No weakness identified undermines this central contribution.

### Minor

- **The test-time selection criterion (Eq. 9) uses loss on the same support set for both fine-tuning and selection, which risks favoring overfitted architectures.** The paper explicitly acknowledges this limitation ("this step risks overfitting," line 250) and argues it is mitigated by the training-time pre-selection to only models "unlikely to overfit." However, no empirical validation is provided—e.g., comparing the ranking induced by ℒ(·, 𝒮, 𝒮) against the true query accuracy ranking for a held-out sample of episodes. This would be straightforward to compute and would substantially strengthen confidence in the N>1 variant. Importantly, this does not affect the paper's core contribution, since the top-1 results (which do not use per-episode selection) already demonstrate the benefit of NAS over hand-designed strategies.

- **No uncertainty measures reported.** All results are point estimates (mean over 600 episodes). Few-shot benchmarks exhibit high variance, and error bars or confidence intervals would help assess the robustness of claims, especially where margins are narrow (e.g., +1.9% in Table 1). This is standard practice in many ML venues and the omission is notable.

- **Meta-Album evaluation does not compare against the same special-case baselines (TSA, ETT, PMF) shown on Meta-Dataset.** While the ablation study (Table 3) on Meta-Dataset demonstrates that NFTS outperforms all four corner-case heuristics (including TSA-like and PMF-like configurations), these same controlled comparisons are not extended to Meta-Album. The large margins over the Meta-Album paper's simple baselines in Figure 3 could partly reflect backbone/pre-training differences rather than the search itself. Running the corner-case configurations on Meta-Album would strengthen the evidence.

- **Key hyperparameters of the evolutionary search are not specified.** The paper mentions population size, mutation rate, number of generations, diversity threshold T, and learning rates η₁, η₂ as inputs to Algorithms 1–2 but does not provide their values in the experimental setup (Section 4.1). While the population size and generation count can be partially inferred from the figures (15 generations, some population size), exact values are needed for reproducibility.

### Trivial

- The notation ℒ(𝑓, 𝒮, 𝒮) in Algorithms 1–2 is mathematically defined (Eq. 5 uses support set for centroids, query set for classification, so ℒ(·, 𝒮, 𝒮) means centroids computed from 𝒮 and queries drawn from 𝒮). The intent is clear, but the paper could add a brief clarification that this is the standard prototypical training loss on the support set.

## Nice-to-Haves

- Including a random-selection baseline among the N pre-selected candidates at test time would quantify the benefit of the selection mechanism beyond just having a diverse pool.
- Reporting the actual selected architecture's performance per dataset (rather than just the performance of individual candidates in Table 4) would further strengthen the narrative of successful per-dataset selection.
- A brief discussion of the computational cost of supernet training relative to the baselines would help practitioners assess the practical trade-off.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"ViT adapter architecture (prefix tuning) is introduced without explicit citation to prefix tuning; the current text only cites ETT."** — This is factually incorrect. The paper cites prefix tuning ([li2021prefix]) explicitly in both Section 2 (Related Work, line 43) and Section 4.1 (Experimental Setup, line 322). The architecture description in Section 3.2 credits ETT as the source of the specific instantiation used, which is appropriate.

- **"The paper does not discuss whether differences in pre-training data could account for some of the gains over TSA and ETT."** — This is factually incorrect. The paper states at line 329: "We also share initial pre-trained backbones with ETT and TSA (but not PMF, as it uses a stronger pre-trained model with additional data). Thus the margins achieved over these competitors are attributable to our systematic approach." The paper explicitly addresses this point.

- **"The paper should discuss whether differences in pre-training data could account for some of the gains"** (in Meta-Album context) — For TSA/ETT, the pre-training is controlled by sharing backbones. For Meta-Album, the paper compares against the baselines from the Meta-Album paper which use different pre-training; this is a valid concern about comparison fairness but is more about the absence of the specific TSA/ETT baselines on Meta-Album (already covered in Minor weaknesses) than about pre-training confounds with TSA/ETT specifically.

- Several generic or unsupported criticisms about missing discussion, formatting, and presentation details that do not affect the paper's substance.

## Novel Insights

The reviews surface one genuinely valuable insight beyond the paper's own contributions: the distinction between the top-1 (training-time only search) and top-N (with per-episode selection) results creates a natural "sensitivity analysis" of the contribution. The top-1 results already demonstrate the core thesis (NAS beats heuristics), while the top-N results add a more speculative but interesting second claim about dynamic selection. This suggests the paper could be strengthened by foregrounding the top-1 results and treating the test-time selection as a supported-but-exploratory extension, rather than presenting both tiers equivalently. Additionally, the observation that the search discovers complex, non-intuitive per-layer patterns (Figure 2a) provides a valuable counterpoint to the simple heuristics assumed by prior work—this qualitative finding could be leveraged more prominently as a contribution in its own right.

## Suggestions

1. Add standard deviations or 95% confidence intervals to all main tables (Tables 1–3, Figure 3). For the key comparisons (NFTS vs. TSA, NFTS vs. ETT), consider reporting paired significance.
2. Add a validation experiment showing that the ℒ(·, 𝒮, 𝒮) selection criterion correlates with true query-set accuracy (e.g., Spearman correlation over a held-out sample of episodes). This would directly address the test-time selection concern.
3. Specify the missing evolutionary search hyperparameters (population size, mutation/crossover rates, diversity threshold T, learning rates η₁, η₂, number of fine-tuning steps) in the experimental setup.
4. Extend the Meta-Album evaluation to include the same corner-case ablation configurations shown in Table 3, so readers can assess how much of the gain is due to search vs. backbone/pre-training.
5. If the test-time selection cannot be rigorously validated, consider positioning the N=1 (top-1) results as the primary contribution and the N>1 results as an exploratory analysis with a known limitation.

## Score and Decision

The paper makes a genuine contribution—it is the first to formulate adaptation strategy design for few-shot learning as a NAS problem, it achieves SOTA on two benchmarks with controlled comparisons against relevant baselines, and the search space is general across architecture families. The weaknesses are real but all addressable: they are matters of missing validation (test-time selection verification), missing uncertainty measures, incomplete benchmark coverage, and missing hyperparameter details—none invalidate the core claim. The paper is a solid contribution that will be strengthened by addressing these points, but in its current form it already provides sufficient evidence for its main thesis.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>