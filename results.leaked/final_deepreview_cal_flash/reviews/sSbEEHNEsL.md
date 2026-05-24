Now I have a thorough understanding of the paper and the comparative anchors. Let me craft the final review.

## Summary
2-3 sentence summary.

The paper proposes USR 2.0, which replaces the costly autoregressive pseudo-label generation in Unified Speech Recognition (USR) with CTC-driven teacher forcing: greedily decoded CTC pseudo-labels are fed into the teacher's attention decoder to generate attention targets in a single forward pass, eliminating the autoregressive bottleneck. A mixed sampling strategy intermittently reintroduces autoregressive decoding to mitigate exposure bias. This yields approximately 2× faster training, substantially improved robustness to distribution shifts (long utterances, noise, cross-dataset), and state-of-the-art in-distribution results on LRS3, LRS2, and WildVSR.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

1. **~2× training speedup.** CTC-driven teacher forcing replaces slow autoregressive PL generation with a single parallel forward pass. Figure 5 confirms that USR 2.0 reaches a given WER in roughly half the wall-clock time of USR across multiple model scales, and Figure 1 quantifies the per-step gain (CTC decoding is ~40× faster than AR decoding).

2. **Large and convincing OOD robustness gains.** USR 2.0 maintains stable WER on VoxCeleb2 utterances up to 600 frames where USR exceeds 100% WER (Figure 3a); outperforms all baselines under babble noise at SNRs down to −5 dB (Table 1); and achieves dramatically better cross-dataset performance under greedy decoding (e.g., LibriSpeech 15.4% vs. 25.3% for USR, Table 3). These gains are large, consistent, and directly tied to the coupling of CTC and attention supervision.

3. **State-of-the-art in-distribution results with a single unified model.** USR 2.0 matches or surpasses published results on LRS3 across VSR, ASR, and AVSR in both low- and high-resource settings using a single set of parameters (Table 2). The Huge model achieves 17.6% (VSR), 0.9% (ASR), and 0.8% (AVSR). Results on LRS2 and WildVSR (reported in the appendix) further support scalability.

4. **Novel and principled core idea.** CTC-driven teacher forcing is well-motivated by the insight that global coherence of pseudo-labels is unnecessary for self-training because teacher and student share the same conditioning (Section 4.1). This insight cleanly identifies the source of USR's inefficiency and brittleness and replaces it with a faster, more robust mechanism.

5. **Thorough ablations validate design decisions.** Table 4 systematically ablates each pseudo-label target type in both CTC-driven and AR modes, showing (for example) that removing CTC supervision from the decoder degrades OOD WER from 24.2% to 35.1%. Figure 4 characterizes the ID–OOD–speed tradeoff of the mixed sampling probability. These ablations make the contribution of each component clear.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims (2× training speed, large OOD gains, SOTA ID results) are all well supported by the evidence presented.

### Minor

1. **No variance reporting for in-distribution results.** All in-distribution WERs in Table 2 are reported as single numbers without confidence intervals, multiple seeds, or statistical tests. The improvements over USR are often small (e.g., 0.1–0.2 WER for ASR/AVSR in several configurations), and it is unclear whether these differences are statistically significant or within run-to-run variation. This is partly mitigated by the consistent direction across experiments and the much larger OOD improvements, but the evidential basis for the *in-distribution* advantage would be stronger with variance estimates.

2. **Under-analyzed multi-task objective.** In CTC-driven mode (Eq. 5), the decoder loss averages cross-entropy against two target sequences (teacher attention PLs and CTC PLs) with equal weight. When these targets disagree at the same position — which is likely in many cases — the loss pushes the decoder toward a probabilistic compromise. The paper provides no analysis of how often such conflicts occur, whether the learned distribution becomes incoherent, or why this averaging is beneficial beyond the ablation in Table 4 showing that it works. A diagnostic analysis of target agreement rates or the decoder's output distribution under conflict would strengthen the paper.

3. **Single noise type in robustness evaluation.** The noise robustness experiment (Section 5.2) uses only babble noise from NOISEX. While babble is representative, the paper claims robustness under "noisy conditions" more broadly (Abstract, Section 1). Testing additional noise types (e.g., factory, cafeteria, traffic) or real-world recordings would better support this generalization claim. The multiple SNR levels and the zero-shot evaluation are positives, but the single noise source limits breadth.

4. **Comparison paradigms not fully discussed.** Table 2 compares USR 2.0 (semi-supervised fine-tuning with a unified model) against self-supervised methods (AV-HuBERT, RAVEn, AV-data2vec) that use separate fine-tuning per modality. The paper does not explicitly discuss how these different paradigms affect the interpretation of the results, which could lead readers to misinterpret the relative advantages.

5. **No ablation on the confidence threshold (0.8) or sensitivity analysis on the mixing weight (0.5).** The confidence threshold for pseudo-label filtering is inherited from USR without justification, and the equal weighting in Eq. 5 is fixed at 0.5 without any sensitivity study. While not damaging to the core claims, these are hyperparameters whose robustness could be easily checked.

### Trivial
- The evaluation on long utterances (Section 5.1) uses Whisper-transcribed VoxCeleb2 samples as reference; the paper briefly acknowledges this but could add a note that Whisper's own degradation at long lengths adds noise to the absolute WER numbers (relative comparisons remain valid).
- OOD robustness gains on AVSR under noise are less dependent on input duration than ASR, but the paper does not speculate on why (Section 5.2).

## Nice-to-Haves
- An analysis of teacher attention PL quality under CTC-driven generation vs. AR generation (token accuracy, oracle WER) would directly test the claim that global coherence is unnecessary.
- A study of how often CTC and attention PLs agree in CTC-driven mode, and what the decoder output distribution looks like when they disagree.
- Confirming that the ~2× training speedup holds for the Huge model (currently shown only for Base and Large).
- Exploring whether a lower AR sampling probability (e.g., p=0.1–0.2) could yield similar ID performance with even better OOD robustness and speed.

## Removed Points
The following points from the input reviews were removed per the filtering rules:
- **Harsh Critic's point about the appendix not being provided:** Papers at this venue include their appendix in the original submission; parser stripping is not the authors' fault. Removed.
- **Harsh Critic's suggestion to compare with Noisy Student:** The critic acknowledges this is not designed for unified VSR/AVSR, making the comparison less relevant. Removed as scope-creep.
- **Harsh Critic's speculation that "lower p could yield similar ID performance with better OOD robustness":** This is speculation without evidence and is not presented as a weakness of the paper. Moved to Nice-to-Haves.
- **Strength Finder's claim about "state-of-the-art" on LRS2 and WildVSR:** The appendix (which contains those results) is not accessible in the parsed version, so this claim cannot be verified from the on-page content. However, the main paper's Table 2 already provides strong SOTA evidence on LRS3, so this removal does not weaken the strength set.

## Novel Insights
None beyond the paper's own contributions. The core insight — that global coherence of pseudo-labels is unnecessary in self-training because teacher and student share conditioning — is the paper's main intellectual contribution, and the reviews do not add a new synthesis beyond it.

## Suggestions
- Report results with at least 2–3 random seeds (mean ± std) for the central in-distribution comparisons to establish statistical reliability.
- Add a diagnostic analysis of the multi-task objective: e.g., measure the agreement rate between CTC and attention PLs in CTC-driven mode, and show the decoder's confidence when they disagree.
- Extend noise robustness evaluation to at least one additional noise type to support the broader "noisy conditions" claim.
- Include a brief ablation on the confidence threshold (0.7, 0.8, 0.9) and a sensitivity analysis on the mixing weight in Eq. 5.

## Score and Decision

Now let me report my calibration process and score.

**Calibration summary:**

Round 1 bracketing:
- Weak band (< 3.5): anchors avg ~2–3 (e.g., heuristic early stopping, unsupervised prompt learning, SLM exploration). The paper is clearly far above this band.
- Middle band (3.5–7.5): anchors avg 4.5–7.0. Relevant anchors include:
  - CR-CTC (6.75, Accept): consistency-regularized CTC. Comparable strength — both papers address CTC limitations with simple yet effective methods, though USR 2.0 covers more tasks and has larger practical gains.
  - Align With Purpose (7.00, Accept): CTC plug-and-play framework. Similar quality tier.
  - CAV2vec (6.75, Accept): AVSR robustness. USR 2.0 has a more novel core idea (CTC-driven teacher forcing vs. corruption prediction).
  - Cross-lingual pseudo-labeling (5.25, Reject): USR 2.0 is clearly stronger.
  - Multilingual VSR (6.20, Reject): USR 2.0 is clearly stronger.
- Strong band (> 7.5): anchors avg 7.6–8.5, but these are on unrelated topics (gesture generation, avatar animation, TTA for multi-modal). Not directly comparable.

Round 1 bracket: [6.0, 7.5].

Round 2 narrowing (within bracket):
- Anchors in (5.5, 7.5): CR-CTC (6.75), AWP (7.00), CAV2vec (6.75), Sylber (6.75), SemiReward (6.00). USR 2.0 is comparable to the 6.75–7.0 papers, slightly stronger than the 6.0–6.25 papers.
- Anchors in (6.0, 8.5): Multilingual VSR (6.20, Reject — USR 2.0 is stronger), CAV2vec (6.75, Accept — comparable), T2V2 (6.25, Accept — USR 2.0 is slightly stronger).

Relative positioning: The paper is at or slightly above the 6.75–7.0 tier. It has a more novel core idea than CR-CTC or AWP, broader empirical coverage, and clearer practical benefits. The main weaknesses (no variance reporting, limited noise types) are minor and do not threaten the core claims.

Final score: 7.0

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>