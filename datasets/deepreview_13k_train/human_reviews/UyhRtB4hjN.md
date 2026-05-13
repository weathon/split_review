# Decision Tree Induction via Semantically-Aware Evolution

- Decision: Accept
- Scores: 8, 6, 5, 6

## Abstract
Decision trees are a crucial class of models offering robust predictive performance and inherent interpretability across various domains, including healthcare, finance, and logistics. However, current tree induction methods often face limitations such as suboptimal solutions from greedy methods or prohibitive computational costs and limited applicability of exact optimization approaches.
To address these challenges, we propose an evolutionary optimization method for decision tree induction based on genetic programming (GP). Our key innovation is the integration of semantic priors and domain-specific knowledge about the search space into the optimization algorithm. To this end, we introduce $\texttt{LLEGO}$, a framework that incorporates semantic priors into genetic search operators through the use of Large Language Models (LLMs), thereby enhancing search efficiency and targeting regions of the search space that yield decision trees with superior generalization performance. This is operationalized through novel genetic operators that work with structured natural language prompts, effectively utilizing LLMs as conditional generative models and sources of semantic knowledge. Specifically, we introduce _fitness-guided_ crossover to exploit high-performing regions, and _diversity-guided_ mutation for efficient global exploration of the search space. These operators are controlled by corresponding hyperparameters that enable a more nuanced balance between exploration and exploitation across the search space. Empirically, we demonstrate across various benchmarks that $\texttt{LLEGO}$ evolves superior-performing trees compared to existing tree induction methods, and exhibits significantly more efficient search performance compared to conventional GP approaches.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents an application of LLMs as a crossover and mutation operator in an evolutionary algorithm. The authors propose “LLM-Enhanced Genetic Operators” (LLEGO), which uses fitness guided crossover and diversity guided mutation to infer decision trees from data. The proposed method (LLEGO) is compared against other decision tree induction algorithms on classification and regression tasks.

### Strengths
- The paper is very well written and easy to follow. The motivations for the proposed methods are detailed well.
- The experiments are well detailed, fitting, and the proposed approach is compared against a good number of baselines. There were very rigorous additional results, addressing issues such as fairness and generalization. Upon the first read, I was concerned that the results might be highly conditional on the solutions existing in the training set of the LLMs, but Appendix D.2 settled my concern.
- The use of LLMs in the loop of an evolutionary algorithm for decision tree induction is, to my knowledge, novel and, in my opinion, very promising.

### Weaknesses
 - I would have been very interested in seeing a different use of selection algorithms, as fitness-proportionate (roulette wheel) selection is somewhat outdated and known to result in low population diversity. For example, perhaps the use of tournament or lexicase selection could adequately balance fitness and diversity?
- You use mutation as purely a technique to inject diversity into the population. I would have been interesting in seeing how “fitness-guided” mutation would perform (i.e. remove XO, and prompt the LLM to generate a better version) as a baseline. This would help motivate the use of XO/mutation as a means to explore/explore, respectively.

small typo:   
- At the beginning of section 3 - “buid” should be “build”

### Questions
- The choice of using natural language as the representation for the evolutionary algorithm is fitting  as they need to be used by an LLM-based genetic operation. Do you imagine there being any ways to improve the syntactic validity from ~86% of the decision trees being outputted by your genetic operators?
- Is there any reason (beyond representation in natural language) that this method could not be used for symbolic regression or more general function induction?
- How well would the method work when starting without initializing with CART models on 25% of the training data?

### Soundness
4

### Presentation
4

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
The paper proposes an innovative method for decision tree induction using genetic programming (GP) enhanced by semantic knowledge from large language models (LLMs). The key contribution is the LLEGO framework, which introduces semantically-aware genetic operators: fitness-guided crossover and diversity-guided mutation. These operators leverage semantic priors from LLMs to improve search efficiency and decision tree generalisation performance. The method is empirically validated on various tabular datasets, demonstrating superior performance compared to traditional and state-of-the-art tree induction methods.

### Strengths
* The integration of LLMs into GP is a significant advancement. Using LLMs to inform genetic operators with semantic priors is a creative and impactful idea, enhancing both search efficiency and the quality of generated decision trees.
* The paper provides a detailed explanation of the LLEGO framework, including how LLMs are utilised and how genetic operators are implemented. The end-to-end algorithm is clearly described, making it easier to understand the overall workflow.
* The paper addresses the limitations of existing decision tree induction methods by offering a scalable and generalisable approach, which could be beneficial across various domains.

### Weaknesses
 * The effectiveness of LLEGO depends heavily on the semantic priors embedded in the LLM. If the LLM lacks relevant knowledge for a particular domain or problem, the performance might degrade. A discussion on this limitation and possible solutions would be helpful.
* While the empirical results are strong, the paper lacks a rigorous theoretical analysis of why and how the semantic priors from LLMs improve search efficiency. This could strengthen the understanding of the method’s underlying principles.
* The paper focuses on decision tree induction, but it is unclear how well the approach generalises to other GP-based tasks. A brief discussion or some preliminary results in this direction would make the contribution more comprehensive.

### Questions
* How does the computational overhead of using LLMs in LLEGO compare to traditional GP approaches in terms of runtime and memory usage? Are there any scenarios where the increased cost might not be justified? Provide a more detailed analysis of the computational cost and scenarios where the trade-off is most beneficial. Consider discussing potential optimisations or the use of smaller LLMs.

* How does the performance of LLEGO change if the underlying LLM lacks semantic priors relevant to a particular problem domain? Are there strategies to mitigate performance degradation in such cases?

* Include a theoretical explanation of how semantic priors impact search efficiency and decision tree quality. This would strengthen the paper’s scientific contributions.

* Do the authors have any preliminary insights or results on how well LLEGO could be applied to other GP-based problems, such as symbolic regression or evolutionary program synthesis? Test how LLEGO might perform in other GP-based problems, such as symbolic regression or program synthesis, to show the method’s broader applicability.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose using LLMs as evolutionary operators to evolve decision trees.

### Strengths
The strength of this paper is that it explores decision tree induction in the era of large language models and shows promising results compared to traditional evolutionary algorithms and optimal decision tree induction methods.

### Weaknesses
Based on the experimental results, it seems that LLMs can achieve better generalization performance than traditional decision tree induction methods in some cases. I have raised the score to 5, as this paper demonstrates that ChatGPT can induce decision trees with improved generalization performance.

However, the main concern is that it is still unclear what mechanisms enable LLMs to achieve better generalization performance. This uncertainty may hinder the applicability of the proposed method, as we do not know when this method can be effectively used and when it cannot.

I acknowledge that the authors have conducted experiments on GPT-3.5 and GPT-4 to confirm that the proposed method works on different versions of GPT models. However, without understanding the mechanisms that allow LLMs to induce decision trees with good generalization performance, the proposed method may fail in the future if OpenAI significantly changes its ChatGPT models.

The authors have presented an example of spurious correlation. In my understanding, in this example, the authors explicitly informed the LLM that certain features were spurious. If we have such prior knowledge, these features should ideally be eliminated before the machine learning pipeline, rather than relying on the algorithm to address them.

Besides concerns about generalization, I am also not entirely convinced about using LLMs to solve MIP problems like decision tree induction. Performing arithmetic calculations remains a challenging task for LLMs [1].

While I agree that LLMs can perform feature selection to improve generalization performance [2], the current evidence is still not convincing enough to demonstrate that LLMs can effectively split the feature space recursively.

### Questions
Here are several questions that need to be addressed:
1. The most important issue in this paper is the claim that existing optimal decision tree methods are computationally complex, with complexity scaling exponentially with depth and the number of possible splits in the dataset. However, in the experimental results, the authors show their method with depths of 3 and 4, which can actually be solved by optimal decision tree induction methods, such as DL8.5 [1]. As shown in the DL8.5 paper, with a depth limit of 4, DL8.5 can find the optimal decision tree in 19 out of 24 cases within 10 minutes. It is unclear why the authors chose to use LLMs, an expensive method, to address this issue.

2. The idea of using large language models for evolving programs with diversity considerations is not novel. For example, the GECCO 2024 paper "LLMatic: Neural Architecture Search via Large Language Models and Quality Diversity Optimization" [2] already considers this. Also, using random selection for parent selection in diversity-guided mutation is insufficient. Please consider quality-diversity optimization for parent selection.

3. Please report the training accuracy as well. It is hard to understand why the proposed method would outperform optimal decision trees within depths of 3 and 4.

4. The proposed method is tested on GPT-3.5. Are the conclusions applicable to other models, such as GPT-4 or Claude? Please conduct experiments to verify this. Analyzing the sensitivity of the proposed method to different LLMs is also important.

5. The paper claims one advantage of the proposed method is using LLMs to apply semantic information to guide the search. However, the conclusion of Table 7 shows that LLMs work well even when semantics are removed. The authors should reconsider why LLMs perform well in this context.

6. The term "semantic information" seems more like "domain knowledge" rather than the commonly understood meaning of semantics in the genetic programming domain. Please consider changing the term or at least add an explanation to clarify the difference. Otherwise, it could be confusing.

References:

[1]. Aglin, Gaël, Siegfried Nijssen, and Pierre Schaus. "Learning optimal decision trees using caching branch-and-bound search." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 34. No. 04. 2020.

[2]. Nasir, Muhammad Umair, et al. "LLMatic: Neural Architecture Search via Large Language Models and Quality Diversity Optimization." Proceedings of the Genetic and Evolutionary Computation Conference. 2024.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel framework LLEGO that leverages LLMs to enhance genetic programming (GP) for decision tree induction. LLEGO incorporates semantic priors and domain knowledge into the optimization process through LLM-based fitness-guided crossover and diversity-guided mutation operators. The framework represents decision trees in natural language, enabling the use of broader contexts and higher arity operations. Empirical results on various benchmarks demonstrate LLEGO's superior performance over existing tree induction methods in terms of search efficiency and the quality of the evolved decision trees.

### Strengths
- Combining LLM and EA for decision tree induction is novel.
- The introduction of fitness-guided crossover and diversity-guided mutation is well-motivated.
- Strong empirical performance compared with the conventional GP method.
- The paper is well-written and easy to follow, and it is accompanied by good visualization.

### Weaknesses
 - **Crossover**: Is fitness guidance truly necessary? Could we instead prompt with "improve on the above decision trees" and still achieve comparable performance? Have you conducted any ablation studies on this?

- **Mutation**:
  - Are the log probabilities of within-population solutions consistently higher than those of out-of-population solutions? Have you verified this in your experiments?
  - According to your experiments, LLEGO sacrifices population diversity compared to traditional GP due to its semantic priors. Could you implement mutation alone to preserve population diversity? If not, does this suggest that the designed diversity-guided mutation operator fails to maintain sufficient diversity?

### Questions
- Can LLEGO be extended to other string optimization problems, or is it currently too specialized for the Decision Tree Induction benchmarks it addresses?
- What does "LLEGO_no_prior" mean? Have you compared LLEGO to vanilla LLM evolution without semantics guidance in crossover or diversity guidance in mutation?
- Recent work has incorporated semantic priors generated by LLM reflections into the evolutionary process [1]. A discussion of how this approach relates to LLEGO would be beneficial.

[1] ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution, NeurIPS 2024

### Soundness
3

### Presentation
3

### Contribution
3
