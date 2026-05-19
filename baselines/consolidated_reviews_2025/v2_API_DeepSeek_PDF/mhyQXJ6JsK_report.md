## Summary
# Final Review Report

## Summary

This paper introduces the **Gaunt Tensor Product**, a method to accelerate the computation of tensor products of irreducible representations (irreps) used in E(3)-equivariant neural networks. The key technical insight is a mathematical connection between Clebsch-Gordan coefficients and Gaunt coefficients (integrals of triple spherical harmonics), which reveals that the tensor product of irreps is equivalent to multiplication between spherical functions. By changing basis from spherical harmonics to a 2D Fourier basis, multiplication becomes a 2D convolution that can be efficiently computed using Fast Fourier Transforms, reducing the complexity from O(L^6) to O(L^3). The authors demonstrate the method across three operation classes (Equivariant Feature Interactions, Convolutions, and Many-body Interactions) and validate on OC20 and 3BPA benchmarks, achieving up to ~43.7× speedup with competitive accuracy.

**Overall assessment:** The paper presents a mathematically elegant and practically useful algorithmic improvement. The theoretical derivation (Wigner-Eckart theorem → Gaunt coefficients → spherical function multiplication → FFT acceleration) is sound and well-structured. The main technical contribution—the O(L^6)→O(L^3) complexity reduction—is clearly motivated and demonstrated empirically. Key weaknesses include: (1) a missing ablation control between Gaunt parameterization and architectural change in the OC20 experiment, (2) unacknowledged OOD accuracy degradation in the 3BPA results that partially contradicts the method's claimed parity invariance, and (3) overly brief discussion of limitations in the conclusion. Novelty verification is deferred to manual literature comparison (Retrieval-Disabled Mode).

## Strengths
**S1. Mathematically rigorous and elegant derivation.** The paper provides a clean derivation connecting Clebsch-Gordan coefficients to Gaunt coefficients via the Wigner-Eckart theorem, establishing that tensor products of irreps are equivalent to spherical function multiplication. The mathematical presentation (Section 3.1-3.2) is self-contained, with key steps clearly shown in Equations (1)-(7). The reliance on established quantum mechanical identities adds credibility.

**S2. Clear asymptotic complexity improvement.** The O(L^6) → O(L^3) complexity reduction is well-motivated and analyzed step-by-step. The three-stage pipeline (SH→2DFFT, 2D convolution via FFT, 2DFFT→SH) is explained with per-stage complexity accounting. The empirical speedup results (Figure 1, Table 2) confirm the practical benefit: 43.7× vs e3nn and 82.3% memory reduction for the Many-body Interaction operation.

**S3. Generality across three operation classes.** The paper systematically maps the Gaunt Tensor Product to three widely-used equivariant operation classes (Feature Interactions, Convolutions, Many-body Interactions) with concrete integration examples (So3krates, eSCN, MACE). This demonstrates practical breadth beyond a single architecture.

**S4. Strong empirical validation on large-scale benchmarks.** OC20 (1.2M DFT relaxations) and 3BPA (with multiple OOD test sets) are challenging, real-world benchmarks. EquiformerV2 + Gaunt-Selfmix achieves the best reported EFwT (1.95) on OC20 2M, and MACE-Gaunt matches MACE's state-of-the-art 3BPA accuracy with dramatically lower memory (5.8% of e3nn's memory cost).

**S5. Excellent exposition of background material.** The Background section (Section 2) and extensive Appendix A provide a thorough tutorial on group theory, representation theory, and quantum mechanical angular momentum. This makes the paper accessible to readers with basic familiarity with equivariant networks.

## Weaknesses
**W1. Ablation confound in OC20 experiment (Major).** In the OC20 experiment (Page 9, Table 1), EquiformerV2 + Gaunt-Selfmix adds a new Selfmix feature interaction layer to each EquiformerV2 block. The baseline EquiformerV2 does not have this layer. The paper attributes the performance improvement (16.8% EFwT at L=6) to "our approach," but this conflates two factors: (a) the additional Selfmix operation providing more expressive feature mixing, and (b) the Gaunt coefficient parameterization itself. A matched control using CG-based Selfmix (at the same computational cost, if feasible) is needed to isolate the Gaunt parameterization's contribution. Without this, a skeptical reviewer could argue that any performance gain comes from increased model capacity, not the Gaunt formulation.

**W2. Unacknowledged OOD accuracy degradation in 3BPA (Major).** In Table 2 (Page 9), MACE-Gaunt shows systematic accuracy degradation on OOD test sets compared to standard MACE: Dihedral Slices Energy MAE 9.9 vs 7.8 (27% worse), 600K Energy MAE 10.6 vs 9.7 (9.3% worse), 1200K Force MAE 63.1 vs 62.0 (1.8% worse). The paper states "performs competitively" and the appendix claims parity exclusion "does not hurt performance," yet the data shows a clear OOD trade-off. This factual inconsistency undermines the defensive argument about Gaunt vs CG equivalence.

**W3. Introduction narrative too generic (Minor).** The first introduction paragraph (Page 1) opens with "The imposition of physical priors..." rather than establishing the paper's specific problem (tensor product computational bottleneck). The reader must wait until the third paragraph (Page 2) to learn about the O(L^6) challenge. This reduces the paper's hook and makes the contribution positioning less crisp.

**W4. Missing limitations section in Conclusion (Minor).** The Conclusion (Page 9) is only 5 sentences long and contains no explicit limitations paragraph. Key limitations—parity constraints, OOD trade-offs, asymptotic-only speedup guarantee, sampling grid assumptions—are not acknowledged. The absence of a limitations section reduces scientific completeness.

**W5. Underspecified constant in Gaunt-CG proportionality (Minor).** Equation (3) states the proportionality constant C̃^{(l)}_{(l1,l2)} as a function of l1, l2, l without explicit form or domain conditions. The parity constraint (l1+l2+l even) is only mentioned in Appendix A.6 (Page 20-21), not in the main text. This could mislead readers into thinking all (l1,l2,l) combinations are valid, when Gaunt coefficients impose stricter selection rules than CG coefficients.

## Key Issues
**Issue 1 (Major): Ablation confound—Gaunt-Selfmix vs CG-Selfmix control missing**
- **Evidence:** Page 9, OC20 experiment paragraph: "EquiformerV2 with our Gaunt Selfmix operation achieves better performance... 16.8% relative improvement on the EFwT metric with L=6."
- **Root cause:** The Gaunt Selfmix operation is added to each layer of EquiformerV2, but the baseline EquiformerV2 does not have any Selfmix operation. The performance gain could come from the additional operation itself (more parameters, more expressivity) rather than the Gaunt coefficient parameterization.
- **Impact:** The core claim "Gaunt Tensor Product achieves improved performance" is not causally separable from "adding a feature interaction layer improves performance."
- **Fix:** Add a matched control: EquiformerV2 + Selfmix using standard CG coefficients (or using the same architecture but with CG-based tensor products). If computational cost is prohibitive, add explicit caveat in the text.

**Issue 2 (Major): Parity constraint claim contradicts experimental data**
- **Evidence:** Page 21 (Appendix A.6): "Gaunt coefficients exclude pseudovectors from the output... this does not hurt performance." Page 9 (Table 2): MACE-Gaunt has 27% higher Dihedral Slices Energy MAE than MACE (9.9 vs 7.8).
- **Root cause:** The parity constraint from Gaunt coefficients (l1+l2+l even) excludes pseudovector outputs. The 3BPA OOD degradation suggests these pseudovector components may be important for long-range or OOD interactions, contradicting the claim of no performance impact.
- **Impact:** The defensive narrative about Gaunt-CG equivalence is factually incomplete. Readers may be misled about the method's generality across all equivariant settings.
- **Fix:** Replace the blanket statement with a nuanced discussion acknowledging the OOD trade-off and recommending task-specific validation.

**Issue 3 (Minor): Gaunt coefficient parity constraint not stated in main text**
- **Evidence:** Equation (3) on Page 4-5 defines the Gaunt-CG proportionality without stating the parity condition (l1+l2+l even).
- **Root cause:** The parity constraint is only mentioned in Appendix A.6 (Page 20-21). A reader who skips the appendix may assume all (l1,l2,l) combinations are supported.
- **Impact:** Potential confusion about the method's output space.
- **Fix:** Add one sentence after Equation (3) stating the parity condition explicitly.

## Actionable Suggestions
**Suggestion 1 (Must): Add matched ablation control for OC20 experiment**
- **Location:** Page 9, "OC20 S2EF performance" paragraph and Table 1.
- **Problem:** The Gaunt Selfmix operation adds a new feature interaction layer. Without a CG-based Selfmix control, the improvement cannot be attributed to the Gaunt parameterization.
- **Action:** Run EquiformerV2 + Selfmix using standard CG coefficients (or the same Selfmix architecture with standard tensor products) under identical training settings. Report results alongside the Gaunt-Selfmix results in Table 1.
- **Expected benefit:** Separates the architectural contribution (adding Selfmix) from the algorithmic contribution (Gaunt coefficients), strengthening the causal claim.
- **Fallback if expensive:** Add a clear caveat: "We note that the Gaunt Selfmix adds a feature interaction layer not present in the baseline; the improvement reflects the combined effect of architectural addition and Gaunt parameterization."

**Suggestion 2 (Must): Revise parity constraint discussion with OOD evidence**
- **Location:** Page 21 (Appendix A.6) and the Conclusion (Page 9).
- **Problem:** The claim that parity exclusion "does not hurt performance" is contradicted by MACE-Gaunt's OOD degradation (Table 2).
- **Action:** (a) Replace the sentence "this does not hurt performance" with a nuanced paragraph acknowledging the in-distribution vs OOD trade-off. (b) Add a one-sentence limitation in the Conclusion: "A limitation is that Gaunt coefficients exclude pseudovector outputs, which may affect OOD tasks as seen in the 3BPA results." (c) In the 3BPA results paragraph, add an explicit sentence: "MACE-Gaunt shows slightly higher OOD errors on dihedral slices (9.9 vs 7.8 Energy MAE), suggesting a trade-off between efficiency and OOD robustness that warrants further investigation."
- **Expected benefit:** Resolves a factual inconsistency, improves scientific transparency, and preempts reviewer criticism.

**Suggestion 3 (Nice-to-have): Tighten introduction narrative**
- **Location:** Page 1, first two introduction paragraphs.
- **Problem:** Opening paragraph is generic ("physical priors... curse of dimensionality..."). The core problem (O(L^6) tensor product cost) is not mentioned until the third paragraph.
- **Action:** Restructure the introduction as: (P1) The tensor product of irreps is the key equivariant operation, but suffers O(L^6) cost, limiting L to 2-3. (P2) This bottleneck has been widely acknowledged; higher L consistently improves accuracy. (P3) Our solution using Gaunt coefficients + FFT reduces to O(L^3). (P4) Contributions summary.
- **Mentor Revised Version (Paragraph 1):**
  "A core operation in Euclidean-equivariant neural networks is the tensor product of irreducible representations (irreps), which enables precise 3D symmetry modeling for molecular, protein, and point-cloud tasks. However, computing the full tensor product up to degree L requires O(L^6) operations, limiting L to 2 or 3 in practice. This restricts model capacity, as higher-degree representations have been shown to consistently improve accuracy across state-of-the-art architectures."

**Suggestion 4 (Nice-to-have): Add limitations subsection to Conclusion**
- **Location:** Page 9, Section 5 (Conclusion).
- **Problem:** No limitations are discussed. The conclusion is too brief and promotional.
- **Action:** Add a 2-3 sentence limitations paragraph after the main summary:
  "Limitations. Gaunt coefficients impose stricter parity constraints than Clebsch-Gordan coefficients, excluding pseudovector outputs. While this preserves in-distribution accuracy, OOD generalization may be affected (as observed on 3BPA dihedral slices). Additionally, the O(L^3) complexity applies to full tensor products; the speedup for sparse path selections depends on the number of active paths."
- **Expected benefit:** Significantly improves scientific completeness and reviewer perception.

**Suggestion 5 (Nice-to-have): Disclose the parity selection rule in the main text**
- **Location:** Page 4-5, after Equation (3).
- **Problem:** The parity constraint (l1+l2+l even) is not stated alongside the Gaunt coefficient definition.
- **Action:** Add: "Note that Gaunt coefficients are non-zero only when l1+l2+l is even (parity conservation). This imposes stricter selection rules than CG coefficients, which only enforce the triangle inequality |l1-l2| ≤ l ≤ l1+l2."
- **Expected benefit:** Provides complete methodological disclosure in the main text.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction (Page 1-2) follows this structure:
1. Physical priors and equivariance are important.
2. Tensor products of irreps are the dominant approach and have universal approximation.
3. However, O(L^6) complexity limits L to 2-3, creating a need for efficiency.
4. We propose Gaunt Tensor Product with O(L^3) complexity.
5. It generalizes to three operation classes.
6. Experiments show efficiency and performance gains.

**Problem Alignment Check:** The stated challenge (O(L^6) cost) matches the proposed solution (O(L^3) via FFT). ✓
**Variable Alignment Check:** Core concepts (Clebsch-Gordan, Gaunt coefficients, 2D Fourier basis) appear as key method variables. ✓
**Contribution-Evidence Alignment Check:** The claimed O(L^3) speedup and competitive accuracy are supported by efficiency benchmarks and two real-world datasets. Partial ✓ (OC20 ablation confound is the main gap).

### Recommended Storyline (Target for Revision)

A stronger narrative arc would be:

1. **P1 (Hook):** "Among E(3)-equivariant architectures, tensor products of irreps via Clebsch-Gordan coefficients are the dominant operation—but their O(L^6) cost limits L to 2-3, capping accuracy improvements that higher-degree representations could enable."

2. **P2 (Gap):** "Prior work has acknowledged this bottleneck and developed sparse approximations (eSCN, MACE), but each sacrifices generality—eSCN restricts to convolutions, MACE uses specialized many-body patterns. A generally applicable acceleration is needed."

3. **P3 (Idea):** "We show that the CG tensor product is mathematically equivalent to multiplication of spherical functions via Gaunt coefficients. Changing basis to a 2D Fourier basis turns this into a 2D convolution, which can be accelerated from O(L^6) to O(L^3) using FFT."

4. **P4 (Scope):** "This Gaunt Tensor Product applies to three broad operation classes: feature interactions, convolutions, and many-body interactions."

5. **P5 (Contributions):** Three specific contributions. Then transition to experiments.

### Abstract Outline (Complete)

The abstract should follow a compact 5-sentence structure:

**S1 (Problem + Domain):** "E(3)-equivariant neural networks rely on tensor products of irreducible representations (irreps), whose O(L^6) computational cost limits practical degree L to 2-3."

**S2 (Gap):** "Prior efficient implementations sacrifice generality—they are restricted to specific operation classes such as convolutions or many-body interactions."

**S3 (Method):** "We show that the Clebsch-Gordan tensor product is equivalent to spherical function multiplication via Gaunt coefficients, and accelerate it by changing to a 2D Fourier basis where multiplication becomes FFT-accelerated convolution, reducing complexity to O(L^3)."

**S4 (Key Result):** "Our Gaunt Tensor Product achieves up to 43.7× speedup and 82.3% memory reduction over standard implementations, while matching or improving accuracy on the OC20 and 3BPA benchmarks."

**S5 (Bounded Implication):** "A limitation is that Gaunt coefficients exclude pseudovector outputs; we verify that in-distribution accuracy is preserved, while OOD tasks may require task-specific validation."

### Introduction Outline (Complete)

**P1 (Current Page 1 first paragraph - needs rewrite):**
- Role: Establish the specific problem (tensor product cost) and its importance.
- Target claim: Tensor products of irreps are central to E(3)-equivariant models but have a severe scaling problem.
- Evidence: O(L^6) complexity → L ≤ 3 in practice.
- Transition: Lead into prior work that acknowledged this bottleneck.

**P2 (Current Page 1 second paragraph - restructure):**
- Role: Survey prior work and the acknowledged bottleneck.
- Target claim: Many SOTA models use tensor products but are limited by its cost.
- Evidence: eSCN, EquiformerV2, NequIP, MACE all operate at L ≤ 3.
- Transition: Explain why the problem hasn't been fully solved.

**P3 (Current Page 2 first paragraph - mostly keep):**
- Role: State the gap clearly (no general O(L^3) acceleration exists across operation classes).
- Target claim: Existing efficient implementations are operation-specific.
- Evidence: eSCN is for convolutions, MACE for many-body interactions.
- Transition: Present the solution.

**P4 (Current Page 2 second paragraph - sharpen):**
- Role: Introduce the core idea.
- Target claim: Gaunt coefficients + 2D Fourier basis + FFT → O(L^3).
- Evidence: Mathematical derivation in Section 3.
- Transition: Describe the three operation classes.

**P5 (Current Page 2 bullet list - keep):**
- Role: Preview the three operation classes.
- Target claim: Generality of the method.
- Transition: To experiments.

## Priority Revision Plan
| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P0 | Ablation confound (OC20) | Add CG-Selfmix matched control or add explicit caveat | Validates core causal claim; prevents reviewer rejection | Medium (run one experiment) or Low (add text) |
| P0 | Parity constraint factual inconsistency | Revise Appendix A.6: replace blanket "does not hurt" with nuanced OOD discussion; update Conclusion | Resolves factual contradiction; improves scientific honesty | Low (text edit) |
| P1 | Missing limitations in Conclusion | Add 2-3 sentence limitations paragraph | Completes scientific narrative; preempts reviewer request | Low (text edit) |
| P1 | Parity selection rule not in main text | Add one sentence after Eq. (3) stating l1+l2+l even condition | Complete methodological disclosure | Low (text edit) |
| P2 | Generic introduction hook | Rewrite first paragraph to start with tensor product bottleneck | Sharper narrative; better reader engagement | Medium (paragraph rewrite) |

### ASCII Diagram — Revision Strategy Roadmap

```text
[Problem: OC20 ablation confound]
    → [Risk: Core claim ("Gaunt improves accuracy") not separable from architectural change]
    → [Fix P0: Add CG-based Selfmix control or explicit caveat]
    → [Expected: Causal claim becomes defensible]

[Problem: Parity constraint statement contradicts Table 2]
    → [Risk: Reviewer identifies factual inconsistency → lowers credibility]
    → [Fix P0: Nuance "does not hurt performance" with OOD evidence]
    → [Expected: Transparent discussion, no factual contradictions]

[Problem: No limitations section in Conclusion]
    → [Risk: Appears promotional; misses scientific completeness]
    → [Fix P1: Add 2-3 sentence limitation paragraph]
    → [Expected: Balanced, rigorous conclusion]

[Problem: Parity rule not stated in main text]
    → [Risk: Reader assumes all (l1,l2,l) combos valid]
    → [Fix P1: Add parity condition after Eq. (3)]
    → [Expected: Complete methodological disclosure]

[Problem: Generic intro hook]
    → [Risk: Delayed problem statement weakens engagement]
    → [Fix P2: Restructure P1 to start with tensor product bottleneck]
    → [Expected: Clearer, more compelling narrative]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Efficiency: Feature Interactions | Random features L≤8, 128 channels, e3nn baseline | Avg inference time (Figure 1 left) | Orders-of-magnitude speedup for L>7 | C2 (O(L^3) complexity) | Only tests full tensor product, not sparse path selections |
| E2 | Efficiency: Convolutions | Random features + SH filters, eSCN baseline | Avg inference time (Figure 1 middle) | Consistent additional speedup over eSCN | C2 + C3 | eSCN already efficient; incremental improvement |
| E3 | Efficiency: Many-body Interactions | Multiple L and ν, e3nn + MACE baselines | Avg inference time (Figure 1 right) | 43.7× speedup vs e3nn; 33.2× vs MACE | C2 + C3 | Memory vs speed trade-off not fully characterized |
| E4 | Sanity Check (accuracy) | SEGNN on N-body simulation | Test error (Figure 1 last panel) | Gaunt parameterization matches CG performance | C3 (generality) | Only in-distribution; synthetic task |
| E5 | Real-world: OC20 S2EF | EquiformerV2 + Gaunt-Selfmix, OC20 2M | Energy/Force MAE, Force Cos, EFwT | 16.8% EFwT improvement at L=6 | C1 + C3 | Ablation confound (Issue 1); no CG-Selfmix control |
| E6 | Real-world: 3BPA | MACE + Gaunt Tensor Product, 500 geometries | Energy/Force MAE (300K, 600K, 1200K, Dihedral) | Competitive accuracy, 43.7× speedup, 82.3% memory reduction | C1 + C2 | OOD degradation unacknowledged (Issue 2) |

### Research-Theme Gap Diagnosis

- **New Knowledge (partial):** The connection between CG coefficients and spherical function multiplication via Gaunt coefficients is a genuine mathematical insight. The O(L^3) algorithm is a new contribution. However, without external literature verification (Retrieval-Disabled Mode), the absolute novelty cannot be confirmed.
- **Reproducibility (good):** The method is well-specified mathematically. Code release is promised. The e3nn-based efficiency benchmarks are clearly defined.
- **Impact on Practice (high potential):** 43.7× speedup and 82.3% memory reduction are practically significant. If confirmed independently, the Gaunt Tensor Product could become a default component in equivariant model libraries.

### Proposed Research Experiments

**P0 Experiment: CG-based Selfmix control for OC20**
- **Target Claim:** "Gaunt Tensor Product improves accuracy on OC20."
- **Hypothesis:** The improvement from Gaunt-Selfmix is partially or fully attributable to the additional feature interaction layer, not the Gaunt parameterization.
- **Minimal Design:** Train EquiformerV2 + Selfmix using standard CG tensor products (or the same architecture with CG-based feature interaction). Keep all other settings identical to the Gaunt-Selfmix experiment (12 layers, L=4 and L=6, OC20 2M).
- **Controls/Baselines:** EquiformerV2 (baseline), EquiformerV2 + Gaunt-Selfmix, EquiformerV2 + CG-Selfmix.
- **Metrics:** Energy MAE, Force MAE, Force Cos, EFwT.
- **Success Criterion:** If CG-Selfmix achieves comparable improvement to Gaunt-Selfmix, the contribution is architectural (weaker). If Gaunt-Selfmix clearly outperforms CG-Selfmix, the Gaunt parameterization is validated.
- **Estimated Cost/Time:** ~48 GPU-days (same scale as existing OC20 experiments).
- **Expected Paper-Quality Gain:** Resolves the most critical reviewer concern.

**P1 Experiment: OOD robustness analysis for Gaunt parity constraints**
- **Target Claim:** "Gaunt coefficients do not hurt performance" (current claim in Appendix A.6).
- **Hypothesis:** The pseudovector exclusion from Gaunt coefficients reduces OOD generalization on tasks requiring long-range angular information.
- **Minimal Design:** On the 3BPA dataset, compare MACE vs MACE-Gaunt on additional OOD splits (e.g., dihedral slices broken down by angle range). Include an analysis of which pseudovector components of the CG output are removed by Gaunt coefficients.
- **Controls/Baselines:** MACE (standard CG), MACE-Gaunt.
- **Metrics:** Per-slice Energy/Force MAE, parity output distribution.
- **Success Criterion:** Identify whether the 27% dihedral Energy MAE gap is correlated with specific angular regimes.
- **Estimated Cost/Time:** ~2 GPU-days (analysis of existing results).
- **Expected Paper-Quality Gain:** Provides a scientifically honest and data-grounded limitation discussion.

**P2 Experiment (Nice-to-Have): Scaling behavior beyond L=8**
- **Target Claim:** O(L^3) complexity holds at higher L.
- **Hypothesis:** The theoretical O(L^3) scaling is empirically confirmed up to L=16 or beyond.
- **Minimal Design:** Extend efficiency benchmarks (Figure 1) to L=10, 12, 16 for the Feature Interaction class.
- **Metrics:** Inference time vs L (log-log plot to verify O(L^3) slope).
- **Success Criterion:** Empirical scaling matches O(L^3) within ±0.3 exponent.
- **Estimated Cost/Time:** 1 GPU-day.
- **Expected Paper-Quality Gain:** Strengthens the asymptotic claim with empirical evidence.

### ASCII Diagram — Experiment Upgrade Plan

```text
[P0] CG-Selfmix control (OC20)
  ├── Baseline: EquiformerV2
  ├── Treatment 1: EquiformerV2 + Gaunt-Selfmix
  ├── Treatment 2: EquiformerV2 + CG-Selfmix (same arch)
  └── Success: Separates arch contribution from Gaunt contribution

[P1] OOD robustness analysis (3BPA)
  ├── Analysis: Per-slice breakdown of dihedral errors
  ├── Diagnosis: Which parity components are removed by Gaunt?
  └── Success: Data-grounded limitation discussion

[P2] Scaling verification (L>8)
  ├── Extend efficiency benchmarks to L=10,12,16
  ├── Log-log slope verification vs O(L^3) prediction
  └── Success: Empirically validated asymptotic claim
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6/10**

*Rationale:* The paper presents a mathematically elegant and practically impactful acceleration method for tensor products of irreps, with strong empirical evidence of efficiency gains (up to 43.7× speedup). The core theoretical contribution (connecting CG coefficients to Gaunt coefficients for spherical function multiplication) is sound and well-derived. However, the score is constrained by: (1) the unresolved ablation confound in the OC20 experiment, which weakens the causal claim about performance improvement; (2) the factual inconsistency between the parity constraint defense and the observed OOD degradation on 3BPA; and (3) the absence of external literature verification (Retrieval-Disabled Mode) for novelty assessment. These issues are fixable but currently limit confidence in the paper's strongest claims.

**Post-Revision Target: [7, 8]/10**

*Rationale:* If the authors (a) add a CG-based Selfmix control (or an explicit caveat) for OC20, (b) revise the parity constraint discussion to honestly reflect the OOD trade-off, and (c) add a limitations section to the Conclusion, the paper would merit a score of 7-8. The mathematical contribution and efficiency results are strong enough that, with these revisions and assuming novelty is confirmed via manual literature verification, the paper would be a solid accept at a venue like ICLR.