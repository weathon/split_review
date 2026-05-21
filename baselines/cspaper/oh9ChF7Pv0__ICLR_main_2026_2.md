---
job_id: 3615e204-ba90-463c-8b91-9a8f5e6609b8
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: oh9ChF7Pv0.pdf
paper: Egg-SR: Embedding Symbolic Equivalence into Symbolic Regression via Equality Graph
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining neurosymbolic learning, reinforcement learning, learning theory, and AI for scientific discovery through symbolic regression.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, methodology, related work, experiments with quantitative results, and conclusion, and it presents a nontrivial methodological contribution with supporting theory and experiments, despite several limitations.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeted instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes Egg-SR, a framework for incorporating symbolic equivalence into symbolic regression via equality graphs, with three instantiated variants: Egg-MCTS, Egg-DRL, and Egg-LLM. The main idea is to compactly represent equivalent expressions using e-graphs, then use these equivalence classes to share search statistics in MCTS, aggregate probabilities across equivalent trajectories in DRL, and enrich feedback prompts for LLM-based symbolic regression. The paper also provides theoretical claims, namely a tighter regret characterization for the MCTS variant and a lower-variance policy-gradient estimator for the DRL variant, together with experiments on several symbolic regression benchmarks.

## Strengths
1. The paper tackles a real inefficiency in symbolic regression, namely that many syntactically different expressions are functionally equivalent, and current search or learning procedures often waste effort rediscovering such variants. This is a sensible problem formulation, and the paper makes a credible case that equivalence-awareness is a useful inductive bias for SR.

2. The framework is broader than a single algorithmic tweak. The same core machinery is used across three different families, MCTS, policy-gradient-based SR, and LLM-based SR. Even if some parts are stronger than others, that unifying perspective is valuable.

3. The intuition behind the e-graph construction is explained reasonably well in the main paper. In particular, **Figure 1** is helpful: the sequence of initialization, matching, substitution, and merging makes the data structure concrete, and it clarifies how equivalent subexpressions are shared rather than explicitly enumerated. This is one of the clearer parts of the exposition.

4. The MCTS integration is conceptually appealing. **Figure 2** illustrates the key mechanism clearly: the paper is not merely simplifying expressions after the fact, but using equivalence during backpropagation to share counts and rewards across matched paths. That is more interesting than using e-graphs only as a post-processing simplifier.

5. The empirical results do suggest that the method can help in practice. In **Table 1**, Egg-MCTS improves over MCTS on most of the reported trigonometric datasets, often by a large margin, especially in the noiseless setting for the harder problems, for example \(0.006\) vs \(0.144\) on \((4,4,6)\), and \(0.009\) vs \(0.147\) on \((5,5,5)\). Egg-DRL also improves over DRL in most reported entries. These are not tiny deltas.

6. The case-study style diagnostics are useful. **Figure 3 (left)** supports the claim that equivalence-aware sharing changes the effective search dynamics in MCTS, and **Figure 5** is helpful because it addresses a natural concern that e-graph manipulation might dominate runtime. Even though the runtime analysis is limited, it is still good that the paper attempted to quantify overhead.

7. The theoretical direction is appropriate for the paper’s goals. The DRL analysis, especially the Rao-Blackwellization-style variance argument in Appendix A.3, is at least aligned with the proposed estimator and gives the reader a principled lens for understanding why aggregating equivalent trajectories could help.

## Weaknesses
1. The paper’s novelty relative to prior e-graph-based symbolic regression work is narrower than the introduction sometimes suggests, and the positioning is still somewhat slippery. On **Page 2** and again in **Section 4**, the authors acknowledge prior uses of e-graphs in GP-based symbolic regression for duplicate detection, simplification, and template matching, citing de França and Kronberger’s line of work. That makes the central novelty here not “using e-graphs for symbolic regression,” but rather integrating them into several modern SR paradigms and providing tailored learning rules. That contribution is still worthwhile, but the writing occasionally overstates the gap, for example in the introduction’s framing of symbolic equivalence as “underexplored” without distinguishing strongly enough between post-hoc simplification, duplicate elimination, and in-loop training-time equivalence sharing. This matters because the paper’s contribution is closer to a framework-level extension than a fundamentally new SR primitive, and the claims should be calibrated accordingly.

2. Theoretical claims in the main paper are materially weaker than their presentation suggests. In **Section 3.4**, **Theorem 3.1** is stated as a regret improvement for Egg-MCTS, but the main text omits several critical assumptions that substantially narrow its relevance. In the appendix, the analysis explicitly switches from the UCT score in **Equation (2)** to OPD-style analysis, and **Appendix A.2.2** even states that “we assume that MCTS operates under the Optimistic Planning for Deterministic Systems (OPD) framework rather than the UCT principle.” This is a major caveat because the actual algorithm described in the main text and visualized in **Figure 2** is a UCT-based MCTS. So the theorem does not really analyze the algorithm the reader is first told to care about; it analyzes a related optimistic planning abstraction after additional assumptions. The paper should have been much more explicit about this in the main text. Otherwise, the theory reads as if it certifies the proposed UCT-style procedure, which it does not.

3. The DRL estimator in **Equation (4)** is underspecified in a way that matters for both correctness and implementation. The estimator is written as
\[
g_{\texttt{egg}}(\theta)\approx \frac{1}{N}\sum_{i=1}^N (\texttt{reward}(\tau_i)-b') \nabla_\theta \log \Big[\sum_{k=1}^K p_\theta(\tau_i^{(k)})\Big].
\]
However, the equivalence set is only approximated by sampling \(K-1\) variants from the e-graph, not by enumerating the full equivalence class \(\mathcal{S}_\phi\). The unbiasedness proof in **Appendix A.3** is carried out for the full class probability
\[
q_\theta(\phi)=\sum_{\tau\in \mathcal{S}_\phi} p_\theta(\tau),
\]
not for a truncated, sampled subset of size \(K\). Those are not the same object. So, unless \(K\) covers the full equivalence class or the authors provide an importance-weighted argument, the theoretical unbiasedness statement does not directly justify the implemented estimator in the main paper. This is not a cosmetic issue. It affects whether the claimed estimator is truly unbiased, approximately unbiased, or simply a heuristic with variance-reduction flavor.

4. The treatment of rewards across equivalent partial expressions in the MCTS section is hand-wavy where it should be careful. On **Pages 5-6**, the paper states that for equivalent partial-expression nodes \(s_1\) and \(s_2\),
\[
\texttt{reward}(s_1,a)\approx \texttt{reward}(s_2,a), \qquad \forall a.
\]
This is plausible only under nontrivial conditions: identical rollout completion policies, identical handling of invalid completions, identical coefficient fitting behavior, and no domain failures introduced by rewrites. But the paper later notes in **Appendix B.2** that many rewrite rules are only valid on restricted domains, for example \(\log(ab)\rightsquigarrow \log a+\log b\) requires positivity conditions. If the rollout distributions or numeric evaluation differ after rewriting, the “same reward” intuition can fail in practice. The theory and method would be cleaner if the authors distinguished semantic equivalence in exact algebra from equivalence under the actual floating-point evaluation and dataset domain used during training.

5. The empirical evaluation is encouraging but still too thin for the breadth of the framework being advocated. For MCTS and DRL, the main quantitative evidence is concentrated in **Table 1**, which only reports trigonometric datasets from one source and only compares against each backbone with and without Egg. That establishes local gains, but not broader competitiveness. There is no comparison in the main paper against stronger non-MCTS, non-DRL SR systems on these tasks, and no evidence that the framework remains useful outside expression families rich in the specific rewrite rules used here. The authors themselves note that the trigonometric datasets were selected because they contain many symbolic-equivalence variants. That is fair as a proof of concept, but it also means the evaluation is somewhat tailor-made to favor the proposed mechanism.

6. Related to the previous point, the LLM evidence in **Table 2** is difficult to interpret as a strong standalone contribution. The improvements are modest on several datasets, mixed across models, and the baseline numbers for LLM-SR are partly taken directly from the original paper rather than fully reproduced under a unified implementation. For example, on bacterial growth, Mistral without Egg is actually better than Egg-LLM on both IID and OOD; on stress-strain, Egg-LLM helps, but the margins are small. Since the Egg-LLM contribution is mostly a prompt-augmentation heuristic rather than a theoretically grounded algorithmic change, I would have preferred stronger controlled ablations, such as varying the number of equivalents in the prompt, comparing against random paraphrase augmentation, or testing whether prompt length itself explains part of the gain.

7. Several figures support the paper’s claims only partially, and the authors occasionally over-interpret them. **Figure 3 (left)** shows Egg-MCTS having a larger search tree than vanilla MCTS. The text on **Page 8** interprets this as “broader and deeper” exploration and “a larger and more diverse search space.” But the connection between larger tree size and better effective exploration is not automatic. If equivalence sharing allows the algorithm to avoid redundant subtrees, one might also expect fewer explicit nodes in some regimes, depending on implementation. Similarly, **Figure 3 (right)** plots empirical mean and standard deviation of an estimated quantity for DRL, but the plotted objective is described as \(R(\tau_i)\log p_\theta(\tau_i)\), whereas the policy gradient in **Equation (3)** involves \((R-b)\nabla_\theta \log p_\theta(\tau_i)\). The figure is therefore, at best, an indirect proxy for gradient variance, not a direct empirical validation of **Theorem 3.2**. The paper should be more precise here.

8. There are multiple clarity and consistency issues in notation, definitions, and even some formula writing. A few examples:
   - **Equation (1)** defines \(\phi_1 \equiv_{\mathcal R} \phi_2\) using “\(\phi_1 \Rightarrow^* \phi_2\) or \(\phi_2 \Rightarrow^* \phi_1\),” which is not the usual symmetric-transitive closure definition one would expect from an induced equivalence relation under bidirectional rewriting. As written, this can fail to capture equivalence through a common descendant or ancestor unless the rewrite system has special properties.
   - In **Table 4** on **Page 30**, the reward function is listed as \(1/1+\mathrm{RMSE}(\phi)\), which is ambiguous due to missing parentheses and also inconsistent with the NMSE-based reward discussed elsewhere.
   - On **Page 10**, **Figure 4 (right)** caption repeats \(\sin(a)\cos(b)+\sin(a)\cos(b)\), which looks like a typo instead of \(\sin(a)\cos(b)+\sin(b)\cos(a)\).
   - The main text alternates between “EGG” and “Egg,” “E-graph” and “e-graph,” and there are multiple naming inconsistencies such as “EGG-MTCS” / “MTCS” in **Table 1**.
   These issues are individually minor, but collectively they reduce confidence that the mathematical and empirical story has been polished to the level expected for a top venue.

9. The domain-validity issue is more serious than the paper admits. In **Appendix B.2**, the authors explicitly note that some rewrite rules are only valid on feasible domains and that invalid rewrites may produce \(-\infty\) or NaN during evaluation. Yet the main method does not seem to enforce rule preconditions when constructing equivalence classes. This means the equivalence relation used by Egg can be semantically unsound over the actual dataset distribution. If a rule is only conditionally valid, then merging expressions in the e-graph without tracking assumptions can collapse non-equivalent candidates. In symbolic mathematics this is a known sharp edge, and for a paper built around equivalence-aware learning, it deserves much more than a brief appendix remark.

10. The extraction procedure in **Section 3.1** and **Appendix B.3.2** is also under-motivated. The method uses random-walk sampling to obtain \(K\) representative expressions from a saturated e-graph, but the paper does not analyze or characterize the distribution induced by this sampler. This matters because the practical effect of Egg-DRL and Egg-MCTS depends strongly on which equivalent variants are surfaced. If the sampler is biased toward short or shallow forms, some equivalence classes may be poorly represented; if it is nearly uniform over nodes rather than expressions, it may overweight specific syntactic templates. Without at least an ablation over \(K\), saturation depth, and extraction strategy, it is hard to tell whether the reported gains come from principled equivalence aggregation or just from a favorable stochastic augmentation policy.

## Questions
1. For **Equation (4)** and **Theorem 3.2**, is the implemented Egg-DRL estimator unbiased for the actual sampled subset of \(K\) extracted variants, or is the unbiasedness proof intended only for the idealized estimator using the full equivalence class \(q_\theta(\phi)=\sum_{\tau\in\mathcal S_\phi} p_\theta(\tau)\)? Please answer this very explicitly. If the implemented estimator is only approximate, please state the approximation and whether there is any empirical evidence that the bias is small.

2. In the MCTS part, are you actually using UCT as written in **Equation (2)**, or an OPD-style planner required by the theorem? If it is UCT in experiments, then the main theorem does not directly analyze the tested algorithm. A precise statement of what is proved for what algorithm would increase my confidence.

3. How are rewrite-rule preconditions handled in practice? The discussion in **Appendix B.2** acknowledges that rules like \(\log(ab)\rightsquigarrow \log a+\log b\) are domain-restricted. Do you filter rewrites based on the sampled data domain, or can the e-graph merge expressions that are only conditionally equivalent? This is important because your central object is an equivalence class.

4. Please provide ablations on the rewrite set, saturation budget, and number \(K\) of extracted equivalents. Right now, the empirical story leaves open whether gains come from a small handful of highly effective trigonometric rules or from a genuinely robust framework.

5. For the LLM setting, could you compare EGG-based prompt enrichment against a control that adds the same number of syntactic alternatives or simplifications not derived from e-graphs? This would help isolate whether the gains in **Table 2** come from equivalence-aware feedback specifically, rather than from simply giving the LLM more examples.

6. Can you report more direct evidence of variance reduction for DRL? **Figure 3 (right)** is suggestive, but it does not directly estimate \(\mathrm{Var}[g_{\texttt{egg}}]\) versus \(\mathrm{Var}[g]\). Even per-parameter gradient variance statistics on a small benchmark would help.

7. The main results would be more convincing with at least one broader benchmark beyond the trigonometric-heavy setting in **Table 1**. If you have results on more heterogeneous expression families using the same backbone and time budget, that would strengthen the paper materially.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper appears to use public datasets and standard open-source or publicly available models, and I did not identify a concrete ethics issue from the main paper that would warrant escalation. The main concerns here are scientific, namely correctness of the equivalence assumptions and the scope of the empirical claims, rather than ethics-specific.

## Soundness Rating
3: good. The core idea is technically plausible and supported by some theory and experiments, but several main claims are qualified by hidden assumptions, especially the mismatch between the UCT-style MCTS presentation and the OPD-style regret analysis, and the gap between the idealized DRL proof and the sampled-\(K\) implementation.

## Presentation Rating
2: fair. The high-level narrative is understandable, and some figures, especially **Figure 1** and **Figure 2**, are useful, but the paper has enough notation issues, theorem caveats, typos, and imprecise claim phrasing that clarity falls short of where it should be.

## Contribution Rating
3: good. I do think the paper makes a meaningful contribution by showing how e-graph-based equivalence handling can be embedded into multiple symbolic-regression paradigms, but the contribution is more incremental and framework-oriented than the framing sometimes suggests, and the empirical scope is not broad enough for a higher score.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a real and useful idea, and the cross-framework integration is interesting enough that I can justify a weak positive recommendation. That said, the theoretical story is looser than advertised, the empirical validation is narrower than the framework claims, and the exposition needs tightening.

## Reviewer Confidence
4: confident. I am confident in the main points of this assessment and checked the technical claims and experiments with care, although some implementation-level details would benefit from clarification in rebuttal.