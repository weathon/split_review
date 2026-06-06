Now I have sufficient information to write the final consolidated review. Let me synthesize the findings carefully.

---

## Summary

This paper identifies post-treatment selection — the selective inclusion of samples in datasets after interventions — as a fundamental and underexplored challenge in interventional causal discovery with latent confounders. The authors show that post-treatment selection creates the same conditional independence (CI) signature as genuine causal relations, making them non-identifiable under existing frameworks (Figure 1). To resolve this, they introduce an augmented DAG formulation (Definition 1), a new FI-Markov equivalence class (Definition 2, Theorem 2), a novel graphical representation called the F-PAG (Definition 5), and a provably sound and complete algorithm F-FCI (Algorithm 1, Theorems 3–4) that uses differential reactions of selection and causation to additional interventions for disambiguation. Experiments on synthetic data and the Norman gene perturbation dataset support the approach.

---

## Strengths

- **Concrete, well-motivated non-identifiability problem (Figure 1):** The paper precisely shows, through paired motivating examples, that post-treatment selection produces the same variant-marginal / invariant-conditional CI pattern as genuine direct causation — and that current methods cannot distinguish them. This is a specific, verifiable theoretical gap that directly motivates the entire contribution.

- **Rigorous formal framework grounded in augmented DAGs:** Definition 1 embeds the selection variable S and intervention indicators ψ into an augmented DAG with an explicit factorization (Eq. 1). Theorem 1 links d-separation in the augmented DAG to observable CI and invariance patterns, providing a principled generative model that bridges the formal and empirical settings. Lemmas 2–4 derive graphical criteria for edge marks under interventions.

- **Well-structured characterization of the new equivalence class:** Theorem 2 gives a clean graphical characterization of FI-Markov equivalence (same skeleton, v-structure, marks, and edges among intervened nodes), and Definition 5 introduces the F-PAG as a maximally informative representation that distinguishes direct causal links, latent confounder edges, inducing paths, and selection-mediated dependencies — captured by a new mark vocabulary (□, ▲, ►).

- **Provably sound algorithm with an elegant disambiguation mechanism:** Theorem 3 establishes soundness. Step 2.3 of Algorithm 1 is the most distinctive contribution: it uses hard interventions on Type I inducing nodes along inducing paths to test CI(ψ_n, X_i), thereby distinguishing a direct causal link from a selection-mediated dependence in cases where endpoint CI patterns alone are insufficient. This mechanism is novel and well-justified.

- **Real-world application to gene perturbation data:** Section 5.2 applies the framework to the Norman scRNA-seq perturbation dataset. The identification of quality-control-driven selection patterns (cells that fail quality control) as selection nodes, alongside causal regulatory links validated via Enrichr, is a credible and biologically relevant demonstration.

---

## Weaknesses

### Fatal

None.

### Major

- **Evaluation design makes outperformance partially expected.** All baselines in Figure 6 (GIES, IGSP, UT-IGSP, JCI-GSP, FCI-interven, CDIS) are explicitly not designed to handle post-treatment selection, yet all experiments are conducted on data generated *with* post-treatment selection. The result is that every baseline conflates selection-induced dependencies with causal links, while F-FCI correctly attributes some to selection — leading to both higher DAG Precision and lower SHD almost by design. Crucially, the primary metric, DAG Precision, rewards conservative edge prediction: F-FCI, by correctly attributing some dependencies to selection (and thus not predicting those as causal edges), will naturally output fewer edges, mechanically inflating its precision relative to methods that commit to all observed dependencies. This means the experiment largely answers "does explicitly modeling selection beat not modeling it?" rather than "does F-FCI recover the true causal structure accurately?" Table 1 (selection identification) is a more direct test of the paper's core contribution — correctly identifying which dependencies are causal and which are selection-induced — but it is reported only in the appendix. The authors should elevate this test to the main paper and complement Figure 6 with at least one condition where selection is absent (to confirm F-FCI does not degrade relative to baselines in the standard setting).

### Minor

- **Completeness claim is overstated in the abstract and introduction.** The abstract says "provably sound and complete algorithm," but Theorem 4 is specifically bounded: it guarantees identification of substructures (tail, arrowhead, square, ►, ◄) between pairs of intervened nodes identifiable via CI patterns — which explicitly excludes inducing paths composed solely of Type II inducing nodes. The limitations section (Section 6) acknowledges this: "The identification of direct causal links and selection structures depends critically on the presence of Type I inducing nodes. One future direction is how to identify the causal structure along inducing paths composed solely of Type II inducing nodes." This is a non-trivial gap — Type II paths (□□ patterns) arise naturally in many graph structures. The theorem statement itself should include this side condition rather than leaving it to the conclusion section; readers citing Theorem 4 as "completeness" will be misled.

- **Preconditions for the disambiguation step are understated.** Step 2.3 requires that interventions be available on Type I inducing nodes to resolve ○→ ambiguity. This is a non-trivial experimental requirement — in practice, the relevant intermediate variables may not be in the intervention target set I. The paper does not explicitly state this as a precondition for the completeness guarantee, nor does it evaluate how often the required Type I nodes are accessible in the synthetic benchmarks or the Norman application.

### Trivial

None that survive filtering.

---

## Nice-to-Haves

- An ablation or focused analysis of Step 2.3 (Type I inducing node disambiguation) would substantially strengthen the empirical story: how often do Type I nodes arise in the random graphs tested? How often does Step 2.3 change an orientation? What is F-FCI's precision specifically on pairs where disambiguation was invoked? This would ground the mechanism in demonstrated empirical behavior rather than theoretical promise.

- A targeted demonstration on the motivating examples from Figure 1 — explicitly constructing paired ground-truth settings (direct causation vs. selection-mediated dependence) and showing F-FCI's recovery in each — would be far more convincing than the aggregate statistics in Figure 6.

- Table 1 (selection identification) belongs in the main paper body as the most direct test of the core claim.

- A condition in the synthetic experiments with no post-treatment selection would clarify that F-FCI does not sacrifice accuracy relative to standard methods when the problem being solved is absent.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Algorithm rendering problem in Step 2.2 (Harsh Critic):** The critic notes that all six orientation rules in Step 2.2 show `(⊥,⊥,⊥,⊥)` — identical CI patterns — which is a PDF parsing artifact. Per hard rules, this is a formatting/parser artifact that should not be attributed to the authors. The paper's original submission almost certainly has distinct CI patterns for each rule (consistent with Figure 4). REMOVED.

2. **Noise distribution Unif([0,2]∪[2,4]) is unusual (Harsh Critic):** The critic says the motivation for this bimodal uniform is not given and makes replication difficult. This is a trivial implementation detail in a simulation study; the exact distribution is specified and the choice does not affect the validity of the evaluation. REMOVED per reproducibility nitpick rule.

3. **Proportions of f and f_s not specified (Harsh Critic):** Minor simulation detail that falls under "trivial implementation details not expected to be disclosed." REMOVED.

4. **The paper addresses an important problem (Strength Finder, generic claim):** Generic, non-evidence-based strength. REMOVED.

---

## Novel Insights

The central insight — that post-treatment selection creates the exact same CI signature as direct causation (variant marginal, invariant conditional after intervention on the cause), making the two cases non-identifiable under all existing interventional causal discovery frameworks — is genuinely novel and consequential. The mechanism to break this non-identifiability by exploiting the differential reaction of selection and causation to *additional* interventions on intermediate Type I nodes is elegant. The result implies that seemingly thorough interventional experimental designs can still be confounded by upstream quality-control selection processes (a pervasive reality in genomics), and that resolving this requires a richer equivalence class and a finer-grained graphical representation than PAGs. The F-PAG and its new mark vocabulary for selection-induced vs. causation-induced inducing paths may find independent use in other causal reasoning contexts beyond the F-FCI algorithm itself.

---

## Suggestions

1. Rewrite the completeness claim in the abstract and Theorem 4's statement to explicitly scope it: "sound and complete for all structures identifiable via Type I inducing nodes" and include the Type II limitation as a formal side condition, not just a limitation in Section 6.
2. Elevate Table 1 (selection identification) to the main paper as the primary evaluation of the core contribution.
3. Add a baseline condition with no post-treatment selection in the synthetic experiments to verify F-FCI does not degrade in the standard setting.
4. Report, within Figure 6 or a supplemental breakdown, the fraction of correctly identified causal edges vs. correctly identified selection-induced dependencies, rather than only aggregate DAG Precision and SHD.
5. Explicitly state in Algorithm 1 that Step 2.3 requires interventions to be available on the relevant Type I inducing nodes, and discuss what happens when this condition is not met.

---

**Originality:** High. The problem formulation (post-treatment selection in interventional discovery) and the F-PAG/F-FCI framework are genuinely new. The connection between selection-node reactions to interventions and disambiguation is novel.

**Importance:** High. Post-treatment selection is a real and pervasive issue in biological causal discovery (quality control in genomics), and the paper identifies a concrete gap in all existing methods.

**Claims supported:** Moderate. The theoretical claims (soundness, qualified completeness, equivalence characterization) appear well-supported. The empirical claims of superiority are largely supported, but the evaluation design limits their informativeness because all comparisons are against methods not designed for the problem being solved.

**Soundness of experiments:** Moderate. The simulation setup is reasonable and the real-world application is appropriate, but the evaluation conflates "outperforms methods blind to selection" with "accurately recovers causal structure," and the most informative test (Table 1) is in the appendix.

**Clarity:** Good. The paper is well-organized, the motivating examples are clear, and the theoretical development follows logically. The completeness qualification buried in Section 6 is the main clarity issue.

**Value to research community:** High. Both the theoretical framework and the practical implication (selection bias from quality control in genomics is a causal confound that requires explicit modeling) are valuable contributions.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>