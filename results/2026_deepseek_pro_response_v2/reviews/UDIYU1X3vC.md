Now I have sufficient anchors. Let me finalize my calibration and write the final review.

**Round 2 Narrowing Summary:**

The PVNN paper is clearly:
- **Stronger than** 30aSE3FB3L (5.67, Matrix Manifold NN++) — PVNN has far more extensive experiments and ablations
- **Stronger than** ekz1hN5QNh (6.00, Fully Hyperbolic CNN) — similar contribution type but PVNN has more tasks, bigger gains, and more thorough ablations  
- **Comparable to or slightly above** bwOndfohRK (6.00, Symmetric Spaces) — both provide practical layer formulations, PVNN is more concrete with better experimental validation
- **Below** skGSOcrIj7 (6.80, Neural Spacetimes) — PVNN has less theoretical novelty (reparameterization of known geometry vs. novel learnable geometry)
- **Comparable to** OTMPdMH9JL (6.50, Neural Eigenfunctions, Reject) — PVNN has comparable quality but more complete experimental validation

**Final score: 6.5 — Accept** (above the 6.0 accept threshold with stronger experiments and ablations).

---

## Summary
This paper proposes Proper Velocity Neural Networks (PVNNs), which use the Proper Velocity (PV) model of hyperbolic space — an unconstrained representation originating in special relativity — as an alternative to the Poincaré ball and hyperboloid models for hyperbolic deep learning. The authors prove that PV space and the Poincaré ball are Riemannian isometric (Thm 4.2) and use this isometry to derive the complete Riemannian toolkit (exponential/logarithmic maps, parallel transport, geodesic distance). They then construct core neural layers (MLR, FC, convolution, activation, batch normalization), with the PV MLR featuring an efficient unconstrained parameterization (Eq. 19) that avoids Riemannian optimization and enables batched matrix multiplication. Experiments on numerical stability, image classification, graph node classification, and genomic sequence learning demonstrate PVNNs' stability advantages and competitive or superior performance.

## Strengths
- **Complete Riemannian toolkit with honest use of isometry (Section 4):** The paper proves that PV space is Riemannian isometric to the Poincaré ball (Thm 4.2) and explicitly uses this isometry to transport exponential/logarithmic maps, parallel transport, and geodesic distance to PV space (Thm 4.3). Rather than hiding the isometry, the paper leverages it transparently as the foundation for all derivations, and further shows that PV gyro operations can be expressed via Riemannian operators (Thm 4.4).

- **Convincing numerical stability evidence across three complementary probes (Section 6.1, Tables 1–3):** Table 1 shows PV maintains zero failure rates up to r=1000 in FP32 while the hyperboloid fails at r=20. Table 2 shows PV round-trip error (2.1×10⁻⁷ in FP32) is four orders of magnitude better than Poincaré (2.1×10⁻⁴). Table 3 demonstrates PV gradients stay in [1.1×10⁻⁴, 2.1×10⁻⁶] while Poincaré gradients vanish to [1.1×10⁻¹¹, 7.6×10⁻¹³] and hyperboloid gradients explode to NaN.

- **Efficient, unconstrained PV MLR parameterization (Theorem 5.2, Eq. 19):** The reformulation collapses constrained hyperplane parameters (p_k, a_k) into unconstrained Euclidean parameters (z_k ∈ ℝ^n, r_k ∈ ℝ), avoiding Riemannian optimization. Eq. 19 expresses class scores through inner products ⟨x, z_k⟩, enabling efficient batched matrix multiplication rather than per-class gyroaddition. The Euclidean limit (K → 0⁻) is cleanly recovered.

- **Competitive or superior performance across diverse tasks (Tables 4, 5, 10):** PVNNs match or exceed Poincaré, hyperboloid, and Klein-model baselines on image classification (PV MLR achieves 95.30% on CIFAR-10, 78.20% on CIFAR-100), graph node classification (97.96% on Airport, 81.15% on Disease, 74.33% on PubMed), and genomic sequence learning (5–9 MCC point improvements over HCNN-S). The breadth of tasks and consistency of results provide strong evidence for practical utility.

- **Thorough ablation studies isolating design choices (Section 6.3, Tables 6–9):** The paper systematically ablates Riemannian vs. tangent-space FC and BN (Table 6), Fréchet iteration counts for GyroBN with timing data (Table 7), input lifting with/without Exp₀ (Table 8), and activation types (Table 9). These reveal nuanced insights — e.g., Riemannian FC provides large benefits on strongly hyperbolic graphs (Airport: 97.93% vs 86.99%) but not on weakly hyperbolic ones, and Fréchet-based GyroBN with 10 iterations achieves the best accuracy while tangent approximations offer 2× speedup.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Large performance gap on Airport warrants deeper investigation:** PVNN achieves 97.96% on Airport vs. 88.40% for the best Poincaré baseline (HNN++) — a 9.56% absolute gap. While the ablations (Tables 6–9) partially explore which design choices matter, a gap of this magnitude between isometric spaces is unusual and the paper does not fully isolate whether the gain comes from the PV coordinate chart, the specific PV FC layer formulation (Eq. 22 with sinh), or optimization dynamics. Running the Poincaré baselines with curvature tuning or showing the gap persists under matched hyperparameter budgets would strengthen confidence in this result.

- **No curvature sensitivity analysis:** All experiments use fixed curvature (K=-1 for stability, dataset-specific for downstream tasks). Whether PV's advantages are robust to curvature choice — or whether PV's benefits interact with specific curvature values — is unexplored. This limits confidence in the generality of the reported gains.

### Trivial

- **PV FC layer structurally differs from Poincaré FC beyond the manifold choice:** The PV FC formulation (Eq. 22, y_k = sinh(√(-K) v_k(x)) / √(-K)) is not a direct isometric transport of a Poincaré FC layer — it uses the PV MLR score v_k(x) in a specific sinh wrapping. While this is a legitimate design choice, the paper could acknowledge more explicitly that the comparison between PVNN and Poincaré baselines conflates the coordinate chart with a specific layer formulation.

## Nice-to-Haves
- A wall-clock time comparison of PV MLR vs. Poincaré MLR for practitioners evaluating the compute/accuracy tradeoff.
- Curvature sensitivity analysis across at least one downstream task.
- A discussion relating PV's unconstrained nature to optimization landscape properties, to explain why the coordinate change yields large empirical differences despite the isometry.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic Claim: "The isometry undermines the claimed contribution"** — REMOVED. The paper explicitly acknowledges and proves the isometry (Thm 4.2, lines 64-90) and uses it openly to derive all operators (lines 98-99: "By Thm. 4.2, we can readily obtain the counterparts on PV space via properties of isometries"). The paper never claims PV is a different geometry; it frames PV as an "alternative representation" and "new alternative" coordinate chart, which is accurate given that PV space is unconstrained while the Poincaré ball is bounded. The isometry is presented as a feature, not a liability — it is the mechanism by which operators are derived.

- **Harsh Critic Claim: "Numerical stability argument against Poincaré is overstated"** — REMOVED. The introduction's claim that Poincaré ball embeddings "might cause gradients to vanish" is directly supported by Table 3, showing Poincaré gradient magnitudes in [1.1×10⁻¹¹, 7.6×10⁻¹³] (vanishing) vs. PV's [1.1×10⁻⁴, 2.1×10⁻⁶]. The fact that Poincaré has 0% outright failure rate (Table 1) does not contradict the gradient-vanishing claim. The evidence is internally consistent: Poincaré does not produce NaN/Inf but does suffer from vanishing gradients at large radii.

- **Harsh Critic Claim: "Comparison unfairness — PV FC layer is structurally different"** — DEMOTED to Trivial. Different coordinate charts naturally enable different layer formulations; this is inherent to any comparison between hyperbolic models. The paper provides tangent-space variants (Table 6) as an additional comparison point.

- **Harsh Critic Claim: "The 'without Exp₀' phenomenon is under-discussed"** — REMOVED. The paper explicitly discusses this at lines 359-360: "This slight discrepancy may stem from the different nature of the inputs. In vision, the ResNet encoder can adapt its learned representation to the chosen lifting, whereas in graphs the raw node features benefit slightly from the explicit exponential map." The paper provides a reasonable hypothesis and evidence.

- **Harsh Critic Claim: "Computational cost is never discussed"** — PARTIALLY REMOVED. Table 7 does provide fit time in milliseconds per epoch for different GyroBN variants. A broader wall-clock comparison is moved to Nice-to-Haves.

- **Strength Finder: generic/superficial strengths** — REMOVED. Strengths about "addressing an important problem" or "targeting an interesting question" were filtered as not grounded in specific paper content.

## Novel Insights
The paper's most genuinely novel contribution is the efficient unconstrained reparameterization of the hyperbolic MLR (Thm 5.2, Eq. 19). By mapping constrained PV hyperplane parameters (p_k, a_k) to unconstrained (z_k, r_k) pairs, the authors obtain a closed-form score function v_k(x) that depends only on inner products ⟨x, z_k⟩ and the norm ‖x‖², enabling batched matrix multiplication while avoiding both Riemannian optimization and explicit gyroaddition. This is not a simple transport of Poincaré MLR via the isometry — it is an architectural insight specific to the PV coordinate chart that has genuine practical value. The reviewer inputs do not surface any additional novel insight beyond this.

## Suggestions

- Add a brief discussion acknowledging that PV and Poincaré are isometric, and therefore performance differences must arise from optimization dynamics, numerical precision, or specific layer formulations — this would preempt reader skepticism and strengthen the paper's framing.
- For the Airport graph result, consider running the Poincaré baselines with curvature tuning or showing that the gap persists under matched hyperparameter budgets. Alternatively, a controlled experiment mapping a Poincaré network through the isometry to produce functionally equivalent PV and Poincaré networks would isolate the numerical/optimization effect.
- Include curvature sensitivity analysis for at least one downstream task to establish robustness of the reported gains.

---

## Calibration Anchor Summary

| Paper | Score | Round | Comparison |
|---|---|---|---|
| ekz1hN5QNh (Fully Hyperbolic CNN) | 6.00 | R1/R2 | Similar contribution type; PVNN has more tasks, bigger gains, more thorough ablations → PVNN stronger |
| bwOndfohRK (Symmetric Spaces NN) | 6.00 | R1/R2 | More general but more abstract; PVNN more concrete with better experiments → PVNN comparable/slightly stronger |
| 30aSE3FB3L (Matrix Manifold NN++) | 5.67 | R2 | Similar structure but weaker experiments and mixed reviews → PVNN clearly stronger |
| 83le3arfeA (Balanced Hyperbolic OOD) | 5.50 | R1 | Fundamental methodological concerns with norm loss → PVNN clearly stronger |
| skGSOcrIj7 (Neural Spacetimes) | 6.80 | R2 | More theoretical novelty (learnable geometry, universal embedding theorem) → PVNN slightly below |
| OTMPdMH9JL (Neural Eigenfunctions) | 6.50 | R2 | Comparable quality; PVNN has more complete experimental validation → comparable |

**Round 1 bracket: 5.5–7.0. Round 2 narrowed to 6.0–6.5. Final score: 6.5 (Accept).**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>