Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

This paper formalizes the All-Day Multi-Scenes Lifelong Vision-and-Language Navigation (AML-VLN) problem, where an agent must continually learn across diverse scenes and environmental conditions (normal, low-light, overexposure, scattering) without forgetting past knowledge. The authors propose Tucker Adaptation (TuKA), which represents multi-hierarchical navigation knowledge (scene-level, environment-level, shared) as a fourth-order tensor decomposed via Tucker decomposition into shared core/encoder/decoder and separate scene/environment expert factor matrices. They further introduce Decoupled Knowledge Incremental Learning (DKIL) with three regularization terms, and build AllDayWalker, an agent using CLIP-based retrieval for task-agnostic inference. The paper also extends Habitat with physically motivated imaging models to create a 24-task benchmark. The experimental results show substantial gains over LoRA-based baselines (65% vs. 44% average SR).

---

## Strengths

1. **Principled problem formalization.** The paper provides a clear, well-motivated definition of AML-VLN (Section 2), specifying multi-hierarchical knowledge, task sequences with non-overlapping scene–environment pairs, and task-agnostic testing. This fills a gap in the VLN continual learning literature and the 24-task benchmark (Figure 6) enables standardized evaluation.

2. **Novel and well-motivated technical approach.** TuKA's use of a fourth-order Tucker decomposition to decouple shared, scene-specific, and environment-specific knowledge is a clean solution to the limitation that 2D matrix adapters (LoRA, MoE-LoRA) can only represent two hierarchical levels. The tensor–matrix alignment mechanism (Eq. 3) that reduces the higher-order tensor to a 2D weight matrix for LLM injection is technically sound.

3. **Large and consistent empirical gains.** AllDayWalker achieves 65% average SR across 24 tasks, compared to 44% for the best prior method (BranchLoRA) and much higher forgetting rates for all baselines (Tables 1–2). The improvement is sustained across SPL, OSR, and their forgetting counterparts (Figure 7). Even under 30-task scaling (Table 4) and unseen-scenario generalization (Table 5, 55% vs. 39–40%), the method remains well ahead.

4. **Useful benchmark extension.** The degradation models (atmospheric scattering, low-light, overexposure) applied to Habitat (Section 4, Eqs. 10–12) are physically grounded and provide a concrete testbed for multi-condition VLN that can benefit future work.

5. **Controlled ablation of shared components.** Table 3 systematically ablates whether the core tensor, encoder, and decoder are shared across tasks, showing that sharing 𝒢 and U² drives the main performance gains while sharing U¹ saves storage without harming accuracy.

---

## Weaknesses

### Fatal
None.

### Major

1. **Baseline evaluation protocol for task-agnostic inference is unspecified.** The AML-VLN problem definition (§2) states that task-ID is unknown at test time. The paper describes its own CLIP-based retrieval mechanism for expert selection (§3.4), but provides no description in the main paper of how the compared baselines — particularly those with multiple expert modules (HydraLoRA, BranchLoRA, O-LoRA, SD-LoRA, MoE variants) — handle this condition. Were they given oracle task-ID? Was the same CLIP retrieval applied? Was the most recently trained module used by default? Each choice produces a fundamentally different evaluation. The paper references Appendix C for "implementation details and methods parameter comparison," but the main text should state the inference protocol for every baseline. Without this, the central comparison in Tables 1 and 2 cannot be properly interpreted, and the claimed improvements are not reliably attributable to the method's design rather than to an asymmetric evaluation setup. This is the most critical issue.

### Minor

2. **Missing ablation of the three loss components.** The DKIL method (§3.3) combines three regularization terms: elastic weight consolidation (ℒ_ewc, Eq. 4), expert consistency (ℒ_co, Eq. 7), and orthogonal expert constraint (ℒ_es, Eq. 8), with hyperparameters λ₁=0.2, λ₂=0.2, λ₃=0.1. None of these are individually ablated, nor is hyperparameter sensitivity reported. While Table 3 ablates shared-vs.-separate components, the individual contribution of each loss term — and whether all three are needed — remains unknown. This weakens support for the claimed effectiveness of the DKIL design.

3. **Forgetting metric definitional issues.** The forgetting rates (F-SR, etc.) are defined (Eq. 13) with M-SR_t as the performance of a joint model trained on tasks 1…t, with the note "t ≤ 20." Yet Table 2 reports F-SR for tasks T1–T24 without clarifying how M-SR_t is obtained for t > 20. Additionally, AllDayWalker shows negative forgetting rates on T14 (–3%) and T20 (–4%), meaning the sequential model outperforms the joint multi-task model on those tasks — an unusual outcome that is not discussed. These issues do not invalidate the overall results but reduce confidence in the reported forgetting numbers.

4. **Overclaimed "real-world deployments."** The contributions list (bullet 3) states "additional real-world deployments also validate the superiority of our AllDayWalker." However, the paper's experiments include real-world *scenes* (as part of the benchmark, e.g., real-world-1, real-world-2) and real-world *datasets* in the generalization experiment (Table 5, G5–G6), not physical robot deployments. This phrasing should be corrected to avoid misleading readers.

5. **Computational cost not reported.** The paper describes TuKA as a "parameter-efficient" method but provides no comparison of total trainable parameters, per-layer parameter counts, or inference cost relative to the baselines in the main paper. Given that the core tensor alone (r₁=r₂=8, r₃=r₄=64) is 8×8×64×64 ≈ 262k parameters per layer, a direct parameter and FLOP comparison is needed to substantiate the efficiency claim. (The paper references Appendix C for parameter comparison.)

6. **Unclear baseline operation in the generalization experiment.** Table 5 compares AllDayWalker with BranchLoRA and SD-LoRA on six unseen scenarios. The paper states that AllDayWalker "select[s] the expert with the highest similarity during testing" but does not explain how BranchLoRA or SD-LoRA handle completely unseen scene–environment pairs without task-ID. If these methods have no mechanism for unseen tasks, the comparison is asymmetric.

7. **Training dataset statistics omitted.** The paper describes the benchmark's scene/environment structure (24 tasks, 5 simulated + 2 real scenes) but does not report the number of training episodes per scenario, data splits, or related statistics in the main text. This information is important for assessing task difficulty and experimental reproducibility.

### Trivial
- None beyond minor presentation issues that are parser artifacts rather than author errors.

---

## Nice-to-Haves

- Ablate the three DKIL loss terms (ℒ_ewc, ℒ_co, ℒ_es) individually to show each one's contribution.
- Provide a side-by-side parameter count and FLOP comparison table for all methods.
- Report results over multiple random task orders (at least 3 seeds) since task order can strongly affect lifelong learning outcomes.
- Include a simple baseline that stores a separate LoRA per task and uses the same CLIP retrieval for inference, to isolate the benefit of the tensor factorization itself.
- Clarify the forgetting metric by using a standard continual learning definition (e.g., per-task performance drop relative to each task's peak) that does not require a multi-task joint model.

---

## Removed Points

The following points from the harsh critic are removed or demoted with justification:

- **"Framing about LoRA limitations overstated"** — The paper's characterization of MoE-LoRA as limited to two hierarchical levels is a reasonable simplification; whether nested gating could capture more structure is a matter of degree, not a factual error. REMOVED (subjective framing judgment).
- **"DKIL training procedure could be more precise"** — The paper describes Kaiming initialization for new scenarios and inheritance for seen experts. When both scene and environment are new, both experts are initialized fresh as described. REMOVED (already addressed).
- **"The paper should also compare against a simple baseline that uses two separate LoRA modules"** — This is a useful suggestion but not a weakness in the presented work; demoted to Nice-to-Have.
- **"Missing related works"** — REMOVED per instruction: cannot confirm existence of missing references.
- **"Reproducibility nitpicks"** (e.g., hyperparameters not disclosed, trivial implementation details) — REMOVED: hyperparameters are listed in §5.1 and Appendix C.
- **Formatting/style nitpicks** — All REMOVED per instruction.

---

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from cross-referencing the reviews is the tension between the method's clear technical novelty (Tucker decomposition for parameter-efficient multi-hierarchical adaptation is genuinely new in the VLN + continual learning space) and the surprisingly conventional experimental gaps (unstated baseline inference protocol, unablated loss terms). This suggests that the paper's contributions are likely solid but that the evaluation narrative needs to be reconstructed with more care. The negative forgetting values (−3%, −4%) also hint at an interesting property of the tensor factorization: later tasks may actively improve performance on earlier tasks through the shared core tensor, which would be a meaningful advantage over standard LoRA adapters. The paper does not discuss this, but it could be a valuable insight to highlight.

---

## Suggestions

1. **Clarify the baseline inference protocol.** For every baseline method in Tables 1–2, state explicitly: does it use oracle task-ID, the same CLIP retrieval, or another mechanism? If the details are in Appendix C, add a one-sentence summary per baseline in the main paper (§5.2).
2. **Ablate the three loss terms.** Add an ablation table showing performance with only ℒ_ewc, only ℒ_ewc+ℒ_co, and all three, plus a sensitivity sweep over λ₁, λ₂, λ₃.
3. **Fix the forgetting metric description.** Clarify how M-SR_t is computed for all 24 tasks (not just t ≤ 20) and discuss the negative values.
4. **Correct the "real-world deployments" claim** to "real-world scenes" or "real-world datasets."
5. **Report parameter counts and inference costs** in the main paper to substantiate the efficiency claim.
6. **Add training episode counts and data splits** to the main text or a table.

---

## Score and Decision

The paper introduces a well-motivated new problem, a technically interesting tensor-based adaptation method, and a useful benchmark. The empirical results show large and consistent improvements. However, a critical methodological gap — the unstated inference protocol for baselines under task-agnostic testing — undermines the main experimental comparison, and several secondary issues (missing ablations, metric inconsistency, overclaiming) reduce confidence. These are addressable in revision and do not invalidate the core contribution.

**MY FINAL SCORE:** 7.0
**MY FINAL DECISION:** Accept