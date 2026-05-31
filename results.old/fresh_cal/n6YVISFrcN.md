I have all the information needed. Let me now produce the consolidated final review.

## Summary

This paper investigates the suitability of the MUSHRA test for evaluating modern high-quality TTS systems. Through a large-scale study involving 47,100 ratings from 471 listeners across Hindi and Tamil, the authors identify two key shortcomings: *reference-matching bias* (raters penalize systems that don't match the reference, even when quality is comparable) and *judgment ambiguity* (high variance from broad, single-scale rating). They propose two refinements — MUSHRA-NMR (removing the explicit reference label) and MUSHRA-DG (providing detailed scoring guidelines with fine-grained dimensions) — and a combined variant (MUSHRA-DG-NMR). The paper also releases the MANGO dataset of human ratings for Indian-language TTS.

## Strengths

1. **Clear empirical demonstration of reference-matching bias via CMOS discrepancy.** Tables 1 and 2 directly contrast MUSHRA scores (e.g., Hindi VITS=67.65 vs. REF=84.18) with CMOS scores showing near-indistinguishability from the reference (VITS CMOS=−0.10). This provides concrete evidence that standard MUSHRA systematically penalizes modern TTS outputs.

2. **Large-scale dataset for an understudied language/dialect context.** 47,100 ratings from 471 listeners across two Indian languages (Hindi and Tamil) is an order of magnitude larger than typical TTS evaluation studies, enabling robust bootstrap analyses of listener/utterance effects, rater rejection rules, and anchor behavior that would be impossible with smaller samples.

3. **Quantified variance reduction and fault-isolation capability of MUSHRA-DG.** The standard deviation of scores decreases by 41% (Hindi) and 58% (Tamil) compared to original MUSHRA (Table 3). The per-dimension breakdowns (Figure 5) reveal specific system weaknesses (e.g., FS2 doing well on pronunciation but poorly on prosody and word-skipping) — a genuinely new diagnostic capability that aggregate MUSHRA or MOS cannot provide.

4. **Actionable practical guidance on listener/utterance requirements.** Section 4.3's bootstrap analysis (≥20 listeners, ≥30 utterances for >95% rank correlation) and the demonstration that increasing listeners matters more than utterances provides concrete design guidance for future TTS evaluations.

## Weaknesses

### Fatal
None. The core contributions — identifying MUSHRA's problems, collecting the dataset, and proposing sensible refinements — remain valuable. However, the validation of the proposed variants has significant gaps, enumerated below.

### Major

1. **MUSHRA-DG scoring formula is not disclosed, preventing replication and independent evaluation.** The paper states that raters were given "a formula to arrive at MUSHRA scores systematically" (Section 5) and lists the input dimensions (pronunciation errors, unnatural pauses, artifacts, word skips, liveliness, voice quality, rhythm on 0–100 scales). But the actual formula — how these inputs are weighted and combined into a final 0–100 score — is never provided. The paper says "these weights can be tweaked depending on the specific use-case," but does not report the specific weights used to produce the results in this study. This omission: (a) makes the results unreproducible; (b) leaves readers unable to assess whether the reported variance reduction stems from the guidelines themselves or from a specific aggregation that compresses score ranges; and (c) prevents diagnosing the anchor-score anomalies (see next point).

2. **Unexplained anchor-score anomalies in MUSHRA-DG-NMR undermine the claim that the combined variant is "more reliable."** In the combined variant, Anchor-X (Hindi) jumps from 70.81 (original MUSHRA) to 89.73 — *exceeding the reference (89.45)*. In Tamil, Anchor-Y jumps from 20.08 to 56.01. These are dramatic, systematic shifts in what should be fixed-quality anchors. The paper does not acknowledge or explain these anomalies. Since the anchors are designed to be degraded samples, these shifts strongly suggest that the scoring process (whether the undisclosed formula or rater adjustment behavior) introduces a calibration issue. The paper's conclusion that "the combined variant is more reliable" is not supported when the behavior of the anchor — the test's calibration point — changes so drastically.

3. **Non-comparable rater pools across variants confound causal attribution.** As shown in Table 1, original MUSHRA used 113 (Hindi) / 100 (Tamil) raters; NMR used 102/97; DG used 14/15; DG-NMR used 15/15. These are entirely different participant groups with no overlap or cross-over design. Any observed difference in variance or mean scores across variants could be driven by differences in rater demographics, training, or rating style rather than the intervention itself. The paper attributes variance reduction to the DG guidelines, but this is confounded by the fact that the DG panels are not only smaller but drawn from a different recruitment pool. Without within-subject comparisons or at least a demonstration that the rater populations are statistically similar, the causal claims are unsupported.

### Minor

1. **The CMOS "ground truth" validation rests on only 15 listeners per language with limited reliability analysis.** The paper uses CMOS as the chief evidence that systems are close to the reference, but the CMOS study uses the same number of raters (15) that the paper itself later recommends as a minimum threshold for 90% rank correlation. No test-retest, bootstrapped ranking CIs, or inter-rater agreement statistics are reported for the CMOS data. While CMOS is a standard test, relying on it as the sole reference point for validating the proposed variants would benefit from additional analysis (e.g., bootstrapped confidence intervals on the ranking itself).

2. **The NMR interpretation is incomplete regarding the reference score drop.** The paper notes that the reference score itself dropped substantially (Hindi: 84.18→76.39; Tamil: 85.22→78.69) and attributes this to "raters were strict." However, if the hypothesized bias was that raters unfairly penalize systems due to the reference label, removing the label should mainly lift *system* scores, not depress reference scores. The reference score drop suggests a mere-label effect (the explicit reference label inflated the reference itself), which is a distinct phenomenon from the claimed reference-matching bias on systems. This nuance is not discussed and would enrich the paper's analysis.

### Trivial
None.

## Nice-to-Haves

- A within-subject or randomized-assignment validation study comparing original MUSHRA vs. the proposed variants with matched rater pools would eliminate the most serious confound.
- Cross-validation of the recommended minimum listener count (≥20 for 90% rank correlation) on the DG/NMR variants to see if the variants reduce the number of listeners needed.
- A brief cost-benefit analysis: DG takes ~2× the time of original MUSHRA — is the fault-isolation capability worth this cost in practice?

## Removed Points

- **"Dataset is not released"** — Removed per hard rules (the paper states it releases MANGO; we assume cited entities exist as of the current date).
- **"Reference score drop is not discussed"** — Removed as factually inaccurate; the paper explicitly says "the score assigned to the reference itself decreased, indicating that the raters were strict" (line 247). The observation about the mere-label effect is retained as a separate minor weakness (see above).
- **Missing related works** — Removed per hard rules (cannot verify existence of missing references without external sources).
- **Formatting/style nitpicks** — Removed per hard rules (parser artifacts, not author errors).
- **Criticisms that demand the paper address problems outside its stated scope** (e.g., demanding the DG variant solve cognitive overload at scale) — Removed or weakened.
- **Strength Finder's generic/superficial strengths** (e.g., "the problem is important") — Removed; only strengths with specific, verifiable evidence are retained.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation about the mere-label interpretation of the NMR reference-score drop is a useful reframing but not novel beyond what the paper already partially addresses. The critic's synthesis of the anchor anomaly and the missing-formula issue as jointly weakening the DG-NMR validation is clear but follows directly from the data presented in the paper.

## Suggestions

1. **Disclose the MUSHRA-DG scoring formula.** Provide the exact formula, the weights used in this study, and the mapping from error counts and perceptual ratings to the final 0–100 score. Without this, the method is incomplete.
2. **Acknowledge and explain the anchor anomalies in MUSHRA-DG-NMR.** The jump of Anchor-X from 70.81 to 89.73 and Anchor-Y from 20.08 to 56.01 needs diagnosis. If the formula or rater adjustment process inflated scores generally, discuss what this means for the reliability claims.
3. **Address the rater-pool confound.** At minimum, add a limitations section discussing that the different variants used different rater pools. Better: provide a bootstrapped re-analysis that shows variance reduction is robust to random subsampling of the larger pools to match the DG size.
4. **Add reliability statistics for the CMOS study** (bootstrapped ranking CIs, inter-rater agreement).
5. **Expand the NMR discussion** to address the mere-label interpretation: the reference score drop suggests the explicit label inflated the reference specifically, not just that it penalized systems.

## Score and Decision

This paper tackles a real and timely problem, collects a valuable dataset, and proposes sensible methodological refinements. The diagnosis of MUSHRA's shortcomings (reference-matching bias, judgment ambiguity) is well-supported by the large-scale original MUSHRA data. However, the validation of the proposed variants has three significant gaps that collectively prevent acceptance: the undisclosed scoring formula for DG, unexplained anchor anomalies in DG-NMR, and confounded rater pools across variants. These are addressable, and the paper's core contributions are strong enough to merit a resubmission after they are resolved.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>