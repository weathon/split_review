### Summary

This paper presents a method that uses large language models (LLMs) to generate subgoals to aid training of multi-agent reinforcement learning (MARL) policies. The proposed approach, Semantically Aligned Task Decomposition in Multi-Agent Reinforcement Learning (SAMA), uses LLMs to generate a language-based task decomposition into per-agent subgoals which are used to train MARL policies that are conditioned on subgoals. The authors present experiments on Overcooked and MiniRTS, two multi-agent environments that are commonly studied in the MARL literature. The authors compare to several prior methods in these two domains, and show that SAMA achieves strong performance in both.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The problem of temporal credit assignment is certainly an important one in multi-agent RL, and the use of subgoals is a promising approach to solving this problem. 
- The use of LLMs to generate subgoals is also a promising approach, and the proposed SAMA method is a novel combination of prior work in language-conditioned RL and LLM-based goal generation. 
- The authors present experiments on two well-studied multi-agent domains, and show that SAMA achieves strong performance in both. The experimental results are sufficient to demonstrate the promise of the proposed approach.

### Weaknesses

#### Some Related Works

[1] Language-Conditioned Goal Generation for Hierarchical Reinforcement Learning
[2] Grounding Language in Multi-Agent Reinforcement Learning
[3] Learning to Compose Language into Multi-Step Actions for Task Planning
[4] Intrinsic Motivation via Language Prompting in Multi-Agent Reinforcement Learning

#### comment

 - The proposed approach is fairly complex, involving several steps of prompting of LLMs, and it is not clear that each step of the method is necessary. The authors do not present any ablations to justify the design choices in the method, and it is not clear that the proposed approach is simpler or more effective than a simpler approach that uses LLMs to generate dense rewards for subgoal completion. The lack of ablation studies makes it difficult to assess the contribution of each component of the method, such as the specific prompting strategies, the self-reflection mechanism, and the use of chain-of-thought reasoning. It is possible that a simpler approach, such as directly prompting the LLM to generate rewards based on subgoal completion, could achieve similar or better performance with less complexity.
- The authors do not compare to several relevant baselines that use LLMs to generate subgoals or rewards for reinforcement learning. In particular, the authors should compare to prior work on using LLMs to generate subgoals for single-agent hierarchical RL [1], as well as prior work on using language to provide rewards for subgoal completion in multi-agent RL [2, 3, 4]. The absence of these comparisons makes it difficult to assess the novelty and effectiveness of the proposed approach compared to existing methods. Specifically, the authors should compare to methods that use LLMs to generate subgoals in a hierarchical RL setting, as well as methods that use language to provide rewards for subgoal completion in multi-agent RL. These comparisons are crucial for understanding the advantages and disadvantages of the proposed approach.
- The authors do not clearly describe the implementation details of the prior methods that they compare to, and it is not clear that the comparisons are fair. For example, the authors mention that several of the compared baselines use population-based training, but it is not clear whether SAMA also uses population-based training. The lack of clarity regarding the implementation details of the baselines makes it difficult to assess the validity of the comparisons. It is important to ensure that all methods are compared under similar conditions, and that any differences in performance are due to the methods themselves rather than differences in implementation details.

### Suggestions

The authors should conduct a thorough ablation study to justify the design choices in their method. This should include ablating each step of the method, such as the specific prompting strategies, the self-reflection mechanism, and the use of chain-of-thought reasoning. The authors should also compare their method to a simpler approach that uses LLMs to generate dense rewards for subgoal completion, to determine whether the proposed approach is simpler or more effective. The ablation study should also investigate the impact of different few-shot examples used in the prompts, to ensure that the results are not sensitive to the choice of examples. The authors should also provide a detailed analysis of the computational cost of their method, and compare it to the computational cost of the baselines.

The authors should compare their method to several relevant baselines that use LLMs to generate subgoals or rewards for reinforcement learning. This should include prior work on using LLMs to generate subgoals for single-agent hierarchical RL [1], as well as prior work on using language to provide rewards for subgoal completion in multi-agent RL [2, 3, 4]. The authors should also compare to methods that use LLMs to generate subgoals in a hierarchical RL setting, as well as methods that use language to provide rewards for subgoal completion in multi-agent RL. These comparisons are crucial for understanding the advantages and disadvantages of the proposed approach. The authors should also provide a detailed analysis of the differences between their method and the baselines, and explain why their method is expected to perform better.

The authors should provide a detailed description of the implementation details of the prior methods that they compare to, and ensure that the comparisons are fair. This should include clarifying whether SAMA also uses population-based training, and ensuring that all methods are compared under similar conditions. The authors should also provide a detailed analysis of the computational cost of their method, and compare it to the computational cost of the baselines. The authors should also provide a detailed analysis of the sensitivity of their method to the choice of prompts, and compare it to the sensitivity of the baselines. The authors should also provide a detailed analysis of the robustness of their method to different environments, and compare it to the robustness of the baselines.

### Questions

- What few-shot examples are used in the prompts? Are the results sensitive to the choice of few-shot examples?
- How does SAMA compare to prior methods that use LLMs to generate subgoals or rewards for multi-agent RL? In particular, how does SAMA compare to prior work on using LLMs to generate subgoals for single-agent hierarchical RL [1], as well as prior work on using language to provide rewards for subgoal completion in multi-agent RL [2, 3, 4]?
- Does SAMA use population-based training? If not, how do the authors ensure that the comparisons to prior methods that use population-based training are fair?

**References**

[1] Language-Conditioned Goal Generation for Hierarchical Reinforcement Learning. Song et al. NeurIPS 2023.

[2] Grounding Language in Multi-Agent Reinforcement Learning. Wang et al. NeurIPS 2023.

[3] Learning to Compose Language into Multi-Step Actions for Task Planning. Chen et al. NeurIPS 2023.

[4] Intrinsic Motivation via Language Prompting in Multi-Agent Reinforcement Learning. Hugues et al. NeurIPS 2023.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
