# Flow Matching with Gaussian Process Priors for Probabilistic Time Series Forecasting

- Decision: Accept
- Scores: 8, 8, 6, 5

## Abstract
Recent advancements in generative modeling, particularly diffusion models, have opened new directions for time series modeling, achieving state-of-the-art performance in forecasting and synthesis.
However, the reliance of diffusion-based models on a simple, fixed prior complicates the generative process since the data and prior distributions differ significantly.
We introduce \oursacro{}, a conditional flow matching (CFM) model for time series that simplifies the generative problem by combining Gaussian processes, optimal transport paths, and data-dependent prior distributions.
By incorporating (conditional) Gaussian processes, \oursacro{} aligns the prior distribution more closely with the temporal structure of the data, enhancing both unconditional and conditional generation.
Furthermore, we propose conditional prior sampling to enable probabilistic forecasting with an unconditionally trained model.
In our experimental evaluation on eight real-world datasets, we demonstrate the generative capabilities of \oursacro{}, producing high-quality unconditional samples. 
Finally, we show that both conditionally and unconditionally trained models achieve competitive results in forecasting benchmarks, surpassing other methods on 6 out of 8 datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The existing diffusion models have problems in the time series generation since the data and prior distributions differ. The authors handle this problem by utilizing conditional flow matching framework. They propose TSFlow, which sets the prior distribution as Gaussian process to make the prior distribution close to the data distribution. Also, they propose conditional prior sampling which makes an unconditionally trained model possible for probabilistic forecasting.

### Strengths
• By utilizing Gaussian process to the conditional flow matching, the model reflects the temporal dependencies of the given time series data better.

• The model enables both unconditional and conditional generations.

• By conditional prior sampling, the unconditionally trained model could follow the given guidance.

### Weaknesses
•	The problem only considers the univariate case. Can the model extend to the multivariate time series problem?

•	I want some more explanation about the effectiveness of informed prior distributions. Why does closedness of the prior and data distribution imply easy learning. Do you have any experiments about train efficiency or path efficiency? 

•	Can the given prior (Gaussian process) extend to the arbitrary prior ? for example, refer to [1].

•	Do you have any theoretical evidence about how the selection of kernel functions effect to the model performance? (ex. OU kernel is better when the data follows OU process)

### Questions
•	The problem only considers the univariate case. Can the model extend to the multivariate time series problem?

•	I want some more explanation about the effectiveness of informed prior distributions. Why does closedness of the prior and data distribution imply easy learning. Do you have any experiments about train efficiency or path efficiency? 

•	Can the given prior (Gaussian process) extend to the arbitrary prior ? for example, refer to [1].

•	Do you have any theoretical evidence about how the selection of kernel functions effect to the model performance? (ex. OU kernel is better when the data follows OU process)

[1] Leveraging Priors via Diffusion Bridge for Time Series Generation, Arxiv24

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
4

### Summary
This paper studies the use of flow matching for time series forecasting. The authors first propose the use of flow matching techniques for unconditional generation using Gaussian process priors (section 3.1.1), followed by a technique for conditioning an unconditional model by sampling a relevant prior $x_0$ (section 3.1.2) or guidance (section 3.1.3), and finally the authors discuss a technique which uses a data-dependent Gaussian process prior for conditional sampling (section 3.2). The proposed methodology is empirically validated on several univariate time series datasets.

### Strengths
- The investigation of techniques for conditional sampling is pretty thorough, and I think the proposed methods are quite interesting
- The proposed method obtains fairly strong empirical results, and the empirical evaluation is convincing 
- Throughout the paper is very clear and well-written

### Weaknesses
 - There is some highly relevant related work that the authors do not discuss. [Functional Flow Matching, AISTATS 2024](https://arxiv.org/abs/2305.17209) proposes the use of GP priors in conjunction with flow matching and studies techniques for forecasting with these models.  Similarly, [Conditional Flow Matching for Time Series Modeling, SPIGM@ICML 2024](https://openreview.net/forum?id=Hqn4Aj7xrQ) uses GPs with flow matching for time series. The authors should cite these works and discuss the differences with their proposed method.
- There are some (relatively minor) clarity issues throughout
     - The use of equation 9 was a bit unclear to me. Why is this specific form of $q_1$ chosen? Some justification for this modeling choice would be good.
     - In Section 3.1.2, I am guessing that once we sample $x_0 \sim q_0(x_0 \mid y^p)$, then we use $x_0$ as an initial condition for the flow model to generate new samples $y \mid x_0$. Is this the case? If so, it would help to state this explicitly somewhere in the paper.
     - In Line 303, the authors write "approximating q_0(x_0 \mid y^p)$ with $q_0(x_0 \mid y^p)$. I think I understand what is meant here, but this seems to be a typo.

### Questions
- The exact problem statement was a bit unclear to me. In lines 154-156 the authors describe a time series as a vector in $\mathbb{R}^L$. Does this mean that the authors only work on time series having a fixed length $L$, or does the method allow for variable-length time series? Similarly, are the authors assuming that the time series all share a fixed discretization (i.e., there are some fixed times $t_1, \dots, t_L$ corresponding to $y_1, \dots, y_L$), or can the discretization vary across time series? Is this discretization assumed to be uniform, or can it be irregular as well?
- It seems to me that the setup is not limited just to forecasting, but could be applied to general conditional generation tasks, e.g., imputation. Have the authors tried anything beyond forecasting?

### Soundness
4

### Presentation
4

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
This paper introduces TSFlow, a model for probabilistic time series forecasting that enhances generative modeling by incorporating Gaussian Process (GP) priors within the Conditional Flow Matching (CFM) framework. The use of more informative GP priors helps align the prior distribution with the temporal structure of the data, potentially improving both performance and leading to runtime efficiency by simplifying the probability paths. TSFlow is flexible and can be used for both, conditional and unconditional, time-series generation.

The model demonstrates strong performance across several benchmark datasets, but there are aspects of the paper that could benefit from further clarification and improvement. Depending on the author's response, I am willing to increase my score from "weak reject" to "weak accept".

### Strengths
**Incorporating Gaussian Process Priors:** The main contribution—replacing the typical isotropic Gaussian prior $q(x_0)$ with a data-dependent conditional prior $q(x_0∣y^p)$ is well-motivated. GP priors are naturally suited for time series due to their ability to model temporal dependencies, and this idea is a clear innovation over existing flow matching methods.

**Empirical Performance:** The empirical results show that TSFlow performs well compared to state-of-the-art models across various benchmark tasks.

**Flexibility in Conditional and Unconditional Modeling:** The approach supports both unconditional and conditional generation. While unconditional generation has fewer use cases compared to conditional generation, it is a feature often overlooked in time-series analysis. The ability to use the same model for both tasks—by applying conditioning only during inference—adds versatility to the paper.

### Weaknesses
 **Majors**

**Difficulty in Parsing for Non-Experts:** The paper assumes substantial familiarity with flow matching and related generative methods, making it challenging for readers without a deep background in these specific techniques. It took for me considerable time to fully grasp the concepts, which suggests that the paper might also be difficult to read for a broader audience.

**Lack of Runtime Analysis:**  The authors propose replacing the isotropic Gaussian prior with a more complex GP prior. Howeer, they do not address the increased computational cost that comes with using GP priors. Although the GP prior is more suited to time-series tasks, this advantage must be weighed against the computational overhead. The paper should clearly state the theoretical runtime complexity of using GP priors and provide empirical runtime comparisons in the experiments. The reduction in NFEs is a positive, but its trade-off with the computational cost of the GP prior must be considered.

**Baseline Comparison:** A simple baseline for the forecasting tasks could involve using  Eq. 6 but with an isotropic Gaussian prior. Please include this method as a comparison partner in Table 3. If it is not a valid approach, it should be explained why such a baseline is excluded.

**Inconsistent Findings on Kernel Choice:** The periodic kernel minimizes the Wasserstein distance in Figure 2, suggesting it aligns well with the data distribution. However, in Table 1, the periodic kernel does not significantly outperform other kernels, and it is not even considered in Table 4.2. This inconsistency is counterintuitive and warrants further discussion. Moreover, the necessity for different hyperparameter choices across tasks (e.g., generative modeling vs. forecasting) weakens the "one model for all" argument, suggesting more task-specific tuning may be required. The fact that the kernel parameterization is fixed across different kernels (e.g., lengthscale) further complicates the analysis and makes it difficult to draw definitive conclusions about the kernel's impact.

**Minors:**

**Missing Experiments on Guided Generation (3.1.3):** I could not find experiments on Guided Generation (3.1.3) in the paper. Where can I find them?

**LPS Score Clarification:** The Linear Predictive Score (LPS) is not sufficiently explained. Please provide more details on how the LPS is calculated, specifically on what the linear model is regressed against and what the output represents.

**GP Hyperparameter Optimization:** You state in your paper that you did not fit the GP hyperparameters. This is somewhat unexpected, I would have had a strong guess that learning the hyperparameters of the GP brings a large benefit to the model. Can you perform a small experiment to evaluate the difference in performance with/without GP hyperparameter optimization?

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a model that uses flow-matching algorithms to generate and forecast univariate time-series. When trained unconditionally, it replaces the isotropic Gaussian prior distribution with an informed one and uses conditional sampling and inferencing. The model itself can also be made conditional. Experiments show that the model surpasses existing ones on benchmark tasks.

### Strengths
1. The model is flexible with many possible options; the informed prior sampling is intuitive.

2. The model shows promising results on univariate benchmark tasks.

### Weaknesses
1. The model right now is only discussed and validated on univariate time-series.

2. While there are many proposed options in the model, there lacks an ablation or a comprehensive comparison of different choices. Neither is there any theoretical insights in the proposed model.

3. The presentation of the model needs a bit more clarification. The problem formulation can potentially be expanded a bit more (see questions below). The discussion of different training/inference choices is a bit dense. Maybe some concise pseudocode or flowchart in the main text could be helpful.

### Questions
1. If my understanding is correct, the overall idea of the model is to push an initial GP to the target time-series. Therefore, the sequence length $L$ in the problem formulation section is equivalent to the vector field dimension $d$ in the background section. Can the author(s) kindly confirm if this is true? It would be nice to clarify the setting a little bit. I think the main source of confusion is that there are two time indices in this paper: the time in flow-matching and the time in the time-series, and these are orthogonal to each other. I think this should be made clear somewhere in the paper.

2. Following the first question, it would be nice to indicate in Figure 1 the time-series index and the flow-matching index. Moreover, different notations should be used. (For instance, on line 202-203, $t$ should not be used for the kernel because it has already been used in Eq. (1).)

3. How would the model respond to a growing $L$? That is, there are two subquestions in this query:
	a. What is the time complexity of the model and how does it compare to other models that you benchmarked against?
	b. When $L$ is large, Eq. (6) seems to suffer from the curse of dimensionality and the integral would be impossible to discretize. How does the model see this issue, or is it not relevant?

4. The section "Effect on the Optimal Transport Problem" only considers the distance between sequences but not anything about the training. Can you show some experiments where models that use the periodic kernel are indeed easier to train on tasks that involve periodicity?

5. On line 302-303, you wrote "we additionally condition the prior distribution on the observed past data by approximating $q_0(\mathbf{x}_0 | \mathbf{y}^p)$ with $q_0(\mathbf{x}_0 | \mathbf{y}^p)$." I assume there is a typo. What would be the intended sentence?

### Soundness
3

### Presentation
2

### Contribution
3
