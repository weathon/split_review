# Exploring the Camera bias of Person Re-identification

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
We empirically investigate the camera bias of person re-identification (ReID) models. Previously, camera-aware methods have been proposed to address this issue, but they are largely confined to training domains of the models. We measure the camera bias of ReID models on unseen domains and reveal that camera bias becomes more pronounced under data distribution shifts. As a debiasing method for unseen domain data, we revisit feature normalization on embedding vectors. While the normalization has been used as a straightforward solution, its underlying causes and broader applicability remain unexplored. We analyze why this simple method is effective at reducing bias and show that it can be applied to detailed bias factors such as low-level image properties and body angle. Furthermore, we validate its generalizability across various models and benchmarks, highlighting its potential as a simple yet effective test-time postprocessing method for ReID. In addition, we explore the inherent risk of camera bias in unsupervised learning of ReID models. The unsupervised models remain highly biased towards camera labels even for seen domain data, indicating substantial room for improvement. Based on observations of the negative impact of camera-biased pseudo labels on training, we suggest simple training strategies to mitigate the bias. By applying these strategies to existing unsupervised learning algorithms, we show that significant performance improvements can be achieved with minor modifications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes to measure the camera bias and develop a simple normalizaiton methods to address the affects of such bias. Experiments also shows the effectiveness of the proposed method.

### Strengths
1. A thorough investigation of camera bias in reID is a big contribution. This paper provides a quantitative view for bias measuring, which is most welcomed.
2. The consequently proposed debiasing normalization is very simple yet effective, with sufficient experimental and theorical analysis.
3. The new findings could advanced exisiting reID methods.

### Weaknesses
 1. The adopted reID method is not new, missing some newly proposed methods.
 2. If the number of cameras arise to a big one, e.g., 10k in a region, would the bias disappeared? Or the bias could be supressed by multi-view learning?

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper empirically investigates camera bias in person re-identification (ReID) models. The authors measure camera bias in ReID models across unseen domains, demonstrating its amplification under data distribution shifts. They analyze the role of feature normalization in mitigating bias, showing it effectively addresses specific bias factors like low-level image attributes and body angles. Furthermore, observing the negative effect of camera-biased pseudo labels on training, the paper proposes simple training strategies to alleviate this bias.

### Strengths
The paper is well-written, with clear motivation and visual aids enhancing the analysis. The main contributions of this work are as follows:
1. The authors investigate camera bias in ReID models across unseen domain data, offering a comprehensive analysis that spans diverse learning methods and model architectures.
2. The authors' analysis explains why it is effective for bias mitigation and shows its applicability to detailed bias factors and multiple models.
3. The authors explore the risk of camera bias inherent in unsupervised learning of ReID models, showing that the performance of existing unsupervised algorithms can be effectively enhanced by simple modifications to reduce the risk.

### Weaknesses
1. The authors’ analysis lacks consideration of the spatial distribution of features, such as a scatterplot of features downscaled to two dimensions using t-SNE. This visualization could reveal feature distributions under camera bias conditions.

2. The paper primarily addresses domain differences as camera biases. However, another type of camera bias, i.e., the number of samples varies between different cameras, and the identity labels may also be different, is not mentioned in the paper. The authors are welcome to discuss this bias.

3. The description of the training strategy in 5.3 is too simple. Does discarding bias clustering drastically reduce the training samples? In addition, the parameter settings of the clustering algorithm can affect the clustering results, and whether there is a correlation between the settings of these parameters and the camera bias. This is not discussed by the authors

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper discusses camera bias, where it might come from, and a simple normalization solution. In particular, the paper uses a test-time batch to compute the feature mean and variance of each camera and then normalize the features in each camera. The method is shown to be useful across backbones and training methods.

### Strengths
- Overall I like this paper. The authors obviously provided lots of interesting insights. They found that existing methods have camera bias, especially for self-supervised/unsupervised ones. The ones that have dedicated camera-aware design has less camera bias. I believe this observation is new. 

- The method is simple and effective. While this method has been used in test-time adaptation, authors use it to address a different problem in person re-id, which should be encouraged. 

- Rich insights are provided why camera bias arise. 

- I particularly like the fact that this method can be used to deal with human viewpoint bias (Sun and Zheng, 2019). Authors clearly have strong understanding of the field. 

- The paper is well written.

### Weaknesses
I don't have particular problem with this paper. If I'm to write this paper, perhaps I will improve the structure a bit more. But given that this paper talks about observations, insights, and an easy solution, perhaps the current struture is fine.

Reviewers may have a problem with novelty. But I would champion this way of doing research - there is no need to come up with some new method if the paper is sound and insightful in itself.

### Questions
None.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To tackle the camera bias issue in person ReID models, this paper offers a comprehensive analysis and proposes a straightforward yet effective test-time post-processing method. Experiments conducted on several ReID datasets demonstrate the method's effectiveness. Overall, the paper is well-written and thorough, but the comparison experiments are somewhat limited, and the novelty of the proposed method may be restricted.

### Strengths
1.The paper is thorough and well-written.

2.The paper offers a comprehensive analysis to address the camera bias issue in person ReID models.

### Weaknesses
1.As similar feature normalization techniques [R1, R2] have been extensively explored in domain generalization (DG) and domain adaptation (DA) tasks, my main concern is that the novelty of this paper may be limited. It would be beneficial to highlight the advantages of this paper compared to existing DG methods for clearer presentation.

2.In my opinion, the effect of the proposed method is similar to that of domain generalization (DG) methods. Therefore, it is not appropriate to directly compare it with supervised or unsupervised methods in the DG setting (training on MSMT and testing on other datasets). For a more thorough comparison, it would be helpful to include additional related DG and DA methods in the experiments. 

3.In Table 3, it shows that the improvement achieved by combining the proposed method with the supervised person ReID task (highlighted in red) is limited. More analysis is needed to explain the reasons for this limitation in this context. 

4.Since ICE-CAM and PPLR-CAM have demonstrated that unsupervised person ReID methods can benefit from camera information, the improvements observed in the unsupervised ReID setting (highlighted in gray) may be due to the incorporation of camera information in these methods. Could the proposed method further enhance the performance of ICE-CAM?

### Questions
1.As similar feature normalization techniques [R1, R2] have been extensively explored in domain generalization (DG) and domain adaptation (DA) tasks, my main concern is that the novelty of this paper may be limited. It would be beneficial to highlight the advantages of this paper compared to existing DG methods for clearer presentation.

2.In my opinion, the effect of the proposed method is similar to that of domain generalization (DG) methods. Therefore, it is not appropriate to directly compare it with supervised or unsupervised methods in the DG setting (training on MSMT and testing on other datasets). For a more thorough comparison, it would be helpful to include additional related DG and DA methods in the experiments. 

3.In Table 3, it shows that the improvement achieved by combining the proposed method with the supervised person ReID task (highlighted in red) is limited. More analysis is needed to explain the reasons for this limitation in this context. 

4.Since ICE-CAM and PPLR-CAM have demonstrated that unsupervised person ReID methods can benefit from camera information, the improvements observed in the unsupervised ReID setting (highlighted in gray) may be due to the incorporation of camera information in these methods. Could the proposed method further enhance the performance of ICE-CAM?

[R1] Domain-specific batch normalization for unsupervised domain adaptation, CVPR, 2019.

[R2] Batch normalization embeddings for deep domain generalization, Pattern Recognition, 2023.

### Soundness
2

### Presentation
3

### Contribution
2
