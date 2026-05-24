Now I have a thorough understanding of the paper and the reviewer claims. Let me synthesize the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me write the review now.

# Review of "Long-Tailed Test-Time Adaptation for Vision-Language Models"

## Summary

This paper introduces L-TTA, a test-time adaptation method for vision-language models (VLMs) explicitly designed to handle long-tailed test distributions. The method comprises three co-designed components: Synergistic Prototypes (SyPs) with Deterministic and Exclusionary prototypes to enrich tail-class representations, Rebalancing Shortcuts (RSs) for learnable cross-modal adaptation, and Balanced Entropy Minimization (BEM) to counter head-class bias during adaptation. Extensive experiments across 15 datasets under multiple imbalance ratios (10, 20, 50), corruption levels, and various backbones show consistent improvements over prior TTA methods in both accuracy and macro-F1.

## Strengths

1. **Comprehensive and convincing empirical evaluation.** The paper evaluates L-TTA across 15 datasets spanning OOD, cross-domain, and corruption benchmarks, at three imbalance ratios (10, 20, 50), using multiple backbones (ViT-B/16, ViT-L/14, ViT-H/14, SigLIP-L/16, MetaCLIP-BigG). Results consistently show L-TTA outperforming a large set of baselines (TPT, C-TPT, TDA, DPE, SCAP, etc.) — for example, on the OOD benchmark at Imb=10, L-TTA achieves 65.97/61.18 (Acc/Mac) vs. the next-best DPE at 64.50/57.57 (Tables 1–3). The cross-domain benchmark improvement is particularly notable in macro-F1 (+2.20% over DPE), supporting the claim of better class balancing.

2. **Well-motivated identification of VLM-specific failure modes.** Section 1 identifies two failure modes specific to long-tailed VLM TTA — Text-induced Tail Erosion and Modality-bias Amplification — with concrete illustrative examples (Figure 1b). The three components of L-TTA are directly motivated by these failure modes, giving the method a clear design rationale rather than being an ad hoc combination of techniques.

3. **Clean ablation study confirming synergistic contribution of all components.** Table 6 systematically ablates each component: removing DPs or EPs from SyPs drops macro-F1 by 3.95%/3.22%, removing RS degrades macro-F1 from 65.17 to 63.40, and replacing BEM with standard EM drops macro-F1 from 65.83 to 65.17. This provides clear evidence that all three components contribute positively.

4. **Competitive efficiency with strong performance.** Table 4 shows L-TTA completes in 1.45h with 1.89G memory on ImageNet, achieving the highest harmonic mean on both LT-CDB (67.20) and LT-CB (46.08), while slower methods like RLCF (18.30h) and WATT (27.70h) underperform or fail.

## Weaknesses

### Major

- **Overclaimed novelty framing.** The paper states "we first study Test-Time Adaptation under long-tailed scenarios" and "the first TTA for long-tailed settings" (Section 1). However, prior work like DELTA (Zhao et al., 2023a) explicitly addresses class bias in TTA via reweighting, and the label-shift TTA literature (importance weighting, reweighted entropy minimization) is relevant. The paper does acknowledge DELTA in the related work but the "first" claim is not sufficiently qualified. The contribution is better framed as "first to address long-tailed distributions specifically for VLMs with bi-modal adaptation," which would be accurate and still significant. This overclaim weakens the paper's otherwise solid positioning.

- **The BEM vs. standard EM comparison shows only modest gains.** In Table 6, the improvement from replacing standard EM with BEM (SyP+RS vs. SyP+RS+BEM) is 0.36% accuracy and 0.66% macro-F1. While the ablation is clean and the improvement is consistent, this modest gain raises the question of whether BEM's additional complexity (the penalty term and class prior estimation) is justified relative to simpler alternatives like temperature scaling or post-hoc logit adjustment. The paper does not compare against a simple class-weighted EM baseline (e.g., minimizing \(\sum_c \pi_c^{-1} p_c \log p_c\)), which would establish whether BEM's specific design is necessary.

### Minor

- **Pseudo-label-driven prior update creates an unanalyzed feedback loop.** The class prior \(\pi\) in BEM (Eq. 9) is "continually updated based on the current predicted pseudo-labels." In a long-tailed setting where the model is initially biased toward head classes, pseudo-labels for tail classes may be unreliable, potentially causing the prior to reflect model bias rather than the true distribution. The paper does not analyze whether this feedback loop amplifies early errors. An oracle-prior comparison (using ground-truth class counts) would cleanly separate this concern.

- **No standard deviations or error bars in main tables.** The paper reports "5 runs" as a note but does not include standard deviations in Tables 1–3. Given that many improvements over the next-best baseline are 1–2% in macro-F1, variance information is essential to assess statistical significance. This is fixable without additional experiments.

- **The notation in Eq. 9 is ambiguous and could mislead readers.** The equation writes \(z' = z - (1 - \tilde{\mathbb{P}})^\beta \log(\pi / \sum_i \pi_i)\) without explicitly defining \(\tilde{\mathbb{P}}\). While the intended reading (\(\tilde{\mathbb{P}} = \sigma(z)\), the original softmax) is clear from context, explicitly defining this would prevent implementation errors. The critic's concern about circular dependency is unfounded (there is no circularity if \(\tilde{\mathbb{P}}\) is taken as \(\sigma(z)\)), but the presentation should be tightened.

- **The theoretical propositions are loosely connected to practical behavior.** Proposition 1 (EM biases head classes) is essentially a formal restatement that if head classes have larger logits, their gradients push toward higher confidence — which follows from the softmax/entropy structure. Proposition 2's gradient gap metric (Eq. 10) is an unusual quantity, and it's not shown that shrinking this gap translates to better classification. A simple empirical demonstration (e.g., tracking the gradient gap across the test stream for EM vs. BEM) would bridge the theory to practice.

### Trivial

- None

## Nice-to-Haves

- A direct comparison between BEM and a simple class-weighted EM baseline (e.g., \(\sum_c \pi_c^{-1} p_c \log p_c\)) would better isolate the value of BEM's specific penalty design.
- An oracle-prior experiment (using ground-truth class counts vs. estimated priors) would strengthen the analysis of the pseudo-label feedback loop.
- Including standard deviations in all main results tables.

## Removed Points

The following points from the input reviews were removed with justification:

1. **"BEM formulation has a circular dependency that undermines reproducibility"** — REMOVED as factually incorrect. The intended reading (\(\tilde{\mathbb{P}} = \sigma(z)\), the original softmax) yields a straightforward two-step computation with no circularity. The notation is slightly ambiguous but not structurally flawed.

2. **"The paper does not directly compare BEM to standard EM while keeping SyPs and RSs fixed"** — REMOVED as factually incorrect. Table 6 compares SyP(DP+EP)+RS (standard EM) with SyP+RS+BEM, which is exactly this comparison.

3. **"The problem framing oversells novelty relative to existing label-shift TTA literature"** — MERGED into a qualified overclaim weakness. The paper does acknowledge DELTA, and the VLM-specific framing is legitimate. The claim is retained as a qualified overclaim rather than a dismissal.

4. **"Long-tailed dataset construction may create uncontrolled variables"** — REMOVED as overly nitpicky. The construction rule ("if calculated cardinality is less than class cardinality, keep unchanged") is clearly stated and is a standard approach to avoid artificially inflating small classes.

5. **"Number of augmented views (Q=15) needs justification"** — REMOVED as too minor to warrant inclusion. The value is within the range used by prior work and is ablated in practice.

6. **"Analysis of prototype quality over time"** — MOVED to nice-to-have. It would strengthen the paper but is not a core weakness.

7. Various generic "missing related works" and formatting/style nitpicks — REMOVED per filtering rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Reframe the novelty claims to "first VLM-specific TTA for long-tailed distributions" (or similar) to avoid overclaim relative to the label-shift TTA literature.
- Add standard deviations to all main result tables — this is the most impactful single fix for the paper's credibility.
- Add a simple oracle-prior comparison experiment to address the pseudo-label feedback loop concern.
- Add a comparison with a class-weighted EM baseline (\(\sum_c \pi_c^{-1} p_c \log p_c\)) to better contextualize BEM's gains.
- Explicitly define \(\tilde{\mathbb{P}} = \sigma(z)\) in Eq. 9 to eliminate notational ambiguity.

## Score and Decision

Now let me do the calibration to position the score properly.

**Round 1 — Bracketing:** I identified that the paper is clearly stronger than the weak anchors (avg ~2.5, clearly reject papers with fatal flaws) and not as specialized/novel as the strong anchors (avg ~8.0, which are paradigm-shifting or analytical contributions). The plausible bracket is [4.5, 7.0].

**Round 2 — Narrowing:** I examined four anchors in the 4.5–7.5 range:
- BaFTA (avg 5.50, Reject): weaker experiments, no long-tailed setting, novelty questioned. This paper is stronger.
- BAT-CLIP (avg 5.50, Reject): some reviewers flagged fatal protocol issues (ground-truth label leakage). This paper is clearly stronger.
- DOTA (avg 6.00, Reject but all 6s): similar prototype-based TTA, narrower evaluation. This paper is comparably thorough but broader in scope.
- RLCF (avg 6.67, Accept): broader in task scope (classification, retrieval, captioning) but similar evaluation depth.

The paper under review is stronger than the 5.5-range papers and comparable to DOTA (6.0). It does not reach the 7+ level due to the overclaimed novelty framing, modest BEM gains, and missing statistical reporting. The most appropriate position is near DOTA/RLCF — slightly above DOTA due to more comprehensive evaluation but below RLCF due to narrower task scope.

**Anchors retrieved:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| pdzHpQbGrn (Active TPT) | 2.50 | 1 | Much weaker; has fatal protocol issues |
| JIlIYIHMuv (LVLM-CL) | 2.50 | 1 | Much weaker; different setting |
| ZaudLwn0Hm (Prototypical evolution) | 2.50 | 1 | Much weaker; different setting |
| gNoqEdT2wO (Multimodal CIL) | 2.33 | 1 | Much weaker; different setting |
| eXrUdcxfCw (Continual TTA prototypes) | 4.80 | 2 | Weaker; marginal gains, limited novelty |
| lF9QXpfNHm (ROSITA) | 4.67 | 2 | Weaker; limited experiments, incremental |
| yD2JMeKumt (DOTA) | 6.00 | 2 | Comparable; less thorough evaluation |
| NeVbEYW4tp (Self-TPT) | 5.00 | 2 | Weaker; narrower scope, questionable novelty |
| x6u2BQ7xcq (Tag2Text) | 5.60 | 2 | Different topic (pre-training, not TTA) |
| KNtcoAM5Gy (BaFTA) | 5.50 | 2 | Weaker; simpler method, less thorough |
| z7PhIgVmZU (BAT-CLIP) | 5.50 | 2 | Weaker; had fatal evaluation concerns |
| 2y8XnaIiB8 (VL dataset distillation) | 5.50 | 2 | Different topic |
| b20VK2GnSs (Concept drift MLLM) | 7.00 | 2 | Stronger; different setting/framing |
| cpGPPLLYYx (VL-ICL Bench) | 6.50 | 2 | Different topic |
| kIP0duasBb (RLCF) | 6.67 | 2 | Stronger in task scope, comparable in eval |
| 75PhjtbBdr (Multi-label TTA BEM) | 6.25 | 2 | Related but different problem (multi-label) |

**Final score determination:** The paper sits slightly above BaFTA/BAT-CLIP (5.5) and DOTA (6.0) due to its more comprehensive evaluation and well-motivated design, but below RLCF (6.67) and the 7+ range. The overclaimed novelty framing, missing error bars, and modest BEM gain prevent a higher score. Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>