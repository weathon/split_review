## Summary
This paper applies Sparse Autoencoders (SAEs) to the outputs of attention layers in transformer language models. The authors train SAEs on the concatenated z-vectors (attention-weighted value vectors before the output projection) across models including GPT-2 Small (12 layers), GELU-2L, and Gemma-2B. They demonstrate that these Attention Output SAEs produce sparse (L0 < 20), faithful (>80% cross-entropy loss recovered), and interpretable (>80% of live features) decompositions. 

The paper makes three primary contributions:
- **C1**: Validation that SAEs applied to attention outputs yield interpretable feature families (induction, local context, high-level context) across models up to 2B parameters.
- **C2**: Systematic inspection of all 144 attention heads in GPT-2 Small using weight-based head attribution, estimating that >90% are polysemantic, and showing that two apparently redundant induction heads specialize in long-prefix vs short-prefix induction.
- **C3**: Application to the Indirect Object Identification (IOI) circuit, revealing that the previously mysterious "positional signal" is determined by the duplicate name's position relative to the "and" token, verified through causal noising experiments.

The paper is well-positioned within the mechanistic interpretability literature and makes a convincing case for Attention Output SAEs as a practical tool. Its strongest scientific contribution is the IOI circuit analysis, which resolves an open question from prior work. However, the paper's novelty is partially bounded by concurrent work (Rajamanoharan et al., Marks et al.) and the core C1 contribution is largely confirmatory. Evaluation metrics also require careful interpretation due to the zero-ablation baseline choice. The paper is generally well-written with honest limitations, though the narrative structure could be tightened.

## Strengths
1. **Clear methodological contribution for interpretability tooling**: The weight-based head attribution (Eq. 2) and direct feature attribution (DFA, Eq. 3) are simple yet effective techniques that leverage the linear structure of attention OV-circuits to map SAE features back to specific heads and source positions. These techniques are well-motivated and presented with sufficient mathematical clarity for reproduction.

2. **Compelling IOI circuit discovery**: The paper's strongest scientific finding is resolving the "positional signal" mystery in the IOI circuit. The noising experiments (Figure 4) showing 93% logit difference recovery after corrupting three signal dimensions while preserving the "and"-relative position, contrasted with 43% recovery when only "and" is replaced with "alongside," provide clean causal evidence. This is a genuine advance over Wang et al. (2023).

3. **Honest and thorough limitation discussion**: The authors explicitly acknowledge that SAEs only capture linear OV-circuit components, that evaluation metrics are not directly comparable across activation sites, that qualitative interpretation relies on subjective judgment, and that concurrent work exists. This transparency strengthens the paper's credibility.

4. **Open-source release of SAE weights and dashboards**: The release of trained SAE weights, feature dashboards, and interactive exploration tools (Appendix A) is a significant service to the community. This enables reproduction and further research without requiring costly SAE training.

5. **Systematic head-level analysis**: The comprehensive inspection of all 144 attention heads in GPT-2 Small (Section 4.1, Appendix S) provides a valuable empirical resource. The identification of both known motifs (induction, previous token, successor, duplicate token) and new motifs (preposition movers) demonstrates the utility of the method.

## Weaknesses
1. **Evaluation metric comparability concern**: The primary fidelity metric (% cross-entropy loss recovered relative to zero ablation, Eq. 4) is not directly comparable across activation sites, as the authors themselves acknowledge in Appendix I. Zero-ablating a single attention layer causes a smaller CE increase than zero-ablating the residual stream or an MLP layer, which can make attention SAEs appear more faithful than they are in absolute terms. The raw CE values (Table 3) are only provided in the appendix.

2. **Novelty bounded by concurrent work**: The paper honestly acknowledges that Rajamanoharan et al. (2024) and Marks et al. (2024) explore similar ideas. While the paper differentiates itself through weight-based head attribution and causal interventions, the core C1 contribution (SAEs work on attention outputs) is partially overlapping with these concurrent efforts. External literature verification is deferred (Retrieval-Disabled Mode), so precise novelty boundaries cannot be fully established here.

3. **Qualitative methodology reliance**: The paper's estimates of interpretability (e.g., 80% interpretable features in Table 1) and polysemanticity (90%) rely on manual inspection of 30 features per layer and inspection of only the top-10 features per head. While the authors acknowledge subjectivity, the small sample size and top-10 heuristic limit the statistical robustness of these headline claims.

4. **Scope confined to OV-circuit**: The SAEs only decompose the linear OV-circuit component of attention (the weighted sum of value vectors). The QK-circuit (attention pattern computation) is not addressed. This is a significant scope limitation that should be signaled earlier in the paper. The title "Interpreting Attention Layer Outputs" may overstate what is actually decomposed.

5. **GPT-2 Small focus**: Although the paper includes Gemma-2B and GELU-2L evaluations, the majority of analysis (head-level inspection, IOI circuit, induction head specialization) is conducted on GPT-2 Small (100M parameters). Scaling claims are preliminary.

## Key Issues
**Issue 1 (Major): Zero-ablation metric may overstate SAE fidelity**
- **Evidence**: Eq. (4) defines %CE Rec. relative to zero ablation. Appendix I admits zero ablation may be "too harsh a baseline" and makes cross-site comparison difficult. Table 3 (appendix) shows raw CE deltas are very small (e.g., GPT-2 Small Layer 1: Clean CE 3.5563, SAE CE 3.5595, delta=0.0032), suggesting the SAE introduces negligible error but also that the "%CE Rec." metric is inflated by the small denominator.
- **Impact**: Table 1 values (75-99% CE Rec.) may give readers a misleading impression of fidelity compared to residual stream or MLP SAEs.
- **Fix**: Move Table 3 to main text; report absolute CE delta as primary metric with %CE Rec. as secondary.

**Issue 2 (Major): Scope limitation (OV-circuit only) not signaled early enough**
- **Evidence**: The method only decomposes zcat (attention-weighted value vectors before the output projection). QK-circuit computation is explicitly excluded in Limitations (Section 6.1). The title "Interpreting Attention Layer Outputs" and abstract do not mention this scope boundary.
- **Impact**: Readers may overestimate the comprehensiveness of the method's "interpretation" of attention.
- **Fix**: Add one sentence in Introduction signaling OV-circuit focus; adjust title or abstract wording if appropriate.

**Issue 3 (Major): Weight-based head attribution and DFA correlation unvalidated**
- **Evidence**: Sections 4.1 and 4.2 rely on weight-based head attribution (Eq. 2) for head-level conclusions. DFA (Eq. 3) is presented as complementary but the two metrics are never formally compared or validated against each other.
- **Impact**: If weight-based and DFA-based attributions systematically disagree for some features, head-level conclusions could be biased.
- **Fix**: Add a correlation analysis between weight-based and DFA-based head attribution scores for at least one layer, reported in the main text or appendix.

**Issue 4 (Major): Polysemanticity estimate relies on small feature sample**
- **Evidence**: The estimate that >90% of GPT-2 Small heads are polysemantic is based on inspecting only the top-10 SAE features per head (out of d_sae ≈ 25k). The paper acknowledges this is a lower bound.
- **Impact**: The headline "90% polysemantic" may be an under- or overestimate depending on whether features 11+ reveal additional polysemanticity or coincidental co-occurrence.
- **Fix**: Perform a sensitivity check on a subset of heads (e.g., 10 heads, inspecting top-50 features) to test estimate stability.

## Actionable Suggestions
### S1: Reframe the contribution structure (Must - Page 1-2)
**Problem**: The contribution list (Page 2) and surrounding text mix confirmatory claims (C1: SAEs work on attention outputs) with genuinely novel discoveries (C2, C3). The paper itself states "we do not see the application of SAEs to attention outputs as our main contribution," which is disarming but risks confusing readers about what is truly new.
**Action**: Restructure the contributions into two tiers: (1) Validation tier: SAEs produce sparse, interpretable attention output decompositions across models. (2) Discovery tier: Using these SAEs, we provide novel empirical findings about head polysemanticity, induction head specialization, and the IOI positional signal.
**Location**: Page 2, "In more detail, our main contributions are as follows:" (lines 86-101)

### S2: Add raw CE values to main Table 1 (Must - Page 4)
**Problem**: The %CE Rec. metric in Table 1 is not directly comparable across activation sites. Raw CE values are in Appendix Table 3.
**Action**: Move Table 3 (or a compact version showing Clean CE, SAE CE, Delta CE) into the main text alongside Table 1, or add a footnote: "†%CE Rec. is computed relative to zero ablation of a single attention layer; see Appendix I for raw CE values and cross-site comparability caveats."
**Location**: Page 4, Table 1

### S3: Signal OV-circuit scope earlier (Must - Page 1)
**Problem**: The method only decomposes OV-circuit outputs. This scope limitation is only mentioned in Section 6.1 (Limitations).
**Action**: Add one sentence in the Introduction (after paragraph 3): "Our method decomposes the OV-circuit component of attention—the linear weighted sum of value vectors—into interpretable features, providing insight into what information is moved by attention heads. The QK-circuit (attention pattern computation) involves nonlinear operations not captured by this decomposition."
**Location**: Page 1, near line 100

### S4: Validate weight-based vs DFA attribution correlation (Must - Page 3)
**Problem**: The paper relies on weight-based head attribution (Eq. 2) for head-level conclusions (Sections 4.1, 4.2) but never validates it against the activation-based DFA (Eq. 3).
**Action**: Compute the Pearson/Spearman correlation between weight-based attribution scores (h_{i,k}) and DFA scores (w_{i,k}^T z_k) across all feature-head pairs for at least one layer (e.g., GPT-2 Small Layer 5). Report the correlation in the main text or a new appendix section.
**Location**: Page 3, after Eq. (3)

### S5: Strengthen IOI causal verification (Nice-to-have - Page 8-9)
**Problem**: The IOI "positional signal" hypothesis is tested with one compound noising experiment. The "alongside" substitution experiment (43% recovery) eliminates the emergent-positional-embedding hypothesis but leaves open whether the effect generalizes to other coordinating conjunctions ("or", "but").
**Action**: Repeat the noising experiment substituting "and" with "or" and "but" separately. Report results split by ABBA/BABA template.
**Location**: Page 8-9, Section 4.3, Figure 4

### S6: Sensitivity analysis for polysemanticity estimate (Nice-to-have - Page 24)
**Problem**: The 90% polysemanticity estimate is based on top-10 features per head.
**Action**: For a random subset of 10 heads (including some "monosemantic" candidates), inspect top-50 features and report how many change category.
**Location**: Page 24, Table 4 or Appendix K

### S7: Expand concurrent work differentiation (Must - Page 9-10)
**Problem**: The Related Work section mentions Rajamanoharan et al. (2024) and Marks et al. (2024) but does not provide a side-by-side comparison.
**Action**: Add a short comparison table or bullet points listing: (a) SAE application scope, (b) attribution method, (c) validation approach, (d) unique capabilities of each work.
**Location**: Page 10, "Sparse Autoencoders" paragraph

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current storyline follows this sequence:
1. P1 (Intro): Mechanistic interpretability goal and potential applications
2. P2 (Intro): Polysemanticity problem with neurons and attention heads
3. P3 (Intro): SAE literature + weight-based head attribution as solution
4. Figure 1/Caption: Overview + "not our main contribution" admission
5. Contribution list
6. Methodology (Section 2)
7. Results (Section 3-4)

**Problem alignment check**: Partially satisfied. The problem (polysemantic attention heads) is stated, but the connection between polysemanticity and SAEs on zcat is not fully motivated. Why should linear decomposition of zcat solve the polysemanticity problem for attention heads? This requires the weight-based head attribution technique, which is not introduced until Section 2.

**Variable alignment check**: Satisfied. Core concepts (zcat, SAE features, weight-based attribution, DFA) appear consistently throughout.

**Contribution-evidence alignment check**: Satisfied for C2/C3; C1 is primarily qualitative.

### Recommended Storyline (Option A - Discovery-First)

A more engaging narrative structure would be:

**Abstract** (revised - see S1 below)
**P1** (Intro): State the mystery: "Why do transformer models have so many attention heads, and why do many appear redundant?" Hook with the induction head redundancy question.
**P2** (Intro): Explain why head-level analysis is insufficient (polysemanticity). Introduce SAEs as a finer-grained tool.
**P3** (Intro): Preview the three contributions but foreground the IOI discovery as the paper's headline finding.
**P4** (Intro): Brief method overview (SAE on zcat + weight-based head attribution). OV-circuit scope note.
**Section 2**: Methodology (as is, but with correlation validation between weight-based and DFA added).
**Section 3**: Validation that SAEs work (slightly compressed).
**Section 4.3**: IOI circuit analysis (moved forward, as strongest result).
**Section 4.1-4.2**: Head inspection and induction head specialization (supporting contributions).
**Section 5**: Related Work.
**Section 6**: Conclusion.

This structure leads with the most novel result (IOI), then shows the tool's broader utility (head inspection).

### Alternative Storyline (Option B - Tool-First)

Keep the current structure but strengthen the transition between the problem and the SAE solution. Add a "Why zcat?" motivation paragraph explaining that zcat is linear in the value vectors, making it naturally amenable to linear decomposition, unlike MLP activations (which have elementwise nonlinearities).

### Abstract Outline (Revised)

**S1** (Problem): "Decomposing attention layer computations into interpretable features remains a key challenge in mechanistic interpretability, because attention heads are often polysemantic and their outputs involve both linear (OV-circuit) and nonlinear (QK-circuit) operations."
**S2** (Gap): "Prior work applying sparse autoencoders (SAEs) to MLP activations and the residual stream has shown promise, but attention layer outputs have remained largely unexplored with this approach."
**S3** (Method): "In this work, we train SAEs on the OV-circuit output of attention layers—the linear weighted sum of value vectors—achieving sparse (L0 < 20), faithful (>80% CE recovered), and interpretable (>80% of live features) decompositions across models up to 2B parameters."
**S4** (Key Finding 1): "Using weight-based head attribution, we systematically inspect all 144 heads in GPT-2 Small, finding that over 90% are polysemantic and that apparently redundant induction heads specialize in distinct behaviors (long-prefix vs short-prefix induction)."
**S5** (Key Finding 2): "Applying our SAEs to the Indirect Object Identification circuit, we resolve a long-standing mystery by identifying the 'positional signal' as the duplicate name's position relative to the 'and' token, confirmed through causal noising experiments."
**S6** (Resource): "We open-source all trained SAEs, feature dashboards, and an interactive exploration tool."

### Introduction Outline (Revised, Option A)

**P1** (The Hook): "Why do transformer language models have dozens of attention heads that appear to perform the same function? In GPT-2 Small, for instance, multiple heads in layer 5 are classified as induction heads, yet careful analysis shows they are not identical. Understanding these functional differences requires going beyond coarse head-level analysis to finer-grained feature-level decomposition."
**P2** (The Problem): "A core challenge is that attention heads are polysemantic—they encode multiple unrelated concepts depending on input context. This means that analyzing heads as atomic units can miss functional specialization. Sparse autoencoders (SAEs) offer a way to decompose activations into interpretable linear features, providing a finer-grained unit of analysis."
**P3** (The Method Preview): "We train SAEs on the attention-weighted value vectors (zcat) before the output projection—the linear OV-circuit output of attention. We additionally develop weight-based head attribution, enabling us to map SAE features back to specific heads. Note that this decomposition captures what information is moved by attention (OV-circuit), not how attention patterns are computed (QK-circuit)."
**P4** (Contributions): List three contributions as per revised structure above, with IOI discovery first.

## Priority Revision Plan
### P0 (Pre-Submission Critical - Must address)

| Priority | Issue | Effort | Impact | Action |
|----------|-------|--------|--------|--------|
| P0-1 | Add raw CE values to main Table 1 | Low (relocating appendix data) | High (prevents metric misinterpretation) | Move Table 3 to main text; add footnote about cross-site comparability |
| P0-2 | Signal OV-circuit scope in Introduction | Low (add 1-2 sentences) | High (sets reader expectations) | Add scope sentence after method description in Intro P3 |
| P0-3 | Differentiate from concurrent work | Medium (add comparison paragraph) | High (clarifies novelty boundary) | Expand Related Work comparison with Rajamanoharan et al. and Marks et al. |

### P1 (Major Improvement - Must address before final submission)

| Priority | Issue | Effort | Impact | Action |
|----------|-------|--------|--------|--------|
| P1-1 | Validate weight-based vs DFA attribution | Medium (compute correlations) | High (validates head-level conclusions) | Add correlation analysis, 1 paragraph + 1 figure |
| P1-2 | Reframe contribution structure | Low (rewrite 1 paragraph) | Medium (clarifies novelty) | Restructure contributions into validation + discovery tiers |
| P1-3 | Sensitivity analysis for polysemanticity | Medium (inspect 10 heads x 50 features) | Medium (strengthens headline claim) | Add 1 paragraph + 1 table in Appendix K |

### P2 (Quality of Life - Nice-to-have)

| Priority | Issue | Effort | Impact | Action |
|----------|-------|--------|--------|--------|
| P2-1 | IOI "and" generalization experiment | Medium (3 new noising conditions) | Medium (strengthens causal claim) | Test "or", "but" as substitutes; report by template |
| P2-2 | Storyline restructure to Option A | High (major rewriting) | High (improves narrative) | Consider for next submission cycle |
| P2-3 | Larger-scale head polysemanticity analysis | High (requires new SAEs) | Medium | Extend to Gemma-2B head analysis |

### Revision Roadmap (ASCII)

```text
P0 (Week 1): Claim/Language Corrections
  ├── Move Table 3 to main text + add footnote
  ├── Add OV-circuit scope sentence to Introduction
  └── Expand Related Work comparison paragraph

P1 (Week 2): Evidence Strengthening
  ├── Compute weight-based vs DFA correlation
  ├── Restructure contribution list
  └── Polysemanticity sensitivity analysis (top-50)

P2 (Week 3-4): Robustness Extension
  ├── IOI "and" generalization ("or", "but")
  └── (Optional) Storyline restructuring
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | SAE sparsity/fidelity on attention outputs | SAE trained on zcat across GPT-2 Small (12 layers), GELU-2L, Gemma-2B | L0, %CE Rec., % Interp. | L0 < 20, >80% CE Rec., >80% interpretable (Table 1) | C1 | %CE Rec. metric not cross-site comparable; interpretability based on 30-feature sample per layer |
| E2 | Feature family identification | Qualitative inspection of SAE features via dashboards | Manual labeling | Three families: induction, local context, high-level context (Section 3.3) | C1 | Qualitative/subjective; families may not be exhaustive |
| E3 | Board induction feature case study | Specificity/sensitivity analysis on GELU-2L L1 | Specificity plots, false negative analysis | High specificity at upper activation ranges (Figure 2) | C1 | Proxy-based validation; lower activation ranges show polysemanticity |
| E4 | Head-level polysemanticity estimate | Top-10 SAE features per head via weight-based attribution (Eq. 2) | Manual classification of feature groupings | >90% heads polysemantic (Table 4) | C2 | Top-10 heuristic only; no stability check |
| E5 | Long-prefix vs short-prefix induction | Synthetic induction datasets; attention score analysis; intervention | Induction score, DLA, prefix length distribution | Head 5.1 specialized for long-prefix; 5.5 for short-prefix (Figures 3, 17) | C2 | Only 2 heads in GPT-2 Small; scaling not tested |
| E6 | IOI positional signal identification | Zero ablation of L5 SAE features at S2 position; feature dashboard inspection | Logit difference change | Three causally relevant features related to "and"-relative position (Figure 13) | C3 | Only L5 SAE analyzed in main text; other layers in appendix |
| E7 | IOI positional signal causal verification | Compound noising experiment (name swap + filler + position corruption) | Logit difference recovery | 93% recovery when "and"-relative position preserved (Figure 4) | C3 | Single noising condition; only "and" tested (not "or"/"but") |
| E8 | "And"-specificity test | Substituting "and" with "alongside" | Logit difference recovery | Only 43% recovery (Figure 4) | C3 | One conjunction substitute; more needed |
| E9 | QK-circuit decomposition (IOI) | Path expansion with SAE features on query/key side | Variance explained | 62% variance explained by 8 feature pairs (Figure 15) | C3 | Only one sub-circuit; only 100 prompts |

### Research-Theme Gap Diagnosis

| Theme | Current Status | Gap | Impact |
|-------|--------------|-----|--------|
| New knowledge | IOI positional signal resolved; induction head specialization discovered | Both findings on GPT-2 Small only; scaling to larger models unclear | Medium |
| Reproducibility/Reusability | SAE weights and dashboards open-sourced | Full code release pending publication; no training hyperparameter search details | Medium |
| Change practice/understanding | Demonstrates SAE utility for attention analysis | Unclear whether method replaces or complements existing head-level analysis | Medium |

### Proposed Research Experiments

**P0-Exp1: Weight-based vs DFA attribution correlation** (Target claim: C2 methodology soundness)
- **Hypothesis**: Weight-based head attribution scores (Eq. 2) and DFA scores (Eq. 3) are positively correlated across features for a given layer.
- **Minimal design**: For GPT-2 Small Layer 5, compute both scores for all feature-head pairs. Report Pearson/Spearman correlation. Create a scatter plot.
- **Controls/Baselines**: Random attribution baseline (permuted head labels).
- **Metrics**: Pearson/Spearman r, p-value, fraction of features where top-1 head agrees between methods.
- **Success criterion**: r > 0.7, >80% top-1 head agreement.
- **Estimated cost/time**: < 1 day (requires one forward pass with SAE + DFA computation).
- **Expected paper-quality gain**: Strengthens methodological rigor of all head-level conclusions.

**P0-Exp2: Polysemanticity sensitivity analysis** (Target claim: C2, ">90% heads polysemantic")
- **Hypothesis**: The polysemanticity fraction estimate is stable when inspecting top-50 features per head instead of top-10.
- **Minimal design**: Randomly select 10 GPT-2 Small heads (5 "monosemantic" candidates, 5 "polysemantic"). Inspect top-50 features each. Count how many heads change category.
- **Controls/Baselines**: Original top-10 classification.
- **Metrics**: Category change count and rate.
- **Success criterion**: 0-1 heads change category (estimate stable).
- **Estimated cost/time**: < 1 day (manual inspection of 10 heads x 50 features via dashboards).
- **Expected paper-quality gain**: Strengthens headline polysemanticity claim.

**P1-Exp3: IOI conjunction generalization** (Target claim: C3, "and"-specificity)
- **Hypothesis**: The positional signal depends specifically on "and", not just any coordinating conjunction in the same syntactic position.
- **Minimal design**: Repeat noising experiment (Figure 4) substituting "and" with "or" and "but". Report logit difference recovery for each, split by ABBA/BABA template.
- **Controls/Baselines**: Original "and" condition (baseline), "alongside" condition (negative control).
- **Metrics**: Logit difference recovery fraction; KL divergence from clean.
- **Success criterion**: "or" and "but" produce recovery closer to "alongside" (low) than to "and" (high).
- **Estimated cost/time**: < 1 day (requires running existing noising pipeline with new tokens).
- **Expected paper-quality gain**: Strengthens the specificity of the IOI positional signal finding.

**P2-Exp4: Induction head specialization in larger models** (Target claim: C2 scaling)
- **Hypothesis**: Long-prefix vs short-prefix induction head specialization exists in models beyond GPT-2 Small.
- **Minimal design**: Identify induction heads in Gemma-2B using attention-pattern-based induction scores. For each candidate, compute induction score as a function of prefix length (as in Figure 3a). Cluster heads into "long-prefix" and "short-prefix" groups.
- **Controls/Baselines**: GPT-2 Small results as reference.
- **Metrics**: Induction score vs prefix length curves; number of clusters found.
- **Success criterion**: At least two clusters emerge with distinct prefix-length preferences.
- **Estimated cost/time**: 1-2 weeks (requires SAE training + analysis for Gemma-2B).
- **Expected paper-quality gain**: Demonstrates that the discovery generalizes beyond GPT-2 Small.

### Experiment Upgrade Plan (ASCII)

```text
P0 (Must, Week 1)
├── Exp1: Weight-based vs DFA correlation  ──>  Methodological rigor
└── Exp2: Polysemanticity sensitivity       ──>  Headline claim stability

P1 (Should, Week 2)
└── Exp3: IOI conjunction generalization    ──>  Causal specificity

P2 (Nice-to-have, Week 3-4)
└── Exp4: Induction specialization scaling  ──>  Generalizability
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

*Rationale*: The paper makes a solid empirical contribution to mechanistic interpretability by demonstrating that SAEs can be effectively applied to attention layer outputs and by generating novel scientific findings (IOI positional signal, induction head specialization). The work is well-executed, transparent about limitations, and provides valuable open-source resources. However, the score is tempered by: (1) the core C1 contribution is largely confirmatory given existing SAE literature; (2) evaluation metrics are difficult to interpret comparatively; (3) concurrent work partially overlaps with the approach; (4) the headline findings are mostly limited to GPT-2 Small; and (5) novelty verification is deferred in this run (Retrieval-Disabled Mode). The research value is primarily in the tool-building and empirical discovery dimensions rather than in methodological novelty.

**Post-Revision Target: [7.0, 7.5] / 10**

This target assumes the following P0 and P1 revisions are completed:
- (P0) Raw CE values added to main Table 1 with comparability caveat
- (P0) OV-circuit scope signaled in Introduction
- (P0) Concurrent work differentiation strengthened
- (P1) Weight-based vs DFA attribution correlation validated
- (P1) Contribution structure reframed
- (P1) Polysemanticity sensitivity analysis conducted

If P2 items (IOI conjunction generalization, storyline restructuring) are also completed and the paper undergoes careful external literature verification confirming the novelty boundaries, the score could reach 7.5-8.0.