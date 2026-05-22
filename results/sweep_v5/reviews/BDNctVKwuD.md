I now have all the information to produce the consolidated review. Let me synthesize everything.

## Summary

This paper makes two connected contributions. First, it identifies a mathematical redundancy in HiResCAM explanations — adding an arbitrary matrix *M* to all class-wise HiResCAMs yields the same softmax probabilities (Theorem 3.2) — and proposes ContrastiveCAMs (pairwise differences of HiResCAMs) that are invariant to this shift. Second, using ContrastiveCAMs, the paper shows that cross-entropy does not penalize non-core region contributions (Proposition 4.2) and introduces Core-Focused Cross-Entropy (CFCE), a loss that suppresses contributions from user-specified non-core regions. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC show that CFCE-trained models achieve dramatically higher IoU with core-region masks and improved robustness to core-region ablation, at some accuracy cost.

## Strengths

1. **Novel theoretical identification of a redundancy in HiResCAMs.** Theorem 3.2 proves that HiResCAM explanations for a given input admit an additive matrix *M* across all classes while preserving the same softmax predictions. This is a clean mathematical observation that was not previously formalized. (Section 3, lines 128–148)

2. **ContrastiveCAMs are well-defined and M-invariant.** Theorem 3.5 proves that ContrastiveCAMs (Definition 3.3) and their reconstructed variant (Definition 3.4) are unaffected by the spurious shift *M*, and Proposition 4.1 shows that softmax probabilities can be expressed as a direct function of ContrastiveCAMs. **Crucially, ContrastiveCAMs also provide granular class-versus-class explanations that HiResCAM does not — this is an independent practical benefit regardless of the theoretical debate about the significance of *M*.** (Section 3, lines 160–184; Section 4, lines 217–224)

3. **CFCE loss is principled and theoretically grounded.** Definition 4.5 introduces a loss that penalizes non-core region contributions by manipulating ContrastiveCAM values, and Theorem 4.6 proves that minimizing CFCE risk converges to the Bayes-optimal core-constrained risk. This provides theoretical backing that many prior empirical masking or regularization approaches lack. (Section 4.2, lines 259–276)

4. **Large empirical improvement in core-region alignment across multiple datasets.** On Hard-ImageNet (Table 2), CFCE+KL achieves 93.39% ContrastiveCAM IoU and RFS of +0.236, compared to cross-entropy's RFS of -0.18. On PASCAL VOC (Table 5), CFBCE+KL achieves 85.39% IoU versus CE's 44.50%. The paper reports results on classification (multiclass, binary, multilabel) and downstream segmentation, showing breadth.

5. **Effectiveness with approximate masks (SAM, bounding boxes).** Table 3 shows that CFCE with SAM-generated masks achieves 85.16% IoU (multiclass valid) versus 93.12% with ground-truth masks, while maintaining competitive accuracy. This demonstrates practical utility when precise core masks are unavailable, a realistic scenario.

6. **Consistent downstream segmentation improvements.** Figure 4 shows that CFCE+KL-pretrained backbones yield higher IoU for nearly all 20 PASCAL VOC classes in both fine-tuning and end-to-end segmentation settings compared to cross-entropy pretrained backbones.

## Weaknesses

### Fatal
None. The paper's core claims are supported by the presented evidence, and no verified flaw invalidates the central contribution.

### Major

1. **The motivation for ContrastiveCAMs as a "fix" to HiResCAMs is overstated.** Theorem 3.2 correctly shows that adding *M* to all class-wise HiResCAMs preserves softmax probabilities. However, for any **fixed trained model given a specific input**, the HiResCAM is uniquely and deterministically computed — the ambiguity exists only across hypothetical alternative logit configurations that produce the same probabilities, not within a single model. The paper's claim that "explanations may be misleading" and "fail to guarantee a faithful interpretation" (lines 148–149) because of this redundancy is unsupported: no experiment demonstrates a case where HiResCAM is actually misleading for a fixed model. The practical significance of Theorem 3.2 is thus unclear; ContrastiveCAMs are better justified by their independent value as pairwise explanation tools (class-versus-class explanations) rather than as a fix for a practical limitation of HiResCAM.

2. **The IoU metric is partially tautological because the CFCE loss directly optimizes what it measures.** CFCE (Definition 4.5) suppresses |ContrastiveCAM| on non-core regions and the KL regularization (Definition 4.7) forces ContrastiveCAM shape similarity to the mask *H*. It is thus expected — indeed, by design — that ContrastiveCAM IoU with core masks is very high (e.g., 89.22–93.39% on Hard-ImageNet). This does not necessarily mean the explanations are more faithful or that the model has genuinely learned better features; it means the model has been optimized to produce ContrastiveCAMs that match the mask. The paper partially mitigates this with independent metrics (accuracy under core-region ablation, RFS), and the ablation results are genuinely impressive (e.g., Gray Mask accuracy drops from 75.94% → 41.78% for CE vs. CFCE). But the paper's core claim of "improving feature alignment" rests too heavily on the IoU metric that the loss was designed to maximize.

3. **Missing comparison with relevant alignment methods.** The paper compares against CORM (Singla et al., 2022) and DFR (Krichenko et al., 2022), which are ablation-based evaluation methods, not training-time alignment methods. It does **not** compare against approaches that use saliency-based regularization to suppress spurious features, such as Right for the Right Reasons (Ross et al., 2017), attention-based masking penalties (Kc et al., 2021; Aniraj et al., 2023), or simpler alternatives like directly masking GAP-pooled features. Without these comparisons, the added value of the full ContrastiveCAM/CFCE machinery over simpler approaches is unclear.

### Minor

1. **No faithfulness evaluation of the explanations themselves.** The paper claims ContrastiveCAM provides "more faithful attention maps" (abstract, line 68), but never evaluates faithfulness (e.g., via deletion/insertion metrics, input perturbation tests, or comparison with ground-truth attribution). The paper evaluates only alignment (IoU with core masks), which is a different property. This gap between claims and evidence weakens the paper's narrative.

2. **The accuracy cost is non-trivial and its acceptance requires stronger justification.** On Hard-ImageNet, un-ablated accuracy drops from 94.25% (CE) to 90.35% (CFCE+KL, ~4% relative drop). On Oxford-IIIT Pets multiclass, valid accuracy drops from 94.41% (CE) to 90.08% (CFCE+KL). While the paper shows benefits on ablation and RFS metrics, it does not demonstrate that these trade-offs are favorable in practical deployment scenarios, or that the alignment gains translate to out-of-distribution generalization.

3. **No ablation study of the KL regularization hyperparameters (λ1, λ2, λ3).** The KL divergence term is a key component (Definition 4.7), yet the paper does not study how varying these parameters affects the accuracy–IoU trade-off. This makes it difficult for readers to understand the method's sensitivity or to apply it to new datasets.

4. **No statistical tests for main claims.** Standard deviations are reported (with ± notation) but the paper does not perform significance tests for the main comparisons (e.g., whether the accuracy drops or IoU gains are statistically significant across runs). This is acceptable in many empirical papers, but given the reliance on relatively small performance differences in some settings (PASCAL VOC AP: 87.32% CE vs. 88.39% CFBCE), it would strengthen the presentation.

### Trivial
None worth listing.

## Nice-to-Haves
- A faithfulness evaluation (deletion/insertion, or occlusion-based metrics) comparing ContrastiveCAM against HiResCAM would validate the claim of "more faithful" explanations.
- An ablation sweeping the KL regularization parameters (λ1, λ2, λ3) would help practitioners apply the method.
- A comparison with saliency-regularization methods (Right for the Right Reasons or similar) would clarify the method's novelty over simpler approaches.
- Analysis of failure cases where CFCE substantially hurts accuracy (e.g., classes where context/non-core regions are genuinely informative) would strengthen the paper's honesty and usefully bound the method's scope.

## Removed Points

1. **Critic's claim (Critical Issue 1, second part):** "The paper's narrative that 'explanations may be misleading' due to this non-uniqueness is misleading itself." — Partially kept as Major weakness #1 but reformulated. The practical significance is overstated, but the mathematical observation is genuine and ContrastiveCAMs have independent value.

2. **Critic's claim about "Figure 1 is artificial; no real model can exhibit CAMs that differ by an arbitrary M because M would change the logits and thus the gradients."** — This misunderstands the paper. The theorem is about the *interpretation* of HiResCAMs relative to probabilities, not about actual gradient computation. A fixed model's gradients are fixed, but the paper's point (however overstated) is that the mapping from HiResCAMs to predictions is many-to-one. Removed as a misunderstanding.

3. **Critic's claim that "γ in Table 1 could simply mean the average HiResCAM over classes has large norm."** — This is a generic speculation without concrete evidence. The redundancy ratio is a reasonable quantification. Removed.

4. **Critic's claim that "Proposition 4.2 and Remark 4.3 are algebraically correct but essentially restate that cross-entropy can be decomposed into core and non-core contributions — this is not a new insight."** — Every theoretical paper builds on known algebra; the insight is that this decomposition *reveals* that CE does not penalize non-core contributions, which is the paper's point. Removed as overly dismissive.

5. **Critic's claim about divergence regularization "forcing the model to use the entire mask region — even parts that may be irrelevant or noisy."** — This is speculation without evidence. The paper could fail in this way, but there is no demonstration that it does. Removed.

6. **Strength Finder strength about "Large empirical improvement in core-region alignment"** — Kept but qualified in weaknesses.

7. **Strength Finder strength about "Effectiveness with approximate masks"** — Kept as strength #5.

## Novel Insights

The reviews surface a genuine tension between the paper's two contributions. The ContrastiveCAM theory (Theorem 3.2, 3.5) and the CFCE loss (Definition 4.5, Theorem 4.6) are **logically independent** — ContrastiveCAMs are justified by their invariance to *M* and their pairwise explanatory value, while CFCE is justified by Proposition 4.1 and 4.2. Yet the paper loosely connects them into a single narrative ("HiResCAMs are unreliable → ContrastiveCAMs fix this → ContrastiveCAMs reveal non-core usage → CFCE suppresses it"). The reviews reveal that the first link (HiResCAM unreliability) is the weakest, but the later links (pairwise explanations, core-region suppression via CFCE) are well-supported. An interesting observation is that the paper could be strengthened by de-emphasizing the "fixing HiResCAM" framing and instead presenting ContrastiveCAMs as a tool for pairwise explanation that *also* has nice theoretical properties, then directly motivating CFCE from the fact that CE does not distinguish core from non-core contributions (already shown in Proposition 4.2).

## Suggestions

1. **Re-focus the motivation.** De-emphasize the claim that HiResCAMs are "misleading" in practice. Instead, motivate ContrastiveCAMs by their pairwise explanatory power (class-vs-class), which HiResCAM does not provide, and their M-invariance as a clean theoretical property.

2. **Add faithfulness metrics.** Include deletion/insertion or occlusion tests comparing ContrastiveCAM vs. HiResCAM to substantiate the "more faithful" claim. Without this, the claim rests entirely on theory with no empirical support.

3. **Add comparisons with saliency-regularization methods.** Compare CFCE against simpler approaches like Right for the Right Reasons (Ross et al., 2017), foreground-masked training, or GradCAM-penalized training. This would clarify whether the complexity of computing ContrastiveCAMs during training is justified.

4. **Add an ablation of KL regularization hyperparameters.** Show the accuracy–IoU Pareto frontier as λ1, λ2, λ3 vary.

5. **Discuss when non-core features are genuinely useful.** The paper assumes non-core = bad, but many tasks benefit from context (e.g., "boat" near water). A discussion or small experiment on this limitation would improve the paper's intellectual honesty.

## Score and Decision

### Calibration Anchors

The following papers from the human review corpus were used for score calibration:

- **GjfIZan5jN** (avg 7.33, Accept) — "Enhancing Pre-trained Representation Classifiability can Boost its Interpretability." Strong paper with extensive experiments across models and datasets, clear metric proposal, and multiple validation angles. The current paper has a comparable level of theoretical contribution but weaker evaluation breadth and fewer baselines.

- **OZWHYyfPwY** (avg 7.00, Reject) — "Don't trust your eyes: on the (un)reliability of feature visualizations." This paper had compelling empirical demonstrations of its claims. Though rejected (score–decision mismatch possible due to ICLR policy), it scored high on contribution and presentation rigor. The current paper has less compelling empirical evidence for its core narrative.

- **GlAeL0I8LX** (avg 6.67, Accept) — "QPM: Discrete Optimization for Globally Interpretable Image Classification." Extensively evaluated with multiple metrics and datasets. The current paper is weaker in evaluation scope (missing faithfulness metrics, fewer baselines).

- **bkdWThqE6q** (avg 6.00, Accept) — "A Simple Interpretable Transformer for Fine-Grained Image Classification." Clean method with clear presentation. The current paper has more theoretical depth but less polished evaluation.

- **57NfyYxh5f** (avg 6.25, Accept) — "How to Probe: Simple Yet Effective Techniques for Improving Post-hoc Explanations." Well-scoped paper with strong empirical findings about training details affecting explanations. The current paper has more theory but less convincing empirical validation of its motivational claims.

- **EwAGztBkJ6** (avg 4.00, Reject) — "On the Generalization of Gradient-based Neural Network Interpretations." Interesting theory but weak experiments. The current paper is substantially stronger in both theory and experiments.

- **waIltEWDr8** (avg 3.00, Reject) — "WASUP." Limited novelty, no comparison with interpretable models, heavy reliance on existing methods. The current paper has significantly more novelty and a stronger theoretical contribution.

- **BwQUo5RVun** (avg 3.00, Reject) — Weak grounding method with limited evaluation. The current paper is substantially stronger.

- **JZjW3k4Kyc** (avg 3.75, Reject) — "Mechanistic Insights: Circuit Transformations." Weak connection between theory and experiments. The current paper has a much tighter connection between its theory and experiments.

Relative to these anchors, the current paper sits above the clearly rejected papers (3.00–4.00) but below the strongest accepted papers (6.67–7.33). It has genuine theoretical contributions and promising results, but the evaluation gaps (overstated motivation, missing baselines, no faithfulness metrics, no hyperparameter ablation) place it below the typical acceptance threshold. A carefully revised version addressing the major weaknesses could reach the acceptance range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>