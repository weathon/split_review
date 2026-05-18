Now I have thoroughly verified all claims against the paper. Here is my consolidated final review.

---

## Summary

This paper presents DPLM-2, a multimodal extension of the discrete diffusion protein language model DPLM that jointly models protein sequences and 3D structures. The key ideas are: (1) tokenizing backbone coordinates into discrete tokens via a lookup-free quantization (LFQ) tokenizer, (2) warm-up initialization from pre-trained sequence-only DPLM with LoRA to preserve sequence knowledge, and (3) joint training on experimental (PDB) and predicted (SwissProt) structures. DPLM-2 achieves competitive performance on unconditional co-generation (sc-TM 0.845), folding, inverse folding, and motif scaffolding, while also providing structure-aware representations for predictive tasks.

## Strengths

1. **Simultaneous sequence-structure co-generation with strong structural compatibility.** DPLM-2 generates both amino acid sequences and 3D structures in a single step, achieving sc-TM of 0.845 in unconditional co-generation, outperforming Multiflow (0.753) and approaching native PDB quality (0.90), without relying on external inverse folding models for distillation. This is the paper's central technical achievement and is convincingly demonstrated.

2. **Efficient warm-up from pre-trained DPLM with LoRA.** The paper shows that initializing from pre-trained DPLM with LoRA fine-tuning enables effective multimodal learning using only ~220K structural examples. Table 4 provides quantitative evidence: adding sequence pre-training improves sc-TM from 0.734 to 0.806 for long proteins (>300 residues) and doubles diversity clusters. This is a practical contribution that reduces the data and compute barrier for multimodal protein models.

3. **Novel structure tokenization with LFQ.** The paper introduces a lookup-free quantization tokenizer for protein backbone coordinates. Figure 1 reports substantially better reconstruction accuracy and faster training (2 vs. 15 days on 8 A100s) compared to VQ-VAE, with a codebook size of 8192 providing the best compression-reconstruction trade-off. The correlation between structure tokens and secondary structure is demonstrated, supporting the tokenizer's interpretability.

4. **Comprehensive evaluation across diverse generative tasks.** The paper validates DPLM-2 on unconditional co-generation, folding, inverse folding, and motif scaffolding, with standardized metrics and comparisons against strong baselines (Multiflow, ESM3, RFDiffusion, ESMFold). In motif scaffolding, DPLM-2 solves more problems and achieves higher success rates than both Multiflow and ESM3. The breadth strengthens the claim that DPLM-2 is a genuine multimodal foundation model.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The relationship between LoRA and the observed catastrophic forgetting in representation learning needs clarification.** The paper states that LoRA is applied to "keep the sequence knowledge intact and reduce the risk of catastrophic forgetting" (§3.2), yet later attributes DPLM-2's weaker representation results to "potentially causing catastrophic forgetting" from the smaller structure dataset (§4.5). These are not contradictory — LoRA reduces risk but does not eliminate it — but the paper would benefit from explicitly discussing why generation tasks are less affected than representation tasks. A plausible explanation is that LoRA preserves the model's *generative* capacity (which the generation metrics test) more than the *representational* quality on specific downstream tasks, but this is not discussed. The paper should also state more clearly whether LoRA is applied throughout all multimodal training stages (including for the model evaluated on understanding tasks), which reading §3.2 suggests is the case, but is never explicitly confirmed.

2. **The self-mixup strategy is listed as a key recipe but insufficiently described in the main text.** The introduction (third bullet) and §3.1 mention the self-mixup strategy for mitigating exposure bias in discrete diffusion, but the main text provides only a one-sentence description and a reference to an appendix section (§self-mixup). Since the appendix content is not available in the main body, readers cannot assess this claimed contribution. While the appendix likely contains the full description in the original submission, the main text would benefit from at least a brief summary of the idea (a few sentences) and ideally an ablation showing its impact on a generation metric. This is a presentation issue rather than a technical flaw, and does not undermine the paper's core contributions.

3. **Reproducibility detail: the multimodal training objective sampling procedure is underspecified.** Equation (3) gives the training loss and mentions "distinct scheduler" for structure and sequence with notation \(t_\mathbf{z}\) and \(t_\mathbf{s}\), but the paper does not specify how these noise levels are sampled during training (e.g., independently, coupled, or with a joint schedule). This detail matters for reproducibility and for understanding the conditional generation capabilities. Clarifying this would strengthen the paper.

### Trivial

- The paper reports quantitative generation results as single numbers without uncertainty estimates (standard deviations or confidence intervals). For generative models, sampling variability can be meaningful; adding these would improve reliability. (This is standard practice for large-scale generative model evaluations, so it is a minor presentation point rather than a flaw.)

## Nice-to-Haves

- An ablation isolating the effect of the warm-up strategy beyond presence/absence of pre-training (e.g., fine-tuning DPLM without LoRA, or varying the amount of structure data) could further illuminate what drives the performance gains.
- A breakdown of motif scaffolding success rates per problem (rather than aggregated) would add granularity to the analysis, since some motif problems are intrinsically harder than others.
- A brief analysis of structure token-level geometric meaning (e.g., correspondence to local backbone angles beyond secondary structure categories) would strengthen the tokenizer evaluation.

## Removed Points

These points from the reviews were removed after verification against the paper:

- **"Direct contradiction" between LoRA and catastrophic forgetting claim** — Removed because the paper says LoRA reduces *risk* of forgetting, not that it eliminates it entirely. No contradiction exists; the two statements are compatible. The underlying clarification question is kept as Minor #1 above.
- **Self-mixup "not described" / "significant gap" due to missing appendix** — The appendix is present in the original submission but stripped by the parser. The criticism that the main text should be more self-contained is kept as Minor #2; the claim that this is a "significant gap" is downgraded.
- **Distribution shift in representation evaluation** — The paper already acknowledges this limitation and conducts a control experiment (DeepLoc without pre-training) to test the hypothesis. This is good scientific practice, not a weakness. Removed.
- **Strength Finder generic strength about "comprehensive evaluation across diverse tasks"** — Verified as adequately specific and backed by actual content; kept.
- **Case study about symmetric oligomers lacking quantitative evaluation** — This is a qualitative demonstration, not a claimed rigorous result. Removed as expecting a quantitative scoring function for a case study figure is beyond reasonable scope.

## Novel Insights

The most interesting insight that emerges across the reviews — beyond the paper's own claims — is the asymmetry between generation quality and representation quality under the same LoRA-based fine-tuning regime. The paper observes that generation tasks (co-generation, folding, inverse folding) are strong, while representation tasks lag behind DPLM and SaProt. The DeepLoc control experiment (where removing sequence pre-training improves performance) suggests this is a data-scale issue rather than a fundamental architectural limitation. This asymmetry is actually informative: it implies that generative capability (producing plausible sequences and structures) and representation quality (discriminative features for downstream tasks) respond differently to the same fine-tuning perturbation, which may merit deeper investigation in future work.

## Suggestions

1. In §3.2 and §4.5, add a few sentences explaining why generation and representation tasks might be differentially affected by LoRA and the smaller structure dataset. Acknowledge explicitly that LoRA mitigates but does not fully prevent forgetting.
2. Add a 2-3 sentence summary of the self-mixup strategy to §3.1 (or early in the experiments section), so that the main text is self-contained for this claimed contribution. If space permits, include one ablation result showing its effect on a generation metric.
3. Clarify the training objective in §3.1 by specifying how \(t_\mathbf{z}\) and \(t_\mathbf{s}\) are sampled (independently? jointly? with what distributions?).
4. Add standard deviations or confidence intervals to the key generation metric tables (Tables 1-2) in the final version.

## Score and Decision

**Originality:** Good — extending a discrete diffusion PLM to multimodal joint modeling with structure tokenization and efficient warm-up is a well-motivated and non-trivial combination.  
**Importance:** High — multimodal protein foundation models are of growing interest, and the efficient warm-up strategy has practical value for the community.  
**Claims support:** Well-supported for generative tasks; representation learning claims are honestly qualified with acknowledged limitations.  
**Soundness:** The experiments are thorough, baselines are appropriate (including the Multiflow retrained on the same data), and limitations are discussed.  
**Clarity:** Generally clear; minor gaps in training procedure specification and self-mixup description.  
**Value:** The released model weights and code will be a useful resource for the protein design community.

The paper makes a solid empirical contribution with a well-executed approach and honest reporting of limitations. The weaknesses are minor and addressable through clarifications.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>