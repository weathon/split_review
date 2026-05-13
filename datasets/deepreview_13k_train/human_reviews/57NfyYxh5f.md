# How to Probe: Simple Yet Effective Techniques for Improving Post-hoc Explanations

- Decision: Accept
- Scores: 6, 5, 6, 8

## Abstract
Post-hoc importance attribution methods are a popular tool for “explaining” Deep Neural Networks (DNNs) and are inherently based on the assumption that the explanations can be applied independently of how the models were trained. Contrarily, in this work we bring forward empirical evidence that challenges this very notion. Surprisingly, we discover a strong dependency on and demonstrate that the training details of a pre-trained model’s classification layer (<10% of model parameters) play a crucial role, much more than the pre-training scheme itself. This is of high practical relevance: (1) as techniques for pre-training models are becoming increasingly diverse, understanding the interplay between these techniques and attribution methods is critical; (2) it sheds light on an important yet overlooked assumption of post-hoc attribution methods which can drastically impact model explanations and how they are interpreted eventually. With this finding we also present simple yet effective adjustments to the classification layers, that can significantly enhance the quality of model explanations. We validate our findings across several visual pre-training frameworks (fully-supervised, self-supervised, contrastive vision-language training) and analyse how they impact explanations for a wide range of attribution methods on a diverse set of evaluation metrics.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper challenges the tradition notation that model explanations are independent of training methods by demonstrating that the quality of attributions for pre-trained models depends significantly on how the classification head is trained. It shows that using binary cross-entropy (BCE) loss instead of conventional cross-entropy (CE) loss leads to marked improvements in interpretability metrics across several visual pre-training frameworks. Furthermore, it is found that the non-linear B-cos MLP probes boost the class-specific localization ability of attribution methods.

### Strengths
1.	Clarity and Organization: The paper is exceptionally well-written and structured, enhancing readability and accessibility of the key finding
2.	The study reveals that training probes using binary cross-entropy (BCE) loss instead of the traditional cross-entropy (CE) loss consistently enhances interpretability metrics. The analysis of the Softmax Shift-Invariance Issue in interesting and insightful. This could have substantial implications for various DNN-based applications.
3.	The improvements in interpretability metrics are shown to be consistent across various training methods for the visual encoder. The robustness of these findings was thoroughly validated using diverse learning paradigms, including supervised, self-supervised and CLIP.

### Weaknesses
1.	(Major) Limited Model Diversity: The research exclusively utilizes the ResNet50 model backbone, which  canot adequately represent the behavior across various architectures. Testing additional backbones, especially Vision Transformers (ViTs), and incorporating explanation methods tailored for these models (referenced as [1][2][3]), would provide a more robust validation of the findings. Specifically, the behavior of attention-based explanation methods, such as those used in [1,2], can differ significantly from gradient-based methods used with CNNs, and this difference needs to be explored. Furthermore, the study should consider the impact of different architectural choices within ViTs, such as varying patch sizes and embedding dimensions, on the observed interpretability improvements.
2.	Inclusion of Additional Methods: The paper could be strengthened by including more population perturbation-based methods, such as RISE [4] and Score-CAM [5], to further substantiate the interpretability improvements. The current analysis primarily relies on gradient-based attribution methods, and expanding to perturbation-based methods would provide a more comprehensive view of the robustness of the findings. Specifically, methods like RISE, which sample input regions, and Score-CAM, which uses feature map weighting, can offer complementary perspectives on the attribution quality.
3.	Selection of Examples: Concerns arise regarding whether the examples shown in Figures 1 and 6 are cherry-picked, especially since the GridPG Score in Figure 5 suggests that the BCE model does not always perform perfectly. Including a broader range of examples, particularly where the BCE model scores lower on the GridPG, would offer a more comprehensive understanding and enhance the paper's credibility. The current selection of examples may not fully capture the variability in the performance of the BCE-trained models, and a more systematic approach to example selection is needed to ensure the generalizability of the findings.

### Questions
See weaknesses.

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper discovers and demonstrates the strong dependence of post-hoc importance attribution methods on the training details of the classification layer of the pre-trained model. Based on this findings, the paper also proposes a simple but effective adjustment to the classification layer to significantly improve the quality of model explanations.

### Strengths
This paper reveals and demonstrates the strong dependence of post-hoc importance attribution methods on the training details of the classification layer in pre-trained models.

### Weaknesses
1. The experimental method is limited to ResNet50, and the results are not extensive enough. Thus, experimental results are not convincing enough to verify the effectiveness of their methods.

2. The contribution of this article is not enough. The author discovered the impact of training details on post-processing methods, but the evaluation metrics used and the subsequent B-cos model are not the author's innovation.

3. [minor] Figures in this paper have obvious flaws. It will be better that authors carefully revise their figures.

### Questions
1. In the case of backbone freezing, increasing classifier parameters can improve performance. Is the design of B-cos MLP necessary? Is MLP not possible?
2. Can you provide more loss function results to verify Softmax Shift-Invariance? How about the cross-entropy loss?

### Soundness
2

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
4

### Summary
The main motivation behind this work is that two models using the same training regime and ending at the same loss can produce two extremely different attributions for the same image. The authors demonstrate that the training paradigm for the final classification layer of a network is the most important decider in generating more precise attributions, regardless of the attribution method. They specifically show that a binary cross entropy trained output layer produces better attributions than a cross entropy trained output layer. The increase in attribution quality does typically come at the cost of <10% accuracy reduction when using a linear layer, but the accuracy can be improved by using a more complex output layer.

### Strengths
Overall, it is an interesting read and demonstrates some interesting results. The writing is generally clear, the issue is well defined, and the experiments are impactful. It is difficult for me to say exactly what the authors did well, other than that it is a good read. 
    
1. In-depth motivation section, outlining the issues around generating consistently clear attributions
2. Plenty of qualitative results
3. Experiments over a variety of pre-trained models and datasets
4. The authors clearly show that this is an attribution-invariant issue.

### Weaknesses
There isn't any discussion of why there is an increase in accuracy and attribution quality with more complex output layers. Is it as simple as the layers being larger, or is there another reason? I assume proper train, test, and validation sets have been used?

### Questions
1. I am still confused as to why CE produces worse attribution than BCE. Could the authors explain this again?
    2. Also, why is it that the last output layer is so important? Why is the rest of the model have such little importance?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors find and support an interesting observation that the method of training the classifier layer of a model has a significant impact on the results of post-hoc attribution methods. Because many post-hoc attribution methods assume that model training does not have an impact, they find that this must be reconsidered, and in fact, simply modifying the method of training the last linear layer(s) can improve model accuracy and explainability.

### Strengths
This paper is very well written and planned. Not only are the approaches and findings very clear but the authors provide extensive support of their findings over numerous models, datasets, attribution methods, and metrics. 

The choice to study multiple pre-training approaches adds significant strength to their arguments and findings.  

The overall findings are simple, but impactful for future considerations of interpretable model design, post-hoc explainability, and improving model interpretation.

### Weaknesses
 There are not significant weaknesses to address. There are minor spelling mistakes, but it does not hurt the delivery of the information.

### Questions
Would the authors suggest the development of future classification models take into consideration the information in this paper?  

Do the authors think that a training loss could be created to further improve explainability as the minor differences in CE and BCE have a significant effect?

### Soundness
4

### Presentation
4

### Contribution
3
