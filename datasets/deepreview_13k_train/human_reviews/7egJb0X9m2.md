# TILDE-Q: a Transformation Invariant Loss Function for Time-Series Forecasting

- Decision: Reject
- Scores: 5, 6, 6, 3

## Abstract
Time-series forecasting has gained increasing attention in the field of artificial intelligence due to its potential to address real-world problems across various domains, including energy, weather, traffic, and economy. While time-series forecasting is a well-researched field, predicting complex temporal patterns such as sudden changes in sequential data still poses a challenge with current models. This difficulty stems from minimizing $L_p$ norm distances as loss functions, such as mean absolute error (MAE) or mean square error (MSE), which are susceptible to both intricate temporal dynamics modeling and signal shape capturing. Furthermore, these functions often cause models to behave aberrantly and generate uncorrelated results with the original time-series. Consequently, the development of a shape-aware loss function that goes beyond mere point-wise comparison is essential. In this paper, we examine the definition of shape and distortions, which are crucial for shape-awareness in time-series forecasting, and provide a design rationale for the shape-aware loss function. Based on our design rationale, we propose a novel, compact loss function called \toolname (Transformation Invariant Loss function with Distance EQuilibrium) that considers not only amplitude and phase distortions but also allows models to capture the shape of time-series sequences. Furthermore, \toolname supports the simultaneous modeling of periodic and nonperiodic temporal dynamics. We evaluate the efficacy of \toolname by conducting extensive experiments under both periodic and nonperiodic conditions with various models ranging from naive to state-of-the-art. The experimental results show that the models trained with \toolname surpass those trained with other metrics, such as MSE and DILATE, in various real-world applications, including electricity, traffic, illness, economics, weather, and electricity transformer temperature (ETT). Dealing with drastic changes, temporal patterns, and shapes in sequential data, which is hardly predicted using existing models, is a critical issue. This is because most time-series forecasting methods aim to minimize $L_p$ norm distances as loss functions, such as mean absolute error (MAE) or mean square error (MSE). These loss functions are vulnerable to not only considering temporal dynamics modeling but also capturing the shape of signals. In addition, these functions often make models misbehave and return uncorrelated results to the original time-series. An effective loss function must be invariant to the set of distortions between two time-series data instead of just comparing the exact values. In this paper, we propose a novel loss function called \toolname (Transformation Invariant Loss function with Distance EQuilibrium), which not only considers distortions in amplitude and phase but also allows models to capture the shape of time-series sequences. In addition, \toolname supports simultaneous modeling of periodic and nonperiodic temporal dynamics. We evaluate the effectiveness of \toolname by conducting extensive experiments with respect to periodic and nonperiodic conditions of data, from naive models to state-of-the-art models. The experimental results indicate that the models trained with \toolname outperform those trained with other metrics (e.g., MSE, dynamic time warping (DTW), temporal distortion index (TDI), and longest common subsequence (LCSS)).
\fi

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a novel loss function for time-series forecasting. Traditional loss functions like Mean Squared Error (MSE) or Dynamic Time Warping (DTW) are insufficient for complex temporal patterns and often fail to capture shape distortions in time-series data accurately. This paper addresses these limitations by proposing TILDE-Q (Transformation Invariant Loss function with Distance Equilibrium), which is designed to be invariant to amplitude shifts, phase shifts, and uniform amplifications.

The main contributions of the paper include:

1. A comprehensive exploration of shape awareness and distortion invariances in time-series data, enhancing understanding of their impact on forecasting accuracy.

2. The design of TILDE-Q, a loss function that achieves shape-aware modeling by accommodating amplitude, phase, and amplification distortions.

3. Empirical evaluations showing that models trained with TILDE-Q outperform those using standard metrics (e.g., MSE, DILATE) in various real-world applications, demonstrating higher forecasting accuracy and robustness across diverse domains like traffic, electricity, and weather forecasting.

This loss function is particularly beneficial for tasks requiring shape preservation in forecasts, providing more reliable and informative results by focusing on temporal dynamics rather than solely point-wise accuracy

### Strengths
Originality

The paper introduces a novel loss function, TILDE-Q (Transformation Invariant Loss function with Distance Equilibrium), which directly addresses a long-standing challenge in time-series forecasting: capturing shape distortions. This approach is innovative in two main ways:

1. It expands beyond conventional Lp norm loss functions by targeting invariance to transformations such as amplitude shifting, phase shifting, and uniform amplification.

2. TILDE-Q creatively combines Fourier coefficients and normalized cross-correlation in its loss function formulation, allowing models to learn temporal dynamics and shape in time-series data more effectively. This novel formulation is highly relevant, as shape-aware forecasting remains underexplored, with traditional metrics often failing in practical scenarios where pattern preservation is essential.

Quality

The paper demonstrates technical depth, grounding the TILDE-Q loss function in rigorous theoretical justifications and thoroughly detailing the transformation invariances it aims to achieve. Additionally, the experiments are carefully conducted, testing the new loss function across multiple state-of-the-art forecasting models and a range of datasets (e.g., ECL, Electricity, Traffic). The authors have thoughtfully incorporated comparative analysis with other prominent loss functions, such as MSE and DILATE, and have shown measurable improvements in both short-term and long-term forecasting. Furthermore, the empirical results support TILDE-Q’s robustness in both periodic and non-periodic settings, establishing the method’s versatility and reliability across different temporal dynamics.

Clarity

The paper is well-organized and clearly written, making its technical contributions accessible without oversimplification. The mathematical formulations are precise, with key concepts like transformation invariance and shape-awareness explained in sufficient detail. Visual aids and examples (e.g., showing model outputs with different loss functions) help illustrate the paper's motivation and results effectively. The authors also contextualize their approach within prior literature, comparing TILDE-Q to existing methods and addressing the limitations of conventional loss functions (e.g., MSE’s inability to capture temporal distortions).

Significance

The proposed TILDE-Q loss function offers substantial benefits to time-series forecasting, particularly in domains where shape preservation is crucial, such as traffic analysis, electricity usage, and economic forecasting. By improving models' ability to capture and retain shape characteristics, TILDE-Q offers significant potential for enhancing predictive accuracy and reliability in real-world applications. The work is especially relevant given the increasing demand for accurate forecasting in complex, non-stationary datasets where existing methods struggle. The approach is model-agnostic, broadening its applicability across various forecasting architectures, which adds further value to the broader AI and forecasting communities.

### Weaknesses
1. Limited Theoretical Analysis of Loss Function Properties

While TILDE-Q’s design is explained in detail, the paper could benefit from a deeper theoretical analysis of the properties and potential trade-offs of the loss function, particularly concerning convergence behavior and sensitivity to noise. For example:

Sensitivity Analysis: TILDE-Q is designed to be invariant to amplitude and phase shifts, but there is limited theoretical discussion on how these invariances impact convergence or stability during training, especially in noisy datasets. A formal exploration or proof of these characteristics would strengthen confidence in the loss function’s robustness and may reveal cases where TILDE-Q could be fine-tuned. Specifically, the paper lacks a discussion on how the softmax operation in the amplitude shift loss affects the loss landscape and its potential for introducing local minima. Furthermore, the interaction between the different loss components and their combined effect on the overall optimization process is not analyzed.

Generalization Properties: Including a theoretical analysis of the loss function’s generalization capabilities for complex time-series data could add value. For example, exploring how well TILDE-Q balances the trade-off between capturing shape and maintaining point-wise accuracy across different domains would support its broader applicability. The paper should also address whether the invariances enforced by TILDE-Q could lead to a loss of information that is crucial for specific forecasting tasks, and if so, how to mitigate this.

2. Limited Comparisons with Alternative Loss Functions Beyond MSE and DILATE

Although the experiments demonstrate TILDE-Q’s effectiveness against MSE and DILATE, it would be beneficial to include comparisons with additional shape-aware loss functions or distance measures. Some alternatives worth considering include:

CID (Complexity Invariant Distance) or CID-DTW: These metrics are known for handling shape similarity in time-series data. While TILDE-Q shows clear advantages over DILATE, CID-based methods are also shape-sensitive, so they could provide further insights into TILDE-Q’s comparative strengths. The paper should discuss why complexity invariance is less suitable for forecasting, as this is not immediately obvious and requires more justification.

MSM (Move-Split-Merge Distance): Another distance measure often used for shape-based comparisons in time-series forecasting. Incorporating MSM into experiments would offer a more comprehensive picture of TILDE-Q’s relative advantages in modeling shape. The paper should also address the computational challenges of MSM and why they were not addressed in the current work, given that approximations exist for other complex metrics like DTW.

3. Limited Analysis on Hyperparameter Sensitivity and Selection

The paper introduces hyperparameters 𝛼 and  𝛾 in the TILDE-Q formulation, which weigh the importance of each distortion invariance. However, there is minimal guidance on how these should be chosen, and the paper does not explore the sensitivity of TILDE-Q to variations in these values:

Hyperparameter Sensitivity Study: Conducting a hyperparameter sensitivity analysis across various datasets and tasks would provide insight into how to best set or tune these values for optimal results. The paper should include a detailed analysis of how the performance of TILDE-Q varies with different combinations of 𝛼 and 𝛾, and whether there are any interactions between these hyperparameters.

Recommendations for Specific Domains: Providing specific recommendations or heuristics for setting 𝛼 and  𝛾 based on the dataset characteristics (e.g., high periodicity, non-stationary) would make the paper more practical for practitioners implementing TILDE-Q in different applications. The paper should also explore adaptive methods for setting these hyperparameters, rather than relying on a fixed value for all datasets.

4. Model-Agnostic Results Could Be Strengthened with Broader Model Comparisons

The paper tests TILDE-Q across several state-of-the-art models, but it focuses heavily on Transformer-based architectures. To strengthen claims of model-agnosticism, it would be helpful to test TILDE-Q on additional, fundamentally different models, such as:

Traditional Statistical Models: Testing on models like ARIMA could illustrate how TILDE-Q performs in a more conventional setting, providing insights into whether TILDE-Q’s shape-aware capabilities are beneficial even in non-deep learning contexts. The paper should analyze if the benefits of TILDE-Q are consistent across different model types, or if certain model architectures are more suitable for this loss function.
Recurrent Models: While the paper includes some experiments with a GRU, additional recurrent models such as LSTM or BiLSTM could highlight whether TILDE-Q’s shape-awareness is generally beneficial across sequential deep learning architectures. The paper should also discuss if the sequential nature of recurrent models interacts with the shape-aware properties of TILDE-Q in any specific way.

5. Limited Real-World Application Case Studies

While the experiments include several datasets, the paper could further validate TILDE-Q’s practical value by demonstrating its application in a real-world forecasting scenario where shape-preserving forecasts are crucial. Such a case study would:

Illustrate Practical Relevance: Applying TILDE-Q in a specific domain with high stakes on shape preservation (e.g., predicting anomalies in sensor data for equipment monitoring) could make its benefits more concrete and relatable to practitioners. The paper should also provide a detailed explanation of how the shape-preserving properties of TILDE-Q lead to better results in the chosen real-world application.
Long-Term Forecasting: Exploring a real-world scenario with longer forecast horizons and showing how TILDE-Q maintains shape fidelity over extended time frames could further highlight its advantages over traditional metrics. The paper should analyze the limitations of TILDE-Q in long-term forecasting scenarios, and whether the shape-preserving properties are maintained over extended time horizons.

### Questions
1. Theoretical Properties and Convergence of TILDE-Q Loss

Could you provide more insights into the theoretical properties of TILDE-Q, particularly in terms of convergence and robustness to noise? Specifically, how does TILDE-Q’s invariance to amplitude and phase shifts impact the stability of the training process? An explanation or analysis of these properties could clarify whether TILDE-Q may introduce any trade-offs or require certain conditions for effective convergence.

2. Hyperparameter Selection and Sensitivity

The hyperparameters 𝛼 and  𝛾 play a key role in balancing TILDE-Q’s distortion invariances. Could you provide guidance on how these hyperparameters were chosen for the experiments and any best practices for tuning them? Additionally, it would be helpful to know if TILDE-Q’s performance is sensitive to the values of these hyperparameters, as this may impact practical implementation across various datasets.

3. Broader Comparison with Other Shape-Aware Metrics

TILDE-Q is compared mainly against MSE and DILATE. Could you clarify why other shape-aware metrics, like CID-DTW or MSM, were not included? Such a comparison might offer additional context for understanding TILDE-Q’s unique strengths. If computational constraints were a factor, do you have qualitative or preliminary findings on how TILDE-Q may perform relative to these methods?
Relevance of Fourier Coefficients for Phase Shifting Invariance

The paper suggests Fourier coefficients to achieve phase shifting invariance. Could you elaborate on why Fourier coefficients are preferred over other potential methods for phase handling? Additionally, are there specific scenarios where this choice may limit TILDE-Q’s effectiveness in capturing certain phase-shifted patterns?

4. Applicability to Non-Deep Learning Models

TILDE-Q is shown to work well with Transformer-based and GRU models. Do you foresee any challenges in applying TILDE-Q to more traditional forecasting models, such as ARIMA or SARIMA? This information could be useful for practitioners interested in testing TILDE-Q with non-deep learning approaches.

5. Computational Complexity and Efficiency

Since TILDE-Q combines several components (e.g., Fourier coefficients, softmax, cross-correlation), could you comment on its computational complexity compared to traditional loss functions like MSE? Additionally, are there potential optimizations or trade-offs that would make TILDE-Q more computationally feasible for large datasets or real-time applications?
Suggestions for Improvement

6. Include Hyperparameter Sensitivity Analysis

Adding a sensitivity analysis for the hyperparameters 𝛼 and 𝛾 would help readers understand TILDE-Q’s robustness and provide guidance for practitioners applying it to new datasets.

7. Explore Real-World Case Studies or Long-Term Forecasting Scenarios

Providing a case study or a long-term forecasting scenario where shape preservation is crucial (e.g., equipment monitoring or anomaly detection) would highlight TILDE-Q’s practical relevance and make its benefits more tangible.

8. Clarify the Limitations or Conditions for Optimal Use

While TILDE-Q shows impressive results, it would be helpful to outline any known limitations or conditions where TILDE-Q may be less effective. For instance, clarifying situations where high noise or extreme non-periodicity may reduce TILDE-Q’s effectiveness could guide users on when to apply it and what adjustments may be necessary.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a Transformation Invariant Loss function with Distance EQuilibrium (TILDE-Q) for time series forecasting. The paper discusses six distortions that usually appear in time series, and proposes a loss function (consisting of three terms) which are invariant to amplitude shifting, phase shifting, and uniform amplification. Experiments are performed which validates that the proposed loss function generally improves the metrics (e.g., MSE, MAE) and can better capture the shape.

### Strengths
Significance: The paper addresses the important problem of capturing the shape (temporal dynamics) in time series forecasting, and introduces a loss function that can better account for it. I think the significance is good.

Originality: I think the originality is reasonable.

Quality: Overall, the paper has good quality. The experiments is sound and extensive.

Clarity: The paper is written in a clear way.

### Weaknesses
There are a few aspects that could improve the presentation and soundness of the paper:

1. Perform ablation study that contain one or two terms of the constituting terms in TILDE-Q, and evaluate the results using different metrics similar to Table 2

2. Put example visualizations (e.g. Appendix C.2) in the main text, to give a more vivid illustration of the benefits of the proposed loss function.

### Questions
1. For the experiments in Table 1 and Table 2, are the hyperparameters the same (including neural architectures, learning rate, etc.) exactly the same when training with MSE or TILDE-Q? How are the hyperparameter searched?

2. Since the TILDE-Q is invariant to amplitude shifting, phase shifting, and uniform amplification, why can it typically improve MSE? Scenarios may happen where the prediction has these transformations, which does not affect the TILDE-Q, but increases the MSE.

### Soundness
3

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
4

### Summary
This paper introduces TILDE-Q, a novel shape-aware loss function for time-series forecasting that addresses limitations of traditional distance-based objectives. By focusing on "shape" in time-series data, the proposed loss function enhances the model's ability to generate informative predictions that capture temporal dynamics, such as peaks and troughs, rather than just reducing point-wise errors. TILDE-Q is model-agnostic and demonstrates robustness to various distortions, outperforming traditional metrics like MSE and DILATE in both accuracy and shape-related evaluations. The approach offers improved forecasting performance across diverse applications.

### Strengths
- The paper is clear and well-written. The main ideas are well exposed.
- Code is provided, making reproducibility easier.
- The presented results demonstrate the performance of the proposed approach. Table 1 demonstrates that the method outperforms regular training objectives quite consistently.
- The authors provide an extensive evaluation of distortion/augmentation methods, hence there is little ambiguity that they have covered the search space extenstively.

### Weaknesses
 - The main weakness I find in this paper is that, essentially, it demonstrates that data augmentation (via input transformations) leads to improved learning performance. This is both true, and interesting, but also expected based on (1) the fact that similar augmentations are key components of similar methods in computer vision and other fields (e.g. the whole field of contrastive learning [1]), and (2) have already been shown to have a strong impact in time-series representation learning [2, 3]. Comparisons to other objectives ([2, 3]) that also use augmentations sound particularly warranted.

### Questions
- Please refer to the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a shape-aware loss function (TILDE-Q) to be used to train time series forecasting models. This loss function learns the shape of the time series besides considering amplitude and phase distortions.

### Strengths
The authors clearly described the problem and their journey toward the proposed loss function, so a big thanks for the clear writing and illustration, which made the review easier.

### Weaknesses
While the paper is well-presented, it still has some weaknesses that need to be addressed.

1. I have some concerns about the main equations, that I list in the "Questions" section.

2. The experiments section does not cover many of the expected questions. For example, I expected to find: 
    - An ablation study that investigates the contributions of each component of TILDE-Q. 
    - An experiment that demonstrates the effectiveness of TILDE-Q under controlled conditions where the transformations (amplitude shifting, phase shifting, and uniform amplification) are systematically introduced. 
    -  A sensitivity analysis to the effect of choosing hyperparameters \alpha and \beta and how they influence performance. 
    - An assessment of the computational complexity added by TILDE-Q, compared with simpler MSE loss.

### Questions
1. In Equation 1: The choice of k is questionable. If k is the same for all time points, it may not always align with real-world scenarios where the deviation between predicted and true values varies over time. 
2. The idea of "shape awareness invariant to amplitude shifting" implies that the model will capture the overall shape or pattern regardless of vertical shifts. So, how this is achieved through a fixed gap k is unclear, as the shape might still be affected if the deviation varies.

3. Equation 2 seems to be oversimplified. Having the same dominant frequency does not necessarily mean that the two time-series samples are similar enough. Two time-series with the same dominant frequency (as in your example; sin(x) and 2 sin(x+x0)) can still have substantial variations in amplitude, phase, and waveform shape.
4. I also find that the claim “Eq. 2 allows a similar shape as the target time-series in forecasting, not exactly the same shape” is vague. It doesn’t clarify what level of similarity is acceptable, and it leaves open questions about how such similarity is quantified.

5. How is constant “k” from Eq. 1 is still applied in Eq. 3?
6. What if \hat{y}_i in Eq. 3 is not 0?
7. The authors claim that softmax produces relative values, hence it can handle any gap k. Softmax outputs are bounded between 0 and 1, and the sum of these values over all elements equals 1. My concern is that this normalization might not effectively capture a consistent gap across all values. 
8. How do the authors chose the values of \alpha and \beta in Eq. 8? Do we need to tune their values per dataset?
9. For Figure 1, the blue boxes before the arrows are not clear what do they mean. What do the left and right subfigures mean?

### Soundness
2

### Presentation
4

### Contribution
3
