# Automatic Curriculum Expert Iteration for Reliable LLM Reasoning

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Hallucinations (i.e., generating plausible but inaccurate content) and laziness (i.e. excessive refusals or defaulting to ``I don't know'') persist as major challenges in LLM reasoning.
Current efforts to reduce hallucinations primarily focus on factual errors in knowledge-grounded tasks, often neglecting hallucinations related to faulty reasoning. Meanwhile, some approaches render LLMs overly conservative, limiting their problem-solving capabilities.
To mitigate hallucination and laziness in reasoning tasks, we propose \textbf{Auto}matic \textbf{C}urriculum \textbf{E}xpert \textbf{I}teration (\textsc{Auto-CEI}) to enhance LLM reasoning and align responses to the model’s capabilities--assertively answering within its limits and declining when tasks exceed them.
In our method, 
Expert Iteration explores the reasoning trajectories near the LLM policy, guiding incorrect paths back on track to reduce compounding errors and improve robustness; it also promotes appropriate ``I don't know'' responses after sufficient reasoning attempts.
The curriculum automatically adjusts rewards, incentivizing extended reasoning before acknowledging incapability, thereby pushing the limits of LLM reasoning and aligning its behaviour with these limits.
We compare \textsc{Auto-CEI} with various SOTA baselines across logical reasoning, mathematics, and planning tasks, where \textsc{Auto-CEI} achieves superior alignment by effectively balancing assertiveness and conservativeness.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper addresses the problem of hallucinations in reasoning for large language models. Specifically, in methods that use expert iteration for improving this reasoning in LLMs. The authors propose adding a Refusal option to the EI pipeline and rewarding the refusal when the problem has a certain level of difficulty (length of reasoning is used as a proxy for difficulty). Based on the reward that a response gets, the data for the next iteration of EI is selected accordingly. To balance refusal and improvements in reasoning, the authors propose using a curriculum to balance the two objectives. Based on measures of accuracy and refusal rate, the authors show the effectiveness of their method compared to baselines and ablations.

### Strengths
- The paper is clearly motivated, the problem of hallucinations in LLM reasoning has not been explored as much.
- The paper presents the problem, the methods and the baselines clearly.
- The results on the three datasets, MATH, blocksworld and boardgameQA are comprehensive and provide sufficient evidence of the utility of the method.
- The authors also present sufficient ablations of their method, with varying versions of the curriculum used.

### Weaknesses
 - Missing citations for central EI works: STaR (https://arxiv.org/abs/2203.14465), Training Chain-of-Thought via Latent-Variable Inference (https://arxiv.org/abs/2403.04642)
- What other measures of difficulty are possible (very recent paper that the authors can choose to ignore since it came out after the paper deadline: https://arxiv.org/abs/2410.04707)? Can a linear probe decode difficulty? A discussion is needed.
- Similarly, are there other mechanisms of knowing when to say I dont know possible? Is a linear probe enough for refusal? Like in Language models mostly know what they know (https://arxiv.org/abs/2207.05221).
- Where could the current framework of length based difficulty fail? When sampling multiple times, what is the variation in the number of steps needed to reach the answer for a problem?
- Are the number of iterations for Auto-CEI and EI etc matched? More generally, how does the amount of training data / compute required vary across the method and baselines? I think some of the implementation details could be moved to main in the revision. This would help readability.
- How could this method be extended beyond expert iteration, to more online methods of learning like PPO or REINFORCE?

### Questions
See weaknesses.

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
5

### Summary
This paper proposes an automatic curriculum expert iteration (AUTO-CEI) to enhance LLM reasoning and align responses to the model's capabilities. Enable the model to answer within its limits and decline when tasks exceed them.
Expert iteration can explore the reasoning trajectories near the LLM policy, guiding incorrect paths back on track to reduce compounding errors and improve robustness.
AUTO-CEI uses the length of reasoning steps to measure difficulty and designs an automatic curriculum for expert iteration that rewards correct reasoning.
AUTO-CEI can automatically estimates the boundary of LLMs' reasoning capacity to achieve a reasonable alignment to maximize capacity and control behaviors.

### Strengths
1. Using expert iteration is a good idea.
2. The authors consider the trade off between avoiding hallucinations and avoiding laziness, which is important.
3. This paper aims to avoiding reasoning hallucinations and teaching the model to say IDK to reasoning tasks which beyond its ability.

### Weaknesses
1. Although considering the trade off between helpfulness and laziness, the paper control this trade off by hyper-parameters, instead of proposing some principles or methods to chose the optimal hyper-parameters.
2. The evaluation metrics in the paper are incomplete; for example, IDK only measures the proportion of times the model outputs "IDK" without assessing the accuracy of those IDK responses.
3. The experiments in the paper may involve unfair comparisons, as AUTO-CEI conducts multiple searches for EI, resulting in significantly more training steps and data compared to other methods.

### Questions
Why the process of update R is called curriculum learning? IMO, I think it is more like a search process and curriculum learning is about first learning elementary stuffs and then complex stuffs.

### Soundness
3

### Presentation
3

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
This paper enhances LLM calibration ability in reasoning tasks by mitigating hallucinations and reducing lazy behaviors. The method uses a curriculum of expert iteration, balancing answering the question and saying 'I don't know' by adapting the reward system according to the difficulty of reasoning tasks. It shows great balancing in assertiveness and conservativeness.

### Strengths
1. The paper presents a reasonable motivation that previous approaches to addressing hallucination problems often suffer from overcorrection, leading to overly conservative responses from LLMs on many questions.

2. The paper introduces an innovative reward mechanism that dynamically balances the choice between responding or refusing to answer based on question difficulty. Subsequent experiments demonstrate that this method effectively handles the trade-off between answering and refusing. Figure 3 also illustrates that as the generated text length increases, more questions are declined.

3. The writing is clear, and the figures are well-designed, enhancing the overall readability of the paper.

### Weaknesses
1. The paper’s reward uses the length of the generated text to measure the level of the exploration. This limits the method’s generalizability and scalability, as it’s challenging to find a universal text processing metric for different types of text (e.g., code, tables). Furthermore, reward parameters such as c1 and c2​ also vary across datasets, which makes me concerned about the method’s effectiveness in situations where training and testing distributions are not similar. The reliance on newline characters as step separators is also problematic, as this is a heuristic that may not apply to all text formats or even all natural language tasks. For example, in tasks requiring JSON output, such as in LLM agent design, this approach would not be suitable. The method's reliance on a specific text formatting convention limits its applicability and requires manual tuning for different output formats.

2. The experimental results show that even the best method in this paper achieves overall accuracy significantly lower than Vanilla EI. While I understand that incorporating refusal may lead to a drop in accuracy, achieving performance closer to Vanilla EI would be more compelling, as the current method shows that adding a refusal option will significantly reduce the accuracy.

### Questions
1. The MATH dataset has manually labeled question difficulty; it would be helpful to include a figure illustrating the correlation between generated text length and question difficulty as a validation of this signal.

2. Is the method effective across datasets with different distributions?

3. There are many established metrics for measuring uncertainty with different confidence levels, such as AP used in R-tuning. The current paper only reports results for the binary case, i.e., answering or refusing to answer. I am curious about the performance of this method at different confidence levels.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes Automatic Curriculum Expert Iteration (AUTOCEI) to enhance LLM reasoning and align responses to the model's capabilities–assertively answering within its limits and declining when tasks exceed them, so as to mitigate hallucination and laziness in reasoning tasks. Through experiments on  BoardgameQA, MATH and Blocksworld with Llama-3.1-8B-instruct, The authors demonstrate the effectiveness of AUTO-CEI, achieving superior alignment by effectively balancing assertiveness and conservativeness.

### Strengths
* This paper is well-written and presents clear ideas.

* The idea of aligning responses to the model's capabilities–assertively answering within its limits and declining when tasks exceed them is novel.

* The  motivation behind AUTO-CEI is straightforward and strong.

### Weaknesses
 * AUTO-CEI introduces additianal training overheads. Considering that the process of AUTO-CEI includes EXPERT ITERATION (each iteration needs large amount of resampling), the additional training overhead can not be ignored. I suggest the authors align the sampling cost between different baselines.

* Limited validation across models. The effectiveness of AUTO-CEI is validated only on Llama-3.1-8B-instruct. Further exploration is needed to assess the generalizability to other models.

* The performance is significantly affected by the hyperparameter λ. Table 2 shows that the performance of AUTO-CEI fluctuates greatly under different λ, which can lead to a considerable amount of additional cost during actual usage.

* The correlation between the number of reasoning steps and difficulty is not sufficiently strong to justify its use as a reliable proxy for difficulty. The reported Pearson's correlation coefficients of 0.263 and 0.196 do not indicate a strong linear relationship, suggesting that reasoning steps may not accurately capture the underlying complexity of the tasks.

### Questions
See weaknesses.

Additionaly,

(1) Have you tested the correlation between the number of reasoning steps and difficulty, as this is a key assumption of AUTO-CEI? If not, I suggest conducting a test experiment on the MATH dataset, considering it has manually labeled difficulty tags.

typos:
line 286 N -> K

### Soundness
3

### Presentation
3

### Contribution
4
