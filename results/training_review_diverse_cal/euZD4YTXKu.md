Now I have everything I need. Let me produce the final consolidated review.

## Summary

ZO-Offloading presents a system that combines zeroth-order (ZO) optimization with CPU offloading to fine-tune large language models on a single GPU, achieving dramatic memory reductions (e.g., OPT-175B on a 24GB GPU). The framework contributes a dynamic scheduler that overlaps block-level computation with CPU-GPU communication, reusable GPU memory to avoid allocation overhead, fused parameter updates with dual forward passes, low-bit compression for AMP mode, and asynchronous checkpointing. The memory and throughput results against MeZO show that ZO-Offloading reduces GPU memory by ~5–10× while maintaining comparable throughput for models where MeZO can run.

## Strengths

- **Enables unprecedented scale on single-GPU hardware.** Table 1 shows ZO-Offloading uses only ~14.3 GB (FP32) and ~2.7 GB (FP16) of GPU memory for OPT-175B, while MeZO fails due to OOM. This is the first demonstration of running such a large model's fine-tuning loop on a single 24GB GPU. The memory savings are verified and substantial.

- **Throughput comparable to standard ZO.** Across all model sizes where MeZO runs (OPT-125M through OPT-13B), ZO-Offloading achieves throughput ratios between 0.86× and 1.00× (Table 1). This is a non-trivial result given the added communication overhead of CPU offloading, and it directly supports the claim of "no additional time cost."

- **Well-designed ablation study confirms each component's contribution.** The reverse ablation (Table 2) cleanly isolates the impact of three system features. Reusable memory causes the largest throughput drop when removed (to 37% for OPT-6.7B), followed by the dynamic scheduler (58%) and efficient parameter updating (89%). This experimentally validates the design choices.

- **Low-bit compression improves throughput for larger models.** Table 3 shows that for OPT-2.7B and OPT-6.7B, lower-bit compression (FP8, BF16, FP16) consistently yields higher throughput than no compression in AMP mode, validating the design of Section 5.4. The finding that OPT-1.3B is computation-bound (where compression adds overhead) shows nuanced understanding of the bottleneck.

- **Asynchronous checkpointing is a practical contribution.** The three-stage mechanism (Section 5.5) that overlaps disk writes with training using self-copies is a well-motivated engineering innovation for long fine-tuning runs, addressing a real pain point in large-model training.

## Weaknesses

### Fatal

None.

### Major

- **No accuracy or convergence results are presented, despite the paper's claim of enabling "fine-tuning."** Section 6.1 states: "We conducted accuracy verification experiments to confirm this. These tests affirm that our ZO-Offloading method preserves model accuracy across different model sizes and data formats." Yet no accuracy numbers, tables, loss curves, or convergence plots appear anywhere in the paper. The paper's title and abstract claim that ZO-Offloading enables fine-tuning of LLMs, and the contributions claim "no decreases in accuracy." However, the only evidence offered is a bare assertion. Without accuracy validation on at least one task (e.g., SST-2, which is already used for throughput evaluation), the reader cannot verify that the offloading scheduler does not introduce numerical drift, that the gradient estimation works correctly under the block-by-block schedule, or that the system produces a usable fine-tuned model. This is the single most important omission—it directly undermines the paper's core claim. *Severity note: the memory and throughput contributions are real and unaffected by this gap. The paper's system-level engineering is independently valuable. But the framing as a "fine-tuning" paper is incomplete without demonstrating that the fine-tuning actually yields useful results.*

- **Ambiguity in how dual forward passes are scheduled under per-block offloading.** Algorithm 1 processes each block once with `C(W_i)`, described as "dual forward computation." The ZO-SGD gradient estimate (Section 3) requires computing the loss for *both* perturbations (+εz and −εz) through the *entire* model. The paper does not clearly explain whether `C(W_i)` encapsulates both forward passes for block i (processing two activation streams simultaneously), or whether the scheduler runs two complete passes through all blocks. The text says each block "undergoes dual forward computation" (Section 4), which implies the former, but the algorithm's single-pass structure and the lack of detail on how the two activation streams propagate across blocks makes this ambiguous. Given that the correctness of the gradient estimation depends on this scheduling, the paper would benefit from an explicit description or diagram showing how the two perturbation signs are applied and how outputs flow between blocks.

### Minor

- **No comparison with first-order offloading methods for context.** The paper motivates ZO-Offloading by arguing that first-order optimizers introduce redundant communication (backward passes, activation storage). However, for model sizes where first-order offloading *can* run (e.g., OPT-6.7B, OPT-13B), the experiments compare only against MeZO. A throughput comparison with, e.g., DeepSpeed ZeRO-Offload or a CPU-offloaded AdamW variant would allow the reader to assess whether ZO-Offloading's claimed advantages materialize and to understand the convergence-vs-throughput trade-offs. Without this, the framing of ZO as "particularly well-suited for CPU offloading" remains a plausible hypothesis rather than an empirically supported claim.

- **Practical feasibility of OPT-175B fine-tuning is not discussed.** At 0.74 tokens/sec (Table 1, FP16), a single training step processes roughly 0.74 tokens. Even with a small batch of 16 tokens, each step would take ~22 seconds. The paper does not report iteration-level latency, convergence requirements, or estimated total training time for a realistic fine-tuning run on OPT-175B. While the memory achievement is significant, the reader has no basis to judge whether the resulting system is practical for actual use or merely a memory-usage curiosity.

- **Asynchronous checkpointing is described in detail but not experimentally validated.** Section 5.5 presents a well-motivated three-stage checkpointing mechanism, but the experiments include no comparison against synchronous checkpointing in terms of throughput, training interruption time, or CPU memory overhead. Since it is listed as a contribution, some validation is expected.

### Trivial

None.

## Nice-to-Haves

- Add task accuracy results (e.g., SST-2) comparing ZO-Offloading to MeZO for at least OPT-1.3B, OPT-6.7B, and OPT-13B. Even a table confirming identical or near-identical accuracy would resolve the main concern.
- Include a brief discussion of practical training time for OPT-175B: estimated tokens/hour, steps to convergence on a typical task, and whether the throughput translates to a feasible workflow.
- A diagram or textual clarification showing how two perturbation streams (±ε) propagate through the scheduler across blocks would resolve the dual-forward-pass ambiguity.
- A comparison with a CPU-offloaded first-order method (e.g., AdamW with manual offloading) for OPT-6.7B would contextualize the system-level contribution.
- Validate asynchronous checkpointing experimentally with throughput comparison against synchronous checkpointing.

## Removed Points

These points were raised by reviewers but are removed for the following reasons:

- *"Typo 'decreases in accuracy' should be 'decrease in accuracy'"* — Per hard rules, formatting/grammar criticisms are treated as parser artifacts and removed.
- *"Figure 5b cross-reference error"* — Likely a parser artifact from PDF extraction; per hard rules, not included.
- *"Strength: Accuracy is preserved"* (from Strength Finder) — Removed because the paper provides no empirical accuracy results; this "strength" conflicts with the verified weakness and is unsupported.
- *"Missing apparatus to verify reproducibility"* — The paper references standard tools (PyTorch, CUDA streams, OPT models). Reproducibility concerns that doubt a cited entity's existence are removed per hard rules.
- *Criticisms demanding additional ablations on memory usage* — The paper convincingly argues that memory reduction is inherent to CPU offloading and not dependent on the ablated features; this is a defensible methodological choice.

## Novel Insights

The synthesis reveals a tension that the paper does not fully address. The strongest empirical claim is the memory reduction (5–10× less GPU memory than MeZO), which is clearly verified. The paper's weakness is that it simultaneously makes a substantive claim ("fine-tuning") while providing only throughput/memory measurements. The reviews surface that the community would value this paper more if it honestly positioned itself as a *systems paper for ZO offloading* rather than a *fine-tuning paper* — the former framing would require only memory and throughput validation (already present), while the latter demands accuracy verification (absent). This disconnect between framing and evidence is the paper's fundamental issue, not any flaw in the system itself.

## Suggestions

1. Add accuracy results on SST-2 comparing ZO-Offloading to MeZO across model sizes. This is the single most impactful addition — it would transform the paper from "promising system demonstration" to "validated fine-tuning framework."
2. Rewrite Section 5.1 / Algorithm 1 description to explicitly state whether `C(W_i)` encapsulates both forward passes (with two activation streams) and show how the scalar `g` is assembled from the full model output.
3. Include a brief experiment comparing throughput against a CPU-offloaded first-order optimizer (e.g., AdamW with DeepSpeed ZeRO-Offload) for OPT-6.7B to support the motivational claim about ZO's suitability for offloading.
4. If practical, report convergence behavior (loss curves) for at least one model size to demonstrate that the offloading schedule does not interfere with training dynamics.

## Score and Decision

This paper presents a well-engineered system with substantial memory savings and credible throughput results. However, the complete absence of accuracy/convergence validation for a paper whose title and contributions center on "fine-tuning" is a significant gap that prevents full acceptance as a fine-tuning paper. The core system contribution is real, but the paper overclaims by presenting a memory/throughput benchmark as a fine-tuning framework without verifying that the training loop produces a usable model. The paper would benefit from a major revision to either (a) add accuracy results or (b) honestly reframe the contribution around memory-efficient gradient estimation without claiming validated fine-tuning.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>