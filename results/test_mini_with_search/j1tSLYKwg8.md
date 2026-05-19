## Summary

This paper proposes a practical method for converting pre-trained autoregressive (AR) language models (GPT2 and LLaMA2, 127M–7B parameters) into diffusion language models (DiffuGPT and DiffuLLaMA) via a lightweight continual pre-training recipe. The approach bridges the gap between AR and diffusion modeling through three components: attention mask annealing (transitioning from causal to bidirectional attention), a shift operation (maintaining the next-token prediction interface), and a time-embedding-free design. The authors scale DLMs to 7B parameters for the first time, provide a comprehensive evaluation across 8+ tasks beyond perplexity, and show that the adapted models outperform prior DLMs and are competitive with their AR counterparts on several benchmarks.

## Strengths

- **First demonstration of AR-to-DLM conversion at scale (up to 7B).** The paper shows that a lightweight adaptation recipe — 200B tokens for GPT2-based models, 60B for LLaMA2 — can convert off-the-shelf AR models into competitive DLMs, establishing a practical paradigm that subsequent works (Efficient-DLM, Fast-dLLM v2, etc.) have built upon. The 7B DiffuLLaMA model is the largest discrete DLM at the time of the work and shows emergent in-context learning capabilities (Table 2: zero-shot→few-shot improvements on TriviaQA, MAWPS, SATMATH).

- **Controlled ablation validates the adaptation components.** Table 3 (GSM8K-symbolic finetuning) provides clean, isolated evidence: using the discrete diffusion (DD) loss with the proposed adaptation recipe (mask annealing + shift operation) outperforms both DD fine-tuning without these components and standard AR fine-tuning, all starting from identical GPT2 checkpoints. This ablation directly attributes the benefit to the method rather than to data or scale.

- **Theoretical unification of AR and diffusion objectives.** Section 3.2 formally connects the discrete-diffusion ELBO (Eq. 4) with the autoregressive cross-entropy (Eq. 5), revealing AR as a special case of deterministic mask-based diffusion. This provides a principled foundation for why adaptation is plausible and why discrete diffusion aligns better with AR than continuous diffusion does.

- **Comprehensive evaluation beyond perplexity.** The paper evaluates on 8 tasks spanning language modeling (Lambada, TriviaQA), commonsense reasoning (HellaSwag, Winogrande, SIQA, PIQA), math reasoning (GSM8K), code infilling (HumanEval), and story infilling (ROCStories), with zero-shot, few-shot, and fine-tuning settings. This moves beyond the perplexity-only evaluation of prior DLM work and reveals capability differences (e.g., DLMs excelling at infilling and math reasoning).

- **Honest reporting of limitations.** The paper explicitly acknowledges where DiffuLLaMA falls short of LLaMA2 (attributed to insufficient training), notes when the comparison for infilling may be unfair to AR models (§4.2, lines 213–214), reports that mask annealing has minimal impact on the 7B model, and opens discussion of knowledge loss in domains requiring factual recall.

## Weaknesses

### Fatal

None.

### Major

- **Confounded GPT2 comparison weakens the central claim.** The paper states "DiffuGPT outperforms GPT2 in most tasks" (abstract, line 34; §4.3, line 209), but DiffuGPT is a *continually pre-trained* version of GPT2 on 30B tokens from FineWeb (a larger, more recent corpus), while the GPT2 baseline is the original model trained on WebText. This conflates two effects: the diffusion adaptation method and the additional training data. The paper acknowledges the data difference (line 173: "an improved corpus than OpenWebText") but still presents the comparison as evidence for the method's value. The only controlled experiment isolating the diffusion objective from the data effect is the GSM8K-symbolic finetuning ablation (Table 3), which is a narrower finetuning setting — not the base-model continual pre-training comparison that the headline claim refers to. This does not invalidate the contribution (the ablation still supports the recipe's value in the finetuning regime, and the comparisons against other DLMs are clean), but the framing overstates the evidence. The claim should either be properly controlled (continue-train GPT2 with the AR objective on the same FineWeb data) or appropriately tempered.

### Minor

- **Multiple-choice evaluation procedure is underspecified.** The paper says "For 4 multi-choices tasks from commonsense reasoning, we compute the loss (Eq. L_T) of each choice (averaged by token) and choose the one with lowest loss" (line 205). However, Eq. L_T involves sampling a timestep *t* and computing a loss over *masked* tokens in a corrupted input. It is not specified how this is applied to a complete, clean multiple-choice option — whether a timestep is sampled, which positions are masked, or whether the loss is averaged over multiple timesteps. Without this detail, the fairness of comparisons with AR models (which use standard log-perplexity) is unclear. (The authors can likely clarify this in a rebuttal; the concern does not undermine the core claims.)

### Trivial

- The ablation shows that attention mask annealing has minimal impact (Table 3: GSM8K-symbolic 45.4→44.6 for small), and the paper omits it entirely for the 7B model. Calling it a "key component" in the abstract (line 28) slightly overstates its role — the framing could be adjusted to reflect the empirical evidence.

## Nice-to-Haves

- A combined figure showing quality (perplexity/accuracy) vs. wall-clock time for different diffusion steps would directly show the Pareto frontier and strengthen the speed-quality discussion.
- The 7B model ablation on the shift operation (at a small-scale proxy) would increase confidence that the recipe generalizes beyond the finetuning setting.
- A dedicated limitations section (separate from the conclusion) discussing knowledge preservation challenges, the instruction-tuning gap, and the inherent biases inherited from AR parent models would be useful for readers.

## Removed Points

*These are points from the inputs that were removed because they are factually incorrect, misunderstand the paper, or do not constitute valid weaknesses:*

- **"Unification of AR/diffusion is not new — already noted in Austin et al. (2021)"**: The paper already cites Austin et al. (2021) and Hoogeboom et al. (2022) in the exact relevant passage (line 119). The criticism is factually wrong.
- **"FIM-capable AR baseline missing for infilling"**: The paper explicitly acknowledges this limitation (lines 213–214: "Regular LLMs like LLaMA2 are not trained for FIM... which might result in an unfair comparison"). The paper already scopes this appropriately.
- **"ICL evaluation is weak"**: The paper describes the ICL results as suggestive ("suggests that DiffuLLaMA can learn from ICL examples," line 235) rather than conclusive, using modest language consistent with the evidence.
- **"Missing limitations section"**: A formatting preference, not a substantive weakness.
- **"Mask annealing is not a key component"**: A minor framing observation elevated to a weakness. The ablation shows small impact, but the paper's own text handles this honestly.
- **"Missing comparison with time-embedding variant"**: A nice-to-have ablation that is not standard for the setting.

## Novel Insights

None beyond the paper's own contributions. The reviews surfaced the core confound issue (GPT2 comparison confounded by data) and the MC evaluation underspecification, both of which the paper would benefit from addressing, but these are not novel observations about the paper's approach itself.

## Suggestions

1. **Run a controlled continual pre-training experiment.** At the 127M/355M scale (where compute is feasible), continue-train GPT2 on the *same* FineWeb data using the *standard AR objective*, and compare DiffuGPT against this "AR-continued" baseline. This directly tests whether the diffusion adaptation yields a net benefit over simply adding more data to the AR model. If the results support DiffuGPT, the headline claim is fully substantiated; if not, the claims should be tempered.

2. **Specify the multiple-choice evaluation protocol precisely.** Describe whether a timestep is sampled, whether the loss is averaged over all timesteps, and whether masking is applied to the clean option. Report the variance across multiple timestep samples if applicable.

3. **Add a small-scale proxy for the shift-operation ablation at the 7B scale** (e.g., on a representative task subset with a distilled proxy) to confirm the recipe's generalization beyond the finetuning setting.

## Score and Decision

**Bracketing (Round 1):** I queried for papers on similar topics (DLM adaptation from AR models) across score bands. Weak anchors (scores ≤ 3) include papers with flawed methodology or minimal contributions — clearly below this paper. Strong anchors (scores ≥ 8) address different problem settings (transduction, scaling laws, protein generation) and are not comparable. This placed the paper in the [4, 7] bracket.

**Narrowing (Round 2):** I retrieved and read full reviews for four relevant anchors in the 4.5–7.5 range:
- *Efficient-DLM* (avg 5.00, Reject): A follow-up that builds on this paper's approach but was criticized for incremental novelty (combining block diffusion + AR init). The paper under review is the *original* work and avoids novelty concerns that apply to its follow-ups, making it stronger than this anchor.
- *Dual-objective LM* (avg 5.50, Accept): Combines AR + diffusion objectives. Similar quality tier — both have clear contributions with notable limitations. This paper offers a more impactful practical paradigm (AR→DLM conversion used by later works).
- *Fast-dLLM v2* (avg 6.00, Accept): Block-diffusion adaptation from AR models. More impressive speed results but builds on the paradigm this paper introduced. The paper under review is slightly weaker on controlled evaluation but more foundational.
- *DLM Knows Answer* (avg 6.50, Accept Oral): DLM inference acceleration. Different contribution type but similar quality tier.

**Final score: 5.5.** This paper sits between the 5.00–5.50 anchors (the confound issue is real and tempers the core claim) and the 6.00 anchor (less controlled evaluation than Fast-dLLM v2). However, it is the *original* AR→DLM conversion work — the paradigm it established has been adopted and cited by multiple subsequent papers at top venues — which strengthens its contribution. The paper provides a solid, well-motivated method with clear ablations, honest reporting, and a useful theoretical connection, but the overclaimed GPT2 comparison weakens the headline evidence.

**Decision: Accept**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>