Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper formalizes the all-day multi-scenes lifelong VLN (AML-VLN) problem, where agents must continually adapt across diverse scenes and environmental conditions (normal, low-light, overexposure, scattering) without catastrophic forgetting. To address this, the authors propose **Tucker Adaptation (TuKA)**, a parameter-efficient fine-tuning method that represents multi-hierarchical navigation knowledge as a 4th-order tensor and uses Tucker decomposition to decouple it into shared subspaces (core tensor, encoder, decoder) and separate scene/environment expert factors. A Decoupled Knowledge Incremental Learning (DKIL) strategy consolidates shared knowledge while constraining task-specific experts. Built on TuKA, the **AllDayWalker** agent is evaluated on a 24-task benchmark (5 simulation scenes × 4 environments + 2 real-world scenes) and achieves an average SR of 65% with only 11% forgetting rate, outperforming matrix-based LoRA variants (SD-LoRA: 52% SR, 18% forgetting; BranchLoRA: 44% SR, 36% forgetting) by substantial margins.

## Strengths

- **Novel high-order tensor adaptation for multi-hierarchical knowledge decoupling.** The paper introduces Tucker decomposition to PEFT for VLN, which is a genuine methodological innovation. By representing scene and environment knowledge in separate factor matrices (U³, U⁴) connected through a shared core tensor (𝒢), TuKA explicitly decouples knowledge hierarchies that matrix-based LoRA variants cannot capture. The ablation in Figure 8 confirms that the 4th-order (decoupled) form outperforms a 3rd-order (coupled) form across all 20 tasks, often by 15–30 SR points, using *fewer* total expert parameters (704 vs. 2,560).

- **Consistent and large-margin improvements over 12+ baselines.** On the 24-task AML-VLN benchmark, AllDayWalker achieves an average SR of 65% vs. 52% for the best baseline SD-LoRA (Table 1), with an average forgetting rate of just 11% vs. 18% for SD-LoRA and 36% for BranchLoRA (Table 2). The advantage is not marginal — it holds across nearly every individual task and across all metrics (SR, SPL, OSR).

- **Strong generalization to unseen scenarios without retraining.** In Table 5, AllDayWalker achieves 55% average SR on six completely unseen tasks (four novel simulation scenes + two real-world scenes), outperforming BranchLoRA (40%) and SD-LoRA (39%) by ~15%. This demonstrates that the decoupled expert structure with retrieval-based matching (Section 3.4) transfers to novel scene–environment combinations, a capability absent in prior methods.

- **Stability under task scaling.** Table 4 shows that scaling from 24 to 30 tasks causes only negligible degradation on original tasks (e.g., T1: 79→77, T7: 87→86) and the average SR drops only ~2%, validating that the DKIL strategy successfully mitigates catastrophic forgetting as the number of scenarios grows.

## Weaknesses

### Fatal
None.

### Major

- **Unexplained negative forgetting rates and unclear M-SR_t oracle computation.** In Table 2, AllDayWalker shows negative F-SR values on tasks T14 (-3%) and T20 (-4%). The forgetting rate is defined as F-SR_t = (M-SR_t − SR_t)/M-SR_t, where M-SR_t is the joint-training oracle. A negative value implies the sequential lifelong model *outperforms* joint training on those tasks. While small negative values are not logically impossible — joint training on imbalanced multi-task data can be suboptimal for individual tasks — the paper provides no discussion of why this occurs or how M-SR_t is computed (training epochs, learning rate, data mixing strategy, number of runs). The definition also notes "t ≤ 20" while the table reports values up to T24, creating ambiguity. Since the core claim of the paper is mitigating catastrophic forgetting, the validity of the oracle directly affects the credibility of the forgetting-rate comparisons. The authors must clarify the M-SR_t computation protocol.

### Minor

- **Asymmetric comparison due to expert retrieval mechanism.** TuKA's inference procedure (Section 3.4) stores CLIP vision features for each scene and environment during training, then selects the best-matching experts via cosine similarity at test time. The baselines (HydraLoRA, BranchLoRA, SD-LoRA, etc.) use learned routing or averaging over all K experts but do not have access to an equivalent retrieval-based selection. This gives TuKA an additional memory-based classification step that is not a direct consequence of the tensor decomposition. While the retrieval mechanism is a legitimate design choice, its contribution should be isolated: an ablation with random expert selection, or equipping baselines with the same retrieval mechanism, would clarify how much of the gain comes from the tensor decomposition vs. the retrieval.

- **Benchmark scope and synthetic degradation validation.** The AML-VLN benchmark comprises 24 tasks from 5 simulation scenes and 2 real-world scenes. The synthetic degradations (scattering, low-light, overexposure) are generated via parametric imaging models (Eqs. 10–12), but no validation is provided that these synthetic images are realistic proxies for actual day/night, fog, or overexposed conditions. Table 5 tests only 4 unseen simulation scenes and 2 real-world scenes under normal/low-light conditions, leaving scattering and overexposure generalization untested in real settings. The "all-day" claim would be strengthened by at least qualitative comparison with real captures.

- **No analysis of task-ordering sensitivity.** The caption of Figure 6 states "The order of tasks is randomized," but no results reporting variance across multiple random orders are provided. A single ordering may yield different difficulty or interference patterns, and the absence of error bars or multi-run statistics limits confidence in the reported numbers.

- **Orthogonality loss (Eq. 8) scope and interaction with DKIL strategy.** The loss penalizes Ũ³(Ũ³)ᵀ − I, applied to the full expert matrices. Since only the currently training rows are updated (others are frozen), this mainly constrains new experts to be orthogonal to existing ones. However, the paper does not discuss whether strong orthogonality could limit positive transfer between semantically related scenes/environments (e.g., two indoor scenes under the same environment).

### Trivial
None.

## Nice-to-Haves

- Equipping baselines (e.g., BranchLoRA, SD-LoRA) with the same CLIP-feature retrieval mechanism to allow a controlled comparison that isolates the tensor decomposition effect from the retrieval effect.
- Validating synthetic degradation realism with side-by-side comparisons to real captures of the same scene under different conditions.
- Reporting results with variance across multiple task-order randomizations.

## Removed Points

The following points from the reviewer inputs were assessed and removed:

1. **Figure 2 naming confusion ("Step-by-step fine-tune" vs. "Sequential fine-tune")** — Removed per style-nitpick rule. The figure is an illustration, and the identical values are a presentation choice for the motivating example.
2. **Problem definition contradicts benchmark (scenes/environments reused)** — Removed as factually wrong. The definition requires non-overlapping *pairs* (S_t, E_t), which holds since (sim-world-v1, Normal) ≠ (sim-world-v1, Scattering).
3. **Orthogonality loss on zero-initialized experts degrades future learning** — Removed as a misunderstanding. Unseen (zero-initialized) expert rows are frozen during training of new tasks; the loss only affects the currently trained row.
4. **Seq-FT values of 0 for T1–T5 suggest evaluation bug** — Removed. Zero success on early tasks after extensive sequential training is expected for naive FT without any forgetting mitigation; it demonstrates the problem the paper aims to solve.
5. **3rd vs. 4th order ablation uses different parameter counts** — Removed as factually wrong. The 4th-order variant has *fewer* expert parameters (704) than the 3rd-order (2,560) yet performs better, which *strengthens* the claim about decoupling, not weakens it.
6. **Large unexplained SD-LoRA gap** — Removed. This is the paper's core finding — that decoupled tensor representation enables better generalization than compositional matrix methods.
7. **Generic hyperparameter tuning concerns for baselines** — Removed as a generic criticism common to all CL papers; the paper states that hyperparameters follow StreamVLN settings and details are in the appendix.
8. **Missing appendix content / stripped sections** — Removed per instruction that the parser strips these; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The key intellectual move — using a 4th-order Tucker decomposition to decouple scene and environment knowledge into separate factor matrices, then reducing to a 2D weight via mode-3 and mode-4 fiber selection (Eq. 3) — is the paper's central contribution and is adequately explained. No novel cross-cutting insight emerged from the review process beyond what the paper already states.

## Suggestions

1. **Clarify the M-SR_t oracle.** Provide the exact protocol: number of training epochs, learning rate, data mixing strategy, and whether a single joint model was trained for each t or a cumulative procedure was used. Explain why the definition says t ≤ 20 but the table shows values up to T24. Discuss why small negative F-SR values arise (e.g., data imbalance in joint training).
2. **Add an ablation isolating the retrieval mechanism.** Compare (a) TuKA with the proposed retrieval, (b) TuKA with random expert selection, and (c) TuKA with uniform mixing of all experts. This will quantify the contribution of the retrieval step vs. the tensor decomposition itself.
3. **Add variance over task orderings.** Run the main experiment with at least 3 different random task orders and report mean ± std for SR and F-SR.
4. **Validate degradation realism qualitatively.** Show side-by-side examples of synthetic vs. real low-light/scattering/overexposure images from the same scene, or acknowledge this as a limitation.
5. **Expand real-world evaluation.** Include real-world testing for scattering and overexposure conditions, not just normal/low-light.

## Score and Decision

**Score calibration against retrieved anchors:**

| Anchor | Avg Human Score | Comparison to This Paper |
|--------|----------------|-------------------------|
| `PaYo96rjij` (Lifelong Embodied Navigation Learning) | 6.00 | Very similar paper — both formalize a lifelong navigation problem, use LoRA-based decoupling, and build a benchmark. This paper's method (Tucker decomposition) is more novel than DE-LoRA, but the forgetting-rate oracle issue is a concern that Uni-Walker doesn't have. Roughly comparable quality. |
| `pFh5ygjN3V` (M³E Continual VLN) | 4.50 | Also addresses continual VLN. This paper has stronger empirical results, more baselines, and a more principled method. This paper is stronger. |
| `kkBOIsrCXh` (Embodied Navigation Foundation Model) | 8.00 | Much larger scale (8M samples, cross-embodiment), broader impact. Not directly comparable in scope. This paper is not at this level. |
| `OyVRrKG8Dj` (CogVLN) | 3.00 | Weak baselines, limited experiments. This paper is substantially stronger on all dimensions. |
| `CA4yNpLTAU` (TIDE Continual Learning) | 4.67 | Different domain (classification). This paper faces more challenging real-world evaluation constraints. Comparable quality but this paper has stronger empirical support. |
| `apaLoTumdO` (CE-Nav) | 4.50 | Different domain (cross-embodiment navigation). Comparable experimental rigor. This paper is slightly stronger in method novelty. |

The paper makes a genuine contribution — the Tucker decomposition approach to multi-hierarchical PEFT is novel, the AML-VLN problem formalization is well-motivated, and the empirical results are consistently strong across tasks and metrics. The evaluation concerns (negative forgetting rates, retrieval mechanism not ablated, benchmark scope) are real but addressable and do not invalidate the core claims. The paper is stronger than the 4.5–5.0 range papers and comparable to the 6.0-level paper, with the forgetting-rate concern tempering the score slightly.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>