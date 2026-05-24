Now I have all the information I need. Let me compile the final review.

---

## Summary

This paper introduces Insertion Language Models (ILMs), a generative modeling paradigm that builds sequences by inserting tokens one at a time at arbitrary positions, jointly predicting both the insertion position and the vocabulary token. ILMs address two key limitations of existing approaches: the rigid left-to-right order of autoregressive models (ARMs) and the fixed-length mask constraints of masked diffusion models (MDMs). The authors propose a biased but computationally tractable denoising training objective based on predicting normalized token counts between retained positions, along with a simple RoPE-based transformer parameterization. The method is evaluated on synthetic planning tasks (star graphs, zebra puzzles), unconditional text generation, and text infilling.

## Strengths

- **Novel and well-motivated paradigm**: ILMs represent a genuinely new point in the design space of sequence generators, combining out-of-order generation (like MDMs) with variable-length output (like ARMs) via a clean insertion mechanism. The joint position-and-token prediction elegantly obviates the need for placeholder mask tokens (Section 3, Figure 2).

- **Compelling results on planning tasks where competitors fail**: On the star graph task with variable arm lengths, ILM achieves 100% and 99.1% exact-match accuracy on the medium and hard variants respectively, while MDM collapses to 36.5% and 21% (Table 1). The paper provides a clear conceptual explanation: MDMs rely on absolute token positions, which become uninformative when sequence lengths vary, while ILMs use relative positions and iterative insertion to solve the task step by step. This is the strongest evidence that ILM delivers on its core promise.

- **Strong performance on zebra puzzles**: ILM achieves 90.0% accuracy vs. 82.6% for MDM and 81.2% for ARM when generating solutions in a fixed but non-optimal order (Table 1), demonstrating out-of-order generation advantage on a realistic constraint-satisfaction task.

- **Competitive text generation, consistently outperforming MDM**: Across both Stories and LM1B datasets, ILM achieves better NLL under Llama 3.2 3B than MDM (2.14 vs. 2.54 on Stories; 4.67 vs. 4.81 on LM1B) and better Prometheus judge scores on coherence and consistency (Table 2, Figure 5). The one-at-a-time insertion mitigates the simultaneous-unmasking artifacts that hurt MDM quality.

- **Simple and practical architecture**: ILMs use a standard RoPE-based transformer without the time conditioning or AdaLN layers required by MDMs (Section 3.1, Eq. 3–4), making the architecture simpler while training successfully.

## Weaknesses

### Major

- **Infilling evaluation does not substantiate the arbitrary-length claim as presented**: The paper's third headline contribution is "greater flexibility on arbitrary-length text infilling compared to MDMs." However, Section 5.3.2 never describes how MDM was applied to the infilling task. For ILM, infilling is natural — the partial sequence with segments removed is the input, and tokens are inserted. For MDM, the model requires mask tokens in its input, and the number of masks determines how many tokens can be generated. If MDM was supplied with exactly as many mask tokens as the ground-truth removed segment contained, then the experiment does not test the claimed "arbitrary length" advantage — MDM is simply performing fixed-length completion with oracle knowledge. If a different scheme was used, it must be specified. Without this detail, the infilling results in Table 3 cannot be interpreted as evidence for ILM's advantage in handling unknown infilling lengths. This is a significant evidential gap for one of the paper's three main contributions.

### Minor

- **Training objective justification is thin**: The paper explicitly labels its training objective as "biased" and states it is used to avoid the high variance of the naive denoising loss (Section 3). While the empirical results support that the objective works, the paper does not clarify what probabilistic model (if any) the joint-count loss corresponds to — e.g., whether it can be understood as learning the conditional distribution under a uniform insertion order. The authors are upfront about the approximation, so this is not misleading, but a brief theoretical connection would strengthen reader confidence in the method's foundations.

- **MDM variable-length handling on star graphs not fully specified**: The paper argues convincingly that MDMs fail on variable-length star graphs because they rely on absolute positions (Section 5.1.1). However, the practical setup is not described: were sequences padded to a maximum length? How was MDM trained and evaluated in this variable-length setting? The conceptual argument is strong, but some implementation details would help readers assess whether the comparison is entirely fair.

- **Shorter sequence lengths from ILM in unconditional generation go undiscussed**: On the Stories dataset, ILM generates sequences averaging 119 tokens, notably shorter than ARM (201) and the dataset mean (205) — nearly a 40% reduction (Table 2). The paper discusses MDM's excessive length but does not address ILM's tendency toward shorter outputs. This could indicate a miscalibrated stop classifier or a systematic bias, and deserves analysis even if the quality metrics (NLL, Prometheus scores) remain competitive.

- **No ablation on key design choices**: The effect of varying the number of dropped tokens used in training, the impact of the joint softmax over positions and tokens vs. separate heads, and the sensitivity to the stop classifier threshold are not explored. These would help readers understand which components are essential to ILM's performance.

### Trivial

None.

## Nice-to-Haves

- An Insertion Transformer baseline on the text generation tasks would contextualize the contribution of the training objective and stop classifier beyond the star graph comparison.
- A more systematic comparison of computational cost (wall-clock time, FLOPs) across ARM, MDM, and ILM beyond the single plot in Figure 6.
- Error bars or significance tests on the Prometheus judge evaluations to support the claimed improvements.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"Soundness of training objective is not adequately justified" as a fatal issue**: While the theoretical connection is thin, the paper is explicit that the objective is approximate/biased and explains the motivation (high variance of the naive estimator). This is a minor concern, not a fatal one. The empirical results validate the approach.

- **Missing comparison with Insertion Transformer on text tasks**: The Insertion Transformer is compared on the star graph task (Table 1), which is the relevant setting for demonstrating the stop classifier advantage. Extending this to text would be nice but is not required for the paper's claims.

- **Prometheus evaluation should report inter-rater reliability**: This is a reasonable suggestion but is a nice-to-have, not a weakness — single-evaluation LLM judging is common practice.

- **Demand for ablations on number of dropped tokens, joint vs. separate heads**: These are standard ablation requests that would strengthen the paper but are not necessary for the core claims to hold.

- **"Missing discussion of computational cost" beyond Figure 6**: Figure 6 already addresses the computation-quality tradeoff; a more systematic comparison would be nice but its absence is not a weakness.

- **"No ablation on key design choices" framed as a major gap**: This was kept at Minor rather than Major because the paper's core contributions (planning advantage, text generation quality) are demonstrated through direct model comparisons, not through internal ablations.

## Novel Insights

The paper's most insightful finding is that insertion-based generation with relative position information fundamentally sidesteps the brittleness that MDMs exhibit when sequence lengths vary. The star graph experiment (Table 1) crystallizes this: MDM's absolute-position reliance means that when arm lengths vary, predicting token positions becomes equivalent to solving the entire puzzle in one pass. ILM's iterative insertion with relative positions decomposes the problem naturally. This insight — that the combination of out-of-order generation and relative positioning is what matters, not just either property alone — is genuinely novel and well-supported by the qualitative trajectories showing ILM building sequences from both ends inward (Figure 7).

## Suggestions

- Clarify the MDM infilling protocol: specify exactly how MDM inputs were constructed for the infilling experiments (how many mask tokens were used, where they were placed, and whether the number of masks matched the ground-truth segment length). If MDM was given oracle knowledge of the infilling length, either acknowledge this limitation or re-run with a protocol that hides the target length from MDM.
- Add a brief discussion connecting the joint-count training objective (Eq. 2) to the inference procedure — for instance, by noting that under a uniform insertion order over remaining positions, predicting the normalized count distribution approximates the expected next-token distribution.
- Discuss the shorter average sequence length from ILM in unconditional generation and investigate whether the stop classifier can be tuned to better match the data distribution.
- Specify the MDM training/evaluation setup for variable-length star graphs (padding strategy, max length).

## Score and Decision

**Calibration anchors considered:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| NSBP7HzA5Z | Inductive Transformers | 3.00 | R1 | Clearly weaker — different topic, no empirical rigor |
| oBmaLuEJda | BMLM | 3.00 | R1 | Weaker — narrower scope, incremental |
| 4y3GDTFv70 | Latent Space Theory | 3.25 | R1 | Weaker — theoretical, no empirical validation |
| 5dDYhvt6dY | Efficient Transformer | 3.00 | R1 | Weaker — small-scale, narrow contribution |
| WNvvwK0tut | Scaling MDMs on Text | 6.50 | R1 | Stronger — 1.1B scale, scaling laws, thorough evaluation |
| 1pTlvxIfuV | Reparameterized Discrete Diffusion | 5.50 | R1 | Comparable tier — narrower task scope (mostly MT) |
| 71mqtQdKB9 | SEDD | 6.60 | R1 | Stronger — deeper theory, stronger text results |
| Qn4HEhezKW | Diffusion LMs Many Tasks | 5.00 | R1 | Weaker — fine-tuning approach, less novelty |
| 0JjsZC0w8x | COrAL | 5.75 | R2 | Slightly weaker — order-agnostic but narrower scope |
| NRYgUzSPZz | Discrete Diffusion for Reasoning | 6.25 | R2 | Most comparable — similar planning focus, slightly cleaner evaluation |
| HnpDHiItd2 | Masked Temporal Interpolation | 6.67 | R2 | Stronger — more focused, cleaner evaluation |

**Round 1 bracket**: 5.0–7.0, narrowed by comparison with NRYgUzSPZz (6.25) and COrAL (5.75).

**Round 2 narrowing**: The ILM paper is most comparable to NRYgUzSPZz (6.25, "Discrete Diffusion for Complex Reasoning"), which also demonstrates that non-autoregressive generation outperforms ARMs on planning tasks. Both papers have novel methodology, strong planning results, and modest-scale evaluation. The ILM paper has broader scope (text generation + infilling in addition to planning) but has a significant experimental gap in the infilling evaluation. ILM is slightly below NRYgUzSPZz due to this gap, but above COrAL (5.75) which has narrower scope and less compelling advantages. I place the paper at **6.0**.

**Originality**: High. The insertion-based paradigm with joint position-and-token prediction is genuinely novel in the context of modern language modeling.

**Importance**: Medium-high. The demonstrated advantages on planning tasks address real failure modes of both ARMs and MDMs, though the current scale (85M params) leaves open questions about scaling behavior.

**Claim support**: Mostly strong for planning tasks; the infilling claim is under-supported due to the missing MDM protocol description.

**Soundness**: Reasonable. The method is clearly described and the planning experiments are well-designed. The infilling experiment and training objective justification need tightening.

**Clarity**: Good. The paper is well-structured with helpful diagrams (Figures 1, 2) and clear notation.

**Value to community**: This paper opens a promising new direction — insertion-based language modeling — that merits further investigation at larger scales.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>