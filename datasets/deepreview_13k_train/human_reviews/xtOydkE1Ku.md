# TACTiS-2: Better, Faster, Simpler Attentional Copulas for Multivariate Time Series

- Decision: Accept
- Scores: 5, 6, 5, 8

## Abstract
We introduce a new model for multivariate probabilistic time series prediction, designed to flexibly address a range of tasks including forecasting, interpolation, and their combinations. 
Building on copula theory, we propose a simplified objective for the recently-introduced \emph{transformer-based attentional copulas} (\tactis{}), wherein the number of distributional parameters now scales linearly with the number of variables instead of factorially. The new objective requires the introduction of a training curriculum, which goes hand-in-hand with necessary changes to the original architecture. We show that the resulting model has significantly better training dynamics and achieves state-of-the-art performance across diverse real-world forecasting tasks, while maintaining the flexibility of prior work, such as seamless handling of unaligned and unevenly-sampled time series.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an advanced model for multivariate time series prediction that excels in forecasting and interpolation tasks. By applying copula theory, the authors propose a scalable transformer-based model with linear parameterization growth and a new training curriculum. This model outperforms existing benchmarks in real-world forecasting while adeptly managing irregularly sampled data. The paper details a modification of an existing approach named TACTiS, reducing computational complexity with a linear-scaling parameterization and a new training curriculum, enhancing performance on forecasting tasks and handling irregular data.

### Strengths
- The paper addresses the challenging problem of estimating joint predictive distributions for high-dimensional time series data, which has broad applicability across numerous fields.
- It introduces a universal model framework that transcends the need for domain-specific models, potentially streamlining predictive analysis in various applications.
- The Two-stage curriculum approach simplifies the optimization process, which is beneficial for practical implementations.

### Weaknesses
 - The core innovation claimed by the paper is the reduction in computational complexity through a two-stage solution, first estimating marginals and then dependencies. However, this approach isn't novel, as seen in references [1,2]. The paper would benefit from a clearer distinction of how its methodology differs significantly from these existing methods. Specifically, while the paper applies this two-stage approach to a non-parametric setting using neural networks, the core idea of separating marginal and dependence modeling is well-established. The paper needs to articulate the specific modifications or theoretical justifications that make its application of this approach novel in the non-parametric context, beyond simply using neural networks for both stages.
- The paper's primary contribution seems to be an incremental advancement in efficiency over the TACTiS approach. More substantial evidence or arguments are needed to establish this as a significant contribution to the field. The reduction in parameter complexity from factorial to linear is a positive step, but the paper needs to demonstrate that this efficiency gain translates to significant practical advantages beyond just faster training. For example, how does this reduced complexity affect the model's ability to generalize to unseen data or its performance on very large datasets?
- When evaluating the model's efficacy, the improvement in terms of Negative Log-Likelihood (NLL) is notable. However, the Mean Continuous Ranked Probability Score (CRPS) metric indicates that these improvements are only marginal when compared to the TACTiS model. This discrepancy raises questions about the practical significance of the NLL improvements, as CRPS is often a more relevant metric for assessing the quality of probabilistic forecasts. The paper should provide a more detailed analysis of why the NLL improvements do not translate to more substantial gains in CRPS, and whether this is a limitation of the evaluation metrics or the model itself.

### Questions
- The core innovation claimed by the paper is the reduction in computational complexity through a two-stage solution, first estimating marginals and then dependencies. However, this approach isn't novel, as seen in references [1,2]. The paper would benefit from a clearer distinction of how its methodology differs significantly from these existing methods.
- The paper's primary contribution seems to be an incremental advancement in efficiency over the TACTiS approach. More substantial evidence or arguments are needed to establish this as a significant contribution to the field.
- When evaluating the model's efficacy, the improvement in terms of Negative Log-Likelihood (NLL) is notable. However, the Mean Continuous Ranked Probability Score (CRPS) metric indicates that these improvements are only marginal when compared to the TACTiS model.

[1] Andersen, Elisabeth Wreford. "Two-stage estimation in copula models used in family studies." Lifetime Data Analysis 11 (2005)

[2] Joe, Harry. "Asymptotic efficiency of the two-stage estimation method for copula-based models." Journal of Multivariate Analysis 94.2 (2005).

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new model for multivariate probabilistic time series prediction. Specifically, it improves the (parameter and computation) efficiency of the previous method TACTiS by introducing a simplified objective and the corresponding learning algorithms and neural network architectures. Experiments show that the proposed method can achieve state-of-the-art performance with less computation.

### Strengths
- The proposed technique is well-motivated. It identifies the drawbacks and the reasons for the previous method TACTiS and designs specific methods to address that. 
- The paper is well-written.

### Weaknesses
 - Although TACTiS-2 is generally well motivated, it is still unclear how the two-stage solution in Sec 3.2 is derived. It should be clarified whether it is derived based on any assumptions/theorem or directly constructed. 
- Can the two-stage optimization achieve the optimal solution of the optimization problem in Eq. (7) and (8)? Although the optimal solution of each sub-problem in Eq (7) and (8) can be achieved, the gap between the theoretical optimal solution and the two-stage method should be discussed clearly. 
- The gap between TACTiS and TACTiS-2 can be further discussed. 
- May the author explain more about the difference between the task “solar-10min” and others, considerin the different behavior on it, as shown in Figure 1.

### Questions
Please clarify the questions mentioned in "Weaknesses".

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes TACTIS-2, a model for multivariate time series forecasting. TACTIS-2 builds upon TACTIS which uses neural networks to parameterize copulas for multivariate time series forecasting. To ensure the validity of learned copulas, TACTIS trains the model with random permutations of the variables which leads to problems with high-dimensional time series. To address this limitation, TACTIS-2 uses two stage training. In the first stage, marginal distributions are learned without any dependency between them. Later, the copula parameters are learned given the optimal marginal parameters. Forecasting and interpolation results on 5 datasets from Monash time series repository show that TACTIS-2 improves over TACTIS in terms of the prediction performance and training time.

### Strengths
- The paper addresses a key limitation in the existing TACTIS model which involves $d!$ factorization of the copula density, in theory. In this work, the authors utilize existing work on copulas to transform the optimization into a two stage problem which scales linearly with the dimensionality.
- The paper is very well written and easy to understand. It discusses the TACTIS model sufficiently for the reader to be able to understand the main contribution. 
- The proposed model performs better than TACTIS while being simpler and faster to train.

### Weaknesses
 - The main weakness of this work is its limited significance. The key contribution is an incremental modification of the existing TACTIS model. While the work may be interesting for individuals specifically focusing on TACTIS, its significance for the broader time series community is unclear. One may argue on the basis of the empirical results; however, in their current form, the results are not exciting and comprehensive enough to fully support this argument (see below).
- In the absence of enough methodological contributions, the empirical contribution needs to be comprehensive. However, the experiments have only been conducted on 5 datasets from the Monash repository. The baseline selection also needs improvement for the _state of the art_ claim. CSDI and SSSD would be better baselines for the empirical comparison.

To improve the paper, consider:
- Adding better baselines such as CSDI and SSSD.
- Comparing on a larger set of datasets from the Monash repository.
- Highlighting other aspects of the model. For instance, the "flexibility to handle unaligned/unevenly-sampled series" is mentioned multiple times in the related work but has only been studied is a toy setting.

### Questions
See above.

- Is there a reason why the numbers for electricity and traffic datasets differ so significantly from existing works [1]?

[1] Tashiro, Yusuke, et al. "Csdi: Conditional score-based diffusion models for probabilistic time series imputation." Advances in Neural Information Processing Systems 34 (2021): 24804-24816.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an improvement of TACTiS, which is a permutation-based non-parametric copulas, by adopting transformers and a two-stage training for multi-variate probabilistic time series prediction. This allows to avoid the expensive permutation-based objective, resulting in the number of distributional parameters scaling linearly in the number of variables. The authors numerically show that the resulting model can better train dynamics and achieve state-of-the-art performance, while keeping the flexibility of prior work.

### Strengths
•	The author skillfully merges statistical time series analysis with deep learning, estimating the marginal pdfs and attentional copula using autoencoders. This innovative combination results in a more efficient and rapid estimation of probability distributions compared to traditional statistical learning.
•	The proposed model appears highly flexible, accommodating heterogeneous datasets with uneven sampling frequencies. It also demonstrates state-of-the-art accuracies and visually impressive interpolation performance.
•	The author showcases a profound understanding of time series analysis by mathematically defining research problems, propositions, and definitions, accompanied by essential proofs.

### Weaknesses
•	While the author elucidates the statistical aspects comprehensively, a more detailed explanation of the autoencoder's use would have been beneficial. For instance, discussing the motivations behind its selection, why it's deemed the best choice, or testing its performance against alternatives like variational autoencoders. Specifically, the paper lacks a discussion on how the chosen autoencoder architecture impacts the learned marginal distributions, and whether the encoder and decoder are jointly trained or pre-trained separately. Furthermore, the paper does not explore the potential benefits of using other generative models, such as normalizing flows, which could offer more flexible and tractable density estimation.
•	In the experiment section, the author evaluates the results using five datasets from the Monash Time Series Forecasting Repository based on dimensions, frequencies, and length. The chosen samples appear to be of a small size. Merely calculating the average rank might not provide an unbiased and comprehensive evaluation. The results would be more persuasive if the author utilized a broader range of datasets and presented a critical difference plot. The current evaluation does not sufficiently explore the model's performance across diverse time series characteristics, such as seasonality, trend, and noise levels. A more robust evaluation would include datasets with varying degrees of these characteristics to demonstrate the model's generalizability.
•	The author might consider employing other techniques, such as artificially creating uneven sampling frequencies, to garner more samples. Additionally, the paper does not discuss the computational cost of the proposed method, particularly the training time and memory requirements, which are critical for practical applications. A comparison with other methods in terms of computational resources would be valuable.

### Questions
•	Why using autoencoders rather than other deep learning models such as CNN to estimate the probability distributions?
•	How to capture the dimensional dependency using this architecture?
•	Why do we take this particular subset of datasets?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
