# Are you SURE? Enhancing Multimodal Pretraining with Missing Modalities through Uncertainty Estimation

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Multimodal learning has demonstrated incredible successes by integrating diverse data sources, yet it often relies on the availability of all modalities - an assumption that rarely holds in real-world applications. Pretrained multimodal models, while effective, struggle when confronted with small-scale and incomplete datasets (i.e., missing modalities), limiting their practical applicability. Previous studies on reconstructing missing modalities have overlooked the reconstruction's potential unreliability, which could compromise the quality of the final outputs. We present **SURE** (Scalable Uncertainty and Reconstruction Estimation), a novel framework that extends the capabilities of pretrained multimodal models by introducing latent space reconstruction and uncertainty estimation for both reconstructed modalities and downstream tasks.  Our method is architecture-agnostic, reconstructs missing modalities, and delivers reliable uncertainty estimates, improving both interpretability and performance. SURE introduces a unique Pearson Correlation-based loss and applies statistical error propagation in deep networks for the first time, allowing precise quantification of uncertainties from missing data and model predictions. Extensive experiments across tasks such as sentiment analysis, genre classification, and action recognition show that SURE consistently achieves state-of-the-art performance, ensuring robust predictions even in the presence of incomplete data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents several key contributions through the development of the SURE (Scalable Uncertainty and Reconstruction Estimation) framework. First, SURE introduces a novel approach for handling missing modalities by incorporating latent space reconstruction
techniques into pretrained multimodal models. Second, SURE addresses the critical challenge of evaluating the reliability of both reconstructed inputs and final outputs by integrating uncertainty estimation. This is achieved through (1) a Pearson Correlation-based loss function and (2) the first application of error propagation in deep network training, allowing SURE to effectively quantify
uncertainties from multiple sources. Third, SURE is adaptable to a wide range of pretrained multimodal networks, demonstrating its robustness across various datasets and tasks, ultimately enhancing both interpretability and performance in multimodal learning scenarios.

### Strengths
* The theoretical proofs and methodology of this article are solid and valid.

* The Error Propagation and Uncertainty Estimation proposed by the authors is interesting and unique.

* The authors implemented diverse experiments on multimodal datasets from different domains.

### Weaknesses
 * A great deal of multimodal works [1,2,3,4,5] related to modal absence has been neglected, leading to results and limitations that are difficult to measure. These multimodal efforts are the main current SOTA in the field of studying modal absence across different modeling paradigms, including learning robust joint representations and reconstructions. It would be useful for the authors to clarify and compare the differences with these works.

* The writing of the article is not good enough. The author does not discuss and explain in depth many of the concepts and structures introduced. For example, there is no clear explanation of what exactly constitutes the reconstruction module described in the methods section.

* The authors consider a limited number of modal absence scenarios, and the study of modal absence should encompass both intramodal absence and intermodal absence obeying real-world scenarios. Then, the authors seem to follow a specific setup, leading to a lack of generalization of the experimental results.

### Questions
* Why use MMML specifically for the introductory introductory presentation? The reader cannot understand where the representation is. Please explain the MMML framework in detail. Would it still be similar if it was replaced with another model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces SURE (Scalable Uncertainty and Reconstruction Estimation), a framework designed to improve pretrained multimodal models when modalities are missing during training or evaluation. SURE focuses on two key areas: reconstructing missing modalities within the latent space and quantifying uncertainty for both these reconstructions and subsequent predictions. A novel Pearson Correlation Coefficient loss function and statistical error propagation are used to estimate uncertainties, improving the reliability of the reconstructed inputs and final predictions. SURE is architecture-agnostic and can adapt to various pretrained multimodal models, achieving robust and interpretable results in experiments on sentiment analysis, genre classification, and action recognition.

Overall, this paper introduces an interesting perspective for enhancing pretrained multimodal models when modalities are missing. The framework integrates techniques for estimating uncertainty and is adaptable across various architectures. However, it requires clearer theoretical justification, especially regarding how uncertainty estimation contributes to improved predictive performance. Additionally, inconsistencies in benchmark results and limited evaluation of uncertainty estimation indicate areas that need refinement. Addressing these issues would enhance both the impact and comprehensibility of the framework.

### Strengths
1. The proposed approach introduces uncertainty estimation to adapt pretrained multimodal models for downstream tasks with missing modalities. This method not only enhances overall performance on downstream tasks but also enables the estimation and interpretation of uncertainty arising from both the model's inherent stochasticity and incomplete inputs.

2. The proposed approach is validated across multiple benchmarks and compared against previous methods.

3. The approach is designed to be compatible with a wide range of pretrained multimodal models, making it adaptable and applicable across diverse architectures and tasks.

### Weaknesses
1. It is unclear how and why uncertainty estimation enhances overall performance. While Section 2.3 suggests that incorporating Bayesian learning can help model the aleatoric uncertainty, there is a lack of theoretical explanation for how this contributes to improvements in predictive performance, such as accuracy. Specifically, the paper does not detail how the uncertainty quantification is integrated into the model's objective function or decision-making process to directly improve accuracy, rather than simply providing an uncertainty estimate.

2. In section 3.2, the authors mentioned that the Gaussian assumption allows for a closed-form solution to uncertainty estimation, suggesting that a strong alignment or correlation between uncertainty and prediction error leads to better performance. However, if the underlying distribution does not follow the Gaussian assumption, is this correlation still necessary for achieving an optimal solution? If not, optimizing the PCC loss to align uncertainty with prediction error may need further justification. The paper needs to address the scenario where the true error distribution deviates significantly from a Gaussian, and how the Pearson correlation coefficient (PCC) loss remains effective in such cases.

3. The performance of IMDer on the CMU-MOSI dataset seems to be inconsistent to the results reported in the original paper. For example, the F1 score for full inputs reported in the original IMDer paper is 85.1 v.s. 62.0 reported in this paper. The authors may need to clarify the difference. This discrepancy raises concerns about the reliability of the experimental setup and the comparability of results, particularly given that the reported performance drop is substantial.

4. The evaluation of uncertainty estimation in the paper is limited. Currently, the paper assesses uncertainty estimation by calculating the correlation between uncertainty and prediction error. However, it does not intuitively explain why a high correlation between these metrics is desirable or how it contributes to the model’s reliability. The paper should include additional metrics beyond correlation, such as calibration error, to provide a more comprehensive assessment of the quality of the uncertainty estimates. Furthermore, it needs to clarify why a high correlation is a good proxy for reliable uncertainty, especially in the context of downstream task performance.

### Questions
1. A detailed caption is missing for Figure 3, making it difficult to understand the symbols and the flow of the proposed pipeline since their descriptions are spread across sections 2.2 to 2.4.

2. How does the number of reconstructors \( r_i \) scale with the number of modalities? Figure 3 suggests that a large number of reconstructors may be necessary to handle all possible missing-modality scenarios, which could affect the model’s scalability. A detailed explanation would clarify how the framework manages this growth efficiently.

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
4

### Summary
This paper focuses on an important challenge in multimodal learning—handling missing modalities, which is common in practical applications. The proposed SURE framework (Scalable Uncertainty and Reconstruction Estimation) aims to enhance pretrained multimodal models by incorporating latent-space reconstruction and uncertainty estimation. The inclusion of uncertainty estimates for both reconstruction and final predictions is valuable, as it provides insights into the model's confidence, especially when modalities are incomplete.

However, while the paper presents extensive experiments, its motivation and novelty are somewhat ambiguous. Moreover, claims regarding “scalability”, “distribution-free” and other aspects lack sufficient justification.

### Strengths
1. The paper brings up an important issue in multimodal learning—handling missing modalities, which is common in real-world applications where all data sources are not consistently available.
2. The framework provides both reconstruction and output uncertainty estimates, which help assess the reliability of predictions.
3. The paper includes extensive experiments across diverse tasks (sentiment analysis, genre classification, and action recognition) and datasets.

### Weaknesses
1. The motivation behind the paper is ambiguous. Although the introduction discusses the benefits of adapting pretrained multimodal models for downstream tasks, the rest of this paper primarily centers on uncertainty estimation. The authors could consider aligning the main content more closely with the stated motivation to improve coherence.
2. Figure 1 suggests that pretraining alone may be sufficient for handling incomplete inputs. Therefore, it remains unclear how missing modalities or incomplete inputs impact the adaptation of pretrained multimodal models. Specifically, the figure does not clearly demonstrate the necessity of the proposed approach over simply using a pretrained model, which could already be robust to missing data.
3. The novelty of this paper may be limited, given that latent-space reconstruction and Bayesian uncertainty estimation are well-established techniques [1,2,3]. The authors should elaborate on how these approaches uniquely enhance the adaptation of pretrained multimodal models for downstream tasks, as their current combination appears somewhat trivial. The paper lacks a clear explanation of how the specific combination of these techniques provides a novel contribution beyond their individual applications.
4. The authors describe the proposed Pearson Correlation Coefficient (PCC) Loss as a 'distribution-free' loss function. However, the notation in equation (4) suggests that the PCC loss still relies on the Gaussian assumption. Additionally, the uncertainty constraint for PCC loss also appears to be derived from this Gaussian assumption. The authors should further clarify the “distribution-free” property of the proposed PCC loss. Specifically, the derivation and application of the PCC loss seem to assume a specific form of the underlying distributions, which contradicts the claim of being distribution-free.

### Questions
1. What does MMML stand for?
2. According to Table 3 and 3, it seems that pretraining contributes to the majority of the performance gain of SURE. For example, the performance of the proposed SURE without pretrained weights in Table 4 seems to be worse than the performance of previous methods in Table 3. However, with pretrained weights, the preformance is significantly increased and surpasses previous methods.
3. The integration of latent reconstructors and multiple uncertainty estimations could add computational overhead. A quantitative analysis of the computational costs compared to other methods would help in understanding SURE’s efficiency and scalability.
4. The authors claim that the proposed approach is scalable (**Scalable** Uncertainty and Reconstruction Estimation). However, no justification or experimental evidence is provided to support this claim.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces latent space reconstruction and uncertainty estimation to address missing modality issues. Experiments validate the effectiveness of the proposed method.

### Strengths
1. The proposed method achieves good results on multiple datasets.

### Weaknesses
1. The authors leverage a pre-trained model and only fine-tune the reconstruction module and the prediction head. This pipeline is similar to prompt-based methods [1,2]. Therefore, these baselines should be incorporated in the experiments. Specifically, the method should be compared against prompt-based methods that also perform reconstruction in the latent space, and those that use similar fine-tuning strategies.
2. The authors claim that existing methods overlook the unreliability of reconstruction features which may damage the quality of the final outputs. However, in [2], they also perform a reconstruction process in the latent space and design prompts to enhance the reliability of the reconstructed features.  Meanwhile, [2] also leverages a pre-trained model. Therefore, the differences should be explained to highlight your contributions. A more detailed comparison is needed, focusing on how the proposed uncertainty estimation differs from the reliability enhancements in [2], particularly in the context of latent space reconstruction.
3. Why do you choose Pearson correlation instead of other correlation coefficient? Have you tried to use other nonlinear correlation coefficient? The justification for using Pearson correlation is weak. The authors should explore other correlation metrics, such as Spearman's rank correlation or Kendall's tau, which do not assume linearity and may be more appropriate for capturing complex relationships between predicted uncertainty and actual error. Furthermore, the authors should provide a rationale for why a linear correlation is suitable for this task, given that the relationship between uncertainty and error may not always be linear.
4. Why not train the reconstruction module and classifier together? The authors should provide a clear explanation of why a two-stage training process is necessary, rather than a joint training approach. A joint training approach could potentially allow for better optimization of both the reconstruction and classification tasks. The authors should also discuss the potential benefits and drawbacks of both approaches, and provide empirical evidence to support their choice.
5. The authors should report the results of all missing cases in Table 1-3. Besides, performances of different missing ratios can be added to enhance the paper. The current presentation of results is incomplete. The authors should provide a comprehensive evaluation of their method by reporting results for all possible missing modality combinations. Furthermore, the impact of different missing ratios on the performance of the proposed method should be investigated and reported.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
