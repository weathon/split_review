# Prompt Optimization with Human Feedback

- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 6, 3, 3, 6

## Abstract
Large language models (LLMs) have demonstrated remarkable performances in various tasks. However, the performance of LLMs heavily depends on the input prompt, which has given rise to a number of recent works on \emph{prompt optimization}. However, previous works often require the availability of a numeric score to assess the quality of every prompt. Unfortunately, when a human user interacts with a black-box LLM, attaining such a score is often infeasible and unreliable. Instead, it is usually significantly easier and more reliable to obtain \emph{preference feedback} from a human user, i.e., showing the user the responses generated from a pair of prompts and asking the user which one is preferred. Therefore, in this paper, we study the problem of \emph{prompt optimization with human feedback} (POHF), in which we aim to optimize the prompt for a black-box LLM using only human preference feedback. Drawing inspiration from dueling bandits, we design a theoretically principled strategy to select a pair of prompts to query for preference feedback in every iteration, and hence introduce our algorithm named \emph{automated POHF} (\alg). We apply our \alg~algorithm to various tasks, including optimizing user instructions, prompt optimization for text-to-image generative models, and response optimization with human feedback (i.e., further refining the response using a variant of our \alg). The results demonstrate that our \alg~can efficiently find a good prompt using a small number of preference feedback instances.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces APOHF, for optimizing prompts for large language models (LLMs) using only human preference feedback rather than numeric scores. APOHF iteratively selects prompt pairs for user comparison, training a neural network to predict each prompt’s utility based on feedback. The algorithm selects prompts by combining utility prediction with an exploration-exploitation approach inspired by dueling bandits. Applied across tasks like instruction optimization and prompt tuning for text-to-image models, APOHF demonstrates more efficient prompt selection compared to baseline methods under limited feedback conditions.

### Strengths
* This paper presents a novel approach to prompt optimization by using human preference feedback alone, which is suitable for black-box LLMs.
* This paper is generally clear in its method description, though certain theoretical justifications could be expanded for a more rigorous understanding of APOHF’s design choices.
* The algorithm design balances prompt utility prediction with exploration, showing reliable performance across varied tasks.

### Weaknesses
 * The method employs the Bradley-Terry-Luce (BTL) model to represent human preference feedback, which assumes consistency and transitivity in user preferences. This may oversimplify human feedback, especially in real-world applications where user preferences can be inconsistent or influenced by context. The reliance on binary feedback might also limit the granularity of information available to the model, potentially leading to suboptimal prompt choices. 
* The method relies on a user-provided initial task description to generate the prompt domain, assuming that these initial examples are representative of the task requirements. This dependency introduces the potential for bias if the initial examples do not capture the full scope of the task or if the user’s interpretation is inconsistent with the intended outcomes. This reliance can constrain the model's flexibility and lead to prompts that are effective only in limited or narrowly defined scenarios.
* APOHF presumes that user preferences are consistent and relevant across multiple iterations, assuming stability in what constitutes an optimal prompt. However, in complex, open-ended tasks or tasks that evolve over time, user preferences may shift, and certain prompts that were optimal initially may no longer be relevant. This assumption limits the model's adaptability to dynamic contexts, reducing its applicability in real-world tasks where user expectations or task goals may evolve.

### Questions
* Have the authors examined how noise in user feedback impacts the accuracy of the prompt selection? Is the model robust to feedback inconsistencies or context-dependency in user preferences?
* Is there a way to iteratively refine or expand the prompt domain based on user feedback, to counteract biases introduced by an incomplete initial task description?
* Has the algorithm been tested in settings where user preferences or task requirements change over time? If so, how does APOHF handle shifts in user preferences?

### Soundness
3

### Presentation
3

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
This paper mentions a common issue of black-box LLM usages, where it is unavailable to automatically obtain a quality score for a given prompt, thus causing the difficulty of prompt optimization. Assuming that only human’s preference feedback is reliable, the authors propose APOHF, a framework to perform prompt optimization with human feedback. The proposed method aims to determine a good prompt via a prompt selection algorithm inspired by Dueling Bandits, based on a neural network performance predictor trained with the information from a small number of human feedback instances. The authors demonstrate quality improvement throughout iterations of the optimization. Overall, the experiment results show that the proposed framework is effective to obtain appropriate prompts with human feedback.

### Strengths
-  Inspired by the concept of RLHF and Dueling Bandits, the authors propose a prompt optimization framework leveraging human feedback. The experiment results show that the proposed method is indeed effective to a certain extent with actual demonstrations.

-  With the Bandit-fashioned prompt selection strategy, powered by a trained NN (MLP) model as the performance predictor, the proposed framework determines the prompt efficiently in terms of the number of required human feedback instances.

-  In the appendix, the authors also provide a brief coverage of theoretical explanations to justify the proposed prompt selection strategy.

### Weaknesses
 -   Limited Comparison with Prompt Optimization Baselines:
The authors' decision to exclude comparisons with state-of-the-art prompt optimization methods (e.g. TextGrad), citing the lack of a scoring method, may be overly restrictive. While direct human scoring might not be feasible, surrogate evaluation metrics (e.g., embedding-similarity between LLM output and ground truth) could serve as viable alternatives for these comparisons. Given the superior performance of existing prompt optimization methods across various tasks, their inclusion in the performance comparisons would provide valuable context and a more comprehensive evaluation of APOHF's effectiveness relative to the current state of the art.

- Dependency on Neural Network Models for Prompt Selection:
The proposed framework's prompt-pair selection strategy heavily relies on a trained neural network (MLP) model for performance prediction based on input embeddings. This approach introduces two potential sources of variability:
a) The choice of embedding model
b) The architecture and training of the performance predictor (MLP)
Both components may significantly influence the accuracy of performance predictions, potentially leading to substantial variations in the final LLM performance. A more robust analysis of these components' impact on the overall framework would strengthen the paper's credibility.

- Ambiguity in Prompt Domain Generation:
The process of generating the "discrete domain of prompts X" lacks sufficient detail. While the authors mention using a powerful LLM (e.g., ChatGPT) for prompt generation via in-context learning, the specifics of this crucial step remain unclear. Moreover, the paper lacks experimental analysis demonstrating how different prompt domain generation methods affect APOHF's overall performance. This omission limits the reader's ability to fully assess the method's robustness and generalizability.

### Questions
see weaknesses

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper mainly studies the prompt optimization problem. In specific, the main motivation coms from that previous PO methods usually require the availability of a numeric score to assess the quality of every prompt. This score is difficult or sometime unable to get in the situation when human interact with a black-box LLM system. Therefore, the authors claimed that preference feedback is more feasible given the mentioned human-llm interaction scenario. The authors thus proposed a method named APOHF for prompt optimization with human feedback. Some results show that this method can find a good prompt with several preference feedbacks used.

### Strengths
The paper is well written and easy to follow
The motivation is clear compared to previous method. [which may not be practical as per the weakness part]

### Weaknesses
The main weakness is the prompt optimization from human feedback itself may not be practical. Let me explain the reasons. 
1) The advantage or the main efforts of LLM is to improve its instruction following abilities, I.e., to cover as many prompts as possible. Therefore, when human in the loop, the key efforts should be in the zero-shot/few-shot abilities. If you expect the user to give feedback to the prompt provided by him/her-self, it may negatively impact the feasible application of this LLM product. How does your approach complement efforts to improve zero-shot/few-shot abilities of LLMs? Are there specific scenarios where human feedback on prompts provides unique value, even as LLMs improve their general instruction-following capabilities?


2) Prompt optimization itself is important for sure, but the efforts on making it automatic are more useful. For instance, as many APO did, LLM can improve the prompt itself by self-reflecting (e.g., reasoning the errors and self-refining current prompts). How does your method compare to or complement automated prompt optimization techniques like self-reflection? Are there potential advantages to incorporating human feedback alongside automated methods?

3) If let’s say we need human preference, we can directly train a reward model. Given the generalization ability of the reward model, we can directly sample the best response with requiring the human-preference during inference. How does your approach compare to training a reward model on human preferences? Could you discuss the potential advantages or disadvantages of your method compared to using a pre-trained reward model?

In addition, the experiments can be done on more types of tasks, such as math, coding, role-play, etc.

### Questions
Most of questions have been listed in the weakness part.

Another general question or suggestion would be: Could the author please raise up several real examples that can show the scenarios where the proposed method will be feasible to apply?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors of this paper studied prompt optimization using dueling bandit. The basic idea is to ask users to provide preference feedback on responses generated by two prompts, which is directly attributed to the quality of the prompts for further selection. Experiments on prompt optimization in text-to-text and text-to-image generation tasks, and also in response optimization, demonstrate the effectiveness of the proposed solution.

### Strengths
1.	Prompt optimization is an important problem in LLM studies, and the paper provides a valid perspective.
2.	The clarity of the manuscript is satisfactory, which helps readers to best comprehend the technique details.

### Weaknesses
1.	The proposed solution is rather standard: running dueling bandits on top of ChatGPT generated rewrites of initial queries. The synergy between these two components is very weak. Ideally, the proposal of new prompts should be informed by the learnt scoring function. But the current way, the new prompts are sampled from ChatGPT independently from the scoring function. The candidate prompt set is generated once by ChatGPT and remains static throughout the optimization process. This limits the potential for discovering truly novel or high-performing prompts that might lie outside the initial set. A more effective approach would involve dynamically generating new prompts based on the current state of the learned scoring function, allowing the search space to evolve and adapt during the optimization.
2.	As the users’ feedback is about the response, rather than the prompt itself, the LLM that generates the responses matters. Specifically, the prompt quality is a function of generator LLM as well. This clearly limits the generality of the proposed solution: the scoring function learnt with one LLM might not work well for other LLMs. Unfortunately, there is no experiment investigating this factor. The paper does not sufficiently address how the learned scoring function would perform when applied to a different LLM than the one used during the training phase. The dependence on the specific LLM used for generating responses is a significant limitation that needs to be empirically investigated.
3.	A few statements made in the paper are somehow overclaiming, for example, using a text encoder can avoid the need of a whitebox LLM, which does not seem to be advantageous, since the availability of whitebox LLM is no worse than an opensource text encoder. And I do not see what the principle is behind choosing the highest scored prompt in history as the first prompt, except it works better than randomly choosing two. The choice of the initial prompts, specifically selecting the highest scored prompt from history, lacks a strong theoretical justification. While it might empirically perform better than random selection, the paper does not provide a clear explanation of why this approach is expected to be optimal or even beneficial for the overall optimization process. This aspect requires more rigorous analysis and justification.

### Questions
1.	As the user feedback is provided to the response, instead of the prompt directly, how to we account for the variance caused by sampling from the LLM? For example, the user feels one result being better than another could be caused by LLM sampling, rather than the prompt. And I am not sure if this variance can be simply factored into the BT model.
2.	Does the learnt scoring function work across different generator LLMs? Similarly, does the learnt scoring function generalize across different tasks, e.g., question answering vs., text summarization?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
In existing prompt optimization work, the vast majority of methods rely on numerical scores to select better-performing prompts. However, in certain real-world tasks (e.g., text-to-image generation), using numerical scores for evaluation may not be applicable. To address this issue, the authors propose a human feedback-based prompt optimization method—APOHF. This method first collects pairs of human preference data and trains a neural network to provide latent scores aligned with human preferences. Then, combining greedy search and the method of maximizing the upper confidence bound, the authors select two prompts from multiple directions, balancing both performance and diverse prompt exploration. Experimental results show that after several iterations, APOHF can generate high-quality prompts.

### Strengths
1. The APOHF method proposed by the authors aims to solve the problem of prompt optimization in tasks that are difficult to evaluate using numerical scores, marking a new attempt different from previous studies.
2. APOHF outperforms other baseline methods in terms of performance.
3. The wide range of experimental types further validates the effectiveness of APOHF.
4. The authors' writing is clear, and the content of the paper is concise and easy to understand.

### Weaknesses
### 1. Experiment

a) From Table 6 in the appendix, I understand that for the user instruction optimization task, the authors chose two tasks, "rhymes" and "word sorting" (presumably from the BigBench dataset), which can be evaluated using numerical scores (such as accuracy), making them compatible with methods like APE, OPRO, and APO. I believe the authors should discuss this in more detail. Considering the rebuttal time constraints, You may focus on an in-depth analysis of 1 or 2 methods (such as APO, OPRO). Additionally, regarding the "sentiment" task in Table 6, why did the authors choose an initial instruction with a score of 0? For a simple instruction like "Determine the sentiment category (positive or negative) of a given sentence," a score of 0 should not occur. It is unclear if this is the score of the initial prompt or the initial task description, and this ambiguity needs to be addressed.

b) I recommend that the authors revise the way the curves are represented in the figures. The current use of square, circular, and triangular symbols makes the figures cluttered, making it difficult to discern curve details.

### 2. Motivation
a) For prompt tasks that are difficult to evaluate with numerical scores (e.g., text-to-image generation), the optimization target of the APOHF method is individual samples (such as generating images of a garden or a street). I believe the practical significance of such single-sample optimization is limited. In everyday usage, this approach has high resource costs, making it inefficient. In industry, optimizing meta prompts holds greater practical value.

b) As I know, APOHF is not the first prompt optimization work considering human feedback. Harvard and MIT have published a similar paper named **PRompt Optimization in Multi-Step Tasks (PROMST): Integrating Human Feedback and Heuristic-based Sampling (https://arxiv.org/pdf/2402.08702)**. I think it maybe diminish the contribution of this work.

### Questions
1. Regarding the resource consumption of APOHF, what is the specific cost? How many API calls were made in total, and how many tokens were consumed during the experiments?

2. In Figure 3, does it show the score of the newly generated prompt after each iteration? Why doesn't APOHF exhibit score fluctuations? Logically, the scores of results generated by different prompts should vary, making it unlikely for them to remain consistent.

3. In the text-to-image task, the authors measure the quality of generated images by calculating the similarity between the generated images and the ground truth. Could this similarity metric also be used as a scoring standard for methods like APO and OPRO?

4. How many data samples does the test set include?

5. Please answer my question refer to **Weakness  Section**

### Soundness
2

### Presentation
3

### Contribution
3
