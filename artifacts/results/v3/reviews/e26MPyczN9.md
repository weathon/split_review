Now I have a comprehensive understanding of the paper and its context. Let me synthesize the final review.

## Summary of Calibration Anchors

**Round 1 — Topic Anchors:**
- `fvTaoyH96Z` (avg 2.33, low-band): Generalization in RL paper with unfair comparisons and overselling. Much weaker than paper under review.
- `It4KL6XnPq` (avg 3.00, low-band): Foundation policies with memory — weak experiments relative to claims.
- `NGVljI6HkR` (avg 3.67, mid-band): "Reclaiming the Source of Programmatic Policies" — focused comparison of programmatic vs latent space search. More focused but less ambitious than paper under review.
- `lUWf41nR4v` (avg 4.50, mid-band): "Addressing Long-Horizon Tasks" — program synthesis + state machines. Comparable ambition, similar execution issues.
- `QiUitwJDKI` (avg 5.75, mid-band): "InnateCoder" — LLM-generated programmatic options. Stronger experimental grounding.
- `tuEP424UQ5` (avg 5.75, mid-band): MORL generalization — tighter theoretical contribution.
- `OI3RoHoWAN` (avg 8.00, high-band): GenSim — clearly stronger paper with thorough evaluation.

**Round 1 — Weakness-Anchored:**
- `ehSQZa4vuk` (avg 5.25): "Bad Habits: Policy Confounding" — similar in being a re-evaluation study identifying confounds. More focused but comparable in quality.
- `R6klub5OXr` (avg 5.25): RL algorithm design premises analysis — methodological critique paper.

**Round 2 — Bracket Narrowing:**
- `qg5JENs0N4` (avg 5.50): TD learning generalization — well-executed but focused.
- `X1p0eNzTGH` (avg 5.67): Level sampling for generalization — good but narrow.
- `PH7ja3T0vN` (avg 4.50): State combinatorial generalization — interesting but execution issues.

**Comparison Synthesis:** The paper under review is stronger than `NGVljI6HkR` (3.67) in scope and ambition but has more methodological concerns. It is comparable to `lUWf41nR4v` (4.50) and `ehSQZa4vuk` (5.25) — all have genuine contributions but execution issues that prevented acceptance. The paper is weaker than `QiUitwJDKI` (5.75) in experimental grounding.

**What low-band anchors failed at, and does this paper share those failures?** Low-band anchor `fvTaoyH96Z` (2.33) failed at having unfair comparisons (baselines not given the same conditions), unclear framework, and overselling. The paper under review shares some overselling in the abstract but has a clearer framework and generally fairer comparisons, though the KAREL comparison has an asymmetry issue. The paper is substantially stronger than low-band anchors but still shares some overclaiming patterns.

**Final Score: 4.5 — Decision: Reject**

Now let me assemble the full review.

Wait - I need to be more careful about my severity assessment. Let me re-check the "fundamental issues" criteria:

1. "The evaluation methodology is unsound" - No, the evaluation is generally sound. The TORCS experiment uses appropriate methodology (multiple seeds, clear reporting). The KAREL experiment has an asymmetry issue but the methodology itself is not unsound.
2. "The central claim is unsupported by the experiments presented" - The central claim is that programmatic generalization advantages stem from confounds, not representation. This IS supported by the experiments (TORCS: reward engineering closes gap; KAREL: last-action augmentation closes gap; PARKING: neither approach is clearly superior). However, the abstract overclaims by not qualifying the seed-success rates. The central claim is supported, just the abstract presentation is too strong.
3. "Required baselines from the same line of work are absent" - No, the baselines from the original papers are included.
4. "The scope of the contribution is too narrow" - No, the scope is appropriate for this venue.
5. "Two or more human-equivalent reviewers would independently conclude soundness <= 2 or contribution <= 1" - The harsh critic would likely give 2-3 for soundness due to the issues raised. The strength finder would give 3-4. So individually none would give 2 or below for soundness.

So no fundamental issues triggered. The paper has Major weaknesses but not Fatal ones.

Let me proceed with writing the review.## Summary

This paper re-evaluates three influential benchmarks (TORCS, Karel, Parking) where programmatic policies were claimed to generalize better than neural policies. The authors find that after controlling for experimental confounds — reward design in TORCS, observation sparsity in Karel — neural policies can generalize comparably to programmatic ones. They then propose an expressivity/discoverability framework for understanding OOD generalization and argue that programmatic representations have a fundamental advantage on problems requiring instance-scaling working memory (supported by a proof-of-concept using FUNSEARCH to synthesize BFS in Python). The paper is a mix of empirical re-evaluation and conceptual framing.

## Strengths

1. **TORCS re-evaluation genuinely identifies a confound in prior work.** Table 1 shows that adjusting the intrinsic reward parameter from β=1.0 to β=0.5 allows neural DRL policies that successfully learn the training track to generalize OOD at rates (76% to G-TRACK-2, 69% to E-ROAD) comparable to programmatic NDPS policies. This directly demonstrates that the previously observed generalization gap was partly an artifact of speed-optimizing reward design, not representational incomparability. The seed-success data (13/30 for G-TRACK-1, 4/15 for AALBORG) is reported transparently, allowing readers to calibrate the result.

2. **The expressivity/discoverability framework (Definitions 2 and 3) provides a useful conceptual lens** for separating whether a policy space contains a generalizing solution from whether the search algorithm can find it. This distinction is applied to explain each re-evaluation result: the TORCS DSL and neural spaces are similarly expressive (both contain generalizing policies), and the reward modification made the neural space discoverable. The framework is clear enough to guide future experimental design and diagnosis of generalization failures.

3. **The PARKING re-evaluation provides a careful, multi-seed comparison (30 PSM, 15 DQN seeds)** showing neither representation achieves reliable OOD generalization — PSM has a smaller generalization gap (0.10 vs 0.68 drop) but similar absolute test performance (0.16 vs 0.18 success rate). This nuanced result honestly reflects the domain difficulty and avoids a simplistic narrative of programmatic superiority.

4. **The identification of memory-scaling tasks as a class where programmatic representations offer a genuine advantage** is conceptually valuable. The connection to pathfinding (BFS requiring Θ(|V|) frontier/visited set) and nested subproblems (stack-like context management in NetHack) gives concrete failure modes for fixed-capacity architectures. The proof-of-concept that FUNSEARCH can synthesize a BFS program, while preliminary, illustrates the claim.

## Weaknesses

### Major

1. **The abstract overclaims the TORCS result by not qualifying the seed-success rate.** The abstract states "neural policies matched programmatic ones in generalization" without noting that only 13/30 seeds (43%) on G-TRACK-1 and 4/15 seeds (27%) on AALBORG successfully learned the training task in the first place. Among those that learned, generalization rates were high — but NDPS succeeded on all 3/3 seeds (100%). The claim "matched" erases this reliability gap. The data is disclosed in the experimental section, but the high-level presentation is misleading. This matters because a reader (or practitioner) choosing between representations cares about both success rate and generalization rate.

2. **The theoretical memory-capacity argument overlooks environment-as-external memory.** The paper argues that neural policies "cannot encode algorithms whose working memory grows with the input size" and therefore "are not expressive to represent instance-growing structures." This ignores that in RL, the environment can serve as external memory — e.g., in Karel the agent can place and sense markers, effectively writing to the grid. A fixed-capacity neural policy using markers as a visited set could, in principle, implement BFS without requiring internal memory proportional to |V|. The paper frames this as an *expressivity* limitation of neural architectures, but the limitation only holds if one restricts attention to *internal* working memory — a restriction not justified in the paper. This weakens the central theoretical claim. The argument should be reframed as a *discoverability* challenge (can RL training discover such a policy?) rather than an expressivity impossibility, and the environment-as-memory possibility should be explicitly discussed and, where relevant, ruled out by experimental design.

3. **The KAREL comparison is asymmetric: the neural baseline receives information unavailable to programmatic policies.** "PPO with a_{t-1}" augments the observation with the agent's last action. The LEAPS programmatic policies operate using only the perception functions in the Karel DSL (`frontIsClear`, `markersPresent`, etc.), which do not include a last-action sensor. The paper does not test whether adding a last-action sensor to the Karel DSL (possible by extending the grammar) would similarly improve LEAPS, nor does it discuss this observational asymmetry as a limitation of the comparison. While the paper's goal is to show neural policies *can* generalize (not that they beat LEAPS), the asymmetry means Table 2 does not fairly compare the two representation classes under the same observational conditions. The paper's framing in Section 4.2 ("Our results show that partial observability combined with a simpler model can generalize...") is defensible, but the direct tabular comparison with LEAPS is misleading without this caveat.

### Minor

4. **The proof-of-concept uses an unrestricted representation (Python) that is incomparable with the DSLs used in the re-evaluation.** The re-evaluation studies restricted domain-specific languages (TORCS grammar, Karel grammar, PSM grammar), while the FUNSEARCH proof-of-concept synthesizes arbitrary Python programs with lists, queues, and mutable data structures. The paper's narrative jumps from "DSL-based programmatic policies are comparable to neural ones" to "programmatic representations solve memory-scaling tasks" without acknowledging that the latter relies on a fundamentally different, far more expressive representation. The argument that "programmatic policies can produce policies whose memory capacity grows" does not follow from the DSLs evaluated in the benchmarks. This is a structural narrative issue, not a factual error — the paper is clear about using Python — but it creates a disconnect between the two halves of the contribution.

5. **The proof-of-concept lacks a neural baseline on the same task.** The paper demonstrates that FUNSEARCH can synthesize BFS for a wall-sparse Karel maze, but does not train any neural policy (e.g., PPO with LSTM or with a_{t-1}) on this task to test whether a neural network could solve it, perhaps using markers for memory. The claim that "the neural policies we evaluated have fixed-sized hidden states... consequently they are not expressive" remains a theoretical assertion without empirical support on this specific task. Adding this comparison would be the most direct way to substantiate the paper's main positive thesis.

6. **The proof-of-concept reports minimal detail.** The paper states "Three runs of FUNSEARCH returned a correct implementation of breadth-first search" but does not report the total number of attempts, the success rate, or a description of the wall-sparse maze (Figure 7, in the appendix which is stripped from the submitted version). The claim that BFS "generalizes to any pathfinding problem" is correctness-by-construction, but no verification results are shown.

7. **The expressivity/discoverability framework is not used to formally analyze the benchmarks.** The paper claims the TORCS DSL and neural spaces are similarly expressive but relies on intuition about ReLU networks rather than an explicit construction or formal argument. Similarly, the claim that LSTM policies "are expressive but not discoverable" for Karel is asserted without formal analysis — the LSTMs could in principle implement the needed finite-state machines (as the paper acknowledges via Weiss et al. 2018), but no analysis explains why the specific RL training setup failed to discover them.

### Trivial

- The paper would benefit from reporting hyperparameters (learning rates, network architectures, training steps) in the main text rather than deferring to future code release, especially for a re-evaluation paper.
- The PARKING interpretation could be more precise: "PSM generalizes better" based on the smaller gap is ambiguous when absolute test performance is nearly identical (0.16 vs 0.18).

## Nice-to-Haves

- A direct experiment training a neural policy (LSTM or PPO with a_{t-1}) on the wall-sparse Karel maze and testing on larger instances would substantially strengthen the paper's main positive thesis.
- Testing whether adding a last-action sensor to the Karel DSL improves LEAPS would make the KAREL comparison fair and potentially reveal whether programmatic policies also benefit from this information.
- The environment-as-memory question could be addressed by designing the wall-sparse maze to block marker-based solutions (e.g., no markers available, or markers don't persist).
- The paper briefly mentions LLMs and memory-augmented neural models (stack-RNNs, neural Turing machines) as alternative approaches to memory-scaling tasks but does not compare against them experimentally.

## Removed Points

- **TORCS "success-rate gap" as a fatal flaw:** The harsh critic argued the headline claim "erases the success-rate gap." While the abstract is too strong, the paper does report seed counts transparently in the experimental section. The claim is about generalization *among successful models*, which is disclosed. Demoted from the harsh critic's framing as a critical/evidential issue to a Major weakness (abstract overclaiming) because the data exists in the paper.
- **"NDPS success rate not reported":** The harsh critic says "the paper does not report the success rate of NDPS seeds (it only says 'all three generalize')." The paper uses NDPS results from the original publication (3 seeds, all succeed) — this is standard for citing prior work. Removed as a non-issue.
- **"KAREL comparison is not a failure of programmatic representation":** The harsh critic frames this as "not a failure of programmatic representation; it is a change in the observation space." The paper's goal is to show neural policies *can* generalize under adjusted conditions, not to claim programmatic representations failed. The asymmetry remains a real concern, but the critic's framing overstates the intent. Demoted from a "methodological gap that undermines the fairness" to a Minor weakness because the paper's central claim (neural policies can generalize) does not depend on beating LEAPS.
- **"No description of wall-sparse maze":** The paper references Figure 7 which is in the appendix. The appendix is stripped from the PDF extraction. The description likely exists in the original submission. Removed.
- **Pure formatting/style nitpicks** (e.g., missing related work mentions, reproducibility about hyperparameters being deferred): removed per instructions.

## Novel Insights

The most interesting insight from the reviews is that the paper's two halves (re-evaluation showing comparability, proof-of-concept showing programmatic advantage) sit in tension with each other. The re-evaluation uses heavily restricted DSLs and shows they're comparable to neural policies; the proof-of-concept uses unrestricted Python and shows an advantage. This paradox — "programmatic representations are special when they are, but only when they are expressive enough to be a different kind of object entirely" — is a genuinely important observation about how the field talks about "programmatic" policies that neither the paper nor the reviews fully articulate. The paper would benefit from explicitly confronting this tension: if the advantage requires moving from DSLs to general-purpose programming languages, then the DSL-based programmatic RL literature may be aiming at the wrong target.

## Suggestions

1. Revise the abstract and introduction to report the seed-success rates alongside the generalization rates for TORCS. The claim should read "neural policies that successfully learned the training task generalized at rates comparable to programmatic policies" rather than "neural policies matched programmatic ones."

2. Add a discussion of the KAREL observation-space asymmetry. Either add last-action sensing to the Karel DSL and test whether LEAPS improves, or explicitly note the asymmetry as a limitation of the comparison.

3. Address the environment-as-memory issue directly. Acknowledge that markers provide external memory in Karel, explain why this does or does not circumvent the expressivity limitation, and clarify that the paper's argument about neural inexpressivity applies to *internal* working memory, reframing the contribution as about discoverability rather than expressivity for environments that allow writing.

4. Add a neural baseline to the wall-sparse maze experiment. Training PPO with LSTM or with a_{t-1} and evaluating on larger mazes would directly test whether neural policies fail on a task where programmatic BFS succeeds.

5. Report proof-of-concept details: number of FUNSEARCH attempts, success rate, description of the wall-sparse maze, and optionally verification of the synthesized BFS program on held-out instances.

## Score and Decision

**Round 1 bracket:** (3.5, 6.0) — based on comparison with topic-anchored and weakness-anchored calibration results. The paper is clearly stronger than the <3.5 band papers (which had fundamental methodology issues) but sits below the 5.75-6.0 papers (InnateCoder, MORL generalization) which had stronger experimental grounding and more focused contributions.

**Round 2 narrowing:** Within the (3.5, 6.0) bracket, the paper compares most directly to "Reclaiming the Source" (3.67, more focused but limited), "Addressing Long-Horizon Tasks" (4.50, comparable ambition and comparable execution gaps), and "Bad Habits: Policy Confounding" (5.25, clearer theoretical framing but toy experiments). The paper under review has more empirical breadth than "Reclaiming the Source" and "Bad Habits" but less rigor in its central claims. The combination of abstract overclaiming, the KAREL asymmetry, the environment-as-memory oversight, and the proof-of-concept disconnect collectively place it at the lower end of this comparison set.

**What the low-band anchors and weakness-anchored papers failed at:** The 2.33 anchor failed at having unfair comparisons and overselling. The paper under review shares some overselling (abstract) and an asymmetric comparison (KAREL). The 5.25 "Bad Habits" anchor was rejected despite a clear theoretical contribution because of toy experiments and overclaiming. The paper under review has more substantive experiments but also more accumulated weaknesses.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>