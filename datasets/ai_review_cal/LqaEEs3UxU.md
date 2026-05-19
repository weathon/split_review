- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper proposes Sign2GPT, a gloss-free sign language translation framework that uses frozen pretrained vision (DinoV2) and language (XGLM 1.7B) models connected via lightweight adapters (LoRA and zero-gated cross-attention). A novel pretraining stage (PGP) automatically extracts pseudo-glosses from spoken-language sentences via lemmatization and POS filtering, then trains the sign encoder with a prototype-based binary cross-entropy loss to recognize whether each pseudo-gloss is present in the sign video. Experiments on Phoenix14T and CSL-Daily show improvements over prior gloss-free methods.

## Strengths

1. **Novel pseudo-gloss pretraining (PGP) eliminates the need for manual gloss annotation.** The method extracts pseudo-glosses automatically from text using spaCy (lemmatization/POS filtering), then aligns sign representations to these pseudo-glosses via a prototype-based objective (Section 3.3, Figure 3). This is a creative and practical way to inject linguistic knowledge without costly manual annotation. The within-method ablation (w/ PGP vs w/o PGP) shows clear gains: +1.3 BLEU-4 on Phoenix14T test and +3.5 on CSL-Daily (Tables 2, 3), confirming that the pretraining itself drives meaningful improvement beyond the architecture.

2. **Frozen large models + lightweight adapters achieve strong results with few trainable parameters.** The paper freezes DinoV2 and XGLM 1.7B, using LoRA and zero-gated cross-attention (initialized to zero) so that linguistic knowledge is preserved. Only ~3.8M parameters are trainable in the decoder (Table 1b), and the bulk of trainable capacity is concentrated in the sign encoder. This is a principled design for small SLT datasets where full fine-tuning would cause overfitting.

3. **Consistent improvements over prior gloss-free methods on two benchmarks.** Sign2GPT w/PGP achieves 21.9 BLEU-4 on Phoenix14T test (vs 20.0 for prior best gloss-free GFSLT-CSLP) and 21.0 on CSL-Daily test (vs 16.6 for GLF-SLT). Improvements are consistent across BLEU-{1,2,3} and ROUGE-L. The gap on CSL-Daily is particularly large (+4.4 BLEU-4), which is the harder dataset.

4. **Meaningful architectural ablations.** The paper ablates spatial adapters, local vs global attention, temporal downsampling, and positional embedding strategies (Table 4). These demonstrate that each design choice contributes (e.g., spatial adapters are critical, sinusoidal positional embeddings are essential after PGP). The finding that pretraining removes temporal information and must be re-introduced via sinusoidal embeddings is an interesting and non-obvious insight.

## Weaknesses

### Fatal
None.

### Major

1. **Decoder model size is a confound in the comparison against prior methods.** The paper uses XGLM 1.7B as its decoder, while prior gloss-free methods use smaller models (e.g., T5-base ~220M, mBART ~680M). The paper lacks an experiment that controls for decoder scale — e.g., replacing XGLM 1.7B with a smaller GPT-style decoder while keeping the adapter architecture and PGP fixed. Without this, it is unclear how much of the +1.1 BLEU-4 on Phoenix14T and +4.4 on CSL-Daily over prior methods is attributable to the method's specific innovations (adapter design, PGP) versus simply using a larger language model. Notably, Sign2GPT without PGP already achieves 20.6 on Phoenix14T (vs prior best 20.0), suggesting that even the baseline architecture (larger decoder + adapters) yields a small gain. The within-method PGP ablation (+1.3 on Phoenix14T, +3.5 on CSL-Daily) is clean and valuable, but the headline comparisons against prior work conflate architecture scale with method contribution. The authors should qualify these comparisons or add a controlled experiment.

2. **The prototype matrix P is underspecified: it is not stated whether P is updated (learnable) or frozen during pretraining.** Line 117 says prototypes are "initialized with word embeddings obtained from fastText" but does not state whether gradients flow through P. If P is learnable, the model could trivially minimize the BCE loss by making prototypes degenerate (all zeros or identical); if frozen, it imposes a strong inductive bias that should be discussed. This is essential for reproducibility and for understanding what the pretraining actually learns.

### Minor

1. **The qualitative analysis is essentially absent.** Section 3.5 ("Qualitative Results") consists of two sentences stating that output matrix E "holds promise for sign spotting" and "may warrant further exploration." No concrete examples, visualizations, or analysis of actual outputs are provided. Either remove the section or include genuine qualitative evaluation (e.g., examples of E matrices with their corresponding video segments, sample translations with analysis).

2. **Missing key ablations that would strengthen the evidence for design choices.** The paper does not ablate (a) the POS filter or lemmatization step in pseudo-gloss extraction, (b) the prototype-based objective against an alternative pretraining objective (e.g., video-text contrastive loss, masked autoencoding), or (c) coverage statistics (what fraction of sentences contain at least one pseudo-gloss? How many pseudo-glosses per video on average?). These would clarify what makes PGP effective versus serving as a generic pretraining signal.

3. **The BCE loss formulation on prototype presence scores is mathematically unusual and not discussed.** The aggregated score $\hat{E}_j = \sum_i E_{i,j}$ sums values bounded by [0,1] over T time steps, so $\hat{E}_j$ can exceed 1 (up to T). Standard binary cross-entropy expects inputs in [0,1] unless a sigmoid is applied internally. The paper does not specify how this is handled. In practice it may work if scores are naturally small, but the discrepancy should be acknowledged.

### Trivial

1. The "Spatial Adapter" and "Global Attention" ablation row labels in the text vs the reported baseline numbers could be more clearly distinguished to avoid confusion about which condition each corresponds to.

## Nice-to-Haves

- **Error bars or multiple-run statistics.** BLEU scores are reported as point estimates without variance. Given small dataset sizes, standard deviations across runs would improve reliability.
- **Computational cost of the pretraining stage** (GPU hours, total training time including pretraining + translation) would help readers assess practicality.
- **Failure case analysis** — a few examples of translations where the model struggles, with discussion of whether failures stem from prototype coverage, decoder hallucination, or video quality.
- **Analysis of whether the E matrix produces temporal alignments that correspond to when the pseudo-gloss is visibly signed.**

## Removed Points

- **"Ablation study is poorly structured and confusing"** (Harsh Critic) — The text clearly separates ablations conducted without pretraining (spatial adapter, attention type, downsampling) from those with pretraining (positional embeddings). The specific claim about a 15.32 vs 15.37 discrepancy cannot be verified from the paper text alone since the table is an included file. The review's substantive point about missing ablations is retained in Minor weaknesses above.

- **"Temperature values of 0.1 could produce near-hard assignments and instability"** (Harsh Critic) — The paper explicitly states τ_T and τ_U are "learnable scaling factors" (line 131) that can adjust during training, so the concern is speculative.

- **"Missing related work on frozen LLMs for SLT"** (Harsh Critic) — Removed per hard rule: I cannot verify whether cited works exist or are missing.

- **"No error bars or significance tests"** (Harsh Critic) — This is standard practice in the SLT literature; demoted to Nice-to-have.

- **"No comparison with sign-speech alignment models"** (Harsh Critic) — Scope creep; the paper focuses on translation, not alignment.

- **"No discussion of failure cases"** (Harsh Critic) — Nice-to-have, not a weakness.

- **"No computational cost discussion"** (Harsh Critic) — Nice-to-have.

- **Strength Finder's claim that the ablation study is "systematic" with "clear empirical evidence"** — While the existing ablations are useful, they are incomplete (missing key ablations noted in Minor weaknesses), so the strength is overstated. The core finding (meaningful architectural ablations exist) is retained in Strengths item 4.

## Novel Insights

The most interesting observation to emerge from the reviews is a methodological tension that the paper does not fully address: the pseudo-gloss pretraining (PGP) is designed to learn word-level sign representations, yet the downstream translation task requires sentence-level coherence. The paper shows this gap is bridged via sinusoidal positional embeddings (temporal information removed during pretraining must be re-injected), but it does not examine whether the prototype assignments genuinely correspond to visual sign occurrences or are merely functioning as a bag-of-words pretraining signal. If the latter, a simpler contrastive objective might suffice — but the paper does not test this, leaving the question open for future work. Additionally, the observation that Sign2GPT w/o PGP (20.6 BLEU-4) already matches prior SOTA (20.0) suggests that the frozen-large-decoder + adapter recipe is competitive even without the pretraining innovation, which partially recontextualizes the headline gains.

## Suggestions

1. **Add a decoder-scale control experiment.** Replace XGLM 1.7B with a smaller frozen GPT-style model (e.g., 350M parameters) while keeping the adapter architecture and PGP fixed. This would isolate the contribution of the method's specific design (adapter architecture + PGP) from decoder scale. If gains persist, it strongly validates the approach; if they shrink, the paper should acknowledge that a primary advantage is enabling larger decoders.

2. **Specify whether the prototype matrix P is learnable or frozen during pretraining** and discuss the implications for both cases. If learnable, verify that prototypes remain meaningful (e.g., by measuring their nearest fastText neighbors before and after training).

3. **Strengthen the qualitative analysis** with concrete examples: show E matrices aligned to video segments for a few cases where pseudo-glosses are present/absent, and provide sample translation outputs comparing w/ and w/o PGP.

4. **Add ablations of the POS filter** (e.g., no filter, different POS sets) and of the prototype objective against a simpler alternative (e.g., video-text contrastive loss using the same pseudo-glosses as positive pairs).

5. **Clarify the BCE loss handling** for $\hat{E}_j$ values that may exceed 1 — specify whether a sigmoid is applied before computing BCE, or whether values are clipped, or whether the scores naturally stay within [0,1] in practice.
