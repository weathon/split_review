# Scattered Forest Search: Smarter Code Space Exploration with LLMs

- Decision: Accept
- Scores: 8, 6, 6, 5, 6

## Abstract
\vspace{-0.1in}
We propose a novel approach to scaling LLM inference for code generation. We frame code generation as a black box optimization problem within the code space, and employ optimization-inspired techniques to enhance exploration.
Specifically, we introduce \method to enhance solution diversity while searching for solutions. 
Our theoretical analysis illustrates how these methods avoid local optima during optimization. Extensive experiments on HumanEval, MBPP, APPS, CodeContests, and Leetcode reveal significant performance improvements.
For instance, our method achieves a pass@1 rate of 67.1\% on HumanEval+ and 87.2\% on HumanEval with GPT-3.5, marking improvements of 8.6\% and 4.3\% over the state-of-the-art, while also halving the iterations needed to find the correct solution. 
Furthermore, our method scales more efficiently than existing search techniques, including tree search, line search, and repeated sampling.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper frames code generation as a black box optimization problem within the code space, and employ optimization-inspired techniques to enhance exploration of the space. They introduce SCATTERED FOREST SEARCH to enhance solution diversity while searching for solutions. Their method improves performance by 4-8% on HumanEval+ and HumanEval

### Strengths
- A timely and appropriate direct of exploration for competitive programming tasks 
- Extensive experiments and ablations on different benchmarks
- Their proposed search mechanism provides a good boost in performance, also in comparison to other search methods

### Weaknesses
- All experiments are only based on gpt-3.5. Showing the performance on at least some SoTA open source llm is helpful to understand the generality of usage of this method.

### Questions
What is the actual cost of the tree-search base inference per instance in comparison to other prior search methods, for the same budget
Would be interesting to see whether such tree-search techniques prove helpful in popular challenging benchmarks like SWEBench

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on scaling inference computing of language models for code generation. The paper proposes Scattered Forest Search (SFS), which involves the following steps: 1) scattering: choosing different search directions given a solution; 2) foresting: starting searching from different initial solutions; 3) scouting: sharing insights across search branches.

Empirically, SFS outperforms some well-accepted baseline algorithms: Best of N (BoN) and tree search, on HumanEval, MBPP, and other coding benchmarks.

### Strengths
This paper is well-written and easy to follow. The illustrations and examples are beneficial for understanding the paper.

The SFS algorithm is overall presented clearly. Although it’s similar to most search-based algorithms in the literature, it has a novel design and outperforms BoN and tree search empiriically. Ablation studies are done to understand the contributions of each component (Sec. E).

### Weaknesses
## Primary Concerns

The paper can be stronger with more thorough empirical evaluations and clearer justification on why it’s better than tree search. Specifically:

**Empirical results.** The number of solutions generated is small (up to 10). How does the algorithm perform with larger numbers of solutions (k)? In our words, do MCTS and BoN catch up with SFS with larger k’s?

I’m not sure if the authors have considered the strongest baselines. The authors seem to use the standard MCTS algorithm (Eq. (1)). Have the authors considered P-UCT, which considers the probability of direction $d$ prescribed by the language model? See Eq. (3) in [2].

**Comparison with tree search.** Can authors clarify why tree search algorithms produce similar results (caption of Fig. 3)? Tree search algorithms like MCTS should do explicit exploration, so they inherently perform the scattering step in SFS?

## Other Comments

**Presentation.**
It would be clearer to have an algorithm block to clarify how the three components work together. Specifically, how does the global memory work? Do you only keep the global memory for the last few steps (otherwise it may not fit in the prompt)?

**Related work.**
FunSearch [1] has a similar idea of exploring the search space which is not mentioned in the paper.

**Miscellaneous:**

Line 208: si, di -> s_i, d_i.

Line 241-242: The insights will then be store[d] in the global memory.

**References:**

[1] Romera-Paredes, Bernardino, et al. "Mathematical discoveries from program search with large language models." Nature 625.7995 (2024): 468-475.

[2] Zhang, Shun, et al. "Planning with large language models for code generation." arXiv preprint arXiv:2303.05510 (2023).

### Questions
See my questions in the weakness section above.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper discusses the search strategy with LLM-based operators for code generation. It has an interesting prompting method to increase the diversity of LLM generations: first ask LLM to generate a list of chain-of-thoughts (COTs) and then ask LLM to generate code given each chain of thought. The generated COTs tend to be more diverse due to the itemized prompting and then the codes get more diverse. It also caches the chain of thoughts to reuse on other codes. One more claimed contribution is using a forest of search trees to "encourage exploration". It compares with simple baselines and reports improved performance in a customized setting.

### Strengths
The itemized chain-of-thought generation prompting method is interesting. It seems to be a general, intuitive, and easy-to-implement prompting method that could potentially be applied in many other reasoning-based domains where the diversity of LLM generations is important. It also unleashed the most significant improvement in the ablation study. I would recommend the authors to test this prompting technique in more domains such as generating math proofs. It would be an interesting addition to our toolbox for LLM-based reasoning. 

Code generation is an important domain to study.

### Weaknesses
* **Non-standard and vague experimental setting**s: This paper claims to use 6 self-generated test cases for each problem to solve. However, I couldn't find any related descriptions or details about how they generate them. The self-generated test cases are neither the contribution of this paper nor part of some public datasets/benchmarks. It is thus hard to reproduce and compare results from this paper with other methods in this domain. It is also unclear how many LLM requests/tokens they use in these experiments. 
* **Missing baselines; only simplest baselines**: There are many more papers discussing the search strategy with LLM-based code refinements/generation (exploration v.s. exploitation), such as Fun-Search [1] based on evolution search and REx[2] based on bandits algorithms. There are many more popular hard-coded tree expansion policies in the field such as [3,4].
* **Missing details of the method**: There are many confusing or missing descriptions of the method such as (1) the definition of rewards/values for each action/code; (2) how to initialize Q in UCB/MCTS; (3) how to generate test cases; (4) what is the overall pipeline? how many LLM requests for each "submission"? 
* **Complicated method; Unclear contributions of each component**: This paper includes many components in its method including (1) self-generated test cases, (2) itemized COT prompting, (3) UCB-based tree-expansion policy, (4) reusing COTs, (5) "foresting", and so on. It is unclear how each component contributes to the performance. I would suggest the authors perform ablation studies in a more common/standard setting, removing influences of components that are not part of this paper's contributions. 


[1] Romera-Paredes, Bernardino, et al. "Mathematical discoveries from program search with large language models." Nature 625.7995 (2024): 468-475.

[2] Tang, Hao, et al. "Code Repair with LLMs gives an Exploration-Exploitation Tradeoff." arXiv preprint arXiv:2405.17503 (2024).

[3] Olausson, Theo X., et al. "Is Self-Repair a Silver Bullet for Code Generation?." The Twelfth International Conference on Learning Representations. 2023.

[4] Wang, Ruocheng, et al. "Hypothesis search: Inductive reasoning with language models." arXiv preprint arXiv:2309.05660 (2023).

### Questions
See the weakness for details. 

* Are there clearer descriptions of the method, from the overall pipeline to each component such as the reward/value design? 
* Are there results without the self-generated test cases which are neither this paper's contribution nor part of standard benchmarks? 
* Are there results of more popular baselines than simple line-search? 
* Are there more detailed descriptions of the experimental settings, including how many LLM requests are used? 
* Are there ablation studies in a cleaner or more standard setting?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper propose a novel in-context learning workflow, which iteratively prompts a PLM to address diverse code generation tasks. Concretely, the authors proposes a reinforced tree search paradigm, termed 'scarttered forest search',  which first initializes multiple seed solutions through promping the PLM with diverse coding requirements, then proceeds the expansion of the forest search by selecting  the improvement direction with maximum UCT score. During the optimization, a global experience pool is maintained to help the exploitation. The results of the proposed searching paradigm show superiority to existing baselines, with certain diversity improvement.

### Strengths
Overall, the motivation of this paper is clear. The related works are properly elaborated. The experimental results are solid.

### Weaknesses
Although the motivation of this paper is quite clear, there are stll several issues on the rejection side:

1) The elaboration of the methodology is still far from sufficient clarity. In particular, what is the overall workflow of this paper? Can you provide a pesudocode?  

2) Besides, in Section 3.1, what is the 'b' in Eq. (1)? In Section 3.3, how do you utilize the collected insights exactly? In Section 3.4, I am confused about the improvement direction 'd', which is also generated by PLM, why it is rather diverse than concentrated?

3) For me, the importance of studying how to train a LM for accurate code generation outweights the importance of studying how to prompt a PLM. This is why I denote this paper as a 'fair contribution' one.  Could the authors provide an in-depth discussion on this point to at least reveal for future readers that there is a tradeoff between the above two research direction?

4)  The experimental analysis lacks a visualization or demonstration that the proposed method really escapes the local optimal, from the results in the shown tables, I can only say that the proposed method escapes the local optima found by previous method and falls into a nes local optima now. Can the authors give a clear demonstration of what they promised in the abstract: 'Our theoretical analysis illustrates how these methods avoid local optima during optimization.'

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes SCATTERED FOREST SEARCH to encourage LLMs to produce diverse outputs. The approach incorporates scattering, foresting, and scouting techniques to strike a balance between exploration and exploitation. Extensive experiments on code generation benchmarks demonstrate its effectiveness.

### Strengths
* This paper is well-organized and clearly structured.
* The proposed method is sound and novel.
* The author provides a theoretical foundation for the approach.
* The experiments are thorough, and the method demonstrates strong empirical performance.

### Weaknesses
* The notations in Section 3 are unclear and could benefit from clarification.
  * What does $b$ represent in Eq. (1)? 
  * The subscripts in lines 208-209 are incorrect.
  * In line 161, the specific direction is denoted as $d_i$, but $d_{0i}$ is used in line 206. 
  * How to initialize $\hat{Q}(s,d)$? 
  * How is $UCT(s,d)$ used to select directions? 
  * $s$ denotes the solution in Section 3.1, but $d$ is used in line 240.
  * It would be better to add a preliminary section to introduce MCTS.
* The proposed framework introduces several layers of complexity but lacks a discussion on time complexity. How does its efficiency compare to the baseline methods?
* Minor: The figures are not clear. Please use PDF format for better readability.

### Questions
* Has the time or space complexity been considered for the code generation task studied in this paper?
* How do you ensure that the textual directions are orthogonal, as mentioned in line 182?
* I'm curious about the performance of the proposed framework when applied to solve combinatorial optimization problems, such as TSP.

### Soundness
3

### Presentation
2

### Contribution
3
