# Odyssey: Empowering Minecraft Agents with Open-World Skills

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 5, 3, 6

## Abstract
Recent studies have delved into constructing generalist agents for open-world environments like Minecraft. Despite the encouraging results, existing efforts mainly focus on solving basic programmatic tasks, \textit{e.g.}, material collection and tool-crafting following the Minecraft tech-tree, treating the \texttt{ObtainDiamond} task as the ultimate goal. 
   This limitation stems from the narrowly defined set of actions available to agents, requiring them to learn effective long-horizon strategies from scratch. Consequently, discovering diverse gameplay opportunities in the open world becomes challenging.
   In this work, we introduce \odyssey, a new framework that empowers Large Language Model~(LLM)-based agents with open-world skills to explore the vast Minecraft world.  
   \odyssey comprises three key parts: 
   (1) An interactive agent with an \textit{open-world skill library} that consists of 40 primitive skills and 183 compositional skills.
   (2) A fine-tuned \mbox{LLaMA-3} model trained on a \textit{large question-answering dataset} with 390k+ instruction entries derived from the Minecraft Wiki.
   (3) A \textit{new agent capability benchmark} includes the long-term planning task, the dynamic-immediate planning task, and the autonomous exploration task. Extensive experiments demonstrate that the proposed \odyssey framework can effectively evaluate different capabilities of LLM-based agents. 
   All datasets, model weights, and code are publicly available to motivate future research on more advanced autonomous agent solutions.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses the development and evaluation of generalist agents in open-world environments like Minecraft. The authors introduce Odyssey, a framework that equips LLM-based agents with enhanced open-world skills to enable more diverse exploration. Odyssey includes (1) an agent skill library with 40 primitive and 183 compositional skills, (2) a fine-tuned LLaMA-3 model trained on Minecraft Wiki instructions, and (3) a new benchmark covering long-term planning, dynamic planning, and autonomous exploration tasks. Experiments show Odyssey’s effectiveness in evaluating agent capabilities. All resources are publicly available to support future research on autonomous agents.

### Strengths
1. This paper demonstrates substantial effort, including the collection of Minecraft-specific data, fine-tuning a large language model, building a Minecraft agent, comparing it with numerous baselines, and designing three evaluation benchmarks.
2. The paper is well-formatted, with clear and coherent expression of ideas, making it easy for readers to follow and understand.

### Weaknesses
I strongly agree with the paper’s critique that “current research in Minecraft is overly focused on tasks like mining diamonds.” Minecraft is indeed a valuable platform for studying generalist agents, as it simulates numerous real-world challenges such as complex perception, an infinite task space, partial observability, and intricate terrains—all unsolved issues. Developing agents in Minecraft should ideally contribute towards generalization in other environments, even the real world. However, much of the current research overlooks these challenges, using scripted, privilege-enabled setups like Mineflayer to turn Minecraft into a text-based game. This approach often revolves around how to prompt large language models like GPT-4 to decompose long-horizon tasks, which isn’t easily transferable to other settings, as few environments provide global privileged information or powerful controllers like Mineflayer. Although there are numerous studies of this kind, they rarely yield new insights, and unfortunately, this paper falls into this paradigm.

1. The paper repeatedly emphasizes that “our focus is not to design a new LLM-based agent architecture.” However, a significant portion is still dedicated to detailing the agent architecture, even listing it as part of the contribution. Since this architecture is not novel, it would be better suited to the appendix.
2. Given that the focus is not on a “new LLM-based agent architecture,” performing an ablation study on a standard architecture seems less meaningful.
3. The comparison in Table 3 is inherently unfair. The VPT model operates in the native, unmodified environment with RGB output and mouse and keyboard controls, while GITM and the proposed work use Mineflayer as a controller.
4. Fine-tuning on Minecraft-specific knowledge is expected to improve performance compared to large, untuned models, so this result is unsurprising.

### Questions
Refer to the weakness.

### Soundness
2

### Presentation
2

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
Manuscript presents several contributions toward building more capable agents in open-world Minecraft: 1) a primitive (and compositional) library of scripted skills; 2) A fine-tuned LLaMA-3 model on QA dataset curated from Minecraft wiki; 3) A new agent benchmark including various tasks in Minecraft. Experiments on programmatic tasks and the tasks in the proposed benchmark show promises over prior arts and counterparts LLMs.

### Strengths
+Overall the paper is clearly written, the graphics are stylish and the write-up is good.

+The research topic (open-world agents, LLMs, etc) is relevant to the interest of NeurIPS community.

+The proposed benchmark is interesting and somewhat comprehensive in terms of the diversity and complexity of tasks and the open-world capabilities that can be evaluated.

### Weaknesses
-The contributions, though they require a considerable amount of work, do not constitute the significance needed by a conference paper of a top-tier conference like ICLR. Indeed I found the three pillars: the primitive skill library, the LLM for Minecraft QA, and the benchmark are loosely connected and it is unclear how they can benefit better open-world Minecraft agents as a whole. 

More importantly, it does not look obvious to me how can these pillars be distinguished from several prior works on similar fronts -- the concept of primitive skills has been introduced by at least a few times including DEPS (Wang et al., 2023), Voyager (Wang et al., 2023), Plan4MC, etc, in both scripted and end-to-end control fashion; the fine-tuned LLM for Minecraft QA can be found in OmniJARVIS (Wang et al., 2024), etc; the benchmark is even more frequently explored in BASALT, MineDoJo, Voyager, DEPS, GROOT (Cai et al., 2023), GROOT-2 (Cai et al., 2024). In the rebuttal, I do expect a comprehensive review of how the contribution presented in the manuscript can be more significant than these for building better open-world agents.

-The results in table 3 should be more carefully examined, as two of the three baselines indeed employ end-to-end control rather than scripted skills. Without an ablation on this, it cannot justify the effectiveness of the proposed method, at least on programmatic tasks.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The ODYSSEY framework enhances LLM-based agents in Minecraft by equipping them with an extensive open-world skill library and fine-tuning a LLaMA-3 model using a large Minecraft-specific dataset. It introduces a new benchmark to evaluate agent capabilities in long-term planning, dynamic planning, and autonomous exploration. ODYSSEY outperforms previous methods in adaptability and efficiency, offering a cost-effective solution for open-world agent research.

### Strengths
1.	The visual illustrations are appealing and elaborate.
2.	The appendix provides a thorough and detailed explanation of the methods.

### Weaknesses
1.	ODYSSEY’s pipeline is highly similar to existing frameworks such as Voyager, Optimus-1[1], and ADAM[2].
2.	ODYSSEY relies on predefined primitive skills, which were generated by GPT-4, whereas GPT-4 itself can directly write JavaScript programs based on Mineflayer. This approach of relying on primitive skills limits the agent’s ability to perform more complex and open-ended tasks, such as building.
3.	On programmatic tasks, ODYSSEY does not demonstrate a broader task range compared to baselines, remaining at the diamond level, already achievable by Voyager. What about more difficult tasks?
4.	The comparisons shown in Table 3 are unfair, as DEPS and VPT use keyboard and mouse as action spaces, rather than JavaScript code, and VPT additionally utilizes visual observation. This is fundamentally different from ODYSSEY, which uses privileged information as its observation space, making such comparisons invalid.
5.	The authors fine-tuned LLaMA-3 on a supplementary dataset (Minecraft Wiki) to create MineMA, but in Tables 4 and 5, the comparison is made against open-source models of equivalent size that lack Minecraft-specific knowledge, resulting in weaker performance. I suggest comparing MineMA with models like GPT and Claude, which possess robust Minecraft knowledge, to demonstrate the significance and efficacy of the additional fine-tuning.
6.	Several related works were not cited, including:
	•	[1] Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks
	•	[2] ADAM: An Embodied Causal Agent in Open-World Environments
	•	[3] OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents, NeurIPS 2024
	•	[4] Steve-Eye: Equipping LLM-based Embodied Agents with Visual Perception in Open Worlds, ICLR 2024

### Questions
See the weakness

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
There is a growing interest in using LLMs as generalist agents for open-world decision-making settings like the video game Minecraft. The authors demonstrate by example that even moderately sized LLMs (~8B parameters) are capable of performing well in this video game when (1) fine-tuned on a large question-answering dataset specific to the domain and (2) interfaced with a rich, hand-engineered skill library. Applying these ingredients to the Llama 3 8B parameter LLM, the authors show that it is possible to achieve performance that is on par with a Voyager GPT-4o Minecraft agent. The authors open source their datasets, model weights, and code.

### Strengths
- The paper is polished and well-written.
- Experiments and analyses of results are thorough. Models that are trained and evaluated using the proposed framework are compared against relevant baselines.
- The code released by the authors is clean and easy to use. 
- The performance of LMs under agentic frameworks like Voyager, which prompt models to generate skill libraries as code from scratch, depends strongly on the ability of the base model to generate quality code. In contrast, the Odyssey framework enables future work studying "tool use" in Minecraft *across* LM parameter scales by decoupling the evaluation of LMs as "high-level" vs "low-level" agentic controllers. This is a valuable contribution to the community.

### Weaknesses
 - The proposed framework has limited novelty. Decomposing complex decision-making tasks with hand-engineered skill libraries has a very long history in robotics [1,2]. The specific implementation of the skill library, while effective for Minecraft, doesn't introduce significant new techniques in task decomposition or skill representation. The paper would benefit from a more detailed analysis of how the chosen skills are different from existing approaches in robotics and how these differences contribute to the performance gains observed.
- The Odyssey framework is designed specifically for Minecraft. Agentic performance is significantly boosted through the careful design of useful, hand-engineered low-level skills. As a result, it is unclear to what extent good LM performance on Minecraft with Odyssey would transfer to other, more practical open-world environments like Web navigation. The reliance on a highly tailored skill library makes it difficult to assess the generalizability of the approach. The paper lacks a discussion of the limitations of the current skill library and how it might be adapted to other environments, including the challenges of creating similar libraries for different domains.

### Questions
It would be interesting how well even smaller LMs than Llama 3 8B would perform on Minecraft under the Odyssey framework. Have any experiments of this sort been conducted?

### Soundness
3

### Presentation
3

### Contribution
3
