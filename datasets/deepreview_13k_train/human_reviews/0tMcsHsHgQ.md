# Towards Undistillable Models by Minimizing Conditional Mutual Information

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
A deep neural network (DNN) is said to be undistillable if used as a black-box input-output teacher, it can not be distilled by knowledge distillation (KD) to train a student model so that the distilled student (called knockoff student) outperforms the student trained alone with label smoothing (LS student) in terms of prediction accuracy. To protect intellectual property of DNNs, it is desirable to build undistillable DNNs. To this end, it is first observed that an undistillable DNN may have the trait that each cluster of its output probability distributions in response to all sample instances with the same label should be highly concentrated to the extent that each cluster corresponding to each label should ideally collapse into one probability distribution. Based on this observation and by measuring the concentration of each cluster in terms of conditional mutual information (CMI), a new training method called CMI minimized (CMIM) method is proposed, which trains a DNN by jointly minimizing the conventional cross entropy (CE) loss and the CMI values of all temperature scaled clusters across the entire temperature spectrum. The resulting CMIM model is shown, by extensive experiments, to be undistillable by all tested KD methods existing in the literature. That is, the knockoff students distilled by these KD methods from the CMIM model underperform the respective LS students. In addition, the CMIM model is also shown to performs better than the model trained with the CE loss alone in terms of their own prediction accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a defense method against knowledge distillation (KD) attacks, where the goal is to avoid the undesired usage of the outputs of deep neural networks (DNNs) by making them undistillable. The authors propose a training method that aims to minimize the conditional mutual information (CMI) across all temperature-scaled clusters, resulting in a model that cannot be effectively distilled by existing KD methods. The CMIM model is shown to be undistillable through extensive experiments on CIFAR-100, TinyImageNet, and ImageNet datasets, while outperforming state-of-the-art methods and even improving upon the conventional cross-entropy (CE) loss in terms of prediction accuracy.

### Strengths
1. The paper's goal is to prevent the misuse of models and serves a partial privacy protection technique, which is significant for the reliable use of AI models. 

2. The paper provides both theoretical and empirical evidence to demonstrate the benefits of the proposed method in enhancing the undistillability of models. T

### Weaknesses
1. The writing quality of the paper could be enhanced.

2. From a methodological perspective, the overall contribution of the paper is somewhat limited. The paper utilizes an existing metric, CMI, to measure the compactness of model outputs and aims to enhance model undistillability by maximizing this compactness metric. This approach appears too trivial and straightforward. It is not clear how this method fundamentally differs from directly employing a maximum entropy term or label smoothing technique to increase output concentration. Moreover, in the field of machine learning, particularly in computer vision, numerous loss functions have been studied to enhance model output compactness, such as the Large-Margin-Softmax-based methods.

3. The paper's finding that the teacher model trained with the proposed method achieves higher accuracy is not surprising. The mechanism by which the proposed method operates is similar to that of label smoothing, which is known to enhance accuracy. The authors might refer to the paper "When does label smoothing help" to understand that label smoothing can also produce the feature compression effect as shown in Figure 2 of this manuscript. The enhancement in accuracy due to the proposed method is expected and aligns with the effects of label smoothing, which is not a novel discovery in the field.

### Questions
Please refer to the weaknesses.

### Soundness
2

### Presentation
1

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
To protect the intellectual property (IP) of pretrained DNNs (teachers), the authors propose a method to prevent student models from using knowledge distillation (KD) to mimic the teacher models’ behavior. Specifically, they focus on a black-box scenario where the student model can only access the inputs and output logits of the teacher model. The proposed conditional mutual information minimization (CMIM) method constrains the output probability distributions of the teacher model so that each cluster associated with a label is highly concentrated (highly peaked around a single label). Intuitively, this eliminates the inter-class information from the teacher model's output logits such that the student model receives no more information than the labels themselves, thereby protecting the IP of the teacher model.

### Strengths
1. The idea is intuitive and with sufficient details.

2. The benchmark defense and knowledge distillation (attack) methods are exhaustive in the experiments.

3. The paper is well-organized and easy to follow.

### Weaknesses
1. The discussions of the proposed method’s limitations are missing. The proposed method collapses the logits so that each class’s output is highly concentrated (as shown in Fig.2), the teacher model might become overly confident in its predictions. This can lead to poor calibration and deteriorate generalization capability on out-of-distribution (OoD) data. Specifically, the method's reliance on concentrating outputs could make it brittle to shifts in the input distribution, as the model might not be able to generalize well to data that deviates from the training distribution. The lack of discussion on how the method impacts the model's uncertainty estimates is also a concern. Therefore, more settings and evaluations on the protected teacher model’s performance beyond prediction accuracy are necessary, including metrics like expected calibration error (ECE) and performance on various OoD datasets.

2. The proposed method involves multiple hyperparameters, e.g., such as the number of power samples $N$ and the range $[0,\beta]$, but the ablation studies on hyperparameter sensitivity are missing. For example, have you assessed how these hyperparameters impact the model’s undistillability and accuracy? If some parameters are particularly influential, could you highlight those findings? The absence of such analysis makes it difficult to understand the robustness and practical applicability of the proposed method. It is crucial to understand how these parameters interact and what are their optimal settings for different scenarios. For instance, a higher value of N might lead to more accurate CMI estimation but could also increase computational cost, while the range of beta could affect the degree of output concentration.

3. The proposed method introduces computation overhead, but the comparisons of computational costs are missing. The method introduces extra computation for minimizing CMI and performing multiple transformations, what is the relative computational cost of training a CMIM-protected model compared to a standard model and other protection methods? As we can see, the experiments are primarily conducted on small datasets, with very limited testing on the larger ImageNet dataset. The lack of computational cost analysis makes it difficult to assess the practical feasibility of the method, especially for large-scale applications. A detailed breakdown of the computational cost associated with each step of the proposed method, compared to standard training and other protection methods, is necessary.

### Questions
Please see the Weaknesses. Other questions:
The proposed method seems to be limited to a single-label classification setting. Can the method potentially extend to regression or multi-label classification, where outputs are continuous or to predict multiple classes simultaneously? Can the method be adapted to protect the IP of the state-of-the-art models, e.g., LLMs, CLIP, and Diffusion models, which require it most?

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
The authors tackle the topic of *defending* trained models from getting *stolen* through knowledge distillation. They investigate when the teacher models are *undistillable* by knowledge distillation and introduce the CMIM method to train teachers to concentrate the predicted probability vectors in close clusters to minimize the information available for distillation. They theoretically introduce and support their method and empirically test the procedure as well as other *defence* techniques against multiple *attacking* techniques.

### Strengths
- The topic of undistillable models is highly relevant, particularly given the growing online prevalence of large closed-source models.
- The paper is mostly well-written with mostly appropriately supported claims.
- The authors provide a nice balance between theoretical and empirical results.

### Weaknesses
 - L040: Missing reference to theoretical paper by Borup and Andersen (2021), “Even your Teacher Needs Guidance: Ground-Truth Targets Dampen Regularization Imposed by Self-Distillation,” NeurIPS.
- *"An insight is provided that in order for a DNN to be undistillable, it is desirable for the DNN to possess the trait that each cluster of the DNN’s output probability distributions corresponding to each label is highly concentrated to the extent that all probability distributions within the cluster more or less collapse into one probability distribution close to the one-hot probability vector of that label.”* Although, I am unable to provide a reference, that a concentrated probability distribution is uninformative, and thus desirable to avoid distillation is, to the best of my knowledge, common knowledge in the field, and should not be considered a contribution of this paper. The authors' claim of concentrating *clusters* of probability distributions is not sufficiently differentiated from the existing understanding that concentrated probability distributions are less informative for distillation.
- Replacing $\hat{Y}$ with $\hat{Y}^\alpha$ in the MI and CMI is simply replacing a variable in a function; the change itself is not inherently innovative and warrant a notion of "contribution". However, the implications and importance of doing so may hold some importance. The core issue is that the transformation of the output probabilities by $\alpha$ is a post-hoc operation, and the implications of this transformation on the information content of the probability vectors is not sufficiently explored. The authors do not provide a clear justification for why this specific transformation is optimal for reducing distillability.
- Section 4.1 appears redundant, as the extension follows naturally by substituting variables (see also comment above). The mathematical derivations in this section do not introduce any fundamentally new concepts beyond the variable substitution. The authors should clarify why this section is essential and not merely a restatement of the previous section with different notation.
- Variance estimates in Appendix J reveal that multiple cases deemed "undistillable" in Table 1 do not definitively qualify as such. Specifically, the reported variances are not sufficiently small to definitively conclude that the proposed method is superior to label smoothing in all cases. A more rigorous statistical analysis is needed to support the claims of undistillability.
- Table 2 mistakenly labels "RSP" as "RSG" and "RSD."
- Omitting CE from Table 1 limits insight into the distillability of the standard training procedure, and it is unclear how much better the proposed method is to the simplest baseline. Without the CE baseline, it is difficult to assess the practical improvement of the proposed method over standard training techniques.
- (Minor) When introducing notation, some notation is used before it is introduced. Consider reordering this section so that no notation convention is used before it has been introduced.
- Equation (3): avoid using $\times$ if it solely represents normal multiplication.
- L403: "intensive" -> "extensive."
- L520-L524 could be rephrased, as the current phrasing appear redundant and confusing.

### Questions
- Please elaborate on the computational requirements of doing the proposed alternating optimization, where the optimization of the Q’s is done over multiple minibatches (I assume for each alternating step)?
- Proving a negative result is challenging empirically; the inability to surpass LS with tested KD methods does not necessarily imply that no viable methods exist or that the models trained were optimally configured. Without theoretical proof of undistillability, the results can unfortunately only be seen as the current state, as new (or already existing and untested) methods for KD might render the claims of this paper invalid soon. Please elaborate on why the results should be considered sufficient to prove a negative result.
- Table 1: A concerning number of results are reported as less than 10, which is either incorrect/faulty reporting or potential issues with collapsed training. If collapsed training runs, this supports the concern above (about negative results), and the authors should investigate and elaborate clearly on this.
- What happens if $\alpha = 1$? Setting $\alpha > 1$ naturally forces the simplex to be more concentrated in the corners, but this post-transform is not applicable to the probabilities a knockoff-student would train on.

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
3

### Summary
The paper presents a method for protecting black-box models against knowledge distillation by student models. The authors define a DNN as distillable if a student model learned from its output outperforms the same model learned from ground truth labels. The proposed objective for the teacher model consists of a standard CE loss and a regularization term based on a tempered conditional mutual information (CMI) between the input and network predictions. Its aim is to make the output of the network close to one-hot encoding. Since the proposed objective is not tractable, through a series of approximations the authors propose a tractable objective. The authors demonstrate their method on CIFAR-100, TinyImageNet, and ImageNet using various teacher and student models, and against other baselines methods.

### Strengths
* The paper introduces a novel objective based on conditional mutual information that includes optimizing over a power-transformed probability distribution.
* Approximating the intractable terms of the objective is original although I am not sure that it is justified. I validated Theorem 4.1.
* I am not an expert in this field, but the experimental part seems very comprehensive in terms of datasets, student and teacher networks, defense strategies, and compared methods.
* The proposed approach seem to be the only one that makes the network not distillable on all benchmarks.

### Weaknesses
 * I believe that further justification, evidence, or analysis (theoretical or empirical) is required to relate the approximation of the second term in the objective to the original one (as $\omega$ was taken to be a finite number). There is some discrepancy that needs to be settled as eventually instead of maximizing over $\mathbf{\alpha}$ (which makes sense), averaging is done over multiple values. Also, can you please share what values of $\omega$ were used in the paper? I didn't find this information.

* Experimental section:
  * I find the improvements over competing methods, and in particular label smoothing, marginal in most cases. I acknowledge that label smoothing does not adhere to the requirement of a network being undistillable, but it gets quite close to it. I am not convinced whether the minor improvements over it really make a difference in practice. Perhaps additional analysis or experiments in other scenarios can demonstrate the practical significance of your method over label smoothing. 
  * This may be a criticism in general for defense methods in this domain and not specifically for this paper. It seems that the evaluation is done under the assumption that the student model has access to the input only ($\mathbf{x}$). How likely is that setup? In my opinion, a more realistic setup is distilling a model based on a new dataset altogether. I believe that a comparison in this setting will be much more informative.

* The paper has some writing issues in my opinion:
  * Some of the sentences are too long which makes it hard to understand at first pass (e.g., the first sentence of the abstract and the sentence in lines 46-50).
  * Some sentences are not clear until properly explained in the paper. For instance, "cluster of its output probability distributions in response
to all sample instances" or "cluster corresponding to each label should ideally collapse into one probability distribution", both are in the abstract.
  * In several locations there seems to be confusion in the citation format or whether a citation is justified at all (e.g., lines 72, 80)
  * The link for the code doesn't work.
  * Table 1 is very busy. The authors should consider breaking it down into several tables/figures.

* The authors claim that their training method makes the network undistillable, but it is validated only empirically. No formal proof is given. This is not an actual weakness since I acknowledge that giving such proof is hard and perhaps even impossible. Hence, it would be beneficial to discuss the limitations of the work in general and the empirical validation specifically. Perhaps adding a section on potential failure cases or datasets/methods where CMIM might not hold would help to provide a more balanced perspective on the method's applicability.

### Questions
* The paper seems to rely heavily on Yang et al. (2023). What is the technical novelty of this paper besides including the power-transformed elements?

### Soundness
3

### Presentation
2

### Contribution
3
