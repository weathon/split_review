# EventFlow: Forecasting Continuous-Time Event Data with Flow Matching

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Continuous-time event sequences, in which events occur at irregular intervals, are ubiquitous across a wide range of industrial and scientific domains. The contemporary modeling paradigm is to treat such data as realizations of a temporal point process, and in machine learning it is common to model temporal point processes in an autoregressive fashion using a neural network. While autoregressive models are successful in predicting the time of a single subsequent event, their performance can be unsatisfactory in forecasting longer horizons due to cascading errors. We propose \texttt{EventFlow}, a non-autoregressive generative model for temporal point processes. Our model builds on the flow matching framework in order to directly learn joint distributions over event times, side-stepping the autoregressive process. \texttt{EventFlow} is likelihood-free, easy to implement and sample from, and either matches or surpasses the performance of state-of-the-art models in both unconditional and conditional generation tasks on a set of standard benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The work proposes a generative approach of modelling (unmarked) temporal point process based on diffusion models. The work decompose the distributions of temporal pointe process into the joint distribution of the number of events in a TPP realization and the joint distribution of event time conditioned on the number of events via a diffusion model in the rectified flow fashion. The proposed approach can be conditioned on history information for generate future events. Evaluation results on both unconditional generation results on commonly used TPP datasets and conditional future events forecasting shows superior performance of the model over baselines.

### Strengths
The work has the following strengths:
* This work extends diffusion models to the domain of temporal point process with a clear motivation of modelling joint distributions of events. This motivation positions the work as a novel approach toward the challenging task of future events forecasting in a fixed time horizon instead of single next event prediction. Experiment results also show clear advantages of the proposed work in multi-events forecasting in a fixed time window over existing works.
* The decomposition of TPP distribution into the distribution of the number of events and the joint distributions of event times is also a novel approach toward TPP modelling.

### Weaknesses
The work has the following weakness:
* The presentation of the work has room of improvements:
    * It is not clear what’s the purpose of introducing balanced coupling of TPPs in Section 4.1. The interpolation between two event sequences can be well defined without introducing balanced coupling and the number of events is modelled separately. In other words, the presentations of the methods does not necessarily rely on the introduction of balanced coupling and the theoretical results of the iff condition for the balanced coupling set to be non-empty. It would be helpful to add some intuitive motivation for this section in the work. Specifically, the necessity of the balanced coupling in the context of the overall model is not well-established. The authors should clarify why this specific type of coupling is essential for their approach, especially given that the number of events is modeled separately. The theoretical results regarding the non-emptiness of the balanced coupling set, while mathematically sound, lack a clear explanation of their practical implications for the model's performance or behavior.
    * In the current presentation of approach, the original contribution (Section 4.1, 4.2, separate modelling of event count and event time) and existing work (Sections 4.3, 4.4, mostly rectified flows[1]) are intertwined in one section. I would suggest the authors to consider either clearly separating their original contributions from the methods in existing works or more clearly stating their contributions in terms of methodology instead of using generic statements of contributions like a generative model for TPP. The current structure makes it difficult to discern the novel aspects of the proposed method from the application of existing techniques. A clearer separation or more precise articulation of the methodological contributions is needed to highlight the unique value of the work.
* The work constrains the type of TPP it models to unmarked temporal point process without event category labels. The practical values of the work is limited. The lack of support for marked TPPs significantly restricts the applicability of the model in real-world scenarios where events are often associated with categorical labels. This limitation should be addressed to enhance the practical relevance of the proposed approach.
* It is arguable that MSE/RMSE for next event prediction is one of the most important evaluation results for TPP models due to its wide existence in many existing TPP works [2, 3, 4], practical applicability, and easiness to compare between models. As the work is capable of conditional generation, not including this evaluation task results is disappointing. The absence of MSE/RMSE results for next event prediction makes it difficult to compare the proposed model with existing TPP models that commonly use these metrics. This omission is a significant drawback, as it hinders a comprehensive evaluation of the model's performance against established benchmarks.

### Questions
1. Do the models for conditional and unconditional generation share parameters?
2. The EventFlow model does not guarantee the generated sequences of event times preserves the original order of $\gamma_0$ but simply relies on learning such prior from training data. Does the work anpply any post-processing to generated results to deal with this potential problem? If not, do the authors encounter situations where the generated event sequence times are not in an increasing order?
3. The author claims the approach is likelihood-free. Is the re-ordering of sampled $\gamma_0$ part of the reasons that make the model incapable of evaluating likelihood of event sequences? Is it possible to define the distribution which $\gamma_0$ is sampled from in a fashion such that the $t_s$ are naturally in an ascending order?
4. Can the approach be extended to model marked TPP with event category labels in trivial ways like using the the hidden states of the denoising neural networks $\v_\theta$ to predict event categories?

### Soundness
3

### Presentation
2

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
This paper introduces EventFlow, a novel generative model for temporal point processes (TPPs). Unlike existing autoregressive models that predict events one at a time and suffer from compounding errors, EventFlow directly learns joint distributions over event times, enabling more accurate multi-step forecasting. The model is likelihood-free, making it easier to implement and sample from than existing methods. EventFlow's performance is evaluated on various synthetic and real-world datasets, consistently outperforming existing methods in both unconditional generation and multi-step forecasting tasks (forecasting in a given window) .

### Strengths
Originality: this is a novel generative model for temporal point processes that bypass the autoregressive paradigm; potential the second model in this category ( the first being diffusion point process by ludke et al.) 

Quality: the paper is very technical and technicality comes from defining appropriate probability measures; the authors reaches to an important conclusion – proposition 1, based on which they proposed eventflow. The proposed method eventflow including interpolant construction and training, and sampling seems very solid (although I did check the full details.) The paper also examines the two important cases conditional forecasting and unconditional with respect to history and conducts experiments which demonstrate the effectiveness. 

Clarity: it is well presented for the most part. 

Significance: I think this is an interest line of research as it deviates from traditional autoregressive models for TPP and I believe it is worthy of investigation by our community.

### Weaknesses
My main concern/weakness is evaluation. Especially for forecasting tasks where a separate model is learned for the event count distribution pφ(n | H). The authors treat the problem as classification. I assume learning is from the training data, where in some target window we have {1,…,N} events as target. The learned pφ(n | H) is then used to sample a count n for a specific instance for further inference task. For the experiments, while the authors use MMD as a metric for sequence distance, I don’t know how the forecasted number of events compared with the ground truth. Specifically, it is unclear how the classification performance of the learned pφ(n | H) translates to the accuracy of the forecasted event counts. A more direct evaluation, such as comparing the predicted number of events to the actual number of events in the test set using metrics like Mean Absolute Error (MAE) or Root Mean Squared Error (RMSE), would be beneficial. Similarly I am not entirely sure how the forecasting times compared with the ground truth. It would be helpful to see a comparison of the predicted event times against the actual event times, perhaps using metrics like the average time difference or a visualization of the predicted vs. actual event sequences. Some visual aids will be very helpful.

### Questions
Can the authors clarify at what flow time do the authors use as results reported for your experiments, since s is discretized.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes EventFlow, a flow-matching model for temporal point processes. EventFlow is evaluated on conditional and unconditional generative tasks. In contrast to previous diffusion-based approaches, balanced couplings are used, and the number of events does not change during generation. Therefore, the inference process consists of multiple steps: (1) EventFlow samples (unconditional) or predicts (conditional) the number of events. (2) A prior sequence $\gamma_0$ is sampled from a mixed-binomial TPP. (3) The sequence $\gamma_1$ is computed by solving the ODE with the vector field $v_\theta$.

In an experimental evaluation, EventFlow shows promising results and consistently outperforms multiple baselines.

### Strengths
- EventFlow models the event times of sequences via a CFM. The resulting model is more straightforward, more elegant, and effective than previous diffusion-based approaches.
- The evaluation includes a reasonable number of experiments, including unconditional and conditional comparisons on multiple datasets. 
- The results show strong improvements compared to diffusion-based baselines.
- The paper is easy to follow, and the methodology is clearly described.
- The baselines are reasonably tuned.

### Weaknesses
 - The biggest weakness, in my opinion, results from the use of balanced couplings. Modeling the event count distribution $p_\theta(n\mid \mathcal{H})$ with a deterministic classifier, even if sampling from the predicted distribution, still limits the distributional forecast compared to methods like AddAndThin that directly model the count distribution. This is because the classifier's output is a discrete probability distribution, which may not fully capture the underlying uncertainty in the number of events, potentially leading to less diverse samples. I assume this would be more noticeable in a likelihood-based evaluation.
- The paper does not discuss whether a likelihood evaluation is possible. As EventFlow is based on a CNF, evaluating the likelihoods of single sequences should be possible. Including an NLL-based comparison, as done in other works (Shchur et al., 2019), would strengthen the evaluation. The absence of this evaluation leaves a gap in understanding the model's performance in terms of density estimation, which is a key aspect of generative models.
- Certain hyperparameters are missing. How many neural function evaluations are used to solve the ODE? An ablation would help compare the performance with previous diffusion-based approaches. Specifically, the number of steps used in the ODE solver directly impacts the accuracy and computational cost of the method, and this should be clearly stated and analyzed.
- A runtime comparison with AddAndThin needs to be included. Especially as EventFlow uses an attention-based model. The computational cost of the attention mechanism could be a bottleneck, and a direct comparison with a non-attention based method is necessary to understand the trade-offs.

Minors:
- page 4 footnote: i.e. -> i.e., 
- Shchur et al. (2019) is cited twice (arxiv and ICLR)

### Questions
- Is computing the likelihood for single sequences possible?
- Are the prior sequences ordered? I.e., can the paths of events cross when interpolating between $\gamma_0$ and $\gamma_1$?
- Are the quantitative results of the classifier $p_\theta(n\mid \mathcal{H})$?

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors created a non-autoregressive model framework for continuous-time event sequences by using flow-matching. This allows them to skip the autoregressive process and also account for irregular time intervals. They achieve good results on a synthetic dataset and real world datasets compared to other baselines.

### Strengths
Paper is clear and is quite original with the framework of flow-matching; math is clear and has good structure.

### Weaknesses
I would've liked to see some more comparison against non-autoregressive type models for generation, such that it clarifies why the authors choose to use flow matching in particular. Comparatively, MMD wise the metric always measures with respect to the distribution, so with respect to this metric joint distribution models instead of autoregressive ones would have the advantage here.
I would like to see some more discussion on the synthetic datasets with IFTPP; why are the performances on the synthetic plot better as compared to the real world data?

### Questions
How does the length affect the corresponding accuracy? Is there an error vs sequence position plot?
Just a note that the appendix should be in the supplementary material and not the main portion :)

### Soundness
3

### Presentation
3

### Contribution
2
