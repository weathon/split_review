## Summary
UniMoD proposes a task-aware token pruning method for unified multimodal transformers (models handling both image generation and understanding in a shared parameter space). Rather than applying a single Mixture-of-Depths (MoD) router to all tasks uniformly, UniMoD assigns separate routers per task, guided by an empirical analysis of attention weight patterns, layer-wise token redundancy (ARank), and inter-task competition. The method is applied to Show-o (diffusion + autoregressive) and Emu3 (fully autoregressive), achieving 15% and 40% FLOPs reductions respectively, with ablation studies confirming that both the task-aware router and the layer-switch module are essential.

---

## Strengths

- **Thorough empirical motivation via multi-model analysis (Figures 2–4, Table 1):** The paper presents three complementary diagnostic experiments across four unified models. Figure 2 shows task-dependent attention weight patterns (image vs. text tokens flip dominance between T2I and MMU). Figure 3 demonstrates via ARank that generation sequences have higher ARank (less redundancy) than understanding sequences in Show-o and JanusFlow — directly motivating separate routers. Figure 4 uses a Gumbel-Softmax competition experiment to confirm that T2I tokens dominate under a shared router, explaining the failure mode.

- **Ablation studies isolate component contributions quantitatively (Table 5):** The ablation on Show-o cleanly shows each component matters. Basic MoD collapses generation (GenEval 0.15 vs. 0.61); removing the layer-switch module hurts MME heavily (920.3 vs. 1093.7); removing the task-aware router severely degrades generation (GenEval 0.50 vs. 0.61). These are large, consistent gaps — not noise — and credibly establish that both the layer selection and task-specific routing are necessary.

- **Practical training cost improvements demonstrated, particularly at larger scale (Table 4, Section 5.2):** For Emu3 (8.5B, 4096 image tokens/image), actual training iteration time improves from 3.56×/iter to 2.80×/iter (~21% speedup), consistent with the 40% FLOPs reduction. The explanation for why gains are larger at scale (more tokens → more redundancy) is plausible and directly grounded in model design differences.

- **Layer importance experiment grounds pruning decisions (Table 1):** Inference-time layer-skipping on Show-o shows that early layers (1, 3) cause catastrophic GQA drops (35.0, 0.0) while late layers (17–23) are recoverable (~51.5 → 50.9), directly justifying the design of only converting later layers into MoD blocks.

---

## Weaknesses

### Fatal
None.

### Major

- **Main results table (Table 3) uses only naive baselines, with the most informative comparison (single-router MoD) relegated to ablation at a different FLOP budget.** The paper's central claim is that *task-aware* routing outperforms *task-agnostic* routing. This claim is substantiated in Table 5 ("w/o task-aware router": GenEval 0.50 vs. 0.61), but this ablation runs at 40.8 TFLOPs vs. UniMoD's 43.3 TFLOPs — different compute budgets. Table 3, the primary results table, only compares against Interleaved Layer Skipping and Early Exit, both admittedly naive approaches that fail catastrophically (Early Exit GenEval: 0.26; Interleaved: 0.29). A direct comparison against a single-router MoD at matched FLOPs in the main table would substantially strengthen the core claim.

- **The Emu3 baseline is a re-implemented model trained on substitute data, limiting what the comparison proves.** Section 5.1 discloses that official Emu3 training data is unavailable, so both the Emu3 "baseline" and UniMoD-Emu3 are trained on LLaVA-v1.5-mix-665K and Show-o T2I data. The paper acknowledges this and notes results differ from the original paper. The internal comparison (substitute Emu3 vs. UniMoD on same data) is methodologically fair for showing that pruning doesn't hurt, but the numbers cannot be compared to published Emu3 figures. The framing in the abstract ("maintaining or improving performance") should be more precisely bounded to the substitute-data setting.

### Minor

- **Task-aware routing is applied to Emu3 despite the paper's own analysis showing similar inter-task redundancy.** Section 3.3 explicitly states: "Lumina-mgpt and Emu3 exhibit similar redundancy levels across both tasks," attributing this to their fully autoregressive architecture. Yet UniMoD is applied to Emu3 with task-specific routers and 80% pruning in the last 16 layers. The paper does not discuss whether task-aware routing provides additional benefit over uniform pruning in this case, or whether the large FLOPs reduction for Emu3 is simply due to aggressive total pruning rather than task differentiation. This gap weakens the evidential chain between the analysis and the Emu3 application.

- **Show-o wall-clock improvement is marginal relative to the FLOPs reduction headline.** Table 4 reports Show-o training speed as 1.30×/iter → 1.27×/iter (T2I) and 1.25×/iter (MMU) — a ~2–4% actual speedup despite 15% FLOPs savings. The paper attributes this to routing overhead and the relatively small token count in Show-o (1024 vs. 4096 per image for Emu3), which is an honest explanation, but the practical efficiency story for Show-o is weak. The paper foregrounds the FLOPs number without adequately contextualizing the wall-clock gap.

- **Pruning ratio estimation heuristic (ARank / sequence length) is not ablated against alternatives.** The layer-switch module determines per-layer pruning ratios by normalizing ARank by sequence length (Section 4.1, Step 2). This is presented as a reasonable approximation, but no comparison to simpler alternatives (e.g., uniform ratio across selected layers, or learned per-layer ratios) is provided. Since this heuristic drives a key design choice, even a brief sensitivity analysis would strengthen confidence in it.

### Trivial
- Some claims about "maintaining or improving performance" in the abstract could be more precisely qualified. On Show-o, GQA drops from 56.3 to 54.5 and VQAv2 from 68.3 to 66.2 — bounded losses, but selective characterization without acknowledgment may mislead readers.

---

## Nice-to-Haves
- Report variance across runs for GenEval and DSG-1K where baseline vs. UniMoD differences are small (e.g., GenEval 0.62 → 0.61 on Show-o).
- For Emu3 specifically, a brief discussion or small ablation comparing single-router MoD to task-aware routing would clarify whether task differentiation is driving the Emu3 result or simply the volume of pruning.
- A brief sensitivity analysis on the ARank-normalized pruning ratio heuristic vs. uniform pruning ratio assignment.

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "The claim in the abstract…cannot be supported by this table"** — Overstated. The Emu3 baseline and UniMoD-Emu3 use the same substitute datasets, making it a valid internal comparison. The abstract's "maintaining or improving performance" refers to benchmarks where improvements do appear (GenEval, DSG, MME for Emu3). The framing is selective but not unsupported. Demoted to a minor note about framing precision rather than a fatal claim.

- **Harsh Critic: MoMa comparison relegated to appendix should be in main table** — The paper explicitly describes MoMa as a simplistic application without unified-transformer-specific design (Section 2.2), and the ablation in Table 5 already provides the more principled single-router comparison. The Appendix A.9 comparison to MoMa is an appropriate placement for a related-work reference comparison. Not a core weakness.

- **Strength Finder: "Training cost improvements extend beyond FLOPs (Table 4)"** listed as a supporting strength — Partially in tension with the verified weakness that Show-o's wall-clock improvement is only 2–4%. Kept only in the context of Emu3 where the speedup is meaningful.

- **Harsh Critic: Inference-skip experiments ≠ training-time MoD decisions** — The concern that inference-time layer skipping (Table 1) may not directly inform training-time layer selection is raised. While this gap is real in principle, the ARank analysis (Figure 3) provides the more direct training-time evidence for layer selection. Table 1 serves as an independent corroborating signal. Not substantive enough to retain as a weakness.

---

## Novel Insights

The paper's most genuinely novel observation is the Gumbel-Softmax competitive routing experiment (Figure 4), which provides a direct empirical demonstration of task imbalance under a shared router: T2I tokens nearly always win out, explaining why generation quality collapses under single-router MoD. This is a cleaner diagnostic than simply comparing task-agnostic vs. task-aware pruning outcomes, and it offers a reusable methodology for diagnosing token importance imbalances in other mixed-task transformers. The multi-model ARank analysis (Figure 3) also offers a useful insight: the degree to which task-aware routing is necessary likely scales with how distinct the task modeling approaches are (diffusion vs. autoregressive → more benefit; autoregressive + autoregressive → less benefit), which has practical implications for when to apply UniMoD-style routing vs. simpler uniform pruning.

---

## Suggestions

1. **Add a single-router MoD row to Table 3 at matched FLOPs** — The ablation in Table 5 already contains the "w/o task-aware router" entry; running it at the same FLOP budget as UniMoD (43.3 TFLOPs) and including it in Table 3 would make the core claim self-contained in the main results.
2. **Explicitly reframe the Emu3 result** — State clearly that the comparison is between two models trained on the same substitute data, and frame the result as: "40% FLOPs reduction incurs ≤X% degradation on substitute training data." This is still a strong result and avoids misleading readers who compare to published Emu3 figures.
3. **Discuss the Emu3 task-homogeneity puzzle** — Add a paragraph explaining why task-aware routing is still applied to Emu3 despite similar inter-task ARank, and whether the benefit comes from task balancing or simply enabling a higher total pruning ratio. This would complete the analysis-to-method chain.
4. **Add wall-clock context when leading with FLOPs numbers for Show-o** — Acknowledge upfront in Section 5.2 that the 15% FLOPs reduction in Show-o translates to ~2–4% wall-clock speedup and explain why (routing overhead, small token count), rather than letting the reader discover this in Table 4.

---

## Score and Decision

**Originality (3/5):** Task-aware MoD for unified transformers is a targeted, incremental but sensible extension. The Gumbel-Softmax competition diagnostic is creative; the overall framing is standard.

**Importance (3/5):** Training efficiency for unified multimodal transformers is a relevant and timely problem; gains are real but modest for Show-o.

**Claims supported (3/5):** Core claims are mostly supported for Show-o, with caveats about the Emu3 data mismatch and selective performance reporting. Ablations are credible.

**Soundness (3/5):** Methodology is reasonable; the layer selection heuristic and the Emu3 task-homogeneity inconsistency are unresolved but not fatal.

**Clarity (4/5):** Paper is well-organized, analysis is presented clearly, and experimental setup is accessible.

**Community value (3/5):** Useful empirical toolkit (ARank multi-model study, competition experiment) and a practical method that could benefit practitioners training unified models.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>