Now I have a thorough understanding of the paper and the calibration landscape. Let me write the final consolidated review.

---

## Summary

This paper re-evaluates prior claims that programmatic policies generalize better than neural policies in RL. Through careful experiments on TORCS, KAREL, and PARKING, the authors demonstrate that much of the previously reported OOD generalization gap stems from experimental confounds — specifically reward design (TORCS) and observation sparsity (KAREL) — rather than intrinsic representational differences. They introduce an expressivity/discoverability framework and argue that programmatic representations hold a genuine advantage only when tasks require working memory that scales with input size (e.g., general pathfinding), providing a proof-of-concept via FUNSEARCH synthesizing BFS.

## Strengths

- **Convincing TORCS re-evaluation isolates the reward confound**: By simply down-weighting the speed term in the reward (β=0.5), neural DDPG policies generalize to unseen tracks (76% on G-TRACK-2, 69% on E-ROAD, Table 1), directly demonstrating that the earlier OOD gap reported for NDPS was driven by optimization incentives rather than representational factors.

- **KAREL results pinpoint observation sparsity as the key factor**: A simple feedforward PPO agent augmented with only the previous action achieves perfect generalization (1.00 return) across four KAREL problems on 100×100 grids (Table 2), while the original baselines (ConvNet on full state, LSTM on partial state) fail. This cleanly isolates sparse observations and appropriate inductive biases as the crucial ingredient previously misattributed to programmatic languages.

- **Expressivity/discoverability framework provides a coherent lens**: Definitions 2 and 3 offer precise criteria for when a representation enables OOD generalization, and the paper consistently applies them to explain why prior programmatic gains were due to discoverability confounds while identifying memory-scaling tasks as the regime where neural expressivity is fundamentally insufficient (Section 5).

- **PARKING results add valuable nuance**: Table 3 shows that programmatic policies (PSM, 0.16 test success rate) and neural policies (DQN, 0.18) both struggle, challenging the narrative of inherent programmatic superiority and pointing toward genuinely hard domains for both representations.

- **Proof-of-concept demonstrates programmatic synthesis for memory-scaling tasks**: FUNSEARCH successfully synthesizes BFS for a wall-sparse KAREL maze where constant-memory heuristics fail, providing concrete evidence of a problem class where programmatic representations hold an advantage (Section 5).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **SparseMaze proof-of-concept is one-sided**: The central theoretical claim — that commonly used neural architectures cannot encode algorithms with instance-scaling memory — is argued theoretically but not tested empirically. Adding a neural baseline (e.g., LSTM, transformer) on the SparseMaze task that demonstrably fails as maze size grows would convert a plausible theoretical argument into a strong empirical demonstration. The paper acknowledges this implicitly by framing the experiment as a "proof-of-concept," but the claim would be substantially stronger with an empirical neural failure case.

- **KAREL observation-space difference deserves explicit discussion**: Adding `a_{t-1}` to the neural observation provides information the LEAPS grammar (Figure 2) does not explicitly include, though LEAPS programs have implicit memory through control flow. The paper's core insight — that sparse observations help generalization — is valid, but the comparison would benefit from acknowledging this difference and explaining why it does not undermine the conclusion (e.g., noting that LEAPS programs can maintain equivalent state through loops and conditionals).

- **Memory-scaling argument scope could be sharper**: The paper asserts that recurrent models "cannot encode algorithms whose working memory grows with the input size" (Section 5), then later acknowledges memory-augmented models (stack-RNNs, NTMs) can approximate such structures. The argument applies cleanly to fixed-capacity architectures commonly used in the compared prior work, but the paper would benefit from explicitly delineating which neural architectures are subject to this limitation and which are not at the point where the claim is first made.

- **NetHack/nested-subproblems thread is mentioned but not developed**: The paper references nested subproblems and NetHack as another class where memory-scaling matters (Section 5), but provides no empirical exploration or concrete analysis. This thread could either be expanded into a substantive point or trimmed to maintain focus.

- **TORCS re-evaluation uses original NDPS results rather than re-running with cautious reward**: The paper compares NDPS (trained with β=1.0) against DRL (trained with β=0.5). The paper's goal is to show the original gap was due to reward, not representation — and the experiment cleanly demonstrates this. However, the claim that neural policies "matched" programmatic ones would be more airtight if NDPS were also evaluated under β=0.5, or if the paper explicitly argued why this is unnecessary given the experimental logic. The paper partially addresses this by conjecturing that "NDPS and PROPEL would not generalize to OOD problems if they could find better optimized policies" (Section 4.4), but this remains a conjecture.

### Trivial

- The expressivity/discoverability definitions (Definitions 2 and 3) are introduced only in Section 5; mentioning them earlier (e.g., in Section 2) would improve coherence for readers following the paper's conceptual arc.

## Nice-to-Haves

- **Leverage PARKING results more fully**: The PARKING domain, where both representations fail, could be analyzed to illustrate what makes a domain genuinely hard — perhaps the need for precise numeric thresholds in transition guards — adding nuance to the overall argument about when representation matters.
- **Quantitative evaluation on SparseMaze**: Reporting success rates on progressively larger maze sizes would make the generalization claim more concrete.
- **More formal treatment of discoverability**: A brief discussion of what makes a search space discoverable (e.g., smoothness of the fitness landscape) would strengthen the conceptual framework.
- **Control for observation space in KAREL**: Training an LSTM with better optimization or curriculum that matches LEAPS's effective information — or augmenting LEAPS with action history and verifying no change — would isolate the representation effect more cleanly.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Asymmetric comparisons in the TORCS re-evaluation" (Harsh Critic #1)** — The harsh critic claimed the comparison "does not isolate the role of the representation." This misunderstands the experimental logic: the paper is showing that the *original* gap was confounded by reward design. Changing only the neural reward while keeping the programmatic result from the original paper (as a reference point) is the correct experimental design for this claim. The paper does not claim NDPS would fail with β=0.5; it claims the original gap arose from the reward, not the representation. Removed as a strawman.

- **"OOD generalization 'match' is not fully supported (Table 1)" (Harsh Critic #2)** — The harsh critic argued that imbalanced sample sizes and lower neural training success rates weaken the conclusion. The paper transparently reports all fractions (13/30, 4/15, 76%, 69%, 1.00) and the claim is that neural policies *can* match programmatic ones — not that they always do or that neural training is more reliable. The data supports the claim. Removed.

- **"SparseMaze proof-of-concept details are absent or removed (presumably in the appendix)" (Harsh Critic, Section-by-Section)** — Per hard rules, criticisms about missing appendix content are removed. The appendix is stripped by the parser.

- **"The KAREL comparison introduces an observation-space asymmetry" (Harsh Critic #3 — full severity version)** — The harsh critic framed this as a major confound. However, adding `a_{t-1}` is the paper's deliberate intervention to handle partial observability with a simpler model, demonstrating that sparse observations + simple model → generalization. LEAPS programs have equivalent state-tracking capability through their control flow. Demoted to Minor (retained above) with a request for explicit discussion rather than treated as a fatal confound.

- **"Underspecified memory-scaling argument" (Harsh Critic #5 — full severity version)** — The harsh critic claimed this "weakens the sharp dichotomy." The paper does distinguish architectures in the last paragraph of Section 5. Demoted to Minor with a suggestion to make the distinction earlier and more explicitly.

- **Strength Finder: "the paper supplies a clear conceptual framework"** — Retained (merged into Strengths #3).

- **Strength Finder: "the re-evaluation spans three distinct, well-known benchmarks and uses minimal, well-motivated modifications"** — Retained (merged into Strengths #1, #2, and #4).

## Novel Insights

The paper offers a genuinely useful reframing: rather than asking "do programmatic policies generalize better?" (a question the literature answered with confounded yes/no results), it asks "under what conditions does representational choice actually matter for OOD generalization?" The answer — that for most tested benchmarks the representations are expressively equivalent and only discoverability differs, while memory-scaling tasks create a genuine expressivity gap — provides a principled way to design future comparisons and representations. This shift from benchmarking representations to characterizing the problem classes they can solve is a productive direction.

## Suggestions

- Consider adding a small empirical neural baseline on SparseMaze to directly validate the memory-scaling argument. Even a simple LSTM trained on small mazes and tested on progressively larger ones would substantiate the theoretical claim.
- Expand Section 5's discussion of which neural architectures are subject to the fixed-capacity limitation, explicitly distinguishing fixed-capacity RNNs/feedforward networks from memory-augmented architectures, to preempt the obvious counterargument.
- Consider trimming or developing the NetHack/nested-subproblems discussion so it does not read as an abandoned thread.

## Score and Decision

### Anchor comparison

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| NGVljI6HkR (Programmatic vs Latent Spaces) | 3.67 | R1 | Same domain (Karel, LEAPS) but much narrower, less novel, significant presentation issues. This paper is substantially stronger. |
| lUWf41nR4v (Program Synthesis + State Machines) | 4.50 | R1 | Related topic but unclear presentation, limited baselines, simpler contribution. This paper is clearly stronger. |
| tuEP424UQ5 (MORL Generalization) | 5.75 | R2 | Similar structure (framework + benchmark + evaluation). Comparable quality; this paper has a stronger conceptual framework and more impactful re-evaluation but shares the limitation of incomplete empirical validation for its central positive claim. Slightly stronger. |
| ehSQZa4vuk (Policy Confounding) | 5.25 | R2 | Interesting theoretical concept but limited to toy examples. This paper has broader empirical scope and more actionable insights. Clearly stronger. |

**Round-1 bracket**: 5.5–7.5 (clearly above the 3.67 and 4.50 directly-comparable anchors).

**Round-2 narrowing**: The paper sits above the 5.25–5.75 anchors (more empirical breadth, stronger framework) but below what a 7.0+ paper would require (the central positive claim about memory-scaling would need empirical neural baselines to reach that tier). The paper's core re-evaluation contribution is solid and well-supported; the memory-scaling argument is insightful but empirically incomplete.

**Final score: 6.0**. The paper makes a clear and valuable contribution — a careful re-evaluation that corrects the record on programmatic policy generalization, plus a useful framework and identification of a regime where programmatic representations genuinely help. The weaknesses are real but addressable; none undermine the core re-evaluation findings.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>