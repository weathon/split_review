Now I have a thorough understanding of the paper. Let me compile the consolidated review.

---

## Summary

This paper formalizes All-Day Multi-Scenes Lifelong VLN (AML-VLN), where an agent must continually learn to navigate across diverse scenes and illumination conditions (normal, low-light, overexposure, scattering) without catastrophic forgetting. The core contribution is Tucker Adaptation (TuKA), which lifts parameter-efficient adaptation into a high-order tensor space via Tucker decomposition — decoupling knowledge into shared subspaces (core tensor, encoder, decoder) and task-specific experts (scene, environment). A decoupled knowledge incremental learning (DKIL) strategy consolidates shared components via elastic weight consolidation and constrains experts via orthogonality. The AlldayWalker agent achieves 65% average SR over 24 sequential tasks, substantially outperforming the best baseline SD-LoRA (56%).

---

## Strengths

- **Strong empirical results with clear margins.** AlldayWalker achieves 65% average SR across 24 tasks vs. 56% for best competitor SD-LoRA, with the lowest forgetting rate (11% F-SR vs. 18%). The gaps are substantial and consistent across all metrics (SR, SPL, OSR; Tables 1–2, Figure 7, Appendix K).

- **Genuinely novel method.** Using Tucker decomposition to represent multi-hierarchical navigation knowledge in a higher-order tensor, with explicit decoupling of scene and environment experts, is a creative idea not present in prior LoRA-variant literature. The tensor-to-matrix alignment via expert row selection (Eq. 3) is a clean solution to the dimensional mismatch problem.

- **Convincing ablation on the core architectural claim.** The fourth-order TuKA (65% SR) substantially outperforms both a third-order tensor variant (54% SR, Table 14/Appendix H) and a hierarchical matrix-based ABC-LoRA (55% SR, Table 15/Appendix I). These 10–11 point gaps directly validate the thesis that high-order tensor decoupling is more powerful than 2D matrix adaptation for multi-hierarchical knowledge.

- **Comprehensive experimental design.** Twelve baselines spanning sequential fine-tuning, regularization-based, MoE-LoRA, orthogonal, and TTA methods. Multiple metrics (SR, SPL, OSR with forgetting variants). Ablations on shared components (Table 3), task scaling (Table 4, 24→30 tasks), rank scaling (Appendix G), and fifth-order extension (Appendix J). Generalization to six unseen scenario–environment pairs (Table 5, 55% SR vs. 39–40%).

- **Real-world validation.** Deployment on a quadruped robot with real hardware in two real-world scenes under normal and low-light conditions (T21–T24), bridging simulation and reality.

- **Parameter efficiency.** 15.64M trainable parameters, comparable to baselines (Table 17).

---

## Weaknesses

### Fatal

None.

### Major

- **Expert retrieval mechanism is unvalidated.** Task-agnostic inference (Section 3.4) relies on CLIP feature matching to select the correct scene and environment experts at test time, when the task-id is unknown. No analysis of retrieval accuracy is provided — the paper never reports what fraction of episodes the correct experts are selected, nor does it compare against an oracle that always picks the right experts. This matters because: (a) the entire task-agnostic deployment claim depends on this mechanism; (b) in degraded conditions (low-light, scattering, overexposure), CLIP features may be less discriminative; (c) a mismatch could cascade into navigation failures that the shared core cannot compensate for. The strong overall SR results and generalization performance (Table 5) indirectly suggest the retrieval works reasonably well, but without direct evidence, the practicality of task-agnostic inference remains incompletely established.

### Minor

- **Unconventional forgetting metric produces negative values that are not discussed.** The forgetting rate F-SR (Eq. 13) is defined relative to joint training on tasks 1…t, not relative to post-training performance. While this definition is clearly stated, it deviates from standard CL practice. AlldayWalker produces negative F-SR values at T14 (−3) and T20 (−4), meaning sequential learning outperforms joint training. SD-LoRA also shows −2 at T14, so this is not unique to TuKA. The paper never explains why this occurs — it could reflect beneficial forward transfer or regularization, but leaving it unaddressed weakens the clarity of the continual learning story.

- **Real-world validation covers only two environment types.** The hardware experiments (T21–T24) evaluate normal and low-light conditions but omit scattering and overexposure. Given the paper's "all-day" motivation, demonstrating the full environmental range on real hardware would strengthen the practical claim. The simulation results for scattering/overexposure are strong, and real-world deployment in those conditions is genuinely difficult, so this is a scope limitation rather than a fundamental flaw.

- **No sensitivity analysis on degradation severity.** The imaging model parameters (Appendix E, Table 8) are fixed. How results change under milder or more extreme scattering (varying β), overexposure (varying exposure multiplier), or low-light (varying brightness) is not explored. This limits understanding of robustness boundaries.

### Trivial

- The number of CLIP features stored per scene/environment is not specified (Section 3.4), and whether matching is performed per episode or per step is not explicitly stated (Algorithm 2 suggests per-step matching).

- The scaling analysis (Appendix G) shows that increasing expert ranks (r₃, r₄) yields larger gains than increasing shared ranks (r₁, r₂), potentially indicating that the shared component is underutilized — this is not discussed.

---

## Nice-to-Haves

- An oracle comparison for expert retrieval (always selecting the correct experts) to establish an upper bound and quantify the gap between the current CLIP-based approach and perfect selection.
- Sensitivity analysis varying degradation parameters to characterize robustness boundaries.
- Ablation on retrieval frequency (per-step vs. per-episode).
- A brief discussion explaining why negative forgetting values occur (e.g., the incremental consolidation may act as a beneficial regularizer compared to joint training).

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

1. **"The core tensor is shared across all tasks, which may limit model's ability to capture scene–environment interactions beyond what a product of vectors can express"** — This is a speculative architectural concern not backed by empirical evidence. The results show the fourth-order tensor works well in practice.

2. **"The orthogonality constraint is applied to entire expert matrices but the paper does not clarify whether enforced only among active experts"** — The paper does specify this. Lines 346–353 show that Les is applied to previous experts (indices i ≠ s for scenes, j ≠ e for environments) against the current expert, which is the natural interpretation.

3. **"No ablation on whether a rank-1 core would suffice"** — The rank scaling study in Appendix G systematically varies all ranks. The concern is already partially addressed.

4. **"Degradation model parameters (Appendix E) not accompanied by justification"** — The parameters are tabulated with references to the imaging models from prior literature (Narasimhan & Nayar, Healey & Kondepudy, etc.). Justification is implicit via those references.

---

## Novel Insights

None beyond the paper's own contributions. The paper itself contributes the insight that multi-hierarchical navigation knowledge (scene × environment) can be effectively represented through Tucker decomposition of a high-order tensor, and that decoupling shared vs. specific knowledge in this tensor space yields stronger continual learning than matrix-based adapters. Both the harsh critic and strength finder essentially restate this contribution rather than adding genuinely independent insight.

---

## Suggestions

1. **Add an expert retrieval accuracy analysis.** Report, for T1–T24 and generalization tasks G1–G6, what fraction of episodes the CLIP-based matching selects the correct scene expert and environment expert. Include an oracle baseline (always correct expert) to quantify the performance ceiling. This would decisively address the main evidential gap.

2. **Explain the negative forgetting phenomenon.** Briefly discuss why sequential learning can outperform joint training — e.g., the DKIL constraints may provide beneficial regularization, or the inheritance mechanism may enable forward transfer that joint training does not exploit. Even a paragraph of informed speculation would help.

3. **Acknowledge the real-world environment limitation explicitly.** State that hardware experiments currently cover normal and low-light, and that scattering/overexposure on real hardware is deferred to future work. This is more honest than implying full coverage.

---

## Score and Decision

### Anchor Comparison

| Anchor | Avg Score | Comparison to current paper |
|--------|-----------|-----------------------------|
| PaYo96rjij (Lifelong Embodied Navigation Learning) | 6.00 | Most directly comparable — also formalizes a lifelong VLN problem with LoRA-based expert decomposition. Current paper has a more novel method (tensor decomposition vs. DE-LoRA), more comprehensive experiments (24 tasks across 4 environments vs. 18 tasks), and real-world validation. Stronger. |
| pFh5ygjN3V (M³E: Continual VLN via Mixture of Macro and Micro Experts) | 4.50 | Also continual VLN with MoE. Simulation-only, weaker ablations, reviewers questioned component contributions. Current paper is clearly stronger. |
| Wm1SjTIjvA (Stability Matters) | 3.00 | Rejected — core insight questioned, limited theoretical justification. Current paper is in a different tier entirely. |
| T3Vc5fkTzV (KeepLoRA) | 5.50 | Continual learning with LoRA for vision-language, but not navigation. Current paper is more application-specific with stronger benchmark construction. |
| HB6KvsqcAn (Physically Executable 3D Gaussian for Navigation) | 7.00 | High-scoring navigation paper with strong physical grounding. Current paper has less novelty in the problem space but more comprehensive CL experiments. Weaker than this anchor. |
| kkBOIsrCXh (Embodied Navigation Foundation Model) | 8.00 | Very high-scoring, large-scale foundation model for navigation. Current paper is narrower in scope but deeper in the continual learning aspect. Weaker than this anchor. |

The paper is stronger than the most directly comparable anchor (PaYo96rij, 6.0) due to the more novel tensor-based method, more comprehensive experiments, and real-world validation. However, the unvalidated expert retrieval mechanism prevents it from reaching the confidence level of the 7.0+ papers. The paper is substantially above the 4.0–5.0 range where papers are typically rejected.

**Originality:** High. The Tucker decomposition approach for multi-hierarchical adaptation in VLN is genuinely novel in the PEFT/continual learning space.

**Importance:** Moderate-to-high. Lifelong VLN across diverse conditions is a practical problem for real-world deployment.

**Claims supported:** Mostly well-supported, with one significant gap (retrieval validation).

**Soundness:** Good experimental design with 12 baselines and thorough ablations; the method is clearly described.

**Clarity:** Good structure, though the forgetting metric discussion is incomplete.

**Value to community:** The AML-VLN benchmark and the tensor adaptation approach are valuable contributions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>