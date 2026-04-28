# From Reward Shaping to Q-Shaping: Achieving Unbiased Learning with LLM-Guided Knowledge

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Q-shaping is an extension of Q-value initialization and serves as an alternative to reward shaping for incorporating domain knowledge to accelerate agent training, thereby improving sample efficiency by directly shaping Q-values. This approach is both general and robust across diverse tasks, allowing for immediate impact assessment while guaranteeing optimality. We evaluated Q-shaping across 20 different environments using a large language model (LLM) as the heuristic provider. The results demonstrate that Q-shaping significantly enhances sample efficiency, achieving a \textbf{16.87\%} improvement over the best baseline in each environment and a \textbf{253.80\%} improvement compared to LLM-based reward shaping methods. These findings establish Q-shaping as a superior and unbiased alternative to conventional reward shaping in reinforcement learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel framework called "Q-shaping," which enhances Q-value initialization by integrating domain knowledge to accelerate training in reinforcement learning (RL). Unlike traditional reward shaping methods, Q-shaping modifies Q-values directly, thereby improving sample efficiency without sacrificing the agent's optimality upon convergence. The experimental results indicate significant performance improvements.

### Strengths
1. **Innovative Approach:** Q-shaping presents a fresh perspective on incorporating domain knowledge into RL, overcoming the limitations associated with reward shaping.
2. **Empirical Results:** The paper includes comprehensive experimental evaluations demonstrating Q-shaping's effectiveness, with a 16.87% improvement in sample efficiency over the best baseline and a remarkable 253.80% enhancement compared to LLM-based reward shaping methods.
3. **LLM Utilization:** The paper effectively harnesses large language models to guide agent exploration, revealing new potentials for LLMs in RL applications.

### Weaknesses
The current version lacks sufficient proof of completeness in both theoretical and experimental aspects. If the authors can convincingly address these issues, I would be open to reevaluating my score.

1. **Comparison to Existing Works:** It’s important to clarify why the challenges of reward shaping cannot be addressed by recent LLM-based methods (e.g., Eureka, text2reward). How does your work differ from these studies? It appears your approach utilizes LLMs to design regularization for RL.
   
2. **Proof of Theorem 1:** The proof seems unconventional; while you provide an update formula for the \(\hat{Q}\) iteration, you immediately reference the Bellman optimal operator to support your theorem. Early works have established the convergence of the Bellman operator, so how can you demonstrate that your update formula aligns with it? This appears to assume the conclusion as a basis for your argument.
   
3. **Clarification on Theorem 2:** Theorem 2 establishes a lower bound rather than an upper bound. What is the convergence sample complexity relative to other works? Is your bound more favorable than existing results, and do other studies not provide established bounds?
   
4. **Relation to Regularization Techniques:** A deeper explanation of how your work relates to reinforcement learning methods employing regularization techniques would be beneficial. The core of your approach seems to hinge on introducing LLMs for regularization in RL.
   
5. **Experimental Settings:** The experimental setup raises some questions. You utilize GPT-4o as the LLM and TD3 as the RL backbone in your LLM-TD3 method. Which LLM do Eureka and text2reward utilize (notably, Eureka uses GPT-4 and GPT-3.5, while text2reward uses GPT-4)? Is GPT-4o also used for these works, and do they employ TD3 as the RL backbone?

**Minor Issues:**
1. In lines 32-36, the literature review on current RL works aimed at enhancing training efficiency lacks citations, which detracts from its objectivity.
2. The origin of the concept of NPBRS (non-potential based reward shaping) in line 53 is unclear and needs clarification.
3. A few LLM-assisted RL studies have focused on Q-function or value function design (e.g., “How Can LLM Guide RL? A Value-Based Approach”). An analysis of these works should be included in the related works section.
4. Figures 4 and 6 do not specify the units for steps (presumably in millions).
5. The prompt example in the Appendix is too brief. A more comprehensive example, including the output Q function and policy function, would greatly enhance reader understanding.

### Questions
1. **Comparison to Existing Works:** It’s important to clarify why the challenges of reward shaping cannot be addressed by recent LLM-based methods (e.g., Eureka, text2reward). How does your work differ from these studies? It appears your approach utilizes LLMs to design regularization for RL.
   
2. **Proof of Theorem 1:** The proof seems unconventional; while you provide an update formula for the \(\hat{Q}\) iteration, you immediately reference the Bellman optimal operator to support your theorem. Early works have established the convergence of the Bellman operator, so how can you demonstrate that your update formula aligns with it? This appears to assume the conclusion as a basis for your argument.
   
3. **Clarification on Theorem 2:** Theorem 2 establishes a lower bound rather than an upper bound. What is the convergence sample complexity relative to other works? Is your bound more favorable than existing results, and do other studies not provide established bounds?
   
4. **Relation to Regularization Techniques:** A deeper explanation of how your work relates to reinforcement learning methods employing regularization techniques would be beneficial. The core of your approach seems to hinge on introducing LLMs for regularization in RL.
   
5. **Experimental Settings:** The experimental setup raises some questions. You utilize GPT-4o as the LLM and TD3 as the RL backbone in your LLM-TD3 method. Which LLM do Eureka and text2reward utilize (notably, Eureka uses GPT-4 and GPT-3.5, while text2reward uses GPT-4)? Is GPT-4o also used for these works, and do they employ TD3 as the RL backbone?

**Minor Issues:**
1. In lines 32-36, the literature review on current RL works aimed at enhancing training efficiency lacks citations, which detracts from its objectivity.
2. The origin of the concept of NPBRS (non-potential based reward shaping) in line 53 is unclear and needs clarification.
3. A few LLM-assisted RL studies have focused on Q-function or value function design (e.g., “How Can LLM Guide RL? A Value-Based Approach”). An analysis of these works should be included in the related works section.
4. Figures 4 and 6 do not specify the units for steps (presumably in millions).
5. The prompt example in the Appendix is too brief. A more comprehensive example, including the output Q function and policy function, would greatly enhance reader understanding.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents Q-shaping, a framework to accelerate training of reinforcement learning agents by using LLMs to produce domain-knowledge based heuristic functions for initializing the Q-function and policy. Specifically, LLMs produce code to categorize good and bad state-action pairs in the environment. Before the start of training, these pairs are used to update the Q-network and policy, thus leading to better network initializations. Results across 20 environments show that Q-shaping can significantly improve sample efficiency and outperform LLM-guided reward-shaping methods.

### Strengths
1. The method is intuitive and simple to understand. The domain knowledge of LLMs is used to find good initializations of the Q-function. This can be generally useful for multiple RL tasks if structured information can be effectively elicited from LLMs.
2. The paper has an appropriate number of citations and properly details existing work in the related work section. 
3. Although multiple works have considered using the domain knowledge of LLMs for improving RL, this work introduces another novel way to harness that expertise.

### Weaknesses
1) **Writing**: The overall writing is lacking and can be significantly improved. The style of writing is currently informal and often lacking important experimental details. For example, the evaluation criteria are not properly explained, some experimental details are not clear. The overall flow of the paper is also not smooth.
2) **Result Discussion**: The discussion of the results is very limited. The ablations conducted are only discussed superficially. For an empirical paper, only 1 page dedicated to discussion of results is too less. I personally feel that more discussion is needed in the experiments section, and some of the theory and notation introduced is not critical to the paper and can be deferred to the appendix.
3) **Significance of Results**: In 6-7 out of the 20 tasks, the presented method is worse than the best-performing baseline. While there are multiple potential causes of this (base RL algorithm, bad LLM outputs, randomness if only 1 seed is uses, etc), it is difficult to validate the generalization capability of the method.
4) **High-Performance Agent Selection**: It is unclear if the high-performance agent selection is applied to all baselines or only to the proposed Q-shaping method. If it is only applied to Q-shaping, this introduces a significant bias in the results as it essentially reports the average performance of the best 10 agents for Q-shaping, while reporting the overall average for the baselines. Furthermore, the 150K additional training steps (10 agents * 15K steps) taken during the selection phase are not accounted for in the sample efficiency results, making the comparison unfair.
5) **Environment Description Details**: The paper lacks details on the 'environment description' provided to the LLMs when prompting them to classify good/bad states. This information is crucial to understand the amount of domain knowledge being provided to the LLMs and to assess how difficult it would be for a human to write the same function. Examples of the good/bad state functions written by the LLMs are also missing.
6) **Seeds**: The paper does not specify the number of runs used to generate the learning curves. It is important to know how many runs were performed to understand the confidence intervals around the curves and the statistical significance of the results. The term 'seed' refers to both the environment and the RL algorithm initialization.
7) **Evaluation of LLM Correctness**: The paper claims that some LLMs achieve 100% correctness in assigning Q-values, but the method for evaluating this correctness is not clearly explained. It is unclear how the correctness of the assigned Q-values is judged, and the paper does not provide sufficient detail on this evaluation process.

### Questions
1. What are the number of seeds used? The curves oscillate a lot and it is difficult to draw conclusions from many of the plots. 

2. I am not convinced by the implementation of the Eureka and text2reward baselines. In 3 out of the 4 plots, both these baselines stay completely flat and do not improve at all. This is strange as Eureka was shown to perform well on a variety of robotic tasks. The tasks selected in this paper do not seem very different, and I am curious why these baselines are so bad. Setting the evolution round to 1 might be partially responsible for this but makes it unfair for the baseline. 

3. What is the state for the environments considered? There is no information provided on this and I do not see how this method will generalize when the states are images. Similarly, when doing RL on real robots, then clean environment code as assumed by this work will not be available. It will be useful to get an idea about the assumptions that this work makes.

4. It will be helpful add the individual impacts of Q-shaping and policy-shaping in the ablation study on different training phases. Currently, it is unclear what the contributions of these two techniques are to the final performance of the method. 

5. I do not understand the significance of the sample efficiency results. Sample efficiency improves by an average of 17% compared to baselines. However, the presented framework also has a high-performance selection phase which is not a part of the baselines. As multiple agents are rolled out for a significant number of timesteps, a fairer comparison would be to add these timesteps into the sample efficiency calculations. 

6. How are the heuristic functions output by LLMs evaluated? For example, one of the evaluation criteria is correctness of assigned Q-values. How is this actually measured?

7. How many times is a LLM prompted per task? If it prompted multiple times, how are they filtered? 

8. I think it is also important to release the entire prompts that are used for the LLMs as there could be a lot of domain knowledge provided in the task descriptions themselves. As the environment task descriptions are currently not provided in the paper, it is difficult to understand the contribution of the LLM.

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
3

### Summary
The authors proposed a method called Q-shaping to enhance the sample efficiency of reinforcement learning algorithms. The main idea is to prompt a LLM to generate samples of good and bad state-action pairs and heuristic Q value estimates. These samples are used to train the initial Q function before turning to the standard RL pipeline. Experiments were conducted on a variety of continuous control environments showing significant improvement in sample efficiency in some environments.

### Strengths
The idea is original to my knowledge and the experiments are well executed.

### Weaknesses
 * The presentation of the idea is somewhat long winded and the notations are somewhat inconsistent as I point out in the questions.
* It is not clear how the method is fundamentally different from Q value initialization.
* Line 155, what does the $A^{\pi}$ symbol represent? Is it the policy improvement operator? I couldn't find any explanation in the text.
* Line 181, are the authors missing a $(1 - \alpha)$ coefficient and brackets in the Q function update rule? The equation seems inconsistent with the update equation on line 744 in appendix B.2.
* I am not too sure how Theorem 1 actually shows the contraction property of the shaped Q iteration and how it differs from the contraction property of the regular Bellman operator. Line 757 in the proof section appears to say that the optimality of the shaped Q iteration is only guaranteed if the addition of heuristic values is stopped. 
* In eq 1, that is $D_{g}$? Is it $D_{LLM} = \{G_{LLM}, B_{LLM} \}$?

### Questions
* Line 155, what does the $A^{\pi}$ symbol represent? Is it the policy improvement operator? I couldn't find any explanation in the text.
* Line 181, are the authors missing a $(1 - \alpha)$ coefficient and brackets in the Q function update rule? The equation seems inconsistent with the update equation on line 744 in appendix B.2.
* I am not too sure how Theorem 1 actually shows the contraction property of the shaped Q iteration and how it differs from the contraction property of the regular Bellman operator. Line 757 in the proof section appears to say that the optimality of the shaped Q iteration is only guaranteed if the addition of heuristic values is stopped. 
* In eq 1, that is $D_{g}$? Is it $D_{LLM} = \{G_{LLM}, B_{LLM} \}$?

### Soundness
3

### Presentation
3

### Contribution
2
