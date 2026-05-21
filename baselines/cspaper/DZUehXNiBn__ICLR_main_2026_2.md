---
job_id: e42dd40c-06fe-4131-b86f-82af29c9bd12
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: DZUehXNiBn.pdf
paper: Efficient Causal Structure Learning Via Modular Subgraph Integration
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically causal reasoning, scalable machine learning, and learning on graphs/structured models.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, methodological development, experiments with quantitative results, and conclusion; while I found several technical and empirical weaknesses, they do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes VISTA, a modular divide-and-conquer framework for causal DAG learning that decomposes the problem into Markov Blanket-centered subgraphs, runs an arbitrary base learner on each local subgraph, then merges the local outputs via a weighted voting rule followed by a feedback arc set heuristic to enforce acyclicity. The paper also presents finite-sample and asymptotic claims for the voting procedure, and evaluates VISTA on synthetic ER/SF graphs and the Sachs benchmark across several standard causal discovery baselines.

## Strengths
The paper addresses a real bottleneck in causal structure learning, namely the difficulty of scaling global DAG learning methods to larger graphs. The decomposition into MB-centered local subgraphs is simple to understand, naturally parallelizable, and potentially useful as an engineering framework even beyond the specific voting rule proposed here.

The overall pipeline is easy to follow. In particular, **Figure 3** gives a helpful end-to-end overview of the divide, conquer, and merge stages, and makes the modularity claim concrete. **Figure 2** also helps clarify the intended implementation flow, especially that aggregation is performed after collecting local directed subgraphs rather than modifying the base learner itself.

Empirically, the weighted voting variant often improves substantially over naive voting. This is visible in **Table 1**, where +VISTA-WV dramatically lowers FDR and SHD relative to +VISTA-NV across all listed base learners. For example, under NOTEARS on ER5, FDR drops from \(0.87\) to \(0.08\), and SHD drops from \(3171.8\) to \(182.4\), which does support the claim that raw overlap-based aggregation is too noisy and requires some calibration/filtering. Similar patterns are visible for GOLEM and DAG-GNN. So, even if I am not convinced by the theory as written, there is empirical evidence that the weighted post-processing is doing something useful relative to a naive merge.

The runtime results are also directionally encouraging. In **Table 3**, wrapping expensive learners such as NOTEARS, DAG-GNN, and GraN-DAG inside the proposed framework yields much lower reported total compute time, especially at \(n=300\). This is consistent with the intuition that many small local problems are easier than one large global optimization.

Finally, the paper is reasonably candid in acknowledging a real limitation in the conclusion, namely that restricting to subsets can induce latent confounding and redundant edges, and that the current framework can only mitigate, not solve, this issue.

## Weaknesses
I have a number of substantial concerns, several of which affect the core technical claims rather than just presentation.

1. **The theoretical claims are much stronger than what the analysis actually supports, and some assumptions directly conflict with the paper’s own motivating setup.**  
   The main paper repeatedly emphasizes that VISTA is “strictly model-agnostic” and requires essentially no assumptions beyond faithfulness, see **Page 2, paragraphs 2-3**. However, the theoretical analysis in **Theorem 3.2**, **Theorem 3.4**, and **Theorem 3.5** relies on a much narrower setting: independent votes across subgraphs, a fixed true-edge support probability \(p\), a fixed false-edge support probability \(q\), and enough repeated subgraph appearances \(m\) for each edge. This is already far from “arbitrary base learners” operating on overlapping subsets from the same data matrix. The votes are not independent in the actual procedure, because all local learners are fit on overlapping variable subsets from the same observational samples. The paper acknowledges this on **Page 6**, but then still uses these results to support broad soundness and consistency claims. That is too much of a leap. At minimum, the scope of the theoretical claims needs to be sharply narrowed.

2. **The asymptotic consistency theorem appears detached from the actual MB decomposition regime, and in fact contradicts the paper’s own appendix analysis of support counts.**  
   **Theorem 3.5** on **Page 7** assumes that the number of local subgraphs per candidate edge is \(m = C \log n\). But in the actual MB-centered construction, an edge \((i,j)\) appears only in subgraphs whose MBs contain both endpoints, which is typically very small in sparse graphs. The appendix effectively says this too. In **Theorem E.4** on **Page 22**, for ER-\(h\) graphs, the paper derives \(m_{ij} = 2 + X\) with \(X \sim \mathrm{Pois}(h^2/n)\), so for most edges \(m_{ij}=2\) with high probability. That is not \(C \log n\), it is basically a constant. This is a serious mismatch: the asymptotic result is built on a coverage growth condition that does not seem to hold in the graph models used in the experiments and even analyzed in the appendix. As written, this makes **Theorem 3.5** feel largely irrelevant to the proposed method.

3. **There are mathematical inconsistencies and sign/interpretation issues around \(\lambda\), including contradictions between the main text and appendix.**  
   The score is defined in **Equation (2)** as
   \[
   s(X \to Y) = \left(1 - e^{-\lambda m}\right)\frac{A}{m}.
   \]
   Since \(1 - e^{-\lambda m}\) is increasing in \(\lambda\), larger \(\lambda\) makes the score *less* penalized for low support counts, not more. The main text on **Page 4** gets this roughly right when it says larger \(\lambda\) tends to preserve limited evidence and improve recall. But **Appendix D.1, Page 17** says “A larger \(\lambda\) yields more aggressive penalization for rare edges,” which is the opposite. This is not a cosmetic issue, because \(\lambda\) is the core hyperparameter of the method, and the paper repeatedly interprets its role.  
   There are also formula-level issues in **Theorem 3.4 / Appendix E.1**. The interval in **Equation (26)** on **Page 21** is written as
   \[
   \lambda \in \left[-\frac{1}{m}\ln(1-t),\ \frac{1}{m}\ln\epsilon\right],
   \]
   but \(\ln \epsilon < 0\) for \(\epsilon \in (0,1)\), so the upper bound as written is negative, which is incompatible with the requirement \(\lambda>0\). The main-text version **Equation (5)** has the correct sign in the upper bound, but then the derivation and interpretation in the appendix become hard to trust. This part needs careful correction.

4. **Theorem 3.4 is not convincingly established as stated, and the “prescribed error control under the union bound” claim is underspecified.**  
   On **Page 6**, **Theorem 3.4** states that if
   \[
   -\frac{1}{m}\ln(1-t) < \lambda \le -\frac{1}{m}\ln \epsilon,
   \]
   then the weighted vote rule achieves the prescribed error control under the union bound. But what is the precise error target being controlled here? The result, as stated in the main paper, does not include the numbers of edges, the values of \(p\) and \(q\), or the graph size \(n\), all of which matter in a union bound over many candidate edges. In the appendix, the proof discusses a surrogate bound \(\mathcal{L}(\lambda)\), but it never really derives the stated theorem in a clean, parameter-complete way. The theorem reads much stronger and cleaner than the proof justifies.

5. **The Bayesian motivation for the weighted score is weakly grounded and uses an unusual prior construction without sufficient discussion.**  
   In **Appendix D.1, Equations (7)-(9)**, the score is reverse-engineered as a posterior mean with a Beta prior using \(\alpha=0\) and a data-dependent \(\beta=\kappa(m)\). This is not a standard Bayesian model, and \(\alpha=0\) is improper in the usual Beta family. I am not objecting to heuristic motivation per se, but the paper presents this almost as if it were a principled statistical derivation. It is better described as an after-the-fact interpretation of a hand-designed shrinkage factor. That is fine, but the text currently oversells it.

6. **The empirical claims of “consistent improvement” and “typically increasing precision without sacrificing recall” are overstated relative to the reported tables.**  
   The headline story is not uniformly true in the main results. In **Table 1**, +VISTA-WV often lowers TPR materially compared with the standalone baseline, sometimes by a lot. For example, NOTEARS on ER5 goes from TPR \(0.74\) to \(0.68\), and on SF5 from \(0.60\) to \(0.68\), which is mixed rather than uniformly better. GOLEM and DAG-GNN show large recall changes, often downward relative to the inflated NV version. More importantly, on the real-data benchmark in **Table 4**, +VISTA worsens TPR for GOLEM (\(0.26 \to 0.18\)) and SCORE (\(0.18 \to 0.12\)); GOLEM’s SHD does not improve at all (remains \(16\)). So the conclusion on **Page 10** that VISTA “typically increases precision without sacrificing recall” is not really supported by the presented results.

7. **The runtime comparisons are suggestive but not yet fair enough to support the strength of the efficiency claims.**  
   The paper states on **Page 8-9** and in **Table 3** that VISTA reduces total computing time substantially. That may well be true in practice, but the current presentation mixes together two effects: problem decomposition and parallel execution. Since VISTA is explicitly parallelized across local subgraphs, while the baselines are presented as monolithic methods, the comparison is not apples-to-apples unless the wall-clock protocol is described very carefully. Were the baselines allowed to use all available parallelism? Is MB identification included in the reported +VISTA times? Are these wall-clock times under the same CPU/GPU utilization policy? The paper says “total computation time,” but the implementation details are not clear enough in the main paper to make this a convincing systems-style comparison. The gains may be real, but the evidence is not yet rigorous enough.

8. **The method’s interaction with latent confounding is a central issue, not a side note, because subgraph restriction itself creates unobserved variables for the local learner.**  
   The paper explicitly states on **Page 5** that taking a subset of nodes from a causal graph introduces unobserved confounding and may lead to additional edges in the subgraph. This is a big deal. Most listed base learners, such as NOTEARS, GOLEM, DAG-GNN, and GraN-DAG, are standard DAG learners assuming causal sufficiency in the observed variables. If the local subproblem is induced by marginalizing out many omitted variables, then the local graph is generally not representable by a DAG over the retained variables without distortion. The current framework relies on a post hoc voting and FAS cleanup to absorb this mismatch, but there is no careful analysis of when this is valid or how severe the bias is. This matters directly for the scientific value of the framework, because it means the “local problems” are not faithful smaller versions of the global problem.

9. **The experimental positioning against prior scalable/local-to-global methods is not fully convincing.**  
   The paper discusses DCILP and several modular methods, but the main tables omit some strong scalable baselines that are relevant to the “large-scale causal discovery” pitch, such as stronger search-based or order-based scalable methods. DAGMA appears only in the appendix via the DCILP comparison, not in the main comparison tables, even though it is a very relevant continuous baseline. Also, the paper cites prior MB-based and divide-and-conquer works, but the experimental study does not really isolate what is new here versus simply “use any learner on MB neighborhoods, then threshold votes.” A stronger positioning would compare more directly against other local-to-global merge rules, not just against standalone global learners.

10. **Some exposition issues make the paper harder to trust than necessary.**  
   There are several notation and labeling inconsistencies. On **Page 4**, the text says “By Theorem 3.1” when it is actually **Proposition 3.1** on **Page 3**. **Corollary 3.3** is titled “Lower bound on node in subgraphs” in the main paper and “Upper bound of node in subgraphs” in the appendix, which is inconsistent and confusing. In **Algorithm 2** on **Page 16**, line 4 says “if \(\mathcal{G}\) contains a source then” and line 5 says “choose the sink \(u\),” which appears to be a typo in an algorithm that is already difficult to parse. These are not fatal individually, but there are enough of them that they undermine confidence in the more delicate mathematical claims.

11. **The figures support some parts of the story, but also expose gaps in the validation.**  
   **Figure 1** is used on **Page 3** to argue that MB identification remains stable while base learners degrade with graph size. The plot is directionally supportive, but it only shows F1 trends and does not report the MB estimator used, the size distribution of MBs, or how MB errors propagate into the downstream learner. Since the whole method depends on the local neighborhoods being meaningful, this figure feels more like a teaser than a validation.  
   Likewise, **Figure 4** is meant to support the \(\lambda\)-sensitivity story, but the caption fixes \(t=0.5\), while the main tables on **Page 8** use \(t=0.7\). So the sensitivity curves do not directly justify the chosen operating point used in the headline results. Also, the three subplots appear somewhat disconnected from the theory because the x-axis sweep shows a plateau region, but there is little quantitative link back to the “theoretical range” beyond a verbal claim.

## Questions
1. The most important point for me is the asymptotic theory. Can the authors reconcile **Theorem 3.5** with their own appendix derivation in **Theorem E.4**, where typical edge support is essentially \(m_{ij}\approx 2\) in sparse ER graphs? If \(m\) does not grow like \(C\log n\) under the actual MB construction, what exactly is the asymptotic regime being claimed?

2. Please provide a corrected and fully self-consistent treatment of \(\lambda\). In particular:
   - clarify whether larger \(\lambda\) penalizes low-support edges more or less,
   - fix the sign inconsistency in **Equation (26)**,
   - and state a clean theorem with all dependencies explicit.  
   Right now the interpretation of the central hyperparameter is internally inconsistent.

3. Can the authors quantify the effect of subgraph-induced latent confounding? A targeted experiment would help a lot, for example: compare performance when local subgraphs are learned from induced observational restrictions versus from oracle local interventions or from settings where the local DAG over the retained variables is actually well specified. This would clarify whether the gains come from decomposition or despite the structural misspecification introduced by decomposition.

4. For the runtime claims in **Table 3**, please specify exactly what is counted in “total computing time.” Does it include MB estimation, vote aggregation, and GreedyFAS? Are times wall-clock under fixed hardware parallelism? Were baselines allowed to use comparable CPU/GPU resources? A clearer protocol could substantially increase confidence in the efficiency claims.

5. Could the authors add an ablation comparing:
   - naive voting,
   - weighted voting without FAS,
   - threshold-then-FAS versus FAS-then-threshold,
   - and perhaps a simpler support-count threshold \(A \ge k\) baseline?  
   This would help isolate whether the real gain comes from the exponential weighting, from DAG projection, or simply from pruning a very noisy union graph.

6. The main text claims broad model-agnosticism, but the theory assumes edge-level probabilities \(p\) and \(q\) and essentially independent repeated votes. Can the authors restate more carefully what “model-agnostic” means here? I would be more persuaded by a modest claim, namely that the *software interface* is agnostic, while the *guarantees* hold only under additional probabilistic assumptions.

7. On the real-data results in **Table 4**, the gains are mixed, especially in TPR. Can the authors explain why VISTA improves SHD/FDR for some baselines while hurting recall? It would be useful to show the actual learned graphs or at least edge counts to understand whether the method is systematically over-pruning on small networks.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None.

## Soundness Rating
2: fair. The empirical signal is promising, but several central theoretical claims are either overstated, internally inconsistent, or not well aligned with the actual decomposition regime analyzed elsewhere in the paper.

## Presentation Rating
2: fair. The high-level idea is understandable and the pipeline figures are helpful, but the paper has enough notation issues, theorem inconsistencies, and mismatched interpretations that the presentation falls below the standard I would expect for a technically ambitious ICLR submission.

## Contribution Rating
2: fair. There is a practically interesting modular recipe here, and the empirical gains over naive merging are real, but the conceptual advance over prior local-to-global/MB-based decomposition methods feels moderate, and the current theory does not yet elevate it to a strong contribution.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The framework is practically interesting and some of the empirical improvements are real, especially relative to naive voting, but the paper currently overclaims on theory, underspecifies key assumptions, and does not fully support its strongest generality and consistency statements.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I checked the equations and theory carefully enough to identify several concrete inconsistencies, and I am familiar with the causal discovery literature, but some implementation details remain unclear from the main paper alone.