Now I have all the information I need. Let me synthesize the final review.

---

## Summary

SpikeBERT adapts the Spikformer architecture (originally designed for vision) for language tasks by replacing vision-oriented modules with language-compatible ones and proposes a two-stage knowledge distillation method (pre-training feature alignment + task-specific distillation) to train a deep 12-layer spiking Transformer. On 6 text classification benchmarks (4 English, 2 Chinese), SpikeBERT outperforms SNN-TextCNN and a directly-trained Spikformer baseline by ~3-5% while consuming roughly 27% of the theoretical inference energy of fine-tuned BERT.

## Strengths

- **First deep Transformer-based SNN for language with a principled training strategy.** Unlike prior SNN language models that use shallow architectures (e.g., TextCNN-based), SpikeBERT introduces a 12-layer spiking Transformer for text. The key challenge — training deep SNNs without gradient collapse — is addressed via a two-stage knowledge distillation from BERT, and the ablation (Table 3) confirms that both stages are necessary (~3.2% drop when either stage is removed). This cleanly demonstrates the viability of the approach.

- **Targeted architectural adaptations from vision to language.** The paper makes three motivated changes to Spikformer: replacing SPS with word embeddings, reshaping self-attention from D×D to N×N (token-level), and substituting convolution+BN with linear+LN (Section 3.2, Figure 1). These are simple but correct for the modality shift and enable the architecture to process discrete text inputs.

- **Clear energy efficiency analysis.** Following standard SNN methodology (45nm technology, 4.6 pJ per AC op vs 0.9 pJ per spike), the paper reports theoretical inference energy showing SpikeBERT uses ~27% of BERT's energy. The energy comparison is transparently scoped to inference (Table 2 caption, Section 4.3) and uses the established SNN energy estimation framework. Per-dataset breakdowns allow the reader to verify the computations.

- **Ablation study isolating each loss component.** The ablation goes beyond just stage-level analysis and dissects the contribution of data augmentation, feature alignment loss, embedding loss, logits loss, and cross-entropy loss individually (Table 3). This is more thorough than many SNN papers.

## Weaknesses

### Fatal
None.

### Major

- **Insufficient SNN baselines to support the "state-of-the-art SNNs" claim.** The paper compares SpikeBERT only to SNN-TextCNN (2023) and a directly-trained version of its own architecture. The claim "outperform state-of-the-art SNNs" (abstract, line 7, line 332, conclusion) requires comparisons to a broader set of contemporary SNN language models. While SpikeGPT (Zhu et al., 2023) targets generation rather than classification, there exist other SNN approaches for text processing cited in the paper (Plank2021ALS, lv2023spiking) that are not fully explored as baselines. With only two SNN baselines, the SOTA claim cannot be verified. The paper should either add more SNN baselines or temper the claim to "outperform existing SNN approaches on text classification benchmarks."

- **"Comparable results to BERT" overstates the 4.13% gap.** The abstract and conclusion claim SpikeBERT achieves "comparable results to BERTs," but the average accuracy gap is 4.13% (80.20% vs 84.33%). While this is strong for an SNN, "comparable" is misleading — BERT consistently outperforms SpikeBERT on all 6 datasets by non-trivial margins (e.g., 7.3% on SST-5, 4.5% on ChnSenti). The language should acknowledge the gap honestly.

### Minor

- **No comparison to simpler single-stage knowledge distillation.** The core contribution is a two-stage distillation method, yet the paper never compares to a standard single-stage KD baseline (e.g., logits-only distillation from fine-tuned BERT without pre-training or feature alignment). The ablation shows both stages help, but a head-to-head against a simpler KD approach is needed to justify the complexity of the two-stage design. This is the most important missing control experiment.

- **Claim that direct MLM/NSP training fails is stated without empirical support.** The paper asserts (line 179) that directly training with MLM and NSP objectives failed to converge due to "self-accumulating dynamics," but provides no loss curves, gradient norms, or any empirical evidence. Since this failure motivates the entire distillation approach, supporting evidence should be shown (even in an appendix).

- **Overclaiming novelty as "among the first."** The paper states it is "among the first to show the feasibility of transferring the knowledge of BERT-like large language models to spiking-based architectures" (line 68). However, it itself cites SNN knowledge distillation works (Kushawaha 2020, Takuya 2021, Qiu 2023) and several SNN language works. The incremental contribution over these — applying it to a deep spiking Transformer for language with a two-stage recipe — is real but the framing oversells the gap.

- **Ablation study (Table 3) reports no variance.** Despite running 10 seeds for the main results (Table 1), the ablation study reports single numbers without standard deviations. Since several ablation drops are small (e.g., w/o DA: -0.76, w/o L_ce: -0.17), it is unclear whether these differences are meaningful relative to run-to-run variance.

### Trivial
None.

## Nice-to-Haves

- **Training energy discussion.** The paper's energy argument is explicitly for inference, which is standard practice. However, since the two-stage distillation is computationally expensive (pre-training on large corpora, 4 GPUs per stage), acknowledging the training cost and discussing the amortized efficiency trade-off would strengthen the energy narrative.

- **Evaluation on longer-form or more complex tasks.** The current evaluation is limited to short-text classification (sentence-level, ≤256 tokens). Extending to sequence labeling, NER, or QA would test generalization.

- **Visualization of feature alignment.** Showing t-SNE plots of aligned hidden features from Stage 1 would provide intuitive evidence that the spike-based representations successfully mimic BERT's.

## Removed Points

- *"Several comparisons show overlapping standard deviations"* — Factually incorrect. Checking the actual numbers (Table 1): Subj 93.00±0.33 vs 91.80±0.29 gives ranges [92.67,93.33] vs [91.51,92.09]; ChnSenti 86.36±0.28 vs 85.45±0.29 gives [86.08,86.64] vs [85.16,85.74]. No overlap at 1σ. Removed per Hard Rules (factually wrong).

- *"L_ce drop of 0.17 undermines the need for task-specific distillation's full loss formulation"* — This is a strawman. The ablation is designed to show the contribution of each component; finding that one component has a small individual contribution does not "undermine" the method — it is normal in ablation studies. The large drops from L_logits (-3.03) and L_fea (-1.90) make the case for the method's design. Removed per Hard Rules (strawman).

- *"Deeper models not improving is at odds with motivation for deep architecture"* — The paper explicitly discusses this limitation (lines 465-468), citing prior work showing that deeper SNNs do not always improve performance. The paper is honestly reporting its findings, not claiming deeper is always better. Removed per Hard Rules (misunderstands paper content).

- *"Energy comparison fundamentally misleading by omission"* — The paper clearly states it measures "energy consumption per sample during inference" (Table 2 caption, Section 4.3: "An essential advantage of SNNs is the low consumption of energy during inference"). The SOP > FLOP point is standard: energy per operation differs (4.6 pJ vs 0.9 pJ), which is the entire basis of SNN energy claims. The paper follows standard SNN energy estimation methodology transparently. Weakened to a nice-to-have (training energy discussion).

- *Various generic strength finder strengths* — Some strengths from the Strength Finder were generic or overlapped with points already covered. Filtered.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the gap between the paper's claims and the evidence, but do not reveal new scientific insights about the method itself.

## Suggestions

1. **Add at least one more SNN baseline.** Even if SpikeGPT is not directly comparable for classification, include a baseline like an SNN-MLP or an adapted version of prior SNN language work to strengthen the comparison.

2. **Add a single-stage KD baseline.** Train SpikeBERT using only logits distillation from fine-tuned BERT (no Stage 1 pre-training) to isolate the benefit of the two-stage design. This is the single most important missing experiment.

3. **Temper the claims.** Replace "outperform state-of-the-art SNNs" with "outperform existing SNN text classification models" and replace "comparable results to BERT" with "competitive results with BERT" or explicitly quantify the gap.

4. **Show loss curves or gradient norms for the direct training failure claim** to support the motivation for distillation.

5. **Add standard deviations to Table 3** to allow the reader to assess whether small ablation differences are meaningful.

## Score and Decision

**Overall assessment:** The paper tackles a worthwhile goal (energy-efficient SNN language models) and presents a clean, well-ablated method. The two-stage distillation is clearly described and the ablation convincingly shows that both stages matter. However, the evaluation is too narrow to support the strongest claims: only two SNN baselines, no comparison to simpler distillation alternatives, and the "comparable to BERT" framing overstates the 4.13% gap. The paper has genuine contributions but needs broader baselines and more measured claims to merit acceptance. As submitted, the contribution is real but the framing significantly overreaches the evidence.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>