Now I have enough comparison data. Let me compile the final review.

---

## Calibration Anchors

| Anchor | Avg Score | Decision | Round/Query | Comparison to AetherCode |
|--------|-----------|----------|-------------|-------------------------|
| LiveCodeBench (chfJJYC3iL) | 6.25 | Accept | R1-Topic-Mid | Stronger: has contamination analysis, dynamic updating, comparison to existing benchmarks. AetherCode lacks these. |
| Putnam-AXIOM (WrBqgoseGL) | 5.80 | Reject | R2 | Similar: both are "harder benchmark" papers. Putnam has contamination variations but smaller dataset. AetherCode has larger dataset and better test methodology but weaker contamination analysis. |
| ENAMEL (suz4utPr9Y) | 5.75 | Accept | R2 | Stronger in focused contribution (efficiency metric) but smaller scope (142 problems from HumanEval). AetherCode has broader sourcing but more severe positioning issues. |
| CS-Bench (fjEZ2LPceZ) | 6.75 | Accept | R1-Topic-Mid | Much stronger: 5K samples, comprehensive, better analysis. AetherCode not comparable in depth. |
| MHPP (TVFVx8TUbN) | 4.25 | Reject | R1-Topic-Mid / R2 | Weaker: 210 problems vs 456, less rigorous test methodology. AetherCode has better methodology but similar weaknesses (no human baseline, no comparison). |
| Tests as Instructions (sqciWyTm70) | 4.00 | Reject | R1-Topic-Mid / R2 | Narrower scope (React TDD). AetherCode has broader scope and better methodology. |
| RACE (diXvBHiRyE) | 3.60 | Reject | R1-Topic-Mid / R2 | Weaker: unconvincing metrics, limited data source. AetherCode has clearer methodology. |
| Codev-Bench (c2C2NQKjZw) | 4.25 | Reject | R2 | Similar type of contribution but narrower (code completion). AetherCode broader. |

**Round 1 bracket:** 3.5–6.0 (based on topic-anchored queries and weakness-anchored queries).

**Round 2 narrowing:** Compared against anchors in the 3.0–5.5 range. AetherCode is stronger than MHPP (4.25), RACE (3.60), and TDD (4.00) due to its larger scale, premier-competition sourcing, and expert-validated test-case methodology. But it is weaker than LiveCodeBench (6.25) and ENAMEL (5.75) because it lacks contamination analysis, human baselines, and direct comparisons to existing benchmarks, and because its own Table 1 contradicts its difficulty claims.

**What the low-band anchors (3.0–4.25) failed at:** They either had small datasets, unconvincing evaluation methodology, narrow scope, or unsupported claims. AetherCode shares the "unsupported claims" failure (difficulty claim contradicted by own Table 1, no human baseline for "gap" claim) and partial "missing comparative evaluation" failure (no quantitative comparison to existing benchmarks), but outperforms them on dataset size and methodological rigor of test case construction.

**Final score positioned relative to round-2 anchors:** Between MHPP (4.25) and ENAMEL (5.75) — closer to MHPP due to the severity of the overclaiming issues, but above it due to better methodology. Score: 5.0.

---

## Final Review

### Summary

AetherCode is a benchmark of 456 competitive programming problems sourced from premier competitions (IOI, ICPC, national OIs) spanning 2024–2025. Its primary methodological contribution is a hybrid test-case construction pipeline combining automated generation (G-V Agent) with expert annotation by 67 competitive programmers, achieving 100% TPR and 100% TNR on a collected corpus of 30,000+ human-written solutions. The paper evaluates 17 LLMs (11 reasoning, 6 non-reasoning), reporting that the best model (o4-mini-high) achieves 35.5% Pass@1, and identifies failure modes across models.

### Strengths

1. **Premier-competition sourcing with expert-validated test cases.** The benchmark draws from IOI, ICPC World Finals, NOI, USACO, and regional ICPC contests — genuinely more prestigious sources than the LeetCode/AtCoder/CodeForces problems used by most prior benchmarks (Table 1, Section 2.1). The test-case pipeline involves 67 experts (most Codeforces rating >2000) and an elite audit team of ICPC gold medalists, substantially more rigorous than the automatic mutation or handcrafted approaches in HumanEval, CodeContests, and LiveCodeBench (Section 2.3).

2. **Quantified test-case discrimination via TPR/TNR.** Instead of using test-case count as a quality proxy, the paper directly measures test-suite quality with True Positive Rate and True Negative Rate, achieving 100% on both metrics on the collected solution set (Section 2.3.1). This provides a concrete, measurable standard that prior benchmarks lack.

3. **Difficulty segmentation grounded in human contest performance.** Problems are classified as Easy/Medium/Hard/Extreme using official contest solve data and expert judgment, with Extreme defined as problems no human solved (Section 2.2). This human-centric categorization enables studying divergence between human and LLM difficulty, a feature absent in most prior benchmarks.

4. **Comprehensive stratified evaluation across 17 models.** Table 3 reports Pass@1/Pass@2/Pass@4 across four difficulty levels and two years for 11 reasoning and 6 non-reasoning models, revealing clear discrimination between model tiers. The wide performance range (4.4%–35.5% Pass@1) confirms the benchmark has headroom and is not saturated.

5. **Failure-mode diagnosis beyond aggregate scores.** Section 3.3 categorizes errors into Wrong Answer, TLE, Runtime Error, and Compile Error, with qualitative analysis of specific model weaknesses (e.g., GLM-4.5's language-instruction confusion, Claude's correct-but-inefficient algorithms).

### Weaknesses

#### Fatal
None.

#### Major

1. **Self-contradictory difficulty claims undermine the paper's central motivation.** The abstract and introduction argue that existing benchmarks suffer from "insufficient difficulty and scope" and that AetherCode offers "higher difficulty." Yet Table 1 rates AetherCode at ★★★ difficulty — the same as LiveCodeBench (which the paper criticizes) and lower than CodeELO and LiveCodeBench Pro (★★★★). Either the ★★★ rating is wrong (and AetherCode is harder than it claims), or the paper's positioning as addressing "insufficient difficulty" is contradicted by its own characterization. This internal inconsistency weakens the paper's framing.

2. **No human baseline for the "significant gap" claim.** The conclusion states "there remains a significant gap compared to top human experts," and the Extreme category is defined by "no human solved." However, actual human solve rates for the 436 non-Extreme problems are never reported, despite the paper having collected "human contestant performance data" (Section 2.1). Without knowing what fraction of Easy/Medium/Hard problems top humans solve during competition, the "gap" claim is unquantified and unsupported. The title ("Evaluating LLMs' Ability to Win") further implies a comparison to human performance that is never operationalized.

3. **No quantitative comparison to existing hard benchmarks.** The paper criticizes LiveCodeBench, CodeContests, and CodeELO for insufficient difficulty but never evaluates the same models on those benchmarks to demonstrate that AetherCode yields lower scores. Table 1 provides a qualitative comparison, not empirical evidence. Without this anchoring, "insufficient difficulty" is asserted rather than demonstrated.

4. **Missing contamination analysis despite collecting the necessary data.** The paper states it collects "the date of the competition (for decontamination purposes)" (Section 2.1) and annotates problems with temporal metadata (Section 2.2), but the evaluation (Section 3) never uses this data. No model training cutoff dates are reported, no time-segmented analysis is provided, and no problems are filtered based on likely contamination. Given that 400 of 456 problems are from 2024 (Table 2), many models' training data likely includes these problems. This is a standard expectation for code benchmarks (cf. LiveCodeBench's time-segmented analysis).

#### Minor

5. **100% TPR/TNR is reported only on the construction set.** The test cases are iteratively improved until they pass all collected correct solutions and fail all collected incorrect solutions. While the expert audit (elite team adding more incorrect solutions) partially mitigates overfitting, the 100% figure would be far more convincing if validated on a held-out set of solutions from different sources. The paper does not discuss this overfitting risk.

6. **Pass@k estimation method is not specified.** The paper states "Each model is evaluated four times in each problem, and the average numbers are reported" and presents Pass@1, Pass@2, Pass@4 columns. It does not specify whether the standard unbiased estimator (Chen et al., 2021) or a simple proportion is used, making the results not precisely reproducible.

7. **Three models showing exactly 7.3% on Tree problems is suspicious.** In Table 4, o4-mini-high, Gemini-2.5-Pro, and DeepSeek-R1-0528 all show exactly 7.3% Pass@1 on Tree (24 problems). Given that these are different models with different capabilities, identical performance to one decimal suggests a data artifact or rounding issue that should be explained.

#### Trivial

8. **Table formatting errors.** "Ssed-1.6-Thinking-0715" (Table 3) should be "Seed-1.6-Thinking-0715"; "Claude-4-Sonnet-nothingking" (Table 3) is garbled; "DeepSeek-V3-Q324" (Table 4) should be "DeepSeek-V3-0324." These typos in model names, while minor, reduce confidence in data handling.

### Nice-to-Haves

- **Report human solve rates** for Easy/Medium/Hard problems using the collected contest data and directly compare to LLM Pass@1. This single addition would address the most consequential weakness.
- **Evaluate a subset of models on LiveCodeBench or CodeContests** to provide an apples-to-apples difficulty comparison.
- **Add time-segmented analysis** showing how model performance varies with problem recency relative to training cutoff dates.
- **Include confidence intervals** on Pass@k estimates, especially for small categories (Extreme: 20 problems, Tree: 24 problems).

### Removed Points

*These points were raised by reviewers but are excluded from the main weakness list for the reasons stated:*

- "The paper does not justify why its collection is more comprehensive than existing benchmarks" — The paper explicitly states that prior work (USACO Bench, LLM-Pros, ICPCEval, OJBench) is "limited to a few specific contests" or "relying on outdated data" and provides contest counts for each (Section 4.2). This justification is present.
- "DeepSeek-V3-0324 shows an increase from 2024 to 2025" — The data in Table 3 shows 8.9% (2024) → 5.4% (2025), which is a decrease. The critic corrected themselves mid-paragraph; the final claim is not a weakness.
- "The 100% TPR/TNR claim is fundamentally invalid" — The paper accurately describes this as measured on the collected solution set and describes the expert audit process. The limitation (no held-out validation) is acknowledged in Minor weakness #5; the claim itself is not invalid.
- "The 'nothinking' naming suggests hasty data entry" — These are likely internal model configuration tags (thinking vs. no-thinking inference mode), not placeholder names.
- "The comparison between reasoning Pass@1 and non-reasoning Pass@4 is unfair" — The paper's actual comparison is non-reasoning Pass@4 (15.3) vs. reasoning Pass@4 (46.6), which is fair. The sentence is ambiguous but the data supports the conclusion.

### Novel Insights

The reviews reveal a productive tension in this paper: it introduces a genuinely rigorous test-case construction methodology (67 experts, ICPC gold medalist audits, 30K+ solutions) that sets a new quality bar for code benchmarks, yet simultaneously overclaims on difficulty in ways its own Table 1 contradicts. This suggests the field may benefit from decoupling the *source prestige* dimension (premier competitions vs. online judges) from the *difficulty* dimension — a benchmark can be prestigious in sourcing without being uniformly harder than alternatives. The observation that human-based difficulty categorization (contest solve rates) can diverge from LLM difficulty is valuable but underexplored here; formalizing this divergence as a diagnostic tool could be a promising future direction.

### Suggestions

1. **Resolve the difficulty claim contradiction.** Either recalibrate the ★★★ rating upward (if AetherCode problems are genuinely harder) or adjust the paper's rhetoric to emphasize *source prestige and test-case quality* as the primary contributions, rather than difficulty.

2. **Report human solve rates** from the collected contest data for Easy/Medium/Hard categories and directly compare to the best LLM Pass@1. This single addition would substantially strengthen the paper.

3. **Run one comparison experiment** — evaluate the best 2–3 models on a subset of LiveCodeBench (or CodeContests) using the same procedure to demonstrate the difficulty differential quantitatively.

4. **Add a contamination analysis table** showing Pass@1 on problems before vs. after each model's training cutoff (using known cutoff dates). This could be a simple supplementary table but would significantly improve confidence.

5. **Clarify the Pass@k estimator** in the main text and add bootstrap confidence intervals for the main results.

### Score and Decision

The paper has genuine substance: the premier-competition sourcing is novel, the test-case methodology is the most rigorous I have seen in a code benchmark, and the evaluation provides useful insights. However, the paper's positioning is undermined by an internal contradiction (★★★ difficulty vs. "higher difficulty" claims), and key claims (the "gap" to humans, "insufficient difficulty" of existing benchmarks) are left unsupported by missing analyses (human baseline, comparison to existing benchmarks, contamination control). The paper needs major revisions to bring its claims in line with its evidence. I cannot recommend acceptance in its current form.

**Score: 5.0**  
**Decision: Reject**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>