## Summary
Empirical study fine-tuning four open-weight LLMs (LLaMA-3.2-1B, Mistral-7B, Gemma-3-1B, Qwen3-1.7B) on EN + p ∈ {0, 10, 50, 100}% of Arabic translations of MMLU/XQuAD/MLQA test items, evaluated on the English originals. Extends TS-Guessing with choice reordering (IDR), and proposes (without implementing) a Translation-Aware Contamination Detection (TACD) blueprint.

## Strengths
- Question is timely and underexplored: how cross-lingual translation interacts with contamination detection.
- Controlled grid (4 models × 3 datasets × 4 proportions) supplies multi-condition evidence; the across-model monotonic MMLU uplift in Table 2 is a real consistent finding.
- Choice-reordering extension to TS-Guessing (IDR) is a clean operationalization of index-recall vs. reasoning; LLaMA's 0.287→0.643 at 50% is concrete supporting evidence.

## Weaknesses

### Fatal
- **The headline claim is contradicted by the paper's own tables.** §4.1 explicitly says MMLU rises monotonically with p (Mistral 0.577→0.690, Gemma 0.220→0.284, LLaMA 0.332→0.431, Qwen 0.553→0.581) and frames this as evidence of contamination-driven memorization. §4.2 then describes the same scores as "approximately equal" / "near-flat" and uses that alleged flatness as the principal evidence that "translation conceals leakage." XQuAD also shows substantial gains for Gemma/LLaMA/Qwen. The central thesis ("flat p-trend ⇒ translation masks contamination") is thus not just unsupported — it is directly contradicted by Table 2 and by §4.1. This is structural, not editorial.

### Major
- **No matched-p English contamination control.** Every condition contains the full EN split plus an AR proportion p; there is no analogous EN-only ladder. Without it, the "translation masks contamination" claim has no quantitative referent — the observed AR-induced lift is equally consistent with partial cross-lingual transfer. The comparison the paper claims to make is not actually instrumented.
- **TS-Guessing IDR pattern is inconsistent with the memorization story and undiagnosed.** Table 3a: Mistral IDR ≈ 0 (0.000, 0.000, 0.001) across all p despite having the largest MMLU lift; Gemma's IDR *decreases* with p (0.350→0.029→0.005); LLaMA is non-monotonic (0.287→0.643→0.410). The probe is presented as a methodological contribution but registers no memorization in precisely the case (Mistral) where accuracy moves most. The paper neither reconciles nor diagnoses this.
- **Setup conflates LoRA fine-tuning on translated test items with pretraining contamination.** Targeted supervised fine-tuning on AR test items is qualitatively different from incidental pretraining exposure that the surveyed detectors (Min-K%, guided prompting) target. The paper does not justify that one is a faithful proxy for the other, undermining external validity of "concealment" claims.
- **TACD framed as a contribution but is an unimplemented sketch.** The abstract and conclusion list TACD as a deliverable ("we propose…"); §5.3 admits it is a "blueprint." There is no implementation, no thresholds, and no demonstration that existing EN detectors fail on the AR-fine-tuned models while TACD recovers signal — even though both halves are achievable with the models already in hand.

### Minor
- §2 occupies roughly half the paper and largely surveys background (Min-K%, blocklists, etc.) that is only loosely connected to the experiment that follows.
- §3.3 motivation gap: masking an *incorrect* MMLU choice (rather than the correct one) as the memorization probe is not justified; the rationale for treating recall of an incorrect choice as a sharper contamination signal needs to be argued.
- §4.3 references an embedding/cosine-similarity figure for AR→EN that does not appear in the main text; the cosine argument also does not, by itself, imply that pretraining-time AR exposure leaks to EN evaluation.
- The "translation can mask but not eliminate contamination" framing argues against a straw target — nobody claims translation removes already-trained contamination.

### Trivial
- Reported prose numbers (e.g., 0.4936, 0.4109, 0.4707) carry more digits than Table 2 (0.494, 0.411, 0.471); reconcile.

## Nice-to-Haves
- Add an EN-only contamination ladder at matched p so the translation effect can be isolated.
- Run existing EN detectors (Min-K%, guided prompting, DCQ) on the AR-fine-tuned models and show they fail; then instantiate even a minimal version of TACD and show it recovers signal.
- Report seed variance for Tables 2 and 3; several "trends" interpreted in §4 are within plausible LoRA noise.
- Diagnose Mistral's IDR ≈ 0 paired with its largest MMLU lift.

## Removed Points
These points are flagged to be removed, treat them with caution.
- Harsh critic's complaint that training hyperparameters are deferred to Appendix A — an appendix-content nitpick, not a substantive flaw.
- "No evidence Arabic translations of these benchmarks are in pretraining corpora of the four models" — the paper's design is a controlled synthetic study, not an in-the-wild audit; this is scope creep.
- Strength-finder claim about "operationalization across structurally different benchmarks" — kept implicitly as supporting context but not promoted to a headline strength.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Reconcile §4.1 and §4.2 into one coherent reading of the p-trend (monotonic-but-attenuated, not "flat").
- Add the EN-only contamination control and pair it with translation-aware probes.
- Implement a minimal TACD evaluation, or downgrade TACD to a future-work mention in the abstract/conclusion.
- Diagnose the Mistral IDR ≈ 0 anomaly, since it directly undermines the central probe.

## Score and Decision

Anchors retrieved:
- Round 1 (bracketing):
  - OdoS6cH8MP.md (2.00, R1, <3.5) — different topic; similarly fundamental issues led to reject.
  - JQbqaQjV7D.md (3.00, R1) — cross-lingual benchmarking with shallow contribution; comparable severity to this paper.
  - RuY1r1PDdQ.md (3.00, R1) — eval-rethinking paper with weak design; comparable.
  - BltaWJZMeR.md (3.20, R1) — benchmark paper, mixed reviews.
  - Nk1MegaPuG.md (4.25, R1, 3.5–7.5) — contamination evasion paper, more substantive than the one under review.
  - m2NVG4Htxs.md (6.75, R1) — longitudinal contamination study, accepted; much stronger experimental design.
  - Nsms7NeU2x.md (6.75, R1) — quantitative scaling analysis of contamination; more rigorous.
  - tbVWug9f2h.md (7.33, R1) — strong contamination-avoiding benchmark.
  - z8sxoCYgmd.md (8.00, R1, >7.5) — strong unrelated benchmark.
  - GGlpykXDCa.md (8.00, R1) — strong benchmark.
  - jOmk0uS1hl.md (8.00, R1) — "Training on the Test Task" — high-quality work on adjacent topic.

- Round 2 (narrowing to 1.5–5):
  - l5ouuojPGe.md (3.00, R2) — narrow technical contribution, weak study.
  - HsB1sQvXML.md (3.80, R2) — empirical detection study with limited contribution.
  - PUXy7vQ5M3.md (3.75, R2) — benchmarking study with gaps.
  - i28ZjVxl81.md (2.50, R2) — very weak.
  - QiyQJqpcYe.md (4.75, R2) — linguistic-reasoning benchmark, more substantive than this paper.
  - GVNYi74t5L.md (4.25, R2) — multilingual benchmark, larger scope.
  - hFQZmKFtlT.md (3.50, R2) — memorization study with stronger methodology.
  - JL42j1BL5h.md (3.50, R2) — multilingual safety, stronger and broader than this paper.

Round-1 bracket: low (~2.5–4). Round-2 narrowing places this paper near JQbqaQjV7D / hFQZmKFtlT / JL42j1BL5h (3.0–3.5): a controlled but small empirical setup, with a self-contradicting headline claim, a missing control that would isolate the effect, an undelivered framework presented as contribution, and a probe whose results undercut the thesis. It is weaker than Nk1MegaPuG (4.25) which presents a coherent threat model and analysis. It is somewhat stronger than i28ZjVxl81 (2.5) because the underlying question and the controlled grid are real.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>