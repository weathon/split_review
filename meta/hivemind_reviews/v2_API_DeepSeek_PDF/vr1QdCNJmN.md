## Summary
# Final Review Report

## Summary

This paper proposes the **Difference-of-Submodular Bregman Divergence (DBD)**, extending the submodular-Bregman divergence framework (Iyer & Bilmes, 2012b) to set functions that are neither submodular nor supermodular, via the strong difference-of-submodular (DS) decomposition. The authors provide three main contributions: (C1) proving that the submodular-Bregman divergence is a proper divergence when the generating function is strictly submodular; (C2) extending this to arbitrary set functions through DS decomposition (Theorem 3.1'); and (C3) proposing a learnable DBD using ε-PointNet architectures with triplet-loss training. Experiments on MNIST (illustrative) and ModelNet40 (clustering and set retrieval) show that the learned DBD substantially outperforms classical set-similarity metrics and modestly improves over single-function baselines.

**Strengths:** The theoretical core is mathematically rigorous and clean: the use of strict submodularity to establish identifiability, the extension via DS decomposition, and the expressive-power theorem (Theorem 3.4) are well-constructed. The paper opens a novel direction—learning divergences on discrete sets—that bridges submodular analysis and neural metric learning.

**Weaknesses:** (1) A theory-practice gap exists: the practical NN construction's strict submodularity guarantee is only proven for the identity-γ case, while the paper claims general submodularity under ReLU activations without proof. (2) The empirical evaluation lacks critical baselines (standard PointNet + Euclidean distance, explicit submodular-Bregman divergences) and the SOTA comparison is not controlled. (3) The conclusion lacks a dedicated limitations section. (4) Related work is structured as a broad catalog rather than focused comparison. (5) Novelty cannot be externally verified in this retrieval-disabled run.

## Strengths
1. **Mathematically rigorous theoretical foundation.** The paper provides clean proofs for the identifiability of submodular-Bregman divergences under strict submodularity (Theorem 3.1) and extends to arbitrary set functions via DS decomposition (Theorem 3.1'). The expressive-power result (Theorem 3.4) is concise and logically sound, establishing that richer function classes yield richer divergences.

2. **Novel problem framing.** The idea of learning a Bregman-style divergence on discrete spaces—rather than using handcrafted set-similarity metrics—is conceptually novel and practically motivated. The connection between submodular analysis, Bregman divergences, and permutation-invariant neural networks is creative.

3. **Complete theoretical apparatus for strict submodularity.** The paper develops and proves several non-trivial technical results: the equivalence of strict submodularity to strict diminishing returns (Lemma A.2), the existence of strict subgradients (Proposition A.4), and the strict supergradient property of the grow/shrink/bar constructions (Proposition 2.5). The log-sum-exp relaxation of facility location (Eq. 3) is correctly proven to be strictly submodular.

4. **Transparent experimental reporting.** Results are reported with means and standard deviations over 10 random seeds, which is good statistical practice. The ablation study (w/ vs w/o DS decomposition) is well-motivated and the comparison across supergradient types (grow/shrink/bar) provides insight.

5. **Reproducibility effort.** Code is provided in supplementary material, and the network architecture (ε-PointNet with 2 hidden layers of 64 units) is specified clearly.

## Weaknesses
1. **Theory-practice gap in submodularity guarantee (Major).** The paper claims that ReLU activations with non-negative outputs guarantee submodularity of ε-PointNet (Page 7, lines 42-44). However, this is only proven for the special case where γ is the summation function (reducing to the relaxed facility location function). When γ is a general MLP, composition with log-sum-exp may not preserve submodularity. Since the strict semidifferential requirements of Theorem 3.1' depend on strict submodularity of f1 and f2, the practical construction may not satisfy the theoretical preconditions. This gap is not acknowledged in the paper.

2. **Missing critical baselines in experiments (Major).** The clustering experiments (Table 2) compare DBD against classical set-similarity metrics (Rand index ~0.02) and submodular-Bregman special cases, but do not include the most natural baseline: a standard PointNet embedding with Euclidean distance. Since DBD uses ε-PointNet as its building block, the comparison against a simple PointNet embedding would isolate the benefit of the DBD formulation from the benefit of having a learnable set encoder. Similarly, the set retrieval comparison against MVTN is not controlled (MVTN uses multi-view images with pretrained 2D backbones vs DBD's raw point cloud MLP).

3. **Conclusion lacks dedicated limitations discussion (Major).** The paper does not include a limitations section, omitting discussion of: (a) exponential cost of exact DS decomposition, (b) unproven submodularity for general γ, (c) empirical scope limited to point clouds, (d) DBD underperforms MVTN in retrieval. This reduces scientific completeness.

4. **Related work is a catalog rather than structured positioning (Minor).** The "Related work" paragraph on Page 2 lists Bregman divergence applications chronologically without an organizing principle. It does not address how the proposed DBD differs from each line of work. The DML paragraph (Page 3) is better but the "to our best knowledge" first claim cannot be verified.

5. **Method section is too brief (Minor).** The entire DBD method is described in 3 lines of equations and 2 sentences of text (Page 7). The derivation from Theorem 3.1' to Eq. (9) is not shown explicitly, and key implementation details (how subgradients/extreme points are computed exactly, pseudocode) are omitted.

6. **Unsupported "statistical significance" claim (Minor).** The text claims bar supergradient is "inferior with statistical significance" (Page 9, line 41) but reports no p-value or statistical test. The standard deviations of the three methods overlap.

7. **Illustrative experiment lacks quantification (Minor).** The MNIST experiment (Section 5.1) is purely qualitative with M=3,4 only. No quantitative metric is reported to verify that DBD ordering correlates with label similarity.

## Key Issues
### Issue 1 (Major): Unproven submodularity guarantee for practical NN construction
- **Location:** Page 5, Page 7
- **Evidence:** The paper states "ReLU is used for the hidden and final layers, which yields non-negative outputs; thus the submodularity is guaranteed" (Page 7, lines 42-44). However, submodularity of ε-PointNet is proven only for the special case where γ=identity, ϕ_k non-negative, which reduces to the relaxed facility location function (Proposition A.5). When γ is a learned MLP, the composition may not preserve submodularity.
- **Risk:** The entire DBD construction relies on the existence of strict subgradients/supergradients of f1 and f2, which requires strict submodularity. If strict submodularity is not guaranteed, the divergence properties of DBD may not hold.
- **Fix:** Either (a) restrict γ to identity in experiments and explicitly state this limitation, or (b) prove that ε-PointNet with ReLU and any non-negative γ preserves submodularity under composition.

### Issue 2 (Major): Missing baselines and uncontrolled comparisons
- **Location:** Page 9 (Table 2), Page 10 (Table 4)
- **Evidence:** The clustering comparison (Table 2) lacks a PointNet+Euclidean baseline. The retrieval comparison (Table 4) uses MVTN (92.9) from another paper without reproducing the result. The "w/o decomposition" vs "w/ decomposition" comparison may also be confounded by parameter count differences (two 64×64 MLPs have more parameters than one 64×128 MLP).
- **Risk:** Readers cannot determine whether DBD gains come from the divergence formulation or simply from having a learnable set encoder.
- **Fix:** Add a standard PointNet + Euclidean distance baseline. Reproduce MVTN under the same data splits or remove the SOTA comparison and bound claims to the Densepoint comparison only.

### Issue 3 (Major): Missing limitations section and overclaiming
- **Location:** Page 10 (Conclusion)
- **Evidence:** The conclusion claims "significantly outperformed existing submodular Bregman divergences" but compares against classical set-similarity metrics (~0.02 Rand index) rather than explicit submodular-Bregman divergences. No dedicated limitations are discussed.
- **Risk:** Readers may overestimate the practical significance and general applicability of DBD.
- **Fix:** Add a limitations paragraph addressing the four points in the annotation. Restructure baselines to include explicit submodular-Bregman divergences.

### Issue 4 (Minor): Related work lacks structure
- **Location:** Page 2 (Related work paragraph)
- **Evidence:** The paragraph lists Bregman applications (k-means, exponential families, information geometry, NMF, mirror descent, variational inference) without organizing principles or critical comparison with the proposed method.
- **Risk:** Missed opportunity to clearly position the novelty.
- **Fix:** Restructure around comparison axes: continuous vs discrete divergences, fixed vs learned divergences.

### Issue 5 (Minor): Method derivation omitted
- **Location:** Page 7 (Proposed Method)
- **Evidence:** Eq. (9) is presented without the explicit derivation from hY = h1_Y - g2_Y. The paper transitions from "hY = h1_Y - g2_Y ∈ ˜∂f(Y)" to the additive Df form without showing the algebra.
- **Risk:** Less experienced readers may not follow the construction.
- **Fix:** Add 3-4 lines of derivation showing the simplification.

## Actionable Suggestions
### S1: Clarify submodularity guarantee (Must fix, Issue 1)
Revise the submodularity claim on Page 7 (lines 42-44). The current wording implies that ReLU + non-negative outputs *always* guarantees submodularity. Replace with:
"In our implementation, we set γ to the identity function with K=1, which reduces ε-PointNet to the relaxed facility location function (3), proven strictly submodular for ε>0 (Proposition A.5). When γ is a learned MLP, submodularity is not guaranteed in general; we restrict experiments to the identity-γ case and leave the general analysis to future work."
This small change resolves the theory-practice gap.

### S2: Add missing PointNet+Euclidean baseline (Must fix, Issue 2)
Add one row to Table 2: "PointNet (MLP-64×64) + Euclidean distance." Extract PointNet embeddings (128-dim from the 64×64 MLP) and run k-means in that space. This isolates whether DBD's advantage comes from the divergence formulation or simply from having a learned representation. If DBD outperforms this baseline, the divergence-specific contribution is validated. Expected delta: DBD should improve ~2-4 Rand index points over plain PointNet.

### S3: Add explicit submodular-Bregman baselines (High priority)
The current Table 2 compares against classical set-similarity metrics (Rand index ~0.02). While the improvement over these is dramatic, the more relevant comparison is against the submodular-Bregman divergences from Iyer & Bilmes (2012b). Add at least 2-3 rows with explicit submodular functions (e.g., facility location, log-det, cut function) as generating functions for submodular-Bregman divergences. This directly supports the claim of "significantly outperforming existing submodular Bregman divergences."

### S4: Report statistical test for supergradient comparison (High priority)
For the claim that bar supergradient is "inferior with statistical significance" (Page 9, line 41), add a paired t-test or Wilcoxon signed-rank test across the 10 seeds, comparing grow-DBD vs bar-DBD and shrink-DBD vs bar-DBD. Report p-values explicitly. If not significant, soften the language accordingly.

### S5: Add limitations section (Must fix, Issue 3)
Insert a "Limitations" paragraph at the end of the Conclusion (Page 10), structured as follows:
"Limitations. Our approach has four main limitations. First, finding the exact DS decomposition for an arbitrary set function f takes exponential time, so our construction uses pre-specified submodular NNs rather than decomposing a target function. Second, strict submodularity of ε-PointNet is guaranteed only when γ is the identity function; more general γ architectures require further analysis. Third, empirical validation is currently limited to point cloud data (ModelNet40); future work should evaluate on other discrete structures such as item sets and combinatorial optimization. Fourth, the retrieval mAP (90.2) is below the multi-view state-of-the-art (92.9), indicating room for improvement in the learned divergence framework."

### S6: Structured related work (Nice-to-have)
Restructure the "Related work" paragraph (Page 2) into three focused sub-paragraphs: (a) Bregman divergences and their applications, (b) discrete-space divergences and submodular-Bregman (Iyer & Bilmes, 2012b), (c) learned divergences (Lu et al., 2023; Siahkamari et al., 2020). Each sub-paragraph should end with a sentence connecting to the proposed DBD.

### S7: Expand method derivation (Nice-to-have)
Add 3-4 lines in Section 4 (Page 7) showing the algebraic derivation from hY = h1_Y - g2_Y to Eq. (9):
"Substituting f = f1 - f2 and hY = h1_Y - g2_Y into Df(X,Y) = f(X) - f(Y) - ⟨hY, 1X - 1Y⟩ yields Df1(X,Y) + Df2(X,Y), where Df1 uses the lower-bound form (7) and Df2 uses the upper-bound form (8)."

### S8: Add quantitative metric to MNIST experiment (Nice-to-have)
In Section 5.1 (Page 8), report the Spearman rank correlation between DBD values and label-based Jaccard similarity across held-out set pairs. This would strengthen the illustrative example and provide a quantitative anchor for the qualitative Figure 1.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction (Pages 1-2) follows: Definition (1.1) -> Bregman divergence Eq. (1) -> challenge of discrete spaces -> submodular-Bregman divergence and its limitations -> Our contribution -> Related work. This is a mathematically natural order but front-loads formal definitions before establishing practical stakes.

### Recommended Storyline (Option A — Problem-Driven)

**Paragraph 1 (Motivation):** "Measuring dissimilarity between discrete objects — sets, point clouds, item collections — is a fundamental need in machine learning. Most existing set-distance metrics simply count the size of intersections and symmetric differences. When the ground set is large, these metrics become uninformative because co-occurrence of identical elements is rare."
*Evidence anchor:* Choi et al. (2010) survey of binary similarity measures, Page 2 lines 2-7.

**Paragraph 2 (Prior Attempt and Gap):** "Iyer & Bilmes (2012b) introduced the submodular-Bregman divergence, leveraging submodular function theory to define a Bregman-like divergence on discrete spaces. However, this framework has two issues: (i) the identifiability condition D(x,y)=0 ⇒ x=y is not guaranteed without strict submodularity, and (ii) the choice of submodular function is ad-hoc, resulting in divergences that still reduce to simple set operations."
*Evidence anchor:* Page 2 lines 8-23.

**Paragraph 3 (Proposed Approach):** "We resolve both issues through the difference-of-submodular (DS) decomposition, which allows any set function — not just submodular ones — to serve as the generator of a valid Bregman divergence. We call this the difference-of-submodular Bregman divergence (DBD). Theoretically, we prove that richer generating function classes yield richer divergences. Practically, we parametrize the generating function using permutation-invariant neural networks (ε-PointNet), making DBD learnable from data."
*Evidence anchor:* Page 2 lines 24-37.

**Paragraph 4 (Evidence Preview + Contributions):** "Experiments on ModelNet40 show that the learned DBD substantially outperforms classical set-similarity baselines in clustering (Rand index 0.80 vs 0.02) and achieves competitive retrieval results (90.2 mAP). The DS decomposition consistently improves over single-function baselines across three supergradient types. These results demonstrate that learned discrete divergences can capture structural properties that simple overlap-based metrics miss."
*Evidence anchor:* Page 9 Table 2, Page 10 Table 4.

**Paragraph 5 (Paper Organization):** "Section 2 reviews submodular functions, semidifferentials, and permutation-invariant NNs. Section 3 establishes the theoretical foundations of DBD. Section 4 describes the learning framework. Section 5 presents experiments, and Section 6 concludes with limitations and future work."

### Abstract Outline (S1-S5)

**S1 (Problem):** "Defining meaningful divergences on discrete spaces is challenging because standard overlap-based metrics become uninformative on large ground sets."

**S2 (Prior Gap):** "The submodular-Bregman divergence (Iyer & Bilmes, 2012b) provides an elegant framework but requires strict submodularity for identifiability and uses ad-hoc generating functions."

**S3 (Proposed Method):** "We propose the difference-of-submodular Bregman divergence (DBD), which extends Bregman divergences to any set function via strong DS decomposition, and introduce a learnable DBD using ε-PointNet architectures."

**S4 (Key Result):** "Experimentally, DBD achieves Rand index 0.80 on ModelNet40 clustering (vs 0.02 for classical metrics) and 90.2 mAP on set retrieval, with DS decomposition consistently improving over single-function baselines."

**S5 (Bounded Implication):** "This work provides a principled framework for learning structure-preserving divergences on discrete data, with limitations discussed in the conclusion."

### Alternative Storyline (Option B — Theory-First)

Keep the current definition-first structure but reorganize as: Definition 1.1 → challenge of discrete spaces → submodular-Bregman limitations → Theorem 3.1 (strict submodularity) → Theorem 3.1' (DS extension) → Theorem 3.4 (expressive power) → practical learning framework → experiments. This works for theory-oriented readers but delays motivation.

### Storyline Comparison

| Dimension | Current | Option A (Recommended) | Option B |
|---|---|---|---|
| Problem alignment | Moderate | Strong | Moderate |
| Variable alignment | Good | Good | Good |
| Contribution-evidence | Good | Better (previews data) | Moderate |
| Reader accessibility | Moderate | High | Low |

**Recommendation:** Adopt Option A for the introduction, and revise the abstract to follow the S1-S5 structure above.

## Priority Revision Plan
### P0 Items (Must fix before resubmission)

| Priority | Issue | Action | Location | Expected Impact |
|---|---|---|---|---|
| P0.1 | Unproven submodularity guarantee | Rewrite submodularity claim: restrict to identity γ or provide proof for general γ | Page 7, lines 42-44 | Resolves theory-practice gap; prevents technical rejection |
| P0.2 | Missing limitations | Add dedicated limitations paragraph addressing 4 points | Page 10 (Conclusion) | Increases scientific completeness and defensibility |
| P0.3 | Missing PointNet+Euclidean baseline | Add one row to Table 2 with standard PointNet embedding + k-means | Page 9 (Table 2) | Isolates DBD-specific contribution from representation learning |

### P1 Items (High priority before submission)

| Priority | Issue | Action | Location | Expected Impact |
|---|---|---|---|---|
| P1.1 | Missing submodular-Bregman baselines | Add 2-3 rows with explicit submodular functions as divergences | Page 9 (Table 2) | Directly supports "outperforms submodular Bregman" claim |
| P1.2 | Unsupported "statistical significance" | Add paired t-test p-values for supergradient comparison | Page 9, line 41 | Strengthens quantitative rigor |
| P1.3 | SOTA comparison not controlled | Reproduce MVTN under same split or bound claim to Densepoint comparison only | Page 10, lines 13-15 | Ensures fair comparison |
| P1.4 | Related work unstructured | Restructure into 3 focused sub-paragraphs with connection to DBD | Page 2, lines 38-57 | Clearer positioning |

### P2 Items (Quality improvements)

| Priority | Issue | Action | Location | Expected Impact |
|---|---|---|---|---|
| P2.1 | Method derivation too brief | Add 3-4 lines showing derivation from hY = h1_Y - g2_Y to Eq. (9) | Page 7, Section 4 | Improves readability |
| P2.2 | MNIST qualitative only | Add Spearman correlation between DBD and label Jaccard similarity | Page 8, Section 5.1 | Strengthens illustrative evidence |
| P2.3 | Introduction narrative | Restructure per Option A (problem-driven) storyline | Page 1-2 | Improves reader engagement |
| P2.4 | Parameter count confound | Report and discuss parameter counts of w/ vs w/o decomposition | Page 9, line 45-46 | Acknowledges potential confound |

### Execution Flowchart

```text
P0.1 Fix submodularity claim
  |
  v
P0.2 Add limitations section
  |
  v
P0.3 Add PointNet+Euclidean baseline
  |
  v
P1.1 Add submodular-Bregman baselines -> P1.2 Add significance tests -> P1.3 Fix SOTA comparison
  |
  v
P1.4 Restructure related work -> P2.1 Expand method derivation
  |
  v
P2.2 Add MNIST quantification -> P2.3 Introduction rewrite -> P2.4 Parameter discussion
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | MNIST illustrative (Section 5.1) | n=50,000 sets, M=3,4, 200 epoch triplet training | Qualitative (Figure 1) | DBD assigns smaller values to similar set pairs | DBD is a proper divergence | No quantitative metric; only M=3,4; no baseline comparison |
| E2 | ModelNet40 clustering (Section 5.2) | k-means with DBD, 10 seeds | Rand index | grow-DBD w/ decomp: 0.794 (ε=0), 0.802 (ε=0.001) | DBD outperforms classical metrics | Missing submodular-Bregman baselines; missing PointNet+Euclidean baseline |
| E3 | ModelNet40 set retrieval (Section 5.2) | Top-5 retrieval, K=5, ε=0 | mAP (Table 4) | grow-DBD 90.13, shrink-DBD 90.20 | DBD competitive for retrieval | MVTN (92.9) not reproduced; DBD underperforms by ~2.7 |
| E4 | Ablation: w/ vs w/o DS decomposition (Section 5.2) | Compare Eq. (9) vs single f1 | Rand index, mAP | DS decomposition improves across all supergradient types | DS decomposition adds value | Parameter count confound (two 64x64 vs one 64x128) |
| E5 | Ablation: supergradient type (Section 5.2) | Grow vs shrink vs bar | Rand index, mAP | Bar underperforms grow/shrink | Local info matters | No statistical significance test reported |
| E6 | Ablation: ε=0 vs ε=0.001 (Section 5.2) | Submodular vs strictly submodular | Rand index | Marginal improvement at ε=0.001, not significant | Strictness has modest effect | Effect too small to draw strong conclusions |
| E7 | Softplus activation (Appendix B.1) | Replace ReLU with Softplus | Rand index (Table 3) | Nearly identical to ReLU | Activation choice has negligible impact | Expected result; confirms ReLU choice reasonable |

### Research-Theme Gap Diagnosis

| Research Value Dimension | Evidence Strength | Gap |
|---|---|---|
| **New knowledge:** DBD framework | Strong theoretical contribution | Empirical scope limited to point clouds; novelty unverifiable without retrieval |
| **Reproducibility:** Code provided | Good | MVTN baseline not reproduced; submodularity guarantee proof incomplete for general γ |
| **Impact on practice/understanding:** Could change how discrete divergences are designed | Moderate | Practical advantage over strongest baselines (not just classical metrics) not yet demonstrated |

### Proposed Research Experiments (P0/P1/P2)

**P0 Experiment: PointNet+Euclidean baseline (Must fix)**
- **Target Claim:** DBD gains come from divergence formulation, not just learned representation
- **Hypothesis:** DBD (k-means with learned divergence) outperforms k-means on PointNet embeddings with Euclidean distance
- **Minimal Design:** Train PointNet (64×64 MLP) to produce 64-dim embeddings, run k-means with Euclidean distance, measure Rand index
- **Controls:** Same data splits, same k-means initialization, same number of clustering iterations
- **Metrics:** Rand index
- **Success Criterion:** DBD Rand index > PointNet+Euclidean Rand index by >0.02
- **Estimated Cost:** <1 GPU-hour
- **Expected Quality Gain:** Isolates DBD-specific contribution; validates core claim

**P0 Experiment: Submodular-Bregman baselines (Must fix)**
- **Target Claim:** "Significantly outperforms existing submodular Bregman divergences"
- **Hypothesis:** DBD outperforms divergences from Iyer & Bilmes (2012b) with facility location, log-det, and cut functions
- **Minimal Design:** Compute submodular-Bregman divergences for 3 explicit submodular functions; run k-means; report Rand index in Table 2
- **Controls:** Same k-means procedure, same data
- **Metrics:** Rand index
- **Success Criterion:** DBD Rand index exceeds all submodular-Bregman baselines
- **Estimated Cost:** <2 GPU-hours
- **Expected Quality Gain:** Directly validates main comparison claim

**P1 Experiment: Statistical significance for supergradient comparison (High priority)**
- **Target Claim:** Bar supergradient is "inferior with statistical significance"
- **Hypothesis:** grow-DBD > bar-DBD and shrink-DBD > bar-DBD with p<0.05
- **Minimal Design:** Paired t-test across 10 seeds for (grow-DBD vs bar-DBD) and (shrink-DBD vs bar-DBD)
- **Controls:** Same seed across methods
- **Metrics:** p-value, Cohen's d effect size
- **Success Criterion:** p<0.05 for both comparisons
- **Estimated Cost:** Computational (no new experiments needed)
- **Expected Quality Gain:** Replaces unsupported claim with verified evidence

**P2 Experiment: OOD evaluation on unseen categories (Nice-to-have)**
- **Target Claim:** DBD generalizes to unseen discrete structures
- **Hypothesis:** DBD trained on 30 categories of ModelNet40 transfers well to 10 held-out categories
- **Minimal Design:** Train DBD on 30 categories, evaluate clustering/retrieval on 10 held-out categories
- **Controls:** Same architecture and hyperparameters
- **Metrics:** Rand index, mAP on held-out categories
- **Success Criterion:** Rand index > 0.70 on held-out categories
- **Estimated Cost:** <2 GPU-hours
- **Expected Quality Gain:** Demonstrates generalization and reduces overfitting concern

### Experiment Upgrade Diagram

```text
Stage 1 (P0 — This week):
  [Add PointNet+Euclidean baseline] 
  -> [Add submodular-Bregman baselines]
  -> [Verify DBD advantage is not from representation learning alone]

Stage 2 (P1 — Before submission):
  [Run paired t-test for supergradient comparison]
  -> [Reproduce or bound MVTN comparison]
  -> [Quantify MNIST experiment with Spearman correlation]

Stage 3 (P2 — Quality polish):
  [OOD evaluation on held-out ModelNet40 categories]
  -> [Parameter count control for w/ vs w/o decomposition]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 5.5 / 10

**Rationale:** The paper has a strong theoretical core with clean proofs for strict submodularity and DS decomposition-based divergence construction. The problem framing (learning discrete divergences) is conceptually novel and well-motivated. However, multiple issues reduce the score: (1) the theory-practice gap in the submodularity guarantee of the NN implementation weakens the claimed theoretical grounding; (2) the empirical evaluation lacks critical baselines (PointNet+Euclidean, explicit submodular-Bregman divergences) and the SOTA comparison is uncontrolled; (3) the paper lacks a dedicated limitations section; (4) novelty cannot be externally verified in this retrieval-disabled run. The research value is moderate — the theoretical construction is sound and potentially impactful, but the empirical demonstration is not yet convincing enough to establish DBD as a practically superior alternative to learned set representations.

**Post-Revision Target:** [6.5, 7.5] / 10

**Conditional on completing the following P0 items:**
- Resolving the theory-practice gap (clarifying submodularity guarantee)
- Adding PointNet+Euclidean and submodular-Bregman baselines
- Adding a limitations section
- Providing statistical tests for supergradient comparison
- Restructuring the related work and introduction narrative

If these P0 items are addressed satisfactorily, the paper would present a rigorous theoretical contribution with substantially stronger empirical support, moving toward the [6.5, 7.5] range depending on the strength of the controlled comparisons.