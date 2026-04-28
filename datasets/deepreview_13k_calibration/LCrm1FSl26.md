# Towards Efficient Adaptation of Pruning Strategy in Large Language Models

- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 8, 8, 3, 3

## Abstract
Post-training pruning has gained increasing attention with the rapid growth of large language models (LLMs). However, significant variations in weight distributions across different LLMs make a fixed pruning strategy inadequate for multiple models. In this paper, we propose an efficient evolutionary optimization framework, \textbf{Mecon}, for adaptive LLM pruning. In particular, we design an effective search space built on our \textbf{Me}ta pruning metric to mitigate diverse weight distributions among LLMs. We then introduce model-wise re\textbf{con}struction error, a lightweight search evaluation to speed up the evaluation of each search trial. We finally leverage Non-dominated Sorting Genetic Algorithm III (NSGA-III) as our search algorithm, handling both the single-objective problem of pruning metric search and the multi-objective problem of layerwise sparsity ratio search in discovering the optimal pruning strategy. We extensively evaluate our framework on LLaMA-1/2/3 and Mistral models across multiple benchmarks. Our results demonstrate that our adaptive pruning metrics consistently outperform existing ones, and the layerwise sparsity ratios improve the effectiveness of other pruning metrics. Furthermore, we validate the cross-task and cross-model generalizability of our pruning metrics, offering a cost-effective solution to streamline the search process. We release our code in the anonymous repository: \textcolor{blue}{\url{https://anonymous.4open.science/r/Mecon-5819}}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper argues there is significant variations in weight distributions across different LLMs, which make it unable to use a fixed pruning strategy for multiple models. Author further propose their framework which first search a pruning metric based on evolutionary optimization and then use Non-dominated Sorting Genetic Algorithm III which search layerwise sparsity ratio to find optimal pruning strategy. Experiments on 4 7B-level models show great improvements over related works.

### Strengths
1. This paper provides insights on diverse wieght distribution of different models which would cause unstable performance for one fixed pruning strategy. And further propose their method for adaptive LLM pruning.
2. Experiments are quite solid with analysis, four 7B models show notable improvements over baselines on 9 tasks.

### Weaknesses
1. It is better to provide reference for Non-dominated Sorting Genetic Algorithm III in introduction (e.g. line 76)

### Questions
1. Is there any insights on why this method show great improvments on 7B level models but negligible improvments on 30B/70B model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents an adaptive and efficient pruning method for large language models (LLMs) within the framework of post-training pruning. It includes a meta pruning metric search, layerwise sparsity ratio search, and introduces a new search evaluation metric: model-wise reconstruction error. The authors first validate and highlight the suboptimal generalization performance of existing methods across different models, analyzing the underlying causes. They propose an adaptive pruning strategy tailored for various LLMs, optimizing both the pruning metric and the layerwise sparsity ratios.

In response to the time-consuming nature and poor task generalization of using perplexity as the evaluation measure under the SEARCH EVALUATION, the authors introduce the model-wise reconstruction error metric. This metric directly measures the difference between the output layers before and after pruning using the Frobenius norm, providing a more direct and effective assessment. Furthermore, the paper employs a unified NSGA-III algorithm to efficiently address both single and multi-objective search problems across the two phases.

In the experimental section, the study conducts comprehensive testing to verify the robustness and superiority of the proposed method under different models, tasks, and parameter requirements, accompanied by an in-depth analysis.

### Strengths
1. The scientific problem addressed in this paper is highly significant. The development of efficient and robust pruning methods within the post-training paradigm has broad applications in the AI community. The authors provide a rigorous validation and analysis of the issues at hand.

2. The methodology presented in this paper is comprehensive, including well-designed solutions to key scientific questions such as pruning metric search, subsequent layerwise sparsity ratio search, and optimization of evaluation metrics. The experiments are solid, the logic is clear, and the paper progressively deepens the discussion, rigorously demonstrating advancements in robustness and effectiveness.

3. The writing is logically structured and clearly articulated, effectively presenting the logical flow of the methodology, the importance of the experiments, and the distinctions and improvements compared to related works in the field.

### Weaknesses
1. Regarding the insufficient generalization performance of current methods across different models, while the pruning metric search presented in this paper shows promising improvements based on experimental results, I find the design of the meta metric and the candidate options in the search space somewhat confusing. Furthermore, I did not see the underlying logic and theoretical support for the pruning metric search.

2. According to the framework of this paper, the pruning metrics from similar methods can be viewed as a special case of the proposed meta metric. I am curious about the resource consumption-effectiveness curve when searching within a potentially smaller search space under similar methods with specific coefficients (α, β). It raises the question of whether simple coefficient tuning within this method could yield satisfactory results.

### Questions
As mentioned in the above weaknesses.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The author proposed a meta-pruning algorithm that uses evolutionary search algorithm to automatically find the right combination of pruning heuristics and sparsity ratio. This work is very novel, the experiment protocol seems rigorous and the results look solid.

### Strengths
- Casting the LLM pruning problem as a meta problem is novel and thought-provoking.
- Very strong evaluation protocol — this work includes comprehensive task evaluation plus end-to-end speedup evaluation.
- Paper is well written and easy to follow.

### Weaknesses
 - No obvious weakness.

### Questions
- What are the most important pruning metrics? I’m looking for a high-level interpretation of your A.2 results.
- As a follow-up, wonder if the optimal searched pruning configuration can shed any light on why SparseGPT/Wanda performed so poorly on some models?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
To address the issue of fixed pruning strategies being unable to adapt to multiple different models, the authors propose an adaptive evolutionary framework for LLMs pruning. Specifically, they introduce designated search spaces for the pruning strategy and layerwise sparsity ratios, aiming to find an optimal pruning method based on model reconstruction loss and sparsity ratio discrepancy. The search algorithm used is the Non-dominated Sorting Genetic Algorithm III (NSGA-III). Additionally, the authors conducted extensive experiments to demonstrate the effectiveness of the proposed method.

### Strengths
1 . The paper designed an effective search space built on our meta pruning metric to mitigate diverse weight distributions among LLMs.
2. The authors leverage Non-dominated Sorting Genetic Algorithm III (NSGA-III) as the search algorithm.

### Weaknesses
1. The motivation of this paper is unclear. Although the authors mentioned that the existing fixed pruning methods cannot adapt to models with different weight distributions (such as Llama-2 and Llama-3), they did not explain the underlying reasons for this. Specifically, Figure 1 only shows that different pruning methods have different performance on models with different weight distributions, but does not analyze the specific reasons from a theoretical perspective. The paper lacks a rigorous analysis of why existing pruning metrics fail to generalize across different model architectures and training regimes. For example, it does not delve into the mathematical properties of the weight distributions or the activation patterns that might cause these discrepancies. A more in-depth analysis, perhaps using tools from statistical analysis or information theory, would be necessary to strengthen the motivation.
2. I believe the overhead introduced by the search algorithm in the proposed method is non-negligible.  the author compressed the search time to an acceptable range by restricting the search space to a limited discrete space. However, the paper does not provide a detailed analysis of the computational cost associated with the search process. While limiting the search space reduces the time, it also potentially limits the optimality of the solution. A more thorough discussion of the trade-offs between search space size, computational cost, and solution quality is needed. Furthermore, the paper does not discuss the sensitivity of the search process to hyperparameter settings, such as population size and number of generations, which could significantly impact the search time and the quality of the found pruning strategy.
3. This paper lacks innovation and is a combination of existing work. The proposed work and Pruner-Zero[1] are not highly distinguishable, and the extended search pruning rate is also the existing work of CV. The paper does not adequately differentiate itself from Pruner-Zero [1]. Both methods employ a search-based approach to find pruning strategies. The paper needs to highlight the key differences in the search space, the search algorithm, and the evaluation metric. The paper also needs to address the concern that extending the search to layer-wise sparsity ratios is not novel, as this has been explored in prior work in computer vision. A more detailed comparison with existing work, highlighting the unique contributions of this paper, is necessary.

### Questions
1. Why didn't the authors conduct experiments on models other than LLaMA and Mistral?
2. Did the authors consider a more general representation to model the relationship between weights and activations?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
1. The paper presents MECON, an evolutionary optimization framework designed for adaptive pruning of large language models (LLMs). Recognizing that fixed pruning strategies are ineffective due to the diverse weight distributions across LLMs, the authors develop a Meta pruning metric and an efficient search space to address this challenge. 

2. The framework utilizes model-wise reconstruction error as a fast evaluation method and employs the NSGA-III algorithm to optimize both single-objective and multi-objective pruning problems. Extensive experiments on various LLaMA and Mistral models show that MECON's adaptive pruning approach outperforms existing methods, improves pruning efficiency, and demonstrates cross-task and cross-model generalizability.

### Strengths
1. The paper is clearly written and free of obvious typos.
2. The proposed evolutionary computation-based algorithm for searching hyperparameters in large model pruning is tested on well-known models such as LLaMA-1/2/3 and Mistral, as well as on datasets like WikiText, GSM8K, and MMLU.
3. The authors conduct an ablation study on the evolutionary computation algorithm used, attempting to justify the choice of Non-dominated Sorting Genetic Algorithm III (NSGA-III) as their search algorithm.

### Weaknesses
1.  The most critical issue with this paper is the lack of testing for the algorithm's efficiency. The authors only evaluate the accuracy under unstructured and semi-structured (N: M) pruning with a 50% mask compression rate across various datasets but do not provide results on memory efficiency or latency in GPU-CPU collaborative scenarios. Without these efficiency metrics, especially for unstructured pruning, it is unclear whether the method can be applied in real-world scenarios. Specifically, the paper lacks concrete measurements of inference time, memory footprint reduction, and energy consumption, which are crucial for assessing the practical viability of any pruning technique, particularly unstructured pruning which often suffers from irregular memory access patterns.

2. The paper only tests and compares baselines at a 50% compression rate and does not explore other extreme compression rates, such as below 50%. This limits the understanding of the algorithm's behavior under more aggressive pruning scenarios, where the trade-off between accuracy and compression becomes more critical. The absence of results at lower compression rates leaves open the question of whether the method can maintain acceptable performance when pushed to its limits.

3. The datasets used to validate the algorithm are limited, as testing is only conducted on GSM8K, MMLU, and WikiText. It would be beneficial to evaluate the model's generalizability on a broader range of datasets, such as those from the lm-evaluation-harness library. The current selection of datasets does not fully represent the diversity of tasks and data distributions that LLMs are expected to handle, thus limiting the conclusions that can be drawn about the method's robustness.

4. The performance improvement of the algorithm appears marginal on some datasets and models. For instance, in Table-2, MECON achieves a score of 63.51 on the Mistral model, while the simpler Magnitude pruning achieves 63.34. This minor gain does not justify the significantly higher time and complexity involved in MECON’s search and pruning process compared to straightforward methods like Magnitude pruning. The small performance gains raise concerns about the practical utility of the method, especially considering the added computational overhead.

5. Some relevant works on compression of LLMs using search algorithms/NAS methods are not mentioned or compared in the paper, such as: 
[1] Pruning Large Language Models via Accuracy Predictor.
[2] Tune As You Scale: Hyperparameter Optimization For Compute Efficient Training.

### Questions
1. Can the authors conduct efficiency testing experiments?

2. Can the authors perform experiments at other compression rates?

3. Can the authors provide additional dataset evaluations to demonstrate the algorithm’s generalizability? Given that post-training algorithms typically do not consume significant computational resources or time, this should be feasible.

### Soundness
2

### Presentation
2

### Contribution
1
