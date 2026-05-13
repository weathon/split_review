# Physiome-ODE: A Benchmark for Irregularly Sampled Multivariate Time-Series Forecasting Based on Biological ODEs

- Decision: Accept
- Scores: 6, 3, 3, 3

## Abstract
State-of-the-art methods for forecasting irregularly sampled time series with missing values predominantly rely on just four datasets and a few small toy examples for evaluation. While ordinary differential equations (ODE) are the prevalent models in science and engineering, a baseline model that forecasts a constant value outperforms ODE-based models from the last five years on three of these existing datasets. This unintuitive finding hampers further research on ODE-based models, a more plausible model family.
In this paper, we develop a methodology to generate irregularly sampled multivariate time series (IMTS) datasets from ordinary differential
equations and to select challenging instances via rejection sampling. Using this methodology, we create Physiome-ODE, a large and sophisticated benchmark of IMTS datasets consisting of 50 individual datasets, derived from real-world ordinary differential equations from research in biology. Physiome-ODE is the first benchmark for IMTS forecasting that we are aware of and an order of magnitude larger than the current evaluation setting of four datasets. Using our benchmark Physiome-ODE, we show qualitatively completely different results than those derived from the current four datasets: on Physiome-ODE ODE-based models can play to their strength and our benchmark can differentiate in a meaningful way between different IMTS forecasting models. This way, we expect to give a new impulse to research on ODE-based time series modeling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Physiome-ODE, a novel benchmark for irregularly sampled multivariate time series (IMTS) forecasting derived from ordinary differential equations (ODEs). Physiome-ODE consists of 50 individual datasets created using biological ODE models. The authors highlight the need for a more challenging and biologically relevant benchmark for IMTS, as existing benchmarks primarily rely on only a few datasets and even simple constant-value baselines outperform complex ODE-based methods. Using Joint Gradient Deviation (JGD) as a metric, they select challenging ODE instances from the Physiome Model Repository, ensuring that the benchmark captures diverse levels of complexity. The paper also provides a comprehensive evaluation of state-of-the-art forecasting models, comparing methods based on neural ODEs with simpler, non-ODE methods.

### Strengths
1. Significant Contribution to IMTS Benchmarking: The introduction of Physiome-ODE represents an important step forward in providing a robust and biologically relevant benchmark for irregular time series forecasting, filling a notable gap in the current research landscape.

2. Use of JGD for Dataset Complexity: The introduction of Joint Gradient Deviation (JGD) to measure the gradient variance and dataset complexity is a well-justified and creative way to ensure that the generated datasets vary in difficulty, addressing the shortcomings of existing IMTS datasets.

3. Broad and Diverse Dataset Generation: The benchmark is derived from biological ODEs, which are inherently multivariate and often irregularly measured. This connection to real biological processes makes Physiome-ODE highly relevant for practical forecasting applications, especially in healthcare and biology.

4. Detailed Evaluation of State-of-the-Art Methods: The evaluation results indicate the diversity of the Physiome-ODE benchmark, where different models excel in different scenarios, highlighting no single model as the best for all datasets. This realistic scenario is useful for researchers to understand the strengths and weaknesses of existing methods.

### Weaknesses
1. The paper could benefit from a more detailed comparison against existing benchmarks for IMTS forecasting. While the authors do compare some models to existing datasets (such as MIMIC-IV and PhysioNet), a direct comparison of Physiome-ODE’s added value over these datasets using a common evaluation metric would be more convincing. Specifically, a quantitative analysis demonstrating the increased difficulty or different characteristics of Physiome-ODE compared to existing benchmarks using metrics like forecasting error, or the distribution of time-series characteristics would strengthen the claims.

2. The majority strategy for selecting challenging ODE instances, although effective in finding complex trajectories, might overlook personalized or localized causal differences that are crucial for domains such as personalized medicine. This lack of granularity could limit the applicability of Physiome-ODE to more individualized forecasting tasks. The selection process, based on maximizing JGD, could inadvertently filter out ODE instances that exhibit subtle but clinically important variations that are not captured by high gradient variance alone. For example, specific parameter regimes that lead to unique patient responses might be missed.

3. Creating and using Physiome-ODE is computationally intensive, especially with diffusion-based data generation and the JGD optimization steps. The paper lacks an analysis of how the dataset's computational demands impact its usability, particularly for researchers with limited access to high-performance computing resources. The paper should provide a detailed breakdown of the computational cost associated with generating a single dataset, including memory requirements and runtime on different hardware configurations, to allow researchers to assess the feasibility of using this benchmark.

4. Physiome-ODE is a semi-synthetic benchmark, as the original biological datasets are often not publicly available. This limits the interpretability and direct clinical relevance of the benchmark since it relies on models rather than real patient data. A more comprehensive discussion on the implications of using purely ODE-generated data, including potential biases, would be beneficial. The paper should discuss the potential for overfitting to the specific dynamics of the ODE models used, and how this might limit the generalization of models trained on Physiome-ODE to real-world data.

### Questions
1. How feasible is it for other researchers to replicate Physiome-ODE in environments with limited computational resources?
2. Could the proposed dataset generation method be adapted to capture personalized features in time series, such as patient-specific characteristics?
3. How does Physiome-ODE perform against benchmarks like Monash Time Series Archive or PDEBench in terms of practical outcomes for IMTS forecasting?
4. Given that the generated datasets are semi-synthetic, how closely do the generated ODE solutions resemble actual biological processes observed in real data? Would you suggest any metrics to measure the closeness?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
An irregularly sampled multivariate time series (IMTS) forecasting benchmark called "Physiome-ODE," which is derived from biological ordinary differential equations (ODEs), is proposed in this paper. Through the provision of a more extensive and varied collection of datasets, it seeks to overcome the shortcomings of the existing IMTS benchmarks, which are small and unvarying. The authors present Joint Gradient Deviation (JGD) as a metric to evaluate the complexity of datasets, asserting that it gives the benchmark a significant degree of rigor.

### Strengths
- Physiome-ODE offers a novel approach to IMTS benchmarks by generating datasets using ODEs, which is an advancement over the few IMTS datasets currently available. The idea of creating datasets using biological ODEs may benefit the scientific community.

- The paper offers a rigorous mathematical setup, especially when defining the JGD metric and the IMTS problem.

- This paper has a wider empirical foundation because it includes experiments on 50 datasets. This could be a benefit when evaluating model performance variability.

### Weaknesses
 - The theoretical explanation of JGD and how it relates to dataset complexity is unclear and excessively detailed. It is difficult to assess the reliability of the claims due to the heavy reliance on mathematical notation without adequate intuitive explanation.
 
- Although the authors assert that JGD scales super-exponentially with the Lipschitz constant, they offer no supporting data or examples. Furthermore, without a comparison to other well-known metrics like variance or entropy, it is difficult to determine how useful JGD is as a complexity metric. 

- The robustness of the results under different experimental conditions is called into question because there is no sensitivity analysis on the numerical solver or noise parameterization. Additionally, there is limited discussion on the generalizability of Physiome-ODE beyond biological applications.

- The integration of observation noise into this configuration is not adequately explained by Equation (2). While Equation (3) discusses the addition of noise to the generated IMTS data later on, but there is no obvious connection to Equation (2), so it is unclear how the noise is actually added in practice. The data generation process might be more rigorous if the differential equation were explicitly formulated to account for noise, as would be the case with a stochastic differential equation (SDE) framework.

- Simple statistical models (like linear regression and ARIMA) and more complex models (like neural SDEs) are conspicuously absent from the selection of baseline models, which lacks rigor. 

- The existence and uniqueness of the solution are not discussed, particularly in Equation (12). The robustness of this optimization is doubtful in the absence of conditions guaranteeing that a unique maximum exists for JGD over these parameters. For example, what are Equation (12)'s spread parameter bounds? 

- Can the authors substantiate their assertion that JGD scales super-exponentially with the Lipschitz constant with empirical data or an example? 

- Lemmas 1 and 2 (Appendix B) are used to approximate MGD and MPGD with finite samples, but the assumptions on function continuity and differentiability are not stated clearly.

### Questions
- The integration of observation noise into this configuration is not adequately explained by Equation (2). While Equation (3) discusses the addition of noise to the generated IMTS data later on, but there is no obvious connection to Equation (2), so it is unclear how the noise is actually added in practice. The data generation process might be more rigorous if the differential equation were explicitly formulated to account for noise, as would be the case with a stochastic differential equation (SDE) framework.

- Simple statistical models (like linear regression and ARIMA) and more complex models (like neural SDEs) are conspicuously absent from the selection of baseline models, which lacks rigor. 

- The existence and uniqueness of the solution are not discussed, particularly in Equation (12). The robustness of this optimization is doubtful in the absence of conditions guaranteeing that a unique maximum exists for JGD over these parameters. For example, what are Equation (12)'s spread parameter bounds? 

- Can the authors substantiate their assertion that JGD scales super-exponentially with the Lipschitz constant with empirical data or an example? 

- Lemmas 1 and 2 (Appendix B) are used to approximate MGD and MPGD with finite samples, but the assumptions on function continuity and differentiability are not stated clearly.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a new benchmark for multi-variable time series (IMTS) prediction called Physiome-ODE, which is generated based on biological dynamical equations (ODEs). The current evaluation methods for irregularly sampled and missing-value time series prediction mainly rely on limited datasets, which may not accurately assess the performance of models due to their small size and diversity. The authors develop a new methodology to generate and filter challenging IMTS datasets from ODEs, successfully creating a significantly larger and more diverse benchmark than existing evaluation settings. Physiome-ODE consists of 50 independent datasets derived from ODE models used in biology research over decades. By comparing the performance of existing IMTS prediction models on this new benchmark, the authors reveal different strengths among the models and indicate that some current prediction models can demonstrate stronger abilities on Physiome-ODE compared to traditional evaluation datasets. Additionally, the paper proposes a new metric, Joint Gradient Deviation (JGD), to measure the difficulty of datasets, demonstrating that the benchmark can effectively distinguish between datasets and models of different complexities. The introduction of Physiome-ODE not only provides a more comprehensive and realistic assessment platform for IMTS prediction but also promotes future research in this field.

### Strengths
- Physiome-ODE provides a larger and more diverse benchmark, allowing for a more comprehensive assessment of IMTS prediction models.

- By comparing existing models' performance on Physiome-ODE, it is possible to discover some models with stronger abilities in handling irregular sampling and missing values.

- A new metric called Joint Gradient Deviation (JGD) has been proposed, which measures the difficulty of the dataset and helps distinguish between different complexity levels of datasets and models.

### Weaknesses
 - The contribution of the proposed Physiome-ODE dataset is not clearly articulated in the manuscript, making it difficult to understand its unique advantages compared to existing time series forecasting benchmarks.

- The study only considers ODE-based predictive models and overlooks more recent models, such as TimeMixer and TimesNet. This limited model selection restricts the breadth of the comparison, potentially missing insights that could be gained from newer approaches.

- Although the study highlights that datasets created with Physiome-ODE encourage models to learn channel dependencies, it does not explain why channel-independent models like PatchTST, DLinear, PDF, and SparseTSF are observed to perform better on traditional datasets. This lack of explanation, coupled with the absence of supporting experiments, leaves the findings incomplete and reduces clarity on model performance differences.

### Questions
- Why is Joint Gradient Deviation (JGD) introduced, and what specific advantages does it offer in creating benchmarks?

- The authors do not adequately address how the Physiome-ODE dataset ensures representativeness and reliability. Without a clear explanation of its distinctive features and validation processes, the dataset's credibility as a benchmark for time series prediction remains uncertain.

- 5-fold cross-validation is used for model evaluation. Is this partitioning sufficiently representative of the dataset's diversity? Could the way the data is split introduce any biases in the results?

- By focusing solely on ODE-based models, the authors fail to incorporate recent advancements like TimeMixer and TimesNet, which may offer alternative or improved performance. This omission results in an incomplete evaluation, as it leaves out potentially competitive models that could impact the study's findings.

- The authors do not clarify why channel-independent models (e.g., PatchTST, DLinear, PDF, SparseTSF) are reportedly more effective on standard datasets, nor do they provide experimental evidence to support this observation. Without a clear rationale or relevant experiments, the paper’s insights into channel dependencies remain unsubstantiated, limiting the strength of its conclusions. Furthermore, this work does not consider the impact of data stationarity on the results.

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
The paper presents a set of ODE generated benchmark dataset for Irregularly Sampled Multivariate Time-Series Forecasting task. Furthermore, it proposes a complexity metric (JGD) to evaluate the difficulty of different datasets. Finally evaluated common forecasting methods and a baseline predicting constant time series.

### Strengths
The paper presents a new set of baselines for Irregularly Sampled Multivariate Time-Series Forecasting, As there is a need for standard baseline in this area therefore the contribution is significant. 
It also provides code to test existing methods on the benchmark, and introduces a new metric to assess the complexity of a given dataset. This metric correlates with the lowest prediction error achieved by the tested models.

### Weaknesses
The new benchmark is a standardized way of generating data from already public ODE models. This would still be valuable, but some of the choices are quite ad-hoc including the parameter noise and the initial condition selection.
These systems have significantly different sensitivity for different parameters and can change between operation regimes by tiny change of some parameters.  Currently the authors use a common $\sigma_{\text{const}}$ and hope for meaningful results. If this not happen (ODE explodes for example) the given time series is simply dropped. This may invalidate the benefit, that there is meaning behind these curated ODEs, by setting physically (or biologically in this case) nonsensical parameters or initial conditions. Expert knowledge should be used to decide what parameters should be fixed what can be modified, and sensitivity analysis should be carried out to create meaningful time series.

The mean gradient deviation (MGD) as metric of complexity is ad-hoc and questionable. As it is mentioned in the paper it automatically assumes faster oscillatory processes are less predictable. How about a huge (length of the rods is large, so in average slowly moving) double pendulum in its chaotic regime? Is it less complex than a very fast sine wave? Also systems like the Lorenz system changes between regimes (two “wings” of the “butterfly” ) suddenly but quite smoothly evolving in between, it seems this is not captured by the metric.
Correlation is found between the error and the composite metric (JGD) but it can be spurious, see bellow.

It is not clear from the paper how the training and the evaluation of the methods are carried out.  In the Experimental protocol (Line 351-352) It stands  “In our experiments models have to predict the last 50% of the time series after observing the first 50%.” How the ODE models were trained? the loss in train time was computed on similarly long sequence and backpropagated or it was trained on a single point future prediction task. 
If the later that the methods had no fair chance to learn to, for example, fall back to the constant model, as they clearly trained optimizing short term error, and go out of phase. Due to the comparatively excellent result of the constant model, it needs to be cleared that this is not the case. In this regime fast oscillating systems are less predictable as well.

### Questions
1) Did you checked that parameters you modify by resampling from a distribution still meaningful? eg.: parameters have to be positive are positive, parameters have to have a given order (e.g. a > b always hold by biology) are such, logarithmic scale parameters are sampled in logarithmic scale etc.  Same for initial condition. 
2) How the suggested complexity measure assesses Lorenz system for example? 
3) You mention the necessity of normalizing the system values. How about time? What happens if a system timescale changed from measured in sec to measured in hours?
4) Describe the training protocol what is the loss computed on, how much ahead prediction is evaluated. Best if you create a figure, If it is changing for some methods, describe it specifically.

Minor:
I would consider calling the "ode constants", “ode parameters” as this is more frequently used, or mentioning at least both name, as it can be confusing.

### Soundness
2

### Presentation
3

### Contribution
2
