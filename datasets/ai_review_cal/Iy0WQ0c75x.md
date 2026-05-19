- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 5, 3
Now I have all the information needed. Here is my consolidated final review:

---

## Summary

This paper proposes HyperGCL, a self-supervised graph contrastive learning framework operating in hyperbolic space. The key ideas are: (1) using hyperbolic distance (rather than Euclidean cosine distance) for the alignment term in contrastive learning, and (2) replacing the standard uniformity loss with a KL-divergence loss that encourages tangent-space features at the identity to match a zero-mean isotropic Gaussian — which maps to an outer isotropic shell in the ambient Poincaré ball. The method is motivated by preventing "leaf collapse" and "height collapse," two forms of dimensional collapse specific to hyperbolic representations. Experiments on node classification and collaborative filtering benchmarks show consistent improvements over both Euclidean and hyperbolic baselines.

## Strengths

- **Novel and well-motivated uniformity mechanism for hyperbolic contrastive learning.** The paper correctly identifies that standard pairwise uniformity (maximizing inter-sample distances) fails in hyperbolic space because of its infinite volume, and proposes a principled alternative: enforce a zero-mean isotropic Gaussian in the tangent space, which maps to an outer isotropic shell in the ambient space. This is validated empirically by the simulations in Figures 4–5 and the ablations in Table 3.

- **Consistent empirical gains across multiple tasks and datasets.** HyperGCL outperforms all compared methods (both Euclidean and hyperbolic) on node classification (Table 1; e.g., PubMed 85.14% vs. HGCL 83.14%) and on collaborative filtering (Table 2; e.g., Amazon-CD Recall@10: 0.1069 vs. HRCF 0.1003). Gains are supported by reported standard deviations.

- **Clear diagnostic framework for hyperbolic dimensional collapse.** The paper characterizes two collapse modes specific to hyperbolic embeddings — leaf collapse and height collapse — and links them to the effective rank (Erank) of features in both ambient and tangent spaces. The ablation (Table 3) shows that alignment alone yields Erank as low as 1.22 on PubMed, while HyperGCL raises it to 6.89, empirically confirming the collapse is mitigated.

- **Rigorous ablation isolating each component.** Table 3 systematically compares Euclidean vs. hyperbolic alignment, different uniformity losses (none, hyperbolic pairwise, proposed tangent KL), and reports both accuracy and effective rank in ambient and tangent spaces. The near-identical Erank values in ambient vs. tangent spaces (e.g., 6.89 vs. 6.88 on PubMed) support the claim that improving rank in tangent space transfers to the ambient space. Table 4 further validates the design choice by showing that non-zero mean or non-isotropic covariance degrades performance.

## Weaknesses

### Fatal
None.

### Major

- **Theorem 1 (mapping of Normal distribution) is improperly derived and the presented formula is non-standard.** The proof environment is empty (lines 261–263), and the claimed density formula (Eq.~\ref{eq:theor_dis}, line 257) contains an ad-hoc function δ(v)=v if Im(v)=0 else 0 — which is not a correct change-of-variables density. For the exponential map (a diffeomorphism), the standard pushforward formula is p_Z(z) = p_N(log⁰_c(z)) · |det J|, where J is the Jacobian. The paper's formula does not emerge from any standard derivation, and the δ function appears to reflect confusion about the argument of tanh⁻¹ (which is always real for points inside the Poincaré ball). The simulations in Fig. 5 may approximate the correct density, but the stated formula and its derivation cannot be relied upon. Since the paper presents this as a theoretical contribution, this undermines the paper's theoretical credibility. *The method itself does not depend on this theorem (it is a post-hoc justification), so the empirical contribution is not invalidated, but the theory as presented is unsound.*

- **Theorem 2's inequality does not support the intended conclusion about effective rank.** The theorem states: -D(Σ, μ) ≤ log[Erank(Σ)] + const. The paper then claims that minimizing L^T_U = D(Σ,μ)+D(Σ',μ') "achieves a higher effective rank" (line 311). This does not follow: when D decreases, -D becomes less negative (larger), which only raises the *lower bound* on log[Erank]; the actual effective rank could remain unchanged or even decrease while staying above the bound. A direct relationship (e.g., an upper bound on -log Erank in terms of D) would be needed for the claimed implication. The empirical evidence in Table 3 does show the desired effect, but the theorem as stated does not prove it. The proof is also empty (lines 307–309).

- **The encoder architecture is under-specified, harming reproducibility.** The paper describes a Euclidean GCN encoder (Eq.~3, lines 161–162) that outputs embeddings Z. These embeddings are then used directly in the hyperbolic alignment loss D_c(z_i, z_i') and mapped to the tangent space via log⁰_c(·) for the isotropy loss. However, there is no specification of how the Euclidean GCN outputs become points in the Poincaré ball (i.e., satisfying ||z||² < 1/c). Line 171 mentions "a small margin ε > 0 to prevent infinite volume" but does not describe any projection, exponential map, or other mechanism. Without this detail, the forward pass cannot be reproduced, and the validity of the hyperbolic operations on these embeddings is unclear.

### Minor

- **The Gaussian assumption on tangent-space features is not discussed.** The isotropy loss assumes that the empirical distribution of log⁰_c(z_i) is well-modeled by a single multivariate Gaussian. For heterogeneous graphs or small minibatches, this assumption may be violated, but the paper does not discuss potential failure modes or alternatives.

- **Computational cost of the proposed uniformity loss vs. pairwise alternatives is not analyzed.** The paper claims pairwise hyperbolic distance (Eq.~\ref{eq:hyper_uni}) "incurs large computation overheads" (line 196) but provides no empirical comparison. The proposed KL-based loss requires computing mean and covariance over a minibatch (O(Nd²) for the covariance) — this is also not trivial, and a cost comparison would substantiate the claim.

- **Statistical significance is not assessed.** Standard deviations are reported, but no significance tests are conducted. Given that some improvements are modest (e.g., ~1% on Cora), it would strengthen the paper to indicate whether differences are statistically significant.

### Trivial
None.

## Nice-to-Haves

- Formal definitions of "leaf collapse" and "height collapse" (currently described qualitatively via figures and text) would strengthen the conceptual framing.
- Applying the full HyperGCL framework (GCN encoder + proposed losses) to collaborative filtering rather than only adding the isotropy loss to HRCF would test the framework as originally defined.

## Removed Points

*These points were flagged for removal from the input reviews — included here for transparency, not as part of the final assessment:*
- **Harsh critic's claim that "the paper never formally defines leaf/height collapse"** — The paper provides qualitative descriptions (tcolorbox, lines 149–150) and figures, which the critic acknowledges "is fine for motivation." This is a minor presentation preference, not a weakness affecting validity.
- **Harsh critic's claim about "comparison includes supervised methods (GCN, GAT)"** — This is a standard contextualization practice; the paper clearly marks supervised vs. self-supervised methods and does not claim to outperform supervised models on a level playing field.
- **Harsh critic's claim about collaborative filtering using a different architecture** — This demonstrates generality, not a weakness. The paper does not claim to evaluate "HyperGCL as a complete framework" on this task but rather shows the isotropy loss transfers across architectures.
- **Strength Finder's claim about "Theoretical lower bound relating the proposed loss to effective rank"** — Removed because, as verified in Major Weaknesses, Theorem 2 does not logically support the claim that minimizing L^T_U increases Erank, so this purported strength conflicts with a verified weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the key issue: the paper's theoretical apparatus (Theorems 1 and 2) attempts to provide formal justification but contains logical and mathematical gaps, while the empirical contribution — a novel, well-validated uniformity loss for hyperbolic contrastive learning — stands on its own merits.

## Suggestions

1. **Clarify the encoder specification.** Explicitly describe how Euclidean GCN outputs become hyperbolic embeddings (e.g., apply exp⁰_c(·) to the GCN output, or use a tanh to project within the ball, or any other standard mechanism). Include the exact forward pass as a step-by-step procedure.

2. **Remove or rigorously fix the theoretical derivations.** Theorem 1's density formula and Theorem 2's logical implication are both problematic as presented. The paper can simply present the tangent-space Gaussian loss as an empirically validated design choice (which the ablation already supports strongly) and drop the flawed theory. Alternatively, provide correct derivations with complete proofs.

3. **Add computational cost comparison.** Report wall-clock time or operations count for the proposed KL-based uniformity loss vs. pairwise hyperbolic uniformity to substantiate the efficiency claim.

4. **Discuss the Gaussian assumption.** Acknowledge the assumption that tangent-space features follow a single Gaussian and discuss when it might break down (e.g., small batches, heterogeneous graphs).
