# True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Despite the impressive performance across numerous tasks, large language models (LLMs) often fail in solving simple decision-making tasks due to the misalignment of the knowledge in LLMs with environments. On the contrary, reinforcement learning (RL) agents learn policies from scratch, which makes them always align with environments but difficult to incorporate prior knowledge for efficient explorations. To narrow the gap, we propose TWOSOME, a novel general online framework that deploys LLMs as decision-making agents to efficiently interact and align with embodied environments via RL without requiring any prepared datasets or prior knowledge of the environments. Firstly, we query the joint probabilities of each valid action with LLMs to form behavior policies. Then, to enhance the stability and robustness of the policies, we propose two normalization methods and summarize four prompt design principles. Finally, we design a novel parameter-efficient training architecture where the actor and critic share one frozen LLM equipped with low-rank adapters (LoRA) updated by PPO. We conduct extensive experiments to evaluate TWOSOME. i) TWOSOME exhibits significantly better sample efficiency and performance compared to the conventional RL method, PPO, and prompt tuning method, SayCan, in both classical decision-making environment, Overcooked, and simulated household environment, VirtualHome. ii) Benefiting from LLMs' open-vocabulary feature, TWOSOME shows superior generalization ability to unseen tasks. iii) Under our framework, there is no significant loss of the LLMs' original ability during online PPO finetuning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- TWOSOME is a general online framework that allows LLMs to be used as decision-making agents in embodied environments.

- TWOSOME uses a two-stage approach to align LLMs with environments: first, it queries the joint probabilities of each valid action with LLMs to form behaviour policies; and second, it enhances the stability and robustness of the policies using normalisation methods and prompt design principles.

- TWOSOME exhibits significantly better sample efficiency and performance compared to other methods in both classical decision-making environment, Overcooked, and simulated household environment, VirtualHome.

- TWOSOME shows superior generalization ability to unseen tasks and does not result in a significant loss of the LLMs' original ability.

### Strengths
Strengths:

- Proposes a novel framework, TWOSOME, for aligning LLMs with embodied environments.

- TWOSOME is a general framework that can be applied to a wide range of decision-making tasks.

- TWOSOME exhibits significantly better sample efficiency and performance compared to other methods.

- TWOSOME shows superior generalization ability to unseen tasks.

- TWOSOME does not result in a significant loss of the LLMs' original ability.


Overall, the paper proposes a promising new framework for aligning LLMs with embodied environments. The framework is well-motivated and the experimental results are good.

### Weaknesses
Weaknesses:

- The paper does not provide a theoretical analysis of the proposed framework.

- The paper does not evaluate the performance of TWOSOME on a wider range of tasks and environments.

- The paper does not discuss the potential limitations of the proposed framework.

- The paper does not introduce anything novel, rather just combines existing components together to generalise to new tasks (apart from word normalisation which is fairly trivial).

- The paper does not compare to other LLM fine tuning baselines which generalise to new unseen tasks.

### Questions
-

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies using a large language model (LLM) as a decision-making agent to interact with an embodied environment. Specifically, the authors proposed to train the policy with reinforcement learning (RL). First, the policy is formed by querying the LLM with each feasible action in a given state. Then, token normalization and word normalization approaches are proposed to stable the training. The proposed approach is evaluated on Overcooked and VirtualHome. The experiments show that the proposed approach outperforms baselines in terms of sample efficiency and return.

### Strengths
Originality and Significance:   
The reviewer appreciates the motivation of the paper: Classical RL agents align well with a given environment but fail to leverage prior knowledge. On the other hand,  LLM has numerous prior knowledge while often fails to align with the given environment. This paper proposed a method to align the LLM policy with the environment and show improvement over classic RL methods.  

Quality:  
The paper is technically sound and the claims are supported by experiments. 

Clarity:    
This paper is generally well-organized and easy to follow. Some minor improvement may be required. Please see the Question section for details.

### Weaknesses
1. The idea of querying joint probabilities of each valid action with LLM to form a policy is explored in previous works such as GLAM (Carta et al., 2023). The reviewer found, in the current version, the credit is not clearly given to authors of previous works. 

2. The reviewer has some concerns on the baselines used in the experiments. In Figure 5, aside from the ablations, the authors only consider classic PPO as a baseline. It seems unfair to directly compare an agent equipped with LLM with a classic trial-and-error PPO agent which doesn’t have access to the prior knowledge in LLM. There are many existing works that leverage LLM to form RL policies [1, 2, 3]. Particularly,  Li [1] also uses virtualHome as test environments. Comparing approaches that also leverage knowledge in LLM could make the experimental section more convincing. 

3. The technical contribution of the paper is somewhat limited. Specifically, the idea of forming valid policy is proposed by previous works and LoRA for fine-tuning is a standard method. The review found the main new method is the proposed normalization approach. That to be said, the reviewer still considers the combination of existing methods might be valuable to our embodied AI community.

### Questions
1. As discussed in Weakness, comparing with methods that also leverage LLM for RL agent could make the experimental section more convincing.  

2. In the experiments, only two tasks from virtualHome and Overcooked are considered. Reporting results on more tasks would be helpful. 

3. In Section 4.3, it reads “The critic’s MLPs use the last token of the observation prompt as input …”. Could you elaborate why only the last token of the observation prompt is used? Shouldn’t the MLP use the output of the frozen LLM?

Minor:    
  4. In Eq (2), using $a_k$ in the summation is confusing.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides TWOSOME (True knoWledge cOmeS frOM practicE), a Large Language Model (LLM)-based policy learning method that fine-tunes a LLM agent with a Reinforcement Learning (RL) algorithm. To address problems incurred when adopting text actions sampled from a LLM policy, this paper proposes a normalization method that divides the log probability of a text action by the number of words (or tokens). This paper demonstrates the effectiveness of TWOSOME by employing Llama-2-7B as a LLM agent and fine-tuning the LLM agent with Proximal Policy Optimization (PPO). This paper provides experiment results in Overcooked and VirtualHome, and shows that the LLM agent fine-tuned with PPO can learn better policy.

### Strengths
- S1. The main approach of fine-tuning a LLM agent (e.g., Llama-2-7B) with a RL algorithm (e.g., PPO) proposed in this paper seems interesting and promising. This approach can be seen as applying recent prevalent reinforcement learning with human feedback (RLHF) into decision-making tasks.

- S2. This paper provides promising initial results toward fine-tuning LLM agents with RL methods.

### Weaknesses
 - W1. The overall approach of TWOSOME is to fine-tune a LLM agent (e.g., Llama-2-7B) with a RL algorithm (e.g., PPO). And, the unique contribution of TWOSOME can be seen as providing a normalization method for the probability distribution over text-based actions sampled from a LLM policy. This paper proposes two normalization methods: token normalization (Eq. 3) and word normalization (Eq. 4). Even though this paper proposes a promising direction towards fine-tuning a LLM agent with a RL algorithm, the main contribution seems rather marginal. The normalization method is about dividing the log probability of a varying length text-based action by the number of words (or the number of tokens). It seems to compensate a text action with larger number of words, but I am not sure that this kind of simple division is a proper way to normalize varying length text actions sampled from a LLM policy. The core issue is that the probability of a sequence of tokens is the product of individual token probabilities, which naturally favors shorter sequences. While dividing by the number of tokens or words might mitigate this bias, it doesn't address the underlying issue that the probability space for longer sequences is inherently more sparse, making it difficult to learn a robust policy over such actions. The proposed normalization might also distort the true probability distribution, potentially leading to suboptimal policy learning.

- W2. This paper shows that TWOSOME can learn the optimal policy in a simple environment like Overcooked. However, I am not sure that TWOSOME can properly learn optimal policy in a complex environment like VirtualHome. When showing the performance of TWOSOME in VirtualHome, the authors masks out unrelated actions to reduce the complexity of the action space. This raises concerns about the generalizability of the method to more complex scenarios without such manual intervention. The action masking, while practical, might be hiding the true limitations of the approach in handling a large and diverse action space. The fact that the method relies on a predefined set of actions also limits its ability to handle novel or unseen actions, which is a crucial aspect of real-world decision-making tasks.

### Questions
- Q1. Regarding W1, how does the word normalization help LLM agents to learn better policy? What is the intuition of the word normalization?

- Q2. Regarding W2, without manual action masking in VirtualHome, how much scores can TWOSOME achieve?

- Q3. Recently, in RLHF, some enhanced RL algorithms such as Direct Policy Optimization (DPO) and Pair-wise Proximal Policy Optimizaition (P3O) have been proposed. Can these enhance RL algorithms be applied to solving decision making tasks? And then, can we expect some performance improvements of TWOSOME?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces TWOSOME, a novel finetuning method designed to ground Large Language Models (LLMs) in embodied environments. TWOSOME comprises three main components: action-selection, where the LLM identifies the best action from a list of actions on criteria such as likelihood, token normalization, and word normalization, LoRA updates and prompt design. The authors conducted empirical experiments using TWOSOME on four fine-tuning tasks within Overcooked/VirtualHome environments. Their results demonstrate that TWOSOME's word normalization component outperforms others. Moreover, the fine-tuned policies exhibit superior generalization to unseen tasks in zero-shot scenarios. Remarkably, TWOSOME's capabilities in NLP benchmarks remain unaffected after the fine-tuning process.

### Strengths
- The authors noticed the limitation of considering plain action likelihood (a problem known in NLP when selecting different texts based on likelihood of the full sentences). To my knowledge, the word normalization is new and I really liked the idea when noticing that dividing by the sequence length is not enough to mitigate the end of words being more likely.
- The authors worked in a compute budgeted setting so the work can be reproduced easily.
- I really liked the task generalization section.
- Results on showing little to no catastrophic forgetting on NLP tasks (possibly coming from LoRA?) are really promising.

### Weaknesses
 - As for now it is hard to consider LoRA to be part of the proposed method: hard to see the benefits of the LoRA contribution to sample efficiency and no catastrophic forgetting without an ablation on with and without LoRA. 
The contribution of the method seems to be the action normalization and some prompt design (qualitatively assessed by the authors in 4.4).  Could you add experiments on these points? 

- Paper mentions that (Carta et al, 2023) “focus on primitive actions in toy environments without rich semantics“. I am not sure actions are primitive in (Carta et al, 2023) but rather semantically described actions, e.g. “go forward”, “turn left”, “drop and toggle”. What makes them more “primitive” seems to be the environment they chose for experimenting (BabyAI vs Overcooked/VirtualHome). 

- Regarding the choice of environments. I am afraid there are too few fine-tuning tasks. I might be wrong, but the task generalization seems almost too-good from 4 tasks only. BabyAI was procedurally generated which would have enabled experimentation on more finetuning tasks.

### Questions
- Can you elaborate on the difference between (Carta et al, 2019) and unnormalized action selection.
- Can you explain the PPO baseline: state/action space and architecture and initialization here (and in the main paper)? This would help in understanding the contribution of pretrained initialization.
- Discussion question (not required to increase my score): 
     - Do you have insights on the use of embodied environments to **improve** LLMs, e.g. dealing with safety concerns?  How to design such environments?
    - It would be nice to see how multi-modal text generation could be used to remove the assumption that the agent can extract a textual description of its state.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
