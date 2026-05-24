Now I have enough calibration anchors. Let me write the final review.

## Summary

The paper studies output length **volatility** in long-form LLM generation, contributing (1) **VOLTBench**, a benchmark scaling chapter-based instructions from 5 to 500 sections (~100k words) with English/Chinese, multiple sampling (N=5), and stability metrics (LSD, LVC, MLA, FAD, SCA, UCA); (2) an **attention-trace probing** analysis that identifies two failure patterns — *Attention Collapse* and *Attention Instability*; and (3) **SELB**, a training-free decoding-stage method that boosts logits of next-section title tokens at length thresholds, bans EOS until the target section count is reached, and bans curated filler tokens. The paper reports SELB improves mean length by 148%, reduces LVC by 69% (45.4% → 14.02%), raises MLA from 31.6% to 78.25%, and SCA from 32.6% to 100% versus LongWriter-8B on a 100-section task.

## Strengths

- **Identifies length volatility as a distinct, under-evaluated failure mode.** Figure 1 quantifies the issue concretely: LongWriter-8B's output standard deviation (17,572) reaches 103% of its mean length (17,082), and Table 1 documents that no prior long-form benchmark includes both multiple sampling and stability evaluation. Framing single-shot quality vs. cross-sample stability as separate axes is a useful conceptual contribution.
- **Multi-axis benchmark design.** VOLTBench varies language (English/Chinese), complexity (simple, fine-grained constraints, complex), output format (structured/unstructured), and target length (5 to 500 chapters). Fine-grained constraints (character pattern, keyword, theme) on designated sections are an honest way to make unstructured-task quality automatically checkable.
- **SELB delivers large measured gains and generalizes beyond structured tasks.** On a 100-section task: LVC drops to 14.02% vs. LongWriter-8B's 45.4%, MLA reaches 78.25% vs. 31.6%, and SCA reaches 100% vs. 32.6% (Section 6.3, Table 2). SELB-Hybrid extends to free-form 20,000-word novel writing with 97% MLA and 12.1% LVC, where baselines collapse below 600 words (Section 6.4).
- **Method is lightweight and training-free.** SELB modifies logits at decoding time (Eqs. 2–3) without retraining, making it deployable on top of any open model. It is shown applied to Qwen2.5-7B, Qwen3-8B, and Llama-3.1-8B (Figure 5).

## Weaknesses

### Fatal
None.

### Major

- **The probing→mitigation narrative is mechanistically loose.** Section 5 identifies *Attention Collapse* and *Attention Instability* in attention traces and frames the paper as a three-stage pipeline ("benchmarking, probing, mitigation"). But SELB (Eqs. 2–3) is a token-level structural enforcement scheme — boost next-section-title logits at `τ_max`, ban EOS until `P_total` is reached, ban a curated filler list. None of these operations touch attention or were derived from attention patterns; the same fix would work absent the probing chapter. The probing section is therefore decorative w.r.t. the proposed method, which weakens the paper's claim to have "targeted the identified internal patterns" (Section 1 contributions). This is a framing/coherence issue rather than an invalidation, but it is exactly the integrated story the paper sells.
- **Headline length-stability metrics are partly mechanical consequences of the algorithm.** SELB cannot emit EOS before `P_total` sections and forcibly emits a next-section header whenever `τ_p ≥ τ_max`. MLA, LVC, FAD, and SCA (= correct chapters / required chapters) are therefore quantities the algorithm directly controls by construction. A "section header injection + EOS ban" decoder will produce close-to-target length and section counts almost tautologically. The paper does not isolate which gains come from this structural skeleton versus the proactive filler-suppression, nor compare against the obvious minimum baseline (a structurally templated decoder with forced section headers and `min_new_tokens` per section) to show what SELB specifically adds. Absent that ablation, the 78.25% MLA / 100% SCA numbers, while real, are not the right test of the contribution.
- **Quality evidence is thin given that quality is the load-bearing claim.** SELB's value proposition is "stable length *without* losing quality." Quality is supported almost entirely by UCA — LLM-as-Judge on N=5 outputs (Table 2: SELB 86.7% UCA). For forcibly extended generations, the very regime where LLM judges are known to struggle, there is no human evaluation, no judge–human calibration, and no qualitative analysis of forced sections. Appendix-H is mentioned as a "representational stability" rebuttal in the main text but does not surface concrete content-quality numbers in Section 6.3. The 100% SCA on structured tasks helps for code/math but does not address unstructured-content quality under length enforcement.
- **The decoding-strategy baselines are not designed for length control.** Table 2 compares SELB against Repetition Penalty, Entropy-Based Stopping, Length Constraint (underspecified — prompt instruction? `max_new_tokens`? logit constraint?), and Lookahead Decoding. Three of these are not length-control mechanisms; "Length Constraint" lacks a definition that lets the reader judge whether it is a fair structural baseline. Comparison with constrained / structured-decoding methods of the same shape (e.g., grammar-constrained decoding, outline-conditioned generation with `min_new_tokens`) would more cleanly isolate SELB's contribution.

### Minor

- **Attention analysis is anecdotal.** Section 5 / Figure 4 grounds "Attention Collapse" and "Attention Instability" in two single traces (Qwen2.5-7B and Qwen2.5-3B, one prompt each). There is no scalar definition of a "collapse" or "instability" event, no population-level correlation between these signatures and per-sample length-volatility failures, and no negative control showing successful generations lack them. Listing this as one of three contributions ("we identify and define common internal patterns") overreaches what two traces support.
- **N=5 yields wide CIs for volatility metrics, and intervals are not reported.** Standard-deviation estimates with N=5 are noisy; reporting LSD/LVC without confidence intervals risks overstating differences between conditions in Table 2 and Figure 3. A subset re-run at higher N (e.g., 20) for the headline comparisons would meaningfully strengthen every downstream claim.
- **MLA saturates at 0 below half the target length.** Given `max(0, 1 − |μ − L|/L) × 100`, models that under-generate by ~10× (e.g., Claude-3.5 at 176 words vs. 1000-word targets) all collapse to ~0 MLA, so the metric does not discriminate among heavily-under-generating models. Since SELB sits at the upper end of length by construction, MLA differences are doing most of the work in the comparison.
- **`V_title^(p+1)` and `V_banned` are tokenizer- and model-specific.** The main text describes both as sets without detailing the curation procedure that turns "next section title" or "conversational filler" into a token list — a non-trivial reproducibility-relevant choice that should be in the main text.
- **`α^{(l,t)}` averaging across heads and layers may hide head-/layer-specific signal.** Prior interpretability work suggests instruction-following effects are concentrated in particular heads; the layer- and head-averaged `ᾱ^(t)` discards exactly that structure and may suppress rather than reveal the attention dynamics that matter.
- **"All models failed when sections > 50" (Section 4.3) is sweeping for an N=5 study.** Per-model, per-length failure rates with numbers would be more credible than the current qualitative framing.

### Trivial
- "Attention summits" is introduced in Section 5 but never operationalized as a measurable scalar.
- The abstract's "+148% mean length / –69% volatility" framing reads as a general capability improvement; the body clarifies it is a structural decoder, but the abstract could be tightened.

## Nice-to-Haves
- A baseline that matches SELB's structural form (forced-section-template decoding, `min_new_tokens` per section) to isolate what SELB adds beyond the skeleton.
- Human evaluation of SELB content quality on a representative subset, especially of the 20k-word novel outputs where length is mechanically guaranteed.
- A small population-level study converting attention-trace features into a scalar predictor of per-sample volatility failures across VOLTBench — this would turn the probing chapter from description into validated diagnostic.
- A confidence-interval pass at higher N on the headline comparisons.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Harsh critic: "The benchmark's '100k length scale' is achieved through 500-chapter tasks; this measures structured chunked output, not a single coherent 100k-word document."* — The paper is explicit (Section 3, "chapter-based design is the key to our scalability") and does not claim single-document coherence at 100k. Not a misrepresentation by the authors.
- *Harsh critic: "Comparison table somewhat overstates the differentiation in Table 1."* — Generic framing complaint; the differentiation columns ("Multiple Sampling", "Stability Eval") are factual table entries. Not a substantive criticism.
- *Strength Finder: "First systematic quantification of length volatility as a core failure mode."* — Kept in revised form (Strength 1); the "first" claim depends on the field-coverage statement and is best held as "identifies as distinct under-evaluated failure mode."

## Novel Insights

None beyond the paper's own contributions. The most genuinely novel observation in the paper itself — that LLMs exhibit cross-sample length volatility on the same prompt at a magnitude comparable to their mean output length (Figure 1) — is a useful framing contribution that the broader field largely has not centered.

## Suggestions

1. Reframe SELB honestly as a *structured-decoding scaffold* for chapter-style outputs, drop the implicit "we fixed the attention patterns" claim, and instead pitch the attention probing as an exploratory analysis rather than a derivation step.
2. Add the obvious minimum baseline (forced section headers + `min_new_tokens` per section + EOS ban) and show what SELB's additional mechanisms — particularly the filler-token bans and Hybrid Keep-Alive — contribute on top.
3. Operationalize "Attention Collapse" and "Attention Instability" as measurable features and validate them as predictors of length-volatility failures across VOLTBench rather than describing them from two traces.
4. Add a small human evaluation on a representative subset of SELB outputs, including the 20k-word novels, focused on coherence, drift across forced sections, and repetition.
5. Raise N from 5 to ≥20 on the headline comparisons and report 95% CIs for LSD/LVC; clarify what "Length Constraint" means as a baseline.
6. Move `V_title` and `V_banned` curation details into the main text — these are essential to reproducing the headline numbers.

---

## Axis-by-axis evaluation

- **Originality:** Moderate. Reframing long-form evaluation around volatility/multiple sampling is novel relative to existing benchmarks. SELB itself is a fairly straightforward structural-decoding scheme.
- **Importance of the research question:** Real. Length and structural stability are obstacles to deploying long-form LLM generation, and the paper's evidence on cross-run variance (Figure 1) is striking.
- **Whether claims are well supported:** Mixed. The benchmark's empirical findings (failure rates, language/complexity/format effects) are well supported. SELB's *length-stability* claims are mechanically guaranteed by the algorithm and not isolated from that tautology; its *quality* claims rest on LLM-as-judge over N=5. The "derived from attention probing" framing is not supported.
- **Soundness of experiments:** Adequate for the benchmark side, weak for the SELB evaluation (missing structural baseline, small N, no human eval, no separate ablation of SELB's components).
- **Clarity of writing:** Generally clear. The probing chapter is the weakest part — terms like "attention summits" and the two failure patterns are introduced but never quantified.
- **Value to the community:** Modest-to-real. VOLTBench fills a gap in the long-form benchmark space; SELB is a usable engineering tool for chapter-style generation once recast honestly.

## Calibration

**Round 1 — bracketing** (broad anchors on long-form generation/benchmarking):
- `ly10tMV6cD.md` (3.25, reject) — structure-rich benchmark — weaker than this paper.
- `JQbqaQjV7D.md` (3.00, reject) — industrial benchmark, narrow scope — weaker.
- `koza5fePTs.md` (2.00, reject) — planning benchmark — much weaker.
- `RuY1r1PDdQ.md` (3.00, reject) — instruction-following eval — weaker.
- `QM2WoPu1It.md` (4.75, reject) — **HelloBench**, very close topic; this paper has more components (probing + method) but more questionable framing.
- `kQ5s9Yh0WI.md` (6.00, accept) — **LongWriter**, very close topic; cleaner contribution arc than this paper.
- `uMEsKEiB7J.md` (6.40, accept) — NovelQA long-context benchmark — stronger evaluation than this paper.
- `293V3bJbmE.md` (6.00, accept) — HELMET long-context eval — stronger and more rigorous than this paper.
- `YrycTjllL0.md` (9.00, accept) — BigCodeBench — clearly stronger.
- `syThiTmWWm.md` (7.75, accept) — gameability of LLM benchmarks — clearly stronger.
- `xoXn62FzD0.md` (8.00, accept) — SMC for constrained generation — clearly stronger methodologically.
- `GGlpykXDCa.md` (8.00, accept) — MMQA — stronger.

After round 1, this paper plausibly lands between **HelloBench (4.75)** and **LongWriter (6.0)**. Round-1 bracket: **[4.5, 6.0]**.

**Round 2 — narrowing within (4.5, 6.5)**:
- `vXf8KYTJmm.md` (5.25, reject) — MAP-decoding paper — methodological pseudo-novelty issue similar in flavor to SELB's framing problem.
- `9WbNpRuFuS.md` (5.75, reject) — Approximately Aligned Decoding — constrained decoding paper with mixed reception.
- `aS1IhKdLPP.md` (4.75, reject) — Reflection Window — generation method, mixed.
- `bobFZ6WxUd.md` (5.33, reject) — constrained HMM for NAT — methodological.
- `0xUEBQV54B.md` (5.00, reject) — Large Language Monkeys — sampling/inference — mixed.
- `zpBamnxyPm.md` (5.75, reject) — scaling prediction — mixed.
- `kjVgyR3RFr.md` (5.50, reject) — hallucination benchmark quality — mixed.
- `lDbjooxLkD.md` (6.00, accept) — emergent abilities prediction — borderline.
- `gkUyYcY1W9.md` (6.50, accept) — SharedContextBench — stronger benchmark contribution.
- `WQwy1rW60F.md` (6.00, reject) — **LV-Eval**, broadly comparable benchmark contribution; this paper is broader (benchmark + analysis + method) but the analysis is anecdotal and the method's headline metrics are partly tautological.

Reading LV-Eval (6.0, reject) and HelloBench (4.75, reject) carefully: LV-Eval has a tighter benchmark contribution but no method; HelloBench has the same shape as VOLTBench (benchmark for long-form generation, novel but incremental) and landed at 4.75.

The paper under review is **broader than HelloBench** (three contributions vs. one) but the SELB component has framing/coherence problems and the headline metrics partly tautologize the design — pulling it below LongWriter (6.0). The benchmark portion is comparable to or slightly broader than LV-Eval and HelloBench.

Final position: clearly above HelloBench (4.75), comparable to but slightly weaker than LV-Eval (6.0) on rigor, clearly below LongWriter (6.0 accept). Settling at **5.0**, in line with mid-cluster constrained-decoding rejects (MAP 5.25, Reflection Window 4.75, Approximately Aligned 5.75) and slightly above HelloBench.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>