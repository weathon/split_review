Now I will write the final consolidated review.

---

## Summary

This paper introduces UniMoD, a task-aware token pruning method for unified multimodal transformers (models that handle both image generation and multimodal understanding in a shared parameter space). The key idea is to use separate routing modules per task—each with its own capacity and pruning strategy—rather than a single router for all tasks. The method is motivated by an empirical analysis of attention weights, ARank-based token redundancy, and task interactions across several unified transformer architectures. On Show-o (1.4B params), UniMoD reduces training FLOPs by ~15% while improving or maintaining most benchmarks; on Emu3 (8.5B params), it achieves a ~40% FLOPs reduction with comparable or slightly better scores.

## Strengths

1. **Substantial FLOPs reduction with maintained or improved performance.** Table 3 shows that UniMoD cuts training FLOPs from 51.1→43.3 TFLOPs on Show-o (15% reduction) and 89.0→53.5 TFLOPs on Emu3 (40% reduction) while achieving comparable or higher scores on several understanding and generation benchmarks (e.g., Show-o MME 1093.7 vs. baseline 1056.0; Emu3 GenEval 0.48 vs. 0.46). This provides direct evidence that the method delivers on its central efficiency–performance promise.

2. **Task-aware routing is clearly necessary; naive MoD collapses generation.** The ablation in Table 5 contrasts "Basic MoD" (single router, uniform pruning) with UniMoD: Basic MoD collapses generation quality (GenEval 0.15 vs. UniMoD's 0.61) while also underperforming on understanding (MME 960.6 vs. 1093.7). This demonstrates that the paper's core innovation—separate routers per task—is essential, not merely incremental.

3. **Systematic empirical analysis motivating the design.** Section 3 provides three complementary analyses: attention-weight patterns showing modality importance varies by task (Observation 1), ARank-based layer redundancy revealing both task- and layer-dependent redundancy (Observations 3–4), and a competitive token-pruning experiment showing generation tokens dominate under a shared router (Observation 5). These grounded observations directly motivate the task-aware design.

4. **Generality across diverse architectures.** The method is validated on Show-o (diffusion-based generation + autoregressive understanding) and Emu3 (fully autoreressive for both), and extended to pure diffusion transformers (DiT, PixArt) in the appendix. This breadth strengthens the claim that UniMoD is a general approach, not a one-off trick for a specific architecture.

5. **Controlled ablation of each component.** Table 5 compares UniMoD against variants that remove the layer-switch module or the task-aware router, with consistent pruning rates. The ablation confirms that both the layer selection and the task-specific routing contribute to the observed results, with the task-aware router being especially important for generation quality.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between the three-type MoD design and the actual experimental configuration.** The method section (Sec. 4.1) introduces three specialized MoD block types—T2I MoD, MMU MoD, and Shared MoD—and states that the layer switch module uses ARank to decide which type to use at each layer. However, the paper never explains how a layer gets assigned as T2I MoD vs. MMU MoD vs. Shared MoD. The three-step procedure described for the layer switch module (layer selection, pruning ratio estimation, token pruning) only determines *which* layers to convert and *how much* to prune, not *which block type* to use. The experimental section then says "we transform the last 12 layers into MoD layers for both tasks" (Sec. 5.1), which is consistent with Shared MoD only. It is unclear whether (a) all 12 layers are Shared MoD, (b) some are T2I MoD and some are MMU MoD according to ARank criteria, or (c) the three types are presented as a general design space but only Shared MoD is used in practice. This ambiguity undermines the reproducibility of the method and inflates the claimed architectural contribution. **Fix:** Clearly state which MoD block types are used in the experiments, how the assignment is made, and whether the three-type design is fully implemented or partially simplified.

2. **No ablation on Emu3.** The ablation study (Table 5) is performed only on Show-o. For Emu3—where the larger 40% FLOPs reduction is achieved—there is no controlled experiment isolating the effect of the task-aware router or the layer-switch module. Without this, the reader cannot determine whether the 40% savings on Emu3 come from the task-aware design or simply from the high token redundancy in Emu3's 4096-token image representations (which the paper itself notes). **Fix:** Add at minimum the "w/o task-aware router" ablation on Emu3, or explicitly justify why it cannot be run.

3. **No error bars or statistical significance.** No results are reported with multiple runs or variance estimates. Several benchmark differences are small enough to be within typical noise levels (e.g., Emu3 GQA 45.2 vs. 46.0 baseline, Show-o ablation GQA 54.4 vs. 54.5). Without confidence intervals, it is impossible to assess whether UniMoD's improvements/drops are significant or simply noise. This is especially important for the understanding metrics where the improvements over the "w/o task-aware router" ablation are modest. **Fix:** Provide at least 2–3 runs with standard deviation for key comparisons, or discuss the known variance of each benchmark.

### Minor

1. **Table 1: GQA=0.0 for layer 3 is unexplained.** Skipping layer 3 during inference produces a GQA score of 0.0—a striking result that is never commented on. If skipping a single early layer truly collapses understanding performance to random chance, this is a strong finding that warrants discussion. If it is an artifact (e.g., a specific module in layer 3 that breaks the computation when removed), that too should be clarified. As presented, it undermines confidence in the analysis.

2. **Standard MoD baselines relegated to ablation only.** The main results table (Table 3) compares UniMoD only against "Interleaved Layer" and "EarlyExit"—both trivial baselines. The more informative comparison—a standard single-router MoD with the same layer selection (the "w/o task-aware router" variant in Table 5)—is absent from the headline table. While the ablation table contains these numbers, a reader scanning the main results cannot directly see how UniMoD compares to a straightforward MoD baseline. The paper would be strengthened by moving the single-router comparison to Table 3.

3. **Inconsistent connection between Top-K pruning and threshold δ_t.** Equation (4) uses a threshold δ_t for each task, but the layer switch module description (Sec. 4.1 step 3) says "each router assigns scores to tokens and retains the Top-K tokens with the highest scores, where K is determined by the pruning ratio." These are two different selection mechanisms. The relationship between δ_t and the Top-K procedure is not explained. If δ_t is unused in practice, the equation is misleading.

4. **Emu3 baseline discrepancy.** The paper acknowledges that the Emu3 baseline results differ from the original Emu3 paper (due to using LLaVA-v1.5-mix-665K instead of the original training data), but the gap is not quantified. The original Emu3 reports GenEval 0.66; the baseline here reports 0.46. This 0.20 gap deserves a brief discussion so readers can calibrate whether UniMoD's 0.48 is meaningfully recovering lost performance or simply staying close to a weaker baseline.

### Trivial

- Table 1 header says "layer" but should clarify these are the odd-numbered layers being individually skipped.
- The ARank-based pruning ratio estimation ("normalizing its ARank score by the sequence length") could use a formula for clarity.
- The term "IMM" appears in Table 5 header without explanation (likely a typo for "MME").

## Nice-to-Haves

- **Per-task efficiency breakdown.** A breakdown of how many tokens are processed per task per layer would help visualize where the savings come from and how the task routers differ in their pruning patterns.
- **Overhead of additional routers.** The method adds one or two routers per MoD layer. The paper does not measure the extra parameters, FLOPs, or memory introduced by the routers themselves. While likely negligible, this should be stated explicitly.
- **Failure analysis / limitations.** The paper would benefit from discussing scenarios where task-aware routing might hurt (e.g., when token redundancy is low for both tasks, or when Shared MoD layers produce conflicting pruning decisions).

## Removed Points

These points were raised by reviewers but are removed for the reasons given:

- **"Baseline comparisons are unfair"** (Harsh Critic point 2): The claim that comparisons are "unfair" overstates the issue. The "Basic MoD" and "w/o task-aware router" variants *are* included in the ablation table (Table 5) with consistent pruning rates. Whether they belong in the main table is a presentation judgment, not a fairness concern. The asymmetry of FLOPs between variants is also noted by the authors. **Removed** because the criticism mischaracterizes a presentation choice as unfairness.
- **"Table 2 task interaction experiment is too vague to assess"** (Harsh Critic, Section-by-section notes): The experiment is simple but sufficient to support its claim ("joint training does not hurt individual task performance"). The three conditions (joint, only MMU, only T2I) are clearly described and the results are unambiguous. The critic's concern about "freezing or removing generation heads" is speculation not supported by what the paper actually states. **Removed** as a strawman.
- **"The paper would be strengthened by discussing scenarios where the method might hurt performance"** (Harsh Critic, Missing Parts): This is a generic suggestion applicable to nearly any paper. It is not a specific weakness of this paper's execution.
- **All formatting, typo, and missing-appendix complaints**: These are parser/stripping artifacts, not author errors, per the hard rules.
- **"ARank may depend on sample diversity"** type concerns: These are generic methodological speculation, not specific identified problems in the paper.
- **Strength Finder's generic strengths** ("the paper tackles an important problem", "the paper is well-structured"): Dropped as generic/superficial. Only concrete, evidence-grounded strengths are retained.
- **Strength that "each component is validated by controlled ablation"**: Kept as a minor strength but not listed as a core strength since the ablation is only on Show-o.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the mapping from the three-type MoD design to the experiments.** Specifically: (a) state explicitly which MoD block types are used in the Show-o and Emu3 experiments, (b) if all MoD layers are Shared MoD, explain why the three-type architecture is presented as part of the method, and (c) if the three-type design is used, explain how ARank informs the type assignment.
2. **Add the "w/o task-aware router" ablation for Emu3.** This is the most critical missing experiment. Without it, the Emu3 results cannot be attributed to the task-aware design.
3. **Add error bars or discuss known benchmark variance** for at least the main comparisons (Table 3) and key ablations (Table 5).
4. **Move the single-router MoD baseline** from the ablation table to the main results table (Table 3) to make the advantage of task-aware routing immediately visible.
5. **Discuss the GQA=0.0 result in Table 1** and either explain the phenomenon or correct a potential artifact.

---

## Score and Decision

### Calibration

**Round 1 (Bracketing):** The paper was queried against three bands. Weak anchors (avg < 3.5) included PyramidDrop (3.00) and A-MoD (4.00). Middle anchors (3.5–7.5) included γ-MoD (6.67), Denoising Task Routing (7.33), and A-MoD routing (4.00). Strong anchors (>7.5) were mostly unrelated (MMIE at 8.00, MoE++ at 8.00). Round-1 bracket: **[4.5, 6.5]**.

**Round 2 (Narrowing):** Inside the bracket, the most comparable anchor was γ-MoD (6.67, Accept), which also uses ARank-guided MoD for multimodal LLMs. UniMoD addresses a harder problem (unified generation+understanding) and contributes task-aware routing, but is less clear in method specification and has weaker ablation coverage. Other anchors: LLM-VTP (5.80, Reject), SM⁴ (5.25, Reject), PUMA (4.75, Reject), and Unified Multimodal Discrete Diffusion (5.75, Reject). UniMoD is stronger than the 4–5 range papers and comparable to papers in the 5–6 range, but is clearly weaker than γ-MoD (6.67).

**Final calibration:** The paper sits between the 5–6 range anchors. The core contribution (task-aware routing for unified transformers) is novel and the FLOPs reductions are impressive, but the method clarity gap and missing Emu3 ablation prevent it from reaching the 6+ level of γ-MoD. Within the 4.5–6.5 bracket, the paper is below the upper anchor (γ-MoD at 6.67) and above the lower anchors (4–5 range). Score: **5.5**.

All anchors retrieved:
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| 5ncdKonxd4 (PyramidDrop) | 3.00 | 1 | Weaker: VLM token reduction without the unified-model setting |
| IqGVIU4rvM (VQ-VAE+Diffusion) | 2.50 | 1 | Unrelated: visual tokenizer paper |
| vlOfFI9vWO (MARL token selection) | 3.00 | 1 | Weaker: RL-based token selection for ViT |
| cagNCwQEEN (Hybrid SSM MLLM) | 3.40 | 1 | Weaker: instruction tuning, not token pruning |
| jIAKjjEmWi (A-MoD routing) | 4.00 | 1 | Weaker: narrower scope (routing only, no task awareness) |
| MY0qlcFcUg (Denoising Task Routing) | 7.33 | 1 | Stronger but different domain (diffusion routing) |
| tI3eqOV6Yt (Hyper-UT) | 5.00 | 1 | Comparable but different task (pointer value retrieval) |
| q44uq3tc2D (γ-MoD) | 6.67 | 1,2 | Stronger: clearer method, more comprehensive MoD for MLLMs |
| uAFHCZRmXk (Modality Gap) | 8.00 | 1 | Unrelated: VLM analysis paper |
| HnhNRrLPwm (MMIE) | 8.00 | 1 | Unrelated: benchmark paper |
| SI2hI0frk6 (Transfusion) | 7.60 | 1 | Unrelated: new model architecture paper |
| t7P5BUKcYv (MoE++) | 8.00 | 1 | Unrelated: MoE framework |
| l2izo0z7gu (OmniBind) | 6.25 | 2 | Stronger in clarity but different domain (representation learning) |
| bIHyMpzeuI (SM⁴) | 5.25 | 2 | Comparable: similar method clarity issues, MoE domain |
| zyBJodMrn5 (Multimodal generalization) | 5.67 | 2 | Comparable but different topic (generalization analysis) |
| SfZpk8CV9l (PUMA) | 4.75 | 2 | Weaker: less clear contribution, unified MLLM generation |
| Acdd83rF1s (LLM-VTP) | 5.80 | 2 | Comparable: token pruning with similar issues (sensitivity, no error bars) |
| oS79Tw3G0c (VAS) | 5.75 | 2 | Comparable: visual token pruning for VLMs |
| FlvtjAB0gl (Unified LV pretraining) | 6.25 | 3 | Stronger: clearer contribution in unified pretraining |
| QyNN5n37nK (Unified Discrete Diffusion) | 5.75 | 3 | Comparable: similar scope (unified multimodal) but different approach |
| 0Nui91LBQS (SEED Tokenizer) | 6.33 | 3 | Stronger: clearer contribution in unified tokenizer |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>