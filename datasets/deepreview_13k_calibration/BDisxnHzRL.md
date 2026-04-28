# Scaling Laws for Predicting Downstream Performance in LLMs

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 6, 5

## Abstract
\looseness=-1
Precise estimation of downstream performance in large language models (LLMs) prior to training is essential for guiding their development process. Scaling laws analysis utilizes the statistics of a series of significantly smaller sampling language models (LMs) to predict the performance of the target LLM. For downstream performance prediction, the critical challenge lies in the emergent abilities in LLMs that occur beyond task-specific computational thresholds. In this work, we focus on the pre-training loss as a more computation-efficient metric for performance estimation. Our two-stage approach consists of first estimating a function that maps computational resources (\textit{e.g.,} \textbf{F}LOPs) to the pre-training \textbf{L}oss using a series of sampling models, followed by mapping the pre-training loss to downstream task \textbf{P}erformance after the critical ``emergent phase''. In preliminary experiments, this \textbf{\approach} solution accurately predicts the performance of LLMs with 7B and 13B parameters using a series of sampling LMs up to 3B, achieving error margins of 5\% and 10\%, respectively, and significantly outperforming the FLOPs-to-Performance approach. This motivates \textbf{\approachmix}, a fundamental approach for performance prediction that addresses the practical need to integrate datasets from multiple sources during pre-training, specifically blending general corpora with code data to accurately represent the common necessity. \approachmix extends the power law analytical function to predict domain-specific pre-training loss based on FLOPs across data sources, and employs a two-layer neural network to model the non-linear relationship between multiple domain-specific loss and downstream performance. By utilizing a 3B LLM trained on a specific ratio and a series of smaller sampling LMs, \approachmix can effectively forecast the performance of 3B and 7B LLMs across various data mixtures for most benchmarks within 10\% error margins.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces FLP (Flops $\rightarrow$ Loss $\rightarrow$ Performance), a two stage framework incorporating scaling laws to accurately predict the downstream performance of language models (LMs) on specific tasks by leveraging the pre-training loss. The first stage uses a power law equation to estimate the relation between flops and loss, $L(C) = \big(\frac{C}{C_N}\big)^{\alpha_N}$ by training 12 sampling LMs ranging from 43M to 3B parameters. The second stage involves using a linear function to estimate the relationship between the loss, $L$, and the task performance, $P$ [$P(L) = w_0 + w_1 * L$]. The second stage is applied carefully on those checkpoints that surpass the threshold of random performance + 5 additional performance points. The authors demonstrate better scalign law fits compared to the baseline of just using a power law function.

The paper then further extends the FLP approach to data mixing during pre-training (FLP-M) and presents an analysis on data-mixing ratios across general text and code and how mixing affects the downstream task performance, and extend the same two-stage framework of FLP, to predict downstream performance under different mixing ratios.

### Strengths
- The paper tackles an important problem of building scaling laws to measure the downstream task performance, especially when we know that task-specific behaviour emerges at different scales and smaller scale LMs might not be able to accurately capture the predictive behaviour of larger models on certain tasks. The paper's two-stage approach of separating the FLOPs $\rightarrow$ Loss and Loss $\rightarrow$ Performance predictive models circumvents the emergent behaviour issue with the FLOPs $\rightarrow$ Performance power law.
- The paper provides good insights on the mixing behaviour during pre-training on general text vs code by extending the FLP approach to FLP-M, with good empirical results on deriving the optimal mixing ratios (in a controlled setting).
- The experiments and results are exhaustive and involve a range of tasks including ARC-C, BBH, Hellaswag, HumanEval, RACE, and TriviaQA.

### Weaknesses
 - The sharp transition in performance of TriviaQA from 1B to 3B models highlights the brittleness of the approach, where the error margins can be huge for downstream task performance prediction. And it's very hard to characterize this behaviour for a whole range of tasks that are usually used to compare various LMs. The fact that the model performance jumps so drastically within a relatively small parameter range suggests that the linear approximation between loss and performance might be inadequate in capturing the underlying dynamics of the model's learning process. This makes the model unreliable for tasks exhibiting such non-linear performance scaling.
- I don't agree with the authors' point on enhancing sample efficiency by collecting losses corresponding to intermediate checkpoints and actually creates a biased estimator for the power law operands. Moreover intermediate checkpoints exhibit transient behaviours especially corresponding to learning rate adjustments (different intermediate checkpoints exhibit different learning rate schedules). While the authors claim to only use converged checkpoints for the FLOPs to loss estimation, the use of intermediate checkpoints for the loss to performance mapping is still concerning. The performance at these intermediate points is not necessarily indicative of the performance at convergence, and the learning rate fluctuations during training can introduce significant noise into the loss-performance relationship.
- I think there's a major typo in Equation 5, where the denominators of the second and the third terms are identical to the numerators. It hinders the understanding of the readers and it persists in the later sections too. [Although it's not a huge weakness and I am not basing my score on this point, assuming the authors will correct it in the rebuttal phase]. The use of similar notation for distinct quantities is confusing and makes the equation difficult to parse. This lack of clarity extends to Table 3, where the same notational issue persists, further complicating the interpretation of the results.
- The experimental setting corresponding to the comparison with Llama-3 is not explained properly, and it's hard to believe the results from Figure 11, provided that the estimated Llama-3 405B performance was quite close to the actual performance on ARC-C, whereas in this paper it's shown to be above 25%. The lack of detail regarding the specific sigmoid function used and the fitting procedure makes it difficult to assess the validity of the comparison. The discrepancy between the reported Llama-3 performance and the results in this paper raises concerns about the robustness of the proposed method when applied to different model architectures and training regimes.

### Questions
Here are a few additional questions for the authors in addition to the weaknesses above:

1. Were the pre-training datamixes used for FLP-M experiments deduped against the validation set used in FLP and FLP-M experiments? Because it might affect the scaling behaviour if there's any overlap.
2. For the comparions with Llama 3 in Section C / Figure 11, what specific sigmoidal function was used? And did the authors ensure to choose the one that results in the best fit on the sampling LMs?
3. Can the authors please correct the typos in Equation 5 and Table 3 corresponding to $C_G$ and $C_C$?
4. In Figure 2, the sampling LMs corresponding to $\leq 10^{18}$ flop scale seem to be missing. Is there a specific reason for this?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes two methods, FLP and FLP-M, for efficiently predicting the downstream performance of large language models. These methods achieve high-precision performance prediction.

### Strengths
A notable strength of the paper is the quality of the writing: the narrative is clear, and the experiments are thorough. Besides, the FLP-M method accurately predicting performance based on data loss from different domains, thus enhancing prediction accuracy in mixed data scenarios. Additionally, Figure 6 demonstrates that FLP-M can be used to derive the optimal data mixing ratio for training.

### Weaknesses
1. The authors utilize intermediate checkpoints to gather data points; however, for the same amount of FLOPs, models with different N (parameters) and D (data)  would yield distinct loss. This raises a critical question: why is it valid to use checkpoints that have not converged and are not optimized configurations to obtain data points?

2. The second drawback is a lack of novelty. Both using FLOPs to predict loss and using loss to predict downstream performance have been explored in prior work.

3. The third drawback is that the authors use a 1B model to validate the effectiveness of FLP-M scaling law for achieving an improved data mixture. However, this claim may be overstated, as 1B models often rely on guesswork for many tasks, undermining the reliability of these results.

### Questions
1. Have ongoing experiments been conducted on larger-scale models？
2. How do you justify the usage of intermediate checkpoints for acquiring scaling law datapoints?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, the authors manage to predict the downstream performance of LLMs according to the computaional resouces (e.g., FLOPs). Experimental results shows that, by utilizing a 3B LLM trained on a specific ratio and a series of smaller sampling LMs, FLP-M can effectively forecast the performance of 3B and 7B LLMs across various data mixtures for most benchmarks within 10% error margins.

### Strengths
1. **Practical Application Value** This paper introduces FLP-M, linking computational resources with LLM downstream performance. This research holds significant importance for real-world applications.

### Weaknesses
1. **Limited Scale of LM** The largest model used in this paper is only 7B, yet there are many LLMs much larger than 7B (e.g., Llama-3 70B, Llama-3 405B). This significantly restricts the generalizability of the findings. The predictive power of FLP-M might degrade when applied to models with significantly different architectures or scales. For instance, the scaling laws observed in smaller models might not hold for models with hundreds of billions of parameters, where emergent behaviors could alter the relationship between computational resources and downstream performance. The absence of experiments on models beyond 7B leaves a critical gap in understanding the applicability of FLP-M to state-of-the-art LLMs.

2. **Limited Domains in Data Mixing** As stated in the limitations, this paper only considers the domains of text and code under Data Mixing settings. This narrow scope limits the applicability of the findings to other domains such as image, audio, or multimodal data. The interactions between different data modalities and their impact on model performance are not explored, which could lead to inaccurate predictions when applying FLP-M to models trained on diverse datasets. The lack of analysis on other data mixtures also restricts the understanding of how FLP-M would perform in more complex real-world scenarios.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces FLP to address the limitations of classical scaling laws, which fail to accurately predict performance when small models perform poorly on evaluation tasks, approaching random sampling. FLP leverages the scaling law of FLOPs to predict pre-training loss and uses this loss to predict downstream performance. FLP successfully predicted the performance of 7B and 13B models across six tasks using a series of language models up to 3B.

Based on FLP, the paper further introduces FLP-M, which aims to predict downstream performance trained with various mixtures of general text and code.

### Strengths
1. The paper identifies the issue of discontinuous performance when models approach the emergent edge, which is difficult to address with classical scaling laws, and proposes a method to resolve with the continuous variant ------ loss.
2. FLP creates more data points for fitting the scaling la, potentially making the fitted curve more generalizable.
3. FLP-M is introduced for data mixtures, providing a more accurate prediction by considering the different impacts of code and general text on downstream tasks.
4. The paper conducts extensive experiments to support its claims.

### Weaknesses
1. In section 3.2 Loss->Performance, there is a strong assumption that loss and accuracy have a linear relationship. Firstly, in all generative tasks shown in Figure 9, the linear relationship between loss and metric is not evident. The authors should provide more explicit statistical indicators to prove this linear correlation. Additionally, in the classification tasks shown in Figure 9, the relationship between loss and accuracy also encounters deviations near the emergent point, indicating that FLP does not completely bypass this issue but only circumvents it in the Flops -> Loss process.
2. A simple w_1*L+w_0 is not fundamentally different from classical scaling laws.
3. FLP-M only considers code and general text, while data mixtures typically need to consider at least five domains, including common crawl (cc), academic, books, encyclopedias, and code.
4. If the paper considers the situation around the emergent point in benchmarks, it lacks a discussion on the scenario when the model approaches near-perfect scores on a particular benchmark.

### Questions
My main concerns are twofold.

1. Does the scaling law proposed in the paper have sufficient innovations compared to the classical scaling law? What are their essential differences? Please explain how the two-stage approach in FLP fundamentally differs from classical scaling laws in terms of methodology and theoretical underpinnings.

2. If the paper focuses on the model performance around the emergent point, is a linear description really suitable? Should other nonlinear descriptions be considered, such as the sigmoid function, when considering scaling near the point of near-perfect accuracy? Is there any comparation?

### Soundness
2

### Presentation
3

### Contribution
2
