# $\texttt{CLR-Bench}$: Evaluating Large Language Models in College-Level Reasoning

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
Large language models (LLMs) have demonstrated their remarkable performance across various language understanding tasks. While emerging benchmarks have been proposed to evaluate LLMs in various domains such as mathematics and computer science, they merely measure the accuracy in terms of the final prediction on multi-choice questions. However, it remains insufficient to verify the essential understanding of LLMs given a chosen choice. To fill this gap, we present \texttt{CLR-Bench} to comprehensively evaluate the LLMs in complex college-level reasoning. Specifically, \((i)\) we prioritize 16 challenging college disciplines in computer science and artificial intelligence. The dataset contains 5 types of questions, while each question is associated with detailed explanations from experts. \((ii)\) To quantify a fair evaluation of LLMs' reasoning ability, we formalize the criteria with two novel metrics. Q$\rightarrow$A is utilized to measure the performance of direct \textbf{\underline{a}}nswer prediction, and Q$\rightarrow$AR effectively considers the joint ability to \textbf{\underline{a}}nswer the question and provide \textbf{\underline{r}}ationale simultaneously. Extensive experiments are conducted with 40 LLMs over 1,018 discipline-specific questions. The results demonstrate the key insights that LLMs, even the best closed-source LLM, i.e., GPT-4 turbo, tend to `\textit{\textbf{guess}}' the college-level answers. It shows a dramatic decrease in accuracy from 63.31\% Q$\rightarrow$A to 39.00\% Q$\rightarrow$AR, indicating an unsatisfactory reasoning ability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper evaluates the reasoning capabilities of current LLMs, introducing a new evaluation method and corresponding dataset. The author argues that assessing only the correctness of answers is insufficient; it is also necessary to evaluate how the model arrives at these answers. To address this, the author constructed a dataset containing different types of questions and answers, along with the reasoning processes behind the answers. The study evaluated both the accuracy of the answers provided by the LLMs and the correctness of their reasoning processes. Testing on mainstream LLMs revealed that these models tend to guess the answers, as the accuracy of their reasoning processes is generally much lower than that of their answers.

### Strengths
1. Currently, considering only answer correctness is indeed insufficient to comprehensively evaluate the reasoning ability of LLMs. The author’s proposal to assess the correctness of the reasoning process is a valuable direction.

2. The author evaluated mainstream LLMs, covering a wide range of models.

3. Using this newly proposed evaluation method, the author arrived at different conclusions, finding that LLMs tend to guess answers, as their reasoning correctness is significantly lower.

### Weaknesses
1. This paper discusses a lot about the logic and process of building datasets, but it does not include any steps for ensuring or validating data quality within this process. Although the paper emphasizes the high quality of the newly proposed evaluation dataset, there is no guarantee of this quality in the outlined process. Simply assuming that human-provided annotations are of high quality is unconvincing.

2. Some descriptions in this paper lack precision. For example, in line 321, how exactly is "partially correct" determined? Does it mean that as long as the first sentence is correct, it counts as partially correct, or is it based on the subjective judgment of experts?

3. The author provides an assessment method to validate Q->R accuracy. However, this method still requires a substantial amount of manual involvement. So, how can the evaluation data proposed in this paper be better spread?

4. The author only provided the 1-shot results. Although some explanation was provided, it was not convincing to me. In my view, conducting 0-shot and k-shot validations remains an important metric for evaluating the performance of different models.

### Questions
Although this work provided a good point to evaluate LLMs, there are still many drawbacks as shown in weakness. Please address them accordingly.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a novel benchmark CLR-Bench to evaluate the reasoning ability of LLM in college-level **computer science and artificial intelligence** tasks.
Based on the experimental results, the authors found that current LLMs tend to ‘guess’ answers for college-level questions, i.e., LLMs can reach the correct answer but contains incorrect reasoning steps.

### Strengths
- a novel benchmark on computer science and artificial intelligence tasks is proposed
- the writing is easy to follow

### Weaknesses
 - many wrong statements in this paper try to mislead readers:
  - In Table 1, GSM8K and MATH are not multiple-choice questions. Moreover, their samples contain complex rationale to evaluate LLMs. 
  - In L105, the authors claim that $Q\to A$ and $Q \to AR$ are two novel metric proposed by them. however, $Q\to A$ (i.e., outcome accuracy) has been widely used in many reasoning tasks to evaluate the performance. also, $Q\to R$ is equivalent to the process accuracy proposed in the paper Let's verify step by step (https://arxiv.org/abs/2305.20050). The only minor novelty in this paper is the $Q\to AR$ metric, which assigns 0.5 to the prediction if the answer is wrong but its process is correct. 
- evaluating the correctness of the reasoning path is a popular topic in LLM (some related works are list below), however, none of them are discussed in this paper.
  - Evaluating Mathematical Reasoning Beyond Accuracy
  - SELF-[IN]CORRECT: LLMs Struggle with Discriminating Self-Generated Responses
  - SELFCHECK: USING LLMS TO ZERO-SHOT CHECK THEIR OWN STEP-BY-STEP REASONING
  - Let's Verify Step by Step
  - The Generative AI Paradox: “What It Can Create, It May Not Understand”
- the proposed benchmark is very small (only about 1k samples) and is very narrow (computer science). Hence, the observations are also limited to the computer science domain and cannot be generalized to other reasoning tasks. 
- Previous works usually study the process correctness of mathematical problems. compared with existing math benchmarks, what are the essential advantages of using computer science discipline?

### Questions
see above Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work presents CLR-BE, a dataset consisting of questions from 16 challenging college disciplines in computer science and artificial intelligence. The dataset contains 5 types of questions, while each question is associated with detailed explanations from experts. The paper introduces a method to judge the models’ reasoning abilities based on the correctness of their reasoning paths.

### Strengths
1.The dataset provides a new way to evaluate the reasoning abilities of LLMs, focusing on the correctness of the reasoning process instead of only on the final answer

2.The paper is well presented, with clear figures and illustrations

### Weaknesses
1.The domain of the problems seems limited, as it seems to only contain computer science related questions. Computer science seems not to be a very representative field for the evaluation of reasoning abilities. The dataset can benefit from inclusion of more challenging and reasoning intensive tasks from subjects such as math and physics.

2.The evaluation of the correctness of reasoning processes involves semantic similarity and GPT-4-assisted expert evaluation. I am not so sure about the accuracy of this evaluation process as reasoning paths can be varied. Also, the errors in reasoning paths can be subtle, and this method of evaluation seems a little coarse to me.

### Questions
The dataset contains a lot of choice questions. Perhaps a more efficient way is to transform choice questions into open-ended ones with more possible final answers to ensure that a correct final answer indicates a correct reasoning process?

It would be good to have more case studies about various model generated solutions, including false positives, false negatives, ect.

### Soundness
3

### Presentation
3

### Contribution
2
