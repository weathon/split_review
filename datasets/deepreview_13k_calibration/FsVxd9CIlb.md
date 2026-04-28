# AttEXplore: Attribution for Explanation with model parameters eXploration

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Due to the real-world noise and human-added perturbations, attaining the trustworthiness of deep neural networks (DNNs) is a challenging task. Therefore, it becomes essential to offer explanations for the decisions made by these non-linear and complex parameterized models. Attribution methods are promising for this goal, yet its performance can be further improved. In this paper, for the first time, we present that the decision boundary exploration approaches of attribution are consistent with the process for transferable adversarial attacks. Specifically, the transferable adversarial attacks craft general adversarial samples from the source model, which is consistent with the generation of adversarial samples that can cross multiple decision boundaries in attribution. Utilizing this consistency, we introduce a novel attribution method via model parameter exploration. Furthermore, inspired by the capability of frequency exploration to investigate the model parameters, we provide enhanced explainability for DNNs by manipulating the input features based on frequency information to explore the decision boundaries of different models. Large-scale experiments demonstrate that our \textbf{A}ttribution method for \textbf{E}xplanation with model parameter e\textbf{X}ploration (AttEXplore) outperforms other state-of-the-art interpretability methods. Moreover, by employing other transferable attack techniques, AttEXplore can explore potential variations in attribution outcomes. Our code is available at: https://github.com/LMBTough/ATTEXPLORE.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new attribution technology AttExplore that improves over three existing gradient integral methods, IG, BIG and AGI. The main contributions are that 1) the proposed method finds a baseline in the integral that serves as an adversarial input for the current model and some other variations; 2) their empirical results show improved insertion and deleting scores compared to baselines.

### Strengths
Authors have made it clear how AttExplore computes the attribution scores. Their experiments include 3 networks and a rich amount of baselines. Table 1 shows a good amount of improvement over the best baseline.

### Weaknesses
My main concerns include the motivation and the evaluation of this paper.

### Motivation
I am not entirely sure I understand the motivation of the paper. It looks like this paper accuses BIG and AGI of using the exact boundary of the underlying model, which fails to be generic to similar models with variations in the decision boundary? This is pretty counterintuitive to me as feature attributions are often perceived as local explanations at the given model and the given input. Why do we need to consider if the explanation generalizes other models? With that being said, generalizing to other decision boundaries may trade in the faithfulness of the underlying model (this would relate to my second question about faithfulness and I will explain later).

### Generalization of Frequency-based Methods?
The motivation to alter features in the frequency domain is because there are works showing high-frequency features help the model to generalize better [1]. I am pretty worried the authors explain this conclusion as altering some features in the frequency domain helps to create examples that transfer better, especially for methods just proposed in this paper (Eq. 4 - 5).  Have you verified your adversarial examples actually transfer better? Can you provide some analytical results convincing me this helps better explore more decision boundaries? So far all descriptions are pretty hand-wavy.  

### Evaluations
Is the method faithful to the underlying model? It looks like to realize “a more general adversarial input” the proposed method manages to find an adversarial example that is much further to the decision boundary compared to the previous methods. I think authors may want to compare how much farther you go. It is pretty concerning to me that no matter how you adjust the feature generations in Table 3 and steps in Table 4, the proposed method has almost identical results on your metrics. Similar, no matter how you decrease $\epsilon$ in Table 5, the results do not change at all. What should we make out of these results? Are they showing the proposed method may be actually unfaithful to something? BTW, using $\epsilon=8$ is pretty huge and I think decision boundaries are usually much much closer than $8/255$ for models without adversarial training. 

I recommend testing INFD score [2] and run sanity check [3].

### Ending

Unlike doing detection or being more robust, I really think research works in explaining feature importance are not result-driven. Namely, it is not about being state-of-the-art on some scores. Not every attribution method uses deletion and inserting scores in baseline papers cited. There are a lot of discussions for the unreliability of feature attributions that are not cited here. It is fine to say “we do not care about those critiques but just want to improve the current method” but it is important to point out *important flaws* in the existing methods and fix those.

### Questions
N/A

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel attribution method called AttEXplore, designed for explaining DNN models through the exploration of model parameters. AttEXplore leverages the concept of transferable attacks as there's consistency between the decision boundary exploration approaches of attributionand the process for transferable adversarial attacks. By manipulating input features according to their frequency information, AttEXplore enhances the interpretability of DNN models.

### Strengths
1. This paper is well-written and easy to follow.
2. AttEXplore outperforms existing methods on the ImageNet dataset and models such as Inception-v3, ResNet-50, and VGG-16, achieving higher insertion scores and lower deletion scores, which underscores its effectiveness in model evaluation.
3. AttEXplore exhibits superior computational efficiency in terms of the number of frames processed per second when compared to existing methods.

### Weaknesses
1. This paper appears to focus exclusively on evaluating AttEXplore using image data, it lacks experiments on other data modalities, such as text data on NLP models. Expanding the evaluation to different data modalities could provide a more comprehensive assessment of AttEXplore's applicability.
2. For image classification models, the authors did experiments on CNN model groups including Inception-v3, ResNet-50, and VGG-16. It is unclear that if the superior explainability of AttEXplore stands still on other model groups, like vision transformers and MLP model groups. Extending the evaluation to diverse model architectures would further validate its effectiveness across different model types.

### Questions
It's shown in Table 1 in the appendix that compared with N = 10, the drop of insertion score  for N = 1is not huge (~0.007 for inception-v3, still better than existing methods ). The perturbation rate was set as 16, while the model performance is better when perturbation rate is 48. Would the trend of model performance under different N be more clear when the perturbation rate is set as a larger value?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present AttEXplore, a novel feature attribution method for explaining Deep Neural Networks (DNNs), designed to address the growing need for transparent and interpretable AI models. AttEXplore is inspired by recent advances in the domain of transferable adversarial attacks, and it combines two essential components: 

(1) Feature attributions based on adversarial gradient integration, and 

(2) Frequency-based data augmentation techniques to enhance the robustness of explanations.

In their paper, the authors conduct an extensive evaluation of AttEXplore on the ImageNet dataset, employing three different DNN architectures (Inception-v3, ResNet-50, VGG-16). They compare AttEXplore's faithfulness and time complexity against other attribution methods, providing valuable insights into its performance. Furthermore, the authors perform an ablation study to better understand the impact of the key components within AttEXplore.

To facilitate the adoption of their method, the authors also provide the associated code, making it accessible for other researchers and practitioners seeking to utilize AttEXplore for their own applications.

### Strengths
The paper offers several notable strengths:

**Leveraging of Insights from Transferable Adversarial Attack Works:** The authors introduce a unique approach that draws inspiration from the field of transferable adversarial attacks. Particularly, their integration of frequency-based data augmentation techniques, aimed at reducing noise in heatmaps (usually caused by gradient shattering and/or high non-linearity of DNNs), is an innovative contribution. This demonstrates a thoughtful incorporation of knowledge from a related domain into the field of local XAI.

**Comprehensive Model Evaluation:** The authors carry out an extensive evaluation, involving multiple deep neural network models and the ImageNet dataset. This thorough examination of AttEXplore's performance across different DNN architectures enhances the credibility of their findings and demonstrates its versatility and applicability.

**Related Work Section:** The authors effectively contextualize their work within the existing literature, highlighting its relevance and significance in the broader research landscape.

**Open-Source Code Availability:** A notable strength of this paper is the provision of the code associated with AttEXplore. This openness enables other researchers and practitioners to readily adopt and build upon the proposed method, promoting further research and development in the area of local XAI."

### Weaknesses
The paper exhibits, however, several weaknesses:

**Clarity:** 
Some sections of the paper lack clarity, making it challenging for readers to grasp the key concepts. The abstract and introduction suffer from being overly specific without providing sufficient context. Additionally, important elements of the proposed method are not adequately introduced, leaving readers without a clear understanding of the approach.

Figure 1, a critical element in conveying the method, could benefit from improved clarity. Enhancements to this figure would help readers better comprehend their motivation for AttEXplore.

Further, the paper frequently references the appendix but fails to provide specific locations. It would be highly beneficial if the authors included clear references to specific sections within the appendix, making it easier for readers to locate relevant supplementary information.

To me, some sentences in the paper do not make sense, such as "DeepLIFT and LIME generate explanations for generic models which limits the understanding of model’s global behaviors.“ Why would it limit the understanding, and what do you mean with global behvior?

In the Method section, Equation (4) includes index $i$ without a clear definition. It is unclear whether $I$ refers to a random draw of sample $x$ or a class index. This ambiguity needs to be resolved to enhance the precision of the method description.

**Evaluation Shortcomings:**
The evaluation has certain limitations. The absence of faithfulness curves is one deficiency as it hinders a comprehensive understanding of the method's performance. Moreover, the paper does not compare AttEXplore against state-of-the-art approaches designed to address noise in heatmaps, such as LRP (composite rules), SHAP, or LIME. Additionally, the time complexity comparison is limited to only a subset of methods, which restricts the scope of the evaluation and limits the ability to assess AttEXplore's competitive performance in terms of speed.

### Questions
Have you compared your method against other local XAI techniques that attempt to generate more robust explanations by reducing noisy attributions?

In the Method section, Equation (4) includes index $i$ without a clear definition. It is unclear whether $I$ refers to a random draw of sample $x$ or a class index. What does $i$ stand for?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes AttEXplore, an attribution framework based on transferable adversarial attacks. The authors claim that there are shared principles between the decision boundary exploration approaches of attribution and transferable attacks. Based on such observation, the framework performs attribution analysis based on the design of a nonlinear integration path. The frequency-based input feature alterations make the framework transferable across different decision boundaries.

### Strengths
1. The paper is well-written with a clear storyline that motivates the work.
2. The experiments on multiple attribution baselines are comprehensive.
3. The idea of bridging attribution methods and adversarial attacks is novel.

### Weaknesses
1. Given the transferable claim of this new attribution method, it will be necessary to show sufficient visualizations of how the attribution generalizes to different types of task models other than image classification. Specifically, the paper lacks experiments demonstrating the transferability of the attribution maps to models trained on non-image data, such as text or time-series data. The current experiments are limited to image classification tasks, which restricts the scope of the claimed transferability. It is crucial to show that the frequency-based input feature alterations can effectively generate meaningful attributions across diverse model architectures and data modalities.

2. The post-hoc explanation methods often suffer from false-positive responses, which highlight the semantic parts that are actually not relevant to the true grounding objects. The paper should elaborate more on how the framework overcomes such challenges. Specifically, the paper should discuss the potential for the method to highlight spurious correlations or background features instead of the actual object of interest. The paper lacks a discussion on how the framework mitigates the issue of attribution maps focusing on irrelevant features, which is a common problem in post-hoc explanation methods. Similarly, the paper shall have more quantitative evaluations on whether the attribution is correctly aligning with the ground truth. The paper needs to include metrics that measure the alignment between the generated attribution maps and the actual regions of importance, such as Intersection over Union (IoU) with ground truth bounding boxes or pixel-level annotations.

3. Recent years have witnessed the development of white-box transformers (e.g., [1]), whose self-attentions naturally emerge as attributions for the model decision. It remains a question as how will AttEXplore outperform these interpretable-by-design approaches. The paper needs to provide a more detailed comparison of the proposed method with the self-attention mechanisms of white-box transformers. It is unclear how AttEXplore's attribution maps compare to the attention maps generated by these models, and whether AttEXplore offers any advantages in terms of interpretability or accuracy.

### Questions
Please address my concerns listed in the weakness section. I look forward to the authors' response and I will possibly consider revising the rating based on the response.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
