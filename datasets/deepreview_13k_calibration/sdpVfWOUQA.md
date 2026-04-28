# Planning with MCTS: Enhancing Problem-Solving in Large Language Models

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3

## Abstract
Despite recent advances in Large Language Models (LLMs), their ability to solve complex reasoning problems remains limited by inconsistent planning and logical flaws. We present a novel framework that significantly enhances LLMs' problem-solving capabilities by leveraging Monte Carlo Tree Search (MCTS) for plan generation. Unlike previous approaches that apply MCTS to solution search, our method uniquely integrates MCTS into the planning phase, guided by specialized LLM-powered agents that evaluate plan quality. Experiments across diverse benchmark datasets demonstrate that our approach improves problem-solving accuracy by an average of 40.59\% compared to zero-shot Chain-of-Thought prompting. Furthermore, we show that using smaller models for MCTS planning and larger models for execution can maintain high performance while reducing computational costs. This work opens new avenues for developing more robust and efficient AI systems capable of tackling complex real-world problems, with potential applications in fields requiring advanced logical reasoning and long-term planning. Our code examples are publicly available at the Anonymous Github Repository.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper explores the use of Monte Carlo Tree Search (MCTS) in the context of planning, arguing for a distinction between planning and reasoning steps.

### Strengths
* The authors present a framework that aims to separate planning and reasoning, which could lead to new insights in this area.

### Weaknesses
 * The distinction between planning and reasoning is not sufficiently articulated, leaving readers unclear about their specific roles and how they interact. This lack of clarity undermines the proposed framework.
* The impact of the evaluation of intermediate nodes on MCTS performance is significant but not discussed in depth. This oversight may lead to an incomplete understanding of the method's effectiveness.
* Applying MCTS to planning is somewhat diminished by the fact that this approach is already well-established in the literature. The paper would benefit from a more thorough comparison with existing methodologies to highlight its contributions.

### Questions
1. Could you have a more detailed clarification about how planning and reasoning are defined in your framework? What specific characteristics differentiate them?
2. The performance of MCTS appears to be influenced by how intermediate nodes are evaluated. Could you provide insights or analysis on this aspect within your methodology?
3. Are there specific scenarios or use cases where your proposed separation provides a distinct advantage over existing integrated approaches?
4. Consider providing a more detailed background on related work to situate your contributions within the existing body of research.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an alternative to Chain-of-Thought (CoT) for enhancing LLM planning and accuracy in multi-task problems.

Given a problem, the method formulates an initial plan by prompting an LLM, and then iteratively creates variations (i.e. mutations) of that plan to produce new plans. New plans are evaluated for their "logical consistency" and "feasibility" using another LLM, and the decision of which node in the tree to expand (i.e. mutate) next is done using a variant of UCB1. 

Once the planning budget or allocated time is depleted, the method selects the plan or node with the highest average reward. That plan is then added to the LLM prompt along, and the LLM generates a solution for the problem.

The paper evaluates this method against CoT on small models of the Llama and Qwen family of models. The authors also do some ablations on search depth, number of rollouts and evaluation functions for their agents. 

Finally, the paper studies using smaller LLMs to provide plans for larger ones in order to strike a balance between efficiency and performance.

### Strengths
Given the inherent computational costs of planning, the inclusion of a study to use smaller LLMs to provide plans for larger ones is very welcome.

The paper is generally well organized.

The code release is definitely a strength, and at a glance the code looks clean and easy to use.

### Weaknesses
 **1. Lack of clarity and error in Section 2.1**

I found Section 2.1 very hard to follow, which is a problem since the method formulation builds on top of it. In particular $C_\textrm{problem}$ is the "problem description", but $X$ denotes in two places "reasoning steps" (lines 140 and 159) and in another $X$ is the "problem" (line 151).

Then, the factorization in Eq. 2 only holds if $P(X|C) = 1$, which cannot be true since planning then involves a search over reasoning steps X. Is this a typo?

**2. This is not MCTS**

As stated in Section 2.2, each  "*new node represents a modified version of the parent node’s plan.*", and the final output of the search algorithm is a single node, rather than a path through the tree, as is the case in MCTS.

Furthermore, the method does not perform Monte Carlo rollouts and instead evaluates each node individually by querying an LLM to assess the logical consistency and feasibility of the plan. 

As a result, *this method is not MCTS*. Instead, the method proposed is an evolutionary method using an LLM to mutate plans at inference time. 

**3. Lack of details on method and evaluators**

There are insufficient details on how the initial plan is sampled, how new plans are obtained by modifying old plans or how the evaluators work.

**4. Cannot find the main result in any of the tables.**

The headline result is that the proposed "_MCTS-enhanced planning approach outperforms the CoT baseline across most datasets, with
an average improvement of 40.59%_". Inspection of Table 1 shows that the largest relative improvement is $17.79 / 57.85 = 30.8$%. How did the authors arrive to the reported 40.59% figure?

**5. Tables are hard to parse and no uncertainty reported.**

Firstly, no measure of uncertainty is provided in the entire paper, making it hard to assess how significant the results are.

Secondly, tables are hard to parse. Authors should consider bolding the best results for each benchmark, or aggregating results over multiple models to help comparisons.  Table 2 would be best presented as plots, to better show the trend.

**6. Lacking baselines**

Authors compare to two baselines (CoT and CoT Plan). However, they compare to none of the methods they cited in their section 4.2. They also don't normalize any of their results by inference costs (or number of tokens). 

Authors dismiss those methods by saying that "_they predominantly rely on the LLM’s inherent reasoning abilities to generate plans_", but their method similarly relies on an LLM to generate plans.

### Questions
1. How do the authors arrive at the 40.59% figure?
2. Can the authors clarify Section 2.1, and whether equation 2 contains a typo?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to use Monte Carlo Tree Search (MCTS) in the planning stage of using LLM to solve reasoning problems. The authors use comprehensive experiments to show that the proposed method can be better than CoT prompting. The authors also discuss the possibility of using smaller model to plan while using a larger model to evaluate and execute.

### Strengths
- The idea of using MCTS in the planning stage is relatively novel compared to many recent works on directly using MCTS in the reasoning stage. 
- The proposed algorithm is tested on a diverse combination of models and datasets.

### Weaknesses
 - While the cost is mentioned multiple times in the paper, there are no results showing the cost. This leads to two major problems: 1). how much motivation do we have to use the smaller LLM to generate a plan and let the bigger model execute? How much cost is it saving from the original setting, and how much cost is it requiring compared to CoT prompting? 2). If the cost is relatively high, can MCTS perform better than simply sampling N times and choosing the best one, i.e, BoN based on reward?
- The comparison in the experiment does not seem to be strong enough to me. Given that MCTS is already spending more cost, other popular methods used in reasoning that could improve the performance with some cost should also be considered, for example, ReAct [1], Reflexion [2]. It is also noteworthy that there is some work on prompt engineers that use MCTS or "gradient descent" [3, 4, 5]. While the domain does not seem directly applicable, a comparison is still needed, or clear clarification should be included in the paper.
- While the paper is overall easy to follow, the reproducibility of the paper is unclear as there are many important details missing, including the prompt used for many important implementation designs. Please refer to my questions for some examples. The discussion on certain failing cases is also highly recommended, especially since this is not even covered in the limitation section of the paper.

### Questions
1. While an ablation study is included in Tab. 2 in the paper, what is the default parameter used for the experiments in Tab. 1 and Tab. 3?
2. How is Q initialized? Is it all 0?
3. How is the expansion done? By another LLM? The prompt used is needed in this case.
4. While I believe that the cost of the proposed method is not so cheap, I am also interested to see what the performance is compared to directly using LLM in the reasoning stage, as given the cost constraint, these two directions probably cannot be used in the meantime.
5. Why is object tracking such a failure for the proposed method? It seems that in all models, MCTS is no better than CoT.

### Soundness
2

### Presentation
3

### Contribution
3
