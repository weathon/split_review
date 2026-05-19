- Decision: Reject
- Avg Score: 5.17
- Scores: 5, 6, 6, 5, 6, 3
Now I have a thorough understanding of the paper and the reviewer claims. Let me produce the final consolidated review.

## Summary

This paper introduces DiMA, a latent Gaussian diffusion model for unconditional and conditional protein sequence generation that operates on continuous encodings from protein language models (ESM-2 or CHEAP). The method trains a 33M-parameter diffusion transformer to denoise pLM latent representations, then decodes them to amino acid sequences. The paper presents a thorough ablation study of architectural choices, compares against 10+ baselines trained under identical conditions, demonstrates generalization to the CHEAP encoder, and showcases conditional generation capabilities via family-specific generation and inpainting.

## Strengths

- **Systematic ablation isolating each design choice (Section 4.2, Table 1)**: The paper quantifies the individual contribution of every component (skip-connections, time conditioning, encoder, self-conditioning, noise schedule, padding masking, decoder finetuning, flow matching) by training models from scratch with one modification at a time. This directly supports the claim that architectural choices matter and provides practical guidance for future work.

- **Fair controlled comparison against 10+ baselines (Section 4.5, Table 3)**: DiMA is compared against autoregressive (RITA, nanoGPT, SeqDesign), discrete diffusion (EvoDiff-OADM, DPLM, D3PM), GAN (ProteinGAN), flow (DFM), and score-based (Walk-Jump) models, all trained from scratch with the same parameter budget (33M) on the same datasets (SwissProt, AFDBv4-90). This is a comprehensive and fair evaluation setup.

- **Demonstrated generalization to a different latent space (Section 4.4)**: Applying DiMA's architecture and hyperparameters without modification to CHEAP encodings yields pLDDT scores (80.3, 81.4) closely matching the dataset (80.7) and FD-seq competitive with the best ESM-2 variant, showing the framework is robust across embedding spaces.

- **Encoder scaling study with clear quality-diversity tradeoff (Section 4.3, Table 2)**: The systematic comparison of ESM-2 sizes (8M to 3B) using two adaptation strategies reveals that larger encoders improve quality but can reduce diversity when the diffusion model capacity is fixed — an informative finding for practitioners.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core methodology is sound, the experiments are extensive, and the claims are largely supported by the evidence presented.

### Minor

- **Imprecise parameter count claims in the abstract and conclusion**: The abstract states DiMA achieves "superior quality, diversity, and distribution matching capabilities...while utilizing ten times fewer parameters," and the conclusion claims "comparable protein generation quality with multibillion models while utilizing a hundred times fewer parameters." These statements conflate DiMA's 33M inference-time diffusion model with the full training pipeline that depends on a frozen ESM-2 encoder (up to 3B parameters). While Section 4.3 does clarify that "during inference, the encoder model can be discarded," the headline claims in the abstract and conclusion lack this crucial context and could mislead readers about the resource tradeoffs. The authors should explicitly state "inference-time model" when making parameter count comparisons.

- **Missing variance information in key comparison tables (Table 1, Table 3)**: The ablation and baseline comparison tables report only point estimates without standard deviations or confidence intervals. Many metric differences between variants (e.g., pLDDT deltas of 1–2 points in Table 1) are small enough that their statistical significance is unclear. Adding error bars or reporting variance over multiple runs/seeds would substantially strengthen the experimental rigor.

- **Insufficient detail on DPLM conditioning setup for inpainting (Section 4.6)**: The inpainting comparison with DPLM is described in one sentence: "Baselines are random and DPLM, because it can be straightforward used for this task." How DPLM was conditioned on unmasked regions is not specified, making it impossible for readers to assess whether the comparison is fair. The DiMA conditioning approach (adapter with 3 transformer blocks) is described; the DPLM counterpart should be described with equal detail.

- **No dedicated limitations section**: The paper lacks an explicit discussion of limitations. Important caveats include: (a) all structural quality evaluations rely on predicted pLDDT (ESMFold) rather than experimental validation; (b) conditional generation experiments use an adapter-based approach whose generalization properties are unexplored; (c) performance on very long sequences (>1000 residues) is not evaluated. While Section 4.1 does discuss metric tradeoffs, a dedicated limitations paragraph would improve completeness.

### Trivial

None.

## Nice-to-Haves

- Reporting inference wall-clock time or FLOPs for DiMA and baselines would strengthen the efficiency claim beyond raw parameter count.
- Training a larger diffusion model (e.g., matching the 150M range) with the ESM-2 3B encoder would test the capacity bottleneck hypothesis directly, rather than leaving it as a suggested future direction.
- Including a summary figure or table of the pretrained model comparison (currently deferred to Table 8 in the appendix) in the main paper would make the "hundred times fewer parameters" claim more concrete.

## Removed Points

- **"Evaluation relies entirely on computational predictions" (Harsh Critic)**: The paper explicitly acknowledges metric limitations in Section 4.1 ("No single metric is sufficient for evaluating protein sequence quality..."), and reliance on pLDDT is standard practice in computational protein design. The paper does not claim experimental validation, and the critique applies equally to all compared baselines.

- **"Encoder scaling analysis is speculative" (Harsh Critic)**: The paper frames the capacity-bottleneck explanation as a hypothesis ("These findings suggest...we likely need to scale up the diffusion model accordingly"), not a concluded result. Asking for a larger-diffusion-model experiment is a fair suggestion but not a weakness of the presented analysis.

- **"Inference speed not reported" (Harsh Critic)**: Moved to Nice-to-Haves. The paper's primary contribution is methodological, not a systems benchmark.

- **"Decoder design unclear" (Harsh Critic)**: The paper states "The decoder architecture comprises a single linear layer" and that it is finetuned from the ESM-2 output head. This is sufficiently clear.

- **Generic concerns about metric validity (Harsh Critic section headings like "method soundness, evaluation validity")**: These are category-level lenses, not specific identified problems. Removed per filtering rules.

- **Generic/superficial strengths from Strength Finder**: None identified — all listed strengths are specific and grounded.

## Novel Insights

The reviews do not surface genuinely novel observations beyond the paper's own contributions. The most interesting insight from the cross-review is the tension around parameter accounting: the paper's central efficiency claim is simultaneously its most attention-grabbing contribution and its most fragile framing. The encoder scaling experiment revealing a quality-diversity tradeoff at fixed diffusion model capacity is perhaps the paper's most understated practical finding — it suggests that to fully utilize large pLMs, the generative model must be scaled alongside the encoder, which has important implications for practitioners deciding where to allocate compute.

## Suggestions

1. **Clarify the parameter count framing**: In the abstract and conclusion, replace "ten/hundred times fewer parameters" with precise language such as "DiMA's 33M-parameter inference model achieves comparable quality to multibillion-parameter models" and note the reliance on a frozen ESM-2 encoder during training. This would make the claim both accurate and appropriately contextualized.

2. **Add variance estimates** to Table 1 (ablation) and Table 3 (baseline comparison). Even reporting results from 2–3 random seeds with standard deviations would significantly increase confidence in the reported rankings.

3. **Expand the inpainting experiment description** to specify how DPLM was conditioned on unmasked regions, enabling reproducibility of the comparison.

4. **Add a brief limitations paragraph** addressing the reliance on computational structural metrics, the scope of conditional generation evaluation, and the unexplored regime of very long sequences.
