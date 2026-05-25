Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

CausalNovo introduces a model-agnostic framework that uses Structural Causal Models (SCMs) to guide de novo peptide sequencing models toward causal signal peaks and away from spurious noise peaks. It incorporates a Causality Extraction Module (CEM) with contrastive and cross-entropy objectives to enforce independence and sufficiency of causal representations. Evaluated on three benchmark datasets (Nine-species, Seven-species, HC-PT) across three strong baselines (CasaNovo, AdaNovo, π‑HelixNovo), it achieves consistent improvements at the amino acid, peptide, and PTM levels (up to ~10–15% relative gains).

---

## Strengths

1. **Consistent and substantial improvements across diverse settings.** CausalNovo improves every baseline on every dataset at every evaluation level (Tables 1–3). The gains are not cherry-picked: e.g., +14.2% AA precision on HC‑PT (CasaNovo → CausalNovo), +15.1% PTM precision on Seven‑species (π‑HelixNovo → CausalNovo), and positive results on cross-species validation (Table 3). This consistency is the paper's strongest evidence.

2. **Model-agnostic framework design.** The method is plugged into three architecturally distinct baselines (CasaNovo, AdaNovo, π‑HelixNovo) without modifying their core architectures, and improves every one (Tables 1–3). This demonstrates generality beyond a single model.

3. **Empirical motivation via vulnerability analysis.** Figure 1 directly shows that perturbing noise peaks causes precision drops >10% in existing models, establishing that spurious-correlation reliance is a real problem and providing a clear rationale for a causality-informed solution.

4. **Mechanistic evidence from attention analysis.** Table 7 shows that the proportion of predictions where all top‑three attended peaks are causal nearly doubles (19.26% → 32.87%), directly linking the performance improvement to increased focus on signal ions.

5. **Robustness evidence beyond standard evaluation.** The NSR analysis (Figure 4) shows CausalNovo maintains higher precision across varying noise-signal ratios, and the peak-distinguishing analysis (Table 6) uses 18 ion types to demonstrate robustness even under stricter definitions of noise.

---

## Weaknesses

### Fatal
None.

### Major

1. **Causal objectives are not isolated from data augmentation and added capacity.** The ablation study (Table 4) adds the Independence objective (CEM + replace+enhance intervention + contrastive loss) and reports +1.2% AA precision. Simultaneously, Table 5 shows that the replace+enhance data augmentation alone, added to the baseline without any CEM or causal objective, also yields +1.2% (0.741 → 0.753). Because there is no control row that includes the CEM and the replace+enhance augmentation **without** the contrastive independence loss, the specific contribution of the causal contrastive objective is confounded by the data augmentation. The improvements of the full framework (+2.4%) come from Purification and Symmetric components on top, but the central "independence" principle — which is the core causal claim — may contribute little beyond the data augmentation itself. This weakens the attribution of gains to the causal mechanism rather than to simply training on more (perturbed) data.

2. **The purification objective is theoretically unclear and its explanation is confusing.** The paper introduces an auxiliary objective that maximizes I(z_s; Y) and claims this "indirectly leads to the purification of z_c." In standard causal disentanglement, one would minimize I(z_s; Y) to remove label-relevant information from the spurious part. The paper's explanation (Section 3.3) is hard to follow: "However, since z_c and z_s may share certain overlapping information… it can reduce I(z_s; Y). To address this issue, we introduce an auxiliary objective that maximizes I(z_s; Y) which can indirectly lead to the purification of z_c." The chain of reasoning is not clearly articulated, and no formal justification is provided. While the empirical improvement from this objective is shown (Table 4, +0.8%), the lack of theoretical grounding makes the design choice appear ad‑hoc.

### Minor

1. **Vulnerability analysis tests a perturbation similar to the training intervention.** The evaluation in Figures 1 and 3 replaces noise peaks at test time — the same style of perturbation used during training (replace-based intervention). It is expected that a model trained with such replacements would be more robust to them. The NSR analysis (Figure 4) partially addresses this concern, but the paper would benefit from a different form of robustness test (e.g., additive m/z noise, random peak removal) that CausalNovo was not explicitly trained on.

2. **Key hyperparameters (γ, α) not reported.** The tolerance threshold γ (Eq. 4) and the replacement fraction α are not specified in Section 4.2. Only the vulnerability experiments show threshold values (16, 12, 8, 4, 2 in the figures), but their units and the training value of γ are absent. This hinders exact reproducibility.

3. **Relative Improvement (RI) definition is ambiguous.** The paper states RI is "defined as the relative performance reduction of CausalNovo compared to the baseline models" — this phrasing is inconsistent with the positive RI values shown; the intended formula is not clearly specified.

4. **Table 7 total counts differ without explanation.** The attention analysis (Table 7) reports totals of 350,274 (baseline) vs. 347,664 (CausalNovo). The paper does not explain what causes this discrepancy, nor how "top three most attended peaks" are determined (the reference to π‑xNovo matrices is not summarized).

### Trivial

- Training time increase (2.3×) is noted but memory overhead from processing two spectra per example is not discussed.
- The perturbation thresholds in Figure 1 (16, 12, 8, 4, 2) are not defined in the caption (units: ppm / Da / mDa?).
- In Table 1, the retrained baselines (†) differ from originally reported numbers (e.g., CasaNovo 0.697 → 0.741). A brief comment on why these retrained numbers differ would be helpful.

---

## Nice-to-Haves

- **Statistical significance / confidence intervals.** Point estimates are reported without variance across runs. Given that some improvements are modest (1–3 pp), confidence intervals would strengthen the results.
- **Controlled ablation separating causal objectives from data augmentation.** As noted in Major weakness 1, training a version with CEM + replace+enhance but replacing the contrastive loss with standard cross-entropy on the full representation would clarify the source of gains.
- **Different-form robustness test.** A test using a noise type not seen during training (e.g., random m/z jitter, intensity perturbations) would make the robustness claim more general.

---

## Removed Points

The following points from the inputs are excluded under the filtering rules:

- **"Missing related works"** — The rules prohibit mentioning missing related works.
- **"CasaNovo retrained discrepancies are misleading"** — The paper reports both original and retrained numbers and clearly marks them with †; this is standard practice.
- **"Limitations of noise identification (unusual fragmentation)"** — The paper already evaluates with 18 ion types and discusses this limitation. The point is largely addressed.
- **"Inference overhead not mentioned"** — The paper states "negligible inference overhead (less than 1%)" in the conclusion; the critic missed it.
- **"Purification objective should be framed differently"** — This is a suggestion, not a weakness. The core point (unclear justification) is retained in Major weakness 2.
- **"Generalizability concern about NovoBench protocol"** — The paper explicitly acknowledges this as future work in the conclusion.
- **"Pure formatting/style nitpicks"** — Removed per the hard rules.

---

## Novel Insights

None beyond the paper's own contributions. The review surfaces a specific confound in the ablation design (the Independence objective matches the data-augmentation baseline) that the paper does not adequately address, and flags the purification objective's unclear theoretical grounding. These observations clarify where the evidence is weaker than the presentation suggests, but do not yield independent novel insights.

---

## Suggestions

1. **Add a control row to the ablation study:** train a version with CEM + replace+enhance intervention but use standard cross-entropy on the full representation (no contrastive independence loss). This cleanly separates data-augmentation effects from the causal contrastive objective.
2. **Clarify the purification objective:** either provide a rigorous theoretical justification (e.g., connecting to information bottleneck or known disentanglement results), or re-frame it as an empirically-motivated regularizer and discuss alternative formulations (e.g., minimizing I(z_s; Y) instead).
3. **Report γ and α values** in Section 4.2 for reproducibility, along with the units of the tolerance thresholds used in the figures.
4. **Provide a clear formula for Relative Improvement (RI)** in the text or a figure caption.
5. **Add a different-form robustness test** (e.g., Gaussian m/z perturbation or random intensity swapping) to demonstrate robustness beyond the specific intervention used in training.

---

## Score and Decision

The paper proposes a well-motivated framework and demonstrates consistent empirical gains across multiple baselines and datasets. The primary concerns are: (a) the ablation design does not separate the effect of causal objectives from data augmentation, leaving the core causal claim partially unsubstantiated, and (b) the purification objective lacks clear theoretical grounding. These are addressable concerns, not fatal flaws. The empirical improvements are real and practically meaningful, and the model-agnostic design is a genuine strength.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>