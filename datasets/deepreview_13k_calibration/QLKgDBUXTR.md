# How many views does your deep neural network use for prediction?

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 3, 5

## Abstract
The generalization ability of Deep Neural Networks (DNNs) is still not fully understood, despite numerous theoretical and empirical analyses.
    Recently, Allen-Zhu \& Li (2023) introduced the concept of \emph{multi-views} to explain the generalization ability of DNNs, but their main target is ensemble or distilled models, and no method for estimating multi-views used in a prediction of a specific input is discussed.
    In this paper, we propose \emph{Minimal Sufficient Views (MSVs)}, which is similar to multi-views but can be efficiently computed for real images.
    MSVs is a set of minimal and distinct features in an input, each of which preserves a model's prediction for the input.
    We empirically show that there is a clear relationship between the number of MSVs and prediction accuracy across models, including convolutional and transformer models, suggesting that a multi-view like perspective is also important
    for understanding the generalization ability of (non-ensemble or non-distilled) DNNs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed MSV (Minimal Sufficient View) -- a method to get the parts(or features) of an input (sample/vector) that are minimal and sufficient to preserve a model's classification decision. Given a model and sample, the method outputs the MSV for that specific sample. The experiments conducted shows a strong correlation between MSV and accuracy (if model uses more MSV, it tends to have a higher accuracy). The authors also give a comparison between MSV and previous XAI methods.

### Strengths
- The paper states an important idea that a model's prediction relies on multiple features/views, and the experimental result (Table 1) provides a strong evidence
- I find the finding in Table 1 interesting (previous point)
- I like the idea that this method can be used to select model without label
- I find the visualizations to be very helpful in understanding the idea

### Weaknesses
 - The method sounds computationally expensive. Given that the author pitch this as a model selection/XAI method, an analysis on runtime will help. Specifically, the paper should provide a breakdown of the computational cost associated with each step of Algorithm 1, including the number of forward passes required for each sample and the time complexity of the search for minimal sufficient views. This is crucial to assess the scalability of the method.
- Although I find the multi view idea and its relation to accuracy interesting, I find the method lack coherence. Is it an XAI method, or a model selection method? The paper needs to clearly define the primary goal of the proposed method. Is it intended to provide interpretable explanations of model predictions (XAI), or is it primarily a tool for model selection based on the identified minimal sufficient views? The current presentation blurs the lines between these two distinct applications.
- In either case, the evaluation is lacking. Not sufficient comparison to existing XAI/model selection methods. For XAI, the paper should compare the MSV with other methods such as saliency maps, attention maps, or concept activation vectors. For model selection, the paper should compare against more established methods that leverage unlabeled data, such as methods based on diversity or uncertainty. The current comparison is too limited.
- What is the difference between single view based method (like gradcam) with combining all MSV into a single image? The paper should clarify how combining MSVs into a single image differs from existing single-view methods. Does this combined view offer additional insights, or is it simply a different way of visualizing the same information? The paper should also discuss the potential loss of information when combining multiple MSVs into a single image.
- Minor, but in Definition 1, c(f(x)): c has not been defined before.

### Questions
see weakness

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study defines the notion of minimal sufficient views (MSVs) as certain subsets of superpixels that preserves the prediction result of the DNN, inspired by the multi-views introduced in Allen-Zhu & Li (2023). This study visualizes MSVs on several examples and empirically discovers that the number of MSVs is positively correlated to the prediction accuracy of the model, thus providing a new perspective for understanding the generalization ability of DNNs.

### Strengths
1.	The mathematical definition of MSVs and the greedy algorithm for computing MVSs are both clearly written. I appreciate the execution example in Figure 3 which makes the computing process intuitive.
2.	The paper is easy to read and follow.
3.	The number of MSVs provides a novel view for estimating and comparing the generalization ability of DNNs.

### Weaknesses
1. The notion of MSVs in this paper is quite similar to the Sufficient Input Subsets (SIS) proposed in [1, 2], which is expected to be discussed in the Related Work section. SIS characterizes the minimal subset of input pixels (pixels outside of this subset is masked) for the model to achieve a certain level of confidence score. In this way, the proposed Minimal Sufficient Views seem to be a simple extension of the Sufficient Input Subsets. Specifically, while SIS focuses on individual pixels, MSVs operate on superpixels. However, the underlying principle of identifying a minimal subset that retains predictive power is conceptually very close. The authors are encouraged to clarify the differences between the two methods, particularly regarding the novelty of MSVs beyond being a superpixel-based variant of SIS.

2. The previous work [2] has noted an interesting phenomenon: for many images in CIFAR-10 and ImageNet, the size of the Sufficient Input Subsets (SIS) is quite small (e.g., only 5% to 10% of total number of pixels) and pixels in SIS are sometimes located outside of the target object. This means that the model might learn shortcut solutions, such as using blue pixels within the sky region to predict the bird class. Since the definition of MSV is similar to SIS, I wonder if a similar phenomenon occurs in this paper. From the current figures presented in this paper, most MSVs are located on the target object and seem to have clear semantic meanings, but I’m not sure if there are some “failure cases” in which the MSVs corresponds to patterns that are not related to the target object (e.g., pixels within the sky region or the grass region). A more thorough investigation into the spatial distribution and semantic relevance of MSVs across a larger dataset would strengthen the paper's claims about the interpretability of MSVs.

3. About the baseline value for masking the image. Although using the average value of the pixels in the training data as the baseline value is a common practice in literature, it is encouraged to test if the derived MSVs and the relationship to the generalization ability are robust under different choices of baseline values. This is because in most views (a masked image), the size of the mask is quite large, thus greatly influencing the output of the model. It is not clear if the current conclusions still hold under a different baseline value. For example, what if black or white pixels are used as the baseline instead of the average? Would the identified MSVs remain consistent, and would the correlation between the number of MSVs and model accuracy persist?

4. I do not quite agree with the claim that “MSVs with common features were obtained for multiple images” in the same class on Page 6. The notion of “left eye”, “right eye” are based on human perception, but it is not clear whether the model also encodes these features for inference. Moreover, the MSVs are defined in the pixel space instead of the feature space. It is not appropriate to simply claim that feature “a left eye with circular shape on a black cat” is equivalent to the feature “a left eye with an almond shape on a white cat”. This claim requires a more rigorous definition of “common features” in the context of MSVs and a more objective method for identifying them across different images.

### Questions
1.	I wonder how will different superpixel methods, such as SLIC and the Voronoi partition, influence the resulted MSVs for the same input image. Will the result be similar or totally different?
2.	Minor. The visualization result of GradCAM in Figure 7 is a bit weird. It is suggested to check the original GradCAM paper and compare this result with that of the original paper.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes the concept of Minimal Sufficient Views (MSVs) as a means to understand the generalization ability of Deep Neural Networks (DNNs). The authors empirically show a relationship between the number of MSVs and prediction accuracy across various models. They argue that a multi-view perspective is crucial for understanding the generalization ability of DNNs.

### Strengths
The paper focuses an important and relevant topic in deep learning - the generalization ability of DNNs.

### Weaknesses
1. This paper lacks a clear motivation for the proposed concept of MSVs. While the authors introduce the concept, they do not adequately explain why MSVs are necessary or how they specifically contribute to a deeper understanding of generalization ability beyond existing methods. For instance, how does the MSV concept compare to or improve upon established techniques for analyzing generalization? A more thorough justification is needed to establish the significance of MSVs.

2. The practical applicability of MSVs in real-world scenarios is unclear. The authors state that MSVs require testing samples to predict the generalization ability of DNNs. However, if one has access to testing samples, it raises the question of why one would need to predict generalization ability rather than directly measuring it using standard evaluation metrics. This apparent redundancy needs further clarification. The authors should elaborate on specific scenarios where predicting generalization ability using MSVs would be advantageous over direct measurement.

3. The experimental results are insufficient to fully validate the proposed concept. The paper primarily focuses on computer vision tasks. To demonstrate the broader applicability and robustness of MSVs, I strongly suggest the authors conduct experiments on other types of data, such as NLP datasets. Expanding the experimental scope would provide a more comprehensive evaluation of the effectiveness of MSVs across different domains.

4. The paper lacks a rigorous theoretical analysis of the relationship between MSVs and the generalization ability of DNNs. While the authors present empirical findings, they do not provide a theoretical framework to explain the observed correlations. A theoretical foundation would strengthen the paper's contribution. For instance, the authors could explore how MSVs relate to established concepts in statistical learning theory. Some XAI methods [1,2,3,4] have rigorous theoretical analysis to guarantee its faithfulness. I suggest the authors theoretically prove the faithfulness of MSVs, demonstrating that they satisfy properties like Minimality and Sufficiency, and explain how these properties relate to generalization performance.

### Questions
Please see the Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes Minimal Sufficient Views (MSVs), which is similar to multi-views but can be efficiently computed for real images. The proposed MSV can be used to understand the generalization ability of DNNs.

### Strengths
Figure 3 is vivid to illustrate the computation of the proposed MSV.

### Weaknesses
1. I think that the proposed MSV is a very typical and common method to evaluate the importance/attribution of each superpixel in XAI. Hence, what is the essential difference between the proposed MSV method and previous methods masking different image patches to evaluate importance/attribution.
2. Different SPLIT method will influence the final result? I think so. Hence, the proposed method indeed depends on the SPLIT method. If not, please conduct experiments for verification. 
3. Will the size of view affect the final result? since in Figure 4, some msvs contain only few image region, while other contain a larger image region. Considering a msv containing more image regions often encodes more information  than a msv containing few image regions, I think msv of different numbers of image regions cannot compare fairly.

### Questions
Stated in Weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
