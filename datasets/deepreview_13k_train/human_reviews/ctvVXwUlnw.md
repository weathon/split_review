# A Causal Framework for Aligning Metrics of Image Quality and Deep Neural Network Robustness

- Decision: Reject
- Scores: 3, 8, 5, 5

## Abstract
Image quality plays an important role in the performance of deep neural networks (DNNs) and DNNs have been widely shown to exhibit sensitivity to changes in imaging conditions. Large-scale datasets often contain images under a wide range of conditions prompting a need to quantify and understand their underlying quality distribution in order to better characterize DNN performance and robustness. Aligning the sensitivities of image quality metrics and DNNs ensures that estimates of quality can act as priors for image/dataset difficulty independent task models trained/evaluated on the data. Conventional image quality assessment (IQA) seeks to measure and align quality relative to human perceptual judgements, but here we seek a quality measure that is not only sensitive to imaging conditions but also well-aligned with DNN sensitivities. We first ask whether conventional IQA metrics are also informative of DNN performance. In order to answer this question, we reframe IQA from a causal perspective and examine conditions under which quality metrics are predictive of DNN performance. We show theoretically and empirically that current IQA metrics are weak predictors of DNN performance in the context of classification.  We then use our causal framework to provide an alternative formulation and a new image quality metric that is more strongly correlated with DNN performance and can act as a prior on performance without training new task models. Our approach provides a means to directly estimate the quality distribution of large-scale image datasets towards characterizing the relationship between dataset composition and DNN performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This work investigates how image quality impacts the performance of deep neural networks (DNNs). The authors propose that aligning image quality metrics with DNN sensitivities could allow these metrics to serve as proxies for predicting image or dataset difficulty. Using a causal framework, the authors examine the predictive power of IQA metrics on DNN classification accuracy and find them to be weak indicators. Building on these findings, the authors introduce a new image quality metric that better correlates with DNN performance. This novel metric offers a more effective method for estimating the quality distribution in large image datasets.

### Strengths
The authors proposed an generalised notation for IQA metrics and how it’s connected to classification accuracy. The paper is well-organised, well-written and easy to follow.

### Weaknesses
The main weakness is that no comparison of ZSClip-iqa with recognition-aware quality metrics is given. There is a class of IQA metrics that predict not subjective quality, but classification accuracy. For example, “ Towards Machine Perception Aware Image Quality Assessment”, “ Quality assessment for face recognition based on deep learning”, “ Ser-fiq: Unsupervised estimation of face image quality based on stochastic embedding robustness.” The proposed framework lacks a clear demonstration of its utility in classifying or improving upon existing IQA metrics. The paper does not adequately address how the proposed framework situates itself within the broader landscape of IQA research, particularly concerning metrics explicitly designed for DNN performance prediction. The lack of comparison to these existing methods makes it difficult to assess the practical value and novelty of the proposed approach. The paper also does not provide sufficient evidence that the proposed metric, ZSCLIP-IQA, offers a significant advantage over existing recognition-aware metrics. Without such a comparison, it remains unclear whether the framework leads to a genuine advancement in the field or simply provides an alternative formulation.

### Questions
1) What is the relation of the proposed metric and the existing IQA metrics designed for face/image classification accuracy?
2) What is the transferability of the proposed metric for predicting DNN performance in tasks other than classification?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a causal framework to determine the relationship between IQA metrics and DNN robustness. The authors run a study with two recent DNN-based IQA methods on how these metrics predict DNN robustness, finding them weakly predictive. The work ends with developing a task-guided IQA metric that aligns better with DNN sensitivities.

### Strengths
1. First, I appreciate how well the authors have presented the paper. The paper is relatively easy to read, and the results are nice to interpret. 
2. A causal framework helped set up the problem of predicting DNN robustness using IQA metrics. Also, clearly stating the desired outcome along with the problem formulation was helpful. 
3. A well-enough coverage of IQA metrics (ranging from BRISQUE to CLIP-IQA). 
4. Convincing empirical results to support the theoretical framework.

### Weaknesses
 1. Experiments limited to the Image Classification task would have been preferred if Object detection/ Image segmentation tasks could have been added to strengthen the results of the proposed causal framework substantially.
2. (minor enhancement) Figure 3 (and similar figures), it is difficult to assess the correlations per distortion category from a single plot . This is especially true in the case of Figure 3, where the correlation is poor. Can a better way to represent visually be provided? Apart from the results reported in the tables. 
3. Domain Gap:   The experiments are conducted on ImageNet and its corrupted synthetically generated variant, which might not represent the diversity of real-world data. 
4. Only one image classification dataset is used. It would be interesting to see results on images from one of  SVHN (http://ufldl.stanford.edu/housenumbers/), CIFAR-10/100  (https://www.cs.toronto.edu/~kriz/cifar.html), MNIST (https://yann.lecun.com/exdb/mnist/)

### Questions
1. Can the authors propose a solution based on the causal framework that can be unimodal? For example, the Image Classification task is unimodal, leveraging multimodal representations to solve the problem while being acceptable. It would be interesting to explore a solution using only image domain representations.
2. While the results with ImageNet are convincing, could the authors run experiments with at least one other image classification dataset, such as CIFAR10/100, SVHN, or MNIST? Or at least provide some explanation.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper seeks to investigate the effect of training image quality on the performance and robustness of trained DNN outcomes. They first characterize the inefficiency of conventional IQA methods targeting HVS under the classification context and then propose a causal framework to formulate another image quality metric correlating to DNN performance.

### Strengths
It is a very interesting and fresh view to investigate the causal relations between quality-related features and task-related features in DNNs. The problem formulation and solution are clearly stated.

### Weaknesses
Despite the efforts mentioned above, there remain several weaknesses in this paper, as stated below.
* The wording and phrasing of this paper are intricate, which significantly impacts its readability.  The text is too long and not coherent, and there are numerous grammatical errors throughout, making it somewhat difficult to understand. 
* In this work, the authors restrict the definition of _image quality_ to a very narrow scope, which is the authentic distortions. However, in many mainstream data augmentation methods in the image classification task, applying artificial distortions to original images is a common practice. What is the reason that the proposed framework cannot be extended to artificially distorted image quality? 
* In contrast to the previous comment, the authors utilized artificially distorted images, such as JPEG compression and additional noise, as the corrupted images. Is this a contradiction to the previous statement?
* In line 141, what is _priori_ knowledge?
* In the introduction, the authors mentioned not only the concept of image quality but also the image difficulty regarding content. However, I cannot find relevant measures on this aspect aside from the _technical quality_ indicators such as corruption, contrast, or capture noise, while the content distribution of training datasets is of crucial importance for image classification tasks. Is this an implicit assumption that the dataset is balanced in content?
* In line 195, how to understand _at least_ correlated? If the relations between X, Q, and M cannot support strong causation, then how could the entire causal presumption stand?
* In sec. 4.1, the authors employ IN-val and IN-c as clean and corrupted image sets, respectively. Why can you regard the IN-val as _clean_ under the NR-IQA context?
* The contribution of this paper reminds the reviewer of _core set selection_.  Can this paper contribute to this aspect?
* This paper primarily assumes without substantial justification that image quality metrics directly correlate with DNN robustness or performance under varying conditions. This assumption might be overly simplistic.

### Questions
See my comments above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper aims to establish a causal link between image quality metrics and DNN performance to enhance robustness. However, the study lacks depth in its analysis and fails to convincingly demonstrate the practical implications of its proposed causal framework.

### Strengths
1. The paper aims to bridge the gap between image quality assessment and DNN performance.
2. Theoretical exploration of the relationship between IQ metrics and DNN behavior.
3. The authors provide a new image quality metric aligned with DNN sensitivities.

### Weaknesses
It is unclear why the authors chose to use a causal framework to analyze the relationship between image quality and DNN performance across various IQA settings.
* The notation is overly complex, making it difficult to recognize the technical details of the proposed causal framework.
* The paper does not clarify the differences between Fig. 1 and Fig. 4, nor does it address potential confounders in establishing causal relationships between IQ metrics and DNN performance.
* The theoretical underpinnings of the causal framework are not sufficiently articulated, which may lead to misunderstandings about how the proposed model operates.

* While the authors emphasize that D4 should be independent of any task-specific model, the TG-IQA is trained for a specific task. This issue requires further elaboration.
* The experiments rely heavily on a single dataset (ImageNet) and do not assess the generalizability of the findings across diverse datasets or tasks.
* The reported correlations between the proposed IQ metric and DNN performance are weak. A more detailed analysis of these results, including confidence intervals and significance levels, is necessary.
* The paper suggests that the new IQA metric can serve as a prior for DNN performance without adequately demonstrating this capability in a variety of contexts, such as the IQA performance validation.

### Questions
* While the authors emphasize that D4 should be independent of any task-specific model, the TG-IQA is trained for a specific task. This issue requires further elaboration.
* The experiments rely heavily on a single dataset (ImageNet) and do not assess the generalizability of the findings across diverse datasets or tasks.
* The reported correlations between the proposed IQ metric and DNN performance are weak. A more detailed analysis of these results, including confidence intervals and significance levels, is necessary. 
* The paper suggests that the new IQA metric can serve as a prior for DNN performance without adequately demonstrating this capability in a variety of contexts, such as the IQA performance validation.

### Soundness
3

### Presentation
2

### Contribution
2
