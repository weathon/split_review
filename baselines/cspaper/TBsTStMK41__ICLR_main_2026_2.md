---
job_id: 3ba62ea1-e6a0-4630-87a3-7e0af20d8145
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: TBsTStMK41.pdf
paper: Accept More, Reject Less: Reducing Up To 19% Unnecessary Desk-Rejections Over 11 Years of ICLR Data
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly about optimization, learning-related conference policy design, and societal/fairness considerations in ML, which fits ICLR’s scope.

## Minimum Quality
Pass ✅. The paper contains the expected components, including abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion. While I have substantial concerns about novelty, mathematical precision, and practical significance, these are review-level weaknesses rather than grounds for desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies submission-limit-based desk rejection at AI conferences and formulates the problem of keeping as many papers as possible under per-author submission caps as an integer program. The authors propose solving an LP relaxation followed by a deterministic rounding procedure, and evaluate the approach on 11 years of ICLR submission data crawled from OpenReview, reporting reductions in desk-rejected papers of up to 19.23% relative to stronger sequential baselines.

## Strengths
The paper tackles a concrete and timely problem. Submission limits and desk rejection policies are increasingly used in major conferences, and the authors are right that the common “keep the smaller submission IDs” heuristic is not obviously optimal if the goal is simply to maximize the number of papers that remain eligible for review.

The core optimization formulation in Definition 4.1 is simple and natural. Once stated as
\[
\max_{x \in \{0,1\}^m} \mathbf{1}_m^\top x \quad \text{s.t. } Ax \le b \mathbf{1}_n,
\]
the problem becomes immediately understandable, and the paper makes this objective easy to follow even for readers without deep OR background.

I appreciated that the authors do not compare only against the weakest baseline. Section 3.2 introduces FORWARDREJECT as a stronger implementation than “reject all excess papers at once,” which makes the empirical comparison less strawman-like than it could have been.

The empirical section uses a reasonably large longitudinal dataset. Table 2, on Page 7, is useful because it shows how the scale changes dramatically over time, from 67 papers in 2013 to 11,672 papers in 2025, and also reports useful structural statistics such as \(\mathrm{nnz}(A)\), MSPA, and ASPA. That table helps contextualize why the optimization problem becomes more relevant in recent years than in older, much smaller ICLR editions.

Figure 1 on Page 1 effectively motivates the paper. The log-scale growth in ICLR submissions visually supports the claim that conference-scale pressures have changed materially over time, which is one of the paper’s central premises. Similarly, Figure 2 on Page 7 is helpful in showing the heavy-tailed per-author submission distribution for ICLR 2023-2025; this is directly relevant because the benefit of any submission-limit policy depends on the existence of a relatively small set of high-submission authors.

The main quantitative result is clearly presented in Table 3 on Page 8. The trend is consistent: the proposed method always matches or improves on FORWARDREJECT, often by nontrivial margins in recent years. For example, for ICLR 2024 at \(b=22\), the proposed method reduces desk rejections from 26 to 21 relative to FORWARDREJECT, corresponding to the reported 19.23% relative improvement. Even if one debates the broader importance of the setting, the empirical claim that the optimization objective helps compared with ID-order heuristics is supported by the table.

The paper is generally readable. The problem statement, algorithms, and experiment setup are organized in a way that makes the story easy to follow.

## Weaknesses
1. **The central optimization problem is very standard, and the paper overstates the methodological contribution.**  
   The formulation in Definition 4.1, on Page 5,
   \[
   \max_{x\in\{0,1\}^m}\mathbf{1}_m^\top x \;\; \text{s.t. } Ax \le b\mathbf{1}_n,
   \]
   is essentially a binary packing / set packing style integer linear program with uniform profits and degree constraints. The paper itself even notes the connection to multidimensional knapsack in Section 4.2. That is fine, but then the contribution is mostly an application of a very standard ILP-to-LP-relaxation pipeline to a niche policy problem. The paper does not provide a new relaxation, a nontrivial approximation ratio, a better exact algorithm for the special structure here, or a structural characterization of instances arising from conference authorship graphs. As written, the algorithmic novelty feels limited.

2. **The paper does not establish that Algorithm 4 is actually solving Definition 4.1 well, beyond feasibility.**  
   This is a major issue for me. The paper’s advocacy depends on the idea that the proposed method meaningfully approximates the maximum desk-acceptance objective, but Theorem 4.6 on Page 6 proves only feasibility of the rounded solution, not any approximation guarantee on \(\mathbf{1}^\top x\). In other words, the method is shown to return *a* feasible integer solution, not a solution with a proven relationship to the LP optimum or the ILP optimum. The result could, in principle, be far from optimal on some instances. Given that the paper’s entire pitch is “accept more, reject less,” the lack of any guarantee like
   \[
   \mathbf{1}^\top \widetilde{x} \ge \alpha \cdot \mathrm{OPT}
   \]
   for some explicit \(\alpha\), or at least an additive loss bound from rounding, is a real gap. Without that, the method is more heuristic than the paper’s framing suggests.

3. **The rounding algorithm is underspecified and the correctness argument is too loose.**  
   Algorithm 3 on Page 6 is the technical heart of the paper, but several steps are not defined rigorously enough:
   - In line 14, the algorithm says “Find the set \(S_i \subseteq (S \cap T_i)\) such that \(\sum_{j\in S_i}\widetilde{x}_j \ge (1-x_l)\).” There may be many such sets; the paper does not specify which one is chosen, whether minimizing the removed mass matters, or how this is found efficiently.
   - It is not proven in the main paper that such a set always exists whenever line 13 triggers. The intended reasoning seems to be that the overflow created by rounding paper \(l\) up is at most \(1-x_l\), but this crucial point is not spelled out.
   - Even if such a set exists for one author, multiple authors of paper \(l\) may induce overlapping removals, and the effect on later iterations is not analyzed carefully.
   
   The proof in Appendix B.2 is much too hand-wavy for the importance of this step. It says, “all the authors affected by up rounding paper \(l\) will be desk-rejected a sufficient number of papers,” but that is exactly the part that requires a detailed invariant and proof. This is not just a style complaint, because the method’s credibility depends on the rounding being well-defined and sound.

4. **There are mathematical and notational inconsistencies that weaken trust in the technical exposition.**  
   A few examples:
   - In Definition 4.1 and Definition 4.3, \(x\) is repeatedly called a “desk-rejection vector,” but by Definition 3.2 and the objective \(\max \mathbf{1}^\top x\), \(x_j=1\) actually means desk-*accepted*. This is more than a typo, because it creates confusion around the semantics of the variables in the main optimization problem.
   - On Page 6, Remark 4.5 says the algorithm guarantees “efficient computation, enabling desk-rejection maximized desk rejection,” which appears to be a garbled sentence and suggests the technical text was not fully checked.
   - In Table 3, the dataset labels say “ICLR 2018 (n=935), ICLR 2019 (n=1419), …” but in Table 2, \(n\) is the number of authors and \(m\) is the number of papers. Here 935 and 1419 correspond to the number of papers, not authors. So Table 3 is inconsistent with the notation introduced in Section 3. This kind of mismatch matters because the paper is presenting itself as a mathematically careful study.

5. **The baseline story is still too narrow for the practical claim being made.**  
   Section 5.1 says the only baselines are ALLREJECT and FORWARDREJECT because the authors are “among the first” to revisit this problem. But once the paper defines an explicit ILP in Definition 4.1, a natural benchmark is simply an off-the-shelf integer programming solver on the original formulation, at least for the smaller and medium-sized years. That would answer an obvious question: how far is the LP+rounding solution from the true optimum? Right now, Table 3 only shows that the proposed heuristic beats very specific procedural baselines. It does not show whether it is close to optimal, occasionally exact, or sometimes still significantly suboptimal.

6. **The practical significance is somewhat oversold relative to the absolute numbers.**  
   The title emphasizes “up to 19% unnecessary desk-rejections,” which sounds dramatic, but this is a relative improvement over the strongest baseline on the subset of already desk-rejected papers, not over total submissions. Table 3 makes this clear. For instance, the headline 19.23% occurs for ICLR 2024 at \(b=22\), where the absolute improvement over FORWARDREJECT is from 26 rejected papers to 21, a gain of 5 papers out of 7,404 total submissions. That is not nothing, but it is also not a conference-scale shift in workload or acceptance dynamics. The paper repeatedly uses broad language such as “saving thousands of authors” and “strong potential to improve current CS conference submission policies,” but the actual improvements are often modest in absolute terms, especially at realistic high \(b\) values.

7. **The empirical evaluation is one-dimensional and does not probe fairness or policy tradeoffs beyond paper count.**  
   The objective is to maximize the number of surviving papers, which is a utilitarian criterion. But the paper repeatedly frames the motivation in terms of “author welfare,” “inclusivity,” and helping early-career researchers. None of that is actually measured. Maximizing \(\sum_j x_j\) may preserve more papers overall while still favoring already prolific or highly connected author groups. A more policy-relevant paper would examine at least some distributional statistics, such as per-author survival rates, concentration of preserved papers among high-submission clusters, or whether the method systematically benefits large coauthor components. As written, “welfare” is asserted rather than analyzed.

8. **The data preprocessing and solver setup are not fully transparent enough for a policy paper.**  
   Section 5.1 states that before solving, the authors “remove all safe authors whose papers have no co-authors exceeding the submission limit.” This may be a valid presolve reduction, but the exact rule is not formalized and no proof is given in the main text that it preserves the optimization problem. In addition, Algorithm 4 includes “Randomly initialize \(x_0\),” but the LP in Definition 4.3 is a linear program, so the role of random initialization is unclear and unnecessary for standard LP solvers. These choices create avoidable ambiguity.

9. **The paper’s use of figures is more motivational than analytical.**  
   Figure 2 on Page 7 shows heavy-tailed submission frequencies for 2023-2025, but the paper does not connect the shape of those distributions to the behavior of the optimization algorithm. For example, one would expect gains to depend on overlap structure in the coauthorship hypergraph, not only on marginal submission counts. The figure supports the existence of prolific submitters, but it does not explain when or why the optimization helps most. A more informative analysis would tie the gains in Table 3 to graph statistics derived from \(A\), not just submission-count histograms.

10. **The literature positioning is thinner than it should be for a paper framed as policy-relevant conference science.**  
    Section 2 mostly cites desk rejection mechanisms and broad comments about AI competitiveness, but there is little engagement with the broader empirical literature on conference review processes and policy evaluation. That makes the paper feel somewhat isolated, as if it treats this as a standalone optimization toy problem rather than a component of a complicated review ecosystem. Even if the method itself is simple, the paper would be stronger if it situated the proposed policy change within existing empirical knowledge about peer review pipelines and procedural interventions.

11. **Some claims in the proofs are simply sloppy.**  
    In Proposition B.1 in Appendix B.1, the proof says “the algorithm iterates through all the \(n\) papers,” but \(n\) is the number of authors, not papers. In Proposition C.1, the contradiction argument is not carefully written and even refers to “Algorithm 3” when proving correctness of Algorithm 5. I realize the appendix is not supposed to determine the final outcome by itself, but these errors reinforce the broader impression that the mathematical layer was not polished to the standard expected for a paper whose main contribution is formalization plus algorithms.

## Questions
1. Can the authors provide a formal guarantee on the quality of Algorithm 3 or Algorithm 4 relative to the ILP optimum in Definition 4.1? Even a weak approximation ratio, additive bound, or a characterization of when the rounding is exact would materially increase my confidence.

2. Why not compare against solving the original binary ILP exactly, at least for smaller years such as 2018-2021? This would let readers judge whether LP+rounding is merely better than the procedural baselines, or actually near-optimal for the intended objective.

3. In Algorithm 3, line 14, how exactly is \(S_i\) selected? Is it the minimum-cardinality subset, minimum-total-mass superset, or arbitrary first-fit? Please define the procedure explicitly and prove that such a set always exists when line 13 is triggered.

4. Can the authors clarify the presolve reduction described in Section 5.1? A short proposition showing that removing “safe authors” and their incident papers preserves the optimum of Definition 4.1 would help.

5. The paper motivates the work using “author welfare” and fairness language. Can the authors report at least one author-level or group-level analysis beyond total number of desk-rejected papers? For example, how are saved papers distributed across authors with different submission counts or collaboration sizes?

6. Table 3 appears to use \(n\) in the dataset labels to denote the number of papers, whereas Section 3 defines \(n\) as the number of authors. Is this simply a typo, or did I misunderstand the notation? Please clean this up because it is genuinely confusing when reading the experiments.

7. Do the gains correlate more with the submission-count distribution in Figure 2, or with coauthorship overlap structure? A simple analysis of connected components, degree distribution in the bipartite graph, or overlap statistics could help explain when the method matters.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper studies conference submission policies using publicly available submission metadata and does not raise an obvious ethics issue requiring escalation based on the main text. That said, if deployed, such policies would have fairness implications, but those are already the subject of the paper rather than an unaddressed compliance concern.

## Soundness Rating
2: fair. The main empirical claim, namely that the proposed procedure beats the specified baselines on the collected ICLR data, is supported. However, the technical presentation around the rounding method is not rigorous enough, and the paper does not establish approximation quality relative to the stated optimization objective.

## Presentation Rating
3: good. The paper is readable and organized, and the motivation, problem setup, and experiments are easy to follow. Still, there are enough notation errors, inconsistencies, and underexplained algorithmic steps that I cannot rate the presentation as excellent.

## Contribution Rating
1: poor. The problem is timely, but the actual scientific contribution feels modest: a standard ILP formulation, LP relaxation, and heuristic rounding for a narrow policy setting, with limited theoretical depth and limited empirical analysis beyond paper-count reduction.

## Overall Rating
2: Reject, not good enough. The paper is competent and addresses a real issue, but for ICLR I do not think the contribution clears the bar. The optimization formulation is very standard, the core rounding algorithm lacks a meaningful quality guarantee, the experiments do not compare to the actual ILP optimum, and the broader policy significance is overstated relative to the absolute effect sizes.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main formulations, algorithms, tables, and proofs carefully, though I did not independently verify implementation details.