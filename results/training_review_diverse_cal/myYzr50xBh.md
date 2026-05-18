Now I have a comprehensive understanding of the paper and all reviewer inputs. Let me produce the final consolidated review.

## Summary

This paper proposes SensZOQ, a zeroth-order (ZO) fine-tuning method that identifies an extremely sparse (0.1%) static subset of "sensitive" parameters—derived from a single forward-backward pass on C4 pre-training data—and updates only these parameters with ZO-SGD while keeping the rest of the model quantized to 4 bits. The combined pipeline fits Llama2-7B fine-tuning within 8 GiB of GPU memory and outperforms full ZO fine-tuning, ZO LoRA/Prefix Tuning, and in-context learning across a suite of discriminative NLU tasks.

## Strengths

- **Transferable static sparsity is convincingly demonstrated.** Figure 3 shows that the C4-derived static mask retains a large fraction of cumulative normalized gradient squares throughout fine-tuning on downstream tasks, and Figure 5b confirms that at 0.1% sparsity the gap between C4-derived and task-specific masks is small. This is the paper's central empirical contribution and it is well-supported.

- **Extreme sparsity (0.1%) combined with 4-bit quantization enables a practical memory target.** Figure 1 validates that SensZOQ fits Llama2-7B ZO fine-tuning within 8 GiB GPU memory—a clean, actionable result for on-device deployment—while Table 1 shows it outperforms ZO Full FT, ICL, and ZO PEFT baselines on most tasks.

- **Sensitive-parameter masks are shown to be uniquely effective at extreme sparsity.** Figure 5a demonstrates that the sensitive-parameter method maintains near-flat accuracy from 10% down to 0.1% sparsity, whereas weight-magnitude baselines (largest, smallest) and GraSP drop sharply below 1%. This provides strong evidence that the mask selection criterion, not just any sparsity, is responsible for the gains.

- **Practical trade-off demonstrated via smaller-model comparison.** Table 2 shows that SensZOQ on OPT-6.7B (under 8 GiB) outperforms FO-Adam full fine-tuning on OPT-1.3B (which exceeds 8 GiB), making a concrete case for the memory–accuracy compromise.

- **Clear motivation for static over dynamic sparsity.** Sections 1 and 3.1 articulate why prior dynamic sparse ZO (SparseMeZO) is incompatible with quantization and incurs wall-clock overhead—this framing justifies the central design decision.

## Weaknesses

### Fatal
None.

### Major

- **Task scope is narrower than the paper's own framing.** The paper evaluates on 8 discriminative NLU tasks (SST-2, RTE, CB, BoolQ, WSC, WiC, COPA, WinoGrande) and one language-modeling perplexity task (Wiki2). However, the paper motivates SensZOQ with on-device personalization scenarios (mobile assistants, email drafting, instruction following) and claims "transferability" broadly. No generative instruction-following, summarization, or open-ended generation tasks are evaluated. The claim at line 125 about taking a "pioneering step" on math tasks is also unsupported—no math benchmarks are presented. The core empirical result (static mask works for ZO fine-tuning) is not invalidated, but the claims about transferability and on-device personalization need to either (a) be tempered to reflect the discriminative NLU scope actually tested, or (b) be supported by at least 1–2 generative tasks (e.g., summarization of short texts, instruction following).

### Minor

- **Theoretical grounding of the static mask is over-promised.** Theorem 1 is mentioned in Section 3.1 ("Our Theorem 1 focuses on dynamic sparse fine-tuning") but is not stated or even sketched in the main text. The paper then relies on empirical evidence (Figure 3, Figure 5b) and cites prior work (Panigrahi et al., Malladi et al.) to argue that static sparsity works. This is a reasonable approach, but the dangling reference to an unseen theorem creates an impression of theoretical depth that the main text does not deliver. The authors should either provide a brief statement of Theorem 1's content and assumptions, or drop the theoretical framing and present the paper as purely empirical.

- **Memory cost of mask generation is not reported.** Computing the C4 gradient mask requires a backward pass on the full model. The paper does not state how many C4 examples are used, the GPU time required, or whether this backward pass itself fits within 8 GiB. If it must be done on a server, this changes the deployment story for on-device personalization. The authors should disclose this cost and clarify whether the mask is generated offline.

- **No discussion of gradient estimation variance at extreme sparsity.** With only 0.1% of parameters perturbed per step, the ZO gradient estimate is extremely sparse. The paper does not discuss whether additional steps or larger batch sizes are needed to compensate for increased variance, nor does it compare convergence curves (steps to plateau) across methods—only final accuracy is reported.

- **Overclaim on "pioneering step" for math/harder tasks.** Line 125 states that "there are no ZO-LLM research yet evaluated on harder commonsense reasoning or math tasks" and that the paper takes "a pioneering step in this direction." While COPA and WinoGrande are valid commonsense reasoning benchmarks, no math results are presented. This statement should be corrected.

- **Memory profiling is only shown for Llama2-7B.** Figure 1 profiles only Llama2-7B. While the paper evaluates Mistral-7B and OPT-6.7B on accuracy (Table 1), confirming that these models also fit under 8 GiB with the same pipeline would strengthen the generality claim.

### Trivial
None.

## Nice-to-Haves

- **Comparison with QLoRA on the same 4-bit base** would provide a first-order upper bound for the memory–accuracy trade-off. This is not required (the paper's contribution is a ZO method, and QLoRA uses backprop), but it would contextualize how much accuracy is sacrificed by avoiding backpropagation.
- **Per-layer breakdown of the C4-derived mask** (attention vs. MLP, layer-by-layer heatmap) would help readers understand what the mask selects and build intuition for when it might fail.
- **Ablation at sparsity levels below 0.1%** (e.g., 0.01%) would better characterize the drop-off region and strengthen the claim that 0.1% is a reasonable choice.
- **Testing with alternative quantization schemes** (GPTQ, AWQ) would probe the generality of the interaction between static sparsity and quantization.

## Removed Points

- **"Narrow evaluation scope" treated as fatal:** The harsh critic initially framed this as a near-fatal issue, but the core claim (static 0.1% mask works for ZO fine-tuning) is validated on 9 datasets across 3 models. The scope limits *generalization claims*, not the central empirical contribution; kept as Major but not Fatal.
- **Missing QLoRA comparison treated as a critical gap:** This is a cross-paradigm comparison (ZO vs. FO). The paper's contribution is specifically a ZO method; QLoRA is a different class of approach requiring backprop. Downgraded to Nice-to-Have.
- **"No generative tasks" overstatement:** Wiki2 (language modeling perplexity) is a generative evaluation, though not task-oriented generation. Adjusted wording accordingly.
- **Request for more models in memory profiling:** Single-model profiling is standard for memory benchmarks. Downgraded to Minor.
- **Formatting/parser artifacts and missing appendix content:** Removed per instructions (the appendix containing Theorem 1 and additional tables exists in the original submission; the parser cannot include it).

## Novel Insights

The reviews collectively highlight a tension that the paper itself does not fully address: the empirical success of a *static* pre-training–derived mask for ZO fine-tuning is hard to reconcile with the theoretical machinery (Theorem 1) that is invoked but applies only to dynamic sparsity. The paper is effectively saying "dynamic sparsity has guarantees, and we observe empirically that a static mask works just as well due to fixed gradient features during fine-tuning"—but this observation deserves a dedicated analysis (e.g., measuring how much the gradient features actually drift during fine-tuning at different sparsity levels) rather than a brief citation of Malladi et al. The real novelty is the *practical combination* of 0.1% static sparsity + 4-bit quantization, and the paper would be stronger if it leaned into this engineering contribution rather than reaching for theoretical framing that requires heavy qualification.

## Suggestions

1. **Add at least one generative task** (e.g., summarization of short chat histories or instruction-following) that is directly relevant to the on-device personalization scenario, OR temper the abstract/intro claims to match the discriminative NLU scope tested.
2. **Correct the unsupported claim** about evaluating on "math tasks" (line 125).
3. **Briefly state Theorem 1's content** (or its conclusion) in the main text so readers can follow the theoretical connection without consulting the appendix.
4. **Report the computational cost** of generating the C4 mask: number of examples, GPU time, and peak memory usage. Disclose whether mask generation fits within 8 GiB.
5. **Add a limitations paragraph** discussing when the C4-derived mask might fail (e.g., domain shift, non-English tasks, tasks requiring different output modalities).
6. **Include convergence curves** (accuracy/perplexity vs. steps) comparing SensZOQ with baselines to address the variance concern.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>