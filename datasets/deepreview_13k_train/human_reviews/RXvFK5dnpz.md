# Contextual Experience Replay for Continual Learning of Language Agents

- Decision: Reject
- Scores: 5, 3, 6, 3

## Abstract
Large language model-based agents have shown their potential in decision-making tasks, such as web navigation. However, solving multi-step decision-making tasks in complex environments like websites often requires the acquisition of environment-specific experiences. Without continual learning of environment-specific knowledge, current methods often fail in these complex tasks. To address this, we propose Contextual Experience Replay (CER), a novel training-free framework to enable efficient continual learning for language agents through experience replay contextually, i.e. in their context window. CER is loosely inspired by experience replay in reinforcement learning, where the agent is trained with past experiences to do continual learning. Specifically, CER accumulates and synthesizes past experiences, which are represented as natural language summarizations and concrete trajectory examples, into a dynamic memory buffer. These experiences encompass environment dynamics and common decision-making patterns, allowing the agents to retrieve and augment themselves with relevant knowledge in new contexts, enhancing their adaptability in complex environments. We evaluate CER on the challenging WebArena and VisualWebArena benchmarks. While orthogonal to other methods, CER improves the GPT-4o agent baseline by a large margin and gets competitive results. On VisualWebArena, CER surpasses the tree search method with much lower token costs and achieves a state-of-the-art success rate of 31.9%. On WebArena, CER also gets a competitive average success rate of 33.16%, relatively improving the success rate of the GPT-4o agent baseline by 36.69%. CER shows that the continual learning of environment-specific knowledge is important and can lead to significant improvements in sequential decision-making tasks in complex environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This submission proposes Contextual Experience Replay (CER) as a continual learning approach that accumulates experiences from the task domain and retrieves relevant ones for later tasks, for building web navigation agents. Specifically, upon obtaining a new experience, they distill it into dynamics-related and behavior-related descriptions, which can be retrieved for augmenting the LLM agent's decision-making on different but relevant or similar tasks. The authors perform an empirical evaluation of their approach on WebArena and VisualWebArena tasks and demonstrate that this approach outperforms the compared baselines. They also provide additional empirical analyses in multiple aspects, such as continual learning concerns (knowledge preservation vs acquisition) and different types of source data.

### Strengths
- The proposed approach is overall sound. Pre-trained LLMs often lack domain knowledge due to the required specificity and continuous updates (like websites), and distilling knowledge from experiences for incorporation into LLMs' input contexts can be useful to mitigate such issues.
- The authors provide multiple empirical analyses with the proposed approach, such as the source of trajectory data and knowledge preservation and acquisition study. These can provide a deeper understanding of the proposed approach.
- Overall, the manuscript is easy to follow, especially with the well-visualizing figures.

### Weaknesses
 - While the continual accumulation of experiences are often useful in practice and the accumulated knowledge can be useful information, doing so during the evaluation on the test task set from each of those benchmarks can make the comparison with other baseline approaches unfair. In most benchmark setups, gaining knowledge about other test tasks usually provides noticeable performance boosts primarily due to the task similarities and increased data size. To properly compare the performance of the proposed approach with the baselines in a "held-out" setting, the "self-guided explorations" configuration from Table 3 seems more appropriate, as it performs the same but without the knowledge of what will happen during the completion of each task.
- I notice that there is a methodologically close paper that is not cited and compared: Fu et al., 2024 (AutoGuide: Automated Generation and Selection of State-Aware Guidelines for Large Language Model Agents). For instance, I think there is some correspondence as follows: (CER's distillation, their guideline extraction), (CER's top-k dynamics and skill retrieval, their top-k guideline retrieval).
- There are some minor typos in the writing, such as missing periods and mis-capitalizations.

### Questions
Please check out the weaknesses section.

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
4

### Summary
This paper proposes CER, which distills foundation model agent experience into environment dynamics knowledge and action guidance to help with decision making, in online or/and offline setting. The authors presented performance improvements on realistic web navigation domains WebArena and VisualWebArena, demonstrating the effectiveness of the proposed method.

### Strengths
- The authors conducted a variety of experiments to analyze the performance from different perspectives. 
- CER shows some promise to learn from failed experience of foundation model agents.

### Weaknesses
 - Missing important baselines and overstating paper contribution: The authors claim that the method is the first framework that distills experiences into both environment dynamics and decision-making patterns from both successful and failed trajectories. However, there are existing works that do the same and also work on challenging tasks like WebArena. For example, 
  - AutoGuide[1] summarizes contextual guidelines from successful and failed trajectories, where the state serve as a similar role as the dynamics and the guideline serves at the same role as decision making patterns.
  - AutoManual[2] autonomously interact with the environment and categorizes environmental knowledge into rules in an online manner. 
- The writing of the method section can be further improved. The author claim that a major contribution of the method is to learn from both successful and failed experience. However, it is unclear how this is done until the experiment section, making it a bit confusing.

### Questions
- Is the current online experiment conducted in the order of the default task ID of the benchmarks? Are the any specific order that will further favor the online learning? For example, a curriculum learning like easy to hard ranking of the tasks. 
- How is the hyper-parameter top-k selected? How will a different k influence the performance? 


---
[1] Fu, Yao, Dong-Ki Kim, Jaekyeom Kim, Sungryull Sohn, Lajanugen Logeswaran, Kyunghoon Bae, and Honglak Lee. "Autoguide: Automated generation and selection of state-aware guidelines for large language model agents." arXiv preprint arXiv:2403.08978 (2024).

[2] Chen, Minghao, Yihang Li, Yanting Yang, Shiyu Yu, Binbin Lin, and Xiaofei He. "AutoManual: Generating Instruction Manuals by LLM Agents via Interactive Environmental Learning." arXiv preprint arXiv:2405.16247 (2024).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents Contextual Experience Replay (CER), a training-free framework to enable efficient continual learning for language agents in sequential decision-making tasks. Specifically, the methodology includes three processes: distilling experiences from trajectories, retrieving experiences from the buffer, and decision-making with contextual experience replay. The methodology can be divided into offline, online and hybrid versions. Experiments conducted on WebArena and VisualWebArena demonstrate the effectiveness of the approach.

### Strengths
1. Continual learning for language agents is a very important topic, and this paper focuses on it by choosing the Web navigation task for study.
2. This paper is well-crafted, with the authors' perspectives clearly and effectively conveyed.
3. The experiments in the paper are thorough, and the authors provide a comprehensive and convincing analysis.

### Weaknesses
1. This paper lacks an evaluation of failed cases and does not address common reasons for the agent’s failure in performing web navigation tasks. For example, failures could arise from misleading input experiences or limitations in the model’s grounding capabilities. To strengthen the evaluation, the authors could consider conducting a manual error analysis to understand the bottleneck for continual learning on web navigation tasks. Specifically, the analysis should categorize failure modes, such as the agent's inability to backtrack when encountering a dead end, or a failure to utilize the full trajectory history, such as not tracking previously visited pages or items. Another failure mode could be the agent's failure to verify relevant context before action, such as clicking on a post without checking if it's the most recent one, or not sorting a forum before selecting a post. A detailed error analysis should quantify the frequency of each failure mode.
2. Additionally, the paper does not explore whether tasks previously failed by the agent can be successfully completed upon reattempt, following a process of summarizing and learning from those failures. To validate this, the authors could include an ablation study that retests previously failed tasks to observe whether the agent’s capabilities have improved. This is crucial for understanding the agent's ability to learn from its mistakes and improve over time, which is a key aspect of continual learning.

### Questions
1.  **Token Efficiency of CER**: The paper mentions that CER can operate with fewer toknes compared to other methods. Could the authors provide statistics on token usage? Additionally, when reporting token efficiency, is the token expenditure from processes like distillation included? 

2. **Fairness of the "Online Setting" in the Main Experiment**: I am somewhat confused by the authors' claim that the "online setting" is fair in the main experiment. In my view, the agent should not use experiences gained from the test set during the testing phase, as this could bias the results in its favor. If the agent leverages data from the test set more than other methods do, this could inherently be unfair. Perhaps dividing the benchmark into separate training and testing sets would be a more balanced approach. I recommend the authors to:

  - Clarify how their online setting compares to standard evaluation practices in continual learning.
  - Discuss potential biases introduced by this approach and how they might affect the interpretation of results.
  - Consider running an additional experiment as suggested if the potential biases are significant.

3. **Clarification on Experience Retrieval Using LLMs (Section 3.2)**: Section 3.2 lacks clarity on how experiences are retrieved. Are large language models specifically employed to select the most similar experiences? If so, how does this retrieval approach compare to traditional algorithms in terms of advantages and disadvantages? Furthermore, does the context window limitation of LLMs affect retrieval effectiveness? Lastly, what is the accuracy of this retrieval method? It would be beneficial to include any metrics or evaluations used to assess retrieval performance.

4. **Further Explanation and Examples for "Environment Dynamics"**: It would be helpful if the authors could provide a few more examples to clarify the definition of "environment dynamics". Additionally, how transferable are the experiences obtained from certain websites to other, potentially new, websites? I hope the authors can give me some examples from experiments to explain this.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces the concept of Contextual Experience Replay (CER), allowing agents to leverage limited experiences while performing web navigation tasks. These experiences can be categorized as offline, which are pre-defined external experiences, online, where the agents reuse their own previous experiences, or a hybrid of both. The authors evaluated CER on two representative web navigation tasks, demonstrating its effectiveness.

### Strengths
The idea proposed in this paper has practical significance. Considering the high post-training costs, a training-free self-improvement method is undoubtedly more attractive, yet also more challenging.

The authors have made some commendable choices in their experimental setup. For instance, they thoroughly considered offline, online, and hybrid scenarios, resulting in a well-rounded narrative. Furthermore, the ablation study was quite comprehensive, examining aspects like template stability, plasticity, etc., which provided a better characterization of CER.

The paper's layout, illustrations, and tables are aesthetically pleasing, leaving a good impression on the readers.

### Weaknesses
Nonetheless, I must offer my apologies as I have several concerns regarding this paper. Allow me to expound on each of these concerns.

First, from a writing standpoint, the paper gives me a somewhat informal impression. (Although the layout is visually appealing, the writing itself, in my opinion, is not of a satisfactory standard.) For instance, in the introduction, the authors emphasize the advantages of web navigation tasks, such as being more controllable than OS tasks and more complex than mobile environments. However, this does not justify why the authors only tested on two related tasks from WebArena in this work on CER. Moreover, considering that Visual WebArena involves multimodal capabilities (which is commendable for incorporating such capabilities), it effectively means that one pure language task and one multimodal task were tested, making it difficult to be convinced of the generalization of the CER method. For example, at the very least, attempting a classic benchmark like WebShop would make this work more persuasive.

In terms of writing, I feel that the paper uses too many terms without sufficient explanation, which gives the impression of inundating readers with jargon. For example, the authors define their work as continual learning and experience replay. If these terms are well-established in the field, the theoretical nature of these terms warrants the establishment of a theoretical framework to prove the effectiveness of the CER method. Conversely, if these terms are coined by the authors, more rigorous discussion is needed rather than presenting the terms without further elaboration, which leaves a sense of shallowness.

Incidentally, I also mentioned that this paper's idea merits a theoretical framework for analysis. I recommend referring to the following papers:

https://arxiv.org/pdf/2407.18219

https://openreview.net/forum?id=9W6Z9IeLzc

Next, in terms of experiments, I have already pointed out the deficiencies of the benchmark. Nevertheless, it appears that the authors primarily tested the effectiveness of GPT-4o, a single model, and conducted most of the experiments based on this closed-source model? This raises several concerns, such as the possibility of real-time updates to the closed-source model, making it difficult to reproduce the results in future work. Additionally, can using only one current state-of-the-art model demonstrate that CER is also effective for weaker open-source models? Therefore, I strongly recommend that the authors conduct more experiments using a wider variety of models. If the authors are unable to do so due to the high cost of experiments, I fully understand. However, I did not see such a statement in the paper. (I believe you could have used this reason to justify why only web navigation was selected since the academic community understands the scarcity of computing resources on campus. However, given your previous claim that web navigation is more controllable and complex, it is hard to avoid the impression that you are not lacking resources but are unwilling to put in the extra effort to illustrate your method more comprehensively.)

Lastly, in terms of method, I do not entirely agree that CER is the first framework to leverage experiences. At least, you can refer to this 2023 paper, which proposed the idea of leveraging experiences earlier:

https://github.com/PanasonicConnect/rap

Please refrain from overstating your work, or at least add qualifiers to narrow the scope of your research.

There are also some debatable aspects, such as your reliance on relative improvement in your experimental results. In my view, this is not an ideal metric because, as you mentioned, these two web navigation benchmarks only have a success rate of less than 20%. Even if you achieved more than a 30% relative improvement, how significant is this improvement in absolute terms?

In summary, I am pleased that you recognize the importance of experience for workloads like agents, which is closely related to in-context learning in NLP. I believe you could also attempt to frame your argument from this perspective. I have raised many issues, and if you are willing to seriously rebut them, there is much that can be done to enhance your experiments. The writing flaws will be difficult to address in the short term, but I hope you take them seriously. Good luck.

### Questions
See the weakness.

### Soundness
2

### Presentation
2

### Contribution
2
