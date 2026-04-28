# ThinkBot: Embodied Instruction Following with Thought Chain Reasoning

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
Embodied Instruction Following (EIF) requires agents to complete human instruction by interacting objects in complicated surrounding environments. Conventional methods directly consider the sparse human instruction to generate action plans for agents, which usually fail to achieve human goals because of the instruction incoherence in action descriptions. On the contrary, we propose ThinkBot that reasons the thought chain in human instruction to recover the missing action descriptions, so that the agent can successfully complete human goals by following the coherent instruction. Specifically, we first design an instruction completer based on large language models to recover the missing actions with interacted objects between consecutive human instruction, where the perceived surrounding environments and the completed sub-goals are considered for instruction completion. Based on the partially observed scene semantic maps, we present an object localizer to infer the position of interacted objects for agents to achieve complex human goals. Extensive experiments in the simulated environment show that our ThinkBot outperforms the state-of-the-art EIF methods by a sizable margin in both success rate and execution efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces ThinkBot, an agent designed for Embodied Instruction Following (EIF) that effectively executes human instructions in complex environments by reconstructing missing action descriptions through the chain of thought. The authors introduce an instruction completer using large language models to predict missing actions and an object localizer to determine object positions for agent interaction. Extensive experiments show that ThinkBot surpasses existing state-of-the-art EIF methods in both success rate and execution efficiency. Key contributions include the development of the ThinkBot agent, the instruction completer for coherent instruction generation, and the object localizer for precise spatial guidance, all enhancing success rates in EIF tasks.

### Strengths
- The paper presents a novel approach to Embodied Instruction Following (EIF) by introducing the concept of a "thought chain" to recover missing action descriptions from sparse human instructions. Integrating an instruction completer and an object localizer enhances the agent's ability to follow instructions in complex environments. This is an effective way to address the coherence issue in action plans.
- The experiments in the paper demonstrate the effectiveness of ThinkBot through extensive testing on the ALFRED benchmark, showing significant improvements in success rates and execution efficiency over state-of-the-art methods.
- The paper is well-structured. The figures and diagrams, such as the pipeline of ThinkBot and the comparison with conventional methods, are clear and effectively illustrate the proposed methods and results. The writing is coherent, and the instructions for reproducibility, including the full system prompt for the instruction completer, contribute to the transparency and clarity of the research.

### Weaknesses
 - The introduced approach heavily relies on the inherent reasoning capabilities of LLMs. If the LLMs are not trained on diverse or comprehensive datasets, it could lead to biases or limitations in the agent's performance. The authors need to demonstrate the robustness of the prompt to different LLMs, e.g., Llama 3, and other open-sourced LLMs (gemma2, qwen2.5). 
- While the paper demonstrates strong performance in simulated environments, there might be concerns about how well ThinkBot's approach translates to real-world applications, where the complexity and variability can be significantly higher. Besides, the time cost of the reasoning process should be considered for real-world applications. However, LLM-based reasoning will lead to a high delay in the inference time. The use of LLMs and complex reasoning processes may require significant computational resources, which could limit the scalability of the ThinkBot system, especially in resource-constrained embodied systems.
- The paper does not extensively discuss how ThinkBot handles errors or recovers from incorrect actions once taken. This is an important aspect of robust autonomous agent design. It is important to make the agent self-improve during the interactions, instead of manually adjusting the prompt. This is also important to generalize the reasoning process to other scenarios or tasks. It is necessary to conduct experiments demonstrating the agent's ability to learn from mistakes (adding noise to actions) and improve performance over time without manual prompt adjustments or discuss how the reasoning process could be made more generalizable.

### Questions
- How does the performance of ThinkBot vary when using different LLMs with potentially different training datasets? Have you tested the robustness of the prompt with LLMs such as Llama 3 or other open-sourced LLMs?
- How does the ThinkBot approach handle the increased complexity and variability of real-world environments compared to simulated ones?
- What is the inference time for the LLM-based reasoning process, and how does this delay impact the feasibility of ThinkBot for real-world applications? How does the computational resource requirement of the ThinkBot system impact its scalability, especially when considering the constraints of embodied systems in real-world scenarios?
- Can the agent learn from its mistakes to improve its performance over time, and is there a mechanism for self-improvement during interactions?
- How to address the generalization of the reasoning process to new scenarios or tasks, ensuring that the agent can adapt and learn from a wide range of situations?

### Soundness
3

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
2

### Summary
This paper proposes a novel agent for Embodied Instruction Following (EIF) tasks. The method uses thought chain reasoning to complete missing action descriptions and employs a multimodal object localizer for enhanced object interaction. Extensive experiments demonstrate better performance in both success rate and execution efficiency compared to previous methods.

### Strengths
The proposed pipeline is technically sound. Using LLM to understand free-form instructions is an effective way to reason about actions in unstructured environments. And the proposed object localizer complements the LLM by addressing its spatial understanding limitations.

### Weaknesses
1. While effective, this work appears to be a combination of LLM with a localizer, which might lack of novelty.

Existing multimodal LLMs (MLLMs) can achieve better reasoning performance than the LLM used here. The authors employed GPT-3.5, but using a state-of-the-art MLLM like GPT-4o could improve performance.

### Questions
What if you take input the instruction with current egocentric image to gpt-4o? I believe it might improve the overall reasoning performance.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents ThinkBot, a system designed to infer missing actions from incomplete human instructions using LLMs and to predict target object locations for these inferred actions. ThinkBot employs a structured CoT prompt to obtain the missing actions using LLMs. With the actions and target objects identified, the multimodal object localizer creates a positional heatmap the given instruction, and the inferred action. ThinkBot achieves improvements over previous methods in the ALFRED benchmark.

### Strengths
- ThinkBot tries to figure out missing actions from instructions, which is an important and challenging problem of embodied instruction following.
- ThinkBot shows a strong improvement over the previous methods (yet the baseline, Prompter+, on which ThinkBot is built already beats SoTA, see weaknesses).
- The paper is well structured and shows clear presentation.

### Weaknesses
 - It looks like the instruction completer finds where is a target object by addressing missing information in the goal statement, but the step-by-step instructions usually contain the missing information. Why not just directly parse the missing information in the step-by-step instructions? Why do we still need the proposed instruction completer?

- Previous work (Prompter) also similarly finds the next receptacle by using language models (BERT) by guessing where a target object is likely to be. Instead, the instruction completer uses LLM with CoT. We may use better language models with prompting techniques for better results, but this is expected.

- Why not just using semantic information in the spatial semantic map, not predicting where is a target by the multimodal object localizer?

- The ablated performance of the multimodal object localizer and the correlation graph seems marginal in valid unseen but not in Hard Valid Unseen. It seems like the model is designed for closed-receptacle cases. And why are they marginal?

- I think that the authors can plug the proposed module in the other baselines like FILM and CPEM. Improvements over these models may indicate good generalizability of the proposed approach.

- The proposed model is evaluated in a single benchmark. I'm not sure if this approach works well in other tasks.

### Questions
See weaknesses above.

### Soundness
3

### Presentation
3

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
This paper presents a ThinkBot agent that recovers underspecified instructions through thought chain reasoning and performs embodied instruction following tasks. The proposed method consists of three components: the instruction completer, the object localizer, and the object correlation graph. The authors employ large language models for the instruction completer and a multimodal transformer for the object localizer. Experimental results show that a ThinkBot agent outperforms prior arts on the ALFRED benchmark, and ablation studies demonstrate the effectiveness of each component.

### Strengths
- The paper introduces a new modular approach for EIF tasks, a ThinkBot agent. The idea of recovering sparse human instruction is a novel direction. 
- The paper conducts extensive analysis, including ablation studies and qualitative analysis, which helps to understand the proposed method.
- The paper is well-written and easy to understand.

### Weaknesses
 - While the authors demonstrated the effectiveness of the instruction completer in ablation studies (Table 2), the improvements are quite marginal in the valid unseen split. It indicates that recovering sparse human instruction is sometimes helpful, but at the same time, this tells us that it is not a fundamental problem in EIF tasks.


### Questions
- What makes the difference between ThinkBot and LLM-Planner in high-level planning (Table 3)?

### Soundness
3

### Presentation
3

### Contribution
2
