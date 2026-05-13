# Reward Collapse in Aligning Large Language Models

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
The extraordinary capabilities of large language models (LLMs) such as ChatGPT and GPT-4 are in part unleashed by aligning them with reward models that are trained on human preferences, which are often represented as rankings of responses to prompts. In this paper, we document the phenomenon of \textit{reward collapse}, an empirical observation where the prevailing ranking-based approach results in an \textit{identical} reward distribution \textit{regardless} of the prompts during the terminal phase of training. This outcome is undesirable as open-ended prompts like ``write a short story about your best friend'' should yield a continuous range of rewards for their completions, while specific prompts like ``what is the capital of New Zealand'' should generate either high or low rewards. Our theoretical investigation reveals that reward collapse is primarily due to the insufficiency of the ranking-based objective function to incorporate prompt-related information during optimization. This insight allows us to derive closed-form expressions for the reward distribution associated with a set of utility functions in an asymptotic regime. To overcome reward collapse, we introduce a prompt-aware optimization scheme that provably admits a prompt-dependent reward distribution within the interpolating regime. Our experimental results suggest that our proposed prompt-aware utility functions significantly alleviate reward collapse during the training of reward models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents the theoretical finding of reward collapse when training reward models on ranking-based preference data. Through experiments, the authors demonstrate that the reward distributions for different prompts converge to a common prompt-independent distribution, disregarding whether prompts are open or closed-ended. To address this issue, they propose a prompt-aware utility function approach that learns distinct reward distributions based on prompt type.

### Strengths
strengths:
1. The paper clearly documents the phenomenon of reward collapse, supported by theoretical analysis and experiments. This is an important observation that will aid the development of prompt-aware reward modeling.
2. Empirically demonstrated that the reward distributions will converge towards a prompt-independent distribution.
3. The method is extended to handle pairwise preference data, improving applicability.

### Weaknesses
1. Does not provide much detail on how the prompt-aware utility function U_prom adaptively selects between U(x) = x and U(x) = -1/x in the experiments mentioned in Section 3.2. Do you manually assign utility functions based on the question type?
2. Experiments are done on only synthetic datasets where the word count is the ground-truth reward. Real-world ranking datasets would provide stronger validation.
3. It is not clear how the prompt-dependent reward distribution will contribute to the performance increase for RLHF or other direct optimization methods or just the best of n sampling. It would be great to see how this reward distribution will increase performance. 
4. The evidence of the reward collapse in Figure 1: what does the dashed region represent? is it over the 128 prompt datasets? It would be clearer to present the reward collapse phenomenon on a close-end question.
5. For the two subfigures in Figure 5, what are the differences between the two plots’s settings? Could you label the y-axis?

### Questions
please see weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the reward modeling in the alignment for LLMs. Specifically, the authors investigate the phenomenon of reward collapse in LLMs and proposes a prompt-aware optimization scheme to mitigate it. The key idea of the paper is to use a prompt-dependent utility function so that the distributions can be more diverse across different prompts. Empirical results are provided to verify the theoretical and intuitive results.

### Strengths
1 This paper is about an important and interesting problem in RLHF, and is very relevant to the community of Neurips. The authors first demonstrate the problem with various experiments of reward modeling, and motivate the approach with sound theoretical analysis.

2 The paper proposes a prompt-aware optimization scheme to overcome reward collapse and introduces utility functions that depend on the prompt to achieve prompt-dependent reward distributions. Real-world experiments on stackoverfolow and also synthetic experiments are conducted to support the findings and demonstrate a method superior to early stopping for addressing reward collapse.

As a paper for understanding some important problem in RLHF, the quality of the work is satisfactory.

### Weaknesses
1 How do the conclusions change if the assumption that the LLM is sufficiently overparameterized so that it can maximize the utility for all the prompts (discussions around equation (2))?

2 While the story and theoretical analysis are sound, the evidences of this paper are limited. But one thing I believe can largely improve the paper is that we can further evaluate the quality of the reward model by best-of-n policy. Specifically, we can fix a LLM, and for each prompt, we sample n responses and then take the one with the highest reward as the final output. Then, we can compare the responses by either human evaluation or GPT4 evaluation. For more details, you may check [1].

------------------------------------
Update in 11.11
Sorry for the late update. I just read the paper again and have a quick question about the choice of U. As I mentioned in the above review, the experiments conducted are rather limited and simple. In particular, the utility function used for the response length seems to be hard to generalize to general practical applications. Could you give an example of the choice of utility function in practice, e.g., used for the HH-RLHF dataset (whose details can be found in huggingface).

### Questions
see weakness

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper study the problem of RLHF for large language models. The paper firstly finds that the reward model trained by human rankings over different completions can not distinguish with open-ended and closed prompts, and call it as  the "reward collapse" phenomenon. The paper theoretically gives the reason, that is, the ranking-based objective function does not consider prompt-based factors. Some experimental analysis validates the claim.

### Strengths
Novelty: The claim proposed by the paper is novel and interesting.
Quality: The paper gives enough theoretical analysis and the experimental results validates the phenomenon.
Clarity: The paper is well written.
Significance: The proposed claim is interesting and meaningful for the LLM community.

### Weaknesses
Quality: The paper claims that we should use prompt-based utility function Eq.(3). However, all follow analysis is about the utility function without the prompt, which is inconsistent. The paper does not provide the implementation details of the prompt-aware training.

### Questions
See the above section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
