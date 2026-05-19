## Summary
# Final Review Report

## Summary

This paper presents CrysBFN, a periodic Bayesian Flow Network (BFN) for crystal structure generation. The core contribution is extending Bayesian Flow Networks, originally defined on Euclidean space, to the non-Euclidean hyper-torus manifold required by crystal fractional coordinates. The authors identify that von Mises distributions (appropriate for periodic data) lack the "additive accuracy" property of Gaussian distributions, breaking the standard BFN simulation-free training paradigm. To address this, they introduce: (1) a periodic Bayesian flow built on von Mises distributions with a new Bayesian update rule, (2) an entropy conditioning mechanism that feeds the concentration parameter c (rather than just timestep t) into the network, (3) a non-auto-regressive equivalent formulation for efficient sampling, and (4) a numerical method for determining the accuracy schedule. CrysBFN achieves competitive or superior results on ab initio crystal generation and crystal structure prediction across four benchmarks, with a dramatic 200× sampling speedup (10 vs. 2000 network forward passes) compared to diffusion-based DiffCSP.

**Assessment:** The theoretical contribution (non-Euclidean BFN for periodic data) is interesting and technically sound. The entropy conditioning mechanism is a principled solution to the non-additive accuracy problem. However, the paper's presentation overclaims the scope of novelty ("unprecedented theoretical issue") and SOTA performance without sufficient qualification. The experimental section reports strong results but lacks analysis of why the method works, and several confounders in the efficiency comparison are not addressed. The conclusion omits any discussion of limitations. Overall, the paper has a solid core contribution but needs significant revision in framing, claim-bounding, and experimental transparency.

## Strengths
1. **Principled theoretical extension:** The paper correctly identifies and addresses a genuine theoretical challenge — the non-additive accuracy of von Mises Bayesian updates — which prevents naive application of BFN to periodic data. The entropy conditioning mechanism is a theoretically motivated solution.

2. **Strong empirical results:** CrysBFN achieves state-of-the-art match rates on crystal structure prediction (64.35% on MP-20, 20.52% on MPTS-52) and competitive property statistics on ab initio generation. The improvements are consistent across multiple datasets and tasks.

3. **Remarkable sampling efficiency:** The 10-step generation achieving 60.02% match rate versus DiffCSP's 51.49% at 2000 steps represents a genuine paradigm advantage. The non-auto-regressive equivalent sampling formulation (Eqs. 15-16) is a clever algorithmic contribution.

4. **Clean mathematical framework:** The derivation of the periodic Bayesian flow (Section 4.1, Appendix A) is rigorous and well-structured. The vector addition interpretation (Eqs. 44-45) elegantly connects the von Mises Bayesian update to the Gaussian case.

5. **Good ablation design:** The ablation study (Table 3) cleanly isolates the contributions of entropy conditioning, accuracy schedule, and torus-specific BFN design, with each component showing clear impact on match rate.

6. **Excellent reproducibility effort:** The paper provides detailed algorithmic descriptions (Algorithms 1 and 2), an anonymous code repository, complete hyperparameter settings, and comprehensive appendix derivations.

## Weaknesses
### W1. Overclaimed novelty language (Major)
The paper uses phrases like "unprecedented theoretical issue" (Page 1 - Abstract and Page 10 - Conclusion) and "first periodic Bayesian flow" without sufficient external verification. While extending BFN to the hyper-torus is a genuine contribution, calling the non-additive accuracy issue "unprecedented" overstates the case — it is a known property of von Mises distributions in directional statistics that was simply unaddressed in the BFN literature. These claims must be tempered.

### W2. Unbounded SOTA claims (Major)
The abstract and conclusion state "consistently achieves new state-of-the-art on all benchmarks" without scope qualification. On MP-20 ab initio generation, CrysBFN's COV-R (99.09%) is lower than DiffCSP (99.71%) and FlowMM (99.49%). The "all benchmarks" claim is factually inconsistent with the reported data. Additionally, the paper does not compare against recent methods like MatterGen, space-group-constrained approaches, or Crystal-GFN.

### W3. Missing limitations section (Major)
The Conclusion (Page 10) has no discussion of limitations, failure cases, or boundary conditions. Every generative model has known failure modes, such as: the method's numerical schedule computation requires hyperparameter tuning; performance on larger systems (beyond 52 atoms) is untested; property statistics are predicted by GNN rather than validated by DFT; and the von Mises-based Bayesian update may have numerical stability issues for extreme concentration parameters.

### W4. Speedup claim confounders (Major)
The 200× speedup (Page 10 - Section 5.4) compares CrysBFN at 10 steps to DiffCSP at 2000 steps, but does not control for: (a) per-step computational cost (CrysBFN may have different per-pass cost), (b) wall-clock time (only NFE is reported), (c) the fact that DiffCSP's performance curve at 2000 steps has not saturated (it is still improving), and (d) parameter count mismatch with FlowMM (28.3M vs 12.3M in Appendix Fig. 7).

### W5. Numerical inconsistency in reported improvement (Minor)
Page 9 - Section 5.1 states "+4.34% compared to DiffCSP with the same level of delem" for compositional validity on MP-20. From Table 1, CrysBFN Comp = 87.51% vs DiffCSP Comp = 83.25%, a difference of 4.26 percentage points, not 4.34. This needs correction.

### W6. Related-work classification gaps (Minor)
The Related Work (Section 2) is organized as a chronological narrative rather than by conceptual axes. Missing discussion or inadequate coverage of: space-group-constrained generation, MatterGen, Crystal-GFN, and the physical connection between von Mises distributions and harmonic crystal force fields (mentioned only in Appendix A.1 but relevant to the main text).

### W7. Loss balancing not discussed (Minor)
The joint training loss sums LA + LF + LL without discussion of loss scales, gradient normalization, or potential modality interference (Page 8, Algorithm 1). The weight "5 × 10^{-2}" mentioned in Appendix C is ambiguous regarding whether it is per-modality or global.

### W8. Numerical schedule validation gap (Minor)
The accuracy schedule determination (Page 7) uses "arbitrarily selected x ∈ [−π, π)" without justifying robustness to this choice. The computational cost of the numerical binary search procedure is not reported.

## Key Issues
The following ranked board prioritizes defects by their impact on research validity and scientific credibility:

| Rank | Issue | Severity | Impact | Section |
|------|-------|----------|--------|---------|
| 1 | SOTA claim inconsistent with reported data (COV-R lower than DiffCSP on MP-20) | Major | Research credibility, overclaim | Abstract, Conclusion |
| 2 | No limitations discussed in Conclusion | Major | Scientific completeness | Page 10 - Conclusion |
| 3 | 200× speedup lacks wall-clock validation and controls for per-step cost | Major | Claim rigor | Page 10 - Section 5.4 |
| 4 | "Unprecedented theoretical issue" language inflates novelty | Major | Tone, defensibility | Abstract, Page 10 |
| 5 | Numerical inconsistency in reported improvement (+4.34% vs 4.26pp) | Minor | Factual accuracy | Page 9 - Section 5.1 |
| 6 | Related Work lacks structured comparison axes | Minor | Readability | Section 2 |
| 7 | Multi-modality loss balancing not discussed | Minor | Reproducibility | Page 8 - Section 4.2 |
| 8 | Numerical schedule robustness to chosen x not validated | Minor | Reliability | Page 7 - Section 4.1 |

### Core Structural Observation

The paper's central scientific contribution — extending BFN to periodic manifolds via von Mises distributions with entropy conditioning — is technically solid. The key issues stem primarily from **overclaiming the scope and strength of results** rather than from methodological flaws. The difference between "what the paper has done" and "what the paper claims to have done" is the largest source of risk for acceptance. With careful claim-bounding and the addition of a limitations paragraph, all major issues are fixable within a standard revision cycle.

## Actionable Suggestions
### S1. Bound all SOTA claims (Must)
Replace "consistently achieves new state-of-the-art on all benchmarks" with specific, scoped claims such as:
"CrysBFN achieves competitive or superior results on the evaluated benchmarks for ab initio generation and crystal structure prediction tasks." Quote exact metrics per dataset and note where other methods are stronger (e.g., DiffCSP has higher COV-R).

### S2. Add a limitations paragraph to the Conclusion (Must)
Add 3-5 sentences discussing: (a) numerical schedule precomputation cost, (b) untested larger systems (>52 atoms), (c) GNN-predicted rather than DFT-verified property statistics, (d) potential numerical stability for extreme concentration parameters, (e) unverified generalization to other hyper-torus data types.

### S3. Add wall-clock time comparison for efficiency (Must)
Report wall-clock generation time alongside NFE for CrysBFN and DiffCSP under identical hardware. Show CrysBFN performance across a wider step range (10, 50, 100, 500) to demonstrate saturation behavior.

### S4. Tone down novelty language (Must)
Replace "unprecedented theoretical issue" with "previously unaddressed challenge in the BFN literature." Replace "first periodic Bayesian flow" with "first non-Euclidean Bayesian flow for periodic data, to our knowledge" throughout the Abstract and Conclusion.

### S5. Fix numerical inconsistency (Must)
Correct the "+4.34%" claim on Page 9 - Section 5.1. Either report absolute difference: "4.26 percentage points higher compositional validity than DiffCSP" or relative improvement: "5.1% relative improvement."

### S6. Restructure Related Work (Nice-to-have)
Reorganize Section 2 around conceptual axes: representation-based vs direct generation, equivariant vs non-equivariant, diffusion vs flow-matching vs BFN. Add explicit comparison table summarizing assumptions, strengths, and limitations of each family.

### S7. Clarify loss balancing (Nice-to-have)
Report the scale of each loss term (LA, LF, LL) at initialization and after training. State whether any gradient normalization or loss weighting was applied beyond the single weight parameter.

### S8. Validate schedule robustness (Nice-to-have)
Add a sentence clarifying the choice of x in the numerical schedule determination (e.g., "x was fixed to 0 for all experiments, which minimizes the expected squared error"). Report the precomputation time for the schedule.

### S9. Add von Mises motivation in main text (Nice-to-have)
Move the physical motivation (von Mises as stationary distribution in harmonic crystal potential) from Appendix A.1 to the main text, adding 1-2 sentences after Eq. (6).

### S10. Add mechanistic analysis (Nice-to-have)
In Section 5.1, add 2-3 sentences explaining why CrysBFN's atom-type modeling in simplex space improves compositional validity, referencing the categorical Bayesian flow formulation.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)

The current abstract over-extends claims. Here is a revised 5-sentence structure:

**S1 (Problem):** "Generative modeling of crystal structures is challenging due to periodic symmetries that most generative frameworks do not inherently respect."

**S2 (Prior Limitation):** "Existing diffusion-based methods address periodicity through wrapped-normal score approximations, which require infinite-sum truncation and operate in high-variance spaces, while Bayesian Flow Networks (BFNs) are limited to Euclidean data."

**S3 (Key Barrier):** "Extending BFNs to the hyper-torus manifold of crystal fractional coordinates breaks the additive accuracy property of Gaussian BFNs, preventing simulation-free training."

**S4 (Solution):** "We introduce CrysBFN, a periodic E(3)-equivariant Bayesian flow network that resolves this barrier via a novel entropy conditioning mechanism and a non-auto-regressive equivalent sampling formulation."

**S5 (Bounded Result):** "On ab initio generation and crystal structure prediction benchmarks, CrysBFN achieves competitive or superior results compared to diffusion- and flow-matching-based methods, with up to 200× fewer network forward passes under matched evaluation settings."

### Introduction Outline (Complete)

The current introduction has 4 paragraphs with a literature-survey opening that is too broad. Recommended structure with 4 revised paragraphs:

**P1 (Stakes + Gap, 6-8 sentences):** 
- Open with the importance of crystal generation for materials discovery.
- State the unique challenges: periodic symmetry, exponential search space, sparsity of stable materials.
- End with the key limitation: existing methods cannot balance quality and efficiency because they lack confidence-guided state updates.

**P2 (Prior Work Failure Mode, 5-6 sentences):**
- Explain that diffusion methods approximate wrapped-normal scores with truncation bias.
- State that BFN offers a principled alternative but only for Euclidean data.
- Articulate the specific barrier: periodic data requires non-Euclidean Bayesian flow, which faces the non-additive accuracy problem.

**P3 (Proposed Solution, 4-5 sentences):**
- Introduce the periodic Bayesian flow on the hyper-torus using von Mises distributions.
- State the entropy conditioning mechanism as the key enabler.
- Mention the fast equivalent sampling formulation.
- Announce CrysBFN as the first periodic E(3)-equivariant BFN for crystals.

**P4 (Contributions, 3 bullet points):**
- C1: Periodic Bayesian flow with entropy conditioning.
- C2: Periodic E(3)-equivariant BFN framework.
- C3: Non-auto-regressive equivalent sampling enabling 200× speedup.

### Comparison of Current vs. Proposed Storyline

| Aspect | Current | Proposed | Benefit |
|--------|---------|----------|--------|
| Opening scope | Too broad (drug design, protein engineering) | Focused on crystal challenges | Reduces confusion time |
| Gap clarity | Implicit (buried in paragraph 2) | Explicit (P1 ends with the gap) | Stronger motivation |
| Technical barrier | Mentioned briefly | Highlighted at P2 end | Better framing of contribution |
| Contribution-evidence link | C3 is purely empirical | C3 linked to algorithmic innovation | Cleaner contribution structure |

## Priority Revision Plan
### P0 (Must fix, pre-submission critical)

| Priority | Issue | Action | Location | Expected Impact |
|----------|-------|--------|----------|-----------------|
| P0.1 | Unbounded SOTA claims | Rewrite Abstract and Conclusion with scoped claims | Abstract, Page 10 - Conclusion | Prevents reviewer rejection on overclaim |
| P0.2 | Missing limitations | Add 3-5 sentence limitations paragraph | Page 10 - Conclusion | Improves scientific credibility |
| P0.3 | Numerical inconsistency | Correct +4.34% to +4.26pp or 5.1% relative | Page 9 - Section 5.1 | Fixes factual error |
| P0.4 | "Unprecedented" language | Replace with "previously unaddressed in BFN literature" | Abstract, Page 10 | Removes unnecessary provocation |

### P1 (High priority, within 1 week)

| Priority | Issue | Action | Location | Expected Impact |
|----------|-------|--------|----------|-----------------|
| P1.1 | Speedup claim robustness | Add wall-clock comparison table + wider NFE range | Page 10 - Section 5.4 | Strengthens efficiency claim |
| P1.2 | Numerical schedule clarity | State chosen x value and precomputation time | Page 7 - Section 4.1 | Improves reproducibility |
| P1.3 | Loss balancing | Report per-modality loss scales | Page 8 - Section 4.2 | Improves reproducibility |

### P2 (Nice-to-have, before next submission)

| Priority | Issue | Action | Location | Expected Impact |
|----------|-------|--------|----------|-----------------|
| P2.1 | Related Work structure | Reorganize by conceptual axes | Section 2 | Improves reader orientation |
| P2.2 | Mechanistic analysis | Add explanation of why simplex modeling helps | Page 9 - Section 5.1 | Adds scientific depth |
| P2.3 | von Mises motivation | Move physical connection to main text | Page 5 - Eq. (6) area | Enriches theoretical grounding |

### Revision Strategy Roadmap

```text
[Current State]
    │
    ├── Overclaimed SOTA + missing limitations
    │   └── P0.1, P0.2, P0.4 → Rewrite Abstract/Conclusion
    │       └── Expected: Claim-evidence alignment + scientific completeness
    │
    ├── Efficiency claim needs validation
    │   └── P1.1 → Add wall-clock + wider NFE
    │       └── Expected: Reviewer confidence in 200× claim
    │
    ├── Missing experimental transparency
    │   ├── P0.3 → Fix numeric error
    │   ├── P1.2 → Clarify schedule determination
    │   └── P1.3 → Report loss scales
    │       └── Expected: Improved reproducibility
    │
    └── Structural improvements
        ├── P2.1 → Reorganize Related Work
        ├── P2.2 → Add mechanistic analysis
        └── P2.3 → Move physical motivation to main text
            └── Expected: Better reader experience
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|----------------------------|---------|--------------|-----------------|-------------------|
| E1 | Ab initio crystal generation quality | Perov-5, Carbon-24, MP-20; unconditional generation of 10K samples | Validity, COV-R, COV-P, dρ, dE, delem | CrysBFN competitive or best on most metrics | C1 (periodic BFN effective), C2 (equivariant BFN effective) | COV-R on MP-20 lower than baselines; no failure-case analysis |
| E2 | Crystal structure prediction (CSP) | Perov-5, MP-20, MPTS-52; conditional p(L,F\|A) | Match Rate, RMSE | CrysBFN best on all datasets (64.35% on MP-20) | C1, C2 | Error bars only shown for seed variance (Tab 5); no hyperparameter sensitivity |
| E3 | Ablation: entropy conditioning | MP-20, CSP task | Match Rate, RMSE | w/o entropy cond: 52.16% vs 64.35% | C1 (entropy conditioning critical) | Single metric (match rate) on single dataset |
| E4 | Ablation: accuracy schedule | MP-20, CSP task | Match Rate, RMSE | w/o approx. sch: 49.76% vs 64.35% | C1 (numerical schedule matters) | Same as E3 |
| E5 | Ablation: torus BFN vs original BFN | MP-20, CSP task | Match Rate, RMSE | w/o torus: 6.17% vs 64.35% | C1 (torus BFN essential) | Same as E3 |
| E6 | Sampling efficiency | MP-20, CSP task; NFE sweep | Match Rate vs NFE | 60.02% at 10 steps | C3 (fast sampling) | No wall-clock time; limited NFE range for CrysBFN |
| E7 | Uniqueness/Novelty/Stability | MP-20, ab initio | Unique%, Novel%, Stable%, S.U.N.% | CrysBFN: 12.16% S.U.N. vs 9.44% (DiffCSP) | C1, C2 | DFT relaxation not performed; stability predicted |
| E8 | Training cost comparison | Perov-5, MP-20, MPTS-52 | GPU hours | CrysBFN competitive (e.g., 85.71h vs 92.22h on MP-20) | Practicality | Only one GPU configuration tested |

### Research-Theme Gap Diagnosis

The experimental section provides strong evidence for generation quality and efficiency, but three research-value claims remain weakly supported:

1. **New knowledge about periodic Bayesian flow**: The paper claims that entropy conditioning is critical (vs. time conditioning), but this is only tested on one task (CSP) on one dataset (MP-20). The generality of this insight across different crystal datasets and hyper-torus data types is not established.

2. **Reproducibility**: While the paper provides pseudocode and hyperparameters, the joint training dynamics (loss scales, gradient flow) and the numerical schedule determination procedure are insufficiently documented for exact reproduction.

3. **Impact on practice**: The practical value of CrysBFN for materials discovery is asserted but not demonstrated. No downstream validation (e.g., DFT relaxation, property prediction on generated structures) is performed.

### Proposed Research Experiments (P0/P1/P2)

| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|-------------|------------|---------------|--------------------|---------|------------------|-----------|---------------|
| C1: Entropy conditioning generalizes | Entropy conditioning benefit holds across datasets | Repeat ablation on Perov-5 and MPTS-52 | CrysBFN vs w/o entropy cond. | Match Rate, RMSE | Consistent improvement >5% match rate | 2 GPU-days | Validates core claim generality |
| C2: 200× speedup is real | Wall-clock speedup matches NFE speedup | Measure wall-clock time for 10/100/500/2000 steps | DiffCSP vs CrysBFN same GPU | Seconds per batch, total generation time | Wall-clock speedup >50× at equivalent match rate | 1 GPU-day | Strengthens efficiency claim |
| C1: Stability validates generation quality | DFT relaxation confirms low-energy structures | Run DFT (VASP) on top-50 generated structures per dataset | Initial vs relaxed energy, structure match rate | Energy above convex hull, RMSD to experimental | >60% structures remain within 0.1 eV/atom of hull | 5-10 GPU-days (DFT cost) | Provides physical validation of generated structures |
| C3: Torus BFN generalizes to non-crystal data | Method works on molecular torsional angles | Test on QM9 torsional conformer generation | Existing torsional diffusion baselines | Conformer coverage, RMSD | Competitive with torsional diffusion | 3 GPU-days | Demonstrates broader impact |

```text
ASCII Diagram — Experiment Upgrade Plan

[Current experiments]
    │
    ├── E1-E5: Quality/ablation completed
    │
    ├── E6: Efficiency (partial)
    │   └── P1 expansion: Add wall-clock time + wider NFE range
    │
    ├── E7: Stability (GNN-predicted, not DFT)
    │   └── P0 expansion: Add DFT validation on subset
    │
    └── Missing: Generality / Downstream validation
        └── P1 expansion: Test on Perov-5/MPTS-52 ablation
        └── P2 expansion: Test on molecular torsional data
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

Rationale: The paper presents a genuinely novel theoretical contribution (non-Euclidean BFN for periodic data) with strong empirical results and a clean mathematical framework. However, the score is limited by three factors: (1) overclaimed novelty and SOTA language that is inconsistent with the actual data, (2) absence of limitations discussion which reduces scientific completeness, and (3) insufficient validation of the headline efficiency claim (no wall-clock comparison). The core contribution is solid but the presentation would benefit from more disciplined claim-bounding.

**Post-Revision Target: [7.0, 8.0]/10**

This target assumes all P0 and P1 items are addressed: SOTA claims are scoped, limitations are added, numerical inconsistencies are fixed, wall-clock validation is provided, and novelty language is tempered. If the authors additionally validate on non-crystal hyper-torus data or provide DFT relaxation evidence, the score could reach 8.0/10. Without addressing the overclaiming issue, the score would remain below 6.5.