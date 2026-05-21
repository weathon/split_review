---
job_id: 4c48a249-2933-4903-b7de-f8168b7711ee
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: e26MPyczN9.pdf
paper: Do Programmatic Policies Really Generalize Better? A Re-Evaluation Study
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, centered on reinforcement learning, OOD generalization, benchmarking, and neurosymbolic/programmatic policy representations.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components for a re-evaluation/positioning-style ML submission, including Abstract, Introduction, background/method sections, experiments with quantitative results, discussion, relation to prior work, and conclusion; while I have significant concerns about the strength of the contribution and some methodological choices, these do not rise to desk-reject level.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper re-examines claims that programmatic policies generalize better than neural policies in RL. Across TORCS, Karel, and Parking, the authors argue that much of the previously reported OOD generalization gap can be explained by experimental confounds, and they show that modified neural training pipelines, such as safer rewards in TORCS and sparser observations in Karel, can substantially narrow or remove the gap. The paper then proposes an expressivity/discoverability framing and argues that programmatic policies retain an inherent advantage on tasks whose solutions require working memory that grows with input size, illustrated with a modified Karel maze where FunSearch synthesizes a breadth-first-search style program.

## Strengths
The paper tackles an important and timely question. There has been a growing narrative that programmatic policies generalize better than neural ones, and this submission usefully pushes back on overly broad versions of that claim. A careful negative result or re-evaluation can be very valuable when a literature risks drawing the wrong lesson from benchmark outcomes.

The expressivity versus discoverability distinction in Section 5 is a useful organizing lens. Even though the formulation is somewhat high level, it gives a clearer vocabulary for separating representational limitations from optimization/search effects. That framing does help make sense of the three case studies.

The empirical sections do contain some genuinely interesting observations. In TORCS, the central point is not merely that reward shaping changes performance, but that it changes the apparent generalization ranking between representations. Table 1 supports that point rather directly: under the original reward, DRL with $\beta=1.0$ crashes on all OOD tracks, whereas under the cautious reward $\beta=0.5$, a substantial fraction of successful seeds transfer, and on Aalborg all successful seeds transfer to both OOD tracks. Even if I have concerns about fairness and selection effects, the table does illustrate that the earlier “programs generalize, neural nets do not” story is not robust to training choices.

The Karel results are also provocative. Table 2 shows that “PPO with $a_{t-1}$” matches or exceeds LEAPS on four tasks, including perfect transfer on STAIRCLIMBER, MAZE, TOPOFF, and FOURCORNER, whereas the fully observable ConvNet baseline collapses on large grids. That is a concrete and useful reminder that representation comparisons can be badly confounded by observation design.

Some figures do help the paper communicate its argument. Figure 3 is simple but effective: it makes the partial observability issue in Karel concrete by showing two different states with the same local observation, which motivates augmenting the observation with the previous action. Figure 7 is also relevant to the final claim because it visually clarifies why the proposed sparse/wide maze is intended to defeat constant-memory wall-following heuristics, making the motivation for the BFS-style solution more understandable.

The paper is generally readable, and the high-level story is easy to follow. For a paper spanning three prior benchmark families plus a more conceptual final section, the narrative is reasonably coherent.

## Weaknesses
1. **The main positive claim is much less convincingly established than the re-evaluation claim.**  
   The paper’s first half, re-evaluating prior benchmark conclusions, is the strongest part. The second half, especially Section 5, aims to answer the deeper question of when programmatic representations have an inherent OOD advantage. That answer is stated quite strongly, namely that tasks requiring working memory that grows with input size are not expressive for the commonly used neural architectures considered here, while programmatic representations can encode such solutions. However, the paper does not empirically test this claim against strong neural alternatives in a controlled way. The only direct positive evidence is a proof-of-concept FunSearch synthesis on a modified Karel maze, described on Pages 9 to 10 and supported by Figure 7 and the appendix listing. This is too thin to support the broader representational claim being made. As written, the paper moves from “we found confounds in prior benchmarks” to “here is the type of task where programs really win” without enough middle ground.

2. **The experimental comparisons are often not apples-to-apples, especially in Karel, and the changes introduced alter the problem structure rather than only improving discoverability.**  
   In Section 4.2, the authors compare fully observable ConvNet PPO, partially observable LSTM PPO, LEAPS with the DSL in Figure 2, and a new baseline “PPO with $a_{t-1}$”. But these are not just different representations with a matched information interface. The paper explicitly changes the observation design and argues that “having access to less information allows the agent to generalize” (Page 4) and later that providing fewer features helps avoid spurious correlations (Page 8). That may be true, but then the comparison is no longer a clean representation comparison. The partial observability itself imposes a strong inductive bias toward local heuristics. This matters a lot because the central conclusion of the paper is about representation, not just about what information should be exposed to the learner. Table 2 is interesting, but it also reflects that the authors changed both the information available and the model. In other words, the paper sometimes treats “representation”, “observation function”, and “training objective” as interchangeable levers, which muddies the conclusions.

3. **The TORCS evidence relies on heavy seed filtering and therefore does not cleanly support the claim that neural policies “match” programmatic policies in OOD generalization.**  
   Table 1 and the discussion on Page 6 reveal an important caveat: for DRL with $\beta=0.5$, the authors trained 30 seeds on G-Track-1 and only 13 learned to complete the training track; for Aalborg, only 4 out of 15 learned to complete the training track, and only those successful seeds were evaluated OOD. This is a serious issue for the strength of the conclusion. If the claim is about OOD generalization of a representation-search pair, then low training success is part of discoverability, not something that can simply be conditioned away. Conditioning OOD evaluation on already-successful seeds substantially changes the interpretation. Indeed, the paper itself emphasizes discoverability as one of its two core criteria, but then the reported OOD numbers in Table 1 partially sidestep poor discoverability by evaluating only seeds that first solved the training problem. The result then shows existence of some generalizing neural policies, not parity of neural and programmatic approaches in practical learnability.

4. **The Parking section does not convincingly support any strong conclusion, yet it is used rhetorically as if it points toward representation-distinguishing benchmarks.**  
   Table 3 is mixed at best. PSM has better “Successful-on-100” than DQN on the test set, but DQN has a slightly higher raw test success rate (0.18 vs 0.16). The paper acknowledges this ambiguity on Page 8, but then Page 8 to 9 still leans on Parking as indicating a direction for future benchmarks that might distinguish representations. I found this over-interpreted. The more direct reading is that both approaches struggle and that the benchmark, under the reward and discretization choices here, is unstable and not yet diagnostic. This matters because one of the paper’s selling points is to disentangle representational factors from confounds; in Parking, the disentanglement seems unresolved.

5. **Several mathematical definitions and claims are imprecise or internally awkward, which weakens the technical framing.**  
   On Page 2, the POMDP is defined as $\mathcal{M}=(S,A,O,p,\Omega,r,\mu,\gamma)$ with reward written as $R_{t+1}=r(o_t,a_t)$ and policy as $\pi:O\times A\rightarrow [0,1]$. This notation is nonstandard and somewhat confusing. Usually one writes either $\pi(a \mid o)$ or $\pi:O \to \Delta(A)$. As written, the policy “returns the probability of taking action $a$ at observation $o$,” which is fine semantically, but the function type obscures that the output should sum to one over $a \in A$ for each $o$. Likewise, the reward is defined from observations and actions only, while the transition is defined on states. None of this is fatal, but it makes the formal setup looser than it should be for a paper that later leans on formal notions like expressivity and discoverability.  
   There is a more substantive issue in **Definition 1** on Page 3. It says a policy generalizes OOD if it is found from $X_{\text{train}} \subset X$ and then “also solves $F(x')$ for any $x' \in X$.” This is effectively a universal quantification over the full problem class. That is an extremely strong notion, much stronger than benchmark OOD generalization as usually measured, and it is not consistently respected later when the empirical sections estimate generalization on finite test sets. If this is intended as an idealized notion, the paper should clearly separate “provable universal generalization over $X$” from “empirical transfer to sampled test instances.” Right now the same term is doing too much work.  
   Definition 3 for discoverability is also too permissive to be very informative: “there exists an algorithm” that returns a generalizing policy “within a bounded time limit.” Bounded by what, as a function of what, and under what access model to $(X,F)$? Without specifying dependence on input size, training set size, or evaluation budget, the definition risks being tautological. A more useful formalization would state something like: for a family $\{(X_n,F_n)\}_{n\ge 1}$, a search procedure $\mathcal{A}$ returns $\pi_n \in \Pi_n$ that generalizes over $X_n$ within time polynomial in a natural size parameter. As written, the concept is intuitively appealing but mathematically too underspecified to bear much argumentative weight.

6. **The key representational argument in Section 5 is asserted at a high level, but not proved in the form needed for the paper’s claims.**  
   The argument around Pages 9 to 10 is that fixed-capacity feedforward and recurrent policies cannot encode algorithms whose working memory grows with input size, such as exact pathfinding or arbitrarily nested subproblems. The intuition is sensible, but the paper often slides between “cannot guarantee exact generalization in the worst case,” “cannot represent instance-growing data structures,” and “are not expressive for the problem class.” These are related, but not identical claims. For example, saying that breadth-first search uses $\Theta(|\mathcal{V}|)$ memory does not by itself prove that no fixed-dimensional recurrent policy can solve the particular POMDP family under the chosen observation interface, unless the family and success criterion are formalized carefully. The paragraph invoking $\Omega(\log |\mathcal{V}|)$ bits to index a vertex is suggestive, but it is not a theorem about the policy classes actually studied. Given how central this section is to the claimed answer of the paper, it needed either a formal impossibility result or a much more measured statement.

7. **The proof-of-concept with FunSearch is not integrated into the paper with enough rigor to support the “provably generalizes OOD” language.**  
   On Page 9 the authors state that FunSearch synthesizes “an implementation of breadth-first search that provably generalizes OOD.” But in the main paper, there is no proof, only the claim that three runs returned a correct BFS implementation. The appendix listing on Pages 16 to 19 indeed resembles BFS, but even there the code is presented informally and contains several apparent transcription issues, for example `convert_path_to ACTIONS` versus `convert_path_to_actions`, `actions extend([1, 1])`, and `visited = set((start_r, start_c))`, which would be incorrect Python if taken literally. I understand that formatting artifacts can happen in listings, but that is exactly why strong claims like “provably generalizes” should not depend on readers reverse-engineering a code snippet. If the claim is that the synthesized policy is extensionally equivalent to BFS on the task family, then that equivalence should be stated and justified in the main paper, not implied through a listing.

8. **The paper sometimes overstates equivalence between programmatic spaces and neural spaces without sufficient qualification.**  
   On Page 8, the paper says the TORCS DSL space resembles that of ReLU networks and that the ReLU space can be made a superset of the TORCS language by exposing `peek` and `fold` as inputs and increasing the number of neurons. This is plausible as an approximation argument, but it is presented too casually. Once hand-crafted temporal summary operators like `fold` are provided as network inputs, much of the algorithmic burden has already been shifted into feature engineering. That substantially changes what is being attributed to the neural representation. A similar issue appears in Section 6 when the paper argues that symbolic equations or if-then-else chains can be represented by standard neural networks if the right primitives/options are exposed. Maybe, but then the meaningful unit of comparison is no longer “programs vs neural networks” in any clean sense. The paper needs more care about what is part of the representation and what is part of the interface.

9. **Some figures and tables expose limitations that the text underplays.**  
   Figure 5, the example PSM state machine on Page 14, actually undercuts part of the paper’s rhetorical contrast between programs and neural policies, because it shows a fairly small, finite control structure driven by a handful of threshold predicates. That kind of policy is exactly the sort of behavior a recurrent or history-augmented reactive neural policy might plausibly emulate on a bounded domain. The text eventually acknowledges this on Page 8, but the earlier framing sometimes sounds stronger than the evidence warrants.  
   Likewise, Figure 8 and Figure 10 in the appendix, while supplementary, visually reinforce an important caveat: the learning process is unstable, especially in TORCS where the reported means are over only successful seeds. That instability is not just a nuisance, it is central to the paper’s own discoverability thesis and should be reflected more directly in the main-paper conclusions.

10. **Positioning relative to related work is incomplete for a paper that is primarily a re-evaluation and conceptual reframing.**  
   The paper cites the earlier programmatic-policy works it re-evaluates, and it cites one recent paper by Carvalho et al. (2024) in the references, but the relationship to that line of work is underdeveloped in the main text. For a submission whose main value lies in reinterpreting prior empirical claims and clarifying what source of generalization is actually being tested, this positioning needs to be sharper. As written, some of the paper’s most interesting claims risk sounding less differentiated than they should.

## Questions
1. **TORCS evaluation and seed filtering:** In Table 1, why is OOD evaluation for DRL $(\beta=0.5)$ conditioned on the subset of seeds that first solved the training track? Could the authors also report unconditional OOD success over all trained seeds, for example treating failure to solve the training track as failure of the full representation-plus-search pipeline? This would better align the experiments with the paper’s own discoverability framing.

2. **Karel fairness of comparison:** Can the authors provide a cleaner matched-information comparison in Section 4.2? For example, compare LEAPS, PPO+MLP+$a_{t-1}$, and PPO+LSTM under the same local observation interface, and separately compare all methods under the same fully observable interface. Right now Table 2 mixes representation effects with observation-design effects.

3. **Formalization of Section 5:** Could the authors sharpen Definitions 2 and 3 and more carefully distinguish:  
   (a) empirical transfer to sampled test instances,  
   (b) exact universal generalization over a problem class, and  
   (c) representability/impossibility results for a policy family?  
   My confidence in the core conceptual contribution would increase if the paper stated these distinctions explicitly.

4. **Pathfinding impossibility claim:** Do the authors have a formal theorem for the claim on Pages 9 to 10 that the evaluated fixed-capacity neural policies are not expressive for general pathfinding families? If not, can they weaken the statement to a more clearly scoped claim, such as inability to guarantee exact OOD generalization over families whose required working memory grows with instance size?

5. **FunSearch proof-of-concept:** What exactly is meant by “provably generalizes OOD” on Page 9? Is the claim that the synthesized program is verified to implement BFS, or only that one can inspect the returned program and recognize BFS? A concise proof sketch in the main paper would help. Also, please clean up the listing inconsistencies in Appendix E, because in its current form the code is difficult to treat as technical evidence.

6. **Parking conclusions:** Given the mixed outcomes in Table 3, what concrete conclusion do the authors want readers to take from Parking? If the benchmark remains inconclusive, I would prefer the paper to say that more bluntly.

7. **Role of engineered primitives:** In arguments such as the TORCS discussion on Page 8, how do the authors separate representational expressivity from feature engineering? If a neural policy is granted `peek`/`fold`-style summaries or previous-action augmentation, what remains of the intended representation comparison?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns stood out from the submission. The paper is a methodological and empirical study of RL representations and benchmarks, and I did not identify specific issues requiring formal ethics escalation based on the provided text.

## Soundness Rating
2: fair. The empirical re-evaluation contains useful evidence, but several conclusions are stronger than what the experiments and formal arguments fully support, especially in Section 5.

## Presentation Rating
2: fair. The paper is readable overall, but the formal definitions are imprecise, some claims are overstated, and important caveats are not always integrated cleanly into the main narrative.

## Contribution Rating
2: fair. The re-evaluation angle is worthwhile, but the strongest positive claim, namely a principled account of when programmatic policies inherently generalize better, is not established with enough rigor or breadth to rise to a stronger contribution score.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper raises an important corrective point and contains some useful benchmark observations, especially in TORCS and Karel, but the evidence is not yet strong enough for the broader conceptual conclusion it wants to claim. I found the re-evaluation more convincing than the proposed answer to the deeper representation question.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The paper is close to my area, I checked the main technical and empirical claims carefully, and my uncertainty is mostly about how much credit to assign to the re-evaluation contribution versus the underdeveloped formal claims.