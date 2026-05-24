Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper introduces BIRD-INTERACT, a benchmark for evaluating LLMs on interactive, multi-turn text-to-SQL tasks. It builds on LIVESQLBENCH by (1) injecting ambiguities and adding follow-up sub-tasks to create 900 interactive tasks spanning the full CRUD spectrum; (2) proposing a function-driven user simulator (mapping queries to AMB/LOC/UNA actions) that prevents ground-truth leakage; and (3) defining two evaluation settings—c-Interact (conversational protocol) and a-Interact (autonomous agent). Experiments across 7 frontier LLMs show that even the strongest models succeed on only ~17% of tasks in either setting, and memory grafting experiments demonstrate that interaction strategy matters separately from SQL generation skill.

## Strengths

- **Function-driven user simulator with strong validation against ground-truth leakage.** The two-stage design (semantic parser → constrained symbolic actions → controlled response) reduces the failure rate on UNA (unanswerable) questions from 67.4% (baseline) to 2.7% on the USERSIM-GUARD dataset (Section 6, Figure 6). This is the first quantitative demonstration that automated interactive text-to-SQL evaluation can be both scalable and fair.

- **Two evaluation settings reveal divergent model rankings, proving they measure distinct capabilities.** Table 2 shows GPT-5 achieving the worst *c*-Interact SR (14.50%) but the best *a*-Interact SR (29.17%), while Qwen-3-Coder-480B shows the opposite pattern. No prior multi-turn benchmark (CoSQL, SParC) provides this split because they rely on static transcripts.

- **Memory grafting isolates communication ability from SQL generation.** Figure 5 shows GPT-5's SR jumps from 13.8% to 20.5% when given O3-mini's interaction history but writing its own SQL. This provides direct causal evidence—not just correlation—that interaction quality is the bottleneck, a finding impossible with shared-transcript datasets.

- **Human alignment study validates simulator realism.** Table 3 reports Pearson r = 0.84 (p = 0.02) between simulator-based and human-based SR for GPT-4o with function calling, versus 0.61 (p = 0.14) without. This is the first quantitative link between simulated and human interaction patterns in text-to-SQL.

- **Comprehensive task construction with strong quality control.** The ambiguity injection taxonomy (superficial, knowledge, environmental) and follow-up sub-task generation are principled. Annotation by 12 experts with 93% inter-agreement inspires confidence. The task suite extends beyond SELECT-only to the full CRUD spectrum (410 BI + 190 DM tasks in the full set).

- **Interaction Test-Time Scaling (ITS) experiment validates that the benchmark rewards effective interaction.** Figure 4 shows Claude-3.7-Sonnet's c-Interact SR rising monotonically (~15% → ~30%) as user patience increases from 0 to 7, while single-turn idealized performance is flat—a capability no static-transcript benchmark can measure.

## Weaknesses

### Fatal

None.

### Major

- **The user simulator backbone used for the main experiments (Table 2) is not specified.** Section 6 validates two function-driven simulators (GPT-4o and Gemini-2.0-Flash), but the paper nowhere states which backbone generated the main results. Table 2's footnote reports an average simulator cost of $0.03 but omits the model identity. This is a concrete reproducibility gap: it prevents others from replicating the leaderboard and assessing whether the system model rankings could be influenced by simulator-model compatibility (e.g., if the simulator uses GPT-4o and GPT-5 is the top system). The paper should disclose the exact model version and verify robustness with a second backbone. This is a fixable issue, but it is the single most consequential missing detail in an otherwise well-documented benchmark.

### Minor

- **Single-run evaluation without variance reporting.** Section 5 acknowledges single runs "due to cost." While temperature=0 reduces variance, LLM API calls are not fully deterministic. The nuanced differences in Table 2 (e.g., GPT-5 at 8.67% vs. Qwen-3-Coder at 10.83% in c-Interact follow-up SR) are presented without confidence intervals or replication. This does not undermine the paper's core finding (the benchmark is hard, and interaction strategy matters), but it limits confidence in fine-grained model ordering. Running 3 seeds on a representative subset would be sufficient.

- **The "ITS Law" claim in the abstract and Section 5.2 is overstated.** The abstract states "performance improves monotonically with additional interaction opportunities across multiple models." However, Figure 4 shows that only Claude-3.7-Sonnet exhibits clear monotonic scaling; O3-Mini and Qwen-3 plateau or show non-monotonic behavior. The formal definition in §5.2 ("A model satisfies this law if...") is conditional, but the framing in the abstract and the naming ("ITS Law") imply broader generality than the data support. This should be softened to a model-specific observation.

- **LOC action coverage and fidelity are not analyzed.** The LOC action handles reasonable clarification requests outside pre-annotated ambiguities using AST-based retrieval from the ground-truth SQL. The paper does not report how many queries in the main benchmark trigger LOC, and whether the AST retrieval always returns a relevant SQL fragment. This is a gap because simulator reliability directly affects evaluation fairness.

- **The "cumulative" label for follow-up success rate is ambiguous.** Table 2 reports follow-up SR as a proportion of all tasks (e.g., GPT-5: 8.67%). Since Section 2 states "subsequent sub-tasks are released only after successful completion of first sub-tasks" and Section 4.1 confirms failure terminates the session, the follow-up SR is necessarily at most the priority SR. The denominator should be explicitly stated—readers unfamiliar with the setup may misunderstand whether this is conditional or unconditional.

### Trivial

- The paper uses "Budget-Constrained Awareness Testing" (Section 4) and later "stress-mode" (Section 8) for the same concept without explicit alignment.
- Debugging turns are described as consuming budget separately from clarification turns, but the reward diagram (Figure 3) could state this more explicitly in the caption.

## Nice-to-Haves

- **Break down what makes an interaction strategy effective in the memory grafting experiment.** The paper shows GPT-5 improves when given other models' histories but does not analyze what specific properties of those histories drove the improvement (number of AMB vs. LOC turns, average turn length, types of questions). A qualitative or quantitative breakdown would deepen the analysis.

- **Direct comparison with LIVESQLBENCH single-turn performance.** The "idealized" baseline in Figure 4 hints at this, but a direct table showing model scores on the original LIVESQLBENCH single-turn tasks versus the corresponding BIRD-INTERACT interactive tasks would more directly strengthen the case that interaction is the distinguishing factor.

- **Report action distributions in tabular form** for the full set (the paper gives percentages only for the lite set at the end of §5.2).

## Removed Points

These points from the input reviews are removed or demoted with justification:

- **"The paper does not report LIVESQLBENCH scores directly"** (Harsh Critic, Strengthening section): This is a scope suggestion, not a core weakness. The paper provides an "idealized" single-turn baseline in Figure 4.
- **"The author's own confound: if the simulator uses GPT-4o and GPT-5 is the same lineage..."** (Harsh Critic, first critical issue): The simulator-backbone-not-specified concern is retained as a Major weakness, but the specific speculation about GPT lineage confounding model rankings is removed because (a) the backbone is unknown, making this untestable, and (b) even if true, it would affect ranking granularity, not invalidate the benchmark.
- **"Does the debugging turn consume a clarification turn?"** (Harsh Critic, Section 4 notes): The paper clearly separates debugging (single separate opportunity with reward penalty) from clarification budget (τ_clar = m_amb + λ_pat). This is sufficiently clarified.
- **"The paper could demonstrate that the benchmark's difficulty does not arise solely from task complexity or SQL length"** (Harsh Critic, Strengthening section): This is a nice-to-have enhancement, not a weakness.
- **"Develop a post-trained local user simulator" and "free-mode evaluation"** (Harsh Critic, Strengthening): These are future work suggestions, not weaknesses.
- **Several generic strengths from the Strength Finder** (e.g., "the paper addressed an important problem"): Removed as generic. Only specific, evidence-backed strengths are retained.
- **"Missing related works"**: Removed per rule — I cannot verify absence of citations without external sources.

## Novel Insights

The most insightful finding to emerge from the reviews is the **disconnect between the paper's own data and its "ITS Law" framing**. The paper defines this law broadly and claims monotonic improvement "across multiple models," yet Figure 4 shows only Claude-3.7-Sonnet demonstrating clear monotonic scaling. The other models plateau or behave non-monotonically. This tension is worth noting because the ITS framing is one of the headline claims in the abstract, and the actual data tell a more nuanced story: only some models can effectively leverage additional interaction turns. Understanding *which* models benefit and why could be a deeper research direction than the law framing suggests.

Beyond the paper's own contributions: the memory grafting experiment combined with the action distribution analysis suggests that effective interaction strategy is task-dependent. GPT-5 (best at a-Interact, worst at c-Interact) succeeds when it can autonomously explore but fails when constrained to a conversational protocol. This pattern hints that current LLMs may have a systematic mismatch with structured conversational workflows—a hypothesis worth testing beyond text-to-SQL.

## Suggestions

1. **Specify the simulator backbone used for Table 2** and ideally verify rankings hold with a second backbone (e.g., Gemini-2.0-Flash).
2. **Run the best and worst models (GPT-5, Qwen-3-Coder) with 3 different seeds on the lite set** and report mean ± std for the key metrics.
3. **Tone down the "ITS Law" framing** to a model-specific observation (Claude-3.7-Sonnet shows clear scaling; other models show partial improvement).
4. **Report LOC invocation frequency** for a typical evaluation run and manually audit a random sample of 50 LOC interactions for faithfulness.
5. **Explicitly state the denominator for follow-up SR** in the Table 2 caption or metric definition section.

## Score and Decision

**Round 1 Bracketing:** I retrieved anchors across three bands. Weak anchors (scores 2.0–3.33) included Octopus (2.50), ConDABench (2.50), and SQLAgent (3.33)—papers with fundamental construction or validation issues. Middle anchors (3.5–7.5) included EHR-ChatQA (4.00), Enterprise Text-to-SQL Benchmarks (3.60), MTIR-SQL (4.67), Beyond Text-to-SQL Debugging (5.00), SPARTA (5.00), and Computer Agent Arena (6.50). Strong anchors (7.5+) included LLMs Get Lost In Multi-Turn Conversation (8.00, Oral), Gaia2 (8.00, Oral), and AstaBench (7.00, Oral).

The paper is clearly stronger than the weak anchors and the lower middle anchors (EHR-ChatQA, Enterprise benchmarks). Compared to Computer Agent Arena (6.50): BIRD-INTERACT has more thorough benchmark construction (12-expert annotation, 93% agreement vs. crowd-sourced tasks), stronger quantitative validation (human alignment r=0.84, USERSIM-GUARD results), and deeper analytical experiments (memory grafting, ITS). CAA's strength is its novel human-preference evaluation paradigm. BIRD-INTERACT is comparable in overall quality.

The paper is not at the 8.0 Oral level—those papers (LLMs Get Lost, Gaia2) have broader cross-domain significance and more novel methodological paradigms.

**Round 2 Narrowing:** I retrieved anchors in the 4.5–6.5 and 6.0–8.0 bands. The most relevant comparison is Beyond Text-to-SQL Debugging (5.00), which was criticized for overclaiming enterprise realism and LLM bias in data generation. BIRD-INTERACT's human annotation and stronger validation make it a clearly stronger benchmark. Computer Agent Arena (6.50) provides the best upper anchor. BIRD-INTERACT is comparable in rigor and slightly stronger in quantitative validation, though CAA's paradigm is more novel.

**Final score: 6.5.** The paper makes a solid contribution to the text-to-SQL evaluation infrastructure. Its main weakness (unspecified simulator backbone) is fixable and does not threaten the core claims. The benchmark construction, simulator validation, and analytical experiments are thorough and well-executed.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>