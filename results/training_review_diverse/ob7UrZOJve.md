Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper identifies "lazy layers" in standard decoder-style LLMs (GPT-2) where deeper-layer attention matrices degenerate to rank-1, single-column structures. It proposes Inheritune, a training recipe that initializes a smaller target model from the early layers of a larger pre-trained reference model, then progressively grows and retrains it until it matches the reference's validation loss. Experiments on GPT-2 Medium, Large, and xLarge across OpenWebText-9B and FineWeb_Edu show that Inheritune-derived smaller models match or exceed the performance of their larger counterparts and outperform same-sized baselines trained from scratch, with stacking, hybrid-stacking, half-width, and knowledge distillation.

## Strengths

1. **Empirical identification of attention degeneration in standard decoder LLMs**: The paper provides systematic evidence (Fig. 1a,b,d,e) that deeper layers in GPT-2 Medium and Large exhibit rank-1 attention matrices with single-column mass concentration. This extends prior theoretical rank-collapse results to practical LLM architectures with residual connections, layer norms, and FFNs, and directly motivates the "lazy layer" concept and the need for inherited initialization.

2. **Inheritune consistently produces smaller models that match or surpass larger ones**: In Table 1, the 16-layer GPT-2 Medium variant matches the 24-layer model's validation loss (2.81) after the same 100K steps and beats a same-size random-init model trained for 200K (2.83). The 18-layer GPT-2 Large variant (2.80) outperforms the full 36-layer model (2.85). The 24-layer xLarge variant (2.64) matches the 48-layer model (2.65). This directly validates the paper's central claim.

3. **Generalization across model scales and data regimes**: The method is validated on three model families (GPT-2 Medium, Large, xLarge) and two datasets — OpenWebText-9B (with data repetition) and FineWeb_Edu (100B tokens, without repetition). The non-repeated setting (Fig. 4, Table 4) confirms that gains are not an artifact of data repetition and that the recipe transfers across data qualities.

4. **Ablation identifies effective initialization sub-modules**: Table 3 shows that initializing both attention and MLP weights (with or without layernorm) yields the best validation loss (2.80–2.81), while initializing only attention or only MLP gives worse results (2.84–2.85). This provides clear evidence about which components drive the improvement.

5. **Outperforms strong baselines including knowledge distillation**: Inheritune beats stacking, hybrid-stacking, and half-width initializations (Table 2) as well as vanilla KD and DistillBERT-style KD (Fig. 3) for the same model size. The 16-layer GPT-2 Medium variant achieves 2.81 after 50K steps versus >2.85 for both KD baselines, positioning Inheritune as a more effective alternative.

6. **Attention visualization shows Inheritune preserves focused patterns**: Figure 2 demonstrates that later layers in a 16-layer Inheritune-trained model (L11, L15) maintain structured attention maps, while the corresponding deeper layers of the vanilla 24-layer model (L20, L22) exhibit degenerate uniform patterns.

## Weaknesses

### Fatal
None.

### Major
None. The core claims are supported by sufficient experimental evidence, and no weakness invalidates the paper's contribution.

### Minor

1. **Growth-phase initialization is underspecified**: Algorithm 1 says "Grow $\mathcal{M}_{\text{tgt}}$ by inheriting additional layers" but does not specify which layers from the reference model are used, how they are selected, or how they are incorporated. The introduction mentions that "the newly added blocks can be initialized with *lazy layers* of the reference LM," and GPT-2 Medium undergoes three growth rounds (12→14→16 layers), but the exact source and initialization of the added layers (e.g., copied from specific reference layers vs. randomly initialized) are not stated in the experimental setup (Section 4). This does not invalidate the results, but it compromises full reproducibility and leaves a gap in understanding what drives the growth step's benefit. An ablation of growth initialization would settle this.

2. **The claim that lazy layers "cannot learn anything meaningful" is stronger than the evidence supports**: The main evidence is a 10K-step fine-tuning experiment (Fig. 1c,f) showing that models initialized with lazy layers perform comparably to random initialization, while early-layer initialization is much better. Ten thousand steps is short compared to the 100K steps used in the main Inheritune experiments, so it tests initial transferability rather than the capacity of these layers to be retrained. The paper later acknowledges that lazy layers "can be collapsed into fewer layers and re-trained" (Section 3), which implicitly recognizes their recoverability. The framing would be more precise if softened to "exhibit reduced transferability when used as initialization" rather than "unable to learn anything meaningful."

3. **No justification for the choice of $n = k/2$ as the starting size**: The paper initializes the target model with $n = k/2$ layers from the reference without discussing why half is the right fraction. A different choice (e.g., $k/3$, $2k/3$) could change the method's efficiency or final performance. While the results are strong with $k/2$, the paper would benefit from an ablation or at least a brief justification.

4. **No error bars or confidence intervals on downstream results**: The downstream evaluations in Table 4 (e.g., 48.08 vs. 47.74 for Medium) show small absolute differences. Without measures of variance, it is unclear whether these improvements are statistically significant. The main pretraining loss comparisons are more definitive, but the downstream claims would be stronger with error bars.

5. **Only GPT-2 family tested, limiting architectural generality**: All experiments use GPT-2 variants (pre-LayerNorm, learned absolute positional embeddings). The paper claims results hold for "standard decoder-style LLMs," but modern architectures (e.g., with Pre-RMSNorm, RoPE, SwiGLU) are not tested. A discussion of expected transferability would strengthen the generality claim.

6. **For GPT-2 xLarge, hybrid-stacking ties with Inheritune (2.64 vs. 2.64)**: The paper states that Inheritune "consistently outperforms" these baselines (Section 4, line 322), which is true for Medium and Large but not perfectly accurate for xLarge hybrid-stacking. The paper's caption (Table 2) more accurately says "consistently achieve lower loss" — still, for xLarge the loss is identical. Separately, the 24-layer random-init model trained for 200K achieves 2.62, which is better than Inheritune's 2.64 at 100K — the paper acknowledges this (line 320–321) and frames it as "the only exception," which is appropriate.

### Trivial
None.

## Nice-to-Haves

- **Ablation of growth initialization**: Compare (a) initializing new layers from the reference's lazy layers, (b) random initialization, and (c) copying from the reference's early layers (stacking style). This would reveal whether the growth phase relies on weight reuse or is simply depth increase with more data.
- **Vary the initial fraction $n/k$** (e.g., $1/3$, $1/2$, $2/3$) to see whether $k/2$ is optimal or performance is insensitive to this choice.
- **Compare with a progressive growth baseline** where new layers are randomly initialized after the initial training phase, to isolate the benefit of weight inheritance during growth.
- **Report computational cost** (total training FLOPs or wall-clock time) to quantify net savings beyond final model size.
- **Brief discussion of whether findings transfer to modern LLM architectures** (e.g., Llama-family with RoPE, RMSNorm, SwiGLU).

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Abstract says 'attention matrices degenerate to single-column for deeper layers' – the paper shows this is common but not universal."* → Removed as a nitpick. The abstract's phrasing is reasonable and the paper provides statistical evidence showing the pattern holds across many deeper layers; it never claims it holds for every single layer.
- *"For xLarge, the 200K random-init baseline beats Inheritune – this shows it's not universally superior."* → Removed because the paper already acknowledges this explicitly (line 320–321: "The only exception is the 24-layer GPT-2 xlarge variant, which surpasses both our model and the full-size model when trained for 200K steps"). The authors are transparent about this limitation.
- *"Distillation comparison is unfair because vanilla KD uses random initialization."* → Removed because the paper includes both vanilla KD (random init) and DistillBERT-style KD (teacher-layer initialization). The DistillBERT-style comparison is a fair baseline, and the vanilla KD comparison is supplementary; the paper does not overclaim based on the random-init KD alone.
- *"Maximum rank across heads could be misleading; report proportion of heads per layer."* → This is a reasonable suggestion but downgraded to nice-to-have. Using maximum rank is a standard, defensible choice for summarizing multi-head attention.

## Novel Insights

The reviews surface one genuinely insightful observation beyond the paper's own contributions: the growth-phase initialization detail is the single most important missing piece. If future work showed that random initialization during growth works as well as reference-based initialization, it would suggest the benefit of Inheritune comes almost entirely from the initial early-layer inheritance and continued training, not from the growth mechanism itself. Conversely, if reference-based initialization is essential, the relationship between the "lazy layer" analysis and the growth procedure becomes more directly connected. This is a concrete, testable question that could sharpen the paper's core narrative.

## Suggestions

1. **Specify the growth initialization explicitly** in Algorithm 1 and the experimental setup: state which reference layers are used for each growth step and whether weights are copied as-is or transformed.
2. **Add an ablation comparing growth-initialization strategies** (reference lazy layers vs. random vs. early-layer copying) for the GPT-2 Medium case where growth occurs.
3. **Temper the claim about lazy layers** from "unable to learn anything meaningful" to "exhibit poor transferability as initialization and can be compressed without immediate loss" — this aligns better with the evidence and with the method's own use of these layers during growth.
4. **Add brief justification for the $k/2$ starting size** — even a short sentence explaining the rationale would help.
5. **Add error bars or confidence intervals** for the downstream zero-shot evaluations where differences are small.

## Score and Decision

**Originality**: Good — the empirical analysis of lazy layers in standard LLMs is novel, and the Inheritune recipe is simple yet effective.  
**Importance of research question**: High — finding principled ways to train smaller LMs without performance loss is practically important.  
**Claims well-supported**: Mostly yes, with some minor overstatements about lazy-layer irredeemability and "consistently outperforms" for xLarge.  
**Soundness of experiments**: Solid across model scales and data regimes; the main pretraining loss results are convincing, though downstream results lack error bars.  
**Clarity of writing**: Generally clear, but the growth-phase initialization is underspecified and the lazy-layer analysis could be better scoped.  
**Value to the research community**: Practical value for practitioners seeking to derive small models from larger ones; the lazy-layer analysis also contributes to the understanding of deep transformer attention behavior.

The paper makes a real contribution: it identifies a structural inefficiency in standard LLMs, proposes a simple method that demonstrably works across multiple scales and data regimes, and provides reasonable baselines. The weaknesses are real but minor — they do not threaten the core claims and are addressable with clarifications and modest additional experiments. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>