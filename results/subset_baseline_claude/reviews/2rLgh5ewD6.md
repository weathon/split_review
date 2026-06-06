## Summary
This paper proposes an Adaptive Correction Mechanism for neural operators that enforces exact conservation laws (linear and quadratic) by appending a lightweight learnable correction operator to the model output. For linear conservation laws, the correction redistributes the conservation discrepancy via a softmax-parameterized vector **A**; for quadratic laws, it applies a rescaling and additive correction in closed form. The method is evaluated on three architectures (UNet, GTNO, FNO) across six PDE benchmarks, consistently achieving exact conservation at machine precision while also improving prediction accuracy over baselines and competing methods (loss-based and projection-based).

---

## Strengths
- **Architecture-agnostic and lightweight design**: The correction module plugs into any neural operator without altering its internal structure, adding only a small convolutional layer or MLP. This makes the method highly practical for the community.
- **Exact conservation at machine precision**: Table 3 shows conservation error of 0.00±0.0 for both mass and norm conservation across all equations—something neither loss-based nor projection-based approaches consistently achieve while also improving accuracy.
- **Consistent accuracy improvement across all 18 architecture–PDE combinations**: Table 1 shows monotone improvement for all baselines; this breadth of consistent improvement is compelling evidence the method works across settings, not just on carefully selected cases.
- **Informative ablation (Table 5)**: FNO* (same MLP appended without conservation) does not improve and sometimes hurts accuracy, isolating the gain to the conservation-aware structure of the correction rather than added capacity. For LSE, FNO* degrades from 0.38% to 1.61% error, while the proposed method achieves 0.32%.
- **Well-motivated comparison with competing approaches**: The paper clearly shows loss-based methods are sensitive to λ (Table 4), that the best λ for one PDE does not transfer (Table 2), and that the projection method can severely degrade accuracy (CAC: 2.01 → 99.7%).

---

## Weaknesses

### Fatal
None.

### Major
1. **Multi-step autoregressive evaluation is only qualitative**: The motivation in the introduction (Section 1) prominently cites long-term stability and error accumulation as key problems. Figures 1 and 2 show qualitative stability improvements, but there is no quantitative table reporting multi-step rollout error. The primary results (Tables 1–5) are all single-step. This is a significant gap: a method claiming to improve long-term stability should demonstrate it with quantitative multi-step metrics.

2. **Design choices in quadratic correction are not adequately justified**: The simplification in Section 3.2 (choosing λ₁ such that λ₁²S_{U²} = c₀) is introduced to "ensure guaranteed feasibility," but the paper does not discuss its effect on expressivity. With this choice, **U**_new = √(c₀/S_{U²}) **U** − (2S_UA/S_{A²}) **A**, meaning the neural operator output is globally rescaled before the additive correction is applied. If the base model's output norm deviates significantly from c₀, this rescaling may severely distort spatial structure before the learned **A** can compensate. There is no analysis of when this simplification is restrictive and no ablation comparing the general-formula version (Eq. 16) against the simplified one.

3. **Loss-based comparison uses a suboptimal λ for non-TE equations**: λ is tuned on TE and then applied to CAC, SWE, LSE, and NSE without re-tuning. This makes the comparison unfair—the projection method and the proposed method are both PDE-agnostic, but the loss-based baseline is artificially handicapped. A fair comparison would use the best λ per PDE for the loss-based method.

### Minor
1. **Single conservation law limitation is acknowledged but not assessed empirically**: For SWE, both mass and momentum are conserved; the paper only enforces mass. No experiment tests whether ignoring momentum conservation affects stability in SWE specifically.
2. **The theoretical guarantee (Theorem 1) is formal but limited**: It compares the proposed approach (unconstrained training on the corrected model) against hard-constrained training with λ=∞ on the original model, showing the former cannot do worse. This is fairly straightforward since the corrected model's feasible set includes any model satisfying the constraint exactly, making the argument nearly tautological. The remark about it replacing λ=∞ soft training is valuable, but the theorem does not provide quantitative bounds on the improvement.
3. **FNO improvements are sometimes modest**: On TE (mass), the improvement is 8.29 → 8.04% (3% relative), which—while consistent—is small. The significant gains on CAC (2.01 → 1.65%) and SWE (2.57 → 2.32%) are more convincing.

### Trivial
None that affect the evaluation.

---

## Nice-to-Haves
- Quantitative multi-step rollout tables (e.g., error at 5Δt and 10Δt) to substantiate the stability claims.
- A discussion or small experiment showing the magnitude of the correction term |(m₀ - M(**U**))**A**| relative to **U** across different PDEs, to understand when the correction is large vs. small and what that implies for accuracy.
- Extension to enforcing two conservation laws simultaneously (e.g., mass + momentum for SWE) would substantially broaden the practical applicability.

---

## Novel Insights
The key insight is that enforcing conservation exactly can be framed as a learnable "distribution" problem: instead of choosing *where* to absorb the conservation discrepancy (as fixed post-processing does), the correction learns input-dependent allocation coefficients **A** that minimize downstream loss. This separates the *what* (exact conservation) from the *where* (learned adaptively), a conceptually clean decomposition that generalizes both the simple constant-adjustment method (Geng et al., 2024) and the projection method. The demonstration that exact conservation enforcement is compatible with—and can actively facilitate—lower reconstruction error (rather than trading off against it) is a practically important message for the neural-operator community.

---

## Suggestions
- Add a quantitative multi-step rollout comparison (at least for FNO on LSE and NSE where stability claims are most dramatic) to make the stability argument rigorous.
- Justify or ablate the specific simplification λ₁²S_{U²}=c₀ in the quadratic case; even a brief comparison on one PDE against using the general closed-form expression in Eq. 16 would strengthen confidence in the design.
- Re-run the loss-based comparison using the per-PDE best λ to make the comparison fair and to strengthen the paper's argument that it is not just easier to tune than loss-based approaches, but fundamentally better.
- Include a brief discussion or figure showing how large the correction term is in practice and whether larger corrections correlate with larger accuracy improvements, which would further illuminate why the method works.

---

## Score and Decision
The paper addresses a well-motivated problem with a clean, practical, and architecture-agnostic solution. The method is technically sound, enforces exact conservation, and demonstrates consistent improvement across a wide experimental grid. The main limitation—that multi-step evaluation is only qualitative—is significant given the motivation, and the loss-based comparison is not fully fair. These are addressable concerns rather than fundamental flaws. Within its class (method paper for PDE learning), this is a solid contribution.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>