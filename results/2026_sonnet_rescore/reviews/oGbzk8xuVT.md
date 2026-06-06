## Summary
BuilderBench is a benchmark for evaluating generalist agents via open-ended block-building. It contributes (1) a fast MuJoCo/JAX simulator, (2) a 42-task suite curated to test distinct reasoning abilities (physics, geometry, long-horizon planning), and (3) two evaluation protocols — a multi-task self-supervised protocol and a "training-wheels" single-task supervised protocol — along with reference implementations of six algorithms. Experiments show that current RL algorithms and frontier LLMs consistently fail on non-trivial tasks, validating the benchmark's purpose of highlighting unsolved challenges.

---

## Strengths

- **Carefully designed task suite with distinct reasoning demands.** The Section 5.1 case study demonstrates this concretely: T-Block requires a non-obvious 45° rotation of the base cube for stability; Four Cube Packing is a geometric packing problem solvable only by rotating each cube before placement; Hexagonal Portal demands scaffolding, simultaneous two-cube grasping, and scaffold removal in the correct order; Leaning Tower requires counterweights and scaffold reuse; Maximum Overhang requires solving a known problem in mathematics about center-of-mass constraints. These tasks cannot be solved by memorized motor primitives.

- **Benchmark demonstrably exposes algorithm gaps.** Figure 6 shows self-supervised algorithms (SFL, MEGA) fail to achieve non-trivial success on 3-cube tasks; Figure 7 shows that even training directly on test goals yields near-zero success as cube count and task complexity increase; Figure 8 shows frontier LLMs (ChatGPT-5, Gemini 2.5 Pro) fail to produce correct high-level plans for any of the five case-study tasks. These are concrete findings that validate the benchmark's difficulty.

- **Hardware-accelerated simulator is a real practical contribution.** The paper reports a 10–100× speedup over CPU-based environments like Crafter, NetHack, and Minecraft (Section 1), making large-scale exploration experiments feasible on academic budgets.

- **Single-file reference implementations lower the barrier to entry.** The release includes implementations of PPO, SAC, CRL, RND, BRO, GNN-ATT (supervised), and SFL, MEGA, UDRL, RND (self-supervised), allowing direct benchmarking and prototyping with minimal engineering overhead.

- **Dual-protocol design provides actionable feedback loops.** The self-supervised protocol evaluates true exploration and generalization; the supervised "training-wheels" protocol enables architectural and reward-function debugging in isolation (Section 6). This separation is thoughtful for supporting a wide range of research workflows.

---

## Weaknesses

### Fatal
None.

### Major

- **Incomplete experimental coverage of the task suite.** The paper claims 42 tasks but only 12 are evaluated under the self-supervised protocol (Figure 6: cube-1: 2, cube-2: 5, cube-3: 5) and 17 under the supervised protocol (Figure 7: cube-1: 2, cube-2: 5, cube-3: 5, cube-4: 5). With possible overlap, a substantial fraction of the suite — including the most compelling tasks highlighted in Section 5.1 — are never evaluated. The Hexagonal Portal task uses 10 cubes and the Leaning Tower uses 9 cubes; neither is near the 3-cube ceiling of the self-supervised protocol or the 4-cube ceiling of the supervised protocol. For a benchmark paper, where the primary deliverable is demonstrating algorithm performance across the full suite, this is a significant gap. It leaves the difficulty curve beyond 4 cubes entirely uncharacterized, and provides no empirical upper bound to indicate how far current algorithms are from the paper's most difficult tasks.

- **Confound in the self-supervised algorithm comparison.** Section 7 explicitly states: "UDRL and RND... Both of these algorithms sample goal collection goals using MEGA." This means UDRL and RND share MEGA as a component for goal sampling and differ only in their policy update mechanisms. Figure 6 then presents MEGA substantially outperforming UDRL and RND. As written, it is impossible to determine whether the performance gap reflects MEGA's policy learning being superior or simply that MEGA-based goal sampling is the dominant factor while the distinguishing policy updates of UDRL and RND add little. The comparison fails to isolate the algorithmic contributions being evaluated.

### Minor

- **Self-supervised protocol mechanism is underspecified at the point of introduction.** Section 6 states the agent "does not receive any task specification during training" yet "learn[s] a task conditioned policy... which can take as input a state... as well as a task specification." The tension is not resolved until Section 7 (where SFL and MEGA are described as sampling autotelic goals from visited states and training via hindsight relabeling). Readers need this clarification in Section 6 itself to understand the evaluation setup and how self-supervised training produces a task-conditioned policy.

- **Validity of author-unsolvable tasks is unaddressed.** Section 5.2 states: "Tasks should include some whose solutions are unknown even to the authors." The design philosophy is reasonable for an open-ended benchmark, but raises a natural question the paper does not address: how is success condition validity established, and how would a researcher distinguish a genuine algorithm success from a false positive arising from environment quirks for these tasks? A brief acknowledgment of how these tasks are scoped or validated would strengthen this design principle.

- **LLM evaluation methodology is too limited to carry its conclusion.** Section 7.1 concludes that the results "highlight how solving our tasks requires non-obvious steps of reasoning that are beyond what current models can achieve through scaling alone." The evaluation tests only an open-loop text-plan generation on 5 tasks, with no execution feedback or iteration. The methodology does not rule out that richer prompting strategies would succeed on simpler tasks. The paper partially hedges ("this is not meant to be an extensive evaluation"), but the broad conclusion about scaling limits overreaches the evidence.

### Trivial

- **Ambiguous pronoun in Section 7.** "As seen in Figure 6, both algorithms achieve trivial performance on tasks with three cubes. MEGA is able to complete both tasks with one cube, and shows improvement on tasks with two cubes." The referent of "both algorithms" is unclear — four algorithms are in scope (SFL, MEGA, UDRL, RND) and the next sentence singles out MEGA. The sentence appears to refer specifically to UDRL and RND but should say so explicitly.

---

## Nice-to-Haves

- **A systematic task characterization table.** The Section 5.1 case study is the paper's most compelling section. Extending its analysis to all 42 tasks — mapping each to required reasoning primitives, cube count, human-solvability, and whether any tested algorithm achieves non-zero success — would make the task suite substantially more usable for future researchers and clarify the benchmark's coverage of the skill space.

- **Human teleoperation or oracle baseline.** The paper mentions that human solutions are available via scripts (Section 5.2). Including even a handful of human-performance data points (e.g., as horizontal reference lines in Figure 7) would calibrate how far current algorithms are from human-level performance and confirm that all reported tasks are achievable within the action space.

- **Extended self-supervised evaluation to higher cube counts.** The self-supervised protocol tops out at 3 cubes in experiments. Even a single result at 4–5 cubes — even if all algorithms fail completely — would strengthen the argument that the benchmark difficulty curve is well-calibrated and that the self-supervised protocol presents genuine challenge beyond what the supervised protocol covers.

- **Clarify the task specification padding/masking scheme.** Section 6 specifies task specifications as R^{34}, while Section 4 defines them as R^{3k} with k ≤ n. It is unclear how padding or masking is applied when k < k_max, and whether goal-conditioned algorithms need to account for this. A sentence of clarification would improve transparency about training mechanics.

---

## Removed Points
*These points are flagged to be removed, treat them with caution.*

- **"There is not much that can be learned in the current generation of interactive benchmarks" is too broad (harsh critic).** This was flagged as overclaiming relative to NetHack, StarCraft, Minecraft. The paper's actual point — that existing benchmarks limit the *diversity* of evaluable behaviors — is well-supported. The quote is imprecise but contextually understandable, and the surrounding paragraph makes the narrower, defensible claim. Not a substantive weakness.

- **R^34 implies an unexplained fixed maximum task complexity (harsh critic).** While worth a clarifying sentence (moved to Nice-to-Haves), this is not a methodological flaw — the design choice is consistent with the benchmark's scope and does not affect validity of reported results.

- **Strength: "addresses an important problem" (generic).** Removed per filtering discipline; no concrete, paper-specific content.

---

## Novel Insights

The most genuinely novel insight surfaced by the review is the structural claim in Section 5.1: that a remarkably small number of physical blocks (3–10) is sufficient to generate tasks requiring distinct, non-composable reasoning capabilities — from packing geometry to center-of-mass physics to temporally constrained multi-object manipulation. This "atomic unit" framing argues that block count is a meaningful axis for scaling benchmark difficulty in a way that is both mathematically principled (Maximum Overhang Problem) and practically verifiable. The implication — that agents cannot generalize across these tasks through simple interpolation or skill reuse — is a testable hypothesis the benchmark is well-positioned to investigate, even though current experiments only scratch its surface.

---

## Suggestions

1. **Extend experiments to cover the full 42-task suite.** At minimum, include normalized return for every task in a summary figure (even if most algorithms score zero). This is the central deliverable of a benchmark paper.
2. **Add an ablation isolating MEGA's goal-sampling contribution.** Run UDRL and RND with a random or uniform goal sampler alongside the MEGA-based version. This would make the Figure 6 comparison scientifically meaningful.
3. **Move the mechanism explanation from Section 7 to Section 6.** The Section 6 protocol description should explain how a task-conditioned policy is produced from self-supervised training — even in one paragraph — before Section 7 gives the experimental details.
4. **Scope down the LLM conclusion.** Replace "beyond what current models can achieve through scaling alone" with a narrower, protocol-specific claim (e.g., "current open-loop LLM planning fails on these five tasks"), reserving broader conclusions for future work with iterative prompting.
5. **Add validity notes for author-unsolvable tasks.** A brief note on how success conditions for these tasks were chosen and what a false-positive result would look like would make the design principle scientifically operational.

---

## Score and Decision

**Originality:** The block-building formulation is novel as a benchmark axis for generalist agents; the insight that a handful of blocks generates compositionally distinct reasoning tasks is genuinely creative. The individual components (MuJoCo physics, goal-conditioned RL, hindsight relabeling) are standard, but their combination and curation are original. **4/5**

**Importance:** Open-ended exploration and generalization benchmarking is a recognized bottleneck. A fast, reproducible, open-source benchmark with well-curated tasks genuinely serves the community. **4/5**

**Claims supported:** The core claim — that current algorithms fail on the task suite — is well-supported by Figures 6 and 7. The subsidiary claim about LLMs is supported but with a methodology too narrow for the stated conclusion. The claim that the full 42-task suite is benchmarked is not supported. **3/5**

**Soundness:** The environment and task design are sound; the experimental methodology has a real confound in the self-supervised comparison and leaves most of the suite unevaluated. **3/5**

**Clarity:** Section 5.1 is excellent. Section 6 has a significant explanatory gap in the self-supervised protocol. Figure 6 discussion has ambiguous pronouns. **3/5**

**Community value:** Fast open-source simulator, six reference algorithm implementations, and a publicly curated 42-task suite with clear design philosophy are high-value contributions for the RL and open-ended learning communities. **4/5**

The paper has a solid, genuine contribution — the benchmark environment and task suite — but the primary empirical deliverable (algorithm coverage of the task suite) is substantially incomplete, and the self-supervised comparison has a methodological confound. These are fixable gaps, not fatal flaws; the foundation is strong and the research direction is important. Current state is borderline-accept: the paper is valuable but needs revision before it is fully usable as a benchmark.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>