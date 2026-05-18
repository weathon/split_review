Now I have all the information needed. Let me construct the final review.

## Summary

This paper studies the impact of test-time augmentation (TTA) on out-of-distribution (OOD) detection, categorizing augmentations into In-Distribution Augmentations (IDA) and Out-of-Distribution Augmentations (OODA). The authors propose using K-nearest-neighbor search on mild TTAs (specifically sequential masking) as a local reference set, replacing the traditional large training-set reference. On ImageNet, 25 sequential-mask TTAs achieve 84.22% average AUROC, outperforming KNN (82.75%) and VIM (82.99%) which use 1.2M training images, while being model-agnostic and requiring no modification to the pretrained classifier.

## Strengths

1. **Novel paradigm: TTAs as a local reference set for OOD detection.** The core idea — replacing a large training-set reference with a sample's own masked augmentations — is genuinely inventive. The paper shows this works competitively on CIFAR-10 (94.19% AUROC, beating KNN's 93.72%) and ImageNet (84.22% vs. KNN's 82.75% and VIM's 82.99%), establishing a new data-efficiency axis for OOD detection.

2. **Systematic IDA/OODA classification backed by LPIPS analysis.** While He et al. (2022) demonstrated TTA *can* be used for OOD detection, this paper provides the first systematic investigation of *which* TTAs work and why. The IDA/OODA categorization (Figure 2, Tables 1–2) is supported by both LPIPS distances and score-distribution shifts, and the correlation between low LPIPS and good detection performance is a useful empirical finding.

3. **Model-agnostic plug-and-play across architectures.** The method works on ResNet, ViT, and Swin Transformer backbones (Table 8) without any model modification. This is a practical advantage over methods like ASH which require dataset-specific shaping-algorithm selection (ASH-P vs. ASH-B).

4. **Thorough ablation on hyperparameters.** The paper systematically examines mask size, number of TTAs, k-value, and source space (Figures 6–8), showing the method is not catastrophically sensitive to these choices. The finding that even worst-case hyperparameters on ImageNet exceed 86% AUROC is informative.

5. **Compatibility with activation rectification (ReAct).** The method can be combined with ReAct for further gains (Table 5: 99.25% AUROC on CIFAR-10, 98.02% on ImageNet near-OOD), demonstrating it is complementary to existing techniques.

## Weaknesses

### Fatal
None.

### Major

1. **Robustness claims are selectively framed relative to the paper's own primary competitors.** The abstract states the method "is also robust to adversarial examples." However, under the C&W attack, the proposed method's performance on CIFAR-10 drops substantially (to ~81.79% from a clean 94.19%), while KNN (93.27%) and VIM (92.66%) — the paper's main baselines — are far more robust (Section 4.5, Table 6). The paper acknowledges this in the body text but the abstract and high-level narrative give the impression of general robustness without qualifying that it is mainly relative to softmax/logit-based methods that collapse under PGD, not relative to the distance-based methods that are the paper's own closest competitors. The narrative should clearly separate where the method is robust vs. where it is not.

2. **Inference cost is misrepresented or omitted.** The paper claims its method "reduces the computational cost" compared to KNN (Section 4.3), but this comparison is one-sided. The proposed method requires **25 forward passes per test sample** (one for each TTA), while KNN requires one forward pass + a nearest-neighbor search against stored features. The paper discusses neither the 25× increase in FLOPs/latency at test time nor the practical trade-off this creates. For a method that sells itself on data efficiency, the cost is shifted from storage/compute to runtime — this is a real practical limitation that must be discussed.

3. **The hyperparameter-insensitivity claim contains an internal inconsistency.** Section 4.6 states that even worst-case hyperparameters yield "over 86%" on ImageNet, "surpassing the SOTA (85.54%)." However, Section 4.3 reports ASH achieving 86.23% average AUROC on the same benchmark. The paper does not clarify what "SOTA (85.54%)" refers to — it does not match the reported ASH number, and no other method's average is given. This is either an apples-to-oranges comparison or an error, and it undermines the hyperparameter-robustness argument.

### Minor

1. **"First comprehensive study" framing is somewhat overstated.** The paper acknowledges that He et al. (2022) already demonstrated TTA can be used for OOD detection, then claims to be "the first" comprehensive study. The difference (comprehensiveness of the taxonomy vs. existence of any prior work) is real but should be more clearly delineated — what exactly did He et al. show, and what gap does this paper fill beyond classifying augmentations as IDA/OODA?

2. **No confidence intervals or statistical significance reported.** All main tables (Tables 3, 4, 6, 8) report point estimates without standard deviations or bootstrap intervals. Experiments include stochastic elements (TTA generation, potentially random mask positions), and the central claim about beating training-set methods would be stronger with uncertainty quantification.

3. **The InD-independence claim is slightly over-stated.** The method does not need InD data as a *reference set*, but it still requires InD data for threshold selection (λ chosen to capture 95% of ID data, Section 3). The paper acknowledges this implicitly but the phrasing "does not necessitate any prior knowledge of the InD data" could mislead readers. Most OOD methods use a held-out ID validation set for thresholding, so this is standard — the paper should align its language with this reality.

4. **Sequential mask implementation details are underspecified.** The paper says masks are applied "in a sequential manner" and gives mask sizes (8×8 on CIFAR-10, 44×44 on ImageNet) and counts (16, 25), but does not specify whether mask positions are random, sliding-window, or grid-based, nor whether masks overlap. A reader cannot reproduce the exact TTA generation from the description alone.

### Trivial
None.

## Nice-to-Haves

- The paper would benefit from a baseline using KNN on a small random subset of the training set (e.g., 25 random images per class) to isolate whether the benefit comes from TTA's sample-specificity or simply from the KNN framework on a small reference.
- An analysis of *why* masking works better than other mild IDAs — beyond the LPIPS correlation — would strengthen the conceptual contribution. The grayscale exception (low LPIPS but poor detection) already suggests LPIPS alone is insufficient.
- Comparing the method on OOD datasets not sensitive to masking (e.g., texture) and discussing when the approach might fail would make the limitations clearer.

## Removed Points

These points were flagged by reviewers but removed or downgraded per verification against the paper:

- **"First comprehensive study" claim is unsupported/likely false** — Removed as an overstatement. The paper does differentiate from He et al. (2022) by claiming *comprehensiveness* (IDA/OODA taxonomy, systematic study of TTA types), not priority of using TTA for OOD detection. The critic conflates these two claims.
- **Abstract performance claim is misleading because ASH beats the proposed method** — Removed. The abstract specifically says "outperforms state-of-the-art methods using the entire training set." ASH does not use the training set. The claim is technically accurate; the paper acknowledges ASH's superior average AUROC in Section 4.3.
- **ASH vs. proposed method hyperparameter symmetry** — This is a valid observation but is already partially acknowledged by the paper (Section 4.3 discusses ASH's dataset-specific shaping vs. the proposed method's consistent approach). The paper could be more transparent, but this is not a weakness so much as a symmetric property of both methods.
- **LPIPS may not transfer across domains** — The paper already acknowledges the grayscale exception (Section 2, Table 2 discussion). The LPIPS-based classification is presented as a useful heuristic with known limitations, not a universal law.
- **Choice of k=2 and k=4 motivation weak** — The paper provides motivation from Figure 8, showing a sharp decline after small k-values. While deeper analysis would be nice, the empirical justification is present and reasonable.

## Novel Insights

The most interesting observation that emerges from the reviews — beyond what the paper itself claims — is the asymmetry in what the method reveals about OOD detection. The paper shows that *local* consistency (between a sample and its own masked variants) carries surprisingly discriminative signal, almost as strong as global consistency with 1.2M training examples. This suggests that the information needed to distinguish in-distribution from OOD samples is redundantly encoded across local spatial regions of a single sample, at least for the kinds of distributions tested. The fact that C&W attacks — which add tiny, imperceptible perturbations — are largely invisible to masking (and thus degrade the method disproportionately) reinforces this: if the method is working by detecting spatial perturbation of local features, then adversaries that preserve spatial structure while shifting semantics will evade it. This spatial-local vs. global-distributional axis of OOD detection is underexplored and the paper's results, despite their framing issues, open a concrete door for future work on sample-local OOD signals.

## Suggestions

1. **Revise the abstract and contribution list** to precisely delineate: (a) the IDA/OODA taxonomy study, (b) the KNN-on-TTA method, and (c) where it is/is not state-of-the-art. The abstract should mention that the method underperforms ASH on average but exceeds training-set-based methods, and should qualify the robustness claim.
2. **Add a discussion of inference cost** (forward passes per sample, wall-clock time vs. KNN and ASH) in Section 4 or as a dedicated limitations paragraph.
3. **Clarify the SOTA reference (85.54%)** in Section 4.6 — either specify it excludes ASH, or correct it if inconsistent with Table 4.
4. **Add confidence intervals** (standard deviations over at least 3 runs, or bootstrap intervals) to the main tables.
5. **Specify the sequential mask positioning strategy** (random positions? sliding window? grid pattern?) in Section 3 so the method is reproducible.

## Score and Decision

**Evaluation:** The core contribution — using TTAs as a local reference set for OOD detection — is novel, empirically validated across two ID datasets and multiple architectures, and produces competitive results. The IDA/OODA taxonomy is a useful addition to the literature. The main weaknesses are in framing (overclaimed novelty, selective robustness presentation), a missing discussion of practical inference cost, and a minor internal inconsistency. None of these undermine the core empirical finding. With reasonable revisions to tone down claims and add missing context, this is a solid paper.

**Originality:** High — using sample-local TTAs as a reference set is a genuinely new approach for OOD detection. **Importance:** High — data-efficient OOD detection is practically relevant. **Claims support:** Adequate with caveats — the main empirical claims are backed, but the robustness and "first comprehensive study" claims need qualification. **Soundness:** Good overall, lacking only statistical confidence measures. **Clarity:** Good, though the sequential mask specification could be clearer. **Value:** Positive — the method is simple, model-agnostic, and competitive.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>