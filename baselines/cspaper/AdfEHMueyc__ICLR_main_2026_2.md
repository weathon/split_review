---
job_id: 08fdbe62-10b0-423c-b794-6e8d60b2dedb
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: AdfEHMueyc.pdf
paper: Evolving Embodied Intelligence: Graph Neural Network-Driven Co-Design of Morphology and Control in Soft Robotics
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining reinforcement learning, learning on graphs, transfer/inheritance across morphologies, and robotics co-design.

## Minimum Quality
Pass ✅. The paper contains the expected scientific sections, presents a coherent method and experiments, and is understandable at a high level, although there are substantial concerns about novelty, rigor, and experimental support that affect the review score rather than triggering desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-directed instructions, or other manipulative content in the provided manuscript text and figures.

# Expected Review Outcome:
## Summary
This paper studies co-design of soft robot morphology and control in EvoGym using graph-based policies. The main idea is to represent each robot as a graph over position sensors, use a GAT encoder plus an MLP head for actor and critic, and transfer controller parameters across generations with a topology-consistent mapping that reuses shared GAT and MLP layers while remapping actuator outputs. Experiments on four EvoGym tasks compare two GAT variants against MLP-based inherited and non-inherited baselines, with claims of better final fitness and improved robustness to morphology changes.

## Strengths
The paper tackles a real pain point in evolutionary co-design, namely that morphology mutations break the fixed input-output assumptions of standard MLP controllers and make inheritance brittle. Framing controller transfer as a graph-structured policy problem is reasonable and well matched to modular soft robots.

The core idea is easy to understand from **Figure 1** on **Page 2**. The parent-to-child transfer picture makes the intended inheritance mechanism concrete, especially the notion that shared graph-processing layers survive morphology changes while actuator-specific outputs are selectively copied or reinitialized. Even though the method is underspecified in places, the high-level intuition is communicated effectively there.

The experimental setup includes several tasks of differing difficulty, rather than a single cherry-picked environment. Evaluating on Pusher-v1, Thrower-v0, Carrier-v1, and Catcher-v0 is a better design choice than demonstrating the method on only one locomotion task.

The comparison against both an inherited MLP baseline and a from-scratch GA+PPO baseline is directionally appropriate. In particular, **Figure 3** on **Page 6** does suggest that inheritance itself matters, and that the proposed GAT variants can sometimes maintain stronger best-so-far fitness trajectories than the MLP baselines.

The paper also provides qualitative rollouts and morphology snapshots. **Figure 4** on **Page 7** and **Figure 5** on **Page 8** at least attempt to connect quantitative trends to behavioral differences and evolved structures, which is useful in embodied AI papers where raw scalar reward often hides what the robots are actually doing.

## Weaknesses
1. **The novelty is limited and the paper does not convincingly establish what is actually new relative to prior graph-based morphology-aware control.**  
   The paper positions itself against fixed-input MLP inheritance, but its technical recipe, graph controller + evolutionary co-design + parameter transfer, feels much closer to a straightforward adaptation of existing graph-policy ideas to EvoGym than the paper acknowledges. The related work on **Page 9** cites NerveNet and Kurin et al., which is good, but the paper still overstates the conceptual gap. What seems new here is not a fundamentally new controller class, but a practical inheritance rule for EvoGym-style morphology mutation. That can still be publishable if the empirical evidence is strong, but then the burden shifts to experiments, and those are not strong enough. As written, the contribution reads as an incremental combination of GAT, PPO, and Lamarckian inheritance rather than a clearly differentiated ICLR-level advance.

2. **The method is under-specified at the mathematical and algorithmic level, to the point that reproduction and technical assessment are difficult.**  
   This is my biggest soundness issue. Section 3 defines a graph \(G=(V,E)\) and mentions node features, edge offsets \((\Delta x,\Delta y)\), one GAT layer, averaging over nodes, and an MLP head, but many core details are missing. For example:
   - What is the exact node feature vector for the "global" and "local" variants? The text on **Pages 3-5** says global properties and local information are combined, but the full feature dimensionality and composition are never explicitly defined.
   - How are edge features incorporated into the GAT? Standard GAT does not directly consume edge features unless modified. The paper says edge features are extended with relative offsets on **Page 5**, but does not give the modified attention score function, e.g. whether attention is of the form  
     \[
     \alpha_{ij} \propto \exp\big(a^\top [W h_i \,\|\, W h_j \,\|\, e_{ij}]\big)
     \]
     or something else entirely.
   - The actor output is described as pooled graph representation followed by an MLP head that maps to actuator commands. But if the representation is globally pooled before the output layer, in what sense is the controller structurally local or per-actuator beyond output remapping? This is especially confusing given the narrative that GNNs let actuators "act locally" through message passing on **Page 4**.
   - No PPO objective is given, nor any training details specific to inheritance, such as whether learning rates, clipping, entropy coefficient, rollout length, or fine-tuning budget differ between newborns and inherited offspring.
   
   These omissions matter because the paper’s main claim is not just that graphs are a nice representation, but that the specific inheritance mechanism and GAT design preserve useful policy structure across changing bodies. Without a precise formulation, it is hard to know whether the gains come from graph inductive bias, from weight reuse, from output-head surgery, or from some unreported engineering choice.

3. **Algorithm 2 contains concrete inconsistencies and ambiguities that weaken confidence in the implementation and the claimed transfer mechanism.**  
   On **Page 4**, line 16 of **Algorithm 1** reads  
   \[
   (\theta_k^{act}, \theta_k^{ct}) \leftarrow \text{MAPWEIGHTS}(\theta_u^{act}, \theta_u^{act}, G_u, G_k),
   \]
   which appears to pass \(\theta_u^{act}\) twice instead of actor and critic weights separately. That may be a typo, but it is not a minor cosmetic issue, because the whole paper’s contribution revolves around inheritance rules.

   **Algorithm 2** has a more serious problem: line 10 says "Copy shared GAT layers from \(\theta_u^{act}\) to \(\theta_k^{ct}\)" rather than from the parent critic to the child critic. If intentional, this should be justified; if unintentional, it suggests the pseudocode was not carefully checked. The critic is also described as inheriting "in the same way" on **Page 5**, but whether actor and critic share an encoder, are trained jointly, or are separate networks is never clearly specified. Since critic inheritance materially affects PPO stability, this is not a trivial editorial slip.

4. **The experimental evidence is too thin for the central claims about robustness, transfer efficiency, and generalization.**  
   The paper’s main empirical figure is **Figure 3** on **Page 6**, which plots the best fitness in the population across generations, averaged over only three runs. This is a very weak summary statistic for a co-design paper. Best-so-far curves can hide instability, dependence on lucky mutations, and differences in compute. They also do not directly measure whether controller inheritance improved sample efficiency per offspring or reduced retraining cost, even though that is one of the paper’s lead motivations in the abstract and introduction.

   More concretely, I would have expected at least some of the following:
   - average and median population fitness, not only top individual fitness,
   - explicit adaptation curves after mutation for parent-to-child transfer,
   - number of PPO updates or environment steps needed for offspring to recover pre-mutation performance,
   - ablations isolating graph structure from inheritance, such as GAT without transfer,
   - sensitivity to mutation magnitude, since the paper claims robustness under morphology changes.
   
   The lack of these analyses matters because the strongest claim is not merely "GAT gets higher reward", but "GAT enables morphology-aware inheritance". The current results only weakly support that stronger statement.

5. **There is no quantitative results table, which makes comparison unnecessarily hard and weakens the empirical presentation.**  
   For a paper making benchmark claims over four tasks and four methods, the absence of a compact numerical summary is a real problem. **Figure 3** gives rough visual trends, and **Section 5.2** provides a few single numbers for Thrower-v0 in prose, but there is no table of final mean ± std returns, no ranking across tasks, and no statistical test. This matters because several curves in **Figure 3** are close, especially on Carrier-v1 and Catcher-v0, and the shaded regions overlap substantially in places. Without a table, the reader cannot tell whether the gains are substantial, consistent, or within noise.

6. **The qualitative analysis is selective and sometimes over-claimed relative to the evidence shown.**  
   In **Figure 4** on **Page 7**, the paper compares four approaches on Thrower-v0 using a single seed and a sequence of snapshots. The discussion claims that the GAT methods produce "human-like throwing mechanics" and that local transfer "reliably" reaches the target. That is a lot to infer from one qualitative example. Single-seed trajectory strips are useful illustrations, but they are not reliable evidence of consistency or mechanism. If anything, this figure underscores the need for rollout statistics over many seeds and morphologies.

   Likewise, **Figure 5** on **Page 8** is used to argue that all methods converge toward similar task-specific morphologies and that controller architecture mainly affects learning speed and adaptability. But the figure is a collage of top morphologies, without any morphological diversity metric, voxel-type statistics, actuator count distribution, or structural similarity analysis. The text draws a broader conclusion than the displayed evidence supports.

7. **The comparison between the "global" and "local" GAT variants is conceptually murky.**  
   The paper names the methods GA-GAT-PPO-Global-Transfer and GA-GAT-PPO-Local-Transfer, but the actual distinction is not cleanly formalized. On **Page 4**, the "global" strategy is described as averaging node features and assigning them uniformly to all nodes, while the "local" strategy gives each node its own feature vector. Yet on **Page 5** both variants are followed by graph processing and then node averaging into a global representation before the MLP head. This makes the architectural distinction narrower than the terminology suggests. The task-level interpretation in **Pages 6-7**, where local supposedly helps fine-grained coordination and global helps system-wide synchronization, is plausible but largely speculative because no mechanistic analysis of attention patterns, feature usage, or actuator-level behavior is provided.

8. **The paper repeatedly claims improved robustness to morphology changes, but does not actually define or measure robustness.**  
   Robustness here could mean many things: less performance degradation after mutation, lower variance across seeds, better transfer under larger topology edits, or better zero-shot performance before fine-tuning. The paper uses the term loosely in **Abstract**, **Page 2**, **Page 6**, and **Page 8**, but the actual evidence is mostly lower variance in best-fitness curves and stronger final scores. That is not the same thing. A cleaner experimental design would mutate trained robots under controlled edit distances and report pre/post adaptation performance. Without such a protocol, the robustness claim is not really pinned down.

9. **The fairness of the baseline comparisons is not fully established.**  
   Section 4 states that hyperparameters are adopted from Harada and Iba (2024) and that the number of robots trained follows Bhatia et al. (2021), but this does not guarantee fairness across architectures. GATs may benefit from different PPO settings, parameter counts, or training schedules than MLPs. The paper never reports model sizes, compute cost, wall-clock time, or total environment steps per method. This matters because the proposed method is sold partly as reducing retraining cost, yet no compute-normalized comparison is provided. If the GAT controller is significantly larger or receives effectively more useful warm-starting, then higher final reward alone is not enough to support the efficiency narrative.

10. **Presentation quality is only fair, with several writing and consistency issues that repeatedly interrupt technical understanding.**  
   There are multiple phrasing problems, for example "We address this by develop" in the abstract, "code design" instead of "co-design" on **Page 2**, and inconsistent notation for the critic, such as \(V_k\), \(\theta_k^{ct}\), \(\theta_u^{ct}\), and the odd use of actor weights for critic transfer in **Algorithm 2**. The references section also has formatting inconsistencies and mislabeled years. None of this alone is fatal, but in aggregate it contributes to the impression that the paper was not polished carefully enough for a method paper whose contribution depends on technical precision.

11. **The paper misses an opportunity to position itself against broader morphology-conditioned control approaches beyond EvoGym inheritance baselines.**  
   The related work is not empty, but the positioning remains too narrow. The paper mainly argues against MLP inheritance baselines, while the broader question is how to control varying morphologies in a reusable way. More discussion contrasting graph-structured inheritance against other morphology-conditioned or universal-controller approaches would help clarify whether the benefit comes specifically from graph topology, from parameter transfer, or from simply using a more embodiment-aware policy class. As it stands, the paper’s framing is somewhat convenient: it compares mostly against the weakest point of fixed-shape MLP policies.

## Questions
1. Please provide the exact actor and critic architectures. How many GAT layers, how many heads, what hidden dimensions, and what is the exact output-head structure for mapping a pooled graph embedding to actuator commands?

2. How are edge features \((\Delta x,\Delta y)\) incorporated into the GAT attention mechanism? Please give the exact attention equation and clarify whether you are using a standard GAT or a modified edge-aware variant.

3. In **Algorithm 1**, should line 16 pass \((\theta_u^{act}, \theta_u^{ct})\) rather than \((\theta_u^{act}, \theta_u^{act})\)? In **Algorithm 2**, should line 10 copy critic layers from \(\theta_u^{ct}\) rather than from \(\theta_u^{act}\)? If not, please explain the intended actor-critic parameter sharing.

4. Can you provide a quantitative table over all four tasks with final mean ± std returns across runs, and preferably also average/median population fitness in addition to best-fitness curves? This would substantially improve confidence in the claimed gains.

5. The central claim is morphology-aware inheritance. Can you provide a direct transfer experiment that measures offspring adaptation after mutation, for example performance immediately after transfer, after a fixed fine-tuning budget, and as a function of mutation size? That would be much more diagnostic than only reporting best-of-generation fitness.

6. What are the parameter counts and training costs of the GAT and MLP baselines? A compute-normalized comparison would help support the efficiency claims.

7. For the "global" vs "local" variants, can you give a precise formal definition of the node feature construction and any evidence, beyond post-hoc interpretation, that one favors local coordination while the other favors whole-body synchronization?

8. If you have them, attention visualizations or actuator-level analyses on examples from **Figure 4** would help justify the mechanistic story that the GAT is learning meaningful structural dependencies rather than simply serving as a larger function approximator.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the paper. The work is a simulation-based robotics/control study in EvoGym and does not appear to involve human subjects, private data, or immediately sensitive deployment contexts.

## Soundness Rating
2: fair. The high-level approach is plausible, but the technical description is underspecified, the inheritance algorithms contain inconsistencies, and the experiments are not strong enough to fully support the main claims.

## Presentation Rating
2: fair. The paper is readable overall and the main idea can be followed, but precision is lacking in the methodology, there are notation and pseudocode issues, and the empirical presentation would benefit from proper quantitative tables and tighter claims.

## Contribution Rating
2: fair. The problem is relevant and the graph-based inheritance angle is sensible, but the advance over prior graph-structured and morphology-aware control work appears limited, and the empirical validation does not elevate it to a stronger contribution.

## Overall Rating
2: Reject, not good enough. The paper addresses an interesting problem and has a reasonable intuition, but in its current form it is too incremental, too underspecified technically, and too weakly validated empirically for ICLR. A stronger version would need much more precise method definition, corrected algorithms, direct transfer diagnostics, and substantially better quantitative evaluation.

## Reviewer Confidence
4: confident. I am confident in this assessment, though it is still possible that some implementation details omitted from the main paper would clarify parts of the method.