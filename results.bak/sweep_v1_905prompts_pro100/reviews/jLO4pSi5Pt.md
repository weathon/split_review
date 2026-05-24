Now I have all the information I need. Let me compose the final review.

---

## Summary

This paper introduces L-TTA, the first test-time adaptation method designed specifically for long-tailed distributions in vision-language models (VLMs). The authors identify two failure modes of existing VLM-TTA methods under class imbalance (text-induced tail erosion and modality-bias amplification) and propose a three-component solution: Synergistic Prototypes (combining Deterministic and Exclusionary Prototypes to continuously enrich tail-class representations), learnable Rebalancing Shortcuts with a Class Re-Allocation loss, and Balanced Entropy Minimization — a theoretically grounded variant of entropy minimization that reduces the gradient gap between head and tail classes. The method is evaluated on 15 datasets across OOD, cross-domain, and corruption benchmarks under three imbalance ratios (10, 20, 50), consistently outperforming 12 existing VLM-TTA baselines in both accuracy and macro-F1 while remaining efficient.

## Strengths

- **Novel problem formulation with clearly identified failure modes**: The paper identifies and illustrates two specific, previously unarticulated failure modes of VLM-TTA under long-tailed distributions — text-induced tail erosion and modality-bias amplification (Figure 1). The quantitative evidence in Figure 2 and Table 1 shows existing SOTAs like DPE and SCAP suffering macro-F1 drops of 2–4% as imbalance worsens, directly motivating the need for a dedicated method.

- **Well-designed Synergistic Prototypes with Exclusionary Prototypes (EPs)**: The EP mechanism (§3.2, Eq. 5) updates prototypes for *all classes* using confidence-derived weights, ensuring tail-class prototypes are continuously enriched throughout the datastream. The component ablation (Table 6) demonstrates that removing EPs from SyPs decreases macro-F1 by 3.22–3.95% (ViT-B/16 and RN50), confirming their contribution to tail-class balancing.

- **Learnable Rebalancing Shortcuts with principled Class Re-Allocation loss**: The RS mechanism (§3.2, Eq. 6–7) uses cross-attention over hyper-class vectors with a load-balancing-inspired CRA loss that distributes prototype semantics evenly. Table 6 shows RS adds 5.21pp macro-F1 over plain DPs (RN50), and Figure 4b confirms significant gain from η>0 vs. η=0.

- **Balanced Entropy Minimization with theoretical grounding**: Propositions 1 and 2 (§3.2) formally characterize how standard EM creates a gradient gap between head/tail classes and how BEM reduces it. The penalty term (1−P̃)^β in Eq. 9 is well-motivated, and Figure 4d empirically validates β=1 outperforming extremes by up to 0.85pp macro-F1.

- **Comprehensive empirical validation**: The evaluation spans 15 datasets across three benchmarks (OOD, cross-domain, corruption), three imbalance ratios, and 12 baselines. Consistent gains are shown in both accuracy and macro-F1 — e.g., +1.47% Acc / +1.70% Mac on OOD Average (imb=10), +1.02% Acc / +2.20% Mac on Cross-Domain, +2.87% Acc / +2.64% Mac on Corruption (Table 1–3). The macro-F1 improvements consistently exceed accuracy gains, directly validating the class-balancing claim.

- **Efficiency and scalability**: Table 4 shows L-TTA completes adaptation in 1.45h with 1.89G memory while achieving the best harmonic mean. Table 5 demonstrates consistent gains (~1.5pp Acc, ~1.8pp Mac) across CLIP ViT-L/14, ViT-H/14, SigLIP-L/16, and MetaCLIP-BigG backbones.

- **Robustness to class ordering**: Table 7 shows stable performance when tail-class samples are shifted earlier in the stream (ϵ varied from 0 to 2/3), indicating the method does not overfit to arrival order.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Missing quantitative comparison with unimodal LT-TTA baselines**: The paper motivates its VLM-specific approach partly by arguing that unimodal LT-TTA methods (SAR, DELTA, LAME) degrade when applied to VLMs — a point supported qualitatively in Figure 1(b.2) for SAR. However, no quantitative results for these methods appear in the comparison tables (Tables 1–3). Including adapted versions of SAR/DELTA/LAME on the CLIP backbone would directly validate the claimed "modality-bias amplification" failure mode and strengthen the argument that VLM-specific handling is necessary. The omission does not undermine the core contribution — the comparison against 12 VLM-TTA methods is the right primary evaluation — but leaves a gap between the paper's motivation and its empirical coverage.

- **Hyperparameter tuning concentrated on a single dataset**: All primary hyperparameters (η, λ₁, λ₂, K, β) are set following ablation studies on ImageNet (§4, Implementation Details) and then applied uniformly to all other benchmarks. While TTA precludes per-dataset validation by nature, relying on a single dataset for tuning raises some concern about whether the chosen configuration is genuinely robust or partially benefits from overlap with ImageNet's class structure. This is partially mitigated by the sensitivity analyses for K and β being conducted on both ImageNet and Food101 (Figure 4c,d), but λ₁, λ₂, and η are only studied on ImageNet.

### Trivial

- **Clarity of CRA implementation**: The phrase "notably, before Eq. 6" in the description of the Class Re-Allocation loss (§3.2) is ambiguous — it could be misinterpreted as to which representation the attention scores are computed from. Clarifying this would improve reproducibility.

## Nice-to-Haves

- Including an analysis of the online prior estimation quality in BEM (tracking the relative error between estimated and ground-truth class frequencies over the adaptation stream) would address the natural concern that pseudo-label-based frequency estimation might misguide BEM, especially for late-appearing tail classes.
- A brief summary in the main paper of the 16 additional corruption types tested in Appendix J would give readers a fuller picture of robustness without needing to consult the appendix.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"EPA may blur inter-class distinctions"** (Harsh Critic): The critic speculates that using the same visual embedding for all classes' EP updates could blur distinctions, but acknowledges results suggest this doesn't occur. This is speculative without concrete evidence from the paper — removed.

- **"Number of augmented views differs across methods — fairness concern"** (Harsh Critic): The critic questions whether comparing L-TTA's 15 views against TPT's 63 views is fair. Since L-TTA uses *fewer* views, any asymmetry favors the baselines. The paper also states baselines are run with their own default protocols. Removed — this is not a valid weakness.

- **"Corruption benchmark only uses Gaussian noise — evaluation appears narrow"** (Harsh Critic): The paper explicitly states that results for 16 additional corruption types are in Appendix J. The main paper summarizes one type for conciseness. This is standard practice under space constraints. Removed.

- **"Head/tail accuracy missing from main paper"** (Harsh Critic): The paper explicitly references Appendix C for head/tail accuracy. Removed — the data exists; it's deferred due to space.

- **"First attempt claim is overstated"** (Harsh Critic): The paper claims to be the first to address long-tailed TTA for VLMs — which is accurate. The critic's observation that some prior VLM-TTA methods use prototype mechanisms is true but those methods were neither designed for nor evaluated on long-tailed settings. Removed — the claim is reasonable.

## Novel Insights

The most genuinely novel insight emerging from this work is the identification and formal characterization of how standard entropy minimization creates a *directional* gradient gap between head and tail classes during test-time adaptation (Proposition 1), coupled with the demonstration that this gap can be provably reduced by a confidence-weighted penalty on class priors (Proposition 2, BEM). This formalizes why naive EM is particularly harmful in long-tailed TTA and why simple logit-adjustment approaches from the long-tailed recognition literature may not transfer cleanly to the TTA setting — a subtlety that prior work has not addressed. The Exclusionary Prototypes mechanism (updating all-class prototypes using confidence-derived weights) also represents a non-obvious design choice that inverts the typical prototype-update logic to specifically benefit tail classes.

## Suggestions

- Add quantitative results for at least one adapted unimodal LT-TTA baseline (e.g., SAR on CLIP) on the ImageNet OOD benchmark to close the gap between motivation and empirical coverage. Even a single-row addition to Table 1 would substantiate the modality-bias amplification claim.
- Extend the λ₁, λ₂, and η sensitivity studies to one additional dataset (e.g., Food101 or Caltech101) to demonstrate that ImageNet-tuned hyperparameters remain near-optimal on a different domain — this would substantially strengthen the generality claim at low experimental cost.
- Clarify the "before Eq. 6" phrasing in the CRA loss description to specify exactly which representations the attention scores are computed from.

## Score and Decision

**Evaluation axes**: The paper addresses an original and important research question (long-tailed TTA for VLMs) that is well-motivated by real-world deployment concerns. The claims are well-supported by comprehensive experiments across 15 datasets, 3 imbalance ratios, and 12 baselines. The methodology is sound, with each component validated through ablation studies and the BEM objective supported by theoretical propositions. The writing is clear, and the contribution is of significant value to the TTA and VLM communities.

**Calibration**: Round-1 bracketing placed the paper between approximately 6.0 and 8.0. Round-2 narrowing retrieved anchors at 6.00 (DOTA — rejected, unclear methodology, limited baselines), 6.25 (Multi-Label TTA with BEM — accepted, mixed reviews), 6.75 (Active TTA — accepted), and 7.50 (TCR — accepted, strong cross-modal retrieval TTA). The paper under review is clearly stronger than the 6.0–6.25 anchors (which had substantive methodology concerns and narrower evaluation) and comparable to TCR at 7.50. L-TTA has fewer significant weaknesses than TCR (which faced concerns about hyperparameter sensitivity, reliance on pre-trained models, and batch assumptions) while offering broader evaluation and stronger theoretical grounding. The paper falls slightly below the 8.00 anchors (READ — a more fundamentally novel challenge identification) due to minor evaluative gaps (missing unimodal LT-TTA baselines, single-dataset hyperparameter tuning). Final score: **7.0**.

**Anchor comparison summary**:
| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| DOTA | yD2JMeKumt | 6.00 | R2 | L-TTA is stronger — clearer methodology, more comprehensive evaluation |
| Multi-Label TTA+BEM | 75PhjtbBdr | 6.25 | R2 | L-TTA is stronger — more thorough evaluation, clearer contribution |
| Active TTA (SimATTA) | YHUGlwTzFB | 6.75 | R2 | L-TTA is comparable or slightly stronger — broader evaluation, better ablations |
| TCR | BmG88rONaU | 7.50 | R2 | L-TTA is comparable — fewer methodology concerns, broader evaluation |
| READ | TPZRq4FALB | 8.00 | R1 | L-TTA is weaker — READ identifies a more fundamental new challenge |
| Concept Drift MLLM | b20VK2GnSs | 7.00 | R1 | L-TTA is comparable — similar novelty level and empirical thoroughness |

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>