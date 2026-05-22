Now I have all the information I need. Let me synthesize the final review.

**Round 1 bracket:** Between 5.0 and 7.0 — clearly above EHR-ChatQA (4.00) and BIRD-Ent (3.60), below the 8.00 Oral papers (Gaia2, LLMs Get Lost).

**Round 2 narrowing:** The paper is stronger than DAComp (5.33) which had weaker validation and less novel analysis, and sits comparably to DeepResearch Bench (6.50). It doesn't rise to the level of MCPMark (7.33) which had extraordinarily positive reviews.

**Final score: 6.5**

Now let me write the consolidated review.

---

Let me double-check the removed points:

1. **Harsh Critic's point about vague second-stage description**: The paper says "Detailed prompts are provided in Appendix R." → REMOVE per rule about missing appendix content.

2. **Harsh Critic's point about annotation training details**: The paper says "detailed in Appendix C" → REMOVE per rule.

3. **Harsh Critic's "Missing Parts" #3 (comparison table in main text)**: This is a nice-to-have, not a weakness.

4. **Harsh Critic's "Missing Parts" #5 (annotation details)**: Appendix content → REMOVE.

For the Strength Finder, let me check if any claims are invalid:

1. "Function-driven user simulator with two-stage action control" - backed by Section 3.3, Figure 3(c), and Figure 6. ✓
2. "Dual evaluation settings that reveal model-specific interaction competencies" - backed by Table 2, Section 4. ✓
3. "Challenging task suite with systematic ambiguity injection and CRUD coverage" - backed by Section 3.2, Table 1. ✓
4. "Interaction Test-Time Scaling and memory grafting experiments" - backed by Section 5.2, Figures 4 and 5. ✓
5. "Budget-constrained awareness mechanism" - backed by Section 4. ✓
6. "Validation of user simulator alignment with human behavior" - backed by Section 6, Table 3. ✓

All strengths are verified and specific. Good.

Now let me finalize the review.## Calibration Summary

**Round 1 — Bracketing:**
| Anchor ID | Avg Score | Domain Notes | Comparison |
|-----------|-----------|-------------|-----------|
| BdlIQGetYv | 2.50 | Octopus (T2S benchmark) | Much weaker — auto-generated, no interactive component |
| jOxfpsnDFo | 2.50 | ConDABench (interactive data analysis) | Much weaker — withdrawn, limited validation |
| hLweUPBz7k | 4.00 | EHR-ChatQA (interactive DB benchmark) | Weaker — only 64 AdaptQA tasks, weaker simulator validation |
| NYLSNHuFzm | 4.67 | MTIR-SQL (multi-turn T2S) | Weaker — method paper, rejected |
| gXkIkSN2Ha | 3.60 | BIRD-Ent (enterprise T2S) | Weaker — synthetic data quality concerns, withdrawn |
| VKGTGGcwl6 | 8.00 | LLMs Get Lost in Multi-Turn (Oral) | Stronger — cleaner experimental design, broader scope |
| 9gw03JpKK4 | 8.00 | Gaia2 (dynamic agent benchmark, Oral) | Stronger — broader agentic evaluation, platform contribution |

**Round 1 bracket: 5.0–7.0**

**Round 2 — Narrowing:**
| Anchor ID | Avg Score | Domain Notes | Comparison |
|-----------|-----------|-------------|-----------|
| NYLSNHuFzm | 4.67 | MTIR-SQL | Weaker — method paper |
| EtzJy9yI5J | 5.33 | DAComp (data agent benchmark, Poster) | Slightly weaker — less validation rigor, mixed reviews |
| 8KE9qvKhM4 | 5.00 | SPARTA (multi-hop QA) | Different domain, comparable tier |
| 8Fm6OKFuRv | 5.00 | Beyond Text-to-SQL (debugging benchmark) | Weaker — rejected |
| hQ0K2Hhq7H | 6.50 | DeepResearch Bench (Poster) | Comparable — similar validation quality, different domain |
| uobROwBsJm | 7.33 | MCPMark (Poster) | Slightly stronger — extremely positive reviews, different domain |
| 3x4SDbXbgl | 6.50 | Computer Agent Arena (Poster) | Different domain |
| ZAx4c4ZH5Y | 6.50 | AnthroBench multi-turn eval (Poster) | Different domain |

**Final calibration:** The paper sits near the 6.5 anchor (DeepResearch Bench) — comparable validation rigor and stronger task scale. It does not reach the 7.33 level of MCPMark. **Score: 6.5**

---

## Summary

This paper introduces BIRD-INTERACT, a benchmark for evaluating interactive text-to-SQL systems through dynamic, multi-turn interactions rather than static conversation transcripts. It builds on LIVESQLBENCH by (1) injecting controlled ambiguities into tasks so that clarification-seeking is required, (2) providing a function-driven user simulator that maps system questions to constrained actions (AMB/LOC/UNA) to prevent ground-truth leakage, (3) defining two evaluation settings (c-Interact for protocol-guided conversation and a-Interact for agentic exploration with budget constraints), and (4) covering the full CRUD spectrum across 600 tasks (with a 300-task lite set). Evaluation of 7 frontier LLMs shows very low absolute performance (best model achieves 17% end-to-end in a-Interact), and analysis via memory grafting and Interaction Test-time Scaling reveals that communication strategy — not SQL ability alone — is the primary bottleneck.

## Strengths

- **Function-driven user simulator with rigorous validation.** The two-stage design (semantic parser → symbolic action → response) effectively blocks the ground-truth leakage and inconsistency problems that plague LLM-as-simulator baselines. The USERSIM-GUARD evaluation (2,100 labeled questions) shows failure rates on unanswerable questions drop from up to 67.4% (baselines) to 2.7% (ours). A human-alignment study (100 tasks, 7 models) finds Pearson correlation of 0.84 (p=0.02) between simulator and human expert success rates — strong evidence of behavioral realism (Section 6, Figure 6, Table 3).

- **Dual evaluation settings expose model-specific interaction competencies.** The c-Interact and a-Interact settings reveal that models have different relative strengths depending on the interaction paradigm. GPT-5 scores worst in c-Interact (14.50%) but best in a-Interact (29.17%), while Qwen-3-Coder does better in c-Interact (22.00%) than a-Interact (13.33%). This demonstrates that the benchmark isolates interaction-mode-specific capabilities that a single setting would miss (Table 2).

- **Memory grafting and ITS experiments cleanly isolate the communication bottleneck.** By providing GPT-5 with ambiguity-resolution histories from better-interacting models (Qwen-3-Coder, O3-mini), its c-Interact success rate rises from 13.8% to 20.5% — proving that the benchmark specifically measures interaction strategy, not just SQL generation ability (Figure 5). The ITS experiment shows that some models (e.g., Claude-3.7-Sonnet) improve monotonically with more interaction turns, while others plateau (Figure 4).

- **Challenging, well-annotated task suite with strong quality control.** 600 tasks with up to 5.16 ambiguities per task, full CRUD coverage (BI + DM), inter-annotator agreement of 93.33–93.50%, and executable test cases for functional verification. The ambiguity injection taxonomy (superficial, knowledge chain-breaking, environmental) is principled and the follow-up sub-tasks with state dependency are a genuine improvement over prior benchmarks (Table 1, Section 3.2).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Synthetic ambiguity injection limits external validity.** Ambiguities are systematically injected for controllability rather than drawn from naturally-occurring user interactions. While this is a sensible design choice for a reproducible benchmark, it means the benchmark measures performance on *synthetic* ambiguities. Real-world user ambiguities are messier, more varied, and sometimes unresolvable. The paper acknowledges this implicitly but does not discuss how findings might generalize to natural interaction settings (Section 3.2). This is a meaningful boundary on the contribution's external validity, not a methodological flaw.

- **Single-run evaluation without variance reporting.** All models are evaluated with temperature=0 in a single run per task, with the paper noting cost constraints. While deterministic decoding reduces variance, the action trajectories in a-Interact could vary with minor prompt differences, and the 1–2% differences between models in Table 2 are reported without confidence intervals or repeated trials. Even a small-scale multi-run analysis on BIRD-INTERACT-LITE would improve confidence in the rankings.

### Trivial
None.

## Nice-to-Haves

- A dedicated limitations section in the main text (rather than implicitly in Future Work) discussing the synthetic ambiguity design, the cost of the simulator, and the static nature of follow-up sub-tasks would improve transparency and trust.
- A concise comparison table with prior multi-turn benchmarks (currently in the appendix) would help readers immediately situate the contribution.
- A more detailed cost breakdown for the user simulator (scaling with task complexity, per-action cost) would help users planning large-scale evaluations.
- A small-scale study comparing simulator-based evaluation with fully natural human-annotated interactions on the same tasks would strengthen the case that synthetic ambiguity patterns mirror natural ones.

## Removed Points

The following points from the inputs were identified and removed under the hard rules:

1. **"Vague description of user simulator's second stage"** (Harsh Critic): The paper explicitly states "Detailed prompts are provided in Appendix R." — the appendix is stripped by the parser. REMOVED per rule: "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references."
2. **"Annotation training and quality control details not described"** (Harsh Critic, Missing Parts #5): The paper states "detailed in Appendix C." REMOVED per same rule.
3. **Harsh Critic's point about the paper citing Appendix for comparison with prior benchmarks** (Missing Parts #3): The paper includes this comparison in the appendix. REMOVED per appendix content rule.
4. **Strength Finder's supporting strength #5 ("Budget-constrained awareness mechanism")**: This is a concrete, specific design feature backed by Section 4 with formulas and action costs. It is appropriately listed as a supporting strength and is verified. **Not removed.**
5. **Any formatting nitpicks or grammar concerns**: None present in the inputs that needed removal.

## Novel Insights

Beyond the paper's own contributions, two observations emerge from synthesizing the reviews: (1) The memory grafting experiment (Figure 5) is perhaps the benchmark's most diagnostic result — it demonstrates that the benchmark's difficulty is *decomposable* into separable skill components (communication vs. SQL generation), a property that few existing benchmarks can claim. This decomposition suggests the benchmark could be used for targeted training of interaction skills independent of SQL ability. (2) The striking mode inversion (GPT-5 worst in c-Interact, best in a-Interact) hints that the *a priori* assumption that more capable models perform better in more constrained settings may be false — and that evaluation modality interacts with model training distributions in ways that the community does not yet understand. This is a finding that could motivate deeper investigation into how LLMs are trained for conversational vs. agentic behavior.

## Suggestions

1. **Add a small multi-run experiment on BIRD-INTERACT-LITE** (e.g., 3–5 runs with temperature>0 for 2–3 models) to provide variance estimates and strengthen the empirical claims about model rankings.
2. **Consider a "natural ambiguity" subset** in a future version, where ambiguities are collected from real user interactions rather than injected, to validate that the benchmark's difficulty and rankings generalize.
3. **Expand the qualitative analysis of effective communication patterns** alluded to in Appendix P — concrete examples of what successful vs. unsuccessful interaction trajectories look like would greatly increase the paper's prescriptive value.
4. **Add a dedicated limitations paragraph** to the main text, explicitly addressing synthetic ambiguity, single-run evaluation, and the static nature of the current follow-up sub-tasks.

## Score and Decision

<score>6.5</score>
<decision>Accept</decision>