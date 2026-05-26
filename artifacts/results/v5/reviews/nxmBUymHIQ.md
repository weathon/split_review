Now I have enough context. Let me compose the final review.

## Summary

The paper introduces LoLoRA, a LoRA fine-tuning variant that updates the A matrix using local unsupervised rules (Hebbian PCA, HPCA) during the forward pass instead of backpropagation, avoiding the need to store activations for A's gradient. The authors provide theoretical justification (Theorem 4.4) showing that the optimal frozen A spans the principal subspace of the input covariance, motivating the use of HPCA which converges to that subspace. Experiments on GLUE, math reasoning (MetaMathQA→GSM8K), multimodal fine-tuning (LLaVA), and ablations on TinyLlama demonstrate LoLoRA achieves competitive performance compared to standard LoRA and LoRA-FA baselines, with memory savings of 13% on an 8B model.

## Strengths

- **Theoretical characterization of optimal A initialization (Theorem 4.4).** The paper proves that, under reasonable simplifying assumptions (Gaussian random regression target), the optimal frozen A matrix spans the top principal subspace of the input covariance. This provides a principled justification for using PCA-based initialization (EVA) and explains why HPCA (which converges to the same subspace) is a natural choice for local updates. The asymmetry result (Theorems 4.4 vs 4.5, showing A benefits from informed initialization but B does not) is a clean analytical insight that directly supports the hybrid design.

- **Comprehensive evaluation across diverse tasks and model scales.** The paper tests on 8 GLUE tasks (RoBERTa-large), mathematical reasoning (LLaMA-3.1-8B), multimodal instruction tuning (LLaVA-v1.5-7B), and detailed ablations (TinyLlama-1.1B). This breadth establishes that the method generalizes across NLU, reasoning, and vision-language domains, and at model sizes from 350M to 8B parameters.

- **Well-designed ablation study comparing local rules.** Table 6 systematically compares five local update rules (HPCA variants, AE, SoftHebb) and shows that HPCA converges to a PCA-like subspace regardless of initialization, matching LoRA-FA with EVA initialization. This confirms the core design choice is sound and the method is robust to the choice of local rule within the class of subspace-tracking algorithms.

- **Clear exposition of the method and the memory-saving mechanism.** Algorithm 1 and Figure 1 clearly illustrate how LoLoRA updates A during the forward pass, frees the input activations, and avoids backprop through A. The paper is well-structured and the main ideas are easy to follow.

## Weaknesses

### Major

- **Central claimed advantage — online adaptation to input distribution shifts — is not tested.** The abstract and introduction tout that LoLoRA "allows it to adapt to input distribution shifts" via its local updates. However, no experiment is designed to test this claim. In every setting (GLUE, math, multimodal, ablations), LoLoRA achieves performance comparable to LoRA-FA with EVA initialization, which freezes A after a one-time PCA precomputation. The paper never evaluates a scenario where the input distribution actually shifts during fine-tuning (e.g., non-stationary data ordering, domain shift, or sequential task fine-tuning). Without such experiments, the "adaptation" framing is speculative. The method may still be useful (avoiding the separate PCA pass), but the paper's headline claim is unsupported.

- **The method does not outperform a well-initialized frozen baseline.** Across all experiments, LoLoRA performs similarly to or slightly worse than LoRA-FA with EVA initialization. On GLUE (Tables 1–2), LoLoRA is numerically below LoRA-FA (EVA) on 5 of 8 tasks. On math reasoning (Table 3), both tie at 0.829. On LLaVA (Table 4), LoLoRA's perplexity is 2.93 vs LoRA-FA (EVA)'s 2.92, and LoLoRA uses 0.2 GB more memory (24.1 vs 23.9 GB). In the ablation (Tables 5–6), LoLoRA HPCA (r=8) achieves 2.535 perplexity vs LoRA-FA (EVA) 2.536 — essentially identical. This pattern undermines the paper's implicit claim that online updates provide a meaningful benefit over a strong fixed initialization.

- **Theory does not cover the online training dynamics.** Theorem 4.4 characterizes the optimal *frozen* A for a *frozen-A* regression problem under i.i.d. Gaussian random targets. LoLoRA, by contrast, updates A online via HPCA while the input distribution shifts because earlier layers change during fine-tuning. The step from "optimal frozen A" → "online HPCA updates during coupled training with B" is heuristic, not rigorous. The paper acknowledges this as a limitation in the conclusion, but the central narrative (Sections 1, 4) presents the theory as if it directly explains why LoLoRA works. The gap between the theoretical assumptions (isolated layer, stationary input, Gaussian regression target) and the actual setting (non-linear, cross-layer, non-stationary fine-tuning) is significant.

- **The memory savings are not unique to LoLoRA.** The memory reduction over standard LoRA comes from not storing activations for A's gradient, which is entirely due to freezing A (or equivalently, avoiding backprop through A). LoLoRA and LoRA-FA have nearly identical memory footprints (Table 3: both 26 GB; Table 4: 24.1 vs 23.9 GB). LoLoRA actually adds small optimizer state for the local updates, making it marginally more memory-hungry than LoRA-FA. The paper should clearly distinguish the memory benefit shared with all frozen-A methods from what is novel to LoLoRA.

### Minor

- **The "up to 20% memory reduction" claim in the GLUE summary is not borne out by the reported numbers.** The paper states this in the GLUE summary with a reference to Appendix D. The main-text numbers show 13% for LLaMA-3.1-8B and ~2–3% for LLaVA-7B. (Assuming Appendix D substantiates the 20% figure in some setting, the main text should at minimum contextualize which setting yields 20%.)

- **The concrete local update rule (HPCA/SNL) should be defined in the main method section (Section 3), not only in the ablation (Section 5.4).** Algorithm 1 uses `LocalRule(A, z, u)` as an abstract placeholder; the reader must go to Section 5.4 to learn that this is the Subspace Network Learning algorithm with running mean subtraction (smoothing factor 0.98). Providing the explicit update in Section 3 would improve reproducibility.

- **The paper claims "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups" (Conclusion), but the GLUE results (Tables 1–2) show LoLoRA is numerically below LoRA-FA (uniform) on most tasks.** This statement is technically true (better on math and multimodal, worse on GLUE) but "consistently outperforms" is misleading given the GLUE comparison.

- **Hyperparameters for the local rule (HPCA learning rate, smoothing factor) are not reported in the main text.** Their sensitivity is not discussed.

- **The method's scope limitation for wide layers is not mentioned.** For very wide layers (e.g., large MLP intermediate projections) where the input dimension n is large and rank r is small, the memory savings from not storing the input for A's gradient may be negligible. The paper should discuss this.

### Trivial

- None beyond presentation issues introduced by the parser.

## Nice-to-Haves

- A comparison to activation checkpointing (gradient checkpointing for the LoRA path) would help contextualize the memory savings.
- An experiment simulating distribution shift (e.g., training on permuted data ordering, or fine-tuning on a sequence of tasks) would directly test the adaptation claim.
- A controlled comparison where A is initialized with EVA and then also updated with HPCA vs frozen would isolate the benefit of online updates from the benefit of good initialization.

## Removed Points

- **"20% memory claim unsupported"** — The paper references Appendix D for this figure; since the appendix is stripped by the parser but exists in the original submission, criticism about missing appendix content is removed per policy. The retained Minor weakness above notes the discrepancy between the "up to 20%" claim and the numbers reported in the main text.

- **"Missing related works"** — Removed per policy; I cannot verify the existence or absence of cited works.

- **"Memory measurement methodology unclear"** — The paper defines "peak extra GPU memory" in the caption of Table 4 ("the difference between the peak allocated memory and the memory required to store the frozen base model parameters in bfloat16"), which is clear enough.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the contribution around the practical benefit.** The main advantage of LoLoRA over LoRA-FA (EVA) is that it avoids the separate PCA precomputation pass, saving wall-clock time while achieving similar performance. This is a real, practical contribution. The current framing around "adaptation to input distribution shifts" is not supported and draws attention away from what the method demonstrably achieves.

2. **Add an explicit distribution-shift experiment.** For example, train on a subset with one data ordering and evaluate on held-out data with a different ordering, or simulate a continual fine-tuning scenario. If LoLoRA outperforms LoRA-FA (EVA) under such conditions, the adaptation claim would be validated.

3. **Define the HPCA update explicitly in Section 3.** The method section should state the SNL update rule and mention the running mean subtraction, not defer this to the ablation section.

4. **Provide a clear breakdown of memory savings.** Show how much memory is saved by not storing z for A's gradient vs. the small overhead from the local optimizer state, and clarify which setting achieves the 20% reduction referenced in the text.

5. **Tone down the comparative claims.** Statements like "consistently outperforms standard LoRA-FA" should be replaced with more precise descriptions (e.g., "achieves comparable or slightly better performance than LoRA-FA with uniform initialization, and is competitive with LoRA-FA (EVA) without requiring the separate PCA pass").

## Score and Decision

Based on comparative calibration with human-reviewed anchor papers:

| Anchor | Avg Score | Round & Query | Comparison |
|--------|-----------|--------------|-----------|
| LoRA-FA (RbKThNNFxr) | 5.33, Reject | R1-topic-mid | Simpler method with similar memory savings; LoLoRA adds theory and local updates but the core contribution over this baseline is modest |
| EVA (DM6Q45HWSk) | 4.75, Reject | R2-weakness | Directly related; LoLoRA provides the theoretical justification EVA lacked, but shares its limitation (marginal gains, contribution not clearly demonstrated) |
| ALLoRA (7X65yoKl3Y) | 3.33, Reject | R1-topic-low | Different LoRA variant; LoLoRA has better experiments and clearer theory but both overclaim relative to evidence |
| HoLoRA (igGeaxOiFM) | 3.00, Reject | R1-topic-low | Another LoRA variant with limited experiments; LoLoRA is more comprehensive |
| ReLoRA (DLJznSp6X3) | 5.75, Accept | R1-topic-mid | Stronger empirical demonstration of its claimed advantage (high-rank training); LoLoRA's central claim is less supported |
| Train Small (s7DkcgpRxL) | 6.20, Accept | R1-topic-mid | More dramatic memory savings (enables training 70B on one GPU); clearly demonstrated practical impact |

**Round-1 bracket:** 3.5–5.75 (between the low-band ALLoRA/HoLoRA cluster and the stronger ReLoRA).

**Round-2 narrowing:** The EVA anchor (4.75) is the most directly comparable — same initialization philosophy, similar empirical pattern. LoLoRA improves on EVA by providing the theoretical justification it lacked, but shares the core liability (the paper's main claim about the benefit of the method is not convincingly demonstrated).

**What the low-band anchors failed at:** Papers scoring ≤3.5 typically had unclear or incorrect reasoning, marginal improvements, missing baselines, or unsupported central claims. ALLoRA had a theory-practice gap and marginal improvements. HoLoRA had limited experiments and trivial novelty. LoLoRA shares the theory-practice gap (Theorem 4.4's assumptions are far from the actual fine-tuning scenario) and the issue of an unsupported claim (online adaptation benefit). However, LoLoRA's experiments are more comprehensive and its theoretical contribution is genuine, placing it above the 3.0–3.33 cluster but still below the stronger mid-band papers where the central claim is convincingly demonstrated.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>