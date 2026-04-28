# RethinkMCTS: Refining Erroneous Thoughts in Monte Carlo Tree Search for Code Generation

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 3, 6, 6

## Abstract
LLM agents enhanced by tree search algorithms have yielded notable performances in code generation. However, current search algorithms in this domain suffer from low search quality due to several reasons: 1) Ineffective design of the search space for the high-reasoning demands of code generation tasks, 2) Inadequate integration of code feedback with the search algorithm, and 3) Poor handling of negative feedback during the search, leading to reduced search efficiency and quality. To address these challenges, we propose to search for the reasoning process of the code and use the detailed feedback of code execution to refine erroneous thoughts during the search.
In this paper, we introduce \our{}, which employs the Monte Carlo Tree Search (MCTS) algorithm to conduct thought-level searches before generating code, thereby exploring a wider range of strategies. More importantly, we construct verbal feedback from fine-grained code execution feedback to refine erroneous thoughts during the search. This ensures that the search progresses along the correct reasoning paths, thus improving the overall search quality of the tree by leveraging execution feedback.
Through extensive experiments, we demonstrate that \our{} outperforms previous search-based and feedback-based code generation baselines. On the HumanEval dataset, it improves the pass@1 of GPT-3.5-turbo from \textbf{70.12} to \textbf{89.02} and GPT-4o-mini from \textbf{87.20} to \textbf{94.51}.}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposed a MCTS variant that allows node level self-refinement as a alternative way to ``expand'' the search tree with ``refined nodes''. This refinement method prompt an LLM to self-refine the thought and corresponding code, conditioned on a erroneous node. In addition to the public test cases, the authors incorporated ``block-level analysis'' and ``LLM self-evaluation'' as feedback signals to improve the evaluation of search rollouts.

### Strengths
- The problem, search in LLM code generation, is very relevant
- Ablation in Figure 3 shows each component plays certain role in the framework

### Weaknesses
 - The evaluation strategy and refinement in tree search appears to be stitched for final performance but are totally irrelevant strategies. As the paper is titled as RethinkMCTS, adding additional feedback effort may make it more difficult for the audience to evaluate the role of ``rethink''.
    - for example, RethinkMCTS without VF (39 in Figure 3) can be lower than PG-TD (40 in Table 1) for APPS Intro. It is not clear what is the performance of rethink only, in comparison with the baselines, as the baselines are mainly about correction/refinements.


- My biggest concern is that, if my understanding is correct, since RethinkMCTS can have maximum 16 rollouts (meaning maximum 16 evaluations with public tests), it is not fair to compare ``pass@1'' to the base model.
    - A important baseline is: run 16 responses with a base model, and then filtered out those failed public tests, and then compute pass@1 using the responses which are correct for public tests for instance by randomly sample 1 multiple times and take the average.
    - If an additional evaluation is available, then another baseline could be best-of-N with such evaluation. For example, with the responses passed the public tests, one could for example use LLM to rank and select the BON

### Questions
- ToT appears very strong in the baselines, a more comprehensive comparison with ToT might be helpful to understand the contributions
    - According to my understanding the major differences are: RethinkMCTS has refine but ToT not, and the difference between evaluation strategy.
    - A comprehensive ablation should be conducted versus ToT:
        - There should be one more case: w Rethink only in Figure 3 so that the audience could understand how the Rethink mechanism improves ToT
        - While conducting the experiment with Rethink only, please include all difficulty levels (and both models as well), 

- Minor points:
    - Please add an average pass rate/pass@1 for APPS (weighted by number of problems in each difficulty level)
    - PG-TD has 43.16 for APPS Comp. with 4o-mini but RethinkMCTS's 42.50 was bold instead.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, the authors propose an enhancement of Monte-Carlo Tree Search, named RethinkMCTS, that refines reasonings with feedback in code generation tasks. The search incorporates both execution feedback and verbal feedback to refine reasonings. Empirical evaluations on two coding benchmarks show modest pass metrics improvements over existing baselines.

### Strengths
1. This paper is well-written and easy to understand. The various feedback and the rethink process are integrated quite well.

2. The included baselines are comprehensive.

### Weaknesses
1. The novelty of this paper seems limited. I am struggling to understand the difference from the LATS and ToT work. In comparison, it seems like the proposed method is essentially LATS + ToT? If that is correct, I think the contribution is of limited significance.

2. The improvements over baselines, especially ToT, are small. With GPT-4o-mini, the differences were quite small. As there are no confidence intervals, there is doubt about the statistical significance of those improvements.

3. It is unclear to me whether the experiment results in Table 1 were controlled for the number of tokens across different methods, which is crucial for a fair comparison. Please provide more details about the comparison setting.

4. One part of the novelty is the block-level feedback, however, there is no example given for what this type of feedback looks like and no explanation about implementation details. Please provide more information.

### Questions
Please see the weakness section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes an MCTS-based approach to incorporate reasoning into code generation. A key hypothesis is that searching in the space of thoughts is better than searching in the space of code, and that searching in thought space allows the LLM to explore better as well as have a higher quality of search by refining its intermediate outputs. The feedback used in MCTS is a combination of scalar feedback and verbal feedback generated by the LLM. This approach differs from other reflection-based approaches using tree search in that intermediate nodes in the tree are refined so that the LLM can follow a better path to the solution using the reasoning provided in the form of verbal feedback. This work also proposes combining LLM self-evaluations with public test cases to evaluate the generated code, to compensate for the low coverage of public test cases with respect to the problem, leading to inaccurate assessment of the generated solution. The results of the proposed RethinkMCTS approach are demonstrated on the HumanEval and Apps datasets, for GPT-3.5-turbo and GPT-4o-mini.

### Strengths
- The paper proposes a neat, conceptually simple way of doing MCTS in the space of LLMs for code generation.
- This work suggests an alternative to current approaches to handle incomplete coverage of solutions by public test cases by proposing LLM self-assessment instead of generating synthetic test cases that may not always be accurate.
- The method section is written well, clearly outlining the different parts of the MCTS algorithm and what they correspond to in this context, as well as the additional verbal feedback and rethink stages that are the novel contributions of the proposed approach.
- The ablation results in Figure 3 and Figure 6, and the search granularity results in Figure 4 and Figure 7 tie together each individual contribution in the paper with the main rethink hypothesis in the paper.
- The proposed approach is compared with several feedback based and tree-search based baselines.

### Weaknesses
 - In Table 1, the RethinkMCTS results have been marked in bold, which I presume indicates the superior performance of this method over other baselines. However, it seems to be the case that for GPT-4o-mini, the results shown by the Tree-of-Thought baseline are in most cases, at par with RethinkMCTS, and the pass rate of PG-TD on APPS-Comp is actually higher than that of RethinkMCTS. This table would be clearer to read if the best baselines that are at par with or better than RethinkMCTS were also highlighted.
- The absence of standard errors in Table 1 makes it difficult to see if the performance improvements are significant or not.
- One important detail that would warrant some discussion in this paper is the number of LLM calls used to generate the final output. Ideally for a fair comparison with baselines, this would be an important parameter to standardise, since recent work in inference-time approaches have shown that given more compute during inference, LLMs can exhibit superior performance. If the baselines use fewer LLM calls at inference time than RethinkMCTS to generate the final output, this would not be a fair comparison.
- The choice of datasets and models makes the evaluation of this approach difficult: given that the base models already show strong performance on these datasets, it becomes difficult to assess the contribution of this approach, which has several components, in increasing performance. If this approach shows significant gains in performance, for either a) a more difficult dataset, or b) weaker models, that might make the strength of the approach as well as its individual components clearer.
- Minor: There is an overloading of the term $a$, in some places it is used to denote the action, in others it is used as a coefficient for the reward weight vector.

### Questions
- The improvements shown by RethinkMCTS compared to other baselines seem to be more pronounced on GPT-3.5-turbo compared to GPT-4o-mini. Is there anything that can be inferred from this result that can tie the effectiveness of this approach with the capabilities of the base model?
- In Figure 3, the result on HumanEval indicates that the rethink mechanism seems to have the least effect out of all components on performance. For all of the other results as well (except APPS Intro. in Figure 6), the rethink component is not the most impactful in determining performance. This appears to be contrary to the claim of this paper. Could the authors clarify how these results were interpreted?
- In Figure 5(a), as the number of rollouts increases from 43 to 58, the performance with rethink reduces, which is counterintuitive. The result in 5(b) is more consistent with what we could expect as we increase the number of rollouts: performance would plateau beyond a certain number of rollouts. Could the authors provide an explanation for why we see the drop in performance in Figure 5(a)?
- The numbers in Table 3 are very different from those in Figure 3; is it a different metric, model, or dataset?
- GPT-4o-mini has comparable token-level search performance compared to RethinkMCTS on HumanEval; is it possible that HumanEval is not the best testbed for this approach, given that base performance is already quite high?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to use Monte-Carlo tree search to discover useful rationale for code generation. It also incorporates block-level info feedback and self-evaluation for better value estimate of nodes in the tree. Experiment results show that the proposed method achieves SOTA performance compared to other augmented code generation method, such as reflexion and tree-of-thoughts.

### Strengths
The propose method is novel and provides a nice way to combine MCTS and chain-of-thoughts. The paper is well-written and easy to understand.

### Weaknesses
The experiment results can be further strengthen:
1. for such a searching algorithm, the results between different runs might differ a lot. Thus, it is better to incorporate std information for pass rate.
2. The run time of different algorithms should also be compared.

### Questions
Nothing necessary stands out.

### Soundness
3

### Presentation
3

### Contribution
3
