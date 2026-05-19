- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have all the information needed. Let me compile the final consolidated review.

---

## Summary

This paper introduces Memory-Consistent Neural Networks (MCNNs), a semi-parametric model class for behavior cloning that hard-constrains policy outputs to lie within double-cone-like regions anchored to prototypical "memory" samples from the training data. The authors provide a theoretical sub-optimality bound (Theorem 1) and demonstrate empirically that MCNN variants consistently outperform their vanilla counterparts (MLP, BeT, Diffusion Policy) across 10 tasks spanning dexterous manipulation, driving, and kitchen environments with varying data regimes.

## Strengths

- **Consistent and large empirical gains across all tasks and backbones.** The paper demonstrates that MCNN variants (MCNN+MLP, MCNN+BeT, MCNN+Diff) outperform their vanilla counterparts in every task and every architecture tested (Figures 3–5, lines 279–297). Notable examples: in hammer-human-v1, MCNN+MLP is the only method achieving positive return (jumping from -11 to 262); in relocate-human-v1, MCNN+BeT is the only method with positive return. The pattern holds across both the low-data "human" regime (25 demos) and the high-data "expert" regime (5000 demos).

- **Plug-in compatibility with diverse architectures.** MCNN is demonstrated with MLP, Behavior Transformer, and Diffusion Policy backbones (Section 5), and in every case improves over the vanilla version. This flexibility is a practical advantage over prior methods tied to a single architecture.

- **Principled ablation identifying a "sweet spot" for memory count.** Figure 6 (left) shows performance peaks at 10–20% of the dataset as memories, with degradation toward 1-NN performance at 100%. This provides concrete guidance for practitioners and validates the design intuition that a moderate number of memories is beneficial.

- **Bounded function class width (Lemma 4).** The paper shows that the width of the MCNN function class is bounded by \(2L(1 - e^{-\lambda d^I})\), a property not available for vanilla neural networks. This theoretical observation is not affected by the |𝒜| issue and stands independently.

## Weaknesses

### Major

- **Theorem 1's use of |𝒜| (action set cardinality) is incompatible with the continuous-action experimental setting.** The sub-optimality bound (Theorem 1, line 152) contains the term \(|\mathcal{A}|\) — the cardinality of the action set. In every experiment, actions are continuous (24–30 dimensional in Adroit, 9-D in Franka Kitchen, 2-D in CARLA; line 213), making \(|\mathcal{A}|\) infinite and the bound \( \min\{H, \infty\} = H \), which is trivially true for any policy in a finite-horizon MDP with bounded rewards. The paper's headline claim of a "guaranteed upper bound" for MCNN policies therefore does not provide any non-trivial guarantee in the setting where it is evaluated. Furthermore, the paper originally included a sentence acknowledging this limitation ("We do not yet have an exact analysis of the performance gap for continuous state and action space MDPs…"), which has been marked for removal from the main text (line 159, `\toremove`). This is a significant mismatch between the theory as presented and the experiments. **Why it matters:** The theoretical contribution as stated is misleading — it promises a bound that is either undefined (infinite cardinality) or vacuous (collapses to \(H\)) for the entire evaluation suite. The authors must either (a) scope the theorem to discrete action spaces, (b) replace \(|\mathcal{A}|\) with a meaningful continuous-action quantity (e.g., action range or Lipschitz constant), or (c) explicitly caveat that the bound currently applies only to the discrete-action case.

### Minor

- **IBC baseline results are taken from the original paper rather than re-run.** The paper reports IBC results "from [florence2022ibc]" (line 219) rather than running the method under identical conditions. While common practice, this introduces uncontrolled variance from different random seeds, evaluation protocols, or data splits. This is not a fatal flaw but weakens the head-to-head comparison.

- **No ablation isolating the effect of the double-cone constraint from mere memory-augmented inputs.** The experiments compare MCNN variants to vanilla backbones, but the vanilla backbones do not receive the memory-augmented input features (closest memory state and action) that MCNN uses. A cleaner control would be: train a vanilla DNN on the same memory-augmented inputs (without the MCNN constraint) to verify that the improvement stems from the hard constraint rather than the extra features alone.

- **Computational cost of nearest-neighbor lookup not discussed.** The method performs a nearest-neighbor search at each evaluation step (against up to ~100k memories for the 1M-transition expert datasets). The paper does not report inference timings or wall-clock training times, nor does it discuss how this cost scales. This matters for potential real-time deployment.

- **No direct measurement of distributional shift.** The central motivation for MCNN is that it prevents large errors on out-of-distribution states. However, the paper does not directly measure whether MCNN rollouts stay closer to the training distribution (e.g., average/minimum distance to nearest training state during rollout) compared to vanilla policies.

### Trivial

- The distance metric \(d\) in the MCNN definition (line 79) is left unspecified in the theoretical development. While this is standard for general analysis, a brief empirical note (e.g., "we use Euclidean distance in practice") would improve clarity.

## Nice-to-Haves

- A hyperparameter sweep over \(\lambda\) and \(L\) to illustrate the trade-off between permissible region size and performance, rather than fixing them across all tasks.
- An empirical check of the realizability assumption on at least one task (e.g., measuring how well the expert's actions can be approximated within the MCNN's permissible regions).
- Reporting the distance to the most isolated state \(d^I\) for typical configurations to ground the theoretical quantities.
- Comparing MCNN with a vanilla DNN trained on the same memory-augmented inputs to isolate the effect of the double-cone constraint.

## Removed Points

*These points were raised by the reviewers but are removed after cross-checking against the paper, as per the filtering rules.*

- **"Realizability assumption is severe and unverified"** — DEMOTED from the reviewer's framing as a major evidential weakness. This assumption (Assumption 1, lines 118–120) is standard practice in theoretical IL work. The paper explicitly states it as an assumption and provides reasonable justification (lines 122–127). Empirically verifying every theoretical assumption is not standard in this community and would not meaningfully strengthen the paper's contribution.
- **"Distance metric not specified"** — The paper states "some distance metric defined on the space \(\mathcal{S}\)" (line 79), which is standard for theoretical development. The practical choice (Euclidean) is implicit in the VINN description. This is not a substantive weakness.
- **"Lemma 1 bound can approach 2L"** — This observation is technically correct but does not identify a flaw; it simply describes the behavior of the bound. The bound is what it is — it does not claim to be tight for all configurations.
- **"Missing ablation on number of architectures"** — The paper already tests three distinct architectures (MLP, BeT, Diffusion), which is more than most comparable papers.
- **"Pure formatting/style nitpicks"** — Removed per hard rules.
- **"Missing related work"** — Removed per hard rules (cannot confirm from external sources).
- **Strength Finder's generic strengths** (e.g., "this paper addresses an important problem") — Removed as generic/superficial. Only concrete strengths with specific evidence are retained.

## Novel Insights

None beyond the paper's own contributions. The key insight — that hard-constraining policy outputs within double-cone regions anchored to memory prototypes can consistently improve behavior cloning across architectures — is the paper's own contribution. The reviews do not surface an independent novel observation beyond what the paper already provides.

## Suggestions

1. **Fix the theory–experiment mismatch.** Either scope Theorem 1 to discrete action spaces explicitly, or derive a bound using a continuous-action quantity (e.g., the action bound \(L\) already used in the MCNN definition). If the bound becomes vacuous (collapsing to \(H\)), state this honestly and present the bounded-width Lemma 4 as the primary theoretical contribution instead.
2. **Re-run IBC** under the same evaluation conditions (or at minimum report the sensitivity of the IBC numbers to seed/protocol variation), to strengthen the baselines.
3. **Add a control ablation** comparing a vanilla DNN trained on memory-augmented inputs (nearest-memory state and action as extra features, without the MCNN constraint) to isolate the effect of the double-cone constraint.
4. **Report compute times** (training + inference) and discuss the scaling behavior of the nearest-neighbor lookup as memory count grows.
5. **Add a distributional shift analysis** measuring, e.g., the average/minimum distance from visited states to the training set during MCNN vs. vanilla policy rollouts, to directly validate the proposed mechanism.
