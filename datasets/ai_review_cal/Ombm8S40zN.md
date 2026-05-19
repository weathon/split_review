- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 6, 5
Now I have a thorough understanding of the paper and can verify each reviewer claim against the actual text. Let me produce the consolidated review.

---

## Summary

This paper introduces Discrete Denoising Posterior Prediction (DDPP), a framework for steering masked discrete diffusion models (MDMs) by framing fine-tuning as Bayesian posterior sampling from a target distribution proportional to a pretrained MDM prior times a reward. Three concrete objectives are derived (DDPP-IS, DDPP-LB, DDPP-KL), each handling the intractable log-partition function differently. The method is validated across synthetic data, pixel-level images, protein sequences (with wet-lab validation of expressed proteins), and text, consistently outperforming baselines including Relative Trajectory Balance (RTB).

## Strengths

1. **Simulation-free off-policy training for DDPP-IS and DDPP-LB** — The sub-trajectory matching objective (Eq. 8) and single-step objective (Eq. 11) are defined per noise level without unrolling the full diffusion process. As the paper explicitly states, this "makes DDPP a simulation-free method" and enables off-policy evaluation via a replay buffer. This is a concrete improvement over RTB, which requires simulating the entire trajectory for each training step (Table 1).

2. **Applicability to non-differentiable reward functions** — DDPP-IS and DDPP-LB require only the evaluation of the reward \(R(\mathbf{x}_0)\), not its gradient (Section 3.1: "the loss computes \(R(\mathbf{x}_0)\) and not a gradient of the reward"). This is demonstrated concretely on the protein tasks (Section 4.3) where ESMFold is explicitly non-differentiable and expensive to query.

3. **Wet-lab validation of generated protein sequences** — Section 4.3 reports that four out of six DDPP-designed protein constructs showed detectable expression in *E. coli*, visualized via SDS-PAGE in Figure 2. This provides real-world evidence beyond in-silico metrics that DDPP can produce synthesizable, expressible sequences.

4. **Theoretical guarantee for the learned log-partition function** — Proposition 1 (Section 3.1) proves that the parameterized log-partition estimate \(\log\hat{\mathcal{Z}}_{\pi_{t},\theta}^{LB}\) is a lower bound to the importance-sampling estimate when using the finetuned model as the proposal, with equality at the optimal proposal. This gives principled grounding to the most computationally efficient variant (DDPP-LB).

5. **Broad empirical validation across four domains** — The paper evaluates DDPP on synthetic grids (Figure 1), binarized MNIST (Table 2), pixel-level CelebA images (Figure 3), protein sequences with wet-lab follow-up (Table 3, Figure 2), and text generation (Table 4). DDPP matches or exceeds baselines on reward and sample quality in each domain.

6. **Consistent outperformance over RTB** — DDPP-LB achieves notably higher log reward than RTB across tasks: 44.7% vs 38.5% \(\beta\)-sheet in proteins (Table 3), log reward 1.85 vs 1.19 on toxicity (Table 4), and 3.42 vs 2.58 on sentiment (Table 4). The simulation-free DDPP objectives are more effective than full-trajectory matching.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **Abstract overclaims "simulation-free" for all three variants** — The abstract states that DDPP leads to "a family of three novel objectives that are all simulation-free." However, Section 3.3 explicitly states that DDPP-KL requires "on-policy" sampling from the fine-tuned model and backpropagation through a discrete sampling step via the REINMAX gradient estimator, making it simulation-based. The paper is transparent about this in the methods section (lines 163–165), but the blanket claim in the abstract is misleading and should be qualified to apply only to DDPP-IS and DDPP-LB.

2. **Missing ethical discussion for toxic text generation** — Section 4.4 tasks include generating toxic content in product reviews. The paper does not discuss potential misuse, safeguards, or ethical considerations around this experiment. Given current community norms, a brief ethics or responsible-use statement would be expected for this experimental design.

3. **No analysis of the importance-sampling estimator variance for \(\log\mathcal{Z}_{\pi_{t}}\)** — DDPP-IS uses a Monte Carlo estimate of the log-partition function with \(M\) samples from the pretrained denoiser. The paper does not analyze how the variance of this estimator scales with sequence length, reward sharpness, or the number of particles \(M\). If the pretrained model assigns low probability to high-reward regions, the IS estimate could have high variance or bias, potentially degrading fine-tuning. An ablation varying \(M\) or a small-scale diagnostic would help characterize when the estimator is reliable.

4. **Pixel-level image results: BPD gap with RTB not discussed** — In Section 4.2, DDPP-LB achieves higher reward than RTB but worse BPD (Figure 3). The paper notes that BPD is "within the range of the base model" but does not discuss whether the lower BPD could reflect reduced sample diversity (mode collapse). A brief discussion of this tradeoff would strengthen the analysis.

### Trivial
None.

## Nice-to-Haves
- A small-scale synthetic experiment where the true log-partition function can be computed, comparing DDPP-IS and DDPP-LB estimates against ground truth across noise levels.
- A discussion of the discretization error introduced by the single-step variant (Section 3.2) relative to the full sub-trajectory objective.
- Clarifying in the abstract that DDPP-IS and DDPP-LB are simulation-free, while DDPP-KL requires on-policy sampling.

## Removed Points
- **"The DDPP objective lacks a rigorous derivation from detailed balance"** — The derivation is clear in the paper. Detailed balance (Eq. 5) implies \(q_\theta(\cdot|\mathbf{x}_t) = \pi_t(\cdot|\mathbf{x}_t)\). Taking logarithms gives \(\log q_\theta - \log p_t^{\mathrm{pre}} + \log\mathcal{Z}_{\pi_t} - \log R = \log q_\theta - \log\pi_t\). Minimizing the MSE of this quantity makes \(q_\theta\) match \(\pi_t\). This is standard and well-explained; the claim of a "missing link" misreads the text.
- **"DDPP-KL has an unfair advantage with differentiable reward on MNIST"** — The paper explicitly acknowledges in Section 3.3 that DDPP-KL "requires the reward model \(R\) to be differentiable and as a result is less broadly applicable" (line 165). The comparison is presented fairly with full disclosure.
- **"Proposition 1's inequality may not hold during joint training"** — The paper explicitly addresses this: "it suffices to take a single gradient step" (line 131). The proposition states the inequality for a fixed proposal, and the practical training procedure with a single step is a standard approximation. The concern is acknowledged and the limitation is clearly stated.
- **"Missing related works"** — Cannot be verified without external sources and is excluded per guidelines.
- **Formatting/style nitpicks** — Removed per guidelines.
- **Generic reproducibility concerns** (undisclosed hyperparameters, etc.) — Removed per guidelines; the paper provides algorithmic descriptions (Algorithms 1 and 2) and experimental details in the appendix.

## Novel Insights

The harsh critic and strength finder together surface an interesting tension: the DDPP framework's core theoretical appeal (principled posterior sampling via detailed balance) is paired with a practical admission that the log-partition function must be estimated, creating a gap between the clean Bayesian framing and the actual algorithm. The strength finder correctly identifies wet-lab validation as the paper's most compelling evidence, but neither reviewer fully explores the implication that the wet-lab results (4/6 constructs expressing, but with low yields) validate the *method's ability to generate synthesizable sequences* more than they validate the *posterior sampling guarantee*. This suggests the paper's strongest contribution may be its practical framework for steering MDMs with non-differentiable rewards, rather than its Bayesian sampling perspective per se.

## Suggestions

1. **In the abstract, qualify the "simulation-free" claim** to apply specifically to DDPP-IS and DDPP-LB, noting that DDPP-KL requires on-policy simulation.
2. **Add a brief ethics discussion** in the text experiments section (4.4) addressing the potential dual-use concerns of generating toxic content and the limitations of the experimental setup as a research demonstration.
3. **Include an ablation on the number of IS particles \(M\)** in a controlled setting (e.g., synthetic grid) to empirically assess the variance of the log-partition estimator and validate that the chosen \(M\) is sufficient.
4. **Discuss the BPD-reward tradeoff** in Section 4.2 more explicitly, including whether lower BPD might indicate reduced diversity and how this interacts with the choice of \(\gamma\) or the partition function estimation strategy.
