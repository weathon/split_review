Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes a distributed method for exact structure learning of Bayesian networks. The core idea is to partition the variable set into an overlapping cover such that each subset forms a *conditional P-map* given its boundary nodes. Each subset's structure can then be learned independently by any P-map learner (constraint- or score-based), and the results are stitched together via a boundary-resolution procedure. The paper claims the output is provably a P-map, distinguishing it from approximate distributed approaches.

## Strengths

- **Conceptually novel framework for exact distributed learning.** The conditional P-map reduction (Definitions 3.2–3.3) is a meaningful formalization that generalizes the simple independence-based partitioning of Example 1 to cases where subsets are only conditionally separable given boundary nodes. This goes beyond prior distributed methods that either approximate or require high-order CI tests/expert knowledge.

- **Low-order conditioning set.** Unlike prior exact distributed algorithms (Xie et al., 2006; Liu et al., 2017) that rely on high-order conditioning or expert knowledge, the approach bounds the conditioning set by a user-specified *W* (set to *W* = 1 in experiments). This is a practically relevant design choice.

- **Flexible learner-agnostic design.** Algorithm 1 is specified to work with any P-map learner (constraint- or score-based), as stated in the abstract and in Algorithm 1 (step 3: "Gi ← P-map learner(Xi)"). The framework does not depend on a particular local learning algorithm.

- **Empirical speedup on standard benchmarks with no accuracy loss in the measured regime.** On 7 benchmark networks (ASIA, ALARM, INSURANCE, etc.), Algorithm 1 runs up to 2× faster than serial PC (p = 0.01, Wilcoxon signed-rank test), while the structural Hamming distance (Table 2) remains comparable. The speedup is statistically significant on this testbed.

## Weaknesses

### Fatal

None. The conceptual approach (conditional P-map reduction) is coherent and addresses a genuine problem; no single flaw invalidates the paper's core thesis.

### Major

- **Experiments do not support the scalability claims made in the abstract and conclusion.** The paper claims to enable structure learning for a "giant number of variables" with "significant reduction in computation time." However, all experiments are on small, decades-old benchmark networks (≈8–70 variables) — problems where serial PC already runs in seconds to minutes. The observed speedup is at most 2× using **30 CPUs**, which is not evidence of scalability to large problems. No experiments are shown on graphs where centralized learning is infeasible (e.g., n > 200), nor is there any analysis — theoretical or empirical — of how the method scales as *n* grows. A 2× speedup with 30 CPUs on a 70-variable problem does not demonstrate that the method enables structure learning where it was previously impossible.

- **No comparison against any existing distributed or parallel structure-learning baseline.** The experiments compare only against serial PC. The paper itself cites Zarebavani et al. (2019) for parallel CI tests and Gu & Zhou (2020) for approximate distributed learning, yet neither is included as a baseline. The reader cannot assess whether the method improves upon or trades off against the closest related approaches. A paper proposing a *distributed* method should at minimum benchmark against other approaches that exploit parallelism.

### Minor

- **The main-text description of Algorithms 2 and 3 (the cover-finding step) is too sparse to assess the method's practical feasibility.** Algorithm 2 is described in a single paragraph (line 99): it iterates over components, picks the greatest, and "checks if any subset 𝒲 ⊂ 𝒰 separates the component." The paper mentions the power set 𝒫(𝒰), suggesting an exponential search, but provides no analysis of worst-case complexity, no guarantee of termination in polynomial time, and no pseudocode or complexity characterization. Algorithm 3 — which was actually used in the experiments — is mentioned but its mechanism is entirely absent from the main text. This makes it difficult for a reader to evaluate whether the cover-finding step itself is tractable, or under what conditions it succeeds. (Full pseudocode may exist in the stripped appendix, but the main text should provide enough structure for an informed assessment.)

- **No sensitivity analysis for key parameters *d* and *W*.** The experiments fix *d* = 0.75*n* and *W* = 1 without exploring how performance changes with these parameters. Since the trade-off between cover-element size, number of CI tests, and runtime is discussed qualitatively in the conclusion (lines 117–118), an ablation study would substantially strengthen the empirical section.

- **The theoretical justification for why local PC correctly learns interior edges given only the conditional P-map property is presented too concisely.** Lines 86–87 argue that conditional P-map condition (ii) ensures PC will not miss edges and will correctly identify missing edges, but the main text defers to "see Remark A" for a key part of the reasoning. Given that the local learner operates on the marginal distribution of 𝒳ᵢ — which may not be faithful even though 𝒢[𝒳ᵢ] is a conditional P-map given bd(𝒳ᵢ) — a fuller intuitive explanation in the main text would help. The conceptual gap the paper must bridge is: PC on 𝒳ᵢ tests CIs over subsets of 𝒳ᵢ (which includes boundary nodes), and the conditional P-map property ensures that d-separations in 𝒢[𝒳ᵢ] correspond to CIs in P[𝒳ᵢ] *when the right boundary nodes are conditioned on*. The paper should explain more clearly why PC's systematic search over conditioning subsets within 𝒳ᵢ will encounter these subsets.

### Trivial

None.

## Nice-to-Haves

- A complexity analysis of the cover-finding step (Algorithm 2 or 3), identifying conditions under which it runs in polynomial time (e.g., bounded treewidth, bounded *W*).
- An experiment on a synthetic or real graph with n > 200 where serial PC fails (time or memory) to demonstrate the method's practical value in the "giant" regime.
- Reporting runtime breakdown (cover-finding vs. local learning vs. boundary resolution) to understand where parallel resources are spent.

## Removed Points

These points from the input reviews are flagged to be removed; treat them with caution:

- **"No algorithm for the core step provided"** (from Harsh Critic): Overstated. The paper provides Algorithm 1 and a paragraph description of Algorithm 2. Full pseudocode likely exists in the appendix, which was stripped by the parser. The main-text description is sparse (retained as a Minor weakness above), but saying "no algorithm" is inaccurate.

- **"Theoretical framework has gaps that affect soundness — no proof in main text"** (from Harsh Critic): The paper refers to "Remark A" in the appendix for the formal proof. Per the review guidelines, criticisms of missing appendix content that was stripped by the parser should be removed. The retained minor weakness above captures the reasonable concern that the main-text intuitive explanation is terse, without penalizing the paper for an absent appendix.

- **"Wilcoxon signed-rank test p-value 0.01 with 7 datasets is borderline"**: p = 0.01 is below the standard 0.05 threshold; this criticism is factually incorrect as stated.

- **"SHD reported without standard deviations or confidence intervals"**: SHD is a per-dataset discrete quantity; standard deviations are not standardly reported for this metric. Generic methodology nitpick.

- **"The algorithm's power-set search would be intractable"** (speculative): The paper mentions 𝒫(𝒰) but does not specify that the algorithm searches all subsets exhaustively in practice. Algorithm 3 (used in experiments) may use a different approach. Without seeing the full algorithm, this speculation about intractability is not a verified weakness. Retained as a Minor concern about missing complexity analysis.

- **Strength Finder: "Reduces memory demand"**: A claimed benefit without experimental demonstration. Generic.

- **Strength Finder: "Strongest evidence is the theoretical proof"**: The proof is in the stripped appendix and cannot be verified from the main text alone; this strength overstates what is verifiable.

- **Harsh Critic's discussion of prior work being "superficial"**: The paper discusses relevant prior work (Gu & Zhou 2020, Xie et al. 2006, Liu et al. 2017, Zarebavani et al. 2019) which is appropriate for a conference paper. No specific missing reference was identified with evidence; per the rules, missing related works should not be mentioned.

## Novel Insights

A genuinely novel observation that emerged across the reviews is that the paper's core difficulty mirrors the classic problem of distributivity in graphical models: even when the global graph is decomposable by separators, the local faithfulness required for constraint-based learning may not hold in the marginal distributions over subsets. The paper attempts to resolve this with the "conditional P-map" concept, which weakens the faithfulness requirement to hold only after conditioning on boundary nodes. Whether this relaxation is sufficient for exact local recovery is the crux of the paper's theoretical claim, and neither review fully resolves this point from the main text alone. The reviews collectively highlight that this gap — between a conditional P-map existing and a local learner correctly recovering it — is where the paper needs its strongest justification, yet the main text defers to the appendix.

## Suggestions

1. **Strengthen the experimental section.** Add experiments on larger graphs (n > 200), either synthetic (e.g., randomly generated DAGs with known structure) or from larger benchmark suites. Show runtime and accuracy for at least one configuration where the serial PC cannot complete within a reasonable time/memory budget. This is critical to substantiate the "giant number of variables" claim.

2. **Include at least one distributed/parallel baseline.** Compare against Zarebavani et al. (2019) (parallel CI tests) or a sensible approximate distributed method to contextualize the speed–accuracy trade-off.

3. **Provide a complexity characterization of the cover-finding step.** State the worst-case complexity of Algorithm 2/3 in terms of *n*, *d*, and *W*, or identify structural conditions (e.g., bounded treewidth, bounded separator size) under which the cover can be found in polynomial time.

4. **Add a parameter sensitivity study.** Vary *d* and *W* across a range of values on one or two datasets and report the effect on runtime, cover structure, and accuracy.

5. **Clarify the link between conditional P-maps and local learning.** Provide a short concrete example or diagram showing how PC, operating on the marginal distribution of a cover element, correctly identifies an interior edge that would only be discoverable by conditioning on boundary nodes. This would bridge the conceptual gap for readers.

## Score and Decision

**Originality**: The conditional P-map reduction is a novel conceptual contribution. The distributed exactness claim is a genuine step beyond prior approximate approaches.

**Importance**: Exact structure learning is a well-known hard problem. A distributed exact method would be impactful if it truly scales. The paper tackles an important question.

**Claims support**: The core exactness claim is presented with theoretical scaffolding but the experiments provide only weak evidence for the scalability claim. The paper's ambition (enabling "giant" problems) is not matched by the experimental demonstration.

**Soundness**: The theoretical framework (Definitions 3.2–3.4, Problem 2) is internally consistent. The main gap is that the cover-finding algorithms are underspecified in the main text and the key proof is deferred to the appendix. The experimental methodology is adequate for the small-scale regime but insufficient for the paper's advertised scope.

**Clarity**: The paper is generally well-written and the intuition (Example 1, Figure 1) is helpful. The algorithm descriptions are the weakest part in terms of clarity.

**Value**: The paper lays conceptual groundwork for exact distributed structure learning. If the theoretical claims hold and the method can be shown to scale, it would be a valuable contribution. However, in its current form, the evidence is insufficient to recommend acceptance.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>