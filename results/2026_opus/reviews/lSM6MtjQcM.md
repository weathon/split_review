Now let me search for calibration anchors.Now I have enough information. Let me compose the final review.

## Summary
AetherCode is a benchmark paper introducing 456 problems collected from premier programming competitions (IOI, ICPC, NOI, USACO, CCPC, 2024–2025), accompanied by a hybrid test-case construction pipeline (G-V Agent + 67 expert annotators + an elite gold-medalist audit team), a multi-dimensional categorization scheme, and an evaluation of 17 contemporary LLMs. The headline contributions are (i) sourcing from premier rather than online judges, (ii) a TPR/TNR-based test-suite quality framework with a reported 100%/100% achievement on the collected solution corpus, and (iii) showing a substantial Pass@1 gap between current top LLMs (o4-mini-high at 35.5%) and the field, with even the best model failing most "Hard" and "Extreme" problems.

## Strengths
- **Premier-competition sourcing is a genuine differentiation.** Table 1 contrasts AetherCode's "Premier Contests" source against CodeForces/AtCoder/LeetCode-based benchmarks (LiveCodeBench, CodeELO, LiveCodeBench Pro, USACO Benchmark, CodeContests). Section 2.1 documents systematic collection of OI (IOI, NOI, USACO) and ICPC series problems (regional, championship, World Finals) with PDF→Markdown+LaTeX conversion and manual proofreading. This addresses a real gap: prior benchmarks under-cover problems that require complex large-scale implementations.
- **Substantial infrastructure for test-case quality.** Section 2.3 reports a curated 30,000+ human-solution corpus (≥5 correct, ≥20 incorrect per problem), automated G-V Agent generation (Section 2.3.2), 67 competitive-programming experts with Codeforces ratings ≥2000 (Section 2.3.3), and an elite audit team of ICPC-gold-medalist problem setters. The reported automated-stage TNR of 89.9% before expert correction is unusually honest reporting.
- **Multi-dimensional categorization enabling fine-grained diagnostics.** Section 2.2 defines four difficulty levels, 10 major and 144 sub-category algorithmic tags, plus metadata (date, organizer, contest scope). Table 4 then leverages this to show category-specific weaknesses (e.g., GPT-4.1's math performance is significantly weaker despite leading non-reasoning overall; computational geometry and tree problems collapse for nearly all models).
- **Clear discrimination across the model zoo.** Table 3 shows a wide spread from o4-mini-high (35.5%) to GPT-4o (4.4%), with consistent ordering across Easy/Medium/Hard tiers, demonstrating the benchmark is not yet saturated.
- **Useful failure-mode diagnostics.** Section 3.3 breaks errors into Wrong Answer / TLE / Runtime Error / Compile Error and surfaces concrete patterns (Claude favoring correctness over efficiency; GLM-4.5's high compile-error rate driven by emitting Python when instructed to use C++).

## Weaknesses

### Fatal
None.

### Major
- **The 100% TPR / 100% TNR headline is measured against the same solution corpus that drove test-case construction.** Section 2.3.3 explicitly states experts were "tasked with constructing targeted test cases specifically designed to fail the various incorrect solutions we had collected," and Section 2.3.1's TPR/TNR is then evaluated against precisely that collected solution corpus. This is a closed-loop measurement: the test suite is engineered to discriminate the corpus it is then graded on. The claim "AetherCode is the first benchmark that sets such a high standard for test cases" is the paper's flagship methodological contribution, and as reported it does not constitute evidence that the test suite would reject *novel* incorrect solutions (e.g., the ones LLMs actually produce in Table 3). An out-of-sample evaluation (held-out solution corpus, agreement with official problem-setter tests on USACO subset, or TNR measured against LLM-produced incorrect submissions) is needed to make the central claim defensible.
- **Contamination is identified as a core motivation but never analyzed.** Section 2.1 annotates contest dates "for decontamination purposes," and Table 3 shows a substantial 2024→2025 drop for most models (o4-mini-high 35.8→32.6; DeepSeek-R1 23.4→14.3; Qwen3-235B-Thinking 23.6→11.6; Gemini-2.5-Pro 33.7→25.0). The paper presents the split as evidence of difficulty/recency but performs no probe (e.g., memorization tests on problem statements, partitioning by model training-cutoff date, or n-gram overlap) to disentangle contamination from genuine difficulty differences. With 88% of problems from 2024 — overlapping the training windows of the evaluated models — every cross-model gap in the table is partly ambiguous on this axis. For a benchmark whose related-work section criticizes prior datasets for contamination risk, the absence of any actual contamination analysis is a substantive gap.

### Minor
- **The "Extreme" tier is inconsistent with the human-vs-LLM gap framing.** Section 2.2 defines Extreme as problems "no human contestant was able to solve during a competition." The conclusion (Section 5) and main-result narrative use Extreme-tier LLM performance to argue about the gap with top humans, but by construction top humans also failed these problems, so Extreme performance cannot evidence such a gap. With only 20 problems (Fig. 2) and most models scoring 0, this tier also adds substantial noise without informative discrimination.
- **No variance/significance for a 4-sample protocol.** Section 3 reports "each model is evaluated four times in each problem, and the average numbers are reported," with no confidence intervals or significance tests. Many rank-orderings in Tables 3 and 4 turn on differences of <1 point (Qwen3-235B-Thinking 22.2 vs. DeepSeek-R1 22.3; Qwen3-32B 16.3 = Claude-4.5-Sonnet-thinking 16.3), and as published the reader cannot tell which are stable. Bootstrap intervals over the 4 samples × 456 problems would be trivial to add and would materially strengthen the evaluation chapter.
- **Table 1's ★★★ rating for AetherCode is in tension with the paper's central positioning.** Table 1 lists AetherCode at ★★★ while CodeContests, USACO, CodeELO, and LiveCodeBench Pro are ★★★★ — directly contradicting the prose argument that premier-contest sourcing makes AetherCode harder than these prior benchmarks. Either the rating or the framing should be revised so the comparison is internally consistent.
- **Language-selection confound in Pass@1 comparisons.** Section 3.3 notes that "over half" of GLM-4.5's compile errors stem from emitting Python when instructed to use C++, which implies a specific language requirement was prompted, but the main text does not specify the harness behavior (which languages are allowed for which models, whether mismatches are graded as compile errors versus converted, retry policy). Although the paper defers harness details to an appendix, the appendix is not visible in the parsed text — to the degree it is unspecified, the cross-model gap between GLM-4.5 and similar-tier models in Table 3 is partly a property of the harness rather than the model.
- **G-V agent strength reporting is opaque per-category.** Section 2.3.2 reports the automated stage achieving 89.9% TNR aggregated, but does not say which problem categories the automated stage tends to miss vs. where expert correction is most needed. Knowing this would help readers reason about how reliable the test cases are on novel LLM outputs (especially since LLM-failure patterns may concentrate in those same categories).

### Trivial
- The Tree category (Table 4) is degenerate for many models (≤7.3, with most reasoning models at 0–4.2). The text acknowledges in passing that this is partly a distribution artifact, but the per-category discussion still treats it as if it reflects stable capability.

## Nice-to-Haves
- A targeted demonstration: pick problems where the expert-annotation layer added test cases that flipped a model verdict in Section 3, and show *which* corner-case bug in *which* model's output was caught only because of the expert layer. This converts "we have higher-quality tests" from an assertion to a demonstration.
- For the USACO subset (where official test cases are publicly available), report TPR/TNR agreement between AetherCode's tests and the official problem-setter tests on a large solution pool. This would be a clean independent validation.
- Quantify how often expert judgment overrode within-contest solver-count rankings in the difficulty assignment (Section 2.2), so readers can calibrate how much of the difficulty axis is subjective.
- Probe contamination directly: e.g., n-gram overlap or completion-given-prefix tests on 2024 problem statements vs. 2025, broken out by model.

## Removed Points
*These points are flagged as removed; treat them with caution.*

- **Harsh critic's harness-specification critique broadly framed.** The critic notes temperature, reasoning budget, system message, and prompt template are not given in the main body. The paper explicitly says "Detailed settings of the experiment are presented in Appendix A," and the parser strips appendices from all submissions in this pipeline. Per the hard rule, appendix-deferred details should not be counted as missing. Demoted to a Minor mention only insofar as the language-confound issue is visible in the main text.
- **Strength: "Clear model discrimination across difficulty tiers."** Retained but de-emphasized — the discrimination claim is partly undermined by the Major weakness on contamination and the Minor weakness on lack of variance reporting.
- **Strength: "Failure diagnosis analysis providing qualitative insights."** Retained but it is qualitative-only; the language-confound minor weakness comes directly from one of these diagnostic observations.

## Novel Insights
None beyond the paper's own contributions. The paper's own observation — that even SOTA reasoning models (o4-mini-high at 35.5% Pass@1) are far from saturating premier-contest problems — is the genuine empirical novelty, and the failure-mode breakdown (Claude trading efficiency for correctness on hard problems; GLM-4.5's language-instruction failures) is concrete and useful for practitioners.

## Suggestions
- Re-ground the headline TPR/TNR claim with at least one out-of-sample measurement (held-out solution corpus, or TNR computed against LLM-produced incorrect solutions from the evaluation in Section 3). This is the highest-leverage fix because the rest of the paper rests on the test-suite quality claim.
- Add a contamination probe using the 2024/2025 split that is already in the data — partition by each evaluated model's training cutoff and report whether performance drops align with training-window boundaries.
- Add bootstrap confidence intervals over the 4 samples per problem to Tables 3 and 4 so close rank-orderings are interpretable.
- Either revise Table 1's difficulty stars to be consistent with the prose comparison, or revise the prose to be consistent with the rating — the two should not disagree.
- Separate or remove the "Extreme" category from the human-vs-LLM gap discussion (since humans also failed those problems); discuss Extreme as a frontier-stress-test rather than as evidence of a human-LLM gap.
- Specify in the main text which language is required (per problem? globally C++?), how mismatches are handled, and the reasoning-budget configuration for thinking models — these affect interpretation of every cross-model comparison.

## Evaluation on key axes
- **Originality.** Moderate. Premier-contest sourcing is a real differentiation from LiveCodeBench / CodeELO-style benchmarks, but the underlying recipe (collect contest problems → build test cases → evaluate frontier models) is well-trodden.
- **Importance of the research question.** Solidly important — current code-reasoning benchmarks are saturated and the community needs harder ones.
- **Soundness of claims.** Mixed. The empirical model rankings are credible; the central "100% TPR/TNR" claim is methodologically weaker than presented because it is in-sample.
- **Soundness of experiments.** Adequate but under-rigorous: no variance, contamination unexamined despite being motivated, harness conditions deferred.
- **Clarity.** Generally good; structure is conventional and easy to follow.
- **Value to the community.** Real, especially if the test suites and 30k-solution corpus are released and the test-quality claim is re-grounded. The premier-contest data layer is genuinely useful.

## Calibration

**Round 1 (bracketing):**
- Weak band: NlY3XppPt3 (avg 2.00, Reject — programming-language benchmark, far weaker scope); BltaWJZMeR (3.20, Reject — DataSciBench, generic LLM benchmark); koza5fePTs (2.00, Reject — planning benchmark); ly10tMV6cD (3.25, Reject — structure-rich text benchmark). All weaker than AetherCode in infrastructure and execution.
- Middle band: chfJJYC3iL (LiveCodeBench, 6.25, Accept — directly comparable, online-judge problem collection with live updating); TVFVx8TUbN (MHPP, 4.25, Reject — 210-problem human-curated harder benchmark); diXvBHiRyE (3.60, Reject — RACE multi-dimensional code benchmark); KRdiRGSNc9 (4.60, Reject — HumanEval-V multimodal coding).
- Strong band: YrycTjllL0 (BigCodeBench, 9.00, Accept); 6s5uXNWGIh (MLE-Bench, 8.00, Accept); jOmk0uS1hl (8.00, Accept — training on test task); KIgaAqEFHW (8.00, Accept — miniCTX).

Round-1 bracket: **between 4.25 (MHPP) and 6.25 (LiveCodeBench)**.

**Round 2 (narrowing):**
- chfJJYC3iL (LiveCodeBench, 6.25, Accept — already read; directly comparable: AetherCode has stronger test-case methodology but weaker contamination analysis).
- CtM5xjRSfm (7.00, Accept — AlgoPerf; a competition results paper, less topically aligned).
- Qyp3Rni2g1 (5.25, Reject — efficiency benchmark, less topical).
- fjEZ2LPceZ (6.75, Accept — CS-Bench, knowledge-heavy LLM benchmark).
- 7o6SG5gVev (TestGenEval, 6.25, Accept — test-generation benchmark).
- Dn7Ay7rZcH (5.50, Reject — PLUM preference learning, off-topic).
- suz4utPr9Y (ENAMEL, 5.75, Accept — read; expert-curated test cases + expert reference solutions, directly analogous in its rigor claims).
- 0yXqV8VJKi (5.25, Reject — VideoQA, off-topic).

Closest topical anchors: LiveCodeBench (6.25), ENAMEL (5.75), TestGenEval (6.25), MHPP (4.25). AetherCode sits roughly at LiveCodeBench's level on scope and execution, but the in-sample TPR/TNR measurement and absent contamination analysis are real methodological weaknesses that LiveCodeBench's reviewers did not penalize LiveCodeBench for (LiveCodeBench actually delivered contamination analysis). ENAMEL is more focused, with cleaner statistical treatment.

Calling it slightly below LiveCodeBench because the headline methodological claim (100% TPR/TNR) is genuinely weakened by the circular construction, while LiveCodeBench's analogous contamination claim was actually empirically supported. Settling at **5.5** — comparable to ENAMEL's neighborhood, just below LiveCodeBench, decisively above MHPP. This is consistent with a paper that has real contributions and useful infrastructure but whose central methodological framing needs re-grounding.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>