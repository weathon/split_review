## Summary

ScaPre proposes a closed-form framework for large-scale concept unlearning in text-to-image diffusion models, combining a conflict-aware stable design (spectral trace regularizer + Bures geometry alignment) with an Informax Decoupler (MI-based channel scaling) to unlearn up to 50 concepts simultaneously while avoiding collateral damage to similar non-target concepts. The framework yields a Sylvester equation with a closed-form solution, requiring no extra data or auxiliary modules. Evaluated against eight baselines, ScaPre achieves meaningfully better scalability-precision tradeoffs on both ImageNet-Diversi50 (Avg Acc 3.9%, CLIP 29.41) and ImageNet-Confuse5 (5.8% unlearn, 76.3% preserve accuracy).

---

## Rebuttal Assessment

**Weakness: Irreconciled timing claim — 120 seconds vs. ~1.5 hours**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author provides a plausible reconciliation (120 seconds = Sylvester solve only; ~1.5 hours = full pipeline including MI computation and evaluation). However, I verified this explanation against the paper: Section 5.5 states "completing the unlearning of 50 concepts within only **120 seconds**" with no qualification, and Figure 3's caption states "ScaPre is shown as the most efficient method in both metrics" — which is factually wrong, since the accompanying table shows UCE at ~0.5 hours vs. ScaPre at ~1.5 hours. The author acknowledges the paper should state this distinction explicitly but has not corrected it. Furthermore, even under the proposed reconciliation, the MI computation (the Informax Decoupler) is a core novel contribution, not just evaluation overhead — if it takes ~1.4 hours, the "120 second" framing for the "lightweight design" contribution bullet is still highly misleading. None of this is fixed in the current paper.
- **Score impact:** Weakness unchanged (major)

**Weakness: Neutral inputs for MI computation are underspecified**
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing — The author honestly acknowledges the gap (Section 4.2 says y=0 for "neutral inputs" but never defines what they are) and promises to add a specification in revision. I verified this against the paper: there is no definition of neutral inputs anywhere in the main text visible in the paper. The "no additional data" contribution claim makes this more pressing, not less — if neutral inputs come from the preserved-concept set, that should be stated. This is still a genuine reproducibility gap for the paper's precision mechanism.
- **Score impact:** Weakness unchanged (minor, as in original review)

**Weakness: Gating function description partially overstated**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author confirms the reviewer's numerical analysis is correct (small σ_i retained at ~50%, not "nearly intact"), acknowledges the language is misleading, and promises to revise to "aggressively suppressing large singular values while moderately attenuating smaller ones." The directional mechanism is indeed correct. This correction is not yet in the paper (Section 4.1 still says "softly decays the large singular values while leaving smaller ones nearly intact"). The author correctly notes that empirical results validate the practical effectiveness.
- **Score impact:** Weakness unchanged (minor)

**Weakness: UQ metric is distribution-relative**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author correctly notes the component metrics (Avg Acc, CLIP) independently confirm ScaPre's advantage, and that the UQ formula is fully stated in Section 5.2. Both points are verifiable in the paper. The promise to add a clarifying note about UQ's relative nature is not yet in the paper.
- **Score impact:** Weakness unchanged (minor, per original)

**Weakness: "SP" abbreviation never defined**
- **Author's response:** Acknowledge
- **Assessment:** Convincing acknowledgment — Section 2.2 introduces "Sculpting Memory (Li et al., 2025a)" but never assigns the abbreviation "SP" used in all tables. The author acknowledges this and promises a fix.
- **Score impact:** Weakness unchanged (trivial)

**Weakness: ×5 threshold unspecified**
- **Author's response:** Acknowledge
- **Assessment:** Convincing acknowledgment — The abstract states "×5 more concepts than the best baseline within the limits of acceptable generative quality" but no quality threshold is defined anywhere in the main text. The author acknowledges this and promises to add a quantitative definition in revision.
- **Score impact:** Weakness unchanged (trivial)

---

## Strengths

- **Compelling scalability result (Table 3):** ScaPre achieves Avg Acc 3.9%, CLIP 29.41, UQ 65.30 on 50-concept ImageNet-Diversi50. SP (next-best with non-collapsed quality) achieves 22.5%/28.83/51.28. UCE/RECE reach 0.0% accuracy only by destroying generation (CLIP ~22). This margin is qualitatively meaningful and not dependent on the UQ metric.
- **Precise unlearning on confusable concepts (Table 4):** On ImageNet-Confuse5, ScaPre achieves 5.8% unlearn and 76.3% preserve accuracy (84.3% overall) — the only method that simultaneously unlearns targets and protects similar non-targets. UCE/RECE achieve 2.9–3.1% unlearn only by collapsing preserve accuracy to 5.5–5.6%.
- **Principled closed-form derivation:** The Sylvester equation (Eq. 9) is derived analytically, and the Bures geometry alignment (Eq. 5) is a principled improvement over Frobenius ℓ₂ regularization used in UCE/RECE.
- **Multi-setting generalization (Table 2):** ScaPre achieves best CLIP_x (3.44) and competitive CLIP_art (26.51) on 50-artist style unlearning with FID 14.37 close to the unmodified model (13.60).

---

## Weaknesses

### Fatal
None.

### Major

- **Irreconciled timing claim — still present in paper:** Section 5.5 claims "completing the unlearning of 50 concepts within only 120 seconds" and Figure 3's caption claims ScaPre is "the most efficient method in both metrics" — both of which are contradicted by Figure 3's own data showing UCE at ~0.5 hours and ScaPre at ~1.5 hours. The author's reconciliation (120 seconds = Sylvester solve only) is plausible but not stated anywhere in the current paper. Even under this reconciliation, the MI computation (a core novel contribution) is included in the 1.5-hour full pipeline, so the "120 second lightweight design" framing in Contribution Bullet 3 remains misleading. No corrections are present in the submitted paper.

### Minor

- **Neutral inputs for MI computation remain underspecified:** Section 4.2 refers to "neutral inputs" (y=0 class) without definition. The resulting α channel weights — which drive the precision results in Table 4 — depend critically on this undisclosed choice. Author acknowledges the gap but has not addressed it in the paper.
- **Gating function language still overstated:** "leaving smaller ones nearly intact" (Section 4.1) is still in the paper. The author acknowledges the numerical analysis showing ~50% attenuation for small values and promises revision, but the current paper remains inaccurate.
- **UQ metric distribution-relative nature not flagged:** Section 5.2 defines UQ without noting its non-comparability across tables. The component metrics independently support all conclusions, but UQ is presented as if it were an absolute metric. Author acknowledges but has not corrected.

### Trivial

- **"SP" abbreviation undefined in main text** (Section 2.2 introduces "Sculpting Memory" but Tables 1–4 use "SP" without definition)
- **×5 headline figure lacks a stated quality threshold** (neither abstract nor Section 5.2 defines "acceptable generative quality")

---

## Nice-to-Haves

- Ablation in main text showing contribution of each component to precision (Table 4) vs. scalability (Table 3)
- Formal definition of "generative collapse" threshold with annotation on Figure 4
- Sensitivity analysis of neutral input choice for Informax Decoupler
- Computational complexity note for the Sylvester solve (per-layer dimensions)

---

## Novel Insights

The Informax Decoupler is the most distinctive contribution: using mutual information over a 2×2 contingency table (discretized activation state × binary concept label) to identify which output channels of a projection matrix are concept-relevant, then scaling those channels' update magnitude by α_i = MI_i / max_j MI_j. This is distinct from gradient-saliency methods (which use gradient magnitudes) and from binary mask methods. The computational cost is extremely low (counting table entries per channel), and it extends naturally to multiple concepts via max aggregation. Table 4's results — where ScaPre achieves 76.3% preserve accuracy while UCE/RECE collapse to 5.5–5.6% — provide genuinely strong evidence that this mechanism disentangles concept-relevant from concept-adjacent parameters in a way that Frobenius-regularized methods cannot. If the neutral input specification is resolved in revision, this component merits independent study as a general tool for targeted weight editing.

---

## Suggestions

1. In Section 5.5 and Contribution Bullet 3, add a parenthetical explicitly stating "120 seconds refers to the Sylvester equation solve step alone; full pipeline including MI computation requires ~1.5 hours total." Correct Figure 3's caption to remove the claim that ScaPre is "most efficient in both metrics" since UCE is 3× faster.
2. In Section 4.2, add one sentence specifying what "neutral inputs" are (e.g., embeddings from the preserved concept set P, or a fixed set of COCO prompts) and justify this choice relative to the "no extra data" claim.
3. Replace "leaving smaller ones nearly intact" with "moderately attenuating smaller singular values (~50% retention) while aggressively suppressing larger ones (~0.7% retention)" in Section 4.1.
4. Add a footnote or parenthetical in Section 5.2 noting that UQ is normalized relative to the compared method set and is not comparable across tables.
5. Define "SP" parenthetically in Section 2.2 at first mention of Sculpting Memory.
6. Annotate Figure 4 with the quality threshold (e.g., CLIP_coco ≥ X) at which each method is considered to have entered unacceptable quality collapse, to make the ×5 claim verifiable.

---

## Score and Decision

**Post-rebuttal assessment:** The rebuttal is honest and acknowledges all six weaknesses. However, none of the promised corrections are present in the submitted paper — every response is "we will add/fix in revision." The major weakness (120 seconds vs. 1.5 hours, with the Figure 3 caption still claiming ScaPre is "most efficient in both metrics") remains unresolved in the paper. The neutral input underspecification — which directly affects reproducibility of the Informax Decoupler, the paper's most novel mechanism — also remains. These are not minor editorial oversights; the 120-second claim appears in the abstract contribution bullets and is one of the three headline contributions, and the neutral input choice determines the α weights that drive the Table 4 precision results.

On the positive side, the core empirical findings (Tables 3 and 4) are independently verified from the component metrics and are not in dispute. The theoretical derivation is principled. The comparison to calibration anchors (Optimal Targets ~6.33, Score Forgetting Distillation ~6.50) remains appropriate. The rebuttal does not reveal new problems beyond those already identified.

The rebuttal is neutral to slightly negative: it confirms the major weakness is a presentation error (not a methodological flaw), which is a mild positive, but it also confirms no fixes are yet in the paper. The score should remain at 6.5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>