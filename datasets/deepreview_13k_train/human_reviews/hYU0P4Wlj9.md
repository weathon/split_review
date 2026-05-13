# LIME-Eval: Rethinking Low-light Image Enhancement Evaluation via Object Detection

- Decision: Reject
- Scores: 8, 8, 3, 6

## Abstract
Due to the nature of enhancement--the absence of paired ground-truth information, high-level vision tasks have been recently employed to evaluate the performance of low-light image enhancement.  A widely-used manner is to see how accurately an object detector trained on enhanced low-light images by different candidates can perform with respect to annotated semantic labels. In this paper, we first demonstrate that the mentioned approach is generally prone to overfitting, and thus diminishes its measurement reliability. In search of a proper evaluation metric, we propose LIME-Bench, the first online benchmark platform designed to collect human preferences for low-light enhancement, providing a valuable dataset for validating the correlation between human perception and automated evaluation metrics. We then customize LIME-Eval, a novel evaluation framework that utilizes detectors pre-trained on standard-lighting datasets without object annotations, to judge the quality of enhanced images. By adopting an energy-based strategy to assess the accuracy of output confidence maps, our LIME-Eval can simultaneously bypass biases associated with retraining detectors and circumvent the reliance on annotations for dim images. Comprehensive experiments are provided to reveal the effectiveness of our LIME-Eval. Our benchmark \href{https://huggingface.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The work: LIME-Eval: Rethinking Low-Light Image Enhancement Evaluation via Object Detection, critiques the standard practice of evaluating low-light image enhancement by retraining object detectors on enhanced images—a method prone to overfitting and reduced reliability. Instead, the authors propose LIME-Eval, an energy-based evaluation framework that eliminates the need for retraining detectors or relying on annotated data. They also introduce LIME-Bench, an online platform that collects human preferences on low-light enhancement to align automated metrics with human perception. Experiments on datasets like ExDark demonstrate LIME-Eval’s effectiveness in evaluating enhanced images in a way that closely mirrors human judgment.

### Strengths
1. Higher detection accuracy does not necessarily correlate with superior enhancement quality, which aligns with my understanding of low-light enhancement models. There exists a gap between low-level, human-visual-oriented perception and high-level, machine-vision-oriented objectives. Additionally, as noted in line 68, 'Is fine-tuning detectors a valid approach to evaluating enhancers?' this raises a valuable point. Relying on fine-tuning detectors to fully assess low-light detection performance can lead to overfitting and is not necessarily a scientifically rigorous approach.

2. The paper is well written, easy to understand, and authors conduct extensive experiments to validate their approach, offering thorough insights into the correlations between detector performance, human ratings, and LIME-Eval metrics.

3. LIME-Bench provides a structured way to incorporate human preferences into evaluation, bridging the gap between machine-based metrics and human perceptual quality. Which could also be helpful to future low-light vision research.

### Weaknesses
1. In the 'enhanced before data augmentation' setting (Table.1), is there a process like 'color jitter'? I think 'color jitter' could introduce significant interference, as it might substantially degrade the results of low-light enhancement if applied. Also the normalization of image maybe also affect the low-light enhancement models. Could the authors provide more detail on this part?

2. The paper mainly uses ExDark and synthetic datasets, can this evaluation tool also been used in the low-light face detection dataset UG2+ DARK FACE ?

3. Some previous low-light object detection works, although have not used pre-defined enhancement modules, they remain closely related to this study. They did not use image enhancement models but instead employed other approaches, such as self-supervised learning and domain adaptation, to address the issue of low-light object detection. It would be beneficial for the authors to reference and discuss these works in the related works section (e.g., [1, 2, 3]).

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses the challenge of evaluating low-light image enhancement without paired ground-truth data, as current high-level vision task evaluations can often lead to overfitting and unreliable metrics. To improve this, the authors introduce LIME-Bench, an online platform that collects human preference data for low-light enhancement, creating a valuable dataset to correlate human perception with automated metrics. They further propose LIME-Eval, a novel evaluation framework using pre-trained detectors without retraining or annotation dependencies, to assess enhanced image quality. Through energy-based confidence map assessment, LIME-Eval effectively gauges enhancement accuracy. Extensive experiments validate LIME-Eval's effectiveness, and the code will be publicly available.

### Strengths
1. this paper addresses the challenges of evaluating low-light enhancement techniques via the proposed LIME-Bench online platform, collecting human preference low-light images for low-light enhancement techniques, and the LIME-Eval framework without fine-tuned detection models and annotation labels.

2. the paper demonstrates the uncorrelation of high detection performance to the enhancement quality of the enhanced images through comprehensive studies and analysis. This provides a scientific foundation to support their proposed LIME-Bench platform and LIME-Eval framework.

3. the paper addresses the challenge of evaluating low-light enhancement techniques without fine-tuning detection models and acquiring annotation labels through the energy-based modeling technique.

### Weaknesses
1. the purpose of consdering background prediction in the LIME-Eval framework is vauge. It would be great for authors to describe the benefit of integrating background prediction into the energy-based evaluation function.

### Questions
Please refer to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper argues that using object detectors trained on enhanced low-light images for evaluation is prone to overfitting, reducing reliability. To address this, the authors introduce LIME-Bench, an online platform collecting human preferences to validate the link between human perception and automated metrics. They also present LIME-Eval, a framework using pre-trained detectors without annotations to evaluate image quality, avoiding retraining biases and dependency on dim image annotations.

### Strengths
In the background of low-light enhancement, the quality of the enhanced image may indeed be independent of the target detection performance. To verify this phenomenon, they established an online benchmarking platform, LIME - Bench, and developed a label-free assessment metric, LIME-Eval, for quality evaluation of image enhancement. This is a metric that considers both human vision and machine vision.

### Weaknesses
I think the experiment lacks conviction.
1. Qualitative comparisons on samples from the ExDark dataset are inadequate and even wrong in my opinion. The reason for this is that the augmentation strategy is random and not a fair input to the target detector.
2. How is LIME-Eval integrated into Retinexformer? I don't see it in the appendix either, rather than you just stating the training details.
3. If LIME-Eva is integrated into the detection, will it participate in the calculation of the parameter gradient of the neural network? If it is involved, then I think that LIME-Eva just has the efficacy of a loss function, since the low-light enhanced image is then fed to the target detector for training, which is not referential in nature, as you conclude in Table I.

### Questions
See Weaknesses.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper reconsiders the evaluation of enhancement quality in low-light tasks, identifies the shortcomings of previous enhancement quality assessment methods, proposes a new dataset based on human preferences, and introduces a novel unlabeled image quality assessment method for enhanced images. The practical significance of the issues addressed in this study is commendable. However, the analysis of the problems is somewhat lacking, and the experimental section could be further improved, as detailed in the Weaknesses section.

### Strengths
This paper provides a systematic analysis of methods for measuring the quality of enhanced images in low-light enhancement tasks using object detection. It identifies the shortcomings of previous methods and introduces a new low-light dataset based on human preferences, analyzing the correlation between the evaluations of the object detector and human preferences. Finally, the authors propose a novel unlabeled image quality assessment method that addresses a significant challenge in the current field of low-light enhancement. Overall, this study holds substantial research significance in the domain.

### Weaknesses
1. In Chapter 3, the introduction of the need to verify the issue of information loss due to quantization seems abrupt. The earlier sections do not mention the implementation of quantization strategies during the detector's testing process. If quantization was indeed utilized, please provide a brief overview of the quantization process, including the bit depth and the specific method used to map floating-point values to discrete levels. It is unclear how this quantization impacts the comparison between the 'Enhancement first' and 'Augmentation First' schemes, and this needs to be clarified with specific details about the quantization parameters and their effects on the image data.
2. In Chapter 5, the author fails to analyze how to achieve unlabeled evaluation metrics. The methods section merely outlines the computational processes related to detection-oriented energy-based modeling. The transition from problem introduction to method description is rather abrupt and lacks an analysis of this issue, such as: why is this approach capable of evaluating the quality of image enhancement in an unlabeled manner? Why is the image with the lowest energy value considered optimal? The author should provide relevant analytical descriptions, detailing the theoretical underpinnings of why the energy function correlates with image quality, and how the background and classification scores are combined to create a meaningful metric. The connection between the energy landscape and the perceptual quality of the enhanced image needs to be explicitly established.
3. It is necessary to standardize the meaning of variable x_bg. Why is it referred to as "object output" in line 402, while in line 415 it denotes "background prediction"? Additionally, the method of obtaining x_bg should be specified in this paper. If the network produces multiple object outputs, how should we derive x_bg? Specifically, is x_bg a single scalar value, or a spatial map? If it's a map, how is it aggregated? If the detector outputs multiple bounding boxes, how is x_bg handled for each box, and how are these values combined to produce a single energy score for the image?
4. In Chapter 5.2, Table 2 presents a comparison of the Spearman correlation coefficients for only IQA algorithm, which is insufficient. I recommend including Spearman correlation coefficients for several additional algorithms, including both full-reference and no-reference metrics, to provide a more convincing conclusion. This should include metrics that are known to correlate well with human perception, and metrics that are commonly used in the low-light enhancement literature. The selection of these metrics should be justified.
5. In Chapter 5.3, Table 3 presents the improvements of the method on the object detection metrics mAP and AP50. The author should also indicate whether there are improvements in other metrics (such as recall mAR and AR50). Furthermore, the author could include experimental analyses of additional object detection algorithms (e.g., YOLOX) to enhance the persuasiveness of the conclusions. The choice of detectors should be justified, and the results should be consistent across different architectures.
6. The article lacks citations for certain terms and methods, such as YOLOX, LOL dataset, and LPIPS. The author should include the relevant references in the text and check for any other missing citations. This is crucial for reproducibility and proper attribution of prior work.
7. This paper only discusses the application of detection-oriented energy-based modeling in low-light enhancement tasks. Is this evaluation strategy also applicable to other enhancement tasks (such as rain removal, fog removal, deblurring, etc.)? If possible, I suggest that the authors include a section reflecting on this aspect, such as adding it to the future work section. The discussion should include the potential challenges and adaptations needed to apply the proposed method to these different tasks.

### Questions
The authors need to solve the questions mentioned, particularly question 2, in the weakness part.

### Soundness
2

### Presentation
3

### Contribution
3
