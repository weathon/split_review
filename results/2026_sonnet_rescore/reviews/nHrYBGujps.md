## Summary

BIRD-INTERACT is a benchmark for evaluating LLMs in dynamic, multi-turn text-to-SQL settings. It extends LIVESQLBENCH with ambiguity injection, follow-up sub-tasks, and a function-driven two-stage user simulator that constrains simulator actions (AMB/LOC/UNA) before generating responses, preventing ground-truth leakage. The benchmark spans full CRUD operations and two evaluation modes—structured conversational (*c*-Interact) and open-ended agentic (*a*-Interact)—revealing that even the strongest models (GPT-5: 8.67% SR in *c*-Interact, 17.00% in *a*-Interact) fall far short on realistic interactive tasks.

---

## Strengths

- **Principled two-stage simulator that dramatically reduces ground-truth leakage.** Figure 6 demonstrates that the function-driven approach reduces failure rates on unanswerable (UNA) queries from up to 67.4% (baseline) to as low as 2.7%, a concrete and directly measurable improvement over the LLM-only baseline.

- **Dual evaluation settings revealing complementary capability gaps.** Table 2 shows that GPT-5 ranks worst in *c*-Interact (14.50% priority SR) and best in *a*-Interact (29.17%), a significant cross-mode rank reversal that demonstrates the benchmark captures qualitatively distinct interaction skills not visible from single-turn scores.

- **CRUD-complete task design with executable test cases.** The benchmark covers INSERT/UPDATE/DELETE/DDL in addition to SELECT (Table 1: 190 DM tasks), with correctness verified via executable test cases (Section 2) rather than surface-level SQL string matching. This moves beyond the SELECT-only scope of prior benchmarks.

- **Comprehensive ambiguity taxonomy and quantifiable task complexity.** The three-category ambiguity injection framework (superficial, knowledge-chain breaking, environmental) is well-motivated, and Table 1 documents that the LITE set averages 5.16 ambiguities/task with 13.04 dynamic interactions/task, demonstrating measurable complexity well beyond static multi-turn datasets.

- **Action-distribution diagnostic exposing trial-and-error bias.** Section 5.2 quantifies that *submit* and *ask* together comprise 60.87% of all actions in *a*-Interact, while knowledge and schema retrieval are systematically under-used. This is a specific, actionable finding for future systems work.

- **LITE and FULL variants enabling both analysis and rapid development.** The split design (300 LITE with cleaner DBs, 600 FULL for comprehensive evaluation) allows detailed behavioral analysis on LITE (e.g., ITS curves in Figure 4) while the FULL set provides robust aggregate benchmarking, which is a practically sensible design.

---

## Weaknesses

### Fatal
None.

### Major

- **No human performance baseline, leaving benchmark difficulty uncalibrated.** The paper's central framing is that BIRD-INTERACT "restores missing realism" and reflects production-grade difficulty, yet no human SR is reported on the actual benchmark tasks. Human experts appear in the alignment study (Section 6: "human experts interact with 7 system models on 100 randomly sampled tasks"), but their per-task success rates are used only for correlation computation and are never reported as a standalone reference point. Without knowing whether a skilled human practitioner achieves, say, 50% or 90% SR within the same budget, the reader cannot determine whether the ~17% ceiling reflects a meaningfully challenging benchmark or an over-constrained one. Given that *c*-Interact budget is set to τ_clar = m_amb + λ_pat (Section 4.1) with no stated rationale for these constants, calibration against human performance is the only external validation available and is currently absent. This is the paper's most significant evidential gap.

- **Alignment study is underpowered at n=7.** Table 3 reports Pearson r=0.84 (p=0.02) for the function-driven simulator versus r=0.61 (p=0.14) for the baseline—both computed over 7 system models as data points. At n=7, the 95% confidence interval around r=0.84 spans roughly [0.18, 0.98], meaning the true correlation is only weakly constrained. More critically, the difference between 0.84 and 0.61 is not statistically distinguishable from zero at this sample size. The paper uses "significantly stronger alignment" in Section 6, which the data does not support. This matters because the alignment study is the primary evidence that the simulator faithfully reflects human behavior—the central design claim of Section 3.3. The USERSIM-GUARD results (Figure 6) are far more convincing and speak to a key property (rejecting UNA queries), but they do not test the *full* alignment claim. Note that adding the Gemini row only adds two more (n=7) experiments with the same data, not independent replications.

### Minor

- **The ITS "Law" framing is premature.** Section 5.2 defines an "Interaction Test-Time Scaling Law" but Figure 4's caption explicitly states that in *a*-Interact mode performance "remains relatively flat or slightly decreases" with patience. The main text then narrows the observed scaling to one model: "Claude-3.7-Sonnet exhibits clear scaling behavior." Calling a monotonic scaling property observed in a single model under a single mode a "Law" is an overclaim; the paper should describe it as an observation or hypothesis.

- **AMB/LOC misclassification effects on model rankings not analyzed.** Figure 6 shows ~90% accuracy for AMB and LOC categories across all simulator variants. The remaining ~10% represents legitimate clarification requests incorrectly routed to UNA() and rejected, potentially penalizing models that use novel but valid disambiguation strategies. Since this misclassification rate applies uniformly, it may not alter relative rankings, but the paper provides no analysis or estimate of the downstream effect. An approximate quantification would strengthen confidence in the benchmark scores.

- **Memory grafting conclusion slightly overclaims the effect size.** Figure 5 shows GPT-5 rising from 13.8% to 20.5% SR (O3-Mini history) or 18.8% (Qwen-3-Coder history) on the LITE set. O3-Mini's unassisted rate is 18.5%. The improvement is real and directionally supports the "communication deficit" hypothesis, but the absolute gain (5–7 percentage points) and the modest ceiling barely exceeding the source model's score are worth noting when framing the claim that "a more effective communication schema is required."

### Trivial

- The a-Interact base budget B_base = 6 and the 2× cost multiplier for user questions (Figure 3) are stated in Section 4.2 without motivation; the justification is deferred entirely to the appendix. For design choices that directly determine benchmark difficulty, a one-sentence rationale in the main text would help readers assess whether the budget regime is reasonable.

---

## Nice-to-Haves

- A brief characterization of domain distribution and schema complexity of the underlying LIVESQLBENCH databases (inherited by BIRD-INTERACT) would help readers assess generalizability. If the 600 tasks skew toward particular domains, this affects the scope of conclusions.
- A trajectory-level analysis—comparing ordered action sequences of successful vs. failed episodes—would be more informative than the aggregate action-frequency analysis in Section 5.2 and would substantiate claims about strategic interaction being the decisive skill.
- Reporting the human SR on the 100-task subset (already collected for the alignment study) as a calibration reference would be a low-cost addition that directly addresses the most significant evidential gap.
- The DM sub-set is notably smaller (190 tasks in FULL vs. 410 BI). A brief discussion of whether test case coverage adequately exercises the range of correct SQL equivalents for UPDATE/DELETE/DDL operations would strengthen claims about "full CRUD coverage."

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "13+ average injected ambiguities per task translate to reliably solvable puzzles."** The critic conflates the LITE (5.16 amb/task) and FULL (3.89 amb/task) statistics with "13+ interactions/task," which refers to the number of dynamic interactions, not ambiguities. This is a misreading—Table 1 clearly distinguishes the two statistics. Removed as factually incorrect.

- **Harsh Critic: "Whether ambiguous queries are solvable is only supported by 93.33% inter-annotator agreement."** The paper also points to the dotted idealized-performance line in Figure 4 showing that unambiguous single-turn performance sits well above interactive curves, which provides supporting indirect evidence. The critic acknowledges this but dismisses it "in passing"—the figure caption explicitly compares interactive SR against the ambiguity-free baseline. This weakens the criticism to below minor threshold.

- **Harsh Critic: LIVESQLBENCH domain bias.** While valid as a nice-to-have, this is an out-of-scope critique because BIRD-INTERACT's database coverage is explicitly inherited from LIVESQLBENCH, which is cited and treated as an existing artifact. Criticizing the base dataset is scope creep for a benchmark extension paper.

- **Strength Finder: "Human-simulator alignment validates automatic evaluation" (as a standalone strength).** This repeats the content of Strength 2 (function-driven simulator) and is weakened by the Major weakness on statistical power. Merged into Strength 2 and the UNA robustness point; not listed separately.

---

## Novel Insights

The most genuinely novel observation in the reviews—confirmed by the paper—is that the rank ordering of LLMs *reverses* between c-Interact and a-Interact modes, with GPT-5 being the weakest in the structured conversational mode yet the strongest in the agentic mode. The memory-grafting experiment provides a mechanistic decomposition supporting the idea that interaction strategy and SQL generation capability are partially orthogonal skills. The function-driven two-stage simulator architecture (semantic parsing → constrained symbolic action → response generation) is an architecturally novel approach to the user simulation problem for benchmarks, with the key insight that symbolic action constraints, rather than prompt engineering alone, are needed to prevent ground-truth leakage and UNA failures. The action-distribution finding—that LLMs spend >60% of their agentic budget on direct submission and user questions rather than systematic exploration—is a concrete, quantified diagnosis of a pre-training bias with clear implications for future training regimes.

---

## Suggestions

1. **Report human SR** from the 100-task expert study (already collected) as an explicit calibration reference in the main paper, alongside per-domain breakdown.
2. **Expand the alignment study** to at least 12–15 system models—even including smaller or older models—to bring the Pearson r confidence intervals to a width that supports the comparative claim.
3. **Soften "ITS Law"** to "ITS observation" or explicitly define it as a property a model can satisfy (as opposed to a universally observed phenomenon), and note that only Claude-3.7-Sonnet clearly satisfies it in the current evaluation.
4. **Add an AMB/LOC misclassification impact analysis:** estimate whether the ~10% misclassification rate materially changes any model's rank in Table 2, for example by simulating a re-run with corrected labels on a subset.
5. **Briefly justify B_base = 6** and the 2× action-cost multiplier for user questions in the main text (one or two sentences suffice).

---

## Evaluation Summary

- **Originality:** High. The function-driven simulator design is novel, and CRUD-complete dynamic benchmarking fills a genuine gap; the methodology is thoughtful rather than incremental.
- **Importance:** High. Static single-turn benchmarks are near-saturated; a benchmark that exposes interaction skill gaps at all current frontier models is timely and needed.
- **Claims supported:** Mostly. Core claims (models struggle, dual modes reveal different capabilities, simulator reduces leakage) are well supported. The "significantly stronger alignment" and "ITS Law" claims are mildly overstated.
- **Soundness:** Good overall, with bounded gaps: human baseline absent, alignment study underpowered.
- **Clarity:** Good. The two-stage simulator design and evaluation settings are clearly explained; key design constants are deferred to appendices.
- **Community value:** High. A freely usable, CRUD-complete interactive benchmark with a validated automated evaluator is a resource the community currently lacks.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>