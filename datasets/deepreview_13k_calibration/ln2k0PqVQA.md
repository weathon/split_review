# Online Intrinsic Rewards for Decision Making Agents from Large Language Model Feedback

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 3, 5

## Abstract
Automatically synthesizing dense rewards from natural language descriptions is a promising paradigm in reinforcement learning (RL), with applications to sparse reward problems, open-ended exploration, and hierarchical skill design. Recent works have made promising steps by exploiting the prior knowledge of large language models (LLMs). However, these approaches suffer from important limitations: they are either not scalable to problems requiring billions of environment samples; or are limited to reward functions expressible by compact code, which may require source code and have difficulty capturing nuanced semantics; or require a diverse offline dataset, which may not exist or be impossible to collect. In this work, we address these limitations through a combination of algorithmic and systems-level contributions. We propose \oni, a distributed architecture that simultaneously learns an RL policy and an intrinsic reward function using LLM feedback. Our approach annotates the agent's collected experience via an asynchronous LLM server,  which is then distilled into an intrinsic reward model. We explore a range of algorithmic choices for reward modeling with varying complexity, including hashing, classification, and ranking models. By studying their relative tradeoffs, we shed light on questions regarding intrinsic reward design for sparse reward problems. Our approach achieves state-of-the-art performance across a range of challenging, sparse reward tasks from the NetHack Learning Environment in a simple unified process, solely using the agent's gathered experience, without requiring external datasets nor source code. We make our code available at \url{URL} (coming soon). \looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents a distributed system and an online learning algorithm for developing a reinforcement learning policy that learns from an intrinsic reward function, which is trained/obtained using feedback from LLMs. The approach depends solely on online experience, removing the need for external datasets or source code, and is assessed in the NetHack environment, comparing its performance to that of the Motif algorithm.

### Strengths
1. The proposed research problem—scaling up LLMs to generate dense intrinsic rewards for online learning—is compelling and significant for advancing LLM agents' ability to tackle complex, long-horizon tasks in real-world applications without assumption of access to expert demonstration.

2. The paper demonstrates strong engineering effort, employing online learning with help of LLMs to train an agent with up to 2 billion environment steps, a notable advance compared to prior work that required either only a few iteration of online training or a large offline dataset.

3. The experimental design effectively supports the method’s claims. The chosen testbed is well-suited, as its long-horizon nature necessitates LLM-generated intrinsic rewards to achieve successful outcomes.

### Weaknesses
1. (main) The authors compare their work only with the Motif baseline algorithm. It would be beneficial to include comparisons with goal-conditioned reward design approaches as well. In the related work section, specifically in the goal-conditioned reward design subsection, the authors list relevant studies but do not critique their limitations or highlight the advantages of their approach. Adding these comment, as done in other subsections, would strengthen the discussion.

2. In Figure 5.4, it is surprising that a higher number of annotations does not improve performance. The author might conduct an ablation study to assess the relationship between annotation volume and performance—reducing annotated data until a performance drop is observed. This may reveal that fewer labeled data points are sufficient for training the reward function, potentially reducing computational resources.

3. Using HTTP for communication between the LLM server and the annotation process may incur high communication costs. Although the authors claim minimal overhead in line 189, an experiment to demonstrate this would provide clearer evidence.

### Questions
I have outlined all my concerns in the weaknesses section. I would be happy to discuss further if the authors can address my questions.

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
3

### Summary
The paper proposes a method to simultaneously learn an RL policy and intrinsic reward function using feedback from LLMs, which annotate the agent’s experiences. The method is shown to outperform competing approaches in the NetHack environment.

### Strengths
ONI seems to be a novel approach with promising results for learning intrinsic rewards. Leveraging LLMs to learn or infer reward functions is an interesting and relevant contemporary topic.

### Weaknesses
In general, the writing could be improved for clarity. There are some sections with unnecessarily long sentences, which impeded understanding. The work could be scoped out better to clarify exactly what the contributions are. For example, the paper does not explicitly state whether the intrinsic reward function is fully learned during the training process or if it represents an approximation that evolves. A clear definition of the learning objective for the intrinsic reward would significantly enhance the paper's clarity. Additionally, the rationale behind the formulation of Equation 6 needs to be elaborated upon immediately following its presentation. The current explanation is insufficient and requires a more detailed justification to ensure the reader's comprehension. While the system design is mentioned as a contribution, it is not distinctly separated from the algorithmic contributions. These aspects should be presented in separate sections to highlight their respective importance and facilitate a clearer understanding of the overall contribution. Finally, the acronym "ONI" is used throughout the paper without ever being defined, which can lead to confusion for the reader.

### Questions
1.	What is the impact of limited annotation on the reward model? Also what is the impact of the quality of annotations?
2.	The lack of difference in performance between ranking and classification methods could be investigated further. Analyzing the distribution of intrinsic rewards generated by each method or comparing their performance on tasks with higher observation diversity could offer further insights. Have the authors considered this?
3.	It would be good to scope out clearly what the method is trying to achieve. For example, is the intrinsic reward used during learning fully learnt or is it just a current estimate?
4.	Is there a difference in the final reward model learnt via ONI and one learnt using say, a good amount of offline data? Does the reward from ONI converge? I wonder whether theoretical properties relating to this have been studied.
5.	The logic behind eq 6 should be clearly and explicitly mentioned immediately after the equation.
6.	Although it may not be directly relevant, it would be reassuring to include additional baselines (or modified versions of it) based on the reported related work.
7.	What does ONI stand for?
8.	The paper has some unusually long sentences (such as in the abstract), which should be split up for simplicity and clarity.
9.	In section 3, it would have been better to focus on the proposed approach rather than elaborating on the details in say, lines 142-148 for example. These details are not central to the understanding of ONI and could have been pushed to the appendix.
10.	URL in the abstract does not work
11.	$\eta$ is not rendered properly in Fig 5.2

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces ONI, a distributed architecture that simultaneously learns a RL policy and an intrinsic reward function using LLM feedback. ONI is built upon Sample Factory, an asynchronous reinforcement learning framework, and incorporates an LLM server hosted on a separate node to annotate observations, facilitating the learning of an intrinsic reward model that improves the sample efficiency of RL algorithms in sparse reward environments. This paper evaluates several designs of the intrinsic reward function and demonstrates ONI’s strong performance in the NetHack Learning Environment.

### Strengths
- The paper is well-written, and the method is clearly introduced.
- The limitations of previous approaches are effectively summarized, and the problem investigated is significant.

### Weaknesses
 - My primary concern lies in the novelty of the contribution. The proposed method, ONI, appears heavily intertwined with Sample Factory[1], adding only a minor extension. The distributed architecture should, in my view, be credited to Sample Factory rather than this work. Furthermore, both the LLM-based annotation and the intrinsic reward design have been previously introduced in existing research[2,3]. As a result, I believe this paper may not be suitable for acceptance at top-tier venues.
- Can the assumption of access to observation captions be relaxed, perhaps by leveraging a multi-modal LLM?
- The experimental domain is limited to the NetHack Learning Environment. Could the method be extended to other widely-used RL benchmarks, such as MuJoCo[4] or Atari[5]?
- The authors noted that increasing LLM annotations did not significantly improve performance. Could computational resources be optimized by reducing the number of annotations? What is the minimum level of annotation needed to maintain performance?
- The discussion on the method's limitations remains insufficient.
- The code is not available.

### Questions
Please take a look at the Weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
ONI introduces a novel distributed framework for developing intrinsic rewards in reinforcement learning by leveraging feedback from large language models (LLMs). This approach supports policy optimization in sparse reward scenarios without needing external datasets. By exploring several methods for reward modeling, ONI demonstrates impressive performance in the NetHack environment, closely matching the results of previous approaches like Motif while eliminating the requirement for pre-collected data

### Strengths
- ONI provides a practical and innovative way to use feedback from large language models as intrinsic rewards, making it especially valuable for reinforcement learning environments where extrinsic rewards are sparse.

- By eliminating the need for external datasets and instead building rewards from the agent’s own experience, ONI offers a scalable approach that could adapt to a wide range of tasks.

- The asynchronous design keeps the policy training process uninterrupted, maintaining high throughput and efficiency throughout.

- ONI shows strong, competitive performance in challenging tasks within the NetHack environment, matching or even surpassing state-of-the-art methods in tasks like Oracle and multi-level exploration without relying on dense reward functions.

- Enough details are provided to reproduce the method. The method reproducibility appears to be good.

### Weaknesses
 - The method is primarily evaluated in the NetHack environment, leaving questions on how well ONI would generalize to other, potentially more diverse RL environments. It would be critical to show that the method can be applied to other environments and domains. In the current state, evaluation is too narrow to demonstrate the impact of this work.

- Asynchronous LLM feedback, while effective here, may face scalability challenges in more complex settings where feedback needs scale up significantly. The paper lacks detailed discussion on this issue. Specifically, the paper does not address the potential bottlenecks in the asynchronous feedback loop, such as the overhead of communication between the agent and the LLM, and how this might impact performance in environments requiring very high throughput.

- The paper should discuss and report evaluation with different LLM. In the current state, the results cannot demonstrate that the method can be used with other LLMs. The paper should explore the sensitivity of the method to the choice of LLM, including different model sizes and architectures, as the quality and consistency of the feedback could vary significantly.

- LLM-generated annotations may carry inherent biases that can influence reward generation. The paper lacks a strategy for identifying or mitigating such biases. The paper should discuss the potential for biases in the LLM's understanding of the environment and how this could lead to skewed reward signals, and propose methods for detecting and correcting these biases.

- Comparisons with other intrinsic reward models and exploration techniques are minimal, limiting clarity on ONI's unique advantages or limitations relative to a wider range of baselines. I would suggest for instance comparing current paper with strong LLM-guided baselines, such as [“Guiding Pretraining in Reinforcement Learning with Large Language Models”, Du et al., 2023], [“Exploring Beyond Curiosity Rewards: Language-Driven Exploration in RL”, Bougie et al., 2024], or other recent papers.

### Questions
- How would ONI perform in other environments beyond NetHack, especially ones with more complex or variable observation spaces?

- Are there any insights into how specific LLM choices impact ONI's performance, especially for larger models?

- Could potential biases in LLM annotations affect the intrinsic reward generation process, and if so, how are they mitigated?

- How does the method compare with stronger recent baselines that guide exploration with LLMs?

### Soundness
2

### Presentation
3

### Contribution
2
