# Dynamic Gradient Alignment for Online Data Mixing

- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 5, 5, 6, 5

## Abstract
The composition of training data mixtures is critical for effectively training large language models (LLMs), as it directly impacts their performance on downstream tasks. Our goal is to identify an optimal data mixture to specialize an LLM for a specific task with access to only a few examples. Traditional approaches to this problem include ad-hoc reweighting methods, importance sampling, and gradient alignment techniques.
This paper focuses on gradient alignment and introduces Dynamic Gradient Alignment (DGA), a scalable online gradient alignment algorithm. DGA dynamically estimates the pre-training data mixture on which the models' gradients align as well as possible with those of the model on the specific task.
DGA is the first gradient alignment approach that incurs minimal overhead compared to standard pre-training and outputs a competitive model, eliminating the need for retraining the model. Experimentally, we demonstrate significant improvements over importance sampling in two key scenarios: (i) when the pre-training set is small and importance sampling overfits due to limited data; and (ii) when there is insufficient specialized data, trapping importance sampling on narrow pockets of data.
Our findings underscore the effectiveness of gradient alignment methods in optimizing training data mixtures, particularly in data-constrained environments, and offer a practical solution for enhancing LLM performance on specific tasks with limited data availability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes Dynamic Gradient Alignment (DGA), an online domain reweighting approach for the purpose of identifying an optimal data mixture for training an LLM for a downstream task with access to only a few examples (denoted specialized set).  DGA estimates stepwise optimal domain weights during model training.  The traditional importance sampling approaches suffer from some limitations, such as overfitting into small-scale pretraining data in each domain, difficulty to handle large domain granularity, and easily trapping into quite suboptimal local optimum with limited specialized set. The authors empirically show that DGA alleviates these limitations, offers an effective approach for optimizing training data mixture for downstream tasks with limited specialized set.

### Strengths
(1)	The proposed DGA shows advantages over traditional importance sampling approaches in two challenging scenarios, that is, the number of training samples in each domain is limited instead of the unrealistic assumption of unlimited number of tokens, and the domain granularity is quite large making traditional domain reweighting methods cause intractable computational overheads.

(2)	The paper proposed two major innovations in DGA, including incorporating EMA term into domain reweighting to mitigate overfitting and improve stability, and also introducing a distribution reweighting scheme, with the number of distributions smaller than the number of domains, for scaling up to very fine-grained domains (very large number of domains). Though DGA is built upon DoGE, the differentiators from DGA over DoGE are clearly explained in the paper, as the lower variance, smaller overhead, and the novel EMA in DGA, compared to DoGE.

(3) Overall, the paper is clearly written. The Appendix provides useful additional results for the two challenging scenarios, hyperparameter information, and algorithm details.

### Weaknesses
 (1)	For empirical validations, the paper used Redpajama-v2 as the pre-training data, which has 30T tokens after filtering and deduplication. This is non-trivial amount of data. However, the paper pre-trained models with 125M, 350M, and 750M number of parameters. In comparison, some SOTA LLMs are trained on smaller or comparable amount of data with much larger model sizes, for example, Llama 3 405B trained on 15.6T tokens, QWen2.5-8B trained on 18T tokens, OpenLLaMA 3B, 7B, and 13B trained on 1T tokens, etc. The model sizes explored in this paper may be too small and too limited model capacity to sufficiently learn from 30T tokens data. It would be useful to pre-train models with larger sizes, e.g., to 3B and 7B, which will correspondingly impact the experimental results and analysis.  A related question is, why not use OpenLLaMA setup including its open-source data for the experiments?

(2)	Figure 1 analyzes the effect of DGA and DGA with EMA. However, 30M tokens/domain are still quite large. How about the comparison when the number of tokens/domain is further reduced, e.g., less than 1M, less than 100K, 10K?

(3)	One critical question when adapting pre-trained LLM for downstream tasks is how much the resulting model can achieve a good balance between general capabilities and performance on downstream tasks. For example, for instruction following capabilities on a downstream task, how much the model can perform for general instruction following tasks with DGA compared to the baselines. This issue of catastrophic forgetting has not been discussed in the paper.

### Questions
(1)	Please address the points listed under Weaknesses.

(2)	There are some typos and grammar errors in the paper. For example, “obtain obtain”.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a novel pre-training data mixing method, called DGA, which enables LLMs to adapt to downstream tasks with just a few examples. By alternately updating model parameters and domain weights, DGA achieves exploration and exploitation on the training data, thereby solving the overfitting problems of importance sampling. DGA provides an approach for the data mixing problem in pre-training for specific downstream tasks. Additionally, the authors validated their method on the Pile and MMLU datasets, demonstrating DGA’s effectiveness in language modeling for downstream tasks.

### Strengths
1,DGA effectively addresses the overfitting issue of importance sampling in scenarios with limited data.

2, By incorporating the EMA term, DGA effectively addresses the issue of training instability.

3, By combining with importance sampling, DGA resolves the issue of "scaling linearly with the number of domains k". Even when there are a large number of domains, it can also demonstrate its advantages.

### Weaknesses
1, DGA's reasoning accuracy on datasets like MMLU is not good, but the authors only emphasize that DGA has strong capabilities in language modeling. The performance on downstream tasks should be related to reasoning accuracy, rather than the capability of language modeling.

2, The authors did not compare the performance differences between DGA and other methods under the paradigm of pre-training + fine-tuning or pre-training + ICL, but LLMs typically adapt to downstream tasks using these paradigms, which significantly differs from actual usage scenarios.

### Questions
1, How would DGA perform under the paradigms of pre-training + fine-tuning or pre-training + ICL?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Dynamic Gradient Alignment (DGA) as a stable and scalable data mixing method for LLM pretraining to address two key challenges of online domain reweighting. DGA is an online algorithm that adjusts the training data distribution according to the current model status, relying on gradient alignments to estimate progress on the target task. The paper demonstrates that DGA with EMA can significantly mitigate overfitting and yield superior performance on the end-task by balancing exploitation and exploration under limited tokens within generic domains. Additionally, a novel distribution reweighting strategy is proposed, enabling DGA to scale up to extremely fine-grained data domains without incurring intensive computations. Experiments on MMLU show that DGA effectively leverages fine-grained domain knowledge to balance specialty and diversity during training, demonstrating the scalability and efficiency of gradient-alignment-based data reweighting methods in data-constrained settings.

### Strengths
1. The paper introduces Dynamic Gradient Alignment (DGA), a novel online gradient alignment algorithm that dynamically adjusts training data mixtures.
2. The experiments are well-designed, covering key scenarios of small pretraining sets and insufficient specialized data, using the MMLU benchmark.
3. The results clearly demonstrate the advantages of DGA over importance sampling and uniform baselines, with detailed analysis of different model scales and domain granularities

### Weaknesses
1. The paper provides a brief description of the theoretical foundation of DGA, lacking in-depth mathematical derivation and theoretical analysis. There is no rigorous proof of convergence and stability for DGA, which raises concerns about the robustness and reliability of the proposed method. Specifically, the paper does not provide a clear formulation of the optimization problem being solved by DGA, nor does it analyze the properties of the gradient alignment metric used to guide data mixing. This lack of theoretical grounding makes it difficult to understand why DGA works and when it might fail.
2. The paper does not compare DGA with other advanced domain reweighting methods. This omission makes it difficult to assess the relative performance and advantages of DGA compared to existing methods. For example, methods that use meta-learning or reinforcement learning to optimize data mixing strategies are not considered, leaving a gap in the evaluation of DGA's novelty and effectiveness.
3. Benchmarking against other methods is essential to establish the novelty and superiority of the proposed approach. The absence of such comparisons weakens the paper's contribution to the field. Without a direct comparison to state-of-the-art techniques, it is hard to determine if the improvements observed with DGA are significant or simply due to the specific experimental setup.
4. The paper lacks a detailed complexity analysis of the experiments, particularly in Section 3.2. A thorough analysis of the computational complexity and resource requirements would provide better insights into the practical implications of implementing DGA. Specifically, the paper does not discuss the time and memory complexity of computing gradient alignments, nor does it analyze how these complexities scale with the number of domains and the size of the model. This is crucial for understanding the practical applicability of DGA in resource-constrained settings.
5. The paper does not provide a comprehensive analysis of the impact of different hyperparameters on the performance of DGA. Understanding how sensitive DGA is to various hyperparameters is important for its practical implementation and optimization. For instance, the learning rate for the domain weights, the frequency of reweighting, and the smoothing factor for the EMA are all important parameters that need to be carefully tuned, but the paper does not provide sufficient guidance on how to choose these values.

### Questions
1. Can you provide more mathematical derivation and theoretical analysis of DGA, including proofs of convergence and stability? This would help in understanding the robustness and reliability of the proposed method.
2. How does DGA compare with other advanced domain reweighting methods (e.g., DoGE)? A detailed comparison would help in understanding the relative advantages and limitations of DGA.
3. Can you provide a detailed complexity analysis of the experiments in Section 3.2?
When k is much larger than T_r, 1) is DGA much more complicated than importance sampling method and 2) no better than DoGE in terms of both performance and complexity? Understanding the computational complexity and resource requirements is crucial for evaluating the practical implications of implementing DGA.
4. Can you provide a comprehensive analysis of the impact of different hyperparameters on the performance of DGA? Such ablation study is important for practical implementation and optimization.
5. In Table 1, DGA does not show significant improvement above importance sampling. However, DGA is much more complicated under this experiment setting?
6. Do you have more benchmarking results against other methods? it is essential to establish the novelty and superiority of the proposed approach.
7. In experiments section, there should be a comparison between DGA and DoGE in terms of performance and computational complexity? As DGA is heavily inspired by DoGE, a detailed comparison would provide insights into the relative strengths and weaknesses of both methods.
8. How does DGA perform across different model scales? Can you provide more detailed results and analysis for various model sizes to understand its scalability and effectiveness?
9. What are the potential directions for future work and improvements on DGA? Are there any planned extensions or enhancements to address the current limitations and expand its applicability?

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
The submission proposes a new method to improve training of LLMs on datasets that have an increased diversity / size ratio, e.g. mix of many small datasets. The method is a combination of increased (local) adaptability via dynamic gradient alignment (DGA) and smoothing via a moving average (EMA). Results report effects on training loss and accuracy in comparison to prior art of "Importance Sampling" with the same target.

### Strengths
The submission is well-written and a good mixture of motivation, analysis of previous work, detailing theoretic foundations, experimental verification and conclusions.

### Weaknesses
Experimental results only show loss, but no accuracy improvements over Importance Sampling (Table 1). Tables 2 & 3 also show no consistency in the pattern of first and second best of the compared approaches and alternating "wins" by tiny margins. This suggests that the proposed technique is just possibly only an alternative to Importance Sampling.

Initially, I had some issues correctly understanding the term "online" in the name of the proposed technique. Similar to me it may mislead other readers to think that this postpones the mixing to inference time (that would be an awesome new result), but it clearly doesn't.

A slight weakness lies in the fact that the technique is based on the assumption of LLMs being trained via gradients. This limits applicability to the current state-of-the-art. In contrast, most sampling techniques are more generally applicable.

Lines 067-069 ("Since the domain weights... leads to snow-balled errors."): this claim is vague and should be verified by experiment(s). Or did I miss that (maybe Figure 1(a)? Can you please add clarity to this?

### Questions
Lines 067-069 ("Since the domain weights... leads to snow-balled errors."): this claim is vague and should be verified by experiment(s). Or did I miss that (maybe Figure 1(a)? Can you please add clarity to this?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Dynamic Gradient Alignment (DGA), an online data reweighting algorithm aimed at optimizing data mixtures for training large language models (LLMs) on specific tasks. Unlike static or previously established gradient-alignment methods, DGA dynamically updates domain weights during training by aligning model gradients on the target task, leading to improved performance and reduced overfitting, especially in data-constrained environments. The method is scalable, incurs minimal computational overhead, and leverages exponential moving averages (EMA) for stabilizing updates.

### Strengths
- **Innovative Approach**: The paper presents DGA as an online, scalable alternative to existing domain reweighting methods, offering significant advantages in flexibility and adaptability.
- **Empirical Evidence**: Detailed experiments show DGA's effectiveness compared to importance sampling, particularly under token-constrained conditions and fine-grained data domains.
- **Theoretical Rationale**: The method is well-anchored in optimization principles, connecting gradient alignment and bilevel optimization frameworks.
- **Practical Relevance**: DGA demonstrates strong utility for real-world data scenarios with limited resources, showcasing improved balance between exploration and exploitation in domain weighting.

### Weaknesses
 - **Theoretical Assumptions**: While the approach connects well to optimization theories, the convergence proofs are limited due to non-convexity in practice. The lack of a robust convergence analysis, especially in the context of highly non-convex loss landscapes common in deep learning, raises questions about the method's behavior in diverse training scenarios. The reliance on empirical validation without a strong theoretical guarantee is a significant limitation.
- **Specificity vs. Generality**: The results on downstream reasoning (MMLU) indicate that while DGA improves language modeling, the gains do not always translate to enhanced reasoning capabilities, suggesting potential limits in generalizability. The discrepancy between language modeling improvements and downstream task performance highlights a potential disconnect between the optimization objective and the desired generalization properties. The method's effectiveness may be highly task-specific, limiting its applicability across a broad range of NLP tasks.
- **Sparse Baseline Comparisons**: The paper could benefit from more varied baseline methods beyond standard importance sampling to contextualize DGA's performance. The current comparison set may not fully capture the landscape of existing data reweighting techniques, making it difficult to assess the true novelty and effectiveness of DGA. A more comprehensive comparison with other state-of-the-art methods is needed.
- **Stability Under Extreme Data Constraints**: Although EMA helps with stability, the paper notes challenges when DGA operates without it, implying potential reliability issues under certain configurations. The sensitivity of DGA to the presence of EMA suggests a potential fragility in the algorithm's core design. The lack of robustness under different configurations raises concerns about its practical applicability in real-world scenarios where hyperparameter tuning may be challenging.

### Questions
- Can the authors provide insights on the performance of DGA on tasks beyond language modeling to substantiate its generalization claims?
- What are the primary factors influencing DGA's stability when EMA is not used?
- Are there any plans to explore hybrid approaches combining DGA with more computationally intensive, sample-level methods?

### Soundness
3

### Presentation
3

### Contribution
3
