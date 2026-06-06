## Summary

CorreGen proposes a generative EM framework for multi-view clustering (MVC) under noisy correspondence. Cross-view correspondences are treated as latent variables and inferred via an E-step combining GMM-guided marginal estimation with entropy-regularized optimal transport (including a virtual sample for unalignable data), while the M-step maximizes the expected log-likelihood to update the encoder. The method is evaluated on four datasets with controlled and organic noise, consistently outperforming baselines, especially under extreme noise.

---

## Strengths

- **Strong empirical robustness across all noise regimes.** Table 1 shows CorreGen consistently leads at all mismatch ratios (0–80%). At the extreme 80% MR on Caltech101, CorreGen achieves 64.74% ACC while the next best (CANDY) drops to 54.17%. On UMPC-Food101 with organic noise, CorreGen achieves 49.77% ACC vs. the strongest baseline's 36.20% at 0% MR, and 37.26% vs. 24.70% at MR=0.5, CR=0.5 in Table 2 — over a 10-point absolute improvement.

- **Novel generative reframing of the problem.** The shift from discriminative pair reweighting/realignment to explicit latent-variable MLE is a genuine conceptual advance within the noisy-correspondence MVC literature. The EM decomposition (Eqs. 4–8) cleanly separates correspondence inference from encoder optimization.

- **Principled GMM-guided marginal design.** Equation 13 assigns higher alignment mass to well-clustered, near-centroid samples and down-weights outliers via Mahalanobis distance and cluster size, while the virtual sample mechanism (Eq. 12) absorbs genuinely unalignable data. Figure 3 confirms that the estimated posterior progressively approaches the ground-truth block-diagonal structure, validating the E-step's ability to uncover category-level correspondences.

- **Efficient, differentiable OT solver.** Proposition 1 derives the Sinkhorn-iteration algorithm (Eq. 15) for the augmented marginal-constrained OT problem, making the E-step practical.

---

## Weaknesses

### Fatal
None.

### Major

- **Proposition 2 is mathematically incorrect as stated.** The joint distribution in Eq. (17) uses a *double-sum* normalizer: $\sum_m \sum_n \exp(s_{mn}/\tau)$. Substituting the degenerate posterior $Q_{ij} = \mathbf{1}[i=j]$ into Eq. (18) yields $\sum_i \log \frac{\exp(s_{ii}/\tau)}{\sum_m \sum_n \exp(s_{mn}/\tau)}$, which has the same fixed denominator for all $i$. Standard InfoNCE (Eq. 19) uses a *row-wise* denominator $\sum_n \exp(s_{in}/\tau)$, which varies with $i$. The two are equal only if the double-sum factorizes as a product of row sums — which is false in general. The InfoNCE-as-special-case claim is therefore not derivable from the model definition as written. The most natural resolution is that the actual implementation uses row-wise normalization (standard practice), and Eq. (17) is an inconsistent theoretical description of that implementation. Whichever is true, the definition in Eq. (17), the M-step in Eq. (18), and Proposition 2 must be made mutually consistent before publication, since Proposition 2 is explicitly listed as a contribution.

- **Theory–practice gap in the EM derivation.** Rigorous EM requires the posterior $p(\mathbf{x}_j^{(v_2)}|\mathbf{x}_i^{(v_1)}, \theta)$ to be computed from the same model distribution parameterized by $\theta$. In practice, the marginal in Eq. (13)–(14) is a heuristic function of Mahalanobis distance and cluster size: $p(\mathbf{x}_i^{(v)};\theta^{(t)}) = \frac{m^{d_i}-1}{m-1} \cdot \frac{N_c}{N}$. This is not equal to $\sum_j p(\mathbf{x}_i^{(v_1)}, \mathbf{x}_j^{(v_2)}; \theta)$ — the model's true marginal. The heuristic is well-motivated (reward high-confidence, large-cluster samples; penalize outliers) and empirically effective, but the paper frames the approach as rigorous MLE solved by EM, which overstates the principled nature of the derivation. Authors should either derive a formal connection between Eq. (13) and the model marginal or acknowledge it as a principled approximation.

- **Base-model entanglement limits generalizability claims.** CorreGen is implemented on top of DIVIDE, while all other baselines are standalone methods. The improvement over DIVIDE is real (e.g., Caltech101 0% MR: 68.52 vs. 62.20 ACC), and CorreGen also surpasses CANDY (which itself beats DIVIDE in several settings), suggesting the generative objective adds genuine value. However, the paper makes no attempt to show that the same generative objective, applied on top of a *different* base model, produces similar gains. The method's generality is asserted but not demonstrated.

### Minor

- **Missing standard deviations for borderline margins.** Table 1 caption states results are averages over five seeds, but no standard deviations are reported. On LandUse21 at 0% MR, CorreGen improves over DIVIDE by only 0.37 ACC (32.87 vs. 32.50); without variance estimates this margin's significance is unknown. This is especially important given the paper's claim of consistent improvement.

- **Noise ratio $\rho$ is not practically grounded in the main text.** The virtual-sample probability mass $\rho$ is described as "the potential noise ratio" but no guidance is given for how to set it when the true noise level is unknown — the typical real-world case. UMPC-Food101 contains organic noise with unknown rate; a sentence in Section 4.1 explaining how $\rho$ was chosen there would materially help practitioners.

- **Occasional losses in Table 2 not acknowledged.** At MR=0.2, CR=0.5 on Caltech101, CANDY achieves 62.57 ACC vs. CorreGen's 61.19, and DIVIDE's ARI of 58.56 exceeds CorreGen's 49.65. These are the only settings where CorreGen falls behind, and the text's implicit claim of across-the-board best performance should note these exceptions.

### Trivial

- **Notation inconsistency in Eq. (3).** The second summation index is written as $v_i$ but should be $i$ (over samples, not views); the intent is clear from context but the formula is formally incorrect.

- **Ambiguous $Q$ subscript in Eqs. (5)–(7).** The auxiliary distribution is written as $Q(\mathbf{x}_j^{(v_2)})$ without an $i$ subscript, obscuring that the tight-bound condition requires a per-anchor conditional $Q_i$. The implementation correctly uses $Q_{ij} = P^*_{ij}/p^{(v_1)}_i$, so only the notation in the derivation is misleading.

---

## Nice-to-Haves

- **Ablation separating GMM marginals from the virtual-sample mechanism.** These two components address distinct problems (category-level vs. sample-level mismatch). Understanding which drives most of the gain over DIVIDE would sharpen the paper's claim to address both types simultaneously.

- **Computational cost discussion.** GMM fitting and Sinkhorn iterations are each $O(N^2)$ per EM iteration. A brief note on wall-clock training time and scalability to larger datasets would be valuable for practitioners.

- **Real-noise visualization analogous to Figure 3.** Figure 3 shows posterior recovery on Caltech101 with synthetic noise. A similar visualization on UMPC-Food101 (organic noise) would provide the clearest evidence that the method solves the real-world problem motivating the paper.

- **Verifying whether generative objective transfers to another base model.** Even a single brief experiment on a second base model would substantially strengthen the generality claim.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic's reproducibility concern about constant $A$ in Eq. (16).** The value of $A$ is a hyperparameter likely specified in Appendix C (stripped). Per rules, nitpicks about undisclosed hyperparameters in stripped appendices are removed.

- **Strength Finder's "Theoretical unification with InfoNCE" as a core strength.** This is directly contradicted by the verified Proposition 2 error (double-sum vs. row-wise normalization). When a strength and a verified weakness conflict, the weakness wins.

- **Strength Finder's "Computationally efficient OT-based solver" as a supporting strength.** While Proposition 1 is technically correct, calling the Sinkhorn iteration over an $N \times N$ matrix "computationally efficient" without any comparative cost analysis is unsupported. Removed as a generic claim lacking a concrete benchmark anchor.

---

## Novel Insights

The key insight that distinguishes CorreGen from prior work is treating cross-view alignment as a *distribution estimation problem* rather than a *pair-cleaning problem*. By optimizing the marginal likelihood of observed views with counterparts as latent variables, the framework naturally captures many-to-many class-level relationships that pairwise reweighting/realignment cannot represent. The GMM-guided marginal assigns higher alignment budget to high-confidence, large-cluster samples — effectively implementing a soft notion of "semantic mass" — while the virtual-sample OT absorbs data that genuinely has no counterpart. Together, these address both failure modes (false negative suppression and outlier isolation) within a single principled objective, which is a structurally cleaner formulation than prior hybrid approaches.

---

## Suggestions

1. **Fix Eq. (17) or revise Proposition 2.** If the implementation uses row-wise normalization (which produces a genuine soft-InfoNCE and makes Proposition 2 correct), update Eq. (17) accordingly. If joint normalization is intended, work out what the objective actually reduces to and revise the claim.
2. **Clarify the EM approximation.** Explicitly acknowledge that Eq. (13) is a principled approximation to the model marginal, and provide either a brief derivation of the connection or a justification for why this specific heuristic is preferable to alternatives (e.g., uniform, raw GMM density).
3. **Add standard deviations to Tables 1 and 2.** At least for the smallest margins, this is necessary to support significance of improvements.
4. **Describe ρ selection in the main text.** A sentence on how ρ is set for UMPC-Food101 (where ground-truth noise rate is unknown) is essential for reproducibility and practical adoption.
5. **Apply CorreGen to one additional base model** (even in an ablation) to support generality claims.

---

## Evaluation Summary

| Axis | Assessment |
|---|---|
| **Originality** | High — generative EM framing for noisy-correspondence MVC is novel in this field |
| **Importance** | High — noisy correspondence is prevalent in web-crawled multimodal data |
| **Claims supported** | Moderate — empirical claims strongly supported; Proposition 2 theoretical claim has a verifiable error |
| **Soundness** | Moderate — EM derivation is approximate rather than exact; main algorithmic design is coherent |
| **Clarity** | Moderate — main narrative is clear; notation inconsistencies and missing practical details reduce clarity |
| **Community value** | High — strong and consistent empirical gains, modular design applicable to existing MVC frameworks |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>