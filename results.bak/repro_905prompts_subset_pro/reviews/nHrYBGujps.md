Now I have all the calibration data I need. Let me synthesize the final review.

**Round 1 Bracket:** Between 5.5 and 7.5 (above DialSim at 5.00, below Spider 2.0 at 8.00).

**Round 2 Narrowing:** MINT (6.75) is the closest comparator — a multi-turn interaction benchmark with an LLM user simulator. BIRD-INTERACT has a more rigorous simulator (function-driven with USERSIM-GUARD validation and human correlation), dual evaluation modes, and domain-specific depth, but narrower task scope. Spider 2.0 (8.00) is a stronger benchmark overall due to real enterprise data and broader impact. BIRD-INTERACT lands between them, closer to the upper end.

**Final Score:** 7.0

---

## Summary

BIRD-INTERACT introduces a benchmark for evaluating LLMs on interactive text-to-SQL through dynamic, multi-turn interactions. The benchmark features 900 tasks (600 FULL + 300 LITE) built by injecting ambiguities into single-turn queries from LIVESQLBENCH and adding state-dependent follow-up sub-tasks. Its key innovation is a **function-driven user simulator** that maps system clarification requests to constrained symbolic actions (AMB, LOC, UNA) before generating responses, substantially reducing ground-truth leakage compared to conventional LLM-based simulators. Two evaluation settings are provided — *c*-Interact (protocol-guided dialogue) and *a*-Interact (autonomous agent) — and experiments on 7 frontier LLMs show that even GPT-5 solves only 8.67% of tasks end-to-end in *c*-Interact and 17.00% in *a*-Interact.

## Strengths

- **Function-driven user simulator is well-validated and genuinely innovative.** The two-stage design (semantic parsing into symbolic actions → controlled response generation) reduces failure rates on unanswerable questions from 67.4% (baseline) to 2.7% on the USERSIM-GUARD dataset (Figure 6). It achieves Pearson r=0.84 with human performance (p=0.02), substantially outperforming the baseline simulator's r=0.61 (Table 3). This addresses a real methodological gap in interactive evaluation.

- **Dual evaluation settings reveal complementary model capabilities.** The *c*-Interact and *a*-Interact modes produce meaningfully different model rankings. GPT-5 ranks worst on *c*-Interact priority sub-tasks (14.50%) but best on *a*-Interact (29.17%), demonstrating that the benchmark captures distinct interaction strategies rather than a single performance axis (Table 2, Section 5.1).

- **Comprehensive and challenging task design with executable validation.** The benchmark covers full CRUD operations across both BI and DM domains, with systematic ambiguity injection (superficial, knowledge-chain-breaking, environmental) and state-dependent follow-up sub-tasks guarded by executable test cases. The 3.89–5.16 ambiguities per task (Table 1) and overall low model success rates confirm the benchmark is genuinely difficult.

- **Memory grafting experiment provides insight into communication vs. generation capabilities.** Providing GPT-5 with clarification histories from stronger models (Qwen-3-Coder, O3-mini) before SQL generation improves its success rate (Figure 5), demonstrating that the benchmark can isolate interactive communication quality from core SQL competence — a useful analytical tool.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Memory grafting conclusion is slightly overclaimed.** The grafted history provides GPT-5 not just with *how* to communicate but with the *result* of effective communication (i.e., resolved ambiguities). The experiment therefore demonstrates that GPT-5 can solve tasks when ambiguities are resolved by other means, but it does not cleanly isolate communication strategy from information content. The claim that this shows GPT-5's weakness is specifically in "communication" rather than reasoning should be tempered (Section 5.2, Figure 5).

- **ITS "Law" framing is definitional, not empirical.** The paper defines "ITS Law" as a criterion ("A model satisfies this law if, given enough interactive turns, its performance can match or even surpass that of the idealized single-turn task") but shows only that some models scale *toward* the idealized line, not that any model *satisfies* the law (Figure 4, Section 5.2). The framing is aspirational rather than misleading, but it would be stronger as a hypothesis or target rather than a named "law."

- **User simulator backbone undisclosed for main experiments.** Table 2 reports an average simulator cost of $0.03/task but does not specify which LLM powers the simulator. Section 6 evaluates GPT-4o and Gemini-2.0-Flash for the alignment study, but whether the same model serves in the main runs is unstated. Given the function-driven design constrains the simulator's output space, this is unlikely to affect rankings substantially, but disclosure would strengthen reproducibility.

### Trivial

- The factor of 2 in the *a*-Interact budget formula ($B = B_{\text{base}} + 2m_{\text{amb}} + 2\lambda_{\text{pat}}$) versus the *c*-Interact formula ($\tau_{\text{clar}} = m_{\text{amb}} + \lambda_{\text{pat}}$) is stated to "maintain consistency" but the rationale is unclear (Section 4.2).
- Single-run evaluation without variance estimates (Table 2) — standard for this scale of LLM benchmarking due to cost, but noted.
- The "Overall" column under Follow Ups in Table 2 could benefit from an explicit definition in the caption as "end-to-end success (both sub-tasks correct)."

## Nice-to-Haves

- A **human performance study** on a subset of tasks (e.g., 100 tasks) would calibrate the benchmark's difficulty scale and show how far current models are from human-level interactive SQL competence. This is not a standard requirement for benchmarks, but would strengthen the interpretability of the low model scores.
- A **sensitivity analysis** varying the user simulator backbone (GPT-4o vs. Gemini-2.0-Flash) on a subset of tasks, to confirm that model rankings are robust to simulator implementation.
- A **limitations section** explicitly acknowledging the artificial nature of some injected ambiguities and the trade-off between controllability and ecological realism. Currently only "Future Work" is presented (Section 8).

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Missing human baseline makes the benchmark uncalibrated" (Harsh Critic, claimed as structural/fatal):** The paper does include a human study in Section 6 with human experts interacting across 100 tasks, used for simulator correlation analysis. A human performance ceiling on the benchmark tasks themselves is desirable but is not standard for text-to-SQL benchmarks (Spider, BIRD, Spider 2.0 did not include them). Demoted from "fatal" to Nice-to-Have.

- **"Ecological validity of injected ambiguities is only partially discussed" (Harsh Critic):** The paper explicitly describes its controlled ambiguity injection methodology as a design choice enabling reproducible evaluation. Demanding external validation against field logs goes beyond what is standard for benchmark construction. The paper's claim of "better reflecting real-world usage scenarios" is comparative to existing static benchmarks, not absolute. Moved to Nice-to-Have as a limitations acknowledgment.

- **"The ITS Law formulation is unsupported / misleading" (Harsh Critic):** The paper defines the ITS Law as a criterion, shows scaling behavior toward it, but does not claim any model satisfies it. The framing could be more precise, but is not misleading. Kept as Minor with softened language.

- **"Abstract and introduction overstate the gap" (Harsh Critic):** The paper clearly distinguishes its contributions from existing multi-turn benchmarks (static transcripts vs. dynamic interaction) in Section 1 and Section 7. The differentiation is accurate. Removed.

- **"Verification that ambiguous tasks are unsolvable before clarification is missing" (Harsh Critic):** The paper states "Quality control ensures that ambiguous queries are unsolvable without clarification yet fully reconstructable once clarifications are provided" (Section 3.2) and refers to Appendix H for details. The appendix is stripped by the parser; this detail exists in the original. Removed.

- **Strength about "problem importance" or generic framing:** The Strength Finder's claim about the problem being important is generic. Removed as a standalone strength (the importance is implicit in the benchmark contribution itself).

## Novel Insights

The benchmark's design reveals a genuine tension between two interaction paradigms that has implications beyond text-to-SQL: *c*-Interact evaluates whether models can follow a structured conversational protocol (akin to a guided customer-support dialogue), while *a*-Interact evaluates autonomous planning under resource constraints. The divergent rankings — GPT-5 performs worst in *c*-Interact but best in *a*-Interact — suggest that training for open-ended agentic behavior may come at the cost of disciplined conversation-following, and vice versa. This trade-off, systematically captured in a single benchmark, is a useful lens for evaluating interactive AI systems beyond the SQL domain.

## Suggestions

- Temper the memory grafting conclusion: explicitly acknowledge that the grafted history transfers both communication strategy and resolved ambiguity content, and reframe the finding as "GPT-5 benefits from prior ambiguity resolution regardless of source" rather than attributing the gap solely to communication skill.
- Rename "ITS Law" to "ITS Hypothesis" or simply describe the scaling pattern without naming it as a law, unless models are shown to satisfy it.
- Disclose the simulator backbone used in Table 2 experiments in the main text.
- Add a brief limitations paragraph distinguishing what the benchmark does and does not capture (e.g., artificial ambiguity injection vs. naturally occurring under-specification).

## Score and Decision

**Anchor comparison summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| DialSim (W1x77vRucB) | 5.00 | 1 | BIRD-INTERACT is clearly stronger — more rigorous simulator validation, dual evaluation modes, domain-specific depth |
| CHASE-SQL (CvGqMD5OtX) | 6.25 | 2 | Method paper, not benchmark; limited comparability |
| MINT (jp3gWrMuIZ) | 6.75 | 2 | Closest comparator — multi-turn interaction benchmark with LLM simulator. BIRD-INTERACT has stronger simulator validation, dual modes, and domain depth |
| WildBench (MKEHCx25xp) | 7.33 | 2 | Different domain (general LLM eval); BIRD-INTERACT is more narrowly scoped but deeper in its domain |
| Spider 2.0 (XmProj9cPs) | 8.00 | 1 | BIRD-INTERACT is below Spider 2.0 — the latter uses real enterprise data, larger scale, broader impact |

BIRD-INTERACT is clearly above MINT (6.75) due to its more rigorous simulator design and validation, and clearly below Spider 2.0 (8.00) due to its synthesized (rather than real-enterprise) tasks and narrower scope. It sits around 7.0.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>