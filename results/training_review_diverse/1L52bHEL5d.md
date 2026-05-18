Now I have all the information I need to produce the final consolidated review. Let me organize my assessment.

## Summary

The paper introduces MiDl, the first test-time adaptation method specifically designed for missing modalities in egocentric video. It formulates missing modalities as a distribution shift and proposes minimizing mutual information between predictions and modality type (to build invariance) combined with self-distillation via KL divergence (to retain performance on complete-modality samples). Empirically, MiDl yields consistent gains (up to +11% on Epic-Kitchens, +6% on Epic-Sounds) across architectures (MBT, self-attention, Omnivore), missing-modality types, and settings (online, long-term adaptation, out-of-domain warm-up).

## Strengths

- **First formulation of missing modality as a test-time adaptation problem**: The paper redefines the missing-modality challenge as a TTA task (Sec 3.1), which is a principled shift from prior work requiring expensive retraining. The streaming evaluation protocol (Sec 3.2) provides a clean benchmark for this new framing.

- **Consistent and significant gains across diverse settings**: MiDl improves the non-adapted baseline by up to 7% in the online setting (Table 1) and up to 11.9% in the long-term adaptation setting (Table 2). Gains hold across different missing rates, architectures (MBT in Table 1, self-attention in Table 3, Omnivore in Table 5), and missing-modality types (dominant vs. non-dominant in Tables 1–4). This breadth convincingly supports the claimed architecture- and modality-agnosticism.

- **Ablation validates the design rationale**: Table 6 cleanly shows that neither the MI component nor the KL component alone suffices — their combination is necessary for consistent gains across all missing rates, directly supporting the design in Section 4.

- **Out-of-domain warm-up demonstrates practical robustness**: Section 5.4 shows that warming up on Ego4D before deployment further boosts performance (e.g., +8% on Epic-Kitchens at 100% missing rate), showing that MiDl does not require in-domain data for the warm-up phase.

## Weaknesses

### Fatal
None.

### Major

- **Limited to a single task (action recognition) with two modalities (audio + video)**: While the paper is thorough within this scope — testing across architectures, missing-modality types, and settings — the task diversity is narrow. The paper claims MiDl is "a comprehensive solution for diverse scenarios," but it has only been validated on egocentric action recognition with audio+video. Claims about generality to other tasks (e.g., moment localization, emotion recognition) or other modality combinations (e.g., video+IMU) are aspirational, not demonstrated. A more measured framing would better match the evidence.

### Minor

- **The p_AV>0 requirement for online adaptation is presented but could be foregrounded more explicitly**: The paper states the assumption that p_AV ≠ 0 (line 77) and reports p_AV=0 results in the LTA setting. However, the abstract and introduction frame the method as handling missing modalities "exclusively at test time" without mentioning that online adaptation requires at least some complete-modality samples in the test stream. If the test stream has p_AV=0, MiDl simply uses the most recently adapted model from a prior phase. This is a real practical constraint worth highlighting earlier in the paper. The method still delivers value in the LTA/p_AV=0 case via prior warm-up, but the framing could be sharper.

- **Hyperparameter values and sensitivity not reported**: The learning rate γ is introduced but its value is not given in the main text; the number of gradient steps per adaptation sample and batch size are unspecified. While these may appear in the appendix (which the parser strips), their absence from the main paper makes reproducibility harder. A brief sensitivity analysis would strengthen the paper.

- **Wall-clock latency not measured**: Section 6.5 estimates a 2× slowdown assuming full parallelization of the four forward passes, but no actual throughput or latency numbers are reported. Real hardware measurements would strengthen the practical claims, especially for online/low-latency deployments.

### Trivial
None.

## Nice-to-Haves

- A brief discussion of temporally correlated modality-missing patterns (e.g., bursts of missing-modality samples) would be a useful addition, since the current evaluation assumes an i.i.d. stream.
- The suggestion from the harsh critic about measuring the prediction gap across modality conditions (e.g., average divergence between audio-only and video-only predictions) would be a nice direct validation of the MI loss mechanism.

## Removed Points

- **"The MI loss implicitly assumes missing patterns match zeroing-out"** — This is standard practice in the missing-modality literature (e.g., Ramazanova et al. 2024, Lee et al. 2023). The paper transparently describes its zero-padding strategy and the limitation is not specific to this work. Removed as not a meaningful weakness.

- **"Evaluation should include other tasks (moment localization, emotion recognition)"** — This would require an entirely different paper with new datasets, architectures, and baselines. The paper is scoped to egocentric action recognition; demanding breadth beyond that scope is not a valid weakness. Moved here.

- **"The method requires complete-modality samples for adaptation which is under-discussed"** — The paper explicitly states the p_AV≠0 assumption on line 77 and reports p_AV=0 results. This is discussed, though could be more prominent. The substantive residue (foregrounding) is kept as a minor weakness above.

- **"The test-time adaptation claim is only true when the test stream includes complete samples"** — This restates the paper's own explicit assumption; it is not a hidden flaw. The paper is transparent about this. Kept only the framing nuance point above.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's strengths and surface minor concerns about scope breadth and assumption visibility, which are already partially addressed in the paper.

## Suggestions

1. **Foreground the p_AV>0 requirement** in the abstract and introduction — even a sentence like "Our method adapts on the fraction of test samples that contain both modalities, and continues to improve even when later samples are unimodal" would resolve the framing tension.

2. **Report hyperparameter values** (learning rate, batch size, number of adaptation steps per sample) and include a brief sensitivity analysis in the main paper or appendix.

3. **Add real wall-clock latency/throughput measurements** on relevant hardware (e.g., a single GPU) to validate the claimed 2× slowdown in practice.

4. **Tone down the generality claims** — the paper convincingly shows architecture-agnosticism and modality-agnosticism *within egocentric video action recognition with audio+visual modalities*. Phrasing like "a comprehensive solution for diverse scenarios" overreaches the evidence.

## Score and Decision

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>