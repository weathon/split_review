Here is my synthesized final review.

## Summary

This paper introduces Mixture-of-Instructions (MoI), a multi-task supervised fine-tuning strategy that combines per-task system prompts, balanced instruction packing, and chunk-based attention masking. The method is applied to Qwen-7B-chat to produce Qwen-SFT-MoI, evaluated across seven benchmarks covering dialogue, code, math, and tool use. The core claim is that MoI outperforms simpler SFT strategies (sequence, packing, balanced sampling) and preserves multi-turn dialogue ability while improving specialized task performance.

## Strengths

- **Strong empirical evaluation with extensive ablations.** The paper goes beyond a single main result, systematically ablating system prompts (Table 3), sampling strategies (Table 2, Figure 5), attention masks (Table 8), and even performing weight-replacement experiments (Table 9). This provides a reasonably decomposed picture of which components contribute to observed gains.

- **Generalizability demonstrated across model families and scales.** MoI consistently improves performance on Llama2-7B, Llama3-8B, and Qwen1.5 models at 1.8B and 4B scales (Tables 6, 7), showing the method is not architecture-specific.

- **Chunk-based attention masking is a clean solution to the attention-cross-contamination trade-off.** Table 8 directly shows that chunk-based masking (51.4 on T-Eval) outperforms both full-cross-contamination (46.8) and fully isolated masking (46.0), while preserving code/math gains. This is a concrete empirical contribution over prior packing approaches.

- **Mechanistic investigation via weight replacement (Table 9).** The finding that swapping MoI-trained attention weights into the original chat model degrades performance, while other SFT-trained attention weights do not, offers evidence that MoI operates by reshaping attention distributions rather than simply fitting new output distributions.

## Weaknesses

### Fatal
None.

### Major

- **Training hyperparameters are entirely absent.** The paper specifies only "8×80G A100 GPUs, DeepSpeed ZeRO-3, FlashAttention-2" (line 113). Learning rate, optimizer, batch size, gradient accumulation steps, number of training epochs/steps, context length, warmup schedule, and weight decay are all unreported. This is not a trivial omission — it makes the work effectively unreproducible by other researchers. The fact that the paper trains multiple models across ablations and model families makes this omission more concerning, not less.

- **The loss function equations (3) and (6) contain notation errors that hinder reproducibility from the formalism alone.** In Equation (3), $|y_i|$ appears in the denominator where $y_i$ is a single token, making the term ill-defined. In Equation (6), the expression $\frac{L_n}{n_{mix}}$ divides a token-position index by a count of instructions, producing dimensionally inconsistent values. While the *conceptual* description of MoI (system prompts + balanced packing + chunk masking) is clear enough that an experienced practitioner could re-implement it, the equations as written do not constitute a precise, self-contained specification of the training objective. This is a presentation issue that the authors must fix before the paper is in publishable form; it is not a fatal flaw because the text and Figure 4 convey the core approach.

### Minor

- **The central motivational claim rests on a single qualitative example.** The paper opens with a case study of the Boyer-Moore algorithm failure on MT-Bench, supported by attention maps for a single question (Figure 2). While Table 3 does provide quantitative evidence that different system prompts affect code benchmark scores, the *attention-based* motivation is never corroborated systematically — e.g., How often do such knowledge conflicts occur across coding questions? What is the average attention distribution to system prompt vs. answer under different prompts? The paper would be stronger with a quantitative characterization of the phenomenon it claims to solve.

- **The contribution of per-task system prompts vs. balanced packing vs. chunk masking is not fully disentangled.** The paper compares "Sequence," "Packing," "Balance," and "MoI" in Table 2, but it is ambiguous whether the "Packing" and "Balance" baselines use per-task system prompts during training or a single default prompt. If "Balance" already uses per-task prompts, then the Balance→MoI comparison isolates the attention-mask contribution, but the Sequence→Balance comparison conflates prompts *and* sampling. A cleaner control — e.g., balanced packing with a *single* default prompt and no chunk masking — would tighten the attribution of gains.

- **Evaluation methodology is underspecified in places.** Greedy decoding is mentioned for Tables 4 and 5 but not for Table 2 (the main result table). The number of evaluation trials and whether results are deterministic are not stated. Statistical significance (e.g., confidence intervals or multiple seeds) is absent, which is common in this setting but worth noting.

- **System prompt sensitivity is not explored for non-code tasks.** Table 3 tests different prompts for code, but no similar ablation is presented for math, dialogue, or tool-use prompts. The claim that per-task prompts matter relies on the code case and the overall MoI results, but a direct test for other domains would strengthen the argument.

### Trivial

- Equation (5) claims a reduction to the sequence loss under constant response lengths but does not show the algebraic steps. While the claim is plausible, showing the derivation would improve clarity.
- The name "Mixture-of-Instructions" could be read as promising more novelty than the combination of existing components warrants; the paper would benefit from stating upfront what is new (the specific combination and the chunk-masking design) versus what is adopted from prior work.

## Nice-to-Haves

- A quantitative analysis of the frequency of knowledge conflicts across a larger set of questions, beyond the Boyer-Moore case study.
- Reporting of per-task system prompts in the main text (Table 1 is an image and not readable in the parsed version).
- A comparison against a baseline trained with balanced packing + *default* system prompt (no per-task prompts), to isolate the prompt effect.
- Wall-clock time or FLOPs comparison to support the efficiency claims.

## Removed Points

These points were raised by reviewers but are removed for the following reasons:

1. **"Equation (2) treats each $y_n$ as a single token"** — Removed (misread of notation). In standard autoregressive LM notation, $\log P_\theta(y_n \mid [s,x]_n)$ where $y_n$ is a sequence denotes the sum of per-token log probabilities. This is standard practice, not an error.

2. **"Loss function is incoherent and makes the paper unverifiable"** — Downgraded from Fatal to Major. The conceptual method is clearly described; the notation issues are presentation problems, not fatal errors.

3. **"No ablation varying the prompts"** — Removed (factually wrong). Table 3 explicitly tests different system prompts for code tasks on HumanEval, MBPP, and MT-Bench.

4. **"Missing appendix content, tables are images"** — Removed. These are parser artifacts; the original submission contains this content.

5. **"The name suggests more novelty than warranted"** — Moved to Trivial. This is a matter of perspective and not a substantive weakness.

## Novel Insights

The most interesting finding is buried in Table 8: attention cross-contamination *helps* code and math performance but *hurts* complex reasoning (T-Eval). The paper's chunk-based masking resolves this trade-off by allowing within-chunk (cross-domain) attention while blocking cross-chunk interference. This suggests that cross-contamination is not uniformly harmful — its effect depends on task type — and that the optimal attention regime is task-dependent rather than universally isolated. This insight extends beyond the paper's specific method and could inform future work on multi-task training architectures. The weight-replacement experiment (Table 9) further suggests that MoI-trained attention heads become specialized to their training-time MLP representations, offering a mechanistic clue about how multi-prompt training differs from single-prompt SFT.

## Suggestions

1. **Report all training hyperparameters** — learning rate, optimizer, batch size (effective and per-device), gradient accumulation, training steps/epochs, context length, scheduler, weight decay, and total compute time. Without these, the paper is not reproducible.
2. **Clean up the loss function notation.** Fix Equation (3) (the $|y_i|$ term) and rewrite Equation (6) with dimensionally consistent indices, or replace it with a clear algorithmic description/pseudocode.
3. **Add a baseline** with balanced packing, a single default system prompt, and no chunk masking to isolate the effect of per-task prompts from the rest of MoI.
4. **Quantify the knowledge-conflict phenomenon** beyond the single Boyer-Moore example — e.g., report the frequency of such failures across a sample of coding questions.
5. **Specify evaluation protocols** for all tables (greedy vs. sampling, number of trials, deterministic/not).

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>