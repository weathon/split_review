# LLMs for Generalizable Language-Conditioned Policy Learning under Minimal Data Requirements

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 6, 3, 3

## Abstract
To develop autonomous agents capable of executing complex, multi-step decision-making tasks as specified by humans in natural language, existing reinforcement learning approaches typically require expensive labeled datasets or access to real-time experimentation. Moreover, conventional methods often face difficulties in generalizing to unseen goals and states, thereby limiting their practical applicability. This paper presents \textit{TEDUO}, a novel training pipeline for offline language-conditioned policy learning. \textit{TEDUO} operates on easy-to-obtain, unlabeled datasets and is suited for the so-called in-the-wild evaluation, wherein the agent encounters previously unseen goals and states. To address the challenges posed by such data and evaluation settings, our method leverages the prior knowledge and instruction-following capabilities of large language models (LLMs) to enhance the fidelity of pre-collected offline data and enable flexible generalization to new goals and states. Empirical results demonstrate that the dual role of LLMs in our framework—as data enhancers and generalizers—facilitates both effective and data-efficient learning of generalizable language-conditioned policies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a policy learning method under minimal data requirements, enabling LLMs to act as both cheap data enhancers and flexible generalizers. This approach addresses the traditional RL methods' dependency on large amounts of offline data or real-time interactions. Experimental results confirm the effectiveness of the method and demonstrate a scaling phenomenon between the method and computational resources.

### Strengths
- The paper uses a substantial amount of symbolic notation to make the descriptions clearer.
- The method proposed in this paper addresses the need for real-time interaction feedback or large amounts of offline data.
- The paper demonstrates the potential performance of the method when provided with greater computational power.

### Weaknesses
1.  The pipeline proposed in this paper requires multiple stages, which imposes certain demands on computational resources.
1.  Even though the paper provides an explanation for selecting BabyAI as the sole benchmark, relying on a single benchmark to validate the method's effectiveness is insufficient. Given the claimed general applicability of the method, more robust and diverse experimental results should be presented to strengthen the evidence.

### Questions
1. Following Weakness 2, is it possible for this method to exhibit performance generalization across different datasets?
1. It appears that Figure 1 is not referenced in the main text.
1. Line 1220, the citation is not displayed correctly.

### Soundness
3

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
3

### Summary
The paper presents a novel approach, TEDUO, for training autonomous agents. TEDUO addresses the challenge of training agents that can generalize to new goals and states while requiring minimal labeled data. The approach leverages large language models (LLMs) as data enhancers and policy generalizers, which allows the use of easy-to-obtain, unlabeled datasets. The approach uses the knowledge of pre-trained large language models to achieve generalization ability, and experiments show that the method has better results and generalization ability than the baseline. However, there are some limitations: First, the method relies on the knowledge of pre-trained large language models, and if the capability of large language models is not good enough, the effect of the method may be significantly decreased. In addition, the experimental scene is relatively simple. Although the experiment proves that the method can generalize, it may not have enough generalization ability for the complex scene in reality.

### Strengths
1) TEDUO effectively leverages LLMs as both data enhancers and generalizers, thus reducing the need for expensive labeled data.
2) Focus on unlabeled, pre-collected data sets with fewer assumptions about their quality or origin.
3) Experiments show that TEDUO proves its ability to improve and generalize compared to the baseline and achieves better performance in zero-shot Settings, making it suitable for new scenarios.

### Weaknesses
1) The paper assumes that environment states can be adequately represented textually. This may restrict the approach's applicability to more complex, real-world scenarios where high-dimensional or continuous representations are required. Specifically, the method does not address how to handle environments where the state space is not easily converted to a textual description without significant loss of information, such as those involving raw sensor data or complex visual scenes. The reliance on textual representations could lead to a bottleneck in performance when dealing with richer, non-symbolic environments.
2) The success of the TEDUO framework heavily relies on the LLMs' pre-trained knowledge. If the domain is not well-represented in the LLM's training data, performance may suffer, limiting generalizability to specialized fields. This dependence introduces a potential bias towards domains well-covered in the LLM's training corpus, and it is unclear how the method would perform in novel or niche domains where the LLM lacks sufficient pre-existing knowledge. The method's reliance on the LLM's knowledge base could also lead to unpredictable performance in scenarios that require reasoning beyond the LLM's training data.
3) The focus on simpler environments like BabyAI may not reflect the challenges of real-world applications, where environments can be more dynamic and less predictable. The limited complexity of BabyAI, with its discrete action and state spaces, may not adequately test the method's ability to handle the stochasticity and continuous nature of real-world environments. This raises questions about the scalability and robustness of the approach when applied to more complex tasks.
4) The approach introduces significant computational demands, especially for LLM-based state abstraction and generalization. The computational overhead of using LLMs for state abstraction and policy generalization could make the method impractical for resource-constrained environments or for applications requiring real-time performance. The paper does not provide a detailed analysis of the computational cost associated with each step of the method, making it difficult to assess its feasibility for various use cases.

### Questions
1) While the method shows generalization capabilities, the extent to which it can handle various novel goals and states in practice remains unclear. More thorough testing in diverse scenarios is needed.
2) Performance on small models may be poor.

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
3

### Summary
This paper introduces TEDUO, a training pipeline aimed at enhancing language-conditioned policy learning in autonomous agents while minimizing data requirements. 

TEDUO leverages large language models (LLMs) to address these challenges by employing a three-step process:

**Data Enhancement**: Using LLMs to perform state abstraction and hindsight labeling on an unlabeled dataset of state-action transitions, allowing for the creation of labeled datasets.

**Policy Learning:** Applying offline RL algorithms to learn optimal policies based on the enhanced datasets for a finite set of training goals.

**Generalization**: Fine-tuning a base LLM to distill knowledge about environment dynamics and optimal actions, enabling the model to generalize to previously unseen states and language commands.

### Strengths
- The authors discuss a very interesting problem in reinforcement learning: generalization with minimal training data. This is also a general concern for RL.

- Using LLM to augment trajectory data is novel and effective. It has the potential to propose many diverse training data without setting up different environments.

- The performance of TEDUO is effective on BabyAI (table 1) and the authors also explore generalizability to compositional tasks.

### Weaknesses
1. The pipeline for data enhancement may rely on the symbolic nature of the tasks. For example, BabyAI is a easy to define symbolic task where changing the shape or color of objects and doors would result in new tasks. However, this would be more difficult to enhance data for more complex environments, e.g. VirtualHome and Alfred. Could the authors provide elaboration on how the pipeline could be generalized to a more complex environment.

2. LLMs are inherently good at simple generalizations (changing only names or objects), however the generalization of reasoning and complex planning are often more challenging. Could the authors benchmark the performance following Table 1 settings on BabyAI more advanced task levels (babyai provides a detailed task levels where some tasks are much more challenging) ? It would be helpful to emphasize what kind of generalization ability does TEDUO possesses.

3. Step 2 is not clearly written. How is an "abstract" MDP solved? For example, for solving a abstract task "picking up the object", what is the solution to the MDP. Also, how to determine if two tasks are the same type of abstract MDP or if they should be labelled as different ?

### Questions
Please see questions above.

### Soundness
2

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
To train a goal-conditioned autonomous agent, the authors propose four existing main challenges: unlabeled data, limited exploration, unknown data collection policy, and goal generalization. They solve these problems mainly through LLM. In particular, they exploit an LLM to label the unsupervised RL dataset and compress it through an LLM-written program. Once every trajectory is compressed into the latent space, they learn the policy and distillate their information into a pre-trained LLM. The presented method outperforms the baseline, and adequate ablation studies support their intuition.

### Strengths
Almost every step of the end-to-end process is automatic. For example, a pre-trained LLM works as a state labeler, so a vast amount of unlabeled data is now usable. Analogously, a state space compressing program is also written through an LLM, which minimizes the human expert's effort. Above all, goal-generalization ability is quite notable. Their experimental results show relatively less performance drop during the test phase compared to the baseline. The ablation study also strongly indicates the capability of hierarchical RL; it learns against a variety of sub-tasks and combines the solutions to reach the ultimate goal.

### Weaknesses
The first drawback is its scalability. Their proposed method can be summarized into three main steps: data labeling and compressing, policy training through offline RL, and knowledge distillation. They generate the Python program from the LLM and use that program to extract the minimal information from the original state space. This step totally relies on the characteristics of the environment. In fact, the LLM could not successfully compress the state space unless it was a discrete grid world. I can not imagine how to scale up the LLM-based state compression approach to much more complex environments. In the offline RL step, they used tabular Q-learning. Tabular iteration is one of the most powerful methods to optimize an MDP policy, but its memory consumption hardly limits its scalability. In addition, more strong baselines are required to verify the capability of their method. They mainly compared the vanilla LLM and finetuned LLM, and actually, it is trivial that finetuned LLM significantly outperforms the vanilla LLM. There is also another baseline that works without LLM, but that was published with the benchmark itself in 2018, which is too outdated these days.

### Questions
Isn't there any benchmark applicable other than BabyAI? I felt like the entire method is highly correlated to the domain knowledge of the BabyAI benchmark. Even for the BabyAI benchmark, there might be more updated solutions (I am not sure about this. I apologize if not) to be compared. Finally, it is a marginal point, but it would be better to introduce your target task or domain at the beginning of your paper. You keep to using terms such as 'autonomous agent', 'state space', and 'reinforcement learning' and it sounds like your target task is very highly abstracted MDP space. However, you also mention 'natural language-written goals' and discuss how to map them into the neural representation. Maybe introducing your domain and task thoroughly at the beginning of the introduction can enhance its readability.

### Soundness
2

### Presentation
2

### Contribution
1
