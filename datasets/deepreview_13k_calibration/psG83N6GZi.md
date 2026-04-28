# Grassmannian Geometry Meets Dynamic Mode Decomposition in DMD-GEN: A New Metric for Mode Collapse in Time Series Generative Models

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 5, 3

## Abstract
Generative models like Generative Adversarial Networks (GANs) and Variational Autoencoders (VAEs) often fail to capture the full diversity of their training data, leading to mode collapse. While this issue is well-explored in image generation, it remains underinvestigated for time series data. We introduce a new definition of mode collapse specific to time series and propose a novel metric, DMD-GEN, to quantify its severity. Our metric utilizes Dynamic Mode Decomposition (DMD), a data-driven technique for identifying coherent spatiotemporal patterns, and employs Optimal Transport between DMD eigenvectors to assess discrepancies between the underlying dynamics of the original and generated data. This approach not only quantifies the preservation of essential dynamic characteristics but also provides interpretability by pinpointing which modes have collapsed. We validate DMD-GEN on both synthetic and real-world datasets using various generative models, including TimeGAN, TimeVAE, and DiffusionTS. The results demonstrate that DMD-GEN correlates well with traditional evaluation metrics for static data while offering the advantage of applicability to dynamic data. This work offers for the first time a definition of mode collapse for time series, improving understanding, and forming the basis of our tool for assessing and improving generative models in the time series domain.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper addresses the significant challenge of mode collapse in time series generative models. The authors introduce a novel definition of mode collapse tailored specifically to time series data and propose a new metric, DMD-GEN, for its quantitative evaluation. DMD-GEN leverages Dynamic Mode Decomposition (DMD) to identify coherent spatio-temporal patterns and uses Optimal Transport to quantify discrepancies between real and generated data. The metric is tested across various recent time series generative models. Experimental results demonstrate DMD-GEN's effectiveness in evaluating the time series generative models.

### Strengths
- The paper studies the critical and underexplored problem of evaluating mode collapse in time series generative models. It also highlights the absence of specific metrics designed to address the dynamic characteristics of time series data.
- The proposed metric DMD-GEN is novel to the best of my knowledge. Furthermore, it provides valuable insights into the dynamics of generated time series, allowing for a deeper analysis in future research on time series modeling.
- DMD-GEN is computationally efficient as no additional training is required, which is very practical in real-time applications.

### Weaknesses
 - The proposed metric effectively demonstrates that Diffusion-TS captures the target time series without mode collapse. However, the paper lacks a comparative analysis with models that are prone to mode collapse. It’s essential to provide such comparisons to verify the metric’s capability to discern between generative models that do and do not suffer from mode collapse.
- The robustness across different types of time series data is not thoroughly discussed, particularly for non-stationary time series with a low signal-to-noise ratio given the results on the stock dataset (please refer to Question 1 for a detailed concern).
- The presentation of results in figures and tables could be more self-contained. Specifically, the captions of Figures 1 and 2 should briefly explain the depicted results. Additionally, Table 1 should clearly indicate whether higher or lower values represent better performance.

### Questions
1. The differences between epoch 0 and the final epoch are significant in the comparisons of DMD eigenvalues of the original and generated time series across various datasets, with an exception noted in the stock dataset. Specifically, in Figure 2, the generated samples closely match the actual data from the start at epoch 0, with a slight improvement after the final epoch. Does it suggest that the DMD-GEN metric might not be as effective for highly non-stationary time series with low signal-to-noise ratio like stocks, compared to other types of data?
2. Do the results on the stock dataset in Figure 2 differ from Figure 6?
3. I am interested in exploring how the proposed DMD-GEN metric performs when applied to time series generated using traditional time series generation methods, e.g., Bootstrap. Could you extend your experiments to include this technique and provide the corresponding results?
4. Can you discuss the limitations of the DMD-GEN metric? Are there particular characteristics of time series datasets that might limit DMD-GEN's applicability, based on your current insight?

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
2

### Summary
This paper presents DMD-GEN, a novel metric for assessing mode collapse in generative models for time series data, specifically using Dynamic Mode Decomposition (DMD). The study addresses a gap in mode collapse research, which has predominantly focused on image data, by proposing a time-series-specific approach. DMD-GEN leverages Optimal Transport to measure dynamic similarities between original and generated data, providing an interpretable metric to quantify the extent of mode collapse. The authors validate DMD-GEN on synthetic and real-world datasets using various generative models, demonstrating its consistency with traditional metrics offering computational efficiency without additional training.

### Strengths
The introduction of DMD-GEN as a time-series-specific metric for mode collapse is a **novel** contribution. This approach brings a new perspective to evaluating time series generative models by capturing coherent dynamic patterns, which is less explored.

The methodology is robust and **comprehensive**, integrating techniques from DMD and Optimal Transport. The authors provide a clear mathematical foundation for their approach, along with thorough experimental validation across diverse datasets. The authors also provide the **public code** of the DMD-GEN implementation for practical use.

DMD-GEN offers both **computational efficiency** and interpretability, making it a potentially valuable tool in time-series modeling. Its ability to detect and quantify mode collapse without retraining the model makes it practical for real-time applications.

### Weaknesses
1. line 136: "Assuming uniform sampling in time, we approximate the dynamical system linearly as $x_{k+1} \approx A x_k$".
It seems to be an unrealistic assumption for real data. The assumption of uniform sampling is particularly problematic for real-world time series, which often exhibit irregular sampling intervals. This linear approximation, while simplifying the analysis, may not accurately capture the underlying dynamics, especially for systems with strong non-linearities or chaotic behaviors. The method's reliance on this assumption could limit its applicability to many real-world datasets where such assumptions do not hold.
2. Limited novelty. DMD was proposed before. While the application of DMD to time series analysis is not new, the paper's novelty hinges on its specific use for evaluating mode collapse in generative models. However, the core DMD algorithm remains unchanged, raising questions about the substantiality of the contribution. The use of Grassmannian geometry and Optimal Transport, while interesting, might not be sufficient to overcome the fact that the underlying method is not novel.
3. I don't understand, why DMD-GEN in superior to alternatives in section 4.5. For example, ContextFID also changes monotonically. The monotonic behavior of ContextFID does not necessarily imply that it captures the same aspects of mode collapse as DMD-GEN. The paper needs to provide a more detailed analysis of the differences between these metrics, including a theoretical justification for why DMD-GEN is expected to be more sensitive to mode collapse. The current explanation is insufficient.
4. A comparison with an MTopDiv (Barannikov et al. 2021) is missing. MTopDiv can also be applied to evaluation of timeseries generative models. The lack of comparison with MTopDiv is a significant oversight, especially given that MTopDiv is designed for comparing data manifolds, which is relevant to the evaluation of generative models. Without this comparison, it is difficult to assess the relative performance of DMD-GEN.
5. You claim "This approach not only quantifies the preservation of essential dynamic characteristics but also provides interpretability by pinpointing which modes have collapsed." I can't find a proof that your method can pinpoint "which modes have collapsed. The claim that the method can pinpoint which modes have collapsed is not sufficiently supported by the current analysis. The paper needs to provide a more detailed explanation of how the method identifies specific collapsed modes and provide empirical evidence to support this claim.
6. You claim that "This work offers for the first time a definition of mode collapse for time series..." 
The definition of mode collapse is quite basic - it means that a particular mode is present in training data, but absent in generated data.

### Questions
Would the authors consider evaluating DMD-GEN on larger datasets and more complex and longer time-series data? This would strengthen the paper's claims regarding the metric's applicability.

Can the authors discuss potential scalability issues when applying DMD-GEN to larger or more complex datasets? For example, it could be useful to measure memory footprint and computational times as dataset size changes, while employing a specific set of computational resources.

### Soundness
2

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
The paper proposes DMD-GEN, a method for evaluating mode collapse in timeseries generative models.
The method is based on evaluating Grassmanian geometry for dynamic mode decomposition (DMD) for timeseries.
In experiments, DMD-GEN is compared to baselines on synthetic and real timeseries.

### Strengths
1. Novelty. To my knowledge, this is the first paper which studies directly a problem of mode collapse in timeseries.
2. A diverse set of timeseries generative models is studied (TimGAN, DiffusionTS, TimeVAE).

### Weaknesses
The main theme of this paper is confusing. The proposed metric seems to trailed for dynamical systems, with "highest frequency $\Delta t$" (`line 135`) known. Yet, the authors claim it to be a generic metric and test it on common time series datasets. Moreover, there are clear logic gaps in conveying the motivation/theoretical ground of the proposal. I find it hard to understand, and not very convincing. I detail reasons and clarification questions in below.

* Why Grassmannian?
* How does the propose method/metric handle the inherent noise in time series? Can you elaborate this from a data-driven perspective? (i.e., how the number of sample affect the noise robustness?)
* The experiments are not convincing. Please include more summary statistics of the generated data, and compare with baselines. For example, it's well-known that stock data have many important  summary statistics like volatility, moving average...e.t.c. It's only fair to show that the proposal achieve more similar summary statistics to ensure its efficacy. 
* Is Thm. 3.4 your own result or from previous work? If it's from previous work, can you use lemma and specify source in lemma title instead?

### Questions
1.  "The results demonstrate that DMD-GEN correlates well with traditional evaluation metrics for static data while offering the advantage of applicability to dynamic data". What is the difference between dynamic and static data?
2. What does "||" mean in line 146, line 203?
3. Do you study univariate or multivariate timeseries?
4. What is the purpose of "x" in generators in section 4.5?

**Conclusion**.
Overall, I think that the paper raises an important research question: how to evaluate mode collapse in timeseries generative models.
But experiments providing the superiority w.r.t. baselines are not convincing and there are only few of them.
Some claims in abstract are not supported with strong evidence.
Overall, my opinion is that the paper contains some interesting ideas (application of DMD to evaluation of timeseries generative models), 
but it must be accompanied with a stronger empirical evidences, including not only synthetic mode collapse (see examples of such experiments in Barannikov et al., 2021).


**Post rebuttal**. I am thankful to authors for the detailed responses and conducting additional experiments. Sorry for the delay in my answers.
I think that the discussion helped to improve that manuscript. I am updating my rating. The final rating is defined by the overall novelty and impact of your method.

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
This work focuses on the time series generation problem. Specifically, they focus on the issue of "mode collapse" in time series generative model and propose a new notation of mode collapse and a new evaluation metric based on Dynamic Mode Decomposition (DMD) to quantify time series model collapse. They claim the proposed metric has connection/motivation/benefits from Grassmannian geometry and optimal transport. They provide some experiments on simple time series datasets to support their claims.

### Strengths
-

### Weaknesses
The main theme of this paper is confusing. The proposed metric seems to trailed for dynamical systems, with "highest frequency $\Delta t$" (`line 135`) known. Yet, the authors claim it to be a generic metric and test it on common time series datasets. Moreover, there are clear logic gaps in conveying the motivation/theoretical ground of the proposal. I find it hard to understand, and not very convincing. I detail reasons and clarification questions in below.

* Why Grassmannian?
* How does the propose method/metric handle the inherent noise in time series? Can you elaborate this from a data-driven perspective? (i.e., how the number of sample affect the noise robustness?)
* The experiments are not convincing. Please include more summary statistics of the generated data, and compare with baselines. For example, it's well-known that stock data have many important  summary statistics like volatility, moving average...e.t.c. It's only fair to show that the proposal achieve more similar summary statistics to ensure its efficacy. 
* Is Thm. 3.4 your own result or from previous work? If it's from previous work, can you use lemma and specify source in lemma title instead?

### Questions
see above Weaknesses

### Soundness
1

### Presentation
1

### Contribution
2
