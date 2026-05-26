Now let me proceed with calibration search.## Summary
The paper studies sparse support recovery when observations come from two Gaussian sources with different noise variances (high-quality with σ₁², low-quality with σ₂²). It provides (i) sufficient conditions on (n₁, n₂) for information-theoretic recovery in both an "agnostic" decoder (unweighted MLE, Thm 1) and an "informed" decoder (variance-weighted MLE, Thm 2), introduces the "Price of Quality" γ = α₁/α₂, and shows γ ≤ 2 in the agnostic case but γ → ∞ in the informed case in certain SNR regimes; and (ii) extends Wainwright (2009)'s LASSO phase transition to heterogeneous noise (Thm 3), showing the algorithmic threshold depends on (σ₁², σ₂²) only through σ_avg².

## Strengths
- **First sufficient sample-size conditions for sparse recovery under two-block heterogeneous Gaussian noise** (Thms 1 and 2, eqs. (9) and (16)). Prior canonical results (Wainwright 2009; Reeves et al. 2019; Gamarnik & Zadik 2022) assume homogeneous noise; the linear trade-off α₁ n₁ + α₂ n₂ ≥ n* and the corresponding agnostic/informed dichotomy are new.
- **Clean extension of Wainwright's primal-dual witness LASSO phase transition to heterogeneous noise** (Thm 3, eqs. (26)–(28)). The QR/Haar-measure step (Lemma D.6) handles the failure of the Wishart structure that arises when Σ is not a scalar multiple of identity, and yields necessary *and* sufficient conditions for signed-support recovery — including the somewhat striking fact that the threshold depends on the variances only through σ_avg².
- **Explicit asymptotic characterizations of γ across SNR regimes** (eqs. (13), (14), (19), (20), (21)) — these give concrete, qualitatively interpretable predictions (e.g., agnostic γ → 2 − σ₁²/σ₂² in low-SNR; informed γ → ∞ in the high-SNR₁/low-SNR₂ regime), tied to closed-form expressions rather than just existence statements.
- **Honest, well-flagged limitations** (Remarks 3.2, 3.3, 4.2): the Chernoff relaxation, the suboptimality of unweighted MLE in the agnostic case, the absence of necessity for Thms 1–2, and the Wishart-breakdown that prevents an analogous informed-LASSO result are stated rather than hidden.

## Weaknesses

### Fatal
None.

### Major

- **γ is defined relative to the authors' sufficient bound, not the information-theoretic threshold itself, but the paper's headline framing repeatedly treats it as a property of the problem.** Eq. (5) defines γ := α₁/α₂ from the coefficients of the sufficient condition; Remark 3.2 explicitly concedes the agnostic Chernoff bound is loose (cubic relaxation); Remark 3.3 admits no lower bound has been established for either Thm 1 or Thm 2. Yet Section 1.2.1 and the conclusion present "agnostic γ ≤ 2 vs. informed γ → ∞" as a structural property of the two settings, and the practical recommendation in Section 5 ("whenever possible, quantify uncertainty in the annotations and rescale the loss accordingly") leans on that contrast. Without matching lower bounds, the comparison is between two sufficient conditions of unknown tightness, and the qualifier "for this sufficient condition to hold" in the abstract is the load-bearing caveat — it should be foregrounded, not buried.

- **The agnostic/informed dichotomy partially conflates "no provenance" with "no per-sample reweighting."** Thm 1 analyzes the specific estimator (8) — the unweighted MLE. Remark 3.2 itself notes a natural Y_i²-reweighted agnostic estimator that does not require knowing σ_i² but uses |Y_i|² as a proxy. Neither this nor any other non-trivial agnostic procedure is analyzed. As a result, the gap between γ ≤ 2 (agnostic) and γ → ∞ (informed) confounds the value of provenance with the choice of loss function. Even a partial analysis of an alternative agnostic estimator would clarify whether the paper's conclusion is about provenance or about variance-aware loss design.

### Minor

- **No converse for Theorems 1 and 2.** The standard companion in this literature (Wainwright; Reeves et al.; Gamarnik & Zadik; Wang et al.) is a matching impossibility result. Only Thm 3 has both directions (eqs. (26)–(28)). For a paper whose headline contribution is a quantitative comparison across settings, at least one converse would substantially strengthen the claims; Remark 3.3 acknowledges this and defers it.

- **The "striking robustness" framing of Thm 3 is slightly overplayed.** The result that the LASSO threshold depends on (σ₁², σ₂²) only through σ_avg² is consistent with what a Wishart-style concentration argument would yield once σ_avg² is identified as the right summary. It is still a genuine and non-trivial extension, but the contrast with the information-theoretic side ("striking departure") is partially a feature of the asymmetric proof effort: only the agnostic LASSO is studied (Remark 4.2). A clearer statement that the cross-comparison is one-sided would reduce the appearance of overclaim.

- **Motivating examples (LLM annotations, weak supervision, citizen science, multi-site trials) are quite far from the Gaussian i.i.d. design / exactly-sparse binary signal / two-block diagonal noise setting actually analyzed.** This is fine for a theoretical paper, but Section 5's practical recommendation ("quantify uncertainty and rescale the loss") generalizes well beyond what the theorems strictly justify in those settings. Trimming the prescriptive language, or marking it explicitly as a stylized takeaway, would help.

- **Section 4 / Theorem 3 main text could call out where Wainwright's argument breaks.** The QR/Haar-measure step is the technical novelty of the algorithmic section, but its role is only fully visible in the appendix. A brief main-text pointer to which step of the primal–dual witness fails under Σ ≠ σI and how Lemma D.6 fixes it would help the reader appreciate the actual contribution.

### Trivial
- None worth flagging given that the parser is the source of any visible formatting issues.

## Nice-to-Haves
- A partial converse for the informed setting (showing γ → ∞ is genuinely required, not just sufficient) would substantially harden the central comparison.
- An analysis — even heuristic — of the Y_i²-reweighted agnostic estimator from Remark 3.2 would either (a) close the gap with the informed bound (and change the paper's message to "loss design, not provenance") or (b) widen the gap (and strengthen the current message).
- State explicitly in the abstract and Section 1.2.1 that γ is defined relative to the sufficient condition, not the operational threshold, to prevent over-reading.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Possible typo in eq. (12) denominator (`2σ_1⁴` vs `2σ_2²` or `2σ_2⁴`).** The harsh critic flagged a discrepancy between the numerator's denominator in (12) and the corresponding term in (9), and questioned whether (14)'s asymptote (2 − σ₁²/σ₂²) actually follows. Since the parser is known to garble equation rendering, and the asymptotics could match the original LaTeX once parser artifacts are accounted for, this is treated as a parser issue per the hard rules rather than a substantive error.

## Novel Insights
None beyond the paper's own contributions. The paper's own observations — that the information-theoretic price of quality is bounded under unweighted decoding but unbounded under variance-aware decoding, and that the LASSO algorithmic threshold collapses heterogeneity into σ_avg² — are themselves the substantive new content.

## Suggestions
- Calibrate the abstract and Section 1.2.1 to make explicit that γ is defined from the sufficient bound, not the threshold; move the "this sufficient condition" qualifier into the headline sentence about γ ≤ 2.
- Add at least a partial converse (ideally in the informed setting) so the agnostic-vs-informed gap is genuine and not a comparison of upper bounds.
- Analyze the Y_i²-reweighted agnostic estimator suggested in Remark 3.2, even informally, to disentangle "provenance" from "variance-aware loss."
- In Section 4, briefly indicate which step of Wainwright (2009)'s primal–dual witness fails under Σ ≠ σI and which lemma the Haar/QR argument replaces.
- Reframe Section 5's practical recommendation as a stylized implication, given the distance between the analyzed model and the motivating examples (LLM labels, citizen science, multi-site trials).

---

## Evaluation on the Standard Axes
- **Originality:** Moderate-to-high. To my knowledge, the first explicit sample-size conditions for two-block heterogeneous-noise sparse recovery; the QR/Haar extension of Wainwright's LASSO argument is a genuine technical novelty.
- **Importance of the research question:** Reasonable. Mixed-quality data is a live concern (LLM labels, weak supervision); the formal model is, however, far from those motivations.
- **Whether the claims are well supported:** Partially. Thm 3 is solid (necessary and sufficient). Thms 1–2 are sufficient-only, and the headline "Price of Quality" comparison conflates a bound with a threshold; this is acknowledged but underplayed.
- **Soundness of analysis:** The proofs in the main text appear standard and correct; the open question is tightness, not correctness.
- **Clarity:** Generally clear; the limitations are flagged transparently in remarks but should percolate up into the framing.
- **Value to the community:** Moderate. Thm 3 is citable as a clean extension of Wainwright; the information-theoretic results are a useful starting point for the heterogeneous-noise line.

## Calibration and Score

Anchors retrieved:

**Round 1 (bracketing):**
- `vQIVbfTMzf.md` (avg 3.25, weak band) — robust regression with self-tuning robustification; broadly theoretical statistics like this paper but with weaker support and clarity. The paper under review is clearly above this anchor: cleaner theorems, transparent limitations, real technical novelty in Thm 3.
- `ZDoaLbOFaP.md` (avg 3.00, weak band) — sparse covariance neural networks; less topically similar. Paper under review is well above.
- `NHhjczmJjo.md` (avg 7.00, strong band) — in-context sparse recovery with Transformers; provides a convergence-rate result and empirical validation. This paper is below NHhjczmJjo: it lacks the empirical leg and the converse for its headline result.
- `fMTPkDEhLQ.md` (avg 8.00, strong band) — tight matching lower bounds for high-order Hölder smooth optimization. Strictly stronger than the paper under review because it actually delivers tight matching bounds, which is exactly what this paper acknowledges it does not (Remark 3.3).
- `TKRIRI9tQv.md` (avg 5.00, middle band) — sample-complexity for nonlinear system identification with adversarial corruption, LASSO-style. Closest topical analog; comparable in narrowness and theoretical level.
- `L0pMPCmEfN.md` (avg 4.33) and `YvOq7jHT6R.md` (avg 3.75) — wavelet/hard-thresholding methods; less similar.

Round-1 bracket: **between 4.5 and 7.0**.

**Round 2 (narrowing):**
- `ghH6YYDs15.md` (avg 4.67) — sparse autoencoders / compressed sensing; less directly comparable.
- `H8OOlBjhkU.md` (avg 5.00) — sparse optimization with mixed constraints; comparable in narrowness; mixed reviewer reception. The paper under review is somewhat cleaner and has a sharper headline result (Thm 3), but with the same kind of "narrow but solid" character.
- `sIcPMMhl9W.md` (avg 5.80) — phase-transition analysis for shuffled regression, also using Chernoff/message-passing tools, ending with closed-form thresholds and some approximation/heuristic steps. Very close in flavor. Reviewers flagged that some steps are rigorous and others are approximations, and the paper sits in the 5–8 range. The paper under review is comparable: rigorous proofs but with admitted looseness in the agnostic bound and no converse for Thms 1–2.
- `gVVoZtiQlt.md` (avg 5.00) — sibling submission of the above; similar profile.
- `wpXGPCBOTX.md` (avg 6.75) — sparsistency for inverse OT, full Lasso-style irrepresentability analysis with both infinite- and finite-sample results. Stronger than the paper under review: provides finite-sample sparsistency *and* infinite-sample analysis, and a non-trivial extension to a different problem domain (iOT/graphical Lasso). The paper under review is more incremental in technique.
- `nxnbPPVvOG.md` (avg 5.67) — linear estimation / extended Gauss-Markov theorem; comparable theoretical-stats accept-borderline.

The paper under review sits closest to **sIcPMMhl9W (5.80)** and **TKRIRI9tQv (5.00)** in profile: a clean but narrow theoretical contribution where part of the analysis is rigorous and part (the "Price of Quality" framing in the agnostic case) leans on a sufficient bound that is admittedly not tight. It is somewhat below **wpXGPCBOTX (6.75)**, which combines comparable theoretical depth with a more complete (necessary + sufficient + infinite + finite sample) story, and clearly below NHhjczmJjo (7.00), which has matching theory and empirical validation. It is above the H8OOlBjhkU (5.00) and L0pMPCmEfN (4.33) cluster on technical novelty and execution.

Placing the paper between sIcPMMhl9W (5.80) and TKRIRI9tQv (5.00), and slightly closer to the lower side because the central comparison is between two sufficient conditions of unknown tightness — a meaningful caveat for a paper whose narrative *is* that comparison — I score it at **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>