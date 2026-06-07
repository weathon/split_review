Now I have sufficient material. Let me write the final consolidated review.

## Summary

Bitune proposes enhancing pretrained decoder-only LLMs during instruction-tuning by processing the prompt with **both** causal and bidirectional attention using separate PEFT weight sets, then mixing the resulting KV-cache features via learnable per-layer coefficients before causal answer generation. The idea leverages the natural two-phase structure of instruction-tuning (prefilling + decoding).

## Strengths

- **Consistent empirical gains across five model families and multiple task types.** Table 1 shows Bitune outperforms both LoRA and parameter-matched LoRA₁₆ baselines on nearly all tasks for Gemma-2B/7B, Llama2-7B, Llama3-8B, and Phi-2 (up to +4pp over LoRA and +9.3pp over the pretrained model on Gemma-2B). Table 2 extends this to GSM8K, a generative reasoning task, where "consistent high gains" are reported. This breadth—spanning commonsense reasoning, arithmetic, and language understanding—is stronger evidence than prior work on adapting causal LLMs (e.g., Springer et al. focused on text retrieval; LLM2Vec focused on embedding tasks).

- **Well-designed ablation study that isolates each design decision.** Table 3 compares the full Bitune against four ablated variants (Naive Bidir, No Mixing, Only Causal, Shared Weights). All variants outperform the LoRA baseline, but the full variant performs best, demonstrating that both separate weights *and* bidirectional attention contribute. This attribution is more rigorous than what prior architectural proposals (UniLM, prefix-LM) provided post-hoc.

- **PEFT-agnostic and effective in full finetuning.** Table 4 shows consistent gains with three different PEFT methods (LoRA, DoRA, IA3), with improvements of +1.6% to +4.0% averaged accuracy. Table 5 extends validation to full-model finetuning on Gemma-2B. This demonstrates generality beyond a single adaptation strategy.

- **Learnable per-layer mixing coefficients with empirical analysis.** The bidirectional-to-causal ratio αⱼ = |θⱼ|/(θ_init + |θⱼ|) (Eq. 7–10) is parameterized per block and per K/V head. Figures 2–3 track this ratio during training and show that bidirectional attention is utilized across *all* layers after training, providing insight into the model's learned allocation of bidirectional vs. causal processing.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The "first method" claim is overstated.** Line 216 states: "This work proposes the first method to utilize the instruction-answer structure of IT datasets that enables bidirectional processing in pretrained decoder-only models." The paper's own Related Work section acknowledges prefix-LM (T5, UniLM, UL2, XLNet), which applies bidirectional attention to a prefix with causal generation on the suffix — the same core mechanism — albeit during *pretraining* rather than post-hoc adaptation. LLM2Vec (BehnamGhader et al., 2024) also enables bidirectional attention in pretrained causal LLMs (converting them to BERT-like encoders). The actual novelty—applying this idea to *already-pretrained* decoder-only models via PEFT in the instruction-tuning setting—is valid and useful, but claiming "first" overstates it given the cited prior work. The authors should tone down this claim.

- **The evaluation underrepresents open-ended instruction-following.** The paper claims improvements in "instruction-following" (line 25), but the main experiments (Table 1) evaluate on multiple-choice log-likelihood benchmarks (PIQA, ARC, CSQA, SIQA, MMLU)—which are more naturally characterized as question-answering or commonsense reasoning. GSM8K (Table 2) is the only generative task requiring free-form response generation and is clearly the strongest evidence for instruction-following claims, but it is a single arithmetic reasoning dataset. Adding an open-ended instruction-following benchmark (e.g., MT-Bench, AlpacaEval) or human evaluation would directly support the paper's core framing.

- **The Gemma-7B result (0.1pp average gain) is not explained or investigated.** The paper notes the result (line 121) and correctly observes that this is not simply a scale issue (Llama2/3-7B/8B show gains), but it does not analyze *why* Gemma-7B behaves differently. Understanding whether this is an architecture-specific, data-specific, or optimization-specific effect would strengthen the paper's scientific contribution and guide future application of the method.

- **Computational cost is acknowledged but not quantified.** The paper notes increased training time and memory (line 212–214) and calls it "a minor limitation," but provides no concrete numbers for training time increase, peak memory usage, or FLOPs overhead. The inference latency example (line 214) contains a garbled comparison. Quantifying these costs would allow readers to make an informed trade-off assessment.

### Trivial
None.

## Nice-to-Haves

- Report standard deviations or confidence intervals for the main results. Several gains are in the range of 1–4pp; variance estimates would clarify which differences are significant.
- Compare against a simple "repeat the prompt with causal attention" baseline (building on Springer et al.'s insight). The "Only Causal" ablation partially addresses this but uses separate weights; a variant with shared weights and two causal passes would isolate the value of the bidirectional mask more cleanly.
- Provide the numerical results of Table 3 (ablations) in the main text explicitly rather than only as figures, since the relative performance of Naive Bidir vs. full Bitune is central to assessing the method's added value.

## Removed Points

These points were raised in the reviews but are removed under the filtering rules:
- *Training hyperparameters (epochs, batch size, optimizer) not stated* — The reproducibility statement (line 218–221) refers to supplementary materials for hyperparameters. Since the appendix was stripped by the parser, this is a parser artifact, not an author omission. (Rule: REMOVE weaknesses about missing appendix content.)
- *Garbled latency sentence* — The sentence "only a 0.2s increase from 11.5s to 11.4 for more results" is garbled. Per the instructions, formatting/parser artifacts are not author errors.
- *"The results are reported as image placeholders"* — The ablation numerical values are in figures that the parser cannot render. The paper itself contains these results.
- *Speculation that the Naive Bidir gap might be small* — Without access to the numerical values in Table 3 (images), this speculation cannot be verified from the parsed text. The paper's textual description states the full variant performs best.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Remove or soften the "first method" claim. A more precise statement (e.g., "the first method to *specifically target the instruction-answer structure* of IT datasets for enabling bidirectional processing in *pretrained* decoder-only models via PEFT") would be accurate and not conflict with the cited prior work.
2. Add at least one open-ended instruction-following evaluation (MT-Bench or AlpacaEval) to directly support the "instruction-following" framing.
3. Investigate and report why Gemma-7B shows negligible gains; this could reveal important boundary conditions of the method.
4. Provide quantitative numbers for training overhead (time increase, peak memory) so readers can evaluate the practical trade-off.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>