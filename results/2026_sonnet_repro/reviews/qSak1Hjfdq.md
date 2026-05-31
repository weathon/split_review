Round 1 bracket: **5.5 to 7.0** (comparable to the 6.4 GSA-VLN paper; stronger than the 5.75 lifelong robot paper which was rejected). Let me narrow in.Now I have enough to write the final review.

**Anchors summary:**
- OALIb8oNfl (5.75, Accept): Tucker-based PEFT for N-d parameter spaces — no new task, no benchmark, no continual learning. Paper under review is more comprehensive.
- GSA-VLN (6.4, Accept): New VLN task + benchmark + method, similar scope. Comparable, with that paper having dataset-diversity concerns.
- HAZARD (6.75, Accept): New embodied benchmark + LLM agent evaluation. Paper under review has stronger methodological contribution.
- Round 1 bracket: 5.5–7.0. Round 2 narrows to **5.5–6.5**.

---

## Summary

This paper formalizes **All-Day Multi-Scenes Lifelong VLN (AML-VLN)**, a continual learning setting where an agent must sequentially learn navigation across multiple scene × environment (illumination) pairs without forgetting. The authors propose **Tucker Adaptation (TuKA)**, which lifts adaptation weights into a 4th-order tensor using Tucker decomposition to explicitly decouple core shared knowledge, scene-specific experts (U³), and environment-specific experts (U⁴). Building on TuKA, they develop **AllDayWalker** with a **Decoupled Knowledge Incremental Learning (DKIL)** strategy (EWC on shared subspaces + consistency + orthogonality constraints on specific experts). A new 24-task benchmark, AllDay-Habitat, is constructed by extending the Habitat simulator with physics-based imaging models (low-light, scattering, overexposure). AllDayWalker reports 65% average SR over 24 tasks vs. the best LoRA-based baseline.

---

## Strengths

1. **Principled multi-hierarchical decomposition**: TuKA's 4th-order tensor **X** ∈ ℝ^{a_l×b_l×M×N} (Eq. 2–3) explicitly separates core skills (𝒢), shared encoder/decoder (U¹, U²), scene experts (U³), and environment experts (U⁴). This inductive bias is well-motivated and goes meaningfully beyond the 2-dimensional matrix form of LoRA and HydraLoRA.

2. **Demonstrated catastrophic forgetting and quantified improvement**: Figure 2 shows sequential fine-tuning yields up to 79% forgetting across 10 tasks, directly motivating the paper. Table 2 shows DKIL reduces average F-SR to 11%, compared with 18% for SD-LoRA and 23% for O-LoRA — a substantive improvement.

3. **Comprehensive experimental setup**: 24 sequential tasks across 5 simulation scenes × 4 environments + 2 real-world scenes × 2 environments; 11 baselines spanning sequential fine-tuning, LwF, EWC, Dense/Sparse MoLE, MoLA, HydraLoRA, BranchLoRA, O-LoRA, SD-LoRA, TTA methods — a thorough evaluation.

4. **Generalization beyond training tasks**: Table 5 shows AllDayWalker achieves 55% average SR on 6 unseen scenarios vs. 39% for SD-LoRA, demonstrating that the Tucker structure facilitates knowledge transfer, not merely retention.

5. **Fourth-order vs. third-order tensor analysis (Figure 8)**: The ablation shows 4th-order TuKA consistently outperforms a 3rd-order version across all 20 simulation tasks, concretely validating the benefit of decoupled scene/environment representations over a joint expert set.

---

## Weaknesses

### Fatal
- None.

### Major

1. **Incomplete Table 1 averages for the strongest baselines** — The Avg. column in Table 1 is left blank for Seq-FT, Lwf-LoRA, EWC-LoRA, O-LoRA, SD-LoRA, and FeedTTA. Critically, SD-LoRA is also missing T23 and T24 data entirely. The paper's headline claim — "allDayWalker achieves 65% average SR, outperforming SD-LoRA (52%)" — cannot be verified or placed in context from the table as printed. While AllDayWalker visually dominates SD-LoRA on most individual tasks (e.g., T3: 71 vs. 52, T7: 87 vs. 71, T9: 79 vs. 63, T11: 79 vs. 42), the aggregate comparison is a central result that deserves complete data. The "52%" figure for SD-LoRA appears in the text but has no corresponding table entry.

2. **Missing direct architectural validation: no independent scene-LoRA + environment-LoRA baseline** — The core mechanistic claim is that the 4th-order Tucker tensor's explicit separation of scene and environment dimensions drives the gain. The natural competing design — two independent LoRA adapters (one per scene, one per environment), with the same EWC + orthogonality + consistency losses — is never tested. The ablation in Table 3 tests which *shared components within TuKA* matter, not whether the Tucker structure itself is responsible. The 3rd-order vs. 4th-order comparison (Figure 8) narrows this to rank order, but does not substitute for the structural comparison. Without it, the gains might plausibly come from the DKIL regularizers rather than the tensor factorization per se.

3. **Inference-time expert retrieval uncharacterized** — Section 3.4 describes CLIP-based nearest-neighbor search to match scene and environment experts at test time without task-id. This mechanism is central: incorrect expert matching would substantially degrade performance. Yet retrieval accuracy is never reported in the main paper or (from what is visible) in the experiments. Figure 7's radar chart appears to compare different retrieval strategies ("Ours, BaseModel, Recall, Task2Vec, CLIP") but this comparison is never introduced or explained in the main text. The reliability of this mechanism — which solves the "task-id agnostic at inference" challenge highlighted in §2 — is simply uncharacterized.

### Minor

1. **Formal definition vs. DKIL inconsistency** — §2 states {S_t, E_t} ∩ (∪{S_j, E_j}) = ∅, which as written would prohibit *any* scene or environment from recurring across tasks. Yet §3.3 explicitly initializes scene expert U³[s,:] from a previously seen task "if previous scenario has learned the same experts" — clearly assuming scenes can recur with new environments. The formal condition likely intends that the (S, E) *pair* must be new, not that the individual components cannot recur. The definition should be stated precisely.

2. **Mechanical zero at T24 in forgetting metrics** — Table 2 shows F-SR = 0 for *every* method at T24. This is mathematically guaranteed by the metric definition: M-SR₂₄ is computed by training on T₁–T₂₄ (the full sequential training), which equals SR₂₄ by construction. The paper does not acknowledge this, creating a misleading impression that all methods exhibit zero forgetting on the final task.

3. **Figure 7 methods unexplained in main text** — The caption names "Ours, BaseModel, Recall, Task2Vec, CLIP" as five comparison models, but none of these are introduced as named methods in §5.2 or §5.3. These appear to be expert-selection strategy ablations rather than continual learning baselines, making the figure difficult to interpret without cross-referencing an appendix that the main text does not clearly point to.

4. **Duplicate rows in Table 3** — Two rows both show ✓✓✓ for (Sd-𝒢, Sd-U¹, Sd-U²) with SR=65, F-SR=11, SPL=58, F-SPL=18, but OSR values differ (69 vs. 68). This appears to be a copy-paste error.

### Trivial

1. **Notation inconsistency in §3.4** — The environment expert matching formula writes the candidate set as {Fe_{e1}, …, Fe_{eM}} using M (the scene count), where N (the environment count) is the appropriate cardinality.

---

## Nice-to-Haves

- **Analysis of real-world sim-to-real gap for scattering/overexposure**: The benchmark includes 24 tasks but the two real-world scenes cover only normal and low-light conditions (Figure 6). Scattering and overexposure, which drive several tasks, are never evaluated in real-world deployment. A discussion of this limitation, or at least why these conditions were omitted from real-world testing, would strengthen the "all-day" claim.
- **Exploration of 5th-order tensor** (mentioned as being in Appendix J): Even a brief statement in the main text about whether adding a fifth dimension yields meaningful improvement would be informative.

---

## Removed Points

*These points are flagged as removed — treat with caution.*

- **"SD-LoRA per-task values exceed AllDayWalker at T8 (74 vs. 38)"**: The harsh critic uses this as evidence that AllDayWalker may not be a decisive win. However, a weaker-than-average performance on a few tasks (e.g., T8, T12) does not undermine the overall claim when AllDayWalker clearly dominates on the majority. This is not a fatal weakness; it is noise around the average. Removed.
- **"AllDay-Habitat is entirely self-designed"**: The harsh critic flags this as a benchmark validity concern. Self-designed benchmarks are common and legitimate; the paper documents all imaging models with explicit physical equations (Eq. 10–12). Removed.
- **Strength "important problem"**: Generic without specific grounding in quantified impact. Removed.

---

## Novel Insights

The key insight that Tucker decomposition, by factorizing adaptation weights into a core tensor (shared navigation skills) × scene-specific vectors × environment-specific vectors, provides an *inductive bias* naturally aligned with the multi-hierarchical structure of the AML-VLN problem is genuinely novel. This is more than an engineering choice: the 4th-order structure forces the model to represent scene knowledge and environment knowledge in separate subspaces, enabling the DKIL strategy to apply orthogonal constraints and consistency regularizers targeted to each hierarchy. The contrast with LoRA-family methods, which can only express two-hierarchy shared/specific structure, is cleanly articulated and empirically supported (Figure 8). The idea of using Tucker rank as a knob for hierarchy depth (3rd-order vs. 4th-order) has potential applicability to any multi-hierarchical PEFT scenario beyond VLN.

---

## Suggestions

1. Complete the Avg. column in Table 1 for all methods, and either provide T23–T24 data for SD-LoRA or explicitly note it failed to converge and report its available average. The "52%" claim must be supported in the table.
2. Add an ablation: independent scene-LoRA + environment-LoRA with the same DKIL losses applied to each. This directly tests whether Tucker structure or DKIL regularization drives the gain.
3. Report expert retrieval accuracy (e.g., per environment type), or add a short analysis showing how often the correct expert is selected and what fraction of failures are retrieval errors vs. navigation failures. This substantiates the "task-id agnostic" property that motivates the paper.
4. Clarify the formal non-overlap condition in §2 to specify that the (S, E) *pair* must be new, not the individual scene or environment.
5. Explain Figure 7's five comparison models (likely retrieval strategy ablations) in the main text.

---

## Calibration Summary

**Round 1 bracket**: 5.5–7.0. The paper is clearly stronger than weak-band papers (2.0–3.0) and comparable to middle-band accepted papers.

**Round 2 anchors and comparisons**:
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/OALIb8oNfl.md` (5.75, R1, Accept): Tucker-based PEFT (FLoRA) — narrower scope (no new task/benchmark/CL), similar theoretical motivation. Paper under review is stronger.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/2oKkQTyfz7.md` (6.4, R1/R2, Accept): GSA-VLN — similar scope (new VLN task + benchmark + method). Comparable; paper under review has more ambitious continual learning setup and Tucker novelty, but GSA-VLN had complete experimental tables.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/n6mLhaBahJ.md` (6.75, R2, Accept): HAZARD — benchmark paper; paper under review has stronger methodological contribution but more evidential gaps.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/YR79EyejsG.md` (5.75, R1, Reject): Lifelong robot learning with retrieval — less comprehensive, overstated claims. Paper under review is stronger.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/tpUEqmjZiS.md` (4.5, R1, Reject): Lifelong robot skill learning — weaker contribution. Paper clearly above this.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/6yJuDK1DsK.md` (4.5, R1, Reject): Lifelong TTA with adapters — less comprehensive. Paper clearly above this.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/k9NYnsC4Mq.md` (5.67, R2, Reject): VLM continual learning — less novel, incremental. Paper under review more ambitious.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/sb7qHFYwBc.md` (6.5, R2, Accept): C-CLIP multimodal CL — comprehensive benchmark + method; paper comparable.

**Narrowing conclusion**: The paper sits between OALIb8oNfl (5.75, accepted, narrower) and HAZARD (6.75, accepted, benchmark-only). The missing averages for key baselines and the architectural validation gap are meaningful weaknesses that put it below GSA-VLN (6.4) and C-CLIP (6.5). Score: **5.5** — weak reject. The contribution is real and the ideas are sound, but the evidentiary completeness issues and the unvalidated core architectural claim are significant enough to warrant revision before acceptance.

---

**Originality**: High. Tucker-based multi-hierarchical adapter for lifelong VLN is novel.
**Importance**: Moderate-high. AML-VLN is a well-motivated problem for real deployments.
**Claim support**: Moderate. Core empirical claims hold for most tasks but Table 1 is incomplete for strongest competitors.
**Experimental soundness**: Moderate. Comprehensive baselines but key ablation (independent adapters) missing.
**Clarity**: Moderate. Figure 7 and Table 3 have presentation issues; formal definition is ambiguous.
**Value to community**: High. New benchmark + method + real-world experiments is a meaningful package.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>