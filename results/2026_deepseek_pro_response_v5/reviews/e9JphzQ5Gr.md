Now I have a solid calibration picture. Let me compose the final review.

**Round 1 Bracket:** 5.0 – 7.0  
**Round 2 Narrowing:** CaPT sits above SimE (5.25, rejected for limited novelty and narrow eval), comparable to SemiCLIP (5.80, accepted with similar SSL+CLIP contribution and novelty concerns), and below C-CLIP (6.50, accepted with cleaner methodology and fewer missing-baseline issues). The missing adapter-tuned CLIP baselines in Tables 3/5 and the undiscussed STL-10 result pull CaPT below the 6.0 line.

**Final Score: 5.5**

---

## Summary
CaPT proposes an asymmetric-modalities co-training framework that integrates CLIP into semi-supervised learning by pairing a fully fine-tuned unimodal ViT with an adapter-tuned multimodal CLIP model, exchanging supervision through entropy-weighted co-pseudo labels. The paper identifies that standard SSL degrades sharply under extreme label scarcity and demonstrates that CaPT substantially outperforms existing SSL methods — notably by 21.38% on CIFAR-100 at 1 label/class. The method is well-ablated and efficiency-conscious (feature-level Mixup avoids costly CLIP re-encoding).

## Strengths
- **Compelling empirical results in extreme low-label regimes**: Table 3 shows CaPT achieving 82.51% on CIFAR-100 at 1 label/class vs. 61.13% (FreeMatch) and 60.49% (RegMixMatch) — a 21.38 percentage-point margin. On EuroSAT at 1 label/class, CaPT reaches 96.33% (+4.05% over the second-best). These are substantial, well-documented gains.
- **Novel asymmetric-modalities co-training design**: The core insight — pairing a pure-vision ViT with a CLIP model whose textual context drives qualitatively different attention patterns — is genuinely novel for SSL co-training. Figure 3 provides visual evidence that CLIP and unimodal ViTs attend to different image regions. The CaPT-Uni ablation (Table 6) confirms removing bidirectional flow degrades performance (−0.88 on CIFAR-100, −1.49 on EuroSAT).
- **Thorough ablation study**: Table 6 cleanly ablates every major component: co-training variants (CaPT-Ada, CaPT-Deb, CaPT-Uni), individual module contributions (only UPM, only MPM), feature-augmented consistency regularization, and entropy-based weighting. Each ablation shows a measurable drop, validating the design.
- **Efficiency-conscious engineering**: Feature-level Mixup (Eq. 9) avoids re-feeding high-resolution images through CLIP's frozen encoder. Table 4 confirms the claim: CaPT uses only 8% more memory and 11% more training time than FreeMatch while being cheaper than RegMixMatch in both dimensions.
- **Transparent reporting of CLIP baselines in Table 1**: The paper includes both zero-shot CLIP and adapter-tuned CLIP alongside the main results, giving readers the raw data needed to assess CLIP's standalone contribution.

## Weaknesses

### Fatal
None.

### Major
- **Missing adapter-tuned CLIP baselines in key experimental settings**: Table 3 (1-label-per-class) compares CaPT only against FreeMatch and RegMixMatch, neither of which uses CLIP. Table 5 (fine-grained datasets) reports zero-shot CLIP but not adapter-tuned CLIP. These are precisely the settings where the paper makes its strongest claims about CaPT's value. Without adapter-tuned CLIP baselines, the reader cannot determine how much of CaPT's gain comes from the co-training framework versus simply adapter-tuning CLIP on the labeled + unlabeled data. Given that adapter-tuned CLIP already achieves 74.90% on CIFAR-100 at 2 labels (Table 1), these missing baselines leave a significant evidentiary gap in the paper's headline settings.
- **The STL-10 result where adapter-tuned CLIP outperforms CaPT is undiscussed**: Table 1 shows adapter-tuned CLIP achieves 96.86% (4 labels/class) and 97.15% (10 labels/class) on STL-10, both exceeding CaPT's 96.07% and 96.34%. Additionally, zero-shot CLIP reaches 97.18%. Yet the discussion (line 210) claims CaPT "leads in all 6 commonly used evaluation settings" and highlights a "6.18% improvement over RegMixMatch" without acknowledging that a simpler baseline — adapter-tuned CLIP alone — actually achieves higher accuracy. This selective framing undermines the narrative that CaPT's full co-training framework is always the right approach for integrating CLIP into SSL.
- **Theorem 1.1 is disconnected from the method design**: The theorem formalizes that pseudo-label error degrades with fewer or less prototypical labeled samples under a Gaussian-mixture model. While competently executed, it does not constrain, validate, or guide any specific design choice in CaPT. The conclusion — "we need mechanisms for utilizing unlabeled data that do not depend exclusively on labeled data" — leads to "use CLIP," which is an independent design choice not derived from the theorem's structure. The paper would lose no technical content if the theorem were removed.

### Minor
- **Bolding convention in Table 1 is inconsistent with the data**: The header states "The best results are highlighted with Bold," yet adapter-tuned CLIP achieves the highest numbers on STL-10 (96.86% and 97.15%) and is not bolded, while CaPT is bolded at lower values (96.07% and 96.34%).
- **Discrepancy between "only MPM" ablation and standalone adapter-tuned CLIP results**: Table 6 reports "only MPM" at 68.32% on CIFAR-100 (2 labels), while Table 1 reports standalone adapter-tuned CLIP at 74.90% on the same setting. This 6.58% gap is not explained, making it unclear whether the ablation isolates the intended variable.
- **Qualitative-only attention map analysis**: Figure 3's claim that asymmetric modalities "mitigate the pattern-homogeneity bottleneck" is supported only by visual inspection. A quantitative metric (e.g., CKA or mutual information between the two models' representations) would strengthen this claim.

### Trivial
None.

## Nice-to-Haves
- A characterization of *when* CaPT's co-training adds value over adapter-tuned CLIP alone. The STL-10 result is actually informative: when CLIP already has strong zero-shot performance on a domain, co-training with a unimodal network may not help. Analyzing this boundary condition would deepen the paper.
- A baseline that uses CLIP visual features in a standard SSL pipeline (e.g., FreeMatch with a frozen CLIP encoder + trainable head) to better isolate whether gains come from the co-training framework or from CLIP's representations.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **HC: "The paper conflates access to external knowledge with advances in SSL methodology" (structural)** — This is a framing critique, not a technical flaw. The paper is transparent about using CLIP and does not claim to advance SSL methodology without external models. The concern about framing overreach is captured in the STL-10 discussion weakness above.
- **HC: "No statistical significance tests"** — Standard deviations across 3 random seeds are reported in Table 1, which is standard practice in the SSL literature.
- **HC: "No evidence for portability claim / missing CLIP variant experiment"** — The paper references Appendices N and L for portability experiments. Per review rules, stripped appendix content is not flagged as missing.
- **HC: "Confidence threshold mechanism is under-specified"** — Section 4.1 explicitly states: "We adopt the adaptive threshold strategy from FreeMatch to filter pseudo labels, as in RegMixMatch." This is specified.
- **HC: "CaPT-Uni ablation contradicts STL-10 result"** — The "only MPM" ablation runs within the CaPT training framework, which differs from standalone adapter-tuned CLIP evaluation. The STL-10 concern is already captured as a Major weakness above.
- **SF: "Theorem 1.1 provides novel formal bound" as a standalone strength** — The theorem is mathematically sound but disconnected from the method. Its weight as a strength is reduced; the formalization has value as part of the empirical-theoretical narrative but is not listed as an independent strength.

## Novel Insights
The paper's attention map analysis (Figure 3) offers a genuinely instructive observation: unimodal ViTs with different initializations converge to similar representational patterns, while CLIP's textual context drives attention to qualitatively different image regions. This provides empirical grounding for the claim that co-training benefits from view independence, and specifically identifies *modality asymmetry* as a mechanism for achieving it — an insight that extends beyond SSL to co-training more broadly.

## Suggestions
- Add adapter-tuned CLIP baselines to Tables 3 and 5. If the numbers are worse than CaPT (as the Table 1 gap on CIFAR-100 suggests), this will strengthen rather than weaken the paper.
- Acknowledge and discuss the STL-10 case where adapter-tuned CLIP alone beats CaPT. This is informative and could lead to a more nuanced claim about when CaPT is most beneficial.
- Either connect Theorem 1.1 to a specific design choice in CaPT, or move it to the appendix and shorten the theoretical exposition. The empirical motivation (Figure 1) is sufficient to justify the method.
- Add a quantitative metric to the attention map analysis to strengthen the pattern-homogeneity claim.

## Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| SelfPrompt (XCg9YcSKCZ) | 3.50 | 1 | Weaker — rejected for novelty + problem-setting issues more severe than CaPT's |
| WSFT (RgWATMmWmz) | 4.75 | 1 | Weaker — similar missing-baseline concerns but less dramatic empirical results |
| SimE (rkAqvDnnmO) | 5.25 | 2 | Weaker — rejected for limited novelty, narrow eval scope; CaPT has broader eval and more novel design |
| SemiCLIP (97D725GJtQ) | 5.80 | 1,2 | Comparable — accepted SSL+CLIP paper with novelty concerns; CaPT has stronger empirical gains but the missing-baseline + STL-10 issues |
| BAT-CLIP (z7PhIgVmZU) | 5.50 | 2 | Comparable — rejected bimodal CLIP adaptation paper |
| C-CLIP (sb7qHFYwBc) | 6.50 | 2 | Stronger — accepted with cleaner evaluation, fewer missing-baseline issues, better theoretical grounding |
| CLIPSelf (DjzvJCRsVf) | 7.00 | 1 | Stronger — accepted with deeper analysis and stronger methodology |
| Why FixMatch (25kAzqzTrz) | 8.00 | 1 | Much stronger — genuine theoretical depth directly guiding method design |

**Bracket:** 5.0 – 7.0 (Round 1) → narrowed to 5.0 – 6.5 (Round 2). CaPT sits between SemiCLIP (5.80) and SimE (5.25), with the missing-baseline issues pulling it slightly below SemiCLIP.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>