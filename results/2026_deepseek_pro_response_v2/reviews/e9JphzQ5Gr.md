Now let me finalize the review with the calibrated score. Let me summarize the calibration:

**Round 1 — Bracketing:**
- Weak anchors (< 3.5): CLIP-based few-shot/adaptation papers at 2.50–3.33
- Middle anchors (3.5–7.5): SemiCLIP (5.80), CLIPSelector (4.50), DOTA (6.00)
- Strong anchors (> 7.5): FixMatch Theory (8.00), CLIP interpretability papers (8.00)
- **Bracket: 6.0–7.5**

**Round 2 — Narrowing:**
- DiffMatch (6.67): SSL segmentation method — CaPT is comparable or slightly stronger
- SelMix (7.00): selective mixup fine-tuning — CaPT is comparable
- PLENCH (7.50): PLL benchmark with theory — CaPT is slightly below
- Dataset Distillation via KD (7.00): different area, comparable quality

**Final score: 7.0** — CaPT is a solid accept with strong empirical results across broad benchmarks, practical efficiency, and good motivation. The evidential gaps (missing CLS baseline, no variance on headline 1-label results) and somewhat overstated framing prevent it from reaching the 7.5–8.0 tier, but the paper's contribution is genuine and well-supported.

---

## Summary

This paper identifies a label-dependency problem in semi-supervised learning: when labeled data is scarce or low-quality, pseudo-label accuracy collapses and unlabeled data stops helping. The authors motivate this empirically (Figure 1, covering quantity, quality, and diminishing returns) and theoretically (Theorem 1.1 under a Gaussian mixture model). Their solution, CaPT, is an asymmetric-modalities co-training framework that pairs a fully fine-tuned unimodal network with an adapter-tuned CLIP model, exchanging supervision through entropy-weighted co-pseudo labels. CaPT achieves state-of-the-art results across USB, ImageNet, fine-grained benchmarks, and extreme low-label settings, with particularly large gains at 1 label per class (e.g., +21.38 pp over the next best method on CIFAR-100).

## Strengths

- **Compelling empirical motivation (Figure 1):** The three-panel demonstration—quantity (accuracy vs. labels/class), quality (prototypicality radar chart), and diminishing returns from unlabeled data (heatmap)—provides clear, concrete evidence for the label-dependency problem. This goes beyond typical motivating figures by covering multiple dimensions of the phenomenon.

- **Practical and efficient design:** CaPT achieves strong gains while adding only 8% memory overhead and 11% training time vs. FreeMatch (Table 4), and is more efficient than the current SOTA RegMixMatch. The use of feature-space Mixup (Eq. 9) and adapter-tuning (Eq. 6–7) is well-motivated by computational constraints.

- **Comprehensive experimental validation:** Results span USB benchmarks (Table 1, 12 baselines, 3 datasets, 6 label settings), ImageNet (Table 2), extreme 1-label/class settings (Table 3), and 6 fine-grained datasets (Table 5). The fine-grained experiments directly address the concern that CLIP-based methods may benefit from test-set leakage on standard benchmarks.

- **Systematic ablation study (Table 6):** Seven ablations (CaPT-Ada, CaPT-Deb, CaPT-Uni, only UPM, only MPM, w/o feat aug, equal weights) systematically validate each component's contribution, showing measurable impact from every design choice.

## Weaknesses

### Fatal
None.

### Major

- **The asymmetric-modalities claim lacks a direct baseline.** The paper argues that CaPT's asymmetric design mitigates the "pattern-homogeneity bottleneck" of symmetric co-training (contribution #2, Section 1 line 51; abstract). CLS (Yao et al., 2022) is discussed as the representative symmetric co-training method but is never run as a baseline. The attention-map evidence in Figure 3 is suggestive but compares a CLIP-pretrained ViT against two randomly initialized ViTs, conflating pretraining with modality difference. The CaPT-Uni ablation (removing bidirectional flow) and "only UPM" ablation (removing CLIP) provide partial evidence but do not isolate the asymmetry claim from CLIP's prior knowledge. This is a significant evidential gap for one of the paper's two stated contributions.

- **No variance reported on headline 1-label and ImageNet results.** Table 3 (1 label/class) and Table 2 (ImageNet) report point estimates without standard deviations, inconsistent with Table 1 which reports ± values from three seeds. With only one labeled sample per class, the random choice of *which* sample is labeled can produce large swings in accuracy—a fact the paper itself demonstrates in Figure 1a (radar chart). Without variance reporting, readers cannot assess whether the 21.38 pp gain on CIFAR-100 at 1 label/class is robust or partly an artifact of favorable labeled-sample draws.

### Minor

- **Theorem 1.1 is motivational only—it does not analyze CaPT.** The bound operates on a nearest-prototype classifier under a Gaussian mixture model that shares no structure with CaPT. The paper frames this honestly as motivational, but the abstract and introduction's emphasis on theoretical establishment somewhat overstates the depth of the theoretical contribution relative to the method.

- **"Breaking" label dependency overstates the contribution.** CaPT demonstrably *reduces* label dependency, but does not eliminate it. The method still requires labeled data, and the only-MPM ablation (Table 6: 68.32% vs. 78.60% on CIFAR-100 with 2 labels) shows CaPT without the unimodal network performs worse than standard SSL.

- **STL-10 results show CaPT underperforming adapter-tuned CLIP.** CaPT achieves 96.07% (4 labels) and 96.34% (10 labels) on STL-10, while adapter-tuned CLIP alone achieves 96.86% and 97.15% (Table 1). This edge case—where CLIP's prior is already near-perfect and co-training adds noise—is not discussed.

- **Narrow ablation scope.** Table 6 ablates on only two datasets (CIFAR-100, EuroSAT) at 2 labels/class. Extending key ablations to the 1-label setting would directly connect the ablation story to the headline result.

- **FGVCAircraft failure under-analyzed.** CaPT loses to FreeMatch and RegMixMatch on FGVCAircraft (Table 5). The explanation—"CLIP's prior is less informative"—is asserted without supporting analysis.

### Trivial
None.

## Nice-to-Haves
- A CKA or centered kernel alignment analysis quantifying representation dissimilarity between unimodal and multimodal branches would strengthen the pattern-homogeneity argument beyond qualitative attention maps.
- Breaking down CaPT's gains by correlation with CLIP zero-shot accuracy per class would give practitioners actionable guidance on where to deploy the method.
- Running multiple random draws of the single labeled sample in the 1-label setting would directly address variance concerns.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"No direct DebiasPL comparison" (Harsh Critic):** The CaPT-Deb variant serves as a reasonable proxy for DebiasPL's strategy, and Figure 2 explicitly contrasts the approaches conceptually. Running full DebiasPL would be a nice-to-have, not a weakness requiring remedy.
- **"Zeroed pseudo-labels may not sum to 1" (Harsh Critic):** The paper explicitly discusses this mechanism at line 196 as a deliberate design choice to reduce confirmation bias. The critic speculates about gradient behavior without evidence of problems.
- **"Feature-space Mixup produces non-real representations" (Harsh Critic):** This is a well-established technique (manifold Mixup, Verma et al. 2019), not a paper-specific concern.
- **"The paper would benefit from analyzing when CLIP's prior is most valuable" (Harsh Critic):** Already captured in Nice-to-Haves.
- **"Missing appendices" or "appendix-deferred proofs" (Harsh Critic):** The parser strips appendices; these exist in the original submission.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Add the CLS (symmetric co-training) baseline on at least one dataset/label setting, or temper the asymmetric-modalities claim to focus on CLIP integration rather than the co-training structure advantage.
- Report variance (mean ± std across multiple labeled-sample draws and seeds) for the 1-label/class experiments in Table 3 and for ImageNet in Table 2.
- Discuss the STL-10 result where CaPT underperforms adapter-tuned CLIP, clarifying when the co-training framework adds value vs. noise.
- Replace "breaking" with "reducing" or "mitigating" in the title and throughout the paper.

## Calibration Summary

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| SemiCLIP (97D725GJtQ) | 5.80 | R1 | CaPT is clearly stronger: broader experiments, more dramatic gains, better ablation |
| CLIPSelector (1rgMkDWfYV) | 4.50 | R1 | CaPT is much stronger |
| DOTA (yD2JMeKumt) | 6.00 | R2 | CaPT is stronger |
| DiffMatch (85G2t3yklD) | 6.67 | R2 | CaPT is comparable; broader classification scope vs. segmentation focus |
| SelMix (rxVBKhyfSo) | 7.00 | R2 | Both method papers with practical contributions; CaPT has broader experiments, SelMix has more theory |
| SSOLE (zBgiCWCxJB) | 6.75 | R2 | Different area (self-supervised representation learning) |
| Dataset Distillation via KD (c61unr33XA) | 7.00 | R2 | Different area; comparable quality |
| PLENCH (FtX6oAW7Dd) | 7.50 | R2 | CaPT slightly below: PLENCH has stronger theory + community benchmark value |
| FixMatch Theory (25kAzqzTrz) | 8.00 | R1 | CaPT is below: FixMatch paper provides foundational theoretical insights |

**Round 1 bracket:** 6.0–7.5. **Round 2 narrowing:** CaPT is comparable to SelMix (7.00) and DiffMatch (6.67), below PLENCH (7.50). Final score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>