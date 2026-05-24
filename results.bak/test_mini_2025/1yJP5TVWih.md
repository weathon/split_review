## Summary

This paper extends the study of rank collapse from transformers to State Space Models (SSMs) using a unifying framework that captures both architectures. It introduces *lambda-skip connections* — a parametrized version of the standard skip connection with a scalar λ — and provides a sufficient condition (Theorem 4.1) under which rank collapse is prevented in the finite-layer regime. The theoretical analysis covers transformers, LTI SSMs, and selective SSMs. The paper also studies necessity via theoretical results showing rank collapse occurs when skip connections are ablated, provides analytical examples, and presents experiments on pre-trained Mamba-2 and Albert models.

## Strengths

- **First theoretical extension of rank collapse analysis to SSMs.** The paper unifies transformers and SSMs under a common framework (Equation 6) and provides rank collapse bounds for LTI SSMs (Theorem 4.1) and selective SSMs (Theorem 4.3) that were not studied in prior work focused only on transformers (Dong et al. 2023; Wu et al. 2024a). This is a clear and original contribution.

- **Architecture-independent sufficient condition for rank collapse prevention.** Theorem 4.1 gives an explicit condition on λ (Equation 7: λ² > a(SC_M + |λ|)²) that guarantees μ(Y^(K))² ≥ a^K μ(Y^(0))² for any model fitting the general form of Equation 6. The condition is not architecture-specific and applies to transformers, LTI SSMs, and selective SSMs alike. Remark 4.1 shows that for Mamba (where S=1), a can be chosen very close to 1, giving near-constant rank collapse measure over 64 layers.

- **Analytical examples and tightness result.** Proposition 4.3.1 constructs a concrete 2-token selective SSM where rank collapse occurs for λ > -3/2 but is avoided for λ < -3/2. Proposition 4.3.2 shows the lower bound cannot be improved without further assumptions, demonstrating tightness. These examples provide useful insight into the role of λ.

- **Empirical observation of the predicted pattern.** Figures 1-2 show that varying λ in a pre-trained Mamba-2 and in Albert changes the rank collapse measure in a manner consistent with the theory: small |λ| yields near-zero μ, while large |λ| produces stable non-zero values. The Albert experiment (Figure 2) is cleaner since it is a transformer without gating, and corroborates the theoretical prediction.

## Weaknesses

### Major

- **Experimental methodology limits the strength of empirical conclusions.** Figures 1 and 3 use a pre-trained Mamba-2 model: the gating mechanism is removed (or retained) and λ is changed at *inference time*, then rank collapse is measured on a forward pass. Because the weights were optimized with gating mechanisms present, removing gating creates an architecture the model was never trained for. The observed rank collapse could partly reflect a weight-architecture mismatch rather than a fundamental property of the ablated architecture. This concern is most acute for the gating analysis (Figure 3), where the claim that "gating mechanisms play a crucial role in preventing rank collapse" would require training models from scratch with and without gating to be fully substantiated. While the forward-pass test of Theorem 4.1 is mathematically valid on any weight set regardless of provenance, the paper's empirical claims about architectural design principles would be stronger with controlled training experiments.

- **Disconnect between the sufficient condition and its verification in practice.** The sufficient condition (Theorem 4.1) depends on constants C_M and S (suprema of Frobenius norms of M and C_V matrices). The paper provides estimates (footnote 2: C_M = √N for transformers, lower bounds for SSMs) but does not actually compute or bound these constants for the specific models used in experiments. Without this, it is unknown whether the λ values that work empirically satisfy the theoretical condition. Remark 4.1 partially addresses this for Mamba (S=1), but the gap between theory and empirical observation remains.

### Minor

- **Table 1 lacks error bars and multiple-seed information.** The comparison between λ=1 and variable λ across four architectures on two tasks reports single accuracy numbers without standard deviations or confidence intervals. Given the small differences between conditions (e.g., 32.64 vs 32.85 for Transformer on LRA Image), it is unclear whether these differences are meaningful. The Figures 1-3 do include shaded standard deviations, making the omission in Table 1 noticeable.

- **The paper does not report what λ values are actually learned.** When λ is treated as a trainable parameter, the paper reports only accuracy (Table 1) but not the learned λ values per layer. If λ grows large during training, that would support the theory; if it stays near 1, the practical benefit is unclear. Reporting these values would significantly strengthen the connection between theory and experiment.

### Trivial

- The section title "Necessary to Prevent Rank Collapse?" (Section 4.2) is somewhat misleading. The paper explicitly states on line 162 that it does *not* provide a formal necessary condition, but explores the idea via ablation results and examples. The title could be more precise (e.g., "On the Necessity of Lambda-Skip Connections").

## Nice-to-Haves

- Training models from scratch with different fixed λ values and gating configurations, then measuring rank collapse during/after training, would substantially strengthen the empirical validation.
- Computing (or upper-bounding) C_M and S for the specific Mamba-2 model used in experiments and verifying whether the λ values in Figure 1 satisfy Theorem 4.1 would anchor the theory to the empirics.
- Reporting computational cost of learning λ (claimed to be minimal but not measured).

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The experiments are structurally invalid / fatal flaw"** — The harsh critic describes the experimental methodology as fatally flawed. This overstates the issue: the theory being tested (Theorem 4.1) is about forward-pass dynamics, and the experiment directly tests those dynamics. The weights, though trained with gating, still define a valid forward pass of the form in Equation 6. The concern is real but not fatal.

- **"Proof sketch too brief" / "Proofs deferred to appendix"** — This is standard practice at ICLR; many papers present proof sketches in the main text with full proofs deferred. Removed per instructions (appendix content is stripped by the parser).

- **"Necessity analysis disconnected from experiments"** — Section 4.2 is a theoretical section, not an experimental one. The experiments in Section 5 do test the effect of λ on rank collapse and are connected to the theory. The criticism conflates theory and experiments.

- **"Missing related works"** — Removed per instructions (cannot confirm existence of omitted references).

- **Various formatting/style nitpicks and typo claims** — These are parser artifacts, not author errors. Removed per instructions.

- **"Missing appendix content, missing proofs"** — The appendix is stripped by the PDF parser; the original submission has these sections. Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The synthesis of the harsh critic and strength finder does not reveal a genuinely novel observation that the paper itself does not already articulate. The key insight — that rank collapse can be provably prevented by choosing λ sufficiently large, formalized in an architecture-independent sufficient condition — is the paper's own contribution.

## Suggestions

1. **Conduct controlled training experiments** for the gating ablation (Figure 3): train Mamba models from scratch with and without gating, measure rank collapse at convergence. This would resolve the primary methodological concern.
2. **Report learned λ values** for the variable-λ experiments in Table 1, along with error bars from multiple random seeds.
3. **Anchor the theory to practice** by computing upper bounds on C_M and S for the specific models used, and verifying whether the λ values in Figure 1 satisfy the condition in Theorem 4.1.

## Score and Decision

**Calibration anchors retrieved:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| In-context Convergence of Transformers | kxpswbhr1r.md | 5.75 | 1 | Reject (6,6,5,6). Paper is stronger — this anchor had no experiments and simplified settings; this paper has a cleaner theoretical contribution. |
| SSM Generalization | EGjvMcKrrl.md | 6.00 | 2 | Reject (6,6,6). Paper is slightly stronger — cleaner theory, more novel direction. Both have some disconnect between theory and experiments. |
| Simplicity Bias via Sharpness | CQF8mTF7qx.md | 6.00 | 2 | Reject (5,8,5,6). Comparable tier — both have genuine theoretical contributions with limiting assumptions/experimental gaps. |
| HOPE for SSMs | RZwtbg3qYD.md | 6.60 | 2 | Accept Poster (6,6,8,8,5). Paper is weaker — HOPE had stronger experimental validation and tighter theory-practice connection. |
| CoT + Sample Efficiency | AmEgWDhmTr.md | 7.00 | 1 | Accept Poster (6,6,8,8). Paper is weaker — this anchor had stronger empirical support and clearer practical implications. |
| Mean-field Transformer Clustering | eBS3dQQ8GV.md | 7.80 | 1 | Accept Oral (8,5,10,8,8). Paper is much weaker on theoretical depth and rigor. |

**Round 1 bracket:** [5.0, 6.5]

**Narrowing:** Compared to the 5.75-6.00 anchors (all rejected), the paper is comparably situated: a genuine theoretical contribution undermined by limitations in experimental validation and theory-practice connection. It is not as strong as the accepted poster papers at 6.5-7.0 where the empirical support was more solid.

The paper's primary weakness is that its central experimental evidence (Figures 1-3) uses pre-trained models with architectural modifications at inference time, which limits the strength of claims about architectural design principles. For a paper submitted to the learning theory track, the theoretical contribution is solid enough to be near the borderline, but the empirical validation falls short of what would confidently support acceptance.

Given the novel theoretical contribution (first extension of rank collapse to SSMs, general sufficient condition) tempered by significant experimental methodology concerns and a gap between theory and practice, the paper is best described as borderline.

**Final score:** 5.5 — marginally below the acceptance threshold.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>