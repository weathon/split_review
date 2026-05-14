Now I have enough information. Let me compose the final consolidated review.

## Summary
This paper formalizes the All-Day Multi-Scenes Lifelong VLN (AML-VLN) problem and proposes Tucker Adaptation (TuKA), a method that represents multi-hierarchical navigation knowledge (scene and environment) using a 4th-order tensor decomposed via Tucker decomposition. The method decouples knowledge into shared components (core tensor, encoder/decoder) and scenario-specific experts (scene and environment factor matrices), combined with a Decoupled Knowledge Incremental Learning (DKIL) strategy. Extensive experiments on a 24-task benchmark (20 simulation + 4 real-world) show AlldayWalker achieving 65% SR with 11% forgetting rate, consistently outperforming LoRA-based baselines.

## Strengths
- **Principled multi-hierarchical representation via Tucker decomposition**: The paper identifies a genuine limitation of 2D matrix-based adapters (LoRA, HydraLoRA, BranchLoRA) — they cannot naturally decouple knowledge across more than two hierarchies. TuKA addresses this by representing scene and environment knowledge as separate factor matrices of a 4th-order tensor. The ablation shows 4th-order tensor achieves 65% SR vs. 54% for 3rd-order (Table 14), and TuKA outperforms the hierarchical ABC-LoRA baseline (65% vs. 55% SR, Table 15), confirming that the tensor structure itself, not just hierarchical design, drives performance.

- **Strong and consistent empirical results**: AlldayWalker achieves 65% average SR (vs. 56% for the best baseline SD-LoRA) and 11% F-SR (vs. 18%) across all 24 tasks (Tables 1, 2). The advantage holds across SPL, OSR, and their forgetting rates (Figure 7, Tables 18–21). Notably, the gains are achieved with comparable parameter counts (~0.3M trainable parameters, Appendix C), demonstrating genuine efficiency.

- **Comprehensive and well-designed benchmark**: The paper extends Habitat with three physically grounded imaging models (atmospheric scattering, low-light radiometric noise, overexposure saturation) to create realistic degraded environments. The AML-VLN benchmark covers 24 tasks spanning 7 scenes × 4 environments with a randomized task ordering (Table 9), providing a challenging and reproducible evaluation platform.

- **Convincing generalization and scalability evidence**: AlldayWalker achieves 55% average SR on six unseen scenarios (vs. 39–40% for baselines, Table 5) via the expert retrieval mechanism. When extended to 30 tasks (Table 4), performance on the original 24 tasks remains nearly unchanged, demonstrating stability under extended lifelong learning.

- **Careful ablations validating design choices**: The ablation on shared components (Table 3) shows sharing the core tensor (G) and encoder (U²) improves SR from 53–55% to 65%. The rank scaling analysis (Appendix G) shows monotonic improvement with higher expert ranks, providing practical configuration guidance. The fifth-order tensor experiment (Appendix J) demonstrates extensibility to additional knowledge hierarchies.

## Weaknesses

### Fatal
None.

### Major
- **No confidence intervals or variance reporting**: None of the reported metrics include standard deviations, confidence intervals, or results from multiple random seeds. Given that VLN evaluation typically exhibits non-trivial variance (100–150 test episodes per task), the 9% SR improvement over SD-LoRA could benefit from statistical significance verification. This is a non-trivial omission for claims of consistent superiority.

- **The expert retrieval mechanism's robustness is insufficiently characterized**: The CLIP-based retrieval (Section 3.4) uses a single initial observation to select both scene and environment experts. The paper does not analyze failure cases (e.g., when the initial viewpoint is ambiguous) or quantify the gap between retrieval-based selection and oracle task-ID selection. Since retrieval errors cascade into incorrect expert activation, understanding this bottleneck is crucial. The paper would be strengthened by an oracle task-ID upper-bound experiment.

### Minor
- **Notation inconsistency in loss formulation**: The total loss (Equation 9) uses L_sk for the shared knowledge regularization, while Algorithm 1 refers to L_ewc for the same term (line 17 vs. line 20). Additionally, the balance hyper-parameter λ = 1 − (λ₁ + λ₂ + λ₃) imposes a linear constraint that determines the supervision loss weight indirectly, which is an unusual design choice that merits brief discussion.

- **The forgetting rate metric comparison could be more precisely specified**: M-SR_t is defined as "performance obtained when training solely on navigation tasks 1 through t" without clarifying whether this single-task training uses the same total number of training steps as the sequential lifelong setting. While this is standard practice in continual learning, explicit specification would improve reproducibility.

- **The ABC-LoRA comparison, while valid, leaves room for alternative interpretations**: The hierarchical ABC-LoRA baseline (Appendix I) demonstrates that TuKA outperforms a matrix-based hierarchical architecture. However, the paper does not test whether a matrix method with explicit Kronecker product structure (which can model joint interactions) would close the gap. The conclusion that tensor-specific properties drive the gains is supported but not uniquely proven.

### Trivial
- The table formatting in the extracted text is heavily garbled (parser artifact), but the underlying data appears coherent.

## Nice-to-Haves
- A controlled single-scene, single-environment continual learning experiment on a standard VLN benchmark (e.g., R2R-CE) would help isolate the benefits of TuKA beyond the AML-VLN setting
- Visualizing the learned factor matrices (U³ for scenes, U⁴ for environments) to verify whether semantically similar scenes/environments indeed cluster in the embedding space would strengthen the claim of meaningful decoupling
- An oracle task-ID experiment (providing ground-truth scene and environment during inference) would establish the upper bound of the retrieval-based selection

## Removed Points
These points are flagged to be removed; treat them with caution:

1. **"Results are implausible/erroneous due to numerical inconsistencies"** — The harsh critic claimed Seq-FT showing 0% SR on T1 is "impossible." This reflects a misunderstanding: Seq-FT sequentially fine-tunes a single LoRA across all 24 tasks without forgetting prevention, so T1=0% is exactly what catastrophic forgetting predicts. The critic's claim about "0% F-SR on T24 being suspiciously perfect" is likewise wrong — T24 is the last task learned, so comparing to a single-task model just trained on tasks 1–24 naturally yields ~0% forgetting. Negative F-SR values (positive transfer) are a known phenomenon in continual learning. These criticisms are based on misreading garbled table output and misunderstanding continual learning fundamentals.

2. **"Task definition conflates scenes and environments, undermining lifelong learning"** — The critic argued that scenes reappearing with different environments makes this "not a standard continual learning problem." This is precisely the point: the paper studies multi-hierarchical knowledge where the same scene appears under different environments. This is explicitly a feature of the problem formulation, not a flaw. TuKA is designed specifically to handle this structure.

3. **"ABC-LoRA comparison is unfair"** — The critic claimed ABC-LoRA (hierarchical matrix) vs. TuKA (tensor) does not demonstrate tensor advantages. In fact, this comparison directly tests the paper's central claim (tensor > matrix for multi-hierarchical knowledge). The critic's demand for a "Kronecker product structure" baseline is a different comparison that doesn't invalidate the existing one. The paper also explicitly discusses why ABC-LoRA underperforms.

4. **Multiple section-by-section nitpicks (Section 1 "hierarchical matrices" phrasing, Section 3.1 HydraLoRA critique, Section 3.4 "features are not independent," Section 5.1 formatting, Appendix G "diminishing returns contradicts claim")** — These are either misunderstandings of the paper, parser artifacts, or logical errors. Cross-checking with the actual paper text confirms the paper's claims are reasonable.

5. **"Margins are implausibly large" (Section 5.2)** — 9% SR improvement with comparable parameter count is well within what a well-designed task-specific method can achieve over generic baselines.

6. **Strength Finder's generic strengths** — Dropped generic strengths like "addressed an important problem" that lack specificity or conflict with verified weaknesses.

## Novel Insights
The reviews reveal an interesting tension: the harsh critic's most severe criticisms (results are implausible, evaluation is buggy) are all based on misreading garbled parser output and misunderstanding continual learning fundamentals, while the actual substantive concerns (no confidence intervals, expert retrieval robustness) are much milder. This suggests the paper's main weakness is presentation/reproducibility polish rather than methodological flaws. Notably, no reviewer identified a fatal flaw — the core idea of using Tucker decomposition for multi-hierarchical knowledge in VLN is sound and well-executed.

## Suggestions
1. **Add confidence intervals or standard deviations** across multiple evaluation runs for all main tables. This is the single most impactful improvement for strengthening claims.
2. **Include an oracle task-ID experiment** to bound the expert retrieval gap and clarify whether future work should focus on selection or adaptation.
3. **Resolve the notation inconsistency** between L_sk and L_ewc in Equation 9 / Algorithm 1, and clarify the λ constraint rationale.
4. **Briefly discuss why negative F-SR values appear** (positive transfer) to preempt confusion.
5. **Specify whether the single-task reference model (M-SR_t) uses matched training steps** relative to the lifelong procedure.

## Score and Decision

**Calibration anchors (retrieved batch):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| PaYo96rjij (Lifelong Embodied Navigation Learning) | 6.0 | Very similar problem (lifelong VLN with LoRA-based expert decoupling). The current paper has a more principled tensor approach, better benchmark (24 vs 18 tasks), and stronger empirical results. Slightly stronger. |
| pFh5ygjN3V (M³E: Continual VLN via Mixture of Macro/Micro Experts) | 4.5 | Similar domain (continual VLN). Current paper has more comprehensive evaluation and a more novel methodological contribution. Stronger. |
| mp0rPiYHPi (MetaTT: Tensor-Train Adapter) | 5.0 | Similar technique (tensor decomposition for PEFT). Current paper applies it to a more complex, well-motivated problem with stronger empirical gains. Stronger. |
| GK4rznYwhn (DualVLN) | 6.0 | VLN with strong real-world results. Comparable quality but different focus (dual-system vs lifelong learning). Comparable. |
| OyVRrKG8Dj (CogVLN) | 3.0 | Weak VLN paper with inadequate baselines. Current paper is substantially stronger. |
| WLSt5tIOSA (Fine-tuning VLMs Without Forgetting) | 4.0 | Empirical study on forgetting, no new method. Current paper has stronger novelty and contribution. |
| GUNUfIO7hs (Contextual Forgetting) | 3.33 | Weak continual learning paper. Current paper is stronger. |

The paper under review is most similar to PaYo96rjij (avg 6.0) in problem and approach, and slightly surpasses it in methodological novelty (tensor decomposition vs. standard LoRA variants), benchmark comprehensiveness, and empirical thoroughness. The actual weaknesses are minor. The harsh critic's severe allegations are demonstrably incorrect after cross-checking with the paper. The paper makes a solid contribution to an important problem.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>