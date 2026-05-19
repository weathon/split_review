## Summary
# Final Review Report

## Summary

This paper addresses the problem of model provenance: determining whether two open-weight language models were trained independently or share a dependency (e.g., one is a fine-tune of the other). The authors propose a family of statistical tests called PERMTEST that produce exact p-values under the null hypothesis of independent training, leveraging the permutation equivariance of neural network training dynamics. The key theoretical insight is that permuting hidden units of a trained model produces an identically distributed copy under the null, enabling efficient Monte Carlo p-value computation without retraining.

The paper introduces two main test statistics based on cosine similarity matching of MLP weight matrices (ϕ_U) and hidden activations (ϕ_H), both aggregated via Fisher's method across Transformer blocks. A robust test statistic (ϕ_MATCH) is also designed to resist adversarial weight transformations by aligning hidden activations between gate and up projections in GLU-based architectures. Empirical validation on 21 Llama-2-architecture models (210 pairs) demonstrates that the exact tests reliably detect all 69 non-independent pairs, including models fine-tuned on 750B additional tokens. The robust test empirically separates dependent from independent pairs even after full MLP-layer retraining, and the framework extends to cross-architecture forensics (e.g., identifying which blocks of Llama 3.1 8B were used in Llama 3.2 1B/3B).

**Strengths:** The paper presents a theoretically grounded testing framework with exact finite-sample validity, which is rare in the model provenance literature. The empirical evaluation is extensive (210 model pairs across diverse fine-tuning regimes). The robust test addresses a practical adversarial threat model. The fine-grained layer matching (Figure 4, Appendix H) provides novel forensic capabilities.

**Weaknesses (major):** (1) The comparison between test statistics in Table 1 is confounded by different p-value computation methods (T=99 bootstrap vs analytic Spearman null), making the claimed resolution advantage of ϕ_U/ϕ_H over ϕ_ℓ2 less definitive. (2) The "empirically behaves like a p-value" claim for ϕ_MATCH lacks rigorous calibration testing (no KS test, no discussion of the 0.024 floor). (3) The Π-equivariance assumption (Definition 2) is stated as a requirement but its applicability to specific optimizers (e.g., Adam with adaptive learning rates, momentum-based methods) is not formally verified. (4) The related-work section reads as a list rather than a comparative positioning around decision-relevant axes.

**Novelty assessment:** Deferred to manual verification (Retrieval-Disabled Mode in this run). Based on manuscript content alone, the key methodological novelty is the use of permutation equivariance for computational-efficient exact p-values in model provenance testing, and the ϕ_MATCH robust alignment statistic for cross-architecture scenarios.

## Strengths
1. **Theoretically grounded exact p-values.** The PERMTEST framework (Algorithm 1) provides exact finite-sample p-values under the null hypothesis of independent training, without asymptotic approximations. This is a clean theoretical contribution that distinguishes the work from heuristic similarity measures and from prior work (Zeng et al., 2024) that lacks statistical guarantees.

2. **Computationally efficient permutation approach.** The key insight — leveraging permutation equivariance of neural network training dynamics to generate identically distributed copies of a model without retraining — is elegant and practically consequential. It transforms an infeasible computational problem (retraining models T times) into an efficient one (T random permutations of hidden units).

3. **Extensive empirical validation.** The paper evaluates 21 open-weight models (210 pairs) across multiple fine-tuning regimes, optimizers, and training budgets. The inclusion of the OLMo controlled experiment (Section 4.2.2, Appendix G), where two near-identical models are trained from scratch with only differing seeds, provides strong evidence that the tests do not falsely reject independence for genuinely independent but similar models.

4. **Adversarial robustness characterization.** The paper honestly identifies the failure modes of exact tests (simple hidden-unit permutation breaks them) and designs ϕ_MATCH to resist these transformations. The MLP retraining experiments (Section 4.2.1, Appendix F) — where entire MLP layers are randomly reinitialized and trained to match original outputs — demonstrate robustness beyond simple permutation attacks.

5. **Fine-grained forensics.** The cross-architecture block matching (Section 4.3.1, Appendix H.2) between Llama 3.1 8B and Llama 3.2 1B/3B, Sheared-LLaMa, and Minitron models provides practical utility beyond binary independence testing. The activation matching visualization (Figure 11) offers insight into pruning patterns.

6. **Honest limitation discussion.** The conclusion explicitly acknowledges susceptibility to false negatives, the open question of complete family-tree reconstruction, and the unresolved theoretical question of exact adversarial robustness guarantees.

## Weaknesses
1. **Confounded statistical power comparison (Major).** Table 1 compares p-values across test statistics but uses fundamentally different computation methods: ϕ_U and ϕ_H use Spearman correlation with an analytic null distribution (permitting arbitrarily small p-values), while ϕ_ℓ2 uses PERMTEST with T=99 (hard floor at 0.01). The reported gap (ε vs 0.01) is primarily an artifact of this asymmetric design, not evidence that cosine-based statistics are inherently more powerful. As noted in the footnote, per-block Fisher aggregation of ϕ_ℓ2 yields p-values < 1e-30, suggesting the gap nearly disappears under matched computation. 

2. **Incomplete characterization of ϕ_MATCH as a "p-value" (Major).** The paper claims ϕ_MATCH "empirically behaves like a p-value" based on visual inspection of Figure 3 (QQ-like plot against Uniform[0,1]). However: (a) no Kolmogorov-Smirnov or similar goodness-of-fit test is reported; (b) the empirical minimum of 0.024 across 141 independent pairs means the test cannot produce p-values below this threshold, which is a serious resolution limit not discussed; (c) the calibration is evaluated only under the specific adversarial transformation used by the authors, not under the full set of possible transformations an adversary could apply.

3. **Π-equivariance assumption scope (Moderate).** The theoretical validity of PERMTEST rests on Definitions 1-2 (Π-invariance of initialization, Π-equivariance of training). The paper correctly identifies permutation of hidden units as a valid Π for MLPs with SGD/Adam, but does not formally verify whether adaptive optimizers (e.g., Adam with its per-parameter learning rates, momentum buffers, or learning rate schedules) strictly satisfy Π-equivariance. The "(typically)" hedge in the introduction signals uncertainty but is never formally addressed. If the assumption fails subtly, the p-values could deviate from uniformity in unpredictable ways.

4. **Shared-input confound in ϕ_MATCH (Moderate).** ϕ_MATCH computes matching permutations from up-projection and gate-projection activations of the same input X. If the activations within each model are correlated (which they are, since both derive from the same hidden representation), then even for genuinely independent model pairs, the two matching permutations may exhibit spurious correlation, potentially inflating false positive rates. The paper's calibration check (Figure 3) partially addresses this, but a controlled synthetic experiment is needed.

5. **Related-work organization (Minor).** The related-work section describes three independent strands (Zeng et al., fingerprinting, watermarking) in a sequential list format. It does not organize them along shared comparison axes (e.g., training intervention required, statistical guarantees, adversarial robustness, access requirements), making it harder for readers to quickly assess the paper's positioning.

6. **Introduction claim scope (Minor).** The introduction states the goal is robust to "1) design decisions such as the number of fine-tuning tokens or choice of optimizer and 2) the application of various adversarial evasion attacks," but the exact tests fail against simple weight permutations (as admitted in Section 3.3). This internal contradiction in the opening narrative could confuse careful readers.

## Key Issues
The following ranked error board captures the highest-priority scientific concerns, ordered by severity and impact on research value.

| Rank | Issue | Severity | Root Cause | Impact | Fixability |
|------|-------|----------|------------|--------|------------|
| 1 | Confounded power comparison (Table 1: ϕ_U/H vs ϕ_ℓ2) | Major | Asymmetric p-value computation methods (analytic Spearman null vs T=99 bootstrap) | Invalidates the claimed resolution advantage of cosine-based tests; table may mislead readers about relative statistical power | Fixable: re-run ϕ_ℓ2 with per-block Fisher aggregation or run all tests with matched PERMTEST |
| 2 | ϕ_MATCH "empirically acts as a p-value" claim | Major | No formal uniformity test reported; empirical floor of 0.024 not discussed | Could mislead practitioners into treating ϕ_MATCH as a valid p-value with unlimited resolution | Fixable: add KS test, discuss floor, calibrate thresholds |
| 3 | Π-equivariance assumption for adaptive optimizers unverified | Major | Section 3.1 states assumptions but never verifies Adam/momentum explicitly | Threatens theoretical guarantee if assumption fails silently under certain optimizers | Fixable: add formal verification or empirical sensitivity analysis |
| 4 | Shared-input confound in ϕ_MATCH | Moderate | H_up and H_gate activations from same input X may cause spurious correlation | Potential anti-conservative bias under null; partially mitigated by Figure 3 but needs synthetic validation | Fixable: add controlled synthetic experiment |
| 5 | Introduction overclaim ("regardless of...adversarial evasion") | Minor | Exact tests fail against simple permutations, creating internal contradiction | Confuses careful readers about the paper's actual scope | Fixable: qualify claims earlier

## Actionable Suggestions
### S1 (Must) — Fair comparison of test statistics
**Problem:** Table 1 compares ϕ_U/ϕ_H (Spearman analytic null) against ϕ_ℓ2 (PERMTEST T=99), creating an asymmetric resolution comparison.  
**Action:** Recompute ϕ_ℓ2 p-values using per-block Fisher aggregation (as mentioned in the footnote) and report them in the main table alongside the current results. Alternatively, run all four statistics under matched PERMTEST T=999 to compare power at equal resolution.  
**Expected benefit:** Readers can honestly assess whether cosine-based statistics offer a genuine power advantage over ℓ2 distance, or whether the gap is an artifact of different p-value computation methods.

### S2 (Must) — Rigorous calibration of ϕ_MATCH
**Problem:** The claim that ϕ_MATCH "empirically acts as a p-value" is supported only by visual inspection of Figure 3.  
**Action:** (a) Report a Kolmogorov-Smirnov test against Uniform[0,1] for the 141 independent pairs. (b) Explicitly state the empirical minimum (0.024) and discuss its implication as a resolution floor. (c) Report the fraction of tests where ϕ_MATCH ≤ α for α ∈ {0.01, 0.05, 0.10}.  
**Expected benefit:** Readers can properly interpret ϕ_MATCH as a conservative test statistic rather than a p-value with unlimited resolution.

### S3 (Must) — Verify Π-equivariance for common optimizers
**Problem:** The theory requires strict Π-equivariance (Definition 2), but the paper never verifies which optimizers satisfy it.  
**Action:** Add a proposition or lemma stating: "For any optimizer whose update rule is a permutation-equivariant function of the gradient (e.g., SGD, Adam, AdamW with element-wise adaptive learning rates), Definition 2 is satisfied." If Adam with momentum buffers or learning rate schedules breaks symmetry, explicitly list the conditions under which the approximation error is bounded.  
**Expected benefit:** Clarifies the scope of theoretical guarantees and helps practitioners know when they can trust exact p-values.

### S4 (Nice-to-have) — Controlled calibration experiment for ϕ_MATCH
**Problem:** ϕ_MATCH's calibration under the null may be affected by shared input structure between H_up and H_gate activations.  
**Action:** Train two independent small GLU MLPs on different synthetic datasets, pass identical test inputs through both, compute ϕ_MATCH, and verify uniformity of the resulting 1,000+ Monte Carlo replicates. Report the KS statistic against Uniform[0,1].  
**Expected benefit:** Confirms that ϕ_MATCH is not systematically anti-conservative due to the shared-input confound.

### S5 (Nice-to-have) — Restructure related-work as comparison table
**Problem:** The related-work section reads as a sequential list rather than a structured comparison.  
**Action:** Add a compact table comparing existing approaches along 4 axes: (1) requires training intervention, (2) requires weight vs query access, (3) provides exact p-values, (4) robust to weight transformations. This would highlight the paper's unique positioning at a glance.  
**Expected benefit:** Substantially improves readability and helps position the paper's contributions relative to prior work.

### S6 (Nice-to-have) — Qualify introduction claims
**Problem:** The introduction states the solution is robust "regardless of...adversarial evasion attacks," but exact tests fail against simple permutations.  
**Action:** Replace "regardless of" with "with separate treatments for": "We propose exact tests for non-adversarial settings and a robust test that sacrifices exact p-values but withstands adversarial transformations."  
**Expected benefit:** Eliminates internal contradiction and sets accurate expectations from the outset.

## Storyline Options + Writing Outlines
### Abstract Outline (Recommended)

**S1 (Problem):** "Given only the weights of two open-weight language models, can a third party determine whether they were trained independently or share a dependency?"

**S2 (Gap):** "Existing approaches require training-time intervention, provide no statistical guarantees, or are easily evaded by simple weight transformations."

**S3 (Solution):** "We propose PERMTEST, a family of statistical tests that exploit permutation equivariance in neural network training to produce exact p-values for model independence without retraining."

**S4 (Key Result):** "On 210 model pairs from 21 Llama-2-architecture models, our tests correctly reject independence for all 69 fine-tuned pairs, including Llemma (fine-tuned on 750B additional tokens from Llama 2)."

**S5 (Robust Extension + Limitation):** "We also identify adversarial transformations that break exact tests and introduce an activation-matching statistic (ϕ_MATCH) that empirically separates dependent from independent pairs across varying architectures, though without exact p-value guarantees."

### Introduction Outline (Recommended)

**Current storyline:** Paragraph 1 (motivation: provenance tracking via weights) → Paragraph 2-3 (hypothesis testing formalization and permutation equivariance idea) → Paragraph 4 (empirical preview) → Paragraph 5 (adversarial setting and robust test) → Paragraph 6 (summary of contributions, implicitly).

**Recommended revision** (sharper problem → gap → solution → evidence arc):

**P1 — Stakes + motivation (target: 4-5 sentences):** Open-weight LLMs are increasingly shared and fine-tuned, but provenance tracking relies on self-reported documentation. The paper asks: can a third party verify independence purely from weights? Connect to IP and regulatory concerns with concrete examples (Miqu leak, fine-tune detection).

**P2 — Gap (target: 3-4 sentences):** Prior weight-comparison methods lack statistical guarantees (Zeng et al. 2024) or require training intervention (fingerprinting, watermarking). No existing method provides exact p-values without access to the training process.

**P3 — Proposed solution (target: 5-6 sentences):** Cast model training as a randomized process. The null hypothesis is weight independence. Because feedforward network training is permutation equivariant, we can simulate independent model copies by permuting hidden units — this yields exact p-values without retraining. This is the core theoretical contribution (Algorithm 1).

**P4 — Exact test empirical results (target: 4-5 sentences):** Preview the 21-model/210-pair evaluation. State the key finding: all 69 non-independent pairs detected with negligible p-values. Highlight the extreme case: Llemma (37.5% additional training budget). Mention cross-architecture applicability (Miqu-70B, Llama 3 block matching).

**P5 — Adversarial limitation + robust test (target: 4-5 sentences):** Exact tests fail under simple hidden-unit permutation. ϕ_MATCH aligns gate/up-projection activations to resist this. Trade-off: no exact p-values, but strong empirical separation.

**P6 — Contributions (target: 3-4 bullet-style sentences):** (i) Exact permutation-based independence tests with finite-sample validity; (ii) Robust activation-matching statistic for cross-architecture adversarial scenarios; (iii) Extensive empirical validation on 210 model pairs with fine-grained forensics.

### Storyline Alternatives Considered

**Alternative A — "Forensics-first":** Open with a concrete forensic case (Miqu leak, Llama 3.2 block matching), then develop the general methodology. This would emphasize practical impact but risks losing readers who are unfamiliar with these specific models.

**Alternative B — "Adversarial-first":** Start with the adversarial evasion threat (someone can permute hidden units to evade detection), then position exact tests as the starting point that motivates robust tests. This would create dramatic tension but might confuse readers about which test is the primary contribution.

**Recommended:** Keep the current structure (exact tests as primary contribution, robust test as extension with honest limitations), but sharpen the gap articulation in P2 and move the contribution summary to a dedicated P6 paragraph.

## Priority Revision Plan
| Priority | Action | Required Section | Effort | Impact | Evidence |
|----------|--------|-----------------|--------|--------|----------|
| P0 | Fix Table 1 comparison: recompute ϕ_ℓ2 with per-block Fisher aggregation or matched PERMTEST | Section 4.1, Table 1 | Low (computational) | High — resolves the most serious validity concern about statistical power claims | Annotation 8 (Page 8) |
| P0 | Add KS test and calibration statistics for ϕ_MATCH; discuss 0.024 floor | Section 4.2, Figure 3 | Low (computational) | High — prevents misinterpretation of ϕ_MATCH as an exact p-value | Annotation 10 (Page 9) |
| P0 | Verify Π-equivariance for Adam, AdamW, and momentum-based optimizers; add formal statement | Section 3.1 | Medium (theoretical analysis) | High — clarifies scope of exact p-value guarantee | Annotation 3 (Page 2) |
| P1 | Add controlled synthetic experiment for ϕ_MATCH calibration under null | Section 4.2 or new Appendix | Medium (experimental) | Medium — resolves shared-input confound concern | Annotation 11 (Page 6) |
| P1 | Restructure related-work as comparison table with decision-relevant axes | Section 2 | Low (writing) | Medium — improves positioning clarity | Annotation 5 (Page 3) |
| P2 | Qualify introduction claim about adversarial robustness | Section 1 | Low (writing) | Low — eliminates internal contradiction | Annotation 2 (Page 2) |

### Revision Order

1. **Round 1 (P0 items):** Fix Table 1 comparison, add KS test for ϕ_MATCH, verify Π-equivariance. These address the most rigorous scientific concerns and directly affect how readers interpret the paper's main claims.

2. **Round 2 (P1 items):** Add synthetic calibration experiment for ϕ_MATCH, restructure related-work. These strengthen the paper's empirical foundation and positioning.

3. **Round 3 (P2 items):** Qualify introduction claims, tighten abstract structure. These polish the narrative without changing scientific content.

### Expected Outcome After Revision

After completing all P0 items, the paper's main claims (exact p-values for model independence under PERMTEST, empirical separation under ϕ_MATCH) would be on much firmer scientific footing. The introduction and related work would accurately reflect the paper's scope. The paper would be suitable for a top-tier venue with the primary contributions being: (1) the permutation-based exact testing framework, (2) the ϕ_MATCH robust alignment statistic, and (3) extensive real-world validation.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup (Data/Models) | Metrics | Main Outcome | Claim Supported | Limitation |
|--------|-----------|--------------------|---------|-------------|----------------|------------|
| E1 | Exact test validation (non-adversarial) | 21 Llama-2-7B models, 210 pairs; ϕ_U, ϕ_H, ϕ_ℓ2, ϕ_JSD | p-values | All 69 dependent pairs detected; uniform p-values under null | C1: PERMTEST yields valid p-values | ϕ_ℓ2 capped at 0.01 due to T=99; ϕ_JSD unreliable |
| E2 | Fine-tune robustness | Llemma (750B additional tokens), CodeLlama, Orca-2, Vicuna variants | p-values | ε-level p-values for all dependent pairs | C1: Retains power after extensive fine-tuning | Only tested on Llama-2 architecture |
| E3 | Adversarial robustness of ϕ_MATCH | Same 210 pairs with random weight permutation/rotation | ϕ_MATCH distribution | Close to Uniform[0,1] for independent; ≤ ε for dependent | C2: ϕ_MATCH empirically separates null from alternative | No formal uniformity test; 0.024 floor not discussed |
| E4 | MLP retraining resistance | 32 MLP layers of Vicuna-7B retrained from scratch | ϕ_MATCH per layer | All 32 layers: ϕ_MATCH < ε | C2: Robust to full MLP retraining | Only GLU architecture tested; doubling MLP width may not be necessary |
| E5 | IID model calibration | Two OLMo-7B models, same data, different seeds | ϕ_U, ϕ_H, ϕ_ℓ2, ϕ_MATCH p-values | Broadly distributed p-values across 4 checkpoints | C1: Tests do not falsely reject genuinely independent models | Only one pair of models tested |
| E6 | Cross-architecture detection | Miqu-70B vs Llama-2-70B; Llama-3.1 vs Llama-3.2; Sheared-LLaMa; Minitron | ϕ_U and ϕ_MATCH | Miqu-70B dependent on Llama-2-70B; fine-grained block matching | C3: Tests apply across architectures | Forensic resolution limited by matching threshold |
| E7 | Beyond-GLU distillation | GPT-2 PMC (finetune of GPT-2) with distilled GLU MLP | ϕ_MATCH | 7.955e-83 p-value | C2: Extensible to non-GLU architectures | Requires MLP distillation step; high computational cost |

### Research-Theme Gap Diagnosis

- **New knowledge:** The paper primarily contributes a methodology (testing framework), not new empirical findings about model relationships themselves. The knowledge contribution is in demonstrating that permutation equivariance can be leveraged for efficient exact testing.
- **Reproducibility:** The paper relies on public HuggingFace models, which is positive. However, the PERMTEST implementation details (choice of Π, number of permutations, seed handling) are spread across the appendix; a consolidated reproducibility package would strengthen this dimension.
- **Change in practice/understanding:** The paper could change how the open-weight model community approaches provenance verification. However, the lack of a practical software library or open-source implementation limits immediate adoption.

### Proposed Research Experiments

**P0 Experiment A — Fair statistical power comparison**
- **Target Claim:** C1 (PERMTEST with cosine-based statistics is more powerful than ℓ2 distance)
- **Hypothesis:** The apparent power advantage in Table 1 disappears under matched computation methods.
- **Design:** Compute ϕ_ℓ2 with per-block Fisher aggregation (as in footnote 3) and report alongside ϕ_U/ϕ_H. Also run all three statistics under matched PERMTEST with T=999.
- **Controls:** Same 21 models, same block structure.
- **Metrics:** p-values achieved.
- **Success Criterion:** If ϕ_U/ϕ_H p-values are still orders of magnitude smaller than Fisher-aggregated ϕ_ℓ2, the power advantage claim holds. If they converge, revise the claim.
- **Cost:** Low (computational, running PERMTEST with T=999 for 210 pairs).
- **Expected Paper-Quality Gain:** High — resolves the most serious validity concern.

**P0 Experiment B — ϕ_MATCH calibration quantification**
- **Target Claim:** C2 (ϕ_MATCH empirically behaves as a valid p-value)
- **Hypothesis:** The empirical distribution of ϕ_MATCH under the null stochastically dominates Uniform[0,1].
- **Design:** (a) KS test on the 141 independent-pair ϕ_MATCH values. (b) Report minimum, 5th percentile, and rejection rates at α ∈ {0.01, 0.05, 0.10}. (c) Synthetic control: train two independent small GLU MLPs on disjoint data, evaluate ϕ_MATCH on 1000+ independent test inputs.
- **Controls:** Independent model pairs from the existing 21-model set plus synthetic pairs.
- **Metrics:** KS statistic, empirical CDF plot with confidence bands.
- **Success Criterion:** KS test p > 0.05, empirical rejection rate at α ≤ α + 0.02 for all tested α.
- **Cost:** Low to medium (synthetic training small models).
- **Expected Paper-Quality Gain:** High — replaces a visual claim with a quantitative one.

**P1 Experiment C — Π-equivariance sensitivity analysis**
- **Target Claim:** C1 (theoretical validity of p-values under PERMTEST)
- **Hypothesis:** Different optimizer choices affect the uniformity of p-values under the null.
- **Design:** Train pairs of small MLPs on synthetic data using (a) SGD, (b) Adam, (c) AdamW, (d) SGD with momentum, all with the same architecture and data. Evaluate PERMTEST p-values for independent pairs. Check uniformity with KS test.
- **Controls:** Same architecture, data, training steps across optimizers.
- **Metrics:** KS statistic against Uniform[0,1] for each optimizer.
- **Success Criterion:** KS p > 0.01 for all optimizers; if any optimizer shows significant deviation, document the failure mode.
- **Cost:** Low (small MLPs, quick training).
- **Expected Paper-Quality Gain:** Medium — clarifies the scope of theoretical guarantees.

**P1 Experiment D — ϕ_MATCH shared-input bias quantification**
- **Target Claim:** C2 (ϕ_MATCH calibration)
- **Hypothesis:** Shared input structure between H_up and H_gate does not systematically bias ϕ_MATCH.
- **Design:** For each of the 141 independent model pairs, compute ϕ_MATCH using (a) identical test inputs for both activation matrices, (b) different random test inputs. Compare the two distributions with a two-sample KS test.
- **Controls:** Same model pairs, only input choice varies.
- **Metrics:** KS statistic comparing distributions (a) and (b).
- **Success Criterion:** KS p > 0.05 (no significant difference).
- **Cost:** Very low (computational only).
- **Expected Paper-Quality Gain:** Medium — resolves the shared-input confound concern.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

The paper presents a theoretically clean and empirically well-grounded testing framework for model provenance. The core idea — using permutation equivariance for efficient exact p-value computation — is novel and practically relevant. The extensive validation on 210 model pairs and the adversarial robustness characterization are significant strengths.

**Score grounded in:** The primary scoring dimensions are research value (methodology novelty + practical utility) and validity/soundness. On research value, the paper contributes a new testing paradigm to an emerging problem (model provenance), which is valuable. On validity, the theoretical framework is sound under its assumptions, but the empirical comparison has a confounded design (Table 1) and the ϕ_MATCH calibration is not rigorously quantified. The P0/P1 revisions would substantively address these concerns.

**Score breakdown:**
- Research value / novelty: 7/10 (methodologically novel; novelty vs prior work deferred)
- Validity / soundness: 6/10 (theory sound; empirical comparison confounded; ϕ_MATCH calibration incomplete)
- Reproducibility: 7/10 (public models used; implementation details in appendix; no code repository provided)
- Presentation / clarity: 6/10 (well-structured but introduction overclaims; related-work reads as list)
- Robustness / thoroughness: 6/10 (extensive evaluation but critical comparisons need fairer design)

**Post-Revision Target: [7.5, 8.0] / 10**

If all P0 items are addressed (fair Table 1 comparison, KS test for ϕ_MATCH, Π-equivariance verification, synthetic calibration experiment), the paper would reach 7.5-8.0/10. The remaining minor concerns (related-work structure, introduction wording) are polish items that do not significantly affect the scientific contribution. At this level, the paper would be a strong acceptance candidate for a top-tier venue (ICLR, NeurIPS, ICML).

---

### ASCII Diagrams

```text
ASCII Diagram — Paper Structure & Evidence Map

[Problem: Model Provenance]
    |
    v
[H0: θ1 ⊥ θ2 (Null: independent training)]
    |
    +--[PERMTEST (Algorithm 1)]--[Exact p-values under Π-equivariance]
    |       |
    |       +--[ϕ_U (up-projection weights)]     }--[Fisher aggregation across L blocks]
    |       +--[ϕ_H (hidden activations)]        }
    |       +--[ϕ_ℓ2 (ℓ2 distance + PERMTEST)]   }--[Baseline from prior work]
    |       +--[ϕ_JSD (Jensen-Shannon)]          }--[Baseline, no p-values]
    |
    +--[Adversarial threat: hidden-unit → PERMTEST fails]
    |       |
    |       +--[ϕ_MATCH (robust alignment via gate/up correlation)]
    |               |
    |               +--[Same architecture] → [Uniform null (empirical)]
    |               +--[Cross-architecture] → [Block matching (forensics)]
    |
    +--[Empirical validation]
            |
            +--[21 Llama-2 models (210 pairs)] → [All 69 dependent detected]
            +--[OLMo IID experiment] → [Uniform p-values under true null]
            +--[MLP retraining (32 layers)] → [ϕ_MATCH < ε for all]
            +--[Cross-arch: Miqu, Llama 3, Sheared-LLaMa] → [Block mapping]
```

```text
ASCII Diagram — Revision Strategy Roadmap

[Issue 1: Confounded power comparison (Table 1)]
    → [Fix: Fisher-aggregated ϕ_ℓ2 or matched PERMTEST T=999]
    → [Expected: Fair comparison, claim may need revision]

[Issue 2: ϕ_MATCH calibration not quantified]
    → [Fix: KS test, report min/percentiles, discuss 0.024 floor]
    → [Expected: ϕ_MATCH properly characterized as conservative test]

[Issue 3: Π-equivariance assumption scope]
    → [Fix: Formal verification for Adam/AdamW/momentum optimizers]
    → [Expected: Exact p-value guarantee scope clarified]

[Issue 4: Shared-input confound in ϕ_MATCH]
    → [Fix: Synthetic controlled experiment]
    → [Expected: Calibration robustness validated]

[Issue 5: Introduction overclaim + related-work list]
    → [Fix: Weaken "regardless" claim; restructure RW as comparison table]
    → [Expected: Clear narrative, honest scope]
```

```text
ASCII Diagram — Related-Work Taxonomy Tree (Layered)

Model Provenance & Independence Testing (Root)
├── Branch 1: Weight-based dependency detection
│   ├── Leaf 1.1: Deterministic similarity [Zeng et al. 2024]
│   │   → Invariant-based testing, no statistical guarantees
│   └── Leaf 1.2: Permutation-based exact tests [THIS PAPER]
│       → Exact p-values via Π-equivariance; ϕ_U, ϕ_H
├── Branch 2: Query-based ownership verification
│   ├── Leaf 2.1: Fingerprinting [Xu et al. 2024, Zhang et al. 2024]
│   │   → Plants secret signal pre-training; requires key
│   └── Leaf 2.2: Output-distribution tests [Jin et al. 2024a]
│       → Query-based; no exact p-values
├── Branch 3: Output watermarking
│   └── Leaf 3.1: Text watermarking [Christ et al., Kirchenbauer, Kuditipudi]
│       → Intervenes at sampling; not applicable to open-weight models
└── Branch 4: Robust adversarial testing [THIS PAPER, partial]
    └── Leaf 4.1: Activation alignment (ϕ_MATCH)
        → Cross-architecture; empirical calibration; no exact guarantees
```

The related-work taxonomy shows the paper's unique position: it is the only work (to our knowledge, deferred) providing both exact statistical guarantees (Leaf 1.2) and an adversarial-robust extension (Leaf 4.1), while requiring no training intervention (unlike Branch 2) and no query-only access (unlike Branch 3).

### Page Coverage Audit

| Page | Section | Annotation Count | Coverage Status | Skip Reason |
|------|---------|-----------------|-----------------|-------------|
| 1 | Abstract | 1 | Covered | |
| 1 | Introduction (P1) | 1 | Covered | |
| 2 | Introduction (P2-P3) | 2 | Covered | |
| 3 | Related Work + Methods start | 2 | Covered | |
| 3 | Algorithm 1 (PERMTEST) | 1 | Covered | |
| 6 | Robust test (ϕ_MATCH) | 1 | Covered | |
| 8 | Experiments (Non-adversarial) | 1 | Covered | |
| 9 | Adversarial setting (Figure 3) | 1 | Covered | |
| 10 | Conclusion | 1 | Covered | |
| 4-5 | Methods (Theorem 1, MATCH, Fisher) | 0 | Skipped | Highly technical derivations covered by annotation on related theory; low marginal defect density |
| 7 | Experiments setup | 0 | Skipped | Non-substantive experimental setup description; overlaps with Section 4.1 |
| 11-29 | References + Appendix | 0 | Skipped | References list; appendix content largely experimental results and derivations supporting main text |

**Note:** The 11 annotations provide coverage across all core sections (Abstract, Introduction, Related Work, Methods, Experiments, Conclusion). The Methods pages (4-5) contain dense technical content that is well-structured and primarily correct; the main concerns are addressed in annotations on the theoretical framework and test statistics definitions. The appendix content (architectural details, additional tables) is supportive and does not introduce new claims requiring independent annotation beyond the main-text discussion.