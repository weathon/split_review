## Summary
The paper introduces the Language Confusion Gate (LCG), a 2-layer MLP that consumes the base LLM's hidden state and dynamically masks tokens from disallowed language families (CJ / Latin / Symbols / Low-Res) at decode time. A mechanistic observation — that output embedding norms are systematically larger for high-resource-language tokens, biasing logits — motivates a *norm-adjusted self-distillation* training procedure. LCG reduces CJ and Latin confusion rates by ~order of magnitude across Qwen3, Llama3.1, Gemma3, and GPT-OSS while preserving BLEU/Pass@k.

## Strengths
- **Norm-decomposition analysis (§3.2, Table 1, Figure 2).** A concrete, mechanistically grounded observation that output-embedding-norm imbalance contributes to confusion, with a clean qualitative example where dividing logits by ‖e_v‖ removes CJ tokens from the top-10 in a Hebrew translation. The authors themselves explicitly flag the mechanism's limits (cannot explain English↔Chinese or low-res↔low-res confusion), which is appropriately scoped.
- **Norm-adjusted self-distillation gives consistent gains over unadjusted (Table 3).** E.g., Llama3.1-8B Latin% 5.7 → 2.9, Qwen3-8B Latin% 6.2 → 2.0 when norm-adjustment is added to the training signal. This is a genuinely useful empirical finding.
- **Deployment-relevant engineering.** Intervention rate is ~0.33–0.38% of tokens; wall-clock overhead is ~0.4% per generation step (§6); compatible with speculative decoding.
- **Broad model coverage** across Qwen3, Llama3.1, Gemma3, GPT-OSS and both thinking/no-think modes — wider than typical for an inference-time intervention.

## Weaknesses

### Fatal
None.

### Major
- **Missing the most natural baseline: norm-adjusted decoding alone.** §3.2/Figure 2 already shows that dividing logits by ‖e_v‖ removes the top-1 confusion token. The gate is *trained* to imitate norm-adjusted top-k/p membership (§4.2 eq. for y*). Without reporting "decode with logit_i / ‖e_i‖" as a standalone baseline, it is not clear how much of LCG's gain comes from the learned gate versus from the norm correction it is built to approximate. This is the single most important ablation given the paper's own framing.
- **No head-to-head comparison with the closest prior interventions (Nie et al., 2025; Ji et al., 2025).** §2 explicitly identifies both as inference-time, non-retraining methods that occupy the same niche. §5.3 instead compares against ICL, greedy decoding, and ORPO — two of which are weak strawmen and the third (ORPO) the authors themselves show suffers general-capability degradation. The "more targeted and effective" claim is therefore not benchmarked against any directly comparable method.
- **Granularity ceiling materially narrows the contribution.** The four-family taxonomy (CJ / Latin / Symbols / Low-Res) plus Rule 1 ("Low-Res tokens are never masked") means LCG structurally cannot intervene on (a) Latin-vs-Latin, (b) low-res-vs-low-res, or (c) Chinese-vs-Japanese confusion. The authors acknowledge this in §6, which is good, but it means the headline "language confusion" framing in §1 (100+ languages) overshoots what the method actually does: it is a script-family gate for high-resource→single-script-low-resource translation.

### Minor
- **Train/eval split for FLORES+ is not stated.** §5.1 lists FLORES+ as a training source and §5.2 evaluates on FLORES+ (Arabic, Hebrew, Korean, Thai). The paper does not specify which FLORES split goes where. Even if a non-overlapping split is used, stating it would rule out in-domain inflation of Table 3 numbers.
- **Mechanism does not fully match the data for GPT-OSS.** Table 1 reports 0.00% CJ in the top-norm bucket for GPT-OSS, yet Table 4 still shows GPT-OSS exhibits CJ confusion (0.38%). The paper acknowledges in §3.2 that norm bias "can account for a subset of such errors" but does not directly discuss this specific contradiction.
- **Code-switch preservation framing in §5.3 / Table 5.** For Qwen3-8B the code-switch rate drops 46.34% → 25.90%, while the ground-truth reference rate is 38.36%. The paper compares to Claude (23.29%) to argue preservation, but the more natural reference is the ground truth, against which LCG is ~12 absolute points low. The paper does acknowledge "LCG does reduce the rate of code-switching" — so the issue is mainly that the abstract's "without negatively impacting task performance" should also flag this side-effect.
- **Single-rule ablations not isolated.** The "No Rule" condition in Figure 3 toggles Rules 1/2/3 jointly. Rule 3 ("always allow previous non-symbol token's family") plausibly does most of the work at intra-sentence positions, but its individual contribution is not quantified.
- **§3.1 statistics ("top-1 is confusion token 56.74%", "correct in top-3 99.29%") are reported only on Qwen3-8B**, yet they motivate the whole approach. A short cross-model replication would strengthen the case.

### Trivial
- §5.2's argument for skipping LCB (Marchisio et al., 2024) — "its language detector sometimes produces wrong results" — is reasonable but removes a point of external comparability with prior work; reporting LCB numbers alongside, even with a caveat, would help readers calibrate.
- Headline reductions like 1.0% → 0.0% and 0.12% → 0.00% involve very small absolute counts; without N or variance these are best read as directional. (Marked minor rather than major because the *Latin* numbers — e.g., 12.1% → 2.0%, 8.4% → 2.9% — do carry the result on their own.)

## Nice-to-Haves
- Per-language breakdown of intervention frequency and false-mask rate, especially for low-resource languages.
- A language-specific (not script-family) extension that addresses Latin↔Latin and low-res↔low-res confusion (the authors flag this as future work).
- Failure-mode case studies — the 13.3% of human-validated code-switches that LCG disallowed.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *"Latin confusion not reported for HumanEval-XL"* (harsh critic §5.3 note). The paper restricts Latin evaluation to FLORES-NO-LATIN because Latin characters are legitimately present in coding tasks (§5.2 explicitly explains this), so omitting Latin% on HumanEval-XL is a deliberate methodological choice, not an oversight.
- *"No variance / CIs / multiple seeds reported"* — Single-run evaluation is standard for LLM decoding benchmarks at this scale; moved to nice-to-have and noted briefly under Trivial only for the smallest-N cells.
- *"Abstract overclaims with order-of-magnitude reductions on near-floor numbers."* The larger reductions (12.1% → 2.0%, 8.4% → 2.9%) are not near-floor and do support the qualitative claim; the harsh critic's framing is too strong.

## Novel Insights
The output-embedding-norm decomposition (logit = ‖h‖·‖e_v‖·cos) and the empirical demonstration that high-resource language tokens dominate the top-norm bucket is the genuinely novel piece. Using this norm correction not as a decoding fix but as the *supervision signal* to distill into a small gate is a clean idea: it converts a coarse mechanistic correction into a learned, sparse, deployment-friendly intervention. Beyond this, no insight in the reviews exceeds what the paper itself surfaces.

## Suggestions
1. Add the standalone "decode with norm-adjusted logits" baseline to every table — this is the most important missing comparison.
2. Run head-to-head against Nie et al. (2025) and Ji et al. (2025) on at least one shared setting.
3. Explicitly state the FLORES+ train/eval split, or provide a held-out benchmark the gate was not trained on.
4. Decompose the contribution of Rules 1, 2, 3 individually.
5. Soften the abstract's framing to reflect the script-family scope and the legitimate-code-switch reduction shown in Table 5.

---

## Evaluation on Required Axes
- **Originality:** moderate — norm-bias observation and using it as a distillation signal are fresh; the gating mechanism itself is straightforward.
- **Importance:** real practical problem; affects deployed multilingual LLMs.
- **Support for claims:** partial — the main reductions are convincing, but the "more targeted and effective than alternatives" claim is undermined by missing baselines (norm-adjusted decoding, Nie, Ji).
- **Soundness of experiments:** adequate breadth across models; weakened by undisclosed FLORES train/eval split and lack of the most natural ablation.
- **Clarity:** generally clear; method and rules are well described.
- **Value to community:** practical, low-overhead recipe that practitioners can plausibly adopt.

## Score and Decision

Anchor comparison (all retrieved):
- `fSbPwHjdDG.md` (3.00) — Llama causal-intervention paper. Narrower scope, weaker results than this paper.
- `BCyAlMoyx5.md` (5.67) — Crosslingual capabilities; broader analysis, mixed empirical support; comparable rigor level.
- `HMa8mIiBT8.md` (6.00) — Cross-lingual consistency analysis; similarly mid-tier mechanistic story.
- `eznTVIM3bs.md` (5.25) — Babel Tower hypothesis; this paper is more practical/engineered, similar empirical weight.
- `tvQNysCP7C.md` (4.20) — KV-Cache Attention-Gate; analogous "plug-in gate" framing, baselines criticized — close peer; LCG is somewhat more empirically grounded.
- `774elYc5tw.md` (4.25) — Constrained decoding for faithfulness; similar baseline-coverage complaints.
- `PL6e9HkVxk.md` (4.25) — Decoder-level safety defense; similar profile, rejected.
- `Wv9Gl1bFbc.md` (3.00) — Self-distillation for fine-tuning small LMs; clearly weaker than LCG.
- `8wjWm5jr1w.md` (6.00) — Semantic-revision distillation; comparable.
- `uZ5K4HeNwd.md` (7.00) — Self-distillation through time for fast LLMs; stronger, more impactful contribution than LCG.
- `NCrFA7dq8T.md` (6.60) — Structural similarities across languages; broader, more mechanistically rigorous.
- `4z3IguA4Zg.md` (6.00) — Dynamic Correction Decoding for hallucinations; very close peer in spirit and scope, accepted.
- `DayPQKXaQk.md` (7.00) — Constrained decoding for cross-lingual label projection; tighter problem, cleaner evaluation than LCG.

LCG sits above the 3–4 cluster (it is genuinely empirically grounded with a useful mechanistic insight) but below 6.0-anchored peers like `4z3IguA4Zg` and `DayPQKXaQk`, which carry stronger or more carefully baselined evaluations. It is closest to `tvQNysCP7C` (~4.2) and the 5–5.7 cluster — better engineered than 4.2 but with the same class of missing-baseline complaint.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>