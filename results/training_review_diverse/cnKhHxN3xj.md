Here is the final consolidated review:

---

## Summary

This paper proposes using the Wasserstein distance (WD) of a neuron's output distribution (pre-activation) to a Gaussian as a measure of neuronal entanglement in LLMs. It identifies a small fraction of "Wasserstein neurons" with highly non-Gaussian output distributions and shows that these neurons are disproportionately sensitive to weight sparsity — sparsifying just the top 3% of WD-ranked neurons causes far greater performance degradation than sparsifying random or magnitude-selected neurons (Figure 3). The paper also introduces Sparse Expansion, a mixture-of-sparse-experts framework that clusters inputs and creates per-cluster sparse copies of each weight matrix via SparseGPT, demonstrating that this reduces the per-neuron WD and recovers performance lost from sparsifying Wasserstein neurons.

## Strengths

- **Novel identification of non-Gaussian output distributions as a marker of sparsity sensitivity.** The paper shows convincingly that neurons ranked by Wasserstein distance to a Gaussian exhibit dramatically higher sensitivity to pruning than those selected by output mean, variance, or weight magnitude (Figure 3). This empirical finding — that the *shape* of a neuron's output distribution matters for sparsity — is genuinely novel and opens a new direction for compression research.

- **Internal consistency between mapping difficulty (MD) and Wasserstein distance.** The paper defines entanglement via the mapping difficulty metric (Equation 2), grounded in superposition theory's notion that entangled neurons must distinguish similar inputs. The strong correlation between MD and WD (Figure 2e) provides internal validation that WD captures a meaningful property related to the input-output computation of individual neurons.

- **Sparse Expansion provides a causal framework (not just correlation) for studying disentanglement.** The paper goes beyond correlation by intervening: Sparse Expansion separates inputs into clusters, and the resulting per-neuron weighted WD decreases by a median of 19% across all neurons and 42% for Wasserstein neurons (Figure 5b-c), with corresponding performance recovery (Figure 5a). This provides controlled evidence that input separation reduces the difficulty of sparse computation, beyond mere correlation.

- **Demonstration that WD outperforms other simple metrics (mean, variance, GMM components) in predicting improvement from disentanglement (Figure 7).** The R² comparison is a clean, quantitative argument that WD captures something distinct from these other statistics about a neuron's output distribution.

## Weaknesses

### Fatal
None.

### Major

- **The performance comparisons of Sparse Expansion against baselines (Figure 9) are confounded by total parameter count.** Sparse Expansion with 16 experts each at 50% sparsity uses ~8× the non-zero weights of a single SparseGPT model at 50% sparsity. While the paper acknowledges the memory cost ("this method is likely not practically implementable") and the X-axis accounts for routing FLOPs, Figure 9 is presented as a head-to-head comparison without controlling for total non-zero parameter budget. This confound inflates the apparent performance advantage of Sparse Expansion over SparseGPT, Wanda, and magnitude pruning. The gains could simply reflect having more parameters per layer rather than successful disentanglement. Controls such as a single SparseGPT model with matched total non-zero weights or a random-cluster version of Sparse Expansion would be needed to attribute the improvement to clustering-based disentanglement.

- **Lack of external validation for WD as a measure of entanglement against established polysemanticity indicators.** The paper validates WD against MD, but MD is itself a new construct introduced in this work. Neither metric is checked against known polysemantic neurons identified by sparse autoencoders (e.g., by testing whether high-WD neurons correspond to neurons known from mechanistic interpretability studies to represent multiple features). Without this external grounding, the claim that WD measures "entanglement" in the sense established by the mechanistic interpretability literature (Elhage et al., Bricken et al.) rests entirely on internal consistency. The metric could be picking up other properties (e.g., non-Gaussianity induced by input statistics) that are not specific to feature superposition.

### Minor

- **The causal link between WD and sparsity sensitivity is not fully established.** Figure 3 shows that high-WD neurons are disproportionately sensitive to sparsification, but this does not rule out alternative explanations such as the neuron's Lipschitz constant, its role in a specific circuit, or its position in the network. The Sparse Expansion results partially address this by showing that disentanglement recovers performance, but a more direct causal experiment (e.g., showing that two neurons with similar WD but different roles in circuits have different sparsity sensitivity) would strengthen the claim.

- **Section 3.5 ("Theoretical Implications") overstates its conclusions.** The paper describes "empirical demonstrations of the existence of bounds" but presents only observational correlations — linear frontiers in log-log plots between PCA components and RMSE (Figure 8b-c). No formal bounds are derived or tested. The term "bound" in the theoretical literature (Hänni et al., Adler & Shavit) carries a precise mathematical meaning that the empirical trends shown here do not meet. The section would be more accurately described as providing empirical trends consistent with the existence of such bounds.

### Trivial

- None.

## Nice-to-Haves

- An ablation or sensitivity analysis on the number of clusters (currently fixed to 16) with respect to both performance and per-neuron WD decrease. The paper references Figure A3 (presumably in the appendix) for this, but a main-text summary would help readers assess the robustness of the framework.
- A discussion of the OOD results (Table A1, A2) in the main text, as many pruning methods degrade on distribution shifts — if Sparse Expansion preserves OOD performance, this is noteworthy.
- A more quantitative estimate of the added latency and memory overhead of Sparse Expansion relative to baselines, to help readers assess practical feasibility.

## Removed Points

*(These criticisms are removed per the meta-reviewer guidelines for the reasons stated.)*

1. **Pre-/post-activation ambiguity (Harsh Critic):** The paper clearly defines the output distribution as the result of Y = WX + b (line 30-31), i.e., pre-activation. The concern about SiLU activation functions is irrelevant because the metric operates on pre-activation values. **Removed: factually wrong about paper content.**

2. **"Wasserstein neurons as a discrete class" (Harsh Critic):** The paper consistently defines Wasserstein neurons by a percentile threshold (top 3% or top 10% by WD), not as a discrete class. The critic's claim is a misreading. **Removed: misrepresents paper content.**

3. **Circular validation claim (Harsh Critic):** MD and WD are distinct metrics; correlating them is not circular. The lack of external validation is a separate, valid concern (retained as a Major weakness above), but the charge of circular reasoning is incorrect. **Removed: factually inaccurate characterization.**

4. **Missing cluster count justification (Harsh Critic):** The paper references tuning the number of clusters in the appendix (Figure A3, line 149). The parser stripped the appendix; the original submission contains this analysis. **Removed: appendix-stripping artifact.**

5. **Missing related works / formatting / typo nitpicks:** All removed as per the meta-reviewer guidelines.

## Novel Insights

The reviews reveal a deeper tension in the paper than its own framing acknowledges: the paper defines "entanglement" in terms of input-output mapping difficulty (MD), then validates WD against MD, but this internal consistency does not bridge to the broader mechanistic interpretability literature where polysemanticity is understood via feature decomposition (sparse autoencoders). The paper's most robust contribution is arguably not the entanglement framing itself, but the empirical finding that distribution shape (non-Gaussianity) predicts sparsity sensitivity — a finding that stands regardless of whether one accepts the entanglement interpretation. A cleaner framing would separate the (well-supported) observation that WD predicts sparsity sensitivity from the (more speculative) claim that WD measures polysemantic entanglement in the sense of superposition theory.

## Suggestions

1. **For the performance comparisons (Figure 9):** Add a controlled baseline that matches the total non-zero parameter budget — e.g., a single SparseGPT model with more non-zero weights per layer (lower sparsity) to match Sparse Expansion's total budget, and a random-cluster version of Sparse Expansion. This would cleanly separate disentanglement gains from parameter count gains.

2. **For the metric validation:** Validate WD against an established polysemanticity measure on a small scale — e.g., correlate high-WD neurons with neurons that sparse autoencoders identify as representing multiple features, or with feature dimensionality from an SAE. Even a small-scale validation (one or two layers in one model) would substantially strengthen the entanglement claim.

3. **For Section 3.5:** Reframe the language from "bounds" to "empirical trends" or "scaling relationships" to avoid overclaiming formal theoretical support.

4. **Clarify the main narrative:** The paper would benefit from explicitly distinguishing the two contributions — (a) WD as a predictor of sparsity sensitivity (well-supported) from (b) WD as a measure of polysemantic entanglement (less well-supported) — rather than treating them as equivalent. The former is a stronger, more defensible claim.

## Score and Decision

This paper makes a genuine empirical contribution by identifying the Wasserstein distance of a neuron's output distribution as a novel and surprisingly strong predictor of sparsity sensitivity. The core finding (Figure 3 and Figure 7) is clean, reproducible, and interesting. The Sparse Expansion framework, despite its parameter-count confound, provides useful causal evidence that input separation improves sparse computation — the per-neuron WD/MD decrease is not confounded by parameter count. However, the paper overreaches by equating WD with polysemantic entanglement without external validation against established measures, and the main performance comparisons (Figure 9) overstate Sparse Expansion's advantage due to uncontrolled parameter budgets. These weaknesses are addressable but nontrivial. The paper's strongest contribution — the distribution-shape/sensitivity link — is valuable and likely to be influential.

**Score:** 5.0 (borderline accept — interesting empirical findings with notable but addressable weaknesses)

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>