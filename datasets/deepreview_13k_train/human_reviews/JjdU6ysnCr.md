# On the feature learning in diffusion models

- Decision: Accept
- Scores: 6, 6, 6, 6, 6, 6

## Abstract
The predominant success of diffusion models in generative modeling has spurred significant interest in understanding their theoretical foundations. In this work, we propose a feature learning framework aimed at analyzing and comparing the training dynamics of diffusion models with those of traditional classification models. Our theoretical analysis demonstrates that, under identical settings, diffusion models, due to the denoising objective, are encouraged to learn more balanced and comprehensive representations of the data. In contrast, neural networks with a similar architecture trained for classification tend to prioritize learning specific patterns in the data, often focusing on easy-to-learn components. To support these theoretical insights, we conduct several experiments on both synthetic and real-world datasets, which empirically validate our findings and highlight the distinct feature learning dynamics in diffusion models compared to classification.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents a novel theoretical framework for analyzing the feature learning dynamics in diffusion models, marking the first such contribution to the existing literature. Through rigorous analysis, the authors demonstrate that diffusion models inherently promote the learning of more balanced features, in contrast to traditional classification methods, which tend to prioritize certain features over others. Additionally, the framework can be adapted to accommodate more complex data settings. This theoretical insight has significant implications for downstream tasks, such as out-of-distribution classification, where only these rare or weak features may be present.

### Strengths
1. The theoretical findings are solid and  innovative.
2. The contribution appears valuable for comprehending the internal mechanisms of diffusion models and neural networks.

### Weaknesses
1. The presentation requires enhancement. Some notations are introduced without prior definition upon their first occurrence, e.g., what does $m$ refer to in line 188?
2. The classifier considered in this manuscript lacks sufficient generality. The use of a shallow neural network, specifically a two-layer network, raises concerns about the applicability of the theoretical findings to more complex, real-world architectures. The analysis focuses on a simplified model, which may not fully capture the intricate dynamics of deeper networks used in practice.

### Questions
1. My main concern is how applicable the theoretical findings are to a broader range of classifiers and diffusion models. To be honest, the shallow neural network function defined in this manuscript appears unsuitable for real-world data.
2. Is the requirement for orthogonality in data setup common in practice?

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
This work study the feature learning mechanism behind the performance of diffusion models in fitting complex distributions and their out-of-distribution transferability. The authors attribute these capabilities to the denoising objective, which results in balanced training and comprehensive representations, in contrast to a classification objective that focuses on specific patterns. A theoretical and empirical analysis are conducted which show that diffusion models (DMs) tend to learn both the signal and noise in a balanced manner, in contrast to supervised classification, which focuses either on signal or noise. These claims are supported using a synthetic dataset and an edited MINTS dataset.

### Strengths
This work addresses a highly interesting problem: elucidating the underlying mechanisms in diffusion models that lead to their performance and transferability. 
The authors have done a good job in building a framework where the mechanism and learning dynamics can be analyzed both empirically and theoretically. 
The problem is well-motivated, and the paper is generally pleasant to read.

### Weaknesses
1) The paper’s objective is to analyze feature learning in diffusion models, which could explain their success. A detailed comparison with supervised classification is provided, however a comparison to other generative approaches such as GANs or VAEs is missing. Therefore, it is unclear if the balanced learning regime is due to DMs' specific denoising based learning, or due to a more abstract or fundamental difference between generative and discriminative approaches. This is a critical omission, as it limits the scope of the conclusions. The authors should investigate whether this balanced learning is unique to diffusion models or a general property of generative models, which would significantly impact the paper's claims.

2) The paper could benefit of more exhaustive experimental setting such a case with larger feature space rather than one label. The current experiments, while insightful, are limited in scope and do not fully demonstrate the generalizability of the findings. Specifically, the use of a single label limits the complexity of the feature space and may not accurately reflect the behavior of diffusion models in more complex scenarios. Experiments with higher dimensional feature spaces and multiple labels are necessary to validate the claims more broadly.

3) The organization and the notation of the paper could be improved. The current structure makes it difficult to follow the arguments and understand the key contributions. Specifically, the redundant content between Sections 1.1 and 2 should be revised. The notation is sometimes difficult to follow in several parts of the paper and needs to be revised: In 1.1, some elements are used without being introduced, such as \(d\). I assume \(d\) and \(n\) refer to vector dimensions, but it would be better not to rely on guesswork. Other variables like \(r\), \(\gamma\), and \(k\) are first used without any introduction. In Section 2, \(W\) and \(x\) sometimes have one or two subscripts, which is confusing. Figures 2 and 4 should be improved (Y Axis labels missing ). In Section 5.1, Figure A.1 should be moved to the main text for better cohesion with the section.

### Questions
1) It is interesting to analyze the learning regimes of diffusion models in comparison to classification objectives. However, it is somehow expected that a generative learning objective (as in diffusion models) results in more balanced learning, unlike the classification objective, which is designed to focus on learning features related to specific labels. A natural question that arises is how DMs behave in comparison to other generative approaches, such as GANs or VAEs. Could the authors discuss this point or provide experimental results?

2) In the diffusion case: Since the neural network input is a noisy version of the data sample, the SNR should be altered as additional noise is introduced. Consequently, the SNR of the neural network input differs between the diffusion model and the classification case. Could you please elaborate on this point?

3) DMs can also be viewed as maximizing the Evidence Lower Bound (ELBO) with a form of data augmentation [1]. Since the neural network input is a noisy version of the data sample, unlike in the classification case, it may be unclear which factors are really influential. Could you elaborate on this point? If data augmentation were applied in the classification case, what behavior would be expected?

4) Redundant content between Sections 1.1 and 2 should be revised.

5) The notation is sometimes difficult to follow in several parts of the paper and needs to be revised:

   * In 1.1, some elements are used without being introduced, such as \(d\). I assume \(d\) and \(n\) refer to vector dimensions, but it would be better not to rely on guesswork. Other variables like \(r\), \(\gamma\), and \(k\) are first used without any introduction.

   * In Section 2, \(W\) and \(x\) sometimes have one or two subscripts, which is confusing.

   * Figures 2 and 4 should be improved (Y Axis labels missing ).

6) In Section 5.1, Figure A.1 should be moved to the main text for better cohesion with the section.

[1] Kingma, D., & Gao, R. (2024). Understanding diffusion objectives as the elbo with simple data augmentation. Advances in Neural Information Processing Systems, 36.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new theoretical framework specifically for analyzing the feature learning dynamics in diffusion models compared to classification models. This is a significant contribution to the existing body of literature, which has primarily focused on the generative aspects of diffusion models.

### Strengths
- The authors not only provide a theoretical analysis of the feature learning process in diffusion models but also validate their findings through experiments. This strengthens the credibility and practical relevance of the proposed framework.
- A key contribution of the work is the comparison between diffusion models and classification models in terms of feature learning dynamics. The results show that diffusion models tend to learn more balanced representations of both signal and noise, which contrasts with the classification models' tendency to focus on one or the other, depending on the signal-to-noise ratio (SNR).
- The paper provides clear mathematical results (e.g., Theorem 1.1 and Theorem 3.1) that demonstrate key differences between diffusion and classification models, particularly in terms of feature learning speed and final outcomes. These results are well-supported by rigorous proofs and visualization (e.g., Figure 1).

### Weaknesses
 - While the theoretical insights are valuable, the paper does not sufficiently discuss how these findings might impact practical applications of diffusion models. The focus is more on theoretical analysis, and less on how these insights could be used to improve real-world tasks like image generation, classification, or other downstream applications.
- The theoretical results depend on several strict assumptions (e.g., Condition 3.1), particularly regarding the dimensionality and network initialization. In real-world scenarios, these assumptions may not hold, limiting the practical applicability of the theoretical findings.

### Questions
- The theoretical analysis relies on specific assumptions about high-dimensional spaces and signal-to-noise ratios. How would these theoretical insights hold up when applied to real-world datasets like ImageNet or COCO? Is there any plan to test these results on more practical benchmarks?
- The analysis is based on a simple two-layer convolutional network. If the architecture changes—say, using deeper networks or different types like ResNets or Transformers—would the feature learning dynamics of diffusion models change? Are there any experimental or theoretical results to explore this?
- The paper suggests that classification models tend to overfit noise when the SNR is low. However, in certain tasks, could learning noise or background features also be beneficial (e.g., in robustness or generalization)? Is there any discussion or analysis of cases where noise learning might be advantageous?
- Diffusion models are typically slower to train due to their iterative denoising process. The paper highlights the balanced feature learning in diffusion models, but are there any methods to accelerate training while maintaining this advantage? Would techniques like accelerated sampling or reduced time steps affect the feature learning dynamics?
- Besides classification, how do diffusion models fare in other tasks like object detection, semantic segmentation, or even reinforcement learning? Are there any theoretical or empirical results that support the use of diffusion models in these more complex tasks?

### Soundness
3

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
2

### Summary
This paper provides a theoretical analysis of feature learning in diffusion models and contrasts that with feature learning in classification models. This work finds that diffusion models tend to prioritize learn balanced representations of the data whereas classification tends to prioritize learning easy to learn features of the data. 

As an applied researcher with no experience in the theory behind feature learning or theoretical analysis of neural networks, I honestly can’t explain how I was assigned this paper. As such it is difficult for me to judge the novelty, impact, and soundness of this work.

### Strengths
* The motivation and essential results were clear even to a non-expert in this subfield
* To the best of my knowledge no one has characterized the differences in feature learning in these settings.

### Weaknesses
 * I don’t find it particularly surprising that when training on Gaussian noised samples that the features learned would be broader than those trained on clean samples where small details that will be destroyed by Gaussian noise will still appear.


### Questions
* Would this analysis apply to the training of a classifier on the same levels of noise as a diffusion model? I.e. my question is whether these results apply specifically to diffusion models, or if they also apply to any model trained on all levels of (Gaussian?) noise. 
* Does this analysis also apply to flow-based models used in flow-matching? I would guess that this is likely and it may increase the impact of this work to study more general frameworks.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper focuses on the theoretical analysis of the feature learning framework of diffusion models. While previous studies have primarily analyzed the generative capabilities of diffusion models, this work examines how diffusion models differ from traditional supervised learning in terms of feature learning. Specifically, they show that, unlike classification models that tend to focus dominantly on either signal or noise, diffusion models learn features that are balanced with respect to signal and noise. They experimentally validate their theoretical claims using synthetic datasets and the MNIST dataset.

### Strengths
* They provide a theoretical analysis of the features learned by diffusion models, a relatively unexplored area. While diffusion models are often expected to have good representational capabilities due to their powerful generative capabilities, they provide a preliminary theoretical grounding for this expectation.

* The comparison between diffusion models and classification models, showing how they differ in feature learning, is interesting and meaningful. This work could contribute to the long-standing research on the discriminative vs. generative perspective in machine learning.

### Weaknesses
 * Comparison with other generative models, such as VAE, could be more informative. Diffusion models have unique features, such as the diffusion timesteps, that distinguish them from other generative models; an analysis of how these differences affect feature learning would add significant value. Specifically, a comparison should explore how the iterative denoising process in diffusion models, as opposed to the direct encoding/decoding in VAEs, impacts the learned feature representations and their sensitivity to noise.
* It would be beneficial to discuss how the theoretical results can be applied to real-world applications, even if only briefly, to provide practical relevance. For example, do the balanced features learned by diffusion models translate to improved performance in downstream tasks, such as robustness to adversarial attacks or better generalization in low-data regimes? This connection to practical scenarios needs to be explicitly addressed.
* The meaning of formulations could be further explained. For example, in Definition 2.1, it would be helpful to explain the rationale or significance of setting the variance of $\xi$ as defined.  Additionally, in Condition 3.1 (5), it would be useful to clarify whether the assumption of constant-order $\alpha_t$ and $\beta_t$ in diffusion models differs from conventional diffusion model formulations. It's important to clarify if this assumption limits the analysis to specific types of noise schedules or if it holds generally for common diffusion model setups.
* A detailed explanation of the theoretical differences between diffusion and classification models would be valuable. For example, diffusion models tie two layers, while classification models fix the second layer to ±1; it needs to be explained whether this difference affects the theoretical results. This analysis should delve into how these architectural choices impact the optimization landscape and the resulting feature representations.
* It would be helpful to know whether the theoretical analysis could also be applied to the score matching loss [1] and the reconstruction loss [2] in diffusion models. Specifically, it would be valuable to understand if the conclusions about balanced feature learning hold when training diffusion models with these alternative loss functions, and if so, how the analysis would need to be adapted.

### Questions
* Could the authors provide their thoughts on the issues raised in Weaknesses?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates feature learning for diffusion models through a theoritical approach. Under assumptions of two-class label setup and using certrain two-layer neural networks, the authors reveal an interesting difference between diffusion models and classification models.  Diffusion models learn both signal and noise in a "balanced way", where the "learning" grows proportionally to $\text{sample size} \times SNR^2$. In contrast, classification models tend to focus on certain features and exhist a "jump" learning behavior when $\text{sample size} \times SNR^2$ exceeds some threshold.

This paper provides theoritical supports for their findings as well as experiments on synthetical data and MNIST data.

### Strengths
1. The paper provides a noval perspective to understand the behavior of diffusion model: the feature learning. Defusion model learns feature over noise in a balanced manner. This addresses a gap in existing theoritical study that focuses mainly on distribution learning and convergance. This provides insights on why diffusion model could learn weak features.

2. The paper provides a rigourous theoritical framework and validate its results with numerical experiments. Experiments results clearly illustrate the feature learning patterns. 

3. The theoretical results are well-organized and explained.

### Weaknesses
1. Using SNR to demonstrate the feature learning pattern may oversimplify other factors. Real-world data can be heterogeneous, where signal structure and noise can vary significantly, making it unlikely to have a consistent SNR. The analysis focuses on a global SNR, neglecting the possibility of spatially varying signal-to-noise ratios within the same data sample. This could lead to different feature learning dynamics in different regions of the input space, which the current framework doesn't capture. Furthermore, the assumption that noise is unstructured and uniform may not hold in practice. Real-world noise often exhibits complex correlations and patterns, which could interact with the signal in non-trivial ways, potentially affecting the balanced learning behavior observed in the study.

2. The assumptions of orthogonal signals and a single feature seem quite strong. The orthogonality assumption, while simplifying the analysis, may not accurately reflect the complex relationships between features in real-world data. In practical scenarios, features are often correlated, and these correlations can significantly impact the learning dynamics. For instance, if two features are highly correlated, the model might learn one feature more easily than the other, even if their SNRs are similar. The single feature assumption also limits the generalizability of the results. In real-world datasets, multiple features often contribute to the signal, and the interplay between these features can influence the learning process. It is unclear how the balanced learning behavior would be affected by the presence of multiple, potentially correlated, features.

3. The synthetic data experiment settings are somewhat limited. Including more SNR settings could provide a better illustration of how feature learning behavior changes gradually with different SNR values. The current experiments only explore a few discrete SNR values, which may not fully capture the continuous spectrum of SNR variations. A more comprehensive exploration of the SNR space, with finer granularity, would provide a more robust understanding of the feature learning dynamics. Additionally, the synthetic data used in the experiments might not fully represent the complexity of real-world data, which often exhibits non-linear relationships and higher dimensionality. It would be beneficial to include experiments on more complex synthetic datasets, or even real-world datasets, to validate the findings.

### Questions
1. In Figure 6 of Appendix A.3, the seeting is described as high SNR, but the caption states "In this low-SNR case, we see classification tends to predominately learn noise while diffusion learns both signal and noise." Seems the caption is not consistent with the setting in the figure. Is my understanding correct?

2. Comparing the plot of difuusion model in left and right panel of figue 2, the $n \, SNR^2$ change significantly from 0.75 to 6.75. However, the ratio between  $max(w_r, \mu)$ and $max(wr, \xi)$ does not appear to change as dramatically much. Could you explain how this aligns with your theory results?  What is the motivation behind selecting 0.75 and 6.75 as low and high SNR settings? I am a bit curious if you have experimental results for other SNR values?

### Soundness
4

### Presentation
4

### Contribution
3
