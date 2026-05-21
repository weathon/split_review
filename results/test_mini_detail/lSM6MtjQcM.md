Here is the final consolidated review.

---

## Summary

This paper presents AetherCode, a benchmark for evaluating LLMs on competitive programming problems sourced from premier competitions (IOI and ICPC series). Its main contributions are (1) systematic collection of 456 problems from both OI and ICPC competitions (2024–2025), (2) a hybrid test-case construction pipeline combining an automated Generator-Validator agent with 67 competitive programming experts and an elite review team (≥3 ICPC gold medals), achieving 100% TPR/TNR on a collected solution set of 30,000+ submissions, and (3) an evaluation of 17 models that shows clear differentiation even among top reasoning models (best Pass@1: 35.5%).

## Strengths

1. **Premier-competition sourcing with expert-validated test cases.** AetherCode is the first benchmark to systematically collect problems from *both* OI (IOI, NOI, USACO) and ICPC (regional championships, World Finals) competitions and validate them through a genuine human-in-the-loop pipeline. The use of 67 experts (Codeforces rating >2000, including International Grandmasters) and an elite review team (≥3 ICPC gold medals) to audit and supplement test cases goes well beyond fully automatic pipelines (e.g., EvalPlus mutation). Evidence: Section 2.3.3, Section 2.3.2 (89.9% TNR from automation alone, raised to 100% with expert annotation).

2. **Clear differentiation among top-tier reasoning models.** The benchmark does not suffer from ceiling effects. Table 3 shows o4-mini-high at 35.5% Pass@1, Gemini-2.5-Pro at 32.7%, and a long tail down to GPT-4o at 4.4%. Only three models solve any *Extreme* problems. This demonstrates that AetherCode measures genuine reasoning difficulty that existing benchmarks (where top models exceed 80–90%) do not capture.

3. **Rigorous test-case quality metrics with explicit TPR/TNR framing.** The paper formalizes test suite evaluation as a binary classifier problem (Section 2.3.1, Equations 1–2) rather than relying on vague "number of test cases" proxies. Achieving 100% TPR and 100% TNR on a collected solution set of over 30,000 submissions is a concrete, verifiable standard that is stricter than any prior open-source benchmark.

4. **Fine-grained hierarchical categorization.** Each problem is annotated with 10 major algorithmic categories and 144 sub-categories, enabling targeted analysis (Table 4). This allows the paper to identify specific failure patterns (e.g., all models struggle with Computational Geometry and Tree problems; Claude models tend toward correct but inefficient algorithms).

## Weaknesses

### Fatal

None.

### Major

1. **Undefined and contradictory difficulty rating in Table 1.** The "Difficulty" column uses a star rating (★–★★★★) that is never defined in the paper. Critically, AetherCode receives ★★★ while USACO and CodeContests receive ★★★★. This directly contradicts the paper's stated motivation that AetherCode offers "higher difficulty" than existing benchmarks. The paper provides no explanation of what the stars measure (problem-level difficulty? benchmark-wide difficulty? something else?) or why its own benchmark—sourced from IOI/ICPC—is rated below benchmarks it criticizes. This must be resolved: either define the star system and justify the rating, or remove the column.

2. **Evaluation protocol underspecified in the main text.** The paper states "Each model is evaluated four times in each problem, and the average numbers are reported" (Section 3) and refers to Appendix A for details (which is stripped). Without specifying temperature, sampling strategy, the exact Pass@k estimation formula (unbiased estimator from Codex paper vs. empirical estimate), and whether the same four samples are reused across Pass@1/2/4 calculations, the results are not reproducible from the main text alone. The appendix is a supplement, not a substitute—the core protocol belongs in the main paper.

3. **No direct difficulty comparison with existing benchmarks.** The paper claims AetherCode is more challenging than LiveCodeBench, CodeContests, etc., but never reports the performance of the same model on those benchmarks alongside AetherCode results. A simple controlled experiment (e.g., run GPT-4o on a subset of LiveCodeBench using the same protocol) would provide direct evidence for the difficulty claim. Without this, the difficulty argument rests entirely on the source of the problems (IOI/ICPC) rather than empirical comparison.

### Minor

1. **"First benchmark" claim overstates novelty.** The paper claims in Section 1 that AetherCode is "the first benchmark to systematically collect latest problems from premier programming competitions worldwide." However, the Related Work section itself cites USACO Bench, OJBench, ICPCEval, and LLM-Pros, which all collect problems from premier competitions (USACO, NOI, ICPC). The paper's actual novelty—comprehensively collecting from *both* OI and ICPC series with recent problems and expert validation—is genuinely valuable and does not need this overstated framing. The text should be adjusted.

2. **Solution collection source is not described.** Section 2.1 states that "over 30,000 human-written solutions" were collected but does not say from where (scraped from online judges? contributed by contest organizers?). This is critical for reproducibility and for assessing potential biases in the solution set used for test-case validation.

3. **Decontamination is mentioned but not elaborated.** The paper notes that competition dates are included in metadata "for decontamination purposes" (Section 2.1) but does not describe any actual decontamination procedure—whether problems were checked against model training data, whether any were excluded, or how cutoff dates were handled. This is especially relevant since 400 of 456 problems are from 2024 and some models (e.g., o4-mini, Gemini-2.5-Pro) may have been trained on data that includes these contests.

4. **No statistical significance or variance reporting.** Results are reported as Pass@1 averages over four runs. Given the small number of runs and the likely high variance on hard problems (where a single successful solution can swing Pass@1 by 25%), confidence intervals or standard errors should be reported, or at minimum the limitation should be acknowledged.

### Trivial

- The star rating system in Table 1 should be either defined with a footnote or removed.
- Figure 2 is described in the text but the description appears three times (parser artifact).

## Nice-to-Haves

- A direct empirical comparison (same model, same protocol) between AetherCode and a subset of LiveCodeBench or CodeContests to substantiate the difficulty claim.
- A brief description of output format handling (exact match vs. whitespace-insensitive comparison) for standard problems, beyond the special-judge discussion.
- Reporting the TPR from automatic generation alone (before human verification of the validator) alongside the reported 89.9% TNR, to quantify the contribution of each pipeline stage.
- Error-type distribution broken down by difficulty level (Easy/Medium/Hard/Extreme) to see whether failures shift from implementation errors to algorithmic limitations as difficulty increases.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Test case quality claims are overstated because 100% is relative to collected set."** — The paper *already states* this explicitly: "on our collected solution set" (Section 2.3.1, line 134). This is not buried; it is stated in the same sentence as the claim. Every test-suite benchmark evaluates against a known solution set; this is standard practice.
- **"The paper should also report the distribution of error types across difficulty levels."** — Fair as a nice-to-have suggestion, but the harsh critic raised it as a weakness. Downgraded to Nice-to-Have.
- **"Missing appendix details about evaluation protocol"** — The stripped appendix issue is a parser artifact. However, the *main text* lacking temperature and Pass@k formula is a real issue, so that part is retained under Major.
- **Strength Finder's claim that "AetherCode is the first benchmark to systematically collect latest problems"** — This conflicts with the paper's own Related Work. Moved from a Strength (it would be a strength if true, but it's not entirely accurate) and instead addressed as a Minor weakness above.
- **"Missing related works"** — Removed per rules (cannot verify).
- **Formatting nitpicks** — Removed per rules (parser artifacts).
- **Criticism about lack of code release link** — Removed per rules (cites the benchmark as released; the submission PDF may have a link that was stripped).

## Novel Insights

None beyond the paper's own contributions. The reviews surface no perspective that the paper itself does not already address.

## Suggestions

1. **Define the star rating in Table 1 or remove it.** If it measures average problem difficulty, explain the methodology and reconcile why AetherCode is ★★★. If it measures something else (breadth, recency, etc.), rename the column accordingly. This single fix would remove the most distracting inconsistency in the paper.

2. **Move the core evaluation protocol (temperature, sampling, Pass@k formula) into Section 3** rather than deferring entirely to Appendix A. A few sentences are sufficient.

3. **Replace the "first benchmark" claim** with precise language such as "the first benchmark to comprehensively collect problems from both OI and ICPC series with expert-validated test cases."

4. **Describe the source of the 30,000+ solutions** (which online judges or contest organizers) and note any selection criteria applied.

5. **Add a controlled difficulty comparison:** run one model (e.g., GPT-4o or a mid-tier model) on a representative subset of LiveCodeBench or CodeContests using the same evaluation protocol, and report alongside AetherCode results.

## Score and Decision

**Calibration summary (all anchors retrieved across rounds):**

| Anchor | Avg Human Score | Round | Comparison |
|--------|----------------|-------|------------|
| `/home/wg25r/review_agent/human_reviews/wC6FQOEfG6.md` | 2.50 | 1 | Much weaker (translation of input specs to test case grammars; withdrawn) |
| `/home/wg25r/review_agent/human_reviews/NlY3XppPt3.md` | 2.00 | 1 | Much weaker (novel computational models; withdrawn) |
| `/home/wg25r/review_agent/human_reviews/ly10tMV6cD.md` | 3.25 | 1 | Much weaker (structure-rich text benchmark; rejected) |
| `/home/wg25r/review_agent/human_reviews/S9YfP4rsfX.md` | 2.50 | 1 | Much weaker (graph logical reasoning; withdrawn) |
| `/home/wg25r/review_agent/human_reviews/2umZVWYmVG.md` | 3.75 | 1 | Weaker (code execution simulation benchmark; rejected — methodological concerns) |
| `/home/wg25r/review_agent/human_reviews/chfJJYC3iL.md` | 6.25 | 1,2 | **Comparable** (LiveCodeBench: similar competition-level code benchmark; accepts contaminated-control focus over test-case quality; AetherCode has stronger test-case rigor but less contamination analysis) |
| `/home/wg25r/review_agent/human_reviews/7o6SG5gVev.md` | 6.25 | 1,2 | Comparable (TestGenEval: test generation benchmark; similar score but different focus — real-world testing vs. competitive programming reasoning) |
| `/home/wg25r/review_agent/human_reviews/wpTitXWGNO.md` | 4.75 | 1,2 | Weaker (xCodeEval: large multilingual benchmark but rejected due to quality concerns) |
| `/home/wg25r/review_agent/human_reviews/YrycTjllL0.md` | 9.00 | 1 | Stronger (BigCodeBench: accepted oral; broader scope with diverse function calls and complex instructions) |
| `/home/wg25r/review_agent/human_reviews/KIgaAqEFHW.md` | 8.00 | 1 | Stronger (miniCTX: formal theorem proving; oral-level contribution with novel context-handling benchmark) |
| `/home/wg25r/review_agent/human_reviews/XmProj9cPs.md` | 8.00 | 1 | Stronger (Spider 2.0: enterprise text-to-SQL; oral-level; broader real-world impact) |
| `/home/wg25r/review_agent/human_reviews/syThiTmWWm.md` | 7.75 | 1 | Stronger (benchmark gaming analysis; oral-level; highly novel angle) |
| `/home/wg25r/review_agent/human_reviews/CahIEKCu5Q.md` | 5.50 | 2 | Slightly weaker (CodeMMLU: MCQA code understanding benchmark; accepted poster but had contamination and bias concerns that AetherCode avoids through execution-based evaluation) |
| `/home/wg25r/review_agent/human_reviews/FP77VtEuaT.md` | 5.25 | 2 | Weaker (3-SAT reasoning characterization; rejected; less directly relevant) |
| `/home/wg25r/review_agent/human_reviews/m2NVG4Htxs.md` | 6.75 | 2 | Comparable (contamination analysis; accepted poster but focuses on measurement rather than benchmark construction) |

**Round 1 bracket:** 5–7. AetherCode is clearly above the weak/sub-4 papers and below oral-level papers (7.5+).

**Round 2 narrowing:** The paper is most comparable to LiveCodeBench (6.25) — both are competition-level code benchmarks with broad model evaluations. AetherCode has stronger test-case validation but weaker contamination control, less model breadth (17 vs. 50+), and more presentation issues (star rating inconsistency, missing evaluation details). Compared to CodeMMLU (5.5), AetherCode has stronger methodological foundations (execution-based vs. MCQA). The star rating inconsistency and underspecified evaluation protocol prevent it from reaching LiveCodeBench's score, but the core benchmark contribution (expert-validated test cases from premier competitions) is solid.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>