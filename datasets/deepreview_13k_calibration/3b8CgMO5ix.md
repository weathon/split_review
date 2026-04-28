# Model guidance via explanations turns image classifiers into segmentation models

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 8, 3, 6

## Abstract
\lipsum[1]

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the weak supervision with image-level labels to achieve segmentation. It establishes formal parallels between differentiable heatmap architectures and conventional encoder-decoder architectures commonly used for image segmentation.

### Strengths
The studied weak form supervision is interesting and helps understanding the learning of convolution neural networks.

### Weaknesses
The organization and presentation of this paper is poor, and some writing and language use is vague, the paper also lacks clear presentation of its contribution in the context of prior research work. for example, the LRP is used many times in the abstract, main text, image caption, section title, e.t.c, but without given concrete definition, which makes the paper quality poor.

### Questions
N.A.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper establishes formal parallels between differentiable heatmap architectures and conventional encoder-decoder architectures used for image segmentation. It conducts a comparative evaluation of these two approaches in terms of segmentation accuracy, finding that differentiable heatmap architectures, when trained with combined classification and segmentation loss, can achieve competitive segmentation performance. The authors also explore semi-supervised training with varying numbers of pixel-level labels, showing that differentiable heatmap architectures outperform standard U-Nets for segmentation in scenarios with few pixel-wise labels.

### Strengths
- This paper is well written and structured. I enjoyed reading this paper and find the idea quite interesting. The proposed unrolled LRP for benefits from having layer-wise guidance from the heatmaps with the skip and tied-in connections for accurate segmentation map prediction. However, it remains somewhat unclear whether this directly leads to improved segmentation performance, as indicated by the authors. It might be the case that the segmentation results are more closely tied to the quality of the heatmaps. Nevertheless, I feel that the idea is novel and is of sufficient interest to the research community.
- The paper makes use of standard training objectives with the proposed unrolled LRP for semi-supervised segmentation, thereby making it directly usable with any task specific architectures. In general, I am in favour of simple and easy to plug-in methods that can complement already existing approaches.
- The proposed method is well supported by experiment results. The empirical finding that concurrent training for classification and segmentation does not compromise classifier performance and holds up comparably to conventional segmentation architectures is quite intriguing. This finding suggests that the method is more generalizable to classification as well as segmentation.

### Weaknesses
 - Continuining from one of my speculations I mentioned in strengths (point 1), the segmentation performance might be closely tied to the quality of heatmaps. This heatmap quality significantly based on amount of available data and the distribution of classes within a dataset. We already know that classification approaches tend to suffer in performance when there is imbalance in the number of samples per class, and I suspect that challenge may also extend to the segmentation performance. How robust is this method to such real-world scenarios with dataset and class imbalances?


### Questions
- Strengths (point 1) and weaknesses sections have an unanswered question for the authors to respond. I have listed a few more questions below.
- Subsequently, bigger multi-label datasets with large number multiple instances per image can also create more uncertain regions the heatmaps. Is the method able to handle this?
- How would the losses from orthogonal semi-supervised segmentation approaches affect the training with an unrolled LRP? Do you expect to see better performances?
- There is no code currently available, will the authors make it available at some point?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a method to turn image classifiers into segmentation models.

### Strengths
It is a promising research direction to turn image classifiers directly into segmentation models, especially considering that there are many well-performed pre-trained (vision-language) classification models.

### Weaknesses
1. The paper lacks important comparisons with other weakly-supervised semantic segmentation methods that can also extract pseudo semantic masks from image-level labels.
2. The authors claim they do not want to achieve the best semi-supervised performance, but the reported results are unacceptably too poor. And there seems not to be any ablations studies on the proposed method. It is strongly recommended to re-prepare the draft. I do not think this work has been well prepared for ICLR submission.

### Questions
Please refer to the above weaknesses.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper optimizes heatmaps towards improved segmentation performance. The authors establish formal parallels between differentiable heatmap architectures and conventional encoder-decoder architectures for image segmentation. Their experimental results demonstrate that unrolled LRP trained with combined classification and segmentation loss, can achieve competitive segmentation performance across comparable U-Nets. And the architectures they showcased exhibit favourable outcomes in certain weakly supervised training scenarios.

### Strengths
The paper establishes unrolled heatmap architectures as encoder-decoder-style convolutional architectures that can be trained for image segmentation.

The paper proposed the combined classification and segmentation loss and showed that differentiable heatmap architectures yield competitive results when trained with this loss.

The models proposed in this paper outperform comparable UNets in all supervision scenarios, with the performance margin increasing significantly as the level of pixel-level supervision decreases.

### Weaknesses
The paper did not conduct extensive datasets to verify the experimental results.

The contrast algorithm is restricted to U-Net and ignores relevant variants.

The paper specifically examines a limited number of cases comparing differentiable heatmap architectures with classical encoder-decoder architectures for image segmentation.

The language description is not clear, and there are some grammatical errors, such as case misuse.

In Section 2.1 LRP BASICS of the paper, algorithm 1 should be presented with a clearer explanation.

In Section 2.2 UNROLLED LRP ARCHITECTURES FOR CONVOLUTIONAL CLASSIFIERS of the paper, what is the role of the 1x1 convolution mentioned in the "Final classifier layers" part?

In Section 2.3 LOSSES AND TRAINING of the paper, the different weight combinations of the loss function require more experimental support.

In Section 2.4 RELATION TO PREVIOUS FORMAL ANALYSES of the paper, “When trained with classification- and heatmap loss, the gradient of the classification loss backpropagates solely through the encoder, while the gradient of the heatmap loss backpropagates solely through the decoder. This can be leveraged for efficient training”, the phenomenon should be further validated through additional experiments or theoretical analysis in order to establish the credibility of this characteristic.

In Section 2.5 RELATION TO STANDARD ARCHITECTURES of the paper, unrolled heatmap architectures can unrolled heatmap architectures only be applied to U-Net or its related architectures? Can it be extended to a wider range of segmentation models? If not, please explain the reasons. If it can, please demonstrate its application and provide experimental comparisons with other architectures.

In Section 3 UNROLLED HEATMAP ARCHITECTURES FOR SEGMENTATION: RESULTS, please provide a more detailed description of the data selection and include validation on a wider range of datasets. Additionally, please include more comparative analysis regarding the improved U-Net models in the Quantitative Results part.

In Section 3 UNROLLED HEATMAP ARCHITECTURES FOR SEGMENTATION: RESULTS, “the ResNet18 UNet is outperformed by the ResNet50 UNet” ,the conclusion lacks experimental data support.

### Questions
In Section 2.1 LRP BASICS of the paper, algorithm 1 should be presented with a clearer explanation.

In Section 2.2 UNROLLED LRP ARCHITECTURES FOR CONVOLUTIONAL CLASSIFIERS of the paper, what is the role of the 1x1 convolution mentioned in the "Final classifier layers" part?

In Section 2.3 LOSSES AND TRAINING of the paper, the different weight combinations of the loss function require more experimental support.

In Section 2.4 RELATION TO PREVIOUS FORMAL ANALYSES of the paper, “When trained with classification- and heatmap loss, the gradient of the classification loss backpropagates solely through the encoder, while the gradient of the heatmap loss backpropagates solely through the decoder. This can be leveraged for efficient training”, the phenomenon should be further validated through additional experiments or theoretical analysis in order to establish the credibility of this characteristic.

In Section 2.5 RELATION TO STANDARD ARCHITECTURES of the paper, unrolled heatmap architectures can unrolled heatmap architectures only be applied to U-Net or its related architectures? Can it be extended to a wider range of segmentation models? If not, please explain the reasons. If it can, please demonstrate its application and provide experimental comparisons with other architectures.

In Section 3 UNROLLED HEATMAP ARCHITECTURES FOR SEGMENTATION: RESULTS, please provide a more detailed description of the data selection and include validation on a wider range of datasets. Additionally, please include more comparative analysis regarding the improved U-Net models in the Quantitative Results part.

In Section 3 UNROLLED HEATMAP ARCHITECTURES FOR SEGMENTATION: RESULTS, “the ResNet18 UNet is outperformed by the ResNet50 UNet” ,the conclusion lacks experimental data support.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
