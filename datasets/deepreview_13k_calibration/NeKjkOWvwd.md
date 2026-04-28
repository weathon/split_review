# Rethinking the OoD Generalization for Deep Neural Network: A Frequency Domain Perspective

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Out-of-distribution (OoD) generalization has long been a challenging problem that remains largely unsolved. Despite numerous attempts to generalize image classification models to OoD datasets, few novel proposals have surpassed the classical Empirical Risk Minimization (ERM) methodology systematically. In this work, we introduce frequency-based analysis into the study of OoD generalization for images. Based on the Shapley value, a theoretical measure in game theory, we quantify the influence of each frequency component on the model's performance. With this analysis, we can explain the model's performance statistically. We observe that although the fallacious outputs of our model on OoD generalization tasks frequently stem from low-frequency components of OoD images, the interference pattern is highly class-wise.  To further exploit our observation, we propose Class-wise Frequency Augmentation (CFA) to augment favorable frequency components and inhibit unfavorable ones. This approach can greatly improve the performance of existing OoD generalization algorithms. Our extensive experiments on five baseline OoD algorithms across seven OoD datasets provide encouraging results that prove the effectiveness of CFA on OoD generalization. Especially,
CFA  outperforms the state-of-the-art methods with the most substantial improvement on ColoredMNIST, increasing the identification accuracy from 60.2\% to 73.0\%.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The work analyses the importance of different frequency components to OOD generalization. The authors utilized Shapley values, which provide evidence of whether a certain frequency is favourable/unfavourable to generalization. Based on the analysis, they proposed a frequency augmentation technique, which benefits the OOD generalization of models.

### Strengths
+ Interesting idea to use Shapley values to analyse different algorithms (ERM, IRM,RSC) from a frequency perspective

### Weaknesses
 __Lacks novelty: analysis and Shapley value__
The analysis approach has quite strong similarity to that of [1], but the authors did not explore or comment about any differences or improvements compared to previous work. Conceptually, the analysis is also similar to [5], which is not discussed. Furthermore, there exist limitations on the approximation of Shapley values through random sampling of permutation proposed by Castro et al. [2], and Castro et al. further improved the approximation in [3], which was not applied by the authors. 
There are some other weaknesses using Shapley-value based methods to explain feature importance (as discussed in [4]), which were not considered by the authors. For instance, different frequency components might be interrelated, but using permutation-based approach might not consider this correlation. 


__Augmentation method__
The calculation of Shapley values is model-based, but it is unclear in either Algorithm 1 or section 4.1 whether the authors use a pre-trained model or the model under training.

__Experiment design__
- Experiments are limited to comparison with empirical risk minimization, invariant risk minimization, etc., while the proposed augmentation approach is not analyzed (and put in context with related works) in comparison with existing  state-of-the-art (frequency) augmentation approaches.
- Vague experiment details, e.g. unknown portion of the randomly sampled permutations, image resolution, training setup, unclear classification tasks on datasets like CelebA.
- Results are limited to MLP and ResNet18 models, without exploring Transformers or even other CNN architectures, and on small datasets. Generalization from ImageNet to e.g. ImageNet-R, ImageNet-O etc. should be studied.
- Formulas have unclear components or use of symboles:
	- ‘m’ was used twice in the equations (2) and (3)
	- no explanation for the designated set ‘T’ and the function f(.) in equation (6)
	- no explanation for ‘N’ when introducing the specific permutation π ∈ Π(N)

### Questions
- How is the analysis approach different from [1], which analyses the importance of frequency components to adversarial robustness, except that the authors extend it to OOD generalization? Also, what are the relations with [5]?
- In the introduction, the authors claim that the augmentation method is model-agnostic. But in sec. 3.1, they claim that the calculation of Shapley values is based on model output. These statements are contradictory to each other. Can the authors clarify the inconsistency?
- The proposed augmentation approach is class-wise and from the matrix of Shapley values, I infer the image resolution is low. Do the experiments show the feasibility of CFA to datasets with thousands classes (e.g. ImageNet1K)? How does the resolution of images affect the calculation of Shapley value? 
- To approximate the Shapley values, the authors randomly sample a portion of the permutation? What is the value of ‘m’, the portion, and how does this affect the calculation of stable Shapley values? Is there any trade-off between efficiency and stability?
- The authors mentioned the OOD generalization for deep neural networks, but the experiments only show results for MLP and ResNet18. What about other CNNs and transformers?

### Soundness
1 poor

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, authors proposed a novel method for OOD generalization based on augmentation in the frequency domains. 
The results shown achieve state of the art performance in both diversity and correlation shifts.

### Strengths
- The proposed method shows consistent results in both diversity and correlation shifts. This is a relevant point as many OOD generalization methods usually achieve good results in only one of the two shifts

- The proposed method can improve the performance of existing algorithms for OOD, making it general and applicable in many contexts

- The explanation is clear

### Weaknesses
 - I have some doubts about the experimental results, it seems that results are reported (e.g. for Colored MNIST) only for a certain degree of correlation/ratio between color and digit. How does the proposed method behave in under different degrees of correlation (as in [1])

- Related to the point above, the explanation about the nature of the shift in the different dataset is lacking. E.g. for MNIST, what ratio/correlation was used? For CelebA which attributes were considered? Etc. Specifically, the paper lacks details on how the spurious correlations are generated and controlled in each dataset. For instance, in Colored MNIST, it is unclear what specific correlation strength between digit and color was used, and how this choice impacts the reported OOD generalization performance. Similarly, for CelebA, the paper does not specify which attributes were used to create the spurious correlations, making it difficult to assess the generalizability of the proposed method across different types of attribute biases. Without this information, it is hard to evaluate the robustness of the method to different levels and types of spurious correlations.

- Comparison or references to relevant work in the debiasing/generalization fields are missing; e.g. [2,3,4]

### Questions
See weaknesses; 

Additional questions: 

- I think that your method could provide some sort of "explanability" in terms of visual interpretation of certain frequencies. Could you add some examples e.g. for ColoredMNIST or CelebA showing the reconstructed images for the most important frequency (both positive and negative)? 

- How where the $\alpha$ and $\beta$ hyperparameters chosen? How robust is your method to changes in these values? 

- I suggest authors change the line "We introduce Shapley value" in the introduction as it seems to suggest that this paper proposes Shapley value rather then their novel application

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper address the important issue of distribution shift fragility/robustness in image classification, using image frequency analysis. The paper proposes computing Shapley values to quantify how much different image frequency bands contribute to model predictions, and uses this analysis on the training data to determine which frequency bands are most useful for classification for each class. The paper then introduces Class-wise Frequency Augmentation: for each training image, amplify the frequency components that are most predictive of that class. This encourages the model to prioritize these more predictive frequency features during training, and empirically aids in OoD robustness (without making any changes to the images at test time).

### Strengths
Overall I like the idea of the paper, it is addressing an important topic, and the quantitative results are encouraging. I have not seen this method before (I believe it to be novel), and it makes sense to me and seems to help robustness.

### Weaknesses
The introduction includes a lot of discussion of related work, and doesn’t describe the contributions of the paper very clearly until the bullet-point list. I would suggest separating this into two sections, one that is a clear and direct introduction of the paper, focusing on your specific contributions, and a separate section covering related work that explains how the current paper fits into the context of the literature.
- A large portion of the paper is spent describing the difference between “diversity shift” and “correlation shift”, but I’m not convinced that this is actually relevant to the proposed method and contribution. My impression from the paper is that some augmentation strategies help only with either one or the other type of distribution shift, but the proposed method helps with both. However, since the proposed method doesn’t directly use anything relating to diversity or correlation shift, I would encourage the authors to avoid spending so much time describing it (or omit it entirely); as a reader I found it confusing and a bit distracting.
- It’s not clear to me how the frequencies are divided into the “buckets” shown e.g. in Figure 5—in particular, images have frequencies in 2D but the figures show a single frequency so I wonder how this maps onto 2D. More importantly: I’m also not entirely sure for the Class-wise Frequency Augmentation if the added and subtracted frequency components themselves are derived from an average over training images, or the method is amplifying and suppressing components of that test image only, but deciding which components to amplify or suppress based on training images.
- The theoretical analysis is billed as a proof of correctness for the proposed CFA method, but the theoretical model looks like it’s a linear prediction that would be quite far from the nonlinear neural nets used in practice. The analysis is still valuable to gain intuition, but I would recommend explaining a bit more about the assumptions behind it and treating it as an illustrative toy setting rather than a full proof of the practical algorithm.
- I don’t understand the difference between Table 1 and Table 2. There are some slight differences in which methods are compared, and the numbers are slightly different, but I don’t know why. If the differences are important then they should be explained more clearly (Table 1 is billed as an “ablation study” but this should be described more), especially why the final full-method numbers are different between the two tables. My primary concern here is that these final results differ between the two tables, which makes me question either the trustworthiness of the results or at least my understanding of them.
- Equations 5 and 6: f and F should be defined. I would guess that f is somehow the model output, but it’s not clear if this is logits, probabilities, top-class prediction, etc. This kind of detail is necessary for others to be able to reproduce and build on the proposed method.

### Questions
Minor suggestions/questions:
- The abstract says “we introduce frequency-based analysis into the study of OoD generalization for images”, which makes it sound like this is the first paper to take a frequency perspective on OoD robustness—though this is not the case. For example, a few papers in this area are: https://proceedings.neurips.cc/paper_files/paper/2019/hash/b05b57f6add810d3b7490866d74c0053-Abstract.html, https://arxiv.org/abs/2002.06349, https://proceedings.neurips.cc/paper_files/paper/2022/hash/48736dba3b8d933fabbfdb4f22a7be71-Abstract-Conference.html
- There are frequent typos and minor grammatical issues; please copy edit the final version of the paper. For example, in many places (including both text and figures) Shapley is misspelled as “Shapely”. Another example is in section 6 where the C in CNN is written as “convectional” rather than convolutional.
- Some terms need to be defined (or removed if not important). For example, in the large paragraph on page 2, the term “missingness” and “domain” are not very clear; I can guess what you mean but it would be better if it were clear. Likewise when describing the “appealing properties” of the Shapley value as a metric, it’s not clear yet what task you are hoping to use Shapley values for, and therefore not clear why these properties are appealing. Another instance of a similar lack of context/clarity is in the third contribution bullet point, which uses the words “all” and “both” without explaining what these are referring to. Another example is some acronyms; I know ERM but it should still be defined, as should RSC and IRM. 
- In equation 2, do you use the same random subset m in all the experiments, or is it chosen randomly each time?
- Around equations 3 and 4, it would be good to explicitly define u and v as spatial coordinates and m and n as frequency coordinates.
- It would be good to give some more description of the datasets that were used in the experiments, particularly how many train and test images, how large each image is, and how many classes there are.
- Is the “modified image” in Figure 6 an actual result of the inverse Fourier Transform, or just an illustration? It looks like just the edges of the input image, which I doubt would appear naturally as a result of the CFA method, but it would be good to specify if this is just an illustration (or even better to show an actual image resulting from the method).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
