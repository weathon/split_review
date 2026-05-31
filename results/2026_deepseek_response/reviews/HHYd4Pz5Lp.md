Now I have a solid calibration picture. Let me finalize the review.

## Calibration Analysis

**Round 1 (Bracketing):** Low band (< 3.5) returned papers clearly weaker (score 1.5–3.0, not SNN SOTA). Middle band (3.5–7.5) returned relevant SNN papers (SOLO 4.0, FGT 5.0, S-TLLR 5.0). High band (> 7.5) returned papers tangentially related. Initial bracket: **4.0–6.5**.

**Round 2 (Narrowing):** Queried inside (5.0–7.5) with SNN-specific terms. Key anchors:

- **DeepTAGE (6.25, Accept):** SNN gradient enhancement, SOTA on ImageNet/CIFAR. Stronger dataset scale but broader scope. DelRec is slightly below — less general and smaller gains.
- **MTT/Temporal Flexibility (6.20, Accept):** SNN training for deployment flexibility, real chip results. Comparable methodology scope, but MTT has hardware validation.
- **ST-DANO (5.75, Reject):** Neuron optimization, 5%+ improvement on DVS-CIFAR10, rejected due to insufficient comparisons. DelRec has better comparisons.
- **FGT (5.00, Reject):** Forward gradient for SNN, no SOTA. DelRec clearly stronger.
- **S-TLLR (5.00, Reject):** STDP-based SNN training, comparable to BPTT. DelRec clearly stronger.

**Final placement:** Above 5.0 (FGT, S-TLLR), comparable to ST-DANO (5.75) but with cleaner comparisons, slightly below DeepTAGE (6.25) and MTT (6.20) which have broader experimental validation. Final score: **5.5**.

## Summary
This paper introduces DelRec, a method for learning per-neuron delays in recurrent connections of spiking neural networks using surrogate gradient learning (SGL). It uses differentiable triangular interpolation with progressive σ annealing to handle non-integer delays, and a scheduling buffer with a pointer mechanism. DelRec achieves new state-of-the-art results on SSC (82.58%) and PS-MNIST (96.21%) using only vanilla LIF neurons, and provides a careful ablation study on SHD showing that learned recurrent delays, specifically, outperform learned feedforward delays under parameter constraints.

## Strengths
1. **New SOTA on two benchmarks with simpler neurons:** Table 1 shows DelRec achieves 82.58% on SSC (vs. prior best 82.03% from SiLIF) and 96.21% on PS-MNIST (vs. 95.77% from ASRC-SNN), using only vanilla LIF neurons with stateless synapses, while most competitors use more complex neuron models (adaptive mechanisms, state-space dynamics, etc.). This cleanly demonstrates that delay optimization can substitute for neuron complexity.

2. **Clean ablation isolating recurrent delay benefit:** Figure 3B provides a direct, controlled comparison at ~10k parameters: learned recurrent delays (82%) outperform learned feedforward delays (80%), fixed random recurrent delays (78%), vanilla RSNN (~40%), and vanilla SNN (~60%). Figure 3C further shows that recurrent delays degrade more gracefully than alternatives as parameter count shrinks. This is concrete evidence supporting the core thesis.

3. **Resource-efficient:** DelRec (0.37M params, only recurrent delays) outperforms SE-adLIF (1.6M params, 80.44%) and matches SiLIF (0.35M params, 82.03%) on SSC with fewer parameters, demonstrating that delay-based approaches are parameter-efficient relative to neuron-complexity approaches.

4. **Methodological clarity and soundness:** The differentiable interpolation with progressive σ annealing (Eq. 9–11, Fig. 2C) and the scheduling matrix with a pointer-based buffer are clearly described. The approach is algorithmically sound, building on established techniques (DCLS triangular spread, σ annealing) and extending them cleanly to the recurrent case.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **"First SGL-based" claim is imprecisely framed:** The paper repeatedly states DelRec is "the first SGL-based method to train axonal or synaptic delays in recurrent spiking layers" (abstract, introduction). The paper itself discusses Xu et al., who learn a per-layer recurrent delay parameter via softmax with decreasing temperature through backpropagation — a differentiable relaxation that uses surrogate gradients for the spike function. Calling DelRec the unqualified "first" is imprecise. The actual novelty — per-neuron (not per-layer) continuous delays, differentiable interpolation with σ annealing rather than softmax over a fixed set, the scheduling matrix mechanism — is still interesting and clearly a genuine contribution. But the framing should be corrected to emphasize these specific technical distinctions relative to Xu et al., rather than claiming exclusivity on SGL.

2. **Modest improvement margins without statistical rigor:** The SOTA gains are ~0.55% on SSC (82.58 vs. 82.03) and ~0.44% on PS-MNIST (96.21 vs. 95.77). On SHD (Table 2), DelRec's best score (93.73%) falls within error bars of SE-adLIF 2L (93.79%) and DCLS (93.77%). The paper reports standard deviations for SSC (3 seeds) but does not test whether the difference from SiLIF (82.03±0.25%) is statistically significant. The PS-MNIST result uses only 1 seed (following prior convention, but the paper's own SSC uses 3 seeds). These margins are consistent across tasks, which is in the paper's favor, but a significance test would strengthen the SOTA claim.

3. **Missing training cost analysis:** The scheduling matrix X^{rec} has dimension N × dim(Ẽ), where Ẽ grows with max delay and σ. Each spike at training time updates a range of future time steps proportional to 1+σ. This could be a significant overhead for large networks and long sequences. The paper does not report training time or GPU memory relative to baselines. For a method whose motivation includes neuromorphic deployment, understanding the training cost profile is important.

4. **Limited direct comparison of recurrent vs. feedforward delays on main benchmarks:** The direct recurrent-vs-feedforward comparison (Fig. 3) is conducted only on SHD with ≤10k parameters. On SSC and PS-MNIST where SOTA is claimed, the best configuration is "recurrent-only delays" (Table 1), but there is no ablation comparing it against "feedforward-only delays" at the same architecture and parameter count on these datasets. The paper would benefit from this comparison to directly test whether recurrent delays are uniquely beneficial at scale, or whether delay learning in general drives the improvement.

5. **Single seed on PS-MNIST:** Following prior convention but the evidence would be stronger with multiple seeds.

### Trivial
- Eq. 12's support calculation yields a lower bound of (d−σ), which for small d could be negative. This is effectively handled by the [0; ...] approximation in Eq. 13 and the pointer buffer mechanism, but a brief clarifying note would improve reproducibility.

## Nice-to-Haves
- Analysis of learned delay distributions (do learned recurrent delays cluster around certain values? relationship to task temporal structure?)
- Ablation on the σ decay schedule (linear vs. cosine vs. other)
- Discussion of whether per-synapse (rather than axonal) delays would further improve performance, and at what computational cost

## Removed Points
- **"Overstated novelty is structural/fatal"** — REMOVED because the paper explicitly discusses Xu et al. and Mészáros et al. in the introduction. The "first SGL-based" claim is defensible but imprecise (SGL refers specifically to surrogate gradients for the spike non-differentiability, while Xu et al. use softmax annealing which is a different kind of relaxation). Demoted from the harsh critic's "structural" severity to a minor framing issue.
- **"Negative τ indices in Eq. 12"** — REMOVED from weaknesses because Eq. 13 explicitly addresses this with the [0; ...] lower bound approximation. The paper already handles this.
- **"Gains not practically significant"** — REMOVED as this is a subjective judgment. Consistent gains (0.5–1.5%) across multiple benchmarks with simpler neurons is meaningful in the SNN literature, where SOTA improvements are typically incremental.
- **Strength Finder: "first SGL method"** — Partially merged into weakness #1; the claim is valid but needs qualification.
- **Strength Finder: "compatibility with any neuron model"** — Kept as a genuine strength since the method only modifies input current computation (Eq. 7), not neuron-specific dynamics.
- **Weakness about statistical significance on PS-MNIST (1 seed)** — Kept as minor since the paper notes it follows prior convention, but the paper's own SSC uses 3 seeds.

## Novel Insights
The most interesting finding beyond the paper's own claims is in Fig. 3B: a vanilla RSNN with *fixed random* recurrent delays achieves ~78% on SHD vs. ~40% for a vanilla RSNN with uniform delays — a massive 38% gap. This suggests that the gradient-mitigating effect of temporal skip connections (highlighted in Fig. 1B) may be more significant than the specific optimal delay values, and that much of the benefit of delay learning in recurrent connections comes from the architectural relief provided by longer skip paths rather than precise temporal alignment. The paper notes this briefly ("the simple introduction of delays in recurrent connections mitigates the training difficulties of RSNNs due to gradient issues") but does not unpack its implications: this finding implies that even a coarse, random delay distribution could serve as a strong initialization for learning, and raises the question of whether the σ annealing schedule could be replaced by simpler (cheaper) approaches.

## Suggestions
1. **Reframe the novelty claim** to emphasize the specific innovations (per-neuron continuous delays, differentiable interpolation with σ annealing, scheduling matrix) rather than "first SGL-based" — directly compare with Xu et al.'s per-layer softmax approach.
2. **Add training time/memory benchmarks** for DelRec vs. vanilla RSNN on at least one dataset (e.g., SSC).
3. **Include a feedforward-only delay ablation** on SSC at the same architecture/parameter count to isolate the recurrent-specific benefit at scale.
4. **Report PS-MNIST with at least 3 seeds** and test statistical significance of the SSC improvement over the prior best method.

## Score and Decision

**Round 1 bracket:** 4.0–6.5 (between weak SNN papers scoring ~3 and strong but unrelated papers scoring 8+).

**Round 2 anchors read in full:**
- FGT (avg 5.00, Reject) — SNN forward gradient training, no SOTA, weaker than DelRec
- S-TLLR (avg 5.00, Reject) — STDP-based training, comparable to BPTT, weaker than DelRec
- DeepTAGE (avg 6.25, Accept) — SNN gradient enhancement, SOTA on ImageNet/CIFAR, stronger dataset scale but broader scope
- MTT/Temporal Flexibility (avg 6.20, Accept) — SNN deployment flexibility, real chip results, comparable methodology contribution
- ST-DANO (avg 5.75, Reject) — Neuron optimization, larger performance gains (5%+) but rejected for insufficient comparisons
- SOLO (avg 4.00, Reject) — SNN online learning, poor results

**Final score relative to anchors:** DelRec is clearly above FGT (5.00) and S-TLLR (5.00). It is comparable to ST-DANO (5.75) but with better comparisons. It is slightly below DeepTAGE (6.25, which has ImageNet-scale validation) and MTT (6.20, which has real chip deployment). **Final score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Borderline Accept</decision>