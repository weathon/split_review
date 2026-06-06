Now I have a clear picture from the calibration anchors. Let me compile the final review.

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Do Symbolic or Black-Box Representations Generalise Better (MpA6HMD7Wq) | 3.00 | R1 | Our paper has more systematic experiments, better baselines, and cleaner methodology. Clearly better. |
| State Combinatorial Generalization (PH7ja3T0vN) | 4.50 | R2 | Our paper has more robust empirical work and better baselines. Better. |
| On the Expressivity of Objective-Specification Formalisms (qr4ECbGcSj) | 4.50 | R1 | Both have conceptual frameworks; ours has more substantial empirical work, theirs has more rigorous theory. Slightly better. |
| Bad Habits: Policy Confounding (ehSQZa4vuk) | 5.25 | R2 | Comparable — both introduce a conceptual lens and validate empirically on limited domains. Our empirical scope is broader but the FUNSEARCH POC is thinner. |
| How the Level Sampling Process impacts ZSG (X1p0eNzTGH) | 5.67 | R2 | Their work has a novel method (SSED) with strong results; ours re-evaluates existing methods. Slightly below. |
| Bridging State and History Representations (ms0VgzSGF2) | 6.75 | R1 | Their work has more thorough theoretical proofs and cleaner empirical validation. Clearly below. |
| DeepLTL (9pW2J49flQ) | 8.00 | R1 | Strong theoretical and empirical contributions. Not comparable; clearly below. |

**Bracket from Round 1:** 4.0–6.0  
**Narrowed from Round 2:** 5.0–5.5  
**Final score:** 5.0 — comparable to Bad Habits, with more systematic empirical work offset by the thin FUNSEARCH POC and TORCS attrition issues. Reject with merit.

Now let me write the final review.

---

## Summary
This paper re-evaluates three prior benchmarks (TORCS, KAREL, PARKING) where programmatic policies were reported to generalize OOD better than neural ones. Through controlled modifications—reward downweighting in TORCS, partial observability with action-augmented input in KAREL, and matched evaluation in PARKING—the authors show neural policies can match or approach programmatic generalization. The paper introduces an expressivity–discoverability framework and argues that instance-scaling working memory (as in general pathfinding and nested subproblems) is the structural boundary where fixed-capacity neural architectures are provably inexpressive while programmatic representations are not, supported by a brief FUNSEARCH proof-of-concept.

## Strengths
- The three-benchmark re-evaluation is systematic and identifies specific controllable factors in each domain. In TORCS (Section 4.1), reducing the speed-weighting coefficient β from 1.0 to 0.5 allows DDPG-trained policies to generalize OOD (76% from G-TRACK-1 to G-TRACK-2, Table 1). In KAREL (Section 4.2, Table 2), a feedforward network with sparse local observations and the previous action a_{t-1} achieves 1.00 average return on 100×100 grids across four tasks, matching LEAPS programmatic results—a striking result that cleanly demonstrates the original gap was a discoverability artifact.
- The expressivity–discoverability framework (Definitions 2–3, Section 5) provides a clean conceptual vocabulary for analyzing when and why representation–search combinations succeed or fail at OOD generalization, and is productively applied across all three experimental domains.
- The instance-scaling memory argument (Section 5) identifies a principled boundary: fixed-capacity neural architectures cannot encode algorithms whose working memory grows with input size (pathfinding requires Ω(log|V|) bits for vertex indexing; BFS requires Θ(|V|) working memory), making them structurally inexpressive for these problem classes while programmatic representations can dynamically allocate memory.
- The paper shows intellectual honesty in reporting PARKING results (Section 4.3), where neither representation reliably generalizes, and acknowledges mixed evidence rather than spinning results.

## Weaknesses

### Fatal
None.

### Major
- **Attrition in TORCS undermines the practical "neural policies can match" claim.** Only 13/30 seeds (43%) learned to complete G-TRACK-1, and only 4/15 (27%) learned AALBORG. The generalization fractions (0.76, 0.69, 1.00, 1.00) are computed over these subsets. Computed over all trained models, roughly 33% of G-TRACK-1 models generalize to G-TRACK-2 versus NDPS's 100% (3/3). The paper's headline claim should be tempered by this high training failure rate, which is not discussed. If only a minority of runs succeed even on the training distribution, "neural policies can match in principle" is meaningfully different from "neural policies are a reliable alternative."
- **The FUNSEARCH proof-of-concept (Section 5) is far too thin to serve as evidence for the paper's central constructive claim.** The entire experimental description occupies a single sentence: "Three runs of FUNSEARCH returned a correct implementation of breadth-first search, which generalizes to any pathfinding problem." There is no description of problem presentation to FUNSEARCH, the prompt or interface used, search configuration, what the synthesized programs look like, how many runs failed, computational cost, or any neural baseline on the same SparseMaze problem. The claim that the synthesized BFS "provably generalizes OOD" is asserted without demonstration—the synthesized program is not shown, no proof sketch is provided, and no evaluation beyond assertion is given. A proof-of-concept at this level of detail cannot anchor the paper's thesis about when programmatic representations are necessary.

### Minor
- **TORCS lap times lack variance reporting.** Table 1 reports only averages across models. Standard deviations or confidence intervals should be provided, especially given the small number of successful seeds (13 for G-TRACK-1, 4 for AALBORG).
- **The two halves of the paper are not well integrated.** Sections 1–4 argue prior programmatic advantages were confounds; Section 5 argues programmatic representations DO have genuine advantages for instance-scaling memory problems. While not contradictory, the paper does not reconcile these framings or use its own expressivity–discoverability framework to systematically re-analyze the original results from Section 4.
- **HARVESTER trade-off is not discussed.** PPO with a_{t-1} achieves only 0.59 on small grids and 0.04 on 100×100 for HARVESTER, while PPO with ConvNet achieves 0.90 on small grids (Table 2). The partial-observability fix that enables OOD generalization on four tasks substantially hurts in-distribution performance on HARVESTER, which goes unacknowledged.
- **The claim that adjusting intrinsic reward "proved discoverability" (lines 284–288) is overstated.** Finding some generalizing solutions (with a 43% training success rate on G-TRACK-1) does not constitute proof of discoverability under Definition 3, which requires an algorithm that returns a generalizing policy within bounded time.
- **Section 6 speculates about other papers (Cui et al., 2024; Guo et al., 2023; Qiu & Zhu, 2022) without re-evaluating them.** While the speculation is plausible and the paper acknowledges it needs investigation, this section reads more like a position statement than an empirically grounded discussion.
- **The NDPS baseline uses only 3 seeds** (inherited from Verma et al., 2018), limiting the statistical robustness of the comparison in Table 1.

### Trivial
- The expressivity argument that "the TORCS DSL space resembles that of ReLU networks" (line 284) is gestured at rather than rigorously argued—the paper cites Orfanos & Lelis (2023) but does not develop the connection.
- The grammar semantics of `fold` in Figure 1(a) are not fully specified (how many steps of history?), though this is inherited from the original papers.

## Nice-to-Haves
- Apply the expressivity–discoverability framework systematically to each re-evaluated domain: explicitly analyze whether both representations are expressive, what caused discoverability failures for original neural baselines, and how the modifications addressed discoverability. This would unify the paper's two halves.
- Either substantially expand the FUNSEARCH experiment (setup details, synthesized programs, failure analysis, neural baseline comparison) or reduce its prominence and let the conceptual argument in Section 5 stand on its own reasoning.
- Discuss the practical implications of high training attrition in TORCS—if only a minority of runs succeed even on the training distribution, "can match in principle" is different from "are a reliable alternative."

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "The experimental confounds are not confounds — they are changes to the problem definition."** REMOVED as a standalone fatal claim. While there is a genuine framing tension worth noting (the TORCS reward β change does modify what the agent optimizes for), the paper explicitly defends this (line 209–210): evaluation is on lap time and crashes, not the training reward. In KAREL, the programmatic policies always had partial observability through their DSL perception functions (Figure 2a); the paper's fix gives neural policies the same observation regime, which is a legitimate confound control. The HC's framing of this as catastrophic is an overstatement. The legitimate concern is preserved as a minor framing issue above.
- **Harsh Critic: KAREL intervention "changes the information available to the agent — partial observability forces the agent to learn local heuristics."** REMOVED. This misreads the paper: the LEAPS DSL always used partial observability. The paper's neural baselines receive the SAME partial information. This is a confound fix, not a problem change.
- **Harsh Critic: "the paper does not report hyperparameter search budgets, architecture details, or training curves."** Partially REMOVED. While some architectural detail is genuinely sparse, the harsh critic's framing as a fatal confound claim about "undertuned baselines" is speculative. The core experimental results are sufficiently described for the claims made.
- **Harsh Critic: mentions about parser not extracting figures, missing appendix, missing proofs in appendix.** REMOVED per hard rules. These are parser artifacts; figures and appendices exist in the original submission.
- **Harsh Critic: "The reproducibility statement... is standard but provides no immediate verification path."** REMOVED per hard rules (questions availability of cited artifacts).
- **Harsh Critic: "NDPS and PROPEL would not generalize... is speculative and untestable."** Partially REMOVED. The paper explicitly flags this as conjecture ("We conjecture that...", line 272). Calling a self-acknowledged conjecture "speculative" adds nothing.
- **Strength Finder: "Proof-of-concept: FUNSEARCH synthesizes provably generalizing BFS" as a core strength.** REMOVED. The experiment is one sentence long with zero supporting detail; it cannot serve as evidence for the paper's claims.
- **Strength Finder: "Self-contained formal problem definition with concrete grounding."** REMOVED as a standalone major strength. The formalism is competent but standard; this is table-stakes, not a distinctive contribution.

## Novel Insights
The paper's reframing of the neural-vs-programmatic generalization debate in terms of expressivity and discoverability, and the specific identification of instance-scaling working memory as the expressivity boundary, is a genuinely productive lens. Prior work largely treated programmatic generalization advantages as an empirical given; this paper offers a structural explanation for when and why those advantages are real (memory-scaling problems) versus artifactual (discoverability confounds in constant-memory domains). The observation that the original TORCS, KAREL, and PARKING benchmarks all fall into the constant-memory regime—and thus probe discoverability rather than expressivity—is a useful meta-insight that recontextualizes the existing literature.

## Suggestions
- Reframe the abstract and introduction to more accurately reflect what the experiments show: the re-evaluation demonstrates that neural policies CAN achieve OOD generalization in these domains when discoverability factors (reward design, observation sparsity, architecture simplicity) are controlled, rather than claiming the original results were "confounds" in a way that implies they were mistakes. The discoverability gap between search procedures is itself a genuine phenomenon worth studying.
- Explicitly discuss the TORCS training attrition and its implications. Either tune training to reduce the failure rate, or honestly discuss what it means that most neural training runs fail on the training distribution even with the β=0.5 fix.
- For the FUNSEARCH experiment: provide the problem specification, prompt/interface, synthesized BFS code, number of runs attempted vs. succeeded, computational cost, and ideally a neural baseline that fails on the same SparseMaze problem. Without these details the proof-of-concept carries negligible evidentiary weight.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>