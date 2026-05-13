# ROPO: Robust Preference Optimization for Large Language Models

- Decision: Reject
- Scores: 5, 6, 6

## Abstract
Preference alignment is pivotal for empowering large language models (LLMs) to generate helpful and harmless responses.
    However, the performance of preference alignment is highly sensitive to the prevalent noise in the preference data.
    Recent efforts for this problem either marginally alleviate the impact of noise without the ability to actually reduce its presence, or rely on costly teacher LLMs prone to reward misgeneralization.
    To address these challenges, we propose the \textbf{RO}bust \textbf{P}reference \textbf{O}ptimization (\textbf{ROPO}) framework, an iterative alignment approach that integrates \textit{noise-tolerance} and \textit{filtering of noisy samples} without the aid of external models.
    Specifically, ROPO iteratively solves a constrained optimization problem, where we dynamically assign a quality-aware weight for each sample and constrain the sum of the weights to the number of samples we intend to retain.
    For noise-tolerant training and effective noise identification, we derive a robust loss by suppressing the gradients of samples with high uncertainty.
    We demonstrate both empirically and theoretically that the derived loss is critical for distinguishing noisy samples from clean ones.
    Furthermore, inspired by our derived loss, we propose a robustness-guided rejection sampling technique to compensate for the potential important information in discarded queries.
    Experiments on three widely-used datasets with Mistral-7B and Llama-2-7B demonstrate that ROPO significantly outperforms existing preference alignment methods, with its superiority growing as the noise rate increases.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper studies preference alignment under the condition when there are poorly-annotated preference pairs. The authors propose a robust preference optimization (ROPO) framework with two key considerations, (1) a noise-robust loss function that suppresses the gradients of samples that the policy model is uncertain about; (2) A robustness-guided rejection sampling technique designed to balance the filtering of noisy samples with the preservation of important information from queries that might otherwise be discarded.

In the experiments, the authors demonstrate that the policy model aligned with ROPO shows the least drop in performance (win rate against a reference model as judged by GPT-4) with an increasing proportion of injected noise in the training data. The injected noise includes both artificial noise, such as flipping the preference labels of training pairs, and practical noise, where responses from a larger model are blindly assumed to be preferred over those from a smaller model.

### Strengths
1. The paper presents a well-motivated study on addressing annotator noise in preference alignment, an issue that is critical for developing reliable policy models.

2. The paper provides a thorough and sensible theoretical analysis of DPO's limitations in discriminating between noisy and clean samples. It also demonstrates how the addition of a regularization loss helps mitigate these issues.

### Weaknesses
1. Limited test datasets. Performance evaluation is only conducted on AlpacaEval and the test split of Reddit TL;DR, lack of comprehensive results on multiple instruction-following / alignment benchmarks, such as Wildbench, Arena-Hard, MT-Bench, etc.

2. The paper consider using loss values to identify model-uncertain samples in the robustness-guided rejection sampling procedure as a major contribution. Yet, there has already been several related works, like [1].

[1] Secrets of RLHF in Large Language Models Part II: Reward Modeling.

3. Lack of human evaluation. The analysis is based on GPT-4, which can be biased in its evaluation.

### Questions
(1) Only one type of practical noise is considered in the paper, specifically, the assumption that annotators inherently favor outputs from larger models over those from smaller ones. What are other type of practical noises? 

(2) The authors mention ROPO is an iterative alignment approach. How the iterative process takes place? It is unclear based on the methodology descriptions in the paper. The authors may provide a detailed algorithm sketch to describe the iterative process.

### Soundness
2

### Presentation
3

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
This paper introduces the RObust Preference Optimization (ROPO) framework, a method designed to improve preference alignment in large language models (LLMs) by addressing the challenges posed by noisy preference data. ROPO employs a noise-tolerant loss function and an iterative process that integrates noise filtering during training. Additionally, ROPO includes a robustness-guided rejection sampling technique to retain valuable data while filtering noise. Experiments show that ROPO outperforms existing methods under various noisy conditions, offering a scalable and effective approach to aligning LLMs with human preferences without the need for external models.

### Strengths
1. An iterative training approach that optimizes LLM performance while filtering out noisy samples.
2. Experimental results demonstrate improvements over DPO.
3. The use of rejection sampling effectively compensates for information lost during the noise filtering step.

### Weaknesses
1. While the paper addresses the impact of noisy data, it lacks a clear definition or characterization of what constitutes noisy data and how it is identified. Specifically, the paper does not distinguish between different types of noise, such as label errors, preference reversals, or irrelevant data points, which could each have distinct impacts on the model's learning process. Furthermore, the method by which noisy data points are identified for filtering is not clearly articulated, making it difficult to assess the robustness of the approach.
2. In the loss function, the primary contribution is the addition of a regularization term, which is not significantly different from the original DPO approach, aside from a scaling coefficient applied to the DPO loss. The regularization term, while intended to improve robustness, appears to be a relatively minor modification to the existing loss function, and the paper does not provide a strong justification for the specific form or scaling of this term.
3. The selection of $\alpha$ is highly variable, making it difficult to determine an optimal value. The paper does not provide sufficient guidance on how to choose an appropriate value for $\alpha$ for different datasets or noise levels, which could limit the practical applicability of the method.

### Questions
1. Could you provide a clear definition of noise in the original data and compare the characteristics of noisy data with clean data? Estimating the noise rate in the dataset would add valuable context and make the approach more impactful.
2. Why choose $\frac{4 \alpha}{(1+\alpha)^2}$ to normalize the ROPO loss? Does this yield any specific advantages over other functions?
3. Besides ROPO's regularization terms, could alternative regularization strategies be applied, and how would they impact performance?
4. Could the rejection sampling introduce its own form of bias, especially if it favours certain types of responses?
5. Given ROPO’s iterative nature, what is the computational cost relative to simpler, non-iterative methods, especially for very large LLMs?
6. Does the model’s performance depend on specific types or levels of noise, and how would it handle different real-world noise distributions?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper examines the unavoidable presence of noise in preference learning and its significant impact on the performance of Large LLMs. Previous research has only slightly reduced the negative effects of noise, which persists during the training phase. Additionally, efforts to filter out noisy samples often lead to increased computational costs. To address these challenges, the paper introduces the ROPO framework, which combines noise tolerance and the filtering of noisy samples. It also incorporates the technique of rejection sampling to further enhance performance. Specifically, the authors derive a loss function through mathematical derivation designed to suppress the gradients of samples with high uncertainty. This approach prevents the model from overfitting to noisy samples while simultaneously identifying them. The effectiveness of the ROPO framework is demonstrated across three datasets in both practical and artificially noisy scenarios.

### Strengths
1. The author demonstrated through extensive derivations that methods such as DPO are not noise-tolerant and have difficulty distinguishing between noisy and clean samples. Additionally, the gradient weighting strategy of DPO amplifies the impact of noise. The author derived a loss as a regularizer through a conservative gradient weighting strategy to prevent the model from overfitting to noisy samples and to identify noisy samples.

2. The author not only proved the effectiveness of ROPO on artificial noise but also validated that ROPO can still outperform DPO and other baselines in more practical noisy scenarios.

### Weaknesses
1. Although the author presented the framework of ROPO in Figure 1, the paper still lacks an overall description of ROPO, making it difficult to understand how the components of ROPO—noisy sample filtering, rejection sampling stages, and noise tolerance training—are integrated and how the method works iteratively. The author could perhaps add some overall descriptions of the framework.

2. ROPO inevitably introduces too many hyperparameters, such as the trade-off hyperparameter alpha and the sample filtering ratio, which seem to require experimental determination. Along with the hyperparameter beta from DPO, does this make the ROPO algorithm more complex? For example, would different tasks require exploring different combinations of hyperparameters, thereby weakening its practical value?

### Questions
1. Could you provide a more detailed overall description of the ROPO framework to clarify how the components (noisy sample filtering, rejection sampling stages, and noise tolerance training) are integrated?

2. Can you include details the iterative process of the ROPO method?

3. Do different tasks require extensive hyperparameter tuning, and if so, how does this affect the practical value of the ROPO method?

### Soundness
3

### Presentation
3

### Contribution
3
