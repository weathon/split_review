Now I have a solid calibration. Let me compare:

- **GC-CLIP (4.75)**: Simple idea (guided cropping for CLIP), limited novelty, marginal gains, evaluation on only 2 datasets. RTA is clearly stronger — it has a more compelling motivating insight (Ceiling TTA), a more novel method, and much broader evaluation.
- **"Extending to New Domains" (5.33)**: Scores [8,5,3]. A creative use of CLIP's modality gap, training-free, but marginal gains over baselines and similarity to prior work flagged by one reviewer. RTA has a similarly creative core idea and similarly marginal gains on the strong backbone, but has a more concrete methodological gap (dimensionality mismatch).
- **DOTA (6.00)**: All 6s. Good idea, well-structured, but methodological gaps about updating distributions in single-image setting. RTA's dimensionality issue is more concrete and undermines more of the experimental evidence.

RTA sits between GC-CLIP (4.75) and DOTA (6.00), closer to "Extending to New Domains" (5.33) but with a more significant methodological gap. I place RTA at **4.5** — the core idea is genuinely interesting and the oracle experiment is a real insight, but the dimensionality mismatch casts doubt on Tables 4-6 (roughly half the experimental evidence), and the gains on the stronger ViT-B/16 backbone are marginal.

---

## Summary
This paper proposes Regression-based Test-Time Adaptation (RTA), which replaces the standard entropy-based view selection in CLIP test-time adaptation with a learned regression model. An offline LightGBM decision tree is trained once on pseudo-labeled ImageNet validation data to predict cross-entropy loss from logit vectors; at test time, augmented views with the lowest predicted loss are selected for ensemble prediction. The key motivating insight is a "Ceiling TTA" experiment showing that oracle label-loss-based view selection dramatically outperforms entropy-based selection (e.g., +25.9 points on ImageNet-A with ViT-B/16), cleanly demonstrating that view-selection quality is the primary bottleneck in current TTA.

## Strengths
- **Compelling Ceiling TTA oracle experiment (Tables 1-2)**: The demonstration that oracle LCE-based view selection achieves enormous gains over entropy (e.g., ViT-B/16 on IN-A with 64 views: 90.2% LCE vs 64.3% entropy) is striking and well-presented. This experiment alone provides a useful benchmark for the field by quantifying the view-selection gap that existing TTA methods fail to exploit.
- **Methodological simplicity and efficiency**: RTA uses a single shallow LightGBM tree (max_depth=5, 16 leaves) trained on only 1,000 pseudo-labeled samples once offline. At test time, inference is a single tree traversal per view — no per-instance gradient updates (unlike TPT), no diffusion model inference (unlike DiffTPT), no cache maintenance (unlike TDA/BCA). This makes the method genuinely practical for deployment.
- **Broad evaluation coverage**: Results span single-label ImageNet variants (Table 3), 10 cross-domain datasets (Table 4), and multi-label benchmarks (Tables 5-6) across both RN50 and ViT-B/16 backbones. Where Table 3 is trustworthy, RTA consistently improves over the CLIP baseline.
- **t-SNE visualization (Figure 2)** provides qualitative evidence of structural relationships between logit representations and cross-entropy loss across diverse distributions, supporting the premise that a regression model can learn this mapping.

## Weaknesses

### Major
- **Input dimensionality mismatch for cross-domain and multi-label experiments**: The regression decision tree is trained on logit vectors computed over ImageNet's 1,000 classes, with internal splits referencing specific feature indices in this 1,000-dimensional space. However, test-time cross-domain datasets have different numbers of classes (Pets: 37, Aircraft: 100, Cars: 196, etc.) and multi-label datasets likewise differ (MSCOCO: 80, VOC2007: 20, NUSWIDE: 81). The paper explicitly defines L as "the number of labels in the test set" (Section 3), and Algorithm 2 computes logits for j = 1,...,L, producing vectors of varying dimensionality that cannot be fed to a tree trained on 1,000 features. No mechanism is described for bridging this gap — no feature selection, dimensionality alignment, or per-dataset retraining protocol. This calls into question the validity of the cross-domain results (Table 4) and multi-label results (Tables 5-6), which together constitute a substantial portion of the paper's experimental evidence. (The ImageNet variant results in Table 3 are not affected since those datasets share the same 1,000-class space.)
- **No controlled comparison isolating regression vs. entropy on identical views**: The paper's central claim is that the learned regression model provides better view selection than entropy. Yet there is no experiment comparing RTA's regression tree against entropy-based selection on the exact same augmented views, using the same ensemble protocol and same number of views. Comparisons are only against published methods (Zero, TPT, BCA, etc.) that each have their own augmentation strategies and selection protocols, making it impossible to isolate whether the regression model adds value beyond what entropy would achieve on the same input.

### Minor
- **Marginal gains on the stronger ViT-B/16 backbone**: On ViT-B/16 (Table 3), RTA achieves OOD Avg 65.84% vs. Zero's 65.03% (+0.81 pp across 4 datasets). The cross-domain margin over BCA is 68.70% vs. 68.59% (0.11 pp, Table 4). These sub-1% differences are within typical measurement noise and do not support the strong language ("significantly outperforms") used throughout the paper. Gains are more substantial on the weaker RN50 backbone, but RN50 results notably omit the Zero baseline.
- **Spearman analysis based on only 2 examples per dataset** (Figure 3): The correlation analysis examines logit-loss relationships for only Example 0 and Example 1 from each dataset. While suggestive, this is too sparse to support general claims about regression structure across the full test distribution.
- **Zero baseline omitted from RN50 results** (Table 3): Zero (Farina et al., 2024) is the most directly comparable method — it also does view selection + ensemble without parameter updates. It is included for ViT-B/16 but absent from RN50, weakening the RN50 comparison.
- **Oracle-to-RTA gap not discussed**: The Ceiling TTA oracle achieves 90.2% on IN-A (ViT-B/16, 64 views) while RTA achieves only 65.65%. The paper does not analyze what fraction of the oracle gain is recovered or why such a large gap remains (the regression model recovers only ~7% of the 25.9-point oracle gain on this metric).

### Trivial
- **Duplicate TDA rows in Table 4**: Two rows are both labeled "TDA [CVPR 2024]" with different numbers (Avg 67.53 vs. 65.58), suggesting a formatting error that makes cross-comparison unreliable.

## Nice-to-Haves
- No variance or standard deviations reported for any results, making it impossible to assess statistical significance of sub-1% improvements.
- No comparison with using maximum softmax probability as a view-confidence measure, which is a simpler baseline than the full regression pipeline.
- The computational cost of the regression training is described as "negligible" but not quantified (training time, number of CLIP forward passes).
- No experiments on distributions radically different from ImageNet (e.g., medical imaging, satellite beyond EuroSAT) to support the "arbitrary test distributions" claim.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "pseudo-label contradictions create contradictory training signals"** — REMOVED. The paper addresses this via the confidence threshold ≥ 0.8 filtering (Section 5.1), which is a standard mitigation. The critic speculates about residual issues without evidence from the paper.
- **Harsh Critic: "existing methods rely solely on probability distribution of a single test instance — this is inaccurate regarding cache methods"** — REMOVED. This is a framing dispute about a sentence in the introduction, not a substantive flaw in the method or results.
- **Harsh Critic: "regression model captures artifacts of weaker backbone's confidence patterns"** — REMOVED. Speculative and unsupported by evidence in the paper.
- **Strength Finder: "training-distribution independence is a notable architectural advantage"** — REMOVED. This claimed strength is directly undermined by the dimensionality mismatch issue — the regression model is not demonstrated to be distribution-independent for arbitrary class spaces.
- **Strength Finder: "the ablation in Figure 5 confirms reasonable data scaling"** — REMOVED. While Figure 5 exists, this is a routine ablation that doesn't rise to the level of a noteworthy strength. Moved to a supporting observation.
- **Harsh Critic: "LightGBM hyperparameters stated without justification"** — REMOVED. Default hyperparameters are standard; demanding justification for every hyperparameter choice is unreasonable.
- **Harsh Critic: "the 'free lunch' framing is misleading since RTA requires curating a pseudo-labeled dataset"** — REMOVED. This is a rhetorical critique about word choice in the abstract, not a substantive weakness.
- **Harsh Critic: missing discussion of radically different test distributions** — MOVED to Nice-to-Haves. Generic "evaluate on more datasets" request.
- **Harsh Critic: no compute time quantification** — MOVED to Nice-to-Haves. Generic efficiency nitpick.

## Novel Insights
The Ceiling TTA experiment is genuinely revealing: the paper demonstrates that view-selection quality — not the augmentation pipeline or ensemble mechanism — is the primary bottleneck in current TTA, and that perfect view selection can recover enormous accuracy (e.g., +25.9 points on ImageNet-A with 64 views). This is a useful benchmark for the field that others can build on even if the specific regression approach has limitations. The paper also makes the interesting observation that the logit-to-loss relationship exhibits learnable structure (t-SNE in Figure 2), opening a new direction beyond entropy-based heuristics for test-time view selection.

## Suggestions
- **Clarify the dimensionality mechanism**: Explain how the 1,000-dimensional regression tree is applied to datasets with different numbers of classes. If the solution involves computing all 1,000 ImageNet-class logits for view selection and separately computing test-class logits for prediction, describe this explicitly and report the computational overhead. This is essential for the cross-domain and multi-label results to be credible.
- **Add the controlled entropy comparison**: Compare RTA's regression tree against entropy-based selection on the identical set of augmented views, with the same ensemble protocol and number of views. This is the single most important ablation — without it, the paper cannot claim that the regression approach is better than entropy.
- **Include Zero in RN50 baselines** and fix the duplicate TDA row in Table 4.
- **Tone down claims** of "significantly outperforms" for ViT-B/16 results where margins are sub-1%.

## Anchor Comparison
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Projected Subnetworks Scale Adaptation | 2.00 | R1 | RTA is substantially stronger — has genuine insight and solid experiments |
| Multimodal Class-Incremental Learning benchmark | 2.33 | R1 | RTA clearly more developed |
| CLIP-Enhance (vMF Clustering) | 3.67 | R1 | RTA has better motivating insight and broader evaluation |
| PRO: Pseudo-label Regularized Optimization | 3.75 | R1 | RTA has comparable novelty but better motivating experiment |
| GC-CLIP: Guided Cropping | 4.75 | R2 | RTA has stronger motivation, more novelty, broader evaluation |
| Test Time Adaptation with Auxiliary Tasks | 4.67 | R2 | RTA has more creative idea, but both have methodological gaps |
| Extending to New Domains w/o Oracles | 5.33 | R2 | Comparable creativity; RTA has a more concrete methodological issue |
| BAT-CLIP: Bimodal TTA | 5.50 | R1 | RTA has a clearer motivating experiment but larger methodological gap |
| DOTA: Distributional TTA | 6.00 | R1 | DOTA is more methodologically solid; RTA below this tier |
| DynaPrompt / CLIP Reward TTA | 6.25-6.67 | R1 | RTA clearly below these accepted papers |

**Bracket**: Round 1 placed the paper between ~3.5 and ~5.5. Round 2 narrowed this — RTA is clearly above the 3.67-4.0 weak-reject anchors and below DOTA (6.00). It is comparable to "Extending to New Domains" (5.33) in creativity but has a more concrete methodological issue (dimensionality mismatch) affecting a significant portion of its experimental evidence. Final placement: **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>