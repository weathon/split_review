Now I have all the evidence needed. Let me synthesize the consolidated review.

## Summary

BIRD-INTERACT introduces a benchmark for evaluating LLMs on interactive text-to-SQL tasks that require multi-turn interaction, ambiguity resolution, and full CRUD operations. The key contributions are: (1) a function-driven user simulator with a two-stage parser-generator architecture that constrains the simulator's behavior to three symbolic actions (AMB/LOC/UNA), reducing ground-truth leakage compared to naive LLM-as-user baselines; (2) dual evaluation settings — c-Interact (protocol-guided conversation) and a-Interact (autonomous agentic mode) with budget-constrained awareness; and (3) a task suite of 600 tasks (300 lite) built by injecting ambiguities into LIVESQLBENCH, each with two sub-tasks and executable test cases. Empirical results show that even GPT-5 achieves only 8.67% (c-Interact) and 17.00% (a-Interact), establishing the benchmark as genuinely challenging.

## Strengths

- **Function-driven user simulator design (§3.3, §6):** The two-stage parser-generator architecture with the AMB/LOC/UNA action space is a genuine methodological contribution. The empirical validation on USERSIM-GUARD (2,100 questions) is convincing: failure rates on unanswerable (UNA) questions drop from 67.4% (baseline LLM-as-user) to 2.7% (function-driven). The human alignment study (Table 3) reports a Pearson correlation of 0.84 (p=0.02) between simulator and human success rates across 7 models on 100 tasks, substantially higher than the baseline simulator (r=0.61, p=0.14). While the small n (7 models) limits the statistical strength, the direction is consistent and supports the design.

- **Comprehensive task construction with principled ambiguity injection (§3.2, Appendix H):** The ambiguity injection methodology is carefully designed, with a clear taxonomy (intent-level, implementation-level, knowledge, environmental) and the knowledge-chain-breaking mechanism (Figure 2) that creates genuinely challenging multi-hop clarification scenarios. The requirement for strategic source selection (User→Environment→User transitions) goes beyond single-source ambiguity in prior benchmarks. The inter-annotator agreement of 93.33–93.50 and the human quality evaluation (97.3% acceptance rate on 300 sampled data points, Appendix Q) demonstrate rigorous construction.

- **Dual evaluation settings reveal non-trivial behavioral differences (§4, §5):** The distinction between c-Interact and a-Interact is well-motivated and reveals meaningful patterns — e.g., GPT-5 performs worst in c-Interact (14.50% SR) but best in a-Interact (29.17% SR on LITE), showing that interaction paradigm choice is an understudied variable. The action-distribution analysis (Figures 10–13) identifying that models overuse expensive trial-and-error (submit/execute) while underusing environment exploration, with a negative correlation between execute proportion and first-subtask success (Pearson r≈−0.52), provides actionable insight for future work.

## Weaknesses

### Major

- **The user simulator's reliance on ground-truth SQL for LOC() actions is a structural limitation that the paper only partially addresses (§3.3, Appendix D).** The simulator is explicitly given the reference SQL (Appendix D: "the simulator is additionally provided with the reference SQL") and uses AST-based retrieval from the GT SQL to answer LOC()-type clarification questions. This means that when a model asks "should I use column X or Y?", the simulator can consult the correct answer — something a real user who lacks formalized intent cannot do. The paper acknowledges this as a "pragmatic design choice" and attempts to mitigate it through the human alignment study (Table 3, r=0.84), but the alignment evidence measures only aggregate success-rate correlation across 7 data points, not turn-level behavioral realism. The benchmark may partially measure a system's ability to extract information from an oracle rather than to collaborate with a user who has genuine uncertainty. This is an inherent tension in simulator-based evaluation, not a fixable bug, and future versions would benefit from turn-level validation (e.g., comparing individual simulator responses to human responses on the same clarification questions) to establish behavioral realism more convincingly.

- **The memory grafting experiment (§5.2, Figure 5) is confounded and does not fully support the conclusion drawn from it.** The experiment gives GPT-5 the full interaction histories (including all clarifications obtained) from better-performing models and shows improved SQL generation. The paper concludes that "GPT-5 possesses robust SQL generation capabilities" and that "a more effective communication schema is required." However, the improvement could simply reflect information acquisition — GPT-5 now has the correct clarifications — rather than anything about communication patterns. The conclusion about "communication schema" requires a cleaner control: giving GPT-5 the *same clarifications* but allowing it to generate its own interaction path (or providing the clarifications as pre-answered facts rather than full dialogue histories). The basic finding (GPT-5 benefits from better interaction data) is valid, but the attribution to communication schema is unsupported.

### Minor

- **The "Interaction Test-Time Scaling (ITS)" framing overclaims what is a straightforward finding (§5.2, Figure 4).** The experiment shows that Claude-3.7-Sonnet's performance improves with a larger interaction budget (patience=0,3,5,7). This is expected — more clarification turns mean more opportunities to resolve ambiguities. Framing this as "Interaction Test-time Scaling" with a branded acronym (ITS) implies a parallel to test-time compute scaling in reasoning models (e.g., chain-of-thought), which this does not match. The finding is useful as a sanity check (the benchmark rewards interaction), but the scaling claim is not novel or informative. The dotted "Idealized Performance" line (ambiguity-free single-turn) sets an uninteresting ceiling — providing all context upfront is by definition not interactive.

- **No specialized text-to-SQL methods are evaluated (§5).** The paper evaluates only 7 general-purpose LLMs. Existing interactive or agent-based text-to-SQL methods (MAC-SQL, DAIL-SQL, CodeS, CHASE-SQL) are discussed in related work but never benchmarked. While the paper is a benchmark contribution and cannot evaluate every method, the omission weakens the headline finding ("GPT-5 only achieves 8.67%") — it is unclear whether specialized methods would perform substantially better. Adding at least one representative agent-based method (e.g., MAC-SQL adapted to the interactive setting) would strengthen the paper's contribution to the text-to-SQL community.

- **The evaluation uses single runs per model (temperature=0).** While deterministic decoding is standard practice and cost constraints are acknowledged, the lack of multiple runs means variance across runs (which can be non-trivial even at temperature=0 due to API non-determinism) is not reported. This is standard practice for large-budget evaluations but should be noted.

### Trivial

- The "full CRUD spectrum" claim (§1, abstract) is not substantiated with a breakdown of task types — only BI vs. DM are reported in the main results.
- The 70/30 reward weighting for sub-tasks (Appendix F) is presented without justification.

## Nice-to-Haves

- **Free-mode experiments (§8 future work):** The current evaluation is exclusively "stress-mode" (tight budget). Free-mode experiments without budget pressure would distinguish budget effects from capability effects and are promised for future work but would strengthen the main paper.
- **Per-ambiguity-type model × type heatmap:** Figure 14 aggregates across 7 models; a per-model breakdown would show which models handle which ambiguity types best.
- **Ablation removing LOC() action** to measure how much the benchmark relies on unannotated clarifications versus pre-annotated ambiguities.

## Removed Points

- **"No evaluation of specialized methods is a fatal omission"** — weakened from fatal to minor. The paper scopes itself as evaluating general LLMs and benchmarks are not required to evaluate every method; however, including one representative would strengthen the contribution.
- **"Human alignment study has n=7, too small"** — the study is acknowledged as limited (the paper reports p-values), and the correlation is directionally convincing despite small n. The real concern is turn-level validation, not aggregate.
- **"§5.2 BI vs. DM claim not supported by data"** — re-reading Table 2, the paper does show BI success rates are consistently lower than DM across models; the claim is supported.
- **"The action costs may bias behavior"** — the cost structure is transparently reported and is a deliberate design choice, not a weakness.
- **"CRUD breakdown not provided"** — moved to trivial; it's a presentation nicety, not a substantive gap.
- Strength Finder #4 ("memory grafting isolates communication as a separate skill") — conflicts with the verified confound; removed.
- Various formatting/parser-artifact criticisms removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The insight that interaction mode (constrained conversation vs. autonomous agent) is a stronger determinant of success than model capability for some models (e.g., GPT-5's diametrically opposite performance across c-Interact and a-Interact) is the paper's most interesting finding and is already presented.

## Suggestions

1. **Address the GT SQL concern more directly** by adding a turn-level behavioral comparison between simulator responses and human responses (even on a subset of 50 tasks), showing whether the simulator answers clarification questions in ways consistent with human users, not just whether final success rates correlate.
2. **Clean up the memory grafting experiment** by adding a control condition where GPT-5 receives the same clarification answers without the interaction history, to isolate whether improvement comes from information content or interaction structure. Alternatively, reframe the conclusion to focus on the finding that GPT-5's failure is not due to SQL generation ability alone.
3. **Downgrade the "ITS" branding** to a more measured description ("performance improves with interaction budget") and add the full set of models to Figure 4 (currently only Claude-3.7-Sonnet is labeled in the narrative).
4. **Add at least one specialized method** (e.g., adapting MAC-SQL's agent framework to the interactive setting) to establish whether the benchmark's difficulty is specific to general LLMs.
5. **Provide a breakdown of task types** (CREATE/READ/UPDATE/DELETE) to substantiate the full-CRUD claim.

## Score and Decision

**Calibration anchors** (batch retrieval results, listed for comparison):

| Anchor Path | Avg Human Score | Comparison |
|---|---|---|
| VKGTGGcwl6 (LLMs Get Lost In Multi-Turn Conversation) | 8.0 | Stronger paper — cleaner methodology, more models, deeper behavioral analysis, no GT SQL concern |
| 9gw03JpKK4 (Gaia2) | 8.0 | Stronger benchmark — asynchronous environments, platform release, more comprehensive evaluation |
| 8Fm6OKFuRv (Beyond Text-to-SQL: Enterprise SQL Debugging) | 5.0 | Weaker paper — overclaimed realism, LLM-generated data without human validation; BIRD-INTERACT has real human annotation and better validation |
| hLweUPBz7k (EHR-ChatQA) | 4.0 | Comparable but weaker — smaller scale (64 AdaptQA tasks), less validated user simulator; BIRD-INTERACT is more comprehensive |
| BdlIQGetYv (Octopus) | 2.5 | Much weaker — fully auto-generated, no human validation; BIRD-INTERACT has rigorous human annotation |
| 762D8ndh2E (UI-Simulator) | 3.0 | Different domain, but weaker methodology — LLM-generated synthetic data with low downstream performance |

BIRD-INTERACT is clearly stronger than the rejected/low-scoring anchors (Octopus 2.5, UI-Simulator 3.0) and comparable to or stronger than EHR-ChatQA (4.0, accepted Poster). It is weaker than the top-tier papers (LLMs Get Lost 8.0, Gaia2 8.0) which have cleaner methodology and fewer unresolved concerns. The paper's function-driven simulator design and comprehensive task construction represent genuine contributions, but the GT SQL reliance in the simulator and the overclaimed analyses prevent it from reaching the top tier. This places it at the boundary between Accept and Reject — solid contributions with clear, non-fatal limitations that can inform future work.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>