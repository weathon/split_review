# Statistical Test for Anomaly Detections using Variational Auto-Encoders by Selective Inference

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
Over the past decade, Variational Autoencoders (VAE) have become a widely used tool for anomaly detection (AD), with research advancing from algorithm development to real-world applications. However, a critical challenge remains --- the lack of a reliable method to rigorously assess the reliability of detected anomalies, which restricts its use in high-stakes decision-making tasks such as medical diagnostics. To overcome this limitation, we introduce the VAE-AD Test, a novel approach for quantifying the statistical reliability of VAE-based AD. The key advantage of the VAE-AD Test lies in its ability to properly control the probability of misidentifying anomalies under a pre-specified level of guarantee $\alpha$ (e.g., 0.05). Specifically, by carefully analyzing the AD process of VAE, which operates through piecewise-linear functions, and leveraging the Selective Inference (SI) framework to assign valid p-values to the detected anomalies, we prove that theoretical control of the false detection rate is achievable. Experiments conducted on both synthetic and real-world datasets robustly support our theoretical results, showcasing the VAE-AD Test’s superior performance. To our knowledge, this is the first work capable of conducting valid statistical inference to assess the reliability of VAE-based AD.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
This paper addresses an important problem: the lack of a statistical reliability test. The authors use VAEs for anomaly detection. They offer a test procedure and offer a theoretical framework to measure how reliable the anomaly detection process is.

### Strengths
+ Important problem to consider
+ Rigorous mathematical analysis

### Weaknesses
 - One dataset with a few thousand images is not enough to establish that the statistical test is reliable in practice. The dataset's characteristics, such as image resolution, object diversity, and the nature of anomalies, can significantly influence the performance of the VAE and the statistical test. A single dataset might not capture the variability encountered in real-world scenarios, making it difficult to generalize the findings. Furthermore, the size of the dataset, while sufficient for training a VAE, may not be large enough to robustly validate the statistical test, especially when considering the tail behavior of the anomaly scores, which is crucial for reliability assessment.

### Questions
-

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
This work presents an interesting statistical test for anomaly detection (AD) based on VAE. First of all, the authors introduce a test statistic for AD. Then they introduce CSI  for image dependent AD. Additionally, the authors present definitions of piecewise-assignment functions and piecewise linear functions to estimate the test statistic in CSI under VAE-based method. Experimental results also echo the theoretical analysis in some extent.

### Strengths
1. A novel and interesting idea on anomaly detection based on VAE.

### Weaknesses
1. There are several theoretical presentation errors which weakens the credibility of the theory and may confuse the readers. For example, in line 211, the marginal distribution is wrongly expressed. Besides, p in line 205 and 211 is not well defined before. Additionally, there may exist other wrong symbol problems and unclearly explained symbol problems in the manuscript.

To elaborate, the expression for the marginal distribution in line 211 appears to incorrectly sum over the conditional probabilities. The correct marginalization should involve integrating over the latent space of the VAE, not summing over a set A. Furthermore, the variable 'p' is used in lines 205 and 211 without a clear definition of what it represents in the context of the statistical test. This lack of clarity makes it difficult to understand the subsequent theoretical derivations. The manuscript needs a thorough review of all mathematical notations and expressions to ensure they are consistent and well-defined.

2. Some symbols seem meaningless, for example, in Sec. 3, the authors split the input image into a signal space and a noise space. However, according to the analysis afterwards, I feel that it has nothing to do with the following descriptions.

The separation of the input image into signal and noise components in Section 3 seems arbitrary and lacks a clear connection to the subsequent statistical analysis. The authors do not provide a mechanism for how this separation is achieved, nor do they use these components explicitly in the later derivations. This raises questions about the purpose of introducing this concept, and it appears to be an unnecessary complication that does not contribute to the core methodology.

To sum up, the weaknesses of 1 and 2 make the soundness and readability poor.

3. It is not clear that the VAE need to be trained from scratch or fine tuned from some pre-trained visual models.

4. As for experiments, the datasets used for verifying effectiveness of the proposed method are limited. Additionally, the comparison methods are also limited, old and not popular. There are too few quantitative results.

### Questions
See the weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes the VAE-AD Test, a statistical framework designed to assess the validity of detected anomalies in pixel reconstruction errors using a Variational Autoencoder (VAE). The authors argue that a significant limitation in the literature on VAE-based anomaly detection is the lack of rigorous statistical measures to validate detected anomaly regions, which is critical for high-stakes applications like medical diagnostics. To address this gap, the authors formulate a statistical test based on differences in average reconstruction errors inside versus outside detected anomalous regions, leveraging Conditional Selective Inference (CSI) to compute valid post-selection p-values via Piecewise-Assignment Functions.

### Strengths
The paper addresses an important problem in the field of deep learning-based anomaly detection by proposing a method for validating detected anomalies using the same dataset. Applying Conditional Selective Inference to assess the reliability of anomaly detection with VAEs fills a notable gap in this area, providing a statistical approach to validate model outputs in scenarios where reliable decisions are essential.

### Weaknesses
•  Defining Anomalous Regions: The method defines an anomalous region as the set of pixels with reconstruction errors exceeding a user-defined threshold. This reliance on a threshold could reduce the method's usability in practice, as users may not know the appropriate threshold value. Typically, anomaly detection methods focus first on detecting or identifying anomalous regions (i.e., selecting λ, while a secondary goal is evaluating whether there is sufficient evidence to confirm those regions as true positives.

•  Region Constraints: The authors’ approach allows for detection of any subset of pixels (i.e., it considers all elements in the power set). Many region-based anomaly detection methods impose constraints to ensure detected anomalies are meaningful. For instance, in the case of brain tumor images, there is no restriction to prevent the selection of a scattered set of pixels that do not form a contiguous region, which may occur with a large enough λ . Conversely, a small λ could lead to selecting all pixels except for a few, producing results that are challenging to interpret. This underlines the importance of selecting λ judiciously to achieve meaningful region detection as a preliminary step.

•  Statistical Test Design: The authors’ null hypothesis H0 posits that the average reconstruction error inside the anomalous region is the same as outside. However, their test statistic actually tests whether the average reconstruction error within the region differs from a theoretical expectation under their parametric model (\eta^T*X, equation 7). This subtle difference implies that even if the in-region and out-region errors are not significantly different, the test could reject H0 if the parametric model's expected reconstruction error deviates from the observed value. Similarly, it could fail to reject H0 even when in-region and out-region errors differ, if these deviations do not align with the model’s theoretical expectations.

•  Section 4 Readability: Section 4, which appears to be the critical contribution, is dense and challenging to follow. The writing assumes familiarity with advanced concepts, placing a high cognitive load on readers who wish to fully understand the authors' approach. A clearer breakdown of the key steps, possibly with illustrative examples, could make this section more accessible and persuasive.

•  Related Work: This work has a similar objective to the literature on scan statistics, which aims to detect and test for “anomalous” regions. For example [1,2] tests for difference in vs out the region (which is the authors' original hypothesis setup), [3] extends this to observed vs expected (which is more consistent with the authors’ test statistic) and focuses efficiently finding the most anomalous subset of data points (which would equate to selecting the correct value of lambda). [4] Seems to extend some of the ideas of [3] to medical images as well. And if we alternatively consider the image to be an adjacency graph of pixels you’d have  [5,6,7]. To be clear, none of these use VAE, but  I also think for the authors VAE just represents a vehicle to measure deviations, upon which they then impose parametric assumptions. To be clear, I think VAE is a good vehicle to capture deviation, but given the use of VAE is not new to this work, the key contribution is the detection/testing of the anomalies produced by a VAE, so I am comparing the authors chosen approach to the scan approaches that making the same parametric assumptions could be applied to the deviations of the VAE

•  Experimental Limitations: The experiments provide limited insights into the practical benefits and drawbacks of this approach. Since the authors make no theoretical claims about properties other than the validity of the selective p-value, and given that the motivation is high-stakes AD, the experiments are crucial. However, they currently offer minimal information. For instance, it’s unclear how the threshold λ=1.2 was selected, which could offer practical guidance. Additionally, exploring the effects of different λ values on detection outcomes would provide valuable context: what happens when it is too small or too large. The graphs are somewhat difficult to interpret, lack confidence intervals, and, beyond Type I error and power, do not demonstrate the accuracy of detected regions compared to true anomaly regions.

### Questions
•  Applicability of CSI with Alternative Region Selection: If a more sophisticated region detection approach (like those in scan statistics) were used to detect anomalous regions based on reconstruction errors, could the authors’ CSI method still be applied? In other words, does CSI impose constraints on the region selection process, or could it flexibly accommodate other detection methods?

•  Comparison to Randomization Testing: Many anomaly detection methods assess validity through randomization testing (which could be performed here, given the authors’ parametric assumptions under H0) by generating samples of data under H0, computing the test statistic in these null data samples, and comparing the test statistic in the original data to those from the null data to compute its empirical p-value. Conceptually and theoretically what additional benefits does CSI provide over this approach? Would it be possible to compare CSI with randomization testing as was done with the naive p-value?

### Soundness
2

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
3

### Summary
This paper proposes the VAE-AD Test, the novel appraoch for statistically evaluating the reliability of anomaly detection results using Variational Autoencoders (VAE). The proposed method introduces a test statistic based on the reconstruction error of the VAE, and by applying selective inference to assign appropriate p-values to the detected anomalies, it can theoretically control the false detection rate. The effectiveness of the proposed method is demonstrated, particularly in experiments using medical images.

### Strengths
The proposed method provides theoretical guarantees for the reliability of anomaly detection using VAE, leveraging techniques that are well-suited to the characteristics of VAE, such as Piecewise-Assignment Functions and Piecewise-Linear Functions. Additionally, it introduces interesting techniques for efficiently computing the proposed method. The proposed method makes a significant contribution to the reliability of detection results and is highly useful in critical decision-making tasks, such as in the medical field.

### Weaknesses
The proposed method is interesting, but there are some unclear points. I will write the details in the Questions section, so please refer to it.

 The proposed method is based on the reconstruction error of a VAE, but the rationale for this choice is not fully justified. While the authors mention the use of VAE for anomaly detection, they do not adequately address why a VAE is preferred over an Autoencoder (AE), especially given that the objective function of VAE, ELBO, includes a KL divergence term that might hinder reconstruction quality. The paper does not sufficiently explore the implications of using reconstruction error as an anomaly score, especially when VAEs offer alternative approaches such as probability values calculated through importance sampling or the ELBO itself. The choice of reconstruction error, while simple, lacks a strong justification compared to these alternatives. Furthermore, the paper does not discuss the existing literature that compares VAEs and AEs for anomaly detection, which is crucial for establishing the novelty and relevance of the proposed approach.

### Questions
1. Why does the proposed method use the VAE? Since it is based on the reconstruction error, I think an Autoencoder would be more suitable. Since the objective function of VAE, ELBO, includes a KL divergence term in addition to the reconstruction error, the reconstruction quality may not be very good, as seen in Figure 1.
2. Conversely, what is the reason for using reconstruction error? With the VAE, it is possible to calculate probability values using importance sampling. I believe probability values would be more appropriate as anomaly scores than reconstruction error. ELBO could also be used as an alternative to probability values.
3. As in Eq. (3), Gaussian noise is being added to the original data. As mentioned at the beginning of Section 6, its covariance matrix is set in two different ways. It seems that the noise based on the identity matrix shows better results, but noise following the identity matrix would be large if the image is normalized, and small if it is not. How would the performance change if the variance were scaled by a constant, such as $\beta I$?
4. In Eqs. (5) and (7), the difference in the mean values of each pixel between the normal and anomaly regions is used as the test statistic. I don't fully understand the reason for adopting this test statistic, so could you explain it? It seems obvious that the pixel values would differ between the normal and anomaly regions.

### Soundness
3

### Presentation
2

### Contribution
2
