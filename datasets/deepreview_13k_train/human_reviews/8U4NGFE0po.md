# PLHF: Prompt Learning from Few-shot Human Feedback

- Decision: Reject
- Scores: 5, 6, 3, 3, 5

## Abstract
Recent advances explore prompt tuning for large language models (LLMs) and develop automatic optimization frameworks to obtain suitable prompts with respect to desired output quality metrics. Although existing approaches can handle conventional tasks such as fixed-solution question answering, defining the metric becomes complicated when the output quality cannot be easily assessed by comparisons with standard golden samples, especially for those natural language applications that multiple outputs are equally valid. Consequently, optimizing the prompts effectively and efficiently without a clear metric becomes a critical challenge. To address this issue, we present PLHF, a few-shot prompt optimization framework inspired by the well-known RLHF technique. Different from naive strategies involving human experts, PLHF employs a specific evaluator module acting as the metric to estimate the output quality. PLHF requires only a single round of human feedback to complete the entire prompt optimization process. Empirical results on both public and industrial datasets show that PLHF significantly outperforms existing output scoring strategies for LLM prompt optimizations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method for few-shot prompt optimization using a small amount of human feedback, aiming to address issues in scenarios where there are no well-established evaluation metrics. Specifically, the authors decompose the system into two modules: the evaluator and the responser, and perform interactive optimization between the two modules. The authors compare their approach with mainstream baseline models on both public datasets and industrial datasets.

### Strengths
1. The paper is well written and easy to follow;
2. This paper investigates prompt optimization in scenarios without a clear metric, which is a very important research question;
3. The idea of introducing human feedback into prompt optimization is valuable.

### Weaknesses
1. As shown in Figure 3, the prompt optimization for E and R appears to only add a few few-shot examples, which is implemented based on methods like DSPy. This form of optimization that focuses solely on few-shot examples is relatively narrow, and the author needs to conduct a more comprehensive comparison with other prompt optimization methods.
2. The experimental baselines compared in the paper do not incorporate human annotations and feedback. The author should compare with methods that also introduce human feedback, such as Prompt Optimization with Human Feedback.
3. The modeling for the iterative optimization of E and R is relatively simple, involving first optimizing E and then optimizing R based on the guidance from E. The author needs to compare this with other iterative optimization methods and provide some theoretical analysis to support it.
4. Most of the experiments in the paper were conducted using GPT-3.5, and additional experiments with other models are needed to verify the generalizability.

### Questions
Please see the weaknesses.

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
4

### Summary
The paper studies the problem of prompt optimization which has recently gained significant attention in the community. In particular, the key focus of the paper is prompt optimization in situations when 1) no automated evaluation metrics for scoring generated outputs is available (as in MMLU, MATH, GSM8K etc) and 2) an automated evaluation / scoring using existing LLMs (e.g., GPT4o) are not reliable w.r.t to human evaluations (Fig.1). To address this, the authors explore a new approach referred to as PLHF, which aims to perform prompt optimization while using atmost linear number of human annotations w.r.t to the underlying dataset. The proposed approach consists of two main modules: responder LLM R and evaluator LLM E. The core of the approach boils down to optimizing the evaluator LLM E using few-shot training samples and then using the same to obtain the optimized prompt P for the responder module R (Alg.1). Quantitative experiments are provided on the three subjective evaluation datasets (e.g., Automated essay scoring) in order to demonstrate the efficacy of the proposed approach.

### Strengths
* The paper studies an important problem of performing prompt optimization for subjective tasks where 1) no objective evaluation is possible, and 2) automated scoring using existing LLMs is not feasible.
* The authors demonstrate consistent improvements across diverse tasks over prior works for prompt optimization when using limited samples and evaluating on subjective tasks
* The paper consists of good figures and examples which highlight the problem with using automated LLM metrics for evaluation.

### Weaknesses
 * One of my main concerns is limiting to gpt3.5 as the base model for the results presented in the paper.
      - While the paper shows prompt optimization results with GPT4o, the same also use GPT4o as the evaluator alone while still using GPT3.5 as the base model
      - Therefore, its not clear performance improvements from the proposed approach are limited to weaker models, or can they be extended to stronger models as well such as GPT4o, LLaMA-3.2 etc.
* Also in terms of the technical contribution, it seems that the proposed approach boils down to performing an additional prompt optimization w.r.t to the evaluator model before using the same for optimizing the prompt using TextGrad or DSPy.
     - For instance, instead of asking GPT4o (evaluator LLM) for rating the prompt, the proposed approach first provides additional prompt optimization for the evaluator prompt before then using the same for prompt optimization.
    - If so, then it would be more beneficial and clearer to state the same upfront in order to put the novelty of the paper in a more clear fashion.
   - Also while Fig.~3 seems to contain examples of initial and optimized prompts for the evaluator, it seems the optimized prompts largely consist of the in-context examples from the human annotations. If so, how is this different from simply providing the human annotations as additional context for the evaluator and responder model
 - It would be more useful to provide detailed initial and optimized prompts (similar to OPRO paper), demonstrating the what the optimization results look like.
* Finally, it would be beneficial to have a plot of the observed performance of the base model on different tasks, while varying the number of samples.
       - While Fig.~4 contains the plot of responder and evaluator LLM performance w.r.t to number of samples, it does not contain a plot for the final performance of the proposed approach as well as the baselines.

### Questions
Please refer the weakness section above.

### Soundness
3

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
The paper introduces Prompt Learning with Human Feedback (PLHF), a framework designed to optimize the prompts of LLMs with limited human feedback. PLHF comprises two key components: a Responder module that generates outputs and an Evaluator module that estimates output quality based on human feedback. It starts by having human experts score a set of training samples, then optimizes the Evaluator module (i.e. update the Evaluator prompt) to mimic these scores. The Responder module is subsequently optimized (i.e. update the Responder prompt) to generate outputs that align with the Evaluator's scoring. Empirical results on public and industrial datasets demonstrate PLHF's superiority over existing output scoring strategies for LLM prompt optimizations.

### Strengths
- The paper is clear, technically sound, and presents a new framework (PLHF) for prompt optimization. 
- The experimental results demonstrate the effectiveness of PLHF across various datasets.

### Weaknesses
 - The paper introduces an automatic prompt optimization method. However, upon reviewing the experimental section, it was observed that the method requires task-specific training to obtain the task-specific optimized prompt, suggesting it is not universally applicable (training one prompt for all tasks). As depicted in Figure 3, the initial prompt appears to be quite simplistic. This raises the question of whether the performance could be significantly improved by manually crafting more complex initial prompts. The manual design cost might be less compared to the overhead of training for each task individually. For instance, in the math problem example on the right side of Figure 1, where user feedback indicates the problem is too easy, an obvious solution would be to specify the difficulty level in the initial prompt. It would be insightful to understand if the proposed framework still offers significant improvements when starting with a more complex initial prompt, such as one incorporating chain-of-thought prompting or other established techniques, as is common in practical scenarios.
- Regarding the prompt optimizations for the Responder, it is unclear if the goal is to maximize the score of the Evaluator. The rationale for using only positive samples for training is not explicitly stated. What would be the impact if all labeled samples were used for training instead? Additionally, on lines 247, it is mentioned that a manual score threshold is required, which seems to imply that it needs to be adjusted on a per-task basis, adding to the task-specific tuning overhead. The lack of clarity on how this threshold is determined and its sensitivity to different tasks is a concern.
- The experimental section lacks details on how the training and test sets were divided, and the term "few-shot" is used without specifying the exact number of shots. This makes it difficult to reproduce the results and assess the generalizability of the findings. Specifically, for the SGD and AES datasets, the absence of a clear split strategy is a significant oversight. Furthermore, the paper does not specify if the few-shot examples were selected randomly or through a more strategic approach, which could impact the results.
- The number of rounds of experiments conducted for the results presented in Table 2 and 3 is not specified. Additionally, it is unclear if any significance testing was performed. As a reviewer, I cannot determine if the improvements obtained in Table 3 are statistically significant, especially considering that the scores are derived from a somewhat stochastic GPT model. The lack of variance reporting and statistical analysis makes it difficult to ascertain the robustness of the results.
- The paper would benefit from a more detailed discussion on the limitations of the PLHF framework and potential directions for future research in the conclusion section. The current conclusion is too brief and does not adequately address the practical challenges and future research avenues.

Typos:
- On line 083, the paper mentions "PO" which seems to be repeated.

### Questions
- What is the impact of more complex initial prompt design on the performance of the proposed framework?
- How does the manual score threshold affect the outcomes?
- Can the authors clarify how the training and test sets were divided for the SGD and AES datasets? This is particularly crucial given the emphasis on the few-shot setting.
- Were significance tests conducted for the results in Table 2 and 3? it would be beneficial for the authors to report the variance of results, especially considering that the test results are derived from the somewhat stochastic nature of GPT models?
- Table 3 shows a notably poor performance of the PO with Exact Matching method. Could the authors provide insights into why this method performed so poorly compared to other baselines?
- On line 320, the term "domain 1" is mentioned, but it is unclear what this refers to within the context of the paper.

Typos:
- On line 083, the paper mentions "PO" which seems to be repeated.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work proposed a few-shot prompt optimization framework that employs an evaluator module acting as a metric to estimate the output quality.  The framework requires only a single round of human feedback to complete the entire prompt optimization process.

### Strengths
Previous work relies on human feedback, whereas this study employs a prompt-optimized LLM as an evaluator to assess the output of LLM responses. By substituting human experts with an LLM, this approach enhances the automation of the evaluation process.

### Weaknesses
This work appears to be more focused on engineering applications rather than theoretical depth.
It is more suited for conferences like EMNLP, NAACL, or other NLP venues.
The contributions seem insufficient for an ICLR submission.

1. the symbols are not clear, for instance, in Figure 2, the abbreviations appear confusing and difficult to read.
2. how to define the score threshold in Figure 3 is not clear to me.
3. How reliable are the training samples labeled by humans, is it possible humans have biases on the scores?
4. I am curious if there is an experiment on page 8 that utilizes the PLHF framework with the base LLMs configured as GPT-4.

### Questions
1. the symbols are not clear, for instance, in Figure 2, the abbreviations appear confusing and difficult to read.
2. how to define the score threshold in Figure 3 is not clear to me. 
3. How reliable are the training samples labeled by humans, is it possible humans have biases on the scores?
4. I am curious if there is an experiment on page 8 that utilizes the PLHF framework with the base LLMs configured as GPT-4.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the lack of effective metrics in prompt refinement by proposing the PLHF method, which leverages human feedback. The approach includes a responder and an evaluator, where the evaluator simulates human feedback scores to iteratively improve the responder’s output based on these scores. Experiments conducted on various datasets and tasks demonstrate the method's effectiveness.

### Strengths
1.The paper's motivation is sound. Using LLMs for scoring may be unreliable and unstable. This paper proposed PLHF adopts a few-shot approach to align LLM scoring by using human-scoring examples, which is both intuitive and reasonable in my view.

2. The iterative, minimal human feedback mechanism effectively enhances the quality of optimized prompts.

### Weaknesses
1.My main concern is whether using few-shot examples of human scoring as feedback for LLM prompt optimization can consistently work. Can it genuinely mitigate the inherent issue of relying on a generative model (LLM) that outputs discriminative scores based on next-token prediction? I believe providing human scoring examples may be partially effective as guidance during the LLM scoring process. However, I remain skeptical about the overall effectiveness of this approach in addressing the core problem.

2.This approach raises a significant issue: the diversity, quality, and downstream task coverage of the human scoring examples become critical. These factors could greatly influence the effectiveness of prompt optimization on unseen cases and introduce specific requirements for data collection.

3.Additionally, the writing makes it somewhat challenging to grasp the main focus. For example, the methodology section lacks formal descriptions, relying heavily on textual explanations that complicate the reader’s understanding. Furthermore, Algorithm 1 appears overly lengthy and complex, covering both training and testing aspects.

4.My final concern lies with the experimental section. The experiments are relatively weak, lacking benchmark results. It would be valuable to see how the proposed PLHF method performs on datasets like Vicuna Eval and Self-instruct Eval.

5.Additionally, there are closely related works [1] that could be discussed.
[1] Black-Box Prompt Optimization: Aligning Large Language Models without Model Training”

### Questions
Please refer to the weakness.

### Soundness
2

### Presentation
2

### Contribution
2
