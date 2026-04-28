# L-WISE: Boosting human image category learning through model-based image selection and enhancement

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
The currently leading artificial neural network (ANN) models of the visual ventral stream -- which are derived from a combination of performance optimization and robustification methods -– have demonstrated a remarkable degree of behavioral alignment with humans on visual categorization tasks. Extending upon previous work, we show that not only can these models guide image perturbations that change the induced human category percepts, but they also can enhance human ability to accurately report the original ground truth. Furthermore, we find that the same models can also be used out-of-the-box to predict the proportion of correct human responses to individual images, providing a simple, human-aligned estimator of the relative difficulty of each image. Motivated by these observations, we propose to augment visual learning in humans in a way that improves human categorization accuracy at test time. Our learning augmentation approach consists of (i) selecting images based on their model-estimated recognition difficulty, and (ii) using image perturbations that aid recognition for novice learners. We find that combining these model-based strategies gives rise to test-time categorization accuracy gains of 33-72% relative to control subjects without these interventions, despite using the same number of training feedback trials. Surprisingly, beyond the accuracy gain, the training time for the augmented learning group was also shorter by 20-23%. We demonstrate the efficacy of our approach in a fine-grained categorization task with natural images, as well as tasks in two clinically relevant image domains -- histology and dermoscopy -- where visual learning is notoriously challenging. To the best of our knowledge, this is the first application of ANNs to successfully increase visual learning performance in humans, and especially robustly across varied image domains.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel approach to augment human learning in image categorization tasks. By leveraging robustified ANNs, the study introduces model-guided image selection and enhancement strategies that increase human test-time categorization accuracy by up to 72% and reduce training duration by around 20-23%. L-WISE employs selecting images based on predicted difficulty levels and enhancing images with pixel perturbations.The proposed approach is tested on natural images, dermoscopy, and histology images. The results demonstrates efficacy of L-WISE in aiding novice learners in fine-grained categorization tasks. This research represents one of the first applications of ANNs in optimizing human visual learning in clinically relevant domains.

### Strengths
- Presents an innovative use of robustified ANNs to predict task difficulty and enhance images, aiding human perception and learning.
- Shows broad applicability by successfully testing across diverse domains, such as natural image classification, dermoscopy, and histology.
- Achieves practical efficiency by reducing training time and improving test-time accuracy, beneficial for fields requiring rapid, accurate human image categorization training.

### Weaknesses
 - Lacks a dedicated related work section, which would help contextualize the research.
- Both low and high logits from ANNs show significant variation in human accuracy, making predictions less reliable in certain logit intervals.
- Uses only the ResNet-50 architecture, limiting generalization; further testing with models like vision transformers (ViT) is needed to support broader conclusions.
- Image enhancement may introduce biases, potentially improving accuracy only for certain major classes; additional metrics like precision and recall per class, rather than just mean accuracy, should be reported to provide a clearer assessment.

### Questions
1. How to choose $\epsilon$ for different tasks and image domains?
2. What criteria determine if a model is "robustified" enough for use? Have you considered specific metrics to evaluate the robustness of guide models, and how do these metrics correlate with human learning outcomes?
3. Did you collect qualitative feedbacks from participants? Did the new curriculum and enhanced images increase mental stress of human learners? Additional learning costs beyond training time should be considered, such as cognitive load and emotional well-being.

### Soundness
1

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
2

### Summary
This paper presents L-WISE, a framework leveraging adversarially robust ANNs to estimate image difficulty and apply nuanced perturbations that facilitate human learning in visual categorization tasks. By selecting challenging images and amplifying category-specific features, L-WISE improves human categorization accuracy by 33-72% and reduces training time by 20-23% across both general and clinical domains (e.g., dermoscopy and histology). The authors also discuss ethical implications, emphasizing the benefits of enhanced medical training and cautioning against potential biases that may arise from reliance on model-derived guidance.

### Strengths
1. The application of Robustified ANNs for improving human visual performance on image categorization seems like an interesting avenue. 
2. L-Wise empirically demonstrate gains in categorization accuracy and training efficiency. 
3. The paper addresses ethics concerns. Since the work mentions use of clinical data ethics discussion is of critical importance.

### Weaknesses
1. The paper focused on the performance of ventral stream. But we know that the human visual stream has a dorsal stream (where) that locates an object and the ventral stream (what) stream. And the interplay of these two streams forms the basis of human visual system. In this work the authors mainly focused on the ventral stream. From only quantified data, we can see the gains but it is very hard to trace this back to the nuanced perturbations the ANN produces. Hence, the suggestion is to use human gaze. The human gaze will precisely pin-point the "where" aspect and then will truly help us understand if at all the model perturbations are helping improve human performance. Can the authors please explain this?
2. A robust DNN actually has worse performance on nominal data points. Data points that have not been corrupted adversarially. What was the motivation of the authors to select such a model for their experiments?
3. The perturbations -  The perturbations if I am not mistaken are very subtle ones. For fine grained classifications, humans do follow curriculum learning but learning structures gradually from simpler to harder concepts. No experiments have shown this. It would be great if the authors can provide some empirical results/ explanation that can explain how will their method occur when you focus on structural cues rather than model perturbations that will benefit fine grained categorization.
4. I am providing some citations related to Gaze and dual stream hypothesis that can help authors clarify my concerns

a. A Dual-Stream Neural Network Explains the Functional Segregation of Dorsal and Ventral Visual Pathways in Human Brains, NeurIPS 2023.
b. Literature related to papers accepted in NeurIPS Gaze Meets ML workshop. That workshop accepted papers will provide intuition of how human gaze can be used in coherence with DL models.

### Questions
1. For model perturbations, can the authors please provide heat maps or any qualitative results that will help us track the ANN perturbations to human visual learning? 
2. Is there a way to show if the study scales/generalizes to other ANNs as well other than Adversarially trained ones? Since human subjects have been used here, I am not sure how feasible experiments will be. This can be a general neural network or a network trained by the CutMix [a] loss that provides robustness benefits as well. 
3. I feel generating perturbations based of dual stream networks and then using human gaze to track these will be a much stronger claim to the work. Can the authors please address this question? 
4. What about adversarially trained transformers? The attention maps are different from CNN feature maps. How will the study be applicable for perturbations based of a transformer backbone? 
5. Please also address concerns raised in the weakness sections. 

a. CutMix: Regularization Strategy to Train Strong Classifiers with Localizable Features. In Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2019,

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
This paper proposes a method to enhance human visual learning by designing a model-based selection and enhancement algorithm to improve classification accuracy during testing. First, the authors select images to present to novice learners based on a model’s estimated recognition difficulty for each image. Next, they apply image perturbations intended to aid recognition for novice learners. The authors conduct experiment on the three benchmark datasets, including the natural image and the clinical image to verify the effectiveness of their proposal.

### Strengths
1. This paper is well-motivated, and a decent amount of technical details are given.
2. The idea of improving the categorization performance of the novice learner by leveraging the capacity of the robustified artificial neural network is both interesting and practical.
3. The reported improvement in novice learners' performance is notable, with gains in both test accuracy and reduced training time.

### Weaknesses
1. The establishment of the empirical observations is somewhat unconvincing. Do these observations hold in more complex classification tasks or when applied to medical imaging? Specifically, the reliance on a 16-way animal categorization task using ImageNet seems limited in scope. It's unclear if the observed relationships between model-predicted difficulty, image perturbations, and novice learner performance would generalize to more nuanced classification problems, such as those found in medical imaging, where subtle differences in visual features are critical for accurate diagnosis.
2. The related work section lacks discussion of both the machine teaching and human-machine vision alignment methods. The absence of a thorough comparison with existing machine teaching approaches, particularly those that focus on curriculum learning or active learning strategies for human learners, is a significant oversight. Similarly, the lack of engagement with literature on aligning machine vision models with human perception limits the paper's contextualization within the broader field.
3. The size of the particants is somewhat small. The number of participants in the experiments, while possibly adequate for basic statistical analysis, may not be sufficient to ensure the robustness and generalizability of the findings. The lack of a detailed power analysis or discussion of effect sizes further weakens the reliability of the results.
4. The perception of enhanced images may be altered due to perturbations. The use of image perturbations, especially with larger ϵ values, raises concerns about whether the enhanced images still preserve the essential visual information required for accurate categorization. This is particularly concerning for medical images, where even slight alterations could lead to misinterpretations or the loss of critical diagnostic features.

### Questions
1. The empirical observations are derived from a 16-way animal categorization task on natural images, which seems somewhat simplistic. It would be valuable to examine how these observations hold up in more complex categorization tasks or with different types of images, especially medical images. Given the typically limited availability of medical images, the proposed method could have promising applications in the medical imaging field.

2. Beyond the empirical observations, is there any physiological insight or analysis on why the proposed model-based selection and enhancement method could improve novice learners’ performance in categorization tasks?

3. The authors do not discuss the related machine teaching literature. An in-depth comparison with machine teaching methods, particularly with "Teaching Categories to Human Learners with Visual Explanations" (CVPR 2018), would be valuable. This work similarly considers image difficulty; an introduction and comparison with it are beneficial.

4. The authors should also discuss the connection to human-machine vision alignment methods, such as "Harmonizing the Object Recognition Strategies of Deep Neural Networks with Humans" (NeurIPS 2022).

5. The sample size of participants is relatively small, and expanding the participant pool is recommended to enhance the reliability of the results; also, recruiting participants from diverse backgrounds would improve the generalizability of the findings. If expanding the participant pool is impractical due to time or budget constraints, performing a power analysis or discussing effect sizes could help strengthen the reliability of the analysis.

6. When using perturbations to enhance images, how does the method ensure that essential image details remain unchanged, particularly when using a large ϵ (e.g., 20)? This concern is especially pertinent for medical images, where even slight pixel changes may alter critical information. I recommend involving medical experts to review the enhanced images or using quantitative similarity measures (such as SSIM or FSIM) to verify that essential details are preserved.

### Soundness
2

### Presentation
2

### Contribution
2
