Now I have sufficient calibration data. Let me write the final review.

## Summary

This paper introduces DelRec, the first surrogate gradient learning (SGL) method to train delays in recurrent connections of spiking neural networks. The approach extends differentiable triangular interpolation (from DCLS) to recurrent connections with a scheduling buffer and pointer mechanism. On the SSC audio dataset, DelRec achieves 82.58% (SOTA) using only recurrent delays with simple LIF neurons and 0.37M parameters, and on PS-MNIST it achieves 96.21% (SOTA). A functional study on the SHD dataset demonstrates that learned recurrent delays significantly outperform vanilla RSNNs (~82% vs. ~40%) and also outperform learned feedforward delays in low-parameter regimes.

## Strengths

- **New SOTA on SSC with simple LIF neurons and far fewer parameters**: Table 1 shows DelRec (only recurrent delays, 0.37M params) achieves 82.58% on SSC, surpassing prior SOTA DCLS (80.69%, 2.5M params) and SiLIF (82.03%, 0.35M params). This is notable because the competing methods use more complex neuron models (adaptive, state-space), while DelRec uses the simplest LIF neuron.

- **First SGL-based method for training delays in recurrent spiking layers**: The paper provides a clearly described method (Section 2.2, Eqs. 9–11) for extending delay learning from feedforward to recurrent connections, including a differentiable triangular interpolation with progressive σ annealing and a scheduling buffer with pointer mechanism. This is a genuine algorithmic contribution.

- **Functional study provides clear evidence for the role of recurrent delays**: Figure 3B on SHD (10k parameter models) shows learned recurrent delays achieve ~82% accuracy versus ~40% for a vanilla RSNN and ~78% for fixed random recurrent delays. Figure 3C further shows recurrent delays degrade less steeply as parameter count decreases. This directly supports the paper's core claim on a controlled setting.

- **Competitive SHD results with rigorous methodology**: Table 2 shows DelRec achieves 93.73% on SHD (matching SE-adLIF SOTA) while using LIF neurons and a proper train/validation/test split (20% of training set as validation). The paper also responsibly notes that SHD is saturated and recommends it only for validation.

## Weaknesses

### Fatal
None.

### Major

- **No controlled ablation on the primary benchmark (SSC)**: The paper's central claim is that learning *recurrent delays* improves performance, yet on SSC—the largest and hardest dataset where SOTA is claimed—there is no baseline: a vanilla RSNN (same architecture, same training protocol, no trainable delays). Table 1 includes models with complex neurons (SE-adLIF at 80.44%, SiLIF at 82.03%) but no LIF-based RSNN without delay learning. The functional study on SHD provides supporting evidence, but SHD uses much smaller models (10k params, 30 epochs, no augmentations) and is qualitatively different from the SSC setting where SOTA is claimed. The reader cannot determine how much of the 82.58% comes from the learned delays versus simply having a well-tuned recurrent architecture.

### Minor

- **Unexplained reversal: combined delays underperform recurrent-only on SSC**: In Table 1, DelRec with *both* recurrent and feedforward delays (0.55M params) achieves 82.19±0.16%, while DelRec with *only* recurrent delays (0.37M params) achieves 82.58±0.08%—a reversal exceeding the reported standard deviations. The paper does not discuss this. If the combination degrades performance, this warrants explanation, especially since the abstract presents the combination as a contribution. The conclusion notes "further improvements could be obtained by better combining DelRec with feedforward delays," but the results section itself is silent on this anomaly.

- **PS-MNIST SOTA claim rests on a single seed**: The paper reports 96.21% on PS-MNIST from one run, with the justification "we only test one seed as all the previous state-of-the-art models on the dataset." While this follows prior practice, the improvement over ASRC-SNN (95.77%) is only 0.44%, and without variance estimates it is impossible to assess statistical significance. This weakens the SOTA claim on this benchmark.

- **Delay type confounded with connectivity type in the comparison**: The functional study (Section 3.2) compares *synaptic* feedforward delays (one per synapse) with *axonal* recurrent delays (one per neuron). The paper acknowledges this difference in one sentence but then draws conclusions like "recurrent delays achieve better performance than feedforward delays for an equivalent number of parameters." The confound between delay type and connectivity type means the observed advantage cannot be cleanly attributed to one factor. A cleaner comparison would require holding delay type constant while varying connectivity.

### Trivial

- **σ annealing schedule is not specified**: The paper states sigma is decreased "throughout training down to 0" but does not provide the schedule (e.g., cosine, exponential, linear). The DCLS paper this builds on uses a specific schedule, and the choice is a free hyperparameter that affects convergence.

## Nice-to-Haves

- Report the σ annealing schedule used for each dataset.
- Provide computational cost / memory footprint analysis, especially given the scheduling buffer dimension scales with max delay + σ.
- For the combined delays underperformance on SSC, a brief hyperparameter search discussion would clarify whether the "Rec + Ff" variant was tuned comparably.

## Removed Points

The following points from the reviewers are removed with justification:

1. **Criticism about missing appendix, missing algorithm pseudocode, missing references**: The parser strips these sections. They exist in the original submission; the review should not penalize the paper for parser artifacts.

2. **Generic speculation about confounders ("could the metric be measuring a proxy?", "are confounders controlled?")** without specific evidence from the paper text: Removed as speculative noise.

3. **The harsh critic's framing of the missing baseline as "fatal"**: The paper does provide evidence on SHD (Fig 3B) that isolates the effect of delays. While the SSC missing baseline is a real weakness, the SHD evidence prevents this from being fatal. Downgraded to Major.

4. **Strength Finder's generic/superficial strengths** (e.g., "the paper addresses an important problem"): Removed as not concrete enough.

5. **Criticism about unreleased code or inability to verify results**: The paper provides a code URL. Per protocol, cited entities are assumed to exist.

## Novel Insights

None beyond the paper's own contributions. The reviews converge on the same core observation: the method is novel and well-motivated, but the evaluation on the primary benchmark lacks a clean ablation that would directly attribute the gains to learned recurrent delays. The interaction of feedforward and recurrent delay learning also needs clarification.

## Suggestions

1. **Add a vanilla RSNN baseline on SSC** with the same architecture and training protocol but no trainable delays. This single addition would directly quantify the benefit of the paper's core contribution and substantially strengthen the paper.

2. **Run 3–5 seeds on PS-MNIST** and report mean ± std. The current single-run result is not credible for a SOTA claim.

3. **Discuss the recurrent-only vs. combined reversal on SSC** explicitly. This could be addressed by tuning the combined variant more carefully or acknowledging the interaction.

4. **Disentangle the delay-type confound**: Either compare delays of the same type (e.g., synaptic recurrent delays), or clearly frame the comparison as "axonal recurrent" vs. "synaptic feedforward" rather than making general statements about delay types.

## Score and Decision

**Round 1 — Bracketing**: I initially searched three bands around delay learning in SNNs. Weak band (≤3.5, avg 1.5–3.0): clear reject papers with fundamental flaws. Middle band (3.5–7.5, avg 4.0–5.75): reject-level SNN papers with significant issues (DeNN at 4.50, FGT at 5.00, Layer Synchronization at 5.75). Strong band (≥7.5, avg 8.0–9.0): accept-level papers with broader impact and cleaner evaluations. This paper is clearly above the weak band and sits within the middle-to-strong transition.

**Round 2 — Narrowing**: I searched for papers inside (4.5, 6.5) and (5.5, 7.5) on delay-specific and recurrent-SNN topics. Key anchors:

- **DeNN** (4.50, Reject): Delay-based SNN with major clarity issues and no SOTA. DelRec is substantially stronger in method clarity, evaluation, and results.
- **Spatio-Temporal Dependency-Aware Neuron Optimization** (5.75, Reject): Proposes neuron optimization but lacks SOTA results. DelRec is comparable or slightly stronger.
- **TS-LIF** (6.00, Accept): Dual-compartment spike neuron for time series. Accepted despite missing controls and biological plausibility concerns. DelRec has comparable evaluation gaps but clearer novelty (first SGL recurrent delay method) and stronger SOTA claims.
- **Temporal Flexibility in SNNs** (6.20, Accept): Training method for time-step generalization. Accepted despite unclear motivation-evidence connection. DelRec is similar in overall quality.

Compared against these anchors, DelRec is clearly stronger than DeNN (4.50) and the FGT paper (5.00). It is comparable to TS-LIF (6.00) and the Temporal Flexibility paper (6.20). The paper's genuine novelty (first SGL recurrent delay method) and SOTA results on two benchmarks are offset by the verified evaluation gaps (missing SSC baseline, single-seed PS-MNIST, unexplained reversal). I place it near the lower end of the accept band.

**Final Score**: 6.0 — a solid contribution with a well-described method and strong SOTA results, but the evaluation contains material gaps (particularly the missing controlled ablation on SSC and single-seed PS-MNIST) that prevent it from being a clearly strong paper. With the suggested additions (vanilla RSNN baseline on SSC, multi-seed PS-MNIST), it would become significantly stronger.

**Calibration Anchors**:

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fnO5h1CFyh.md` | 3.00 | R1 | Unrelated topic (Hebbian temporal memory). Much weaker. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/SI6zocV2SS.md` | 1.50 | R1 | Continual learning. Much weaker. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7eYmijcuqO.md` | 3.00 | R1 | RNN dynamics. Much weaker. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NPzuN3Rxi8.md` | 3.00 | R1 | Graph RNN for neuroscience. Much weaker. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pIJR9uPjy3.md` | 4.50 | R1 | Delay neural networks (DeNN) — most topically similar. Had major clarity issues and no SOTA. DelRec is substantially stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6iM7mmVhXh.md` | 5.75 | R1 | Layer synchronization in SNNs. Well-motivated but mixed evaluation. DelRec is comparable or slightly stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/yBP36xQhZl.md` | 5.00 | R1 | Forward gradient SNN training. Limited by novelty concerns. DelRec is stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vq75kRCYuY.md` | 4.00 | R1 | Online SNN training. Weaker method and results. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/nwDRD4AMoN.md` | 9.00 | R1 | Kuramoto oscillatory neurons. Much broader impact, far stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/RWJX5F5I9g.md` | 8.00 | R1 | RL + neuroscience. Much stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/agPpmEgf8C.md` | 8.00 | R1 | RL auxiliary objectives. Much stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Xo0Q1N7CGk.md` | 8.00 | R1 | Grid cells. Much stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Nz2UApmv2e.md` | 5.00 | R2 | SNN audio localization. Weaker evaluation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/eN4g4cjFX1.md` | 5.75 | R2 | Neuron optimization. Comparable weakness level, DelRec has stronger SOTA claims. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/JAnyCnK5In.md` | 4.75 | R2 | Online SNN training. Weaker. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/rDe9yQQYKt.md` | 6.00 | R2 | TS-LIF. Accepted with comparable weaknesses (missing controls, biological plausibility). DelRec is similarly positioned. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xwKt6bUkXj.md` | 6.75 | R2 | RNN mechanisms. Cleaner evaluation. Stronger than DelRec. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9HsfTgflT7.md` | 6.20 | R2 | Temporal flexibility. Accepted despite motivation-evidence gap. DelRec is comparable. |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>