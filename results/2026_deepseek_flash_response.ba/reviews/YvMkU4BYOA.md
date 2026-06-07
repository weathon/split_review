## Summary

XBIC augments BIC's complexity penalty with Shapley-value-based directional signals for score-based causal discovery in discrete Bayesian networks. The method trains per-node XGBoost classifiers, aggregates Shapley attributions to obtain edge-specific directional evidence, and uses this to soft-weight BIC's penalty during hill-climbing search. Evaluated across 10 benchmark networks (6–76 nodes) and 7 sample-size regimes (700 runs), the paper reports +5.6% oriented-edge F₁ over BIC-HC, +9.6% over GES, and +20.9% over PC.

## Strengths

1. **Genuinely novel idea with clean mathematical formulation.** Using local feature attributions to guide score-based structure learning reverses the typical direction (causality→XAI to XAI→causality). The formulation preserves BIC's O(log N) penalty growth and reduces exactly to BIC when w=0 or SHAP(G)=0, making it a principled drop-in upgrade. The contrast with prior work (Section 2.3) that uses causal knowledge to constrain explanations is clearly articulated.

2. **Broad evaluation across diverse networks and sample sizes.** The paper spans 10 networks from 6 to 76 nodes across four domains (medical, biology, weather, software) and 7 sample-size regimes. Statistical significance testing (adjusted Friedman + Wilcoxon) is applied, which is a higher standard than many causal discovery papers.

3. **Transparent reporting of limitations.** The paper acknowledges GES survivorship bias (Section 4.5), documents runtime overhead (Table 5: 100–600× slower than BIC-HC), and discusses parallelization paths. The τ confidence threshold is checked for sensitivity (<1% F₁ variation over 0.7–0.95). Code is released.

## Weaknesses

### Major

1. **PC and GES comparisons are structurally biased by the evaluation protocol.** The paper states: "For baselines that return a PDAG, we complete it to a DAG by randomly orienting undirected edges (while preserving acyclicity) before computing directed-edge metrics" (Section 4.1). This systematically penalizes PC and GES for correctly representing ambiguity — undirected edges in a CPDAG are not failures but honest outputs reflecting what cannot be determined from data. The headline +20.9% over PC and +9.6% over GES are therefore not interpretable as evidence of XBIC's superiority in causal discovery; they are partly artifacts of how random orientation happened to fare. The BIC-HC comparison (+5.6%) is not affected because BIC returns a fully directed DAG, but the paper's most dramatic numeric claims rest on this flawed comparison.

2. **No direct validation that Shapley asymmetry tracks causal direction.** The core premise is that |φ̄_{j→i}| ≫ |φ̄_{i→j}| indicates Xⱼ → Xᵢ (Section 3.2, "Intuitively..."). However, SHAP measures predictive importance, not causal direction. Asymmetries can arise from non-causal factors (differences in variable cardinality, marginal entropy, classifier inductive biases) that have nothing to do with causal structure. The paper provides no theoretical analysis, synthetic diagnostic, or controlled experiment to validate this premise. While the empirical results against BIC-HC suggest something is working, it is unclear whether the improvement comes from the directional SHAP signal specifically or from other properties of the composite score (e.g., the non-local penalty modulation discussed in Weakness #4).

### Minor

3. **Absolute F₁ values are not reported.** Table 4 reports only deltas and relative percentages (e.g., absolute +0.04 over BIC for w=2). Without knowing whether XBIC achieves F₁=0.42 vs. 0.38 or F₁=0.75 vs. 0.71, a reader cannot assess practical significance. An absolute improvement of 0.04 on the [0,1] scale is modest and may correspond to only a handful of correctly oriented edges.

4. **The XBIC score has a non-local coupling that is not discussed.** Since SHAP(G) = Σ|φ̄| aggregates over all edges in G (Equation 3), adding a well-supported edge reduces the effective penalty for *all* edges simultaneously, not just the added edge. This creates a peculiar property: the penalty for adding a spurious edge depends on what other edges are already in the graph and their aggregate SHAP support. The paper's consistency remark (lines 155–159) does not address this coupling; it only notes that the penalty grows as O(log N).

5. **No ablation isolating the SHAP signal.** The paper compares XBIC against BIC but does not test whether replacing SHAP(G) with a random signal, a symmetric signal, or a constant preserves the improvements. Without this, it is unclear whether the gains come from the directional information or simply from reducing the penalty (which would also happen with any positive signal).

6. **Runtime overhead is substantial for the gains delivered.** On the 6-node Survey network, XBIC takes 54.21s vs. 0.09s for BIC (600× slower). On the 8-node Asia network, 74.78s vs. 0.39s (190× slower). For a +0.04 absolute F₁ improvement, this trade-off should be discussed more candidly.

7. **GES comparison suffers from survivorship bias** (acknowledged in Section 4.5). GES timed out on larger/denser networks, so the comparison is restricted to easier settings. While the paper acknowledges this, the resulting comparison is not representative.

8. **Weight w tested at only {1, 2, 3}.** The selection of w=2 as "best overall" is post-hoc rather than based on a principled criterion or data-driven method.

### Trivial

None.

## Nice-to-Haves

- A diagnostic experiment validating SHAP asymmetry as a causal direction signal in controlled synthetic settings, varying known factors (cardinality, entropy, noise) to show the signal is not driven by non-causal confounders.
- A proper CPDAG-compatible evaluation of PC and GES (e.g., SID, CPDAG-level SHD, or restricting comparison to edges these methods actually orient) to produce interpretable comparisons.
- An ablation replacing SHAP(G) with a control signal to isolate the role of directional information.
- Per-edge penalty modulation as an alternative formulation to avoid the non-local coupling of the current score.

## Removed Points

- *Criticism about BIC equivalence class conflation (harsh critic):* The point about BIC's score-equivalence vs. practical hill-climbing getting stuck is a nuance that does not undermine the paper's contribution.
- *Confidence threshold selection bias concern:* The paper provides τ sensitivity analysis showing <1% F₁ variation; the concern is partially addressed.
- *Collider confounding speculation:* Plausible but not demonstrated; too speculative to retain.
- *Generic "evaluation lacks rigor" framing:* Removed per filtering rules; only specific, anchored weaknesses are retained.
- *The strength finder's generic praise about "addressing an important problem":* Generic, removed per filtering rules.
- *Claims about missing appendix content:* Parser artifact; the appendix existed in the original submission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Re-run PC and GES comparisons using CPDAG-compatible metrics** (structural intervention distance, CPDAG-level SHD) that do not require random orientation of undirected edges. This would either confirm or refute the headline claims against these baselines.
2. **Add a diagnostic experiment** that generates data from known DAGs and measures whether the SHAP asymmetry signal correctly identifies true causal direction, controlling for non-causal asymmetries.
3. **Add an ablation** replacing SHAP(G) with a random or symmetric signal to isolate the effect of directional information.
4. **Report absolute F₁ values** alongside deltas.
5. **Discuss the non-local penalty coupling** (or reformulate with per-edge modulation) and analyze whether it could encourage spurious edge accumulation.

---

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Low bracket (avg < 3.5): JzFLBOFMZ2 (3.20, LLM-supervised CSL), TRHyAnInUC (3.25, diffusion causal discovery), fSxiromxAq (3.00, sparse causal model) — clearly weaker papers
- Middle bracket (3.5–7.5): ljZFM2mhbR (5.00, DAG-SHAP), i5JfdnCob7 (4.40, kernel choice for score-based CD), eeJz7eDWKO (6.00, meta-learning BCD), 8muemqlnG3 (6.50, DrBO)
- High bracket (avg > 7.5): xByvdb3DCm (8.00), k38Th3x4d9 (8.00) — clearly stronger papers

**Round 1 bracket:** 3.5–6.5

**Round 2 (Narrowing):**
- orD5t7blqV (4.25, PIT algorithm) — incremental improvement, less novel. XBIC is stronger.
- l3Q0scRuT9 (5.00, diffusion causal discovery) — comparable novelty but cleaner evaluation. XBIC is similar.
- 8muemqlnG3 (6.50, DrBO) — accepted, clean method paper. XBIC has more methodological concerns and is weaker.
- eeJz7eDWKO (6.00, meta-learning BCD) — accepted, clean formulation and evaluation. XBIC is weaker.

**Final score:** 4.5

The paper presents a genuinely novel idea (using Shapley attributions to guide discrete causal discovery) with a clean mathematical formulation and broad evaluation. However, two significant issues prevent acceptance at ICLR standards: (1) the PC/GES comparisons rest on an evaluation protocol that randomly orients undirected edges, making the headline +20.9% and +9.6% claims uninterpretable as evidence of superiority; and (2) the core premise — that SHAP asymmetry tracks causal direction — is asserted without theoretical or diagnostic validation. The surviving comparison against BIC-HC shows only a modest +0.04 absolute F₁ improvement at 100–600× the computational cost. These issues are addressable but too substantial for the paper in its current form.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>