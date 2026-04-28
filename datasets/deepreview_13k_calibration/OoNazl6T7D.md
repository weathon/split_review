# Language Model Non-Myopic Generation for Reasoning and Planning

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Large Language Models have demonstrated remarkable abilities in reasoning and planning by breaking down complex problems into sequential steps. Despite their success in various domains like mathematical problem-solving and coding, LLMs face challenges in ensuring reliable and optimal planning due to their inherent myopic nature of autoregressive decoding. This paper revisits LLM reasoning from an optimal-control perspective, proposing a novel method, Predictive-Decoding, that leverages Model Predictive Control to enhance planning accuracy. By re-weighting LLM distributions based on foresight trajectories, Predictive-Decoding aims to mitigate early errors and promote non-myopic planning. Our experiments show significant improvements in a wide range of tasks for math, coding, and agents. Furthermore, Predictive-Decoding demonstrates computational efficiency, outperforming search baselines with reduced computational resources. This study provides insights into optimizing LLM planning capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper looks at LLM planning and reasoning from an optimal control perspective and proposes a novel method to enhance planning accuracy. The authors argue that LLMs face challenges in reliable and optimal planning due to their inherent myopic nature of autoregressive decoding. Predictive-Decoding leverages Model Predictive Control to re-weight LLM distributions based on foresight trajectories, aiming to mitigate early errors and promote non-myopic planning.

### Strengths
1. The idea of making the LLM to think long term (non-myopic) makes sense for LLM planing and reasoning
2. The author seems to perform different experimentation on different test-beds.

### Weaknesses
1. the presentation of this paper could be improved (for instance fig 1 is too many figures/text, could you make it simpler)?
2. the introduction of "Myopic Gap" seems to be interesting, but the section could be rewritten for better readability. 
3. lacking larger llm model size for math and gsm experimentation.

### Questions
1. how does the number of FLOPS related to # of tokens? And also to the actual decoding/inference time?
2. how sensitive in the sampling temperature in determining the optimal solution parameter? Do you have to tune this for each test-beds?
3. it seems the diversity is still an issue even in the MPC problem right? how would you solve it?

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
In this work, authors propose Predictive-Decoding, a training-free approach to improve LLM planning with non-myopic generation, based on their claim that focusing solely on historical information can lead to irreversible mistakes and potential planning failures. Targeting at the myopia issue in language models pretrained with next-token prediction, Predictive-Decoding leverages Model Predictive Control to enhance planning accuracy.

### Strengths
1. investigate an important problem, i.e. short-sightedness.
2. Good performance-budget balance in experiments.

### Weaknesses
1. case study? (focusing solely on historical information can lead to irreversible mistakes and potential planning failures.)
2. The formulation in lines 126-127 is not a POMDP, and lacks of mapping from global states to local observations. 
3. I'm concerned that the author's hypotheses in lines 188-191 are untenable. It seems like saying that "the more confident the answer is for a given model, the more likely it is to be correct." and in this case the greedy answer should usually be selected?

### Questions
See the Weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper addresses the problem of myopia (short-sightedness) in Large Language Models (LLMs) during reasoning and planning tasks. It proposes a novel method called Predictive-Decoding, which leverages Model Predictive Control (MPC) to mitigate early errors and enhance non-myopic planning. By re-weighting the LLM distributions based on foresight trajectories, the method aims to improve planning accuracy. Extensive experiments demonstrate significant improvements in performance across various tasks, including math problem-solving, coding, and agent-based interactions. The proposed method shows computational efficiency, outperforming search-based baselines with reduced computational resources.

### Strengths
- The application of Model Predictive Control to mitigate myopia in LLMs is a novel approach that enhances planning accuracy.
- The paper provides a solid foundation and supports the claims with experimental results.
- The paper is well-organized, with clear explanations of the problem, methodology, and results.

### Weaknesses
See questions

### Questions
Failure Cases: Can the authors provide more insights into the specific scenarios where Predictive-Decoding may fail or perform sub-optimally? What are the common characteristics of these failure cases?

Broader Applicability: Have the authors considered testing the method on more open-ended tasks, such as advanced data analysis or complex decision-making scenarios? 

Parameter Sensitivity: Can the authors provide more details on the sensitivity of the method to different hyperparameters (e.g., foresight length, sampling number)?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents "Predictive-Decoding," a novel optimal-control approach that enhances Large Language Models' planning and reasoning capabilities by leveraging Model Predictive Control to overcome the myopic limitations of autoregressive decoding. The method reweights LLM distributions based on foresight trajectories, demonstrating improved performance in math, coding, and agent-based tasks while being computationally more efficient than existing search-based methods.

### Strengths
- The framework can work on different kinds of tasks.
- The method makes sense.
- Attempt to fair comparison on the effort to the number of tokens.

### Weaknesses
 - The proposed method is not particularly fancy; the Lookahead Search in [1] presented an almost identical approach.
- The paper lacks comparison with the latest search algorithms, such as BFS-based TOT and A*-based Q*[2]. The authors should have included comparisons with these SOTA algorithms in the experimental section.
- The paper needs more discussion on results based on different rewards (Self reflection/Reward model). There seems to be a lack of details regarding the evaluation steps in the search process.
- Many existing papers have suggested that LLMs do not inherently possess self-reflection capabilities. This paper lacks detailed experimental discussion regarding self-feedback abilities.

### Questions
- Differentiate between the mentioned Lookahead Search and explain what makes Predictive-Decoding unique. 
- Additional experimental results are needed: provide more detailed comparison with TOT and Q*.
- More specifics about the evaluation process during decoding.

### Soundness
2

### Presentation
3

### Contribution
2
