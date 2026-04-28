# Improving Resistance to Noisy Label Fitting by Reweighting Gradient in SAM

- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 5, 5, 5, 6

## Abstract
Noisy labels pose a substantial challenge in machine learning, often resulting in overfitting and poor generalization. Sharpness-Aware Minimization (SAM), as demonstrated by \citet{foret2021sharpnessaware}, improves generalization over traditional Stochastic Gradient Descent (SGD) in classification tasks with noisy labels by \textit{implicitly slowing noisy learning}. While SAM's ability to generalize in noisy environments has been studied in several simplified settings, its full potential in more realistic training settings remains underexplored. In this work, we analyze SAM's behavior at each iteration, identifying specific components of the gradient vector that contribute significantly to its robustness against noisy labels. Based on these insights, we propose SANER (\textbf{S}harpness-\textbf{A}ware \textbf{N}oise-\textbf{E}xplicit \textbf{R}eweighting), an effective variant that enhances SAM’s ability to manage noisy fitting rate. Our experiments on CIFAR-10, CIFAR-100, and Mini-WebVision demonstrate that SANER consistently outperforms SAM, achieving up to an 8\% increase on CIFAR-100 with 50\% label noise.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper builds on the observation that SAM improves robustness to label noise over SGD. The paper analyzes which parameters' gradients are affected in different ways, between the SAM and SGD update. This provides some insight into the importance of further decreasing the norms of those parameters that have a lower norm under the SAM perturbation. Empirical results seem to show gains when performing this modification of SAM.

### Strengths
This paper builds up and contributes to the literature on understanding the benefits of SAM. The paper is generally well written and easy to read. Understanding SAM is broadly conceptually interesting, and the application to label noise is practically well motivated. 

It builds up ideas in a simple fashion, and lays out clear hypotheses being tested and implications of these hypotheses. The study of which parameters have their gradients upweighted, down-weighted or reversed is novel to the best of my knowledge. The broader implications of this analysis are a little unclear (detailed below), but the analysis is clean and clearly presented. 

The paper provides a new and simple modification to SAM based on the analysis and performs a large-scale evaluation over many datasets and architectures. While I have some reservations about the soundness of some aspects, overall this was a clear effort for a thorough investigation.

### Weaknesses
One glaring gap in the analysis of the paper is the effect of early-stopping. Early-stopping seems to improve clean test accuracy in both SAM and SGD. The paper does not make it clear whether the goal is to compare SANER, SAM, and SGD at the final checkpoint or best early stopped checkpoint. Even with early stopping, SAM outperforms SGD. However, from Fig 1(c) it seems like SAM vs SANER shows no gains if we do early stopping. In all the experiments reported later, it is unclear which checkpoints are compared. 

From an analysis perspective, the authors acknowledge the weakness of focusing on noisy train accuracy (rather than final test accuracy): intuitively fitting noise at training is bad, but for different algos, this could manifest differnetly in terms of affecting test accuracy. Furthermore, clean training might also be affected which can affect test accuracy. I agree with the authors on this weakness. 

From a practical perspective, if the gains do not hold with early stopping, the benefit is less clear. Furthermore, SANER introduces a new hyperparameter \alpha and adds complexity in practice. 

The role of the perturbation radius of SAM is not discussed - in practice, this is another important parameter. How does this radius interact with the new hyperparameter \alpha introduced? Is it strictly better to tune \alpha rather than the radius, or should we tune both in parallel, or do they interact in ways such that we need to tune over both in combination. 

Overall, the analysis is potentially clean and interesting, but for reasons above, the soundness / comprehensive analysis is missing some key aspects. There is no clear generalizable insights from this work, and gains in practice (if they hold up under further experiments) come at the cost of additional hyperparameters.

### Questions
(1) Please explain how you consider the role of early stopping, and what regime does the analysis and SANER experiments consider. 

(2) Does SANER improve over SAM even accounting for early stopping, i.e. is the best early-stopped checkpoint of SANER better than best early-stopped checkpoint with SAM?

(3) I am sorry if I missed this, but how do you set the SAM perturbation radius hyperparameter. How does it interact with \alpha? Do the trends of gradients across different groups hold for different radii as well?

### Soundness
2

### Presentation
4

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
The author studied the relationship between the gradients of the SAM and SGD algorithms, and through experimental validation, found a method more suitable for enhancing the model's resistance to overfitting on noisy label data. The algorithm modifies the weights of different parameter gradients during model updates to improve the model's robustness. In terms of experiments, the author conducted validation on several classic public datasets.

### Strengths
1. In the context of increasingly large training datasets, it is practically significant to effectively prevent models from overfitting on noisy label data. Relying solely on algorithms and rules to clean the data is often too costly, so optimizing algorithms to reduce the impact of noisy label data is more valuable.
2. The author's approach of comparing the relative sizes of the gradients of each parameter in the SAM and SGD algorithms during model updates, and using this as a criterion to assess whether the parameters are overfitting to the model due to noisy label data, is straightforward and exhibits a certain level of innovation. The experimental design is also very reasonable.
3. The author's experimental design is quite rigorous, and they conducted a substantial number of experiments and tests on several public datasets.

### Weaknesses
1.I noticed that Figure 2 in Section 3 is based on training a ResNet-18 model on CIFAR-10. Shouldn't testing be conducted on more models and datasets to confirm that the three types of parameters, Group A, B, and C, indeed exhibit the proportions mentioned in the paper?Perhaps conducting experiments on a larger ResNet model (ResNet-50) and a larger dataset like CIFAR-100 or ImageNet (if conditions permit) would provide more convincing results.

2.Based on the author's analysis, in fact, at epoch 100, there was a noticeable increase in the parameter ratio of Group C, which maintained around 10% during the early training stages. Would it be more meaningful to directly use the reverse gradients for noisy label data? Also, I noticed that the ratios of Group B and Group C are quite similar in the early stages of training, and the values for Group A are mostly around 1.0 while those for Group B are around 0.99. If this is the case, I don't believe that SGD and SAM have different perspectives on the parameters in these two groups.As before, I believe it is necessary to validate this distribution pattern on larger models and datasets. Additionally, I think it would be meaningful to further investigate whether there are significant changes in the parameters within the three groups as training progresses, as well as the specific distribution of values.

### Questions
Please refer to the comments on weaknesses.

### Soundness
3

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
5

### Summary
The paper conducts an empirical study which reveals that during training, some gradient dimensions contribute to the superior robustness of SAM over SGD against noisy labels. These dimensions have lower magnitudes and the same signs as the corresponding components in SGD. Reducing the weight of such dimensions during training improves robustness of SGD and SAM variants against label noise.

### Strengths
The paper reveals an interesting phenomena, showing that there are dimensions with lower magnitudes and the same signs as the corresponding components in SGD, that are responsible for superior robustness of SAM. This is interesting and novel to my knowledge.

The paper is clear and easy to follow. While I found the observation interesting, I believe the paper requires to back up the results with a more in-depth study (either some theoretical analysis or more in-depth ablation study and a wider range of experiments) to be considered significant.

### Weaknesses
While the proposed idea of reweighting dimensions with lower magnitudes and same signs as SGD is simple (simplicity is good), it requires an appropriate linear scheduler that gradually decreases the reweighting factor from 1 to a predetermined value over k epochs. Both the reweighting factor and k needs to be tuned and I didn't find an ablation study or any insight on how to set these parameters for different datasets/architectures. Table 5, 6 in the appendix only compares using or not using this scheduler (k=0 and k=50).

Considering that this is an empirical study, I'd expect much more in-depth empirical study of the observed phenomena. For example, what is the effect of datasets and architectures on the observed phenomena? What's the effect of the label noise level on the observed phenomena? How should one set the parameters of the proposed method? The paper includes experiments on Cifar10-100 (and their subsampled versions) with label noise level of 25% and 50%, and Webvision. On Cifar-10, the improvement is not significant, while on Cifar-100 the proposed method works much better. Nevertheless, there is no explanation or deeper analysis provided in the paper. Existing methods for robust training against noisy labels usually perform much better on Cifar10. Considering that the pattern is different for the proposed method, digging deeper into why things work differently would be an interesting addition to the paper. The authors can also analyze the effect of the proposed reweighting methods combined with existing robust training methods, as is done in the original SAM paper.

Finally, I believe adding a theoretical study of the observed phenomena using a simple data model and network architecture, or even a simple toy example explaining the effect of reweighting would significantly strengthen the paper.

### Questions
Please see the weaknesses above.

### Soundness
3

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
3

### Summary
This paper presents SANER, a novel approach designed to improve the robustness of Sharpness-Aware Minimization (SAM) in the presence of noisy labels. The proposed method introduces a reweighting mechanism for gradient components to suppress the fitting to noisy labels, thereby enhancing generalization performance. Extensive experiments are conducted on various datasets, demonstrating the effectiveness of SANER compared to SAM and other optimizers.

### Strengths
1）SANER introduces a novel reweighting mechanism for specific gradient components, effectively extending SAM to better handle noisy labels. This innovation is well-motivated and provides a meaningful contribution to the field of noise-resistant optimization.
2）The experimental validation convincingly demonstrates that SANER outperforms SAM and other optimizers in different noise scenarios. The visualizations provided further reinforce the claims regarding the noise robustness of SANER.
3）The use of a linear schedule for adjusting parameters during training is practical and helps stabilize the learning process, especially in the early stages when noisy labels are more problematic.

### Weaknesses
1）The paper lacks a detailed explanation of how the gradient components are divided into Group A, B, and C. It is unclear what specific criteria were used for this division, and including pseudocode would enhance clarity and reproducibility. Additionally, while visual evidence supports the reweighting mechanism, systematic mathematical derivations justifying the effectiveness of the approach in suppressing noisy label fitting would be valuable. Specifically, the paper does not provide a clear mathematical formulation of how the reweighting of Group B gradients directly leads to reduced sensitivity to noisy labels, nor does it offer a theoretical analysis of the impact of different reweighting factors on the convergence behavior under noisy conditions.
2）The manuscript includes comparisons with VaSSO, but there are notable gaps in performance under different noise rates, even with identical experimental settings. Clarifying why these significant differences occur would improve the discussion. Moreover, additional experiments with varied noise ratios would help provide a more balanced comparison. Furthermore, comparing SANER with methods such as AdaSam and Adan could better help demonstrate its broader generalization capabilities or effectiveness across different tasks and domains. AdaSam is primarily used in natural language processing tasks, while Adan is a recent adaptive Nesterov momentum algorithm showing promise in vision, language, and reinforcement learning tasks. The paper should also explore the computational overhead of SANER compared to standard SAM and other optimizers, particularly in terms of training time and memory usage, to provide a more comprehensive evaluation.
3）The analysis of the sensitivity of the parameter α is limited. A more comprehensive study covering different noise ratios, network architectures, and training conditions would be beneficial. For instance, exploring α’s behavior in noisy segmentation tasks using Vision Transformers (e.g., ViT-based noisy segmentation) as well as standard classification tasks with different architectures (e.g., ResNet versus VGG) would provide a clearer picture of the parameter's impact across varied settings. The paper should also investigate the interaction between α and the reweighting factor k, and how their combined effect influences the performance of SANER under different noise conditions. The current analysis focuses on the individual effects of α, but a more detailed exploration of their interplay is needed.

### Questions
1）Regarding the division of gradient components into Group A, B, and C, what specific criteria or methodology did you use for this grouping? Could you provide pseudocode for this process to make the grouping mechanism clearer? Additionally, could you explain why these particular components were chosen for reweighting, and include systematic mathematical derivations to show how these components effectively suppress noisy label fitting?
2）The paper includes comparisons with VaSSO; however, the results under different noise rates show considerable gaps. Could you explain why such significant differences occur under identical experimental settings? Moreover, could you conduct additional experiments covering more diverse noise ratios to provide a balanced comparison, and clarify whether these differences are due to inherent limitations of the methods or specific experimental setups?
3）In the appendix, only ablation studies for the presence or absence of the α parameter were conducted, but there is a lack of detailed experimental analysis on the selection of α values (e.g., from 0 to 1 or values greater than 1). How do different values of α affect performance across varying noise ratios and network architectures? Providing such detailed experimental support would help in understanding the optimal choice of α under different scenarios.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This manuscript explores the potential of SAM in the context of noisy label learning. Specifically, it provides an empirical study of the component-wise gradients in SAM, identifying the gradient components most crucial for handling noisy labels. Building on these insights, this manuscript proposes SANER, a method that adjusts SAM gradients to improve model robustness against label noise.

### Strengths
1. The writing quality is good.
2. This manuscript provides a detailed experimental analysis of SAM and its robustness to label noise.
3. The proposed method is tested across different model architectures, layer widths, and data sizes, demonstrating its generalization capability across different settings.

### Weaknesses
1. The theoretical analysis is lacking. Specifically, there is no justification for why downweighting the gradient component in Group B helps the model resist label noise, or why gradients from noisy samples dominate Group B as the model begins to overfit. A theoretical analysis could suggest a more effective gradient adjustment method than simple downweighting. The manuscript does not provide a clear explanation of the underlying mechanisms that cause the observed behavior of Group B gradients. It is unclear why the gradients of noisy samples are more prominent in Group B, and a more rigorous analysis is needed to support this claim. Furthermore, the current approach of simply downweighting Group B gradients lacks a strong theoretical basis and may not be the optimal solution.
2. Some experimental results are missing.
    1. Experimental results for high label noise settings (e.g., 80% symmetric label noise) are absent. Given that this manuscript primarily addresses label noise learning, evaluating the proposed method under high label noise conditions is essential, as it is a common practice in current label noise learning literature. The absence of high noise experiments limits the evaluation of the proposed method's robustness. It is crucial to demonstrate the method's performance under extreme noise conditions, as this is a key challenge in noisy label learning.
    2. The clean accuracy results for different values of $\alpha$ are missing. Recall that $p_\text{clean}$ still accounts for 1 / 3 of the total components in Group B, so downweighting Group B may potentially harm the accuracy of clean samples. The manuscript should include an analysis of how the downweighting factor affects the performance on clean samples. It is important to show that the proposed method does not significantly degrade the performance on clean data while improving robustness to noisy labels.

### Questions
1. Regarding Figure 3, since Group A also contributes to SAM’s resistance to noisy fitting, why not reweight Group A as well?
2. Since SAM enhances model performance in clean label scenarios, would SANER perform worse than SAM in such cases?
3. Are there any improvements when combined with other label noise learning algorithms?

### Soundness
3

### Presentation
3

### Contribution
2
