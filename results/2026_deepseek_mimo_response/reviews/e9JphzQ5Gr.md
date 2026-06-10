Now let me write the final review with calibration analysis.

---

## Summary
This paper proposes CaPT, an asymmetric-modalities co-training framework that integrates CLIP into semi-supervised learning by jointly training a fully fine-tuned unimodal vision network (UPM) and an adapter-tuned multimodal CLIP model (MPM), connected via entropy-weighted co-pseudo labels. Results span USB benchmarks, ImageNet, extreme one-label-per-class settings, and fine-grained datasets, with particularly large gains under extreme label scarcity (e.g., +21.38% on CIFAR-100 one-shot).

## Strengths
- **Very large performance gaps under extreme label scarcity (Tables 2, 3):** CaPT outperforms the second-best method by 21.38% on CIFAR-100 (82.51% vs. 61.13%) and 4.05% on EuroSAT (96.33% vs. 92.28%) under one-label-per-class. On ImageNet with 10 labels/class, it surpasses RegMixMatch by 9.33% (67.68% vs. 58.35%). These margins substantially exceed typical SSL improvements.
- **Near-negligible computational overhead (Table 4):** Compared to FreeMatch, CaPT adds only 8.00% more memory (5050 vs. 4676 MiB) and 11.18% more training time (0.1044 vs. 0.0939 sec/iter), while being faster and lighter than RegMixMatch. This is achieved through adapter-tuning and feature-level Mixup.
- **Systematic ablation validating each component (Table 6):** Each design choice is isolated with clear performance deltas. The largest drops from removing CLIP or the unimodal network confirm co-training synergy is essential. The CaPT-Deb result (−12.73% on EuroSAT) demonstrates adapter-tuning's role in mitigating CLIP's class bias, corroborated by Figure 5.
- **Comprehensive evaluation (Tables 1–5):** Evaluation spans USB benchmarks, ImageNet, extreme one-shot settings, and six fine-grained datasets, with honest reporting of the FGVCAircraft failure case.

## Weaknesses

### Fatal
None

### Major
- **All main comparisons are against methods without any pretrained VLM:** Every baseline in Tables 1–5 uses only labeled/unlabeled SSL training data with no access to CLIP's 400M+ image-text pretraining. The headline improvements are measured against methods that lack this knowledge. The ablation in Table 6 partially disentangles this ("only MPM" = 68.32%, "only UPM" = 78.60%, CaPT = 84.83% on CIFAR-100), isolating ~6% gain from the co-training mechanism itself—but only on two datasets at one label count. Neither DebiasPL nor CLS appear in the main tables, and the CaPT-Deb ablation conflates multiple design changes (disabling adapter-tuning AND disabling the vision→CLIP flow), making it impossible to isolate what DebiasPL's actual procedure would score. The key question—is the framework design the key driver, or is it mostly CLIP's prior?—cannot be fully answered from the main paper.
- **Missing standard deviations in Tables 2, 3, and 5:** Table 1 reports standard deviations across 3 random seeds, and the text highlights CaPT's "lower standard deviation." However, Tables 2, 3, and 5—containing the paper's most dramatic results—report no standard deviations. This is especially concerning for Table 3 (one-label-per-class), where gains are enormous and the setup is highly variable (sensitivity to which single labeled sample is chosen). Without variance information, the reader cannot assess stability of the 21.38% gap on CIFAR-100.

### Minor
- **Pattern-homogeneity claim supported by qualitative evidence only:** This is presented as a core contribution (abstract, contribution point 2) but supported only by attention maps on 8 images (Figure 3). A quantitative measure such as CKA between UPM and MPM feature spaces would strengthen this significantly.
- **Theoretical contribution is illustrative rather than explanatory:** Theorem 1.1 bounds pseudo-label error under a Gaussian mixture model with nearest-prototype classification, but does not model the actual SSL training loop (iterative pseudo-labeling, consistency regularization, thresholding). It illustrates the label-dependency problem but cannot explain why CaPT specifically helps or provide design guidance.

## Nice-to-Haves
- Report standard deviations in all experimental tables
- Include DebiasPL and/or CLS in main comparison tables (at least CIFAR-100 and one fine-grained dataset)
- Quantify the pattern-homogeneity claim with CKA or feature cosine-similarity
- Briefly acknowledge in the main text that CLIP's prior can be unhelpful on domain-specific datasets (FGVCAircraft)

## Removed Points
These points are flagged to be removed, treat them with caution.
- **Co-pseudo label summing behavior:** The harsh critic flagged Eq. 13's soft label summing, but the paper already addresses this at line 196—low-confidence pseudo labels are replaced with all-zero vectors and the resulting weight is intentionally less than 1. This is a strawman weakness.
- **"Breaks" vs. "reduces" label dependency framing:** This is a minor terminological issue in the title/abstract, not a substantive problem.

## Novel Insights
The paper's genuinely novel insight is that SSL's performance cliff under extreme label scarcity stems from a fundamental coupling where unlabeled data utility is bounded by labeled data quality/quantity, and that an external pretrained VLM can serve as an independent prior to partially decouple this. The asymmetric-modalities co-training design—using adapter-tuning for efficiency and bidirectional flow for mutual improvement—is a well-executed integration strategy. While the empirical demonstration of effectiveness in extreme low-label regimes is convincing and practically valuable, the degree to which the gains come from the co-training mechanism versus simply having CLIP's prior remains partially unresolved by the main experiments.

## Suggestions
- Add DebiasPL and/or CLS as baselines in main comparison tables
- Report standard deviations for all experimental tables
- Add a quantitative metric (CKA, cosine similarity) to the pattern-homogeneity analysis

## Calibration Report

### Anchors Retrieved

**Round 1 (Bracketing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| FwkYeLovHk.md | 3.33 | 1 | Weakly related CLIP work; CaPT is substantially stronger |
| HfJxXbXlYJ.md | 3.00 | 1 | LLM2CLIP rejected paper; CaPT is much stronger |
| E0UsEIRBQ8.md | 3.00 | 1 | Underwater SSL; CaPT is much stronger |
| j1FLTvgyAh.md | 2.50 | 1 | Few-shot CLIP prompting; CaPT is much stronger |
| 97D725GJtQ.md | 5.80 | 1 | SemiCLIP; similar topic, weaker results; CaPT is stronger |
| 1rgMkDWfYV.md | 4.50 | 1 | VLM for label noise; CaPT is stronger |
| ptCIlV24YZ.md | 5.80 | 1 | Image clustering with CLIP; less comparable |
| RgWATMmWmz.md | 4.75 | 1 | Weakly supervised with CLIP; CaPT is stronger |
| 25kAzqzTrz.md | 8.00 | 1 | Theoretical FixMatch analysis; deeper theory, CaPT is weaker theoretically |
| RvUVMjfp8i.md | 8.00 | 1 | SSL in open environments; broader scope, CaPT is weaker |
| PdaPky8MUn.md | 8.00 | 1 | Long-sequence models; less comparable |
| Fk5IzauJ7F.md | 8.00 | 1 | Partial-label learning; less comparable |

**Round 2 (Narrowing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| eSO9quCgmz.md | 5.00 | 2 | Pseudo-labeling data-centric; CaPT is stronger |
| dnqPvUjyRI.md | 6.00 | 2 | SemiReward; good SSL paper, CaPT has larger improvements |
| RgWATMmWmz.md | 4.75 | 2 | Weakly supervised CLIP; CaPT is stronger |
| AEi2wyAMyb.md | 5.33 | 2 | Bi-level SSL optimization; CaPT is stronger |
| rxVBKhyfSo.md | 7.00 | 2 | Selective Mixup fine-tuning; less directly comparable |
| zBgiCWCxJB.md | 6.75 | 2 | SSOLE self-supervised; less directly comparable |
| 85G2t3yklD.md | 6.67 | 2 | DiffMatch; well-motivated SSL with theory, comparable quality |
| Bo6GpQ3B9a.md | 7.00 | 2 | OOD unlabeled data SSL; less directly comparable |

### Bracketing and Calibration
- **Round 1 bracket:** 5.5–7.0. The paper is clearly above weak/medium SSL papers (5.0–5.8 range) but has a meaningful baseline comparison gap vs. the strongest anchors (8.0+).
- **Round 2 narrowing:** CaPT is stronger than SemiReward (6.0) due to larger improvements and more thorough design/ablation, and comparable to DiffMatch (6.67) which also has strong empirical results plus a theoretical component. The baseline gap issue prevents scoring above DiffMatch, but the extremely strong empirical results in low-label regimes and comprehensive evaluation push it above 6.0.
- **Final score: 6.5.** The paper delivers substantial practical value with strong empirical results and a well-designed framework, but the inability to fully isolate the contribution of the co-training mechanism from simply having CLIP's prior—and missing variance reporting on the key tables—prevents a higher score.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>