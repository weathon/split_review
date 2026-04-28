# OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models

- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 8, 8, 6, 6

## Abstract
Offline evaluation of LLMs is crucial in understanding their capacities, though current methods remain underexplored in existing research.
In this work, we focus on the offline evaluation of the chain-of-thought capabilities and show how to optimize LLMs based on the proposed evaluation method.
To enable offline feedback with rich knowledge and reasoning paths, 
we use knowledge graphs (\emph{e.g.}, Wikidata5M)
to provide feedback on the generated chain of thoughts.
Due to the heterogeneity between LLM reasoning and knowledge graph structures, direct interaction and feedback from knowledge graphs on LLM behavior are challenging, as they require accurate entity linking and grounding of LLM-generated chains of thought in the knowledge graph.
To address the above challenge, 
we propose an offline chain-of-thought evaluation framework, \texttt{OCEAN},
which models chain-of-thought reasoning in LLMs as a Markov Decision Process (MDP),
and evaluate the policy's alignment with knowledge graph preference modeling.
To overcome the reasoning heterogeneity
and grounding problems, we leverage on-policy knowledge graph exploration and reinforcement learning to model a knowledge graph policy that generates token-level likelihood distributions for LLM-generated chain-of-thought reasoning paths, simulating knowledge graph reasoning preference.
Then we incorporate the knowledge-graph feedback on the validity and alignment of the generated reasoning paths into \textit{inverse propensity scores} and propose KG-IPS estimator.
Theoretically, we prove the unbiasedness of the proposed KG-IPS estimator and provide a lower bound on its variance.
With the off-policy evaluated value function, we can directly enable off-policy optimization to further enhance chain-of-thought alignment.
Our empirical study shows that OCEAN can be efficiently optimized for generating chain-of-thought reasoning paths with higher estimated values 
without affecting LLMs' general abilities in downstream tasks or their internal knowledge.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores a novel approach for enhancing the chain-of-thought (CoT) reasoning in large language models (LLMs) through an offline evaluation and optimization framework. The proposed OCEAN framework utilizes knowledge graphs (KGs) to provide feedback and improve alignment in CoT tasks by modeling reasoning paths as a Markov Decision Process (MDP). By employing a KG-based inverse propensity score (KG-IPS) estimator, the framework enables unbiased offline evaluation, bridging the gap between LLMs and structured KG reasoning to ensure consistent, accurate CoT reasoning without undermining LLMs' performance in general tasks.

### Strengths
1. The concept of aligning CoT reasoning with knowledge graphs via a KG-IPS estimator is well-motivated, particularly in addressing the challenges associated with human feedback limitations and online deployment costs. The offline nature of the OCEAN framework allows for feasible and efficient model alignment using KGs as a structured feedback source.

2. The paper provides a thorough theoretical foundation for the KG-IPS estimator, proving its unbiasedness and offering a variance lower bound. This adds robustness to the evaluation framework and offers a sound basis for its application in LLM alignment.

3. The authors conduct a wide range of experiments across multi-hop question answering, knowledge-intensive tasks, and commonsense reasoning. These diverse evaluations demonstrate OCEAN's ability to align reasoning paths effectively while maintaining or enhancing the generalization capabilities of the LLMs across domains.

### Weaknesses
1. While the OCEAN framework is well-conceived, the reliance on multiple components (MDP formulation, KG-IPS estimator, verbalized KG policy) might limit its accessibility for practitioners. Simplifying or modularizing the system, potentially with more explicit guidance for implementation, could improve its applicability.

2. Limited Scope in KG-Based Reasoning Tasks: Although the alignment with KGs enhances factual consistency, the paper does not deeply explore its limitations in more abstract CoT reasoning, where LLMs rely on conceptual, rather than fact-based, reasoning. This could be an area for future work, as abstract reasoning is a critical facet of human-like reasoning in LLMs.

3. The paper focuses on large-scale LLMs, which are often resource-intensive to train and evaluate. While the experiments are comprehensive, further validation on smaller LLMs could strengthen the claim of OCEAN's adaptability across various scales.

### Questions
1. Could you elaborate on the specific challenges encountered in balancing entity and non-entity token weights in the KG-IPS estimator? How sensitive is the estimator to variations in these weights across different types of reasoning tasks?

2. Since your framework relies on structured knowledge graphs, how does OCEAN perform on CoT reasoning tasks that are less fact-based and more abstract or conceptual? Have you considered extending the model to handle these types of reasoning, and what might be the challenges?

3. Given the framework's reliance on multiple components (e.g., MDP modeling, KG-IPS estimator), what is the additional computational overhead compared to baseline CoT methods? Could you provide some insights into how to make OCEAN more computationally efficient?

4. How well does the OCEAN framework adapt to different types of knowledge graphs (e.g., smaller or domain-specific KGs)? What, if any, modifications are necessary when using a KG that differs substantially in structure or domain from Wikidata5M?

5. In some tasks, you noted the possibility of knowledge conflicts when aligning LLM outputs with knowledge graphs. How does OCEAN address or mitigate conflicts between an LLM's parametric knowledge and KG-based feedback, especially in cases where both knowledge sources might offer valid, but differing, information?

6. The paper mentions using sub-Gaussian concentration inequalities to establish confidence intervals for the KG-IPS estimator. Could you explain why this choice was made and how these intervals compare to other possible statistical measures?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a novel technique for performing offline evaluation of the chain-of-thought capabilities of LLMs using trajectories generated on knowledge graphs. Specifically they propose a well thought out framework, coined OCEAN, which models CoT reasoning in language models as an MDP, where they leverage on-policy reinforcement learning methods to learn a knowledge graph policy which generates likelihood distributions for LLM reasoning paths. They then define and introduce the KG-IPS estimator to evaluate the policy, which they prove is unbiased while also providing a lower bound on its variance. They then discuss how this estimator can be used for policy optimization which would align LLMs to favor the reasoning paths generated in the knowledge graph. Finally, they conduct experiments to evaluate their approach in knowledge-intensive, multi-hop and common sense reasoning tasks compared to various baseline and supervised fine-tuned language models.

### Strengths
1. The paper considers a practical approach for the offline evaluation of LLMs, which is an important area of research given that the dominant approach of RLHF is highly labor intensive and expensive.
2. The notion of using knowledge graphs for LLM alignment is very interesting, and their approach consisting of verbalizing the KG trajectories is novel to the best of my knowledge.
3. The paper contains very detailed and thorough experiments to demonstrate their results empirically.
4. Theoretical proofs look sound.
5. The paper is very well-written and enjoyable to read.

### Weaknesses
1. One aspect of the methodology that was not clear is the case where there are multiple trajectories that lead to the correct answer, which I believe can often be the case in reasoning tasks solved by LLMs. How will this be represented in the knowledge graph preference policy? Additionally, does the current methodology hold the potential to penalize reasoning paths that are correct but just not identified in a knowledge graph?

2. In a similar vein, it is not clear that the knowledge graph used in this model (which seems to be Wikidata5M) is extensive enough to capture all possible reasoning paths given I believe it only contains entities and relations captured on wikipedia. I think it is imperative that the authors provide more information on the specific knowledge graph they are using and why it is sufficient to model reasoning queries given to LLMs.

3. It is not clear from the tables provided in Section 5 that the OCEAN model significantly outperforms the baseline. A more detailed discussion explaining this seems necessary.

### Questions
Some questions were raised above. 

1. Why did you choose to 'verbalize' the trajectories generated on the knowledge graphs instead of inversely trying to reformat the LLM reasoning chain as a trajectory using entity and relationship linking? This approach seems initially more intuitive and less likely to cause errors?

### Soundness
3

### Presentation
4

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
This paper focuses on evaluating Chain-of-Thought (CoT) reasoning with guidance from a Knowledge Graph (KG). The authors propose training a KG model as a reference and using KG-IPS to assess the target language model's performance based on the reference model’s output. They conduct extensive experiments to support this approach.

### Strengths
Overall, I find the paper’s idea and methodology compelling. The provided theoretical analysis is nice and the experimental results can support their statements.

### Weaknesses
 Overall, I find the paper’s idea and methodology compelling. The provided theoretical analysis is nice and the experimental results can support their statements.

 However, improvements in writing would enhance readability and comprehension.

Please use the full name when introducing KG-IPS for the first time.

What role does the base LLM policy $\pi_0$ play? Including a figure to illustrate the entire pipeline—showing the knowledge graph reference policy $\mu_\phi$, target policy $\pi_\theta$, and base LLM policy $\pi_0$—would improve clarity and help readers follow the workflow more easily. 

Could you expand on Equation 3, especially explaining the term $T_i | c_t^{(I)}$ and the intuition behind defining this term after the third summation symbol?

What does the x-axis in Figures 1(b) and 1(c) represent? This clarification is essential to verify the conclusions in the final paragraph of Section 4.

Readers might also wonder about the performance of the reference models and how the architecture of these models impacts the evaluation of the target model.

Finally, how would the reference model perform if it included process-based reward signals rather than relying solely on binary outcome signals defined by answer accuracy? Is a binary signal sufficient, or would process-based feedback add value?

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Evaluating the chain-of-thought (CoT) reasoning of large language models (LLMs) is challenging due to the difficulty in gathering accurate labels. Since CoT reasoning involves a sequential decision-making process, using traditional feedback methods like reinforcement learning from human feedback (RLHF) becomes impractical. The author leverages knowledge graphs to address the challenge of evaluating LLMs CoT offline. The authors propose aligning LLMs' multi-step reasoning with multi-hop knowledge graph trajectories using inverse propensity scores (IPS). Specifically, the author proposes OCEAN, an estimator that evaluates a model's reasoning ability using CoTs from knowledge graphs. The authors demonstrated that their proposed offline evaluation method performed well across several reasoning tasks, including multi-hop question answering, knowledge-intensive question answering, and commonsense reasoning.

### Strengths
- The authors are focused on addressing a very important problem.
- The authors performed experiments across three types of datasets and four different models.
- The idea of evaluating multi-reasoning with a multi-hop knowlege graph is interesting.

### Weaknesses
 - Reasoning only requires the model to generate sequences of thoughts with itself, which means we can optimize these thoughts online rather than offline [1,2,3].
- The ability to evaluate a model of multi-step reasoning based only on a multi-hop knowledge graph is very limiting.
- The paper lacks ablation experiments to clearly explain the performance gains of OCEAN, which come from the objective in equation 3 and training on GPT-4's verbalized structured chain of thoughts.

### Questions
- How does the proposed IPS approach compare to simply doing the direct method (DM) for evaluation?
- What is the offline policy evaluation performance without performing updated according to equation 4? How does the offline policy evlauation change as you update the policy using equation 4?
- How does SFT + normal COT perform?
- How are you computing the value function estimate for SFT and the base model?
- Did you start training OCEAN with the SFT model?
- Did you also train SFT on the reasoning steps, or just on the questions and answers? If it was only on questions and answers, how does it perform when trained on reasoning steps similar to OCEAN?
- How does the index k depend on the question q and answer y for the policy gradient?
- How does SFT + normal CoT perform?
- What does context mean in w/ctx and w/o ctx?

[1] Rewarding Progress: Scaling Automated Process
Verifiers for LLM Reasoning by Setlur et al.
[2] Quiet-STaR: Language Models Can Teach Themselves to
Think Before Speaking by Zelikman et al.
[3] V-STaR: Training Verifiers for Self-Taught Reasoners by Hosseini et al.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel approach for aligning LLMs with chain-of-thought reasoning by leveraging offline knowledge graph data. Specifically, a knowledge graph preference policy is first trained using reinforcement learning on question-answering data derived from verbalized exploration trajectories within the offline knowledge graph. This policy, which serves as a proxy for the knowledge graph’s preferences, is then used to fine-tune the target LLM policy through a novel KG-IPS estimator that assesses the difference between the proxy knowledge graph preference policy and the target policy. Extensive experiments are conducted to evaluate both the chain-of-thought reasoning alignment performance and the impact of this alignment on the base LLM's general capabilities.

### Strengths
- The research goal of aligning LLMs with chain-of-thought reasoning is both interesting and important.
- The approach of using graphs as supplementary information to align LLMs with chain-of-thought reasoning is a promising avenue for exploration.
- The paper is clearly presented and easy to follow, making it a pleasure to read overall.
- The experiments are thorough and extensive.

### Weaknesses
Several key concepts and notations in the task formulation and methodology are not clearly defined, and certain details about the dataset are missing. Please refer to the questions for further details.

# Task formulation
- Line 156, what is the "surrounding context $c_t  \backslash a_t$"? Could you please elaborate on why $a_t$ "is a sub-sequence in the reasoning path $a_t \in c_t$,"? Providing some intuitive examples may help improve understanding. The definition of $c_t$ as the surrounding context excluding $a_t$ is unclear, especially given that $a_t$ is described as a subsequence within the reasoning path. This creates a circular definition that needs clarification. It's not clear how the model distinguishes between the reasoning path and the surrounding context, and how these are separated during the training process. A concrete example illustrating how $c_t$ and $a_t$ are extracted from a given text would be beneficial.
- In line 169, "the current edge $e_{t-1}$" implies that $e$ represents edges in graphs. However, in line 172, "the entity $e_{t-1}$" implies that it represents entities. Could you please clarify the meaning of the notation $e$? The notation $e$ also appears in Equation 3. Please see related questions below. The inconsistent use of $e$ to denote both edges and entities is confusing and needs to be addressed. The paper needs to clearly define whether $e$ represents an edge, an entity, or both, and maintain consistency throughout the paper. This ambiguity makes it difficult to understand the methodology and the equations.

# Methodology
- As most of readers would be not familiar with the Wikidata5M dataset, could you please present some cases of sampled trajectories $h$ from the knowledge graph $\mathcal{G}$? In addition, some cases of the verbalizing transformation from $h$ to $c$ using GPT-4 would also be very interesting to see. Without concrete examples of the sampled trajectories and their verbalizations, it is difficult to assess the quality of the data used for training. The paper should provide examples of the raw graph trajectories and the corresponding verbalized text. This would help the reader understand the nature of the data and the potential biases it might introduce.
- What are the transition dynamics in the exploration of the knowledge graph? The paper lacks details on how the knowledge graph is explored. It is unclear how the trajectories are sampled, what the sampling strategy is, and what the criteria are for selecting the next node in the graph. This information is crucial for understanding the data generation process and the potential biases it might introduce.
- Could you please provide more detailed information about the resulting offline dataset used for knowledge graph preference modeling? The paper should provide more details on the size and composition of the offline dataset, including the distribution of trajectory lengths, the number of entities and relations, and any other relevant statistics. This information is essential for understanding the scale and diversity of the data used for training.
- Could you please clarify whether the training of the knowledge graph preference policy is conducted in an online or offline manner? The paper does not clearly state whether the knowledge graph preference policy is trained online or offline. This is a crucial detail that affects the reproducibility and the computational cost of the method. The paper needs to explicitly state the training paradigm used.
- About Equation 3:
  - $e \in c_t$ implies that $e$ is a sub-set of $c_t$. Could you please explain a little bit on the relation between these three notations: $e$, $a_t$, and $c_t$? Could we simply understand that $e$ represents a sequence of tokens? The relationship between $e$, $a_t$, and $c_t$ is not clear. The paper needs to clarify whether $e$ represents a single token, a sequence of tokens, or something else. The notation $e \in c_t$ suggests that $e$ is a subset of $c_t$, which is confusing given the other definitions. A clear explanation of these notations is needed to understand the equation.
  - $c_t^{(i)}$ is outside of the summation $\sum\limits_{t=1}^{T_i}$. The subscript $t$ for this variable is unassigned. The placement of $c_t^{(i)}$ outside the summation is incorrect and needs to be fixed. The subscript $t$ is missing, which makes the equation ambiguous.
  - Should $e \in c_t$ be $e \in c_t^{(i)}$? The notation $e \in c_t$ is inconsistent with the use of $c_t^{(i)}$ in the equation. It is unclear whether $e$ should be a subset of $c_t$ or $c_t^{(i)}$. This inconsistency needs to be addressed.
- Line 221, is it correct that the reward function is defined as $r_t^{(i)} = \log \pi_0(e|s_t^{(i)})$ for the training of the target policy? If so, why we consider the reward in the token level, instead of the reward in the reasoning step level? Utilizing the reward function at the token level conflicts with the formulation in line 159, where $r_t = r(s_t, c_t)$. The use of token-level rewards for the target policy training is not well-justified, especially given the formulation in line 159 which suggests a step-level reward. The paper needs to explain why a token-level reward is used and how it aligns with the overall objective of aligning LLMs with chain-of-thought reasoning. The conflict between the token-level reward and the step-level formulation needs to be addressed.

# Minor suggestions
- Some background knowledge about the conventional inverse propensity scores (IPS) method could be interesting for readers.

### Questions
# Task formulation
- Line 156, what is the "surrounding context $c_t  \backslash a_t$"? Could you please elaborate on why $a_t$ "is a sub-sequence in the reasoning path $a_t \in c_t$,"? Providing some intuitive examples may help improve understanding.
- In line 169, "the current edge $e_{t-1}$" implies that $e$ represents edges in graphs. However, in line 172, "the entity $e_{t-1}$" implies that it represents entities. Could you please clarify the meaning of the notation $e$? The notation $e$ also appears in Equation 3. Please see related questions below.

# Methodology
- As most of readers would be not familiar with the Wikidata5M dataset, could you please present some cases of sampled trajectories $h$ from the knowledge graph $\mathcal{G}$? In addition, some cases of the verbalizing transformation from $h$ to $c$ using GPT-4 would also be very interesting to see.
- What are the transition dynamics in the exploration of the knowledge graph?
- Could you please provide more detailed information about the resulting offline dataset used for knowledge graph preference modeling?
- Could you please clarify whether the training of the knowledge graph preference policy is conducted in an online or offline manner?
- About Equation 3:
  - $e \in c_t$ implies that $e$ is a sub-set of $c_t$. Could you please explain a little bit on the relation between these three notations: $e$, $a_t$, and $c_t$? Could we simply understand that $e$ represents a sequence of tokens?
  - $c_t^{(i)}$ is outside of the summation $\sum\limits_{t=1}^{T_i}$. The subscript $t$ for this variable is unassigned. 
  - Should $e \in c_t$ be $e \in c_t^{(i)}$?
- Line 221, is it correct that the reward function is defined as $r_t^{(i)} = \log \pi_0(e|s_t^{(i)})$ for the training of the target policy? If so, why we consider the reward in the token level, instead of the reward in the reasoning step level? Utilizing the reward function at the token level conflicts with the formulation in line 159, where $r_t = r(s_t, c_t)$. 

# Minor suggestions
- Some background knowledge about the conventional inverse propensity scores (IPS) method could be interesting for readers.

### Soundness
3

### Presentation
3

### Contribution
3
