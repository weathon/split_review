Now I have enough information to draft the review. Let me compile it before calling `draft_review`.Now for calibration. Round 1 — bracketing.Let me read the most topically relevant anchors for comparison.**Initial bracket: 5.0–7.0**

The paper is clearly better than the 4.0 anchor (gz8Rr1iuDK — weak baselines, misleading messaging) and at least comparable to the 5.0 anchor (KEpR8hFzvO — broader scope but sparser experiments, missing related works). Now narrowing within the bracket.

**Round 2 — narrowing within [5.0, 7.0]:**Now I have enough anchors for scoring. Let me compare:

- **KEpR8hFzvO (5.0, Reject)** — topically most similar (conservation-encoding NOs). Rejected for missing related works, sparse experiments, limited architecture applicability. Our paper is meaningfully better: handles both linear + quadratic, architecture-agnostic, has proper ablation, and cleaner derivations. But our paper also has a comparable gap (missing Geng et al. constant adjustment baseline).

- **stcN89QGfL (5.67, Reject)** — PDE-constrained network with multi-time-stepping. Similar quality tier, more ambitious but more overextended.

- **jqVj8vCQsT (5.60, Accept)** — Learning a neural solver for parametric PDEs. Accepted, similar scope and clarity to the paper under review.

**Final bracket: 5.5–6.5.** The paper is clearly above the 5.0 reject anchor but the missing Geng et al. comparison baseline (which directly bears on the core novelty claim for the linear case) and the overclaimed abstract are real issues that put a ceiling below a strong accept (7+). The quadratic conservation contribution is genuinely novel and the stability evidence is compelling. I settle on **6.0**.

---

## Summary
This paper proposes an adaptive correction mechanism for neural operators that enforces conservation laws exactly at inference time. For linear conservation laws (mass, momentum), a softmax-parameterized correction vector redistributes the conservation deficit across grid points in a learnable, input-dependent way—generalizing the static constant-adjustment of Geng et al. (2024). For quadratic conservation laws (norm, energy), a novel closed-form rescaling enforces exact norm preservation while remaining end-to-end differentiable. The method is architecture-agnostic, applied to UNet, GTNO, and FNO across six PDE benchmarks, demonstrating exact conservation at machine precision and compelling long-term stability improvements.

## Strengths
- **Learnable, input-dependent distribution of the conservation deficit**: Equation (8) introduces a softmax-parameterized vector **A** that adapts to each input, directly contrasted with prior static post-processing in Section 2. The ablation (Table 5) confirms that the conservation structure—not just the extra parameters—drives improvement: FNO* (unconstrained MLP appended) worsens performance on several tasks (LSE: 0.38% → 1.61%) while "Ours" reduces it (0.32%).
- **Closed-form quadratic conservation operator**: Equations (11)–(17) derive a differentiable, closed-form norm-preserving rescaling via the ansatz **U**_new = λ₁**U** + λ₂**A**. This extends conservation enforcement to quadratic laws where prior architectural methods (Liu et al., 2023a; Richter-Powell et al., 2022) explicitly cannot apply.
- **Compelling multi-step stability evidence**: Figures 1–2 show that ten-step autoregressive rollout of standard FNO diverges with large oscillations (NSE), while FNO with adaptive correction remains closely aligned with the true solution. This is the most persuasive demonstration in the paper and directly supports the claimed stability benefit.
- **Exact conservation at machine precision**: Table 3 reports 0.00 ± 0.0 conservation error for the proposed method on all six equations, directly demonstrating exact constraint satisfaction.
- **Lightweight and architecture-agnostic**: A single convolutional layer (UNet/GTNO) or three-layer MLP (FNO) is sufficient, preserving the original architecture without modification and enabling easy integration.

## Weaknesses

### Fatal
None.

### Major
- **Missing Geng et al. (2024) constant adjustment baseline**: The linear correction in Equation (8) is explicitly a generalization of Geng et al.'s constant adjustment (which fixes **A** = 1/N uniformly). Section 2 states: "the constant adjustment method works by computing the mass discrepancy…and adds it to the latter." Yet Tables 2 and 3 compare only "Loss," "Projection," and "Ours"—never constant adjustment. Since the sole novelty of the linear case over Geng et al. is the learnable **A**, omitting this baseline leaves the central linear-case claim—that *learning* the correction distribution is beneficial—undemonstrated. The ablation in Table 5 (FNO* vs. Ours) isolates conservation structure vs. extra parameters but does not isolate *learnable* vs. *fixed-uniform* distribution.

### Minor
- **Unexplained catastrophic projection failure on Conservative Allen-Cahn (Table 2)**: The projection method achieves errors of 8.14e-2 (TE), 3.01e-3 (SWE), and 3.52e-2 (NSE), but collapses to 99.7e-2 on CAC—a ~50× degradation relative to the baseline FNO (2.01e-2). Section 4.3 acknowledges the failure ("significantly increases it") but provides no mechanistic explanation. Since CAC enforces a linear mass conservation law (Eq. 21), the projection should solve a linear-constrained problem and not face qualitatively different difficulty. Without an explanation, it is unclear whether this reflects a principled limitation of projection or a numerical failure specific to the solver used for CAC, which would limit the interpretability of this comparison.
- **Abstract overclaims accuracy significance**: The abstract states the method "significantly improves both accuracy and stability." The stability claim is well-supported by Figures 1–2. However, several one-step accuracy improvements in Table 1 fall within overlapping uncertainty bands: UNet on CAC (1.48±0.08 vs. 1.42±0.14e-2), GTNO on TE (9.11±0.76 vs. 8.15±0.87e-2). The word "significantly" should be qualified or restricted to the multi-step stability setting, where the evidence is compelling.
- **Theorem 1 is of limited depth**: The theorem proves that the adaptive correction network achieves reconstruction loss ≤ the hard-constrained network (infinite-penalty). This is essentially a consequence of the corrected architecture's hypothesis class being at least as large: any conserving output reachable under hard-constraint training is also reachable by the corrected architecture (by construction). The result is formally correct but nearly immediate from a hypothesis-class argument and does not illuminate finite-parameter behavior, gradient dynamics, or the benefit of learning **A** vs. fixing it uniformly. Remark 1 attempts to connect this to soft-penalty λ→∞, but the theorem is stated only for hard constraints—the connection is informal.

### Trivial
- The value of ε in Equation (17) is described only as "a small constant added for numerical stability." Stating the actual value used (presumably ~1e-8 or machine epsilon) would complete the implementation description, especially since Table 3 reports exactly 0.00 conservation error.

## Nice-to-Haves
- A quantified multi-step error growth curve (error vs. prediction step count) across all six PDEs would sharpen the stability argument beyond the qualitative demonstration in Figures 1–2.
- A direct quantitative comparison between "constant adjustment" (Geng et al., 2024) and "Ours" in Tables 2 and 3 would be the single most impactful addition, demonstrating the value of learning the distribution of correction for the linear case.
- Per-equation λ sensitivity for the loss-based baseline would show whether the proposed method surpasses loss-based methods even under favorable tuning conditions.
- The quadratic correction (Eq. 17) fixes λ₁ = √(c₀/S_{U²}), leaving only the direction of **A** as the learnable degree of freedom. A brief discussion of whether this restricts expressiveness—and whether relaxing this assumption (treating λ₁ as a free learnable scalar) would improve performance—would strengthen Section 3.2.

## Removed Points
*These points are flagged to be removed; treat them with caution:*

- **Harsh Critic: FNO* worse than FNO baseline indicates implementation problem** — FNO* worsening performance (e.g., CAC: 2.01 → 2.23) is fully consistent with the paper's intended narrative that adding parameters without conservation structure can hurt. This is not an implementation error. REMOVED as strawman.
- **Strength Finder: "No baseline improves on all tasks"** — While directionally true from Table 1, this phrasing is vacuous as a strength; several improvements are within uncertainty bounds. REMOVED as overclaimed.
- **Strength Finder: "Theorem 1 provides formal guarantee of lower reconstruction loss"** — The theorem is correct but shallow (see Minor weakness). The strength as stated conflicts with the verified weakness. REMOVED; the Minor weakness stands.
- **Harsh Critic: the $\epsilon$ terms in Eq. 17 break exact conservation** — Exact conservation is preserved up to machine epsilon by construction given the fixed-λ₁ simplification. The 0.00 entries in Table 3 are consistent with this. The concern that ε could be 1e-6 is speculative. DEMOTED to Trivial (specify the value).

## Novel Insights
The paper's most useful contribution is reframing the "where to correct" question as a learnable, input-dependent inference problem: rather than uniformly distributing the conservation deficit (Geng et al.) or solving an iterative projection (Cardoso-Bihlo & Bihlo), the correction direction **A** is learned from data. This framing cleanly unifies the linear and quadratic cases, and the empirical result that the ablation FNO* (extra parameters without conservation structure) consistently underperforms "Ours" (Table 5) provides direct evidence that it is the *direction* of learned correction—not the extra capacity—that matters. The closed-form quadratic rescaling is particularly elegant: by fixing the magnitude of the neural operator output (λ₁ = √(c₀/S_{U²})) and adjusting only the learned component, it achieves exact norm conservation without any iterative solver.

## Suggestions
1. Add Geng et al.'s constant adjustment as a direct baseline in Tables 2 and 3. This is the most impactful single addition.
2. Explain mechanistically why the projection method fails catastrophically on CAC while succeeding on all other equations.
3. Qualify "significantly improves accuracy" in the abstract, distinguishing marginal single-step gains from compelling multi-step stability improvements.
4. State the concrete value of ε used in Equation (17).
5. Add a brief theoretical/empirical discussion of the expressiveness restriction in the quadratic case (λ₁ fixed by the neural operator output).

---

## Score and Decision

**Anchor papers retrieved:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| KEpR8hFzvO.md | 5.00 (Reject) | R1 | Most topically similar (conservation-encoding NOs); our paper is better: handles quadratic, architecture-agnostic, cleaner ablation |
| gz8Rr1iuDK.md | 4.00 (Reject) | R1 | Symmetric/physical constraints for PDE integration; weaker on methodology, baselines, presentation |
| 5KqveQdXiZ.md | 5.25 (Accept) | R1 | Constrained learning for PDEs; comparable in scope |
| vAuodZOQEZ.md | 6.50 (Accept) | R1 | Physics-informed neural predictor for fluids; more domain-specific |
| H8CtXin7mZ.md | 5.25 (Reject) | R2 | Neural-preconditioned Poisson solver; less topically relevant |
| stcN89QGfL.md | 5.67 (Reject) | R2 | PDE-constrained multi-time-stepping network; comparable tier |
| jqVj8vCQsT.md | 5.60 (Accept) | R2 | Learning a neural solver for parametric PDEs; comparable scope and clarity |
| Wo66GEFnXd.md | 6.75 (Reject) | R2 | Time-dependent DFT with physics awareness; higher-complexity contribution |
| kpq3IIjUD3.md | 7.33 (Accept) | R2 | Equivariant quantum operators; different topic, stronger theoretical grounding |
| WhZoCLRWYJ.md | 6.80 (Accept) | R2 | Light Schrödinger Bridge; different topic |

**Round 1 bracket**: 5.0–7.0 (paper clearly above 4.0 reject anchors; well below 7.5+ strong anchors).

**Round 2 narrowing**: The paper compares favorably to the 5.0 reject anchor (KEpR8hFzvO) and comparably to the ~5.25–5.67 tier. Its quadratic conservation novelty and multi-architecture/multi-PDE coverage push it above the 5.0-5.25 tier. The missing Geng et al. baseline (major gap for the central linear-case claim) and limited theorem depth prevent a 6.5+ score. The paper is comparable to jqVj8vCQsT (5.60 Accept) and stcN89QGfL (5.67 Reject) but with more polished presentation, better ablation, and a broader conservation coverage. The nice-to-haves (quantified multi-step stability, missing baseline) would not be difficult to address but are currently absent. **Final score: 6.0**, reflecting a borderline accept: the method is sound, novel for the quadratic case, and well-evaluated except for the missing closest baseline.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>