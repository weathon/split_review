---
job_id: 192940e9-8ddd-4755-9792-76186647a70a
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 5H8kxW0Efk.pdf
paper: Neural Network Ising Machines: Algorithm Unrolling for Combinatorial Optimization
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining learning-to-optimize, zeroth-order optimization, neural algorithm design, and graph/combinatorial optimization.

## Minimum Quality
Pass ✅. The paper contains the required scientific components, including abstract, introduction, related work, methodology, empirical analysis, benchmark results, and conclusions. While there are notable weaknesses in evaluation fairness, mathematical precision, and overclaiming, these are review-level concerns rather than desk-reject-level fatal flaws.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes a neural-network-parameterized Ising machine (NPIM) for solving Ising / Max-Cut style combinatorial optimization problems. The core idea is to unroll an iterative Ising-machine-style dynamical system, parameterize its update rule with a small time-dependent MLP, and train the resulting solver using a zeroth-order evolutionary optimizer rather than backpropagation or policy gradients.

The paper studies both continuous and discrete variants of the method, analyzes some learned dynamics, and benchmarks the approach on synthetic Ising / Max-Cut related tasks as well as G-set instances. The authors report competitive results against prior neural CO methods and several Ising-machine baselines.

## Strengths
1. **Interesting synthesis of ideas across communities.**  
   The paper combines algorithm unrolling / learning-to-optimize, Ising-machine dynamics, and derivative-free parameter learning in a way that is coherent and practically motivated. Even if each ingredient is individually familiar, the combination is not trivial, and the paper makes a case that this compact parameterization can learn nontrivial search behavior for NP-hard graph problems.

2. **Compact solver parameterization is appealing.**  
   A major practical strength is that the learned policy is very small. The parameter count in Section 3.3 is modest, and the temporal basis parameterization in **Equation 6** is a sensible way to allow nonstationary dynamics without learning a fully separate network at each step. This is a cleaner design choice than throwing a large graph model at the problem and calling it a day.

3. **The dynamical-system framing is reasonably intuitive and, at a high level, well motivated.**  
   **Figure 1a** is helpful in showing the information flow, especially the role of the coupling field history as the network input. It makes the proposed solver easier to understand than many neural CO papers where the architecture and optimization loop are buried in implementation detail. **Figure 1b** also helps position the method conceptually relative to “pure neural solver” versus “hand-crafted iterative algorithm.”

4. **Some of the analysis is genuinely informative rather than being benchmark-only.**  
   The discussion around the emergence of momentum-like behavior in Section 4.1 is one of the more interesting parts of the paper. In **Figure 2**, the contrast between “Network A” and “Network B”, especially the change in connection signs in the weight visualizations and the corresponding residual-energy trajectories, provides at least a plausible qualitative story that the learned dynamics are evolving beyond simple greedy descent. I appreciate that the paper attempts to inspect the learned solver rather than only reporting final objective values.

5. **There is a nontrivial empirical effort across multiple benchmark styles.**  
   The paper does not restrict itself to a single benchmark family. It reports both neural-CO-style benchmarks in **Table 1** and Ising-machine-style TTS benchmarks in **Table 2**, plus further architecture studies in **Figure 3c / Table 3** and instance-wise details in **Table 4**. That breadth is useful for a paper trying to bridge multiple literatures.

6. **The architecture study gives at least some evidence that the model is doing more than memorizing a toy update rule.**  
   In **Figure 3c** and **Table 3**, success rate generally improves as parameter count grows, and this trend appears for both cNPIM and dNPIM. The exact effect sizes are not huge, but the result supports the claim that extra temporal and hidden degrees of freedom matter.

## Weaknesses
1. **The strongest empirical claims are undermined by an evaluation protocol that is not fully apples-to-apples.**  
   This is the main issue for me. In **Table 1**, the reported dNPIM result is explicitly “top 30”, meaning the method runs 30 trajectories in parallel and takes the best outcome, while the compared methods are reported as single entries copied from prior work. The paper states this in the caption, but does not normalize the comparison by equal sample budget, equal wall-clock budget, or equal number of parallel candidate solutions. That matters a lot, because for stochastic solvers the best-of-\(K\) effect can substantially change both objective quality and time. The fact that dNPIM is labeled “top 30” while baselines are not presented in the same way makes the comparison hard to interpret as solver superiority rather than budget superiority.

   The same concern appears in the G-set comparisons. In Section 5 and **Table 2**, the authors compare TTS values against prior Ising-machine results, but the paper does not really establish that the tuning effort, run budget, stopping rules, and implementation assumptions are matched. Since the central claim is “competitive” or near-SOTA performance, this fairness issue materially affects the paper’s scientific value, not just presentation polish.

2. **The benchmark story is selective, and some results directly weaken the broad performance claims.**  
   The paper’s own data show clear failure modes that are somewhat buried in optimistic language. In **Table 2**, the planar \(P,+\) category is dramatically worse for dNPIM than all listed baselines, for example \(4.42\times 10^7\) versus \(1.81\times 10^6\) for CAC median TTS. **Table 4** makes this even sharper: instances G14-G17 are all substantially worse than SOTA, in some cases by over an order of magnitude. Yet Section 5 still says the method outperforms existing Ising-machine state of the art on “almost all problem instances.” That phrasing is too generous given how severe the planar failures are.

   This matters because the paper is selling a learned dynamical heuristic that should discover effective search rules. If there is a whole structural family where it fails badly, that should be elevated into the main conclusion, analyzed, and connected back to the architecture. Right now it reads more like the failures are treated as an inconvenient corner case, when in fact they are evidence of strong distribution dependence.

3. **Several mathematical definitions and claims are underspecified or imprecise, which makes it hard to verify what is actually being optimized.**  
   A first example is the Ising objective in **Equation 1**. The paper writes
   \[
   \min_{\sigma \in \{-1,1\}^N} \sum_{i,j} J_{ij}\sigma_i\sigma_j - \sum_i l_i \sigma_i.
   \]
   Since \(J\) is said to be symmetric, this double sum appears to count each pair twice unless the intended convention is that \(J\) already incorporates the factor \(1/2\). That convention is not stated. This becomes relevant because **Equation 3** defines
   \[
   h_i(t) = \sum_j J_{ij} x_j(t) + \tfrac12 l_i,
   \]
   and the text calls \(h_i\) a “discrete gradient.” If **Equation 1** is taken literally as a full double sum over all \(i,j\), then the spin-flip energy change would involve factors of \(2\) or \(4\) depending on convention. The current formulation leaves the gradient interpretation ambiguous.

   A second example is **Equations 4-5**. The notation oscillates between scalar and vector arguments. In **Equation 2**, \(F\) is defined per-coordinate, \(x_i(t)=F(t,h_i(0),\dots,h_i(t-1))\), but in **Equations 4-5** the authors write \(F(t,h(0),\dots,h(t-1))\) and then use matrix notation that looks like a scalar-output MLP applied to a temporal vector. This can be inferred, but it is not cleanly specified. Since the paper is method-heavy, this level of notation sloppiness is not a minor issue.

4. **The reward design raises validity concerns, especially because the target optimum is partially defined using the algorithm’s own previous runs.**  
   In Appendix F, the success reward \(\mathcal{R}_{\text{succ}}\) in **Equation 24** depends on \(E_0\), described as “the best energy found by all previous runs of all algorithms,” and in practice during training they keep track of the best energy found so far and use that as \(E_0\). This is a very unusual setup. It means the reward target is nonstationary and partially endogenous to the training process itself. For hard instances where the true optimum is unknown, this reward can suddenly change when the running best changes, and it can also reward matching a historically found value rather than solving the original optimization problem in a stable sense.

   This matters for two reasons. First, it makes training dynamics harder to interpret. Second, it complicates claims about “success rate,” because success is defined relative to a moving target that is not necessarily the ground truth optimum. The paper acknowledges this informally, but not enough. At minimum, the main text should discuss how often \(E_0\) changes late in training, and whether evaluation is ever contaminated by using a target discovered during or after training.

5. **The policy-gradient comparison is too underdeveloped to support the strong dismissal in Section 2.4 and Appendix E.**  
   The paper repeatedly argues that policy gradients are ineffective here because of poor reward attribution over many small decisions. The intuition is reasonable, but the evidence presented in Appendix E is thin. The MDP formalization in **Equation 23** is minimal, the hyperparameter tuning effort for the policy-gradient baseline is not described carefully, and the theoretical argument is only a back-of-the-envelope SNR heuristic, not a rigorous comparison. Yet the main text frames this almost as a settled methodological conclusion.

   This matters because one of the paper’s central selling points is the choice of zeroth-order training. If the alternative baselines are not carefully instantiated, the reader cannot tell whether the gain comes from a superior estimator or from a weak policy-gradient implementation.

6. **The “learned dynamics” interpretation is suggestive, but still too anecdotal.**  
   Section 4.1 and **Figure 2** are visually interesting, but the claims about emergence of momentum and annealing are still interpretive rather than demonstrated. For example, the paper says the early network learns a greedy steepest-descent strategy and later acquires a momentum-like effect, inferred from the signs of temporal weights and from trajectory shapes. That is a plausible story, but not yet an empirical test. A much stronger analysis would compare to explicit hand-designed ablations: a greedy-only update, a momentum-only variant, fixed versus time-varying weights, or a learned network with the positive temporal weights clamped to zero after training.

   Without such ablations, **Figure 2** is more of a compelling illustration than a validation of the claimed mechanism. I liked the figure, but the paper leans on it more heavily than the evidence justifies.

7. **The out-of-distribution and scaling claims are modestly supported at best.**  
   The paper states in Section 4.3 and 4.4 that the method can generalize across problem size and hardness with fine-tuning. **Figure 3a** does show some transfer from \(N=100\) pretraining to larger SK instances, but the text also admits that training from scratch at \(N=500\) is “not possible.” That is important. It means the method’s scaling story currently depends on a curriculum / fine-tuning recipe rather than direct optimization on the target distribution. Similarly, in **Figure 3d**, performance degrades away from the tuned hardness regime. So the paper’s own evidence supports “distribution-specific learned heuristics with limited transfer,” not a broadly scalable learned optimizer.

   This does not kill the paper, but it should significantly temper the framing.

8. **The choice of baselines is narrower than the paper’s claims warrant.**  
   The method is positioned both against neural CO and against Ising machines, but the actual comparisons are mostly to a handful of methods copied from prior papers. There is no comparison to simple strong local-search heuristics on the main Max-Cut tasks in the paper, nor to broader learning-to-optimize / unrolled solver baselines adapted to the same update-budget regime. Since the method’s contribution is not merely “another Ising machine,” but specifically “learned Ising-machine dynamics,” the ablation space should include non-neural and semi-neural solver families under matched computational budgets.

9. **Presentation quality is mixed, and some exposition issues obstruct technical understanding.**  
   There are many grammatical errors and awkward phrasings throughout the paper, for example in Sections 1, 2.4, 4.3, and 5. More importantly, the notation is inconsistent in a few places, there are several typos in references and captions, and some claims rely on appendix details that should be in the main paper. **Figure 3** is dense and contains multiple subplots carrying different messages, but the text discussion is somewhat scattered. The paper is readable, but not polished enough for the level of technical claim it is making.

## Questions
1. **Can the authors provide strictly budget-matched comparisons for the main benchmarks?**  
   For **Table 1**, I would like results where each method is given the same number of samples / trajectories, and separately the same wall-clock budget. For dNPIM specifically, please report single-trajectory, best-of-5, best-of-10, and best-of-30 performance. This would substantially increase my confidence in the comparative claims.

2. **How often does the reference energy \(E_0\) change late in training, and how sensitive are results to this moving-target reward definition?**  
   A useful response would include a plot showing the fraction of instances whose \(E_0\) changes over epochs, plus a version where \(E_0\) is frozen after a warmup phase. This would clarify whether the reported optimization is stable or heavily shaped by a nonstationary internal target.

3. **Can the authors clarify the exact energy convention behind Equations 1 and 3?**  
   Please explicitly derive the spin-flip energy change \(\Delta E_i\) under your convention and show how **Equation 3** corresponds to the correct local field. Right now the factor-of-2 conventions are ambiguous.

4. **Can the authors provide more mechanistic ablations supporting the “momentum” interpretation from Figure 2?**  
   For example: remove temporal history, remove sign changes in late-lag weights, fix \(M=1\), or replace the learned temporal basis with constant weights after training. If the performance drop matches the interpretive story, that would make Section 4 much stronger.

5. **What exactly is being tuned on which data split for the benchmark tables?**  
   The paper says that for each G-set graph type, synthetic training instances are generated and the model is fine-tuned to that instance family. Please clarify whether any benchmark-instance-specific information influences tuning, how validation is performed, and whether the best checkpoint is selected without looking at the reported test instances.

6. **For the poor planar-graph performance in Table 2 / Table 4, do the authors have a concrete hypothesis tied to the update architecture?**  
   A rebuttal that explains whether this failure is due to local moves, limited memory \(T_c\), the training distribution, or the reward definition would materially affect my view of the method’s robustness.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the submission. The work studies heuristic optimization algorithms on standard synthetic and benchmark graph problems and does not involve sensitive data, human subjects, or obvious safety-critical deployment claims.

## Soundness Rating
2: fair. The method is plausible and supported by a nontrivial empirical study, but important technical details are imprecise, and the core comparative claims are weakened by evaluation design and underspecified baselines.

## Presentation Rating
2: fair. The high-level idea is understandable and some figures are helpful, but the paper has enough notation issues, writing problems, and missing clarifications that the presentation falls short of what I would expect for a strong ICLR paper.

## Contribution Rating
2: fair. The paper offers an interesting combination of algorithm unrolling, Ising dynamics, and zeroth-order training, but the contribution is narrower and less convincingly validated than the paper’s framing suggests.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
There is a real idea here, and I think the compact learned-dynamics angle is interesting. However, the current version overclaims relative to the evidence. The fairness of the comparisons, the ambiguity in key mathematical definitions, the moving-target reward construction, and the substantial failure cases on some benchmark families collectively keep this below the bar for me in its present form.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I am familiar with neural combinatorial optimization, learning-to-optimize, and Ising-machine style methods, and I checked the main equations and experimental claims with care.