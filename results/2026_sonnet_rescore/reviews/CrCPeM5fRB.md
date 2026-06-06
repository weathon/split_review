## Summary

This paper proposes the Signal Dice Similarity Coefficient (SDSC), a reconstruction metric for time-series self-supervised learning inspired by the Dice Similarity Coefficient from segmentation. SDSC measures local waveform consistency via sign agreement and magnitude overlap, addressing polarity-blindness, amplitude-scale sensitivity, and unboundedness of MSE. The method replaces only the reconstruction branch of SimMTM (keeping InfoNCE fixed), enabling a controlled comparison of reconstruction objectives. Experiments span forecasting and classification benchmarks.

---

## Strengths

- **SDSC correctly identifies structurally distinct signals that MSE conflates**: Table 1 is concrete and compelling. An inverted waveform receives MSE = 0.0200 (appears high quality to MSE) but SDSC = 0.0000. A zero signal and a 2× scaled waveform both score MSE = 0.4995 despite being structurally unrelated, yet receive SDSC = 0.0000 vs. 0.6667 respectively. These examples directly ground the paper's motivation.

- **Controlled experimental design isolates the reconstruction objective**: By replacing only the reconstruction loss in SimMTM while keeping InfoNCE fixed (Eq. 9), any performance difference in Tables 2–6 is attributable solely to the choice of reconstruction metric—a clean and methodologically appropriate design.

- **Frozen in-domain classification shows SDSC outperforming all baselines**: Table 5 reports SDSC achieves 70.34 average score (Acc/Prec/Rec/F1 averaged) versus 69.15 for MSE and well below 55 for SoftDTW and PCC—the strongest downstream evidence that structural reconstruction improves representation quality.

- **SDSC is bounded, normalized, and made differentiable**: Lemma 1 proves SDSC ∈ [0, 1], the sigmoid approximation (Eq. 7) enables gradient-based optimization, and the metric is O(n) vs. O(n²) for SoftDTW—concrete, useful properties.

- **Qualitative insight about task-signal alignment**: Section 4.3 identifies that the gesture dataset (waveform-structure-dependent) benefits from SDSC while the epilepsy dataset (amplitude-dependent) favors MSE—a genuinely useful observation for practitioners.

---

## Weaknesses

### Fatal
*None.*

### Major

- **Near-null effect sizes in forecasting with no statistical validation**: Table 4 shows forecasting Avg MSE of 0.295/0.316 (MSE pretraining) vs. 0.294/0.316 (SDSC) vs. 0.294/0.316 (Hybrid). These differences are on the order of 0.001. The paper runs with fixed random seeds (single run per condition), reports no standard deviations, no confidence intervals, and no significance tests. At these effect sizes, it is impossible to draw any conclusion about loss-function ordering. The paper acknowledges this only in passing—the Conclusions frame these as meaningful results rather than as null/inconclusive findings. This matters because the forecasting experiments, which span the most benchmarks, essentially show that reconstruction loss choice does not affect downstream performance, directly undercutting the thesis.

- **Single backbone (SimMTM) limits generalizability**: All experiments use SimMTM as the sole pretraining framework. The paper explicitly notes this in Section 4 and defers additional frameworks (TI-MAE, TS2Vec, etc.) to future work. However, SimMTM's specific balance between InfoNCE and the reconstruction branch may not generalize. Whether SDSC's structural properties survive in architectures without a strong contrastive term—or with different reconstruction architectures—is entirely unknown, which substantially constrains the paper's claim that SDSC is "a promising metric for structure-aware learning in time-series domains."

### Minor

- **SDSC's amplitude blindness is not stated clearly in the method section**: Table 1 shows SDSC(0.5× scaled) = SDSC(2× scaled) = 0.6667, meaning SDSC is invariant to amplitude scaling. This is a meaningful limitation for amplitude-sensitive tasks (acknowledged in Section 4.3 and addressed by the hybrid loss), but it is not foregrounded in Section 3.2 where SDSC is defined as a "theoretically sound foundation." A reader not scrutinizing Table 1 may not realize this property until the experimental section.

- **SDSC underperforms MSE in fine-tuning classification**: Table 6 shows SDSC Avg = 74.21 (in-domain) and 83.29 (cross-domain) vs. MSE Avg = 74.46 and 84.65. The primary advantage of SDSC appears only in the frozen encoder setting; end-to-end fine-tuning erases it. This regime-specificity is not adequately highlighted in the abstract or introduction, which frame the result more broadly.

- **The "theoretically sound foundation" framing for the DSC analogy is overstated**: Section 3.2 describes using area-under-the-curve as "a natural and theoretically sound foundation" for the metric. The extension from binary segmentation sets (positive cardinalities) to continuous signed signals is non-trivial—the Heaviside gating function is added to handle polarity, not derived from the DSC analogy. The analogy is useful and intuitive, but calling it "theoretically sound" without a formal derivation is an overstatement.

### Trivial

- None worth noting.

---

## Nice-to-Haves

- The epilepsy/gesture contrast in Section 4.3 is the paper's sharpest empirical insight. A systematic typology—characterizing which dataset properties (amplitude vs. shape diagnostic) predict when SDSC outperforms MSE—would transform this from an observation into a design principle and significantly strengthen the paper's practical contribution.
- Reporting whether the learned uncertainty weights (Kendall et al.) offer a meaningful advantage over fixed λ = 0.5 in the main text (currently deferred to appendices A.6/A.8/A.10/A.13) would help readers assess whether the dynamic weighting mechanism is necessary.
- Multi-seed evaluation with variance estimates would resolve the interpretive ambiguity around small effect sizes without requiring new architectural experiments.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "Alternative interpretation that reconstruction loss barely matters is not discussed"** — Removed as a standalone weakness because the paper explicitly addresses this interpretation in Section 5: "The comparable downstream performance between MSE and SDSC does not necessarily imply the superiority of MSE. Rather, it suggests that amplitude-based metrics like MSE may overestimate reconstruction quality." The paper engages with this interpretation; one may disagree with how it is resolved, but the charge of non-discussion is factually incorrect.

- **Harsh critic: "Hybrid loss uncertainty weighting may not be better than fixed λ"** — Moved to Nice-to-Haves. The paper already reports fixed-λ results in appendices A.6/A.8/A.10/A.13 and mentions them in the main text. Demanding the main text re-summarize them is a presentation preference, not a scientific flaw.

- **Harsh critic: "SDSC models achieve comparable accuracy with significantly higher MSE — this supports contrastive dominance rather than SDSC's value"** — Partially incorporated into the Major weakness above (effect sizes/statistical validation). However, the binary framing ("SDSC is good" vs. "reconstruction loss doesn't matter") ignores a third possibility: that SDSC is legitimately sufficient despite higher amplitude error, which the paper argues. The specific framing of "structural tension" is demoted — not a separate weakness from the statistical validation issue.

- **Strength Finder: "In-domain frozen classification improvement is the 'primary downstream evidence'"** — Kept, but contextualized: the 1.2-point improvement over MSE (70.34 vs. 69.15) is real but modest and lacks significance testing.

---

## Novel Insights

The paper's strongest genuine observation is the dissociation between reconstruction metrics and downstream performance: SDSC models incur 30% higher MSE during pretraining (0.6348 vs. 0.4852, Table 2) yet match MSE models at forecasting. This is not a new claim in SSL generally, but the paper makes it concrete via the SDSC lens: structural alignment is sufficient for downstream prediction quality even when amplitude fidelity is sacrificed. The subsidiary finding—that signal datasets with amplitude-dependent labels (epilepsy) favor MSE while shape-dependent datasets (gesture) favor SDSC—provides a practical selection criterion, though it is currently described anecdotally rather than validated systematically.

---

## Suggestions

1. **Run 3–5 seeds and report variance/significance**: At effect sizes of 0.001–1.2%, single-seed results are uninterpretable. This is the single highest-leverage improvement.
2. **Add one additional pretraining framework** (e.g., TS2Vec or TI-MAE) to test transferability of results beyond SimMTM.
3. **Reframe the abstract/introduction** to lead with the more honest finding: "SDSC achieves structurally superior reconstruction at comparable downstream cost, and matches MSE in all forecasting settings; the largest benefit emerges in frozen-encoder, in-domain classification."
4. **Formalize the task-signal typology**: Characterize datasets along an amplitude-vs.-shape diagnostic axis and test whether this predicts SDSC advantage, turning the epilepsy/gesture observation into a falsifiable design principle.

---

## Evaluation Along Key Axes

**Originality**: Moderate. Extending DSC to continuous time-series signals is creative, and the controlled loss-ablation framing is clean. However, the metric idea is incremental (DSC adaptation + differentiable approximation) and does not represent a conceptual breakthrough.

**Importance of research question**: The question of whether MSE is the right reconstruction objective for time-series SSL is genuinely useful. The answer from this paper—"it mostly doesn't matter, but SDSC is slightly better when encoders are frozen"—is somewhat deflating relative to the motivated question.

**Claims well-supported**: Partially. The theoretical properties (bounded, differentiable, polarity-aware) are well-supported. The downstream advantage claims are technically accurate ("comparable or improved") but the evidence for "improved" is narrow and lacks statistical validation.

**Soundness of experiments**: The design is sound—controlled, ablated, with multiple competitors. The weakness is single-seed, single-backbone execution.

**Clarity of writing**: Good. The paper is organized, notation is consistent, and Table 1/Figure 1 are effective pedagogical tools.

**Value to the research community**: Limited to moderate. The metric is usable, the analysis is honest, and the insights about task-dependent objective selection are practical. The limited effect sizes and single-backbone scope constrain the impact.

---

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>2</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>