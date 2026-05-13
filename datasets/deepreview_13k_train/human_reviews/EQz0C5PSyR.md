# Embedding Learning for Approximating Person-specific Cognitive Similarity

- Decision: Reject
- Scores: 3, 5, 6, 6, 3

## Abstract
Metric learning is often applied in scenarios where labels are well-defined or where there is a ground truth for semantic similarity between data points. However, in expert domains such as medical data, where experts perceive features and similarities differently on an individual basis, modeling psychological embeddings at the individual level can be beneficial. Such embeddings can predict factors that influence behavior, such as individual uncertainty, and support personalized learning strategies. Despite this potential, the amount of person-specific behavioral data that can be collected through similarity behavior sampling is insufficient in most scenarios, making modeling individual cognitive embeddings challenging and underexplored. In this study, we proposed integrating supervised learning on small-scale similarity sampling data with unsupervised autoencoder-based manifold learning to approximate person-specific psychological embeddings with significantly improved similarity inference performance. We conducted a large-scale experiment with 121 clinical physicians, measured their cognitive similarities using medical image data, and implemented person-specific models. Our results demonstrate that even in complex expert domains, such as medical imaging, where cognitive similarity varies between individuals, person-specific psychological embeddings can be effectively approximated using limited behavioral data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper explores approximating person-specific cognitive embeddings in expert domains, where similarity perceptions vary between individuals.  The authors combine supervised learning on limited similarity data with unsupervised autoencoder-based manifold learning.  An experiment with clinical physicians and medical images demonstrates the feasibility of this approach.  The paper contributes a new method for modeling individual-level psychological embeddings, showing the potential of autoencoders in this context, and validating the use of variable triplet loss.

### Strengths
- The paper tackles a unique problem: approximating person-specific cognitive embeddings, particularly in domains with high inter-observer variability like medical image interpretation. This approach is a novel application of metric learning.   

- The study includes an experiment with 121 clinical physicians, using real medical image data. This provides empirical support to their claims.   

- The paper clearly outlines the methodology, including the triangular measurement framework for collecting behavioral data and the integration of supervised and unsupervised learning for embedding modeling.

### Weaknesses
 - The core focus of the study leans more towards cognitive science and human-computer interaction, with limited novelty in terms of machine learning techniques. The use of standard autoencoder architectures and the absence of new metric learning algorithms may lessen its impact on the machine learning community. 
 
- The study primarily focuses on medical image interpretation with limited exploration of the generalizability of the proposed approach to other domains. Further experiments on diverse datasets and tasks would strengthen the paper's contribution. 

- The paper lacks a thorough analysis of the proposed method, especially concerning the convergence properties of the loss function and the interaction between triplet loss and manifold learning in autoencoders.

### Questions
- Could the problem of approximating person-specific embeddings be framed in the context of existing machine learning challenges like label noise or annotator disagreement? This could help position the work within a more familiar framework for the ML audience.

- Have you considered evaluating the approach on publicly available benchmark datasets for label noise or annotator disagreement? This would provide a point of comparison with existing methods and offer insights into the generalizability of your findings.

- How does the proposed approach scale with an increasing number of individuals and data points? Are there any considerations for improving the computational efficiency of the method?

- How can the insights from this study be used to develop personalized learning strategies for experts or improve human-AI collaboration in domains with high inter-observer variability?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the challenge of modeling individual cognitive embeddings in expert domains, like medical data, where perceptions of features and similarities vary significantly among individuals. It proposes a novel approach that combines supervised learning on limited similarity sampling data with unsupervised autoencoder-based manifold learning to enhance the accuracy of person-specific psychological embeddings. The results from a large-scale study involving clinical physicians show that even with limited behavioral data, the proposed method effectively approximates these embeddings and improves similarity inference performance in complex domains.

### Strengths
1. The proposed method intriguingly combines supervised learning on small-scale similarity sampling data with unsupervised autoencoder-based manifold learning to approximate person-specific psychological embeddings.

2. The authors conducted a comprehensive experiment involving 121 clinical physicians, measuring their cognitive similarities using medical image data, which lends credibility to the results.

### Weaknesses
1. The paper's organization is unclear, making it difficult to follow. For instance, Figure 2 lacks sufficient detail and explanation regarding how the various modules interact with one another.
 2. Figure 1 and Equation 1, which illustrate the person-specific cognitive embedding modeling framework and the variable triplet loss function, lack detailed explanation. The authors should clarify how the proposed variable triplet loss function (Equation 1) innovatively captures individual cognitive similarity compared to standard triplet loss functions. A comparative analysis with traditional triplet loss in terms of mathematical formulation and expected outcomes would be beneficial.
3. The authors should conduct a sensitivity analysis on $\alpha$ and $\beta$ to demonstrate the robustness of the model concerning these critical parameters.
4. Figure 3 and Section 4.3 present the group-based similarity pattern analysis results. While the t-SNE visualizations illustrate the variability in similarity patterns among subjects, the paper lacks a statistical test to quantify the significance of these differences. The authors should include statistical validation, such as ANOVA or post-hoc tests, to confirm the variability of cognitive similarity patterns across different subjects. Additionally, the paper should discuss how these findings may generalize beyond the specific group of clinical physicians studied.

### Questions
The authors are required to address all my concerns carefully listed in the Weaknesses part.

### Soundness
2

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
2

### Summary
This paper presents a new method to model individual ways of understanding and interpreting medical images. In the filed of medicine, experts often see images differently based on their personal experiences and knowledge. Therefore, this paper aims to capture these unique perspectives by creating custom models for each doctor that reflect how they personally perceive similarities in medical images. To achieve this, the authors combine supervised learning for views image similarity, and unsupervised learning with an autoencoder to build a broader model of each doctor's cognitive pattern without requiring labels. In addition, the model uses triplet loss to help the system understand which images a doctor sees as more similar or different from each other. The authors conducted an extensive experiment with 121 doctors, asking them to judge the similarity between chest X-rays.

### Strengths
1.	The paper is well-structured, with clear explanations of the proposed framework and its components. The authors provide a thorough background, outlining the challenges in modelling person-specific cognitive similarities and the limitations of existing methods.
2.	The research is underpinned by a robust experimental design involving 121 clinical physicians, providing a substantial dataset for analysis. The methodology is meticulously detailed, ensuring reproducibility and transparency.  The integration of behavioural sampling to capture each participant's perception of similarity among chest X-ray images adds depth to the study, reinforcing the reliability of the findings.

### Weaknesses
1.	In Section 3.1, the authors implemented the measurement of cognitive similarity through a triangular arrangement of images, where physicians arrange images based on perceived closeness. However, this may lack depth in capturing nuanced interpretative differences. This approach does not account for context-dependent interpretation, such as how a physician might consider patient demographics or clinical history when assessing similarity. Therefore, the authors can benefit from incorporating more sophisticated cognitive tests or context-dependent tasks that could improve the understanding of the factors that influence these cognitive patterns. This added information could be used to fine-tune the embedding model.
2.	The authors use a convolutional autoencoder for CXR images and prove its efficiency. However, testing alternative architectures — like ViT (Dosovitskiy et al., 2020) — could provide insights into which architectures best capture complex cognitive similarities. Moreover, adding architectural flexibility or adaptivity within the model, perhaps by using modular components that can adjust based on data type, would make the framework more broadly applicable.
3.	The paper lacks comparisons with alternative embedding models that could serve as baselines. Without baselines, it is difficult to understand whether the proposed autoencoder with variable triplet loss truly excels over other methods.

### Questions
1. Could you give a more detailed explanation of the variable triplet loss function? And why do you define such variable triplet loss and what mechanisms allow it to adapt to individual cognitive patterns?
2. While the study focuses on chest X-ray images, have you considered applying this approach to other medical imaging modalities, such as MRI or CT scans? If so, what adaptations would be necessary to accommodate the distinct characteristics of these modalities?
3. Could you elaborate on the decision to utilize CNNS for the autoencoder component instead of Transformer-based architectures? Given that Transformers have demonstrated effectiveness in capturing long-range dependencies and global context in image processing tasks, what were the considerations that led to favouring CNNs in this context? Additionally, how was the network architecture determined to ensure optimal performance in fine-grained image processing tasks?

### Soundness
2

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
4

### Summary
This paper presents an investigation of using a small amount of similarity sampling data to fine-tune pretrained embeddings and learn person-specific embeddings.  The authors evaluate this on a medical imaging task and perform an impressive scale evaluation with 121 clinical physicians.  Person specific/ personalization analyses are interesting and valuable as there many tasks in which there are individual differences and performance can be improved significantly by adapting to a user.

### Strengths
The paper has several strengths, it is well written and clearly presented overall.  The data collection is impressive and valuable to the research community.  The paper generally has sufficient details for replication.

### Weaknesses
The authors claim theirs is  “first large-scale experimental study to model individual-level psychological embeddings” This is a big claim and I don’t think it is really justified. There are many papers on personalization and subjective tasks such as emotion labeling in affective computing.  I would request the authors to clarify what the novelty is or if I have misunderstood the approach.
Related to this I think the paper should have a more extensive related work section on personalization that helps the reader understand the differences between this work and other adaptive/personalized models.

The details of the data collection are a little unclear.  1) How many images did each clinician label?  Did they all complete 500 exactly? What was the range of times it took for them to complete these?  This is a might seem a little like I am nitpicking, but the authors claim the data collection as one of their three main contributions and so it would be great to have a little more detail about the data collection over all, including (a) the background of the clinicians, (b) the average and range of number of years of experience, (c) more details about the instructions they were given.  

The data collection is impressive and the study is interesting.  I commend the authors on this.  The results also support the performance claims showing a consistent bump in accuracy.  This is not particularly surprising given that personalization usually leads to better results than a generic one. 
Will the data be released?  I apologies if I missed something but again the value of these data for future research could be significant. 

I did not quite understand the message behind Fig.4 (b) - Are they both highlighting that there is little correlation between the two? 

In the introduction key contributions numbered points the text in parentheses e.g. “Perspectives on cognitive science” seem unnecessary.  I would remove these.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents an approach for learning a human-like representational space using a deep learning architecture. This embedding space is supervised by human similarity judgments, specifically, for triplets of chest X-ray images.  The deep learning architecture is an autoencoder, and the representation learning is implemented using a triplet loss function, whose purpose is to produce an embedding space where objects (images) perceived as more similar by humans are positioned closer together. The model successfully generalizes to predict human similarity judgments.

### Strengths
The main contribution of this paper is its demonstration that it is possible to learn person-specific embeddings, as seen in good out-of-sample prediction of similarity relations at the individual level.  Additionally, the findings suggest that person-specific embeddings effectively capture unique, idiosyncratic aspects of each person's similarity judgments. This is seen in the fact that models learned for one participant do not perform well in predicting similarity judgments of other participants.

### Weaknesses
1) Novelty of embedding workflow: The novelty of the paper is somewhat limited, because several studies have already presented related methods for learning embedding spaces that align object distances with human similarity judgments, or related tasks like the triplet task (where a person selects which of two objects is more similar to a reference object). Palazzo et al. (2020) use a triplet loss to learn a joint embedding of EEG data and visual images; Zhang et al. (2018) present LPIPS which reweights layers of a pre-existing network based on human triplet judgments;  Tarigopula et al. (2023) use pruning to improve the alignment between object-distances in the embedding space and human similarity judgments;  Jha et al. (2023) extract low-dimensional representations from pre-trained CNNs using similarity learning in a lower-rank embedding space so that distances in the embedding space maintain monotonic relation with human similarity judgments.  Given these prior studies, the main differences in the present study are the use of an autoencoder and learning/modeling single-participant data. However, even these differences are associated with some weaknesses as detailed below.

2) Some architecture and implementation details are not well explained or justified. In particular, it is not clear why the authors choose to use an autoencoder architecture rather than a simpler encoder operating on features produced from a separate feature extractor.  In principle, it should be possible to learn an embedding space without the decoder (see Jha et al, Palazzo et al.). That would produce a smaller, less complex model.  Looking at the details of the ablation study it is clear that the addition of the decoder improves performance, as compared to using the triplet loss alone, and the reason is probably that the decoder is necessary for learning a rich set of visual features.  An alternative (used by prior studies) is to use a pretrained CNN as a feature extractor, and then rely only on an encoder alone for metric learning.  A potential weakness in using the autoencoder is that the object-distances end up relying on features that are also required to reconstructing the image, but it is not clear whether those are necessarily the most important drivers of human similarity judgments.  Another reason for using a pre-trained network as a feature extractor is suggested from the ablation exercise presented in Table 1. It shows that using a reconstruction (decoding) loss alone produces above-chance performance in predicting human judgments. This suggests that certain image features, captured by the decoder, drive similarity judgments across the group. This strengthens the argument for using a strong pretrained architecture as feature extractor, which could then be fine-tuned on subject-specific data.

3) Absence of justification for modeling individual data: The abstract and introduction write that “modeling psychological embeddings at the individual level can be beneficial,” but the authors do not provide a clear demonstration of how single-participant modeling improves a specific objective or task. For certain applications, such as identifying individuals who may differ from others, it is not even necessary to use an embedding space; such analyses can be conducted directly from the similarity matrices computed from the behavioral data.

4) Novelty and strength of interpretability analysis (section 4.6): the authors introduce an interpretability analysis whose purpose is to identify important parts of the images. It has a few weaknesses. First, the details are not presented in a separate methods section but introduced on the fly in the results. Second, the analysis choices are not argued for. The indicator of quality to be explained is the variance in a single reference unit of the network, which presents the strongest variance for a batch of images. They then define more important image pixels as those whose masking reduces the variance in this unit.  Both Palazzo et al. and Tarigopula et al. report related masking procedures, but in those studies, the impact of masking was evaluated by determining how the masking of each pixel (or image region) impacts the alignment between the DNN and human similarity spaces, which is a more direct test of which image areas are psychologically relevant than the test evaluated here.  As a consequence, the novelty and validity of the masking procedure suggested here is weakened. 
Separately from this issue, a formal quantitative overlap between human raters and the interpretability measure is missing; only a qualitative evaluation is provided via a figure.

### Questions
it was not clear to me why the loss term called ‘variable triplet loss’ was used. The traditional triplet loss forces a solution where D(a,c) < [D(a,d)+margin] where D is distance, a the anchor and c,d the similar and dissimilar objects.  To my understanding, the loss term used (stronger weight on distance to closer anchor) will encourage D(a,c) < D(a,d) but does not force it. That is, there could be solutions where this does not hold. The choice of this term should be better motivated. 

Additional feedback and references mentioned
Re: Figure 3 – The figure shows how participants are positioned in a lower-dimensional space. To interpret these distances, it would be good to include a test-retest measure for each participant, which would formally quantify intra-participant variability, not just inter-participant variability.
p. 1 Re’ the statement that “the amount of person-specific behavioral data that can be collected through similarity behavior sampling is insufficient in most scenarios”, and similar statements in Section 2.1: There are effective multi-item arrangement methods, similar to the procedure used here that allow estimating object similarity in multiple dimensions (Kriegeskorte and Mur, 2012). 
p.2 Re’ the statement “we conducted a first-ever behavioral sampling experiment to measure the cognitive similarity of actual CXR images with 121 clinical physicians, focusing on realistic scenarios.” This seems to be an important point, but it was not clear what does the similarity of medical images measure? If these judgments are independent of diagnosis (as appears to be the case here), the dimensions that drive similarity might be completely unconstrained and left to each person’s own interpretation. This means that it’s possible that two physicians could make very different similarity judgments even if they arrive at the same diagnosis. It would be interesting to know whether these similarity judgments correlate with agreement on diagnosis.
P. 4 The authors mention a limitation of person-specific modeling, writing, “behavioral data from a subject can typically only be used to train an individual model for that subject.” The word ‘only’ was unclear; the judgments could be averaged  to create a group -level similarity matrix if the triplets are same across participants.
p. 5 It’s not completely clear how the binary labeling was applied to a triplet so that concatenation produced SPV.
p. 6 The participants were 121 clinical physicians.  They seem to vary widely over age/experience (Appendix; Table 2 Min = 26; Max = 55 years of age). It’s probable they differ considerably in their ability to evaluate chest X-ray images. It could be interesting to see whether the embeddings or behavior are more similar among the more experienced participants.
p. 7 The method for applying t-SNE to binary strings of SPV is unclear. Binary data require specific distance functions, and those details are missing here.
p. 7 section 4.5 clunky writing around the text in parentheses. 

Refs
Palazzo, S., Spampinato, C., Kavasidis, I., Giordano, D., Schmidt, J., & Shah, M. (2020). Decoding brain representations by multimodal learning of neural activity and visual features. IEEE Transactions on Pattern Analysis and Machine Intelligence, 43(11), 3833-3849.
Zhang, R., Isola, P., Efros, A. A., Shechtman, E., & Wang, O. (2018). The unreasonable effectiveness of deep features as a perceptual metric. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 586-595).
Jha, A., Peterson, J. C., & Griffiths, T. L. (2023). Extracting low‐dimensional psychological representations from convolutional neural networks. Cognitive science, 47(1), e13226.
Tarigopula, P., Fairhall, S. L., Bavaresco, A., Truong, N., & Hasson, U. (2023). Improved prediction of behavioral and neural similarity spaces using pruned DNNs. Neural Networks, 168, 89-104.
Kriegeskorte, N., & Mur, M. (2012). Inverse MDS: Inferring dissimilarity structure from multiple item arrangements. Frontiers in psychology, 3, 245.

### Soundness
2

### Presentation
1

### Contribution
2
