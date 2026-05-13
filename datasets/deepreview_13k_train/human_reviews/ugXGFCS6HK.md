# Discriminating image representations with principal distortions

- Decision: Accept
- Scores: 6, 5, 6, 8, 6

## Abstract
Image representations (artificial or biological) are often compared in terms of their global geometry; however, representations with similar global structure can have strikingly different local geometries. Here, we propose a framework for comparing a set of image representations in terms of their local geometries. We quantify the local geometry of a representation using the Fisher information matrix, a standard statistical tool for characterizing the sensitivity to local stimulus distortions, and use this as a substrate for a metric on the local geometry in the vicinity of a base image. This metric may then be used to optimally differentiate a set of models, by finding a pair of ``principal distortions'' that maximize the variance of the models under this metric. We use this framework to compare a set of simple models of the early visual system, identifying a novel set of image distortions that allow immediate comparison of the models by visual inspection. In a second example, we apply our method to a set of deep neural network models and reveal differences in the local geometry that arise due to architecture and training types. These examples highlight how our framework can be used to probe for informative differences in local sensitivities between complex computational models, and suggest how it could be used to compare model representations with human perception.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel metric on image representations to measure differences in local geometry. The authors then leverage this metric to generate "principal distortions" that maximize variance across a set of models. Experimental results of the proposed method reveal qualitative differences in the local geometry of ResNet50 and AlexNet, which is quite interesting.

### Strengths
- This is well-written and organized paper; hence it is easy for readers to follow. 
 
- The concept of exploring the local geometry of deep networks and examining the interplay between local geometry and the global structure of images is compelling.

- Developing a novel metric to compare two image representations is highly innovative.

### Weaknesses
 - While the proposed method of using the Fisher Information Matrix to measure the sensitivity of a representation to a stimulus distortion seems reasonable, its effectiveness as a metric is unclear, or difficult to justify. Specifically, the paper does not sufficiently demonstrate that the FIM captures meaningful differences in local geometry beyond simple sensitivity to image perturbations. The connection between the FIM and the actual geometric properties of the representation space remains tenuous.

- Identifying the types of principal distortions to which the network is most sensitive is an interesting idea. However, the proposed method lacks a good validation plan to confirm the accuracy or reliability of these findings. The paper presents qualitative results, but it is unclear if these distortions are consistent across different images or if they are specific to the chosen examples. Furthermore, the method does not provide a clear way to quantify the significance of the identified principal distortions or to compare them across different models in a statistically rigorous manner.

### Questions
- How is the stimulus-dependent function $f(s)$, defined after Eq. (1), computed in practice?  
- If $I(s)$ is positive semi-definite, this seems to cause issues with the metric defined in Eq. (3) when it approaches zero.   
- How are two image representations obtained from a single image $S$? Are $I_A(S)$ and $I_B(S)$ learned by different neural networks? Please clarify. 
- How are the coefficients for $\epsilon_1$ and $\epsilon_2$ determined in the proposed approach?  
- The interpretation and justification of the estimated principal distortions are difficult to justify. For instance, in Fig. 3, while the finding that AlexNet and ResNet are more sensitive to complementary parts of the images is interesting, its validity is unclear. Providing additional justification would strengthen the claims. One possible approach is to introduce adversarial noise to different parts of the images and evaluate its impact on downstream classification tasks, e.g., comparing the performance drop across different parts of the images.  
- This reviewer finds it difficult to connect the identified distortions with the concept of local geometry. The method appears to focus more on differences in image intensities and textures. However, it is possible that this reviewer has misunderstood some aspects of the proposed approach. Please clarify.

### Soundness
3

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
4

### Summary
The paper proposes a novel framework to compare local geometry within image representations, arguing that image representation encompasses both global and local geometry information. The authors introduce a method to quantify the local geometry of image representations using the Fisher information matrix and statistical techniques sensitive to local stimulus distortion. This approach aims to identify "principal distortions pairs," which maximize model variances and serve as optimal discriminative tools for evaluating model performance.

### Strengths
The framework's focus on comparing local geometry is innovative, and the use of the Fisher information matrix and sensitivity to local distortions represents a unique approach to quantifying image representation. This novel method to derive principal distortion pairs that maximize model variance offers a potentially valuable tool for model discrimination.

### Weaknesses
Model Selection: The authors demonstrate the metric’s functionality using older architectures, specifically AlexNet and ResNet. Given that AlexNet is largely obsolete in current practical applications, the paper would benefit from extending the evaluation to more contemporary and widely-used networks (e.g., EfficientNet, Vision Transformers). Demonstrating the framework's effectiveness across a variety of modern architectures would strengthen the claim that the metric is universally applicable and capable of distinguishing models.

Practical Utility and Generalizability: The manuscript does not clearly establish the practical relevance and utility of this framework in real-world applications. A more explicit discussion on the potential benefits of this metric in actual deployment scenarios, or in improving model interpretability and selection, would add significant value. Additionally, empirical results supporting the framework’s effectiveness across diverse, practical model architectures are essential to substantiate the generalizability and robustness of the proposed approach.

### Questions
Model Selection: The authors demonstrate the metric’s functionality using older architectures, specifically AlexNet and ResNet. Given that AlexNet is largely obsolete in current practical applications, the paper would benefit from extending the evaluation to more contemporary and widely-used networks (e.g., EfficientNet, Vision Transformers). Demonstrating the framework's effectiveness across a variety of modern architectures would strengthen the claim that the metric is universally applicable and capable of distinguishing models.

Practical Utility and Generalizability: The manuscript does not clearly establish the practical relevance and utility of this framework in real-world applications. A more explicit discussion on the potential benefits of this metric in actual deployment scenarios, or in improving model interpretability and selection, would add significant value. Additionally, empirical results supporting the framework’s effectiveness across diverse, practical model architectures are essential to substantiate the generalizability and robustness of the proposed approach.

### Soundness
3

### Presentation
3

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
This paper proposes a framework for comparing image representations regarding their local geometries through the Fisher information matrix by finding a pair of “principal distortions” that maximize the variance of the models under this metric. The experiments include (1) comparing a set of simple models of the early visual systems and 2) comparing a set of deep neural network models to reveal differences in the local geometry that arise due to architecture and training types.

### Strengths
1. The idea is simple but effective -- as the first approach to compare more than two models.
2. The problem statement and method description are well-written and clear to understand.
3. The experiment result is interesting, with meaningful discussions about texture bias and adversarial vulnerability. Visualizations are very helpful. 
4. The supplementary is very informative.

.

### Weaknesses
1. It is not clear how this paper's principal distortions relate to human sensitivity. There seem to be no experiments to prove this statement, such as using human observers for evaluation of the principle distortions [1]. Specifically, the paper does not address whether the identified principal distortions are perceptually relevant or if they simply reflect mathematical properties of the Fisher information matrix. The lack of a psychophysical validation leaves a gap in demonstrating the practical relevance of the proposed method.
2. For example, in 4.1 Early Vision Models, it is not stated how to determine the effectiveness of this approach. There is no quantitative evaluation, and it is unclear how to understand the visualizations of the principle distortion images. The analysis relies solely on visual inspection of the distortion patterns, which is subjective and lacks a clear metric for comparison. Without a quantitative measure, it is difficult to assess the significance of the observed differences between models.
3. Are there some practical applications of this approach? Or how to use visualizations of principle distortions? The paper does not provide concrete examples of how the principal distortions can be used in practice. It remains unclear how these visualizations can be leveraged for model improvement, transfer learning, or other practical applications. The lack of practical use cases limits the impact of the proposed method.
4. What kind of networks can be compared with this approach? Only networks for classifications? How about the models for detections, segmentations, and other applications? The paper focuses primarily on classification networks and does not explore the applicability of the method to other types of models. It is unclear whether the method can be generalized to models trained for tasks such as object detection, semantic segmentation, or generative modeling. The lack of discussion on the method's versatility limits its scope.
5. This paper is over nine pages.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

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
The paper introduces a new method for comparing vision models that map input images to stochastic representations, leveraging the Fisher Information Matrix (FIM) to analyze the local geometry of image representations. This approach allows for the comparison of multiple models, including computational models of the visual system and deep neural networks (DNNs). By focusing on relative sensitivities to principal distortion directions in the stimulus (image) space, the method reveals differences between models that are not captured by global geometric approaches such as representational similarity analysis (RSA). The authors demonstrate the utility of their method through computational studies, showing consistent findings with previous research on early visual system models and uncovering differences in local image representations between models like AlexNet and ResNet50.

### Strengths
- The paper is clearly written and easy to follow, with a strong motivation that outlines how it builds on previous work.
- Presents a new method to compare the local geometry of image representations between models, generalizing prior approaches to accommodate multiple models.
- The method uncovers differences invisible to global geometric approaches, providing deeper insights into model behaviors.
- Includes several computational experiments that support the method's effectiveness and relevance.
- Discusses potential applications in studying biological vision, DNNs, and the interplay between them.
- Offers a well-rounded discussion that contextualizes the findings within the field.

### Weaknesses
 - The technical advancement may be seen as an incremental improvement over existing metrics.
- The method primarily applies to stochastic representations, which are uncommon in DNNs; applying it to deterministic models may seem arbitrary.
- It is not entirely clear how the proposed local metric can be aggregated to provide global insights across different stimuli or datasets.

### Questions
1. How do you plan to extend this work to achieve more quantitative results? For instance, do you have ideas on quantifying the distinction between "noisy" versus "smooth" image distortions?
2. The authors essentially present a metric between models, which is based on the model’s representations for a single stimulus. It seems to me that the results and conclusions drawn from them could potentially disagree for different stimuli. How do you either choose a representative stimulus or how do you choose multiple and how could the results be aggregated?
3. How does your approach compare to, or how could it be integrated with, explainability methods based on saliency or relevance maps?
4. Could you clarify how you scaled the relative sensitivities between models of the early visual system (as mentioned on pages 5 and 6)? A revision of this explanation might enhance understanding.
5. Can you speculate on how the observed differences in sensitivity to noisy distortions between AlexNet and ResNet50 relate to their architectural differences or inductive biases?

Additional feedback:
- For deterministic representations in DNNs, the application of the FIM might seem less direct. It would be beneficial to elaborate on this aspect, perhaps by relating it to concepts like the pullback of the Euclidean metric onto the image space.
- Strengthening the discussion of experimental results and their key takeaways would enhance the paper. Specifically, clarifying how principal distortions inform us about a model's alignment with human visual representation, responses to adversarial examples, and contributions to interpretability would be valuable.
- Introducing more quantitative analyses or metrics could solidify the results and provide stronger evidence of the method's effectiveness.

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
3

### Summary
The paper proposes a method to compare image representations by analyzing local geometries using the Fisher information matrix, enabling differentiation of models based on local sensitivity to distortions. For comparison, it has been applied to both early visual system models and deep neural networks, the method enables comparison of multiple models (>2) and can be used to compare model representations with human perception.

### Strengths
I found the paper's topic interesting and overall the language of the paper was clear. The paper targets an important problem in cognitive science and is a step toward understanding visual models better. The figures and qualitative results were sufficient to understand the concept and the differences. The paper is also based on a sound experimental framework to investigate the source of variability in results from both training data and architectural design.

### Weaknesses
I have a few questions and would like to know the authors' response to them:

1. (minor) It has been claimed in Figure 4 that the differences between AlexNet and ResNet come from the architecture than the training procedure. There is always randomness in the training where initialization of the model's weights and also the random split of data can effect one single model's performance. In fact, the model output may change if we train it on different seeds. I am wondering wouldn't that be a better approach to replicate the results on models trained on at least three different seeds? (basically 3 different versions of a model)

2. (minor) I expected to see a candidate from Transformers in the experiments, however, there was no candidate from those (currently) popular models. Can authors justify why they have not included any transformers such as ViT or Swin?

3. With Transformers, it has been a trend to show the attention maps (on tokens of an image) and show the behavior of the model. I am wondering if the authors can comment on this. Can the distortion maps be correlated to attention maps? This can ideally (if correlated) help with the explainability of attention-based models.

4. (major) Currently the manuscript is heavily populated with qualitative results. I strongly suggest the authors add a per-class sensitivity distribution for the dataset they are using for different models. This helps to understand on a population level and over different classes which models are more sensitive to high freq. localities and which ones are not.

5. I could not find a Dataset section in the manuscript :) Adding an independent dataset section would make it easier to understand the scale of experiments. currently, it is hard to find within the text

### Questions
mentioned everything in weaknesses

### Soundness
4

### Presentation
3

### Contribution
3
