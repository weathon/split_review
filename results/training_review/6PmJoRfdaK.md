Now I have all the information needed to verify every claim. Let me produce the consolidated review.

---

## Summary

LongLoRA proposes two techniques for efficient long-context fine-tuning of LLMs: (1) Shifted Sparse Attention (S²-Attn), which uses local attention with a half-group shift across attention heads during training to approximate full attention while saving computation, and (2) an improved LoRA variant (LoRA⁺) that makes embedding and normalization layers trainable, closing the perplexity gap between standard LoRA and full fine-tuning. The paper demonstrates extending Llama2 7B to 100k context and 70B to 32k on a single 8×A100 machine, while retaining the original attention architecture at inference.

## Strengths

- **S²-Attn is a clean, well-motivated idea that demonstrably enables efficient training with minimal perplexity loss.** Table 2 (the pilot study) directly compares S²-Attn against full attention under identical conditions (same dataset, same PI, same full fine-tuning): S²-Attn achieves 8.04 vs. 8.02 (8k), 8.03 vs. 8.05 (16k), and 8.08 vs. 8.04 (32k). The two-line implementation (Algorithm 1) is a genuine practical contribution — models trained with S²-Attn use standard full attention at inference, preserving compatibility with FlashAttention-2 and DeepSpeed.

- **The discovery that trainable normalization and embedding layers are critical for LoRA in context extension is well-supported and practically useful.** Table 3 shows that standard LoRA (rank=8) yields 11.44 PPL at 32k, while adding trainable normalization and embedding brings it to 8.12 — nearly matching full fine-tuning's 8.08. Larger ranks alone (up to 256) fail to close this gap (11.98), cleanly isolating the role of these extra layers.

- **The method achieves nontrivial practical scaling on limited hardware.** Table 5 shows Llama2 7B extended to 100k context, 13B to 64k, and 70B to 32k on a single 8×A100 machine with strong perplexity at all evaluation lengths. The compatibility with FlashAttention-2 and DeepSpeed means this is immediately usable.

- **Rigorous ablation on attention patterns.** Table 8 systematically compares S²-Attn against four alternative efficient attention designs (dilated, block sparse, stride sparse, and various shift strategies) under both sparse-attention testing and full-attention testing, with clear results showing S²-Attn's advantage.

- **Validation on practical retrieval tasks.** Table 6 shows LongLoRA-13B achieves 0.94 accuracy at 16k on topic retrieval, comparable to the fully fine-tuned LongChat-13B (0.90). Figure 3 demonstrates passkey retrieval accuracy above 90% up to 33k tokens for the 7B 32k model, confirming that the model functions with full attention at inference.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by evidence. The weaknesses below are addressable but do not threaten the main contributions.

### Minor

- **Full-attention evaluation (passkey retrieval) is only shown for the 32k 7B model, not for the 100k 7B or 70B models.** The paper's central claim is that S²-Attn fine-tuned models can be deployed with dense global attention at inference. The passkey retrieval experiment (Figure 3) validates this for the 32k 7B model. However, for the 100k 7B model, the 64k 13B model, and the 32k 70B model — all reported in Table 5 — no equivalent full-attention retrieval test is provided. The perplexity numbers in Table 5 use sliding window evaluation (stride 256, following the standard protocol from prior work), which only measures local context. While passkey retrieval for 32k 7B provides a proof of concept, the absence of such a test for the more extreme configurations limits the strength of the empirical support for the core claim.

- **LongAlpaca SFT dataset is mentioned as a contribution but never evaluated.** The abstract, introduction, and conclusion all reference LongAlpaca and supervised fine-tuning, yet the paper contains no experiments, results, or even a dataset description for this component. This does not affect the paper's primary contribution (efficient context extension via S²-Attn + LoRA⁺), but it is a clear gap: the reader cannot assess whether this claimed contribution has any value.

- **The main results table (Table 1) claims "comparable performance to the full attention or full FT baselines" in its caption but does not include those baselines.** The full-attention and full-fine-tuning comparisons do exist in other tables (Table 2 on PG19 with full fine-tuning, Table 3 on PG19 with full FT at 32k), but they are on a different dataset (PG19 validation) than Table 1 (proof-pile test). A direct full-FT row on proof-pile in Table 1 would make the comparison cleaner and would better support the claim stated in the caption.

- **The difference between S²-Attn and block sparse attention under full-attention testing is small (8.12 vs. 8.30 PPL in Table 8), yet the paper dismisses block sparse as not working well without deeper analysis.** The gap of 0.18 PPL does not strongly support the claim that "other efficient attentions... have a large gap to the standard style and do not work well like ours" (line 44–45). A more nuanced discussion or additional tasks differentiating these patterns would strengthen the paper's claims.

- **The ablation on LoRA⁺ (Table 3) is only shown at 32k context.** The effect of trainable normalization and embedding at shorter context lengths (8k, 16k) is not reported, making it unclear whether this finding generalizes across all context lengths or is specific to the 32k setting.

### Trivial
None.

## Nice-to-Haves

- **Ablation of S²-Attn without Position Interpolation** (e.g., using original RoPE or NTK-aware scaling) would strengthen the paper's claim of orthogonality to position embedding methods, but is not required since the paper explicitly scopes this as future/directions work and all baselines use the same PI setting.
- **Full-attention perplexity evaluation** (e.g., by averaging log-likelihoods over entire sequences rather than sliding window) would be a cleaner validation that full attention works for language modeling, though passkey retrieval already tests this capability.
- **Exploration of group size sensitivity** at different context lengths would provide practical guidance for practitioners.
- **Passkey retrieval for 13B and 70B models** would broaden the validation of full-attention capability across model scales.

## Removed Points

- **Criticism that sliding window evaluation "does not measure full-attention capability" and "does not demonstrate that the claimed property actually works."** This is overstated — the paper does demonstrate full-attention capability via passkey retrieval (Figure 3) for the 32k 7B model. Sliding window perplexity is the standard evaluation protocol used by prior work (ALiBi, Position Interpolation). The valid remaining concern (limited to one model/context) is already captured above.

- **Criticism about "confounding effect of Position Interpolation."** The paper explicitly states (Section 2, line 77) that the method is "orthogonal to these position embedding methods." All baselines in Table 2 use the same PI, so PI is controlled across comparisons. Requesting an ablation without PI is scope creep beyond the paper's stated contribution.

- **Criticism about "no direct comparison to full fine-tuning in the main results table."** The comparisons exist in Tables 2 and 3 (different datasets). The concern about absent proof-pile FT baselines is already captured in the minor weakness above with appropriate framing.

- **Formatting/style nitpicks** about Figure 1 axis labels or missing standard deviations — these are either parser artifacts or non-standard in this evaluation setting.

- **Criticism about 1000 training steps being insufficient** without further justification — the paper shows an ablation on steps (Figure 5) confirming convergence at 8k within 200 steps, making this a speculative concern.

## Novel Insights

Beyond the paper's own contributions, the reviews highlight an interesting tension: the paper's strongest experimental evidence for full-attention inference comes from the passkey retrieval task (a synthetic probing task), not from the language modeling perplexity evaluation (which uses sliding window). This suggests that for real-world deployment, practitioners using LongLoRA should validate long-context capabilities with retrieval-oriented benchmarks rather than relying solely on perplexity, even if the architecture nominally supports full attention. The small gap between S²-Attn and block sparse attention under full-attention testing (0.18 PPL) also raises the question of whether the key advantage of S²-Attn is less about raw perplexity and more about its specific compatibility with the pre-training attention distribution — an area the paper could explore further.

## Suggestions

1. **Add passkey retrieval (or another full-attention retrieval task) for the 100k 7B model** to validate the core claim at the paper's most impressive scale.
2. **Include a full-FT baseline row in Table 1** on proof-pile for at least one context length (e.g., 32k) so the "comparable performance" claim is directly supported in the same experimental setting.
3. **Either provide LongAlpaca SFT evaluation results or remove SFT claims** from the abstract and conclusion — as it stands, the reader cannot assess this claimed contribution.
4. **Provide a more nuanced discussion of block sparse attention in Table 8** — the 8.30 result under full-attention testing is reasonably close to 8.12, and explaining why S²-Attn is preferred despite the small gap would strengthen the paper.

## Score and Decision

**Originality:** The S²-Attn mechanism is a well-motivated application of the shift idea (inspired by Swin Transformer) to LLM context extension. While individually the components are not novel, their combination and the practical insight about trainable normalization/embedding for LoRA are useful contributions.

**Importance of research question:** Very high — efficient long-context LLM fine-tuning is a practically important problem.

**Claims support:** Mostly well-supported, with some gaps: the full-attention inference claim is validated for one model/scale, and the SFT component is unvalidated.

**Soundness of experiments:** The core experiments (perplexity, retrieval, ablations) are well-designed and cover the main claims. The sliding window perplexity follows community standards.

**Clarity of writing:** Clear, well-structured, with helpful figures and a concrete algorithm.

**Value to community:** High — the two-line S²-Attn implementation and the finding about trainable normalization/embedding are immediately useful to practitioners.

Based on the verified strengths and weaknesses, this is a solid paper with a useful contribution. The weaknesses are minor and addressable; none invalidate the core claims.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>