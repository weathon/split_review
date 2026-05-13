# Gone With the Bits: Revealing Racial Bias in Low-Rate Neural Compression for Facial Images

- Decision: Reject
- Scores: 3, 3, 6, 5

## Abstract
Neural compression methods are gaining popularity due to their impressive rate-distortion performance and their ability to compress data to extremely small bitrates, below 0.1 bits per pixel (bpp). As deep learning architectures, these models are prone to bias during the training process, potentially leading to unfair outcomes for individuals in different groups. In this paper, we present a general, structured, scalable framework for evaluating bias in neural image compression models. Using this framework, we investigate racial bias in neural compression algorithms by analyzing 7 popular models and their variants. Through this investigation we first demonstrate that traditional distortion metrics are ineffective in capturing bias in neural compression models. Next, we highlight that racial bias is present in all neural compression models and can be captured by examining facial phenotype degradation in image reconstructions. Additionally, we reveal a task-dependent correlation between bias and model architecture. We then examine the relationship between bias and realism in the image reconstructions and demonstrate a trade-off across models. Finally, we show that utilizing a racially balanced training set can reduce bias but is not a sufficient bias mitigation strategy.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a framework for assessing bias in neural image compression models, analyzing seven popular models and finding prevalent racial bias, manifested as unequal degradation of facial features. The study indicates that while using a racially balanced dataset helps mitigate bias, it is not a complete solution. The study indicates that while using a racially balanced dataset helps mitigate bias, it is not a complete solution.

### Strengths
Strength: (1)The topic of this paper is novel, and the racial bias of image compression on face data sets is studied (2)The authors have conducted quite sufficient experiments around this argument to verify that this problem does exist

### Weaknesses
Weakness: (1)Although the author presents a novel topic, it seems that the author did not fully explore the way to solve the problem. Using a more balanced dataset seems to be one solution, but after discussion by the authors, this approach does not completely eliminate racial bias. So, how to better solve this problem? The author needs to give further elaboration. In fact, this is the point I am most concerned about. (2)The authors used traditional metrics such as PSNR and SSIM in their experiments to reflect racial bias. However, these metrics differ significantly from human visual experience. I wonder if the authors explored more perceptual metrics, such as LPIPS or FID?

### Questions
Weakness: (1)Although the author presents a novel topic, it seems that the author did not fully explore the way to solve the problem. Using a more balanced dataset seems to be one solution, but after discussion by the authors, this approach does not completely eliminate racial bias. So, how to better solve this problem? The author needs to give further elaboration. In fact, this is the point I am most concerned about. (2)The authors used traditional metrics such as PSNR and SSIM in their experiments to reflect racial bias. However, these metrics differ significantly from human visual experience. I wonder if the authors explored more perceptual metrics, such as LPIPS or FID?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigated the racial bias problems existing in learned image compression. The authors built a framework to systematically examine the extent to which racial bias occurs in compression. Based on the evaluating framework, they proposed a classification-accuracy-based loss function to better reveal the bias. The correlation between bias, model architecture and image realism has been measured. They also show that utilizing a racially balanced training set cannot fix the problem.

### Strengths
1.	The paper has a clear problem definition, constructed a reasonable evaluation framework.
2.	Existing experiments have proved the existence of the problem from multiple angles to a certain extent

### Weaknesses
1.  The paper seemly shows few contributions to the compression community. Since the paper just proposes the racial bias problem existing in learned image compression but provides no solution from the compression perspective. Similar evaluation schemes seem to be applicable to any field. Have you considered proposing compression-specific bias mitigation techniques?
2.  It seems that the bias problem is mainly attributed to the dataset and optimizing method. But the authors only focus on the data-related reasons and do not explore the impact of model optimization methods on this issue. It seems unconvincing to simply attribute the difference in model bias to the difference in model architecture. Have you considered analyzing how different loss functions or training regimes impact bias in compression models?
3.  The authors did not provide bias analysis results for images decoded by traditional codecs like JPEG, HM and VTM. The optimization of traditional codecs is not affected by the distribution of the dataset and should not lead to bias. If this experiment can be provided, it will promote our understanding of this problem. Please estimate traditional codec results at equivalent bitrates using the same bias evaluation framework.
4.  The author used the accuracy of the classification model to evaluate the loss of image attributes at low bitrates. However, the classification model was learned on undistorted images, and whether it can accurately classify features on distorted images is unverified. Additional experiments should be conducted in this regard to enhance the persuasiveness of the bias-related conclusion. For example, you could compare classifier’s results with human evaluations on a subset of distorted images and report the accuracy.

### Questions
Please refer to above weakness part.

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
4

### Summary
The paper presents an analysis of racial bias in different neural compression algorithms. To measure this, the method uses face/phenotype classifiers and measure how much the classification decision is affected by the neural compression algorithm. This is similar to a rate-distortion measure where distortion is classification error instead of pixel error. The paper shows a clear bias in neural compression algorithms when trained on imbalanced datasets which is only partially mitigated by using balanced data.

### Strengths
The work here is interesting and timely. As neural compression continues to approach a usable state, but has yet to be deployed in any meaningful way, it is extremely important to start considering any potential bias in trained models or inherent to the algorithms. This way, the community can develop mitigations and ensure that those mitigations are used in future products. Additionally, I think the metrics used by the method to quantify bias are sensible and the finding that traditional distortion metrics, such as PSNR, do not accurately capture bias is a good result. This also makes sense since many compression techniques use pixel-error metrics as their objective. 

Although there is some overlap with prior work, as discussed in the paper, I think there is significant value in extending the analysis to neural compression.

### Weaknesses
While the classification error metrics presented in the paper is a good start it may need some additional development to make it fully capture bias. As the authors point out: the metric is only as good as the classifier itself. If the classifier is not able to make reliable decisions then the metric could miss bias or overly assign bias. I think this topic deserves more attention. Additionally the sensitivity of classifiers to different frequency degradations (which are common for compression); this may also explain different classification results at low bitrates. Specifically, the paper does not explore the impact of different types of frequency degradation (e.g., high-frequency loss vs. low-frequency loss) on the classifier's performance, and how these degradations might interact with different facial features relevant to the phenotype classification. This is important because compression algorithms often introduce artifacts that are not uniform across the frequency spectrum, potentially leading to spurious correlations with the classifier's decision. Furthermore, the paper should investigate the robustness of the classifier to these frequency-based artifacts, as a classifier highly sensitive to specific frequency bands could lead to misleading bias measurements. Finally, there is an entire class of compression algorithms based on Implicit Neural Representations (see SIREN [1] for one example) which train a neural compression model unique to each example. This kind of technique could help mitigate any bias but these were not tested in the paper.

### Questions
* How can we show better reliability of the classification metric?
* Could INR methods overcome potential bias in neural compression?

### Soundness
3

### Presentation
3

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
This paper investigates racial bias in neural compression models for facial image compression, particularly at low bitrates. The authors demonstrate that traditional distortion metrics are insufficient for capturing racial bias, which manifests in noticeable degradation of facial features, especially for darker-skinned individuals. They examine the relationship between bias, model architecture, and visual realism, and show that while balancing the training dataset can help reduce bias, it does not fully eliminate it.

### Strengths
1. This paper investigate bias in neural compression models, bringing attention to an underexplored area of fairness in AI. The authors reveal clear biases, particularly in skin-type degradation. 

2. The raised issue is very noteworthy and worth investigating, as it holds certain value for the generalization and reliability of neural compression methods.

### Weaknesses
1. One of the major concern is that: while the paper identifies the presence of bias, the essential reasons are not thoroughly explored and mitigation strategies suggested (like dataset balancing) are not shown to be completely effective.

2. The experiments demonstrate that balancing the training dataset can help but does not fully mitigate the bias.  If the dataset balance is not working well. Network architecture’s impact on bias could be critical and should be analyzed further.

3. Exploring the fundamental causes of bias is critical. For instance, what would the bias level and visualized results be like if the network is trained and tested on an Africa-only dataset?

### Questions
1. Bias is defined as the maximum difference in loss (Eq. 3 and Eq. 6). How to deal with the impact of extreme values on results and how well does this definition of bias reflect the overall dataset?

### Soundness
3

### Presentation
3

### Contribution
2
