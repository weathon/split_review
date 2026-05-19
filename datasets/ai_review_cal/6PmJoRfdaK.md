- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6
Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

LongLoRA proposes two complementary techniques for efficiently extending the context windows of pre-trained LLMs: (1) **Shifted Sparse Attention (S²-Attn)**, which splits tokens into groups and performs attention within each group, with a shift of half the group size in half the attention heads to enable cross-group information flow, and (2) an **improved LoRA variant (LoRA⁺)** that additionally makes embedding and normalization layers trainable. The method is evaluated on Llama2 7B/13B/70B, achieving extension up to 100k/64k/32k context on a single 8×A100 machine with perplexity close to full fine-tuning.

## Strengths

- **S²-Attn with group size 2048 matches full-attention perplexity while using 4× shorter attention sequences.** Table 1 shows S²-Attn achieves perplexities of 8.04, 8.03, and 8.08 at target lengths 8192, 16384, and 32768 — essentially identical to full attention (8.02, 8.05, 8.04) — while short attention without shifting degrades to 8.29, 8.83, 9.47. This directly validates the core premise that sparse local attention with shifting can approximate dense global attention during fine-tuning.

- **Trainable embedding and normalization close the perplexity gap between standard LoRA and full fine-tuning.** Table 2 shows standard LoRA (rank=8) yields 11.44 perplexity at 32768 context, while adding trainable normalization alone drops to 10.49, trainable embedding alone drops to 8.29, and both together reach 8.12 — nearly matching full fine-tuning's 8.08. Crucially, increasing LoRA rank (8→256) does not help (~11.9 all), confirming that opening these specific parameters is the key enabler.

- **LongLoRA extends Llama2 7B to 100k context and 70B to 32k on a single 8×A100 machine.** Table 4 reports these extreme-length evaluations (e.g., 7B at 100k achieves 2.52 perplexity on proof-pile), directly supporting the paper's efficiency and scalability claims.

- **S²-Attn with cross-head shifting uniquely supports full-attention testing without large degradation.** Table 7 shows that when tested with full attention (the inference-time behavior), S²-Attn (cross-heads) gives 8.12, while dilated attention (11.78), block sparse (8.30), and stride sparse (24.03) all suffer substantial degradation. This validates the design choice of retaining the standard attention architecture at inference.

- **Competitive retrieval performance despite lower training cost.** Table 5 shows LongLoRA 13B scores 0.94 at 16k context on topic retrieval, slightly outperforming the fully fine-tuned LongChat-13B (0.90), while being adapted via next-token prediction on RedPajama rather than expensive long-conversation fine-tuning.

## Weaknesses

### Fatal

None.

### Major

- **The causal mask modification to prevent information leakage in S²-Attn is mentioned but never specified.** The paper acknowledges that "potential information leakage might be introduced by shifting" and states it is "easy to prevent via a small modification on the attention mask" (Figure 2 caption). However, the pseudocode in Algorithm 1 simply calls `self_attn(qkv)` without describing the mask modification. The issue arises because `roll(-G/2, 1)` wraps the last G/2 tokens around to the beginning; in the last group of the shifted heads, tokens from the end of the sequence (e.g., positions N-G/2 to N-1) appear before tokens from the start (positions 0 to G/2-1). A naive causal mask within this group would allow early-position (original) tokens to attend to later-position (original) tokens — a causality violation. While the fix is conceptually straightforward (design a custom mask that prevents this), the submission as written is incomplete on a detail that touches the correctness of the training procedure. This is the single most important gap in the current manuscript.

### Minor

- **The "two lines of code" framing is slightly promotional.** Algorithm 1 does show two key lines, but a production implementation requires additional surrounding boilerplate (imports, the `self_attn` function definition, handling of edge cases). This is a minor presentation issue.

- **No ablation on group size.** All experiments use a fixed group size of 2048. The paper would benefit from showing how performance/efficiency trade-offs shift with different group sizes (e.g., 1024, 4096).

- **Data preprocessing details are minimal.** The paper does not describe how documents of varying lengths are handled during training (e.g., packing multiple documents, truncation, or concatenation). This is a minor reproducibility gap.

### Trivial

None.

## Nice-to-Haves

- Provide the explicit attention mask modification (a few lines of code or an equation) to resolve the specification gap — this is the most impactful improvement.
- Include a direct perplexity comparison to a full-attention fine-tuned model at the same maximal context lengths (e.g., 100k for 7B), even at reduced scale, to bound the degradation at extreme lengths.
- Report variance across random seeds for key numbers, since several results are close (e.g., 8.04 vs 8.08).

## Removed Points

These points were raised by one or both reviewers but are removed as per the filtering instructions:

1. **"LongAlpaca SFT results are absent in the paper."** The abstract, introduction, and conclusion mention conducting supervised fine-tuning with the LongAlpaca dataset, but no results or evaluation appear in the main text. However, these results likely reside in the appendix, which was stripped by the parser. As per the hard rules, weaknesses about content potentially in the stripped appendix should be removed. The correct fix is for the authors to reference SFT results from the appendix in the main text more explicitly.

2. **"No comparison to other PEFT methods (e.g., IA³, adapters, prefix tuning)."** This is scope creep — the paper focuses on LoRA, and the contribution is the combination of S²-Attn with an improved LoRA variant. The related work section (Section 2) does discuss alternative PEFT approaches and explains the paper's focus.

3. **"No variance or confidence intervals reported."** Single-run evaluation on large-scale benchmarks is standard practice in this area. Not a meaningful weakness.

4. **"How document-length distribution is handled."** Already noted as a minor missing detail; does not threaten the core claims.

5. **Several generic strengths from the Strength Finder** (e.g., "the problem is important," "addressed a timely question") were removed as they lack specific, grounded evidence tied to this paper's content.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation about the method that the paper itself does not already articulate.

## Suggestions

- **Specify the attention mask modification explicitly.** Add a short sentence or a modified pseudocode line that describes how the causal mask should be adjusted in the shifted heads to prevent the boundary cross-attention issue. This single fix resolves the most serious concern.
- **Add a brief ablation on group size** to show the trade-off between efficiency and quality for different G values (e.g., 1024, 2048, 4096).
- **Reference the LongAlpaca SFT results more explicitly** in the main text if they are in the appendix (e.g., "see Appendix X for SFT results"), so readers are not left wondering.
