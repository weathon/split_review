# F-Fidelity: A Robust Framework for Faithfulness Evaluation of Explainable AI

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Recent research has developed a number of eXplainable AI (XAI) techniques, such as gradient-based approaches, input perturbation-base methods, and black-box explanation methods.
Although extracting meaningful insights from deep learning models, how to properly evaluate these XAI methods remains an open problem.  
The most widely used approach is to perturb or even remove what the XAI method considers to be the most important features in an input and observe the changes in the output prediction.
This approach although efficient suffers the Out-of-Distribution~(OOD) problem as the perturbed samples may no longer follow the original data distribution. 
A recent method RemOve And Retrain (ROAR) solves the OOD issue by retraining the model with perturbed samples guided by explanations. 
However, the training may not always converge given the distribution difference.
Furthermore, using the model retrained based on XAI methods to evaluate these explainers may cause information leakage and thus lead to unfair comparisons.  
We propose Fine-tuned Fidelity (\ffid), a robust evaluation framework for XAI, which utilizes i) an explanation-agnostic fine-tuning strategy, thus mitigating the information leakage issue and ii) a random masking operation that ensures that the removal step does not generate an OOD input.
We designed controlled experiments with state-of-the-art (SOTA) explainers and their degraded version to verify the correctness of our framework.
We conducted experiments on multiple data structures, such as images, time series, and natural language. The results demonstrate that \ffid~significantly improves upon prior evaluation metrics in recovering the ground-truth ranking of the explainers. 
Furthermore, we show both theoretically and empirically that, given a faithful explainer, \ffid~metric can be used to compute the sparsity of influential input components, i.e., to extract the true explanation size.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a fidelity evaluation framework which utilizes an explanation agnostic fine tuning and a random mask generator which ensures that the generates input is not OOD. The efficacy of the proposed method if shown in various data types like images, time series etc.

### Strengths
1) The paper deals with important aspect of fidelity evaluation
2) The authors discuss about OOD issue during fidelity evaluation
3) The authors propose an approach to handle the issues and show the performance in different data types like images, time series and NLP.

### Weaknesses
W1) In section 3, it is mentioned in lines [215 to 222] that the size of the removed part is upper bounded by a fraction of the input and not a fraction of the explanation. It would be helpful to the readers if the authors could explain what they mean by "removed," as it might mean different in tabular data and images. Further, the authors should also explain how their strategy of selecting a fraction of input and not explanation addresses the OOD issue.

W2) In lines[224:235], the authors use fine tuning to address the problem of robustness of the classifier for small perturbations(mentioned in lines [213:214]). However, at least from the perspective of images, it is unclear how applying a mask of {0,1} on random patches of an image can be considered as a perturbation. It is not clear how this relates to the concept of small perturbations, and it would be beneficial to see a comparison with more traditional perturbation methods.

W3) Further, the fine-tuning process mentioned in lines[224:235] seems like retraining the classifier with occlusion (for image classifiers). The authors should explain how their method won't change the decision boundary drastically so that their approach can be called fine-tuning and not training a different classifier altogether.

W4) The authors should explain why explaining the fine-tuned classifier is equivalent to explaining the original classifier (as mentioned in line[224])

W5) For the ease of readers, the authors should explain more about GT and how they extract it(in Section 4)

W6) It needs to be clarified to see why F-Fidelity performs worse than vanilla Fidelity and R-Fidelity for SST2 dataset with LSTM (Table 8). The authors are requested to explain this phenomenon in detail for the ease of readers.

### Questions
Questions are as below

#### W1:
- a) Provide specific examples of how "removal" is implemented for different data types like images, tabular data, and text.
- b) Give a more detailed explanation of how bounding the removed portion to a fraction of the input, rather than the explanation, helps mitigate OOD issues.

#### W2:
- a) Elaborate on how the random masking process relates to or simulates small perturbations, particularly in the context of image data.
- b) Provide examples or visualizations that demonstrate how this masking approach compares to traditional perturbation methods.
- c) Present empirical evidence or theoretical justification for why their masking approach is an effective way to improve classifier robustness.

#### W3:
- a) Provide empirical evidence or theoretical justification for why their fine-tuning process preserves the original classifier's decision boundaries.
- b) Compare the original and fine-tuned classifiers' outputs on a test set to demonstrate the degree of change.

#### W4:
- a) Provide theoretical or empirical evidence demonstrating the equivalence between explanations of the original and fine-tuned classifiers.
- b) Include a comparison of explanations generated for both classifiers on a set of test examples.

#### W5:
- a) Provide a step-by-step description of how they generate or obtain the ground truth (GT) explanations, including any assumptions made in this process.
- b) Include examples of GT explanations for different data types.

#### W6:
- a) Provide a detailed analysis of why F-Fidelity underperforms on this specific dataset and model combination.
- b) Investigate potential reasons, such as dataset characteristics, model architecture specifics, or hyperparameter settings that might contribute to this result.
- c) Discuss the implications of this finding for the broader applicability of their method.
- d) Consider conducting an ablation study to isolate the factors contributing to this performance difference.

The paper addresses an important aspect of fidelity evaluation and the issue of OOD while doing it. Overall, I like the central theme of the paper and that’s why I am leaning towards mild acceptance but I would like the authors to address the points in the weakness section and the questions in this section.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a new attribution evaluation framework which attempts to solve existing issues in current metrics such as the OOD problem from perturbation metrics, and the information leakage of fine-tuning methods like ROAR. To do this, the authors propose limiting the size of the perturbations made to each image and performing fine-tuning on images randomly masked under this perturbation size limitation.

### Strengths
From their experiments which cover a broad range of applications and datasets, it seems this new method does improve over existing methods in rank correlation tests, indicating its ability to fairly and consistently sort attributions under evaluation. 

The solutions presented are simple.

### Weaknesses
I do not think the intuition behind the solutions is entirely clear and I do not think the presentation of the solutions is clear.  

The choices for multiple hypermeters are not indicated. 

More attribution methods should have been employed for a better representation of the existing space.

The ablation study provided regarding B selection suggests this value can approach 1 (i.e. this is the same as if the value was not implemented) and the correlation scores would be good. Is this true? If so, what use does B have? In addition, what value of B is used and how was it selected? 

What is the intuition for fine tuning with the image perturbation limitation? I do not see why fine-tuning under image perturbed by random masks instead of perturbed explanations is better either. It is not obvious that this skirts the OOD problem. 

What is the value of being able to extract the explanation size? The motivation for this is lacking and it is not clear why it is important or interesting.

### Questions
The ablation study provided regarding B selection suggests this value can approach 1 (i.e. this is the same as if the value was not implemented) and the correlation scores would be good. Is this true? If so, what use does B have? In addition, what value of B is used and how was it selected? 

What is the intuition for fine tuning with the image perturbation limitation? I do not see why fine-tuning under image perturbed by random masks instead of perturbed explanations is better either. It is not obvious that this skirts the OOD problem. 

What is the value of being able to extract the explanation size? The motivation for this is lacking and it is not clear why it is important or interesting.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors presented F-fidelity, a new metric for evaluating the faithfulness of attribution methods. Traditional evaluation methods such as MoRF and LeRF suffer out-of-distribution(OOD) issue, and ROAR method suffers information leakage issue. F-fidelity overcomes these limitations through two strategies. 1. explanation-agnostic fine-tuning, which fine-tunes the model using stochastic masking operations. 2. a controlled random masking operation to overcome the OOD issue, by applying a random masking operation conditioned on the explainer's output so that removal of input features does not produce OOD samples. The authors conducted controlled experiments with other explainers. Moreopver, they showed that F-fidelity can be used to determine the sparsity of influential input components.

### Strengths
The paper is well written, especially introduction section and preliminary section.

The paper effectively tackles the OOD problem inherent in traditional removal-based evaluation methods. This is a crucial issue because OOD inputs can lead to unreliable assessments of an explainer's faithfulness.

The authors conducted extensive experiments across broad data, such as images, time series, and natural language processing.

The method is well mitigate limitation of prior methods; Addresses the information leakage issue and OOD issue at once.

The paper provides theoretical analysis demonstrating that F-Fidelity can recover the sparsity of the ideal SHAP explanations.

The paper introduces a novel approach by assuming that an explainer is better the closer it is to an ideal Shapley value explainer. This assumption is appealing because Shapley values provide a theoretically sound basis for feature attribution.

### Weaknesses
Lack of Visualizations Demonstrating F-Fidelity's Effectiveness. The paper does not include figures or visualizations that illustrate the effectiveness of F-Fidelity. Providing attribution maps or examples where there is a significant discrepancy between F-Fidelity and other evaluation metrics would enhance understanding and make the results more tangible. Visual comparisons could help readers better appreciate the advantages of F-Fidelity over existing methods. For example, Attribution map between samples that have discrepancy between F-Fidelity and MoRF - LeRF.

Novelty issue. Though theoretical availability of extracting the size of the ground-truth explanation is novel, the core difference between F-fidelity and R-Fidelity is introducing an upper bound on the fraction of input elements removed. This extension seems an incremental refinement rather than a fundamental novel idea.

Limited Explanation of Ground Truth. The paper's approach to establishing ground truth rankings involves using Integrated Gradients with systematically added noise levels. However, Integrated Gradients is known to be less faithful than some state-of-the-art explanation methods, such as the LRP (Layer-wise Relevance Propagation) family or LayerCAM. This raises concerns about whether the ground truth used is an appropriate benchmark. As the authors discuss ideal Shapley value explainers in Section 5, utilizing Shapley values as the ground truth might have been more appropriate to align with their theoretical framework.

Insufficient Clarification on the Importance of Macro Correlation. The paper could benefit from a more thorough explanation of why macro correlation between different evaluation methods is important. It was not immediately clear how macro correlation demonstrates the usefulness of F-Fidelity. Including figures or visual aids that depict the relationship between macro correlation and the effectiveness of F-Fidelity would help clarify this point and strengthen the argument.

Limited Variety of Explanation Methods Evaluated. The experiments involve a relatively small number of explanation methods. Comparing F-Fidelity scores across a wider range of explainers would provide a more comprehensive evaluation. For instance, methods like LayerCAM and LRP family are known to have higher fidelity than GradCAM, and GradCAM typically outperforms the pure gradient. Demonstrating whether F-Fidelity can reflect these known differences in fidelity would enhance the paper's validity.

Practical Challenges in Determining Explanation Size (c₁). In the section 6, the size of the most influential tier (c₁) is assumed to be known. However, in real-world applications, c₁ is not readily observable. It would have been beneficial if the authors had demonstrated how c₁ could be estimated or inferred from practical data, such as through experiments on datasets like ImageNet. Providing practical guidance on determining c₁ would make the theoretical contributions more applicable.

Misclassification and FFid+ Score: While the model may misclassify an input image, this often occurs because the image contains features that align with the misclassified label. For instance, if an image of a border collie is misclassified as a collie, it is likely due to the shared features between these two categories. Since most misclassified images also exhibit high confidence in the original label, it is less convincing to attribute a negative FFid+ score solely to the misclassification. Additionally, the variance in FFid scores is notably high, making it difficult to conclusively claim that Grad-CAM provides a better explanation than the saliency method based on FFid alone. For example, the standard deviation across the five samples exceeds 0.33, which is significantly greater than the observed difference in FFid scores.

Attribution Map Sparsity: Some methods favor less fine-grained attribution maps, yet sparsity is a key desideratum for saliency methods. For example, the MoRF insertion metric tends to favor Grad-CAM over Guided Backpropagation, even though Guided Backpropagation can be considered a more fine-grained representation of Grad-CAM. This phenomenon is largely due to out-of-distribution (OOD) issues. I would anticipate that Guided Backpropagation would achieve a higher F-Fid score. Could the authors provide results comparing the two methods?

Decision Boundary and Practicality: The equivalence between the original and fine-tuned models is critical for practical applications, as these are essentially different models with distinct weights. Although the authors demonstrated equivalence using both global and local decision boundaries, a key practical concern remains: ensuring equivalence between the two models may require a substantial dataset for fine-tuning. This requirement could pose significant challenges in scenarios where access to large datasets is limited, such as in the medical domain.

### Questions
1. I couldn't find how Pan et al., 2021, or Zhu et al., 2024 utilized macro correlation in their work. Can you explain how they employed macro correlation and how it relates to your citation of their work?

2. In Section 6, it seems that both MoRF and LeRF conditions would be satisfied equally. This is because deleting or inserting features based on the gamma value would maximize the MoRF-LeRF difference. I'm uncertain whether this experiment effectively demonstrates that F-Fidelity can distinguish explainers that are closer to the ideal Shapley explainer than other metrics. Could you clarify how this experiment supports that claim?

3. Regarding computational resources, I would like to know how much computational effort your method requires. One of the primary reasons ROAR isn't widely adopted is not just due to information leakage but also because of its significant computational cost. It would be helpful if you could provide details on the computational resources required for F-Fidelity and how they compare to those needed for ROAR.

** Typo : in figure 1, the y-axis label is RFid.

### Soundness
3

### Presentation
2

### Contribution
3
