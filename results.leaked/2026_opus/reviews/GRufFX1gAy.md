## Summary
InnoGym proposes a framework and benchmark (iBench + iGym) for evaluating "innovation" in AI agents along two axes: Performance Gain G (improvement over the best-known solution) and Novelty N (LLM-judged minimum methodological distance to known solutions). The benchmark curates 18 "Improvable" engineering/competition tasks, of which 10 are evaluated against three agent scaffolds (MLAB, CodeAct, AIDE) using DeepSeek-v3.1, with additional ablations on Circle Packing.

## Strengths
- **Two-axis (G, N) formulation is a real conceptual contribution.** Eqs. (2)–(3) and the Solved/Improvable/Exploratory taxonomy (Sec. 2.3) give a defensible way to talk about "novel-but-not-better" or "better-but-not-novel" solutions, which most ML-engineering benchmarks (MLE-Bench, MLAgentBench, MLRCBench, InnovatorBench) explicitly do not measure (Table 1 contrast is fair).
- **Principled multi-stage task curation.** The 197 → 72 → 18 pipeline (Fig. 2; Sec. 3.1–3.2) — resource availability, evaluator validation, normalization with Pearson ≥ 0.9 / Kendall-τ ≥ 0.8, and explicit visible/hidden partitioning — is more rigorous than typical benchmark curation.
- **Concrete diagnostic finding.** Table 2 shows that on the same tasks where agents achieve mid-to-high novelty (e.g., RCIC novelty 83.33 for CodeAct), performance is catastrophic (RCIC G = −99.67). Read carefully, this is real evidence that novelty alone does not predict effectiveness on these tasks.
- **Useful Circle Packing analyses.** Fig. 6(a)–(c) — execution time, base model ablation, and the temperature sweep showing a "sweet spot" near 0.5–0.75 — exercise the metrics in a controlled regime and yield interpretable trends.

## Weaknesses

### Fatal
None. The empirical issues below are serious but the contribution is verifiable on the page and not invalidated by a single irrecoverable error.

### Major
- **Novelty metric is the load-bearing contribution but its reliability is not demonstrated in the main paper.** N is operationalized as Codex-extracted features → GPT-5 rubric over six 0–4 dimensions → averaged and aggregated by min over S_known → rescaled to [0,100] (Sec. 3.4, 4.1). The main paper offers no inter-judge agreement, no rubric/extraction perturbation, no human-expert correlation, and no sensitivity to which LLM serves as judge. The paper points to Appx. F for "behavior and reliability of D," but the principal evidence supporting the entire reason to adopt this benchmark over MLE-Bench/MLRCBench/InnovatorBench is not in the main text.
- **Every reported G in Table 2 is strictly negative**, with averages −24.32 (MLAB), −41.58 (CodeAct), −42.68 (AIDE) and the best single result a tie (CodeAct on CirclePacking, G = −0.008). This means the (G, N) decomposition is never exercised in the regime it was designed to discriminate — performance vs. conceptual vs. breakthrough innovation (Sec. 2.2) all live in the G ≥ 0 region. The headline framing of "novel approaches without robustness" is therefore not cleanly separable from the simpler reading "broken submissions happen to look different from working baselines." At least one positive-G data point is needed to validate that (G, N) actually discriminates the three innovation regimes the framework defines.
- **Self-judging is unaddressed.** GPT-5 is the Novelty judge (Sec. 3.4/4.1) and is also one of the backbone models compared in Sec. 4.3 / Fig. 6(b). The paper does not control for, or even discuss, evaluator-agent identity overlap, despite the GPT-5 column being part of a headline comparison.
- **Best-of-3 reporting hides exactly the variance that matters here.** Sec. 4.1 reports the best of three runs and "/" if all three fail. Given how many Table 2 entries are "/" and how long-horizon agent runs vary, the protocol both discards the failure mass (which the paper itself argues is the central finding) and precludes any statistical claim about agent ordering. For a benchmark marketed on reproducible cross-agent comparison, at minimum mean ± std and a failure-rate column are needed.
- **Symbol overloading of G in Sec. 4.3 ("Temporal Dynamics").** The text says "each is measured relative to the previous time step" and then concludes "G remains non-negative throughout, indicating a stable, monotonically improving search process." This G is a different quantity from the G in Table 2 (defined relative to V*_known, which is uniformly negative). Using the same symbol for both invites the reader to interpret non-negative step-wise G as evidence of approaching SOTA, which the Table 2 data contradicts.

### Minor
- **Framework-vs-benchmark scope mismatch.** Sec. 2.3 motivates (G, N) partly through Exploratory tasks where N = ∞ is natural, but Sec. 3 paragraph 1 explicitly excludes Solved and Exploratory tasks. The benchmark in its current form instantiates only the Improvable slice; the abstract and intro should not let the broader taxonomy be read as something the empirical contribution exercises.
- **Min-over-S_known novelty is conceptually fragile.** N(s) = min_h D(s, h) (Eq. 3) means a solution that hybridizes two known approaches can score higher novelty than either parent, while a genuinely new method resembling one known h is penalized. The framework section does not discuss or compare alternative aggregations (farthest-h, coverage against the hull of known approaches), even briefly.
- **Cross-domain claim vs. evaluated subset.** Table 1 emphasizes cross-domain coverage (ML, OR, Systems, Math, Science), but Sec. 4.1 restricts the main experiment to 10 "more tractable" tasks. The cross-domain framing is stronger than what Sec. 4 actually exercises.
- **iGym is presented as a co-equal contribution but the main paper does not justify it.** Sec. 3.5 leans entirely on appendix references for the claim that OpenHands/AutoGen/LangGraph "lack recovery, concurrency, and consistent tool management." Without at least one concrete example or head-to-head test in the main text, iGym reads as a wrapper rather than a contribution.
- **AlphaEvolve comparison overstates closeness.** Sec. 4.3 frames Gemini-2.5-Pro (2.49) and GPT-5 (2.44) as "closely approaching the AlphaEvolve of 2.65," which is a non-trivial gap on this scale and against an autonomous discovery system; the wording should be calibrated.

### Trivial
- "A hypothetical GPT-5" wording in Sec. 4.3 reads as drafting residue.

## Nice-to-Haves
- A small human study (50–100 (solution, h) pairs) correlating expert dissimilarity judgments with the rubric output — the single highest-leverage addition for the paper's main contribution.
- Judge-side ablations (different LLM judges, different seeds, extraction-prompt perturbations) reporting score stability.
- At least one configuration that achieves G > 0 on some task (e.g., a seeded-then-refined agent) to show the (G, N) plane is non-degenerate.
- Per-task Pearson/Kendall numbers from the absoluteness normalization (Sec. 3.2) so readers can see which tasks barely passed.
- Reframing the empirical narrative around the verified finding ("agents fail to produce valid submissions or underperform baselines") and positioning Novelty as a diagnostic of *how* they fail, rather than evidence of a creativity/effectiveness gap.

## Removed Points
*These points are flagged to be removed, treat them with caution.*

- **"AIDE only reaches 2.61 from a 2.59 seed — comparison to AlphaEvolve (2.65) is misleading" (harsh critic).** This conflates two distinct Sec. 4.3 experiments. The 2.59 → 2.61 trajectory is from the "Impact of Prior Knowledge" study with an AIDE+Gemini seed (Fig. 5). The AlphaEvolve comparison in Fig. 6(b) is the base-model ablation (Gemini 2.49, GPT-5 2.44, DeepSeek 2.40, AlphaEvolve 2.65), not started from a seed. The 0.02-improvement framing is wrong; the calibration concern (2.49 vs 2.65 is not "closely approaching") is kept in Minor.
- **Generic Strength Finder claims** (e.g., "vector-space representation provides richer visualization than scalars," "iGym provides asynchronous tool dispatch and recovery"): kept only as supporting context, not as primary strengths, because they describe features rather than evidence of effectiveness.

## Novel Insights
None beyond the paper's own contributions. The framework's most interesting move — separating performance breakthroughs from methodological novelty in a single (G, N) space — is the paper's own, not something the reviews surface independently.

## Suggestions
- Run the metric-validation study (judge agreement, rubric robustness, human correlation) and put a condensed version in the main paper; this is the single change with the highest return.
- Report Table 2 with mean ± std across the three runs and a separate failure-rate column; do not discard "/" entries.
- Construct at least one G > 0 configuration (seeded agent, iterative refinement loop) so the (G, N) framework has a non-degenerate empirical point.
- Use distinct symbols for "G relative to V*_known" (Table 2) and "G relative to previous step" (Fig. 6a); restate the "monotonic improvement" claim accordingly.
- Quantify the self-judging risk: report Novelty scores under at least one alternative judge LLM, especially for the GPT-5 backbone row.
- Either (a) restrict framework claims in Sec. 2 to the Improvable slice the benchmark actually instantiates, or (b) add a small set of Solved/Exploratory tasks to demonstrate the broader taxonomy.

## Axis-by-Axis Assessment
- **Originality:** Moderate-to-high. The (G, N) decomposition and the Improvable/Solved/Exploratory taxonomy are conceptually novel relative to MLE-Bench-style benchmarks.
- **Importance of research question:** Genuine. Measuring methodological distinctness alongside performance is a real gap.
- **Are the claims well-supported?** No on the central claim. "Novelty without robustness" cannot be cleanly demonstrated when every G in Table 2 is negative and the Novelty metric is itself unvalidated.
- **Soundness of experiments:** Limited. Best-of-3 reporting, self-judging, and the G symbol overloading collectively undermine the trustworthiness of specific rankings and trends.
- **Clarity of writing:** Adequate. Definitions are clean; some narrative framing (Sec. 4.3 temporal dynamics, AlphaEvolve comparison) overstates the evidence.
- **Value to the research community:** Real but contingent. The curated 18 tasks and the (G, N) formulation are usable artifacts; the Novelty metric requires validation before it can be trusted by downstream users.

## Score and Decision

**Anchors retrieved:**

Round 1 (bracketing):
- `o3V7OuPxu4.md` — StarCraft II Arena, 3.00, Reject — weaker, less rigorous than InnoGym.
- `nE3flbe88p.md` — TeamCraft, 3.25, Reject — narrower scope, weaker than InnoGym.
- `2wwPG1wpsu.md` — LST-Bench, 2.50, Reject — much weaker than InnoGym.
- `YGDWW6rzYX.md` — ZeroSumEval, 3.00, Reject — narrower scope, weaker.
- `zAdUB0aCTQ.md` — AgentBench, 6.20, Accept — more comprehensive, better validated; clearly above InnoGym.
- `IWC6zUEVcL.md` — MCU, 4.00, Reject — comparable conceptual ambition, similar validation gaps.
- `fp6t3F669F.md` — AgentQuest, 6.25, Accept — better validated than InnoGym.
- `6pPYRXKPpw.md` — D3IL, 7.33, Accept — different topic, stronger.
- `6s5uXNWGIh.md` — MLE-Bench, 8.00, Accept — far stronger curation, clearly above.
- `YrycTjllL0.md` — BigCodeBench, 9.00, Accept — far stronger, much above.
- `XmProj9cPs.md` — Spider 2.0, 8.00, Accept — stronger, above.
- `or8mMhmyRV.md` — MaestroMotif, 7.75, Accept — different topic, stronger.

Round-1 bracket: roughly **[3.5, 5.5]** — clearly below well-validated benchmarks like MLE-Bench and ScienceAgentBench, clearly above weak rejects.

Round 2 (narrowing):
- `c2C2NQKjZw.md` — Codev-Bench, 4.25, Reject — narrower scope, less ambitious framework; InnoGym slightly above.
- `ga1IraEqTE.md` — A2Perf, 4.75, Reject — broader scope but limited novelty in metric design and limited baselines; comparable to InnoGym, perhaps slightly stronger because InnoGym's central metric is unvalidated.
- `w0es2hinsd.md` — RD2Bench, 5.25, Reject — most analogous: new benchmark, custom metrics, limited validation; InnoGym slightly weaker because its central novelty metric is the contribution yet untested in main text, and all G < 0 undermines the headline.
- `hDkLpu1E64.md` — FEABench, 4.50, Reject — comparable rigor, narrower domain.
- `vJ0axKTh7t.md` — Labyrinth of Links, 6.25, Accept — better-validated metric, above InnoGym.
- `6z4YKr0GK6.md` — ScienceAgentBench, 6.00, Accept — far better expert validation, broader and more thoroughly assessed; above InnoGym.
- `W48CPXEpXR.md` — Hallucinating LLM Could Be Creative, 5.00, Reject — similar in attempting to measure creativity, similar in shallow validation; comparable.
- `toqQYz2N2X.md` — TAG-EQA, 4.00, Reject — narrower, weaker.

Round-2 narrowing: InnoGym sits below ScienceAgentBench (6.00) and Labyrinth (6.25) — both have better-validated central metrics — and below or comparable to RD2Bench (5.25) — analogous concept paper with similar issues. InnoGym is above Codev-Bench (4.25), FEABench (4.50), and A2Perf (4.75) in conceptual ambition but its central metric being unvalidated and all-negative G pull it down. The closest match is between A2Perf/RD2Bench. Given the unvalidated-Novelty issue is more central to InnoGym's contribution than the corresponding weaknesses in RD2Bench, I place it slightly below RD2Bench.

Final score: **4.0**.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>