Here is my consolidated final review:

---

## Summary

DPLM-2 extends the discrete-diffusion protein language model (DPLM) from sequence-only to joint sequence-structure modeling. It uses a lookup-free quantization (LFQ) tokenizer to discretize 3D backbone coordinates, warms up from the pre-trained DPLM with LoRA, and trains on ~220K experimental and AF2-predicted structures. The resulting model performs unconditional sequence-structure co-generation, folding, inverse folding, motif-scaffolding, and structure-aware representation learning — all within a single architecture, without cascaded external models.

## Strengths

- **Effective LFQ-based structure tokenization enables discrete multimodal protein LMs.** The paper demonstrates that LFQ achieves substantially better reconstruction accuracy than VQ-VAE (Figure 2A) while reducing training time from 15 days to 2 days on 8 A100s. The learned tokens also exhibit strong correlation with secondary structure (Figure 2B), validating that discrete structural tokens capture meaningful local geometric information.

- **Pre-trained sequence LM warm-up with LoRA significantly improves co-generation quality.** The ablation (Table 5) shows that initializing from pre-trained DPLM with LoRA tuning dramatically improves designability (sc-TM) and diversity, especially for long proteins (length > 300). This supports the claim that evolutionary information from sequence pre-training transfers to multimodal modeling while LoRA mitigates catastrophic forgetting.

- **Simultaneous sequence-structure co-generation achieves competitive quality without cascaded models.** DPLM-2's simultaneous generation matches or exceeds cascaded approaches (sc-TM of 0.93 vs. 0.89 for structure→sequence) and approaches native PDB quality. The density plots (Figure 2A/B) confirm high designability across lengths 100–500.

- **Competitive conditional generation across multiple tasks without task-specific architectures.** DPLM-2 demonstrates strong performance on folding (zero-shot and SFT competitive with ESMFold), inverse folding (outperforms MultiFlow and ESM3 in AAR), and motif-scaffolding (solves more problems at higher success rate than RFDiffusion and ESM3 across sequence, structure, and co-generation evaluations).

- **Generated proteins more closely resemble natural secondary structure distributions.** Analysis (Figure 3A) shows DPLM-2's generated proteins match PDB secondary structure proportions more closely than structure-based models (RFDiffusion, MultiFlow) which overproduce helices, and ESM3 which overproduces loops.

- **Length extrapolation beyond training cutoff.** DPLM-2 maintains high pLDDT scores for proteins up to 1000 residues despite a 512-length training cutoff, indicating retention of sequence generation capability from pre-trained DPLM.

## Weaknesses

### Fatal
None.

### Major

- **The self-mixup strategy — claimed as a "key recipe" — is never evaluated or ablated.** The paper mentions self-mixup (§3.1, §4) as a method to mitigate exposure bias in discrete diffusion, claiming it "leads to enhanced generation quality and diversity." However, the ablation study (§4.1.3) tests only sequence pre-training and data augmentation; the effect of self-mixup on generation quality, diversity, or any other metric is never measured. For a component labeled as a core contribution, this is a significant methodological gap — readers cannot assess whether the generative results rely on this strategy or would hold without it.

### Minor

- **Structure tokenizer compared only to vanilla VQ-VAE, not to protein-specific alternatives.** The paper cites recent protein structure tokenizers (FoldToken, FoldSeek-based tokens, Gao et al.) as related work but does not compare against them on reconstruction accuracy or downstream task performance. While LFQ's superiority over standard VQ-VAE is convincingly shown, the tokenizer is a core enabler, and a comparison to more recent protein-specific alternatives (even on reconstruction metrics) would strengthen the paper's claims about tokenizer quality.

- **Representation learning claims are slightly stronger than the evidence.** Claim (iv) states that structure-aware representations bring "additional benefit for a range of protein predictive tasks," but §5.5 shows improvement only on "some tasks," with DPLM-2 falling behind SaProt on most tasks and even behind DPLM on certain tasks. The paper is transparent about this (catastrophic forgetting hypothesis, DeepLoc control experiment), but the framing in the introduction could be more precisely scoped to match what the evidence actually shows.

- **No error bars or confidence intervals for generative results.** Comparisons across unconditional generation, folding, inverse folding, and motif-scaffolding are presented as point estimates without variance. Given the stochasticity of diffusion sampling, reporting variability (e.g., across seeds) would help assess whether observed differences between methods are meaningful.

### Trivial

- None.

## Nice-to-Haves

- An ablation comparing training with and without the separate noise schedules ($t_z$, $t_s$) would further validate this design choice.
- Reporting inference time / number of diffusion steps would strengthen the efficiency claims made in the paper.

## Removed Points

These points were identified by the reviewers but have been removed or downgraded as per the filtering rules. They are listed here with brief justification:

- **"Self-mixup not described in main text"** — Removed per rule about missing appendix content (the description exists in §S of the appendix, which the parser strips from all papers).
- **"Representation learning claim is unsupported and partly contradicted"** — Removed as a Major weakness; the paper's own data (improvement on some tasks, DeepLoc control experiment) partially supports the claim, and the paper is transparent about limitations. The claim is slightly overstated (downgraded to Minor above), not contradicted.
- **"ESM3 characterization is an oversimplification"** — Removed as a factual dispute about another model's capabilities that does not affect the paper's contributions.
- **"Unconditional generation conflates joint/sequential generation"** — The specific claim about "statistical significance" and "which inverse folding model" cannot be verified without the tables (parser-stripped `\input` commands). The Multiflow retrained baseline is explicitly acknowledged by the authors (lines 341–343), so it is not a hidden weakness.
- **Strength Finder strengths: "Competitive conditional generation across multiple tasks" and "Length extrapolation"** — These were correctly identified and kept. No strengths were removed as generic or conflicting.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Ablate the self-mixup strategy.** Even a small-scale experiment (e.g., 100 generated proteins with/without self-mixup, reporting sc-TM and diversity) would tie the claimed "key recipe" to concrete evidence and close the most significant gap in the paper.
2. **Compare the LFQ tokenizer to at least one protein-specific discrete structure representation** (e.g., FoldToken, or a FoldSeek-based encoding) on reconstruction metrics. This would strengthen the claim that LFQ is a good choice for multimodal protein LMs.
3. **Scope the representation learning claim more carefully** in the introduction to match what is actually shown ("benefit on some predictive tasks" rather than "a range"), or add experiments that more broadly demonstrate the benefit (e.g., comparing fine-tuning strategies like LoRA vs. full fine-tuning).

## Score and Decision

The paper proposes a well-motivated, technically sound approach to multimodal protein generative modeling. The core design — discrete diffusion with LFQ tokenization, warm-up from pre-trained DPLM with LoRA, separate noise schedules — is coherent and yields competitive results across multiple tasks. The main methodological gap is the unevaluated self-mixup strategy, which weakens the paper but does not invalidate its contributions (the co-generation results stand on their own, and the warm-up/LoRA strategy is independently ablated). The remaining issues are minor and addressable. On balance, this is a solid contribution that will be of interest to the community, pending the self-mixup ablation.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>