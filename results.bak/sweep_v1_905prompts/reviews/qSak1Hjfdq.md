Now let me write the consolidated review.

## Summary

This paper formalizes the **all-day multi-scenes lifelong VLN (AML-VLN)** problem, where an agent must continually learn across multiple scenes and diverse imaging environments (normal, low-light, overexposure, scattering). To address this, the authors propose **Tucker Adaptation (TuKA)**, which represents multi-hierarchical navigation knowledge as a **fourth-order tensor** and uses Tucker decomposition to decouple it into shared subspaces (core tensor, encoder/decoder) and scenario-specific expert factor matrices (scene experts U³, environment experts U⁴). A **Decoupled Knowledge Incremental Learning (DKIL)** strategy consolidates shared knowledge via elastic weight consolidation while orthogonalizing new experts. The resulting agent **AllDayWalker** is evaluated on a new **24-scenario benchmark** (AllDay-Habitat, built on Habitat with three physically based degradation models) and achieves **65% SR / 11% F-SR**, outperforming the next-best method by 13% SR and 7% F-SR. The paper also demonstrates generalization to unseen scenarios (+15–16% over baselines) and stable scaling to 30 tasks.

---

## Strengths

1. **TuKA provides a principled way to decouple multi-hierarchical knowledge beyond matrix-based adapters.**  
   Unlike LoRA and MoE-LoRA variants that represent knowledge within two hierarchical matrices (one shared, one task-specific), TuKA (Eqs. 2–3, §3.2, Figure 3c) uses a fourth-order Tucker decomposition to explicitly separate shared navigation skills (core tensor 𝒢, encoder U², decoder U¹), scene-specific knowledge (expert matrix U³), and environment-specific knowledge (expert matrix U⁴). The alignment mechanism (Eq. 3) coherently reduces the high-order tensor to a 2D weight matrix compatible with LLM backbones.

2. **Strong and consistent empirical results across 24 tasks.**  
   AllDayWalker achieves 65% average SR (Table 1) and 11% average F-SR (Table 2), substantially ahead of the best baseline (SD-LoRA: 52% SR, 18% F-SR) — a gap of +13% SR and –7% forgetting rate. The advantage is consistent across practically every individual task, not just the averages. Supplementary results on SPL, F-SPL, OSR, and F-OSR (Figure 7) reinforce the same pattern.

3. **Generalization to completely unseen scenarios.**  
   On six unseen tasks spanning novel scene–environment combinations (Table 5), AllDayWalker reaches 55% SR, outperforming BranchLoRA (40%) and SD-LoRA (39%) by 15–16%. This provides direct evidence that the decoupled expert structure enables zero-shot scenario adaptation, not just memorization of training tasks.

4. **Stable lifelong learning under task scaling (24 → 30 tasks).**  
   Table 4 shows that adding six more tasks causes no notable degradation on early tasks (e.g., T1: 79%→77%, T7: 87%→86%, T24: 72%→66%), confirming that the DKIL strategy prevents accumulation of forgetting.

5. **Problem formalization and benchmark construction.**  
   Section 2 provides a precise formulation of AML-VLN with non-overlapping task sequences and a task-ID-agnostic inference requirement. Section 4 extends Habitat with three physically grounded degradation models (Eqs. 10–12) for scattering, low-light, and overexposure, creating a practical benchmark that is more realistic than single-condition evaluations.

---

## Weaknesses

### Fatal
None.

### Major
None that threaten the paper's core claims. The issues below are minor to moderate and addressable in a rebuttal or revision.

### Minor

1. **Task order randomization is claimed but not tested with multiple seeds.**  
   Figure 6 states "The order of tasks is randomized," yet all results in Tables 1–2 are reported from a single random order without standard deviations or multiple runs. In continual learning, performance can depend heavily on task ordering. The paper should report statistics over at least 3–5 random orderings, or clarify that the order shown in Figure 6 is fixed (the randomization was done once during benchmark construction) and acknowledge this limitation.

2. **Pre-allocated expert matrices limit truly open-ended lifelong learning.**  
   The factor matrices U³ ∈ ℝ^(M×r₃) and U⁴ ∈ ℝ^(N×r₄) are fixed at M=7 scenes and N=4 environments. If a novel scene or environment appears at test time beyond this pre-allocation, the method lacks a mechanism to expand the expert matrices. This is at odds with the lifelong learning ideal where the taxonomy of tasks is unknown a priori. The paper should discuss how TuKA could be extended (e.g., dynamic row insertion into U³/U⁴) or explicitly scope this as a limitation.

3. **Baseline handling of the task-agnostic test setting is not clearly explained.**  
   The paper states that "task-id is seen during training but is agnostic during the testing phase" (§5.1). AllDayWalker uses a retrieval mechanism (CLIP feature matching, §3.4) to select experts at test time. However, it is not described how baselines like O-LoRA (which stores separate orthogonalized modules per task) and SD-LoRA handle this setting — whether they also use input-based routing, require oracle task ID, or rely on a heuristic. This gap makes it difficult to assess whether the comparison is fully equitable on the task-identification dimension. (The paper notes that details are in Appendix C, but the main text should at least summarize the approach for each family of baselines.)

4. **Negative forgetting rates (T14: –3%, T20: –4% in Table 2) are not discussed.**  
   A negative F-SR means performance after lifelong learning exceeds the multi-task joint-training upper bound. This is unusual and could indicate positive transfer — or it could point to a quirk in how the multi-task upper bound M-SR was computed for the real-world tasks (since T14 and T20 are real-world tasks). Either way, the phenomenon merits explicit commentary.

5. **SD-LoRA has blank entries for T23–T24 in Table 1.**  
   The SR row for SD-LoRA in Table 1 appears to have missing values for the final two simulation tasks. The corresponding F-SR row (Table 2) has complete data including T23=17%, T24=0%, which implies the underlying SR values exist. This is likely a formatting/parsing artifact, but it should be confirmed and corrected in the main table.

### Trivial

- The initialization description (§3.3) says "Kaiming initialization...and U³, U⁴ with zero-initialization" — a sentence that seems to apply Kaiming to factor matrices and core tensor but then zero-initializes U³, U⁴. The intended initialization scheme could be stated more precisely.
- The loss balance λ = 1 – (λ₁+λ₂+λ₃) = 0.5 gives equal total weight to the main objective and the regularization sum. This is a reasonable design but unusual enough to warrant a brief justification.

---

## Nice-to-Haves

- A breakdown of trainable parameter counts for each method would help contextualize the "parameter-efficient" claim.
- An analysis of the learned expert factor matrices (e.g., visualizing the similarity structure of U³ rows across scenes) could provide direct evidence for the decoupling claim.
- The third-order vs. fourth-order ablation (Figure 8) uses a coupled scenario expert (M×N rows) for the third-order variant. An additional comparison with a 4D variant that concatenates scene+environment into one dimension of a 3D tensor would further isolate the benefit of decoupling.

---

## Removed Points

These points were flagged by the harsh critic but are removed after verification:

- **Figure 2 inconsistency**: The critic claimed the identical values in "Step-by-step" and "Sequential" columns are erroneous. This is a misunderstanding — the table shows per-current-task performance, and the forgetting rate column measures forgetting of *previous* tasks, not the current one. The identical values are expected and the figure correctly illustrates catastrophic forgetting. **Removed.**
- **O-LoRA "ending abruptly"**: O-LoRA in Table 1 has all 24 task values; the missing Avg column is a parser artifact. **Removed.**
- **Problem definition overlap contradiction**: The paper's definition (§2) states each new scenario {S_t, E_t} does not repeat a prior {S_j, E_j} pair. The critic's concern about the same scene reappearing under a different environment is a *different pair*, which is explicitly allowed and handled by the method. **Removed.**
- **Loss down-weighting**: λ=0.5 is a standard coefficient choice. The critic's framing of it as "unusual" is a matter of preference, not a flaw. **Removed.**
- **Third-order ablation criticism**: The comparison compares a coupled expert (3D) against a decoupled one (4D), which directly tests the effect of decoupling — the very claim the paper makes. **Removed.**
- **Missing related works, typos, formatting artifacts**: Standard removal per policy.

---

## Novel Insights

None beyond the paper's own contributions. The key insight — using a higher-order Tucker decomposition to represent multi-hierarchical continual learning knowledge with separable scene and environment expert dimensions — is the paper's own.

---

## Suggestions

1. Run the main experiments with 3–5 random task orderings and report means ± std to verify that the results are not sensitive to a particular order.
2. Add a paragraph describing how each baseline family (per-task LoRA, MoE-routed, composition-based) handles task-agnostic inference, to clarify that the comparison is equitable.
3. Discuss the negative forgetting rates and the pre-allocation limitation in a "Limitations" subsection.
4. Include a parameter count table for all methods.

---

## Calibration and Scoring

**Round 1 bracketing:** I searched for VLN/continual learning papers across three bands. Weak anchors (score < 3.5) were straightforward rejects with fundamental flaws (e.g., "LVLM-CL" at 2.50, "Multimodal Class-Incremental Learning" at 2.33). Middle-band anchors (3.5–7.5) included GSA-VLN (6.40, Accept — proposes a new VLN task + dataset + method) and CA-Nav (5.00, Reject — zero-shot VLN, moderate contributions). Strong anchors (>7.5) were top papers (8.00) with clean, broadly scoped contributions. The paper clearly sits in the middle band.

**Round 1 bracket:** [5.0, 7.0].

**Round 2 narrowing:** I retrieved and compared against anchors inside that bracket. GSA-VLN (6.40, Accept) is the closest topical comparison: it also proposes a new VLN task, dataset, and method. The current paper has a stronger method contribution (TuKA is more technically novel than GR-DUET) but comparable empirical substantiation. FLoRA (5.75, Accept) uses Tucker decomposition for PEFT across broad domains — the current paper is narrower (VLN-specific) but deeper (full agent + benchmark). ADePT (7.00, Accept) is stronger on experimental breadth (23 tasks across NLP/VL) but is a pure PEFT method without the hierarchical lifelong problem framing.

**Final placement:** The paper sits between the FLoRA-like accepted PEFT papers (~5.75–6.0) and the GSA-VLN paper (6.40). It has genuine strengths (novel method, strong empirical results, new benchmark) offset by several minor evaluation concerns that do not threaten the core claims. This places it comparable to or slightly above GSA-VLN.

**Anchors considered:**
- JIlIYIHMuv (2.50, weak rej.) — clearly weaker than the current paper
- gNoqEdT2wO (2.33, weak rej.) — clearly weaker
- 2oKkQTyfz7 (6.40, GSA-VLN, Accept) — comparable; this paper's method is more novel but evaluation questions are similar in severity
- eWFkMCBySw (5.00, CA-Nav, Reject) — weaker contribution; this paper is stronger
- OALIb8oNfl (5.75, FLoRA, Accept) — comparable; narrower domain but deeper system contribution
- fswihJIYbd (7.00, ADePT, Accept) — stronger on breadth, but less directly relevant
- tpUEqmjZiS (4.50, PSPL, Reject) — weaker
- rwmwFnmjAX (4.75, Continual LLaVA, Reject) — weaker

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>