# Integrating Expertise of Software Engineering Agents

- Decision: Accept
- Scores: 6, 6, 5, 8

## Abstract
Large language model (LLM) agents have shown great potential in solving real-world software engineering (SWE) problems. The most advanced open-source SWE agent can resolve over 27% of real GitHub issues in SWE-Bench Lite. However, these sophisticated agent frameworks exhibit varying strengths, excelling in certain tasks while underperforming in others. To fully harness the diversity of these agents, we propose DEI (Diversity Empowered Intelligence), a framework that leverages their unique expertise. DEI functions as a meta-module atop existing SWE agent frameworks, managing agent collectives for enhanced problem-solving. Experimental results show that a DEI-guided committee of agents is able to surpass the best individual agent's performance by a large margin. For instance, a group of open-source SWE agents, with a maximum individual resolve rate of 27.3% on SWE-Bench Lite, can achieve a 34.3% resolve rate with DEI, making a 25% improvement and beating most closed-source solutions. Our best-performing group excels with a 55% resolve rate, securing the highest ranking on SWE-Bench Lite. Our findings contribute to the growing body of research on collaborative AI systems and their potential to solve complex software engineering challenges.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces DEI (Diversity Empowered Intelligence), a framework designed to leverage the diverse capabilities of software engineering (SWE) agents. Through comprehensive analysis, the authors demonstrate that different SWE agents solve distinct sets of issues despite having similar overall performance metrics. The paper introduces DEI as a meta-module framework that harnesses this diversity through multi-stage rating and re-ranking, rather than attempting to build a single "best" agent. Their experimental results show significant improvements, with their best group achieving a 55% resolve rate on SWE-Bench Lite. The framework is well-documented with ablation studies and analysis.

### Strengths
- The paper is the first to investigate and establish that different SWE agents solve different types of issues.
- Proposes novel DEI meta-framework that uses diversity to build a better resolver than any single agent.
- Achieves 55% resolve rate on SWE-Lite beating baselines significantly.
- DEI-Base Open using open source LLMs achieves a 33% resolve rate outperforming many closed source LLMs.
- Well motivated with thorough analysis, and ablation studies.
- The release of code and prompts  makes the research reproducible.

### Weaknesses
 - While the authors demonstrate that different SWE agents solve different sets of issues, they provide no analysis of why this occurs (e.g., no investigation of which types of issues each agent excels at, or how agent architectures relate to their success patterns). This limits understanding of the relationship between agent design and issue-solving capabilities.

- The framework uses fixed agent groups (DEIBASE-1/2/Open) where all agents in a set contribute patches that are then scored. There is no learning mechanism to dynamically select agents based on past performance or issue characteristics. As a result, the system relies entirely on inherent diversity and fails to leverage agent specialization.

- DEI employs a fixed sequential review process (issue -> patches -> scoring) without iterative refinement or feedback loops between components. This linear approach potentially misses opportunities for improved patch selection that could be achieved through multi-round evaluation.

### Questions
- Could you provide a deeper analysis of why different agents excel at different issues? For example, have you analyzed patterns in the types of issues each agent solves successfully or investigated how specific agent architectures (e.g., execution vs non-execution-based agents) relate to their issue-solving capabilities?
- Could DEI's architecture be extended to provide feedback to the agents about why their patches failed, potentially enabling them to generate better patches?
- Could you provide a detailed analysis of DEI's failure cases? For instance, are there specific types of patches or issues where the scoring mechanism consistently makes wrong decisions?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes using an esamble of agents to increase the number of software engineering (SWE) problems that can be solved showing that using different agents for different problems is better than using a single agent for all. The approach is based on a reinforcement learning formulation.

### Strengths
* Important problem with significant real world value.
* The paper is well written and easy to follow.
* The evaluation clearly shows both the added value of the approach and how much better it could be.
* Considers both intra and inter agent diversity.
* Good potential to extend the approach, see questions.

### Weaknesses
 * It is unclear what new knowledge we have gained from the paper. That diversity is good is expected. To select the best candidate for each individual problem seems also expected. What is the unexpected or novel result of the paper? Or is the main result that you managed to get to work? - The authors clarified that it is how easy it is to achieve diversity and how significant it is.
* The significance of the approach might be on the low end. Since the approach is effective but straight forward, more elaborate analysis and/or experimentation would be expected. - Based on the authors response, the significance is higher than I initially estimated, but still somewhat limited.
* Some things are unclear, see questions. - Most of these were addressed by the authors.

### Questions
1) It seems to me that Eq. 3 expects the context to never change. Is that correct? (You fix the context, then you select the optimal policy for that context and then you use the expected reward from that policy.)
2) How do you select the optimal policy for a given context? Do you compute the expected reward for every policy given that reward and selected the highest? Or is this what is done in Step 3 Patch scoring?
3) Is there any learning involved in computing the DEI policy? It seems to me that the policies are given and then it is a deterministic computation to select the best of those.
4) Would it be possible to identify what the missing expertise is? I.e., if there was an agent capable of doing X, then the score would be significantly higher. There seems to be a potential to identify contexts that are far away from the contexts covered by the current policies. 
5) Have you considered composed policies? Maybe a but is complex and would require two different patches, i.e. first apply partial solution by agent a_i and then apply partial solution by agent a_j.
6) If you have as many members on the committee as you have different agents, wouldn't you always get the oracle answer? 
7) If the statement above is correct, wouldn't the interesting question be: What is the minimal number of members on the committee to get an acceptable score? What is the cost ($) benefit (resolve %) trade-off? The results would be much more interesting if the cost of running the different options would be included. It seems that you should be able to get a very clear analysis which would allow developers to estimate how much it would be worth to them to fix an issue.

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
The paper focuses on software engineering (SWE) agents, i.e., AI agents, in support of various software engineering tasks, such as code generation, automated testing, and project management. Specifically, in this work, the authors focus on AI agents' ability to resolve GitHub issues based on their descriptions. Observing that different SWE agents resolve different sets of issues successfully despite having similar resolve rates, the authors propose a method for organizing various SWE agents into ensembles with the intent to use the union of their expertise in resolving GitHub issues. The proposed method, Diversity Empowered Intelligence (DEI), is evaluated using realistic issue tracker data. The results show superior performance compared to single SWE agents' performances.

### Strengths
- The topic is important. There is a clear emerging need for systematic methods for using LLMs, especially for software engineering.
- The method seems to be novel.
- The quality of the experiments is solid.

### Weaknesses
 - The method is not exactly systematic, which limits its applicability and forces an ad-hoc way of working with ensembles of AI agents.

  - Sec 3.3.2, Equation 3: It is clear at this point that diversity is not purposefully engineered but rather: it's an emergent property of the system. One then has to wonder if this approach can be purposefully used in any problem or if its success will be rather non-deterministic and dependent on the problem at hand and its parameters (~ context).

  - Sec 3.3.2, L214-215: "The DEI framework leverages the strengths of each agent in their respective contexts to enhance overall performance across all contexts." - How does the framework account for intra-agent diversity? It seems that Figure 1 is rather deterministic, though some non-determinism is likely.

- Often vague formal underpinnings

  - Sec 3.3.1 is rather vague to provide formal underpinnings to the contributions. For example, L182: "The context space, C, includes relevant repository information and issue descriptions." What does "relevant information" entail here?

- Potentially limited mitigation of inconsistent agent behavior
  
  - Sec 3.2: "We consider two types of diversity: intra-agent diversity and inter-agent diversity." - I don't entirely agree with the proposed term of "intra-agent diversity". Diversity seems to be an artifact of non-determinism in this case, i.e., basically a temporal inconsistency. As such, it requires different means to mitigate, compared to the diversity stemming from the number of different agents. The method does not seem to acknowledge this.


- Typo: L057, citation "Team, 2024"

### Questions
- Sec 4.4: Are these results statistically significant?

- Is it possible to add human developers to the committee? (Fig 1c.)

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose “Diversity Empowered Intelligence,” a method for aggregating the solutions of several SWE agents by means of LLM prompting. They show a significant increase in scores on SWE-Bench Lite and attribute this to the fact that different SWE agents can solve different subsets of the problems.

### Strengths
[1] The authors systematically explore the benefits of ensembling of SWE agents and show significant improvement over single-agent solutions.

[2] Figure 1 nicely illustrates the idea behind DEI. Table 1 is very insightful and provides strong evidence of the value of DEI.

### Weaknesses
[1] The results are presented for SWE-Bench only. Even though SWE-Bench is a fairly reliable and diverse benchmark, validating DEI on another SWE benchmark could solidify the claim. The lack of evaluation on other benchmarks makes it difficult to assess the generalizability of the proposed method. It is possible that the observed improvements are specific to the characteristics of SWE-Bench and might not translate to other software engineering tasks or datasets. For example, a benchmark with different types of bugs or code structures could reveal limitations of the approach.

[2] The improvement in scores comes at the cost of significantly higher token usage (or compute). The paper does not sufficiently address the computational overhead associated with running multiple agents and evaluating multiple candidate solutions. While the authors mention the increased cost, they do not provide a detailed analysis of the trade-off between performance gains and resource consumption. This is a crucial consideration for practical applications, as the cost of running multiple agents might be prohibitive in some scenarios.

[3] The following papers are closely related but not cited:

a) SELF-CONSISTENCY IMPROVES CHAIN OF THOUGHT REASONING IN LANGUAGE MODELS

https://arxiv.org/pdf/2203.11171

Since a common decision is made based on a diverse set of candidates.

b) Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena

https://arxiv.org/abs/2306.05685

Since the scoring by an LLM is prompted, which is essentially LLM-as-a-Judge.

[4] The metrics in 4.1.2 are tied to the order in which the agents (and, by extension, their proposed solution patches) are added to the list. This is unacceptable for a metric as the solutions are fundamentally an unordered set. The metrics should be refined to be permutation invariant towards the set of agents. Whereas the proposed metrics are flawed in the general case, the main results in section 4.2 that are collected with the specific ordered list of agents are not flawed and have analytical value.

### Questions
[1] In “4.1.2 Evaluation Mertics” for Union@k: “Solved by any of the k solutions.”, what is the mathematical definition of “any”?

[2] Likewise, for Intersect@k, “solved by all k solutions”: is k tied to the number of agents at hand, or is it a free parameter? If independent, which agents are chosen from the (unordered) set of agents?

### Soundness
3

### Presentation
3

### Contribution
3
