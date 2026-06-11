Now I have a clear picture. Let me produce the final review.

## Summary

DelRec introduces the first surrogate-gradient-based method to learn per-neuron delays in recurrent connections of spiking neural networks. It uses differentiable triangle-function interpolation with progressive σ annealing to handle non-integer delays during training, and a scheduling matrix for efficient implementation. The method achieves 82.58% on SSC (LIF-based SOTA) and 96.21% on PS-MNIST using simple LIF neurons with competitive parameter counts. A controlled ablation on SHD demonstrates that learned recurrent delays outperform feedforward delays under low-parameter constraints.

## Strengths

1. **First SGL-based method for learning per-neuron delays in recurrent SNNs.** Prior work either learns a single recurrent delay per layer via softmax selection (Xu et al.) or uses EventProp with scalability limitations (Mészáros et al., 2025). DelRec's SGL approach is compatible with standard backpropagation and any spiking neuron model (Section 2.2).

2. **New LIF-based SOTA on SSC (82.58±0.08%) and PS-MNIST (96.21%) with competitive parameter counts** (0.37M and 0.16M respectively), achieved using only simple LIF neurons rather than complex adaptive, resonant, or multi-compartment neurons used by many competitors (Table 1). This is the paper's headline empirical result.

3. **Controlled ablation on SHD (Fig. 3C) demonstrates systematic advantage of learned recurrent delays.** Under low-parameter constraints (~10k down to ~2k parameters), recurrent-delay models consistently outperform learned feedforward delays, fixed random recurrent delays, and vanilla baselines, with accuracy degrading less steeply. This provides the cleanest causal evidence for the paper's claims.

4. **Differentiable triangle-function interpolation with progressive σ annealing** is technically clean: it avoids predefining a maximum delay range, provides well-defined gradients for continuous-valued delays during training, and the finite-support property (Eq. 12) bounds computational cost automatically.

5. **Methodological care in the SHD study:** the paper acknowledges SHD saturation, creates a proper validation split from 20% of the training set (a recognized best practice), reports results over 10 seeds, and carefully separates LIF-based from non-LIF-based models in Table 1 with clear rationale.

## Weaknesses

### Major

1. **The combined recurrent+feedforward variant underperforms the recurrent-only variant on SSC without explanation.** On the primary SSC benchmark, DelRec with both recurrent and feedforward delays achieves 82.19±0.16%, while the recurrent-only variant achieves 82.58±0.08% (Table 1). The paper presents the combined approach as a contribution ("our study is the first to combine the optimization of feedforward delays using DCLS...and delays in recurrent connections") but does not address why adding feedforward delay optimization *hurts* performance on the larger benchmark. This weakens the case for the combined method and suggests possible overfitting or optimization interference that needs investigation.

2. **The PS-MNIST result is reported from a single seed without variance estimates, and the improvement over the prior LIF-based SOTA (ASRC-SNN, 95.77%) is only 0.44 percentage points.** The paper's justification ("we only test one seed as all the previous state-of-the-art models on the dataset") is insufficient — prior work's methodological limitation does not license repeating it. Since PS-MNIST is one of the two headline SOTA claims, the absence of error bars makes it impossible to assess whether this result is statistically meaningful.

### Minor

3. **The SOTA claim in the abstract is unqualified.** The abstract states "new state-of-the-art (SOTA) on two challenging temporal datasets" without caveat. The body and footnote 1 are transparent about the restricted comparison class (LIF-based models without complex neurons like multi-compartment or attention mechanisms), but the abstract's framing exceeds what the evidence supports relative to the broader SNN literature. Models with complex neurons (Wang et al., 2024: 83.69% on SSC; Chen et al., 2024: 97.78% on PS-MNIST) achieve higher absolute numbers, and the paper's SOTA claim only holds within a specific subset.

### Trivial

None.

## Nice-to-Haves

- **Report learned delay distributions** after training (do delays cluster at particular values or spread across the allowed range?). This is analysis of existing trained models and would give insight into how the method uses its degrees of freedom.
- **Provide empirical gradient analysis** to support the claim that delays mitigate gradient challenges (Fig. 1B), which is currently supported only by a computational graph illustration. Gradient norms or variance during training for delayed vs. non-delayed RSNN would strengthen this motivation.
- **Discuss compatibility with convolutional architectures**, since per-neuron axonal delays in conv layers would interact with shared weights in non-trivial ways.

## Removed Points

Points from the reviewers that were removed:

- **"The vanilla RSNN baseline on SHD is poorly configured"** — REMOVED. The paper attributes the poor performance (~40%) of uniform-delay-1 RSNN to known gradient issues and uses this gap as *evidence* for its thesis that delays help mitigate gradient problems. This is internally consistent, not a weakness.
- **"Eq. 15 reference is a labeling error"** — REMOVED per hard rule (typographical nitpick).
- **"EventProp is included despite being feedforward-only"** — REMOVED. Including relevant baselines in a comparison table is standard practice.
- **"Missing appendix content / Algorithm 1 not verifiable"** — REMOVED per hard rule (appendix stripped by parser).
- **"The paper does not report learned delay distributions"** — MOVED to Nice-to-Haves.

## Novel Insights

The most striking observation emerging from the review process is that the paper's strongest evidence lies in the SHD controlled study (Section 3.2), not in the headline SOTA figures. The smooth degradation curve of recurrent-delay models under aggressive parameter reduction (from ~10k down to ~2k parameters) provides genuinely clean causal evidence that learned recurrent delays improve temporal processing efficiency. The SSC/PS-MNIST results serve as validation that the approach scales, but the SHD study is where the paper proves its thesis. This stands in contrast to many SNN papers where the main contribution is claimed through SOTA numbers alone, without isolating the mechanism responsible.

## Suggestions

1. **Explain the recurrent-only vs. combined discrepancy on SSC.** If the combined model overfits or encounters optimization difficulties, the paper should say so explicitly. This is the most impactful fix.
2. **Run 3–5 seeds on PS-MNIST and report mean±std** to establish whether the 0.44 pp improvement over ASRC-SNN is significant.
3. **Qualify the SOTA claim in the abstract** (e.g., "new SOTA among LIF-based models").
4. **Report learned delay distributions** as an analysis of existing trained models — high insight per unit effort.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Strong reject band (<2.5): SI6zocV2SS (1.50), a8XwgTZzE0 (2.00), epFk8e470p (1.67) — clearly weaker than DelRec.
- Weak band (2.5–4.5): vq75kRCYuY (4.00, SOLO — SGL online learning, significant accuracy drops, weaker than DelRec), A6K4aqReoF (3.75), KJ4hQAfqVa (4.20) — DelRec is clearly stronger.
- Middle band (4.5–6.1): eN4g4cjFX1 (5.75, ST-DANO — neuron optimization, comparable depth), RmQAKu1wCe (5.00), vlQ56aWJhl (5.00).
- Strong band (6.0–7.5): 9HsfTgflT7 (6.20, MTT — accepted with temporal flexibility), drPDukdY3t (6.25, DeepTAGE — accepted with ImageNet experiments), UvfI4grcM7 (6.75).
- Very strong (>7.5): RWJX5F5I9g (8.00), kbjJ9ZOakb (8.00), cNmu0hZ4CL (8.00).

**Round 1 bracket:** 5.0 – 6.5

**Round 2 (Narrowing within bracket):**
- eN4g4cjFX1 (5.75, ST-DANO, Reject) — comparable depth of contribution; DelRec has a cleaner method but narrower experiments.
- 6iM7mmVhXh (5.75, layer synchronization limitations, Reject).
- 9HsfTgflT7 (6.20, MTT, Accept) — accepted but with notable reviewer concerns about marginal improvements.
- ZyknpOQwkT (5.50, Ensemble perspective, Accept) — accepted despite moderate novelty; DelRec's method is more novel.
- yBP36xQhZl (5.00, Forward gradient SNN, Reject).
- drPDukdY3t (6.25, DeepTAGE, Accept) — stronger empirically (includes ImageNet), but comparable method novelty.
- qzZsz6MuEq (6.60, Spiking ViT, Accept).

**Final placement:** DelRec is cleaner and more novel than the Ensemble paper (5.50, Accept) and comparable to ST-DANO (5.75, Reject). It has a stronger method than DeepTAGE (6.25) in terms of novelty, but narrower experimental breadth (no ImageNet, no convolutional architectures, only fully-connected networks). The unexplained recurrent-only vs. combined discrepancy and the missing variance on PS-MNIST are substantive weaknesses that lower the paper below the DeepTAGE and MTT anchors.

**Final score: 5.5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>