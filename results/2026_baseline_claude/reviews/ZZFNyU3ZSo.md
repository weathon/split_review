## Summary
UniMoD proposes a task-aware token pruning method for unified multimodal transformers that handles both generation and understanding tasks in a shared parameter space. Motivated by an empirical analysis of attention weight patterns, layer-wise token redundancy (using the ARank metric), and task interactions across four unified models (Show-o, JanusFlow, Emu3, Lumina-mgpt), the authors identify that different tasks exhibit distinct redundancy profiles across layers. They extend Mixture of Depths (MoD) by introducing per-task routers with task-specific capacities determined by ARank-guided layer selection, reducing training FLOPs by ~15% for Show-o and ~40% for Emu3 while maintaining or slightly improving benchmark performance.

---

## Strengths

- **Systematic empirical analysis grounding the design**: The authors examine four unified models across three complementary lenses—attention weight distributions, ARank-based redundancy, and competitive token-selection experiments. Concrete data (Figs. 2–4, Tab. 1–2) supports each of the five observations and each observation maps directly to a design choice, giving the method a principled rather than heuristic origin.

- **Strong Emu3 result**: On the larger, fully-autoregressive Emu3 (8.5B params, 4096 image tokens/image), UniMoD achieves a 40% FLOPs reduction (89.0 → 53.5 TFLOPs) while matching or exceeding the baseline on all benchmarks (MME, GenEval, DSG, CLIP score). The larger token count amplifies redundancy, making the efficiency gain compelling and well-explained.

- **Clear ablation confirming each component**: Table 5 isolates the layer switch module and the task-aware router separately. The task-aware router provides the largest performance gain (especially for T2I: GenEval jumps from 0.50 to 0.61), and the layer switch module provides additional improvement, validating the design hierarchy.

- **Breadth and generality**: The method is validated across both hybrid (diffusion+AR) and fully-AR unified transformers, and extensions to pure diffusion models (DiT, PixArt) are described, demonstrating architectural generality beyond the primary setting.

---

## Weaknesses

### Fatal
None.

### Major

1. **Modest FLOPs savings on Show-o with concurrent degradation on some benchmarks**: The flagship Show-o result achieves only 15% FLOPs reduction (51.1 → 43.3 TFLOPs). Moreover, several MMU metrics show clear drops: GQA falls from 56.3 to 54.5, VQAv2 from 68.3 to 66.2, and MMMU from 25.8 to 25.7. The improved MME (1056.0 → 1093.7) and POPE (79.8 → 80.3) do not fully compensate. Presenting mixed results as "maintaining or improving performance" may overclaim relative to what the data shows.

2. **The Emu3 baseline is confounded**: The paper acknowledges that official training data and code for Emu3 are not released, so a custom dataset (LLaVA-v1.5-mix-665K + Show-o T2I data) is used for both the baseline and UniMoD. The baseline Emu3 scores (MME: 881.3, GQA: 46.0) are substantially below the original paper's reported performance, indicating the baseline is undertrained relative to the published model. The 40% FLOPs claim is thus measured against a weakened baseline, not the production model, reducing the claim's impact.

3. **The main comparison lacks a properly tuned single-router MoD at the same selected layers**: The baselines in Table 3 (Interleaved Layer Skipping, EarlyExit) are weak straw-men. The most informative comparison—a single-router MoD applied only at the ARank-selected layers with the same total compute budget—appears only in the ablation as "w/o task-aware router." Promoting this to the main results table would make the benefit of task-awareness more credible.

### Minor

1. **Layer switch module heuristic is weakly justified**: The procedure of normalizing ARank by sequence length to estimate pruning ratios is ad hoc and evaluated only indirectly. No sensitivity analysis to the number of samples (50 per task) or the threshold (bottom half of layers by ARank) is provided in the main paper.

2. **MMMU scores near random chance**: All Show-o variants score around 25–26 on MMMU (chance ≈ 25% on 4-way MC), making this benchmark uninformative for discriminating between methods in this setting. Reporting it without qualification may mislead readers about model competence on this task.

3. **Inference efficiency not fully characterized in the main paper**: Inference FLOPs and latency changes from UniMoD are deferred entirely to Appendix A.4. Given that training efficiency and inference efficiency may diverge (e.g., the router adds overhead at inference), characterizing at least the inference FLOPs delta in the main paper would strengthen the practical argument.

### Trivial

- "UniMod" (Tables 3, 4, 5) vs. "UniMoD" (title, abstract, method section) is an inconsistency throughout the paper.

---

## Nice-to-Haves

- A sensitivity study of the ARank-based layer selection threshold (e.g., selecting the bottom third vs. bottom half of layers by ARank) would help practitioners adapt the method without re-running the full analysis.
- Reporting wall-clock training time reduction (not just FLOPs) for both models on consistent hardware would make the practical benefit more concrete.
- Showing performance at multiple FLOPs budgets (a Pareto curve in the main paper) would make the efficiency–performance trade-off easier to evaluate and situate relative to the baselines.

---

## Novel Insights

The competitive token pruning experiment in Section 3.4—where T2I and MMU tokens literally compete for selection slots via a Gumbel-Softmax router—is an elegant diagnostic that directly reveals asymmetric cross-task importance in a single experiment. The finding that generation tokens almost entirely crowd out understanding tokens (Fig. 4) provides a concrete mechanistic explanation for why naive shared-router MoD fails in unified transformers, going beyond the more indirect ARank analysis. This design of "competition as a diagnostic" for multi-task token importance is a transferable methodology that could inform future work on multi-task efficiency.

---

## Suggestions

- Reframe the Show-o results more carefully: since GQA and VQAv2 decline, consider presenting a table that explicitly shows per-benchmark delta (Δ) from baseline rather than absolute scores, and report the harmonic mean or aggregate score to give an honest overall picture.
- Include a single-router MoD at ARank-selected layers as an explicit baseline in Table 3 (currently only in the ablation), to cleanly demonstrate the value of task-awareness independently of the layer selection strategy.
- Provide a brief characterization of inference cost impact in the main text—even a two-row table showing inference TFLOPs with and without UniMoD would suffice.

---

## Score and Decision

The paper addresses a timely and underexplored problem (efficient training of unified multimodal transformers), grounds its method in principled analysis, and produces solid empirical results especially on Emu3. The task-aware MoD framing is a natural and useful generalization. The main weaknesses are a modest FLOPs gain on Show-o with mixed per-benchmark results, a confounded Emu3 baseline, and an incomplete comparison in the main results table. These concerns are significant but do not invalidate the contribution. The paper provides a useful and reproducible framework for practitioners working on unified models.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>