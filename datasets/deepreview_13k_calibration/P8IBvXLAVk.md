# Symbolic Learning Enables Self-Evolving Agents

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5

## Abstract
The AI community has been exploring a pathway to artificial general intelligence (AGI) by developing ``language agents'', which are complex large language models (LLMs) pipelines involving both prompting techniques and tool usage methods. While language agents have demonstrated impressive capabilities for many real-world tasks, a fundamental limitation of current language agents research is that they are model-centric, or engineering-centric. That's to say,  the progress on prompts, tools, and pipelines of language agents requires substantial manual engineering efforts from human experts rather than automatically learning from data. We believe the transition from model-centric, or engineering-centric, to data-centric, i.e., the ability of language agents to autonomously learn and evolve in environments, is the key for them to possibly achieve AGI. 

In this work, we introduce \textit{\baby}, a systematic framework that enables language agents to optimize themselves on their own in a data-centric way using \textit{symbolic optimizers}.  Specifically, we consider agents as symbolic networks where learnable weights are defined by prompts, tools, and the way they are stacked together. Agent symbolic learning is designed to optimize the symbolic network within language agents by mimicking two fundamental algorithms in connectionist learning: back-propagation and gradient descent. Instead of dealing with numeric weights, \baby works with natural language simulacrums of weights, loss, and gradients. We conduct proof-of-concept experiments on both standard benchmarks and complex real-world tasks and show that \baby enables language agents to update themselves after being created and deployed in the wild, resulting in ``self-evolving agents''. We demonstrate the potential of the \baby framework and open-source the entire framework to facilitate future research on \textit{data-centric} agent learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces a multi-agent framework called "agent symbolic learning," which aims to optimize all symbolic components within an agent system holistically. Drawing inspiration from traditional connectionist learning methods, this framework utilizes language-based loss functions, gradients, and optimizers to enhance prompts, tools, and workflows for agents, thereby avoiding local optimum and improving overall performance. It allows language agents to "learn from data" and "self-evolve" after deployment. Several proof-of-concept experiments demonstrate the framework's effectiveness across varying task complexities, suggesting a significant shift from model-centric to data-centric research in agent development, which authers believe is the key for optimizing agents.

### Strengths
- The presentation of this paper is quite interesting.
- The paper includes tasks related to question answering, mathematics, coding and writing.

### Weaknesses
- The improvements in the experimental results of this paper are not very significant.
- The paper is more like a multi-agent cooperation framework, describing operations such as reflection and discussion as forward and backward propagation, and combining them into a framework. The paper does not obtain better agents through training or similar methods, so describing it as "evolve" is a bit far-fetched.
- There is a lack of evaluation on complex sequential decision-making agent tasks, such as those in AgentBench [1], AgentTuning [2], AgentGym [3], and τ-bench [4], and the paper lacks comparison with these frameworks.
- The backbone models used are mainly from the GPT series, and it is necessary to include more models, especially open-source models.



[1] AgentBench: Evaluating LLMs as Agents

[2] AgentTuning: Enabling Generalized Agent Abilities for LLMs

[3] AgentGym: Evolving Large Language Model-based Agents across Diverse Environments

[4] τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

### Questions
See above

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
# Problem:

The AI community explores AGI via the ‘language agent’ framework involving a complex workflow of LM prompting and tool usage. This framework can only be improved through through human experts’ manual engineering efforts (engineering/model-centric).

How to depart from this painstaking engineering-centric paradigm?

# Contributions:

The paper aims to switch to a data-centric paradigm where language agents have the ability to ‘autonomously learn and evolve in environments’ from the data they observe, all symbolic nodes being optimized jointly and autonomously rather than separately by domain experts. To this end, they propose the ‘agent symbolic learning’ framework where agents self-optimize using symbolic optimizers.

Symbolic optimizers are mimicking the connectionist learning algorithms of backpropagation and **gradient descent over the substrate of symbolic elements of the language agents, i.e. prompts, tools and the way they are stacked together** (as a graph of nodes), rather than over the substrate of numerical weights. They optimize a **text-based loss** that is the result of applying an LLM-as-a-judge framework onto evaluation of the whole forward pass/agent execution, and use backpropagation from the last to the first node along the computational graph of the agent execution.

**Each symbolic element is then optimized by asking an LLM to modify it based on the backpropagated feedback.**

The papers presents proof-of-concept experiments showing the value of their approach against static agent framework and other prompt/tool optimization methods (e.g. DSPy).

### Strengths
# Strengths:

## Quality:

SQ1: the paper is of good quality, with seemingly high reproducibility.

## Clarity:

SC1: the paper is easy to read and overall well-written.

SC4: I really appreciate the insights of section 4.3 and would like to encourage the authors to expand on their writing by being more explicit about what real-world tasks they have considered and that are not necessarily well-represented in mainstream benchmarks.

## Originality:

SO1: Apart from the comtemporary approach of [1], this paper is as original as it gets. And, if I understand correctly, it improves over [1] by adding (i) the possibility of autonomously modifying the computational graph of the language agent, and (ii) the possibility of autonously updating tools or implement new ones.

## Significance:

SS1: I think the main contribution of the paper has the potential to be greatly significance for the community, but I find the current state of the paper to inadvertently occlude some valuable insights about limitations for instance.

### Weaknesses
# Weaknesses:

## Quality:

WQ1: Section 3.1 offers an analogy between connectionist learning and agent symbolic learning, but it fails to mention and discuss where does the analogy breaks, such as for instance:

- in the fact that the loss function requires comparison to a groundtruth label which is not instantiated here in the agent symbolic learning ;
    
- in the fact that the lack of groundtruth labels makes the whole approach more akin to an unsupervised learning approach rather than a supervised learning approach (like connectionist learning) ;
    
- in the fact that the connectionist gradient is effective due to mathematical guarantees that ascertain that updating numerical weights in the gradient direction will lead to an optimization of the corresponding loss ; but there is no such guarantee when considering language gradient as they are only the result of an LLM output, which we know to be riddle with issues, such as hallucinations[2,3] and unfaithfulness[4,5] ;
    
- …
    

Adding this discussion would improve the quality and significance of the paper, by detailing to the reader possible limitations that could be addressed down the line, and it would greatly improve my appreciation of the paper towards proposing honest and thought-through research that does not build unnecessary hype.

WQ2: I would like to invite the authors to present results with open-source LMs, as it would be valuable for overall replicability purposes and also to understand better how the approach performs with different LMs.

WQ3: I would like to invite the authors to consider include an experiment that studies how the performance scale with the size of both the forward pass LM and the symbolic optimizer LM. I think it would provide great insights into the potential of the propose approach for the democratisation of LMs, for instance.

## Clarity:

WC1: In Section 3.2, in the paragraph explaining equation (1), ‘task requirements’ are mentioned without much details, and I believe it is the first time it is mentioned in the paper. I would like to invite the authors to define it as precisely as possible, possible in section 3.1 for problem formulation, as I now realise how important of an element it must be (Please clarify if I am mistaken?). I also suspect that it is an element that cannot be optimised in a data-centric way but is still dependent on manual engineering effort, along with the prompt $\mathcal{P}_\text{loss}$, right? If so, I mean to invite the authors to collate all of those elements that are not yet data-centric-ly optimisable within the propose agent symbolic learning framework and propose a discussion of how future works may try to address them?

WC2: In section 3.2, the language loss computation paragraph actually details supervised agent learning vs unsupervised agent learning scenarios. I think it would make better sense to introduce this in Problem Formulation Section 3.1, and clearly highlight in which scenario will the main paper present experiments. I was actually assuming until this paragraph that only the unsupervised agent learning scenario was performed given the mention of using LLM-as-a-judge framework. It might be valuable to nuance and explicitly detail what is meant by LLM-as-a-judge when it is used in Section 3.1 actually.

WC3: As much as possible, it would be really valuable to integrate the different prompt templates for loss and gradient, and gradient update computations into the main text of the paper, in a concise form, or at least point specifically at them and discuss some of their guiding principles further in depth, in order to give a more concrete understanding of their impact to the reader.

## Originality:

WO1: Optionally adding a comparison of the contemporary approach of [1] could improve the impact of the paper.

## Significance:

WS1: Following up on my concerns in SS1, I find that the paper does not sufficiently discusses the limitations of the proposed framework, which result in an impression of building up hype for a product rather than doing thought-through research. I would like to emphasise again that my appreciatetion of the work would be greatly improve if the authors could revise the paper by including a lot more insights about limitations and what does not work fully (yet) and/or how some critical elements may impact the performances of their proposed work. For instance, could it be possible to perform an ablation study on the quality of the task description or the quality of the different engineering-centric prompt templates for loss and gradient and gradient update computation, please?

### Questions
Please refer to the different points above.

# References:

[1]: Yuksekgonul, Mert, et al. "TextGrad: Automatic" Differentiation" via Text." *arXiv preprint arXiv:2406.07496* (2024).

[2]: Banerjee, Agarwal, and Singla, ‘LLMs Will Always Hallucinate, and We Need to Live With This’.

[3]: Zhang, Muru, et al. "How language model hallucinations can snowball." *arXiv preprint arXiv:2305.13534* (2023).

[4]: Lanham et al., ‘Measuring Faithfulness in Chain-of-Thought Reasoning’.

[5]: Turpin et al., ‘Language Models Don’t Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting’.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes agent symbolic learning, a data-centric method for optimizing agentic systems presented in a sequential workflow. As part of the proposed methods, the analogy of back-propagation and gradient descent for optimizing neural networks is presented. Furthermore, optimizers that update tool uses and the agent workflow are introduced. The proposed method was tested on three benchmarks in different domains and showed improved performance compared to other baseline methods. The proposed method also outperforms other baseline methods on software development and creative writing based on excitability and GPT-4 scored metrics, respectively.

### Strengths
1. This work is well-motivated.

### Weaknesses
1. The second paragraph of the introduction needs references.
2. The claim that "these optimization methods are prone to a local optimum of isolated prompts, tools, and nodes" in the paragraph from lines 079 to 092 is incorrect. GPTSwarm includes an edge optimization method, which optimizes the connection of nodes globally.
3. Moelding the nodes or components with a sequential structure, as defined in line 213, is not making a full analogy with computational graphs in neural nets, as claimed in line 211. A computational graph of neural nets can be arbitrary directed acyclic graphs.
4. It is better to have a citation for dynamic neural nets at the end of page 4.
5. There is an inconsistency of variable use. Variable $n$. is used for the number of nodes in line 213. However, it is used as an arbitrary index of the node in equation 2. The same inconsistency also applies to lines 12, 13, and 17 of algorithm 1.
6. It is unclear to me how the gradient of the last node is defined.
7. There are typos, such as the word "optimizer" in line 351 should be "optimize." 
8. Line 13 of algorithm 1 appends a gradient to the trajectory. This is not mentioned in the main text. Which strategy should I follow?
9. The abstract claims that the proposed methods outperform others on real-world tasks, which I do not think is the case.
10. It is better to give a reference about how OpenAI implements GPTs in line 423.
11. There is a lack of detail about how the initial agents are implemented.
12. Many experimental details are missing. For example, what are the learning rate and batch size used for experiments? Is the optimization done in a supervised or unsupervised setting? 
13. Many of the references are missing the publisher.

### Questions
1. What are the "components of the prompts" and "functions" on line 083 and line 085, respectively, referring to?
2. What exactly is the programming language introduced in Zhou et al. (2023b)? In what sense is it a programming language?
3. How does the "learning rate" defined for each of the prompts apply when optimizing prompts, tools, and agent workflows? 
4. Are Prompt Optimizer and ToolOptimizer part of the proposed framework? Why are they not described in Algorithm 1? Are they used in the experiments?  
5. What optimization method of DSpy is used in the experiments? 
6. Are the results presented on some hold-out test set or the set used for optimization? If applicable, how are the sets split?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes agent symbolic learning, a framework to enable automatic self-improvement of language agents in a data-driven way, in comparison to model-centric and engineering-centric optimization methods. The framework draws language-based analogs to back-propagation and gradient descent, optimizing agents via text-based weights, loss, and gradients. The key idea is to optimize the prompt, tool use, and workflow as a whole instead of separate components to avoid local minima. The effectiveness of the method is demonstrated through experiments on several benchmarks, showing improvements over baselines.

### Strengths
**Originality:** The analogy to the neural network training paradigm is interesting.

**Quality:** The experimental results showcase the performance improvements achieved by the proposed approach.

**Clarity:** The framework is well-explained and the writing is easy to follow.

**Significance:** The problem of self-evolving agents considered is important.

### Weaknesses
1. **Reliability of Language Loss and Gradients**: The idea of using evaluator networks to improve performance is not new, especially for complex reasoning tasks. However, the reliance on LLMs for computing language loss and gradients raises concerns of reliability, especially when the authors want to "back-propagate" the loss. Deviations may accumulate and make the overall update unstable. Could the authors conduct experiments with complex tasks where the analogous symbolic network has extended node numbers and investigate how the language loss transits under such settings?
2. **Data-Centric Claims and Unsupervised Role of Data**: While the authors claim the framework to be data-centric and can be applied in an unsupervised way, the exact role of data under such setting is not thoroughly addressed. The appendix only provides templates for language loss function under the supervised setting. Could the authors provide the template for the unsupervised setting, and the corresponding experiment results?
3. **Convergence**: Convergence is a critical aspect of neural network training, yet the paper does not discuss when or how the analogous "training" process stabilizes for the framework. Could the authors elucidate specific metrics or criteria they use to determine convergence in their framework and potential challenges in reaching it?
4. **Expanded Baselines and Benchmarks**: While the framework shows promising results on selected tasks over several methods, additional baselines and benchmarks are needed to comprehensively evaluate the performance. Specifically, for the "standard LLM benchmark", the paper does not clearly state the benchmarking method for GPTs. Is it zero-shot or few-shot based? Given that the method uses few-shot examples, few-shot prompting for GPTs would be necessitated for a fair comparison. Also comparisons with other baselines, such as CoT/ToT at least, are important for validating the effectiveness of the method. A wider choice of tasks would also be favorable since creative writing and software development alone might not be sufficient for representing complex agent tasks.
5. **Ablation Studies for Component Analysis**: An ablation study on the components, such as the workflow optimizer and prompt optimizer, would provide more granular insights into each component’s contribution and help understand how the proposed method achieves its reported performance improvements.
6. **Open-Sourcing the Framework**: The authors mentioned that the framework would be open-sourced. I wonder if this could be done in the rebuttal period.

### Questions
See the Weaknesses section above.

### Soundness
2

### Presentation
2

### Contribution
2
