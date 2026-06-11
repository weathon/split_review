## Summary

This paper proposes NuSA-CL, a memory-free continual learning method for CLIP that constrains low-rank (LoRA-style) weight updates to the approximate null space (low-energy singular directions) of each weight matrix, identified via SVD before each task. The update is merged back into the backbone after each task, maintaining a fixed parameter budget with no replay buffer or knowledge distillation. Experiments on the 11-task MTIL benchmark and class-incremental CIFAR-100 show NuSA-CL substantially outperforms other storage-free methods (LoRA, MiLoRA) and approaches storage-based SOTA at a fraction of the cost.

## Strengths

1. **Clean, well-motivated method with strong empirical results on storage-free CL.** NuSA-CL achieves 68.6% Transfer, 75.1% Avg, and 82.8% Last on MTIL (Table 1) with only 1.5M trainable parameters and zero additional storage, outperforming other storage-free methods (LoRA: 63.9/70.1/79.9; MiLoRA: 62.8/68.7/77.4) by a clear margin. The persistent null-space constraint is a conceptually clean and principled mechanism.

2. **Persistent constraint cleanly validated as critical via controlled ablation.** Table 4a shows that freezing the null-space bases (U_n, V_n) and training only M yields 75.08% Avg, while unfreezing them drops performance to 68.12% — a ~7pp decline. This cleanly distinguishes NuSA-CL from methods that only use the subspace for initialization (e.g., MiLoRA) and validates the core design choice.

3. **Long-sequence scalability demonstrated with widening advantage.** On CIFAR-100, the gap over ZSCL grows from +0.86pp (10-step) to +4.26pp (20-step) to +4.49pp (50-step) on Last accuracy (Table 3). This provides concrete empirical evidence that the dynamic null-space recomputation strategy compounds in effectiveness over longer streams.

4. **Insightful analysis of learning dynamics.** Figure 2 shows that NuSA-CL's effective rank increases progressively across tasks while LoRA and Full-FT remain static, providing direct evidence of knowledge accumulation rather than overwriting. The analysis further quantifies that even after 10 tasks, the most saturated layer retains 313+ null directions — more than double the update rank of 128.

5. **Practical efficiency quantified.** Table 4b reports SVD initialization at <1 min per task vs. InLoRA's ~81 min of data-dependent computation, while NuSA-CL achieves better accuracy and lower total training time (1.21 vs. 4.29 GPU-hours).

## Weaknesses

### Fatal
None.

### Major

1. **No uncertainty quantification across runs.** All tables report single-point estimates with no confidence intervals, standard deviations, or number of seeds. This is a significant evidential gap because (a) improvements over the best storage-free baselines (LoRA, MiLoRA) are moderate on some metrics; (b) per-task results in Table 2 show task-level ordering flips consistent with noise (e.g., DTD Transfer: 43.3 vs. 44.5; Flowers Last: 85.9 vs. 90.0); and (c) core ablation gaps (e.g., unfreezing V_n drops Transfer from 68.58 to 66.37) could fall within normal variability. Reporting results over 3–5 seeds would substantially strengthen the paper's competitive claims.

### Minor

2. **Theoretical bound is in parameter space, not function space.** Lemma 1 and Theorem 2 bound interference in Frobenius inner product between weight matrices, which does not guarantee small changes in model predictions on past tasks. The paper acknowledges this ("local stability condition rather than a full function-level guarantee," line 122), but the gap between parameter-space orthogonality and function-space preservation is central to continual learning. The theory should be more clearly presented as heuristic motivation rather than as a forgetting guarantee. A connection to function-space preservation via Lipschitz arguments would strengthen the presentation.

3. **Training hyperparameters not reported in the main text.** The main experiments do not report learning rate, batch size, optimizer, or scheduler — only "1000 training iterations per task" is mentioned for the ablation (line 254). These details are presumably deferred to the appendix (removed from the review copy), but the main text should summarize them for basic reproducibility.

4. **SVD cost for larger backbones is discussed but not analyzed.** The limitations section acknowledges SVD "could become a bottleneck for substantially larger models" and suggests truncated/approximate SVD, but no runtime breakdown is provided at the current ViT-B/16 scale to characterize what fraction of total compute SVD represents.

### Trivial
None.

## Nice-to-Haves

- Compare against methods with a tiny fixed-size rehearsal buffer (e.g., 1 example/class) to quantify the performance cost of being fully memory-free. The paper's storage-free vs. storage-based dichotomy is clean but leaves out the practical middle ground.
- Provide a runtime breakdown showing SVD's fraction of total compute at ViT-B/16 and a projection to larger backbones to substantiate the scaling concern.

## Removed Points

- "Zero storage overhead is slightly overstated" — REMOVED. The method stores U_n/V_n only transiently during training; these are discarded after merging. The claim is accurate.
- Table 1 boldface formatting complaint — REMOVED. The caption explicitly states boldface indicates top storage-free performer; this is clearly communicated.
- CIFAR-100 evaluation doesn't test "emerging classes" — REMOVED. The paper explicitly frames CIFAR-100 as testing "long-sequence scalability" (line 196), not learning genuinely novel classes. The abstract mentions "emerging classes" only in a real-world deployment context, not tied to this benchmark. The zero-shot numbers are reported transparently.
- Aircraft first-task "−" notation — REMOVED. Context makes it clear Aircraft is the first task; this is standard notation.
- Missing lightweight rehearsal baselines — MOVED to Nice-to-Haves. The paper explicitly scopes itself as storage-free; adding small-buffer methods would strengthen but is outside stated scope.
- Strength Finder: generic strengths about the problem being important — REMOVED. Only evidence-grounded strengths retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Report the main results (Tables 1–3 and Table 4a) over 3–5 random seeds with standard deviations or confidence intervals. This is the single highest-leverage improvement.
2. Clarify in Section 4 that the theoretical bound is a heuristic motivation and explicitly discuss the parameter-space to function-space gap, rather than describing it as a "bound" on forgetting.
3. Summarize training hyperparameters (learning rate, batch size, optimizer) in the main experimental setup section.

## Score and Decision

**Calibration:** Round 1 bracketing identified the paper as sitting in the (3.5, 7.5) range, above weak CLIP-CL papers (2.0–2.5) and below unrelated high-scoring papers (7.5+). Round 2 narrowing compared against the following anchors:

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| C-CLIP | sb7qHFYwBc.md | 6.50 (Accept) | R1/R2 | Most directly comparable; uses LoRA+distillation for CLIP CL. NuSA-CL has a cleaner core idea and better ablations, similar rigor level. Comparable quality. |
| TiC-CLIP | TLADT8Wrhn.md | 6.25 (Accept) | R2 | Benchmark paper for continual CLIP training. Different contribution type. NuSA-CL is a method paper of similar quality. |
| Spectral Regularization | Hcb2cgPbMg.md | 6.25 (Accept) | R2n | Thematically related (spectral approach to CL). NuSA-CL is more targeted and has cleaner mechanism validation. |
| PROOF | k9NYnsC4Mq.md | 5.67 (Reject) | R1/R2 | VLM CL with projections. NuSA-CL is clearly stronger (cleaner method, better ablations, stronger results). |
| CLIP Online CL | G9Ea7mlqGO.md | 3.80 (Reject) | R1 | CLIP online CL. NuSA-CL is substantially stronger. |

The paper sits slightly above TiC-CLIP (6.25) and the Spectral Regularization paper (6.25), comparable to C-CLIP (6.50), and clearly above PROOF (5.67). The core method is novel, well-motivated, and validated through careful ablations. The main weakness — absence of uncertainty quantification — is significant but not fatal, as the performance margins over storage-free baselines are clean and the mechanism ablations are decisive.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>