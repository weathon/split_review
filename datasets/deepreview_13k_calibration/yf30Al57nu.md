# CodeLutra: Boosting LLM Code Generation via Preference-Guided Refinement

- Decision: Reject
- Avg Score: 5.00
- Scores: 8, 5, 3, 3, 6

## Abstract
Large Language Models (LLMs) have significantly advanced code generation but often require substantial resources and tend to over-generalize, limiting their efficiency for specific tasks. Fine-tuning smaller, open-source LLMs presents a viable alternative; however, it typically lags behind cutting-edge models due to supervised fine-tuning's reliance solely on correct code examples, which restricts the model's ability to learn from its own mistakes and adapt to diverse programming challenges. To bridge this gap, we introduce \textsc{CodeLutra}, a novel framework that enhances low-performing LLMs by leveraging both successful and failed code generation attempts. Unlike conventional supervised fine-tuning, \textsc{CodeLutra} employs an iterative preference-guided refinement mechanism to compare correct and incorrect solutions as well as maximize the likelihood of correct codes. Through continuous refinement, \textsc{CodeLutra} enables smaller LLMs to match or surpass GPT-4’s performance in various code generation tasks without relying on vast external datasets or larger auxiliary models. On a challenging data science coding task, using just 500 samples improved Llama-3-8B's accuracy from 28.2\% to 48.6\%, approaching GPT-4's performance. These results highlight \textsc{CodeLutra}'s potential to close the gap between open-source and closed-source models, making it a promising approach in the field of code generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents CodeLutra, a supervised fine-tuning (SFT) approach that demonstrates significant improvements on coding tasks. Specifically, CodeLutra achieves GPT-4-level performance fine-tuning an open-source 8-billion-parameter model using as few as 500 samples (with groundtruth solutions). The key idea behind CodeLutra is to use both positive and negative examples to fine-tune the model, creating a hybrid of SFT and DPO techniques. CodeLutra assumes a ground truth to generate these examples: if a sample code produces the same inputs/outputs as the ground truth, it is a positive example; otherwise, it is a negative example.

### Strengths
- CodeLutra simple yet effective method, with clear articulation of how it differs from related work.

- Impressive results: with only 500 samples, CodeLutra achieves GPT-4-level performance on a base model with just 8 billion parameters. For the Spider benchmark, it improves base model performance from 59.3 to 74.4 in just four iterations, surpassing GPT-4’s 74.4. On BIRD, it increases performance from 22.3 to 42.6 in four iterations, approaching GPT-4’s 46.3.

- Comprehensive evaluation, covering three coding benchmarks (Spider, BIRD, and DS-1000) and three models (Llama-3-8B, Gemma-7B, and StarCode-7B), demonstrating the approach's generalizability.

- Strong ablations that address key questions: (i) dual loss significantly boosts performance, raising it from 17.2 (DPO) to 76.6 on Spider; (ii) negative samples are crucial, as performance increases from 20 to over 40 with their inclusion, while positive samples alone yield minimal improvement.

### Weaknesses
 - Current evaluation focuses on SQL queries and data science problems, which are relatively short (from a few lines of code to several 10s of lines of code). It would be interesting to see how this approach generalizes to longer programs. Specifically, the evaluation lacks assessment on code that involves complex control flow, multiple function calls, or intricate data structures, which are common in real-world applications and competitive coding scenarios. The current benchmarks, while useful, do not fully capture the challenges of generating and refining longer, more complex code sequences. 
- Limited exploration of scenarios without ground truth. In such cases, CodeLutra relies on syntactic error detection, but the results are, as expected, less impressive. The reliance on syntactic error detection as a fallback mechanism without ground truth is a significant limitation. This approach does not address semantic errors or logical inconsistencies that may be present in the generated code, which are critical for ensuring the correctness of the program. The paper should explore alternative methods for error detection and correction in the absence of ground truth, such as using static analysis tools or employing more sophisticated techniques for code verification.

### Questions
- How does CodeLutra perform on longer programs, e.g,, competitive coding? (This is nice to have; the material in the paper is enough for publication.)
- What is the CodeLutra's performance vs program length on the current data sets?

### Soundness
3

### Presentation
3

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
This paper proposes a method by iteratively generating successful and failed code and training with preference optimization.

### Strengths
The paper is well-written. The proposed method with training with correct and failed generations iteratively makes sense. Experiments show good improvement on benchmarks.

### Weaknesses
Some experimental setup is not clear enough, such as training data, SFT setting, and details of synthetically generated dataset. One of the contribution DPO and SFT loss is studied in previous literature. More experiments might be needed for comparing SFT then DPO with DPO+SFT loss.

- In line 150, "if the model only predicts wrongly in the final token in a code snippet, the overall probability P (y|x) in the Equation 1 might still remain high as the preceding tokens are correct". While the hypothesis makes sense, do you really observe this situation in real LLM and dataset? I doubt it.
- Equation 6 is studied in a previous literature "Provably Mitigating Overoptimization in RLHF: Your SFT Loss is Implicitly an Adversarial Regularizer" with theoretical support, but not cited. This also limits the novelty contribution (at least on this part).
- I'm confused with the experimental setup. What is the training dataset? It seems the experiment is using the test dataset to train. Could you clarify?
- Could you explain the setting for SFT in Table 1? One baseline is the SFT model that only uses the groundtruth training solutions, or use the synthetically generated correct solutions. Which one are you using?
- I don't think Table 2 is a right setting, where 17.2 and 12.4 is extremely low for DPO-only method. Normally we do DPO training on top of SFT model. The right setup should be training on top of SFT model. What is the gap between, SFT then DPO training and the SFT regularized preference training?
- 500 samples might mean that 500 prompts or problems. What is the size of generated samples overall?

### Questions
- In line 150, "if the model only predicts wrongly in the final token in a code snippet, the overall probability P (y|x) in the Equation 1 might still remain high as the preceding tokens are correct". While the hypothesis makes sense, do you really observe this situation in real LLM and dataset? I doubt it.
- Equation 6 is studied in a previous literature "Provably Mitigating Overoptimization in RLHF: Your SFT Loss is Implicitly an Adversarial Regularizer" with theoretical support, but not cited. This also limits the novelty contribution (at least on this part).
- I'm confused with the experimental setup. What is the training dataset? It seems the experiment is using the test dataset to train. Could you clarify?
- Could you explain the setting for SFT in Table 1? One baseline is the SFT model that only uses the groundtruth training solutions, or use the synthetically generated correct solutions. Which one are you using?
- I don't think Table 2 is a right setting, where 17.2 and 12.4 is extremely low for DPO-only method. Normally we do DPO training on top of SFT model. The right setup should be training on top of SFT model. What is the gap between, SFT then DPO training and the SFT regularized preference training?
- 500 samples might mean that 500 prompts or problems. What is the size of generated samples overall?

### Soundness
4

### Presentation
4

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
The paper introduces CODELUTRA, a framework designed to enhance the performance of LLMs in code generation tasks. However, the method is almost the same as an existing method.

### Strengths
NA

### Weaknesses
1. The proposed method closely resembles that presented in [1]. Applying the same approach to a different scenario does not warrant publication, especially since this new scenario is simpler and benefits from execution feedback.

[1] Iterative Reasoning Preference Optimization. https://arxiv.org/abs/2404.19733

### Questions
NA

### Soundness
2

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
4

### Summary
The paper proposes CODELUTRA, a preference-guided training framework to let code LLMs iteratively refine itself based on execution signals from its own generations. Specifically, given a task-specific training set, at each iteration, the model generates answers which are then evaluated by unit tests. Each correct answer is paired with an incorrect answer to form a preference pair. The preference dataset is then used for DPO training. To address the issue that DPO may reduce the generation probability of both correct and incorrect answers, supervised finetuning loss is added to DPO loss for joint training. Experiments show that CODELUTRA significantly improves performance on SQL and data science tasks, and is much more effective than DPO alone.

### Strengths
* Comprehensive evaluation, ablation, and analysis support the effectiveness of the proposed method. In particular, the necessity of negative training samples and of SFT loss are both well studied.
* The paper is well written and easy to follow.

### Weaknesses
 * The technical novelty of this paper is somewhat limited. L233-246 claimed two major points of novelty: refinement from execution feedback and dual loss mechanism. First, using feedbacks from program execution to iteratively refine code LLMs is a direction that has been extensively studied (e.g., CodeRL [1], and NExT [2]). However, these works are not discussed in the related work section. Second, the dual loss objective (i.e. adding SFT loss in DPO training) was proposed in [3], known as RPO, which is not cited.
* I find DS-1000 Pass@1 results in Table 1 are inconsistent with the public leaderboard (https://ds1000-code-gen.github.io/model_DS1000.html). In particular, pass@1 of Codestral-22B and Llama-3-70B-Chat is 51.2 and 48.6 respectively in the leaderboard, but 35.8 and 36.4 respectively as reported in the paper.

### Questions
* Are the two answers in Figure 5 flipped? Given Currency is in table customers, I feel the first answer is correct, and the second is wrong.

### Soundness
2

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
3

### Summary
The authors proposed a new training framework called CODELUTRA which aims to fine-tune a small CodeLM to match or surpass the closed-source LLMs like GPT-4. CODELUTRA adopts an iterative method to learn by comparing the correct generation and the failed generation. At each iteration, CODELUTRA constructs the preference dataset by classifying the generation codes of the model from the last iteration and employs a dual-loss function that combines DPO with SFT for training. The authors show that their method can achieve a performance comparable to GPT-4 in the data query and data science tasks.

### Strengths
1. The paper is well-organized and easy to follow
2. The proposed method can lead to a fine-tuned LLAMA3-8B model which has comparable performance to GPT-4.
3. The authors conduct comprehensive ablation studies that the effect of every component involved in their method is clearly demonstrated.
4. The method can still have good performance with limited annotations or training samples.

### Weaknesses
1. Line 230 states that "The refinement process continues until the improvement between consecutive iteration becomes marginal". However, in the experiments, the authors seem to fix the iteration number to 4. In practice, how do you decide if the improvement between consecutive iterations is marginal?

2. The baseline setup is not clear enough and may not be comprehensive.
a) For closed-source LLMs, it is unknown what prompting method is used. It is also not clearly stated what fine-tuning method is used. From the Appendix, I infer that the LoRA is used in CODELUTRA but is it also used in the fine-tuning baseline?
b) In Table 1, since LLAMA-3 is used as the base model for CODELUTRA, the authors should apply more previous fine-tuning methods in the same setting and compare with them instead of comparing with different open-source CodeLLMs. For example, the related work section mentions other fine-tuning methods (Line 520), e.g. Self-debug and Codefort. The authors should apply them to fine-tune LLAMA3 and compare the results.

3. Paper presentations can be further improved. Specifically, a) Line 142 $f$ is not defined. b) The notations in the legend of Figure 2 are not defined.

### Questions
1. See weakness 1, 2
2. I am curious that if this method can lead to a model that is generalizable. For example, the authors split DS-1000 for training and evaluation. I wonder how the resulting model would perform on other similar datasets, e.g. MBPP?

### Soundness
3

### Presentation
3

### Contribution
3
