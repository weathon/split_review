## Summary
This paper proposes Hebbian View Orthogonal Projection (HVOP), a framework for **view incremental learning** — a novel multi-view setting where feature views arrive sequentially rather than being available all at once. The core technical idea is to use an orthogonal projection mechanism (projecting new-view gradients to be orthogonal to the subspace spanned by prior-view representations) to prevent "view forgetting." The paper substitutes computationally expensive SVD-based principal component extraction with Oja's rule (a Hebbian learning variant), framed as a bio-plausible implementation. Experiments on six node-classification datasets demonstrate competitive or superior accuracy compared to both static multi-view methods and continual learning baselines.

**Core contributions (author-claimed):**
- **C1:** Introduction of the **view incremental learning** paradigm, distinct from task/class-incremental continual learning.
- **C2:** HVOP with **Knowledge Transfer Space (KTS)** and orthogonal projection to mitigate view forgetting.
- **C3:** Bio-inspired implementation using **recursive lateral connections + Oja's rule** to replace SVD-based PCA for dynamic subspace estimation.

**Strengths:** The paper addresses an interesting and practical problem (sequential multi-view learning). The combination of orthogonal projection with Hebbian learning is conceptually novel. The experimental evaluation across six datasets is reasonably broad.

**Weaknesses:** The mathematical derivation of the orthogonal projection equivalence (Eq. 8 vs. Eq. 4) is incomplete without orthonormality constraints on R. The neuroscience claims are metaphorical rather than mechanistically grounded. Several key implementation details (dimensions, convergence, hyperparameters) are missing, affecting reproducibility. The conclusion overclaims generalization and "first-time" priority. Novelty cannot be fully assessed without external retrieval (deferred to manual verification).

## Strengths
1. **Novel problem formulation.** The view incremental learning setting — where feature views arrive sequentially and must be integrated without forgetting — is practically relevant (medical imaging, sensor fusion, social networks) and clearly distinguished from existing task/class incremental learning paradigms.

2. **Conceptually elegant mechanism.** The combination of orthogonal gradient projection and Hebbian learning (Oja's rule) is a neat way to replace static SVD-based PCA with an online, adaptive alternative. The idea of using a single mechanism (recursive lateral connections) to approximate both subspace estimation and gradient projection is aesthetically pleasing.

3. **Broad empirical evaluation.** Six multi-view datasets (Animals, Flower17, Iaprtc12, NGs, NoisyMNIST_15000, YaleB_Extended) spanning different domains and feature types, with four metrics (ACC, Precision, Recall, Macro-F1). The comparison includes both static multi-view methods and incremental learning baselines.

4. **Ablation and analysis experiments.** The paper includes a view forgetting analysis (Fig. 4), single-view comparison (Fig. 5), loss convergence (Fig. 6a), and view-order analysis (Fig. 6b), providing some insight into the method's behavior beyond final accuracy numbers.

5. **Consistent performance advantage.** HVOP achieves the highest accuracy on 5 out of 6 datasets among incremental methods, and outperforms all static methods on NGs, demonstrating competitive or superior performance in the incremental setting.

## Weaknesses
1. **Mathematical incompleteness in core mechanism (Major).** The claimed equivalence between the SVD-based orthogonal projection (Eq. 4: P = I - K K^T) and the bio-plausible version (Eq. 8: P' = I - R^T R) requires R to have orthonormal rows (R R^T = I). The Oja rule (Eq. 9) does not enforce this constraint. Without it, P' is not an orthogonal projection matrix, and the gradient modification may not actually prevent interference. This is a technical gap that could invalidate the core contribution.

2. **Unsupported neuroscience claims (Major).** The paper repeatedly claims "brain-like dynamic adaptability," "simulating lateral connections in neural circuits," and KTS being "akin to regions in the hippocampus." These are metaphorical assertions without mechanistic evidence. No biological data, neural recordings, or cognitive psychology experiments are presented. This framing risks overclaiming and may mislead readers about the model's biological fidelity.

3. **Missing gradient projection baseline (Major).** The most closely related method — Gradient Projection Memory (GPM, Saha et al., ICLR 2021) — is mentioned briefly ("Inspired by Saha et al.") but not properly cited in the references or included as an experimental baseline. Since HVOP's core mechanism directly extends GPM to the view-incremental setting, this omission undermines the novelty assessment and comparison fairness.

4. **Figure reference inconsistency (Minor).** On Page 2, the text refers to "Fig. 2(a)" but the figure is labeled "Figure 1." This is a basic formatting error that suggests incomplete manuscript polishing.

5. **Vague evaluation questions (Minor).** EQ1-EQ3 (Page 7) use subjective terms ("superior performance," "tight association") without quantified success criteria. This makes the experimental section less rigorous.

6. **Insufficient quantitative forgetting analysis (Minor).** Definition 3.1 provides a precise forgetting formulation (F_{v,V} < F_{v,v}), but the experimental section (Section 4.2) only provides qualitative visual inspection of forgetting curves. No numeric forgetting rates are reported.

7. **Conclusion overclaim and missing limitations (Minor).** The conclusion states "for the first time" without literature verification and claims "adaptability and generalization" without OOD experiments. No explicit limitations section is provided.

## Key Issues
### Key Issue 1: Orthogonal projection equivalence is mathematically incomplete [Page 6 - Section 3.3-3.4]

**Severity: Major | Validity Risk: High | Fixability: High**

The core technical claim is that P' = I - R^T R (Eq. 8) is equivalent to the orthogonal projection P = I - K K^T (Eq. 4), with R learned via Oja's rule (Eq. 9) replacing the static SVD-extracted K. However, this equivalence requires R to have orthonormal rows (R R^T = I), which Oja's rule does not guarantee on its own. Without this, P' is not an orthogonal projection, and the gradient modification may not prevent interference with old-view subspaces.

**Root cause:** The paper assumes that Oja's rule approximates principal components, but does not enforce that R maintains orthonormal rows for the projection matrix to be valid.

**Fix path:** Add an explicit orthonormalization step (e.g., R ← R (R^T R)^{-1/2}) after each Oja update, or cite a variant of Oja's rule that automatically maintains orthonormality.

---

### Key Issue 2: Neuroscience claims are meta- phorical, not mechanistic [Page 3 - Introduction bullet points]

**Severity: Major | Validity Risk: Medium | Fixability: High**

The paper claims its mechanisms are "brain-like," "simulating lateral connections," and KTS is "akin to the hippocampus." These are framed as direct neural implementations, but no biological constraints (e.g., Dale's law, locality, timescales, or connectivity patterns) are imposed. The scientific risk is that the neuroscience framing may be perceived as overclaiming by reviewers.

**Root cause:** The paper uses neuroscience terminology for algorithmic components without respecting the biological constraints of those terms.

**Fix path:** Reframe as "computationally inspired by" not "simulating." Remove or qualify hippocampal analogy unless neural constraints are added.

---

### Key Issue 3: Missing GPM citation and baseline [Page 6 - Section 3.3]

**Severity: Major | Validity Risk: Medium | Fixability: High**

The orthogonal projection mechanism is explicitly "inspired by Saha et al." (Gradient Projection Memory, ICLR 2021), but this work is not cited in the references and not included as an experimental baseline. GPM is the closest methodological relative.

**Root cause:** Manuscript oversight in reference management.

**Fix path:** Add full GPM citation, discuss differences (task-inc vs. view-inc, SVD vs. Oja), and include GPM as an incremental baseline if feasible.

---

### Key Issue 4: Unfair baseline comparison [Page 8 - Table 1]

**Severity: Major | Validity Risk: Medium | Fixability: Medium**

Static multi-view methods (DUANet, LGCNFF, RCML) access all views simultaneously, while incremental methods process views sequentially. The paper presents these in one unified table without explicitly acknowledging this structural advantage. The claim "outperforms both traditional and state-of-the-art multi-view learning methods" (Abstract) conflates these two categories.

**Root cause:** The table and narrative do not separate the comparison by information-access regime.

**Fix path:** Add a table note clearly distinguishing all-at-once vs. sequential access. The primary comparison should focus on incremental baselines, while static methods serve as upper-bound references.

---

### Key Issue 5: Reproducibility gaps [Page 5-7 - Method section]

**Severity: Major | Validity Risk: High | Fixability: High**

Several critical details are missing:
- The dimensions and derivation of x_t and y_t in Oja's rule (Eq. 9) are not specified relative to the GCN output Z_v.
- The hyperparameter k (number of principal components in K) is not reported.
- Learning rate η for Oja's rule and its schedule are unspecified.
- The loss weight/balancing between L_RE and L_CE is not provided.
- The kNN parameter for graph construction is not given.

**Root cause:** The method section prioritizes high-level description over implementation precision.

**Fix path:** Add a hyperparameter table summarizing all settings per dataset (k, η, α, training epochs, optimizer, learning rate).

## Actionable Suggestions
### S1 (Must): Fix the orthonormality gap in the projection [Page 6 - Section 3.3-3.4]

**Problem:** P' = I - R^T R is not an orthogonal projection unless R R^T = I. The Oja rule does not enforce this.

**Action:** Add one of the following: (a) after each Oja update, orthonormalize R via R ← R (R^T R)^{-1/2}; or (b) use a variant of Oja's rule that maintains orthonormality (e.g., the symmetric Orthogonal Oja rule); or (c) add a regularization loss λ∥R R^T - I∥_F^2. Then rerun experiments to verify the projection still works and report the subspace alignment error ∥KK^T - R^T R∥_F as a sanity check.

### S2 (Must): Tone down neuroscience claims [Page 3, also Abstract and Page 3 conclusion paragraph]

**Problem:** "Brain-like dynamic adaptability," "simulating lateral connections," KTS "akin to hippocampus" — these are metaphorical, not mechanistic.

**Action:** Replace all instances with bounded language:
- "Lateral connections" → "recursive feature integration mechanism"
- "Hippocampus-like" → "a feature subspace for knowledge preservation"
- "Brain-like" → "computationally inspired by neural principles"
Add a caveat in the introduction: "The neuroscience connection is at the level of computational principle, not biological simulation."

### S3 (Must): Add GPM reference and context [Page 6, References]

**Problem:** "Inspired by Saha et al." appears without proper citation. GPM (ICLR 2021) is the direct methodological predecessor.

**Action:** Add the full citation: "Saha, G., Garg, I., & Roy, K. Gradient Projection Memory for Continual Learning. ICLR 2021." Discuss differences in a related-work paragraph: GPM operates in task-incremental setting with task boundaries; HVOP extends to view-incremental setting without boundaries and replaces SVD with Oja's rule for online adaptation.

### S4 (Must): Add hyperparameter details [Method Section]

**Action:** Add a table (Table 2) reporting for each dataset: feature dimensionality per view, number of views V, number of samples n, number of classes c, kNN parameter, number of principal components k (in K), learning rate η for Oja's rule (Eq. 9), mixing coefficient α (Eq. 7), and training epochs/iterations per view.

### S5 (Nice-to-have): Quantify forgetting [Page 9 - Section 4.2]

**Action:** Compute and report average forgetting rate Forgetting = (1/(V-1)) Σ_{v=1}^{V-1} (F_{v,v} - F_{v,V}) for each dataset, with standard deviations. Add a t-test comparing HVOP vs. GCN forgetting.

### S6 (Nice-to-have): Reframe baseline comparison [Page 8 - Table 1]

**Action:** Add a table footnote: "Static methods access all views simultaneously (upper-bound reference); incremental methods process views sequentially." Move the comparison emphasis to incremental baselines.

### S7 (Nice-to-have): Add limitations section [Page 10 - Conclusions]

**Action:** Add a standalone "Limitations" paragraph listing: kNN parameter sensitivity, single-layer GCN only, projection only on classifier layer, no OOD generalization verification, Oja convergence in non-stationary setting not analyzed.

## Storyline Options + Writing Outlines
### Abstract Outline (Recommended — 5-sentence structure)

**S1 (Problem):** "In multi-view learning, views often arrive sequentially over time; however, existing methods assume all views are available simultaneously and suffer catastrophic 'view forgetting' when new views are introduced."

**S2 (Gap):** "This setting — view incremental learning — differs from task/class incremental learning because the task remains the same while the feature representation changes, requiring both knowledge preservation and cross-view transfer."

**S3 (Method):** "We propose Hebbian View Orthogonal Projection (HVOP), which constructs a Knowledge Transfer Space and projects new-view gradients orthogonally to old-view subspaces, preventing interference while enabling knowledge transfer."

**S4 (Implementation):** "HVOP replaces costly SVD recomputation with a recursive lateral connection mechanism trained via Oja's rule, enabling online adaptation to new views."

**S5 (Result):** "On six node-classification datasets, HVOP achieves consistent accuracy improvements over incremental baselines while maintaining stable performance on earlier views, reducing average forgetting from >15% (GCN) to <5%."

---

### Introduction Outline (Recommended — 5 paragraphs)

**P1 — The Problem (Page 1):** Open with a concrete example: medical imaging where a model trained on CT scans must later incorporate MRI without forgetting. State the research question: how to learn from incrementally arriving views while preserving prior knowledge. **Current issue:** paragraph opens with generic brain analogy.

**P2 — Prior Work Gap (Page 1):** Briefly describe traditional multi-view learning (all-views-at-once) and continual learning (task/class increments). Point out that neither addresses view incremental learning — where the task is the same but feature views change. **Current issue:** too many application-domain citations; condense.

**P3 — View Forgetting Mechanism (Page 2):** Explain intuitively why gradient interference causes view forgetting (weight update for new view may increase loss on old views). State the orthogonal projection solution: constrain ΔW such that ΔW x_old ≈ 0. Fix the figure reference (Fig 1, not Fig 2). **Current issue:** figure reference mismatch.

**P4 — Proposed Method (Page 2-3):** Present HVOP in three principles: (1) orthogonal gradient projection via KTS, (2) online subspace estimation via Oja's rule, (3) recursive integration. Frame neuroscience as "computational inspiration" not "biological simulation." Remove hippocampus analogy unless constrained.

**P5 — Contributions and Results (Page 3):** Summarize the three contributions concisely. Preview experimental results: six datasets, consistent improvements, forgetting analysis.

---

### Title Recommendation

**Current:** "Brain-inspired Multi-View Incremental Learning for Knowledge Transfer and Retention"
**Suggested:** "HVOP: Orthogonal Gradient Projection for View Incremental Learning via Hebbian Subspace Estimation"

The suggested title removes the vague "brain-inspired" modifier and instead communicates the mechanism (orthogonal gradient projection), the problem setting (view incremental learning), and the technical innovation (Hebbian subspace estimation).

## Priority Revision Plan
| Priority | Action | Section Affected | Effort | Impact | Type |
|----------|--------|-----------------|--------|--------|------|
| P0 | Fix orthonormality constraint in projection (add normalization or regularization for R) | Section 3.3-3.4 | Medium | Core validity | Must |
| P0 | Tone down neuroscience claims throughout (meta- phorical → computational inspiration) | Abstract, Intro, Conclusion | Low | Credibility | Must |
| P0 | Add GPM citation and baseline discussion | Section 2, References | Low | Completeness | Must |
| P1 | Add hyperparameter table (k, η, α, epochs, kNN) | Section 3 | Low | Reproducibility | Must |
| P1 | Quantify forgetting metric (average F_{v,V} - F_{v,v}) | Section 4.2 | Low | Rigor | Must |
| P1 | Reframe Table 1 with access-type distinction | Section 4.1 | Low | Fairness | Nice-to-have |
| P2 | Add convergence metrics across 3+ datasets | Section 4.4 | Medium | Robustness | Nice-to-have |
| P2 | Add limitations paragraph | Section 5 | Low | Completeness | Nice-to-have |
| P2 | Add OOD generalization experiment (cross-dataset) | Section 4 | High | Scope | Nice-to-have |

### Revision Roadmap

```text
ASCII Diagram — Revision Strategy Roadmap

[Phase 1 — Core Fixes (3-5 days)]
  P0: orthonormality fix → rerun experiments → verify P' ≈ P
  P0: neuroscience language cleanup → abstract, intro, conclusion
  P0: add GPM citation + related work paragraph

[Phase 2 — Reproducibility & Rigor (2-3 days)]
  P1: hyperparameter table
  P1: forgetting metric computation + table
  P1: Table 1 footnote on access-type distinction

[Phase 3 — Robustness & Completeness (3-5 days)]
  P2: convergence analysis across 3 datasets
  P2: limitations paragraph
  P2: optional OOD generalization experiment
```

### Expected Impact After Fixes

1. **Fix orthonormality**: Core mechanism becomes mathematically valid; replicability restored.
2. **Language toned down**: Reviewer trust improved; no risk of perception as overclaiming.
3. **GPM discussion**: Novelty positioning clarified — HVOP extends GPM to view-incremental setting with Oja-based dynamic subspace estimation.
4. **Hyperparameter table + forgetting metric**: Paper becomes reproducible; empirical claims are backed by quantitative evidence.
5. **Limitations paragraph**: Demonstrates scientific maturity and honest scope awareness.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 (Sec 4.1) | HVOP achieves superior accuracy vs. baselines | 6 datasets, 7 baselines (DUANet, LGCNFF, RCML, GAT, SI, MAS, MVCIL) | ACC, P, R, Macro-F1 | HVOP best on 5/6 datasets | C2 (KTS+orthogonal proj) | No GPM baseline; static methods have unfair advantage |
| E2 (Sec 4.2) | HVOP alleviates view forgetting vs. GCN | 2 datasets (NGs, Animals), per-view accuracy tracking | Per-view accuracy (visual only) | HVOP declines smoother than GCN | C2 (forgetting relief) | No quantitative forgetting metric reported |
| E3 (Sec 4.3) | HVOP enables knowledge transfer vs. single-view | 2 datasets (Flower17, YaleB_Extended) | Accuracy over views | HVOP > single-view accuracy | C3 (knowledge transfer) | Only 2 datasets; single-view baseline is weak |
| E4 (Sec 4.3) | Orthogonal projection ablation (remove module) | 2 datasets, HVOP w/o orthogonal proj | Accuracy over views | Performance fluctuates without module | C2 (module importance) | Only 2 datasets; no statistical test |
| E5 (Sec 4.4) | HVOP has stable convergence | 1 dataset (NGs), loss curves | Loss value (visual only) | HVOP loss more stable than GCN | C3 (stability) | Single dataset; no quantitative metric |
| E6 (Sec 4.5) | View order analysis | 1 dataset (NGs), 3 order permutations | Accuracy bar chart | All permutations beneficial | C3 (robustness) | Only 1 dataset; small permutation set |

### Research-Theme Gap Diagnosis

Three research-value claims are weakly supported:

1. **New knowledge — View incremental learning paradigm (C1):** The paper distinguishes its setting from task/class incremental learning conceptually, but does not provide a formal definition of view incremental learning as a distinct learning problem with unique constraints (e.g., fixed label space, changing feature space, no task boundary signal). The claim would be strengthened by a formal problem definition and a proof that existing continual learning methods cannot be directly applied.

2. **Reproducibility (cross-cutting):** Critical hyperparameters (k, η, α, kNN parameter) are missing, making independent reproduction infeasible. This is the most fixable weakness.

3. **Impact on practice (C2/C3):** The experiments are limited to semi-supervised node classification on relatively small datasets (hundreds to thousands of samples). Practical impact would require: (a) larger-scale datasets, (b) real-world streaming settings, (c) computational cost comparison (training time, memory).

### Proposed Research Experiments (P0/P1/P2)

#### P0 Experiment: Orthonormality Validation

- **Target Claim:** C2 (P' = I - R^T R is a valid orthogonal projection)
- **Hypothesis:** With added orthonormalization (R ← R(R^T R)^{-1/2}), P' ≈ P and HVOP accuracy is maintained or improved.
- **Minimal Design:** On 2 datasets (NGs, Animals), compute subspace alignment error ∥KK^T - R^T R∥_F between SVD-based K and Oja-based R. Compare HVOP accuracy with and without orthonormalization.
- **Controls/Baselines:** HVOP-SVD (K from SVD, no Oja) = gold standard; HVOP-Oja (current) = comparison target.
- **Metrics:** Subspace alignment error (Frobenius norm), test accuracy per view.
- **Success Criterion:** Subspace alignment error < 0.1; accuracy difference < 1% between HVOP-SVD and HVOP-Oja (orthonormalized).
- **Estimated Cost/Time:** 1-2 days (adds orthonormalization step, reruns existing code).
- **Expected Paper-Quality Gain:** Core mechanism validated; mathematical rigor restored.

#### P1 Experiment: Comprehensive Forgetting Quantification

- **Target Claim:** C2 (view forgetting relief)
- **Hypothesis:** HVOP reduces average forgetting rate below 5% across all datasets.
- **Minimal Design:** Compute Forgetting_v = F_{v,v} - F_{v,V} for each prior view and average across all datasets. Report mean ± std across 5 seeds.
- **Controls/Baselines:** GCN, GAT, SI, MAS, MVCIL.
- **Metrics:** Average forgetting rate, per-view forgetting, paired t-test (HVOP vs. each baseline).
- **Success Criterion:** Average forgetting < 5% for HVOP; significantly lower (p < 0.05) than all baselines on at least 4/6 datasets.
- **Estimated Cost/Time:** 2-3 days (compute from model checkpoints).
- **Expected Paper-Quality Gain:** Empirical forgetting claim becomes quantitative and testable.

#### P2 Experiment: OOD/Cross-Dataset Generalization

- **Target Claim:** C1/C3 (generalization and transfer)
- **Hypothesis:** HVOP representation transfers to unseen datasets better than single-view baselines.
- **Minimal Design:** Train HVOP on NGs, freeze encoder, evaluate on Flower17 features. Compare to training Flower17 from scratch.
- **Controls/Baselines:** Direct training on target data; GCN without projection.
- **Metrics:** Accuracy, transfer learning gain (accuracy improvement over scratch training).
- **Success Criterion:** Positive transfer gain (>2%) on at least 1 cross-dataset transfer pair.
- **Estimated Cost/Time:** 1-2 days.
- **Expected Paper-Quality Gain:** Generalization claims become evidence-backed.

```text
ASCII Diagram — Experiment Upgrade Plan

P0 (Must): Orthonormality Fix Validation
  └─ Add R←R(R^T R)^{-1/2} → compute ∥KK^T - R^T R∥_F → compare accuracy
  └─ Expected: alignment <0.1, accuracy unchanged

P1 (Must): Forgetting Quantification
  └─ Compute Forgetting_v for all 6 datasets, 5 seeds
  └─ Report table: mean±std, paired t-test vs baselines
  └─ Expected: HVOP forgetting <5%, significant vs GCN/GAT

P2 (Nice-to-have): OOD Transfer
  └─ Cross-dataset transfer experiment (NGs→Flower17, Animals→YaleB)
  └─ Measure transfer gain
  └─ Expected: positive transfer >2%
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5/10**

The paper addresses an interesting and practical problem (view incremental learning) with a technically sound high-level approach (orthogonal projection + Hebbian learning). However, the score is constrained by:

- **Research Value (5/10):** The view incremental setting is conceptually interesting but has limited empirical validation. The contribution is incremental relative to GPM (gradient projection for continual learning) with the main novelty being: (a) applying it to a view-incremental (not task-incremental) setting and (b) replacing SVD with Oja's rule. Without external literature verification, the novelty cannot be fully confirmed.
- **Validity Risk (5/10):** The core mathematical claim (equivalence of P' and P) requires an orthonormality constraint that is not currently enforced. This could affect the mechanism's validity if not fixed.
- **Reproducibility (3/10):** Missing hyperparameters, network dimensions, and implementation details make independent reproduction infeasible.
- **Writing Quality (6/10):** Clear structure but overclaims neuroscience framing. Several minor errors (figure reference mismatch).

**Post-Revision Target: [6.5, 7.5]/10**

If the following are addressed:
- Orthonormality constraint added and validated (P0)
- Neuroscience claims toned down (P0)
- GPM baseline/citation added (P0)
- Hyperparameter table and forgetting metrics reported (P1)
- Limitations section added (P2)

The paper could reach 6.5-7.5/10, making it a solid conference submission. The main remaining limitation would be the scope of empirical validation (node classification only, small datasets), which would require more extensive experiments to push beyond 7.5.

**Decision Rationale:** The paper has a clear research contribution and technically sound core idea, but the mathematical gap in the projection equivalence and the missing reproducibility details are significant weaknesses that prevent a higher score in the current form. The revisions are feasible within a standard revision cycle.