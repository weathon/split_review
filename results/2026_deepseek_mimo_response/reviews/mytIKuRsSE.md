## Summary
This paper introduces Dual-level Noisy Correspondence (DNC) as a practical, under-explored problem in Multi-Modal Entity Alignment (MMEA), where noise exists at both intra-entity (entity-attribute) and inter-graph (entity-entity, attribute-attribute) levels. The authors propose RULE, a framework that estimates correspondence reliability via uncertainty (Dempster-Shafer Theory) and consensus principles, divides pairs into clean/noisy subsets, and applies tailored robust losses during training. A test-time correspondence reasoning (TTR) module uses Qwen2.5-VL-72B with CoT prompting to uncover latent attribute connections. Experiments on 5 benchmarks with 7 baselines under inherent, 20%, and 50% noise settings demonstrate large, consistent improvements.

## Strengths
- **Well-motivated problem formulation with empirical grounding**: The DNC problem is formally defined (Section 2.1) with concrete motivating examples (Elvis Tsui/Jason Momoa, Mr. & Mrs. Smith) and supported by empirical statistics (over 50% DNC in ICEWS benchmarks, Appendix B). This is a genuine gap in the MMEA literature.
- **Comprehensive experimental evaluation**: Tables 1-2 compare against 7 SOTA methods on 5 benchmarks under 3 noise settings. On ICEWS-WIKI Non-name under inherent DNC, RULE achieves 64.2 H@1 vs. the best baseline PMF at 52.6. The training-only variant ("w/o TTR" in Table 3) achieves 56.5 H@1 vs. HHREA at 43.9 under 50% DNC, demonstrating the core training method alone provides large margins.
- **Well-designed ablation study**: Table 3 cleanly decomposes contributions: removing DRL drops H@1 to 31.6; only uncertainty gives 53.5; only consensus gives 48.3; full training model achieves 58.2. Complementarity between uncertainty and consensus is clearly shown.
- **Effective noise-aware pair division with self-adaptive thresholds**: Figure 3(b) shows clean/noisy pairs are well-separated in reliability space, and Figure 4 shows the three subsets (S_U, S_I, S_C) are well-separated in uncertainty-consensus space, confirming the design works as intended.
- **Visualizations confirming module behavior**: Figure 5 shows RULE correctly assigns low reliability to entity-attribute pairs with injected noise while maintaining high reliability for correct attributes.

## Weaknesses

### Fatal
None

### Major
- **TTR module inflates headline results without controlled comparison** — The TTR module uses Qwen2.5-VL-72B-Instruct at inference time while none of the 7 baselines have any comparable MLLM. Tables 1-2 report only the full model as "Ours," but the training-only variant ("w/o TTR" in Table 3) achieves 56.5 vs. 58.2 H@1 on Non-name 50% DNC — already 12.6 points above the best baseline. Presenting only the full model in the main tables overstates the contribution attributable to the proposed training framework. The paper should present "w/o TTR" in Tables 1-2 or augment baselines with the same MLLM. Additionally, computational cost of running a 72B MLLM per candidate at test time is never discussed (confirmed: no mention of efficiency/cost in main text).

- **Circularity in noise estimation unacknowledged** — The consensus principle (Eq. 5: c_i = max(0, s_i · y_i)) uses the potentially noisy annotation y_i, and pair division thresholds (Eq. 8) define S^{TP} = {i | arg max(s_i) = arg max(y_i)} by matching predictions to noisy labels. Using noisy labels to identify which pairs are reliable is circular. The uncertainty principle partially breaks this, and Figure 3(a) shows robustness up to 70% noise, but the paper never acknowledges this circularity or analyzes when it fails.

### Minor
- **Theorem 1 restates standard Dirichlet properties** — The theorem (Eq. 4) states low uncertainty does not guarantee highest belief is on annotated correspondence — a standard property of subjective logic. The paper would benefit from characterizing *when* this failure occurs rather than merely stating it can.
- **Eq. 18 referenced in main text but not present** — Line 310 references "Eq. 18" for the uncertainty-guided loss, but the highest equation in the main text is Eq. 16. The ablation text should include the equation or reference the appendix explicitly.
- **Entity-attribute noise rate not specified** — Line 266 states the 20%/50% figures cover "E-E/A-A pairs" only, but the rate of entity-attribute noise injection is not stated despite being a core part of DNC.

### Trivial
None

## Nice-to-Haves
- Wall-clock comparison of inference with/without TTR for practicality assessment.
- Augmenting a baseline with the same MLLM (e.g., MEAformer + Qwen re-scoring) to isolate training framework contribution vs. MLLM contribution.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Formatting/style nitpicks** — removed per rules (parser artifacts, not author errors).
- **Harsh critic's "Shapley-inspired" naming concern** — demoted to near-trivial: the paper doesn't formally claim Shapley equivalence, just "inspired by" Shapley-type reasoning (Eqs. 6-7). The greedy heuristic is simpler but the naming is only mildly misleading.
- **Strength finder's generic strengths** — partially kept but grounded in specific numbers rather than general praise. Dropped strength "Novel test-time correspondence reasoning module" as it conflicts with the verified Major weakness about TTR fairness.

## Novel Insights
The paper's core novel insight is identifying and formalizing DNC as a dual-level problem in MMEA — previous noisy correspondence work addressed either intra-entity or inter-graph noise but not both simultaneously. The empirical observation that real-world MMEA benchmarks contain >50% noise in ICEWS datasets is consequential and makes the problem practically significant. The demonstration that the training-only variant already substantially outperforms all baselines (13+ points on ICEWS under 50% noise) confirms the robustness approach is genuinely effective rather than relying on the MLLM.

## Suggestions
- Present "w/o TTR" results alongside full model in Tables 1-2, or at minimum discuss the decomposition prominently.
- Add a brief analysis of the circularity in noise estimation and when it might fail.
- Discuss computational cost of the TTR module.
- Include or properly reference Eq. 18 in the main text.
- Specify entity-attribute noise injection rate explicitly.

---

## Calibration Report

### All anchors retrieved:
**Round 1 (bracketing):**
| Path | Avg Score | Round | Band | Comparison |
|------|-----------|-------|------|------------|
| a4O528mek9.md | 3.00 | 1 | Weak | Multimodal representation learning, rejected — our paper is clearly stronger |
| rwdeKOdAwY.md | 3.00 | 1 | Weak | Multimodal retrieval, rejected — our paper clearly stronger |
| 4qRCiEZGKd.md | 3.40 | 1 | Weak | Neural DL reasoning, rejected — unrelated domain, clearly weaker |
| 6PGT9OJX5N.md | 3.00 | 1 | Weak | Noisy data pruning, rejected — different problem, weaker |
| z3dfuRcGAK.md | 6.67 | 1 | Middle | GEEA entity alignment — our paper has more comprehensive evaluation and more novel problem |
| NNUiUwQWx6.md | 5.75 | 1 | Middle | NeuSymEA entity alignment — rejected, our paper is substantially better |
| QQYpgReSRk.md | 6.25 | 1 | Middle | MOFI noisy entity images — different setting, our paper more thorough |
| 5BXWhVbHAK.md | 6.33 | 1 | Middle | Multi-modal synergy — less directly comparable |
| 9Cu8MRmhq2.md | 8.00 | 1 | Strong | Norton noisy correspondence video-language — our paper has TTR fairness issue Norton doesn't |
| TPZRq4FALB.md | 8.00 | 1 | Strong | READ test-time multimodal adaptation — cleaner evaluation design |
| zBbZ2vdLzH.md | 8.00 | 1 | Strong | JDR graph denoising — less directly comparable |
| GGlpykXDCa.md | 8.00 | 1 | Strong | MMQA benchmark — different contribution type |

**Round 2 (narrowing):**
| Path | Avg Score | Round | Band | Comparison |
|------|-----------|-------|------|------------|
| NNUiUwQWx6.md | 5.75 | 2 | Low-narrow | NeuSymEA — our paper clearly better |
| z3dfuRcGAK.md | 6.67 | 2 | Low-narrow | GEEA — our paper has stronger eval, more novel problem |
| ue1Tt3h1VC.md | 6.60 | 2 | Low-narrow | MoMoKE MMKG — our paper more comprehensive, more novel |
| QQYpgReSRk.md | 6.25 | 2 | Low-narrow | MOFI — our paper more thorough |
| 9Cu8MRmhq2.md | 8.00 | 2 | High-narrow | Norton — closest analog; our paper has MLLM fairness concern |
| TPZRq4FALB.md | 8.00 | 2 | High-narrow | READ — cleaner problem and evaluation |
| X1OfiRYCLn.md | 7.50 | 2 | High-narrow | VLB dynamic eval — less directly comparable |
| HnhNRrLPwm.md | 8.00 | 2 | High-narrow | MMIE benchmark — different contribution type |

### Round-1 bracket: 6.5–8.0
### Round-2 narrowing: Paper is clearly better than all 6.x anchors (NeuSymEA 5.75, MOFI 6.25, MoMoKE 6.60, GEEA 6.67) due to more comprehensive evaluation, more novel problem formulation, and stronger empirical results. Paper is below Norton (8.0) and READ (8.0) due to the TTR fairness concern and less clean evaluation design. Score 7.0 sits in the gap, reflecting a solid, accept-worthy paper with one notable comparison issue.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>