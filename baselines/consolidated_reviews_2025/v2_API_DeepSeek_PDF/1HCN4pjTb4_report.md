## Summary
# Final Review Report

## Summary

This paper presents a theoretical framework proving that deep neural networks with at least two linear layers, trained end-to-end via gradient descent with weight decay, provably exhibit neural collapse (NC). The work makes three main contributions: (C1) a general sufficient-condition theorem (Theorem 3.1) linking low training error, approximate balancedness of linear layers, and bounded conditioning to NC1 (within-class collapse), NC2 (orthogonality of class means), and NC3 (alignment with the last weight matrix); (C2) a proof that these conditions hold for networks with a wide first layer, smooth activations, and pyramidal topology trained via GD with weight decay (Theorem 4.4), providing the first end-to-end guarantee of NC1 for deep networks; and-to-end trained DNNs; and (C3) two complementary sufficient conditions for well-conditioned linear layers — global optimality under ℓ2-regularized loss and stability under large learning rates — that extend the framework to NC2/NC3. The paper includes experiments on MLP and ResNet20 with MNIST and CIFAR10 that qualitatively agree with the theoretical predictions, particularly the depth-driven improvement in NC2.

The theoretical framing is novel and technically rigorous, bridging the gap between the widely-used but data-agnostic unconstrained features model (UFM) and practical end-to-end training. However, the paper faces a significant gap between the assumptions required for the main theoretical result (smooth activations, pyramidal topology, tailored initialization, exponentially small learning rates in depth) and the experimental validation (standard ReLU, standard architectures, standard initialization, practical learning rates). The large-LR analysis for NC2/NC3 (Section 5.2) is acknowledged as incomplete by the authors. These issues are fixable through more explicit discussion and targeted bridging experiments, but they limit the strength of the current claims.

## Strengths
1. **Theoretical novelty and significance.** The paper provides the first end-to-end theoretical proof of neural collapse emergence in deep networks with at least two linear layers, moving substantially beyond the data-agnostic unconstrained features model (UFM) that dominated prior theoretical work. The sufficient-condition framework (Theorem 3.1) is elegant and general, cleanly separating the roles of interpolation, balancedness, and conditioning.

2. **Methodological rigor.** The proof structure is well-organized: Theorem 3.1 establishes generic sufficient conditions; Theorem 4.4 verifies these conditions under GD with weight decay for a specific network class; Section 5 extends to NC2/NC3 via global optimality and large-LR stability arguments. The two-phase dynamics analysis (NTK phase for interpolation, weight-decay phase for balancedness) is a clever use of timescale separation.

3. **Honest treatment of limitations.** The paper acknowledges several important caveats: that the large-LR analysis for NC2/NC3 is incomplete ("we are hopeful that a more careful analysis..."), that the η ∼ c^{-L} requirement for Theorem 4.4 is unrealistic, and that Assumptions 4.1-4.3 could be replaced by other convergence guarantees. This transparency is commendable and helps reviewers assess the scope.

4. **Empirical support.** The experiments on MLP and ResNet20 across MNIST and CIFAR10 are well-designed, with multiple runs, standard deviation reporting, and systematic exploration of linear-head depth effects. The qualitative agreement between theory (NC2 improves with linear-head depth) and experiments is compelling, even though the experimental conditions do not exactly match the theoretical assumptions.

## Weaknesses
1. **Theory-experiment assumption gap (Major).** The sufficient conditions of Theorem 4.4 (smooth activations with σ' ∈ [γ,1], pyramidal topology n1 ≥ N ≥ n2 ≥ ... ≥ nL, tailored initialization satisfying (8)) are not instantiated in the experiments. The experiments use standard ReLU (whose derivative is 0 for x<0, violating σ' ≥ γ), standard architectures (ResNet20 does not satisfy pyramidal topology), and standard initialization. This gap means the paper does not provide an end-to-end empirical validation of its own theoretical conditions, weakening the claim that the theory "proves" NC in trained DNNs as observed in practice.

2. **Exponentially small learning rate requirement (Major).** Theorem 4.4 requires η ∼ c^{-L} (exponentially small in total depth), while Section 5.2's large-LR analysis requires η ∼ L^{-1}. The paper acknowledges this gap ("The issue is that the proof of Theorem 4.4 requires an extremely small learning rate for large depths...") and does not resolve it. Since practical training uses η ∼ O(1) or η ∼ L^{-1/2}, the theoretical guarantee for NC1 (Theorem 4.4) applies to a training regime not used in practice.

3. **Limited empirical validation of NC3.** The paper reports NC1 (tr(ΣW)/tr(ΣB)) and NC2 (κ(¯Z)) metrics, but NC3 (average cosine similarity between features and weight vectors) is not shown in any figure. Given that Theorem 3.1 provides explicit bounds on NC3, its absence from the experiments is a notable omission.

4. **Quantitative theory-experiment mismatch.** The NC1 bounds in Theorems 3.1 and 4.4 are O((ϵ1+√ϵ2)²), which should vanish as training progresses. However, the experiments show NC1 approaching small but non-zero values (visible in Figure 1). The paper does not quantitatively compare the observed NC1 values to the theoretical bound, missing an opportunity to validate the bound's tightness.

5. **Dependence on the nonlinear parameter norm c in Theorem 5.2.** The bound on κ(WL) at global minimizers depends on exp(c/(2L2)), where c = ∥θnonlin∥²₂ is the norm of nonlinear parameters fitting ZL1 = Y. The scaling of c with problem size (N, K, width) is not discussed, making it unclear when the bound is meaningful.

## Key Issues
### Issue 1 (Major): Theory-experiment assumption gap undermines claims of "proving" NC in practice

**Anchor:** Page 5 - Assumptions 4.1-4.3; Page 8 - Experimental Setup.

**Problem:** Theorem 4.4 assumes (i) pyramidal topology with n1 ≥ N and n2 ≥ n3 ≥ ... ≥ nL, (ii) smooth activations with σ'(x) ∈ [γ,1] (γ>0), and (iii) initialization satisfying λF λ3→L min(λF, minℓ≥3 λℓ) ≥ 8γ(2/γ)^(L/2) C0(θ0)^{1/2}. The experiments use ReLU (σ'(x)=0 for x<0), standard architectures (ResNet20 does not satisfy pyramidal topology), and standard initialization (not manually tuned). The paper does not clarify that the experiments test a different regime than the theory.

**Impact:** The central claim "provably exhibit neural collapse" should be scoped to the specific theoretical conditions. Without an experiment that instantiates Assumptions 4.1-4.3, the paper does not demonstrate that the proven regime actually produces NC in practice, nor that the observed NC in standard settings falls within the theorem's scope.

**Fix:** (1) Add a sentence stating that the theoretical sufficient conditions are not necessary. (2) Consider a small-scale experiment that satisfies Assumptions 4.1-4.3 (e.g., a toy network with smooth leaky ReLU, manually tuned initialization, and pyramidal widths) to demonstrate NC emergence under the exact theoretical conditions.

### Issue 2 (Major): Incomplete large-LR analysis for NC2/NC3

**Anchor:** Page 8, Section 5.2, paragraph beginning "The issue is that the proof of Theorem 4.4 requires..."

**Problem:** Section 5.2 attempts to provide sufficient conditions for NC2/NC3 via large learning rates and the edge of stability. However, the paper concedes that Theorem 4.4 requires η ∼ c^{-L} while Proposition 5.3 requires η ∼ L^{-1}, and these regimes are not reconciled. The section ends with "We are hopeful that a more careful analysis could show..." — a statement of aspiration, not a result.

**Impact:** The large-LR condition is presented as a contribution (bullet 3 in the introduction) but is not a fully proven sufficient condition. This inflates the contribution list.

**Fix:** Either (a) provide a proof that resolves the η ∼ c^{-L} vs η ∼ L^{-1} gap, or (b) downgrade this contribution from a claim to a conjecture, and explicitly state that Section 5.2 provides heuristics and a partial result (Proposition 5.3) rather than a complete proof.

### Issue 3 (Minor): First-claim over-scoping

**Anchor:** Page 1 - Abstract, closing sentence.

**Problem:** The abstract claims "our results are the first to show neural collapse in the end-to-end training of DNNs." While the paper makes a strong case for being the first end-to-end proof for networks with ≥2 linear layers under GD with weight decay, the scope qualifier is missing from this claim. Prior work (e.g., Hong & Ling 2024 for 2-3 layer networks, Beaglehole et al. 2024 for kernel-based training, Pan & Cao 2023) has shown NC in settings that could be considered "end-to-end" under different assumptions.

**Impact:** The unbounded "first" claim is vulnerable to reviewer challenge if they interpret "end-to-end" more broadly than the paper's specific setting.

**Fix:** Scoped wording: "first end-to-end proof of NC for deep networks with at least two linear layers, under the considered architectural and initialization conditions."

### Issue 4 (Minor): NC3 metric not shown in experiments

**Anchor:** Page 8-9, Experimental figures.

**Problem:** NC3 (alignment of features with the last weight matrix) is defined in Section 3 but never plotted in the experimental section. The paper provides bounds on NC3 in Theorem 3.1 but does not verify them empirically.

**Impact:** Missing validation of a theoretically claimed NC property.

**Fix:** Add a figure showing NC3 evolution across training, analogous to the NC1 and NC2 panels in Figure 1/Figure 4.

## Actionable Suggestions
### Suggestion 1 (Must): Scope the "first" claim precisely
**Location:** Page 1 - Abstract, closing sentence; Page 2 - Introduction bullet list.

Replace the unbounded "first to show neural collapse in the end-to-end training of DNNs" with a scoped version that specifies the exact conditions: first end-to-end proof of NC for deep networks with ≥2 linear layers, under the considered architectural, activation, initialization, and training conditions. This makes the claim defensible without diminishing its significance.

### Suggestion 2 (Must): Add a dedicated Limitations paragraph
**Location:** Page 10 - Discussion/Concluding Remarks.

Add a paragraph explicitly discussing (a) the large-LR gap (η ∼ c^{-L} vs η ∼ L^{-1}), (b) the theory-experiment assumption gap, and (c) the unresolved scaling of c in Theorem 5.2. See the Mentor Revised Version in the annotation on Page 10 for copy-ready text.

### Suggestion 3 (Must): Add NC3 metric to experimental figures
**Location:** Page 8-9 - Experimental Results / Figures 1-2.

Include a panel for NC3 (average cosine similarity) alongside the NC1 and NC2 panels in Figures 1 and 4. This validates the theoretical NC3 bounds from Theorem 3.1 and completes the empirical picture.

### Suggestion 4 (Nice-to-have): Quantitative comparison of NC1 bound
**Location:** Page 4 - Theorem 3.1; Page 8 - Results.

From Figure 1, estimate the observed NC1 value (≈10^{-2} to 10^{-3} depending on layer) and compare it to the theoretical bound from Theorem 3.1 given the known ϵ1 (training error), ϵ2 (balancedness metric), r (weight norm bound), n_{L-1}, N, and K. Even a rough calculation would strengthen the theory-experiment connection.

### Suggestion 5 (Nice-to-have): Restructure Introduction paragraph 1
**Location:** Page 1 - Introduction, first paragraph.

Split the first paragraph into two: one defining NC and establishing the UFM gap, the second surveying beyond-UFM work and stating the open problem. See the annotation on Page 1 for copy-ready text.

### Suggestion 6 (Nice-to-have): Add experiment satisfying theoretical assumptions
**Location:** New subsection in Experiments or Appendix.

Conduct a small-scale experiment with smooth leaky ReLU (σ(x) = 0.1x + 0.9 max(0,x) to satisfy σ' ∈ [0.1, 1]), pyramidal widths satisfying Assumption 4.1, and initialization satisfying Assumption 4.3. This would demonstrate NC emergence under the exact conditions of Theorem 4.4.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current storyline follows: NC definition → UFM limitation → Beyond-UFM gap → Our contributions (bullet list) → Related Work → Theorem 3.1 (framework) → Theorem 4.4 (NC1 guarantee) → Section 5 (NC2/NC3) → Experiments → Discussion.

The narrative is logically structured but the Introduction (P1-P2) mixes three roles (NC definition, UFM critique, beyond-UFM survey) into two dense paragraphs. The Related Work section (Section 2) reads as a literature listing rather than an organized comparison.

### Proposed Storyline Candidate A (Recommended)

Title: "Wide Neural Networks Trained with Weight Decay Provably Exhibit Neural Collapse"

**Abstract Outline (5 sentences):**
- S1 (Problem): "Deep neural networks at convergence exhibit a geometric structure in the last layer called neural collapse (NC)."
- S2 (Gap): "Existing theoretical proofs of NC rely on the unconstrained features model, which is data-agnostic and does not capture end-to-end training."
- S3 (Method): "We prove that NC emerges in networks with at least two linear layers, under the sufficient conditions of low training error, balanced linear layers, and bounded conditioning."
- S4 (Result 1): "For networks with a wide first layer and pyramidal topology, we show that gradient descent with weight decay satisfies these conditions, providing the first end-to-end guarantee of within-class collapse (NC1)."
- S5 (Result 2 + Bound): "We further give two sufficient conditions — near-optimality or large-LR stability — under which the linear head is well-conditioned, yielding NC2 and NC3. Experiments on MLP and ResNet20 confirm the theoretical predictions."

**Introduction Outline (paragraph-by-paragraph):**
- P1 (Big Picture + NC definition): Define neural collapse (NC1/NC2/NC3) and its empirical prevalence.
- P2 (UFM limitation): Introduce UFM, summarize what it has achieved, then state the data-agnostic limitation clearly.
- P3 (Beyond-UFM gap): Survey beyond-UFM work, organized by assumption type (shallow networks, kernel methods, strong geometric assumptions). End with "consequently, a proof of NC in deep networks trained end-to-end remains open."
- P4 (Our approach + contribution summary): Briefly state the balancedness + interpolation framework. Present the three contributions with explicit logical dependency (framework → instantiation → conditioning → experiments).
- Transition to Related Work.

### Proposed Storyline Candidate B (Alternative)

Title option: "Balancedness and Interpolation Provably Induce Neural Collapse: An End-to-End Analysis of Deep Networks with Linear Heads"

This title foregrounds the mechanism (balancedness) rather than the architecture (wide networks). The Introduction structure would be:
- P1: Same as Candidate A.
- P2: Focus on the balancedness concept — its origins in linear network analysis (Arora et al., 2018b) and its connection to NC via low-rank bias.
- P3: Present Theorem 3.1 as the core conceptual contribution, then Theorem 4.4 as an instantiation.
- P4: Contribution summary.

**Recommendation:** Candidate A is preferred because it follows the conventional problem→gap→solution→evidence arc that readers in the ICLR/NeurIPS community expect. The current title "Wide Neural Networks Trained with Weight Decay Provably Exhibit Neural Collapse" is good and should be retained.

## Priority Revision Plan
### P0 (Must-do before resubmission)

| Priority | Issue | Action | Expected Impact | Annotation Ref |
|----------|-------|--------|-----------------|----------------|
| P0.1 | Scope the "first" claim | Add qualifiers to abstract and conclusion | Prevents novelty challenge | Page 1 - Abstract |
| P0.2 | Add Limitations paragraph | Insert dedicated paragraph in Discussion | Improves scholarly honesty, preempts reviewer concerns | Page 10 - Discussion |
| P0.3 | Add NC3 metric to experiments | Include NC3 panel in Figures 1 and 4 | Completes empirical validation | Page 8-9 - Experiments |

### P1 (High priority)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P1.1 | Theory-experiment gap | Add sentence clarifying that theory provides sufficient (not necessary) conditions; consider toy experiment under exact assumptions | Bridges criticism about assumption mismatch |
| P1.2 | Large-LR gap | Either prove the gap or downgrade contribution from "proof" to "partial result" | Aligns contribution claims with evidence |
| P1.3 | Restructure Introduction P1 | Split into two paragraphs (NC definition + UFM gap, Beyond-UFM survey) | Improves readability and narrative clarity |

### P2 (Quality improvement)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P2.1 | Quantitative NC1 bound comparison | Compute theoretical NC1 bound from experimental parameters and compare to observed values | Strengthens theory-experiment connection |
| P2.2 | Discuss c scaling in Theorem  scaling in Theorem 5.2 | Add note about how c scales with N, K, width | Clarifies bound meaningfulness |
| P2.3 | Related Work restructuring | Reorganize Section 2 by comparison axes (UFM family, kernel methods, beyond-UFM with assumptions) | Better positioning of contribution |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|--------------------------------------|---------|--------------|-----------------|-------------------|
| E1 | NC emerges in deep linear head (Fig 1) | ResNet20 + 6 extra layers (3 ReLU) on CIFAR10, MSE loss, WD=0.001, LR=0.001, 5000 epochs | NC1, NC2, balancedness, negativity | NC2 improves across linear head layers | C3 (the depth effect) | Uses ReLU (violates Assumption 4.2), standard architecture (violates Assumption 4.1) |
| E2 | NC depth dependence (Fig 2, top) | MLP (5 non-linear layers) on MNIST, linear layers 1-5, WD=0.001/0.004, LR=0.001 | NC1, NC2 (last layer and first linear layer) | NC2 improves with linear depth | C3 (depth → NC2) | High variance from averaging over different WD values; NC3 not reported |
| E3 | NC depth dependence (Fig 2, bottom) | ResNet20 on CIFAR10, 1-6 linear layers, WD=0.001, LR=0.001 | NC1, NC2 | Same as E2 | C3 | Same as E2 |
| E4 | Balancedness & non-linearity vs non-linear depth (Fig 3) | MLP, non-linear depth 4-12, LR=0.001/0.002, WD=0.016/L | Min/mean balancedness, min/mean negativity | Balancedness improves with depth | Balancedness trend | Only 2 hyperparameter setups |
| E5 | Extension to MNIST + MLP (Fig 4, Appendix) | 9-layer MLP (5 NL + 4 L) on MNIST, WD=0.0018, LR=0.001, 10000 epochs | NC1, NC2, balancedness, | Same qualitative behavior as E1 | Robustness | Same as E1 |
| E6 | Extension to ResNet20 on MNIST (Fig 5, Appendix) | ResNet20 on MNIST, varying linear depth | NC1, NC2 | Matches E2/E3 | Robustness | Same as E1 |

### Research-Theme Gap Diagnosis

1. **Reproducibility gap:** The theoretical assumptions (smooth activations, pyramidal topology, tailored initialization) are not instantiated in any experiment. A reader cannot verify that NC emerges under the exact conditions of Theorem 4.4.

2. **NC3 validation gap:** Despite providing theoretical bounds, NC3 is not empirically evaluated.

3. **Large-LR regime gap:** The theory requires η ∼ c^{-L} but experiments use constant LR (0.001). The large-LR regime analysis (Section 5.2) is incomplete.

### Proposed Research Experiments (P0/P1/P2)

**P0.1: Toy experiment under Assumptions 4.1-4.3**
- **Target Claim:** Theorem 4.4 — NC1 emergence under GD with weight decay.
- **Hypothesis:** A network satisfying pyramidal topology, smooth leaky ReLU, and Assumption 4.3 initialization will exhibit NC1 approaching 0.
- **Minimal Design:** n1=128 (≥ N=64 for 2-class subset of MNIST), leaky ReLU with slope 0.1, manually tuned initialization (small W2, large other layers), MSE loss, small LR.
- **Controls/Baselines:** Same architecture but with ReLU activation; same architecture but standard initialization.
- **Metrics:** NC1, NC2, NC3, training loss, balancedness metric.
- **Success Criterion:** NC1 < 0.01 at convergence; balancedness < 0.01.
- **Estimated Cost/Time:** Low (one GPU-hour).
- **Expected Gain:** Directly validates Theorem 4.4's sufficiency; demonstrates NC under exact theoretical conditions.

**P0.2: NC3 metric in existing experiments**
- **Target Claim:** Theorem 3.1 — NC3 bounds hold.
- **Minimal Design:** Compute average cosine similarity (NC3) from saved activations of existing experiments (E1-E6).
- **Metrics:** NC3 vs training epochs, for each linear head layer.
- **Success Criterion:** NC3 trends visible and consistent with theory.
- **Estimated Cost/Time:** Minimal (data already exists).
- **Expected Gain:** Completes the empirical picture; validates NC3 bound.

**P1.1: Large-LR regime study**
- **Target Claim:** Section 5.2 — Large learning rates induce bounded conditioning.
- **Hypothesis:** Training with η = η0/L (as suggested by Proposition 5.3) leads to better-conditioned WL than η = constant.
- **Minimal Design:** Compare η = 0.1/L vs η = 0.001 (constant) on a small network.
- **Metrics:** κ(WL), NC2, NC3, training loss stability.
- **Success Criterion:** Lower κ(WL) under η = 0.1/L regime.
- **Estimated Cost/Time:** Low (2-4 GPU-hours).
- **Expected Gain:** Provides empirical evidence for the large-LR argument even if a complete proof remains open.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6/10**

Rationale: This score reflects the paper's solid theoretical contribution (moving beyond UFM to end-to-end NC analysis, elegant sufficient-condition framework, novel two-phase dynamics analysis) weighed against the significant gap between theoretical assumptions and experimental validation, the incomplete large-LR analysis for NC2/NC3, and the over-scoped "first" claim. The paper makes a meaningful advance in the theoretical understanding of neural collapse, but the current limitations prevent it from being a fully self-contained proof of NC emergence in practical training.

- **Research value/contribution: 7/10** — The sufficient-condition framework (Theorem 3.1) and the two-phase training analysis are genuinely novel and conceptually clean.
- **Novelty: 7/10** — First end-to-end proof for deep networks with ≥2 linear layers under GD with weight decay. (Deferred manual verification: external literature search was unavailable.)
- **Validity/soundness: 6/10** — The proofs appear mathematically sound, but the large gap between theoretical conditions and experimental validation weakens the overall validity claim.
- **Reproducibility: 5/10** — The theoretical results are reproducible from the proofs. The experiments are reproducible from the description, but no hidden implementation details were noted. However, no code is provided in the submission.

**Post-Revision Target: [7, 8]/10**

If the authors address the P0 and P1 items (scope the "first"first" claim, add Limitations, add NC3 experiments, clarify the large-LR gap status, add a toy experiment satisfying Assumptions 4.1-4.3), the paper would become a stronger contribution. The upper bound of 8/10 is limited by the inherent difficulty of the large-LR regime gap, which may require a separate follow-up paper to fully resolve.