# VerifierQ: Enhancing LLM Test Time Compute with Q-Learning-based Verifiers

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 8, 5, 3

## Abstract
Recent advancements in test time compute, particularly through the use of verifier models, have significantly enhanced the reasoning capabilities of Large Language Models (LLMs). This generator-verifier approach closely resembles the actor-critic framework in reinforcement learning (RL). However, current verifier models in LLMs often rely on supervised fine-tuning without temporal difference learning such as Q-learning. This paper introduces VerifierQ, a novel approach that integrates Offline Q-learning into LLM verifier models. We address three key challenges in applying Q-learning to LLMs: (1) handling utterance-level Markov Decision Processes (MDPs), (2) managing large action spaces, and (3) mitigating overestimation bias. VerifierQ introduces a modified Bellman update for bounded Q-values, incorporates Implicit Q-learning (IQL) for efficient action space management, and integrates a novel Conservative Q-learning (CQL) formulation for balanced Q-value estimation. Our method enables parallel Q-value computation and improving training efficiency. While recent work has explored RL techniques like MCTS for generators, VerifierQ is among the first to investigate the verifier (critic) aspect in LLMs through Q-learning. This integration of RL principles into verifier models complements existing advancements in generator techniques, potentially enabling more robust and adaptive reasoning in LLMs. Experimental results on mathematical reasoning tasks demonstrate VerifierQ's superior performance compared to traditional supervised fine-tuning approaches, with improvements in efficiency, accuracy and robustness.  By enhancing the synergy between generation and evaluation capabilities, VerifierQ contributes to the ongoing evolution of AI systems in addressing complex cognitive tasks across various domains.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focused on integrating reinforcement learning techniques with language models to enhance multi-step reasoning capabilities. To do that, the approach of VerifierQ was proposed by formulating the problem into a utterance-level MDP and solving it with IQL and CQL. Finally, experiments were conducted on two datasets of GSM8K and MATH, comparing VerifierQ with PRM and Majority Voting.

### Strengths
- This is a timely important topic that the paper aims to leverage verifier models with reinforcement learning to enhance the reasoning capabilities of large language models. It's interesting to pay attention to the verifier component instead of the generator component.
- Novelty: although this work is built from the previous work on multi-step reasoning with generator-verifier, it's novel to formulate the problem into a utterance level MDP, from the perspective of verifier models, and solve it with reinforcement learning techniques.

### Weaknesses
 - The presentation of the paper should be improved. For example, it can be more helpful if Figure 1 could include IQL and CQL and show how different modules/components interacct with each other and what's the forward pass and backward pass. The paper mentioned that the utterance level RL allows better handling of long-term horizons, so, what's the MDP definition in the utterance level? what's the difference between their utterance level and token level in this paper?
- The current results are insufficient to support the paper's claim. For example, I didn't find the results used for showing the computational efficiency of VerifierQ and others. In Figure 4, particularly on GSM8K dataset, VerifierQ performed worse than PRM when the number solutions per problem was lass then 2^5, and it became the best when the number was larger than 2^5. However, the improvement looks very marginal. On MATH dataset, VerifierQ performed worse than Majority. Eventhough, the improvement of VerifierQ over PRM looks still very marginal. The paper mentioned that this might be because of the small model size of Majority Vote. So, what is the model size for the other methods? Why the model size matters on this MATH dataset? It's not clear to me. For overestimation analysis, the paper said "Figure 6 reveals that PRM generally assigns higher Q-values to incorrect tokens, while VerifierQ assigns lower values", however, it feels to me that CQL in VerifierQ assigned low Q-values to all tokens where incorrect tokens got more penalization (lower Q-values) than the correct one. The ablation study should include the comparison of VerifierQ w/ CQL and VerifierQ wo/ CQL, in order to further show the mitigation in addressing overestimation. Overall, the conclusion is vauge.

### Questions
- See the comments in the weaknesses.
- How to get the "two tokens + and -" to represent correct and incorrect states, and the other "tag token indicating estimation"?
- In Equation 2, what's the difference between R(s,a) and r? How does equation 2 bound the Q-values within the range of (0,1)?
- What's the data for plotting Figure 3?
- What's the size of the action space for each dataset? Does the solutions per problem represent the action space for RL?
- "test accuracy %" should not include "%", for example, the numbers reported in Figure 4 should be the accuracy number in decimal instead of in percentage, right?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces VerifierQ, a novel method that integrates Offline Q-learning into verifier models for LLMs, significantly enhancing their multi-step reasoning capabilities. It addresses key challenges such as handling utterance-level MDPs, managing large action spaces, and mitigating overestimation bias through a modified Bellman update and a tailored formulation of Conservative Q-learning. Experimental results demonstrate that VerifierQ outperforms traditional supervised fine-tuning approaches in mathematical reasoning tasks, suggesting a promising direction for improving test-time compute in LLMs.

### Strengths
1- The paper is well-structured and easy to follow.

2-  The paper cleverly handles multiple challenges (utterance level RL - large action space and overestimatrion ) and proposes a novel loss function formulation that integrates both IQL and CQL, allowing for a more optimistic Q-values estimation within the CQL framework. 

3- Comprehensive evaluation and ablation study.

### Weaknesses
Overall, I think this is a good paper but I do have the below comments:

1- Clarification on Q-learning Update Bounds: 
- In page 4, Section 5.1, it is not clear to me how multiplying the q-learning update by 1/2 bounds the Q-value between (0,1) as the authors claim. The explanation lacks sufficient detail regarding the interplay between the reward, discount factor, and the Q-value itself within the Bellman update. Specifically, it's unclear how the reward, which is bounded between 0 and 1, and the discounted future Q-value, also bounded between 0 and 1, interact to ensure the updated Q-value remains within the claimed (0,1) range after being multiplied by 1/2. A more rigorous mathematical justification, perhaps showing the derivation of the upper and lower bounds, is needed to fully understand this claim. The current explanation is too high-level and does not provide a clear understanding of the bounding mechanism.

2- Clarity of the figures: 
- The figures throughout the paper are difficult to read due to the small font size.  Please increase the font size. Additionally, Figure 2 A) could benefit from more context or annotations to aid in comprehension. The current figure lacks sufficient labels and explanations of the different components, making it hard to understand the flow of information and the role of each element. For example, the different loss components are not clearly identified, and the connections between them are not well-explained. 

- Lastly, in Figures 4 and 5,  the y-axis is labeled 'Test Accuracy %', but the values (e.g., 0.53, 0.54) are presented as decimal fractions rather than percentages. The authors should clarify whether this is a typo or if the values are indeed less than 1.

### Questions
Please see the questions above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
VerifierQ introduces a new approach for enhancing verifier models in Large Language Models (LLMs) through Offline Q-learning, focusing on utterance-level tasks, featuring three key contributions:
- Adaptation of Q-learning to work on utterance-level for Language Modeling
- Handling Large Action Space with Implicit Q-Learning (IQL): To handle large action spaces in LLMs VerifierQ integrates Implicit Q-Learning (IQL), which approximates Q-values without explicit maximization, making Q-value estimation feasible even with extensive token vocabularies.
- Conservative Q-learning for Overestimation Control: VerifierQ incorporates a Conservative Q-learning (CQL) term to counter overestimation bias, making Q-value updates more conservative. In contrast to classic CQL, VerifierQ add a term to enabling balance between conservatism and optimism

### Strengths
The combined use of Implicit Q-learning (IQL) and Conservative Q-learning (CQL) is innovative and could offer promising results for balancing efficiency and accuracy in Q-value estimation for language models.

### Weaknesses
The paper is difficult to follow and some concepts and sections lack clear explanations

There are missing citations, often important concepts are introduced without a proper citation, for examples: 
-- line 094: generator-verifier framework
-- line 342: Polyak-average

Incomplete References: Published versions of cited works are not referenced.
Line 107: the two articles you are citing have been published respectively to NIPS 2020 and NIPS 2021, but you do not report this in the references.

Figures are hard to read, with text and images being too small (especially Figures 3 and 5).

The ablation section is inadequately detailed and lacks clarity.
Experiments described in figure 5 investigate parameter tuning rather than a true ablation, as they do not remove components to measure their impact, but rather modify \tau_1, without exploring the effect of \tau_2
The second part is unclear; it does not specify which components were from the original architecture, nor does it provide sufficient comments on results
Authors should enrich the ablation section by clearly detailing removed components, explaining the experimental setup, and discussing the results.

Detailed comments on the text (numbers refer to lines in the pdf):

044: I could not understand to which work "This approach" refers, please clarify.
068: Should this be "offline Q-learning" instead of "Q-learning"?
097: Please provide a clear definition for the input and output of the verifier
103: When you talk about offline Q-Learning, are you referring to a particular work or generally about offline techniques built upon Q-learning? Please clarify.
104: "More efficient" in what terms? Please specify.
Figure 1: 
    What is the source of action a_2 ?
    Why does a state generator generate an action?
    Why is the generator output described as a single action a_1, when for example at line 094 you say that "the generator's output can be treated as a SEQUENCE of actions" ?
164: Could you clarify or highlight where "utterance-level RL" is defined?
175-178: This concept is unclear; can you explain it further?
199: You mention modifying the offline Q-learning algorithm without defining offline Q-learning itself.
236: "taking action a'" is missing after ".. the next state s'"
325: When you talk about step, please refresh to what you are referring
363: What’s the rationale for splitting the fine-tuning process (first full, then LoRA)?
435: This is the first mention of “BERT-type” approaches. Please add context and references, and include utterance-level online approaches in related work if you plan to compare against them here.
440: Can you substantiate the claim of saving "10x training time"? What is the comparison baseline?

### Questions
Q1) Distributional shift is a typical issue for offline RL, I guess this is an issue for this apprach as well, please clarify.

Q2) Ablation: i) Did you explore changes to /tau_2? ii) How challenging is it to fine-tune /tau? iii) One dataset showed substantial differences with incorrect /tau_1 values. Have you tested other datasets in order to prove how sensitive is your model to /tau selection?

Q3) Possible limitations of the approach 
    - How much is the model sensible to parameters changes?
    - How does the method compares to other approaches in terms of memory rquirements ?

Q4) Would it be possible to test the code for reproducibility ?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes the VerifierQ, which use offline Q-learning to train the Verifiers of LLMs. The authors address three key challenges in applying Q-learning to LLMs: (1) handling utterance-level Markov Decision Processes (MDPs), (2) managing large action spaces, and (3) mitigating overestimation bias. The experiments on GSM8K and MATH show that the methods are better than baselines.

### Strengths
1. Combining RL and LLM is an important topic,  and VerifierQ validates the integration of RL into verifier models and demonstrates its potential to enhance test-time compute results.  

2. The authors address three practical challenges for the combinition of RL and LLM. Some of the design seems to be reasonable (Some Theorem shown that the methods can converge under mild conditions)

### Weaknesses
1. The paper writing needs to be improved. For example, line-068: key contributions:(1) We propose  ==> key contributions: (1) We propose; line-183: doesn't ==> does not; line-188: it's ==> it is; line-191: we've ==> we have; line-398: tau = 0.5 ==> tau_1 = 0.5; etc...

2. Some important details for the methods are missing. For example, Section 5.1 is hard to understand: (1) the authors say "We propose using the mean of the current Q-value and the traditional Bellman update as the target value" in line-212, and "The mean of the reward and next estimate serves as the target value for the Bellman update." in line-240. (2) The Figure 2 demonstrates the architecure, but it is not clear and not consistent with the text writing. 

3. Why directly applying IQL and CQL can address the Large Action Spaces and overestimation? It is know that large action space is very hard for RL. IQL and CQL are generally applied to traditional RL setting, with a few actions in the action space. 

4. The experiments are weak. Only testing the methods on two datasets with small LLMs.

### Questions
see the above.

### Soundness
2

### Presentation
2

### Contribution
3
