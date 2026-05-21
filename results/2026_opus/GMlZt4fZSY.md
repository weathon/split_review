## Summary

The paper introduces MobileLLM-R1 (140M/360M/950M), a series of sub-billion-parameter reasoning models trained with a data-centric recipe combining: (i) leave-one-out NLL-based dataset selection on capability-probing sets, (ii) an AutoMixer-derived influence-score weighting scheme for pretraining mixtures, and (iii) iterative mid-training that rejects non-positive-influence samples. The resulting 950M model is reported to match Qwen3-0.6B on multiple reasoning benchmarks at 11.7% of its pretraining tokens, and to substantially outperform OLMo-2 and SmolLM-2 under a matched SFT corpus.

## Strengths
- **Counter-intuitive LOO finding well-supported.** Figure 3 / §2.1.2 shows that removing FineWeb-Edu causes the largest cross-domain degradation, and StarCoder benefits math more than OpenWebMath benefits code — reversing a common belief (Lewkowycz et al., 2022). This is a concrete, non-obvious empirical contribution.
- **Clean apples-to-apples comparison against fully-open baselines (Table 2).** Fine-tuning all baselines on the identical reasoning-SFT corpus isolates the pretraining/mid-training contribution: at 360M, MobileLLM-R1 reaches MATH 19.2 vs. SmolLM2-360M-Instruct's 3.2; at 950M, MATH 57.8 vs. OLMo-2-1.48B-SFT's 53.0. This is the paper's strongest evidence.
- **Post-training pipeline ablation gives actionable findings (Table 1).** Demonstrates (a) Tulu-3 alignment before reasoning is essential, (b) decoupling alignment and reasoning beats joint training (GSM8K 68.5 vs. 53.1), and (c) scientific reasoning data transfers to math/code.
- **Mid-training subsampling shows measurable downstream effect.** Figure 6 shows that influence-positive subsampling consistently outperforms the unfiltered mid-training corpus on MMLU under both CE and KD setups.
- **Full open release of weights, data sources, mixing ratios, and code** ensures reproducibility — a meaningful step beyond partially-open competitors (Qwen3, Gemma, LLaMA).

## Weaknesses

### Fatal
None.

### Major
- **The "benchmark-free, self-adaptive optimization" framing is overstated.** §2.1.1 explicitly constructs the capability-probing datasets to be representative of *exactly the three benchmark domains* (Code, Math, Knowledge) — i.e., GSM8K, MATH, HumanEval, MMLU. The probe is a proxy for the benchmark distribution by design; only literal test-set examples are avoided. Repeated claims (abstract, §2.2 around Eq. 5, Conclusion) that the method optimizes "without exposing benchmarks" are partly semantic. "Leakage-free" or "task-distribution-targeted" would be the honest framing.
- **Missing data-mixing baselines undermine the isolated value of the influence-based mixture.** Figure 4 compares the proposed Datamix only against *uniform sampling* over the same selected corpora. There is no comparison against DoReMi-style proxy reweighting, vanilla AutoMixer at the same scale, or manual SmolLM2/OLMo2-style recipes. Beating uniform is a weak null and cannot isolate whether the gain comes from (a) corpus selection (already established by the LOO study), (b) cross-capability influence aggregation specifically, or (c) any non-uniform weighting. Since the influence machinery is one of the paper's two distinguishing technical contributions, this gap directly affects how much credit it deserves.
- **The headline Qwen3 comparison is one-sided.** The abstract leads with "matches or surpasses Qwen3-0.6B" at 11.7% of the tokens, but on AIME'24 (Figure 9) Qwen3-0.6B sits substantially above MobileLLM-R1-950M (the paper itself reports AIME 15.5 for the 950M; Qwen3-0.6B is higher). Conditioning the token-efficiency claim on the metrics where the method wins while not similarly conditioning on those where it loses is not calibrated. Additionally, Qwen3's 36T-token corpus targets many capabilities (multilingual, agentic, instruction following) outside reasoning, so the "11.7% of tokens" framing partly misattributes a curriculum-scope difference to a curation-method gap. The cleaner story is the fully-open comparison (Table 2, Figure 8/9 vs. OLMo-2 and SmolLM-2), where the wins are decisive and methodologically clean.

### Minor
- **Mid-training "two phases suffice" is asserted without downstream evidence.** §3 reads "convergence" off the Figure 5 influence-score histogram rather than from downstream metric plateauing. A third-iteration result (even null) would substantiate the convergence claim that anchors the mid-training contribution.
- **Mid-training rejection sampling not analyzed for non-target capabilities.** Table 1 already shows MMLU drops when math/code reasoning data is added; aggressive positive-influence filtering against probe sets aligned to those domains could plausibly compound the effect on general capabilities, but the paper does not directly track this across iterations beyond the single MMLU plot in Figure 6.
- **AutoMixer extension hyperparameters introduced without sensitivity analysis.** §2.2 sets $\alpha_{c,t} \propto t$ and "uniform weights across capabilities $c$" with no justification or robustness check. Since these blending choices drive the joint influence in Eq. 4, a brief sensitivity sweep would meaningfully tighten the methods section.
- **No variance on small-N benchmarks where headline gaps live.** Conclusions about whether MobileLLM-R1-950M "matches" Qwen3-0.6B turn on a handful of points on AIME (30 problems) and LiveCodeBench-v6; the paper does not report pass@k or seed variance. Single-run reporting is standard in the field, but cross-model "matches/surpasses" claims at this scale warrant at least one confidence interval.
- **§4 cross-domain SFT transfer claim is loosely supported.** The text states "scientific reasoning data further exhibits strong cross-domain transfer to math and code," but Table 1 shows M+S is best on MATH while M+C+S is best on GSM8K and the C+S row beats M+S on LCBv6 — the cross-transfer signal is mostly carried by the M-vs-M+S comparison rather than the broader claim.

### Trivial
None retained beyond what would be classed as formatting/parser issues.

## Nice-to-Haves
- A head-to-head against at least one learned data-mixing baseline (DoReMi, vanilla AutoMixer, or AutoScale) on the same corpora and token budget — this is the single most impactful addition for substantiating the methods claim.
- Foreground the StarCoder → math transfer finding as a first-class analysis (half a page on whether it is a code-as-structured-reasoning effect or a property of how OpenWebMath was filtered).
- Reframe "benchmark-free, self-adaptive" as "leakage-free, task-distribution-targeted." This is a zero-cost revision that resolves a real overclaim.
- Lead the narrative with the fully-open Table 2 / Figure 8 comparison (e.g., 19.2 vs. 3.2 MATH at 360M) rather than the more contested 11.7% Qwen3 ratio.
- A third mid-training iteration to substantiate the convergence claim with downstream-metric evidence.

## Removed Points
These points are flagged to be removed, treat them with caution.

- *"Strawman two-assumption framing in Abstract/Intro."* — Removed: the paper itself explicitly acknowledges that the first assumption (large size required) is already debunked by Qwen3-0.6B and DeepSeek-distilled variants, so the framing is not deceptive.
- *Demand for confidence intervals as a fatal issue.* — Demoted to Minor (kept above). Single-run reporting is standard in this benchmark setting; the criticism is valid but does not invalidate the central comparison.
- *Strength: "directly challenges the assumption that small reasoning models require massive corpora."* — Trimmed because this overlaps with the same overclaim addressed in the Major weakness; cannot be uncritically retained.
- *Strength: "important problem / fully open-source distinguishes from Qwen/Gemma/LLaMA"* — Kept in trimmed form, but the framing-as-strength bullet about challenging conventional belief was tightened since the wins against Qwen3 are uneven.

## Novel Insights
The leave-one-out finding that **StarCoder (a code corpus) benefits math more than OpenWebMath (a math corpus) benefits code** is the most genuinely novel observation here. It cuts against the prevailing belief (Lewkowycz et al., 2022) that math data disproportionately helps coding and suggests that the structured/symbolic regularities in code may be a stronger reasoning prior than mathematical web text — a result with implications for data-curation priorities in small reasoning models beyond this paper. The framing of FineWeb-Edu as cross-domain "glue" is a useful, paper-specific synthesis but is more confirmatory than novel.

## Suggestions
- Replace the abstract's "11.7% of Qwen3's tokens" headline with the fully-open comparison; reserve the Qwen3 comparison for a per-metric breakdown in the experimental section with the losing metrics shown alongside the winning ones.
- Add at least one learned-mixture baseline (DoReMi or AutoMixer at matched scale) in Figure 4. Without this, the influence-based mixture's marginal value over any non-uniform weighting cannot be established.
- Reframe "benchmark-free" as "leakage-free" in the abstract, §2.2, and Conclusion to match what the method actually delivers.
- Track MMLU (and ideally one general-capability benchmark like ARC) across all mid-training iterations to detect any drift induced by aggressive positive-influence filtering against domain-aligned probes.
- Provide a third mid-training iteration result, even if null, to substantiate the "two phases suffice" / "convergence" claim with downstream evidence rather than only the Figure 5 histogram.
- Add a short sensitivity analysis on $\alpha_{c,t}$ and per-capability weighting in Eq. 4.
- Report pass@k or at least two seeds on AIME and LiveCodeBench v6 given the small-N nature of those benchmarks.

## Axis-by-axis evaluation
- **Originality:** Moderate. Capability-probing-set design and the influence-based mid-training rejection sampling loop are concrete extensions, though built on AutoMixer; not transformative.
- **Importance of the question:** Genuinely useful — sub-billion reasoning models are a deployable target, and the open recipe is a real community asset.
- **Claims well supported:** Mixed. The Table 2 / fully-open story is well supported; the "benchmark-free" and "11.7% of Qwen3" claims are partly overstated.
- **Soundness of experiments:** Adequate. The post-training ablation and matched-SFT comparison are clean; the data-mixing claim leans on a too-weak baseline (uniform only).
- **Clarity of writing:** Good overall. The pipeline and methods are clearly described.
- **Value to the research community:** High. Full open release of data sources, mixing ratios, models, and code at three sub-1B scales is a real artifact contribution.

## Score and Decision

**Round 1 — Bracketing.** Anchors:
- `qgLyKwXVDs.md` (FreeLM, avg 2.00, Round 1, low band): irrelevant pretrain+task framing, far weaker than this paper.
- `mfTM4UdYnC.md` (LogicJitter, avg 2.50, Round 1, low band): unrelated misinformation/logic puzzles, far weaker.
- `v3DwQlyGbv.md` (Paramanu-Ganita, avg 2.33, Round 1, low band): 208M math LM trained from scratch, lacks ablation rigor; this paper is substantially stronger in methodological depth and benchmarks.
- `49jkevjF6x.md` (Lemonade EE, avg 3.00, Round 1, low band): unrelated event extraction.
- `bppG9srkpR.md` (LokiLM, avg 3.60, Round 1, middle band — read in full): a small-LM technical report rejected for vague data description, no ablations, no model release. MobileLLM-R1 is much stronger on every axis (release, ablations, methods).
- `UNxCphTxWp.md` (ProX, avg 6.00, Round 1, middle band — read in full): rejected despite strong empirical work; criticized for unclear marginal contribution and limited scale comparisons. This paper has a comparable scope, similar reviewer concerns (baseline strength).
- `jKHmjlpViu.md` (OpenWebMath, avg 6.00, Round 1, middle band): a dataset release with strong ablation; MobileLLM-R1 is comparable as a release-with-methodology.
- `5BCFlnfE1g.md` (MetaCLIP, avg 6.75, Round 1, middle band): isolates a data effect rigorously; this paper is comparable in framing but with weaker mixture baselines.
- `07yvxWDSla.md` (Synthetic continued pretraining, avg 8.00, Round 1, high band): much more principled, cleaner story — this paper is below it.
- `1oijHJBRsT.md` (Instruction backtranslation, avg 8.00, Round 1, high band): cleaner methodological isolation; this paper is below.
- `f4gF6AIHRy.md` (DiSF / submodular file selection, avg 8.00, Round 1, high band): more rigorous methodological isolation; this paper is below.
- `jOmk0uS1hl.md` (Training on the Test Task, avg 8.00, Round 1, high band): an analytical contribution; not directly comparable but stronger.

Round-1 bracket: **5.0–6.5**.

**Round 2 — Narrowing.** Anchors:
- `sZGZJhaNSe.md` (Aioli, avg 6.25, Round 2 — read in full): a data-mixing framework accepted at 6.25; reviewers raised similar concerns (small-scale validation, insufficient comparison). MobileLLM-R1 has stronger artifact release but weaker theoretical framing — comparable overall.
- `O3SatrdL97.md` (DGA online gradient alignment, avg 5.20, Round 2): a methodologically tighter mixing paper, rejected at 5.20 due to limited evidence. This paper has a stronger release story.
- `54KcduuYeG.md` (AutoScale, avg 5.50, Round 2): rejected at 5.50 on similar "limited comparisons" grounds.
- `aqok1UX7Z1.md` (ADO, avg 5.50, Round 2): accepted at 5.50 despite mixed reviews; comparable in scope to this paper's mixing method.
- `4xBew7kuYB.md` (Effects of training data on SLMs, avg 5.50, Round 2): a careful analytical study, rejected at 5.50.
- `79ZkWgY2FI.md` (Small-to-Large Generalization, avg 5.25, Round 2): accepted at 5.25.
- `mao3y822aM.md` (NanoLM, avg 5.50, Round 2): rejected at 5.50.
- `Fq8tKtjACC.md` (Phi-1 / Textbooks Are All You Need, avg 6.00, Round 2 — read in full): the closest analog — small model + curated data recipe — rejected at 6.00 despite strong results, on grounds of methodological transparency and not fully isolating data quality contribution. MobileLLM-R1 is more transparent (full data sources released) but raises similar concerns about isolating the data-mixing contribution.

**Comparison.** This paper sits squarely with Phi-1 (6.00, reject) and Aioli (6.25, accept) in scope and weight. Compared to Phi-1, MobileLLM-R1 has stronger openness and a cleaner Table 2 comparison; compared to Aioli, it has weaker mixture-method isolation (only uniform baseline) and slightly overstated framing. The fully-open Table 2 result is a genuinely strong artifact, but the headline methodological claim (influence-based mixing) is undersupported relative to similarly-scored papers.

Settling near **5.5**: above the cluster of rejected mixing papers (5.20–5.50) due to the strong release and the LOO + Table 2 evidence, but not high enough to clear Aioli (6.25) or DiSF (8.00) given the missing learned-mixture baseline and the partially overstated framing.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>