# CodeDPO: Aligning Code Models with Self Generated and Verified Source Code

- Decision: Reject
- Scores: 3, 5, 3, 6

## Abstract
Code generation models have shown significant potential for programming tasks. 
However, existing training methods like supervised fine-tuning face key limitations: they do not effectively teach models to prioritize correct over incorrect solutions in ambiguous situations, nor do they effectively optimize the runtime efficiency of the generated code. 
To address these challenges, we propose CodeDPO, a framework that integrates preference learning into code generation to improve two key code preference factors: code correctness and efficiency.
CodeDPO employs a novel dataset construction method, utilizing a self-generation-and-validation mechanism that simultaneously generates and evaluates code and test cases. 
The underlying assumption is that test cases executable by multiple code snippets provide more reliable validation, and code that passes more tests is more likely to be correct. 
Through this self-validation process, our PageRank-inspired algorithm iteratively updates the ranking score of each code snippet, ultimately creating a code preference optimization dataset based on correctness and efficiency.
CodeDPO is flexible and scalable, generating diverse preference optimization data without depending on external resources. 
Through comprehensive evaluations of five widely used benchmarks, CodeDPO demonstrates significant improvements in correctness and efficiency compared to existing methods. 
Our experiments prove that CodeDPO enhances the capabilities of LLMs in code generation and provides a robust foundation for conducting code preference optimization in more complex and challenging real-world scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes CodeDPO, a new framework for improving code generation models by incorporating preference learning to prioritize code correctness and efficiency. Unlike traditional methods, CodeDPO uses a self-generation-and-validation approach, generating and evaluating code with test cases to produce a dataset optimized for code preference. By iteratively ranking code snippets based on test pass rates and using a PageRank-inspired algorithm, CodeDPO enhances model performance on correctness and efficiency without external resources. Evaluations show that CodeDPO significantly outperforms existing methods.

### Strengths
1. This paper focuses on an important topic, LLM-based code generation. 
2. Experimental results show the proposed CodeDPO outperforms existing methods.

### Weaknesses
This paper should be rejected for the following reasons:
1. The paper lacks many details, and the explanations of the experiments are insufficiently clear, making it difficult to understand.
2. The paper lacks sufficient novelty and rigor; it does not explain the costs associated with the proposed algorithm.
3. The writing is unrefined and not polished.

Main Argument
First, the paper is based on a variant of DPO and applies it to the code generation domain. However, it does not provide an explanation of DPO, merely mentioning what it is, which makes it hard for readers unfamiliar with DPO to grasp the concepts. Additionally, the paper lacks clear diagrams to illustrate the workflow of the proposed strategy, which further complicates understanding.
Here are specific points I find unreasonable or imprecise in the paper:
1.In terms of correctness within code preference, the paper employs the PageRank algorithm to rank code based on the principles of PLUM, but there are no other innovations related to correctness presented in the paper.
2. The paper does not explain how the test cases in the algorithm are generated.
3. In section 3.2, the choice of 15 code solutions and test cases is mentioned, but no justification is provided for this number. Should there not be comparative experiments? Furthermore, why was a temperature of 1.5 chosen for the model?
4. Does the proposed algorithm incur significant economic costs?
5. The concept of code efficiency is quite broad. In this paper, efficiency is evaluated solely based on the execution time of test cases, which is clearly insufficient. In practical applications, code efficiency is influenced by various factors such as the production environment and tools used. Moreover, the paper does not provide adequate evidence to demonstrate that the execution time of test cases reflects code efficiency.
6. In Chapter 3, the paper should provide a detailed description of the overall process for training the code, rather than only explaining the process after SFT.
7. In Table 2, the pass rates for CODEDPO and PLUM on the more complex benchmarks MBPP and MBPP+ are similar. However, the paper does not adequately explain this point. Why are the results similar? Does this not indicate that CODEDPO does not offer significant improvement?
8. The paper does not report statistics on the average execution time of the test cases. Is the execution time in milliseconds or seconds?
9. The experimental strategy in section 5.3.1 lacks theoretical justification and is difficult to understand.
10. In section 5.3.2, what strategy was used to construct CODEKTO? Why was CODEKTO chosen for comparison, and why not compare against other PO strategies?

### Questions
See weakness, please.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents CodeDPO, a framework that improves code correctness and efficiency via direct preference optimization. To construct the preference learning datasets, CodeDPO adopts OSS-Instruct to generate code generation tasks from real-world code repositories. For each code generation task, CodeDPO prompts an LLM to generate multiple code solutions and test cases simultaneously. Since the LLM may generate incorrect solutions and test cases, the authors proposed to use the PageRank algorithm to iteratively score the code solutions and test cases based on the number of test cases each solution passes. CodeDPO further integrates code efficiency into the preference dataset by measuring the execution time of each code solution and selecting both fast and slow solutions. In the end, the authors constructed a dataset with 93K correctness optimization samples and 21K efficiency optimization samples. The authors evaluated CodeDPO on multiple LLMs and code generation datasets. The evaluation results show that CodeDPO outperformed OSS-Instruct and two similar code preference optimization methods, Code-Optimise and PLUM, in most settings. Furthermore, the authors investigated the impact of the PageRank-based scoring algorithm, the preference optimization strategies, and the dataset size.

### Strengths
1. This work presents an interesting investigation of DPO in the domain of code generation. While there have been some similar investigations like Code-Optimise and PLUM, this work involves a couple of new ideas, including the PageRank-inspired algorithm and the integration of code efficiency into the optimization objective. 

2. The authors compared CodeDPO with two similar approaches, Code-Optimise and PLUM, on multiple LLMs and code generation datasets. The results look promising.

3. The authors also did additional experiments to investigate the effectiveness of alternative design choices, such as the code solution scoring algorithm and the optimization strategy.

### Weaknesses
1. There is a potential fairness issue in the comparison with baseline methods. The finetuning dataset generated by CodeDPO includes 114K training samples in total. There is no description of the finetuning dataset sizes used in other baseline methods. For instance, if the authors used the original finetuning dataset generated by OSS-Instruct in Table 1, this would be unfair to OSS-Instruct since its dataset only includes 75K training samples. It is crucial to ensure that all methods are compared using datasets of comparable size and diversity to isolate the impact of the proposed approach. The lack of clarity on dataset sizes for baselines makes it difficult to assess the true contribution of CodeDPO.

2. This paper only describes the final dataset generated by CodeDPO, but it does not describe the initial seeds used to generate the final dataset other than vaguely saying that the initial seeds were from real-world repositories. This raises a concern about whether this dataset may include tasks similar to those of the evaluation benchmarks---HumanEval, MBPP, and DS-1000. The paper should specify the number of initial seeds, the criteria for their selection, and the process of data cleaning and decontamination to ensure the integrity of the evaluation. Simply stating that the seeds are from real-world repositories is insufficient.

3. The evaluation results in Table 2 and Table 3 are not complete. Table 2 does not report the performance of PLUM for MagiCoder-CL-7B, Phi-2-2.7B, and DeepSeekCoder-1.3B. Table 3 does not report the performance of Code-Optimise and PLUM on DS-1000. Figure 3 only code efficiency results on HumanEval and MBPP, but not on DS-1000. The absence of these results makes it hard to fully assess the generalizability of CodeDPO across different models and datasets. A comprehensive evaluation should include all models and datasets for all methods.

4. The design of the PageRank-based scoring algorithm has an issue when scoring test cases. According to Equation 2, if many code solutions pass a test case, the test case will receive a high score. As a result, many weak test cases will receive high scores. For example, if a test case does not check any requirement mentioned in the task description (e.g., "assert true" as an extreme case), this test case will receive a very high score and will be included in the training set. This could lead to the model being trained on low-quality test cases, potentially hindering its performance.

5. The evaluation baselines used in RQ3 are weak. CodeT (Chen et al. 2022) uses a dual execution agreement algorithm to rate the correctness of the code solutions and test cases simultaneously generated by CodeT. PLUM uses a self-consistency filtering mechanism to select test cases and code solutions. It is unclear what the advantages of the PageRank-based algorithm are compared with these two SOTA methods. The paper should provide a more detailed comparison of the PageRank-based algorithm with these existing methods, highlighting its specific advantages and limitations.

6. This paper makes several incorrect claims about existing work. First, Section 3.1 says OSS-Instruct extacts key programming concepts from open-source projects and leverages these concepts to generate programming tasks. OSS-Instruct doesn't perform any extraction of program concepts. It directly generates a task description from code fragments in open-source projects. Second, Section 2.2 claims that PLUM generates a limited number of test cases and has an imbalanced dataset. This claim seems unsubstantiated. There is no evaluation of the test cases generated by CodeDPO vs. PLUM. Furthermore, the self-consistency filtering mechanism used in PLUM also looks reasonable. Third, the authors claim that CodeDPO "does not rely on external resources" several times. This sounds wrong since CodeDPO needs to select initial seeds from real-world repositories to generate the finetuning dataset.

7. None of the code generation datasets used in this evaluation are designed for code efficiency. The authors should evaluate CodeDPO on a code efficiency dataset like EffiBench (NeurIPS 2024). https://github.com/huangd1999/EffiBench

### Questions
1. Can you report the number of training samples used in OSS-Instruct, Code-Optimise, and PLUM?

2. Can you elaborate on how the real-world repositories were selected to construct the initial seeds for data generation? Did you perform any data cleaning and decontamination when curating the dataset?

3. Can you report the performance of PLUM for MagiCoder-CL-7B, Phi-2-2.7B, and DeepSeekCoder-1.3B in Table 2? Can you also report the performance of Code-Optimise and PLUM on DS-1000 in Table 3 and the code efficiency results on DS-1000 in Figure 3?

4. Can you compare your PageRank-based algorithm with the scoring algorithms used in CodeT and PLUM?

5. Step 2 in Figure 2 is hard to understand. The authors should redraw that part to illustrate the iterative scoring process.

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
The paper describes CodeDPO, a framework developed to improve code generation models by incorporating preference learning to prioritize both code correctness and efficiency. CodeDPO generates a dataset through a self-generation-and-validation mechanism, where code snippets and test cases are created and iteratively ranked based on performance. Evaluations on five coding benchmarks indicate that CodeDPO offers improvements in model alignment for code correctness and efficiency over existing approaches, providing a dataset that can be used to optimize various code generation models in realistic scenarios.

### Strengths
+ The paper trains a code generation model with DPO with several pre-trained checkpoints, illustrating the effectiveness of functional-correctness-driven DPO for code generation.
+ The paper proposes a handful of research questions to evaluate CodeDPO on varied benchmarks and compare with multiple baselines

### Weaknesses
__Few Novel Ideas Proposed and Few New Insights Concluded.__

The idea of trying DPO for code generation seems to be an intuitive combination for post-SFT phases of training, and such a combination has been tried in varied domains including code. For example, in the latest technical report of Llama-3.1, DPO has become the main algorithm for preference optimization, where they have empirically illustrated DPO's effectiveness in coding, math, natural language understanding, etc. Besides, Llama-3.1 also revealed that DPO has more stable scalability across 8B to 405B than on-policy algorithms, such as PPO. The point I hope to make here is that the effectiveness of DPO on code, as well as other data modalities, has been comprehensively studied and effectively applied to the product-level code LMs. The conclusion that training with SFT+DPO is more effective than SFT only, which is the main observation of CodeDPO, seems obvious nowadays, restricting the value of this paper alone.

The other techniques applied in this work also seem to be very mature and proved to be practical and effective already. For example, the idea of seeding realistic code and sampling synthetic coding problems + solutions using teacher LLM has been well-studied in pioneer work, such as WizardCoder and MagiCoder, and this technique turns out to be very effective and has been used by industry models, including Llama-3.1, Gemma, CodeGemma, Gemini-1.5, etc. Also, the code correctness scoring with LLM-generated tests seems very similar to related work like CodeT[1], and the iterative pipeline has become a popular strategy since the proposal of the Self-Debugging paper[2].

The new thing I noticed is maybe, considering the efficiency of code execution, this perspective has not been soundly studied regarding its standalone effects on other features, like code correctness and helpfulness, so it is not clear how important we should include this feature during DPO. I would encourage the authors to study this new feature in a controlled and isolated way, but this is just a minor suggestion.

Overall, I feel this paper is more of a proof-of-concept implementation of ideas that have been proven to be practically effective. Therefore, unfortunately, I feel the conceptual novelty and the scientific values in terms of new insights concluded from this paper alone are unsatisfactory for top venues like ICLR. However, I still encourage the authors to join the discussion during the rebuttal phase to clarify their novelty and new insights that have __not__ been revealed by the existing works that I might have missed during the review.

__Restricted Evaluation Setting__

All the evaluation settings are still restricted to simple benchmarks like EvalPlus and DS-1000. I am not sure how this simplified code generation setting with the most straightforward reward design might work in more challenging programming tasks, such as repository-level code completion or competition-level programming problems. 

Intuitively, a very capable policy model is the prerequisite for applying preference optimization or RL, and that might be why we could always see DPO/PPO providing additional value on top of HumanEval and MBPP. However, it is unclear but interesting to check that, if the LLM after SFT is not yet promising in the task (e.g., Magicoder reports 70+ accuracy in HumanEval while <30% accuracy in LiveCodeBench), whether DPO could still bring them a significant improvement, or it will hurt the model performance instead. I would encourage the authors to evaluate their model on the latest benchmarks, such as LiveCodeBench[3] and R2E[4].

### Questions
- Could the authors illustrate a bit more what are the main novelties of this work, beyond the combination of implementing existing ideas (See weaknesses)? This will help me better understand the additional value and contribution this work provides to the community, which I might have missed. A better understanding could significantly change my attitude towards this paper.
- Could the author discuss why their results using DPO and KTO contradict with those reported in PLUM? PLUM and CodeDPO have completely opposite conclusions about using DPO and KTO to train code generation models, and it is very confusing which algorithms are more suitable for learning preference with execution feedback and why. I would regard a systematic discussion to deeply understand this perspective as an interesting contribution. Unfortunately, neither PLUM nor CodeDPO provides sufficient discussion on it.
- Can the author provide some thoughts on, besides the straightforward execution signal we can get from the interpreter (e.g., execution correctness and efficiency), what other information can be used to improve the helpfulness, readability, and security of code? Since the test-case-driven functional correctness DPO has been studied by the existing work, it will be interesting to see more insights into the future work of DPO on code.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes self generation of code solutions and tests, and cross-verify the code and tests via a pagerank-inspired algorithm.

### Strengths
The proposed method alleviates the problem of wrong tests when using LLMs generated tests, and the data generation does not require a strong teacher LLM. The page-rank-like algorithm is interesting. Extensive experiments have been conducted to show the effectiveness of the approach, and a number of ablation studies have been conducted to showcase the correlation with groundtruth, impact of different preference optimization method and data scaling.

### Weaknesses
I do not see strong weakness of the paper.
Some section of the paper lack sufficient details. For example, since the correctness score is no longer 0 and 1, the creation of pairs is not that straightforward. Do you pick the highest score code snippet with the lowest score one to form the pair, or is it another way?

### Questions
- Have you performed deduplication of the dataset against the benchmarks? The dataset leakage could be an issue.
- The creation of DPO pairs for correctness and effeciency lack sufficient details. Since the correctness score is no longer 0 and 1, the creation of pairs is not that straightforward. Do you pick the highest score code snippet with the lowest score one to form the pair, or is it another way?
- In table 2, MagiCoder-DS-6.7B, CodeDPO is performing significantly worse than PLUM on HumanEval/HumanEval+. This result is different from the rest of the results. Do you have an explanation?
- In table 4, the correlation analysis is interesting. Do you have access to the unit tests generated from GPT-4 from PLUM? Could you evaluate the correlation of "filter all tests" with these more trustworthy tests from the stronger model?
- In table 6, KTO results are often worse than SFT results. Do you have an explanation for the phenomenon? Is it KTO training just not that good or is it your KTO training is problematic?

### Soundness
3

### Presentation
3

### Contribution
3
