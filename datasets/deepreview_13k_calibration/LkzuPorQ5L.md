# Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 5, 8, 3

## Abstract
\vspace{-0.6em}
Recent advancements in large language model (LLM)-powered agents have shown that collective intelligence can significantly outperform individual capabilities, largely attributed to the meticulously designed inter-agent communication topologies. Though impressive in performance, existing multi-agent pipelines inherently introduce substantial token overhead, as well as increased economic costs, which pose challenges for their large-scale deployments. In response to this challenge, we propose an economical, simple, and robust multi-agent communication framework, termed \ourmethod, which can seamlessly integrate into mainstream multi-agent systems and prunes redundant or even malicious communication messages. Technically, \ourmethod is the first to identify and formally define the \textit{communication redundancy} issue present in current LLM-based multi-agent pipelines, and efficiently performs one-shot pruning on the spatial-temporal message-passing graph, yielding a token-economic and high-performing communication topology.
Extensive experiments across six benchmarks demonstrate that \ourmethod \textbf{(I)} achieves comparable results as state-of-the-art topologies at merely $\$5.6$ cost compared to their $\$43.7$, \textbf{(II)} integrates seamlessly into existing multi-agent frameworks with $28.1\%\sim72.8\%\downarrow$ token reduction, and \textbf{(III)} successfully defend against two types of agent-based adversarial attacks with $3.5\%\sim10.8\%\uparrow$ performance boost.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces AgentPrune, a communication framework designed for LLM-MA systems. AgentPrune addresses inefficiencies in traditional multi-agent communication by reducing redundant messaging, which can lead to excessive token usage and increased costs. The framework formalizes the communication between agents as a spatial-temporal message-passing graph and optimizes its token usage without compromising task performance. Key findings include a significant reduction in token overhead and improved robustness against adversarial attacks. Through extensive testing on various benchmarks, AgentPrune demonstrated cost-effective, high-performance capabilities, achieving similar or better results compared to conventional models but at a fraction of the token cost.

### Strengths
1. The connectivity optimization methods (distribution approximation and low-rank sparsity) appear highly effective. By applying a straightforward policy gradient approach and sparsity optimization on the graph masks, the framework efficiently enhances the performance and robustness across various multi-agent frameworks and tasks while reducing the token cost.

### Weaknesses
1. It appears necessary to fix the number and roles of agents before implementing AgentPrune. 
2. To effectively train each version of the framework, a substantial amount of data is required to optimize the connectivity parameters through sufficient rollouts.

### Questions
I would like to know the required quantity of data to be generated as well as the number and types of mask configurations necessary for training in Sections 3.2 and 3.3.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work focuses reducing communication between multi-agent LLM systems. The goal is to reduce spatial and temporal communication required between multiple LLM agents while keeping high accuracy. The authors propose learning a graph mask using distribution approximation and low-rank sparsity. The proposed method is evaluated on a wide variety of benchmark in terms of communication and cost required and the accuracy achieved.

### Strengths
- This work looks into an important problem of reducing cost when using multi-agent LLM system. 
- The paper is well written and relatively easy to follow.

### Weaknesses
 - The paper start with showing random pruning can provide performance improvement, but the proposed method is not compared to the random pruning, so it is hard to understand how much improvement compared to random pruning we have.
- It is not unclear how much training and query/tokens is need to train the system, and how different number of training (one-shot) is needed and how they affect the performance.
- Missing ablation study about the benefit of each of the propose methods (i.e. distribution approximation, low-rank sparsity)

### Questions
- What's the training time for this proposed method. Does it overfit to the training data? How does the K' affects the performance.
- Does the mask changes depending on the input data?
- How does the proposed method perform compared to random pruning? 
- Can distribution approximation and low-rank sparsity work in isolation? what's their effect on the accuracy and communication reducing?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies the communication redundancy problem, i.e. the fact that when multiagent networks solve a task, several exchanged messages are redundant. To address this problem, they model communication as a spatiotemporal graph (i.e. a graph that models both which agents interact with each other and what context should be included) and introduce AgentPrune, an optimization technique that reduces the level of redundancy while preserving performance. This technique involves three steps:
* In the "training" phase ($K^\prime$ rounds), the spatiotemporal graph is optimized according to a metric that rewards assigning higher weights to important connections while at the same time increasing sparsity;
* The connections are then pruned according to a threshold;
* From that point onwards ($K - K^\prime$ rounds), only the non-pruned connections are used.

The authors then study the performance of AgentPrune both in its standalone form and in conjunction with other multiagent frameworks, finding a reduction in overall cost; they also find that AgentPrune leads to improvements in robustness against agent-targeted adversarial attacks.

Overall, the paper studies an important problem and proposes a reasonable (though far from perfect) approach to reduce communication redundancy. In particular, the technique requires an expensive training step; however, for large enough datasets, this leads to long-term efficiency gains. Aside from some issues that raised a few eyebrows, the experimental analysis is well done and the model also offers some robustness gains as a bonus. ~For this reason, my recommendation is 6 (Marginally above acceptance threshold).~

~I would be willing to raise my score should the authors take the following steps (see the Weaknesses section):~
* ~Presenting the results in Table 2 and 3 in a more balanced light;~
* ~Adding the missing experimental info;~
* ~Answering the questions reported in the Questions section (assuming that the results showcase the transferability of AgentPrune).~

Update: the authors' rebuttal has addressed essentially all of my concerns, which is why I'm raising my score to 8 (Accept).

### Strengths
* The paper does a good job of formalizing the problem, which I agree is an important one;
* Modelling the task as a spatiotemporal graph is also a pretty solid idea, and the proposed technique can be seen as an intuitive extension of this approach;
* The cost reduction is significant;
* I appreciated the parameter sensitivity analysis and the ablation study, as these types of studies, while expensive, are very important for proper science.

### Weaknesses
It is unclear to me how applicable AgentPrune is in a real-world context. AP makes sense in situations where the deployer already has a training set for a given task and is willing to invest resources into optimizing the communication graph for future queries. In other words, using AP is reasonable from an economics point of view only at large scales, where there are enough training examples and enough expected future queries to warrant such an optimization step. To be clear, this is not a dealbreaker: several real-world applications fit this description, and my critique of AP can also be applied to any other network optimization technique (e.g. GPTSwarm). Still, it’s hard to make a case for widely applicable cost savings, especially since each graph appears to be task-specific and thus not transferable. Comparing with optimization-free baselines (e.g. CoT) is also a bit unfair, since they do not require this initial training step.

Moreover, emphasizing the reduction in prompt tokens instead of the cost itself (e.g. in Table 3) is slightly misleading, since a) deployers care about the cost, not the prompt tokens b) the cost reductions, while still good, are often less impressive than the prompt token reduction (e.g. -17% cost vs -36% tokens for AG+HumanEval, -55% cost vs -78% tokens for GPTSwarm+MMLU, -52% cost vs -73% tokens for GPTSwarm+HumanEval). In the same vein, reporting in Table 2 the performance gain w.r.t. Vanilla sort of hides the fact that AgentPrune has slightly worse performance compared to Reflexion prompting (which is not a dealbreaker, but it should still be noted).

Finally, there are some missing experimental details in the paper, such as:
* What function is used as $\phi$ in the experiments?
* What connection probability is used to generate the random graph?
* What’s the diversity penalty for the OpenAI models?

While I found the answers to these questions in the code, given the non-static nature of repositories these values should also be reported in the experimental setup appendix of the code.

Minor notes:
* In Table 6 there's a typo related to the word "ablation";
* Again in Table 6, the original scores have 4 significant digits, but the ones after ablation only have 3;
* The title of Appendix F contains a misspelled "Existing";
* Figure 30 has a typo in the word HumanEval;
* In G.3 “liar" is misspelled as “lier”.

### Questions
* What’s the minimum scale (in terms of e.g. dataset size and number of queries) where AgentPrune is more cost-effective than other techniques?
* Do networks trained on a task transfer to similar tasks?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces AgentPrune, a framework aimed at optimizing communication in LLM-based multi-agent systems by reducing unnecessary message exchanges, which in turn lowers token usage and economic costs. In MAS, agents collaborate through complex communication topologies, which, while enhancing collective intelligence, can lead to significant token overhead and high operational expenses.

AgentPrune addresses this challenge by introducing a "communication pruning" mechanism, where redundant or non-essential messages within the spatial (intra-dialogue) and temporal (inter-dialogue) message-passing graph are pruned. 

Experiments demonstrate AgentPrune's effectiveness across several benchmarks, including MMLU, GSM8K, and HumanEval. Experimental results indicate that AgentPrune achieves comparable performance to existing MAS topologies at a fraction of the cost, with a reported token reduction of up to 72.8% and an increased robustness to basic adversarial attacks by 3.5% to 10.8%

### Strengths
1. It addresses an important problem in MAS involving LLMs: the significant economic costs associated with token usage. By focusing on token efficiency, it highlights an often-overlooked aspect of MAS design, especially relevant as these systems scale up. The emphasis on reducing token consumption could encourage future MAS research to adopt similar cost-effective approaches, making it a useful reference for economical MAS deployment.

2. It borrows idea from the spatial-temporal graphs to manage agent communication provides a structured way to visualize and optimize message passing in MAS. This graph-based approach brings an analytical perspective to inter-agent communication, offering insights into which interactions can be minimized without sacrificing performance. Such structured pruning could inspire other MAS research to explore graph-based techniques for optimizing agent communication.

3. It formally define "communication redundancy" in LLM-powered MAS, bringing attention to the often excessive and unnecessary communications within these systems. By identifying this redundancy, the authors shed light on a specific inefficiency that had not been well-formalized in previous MAS research, thus contributing a valuable perspective to MAS optimization.

### Weaknesses
1. Inadequate Justification for Pruning Methodology: The one-shot pruning approach, though efficient, lacks theoretical grounding in the context of MAS. The decision to prune a fixed percentage of tokens and communication paths across all tasks does not account for the varying communication needs of different agents or tasks. This oversimplified pruning criterion may lead to suboptimal performance in scenarios where more dynamic and context-sensitive pruning is required.

2. The paper provides little analysis of how pruning affects the quality and depth of agent interactions or task accuracy, especially in more nuanced MAS tasks. **For instance, the pruning’s impact on collaborative tasks requiring high contextual awareness is underexplored.**

3. The number of colors and the format of text in Figure 1 is excessive, and the text is too lengthy, making the annotations unclear and distracting from the overall understanding of the figure.

### Questions
Regarding point 2: If you could include experiments that require high contextual awareness, demonstrating that your model can improve both quality and token efficiency in such scenarios, I would be happy to raise my evaluation score.

And I would appreciate a deeper analysis of the types of errors or ineffective communications that AgentPrune eliminates, as this would clarify the practical implications of its pruning method. Such insights would better illustrate AgentPrune’s strengths and limitations and help inform users of any potential side effects.

### Soundness
2

### Presentation
2

### Contribution
2
