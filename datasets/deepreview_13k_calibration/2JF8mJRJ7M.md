# Lipsum-FT: Robust Fine-Tuning of Zero-Shot Models Using Random Text Guidance

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Large-scale contrastive vision-language pre-trained models provide the zero-shot model achieving competitive performance across a range of image classification tasks without requiring training on downstream data. Recent works have confirmed that while additional fine-tuning of the zero-shot model on the reference data results in enhanced downstream performance, it compromises the model's robustness against distribution shifts. Our investigation begins by examining the conditions required to achieve the goals of \textit{robust fine-tuning}, employing descriptions based on feature distortion theory and joint energy-based models. Subsequently, we propose a novel robust fine-tuning algorithm, \texttt{Lipsum-FT}, that effectively utilizes the language modeling aspect of the vision-language pre-trained models. Extensive experiments conducted on distribution shift scenarios in DomainNet and ImageNet confirm the superiority of our proposed \texttt{Lipsum-FT} approach over existing robust fine-tuning methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper points out that fine-tuning zero-shot model like CLIP can improve downstream performance, however, the accuracy of the fine-tuned model falls short of the original zero-shot model across distribution shifts. To address the chanllenge of robust fine-tuning, authors first delve into the problem by employing feature distortion theory and joint energy-based models. Subsequently, they introduce a novel robust fine-tuning algorithm called Lipsum-FT. This approach leverages random text guidance as a regularization technique during the fine-tuning process to minimize the change in energy. Authors conduct extensive experiments on two datasets to demonstrate the effectiveness of the proposed approach in addressing distribution shift scenarios.

### Strengths
1. This paper investigate the trade-off between the reference and distribution shift data when fine-tuning the zero-shot CLIP model, utilizing feature distortion theory and joint energy-based models as analytical tools.
2. This paper proposes a simple and effective regularization term based on the correlation between the similarity of vision features and text features derived from the fine-tuned model and original model respectively. Specifically, the text tokens are generated randomly.
3. The proposed method outperforms the original zero-shot model and exisiting robust fine-tuning methods in both reference and shift domains, demonstrating its superior performance in handling distribution shifts.

### Weaknesses
1. It would be benefical if authors could include visualizations of $v_{\theta, \phi}(x)$ and $v_{\theta_0,\phi}$ to provide an inituitive understanding of the distinctions between the original zero-shot model, the fine-tuned model with exisiting methods, and the fine-tuned model with the proposed emthod. Specifically, visualizing the high-dimensional feature vectors using dimensionality reduction techniques like t-SNE or PCA would help to illustrate how the feature space is altered by different fine-tuning approaches. Showing the clustering of features from different domains before and after fine-tuning could provide a more intuitive understanding of the method's effectiveness in preserving the original feature space while adapting to the target domain.
2. Expanding the experiments to involve various domains as reference data for fine-tuning and using other domains for evaluation would enhance the comprehensiveness of the study. This approach can shed light on the adaptability and robustness of the proposed method in different real-world scenarios. For example, using datasets with varying degrees of domain shift, such as synthetic to real or different image styles, would provide a more thorough evaluation of the method's generalization capabilities. It would also be beneficial to explore scenarios where the reference data is significantly different from the evaluation data, to test the limits of the proposed approach.
3. It remains unclear whether there exists a weight for incorporating the regularization term proposed in Eq. (7) into the loss function. In Appendix B.2, authors have discussed existing methods that involve weights related to the regularization term, such as $\lambda_{L2SP}$ in Eq. (10), $\lambda_{KD}$ in Eq. (12), and $\lambda_{CAR-FT}$ in Eq. (12). Authors have also detailed how to select these hyperparameters. However, there seems no mention of how the weight for the proposed method is determined. The lack of clarity on how this weight is chosen makes it difficult to assess the method's robustness and reproducibility. A more detailed explanation of the hyperparameter selection process is needed.
4. The precision of the standard deviation values in Table 2(b) should be improved. The values of NLL are presented accurately to two decimal places, whereas the standard deviation values are limited to only one decimal place, with many of them showing as 0.0. Ensuring consistent precision in reporting these values would enhance the clarity and reliability of the results. The standard deviation values are crucial for understanding the variability of the results, and reporting them with insufficient precision can obscure important information.
5. There may be a typo in the gradient descent update rule presented in Eq. (9). It should be as follows: $\theta_t = \theta_{t-1} - \eta \nabla_\theta L_{CE}(\theta)$. It's advisable for the authors to thoroughly review other equations to ensure they are accurately represented.
6. It would be interesting to know if the proposed method is applicable to various fine-tuning techniques, such as adapters, LoRA, and prompt tuning. The authors should discuss the compatibility of their regularization approach with different fine-tuning strategies. Specifically, it would be useful to understand whether the method can be applied when only a subset of the model parameters are updated, as is the case with adapters and LoRA, or when the model is tuned via prompt learning.

### Questions
1. It remains unclear whether there exists a weight for incorporating the regularization term proposed in Eq. (7) into the loss function. In Appendix B.2, authors have discussed existing methods that involve weights related to the regularization term, such as $\lambda_{L2SP}$ in Eq. (10), $\lambda_{KD}$ in Eq. (12), and $\lambda_{CAR-FT}$ in Eq. (12). Authors have also detailed how to select these hyperparameters. However, there seems no mention of how the weight for the proposed method is determined.
2. The precision of the standard deviation values in Table 2(b) should be improved. The values of NLL are presented accurately to two decimal places, whereas the standard deviation values are limited to only one decimal place, with many of them showing as 0.0. Ensuring consistent precision in reporting these values would enhance the clarity and reliability of the results.
3. There may be a typo in the gradient descent update rule presented in Eq. (9). It should be as follows: $\theta_t = \theta_{t-1} - \eta \nabla_\theta L_{CE}(\theta)$. It's advisable for the authors to thoroughly review other equations to ensure they are accurately represented.
4.It would be interesting to know if the proposed method is applicable to various fine-tuning techniques, such as adapters, LoRA, and prompt tuning.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a fine-tuning model, Lipsum-FT, by utilizing the language modeling aspect of the vision-language pre-trained models for zero-shot classification.

### Strengths
This paper proposed a fine-tuning model, Lipsum-FT, by utilizing the language modeling aspect of the vision-language pre-trained models for zero-shot classification. Lipsum-FT as an incremental algorithm enhances the robustness of zero-shot models by combining language and visual information.

### Weaknesses
The motivation is unclear. The authors mention a problem with cross-distribution shifts, but Lipsum-FT is a fine-tuning model.

What means of four distribution shifts DomainNet-{P, C, I, S}. Figure 1 fails to represent the distribution shifts.

There are too many contents that need to be referred to Appendix. Please reduce some important Appendix contents and put them into the text.

It looks like capturing correlations between images and each language by calculating their inner product vectors in Equation 8. The meaning of Equation 8 wants to express is to match all the language information one by one or to match the current m-th information? If it matches M language information, how much does the algorithm complexity increase? What is the significance of matching with alonely m-th?

Lack of complexity analysis on the Lipsum-FT algorithm and its impact on the experiments.

### Questions
What means of four distribution shifts DomainNet-{P, C, I, S}. Figure 1 fails to represent the distribution shifts.

There are too many contents that need to be referred to Appendix. Please reduce some important Appendix contents and put them into the text.

It looks like capturing correlations between images and each language by calculating their inner product vectors in Equation 8. The meaning of Equation 8 wants to express is to match all the language information one by one or to match the current m-th information? If it matches M language information, how much does the algorithm complexity increase? What is the significance of matching with alonely m-th?

Lack of complexity analysis on the Lipsum-FT algorithm and its impact on the experiments.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on the problem of robust fine-tuning a large-scale vision-language pre-trained model, which is expected to obtain enhanced downstream performance while maintaining its accuracy across distribution shifts on zero-shot tasks. By investigating the behavior under the perspectives of feature distortion theory and joint energy-based models, the authors propose a robust fine-tuning algorithm Lipsum-FT. Experimental results on DomainNet and ImageNet proves effectiveness of their proposed method.

### Strengths
1. This paper focuses on the problem of how to maintain the performance of a zero-shot model on distribution shift data while improving its performance on reference data during fine-tuning, which is an important and valuable topic.
2. The proposed method is easy to realize since it simply introduces an extra regularization term.
3. The idea of utilize the language model to construct regularization on the vision model is interesting.
4. The English writing is good and I do not find obvious grammar errors or typos.

### Weaknesses
1. I am not sure whether the novelty of this paper can be regarded as significant. It just introduces a regularization item to make the vision model keep the original inner products with features generated by the language model after fine-tuning.
2. The illustration organization of this paper is not clear enough. Therefore, even though the key idea is not so complicated, I find it difficult to understand the viewpoint quickly.

### Questions
1. As the main contribution of this paper is to utilize the regularization term in (7) to minimize the energy gap in (6), please explain why the energy gap is chosen for improving the robustness of zero-shot model fine-tuning. Why is it defined to be the squared difference of two inner products as in (6)?
2. Could the authors give more details about how the tokens $\mathbf{t}$ are generated? The authors just assert that they are generated randomly from the vocabulary. I also want to know what types of texts are used for constructing such regularization and to what extent it covers the common used semantic information.
3. How much extra computation are introduced by such a regularization term?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a method named LIPSUM-FT for zero-shot robust fine-tuning. Specifically, the authors, by observing the relationship between accuracy and energy gap under distribution shift, propose enhancing the accuracy of fine-tuned pre-trained models under distribution shifts by reducing the energy gap. The experimental results demonstrate that the method proposed in this paper can effectively improve the performance of CLIP during zero-shot fine-tuning.

### Strengths
1. The authors explain the performance degradation of fine-tuned pre-trained models under distribution shifts from the perspective of energy models.

2. The proposed LIPSUM-FT effectively enhances the robustness of fine-tuned pre-training.

3. Ablation studies indicate that LIPSUM-FT is insensitive to random token lengths and token quantities.

### Weaknesses
1. Utilizing energy models to explain the fine-tuning of pre-trained models seems not to be essential. As per my understanding, the objective of the method in this paper as well as related methods is to reduce the difference in features extracted by the models before and after fine-tuning. While the authors frame their approach through the lens of energy-based models, the core mechanism appears to be more directly related to feature preservation, which is already explored by other methods. The connection to energy models, while potentially interesting, does not seem fundamental to the method's effectiveness.

2. The authors claim that the text used is randomly generated, but it appears from the code in the supplementary material that tokens are sampled from the openai_imagenet_template. According to CAR-FT, using all templates as text input also yields good performance. What then is the significance of random token sampling in this scenario? The use of a fixed template set for text generation, even if randomly sampled, raises questions about the generality of the approach. It's unclear if the observed performance gains are specific to this particular template set or if they would generalize to truly random text inputs.

3. It is suggested that the authors provide a brief introduction to energy models in the related work section. In Figure 1, it is not mentioned which points different learning rates in the left graph and different steps in the right graph correspond to. This lack of clarity makes it difficult to interpret the results presented in the figure and understand the relationship between the energy gap and the fine-tuning process.

### Questions
The authors claim that the text tokens are randomly generated. What are the specific rules for generation?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
