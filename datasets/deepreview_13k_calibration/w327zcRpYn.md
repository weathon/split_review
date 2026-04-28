# SUBER: An RL Environment with Simulated Human Behavior for Recommender Systems

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3

## Abstract
Reinforcement learning (RL) has gained popularity in the realm of recommender systems due to its ability to optimize long-term rewards and guide users in discovering relevant content.
    However, the successful implementation of RL in recommender systems is challenging because of several factors, including the limited availability of online data for training on-policy methods. This scarcity requires expensive human interaction for online model training. Furthermore, the development of effective evaluation frameworks that accurately reflect the quality of models remains a fundamental challenge in recommender systems. To address these challenges, we propose a comprehensive framework for synthetic environments that simulate human behavior by harnessing the capabilities of large language models (LLMs). We complement our framework with in-depth ablation studies and demonstrate its effectiveness with experiments on movie and book recommendations. Using LLMs as synthetic users, this work introduces a modular and novel framework to train RL-based recommender systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors present a promising solution to the challenge of training recommender systems when real user interactions are not available. They propose SUBER, a novel Reinforcement Learning (RL) simulated environment tailored for recommender system training, which leverages recent advancements in Large Language Models (LLMs) to simulate human behavior within the training setting. A series of ablation studies and experiments demonstrate the effectiveness of their approach. This research represents a significant step towards creating more realistic and practical training environments for recommender systems, even in the absence of direct user interactions.

### Strengths
1.	The concept of employing Large Language Models (LLMs) to mimic synthetic users is intriguing. SUBER offers a multifaceted approach, generating synthetic data while harnessing the potential of LLMs to accurately emulate the behavior of users with undisclosed patterns.
2.	The authors meticulously conduct comprehensive ablation studies to dissect the various components of LLMs, demonstrating the scalability and versatility of SUBER in the process.
3.	The article is impeccably articulated, presenting its ideas with clarity and maintaining a logical flow throughout.

### Weaknesses
1.	How do the authors assess the accuracy of their simulated environment? The paper primarily showcases the training curve of the RL model within this environment but lacks a comparative analysis against other environment simulation methods. The absence of online experiments further challenges the validity of the simulated environment. The paper does not provide a clear methodology for validating the simulated user behavior against real-world user interactions, making it difficult to ascertain the fidelity of the simulation.

2.	The authors should expound on their rationale for using LLMs to simulate users, clarify why this approach is effective, and outline the advantages it offers over alternative environment simulation methods. The paper lacks a detailed discussion on the specific capabilities of LLMs that make them suitable for this task, such as their ability to capture complex user preferences or adapt to changing interaction patterns. A more thorough comparison with other simulation techniques, highlighting the limitations of those methods and the benefits of using LLMs, is needed.

3.	The authors claim that this dynamic environment can serve as a model evaluation tool for recommender systems, but it lacks empirical evidence to support this claim. A clear methodology for measuring the accuracy of the proposed evaluation method is needed. The paper needs to demonstrate how the proposed environment can effectively differentiate between various recommender system models and provide a reliable ranking of their performance.

4.	The absence of t-tests or error bars in the results section raises concerns about the reliability and reproducibility of the experimental findings. The lack of statistical significance testing makes it difficult to draw firm conclusions from the experimental results.

5.	The paper mentions the limitation of context length for providing a list of all possible items to an LLM. Further details are required regarding how the author addressed this particular issue. The paper needs to elaborate on the specific techniques used to handle the context length limitation, such as item retrieval or summarization methods, and discuss their impact on the simulation's accuracy.

### Questions
1.	I suggest the authors evaluate the simulated environment from more aspects. To establish the accuracy of the simulated environment, consider conducting comparative experiments. Compare the performance of your proposed environment with existing methods for simulating user interactions. Additionally, performing online experiments where applicable, could help validate the authenticity of your simulated environment.

2.	I suggest the authors provide a more in-depth explanation of why LLMs are chosen to simulate users. Elaborate on the effectiveness of this approach by highlighting its advantages over alternative simulation methods. This could include discussing how LLMs can capture complex user behavior or adapt to changing patterns more effectively.

3.	To substantiate the claim that your dynamic environment serves as a model evaluation tool, conduct experiments that demonstrate its utility in evaluating recommender systems. Present a clear experimental setup and results that support this assertion.

4.	Enhance the reliability and reproducibility of your experimental results by including t-tests or error bars. 

5.	Explain in detail how you addressed the limitation of limited context length. What techniques or strategies did you employ to mitigate this constraint when using LLMs in your environment?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a framework for training and evaluating RL-based recommender systems, which uses large language models (LLMs) to simulate human behavior and rate recommended items.

### Strengths
+ The paper proposes a user simulation framework based on large language models, which can alleviate the problems of data scarcity and model evaluation for reinforcement learning based recommender system.
+ The paper designs a flexible and extensible environment based on reinforcement learning principles, which can interact with different LLMs and recommendation strategies.
+ The paper provides a modular framework and open-source code, which is a valuable tool for the recommender system domain. It helps researchers and developers to train and evaluate reinforcement learning based recommender systems without real user interactions.

### Weaknesses
 - The manuscript could benefit from more robust experimental support. The absence of comparisons with other simulation algorithms may impact the persuasiveness of the paper.

- The paper appears to lack some key experiments that validate the effectiveness and advantages of RL training in the proposed environment. While the paper presents ablation studies on different components of the environment, it does not compare the RL-based recommender system with other baselines or state-of-the-art methods on real user data or benchmark datasets. It would be advantageous if the authors could include such experimental validations in future research.

- The use of LLMs to generate synthetic users is an innovative approach that leverages the powerful capabilities of LLMs to simulate human behavior and preferences. However, the paper does not evaluate the quality and diversity of the user generation, nor does it compare it with real user data. This could potentially lead to biases and inaccuracies in the simulation. It would be beneficial if the authors could delve deeper into this aspect in future research.

- The related work section of the paper seems too general and lacks precision. It does not adequately highlight the differences and connections between their work and existing research. It would be advantageous if the authors could elaborate more on the relationship and uniqueness of their work in relation to existing research, to enhance the depth and breadth of the paper.

### Questions
1.	Can the author provide a distribution chart for scores predicted by LLMs and actual scores? The numbers reported in the table do not provide an intuitive image. On the other hand, it is more important to focus not on the overall score distribution, but on the differences in scoring for each item (it is possible for the overall score distribution to be the same, but with significant differences in individual item scores).
2.	What is the difference between the last two rows in Table 1? Is it a type error? 
3.	Comparing rows 3-8 in Table 1 with the 9th row, it can be observed that the model is very good at distinguishing between High and Low Ratings on a scale of 0-9. However, when the score scale changes to 1-10, there is a significant decrease in performance. Does this indicate that the model can only identify very poor items? (0 score)
4.	I suggest the author showcases the performance of several traditional models and conventional RL methods, under your reward metric (Figure .4a)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposed SUBER, a framework designed to address common challenges in RL-based recommender systems, such as issues related to data availability and the design of reward functions. The paper conducted several ablation studies on movie and book recommendations to demonstrate the effectiveness of the method and examine the effect of each component in the framework.

### Strengths
-	The motivation of this paper is clear and the challenges it aims to address are significant to the RL-based recommender system.
-	The method is presented clearly. Each component is well explained, and the flow of the entire framework is well presented in the figure.
-	The paper conducted a series of ablation studies to scrutinize the effect of different components within the framework.

### Weaknesses
 - The proposed  framework is to tackle key challenges in RL4Rec, such as data accessibility, the uncertainty of the user model, and the assessment of models. However, the originality of this research is ambiguous to me. It appears to predominantly integrate components of Reinforcement Learning (RL) with Large Language Models (LLMs). Furthermore, due to the absence of a thorough comparison with existing RL simulators and state-of-the-art techniques including RL4Rec and LLM-integrated RecSys, it's challenging to position the precise significance of the contributions claimed in this study.
- The paper has only made comparisons between different settings of SUBER on the metrics proposed in this paper. The comparisons with other methods on some commonly used metrics such as MAP/R^2/Personalization are missing. These comparisons would be essential to understand the benefits of using this method.
- The prompts used in the pre-processing module and the user description generation step require hand-crafted templates, which may limit the generalizability of the method in other scenarios.
- This method may require more computational resources than other methods due to the usage of LLM. More analysis and evaluations should be done. 
- The authors failed to monitor significant existing literature on RL4Rec, including various methods and simulators, as well as RecSys integrated with LLMs. This oversight renders the paper's scope and credibility questionable.

### Questions
-	The paper claims that it addresses the challenge of model evaluation, is it referring to the evaluation metrics mentioned in Section 4.2 and Table 1-2? How do these metrics outperform the existing evaluation methods?
-	As addressed in the weakness section, I think the comparisons between this method and other methods on metrics such as MAP/R^2/Personalization are essential to verify the effectiveness of the method. Could the authors provide these results?
-	I’m not sure about the purpose of generating the user descriptions. The paper mentioned that the Age / Job / Hobbies of the users are randomly sampled from external distributions, how does this random information affect the outcome? And what’s the motivation for doing so? An ablation study to compare the results with/without this information would be helpful.
-	It’s known that different prompt methods could affect the response of LLMs. How does the prompt template affect the outcomes in this framework? I suggest the authors try several different prompt templates in the pre-processing module and the user description generation step, then report the range of the results.
-	In Fig 4a, I observed a significant performance drop somewhere between 1.6M - 1.7M steps, why does this happen? It seems not due to the randomness because this pattern is consistent across all embedding dimensions. Or more generally, I found the pattern of these three lines seems to be extremely similar, I’m surprised by this because I suppose these are three independent experiments with different dimension settings. Is there any particular reason for the similarity between these three lines?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper propose SUBER, a RL environment that applies LLM to simulate user behaviors. SUBER consists of several components including memory, preprocessing,  postprocessing, and LLM modules. The user history is sent to the RL module, and it returns an item. Both user history and the recommended item are processed as a prompt, then the LLM outputs the simulated user rating over the item. SUBER is built on two public datasets. The paper does experiments to validate its effectiveness. Finally, the paper shows that how A2C is trained in this environment.

### Strengths
1.Using LLM to simulate user behaviors is interesting.
2.The paper is easy to follow.
3.The paper does detailed ablation study.

### Weaknesses
1.The paper does not discuss the limitation of SUBER. In my opinion, I think the input feature is quite simple, and miss numerical and sequential informations. Specifically, the state representation appears to be limited to the last rating a user provided, which discards potentially valuable information about the user's rating history, such as trends in their preferences or the time elapsed between ratings. This simplification may hinder the model's ability to capture complex user behaviors.
2.The paper does not compare SUBER and other RL-based simulators, such as VirtualTaobao, RecoGym. Thus it is quite hard to evaluate the significance of SUBER in the RL4RS area. Without a comparative analysis against existing simulation environments, it's difficult to ascertain the novelty and practical advantages of SUBER. The paper needs to demonstrate how SUBER offers unique benefits or addresses limitations of current simulators.
3.The paper does not cite two recent papers about RL4RS simulators, "RL4RS: A Real-World Dataset for Reinforcement Learning based Recommender System" and KuaiSim: A Comprehensive Simulator for Recommender Systems.
4.As an RL environment, I would suggest that the author evaluate more RL algorithms besides A2C, such as SA2C(Supervised Advantage Actor-Critic for Recommender Systems), HAC(Exploration and Regularization of the Latent Action Space in Recommendation) and off-policy top-k(Top-K Off-Policy Correction for a REINFORCE Recommender System). The lack of evaluation with diverse RL algorithms limits the understanding of the environment's characteristics and its suitability for different types of RL methods. The authors should demonstrate the environment's versatility by testing it with a range of algorithms, including those designed for specific challenges in recommendation systems.

### Questions
See the above question.

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor
