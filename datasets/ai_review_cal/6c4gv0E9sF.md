- Decision: Reject
- Avg Score: 6.33
- Scores: 8, 8, 3
I have thoroughly read the paper and verified all reviewer claims against the actual content. Here is my consolidated review.

---

## Summary

This paper adapts the Spikformer (a spiking Transformer) for language tasks by modifying its attention mechanism from dimension-level to token-level and replacing vision-specific modules with language-appropriate ones. It proposes a two-stage knowledge distillation method from BERT (pre-training distillation on unlabeled text + task-specific distillation on labeled data) to train the resulting SpikeBERT. Experiments on six English and Chinese text classification datasets show SpikeBERT improves ~3.5% over prior SNN baselines, uses ~27.8% of BERT's inference energy, and narrows the gap to BERT to ~4.13%.

## Strengths

1. **Significant improvement over existing SNN text classifiers**: Table 1 shows SpikeBERT outperforms SNN-TextCNN and directly-trained Spikformer on all six datasets (e.g., MR: 80.69 vs 75.45/76.38; SST-2: 85.39 vs 80.91/81.55; average: 80.20 vs 76.71/77.36). This is direct evidence that the method substantially narrows the gap between SNNs and BERT.

2. **Large energy savings with modest accuracy loss**: Table 2 quantifies that SpikeBERT uses only ~27.82% of BERT's inference energy on average (e.g., MR: 28.03 mJ vs 102.24 mJ) while losing 4.13% accuracy. This supports the central claim of achieving competitive performance with much less energy.

3. **Two-stage distillation is critical**: The ablation study (Table 3) shows removing either stage 1 or stage 2 causes a ~3.2% average accuracy drop (from 76.30 to ~73.1), demonstrating both stages contribute meaningfully. Logits loss is the most important single component in stage 2.

4. **Non-trivial architectural adaptation for language**: Section 3.2 details specific modifications — switching SSA attention from D×D to N×N (token-level interrelation), replacing convolutions+BN with linear layers+layer normalization, and replacing SPS with word embedding — that adapt Spikformer from vision to text. These are concrete changes validated by experiments.

5. **Thorough hyperparameter analysis**: Figure 5 provides systematic experiments varying time steps (optimal T=4), model depth (deeper not always better), and decay rate (β=0.9 near-optimal) across multiple datasets, providing practical guidance for SNN deployment.

6. **Cross-lingual validation**: Consistent improvements on both English (MR, SST-2, Subj, SST-5) and Chinese (ChnSenti, Waimai) datasets demonstrate language-agnostic applicability.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaimed "state-of-the-art SNN" status.** The paper claims to "outperform state-of-the-art SNNs" (abstract, conclusion) but compares to only one prior external SNN (SNN-TextCNN from lv2023spiking) plus a self-constructed baseline (Directly-trained Spikformer). Other SNN language models are cited in the introduction — SpikeGPT (zhu2023spikegpt) and Plank et al. (2021) — but are not discussed in comparison. Even if those models target different tasks/architectures, the paper should qualify the scope of its SOTA claim (e.g., "Transformer-based SNNs for text classification") or explicitly explain why direct comparison is infeasible. *Evidential basis: The abstract states "outperform state-of-the-art SNNs," yet Table 1 contains only two SNN baselines, one of which is self-constructed. The claim is broader than the evidence supports.*

2. **Overstated "comparable results to BERT."** The paper repeatedly describes SpikeBERT's results as "comparable" to BERT. The average accuracy gap is 4.13% (80.20% vs 84.33%), ranging from 0.6% (Waimai) to 6.94% (MR). A 4+ point gap across six benchmarks is meaningful, not negligible. Only one of six datasets is within one point. "Competitive" or "approaching BERT performance" would be more accurate descriptors. *Evidential basis: Table 1 shows the gap; the paper's text (line 334, 476, abstract) calls this "comparable" and a "small drop." This framing misrepresents the magnitude of the difference.*

### Minor

1. **Missing Stage 1 training duration.** Section 4.2 gives batch size (128), learning rate (5e−4), optimizer (AdamW), and loss weights for Stage 1 pre-training, but does not specify the number of training steps or epochs. Given the large unlabeled corpus (Wikipedia + BookCorpus), this detail is needed for reproducibility and for understanding whether pre-training was run to convergence. *Evidential basis: Section 4.2 lists Stage 1 hyperparameters but omits training steps/epochs.*

2. **Vague "ignored front layers" heuristic in feature alignment.** Section 3.3.1 states "we choose to ignore some front layers when calculating feature alignment loss" because early layers are hard to align. The paper does not specify how many front layers are skipped or the precise decision rule. While the ⌈B/M⌉ formula handles mapping layers between differently-sized teacher/student, the "ignored front layers" decision remains unspecified. *Evidential basis: Lines 217-219 explicitly reference ignoring front layers but provide no criterion for how many.*

3. **No evidence for direct training failure claim.** The paper states that Directly-trained Spikformer fails to converge due to gradient vanishing/exploding (lines 336-338), but provides no loss curves, gradient norm analysis, or training trajectories. The accuracy gap in Table 1 is consistent with this explanation but does not directly evidence the claimed mechanism. *Evidential basis: Lines 336-338 state the convergence claim with a citation to Fang2020 but show no training curves from the authors' own experiments.*

### Trivial
None.

## Nice-to-Haves
- An acknowledgment of the training computational cost (the energy analysis covers inference only; training requires running a BERT teacher on a large corpus with 4 A100 GPUs).
- Qualitative error analysis comparing SpikeBERT and BERT predictions (e.g., does SpikeBERT struggle more on long sentences, rare words, or ambiguous sentiment?).
- An ablation on which specific front layers are skipped in feature alignment and how this choice affects accuracy.
- Training loss/accuracy curves comparing SpikeBERT and Directly-trained Spikformer to substantiate the convergence claim.

## Removed Points

These points were raised by reviewers but are removed after verification:

1. **"Data augmentation may corrupt labels"** (Harsh Critic Critical Issue #4): REMOVED. The paper follows Tang2019DistillingTK, a standard data augmentation strategy in knowledge distillation. In KD with soft labels, the teacher's prediction on augmented inputs naturally adapts — this is by design, not a flaw. The critique misunderstands a well-established practice.

2. **"No discussion of temporal information loss from averaging spike trains"** (Harsh Critic's section notes on 3.3): REMOVED. The paper explicitly describes summing over the time dimension followed by MLP+LayerNorm (Equation 5). This is a deliberate design choice for aligning ANN and SNN feature spaces, not an oversight. The paper is not claiming to model temporal patterns.

3. **"Missing related works"**: REMOVED per instructions — I cannot confirm the existence of missing related works without external sources.

4. **General speculation from harsh critic's area sweeps** (e.g., "could the metric be measuring a proxy?"): REMOVED as these lack specific anchors in the paper's content.

## Novel Insights

None beyond the paper's own contributions. The review process surfaces no new perspective not already present in the paper.

## Suggestions

1. **Recalibrate claims.** Replace "outperform state-of-the-art SNNs" with a scoped claim such as "outperform existing SNN text classification models" (or explicitly specify the scope: Transformer-based SNNs for text classification). Replace "comparable results to BERT" with "competitive" or "approaching BERT performance," and discuss per-dataset gaps (e.g., within 0.6% on Waimai vs 6.9% on MR) to give a nuanced picture.

2. **Add Stage 1 training details.** Specify the number of training steps or epochs for pre-training distillation, and explicitly state the rule for which front layers are ignored in feature alignment.

3. **Add training loss/accuracy curves** for SpikeBERT vs. Directly-trained Spikformer to substantiate the convergence failure claim.
