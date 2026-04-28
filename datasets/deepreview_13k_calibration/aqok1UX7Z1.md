# Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws

- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
The composition of pretraining data is a key determinant of foundation models' performance, but there is no standard guideline for allocating a limited computational budget across different data sources. Most current approaches either rely on extensive experiments with smaller models or dynamic data adjustments that also require proxy models, both of which significantly increase the workflow complexity and computational overhead. In this paper, we introduce Adaptive Data Optimization (\ours{}), an algorithm that optimizes data distributions in an online fashion, concurrent with model training. Unlike existing techniques, \ours{} does not require external knowledge, proxy models, or modifications to the model update. Instead, \ours{} uses per-domain scaling laws to estimate the learning potential of each domain during training and adjusts the data mixture accordingly, making it more scalable and easier to integrate. Experiments demonstrate that \ours{} can achieve comparable or better performance than prior methods while maintaining computational efficiency across different computation scales, offering a practical solution for dynamically adjusting data distribution without sacrificing flexibility or increasing costs. Beyond its practical benefits, \ours{} also provides a new perspective on data collection strategies via scaling laws.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose ADO, an online data selection method that adjusts data distribution dynamically across various domains by leveraging domain scaling laws. Without requiring a proxy model or external knowledge, ADO forecasts the model's loss on different data domains and automatically modifies the training data distribution according to each domain's learning potential. The experiments indicate that ADO surpasses baseline methods overall, with only a minimal increase in clock time.

### Strengths
1. The motivations presented in Section 2 highlight significant concerns, and the proposed method properly addresses these issues.
2. ADO outperforms the baselines overall, offering online data selection without the requirement of external knowledge or proxy models.
3. The authors present several interesting observations that align with our intuition and the literature (e.g. line 428, 409, 431).

### Weaknesses
1. Although the 1.3B model is not small, ADO is especially practical and relevant for LLMs with at least 8B parameters—the size typical of many popular "small" LLMs such as Llama 3.1 8B. The paper's relevance and importance might have been enhanced if the authors had conducted experiments with language models of at least 8B parameters
2. The performance improvement achieved by ADO does not seem significant enough, especially on the 1.3B model. More problematically, Table 1 shows diminishing returns as the model scale increases from 124M to 1.3B parameters. For example, 1.3B-ADO only outperforms 4 out of 7 downstream tasks, whereas 124M-ADO outperforms 6 out of 7 tasks. Additionally, the gap between the average score of ADO and the second-best baseline is less pronounced in the 1.3B model. This suggests that ADO may not scale well as the number of parameters increases.
3. Although the authors propose interesting future research directions (e.g. Section 6), incorporating some of these suggestions—such as learning rate scheduling—into the current paper would make it more complete and thorough.

On Comparisons to DoReMi and DoGE
- It is surprising that the rebuttal does not discuss DoReMi (NeurIPS 2024) when addressing conventional model sizes for academic conferences. DoReMi explicitly targets the training of 8B models, as stated clearly in their abstract, and evaluates their method at the 8B scale, showcasing their relevance in the current landscape.

- Furthermore, both DoReMi and DoGE provide significant theoretical contributions. For instance, DoReMi includes a rigorous theoretical contribution (Appendix D), while DoGE complements its experimental results with theoretical justification (Appendix B). These contributions enhance the broader impact and rigor of their work, even when experiments are limited to smaller scales (DoGE). Experiments in DoReMI are more comprehensive, testing 8B models on more datasets than this work does.

- In contrast, ADO neither performs experiments at larger scales nor offers meaningful theoretical contributions. While the empirical results are interesting, the absence of theoretical justification or deeper analysis significantly weakens the paper, particularly when compared to these prior works. This is especially problematic for a method that claims to introduce an original approach but does not delve into why ADO (or some of its elements) works at a fundamental level.

On Downstream Task Performance and the “Natural” Baseline
- While the authors argue that both “natural” and ADO are original contributions of this work, the focus of this paper is on ADO. As such, ADO must consistently outperform the “natural” baseline to demonstrate its value. For the 1.3B model, ADO only outperforms “natural” on 4 out of 7 tasks, compared to 6 out of 7 tasks at 124M. In particular, the “natural” baseline outperforms ADO on ARC-E, SciQ, and LogiQA2.

Empirical Nature of the Paper
- The paper is heavily empirical and lacks theoretical justification for why ADO works. While simplicity and practicality are valuable attributes, they are not sufficient to compensate for the absence of theoretical insights or deeper analysis. In this regard, the paper falls short of the standards set by prior works such as DoReMi and DoGE, both of which balance empirical results with robust theoretical contributions.

After reevaluating the paper, I have decided to lower my score to 5 (“below acceptance threshold”). While ADO demonstrates merit in terms of compute efficiency and modest empirical improvements, the paper falls short in its theoretical and experimental rigor relative to existing literature. Specifically:
- ADO’s inability to consistently outperform the “natural” baseline at larger scales undermines its claim of scalability.
- The lack of theoretical contributions or deeper analysis makes the paper overly reliant on its empirical results, which are not sufficiently comprehensive.
- Comparisons to prior work reveal significant gaps in scope, relevance, and contribution.

### Questions
1. Figures 6, 7, and 8 show the training loss for ADO only. I'd like to see how quickly ADO's training loss decreases compared to the baselines. I assume that ADO converges faster, but it would be interesting to observe how it performs relative to the baselines.

2. Can ADO be effectively applied to vision data and tasks? It would be of great importance if ADO could be used in training vision models that require multiple domains, such as large vision-language models (LVLMs) and diffusion models for image generation.

### Soundness
3

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
3

### Summary
This paper proposes a novel method ADO to adaptively sample data from different domains based on their contribution to model training, which is estimated from scaling law in an online manner. Empirical results on different data sets demonstrate the effectiveness of the proposed method.

### Strengths
The proposed method is introduced clearly and easy to understand

### Weaknesses
 - Several parts of ADO lack sufficient motivation
- Empirical results seem not supportive enough to fully evaluate the proposed method

### Questions
- The smoothing parameter $s$ for computing the credit assignment scores seems a bit confusing. By using $s<1$, I suppose $\lambda_k$ indeed changes drastically when $h_k$ is close to 0? Should using $s<1$ encourages $\lambda_k$ to be larger than $h_k$ especially when $h_k$ is originally close to 0? Some further discussion on the effect of this hyper-parameter may be necessary. 
- Also, can we consider other types of functions to compute $\lambda_k$ from $h_k$? Some empirical comparison on different types of functions may help others better understand how the credit assignment score affects model training, and why the authors reject simply using $\lambda_k=h_k$ here. 
- Experiments are limited to medium scale models (124M and 1.3B), and the performance gain seems to decrease with increasing model size. Such a tendency can naturally make one wonder if the performance gain can be smaller or even diminish on larger models (e.g., 2.3B or 7/8B)? Some more empirical results may be necessary to better support the proposed method. 
- While the proposed method includes many hyper-parameters (e.g., the smoothing parameter $s$ mentioned above), the authors did not provide sufficient analysis on how these hyper-parameters can affect the final performance. These results should be necessary to demonstrate that ADO can be robust to different values of these hyper-parameters. 
- Despite showing the final sampling probabilities in Figure 5, the authors may also consider further showing how $\lambda_k(t)$ and $\frac{\partial}{\partial n} \hat{L}_k(n)$ changes with training iteration $t$. These results may help others better understand how these two terms affect the sampling probabilities of different domains and how they can affect model training.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces ADO, a novel online algorithm for optimizing data distributions during the training of large-scale foundation models. ADO addresses the challenge of efficiently managing data mixtures in pretraining by continuously adapting the data distribution based on scaling laws, without requiring proxy models or significant computational overhead. The primary contribution lies in the use of per-domain scaling laws to estimate learning potential and dynamically adjust the data mixture during model training. Experimental results demonstrate that ADO can achieve comparable or better performance than prior methods, while maintaining computational efficiency across various model scales.

### Strengths
1.	ADO utilizes online scaling laws to dynamically adapt data selection during training, replacing the need for pre-trained proxy models or multi-staged processes. It requires no prior domain knowledge or external models, making it highly practical and versatile.
2.	The paper presents empirical evaluations demonstrating ADO's effectiveness across multiple benchmarks and datasets. ADO outperforms or matches existing baselines on several downstream tasks while incurring a small computational overhead (e.g., less than 0.4% additional wall-clock time).
3.	ADO offers a practical, scalable solution for data selection in large model training, with the potential to significantly reduce computational waste. The method aligns with the growing emphasis on efficient resource utilization in AI research, especially as models scale in size and cost.

### Weaknesses
1.	Figure 4 reveals that fewer than half of the datasets achieve minimal perplexity under the ADO algorithm, indicating potential limitations in the algorithm’s generalization capability across diverse scenarios. The paper would benefit from a more detailed analysis of ADO's applicability, specifically investigating why certain datasets do not converge to minimal perplexity and whether this is correlated with specific dataset characteristics or model architectures. This analysis should also explore the potential for overfitting to certain domains at the expense of others.
2.	The algorithm employs heuristic choices for key parameters, such as the exponential moving average in credit assignment and smoothing coefficients, which may impact the robustness and consistency of ADO across different datasets and tasks due to the lack of a more systematic basis for parameter selection. The paper should include a sensitivity analysis of these parameters, showing how different values affect the final performance and convergence behavior of the model. This analysis should also explore the interaction between these parameters and their impact on the stability of the training process.
3.	Symbols such as $\gamma_2$ appears in key formulas but might be clarified further with more detailed context, especially for readers unfamiliar with its role in the algorithm. The paper should provide a more intuitive explanation of the role of $\gamma_2$ in the algorithm, relating it to the overall optimization process and explaining how it affects the balance between exploration and exploitation in the data selection process. A more detailed description of how $\gamma_2$ interacts with other parameters would also be beneficial.
4.	Although ADO highlights low computational overhead as a strength, the paper lacks a systematic computational complexity analysis and comparative experiments. The absence of quantitative and visual evidence of its efficiency limits the clarity of its computational advantages. The paper should provide a more rigorous analysis of the computational complexity of ADO, detailing how it scales with the number of domains, the size of the model, and the number of training steps. Comparative experiments with other data selection methods, including detailed wall-clock time measurements, would also be beneficial to substantiate the claim of low overhead.

### Questions
1.	In ADO's data selection process, some datasets might receive minimal training due to low selection probabilities, potentially leading to under-representation. Have any additional measures been implemented to balance data distribution and ensure adequate representation across datasets?
2.	How sensitive is ADO to changes in its hyperparameters, such as the smoothing coefficient (γ1) and update intervals? Would different tasks or datasets require significant parameter tuning?
3.	Given the current limitation in modeling solely intra-domain interactions, have the authors considered potential methodologies to incorporate inter-domain interactions within the ADO framework? What approaches might be feasible for capturing these cross-domain dynamics to enhance the model’s adaptability and performance in tasks where inter-domain relationships play a significant role?
4.	ADO is designed to be task-agnostic, but certain applications may benefit from targeted data selection. Could ADO be extended to incorporate task-specific objectives without compromising its efficiency?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes an online adaptive data optimization (ADO) method for finding a policy (weighting) for different domains when pre-training a language model. The core idea is to use scaling law to model training loss. The derivative of the loss w.r.t. to the number of data points can be understood as loss reduction per data point locally, i.e. outline the potential for a domain. The final scoring also considers the contribution of the domain itself from the last update and makes it stable with a moving average. Their experiments show the ADO brings improved downstream performances on 7 common-sense reasoning tasks.

### Strengths
- Novelty. It’s a novel idea to improve over online data optimization (ODM, Albalak et al. (2023)) on 3 aspects. 1) Using scaling law to predict training loss on each domain and the derivative of the loss w.r.t. to the number of data points has intuitive interpretation as the loss reduction per data point. 2) The weighting also considers the number of data points used for a domain. 3) A combined weighting with the above two and temporal average.
- Readability. The paper not only shows their method works but also spends a reasonable amount of space discussing perspectives, hence better readability. For example on the curriculum learning (Section 2) and on the requirements (Section 3, online and agnostic to downstream tasks) of data optimization for pretrained models.
- Besides their proposed method, the authors also discover a strong baseline called “natural” policy, that depends on the number of tokens in each domain.

### Weaknesses
 - Many heuristics are used such as fitting of scaling law (Section 3.1 eq1), credit assignment (Section 3.2, eq2 ), preference distribution (Section 3.3, eq3) and temporal average (eq4 and eq5). The authors try to motivate those choices from related works and intuitions, but only eq1 is adequately explained and validated. 
- Following the above, are all the heuristics (eq 1- 5) necessary? How important are they? This is a missing part in the paper. An ablation on them can validate if the invented heuristics are actually all useful.

### Questions
- About Figure 2, I think the point on the variance is clear. But what’s more important is the agreement of the relative order of data strategies: if a data strategy is better than another on a smaller model, is it also better on a larger model? Did the authors study that? Also, what are the blue dots? I guess they are the actual validation loss of different model sizes, but would be nice to make it clear in the caption.
- The authors also write “they find $\gamma_1 = 0.1$, $s = 0.5$, $\gamma_2 = 0.1$” works well. How exactly is the process of finding those values?
- The authors write in line 480: “they are accurate locally for much of training and thus can act as a learning signal for the data policy”. On what basis do the claims are made?

### Soundness
3

### Presentation
4

### Contribution
2
