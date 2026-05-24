Now I have enough calibration. Let me write the final review.

## Summary
The paper proposes Steady Thought (ST), a thought-level preference optimization framework to mitigate "under-thinking" in large reasoning models. The pipeline (i) segments responses into thoughts via entropy spikes, (ii) generates counterfactual no-switch continuations from intermediate thoughts by suppressing "wait"/"alternatively" logits, and (iii) trains the model with a SimPO-style objective (STPO) that prefers the correct no-switch completion over the original switching tail. Empirical results across three model sizes (1.5B, 8B, 14B) and four datasets show 17–25% token reduction and modest accuracy gains, including +5.3% OOD on LiveCode for Qwen3-8B.

## Strengths
- **Concrete data-construction pipeline.** The chosen response is the model's own no-switch completion from intermediate thought T_i, and the rejected response is the model's own switching tail — a clean construction that isolates the switching decision (Section 3.3).
- **STPO conditioning is well-motivated against DPO.** Conditioning on (Q, T_i) plus length normalization addresses the systematic length asymmetry between chosen and rejected continuations; Table 4 shows STPO beats DPO and SFT on this preference data, which justifies the choice of objective.
- **OOD generalization is non-trivial.** Training on omni-math and observing +5.3% on LiveCode for Qwen3-8B (Table 1) with concurrent 19% token reduction is real evidence that the learned policy is not pure memorization. The "proportion of last thought" rising from 8.28% → 32.36% on LiveCode (Figure 2 / Section 4.4.1) corroborates that the model commits more deeply rather than just truncating.

## Weaknesses

### Fatal
None. The empirical gains exist and the engineering contribution stands, even if the conceptual framing is overstated.

### Major
- **Conceptual claim ("selective" switching) is not supported by the loss.** Sections 1, 3.3 repeatedly claim ST preserves the model's ability to switch when a thought is genuinely unpromising ("without detriment to the model's capability for preliminary exploration"). But the preference data is uniform: every chosen response is a no-switch completion and every rejected response is the switching tail (Section 3.3, Eq. 7). There is no training signal that ever marks switching as the correct behavior, so the loss cannot teach selectivity — it teaches commitment from every (Q, T_i) prefix that admits a correct no-switch completion. The paper offers no stratified analysis (e.g., over problems where the first-tried thought is wrong) to show ST does not collapse into a NOWAIT-style global suppressor. The differentiator from NOWAIT/SEAL — the paper's headline conceptual claim — is therefore unsupported.
- **"Promising thought" is defined by hindsight oracle, not a model-detectable signal.** Section 3.2 / Eq. 6 labels T_i promising iff a logits-suppressed completion happens to produce the correct answer. Section 3.3 then asserts the trained model learns "to recognize and commit to a promising intermediate thought." Recognition is not part of the loss — only commitment is rewarded. The Bradley-Terry "Steadiness Score" in Section 2.1 reduces to S_π(τ|P_i) := log π_θ(τ|P_i), i.e., standard SimPO scoring; no new recognition mechanism is introduced.
- **Entropy threshold appears tuned on the headline test sets.** Section 4.4.3 / Table 3 selects threshold = 3.0 by judging accuracy and token count on MATH500 and AIME 2024 — the same benchmarks reported in Table 1. No held-out validation split is described. As reported, the headline gains are partly attributable to test-set tuning. Note that AIME accuracy in Table 3 varies non-trivially with threshold (29.2/31.2/28.3), so the choice is not innocuous.
- **NOWAIT baseline on Qwen3-8B is anomalous and not investigated.** Table 1 shows NOWAIT collapses accuracy from 80.23 → 59.03 *and* lengthens outputs by +84.6% (4724 → 13274 on MATH-500, etc.) — the opposite direction NOWAIT produces on the 1.5B and 14B models in the same table. This makes ST's relative gain against NOWAIT on Qwen3-8B look much larger than it likely should. Either the re-implementation has a configuration issue or the behavior needs explanation; as it stands, the comparison is not credible on this model.
- **Mixed/contradictory metric story in §4.4.1.** Figure 2 is presented as evidence for "in-depth exploration," but the numbers don't agree across rows: on DeepSeek-1.5B / AIME 2024, ST *increases* the number of thoughts (12.87 → 18.21) and *decreases* the proportion of the last thought (18.96 → 15.66) — the opposite direction from the narrative. The paper notes the AIME-1.5B exception but does not reconcile it with the claim that ST produces deeper commitment. If the metric supports the story sometimes and contradicts it other times, either the interpretation or the metric is wrong. Relatedly, Table 2's "percentage of correct intermediate thoughts" decreasing is interpreted as fewer Invalid Switches, but the metric cannot distinguish "kept the correct thought" from "did not produce the correct thought at all" — exactly the suppression failure mode the paper claims to avoid.

### Minor
- **No variance on AIME-2024.** AIME has 30 problems averaged over 8 runs. A single problem is ~3.3 points, so claimed +3.7% and +5.0% gains need standard deviations or significance tests before headline citation.
- **Entropy-as-switch-signal not validated on this data (§3.1).** The claim that entropy spikes correspond to thought switches is asserted via citation but not validated; many non-switch positions (variable choices, numeric values) are also high entropy. An agreement statistic with heuristic or manual switch labels would make the segmenter credible.
- **SFT ablation in §4.4.4 is weak.** SFT trains only on the chosen completion at the divergence point. A stronger comparison would be SFT on (Q, T_i) → T_i' pairs *plus* the regular full-trace SFT data (or rejection-sampling-style fine-tuning). The current setup cannot conclude that "preference optimization is uniquely necessary."
- **STPO ≈ SimPO with conditioning.** Section 2.1's "Steadiness Score" abstraction reduces to S_π := log π_θ, and STPO's loss (Eq. 7) is SimPO with the prompt extended to (Q, T_i). This is reasonable but worth framing more honestly — the novelty is the data construction, not the optimizer.

### Trivial
None worth flagging.

## Nice-to-Haves
- A stratified analysis over (first-thought-correct) vs. (first-thought-wrong) problem subsets would directly test the selective-switching claim. If ST still switches on the latter, the differentiator from NOWAIT is real; if not, the paper should reframe.
- A control where the chosen response is constructed *without* logits suppression (e.g., temperature sampling + correctness filtering) would isolate whether the active ingredient is the thought-level preference signal or just the NOWAIT-style chosen distribution distilled in.
- Threshold-tuning on a held-out portion of omni-math with MATH500/AIME left untouched.
- Investigate/fix the NOWAIT-Qwen3-8B configuration or drop that row from the headline comparison.

## Removed Points
*These points are flagged to be removed, treat them with caution.*

- *Related work — no empirical comparison to Wang et al. (2025c)'s original under-thinking mitigation method.* The paper cites it as the origin of the concept but compares only to NOWAIT and SEAL. Without external sources I cannot confirm a missing baseline is required; demoting per the rule on missing-related-works.
- *Strength: "Entropy-based segmentation has a principled motivation."* Conflicts with the verified weakness that entropy-as-switch-signal is asserted but not validated on this paper's data. Kept as Minor weakness instead.
- *Strength: "Diagnostic metrics isolate the mechanism."* Conflicts with the verified weakness that Figure 2 and Table 2 give a mixed/contradictory picture; the metrics do not unambiguously isolate the mechanism, so this is not a clean strength.

## Novel Insights
None beyond the paper's own contributions. The most interesting observation surfaced in synthesis is that ST can be read as "distill NOWAIT-style completions, but only the correct ones, into the model via preference optimization" — which is a useful re-framing for the authors but not a novel scientific insight beyond the paper.

## Suggestions
- Reframe the contribution to match what the loss actually rewards: "thought-level preference optimization that distills correct no-switch continuations." Drop or empirically substantiate the "preserves exploration" claim.
- Run the stratified subset analysis (first-thought-correct vs. wrong) to show ST is not a covert NOWAIT.
- Re-tune the entropy threshold on a held-out split of omni-math (not on MATH500/AIME 2024); report results under the original protocol with a clear ablation.
- Either debug or omit the NOWAIT-Qwen3-8B configuration; current Table 1 row makes the comparison look inflated.
- Report standard deviations / per-run accuracies on AIME 2024.

---

**Axis-by-axis evaluation.**
- *Originality:* Moderate. The data-construction step is a sensible new idea on top of SimPO; the formal apparatus (Steadiness Score) does not add real content.
- *Importance of the research question:* The under-thinking phenomenon and token-efficiency are timely, well-motivated questions for LRMs.
- *Whether claims are well supported:* The "selective switching" / "recognize and commit" claim is *not* well supported by the loss or the analysis. The token-reduction-with-comparable-accuracy claim *is* reasonably supported by Table 1 and the OOD LiveCode result, modulo threshold-tuning and the NOWAIT anomaly.
- *Soundness of experiments:* Adequate scale (3 models × 4 datasets) but two methodological issues (test-set threshold tuning; uninvestigated NOWAIT anomaly) and one interpretive issue (mixed metric story) lower confidence.
- *Clarity of writing:* Generally clear; the gap between conceptual framing and what the method actually does is the main clarity problem.
- *Value to the research community:* Moderate. The data-construction recipe is portable and the OOD result is interesting; reframed honestly, this would be a solid incremental contribution.

---

**Calibration anchors.**

| Path | Avg score | Round | Comparison to this paper |
|---|---|---|---|
| `28TLorTMnP.md` (Soft Alignment) | 2.50 | R1 | Much weaker than this paper; method less concrete. |
| `EVZnnhtMNX.md` (CVX-DPO) | 3.00 | R1 | Weaker; this paper has more empirical depth. |
| `aYYZBPoSHb.md` (ORPO self-judge) | 3.40 | R1 | Weaker. |
| `fTdhM7q1o2.md` (Reward Learning with Ties) | 3.00 | R1 | Different domain; weaker empirical case. |
| `rpbzBXdo4x.md` (Mind Your Step) | 5.00 | R1 | Comparable; pure analysis paper, this one offers method + gains. |
| `85Ik12q2hP.md` (ReAct critical eval) | 4.00 | R1 | Comparable analytical critique; this paper has more empirical contribution. |
| `O0sQ9CPzai.md` (TPO) | 6.33 | R1 | Stronger; cleaner formal contribution and less conceptual overclaim — accepted. |
| `bGGMLWAGMc.md` (IUPO) | 5.50 | R1/R2 | Closest analog: preference optimization for reasoning, similar empirical scope. IUPO's weaknesses (heuristic uncertainty, limited applicability) are roughly the same severity as STPO's (conceptual claim mismatch, test-set tuning). I rate this paper slightly *below* IUPO because the framing-vs-loss gap is a more central issue. |
| `XgYZT35N76.md` (VLM CoT) | 4.25 | R2 | Comparable empirical effort, somewhat weaker idea. |
| `8QkpCRio53.md` (PO for combinatorial opt) | 5.75 | R2 | Different domain; cleaner formal contribution. |
| `ToWKyjwDqO.md` (Direct Judgement PO) | 5.00 | R2 | Comparable. |
| `6VhDQP7WGX.md` (VLM 1 visual token) | 5.80 | R2 | Different topic. |
| `am5Z8dXoaV.md` (LazyLLM) | 5.00 | R2 | Different topic. |
| `fL8Zp8o6RL.md` (FTP) | 5.50 | R2 | Different topic. |
| `z1ohBxWeL2.md` (SwiftKV) | 5.50 | R2 | Different topic. |
| `L9j8exYGUJ.md` (Distributional reasoning) | 5.00 | R2 | Analysis paper. |
| `tn2mjzjSyR.md` (DOTS) | 6.25 | R2 | Stronger formal/method contribution — accepted. |
| `ON3QLXrwVb.md` (Reasoning trees) | 4.67 | R2 | Comparable empirical paper, slightly weaker. |

**Round 1 bracket:** between ~4.0 and ~6.0 (between Mind Your Step / ReAct-eval at the bottom and IUPO / TPO at the top).

**Round 2 narrowing:** anchors cluster around 4.25–5.75 for similar preference-optimization-for-reasoning papers. IUPO (5.50, reject) is the closest analog and has roughly the same character of issues — heuristic choices, limited generality. This paper is slightly worse than IUPO because the central conceptual claim is *contradicted* (not merely incomplete) by the loss, and because there is a verifiable test-set-tuning issue. It is somewhat better than VLM-CoT (4.25) because the empirical scope (3 models, 4 datasets, OOD result) is broader. Landing zone: low 4s. Settling on **4.0** — a reject in the same neighborhood as ReAct-eval / VLM-CoT / IUPO-minus, recognizing real engineering value but flagging the conceptual-vs-loss gap and the threshold-tuning issue as substantive enough to weigh against acceptance.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>