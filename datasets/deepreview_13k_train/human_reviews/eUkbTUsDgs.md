# A little less conversation, a little more action, please: Investigating the physical common-sense of LLMs in a 3D embodied environment

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
As general-purpose tools, Large Language Models (LLMs) must often reason about everyday physical environments. In a question-and-answer capacity, understanding the interactions of physical objects may be necessary to give appropriate responses. Moreover, LLMs are increasingly used as reasoning engines in agentic systems, designing and controlling their action sequences. The vast majority of research has tackled this issue using static benchmarks, comprised of text or image-based questions about the physical world. However, these benchmarks do not capture the complexity and nuance of real-life physical processes. Here we advocate for a second, relatively unexplored, approach:~`embodying' the LLMs by granting them control of an agent within a 3D environment. We present the first embodied and cognitively meaningful evaluation of physical common-sense reasoning in LLMs. Our framework allows direct comparison of LLMs with other embodied agents, such as those based on Deep Reinforcement Learning, and human and non-human animals. We employ the Animal-AI (AAI) environment, a simulated 3D \textit{virtual laboratory}, to study physical common-sense reasoning in LLMs. For this, we use the AAI Testbed, a suite of experiments that replicate laboratory studies with non-human animals, to study physical reasoning capabilities including distance estimation, tracking out-of-sight objects, and tool use. We demonstrate that state-of-the-art multi-modal models with no finetuning can complete this style of task, allowing meaningful comparison to the entrants of the 2019 Animal-AI Olympics competition and to human children. Our results show that LLMs are currently outperformed by human children on these tasks. We argue that this approach allows the study of physical reasoning using ecologically valid experiments drawn directly from cognitive science, improving the predictability and reliability of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a framework, LLM-AAI, to assess the physical common-sense reasoning abilities of large language models (LLMs) by situating them within a 3D virtual environment known as Animal-AI. The authors aim to evaluate how well LLMs perform tasks such as navigation, object permanence, and tool use by using a suite of tests inspired by cognitive science. The framework enables direct comparisons between LLMs, reinforcement learning (RL) agents, and human children. The results show that LLMs struggle with complex physical reasoning tasks, often underperforming compared to both children and specialized RL agents.

### Strengths
The paper uses a minimalist yet structured environment (Animal-AI) that allows researchers to test LLMs’ physical common-sense reasoning in a controlled setting. This setup avoids the limitations of static benchmarks by providing a dynamic, interactive arena where LLMs can showcase their reasoning abilities in real-time. The use of Animal-AI as a testing ground allows the study of fundamental aspects of physical common sense, enabling a valuable comparison between the performance of LLMs and other entities, including human children. The methodology’s simplicity and focus make it easy to interpret and isolate the abilities being measured.

### Weaknesses
A significant limitation of this paper lies in the simplicity, or “toy” nature, of the Animal-AI environment. Although useful for initial assessments, the constrained setup does not approximate the complexities of real-world interactions. There is an inherent risk that high performance in this environment could falsely suggest deeper physical understanding, a trend that has been observed in prior research on similar “toy” environments. More robust environments, such as Minecraft or Omniverse, may better reveal practical competencies in physical reasoning due to their greater fidelity to real-world dynamics. 

Furthermore, the paper lacks novel insights; it primarily documents performance differences without offering deeper interpretations or mechanisms underlying these differences. As such, it provides limited understanding beyond comparative scores, which raises questions about the broader applicability and practical utility of the results.

### Questions
What can the community learn from this work, apart from performance difference?

### Soundness
2

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
2

### Summary
This study presents a framework for assessing physical common-sense reasoning in large language models (LLMs) using the Animal-AI (AAI) environment. By replicating animal lab experiments in a virtual 3D lab, the framework compares LLMs with Deep Reinforcement Learning agents, humans, and animals on tasks like distance estimation, obstacle navigation, object tracking, and tool use.

### Strengths
It builds a platform and benchmark for physical common-sense reasoning evaluations. In this platform, rather than reasoning, the agent can make actions to show their understanding of the environment.

### Weaknesses
1. Throughout the paper, the authors refer to using LLMs, though VLMs would be more accurate, given that the observations are primarily image-based.

2. The environment appears overly simplistic, lacking reflections of real-world physics and focusing mainly on semantic aspects.

3. The central contribution of this work remains unclear, as much of the effort seems concentrated on API and prompt design.

### Questions
The major contributions of this paper are unclear to me, leading to the following questions:

1. What real-world physical phenomena are represented in this environment?
2. How does the work demonstrate that the VLMs can reason about these physical phenomena?
3. What are the primary challenges in building such a benchmark, and how does this paper address them?
4. Are there any comparable previous works? What specific advantages does this work offer over them?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces LLM-AAI, a framework to evaluate Large Language Models (LLMs) on physical common-sense reasoning in a 3D embodied environment using the Animal-AI Testbed. This method allows for dynamic interaction, testing LLMs’ spatial and physical reasoning through tasks involving navigation, tool use, and object tracking. The study shows that state-of-the-art LLMs perform well on basic tasks but lack robust physical reasoning compared to human children and top reinforcement learning agents. While valuable for assessing LLMs’ spatial reasoning, the benchmark lacks components directly aimed at improving model training, functioning solely as a testing benchmark.

### Strengths
- Novelty: The LLM-AAI framework introduces a new approach by situating LLMs within 3D environments to evaluate physical common-sense reasoning, shifting the focus from static benchmarks to embodied assessments.
- Significance: This framework could set a new standard for LLM evaluation, addressing key questions about their ability to reason about and act in physical environments.
- Clarity: The paper is generally well-organized, with a logical flow from problem setup to experimental results and implications.

### Weaknesses
 - The “Think” function, while useful, feels a bit too specific for genuine decision-making. Depending on the agent design, LLMs could have more diverse commands—like “use tools” or “save to memory”—to handle different situations. The decision to define the action protocol with just “Go,” “Turn,” and “Think” needs some justification. In other words, what is the design principle behind this protocol?
- The benchmark is also set up to test out-of-the-box LLMs, yet the comparison to children can feel unbalanced since LLM agents might benefit from a more complex setup than just these three actions.
- While this benchmark does a great job assessing spatial reasoning, it’s solely focused on testing. There’s not much clarity on how the framework could directly support model training or help develop improved physical reasoning abilities in LLMs.

Overall, the design of the three actions (“Go,” “Turn,” and “Think”) feels somewhat unnatural and unbalanced. Specifically, “Go” and “Turn” are highly specific to this particular environment, while “Think” is overly generic.

If we take this approach, for example, in an environment where the agent needs to nail something, a “Use Tool” action could be added to better evaluate physical common sense. Similarly, a “Jump” action might be essential in an environment requiring the agent to traverse obstacles. These actions are also closely tied to the type of physical reasoning that this paper aims to assess.

Additionally, the “Think” action appears overly generalized, with no clear justification as to why it should be “Think” but not others. For instance, an action like “Memorize”, "Sense", or some other commands could be just as relevant in reflecting the agent’s capacity for physical common sense.

Overall, the design of these actions seems somewhat arbitrary. Instead of being grounded in a clear and comprehensive set of principles for evaluating physical reasoning, the choices appear to be driven by the constraints of the AAI environment and the ReAct agent framework. A more principled approach to designing the action set—one that systematically reflects the components required for physical reasoning—would significantly enhance the framework’s robustness and relevance.

### Questions
Overall I think the paper is proposing a benchmark for an important problem. However, I would like to hear the authors' opinions on the design principles of how LLMs interact with the environment.

### Soundness
2

### Presentation
3

### Contribution
3
