# Towards Learning to Reason at Pre-Training Scale

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Prompting a Large Language Model (LLM) to output Chain-of-Thought (CoT) reasoning improves performance on complex problem-solving tasks. Moreover, several popular approaches exist to "self-improve" the CoT reasoning abilities of LLMs on tasks where supervised (question, answer) datasets are already available. An emerging line of work explores whether self-improvement is possible without these supervised datasets, instead utilizing the same large, unstructured text corpora as used during pre-training. This would overcome the data availability bottleneck present in current self-improvement methods, and open the door towards compute-only scaling of language model reasoning ability. We investigate a fundamental question in this line of work: What constitutes a suitable reward function for learning to reason during general language model pretraining? We outline the desirable qualities of such a reward function and empirically demonstrate how different functions affect what reasoning is learnt and where reasoning is rewarded. Using these insights, we introduce a novel reward function called Reasoning Advantage (RA) that facilitates self-improving CoT reasoning on free-form question-answering (QA) data, where answers are unstructured and difficult to verify. We also perform an exploratory experiment optimizing RA on general unstructured text using offline RL, and our analysis indicates that future work should investigate methods for generating a more diverse set of CoTs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores how to enable large language models (LLMs) to self-improve their Chain-of-Thought (CoT) reasoning abilities using general pre-training data rather than supervised datasets. The authors investigate what makes a good reward function for learning reasoning during language modeling, examining how different reward functions affect both what reasoning is rewarded and where reasoning is applied. They introduce a novel "Reasoning Advantage (RA)" reward function that combines clipping and normalization techniques, and demonstrate its effectiveness on a new free-form question-answering dataset called MMLU-FREE-FORM, showing improved transfer to math reasoning tasks.

### Strengths
The systematic analysis of reward functions and their properties is thorough and well-motivated. The introduction of the RA reward function addresses key limitations of existing approaches, particularly in distinguishing good reasoning from random text and identifying appropriate contexts for reasoning. The creation of MMLU-FREE-FORM as an intermediate benchmark between structured QA and general language modeling is clever and useful for the research community. The empirical results showing successful transfer learning to GSM8K math problems provide concrete validation of their approach.

### Weaknesses
The paper's primary limitation appears in the scaling to general pre-training data, where the offline reinforcement learning approach that worked well on MMLU-FREE-FORM struggles to escape local optima of conservative reasoning. While the authors acknowledge this limitation and suggest future research directions, the paper doesn't fully solve the challenge of self-improving reasoning at pre-training scale. Additionally, while the authors demonstrate improved performance on mathematical reasoning tasks, there could be more exploration of how well their approach generalizes to other types of reasoning beyond mathematics. The analysis of high-scoring CoTs on OpenWebMath is also limited, and it's unclear what specific characteristics make these CoTs successful beyond a general notion of 'conservative' reasoning. The paper would benefit from a deeper dive into the specific types of errors that are reduced by the RA reward function.

### Questions
Have you explored whether the effectiveness of Reasoning Advantage (RA) varies across different types of reasoning tasks beyond math and standard QA?
In Section 5.2, you show that optimizing for RA leads to a 7% improvement on GSM8K. Could you provide more analysis of what specifically improved in the model's reasoning capabilities? Are there particular types of math problems where the improvement was more pronounced?
The paper mentions that only 0.01% of generated CoTs achieve a reward above 0.2 on OpenWebMath. Have you analyzed these high-scoring CoTs to understand what makes them successful? This analysis could inform better prompting strategies.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper titled explores the potential for self-improvement in large language models' ability to perform CoT reasoning without the need for supervised datasets. The authors frame this as a reinforcement learning problem where an LLM generates a CoT to predict subsequent tokens in a text corpus, receiving a reward based on the effectiveness of the CoT in predicting the next tokens. Their approach explores generating CoTs for next-token prediction in unstructured data, aiming to improve general-purpose reasoning abilities.

### Strengths
1. The paper presents a novel approach to improving CoT reasoning in LLMs, exploring reinforcement learning as a framework for unsupervised self-improvement. The introduction of RA offers an innovative solution to the reward function challenge.
2. This work addresses a crucial challenge in LLM development—achieving autonomous improvement in reasoning without reliance on human-generated data. If successful, this approach could significantly reduce reliance on expensive, curated datasets and enable more scalable reasoning improvement across diverse domains.

### Weaknesses
1. Some aspects of the reinforcement learning formulation could benefit from additional clarity, specifically regarding the choice of reward clipping values and the normalization strategies within RA. Additional explanation of these parameters and their impact on performance would make the approach more accessible.
2. The experiments focus primarily on a limited scope of problems (e.g., MMLU and OpenWebMath). The model’s performance on broader tasks, such as Tool learning or agent problem-solving scenarios, would offer stronger evidence of the approach’s generalizability.
3. By relying on the log-likelihood to evaluate the quality of intermediate reasoning (Chain-of-Thought) solely based on the model's ability to predict the following tokens, there is a risk that the model may overly focus on matching specific token patterns in the training data rather than developing generalized reasoning capabilities.

### Questions
See above.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores a method for self-improving CoT reasoning in LLMs without relying on curated datasets. By leveraging reinforcement learning on general pre-training data, the authors aim to enhance models’ reasoning abilities across diverse tasks. They introduce a new reward function, Reasoning Advantage (RA), which better identifies effective reasoning, and demonstrate its impact on open-ended question-answering tasks. The paper highlights RA’s potential but also suggests that more advanced optimization methods are needed for scalable CoT improvements in broader, less structured contexts.

### Strengths
1. This paper addresses an important issue: achieving self-improvement of CoT reasoning during the pre-training phase. This approach has significant potential to help overcome the data bottleneck in LLMs.

2. The paper explores several types of reward functions and establishes criteria for an effective reward function, which is valuable and insightful for future research in this area.

### Weaknesses
1. The technical contributions of the paper are relatively weak. The proposed MMLU-FREE-FORM is merely a simple adaptation of the original MMLU, and the introduced RA is only a minor modification based on token loss.

2. The paper somewhat overstates its contributions. The authors primarily demonstrate the positive impact of RA on MMLU-FREE-FORM, yet MMLU-FREE-FORM is derived from the structured MMLU dataset and cannot be regarded as a typical pre-training dataset. In fact, experiments on OpenWebMath show minimal improvement. Typical pre-training datasets often include substantial noise, such as HTML elements, which is a key challenge in achieving self-improvement CoT during the pre-training phase.

3. The paper lacks discussion on relevant work in reasoning enhancement during the pre-training phase, such as https://arxiv.org/pdf/2404.07965.

4. The experiments are insufficiently comprehensive, as they are conducted on only one model and one dataset. Testing with models of different parameter sizes within the same series or different architectures could help demonstrate the generalizability of RA.

5. The presentation of the paper could be improved. Some key findings should be in the main body rather than the Appendix, such as Appendix D and the definition of RA in Appendix A. Essential parameters, like the type of LLM used and inference hyperparameters, should also be included in the main text.

    Minor:
    - Punctuation should be added at the end of each equation.
    - Some quotation marks are unmatched, such as in line 265 and line 349.
    - Figure 1 appears somewhat rudimentary.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper explores effective rewards that could be applied during LLM pretraining. Especially, the paper explores various reward functions based on what reasoning is learnt and where reasoning is rewarded. Based on the findings, the paper suggests, RA (Reasoning advantage) which facilitates self-improving CoT reasoning on free- form question-answering (QA) data.

### Strengths
- The paper provides useful insights for designing rewards for language model training.
- The authors explores the effectiveness of RA on multiple experimental settings.

### Weaknesses
 - Unlike the motivation of the paper, the proposed method, RA, is not effective for pre-training scale, questioning the scalability of the proposed method.
- The paper measures the performance by using 'expected accuracy' metric, which makes comparison with other methods difficult. What is the absolute accuracy performance for Figure 4?
- The paper only uses a single backbone model to show the effect of the proposed method.

### Questions
- How effective is RA compared to another baseline model which is directly trained to predict the final answer without training to generate CoT?
- How much additional overhead occurs for applying RA during pre-training (Section 6)?

### Soundness
3

### Presentation
3

### Contribution
3
