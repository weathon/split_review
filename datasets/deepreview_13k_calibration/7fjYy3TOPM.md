# Zero-shot Object-level Out-of-distribution Detection with Context-aware Inpainting

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Detecting when an object detector predicts wrongly, for example, misrecognizing an out-of-distribution (ODD) unseen object as a seen one, is crucial to ensure the model’s trustworthiness. Modern object detectors are known to be overly confident, making it hard to rely solely on their responses to detect error cases. We therefore investigate the use of an auxiliary model for the rescue. Specifically, we leverage an off-the-shelf text-to-image generative model (e.g., Stable Diffusion), whose training objective is different from discriminative models. We surmise such a discrepancy would allow us to use their inconsistency as an error indicator. Concretely, given a detected object box and the predicted class label, we perform class-conditioned inpainting on the box-removed image. When the predicted object label is incorrect, the inpainted image is doomed to deviate from the original one, making the reconstruction error an effective recognition error indicator, especially on misclassified OOD samples. Extensive experiments demonstrate that our approach consistently outperforms prior zero-shot and non-zero-shot OOD detection approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents RONIN for object-level out-of-distribution (OOD) detection. Given a detected object box and its predicted class label, RONIN first performs class-conditioned inpainting on the image with the object box removed. It then compares the similarities between the original detected objects and their inpainted versions to identify OOD instances.

### Strengths
1. The concept of using inpainting and comparing similarity scores for OOD detection is both reasonable and straightforward.
2. The proposed method outperforms zero-shot baseline methods by noticeable margins.

### Weaknesses
1. The technical contribution is limited. The proposed method simply combines image inpainting with similarity comparison, both of which are straightforward and well-established techniques. The core idea of using inpainting to generate a counterfactual image and then comparing it to the original is not novel. The method lacks a significant technical innovation or a novel way of combining these techniques. The overall approach feels like a straightforward application of existing tools rather than a significant advancement in the field.
2. The paper lacks comparisons with recent methods. The latest method cited in Table 1 is from 2022. Comparisons with more recent approaches, such as [1] and [2], are expected. This makes it difficult to assess the true performance of the proposed method relative to the current state-of-the-art in OOD detection. The absence of these comparisons leaves a gap in the evaluation and limits the impact of the work.
3. It seems from Table 4 the results are highly sensitive to the choice of $\alpha$ and $\beta$, suggesting that careful parameter fine-tuning may be required. The performance fluctuations observed when certain similarity measurements are excluded indicate a lack of robustness in the method. The need for careful parameter tuning could limit the practical applicability of the approach, as it may not generalize well to new datasets or scenarios without extensive experimentation.

### Questions
1. The authors did not conduct experiments on ImageNet-1K, a commonly used dataset for out-of-distribution (OOD) detection. Could the authors provide results on this dataset as well?
2. Instead of performing image inpainting, would generating a complete image of the predicted category using a pre-trained diffusion model work? Can the authors include comparisons with this simple baseline?
3. In Line 261, it is mentioned that "one can use a thresholding method to identify OOD objects effectively". What is the threshold used in the experiments?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a zero-shot object-level out-of-distribution detection method using context-aware inpainting to improve the model's ability to identify unseen objects. By leveraging generative models for class-conditioned inpainting, the differences between detected and original objects serve as indicators of recognition errors. Experiments demonstrate that this approach outperforms existing zero-shot and non-zero-shot OOD detection methods.

### Strengths
1. Proposes a novel approach by integrating generative models for OOD detection, offering a solution distinct from traditional methods.
2.  Supported by data, showing exceptional performance across multiple benchmark datasets.
3. The method does not require modifications to pre-trained models, facilitating integration into existing systems.

### Weaknesses
1. High reliance on generative models may be limiting, especially if the models are inaccurate or under-trained. The performance of the proposed method is intrinsically tied to the quality of the inpainting results. If the generative model struggles to accurately reconstruct objects, particularly those with complex structures or unusual viewpoints, the discrepancy between the inpainted and original object may not reliably indicate an out-of-distribution sample. This could lead to both false positives and false negatives in OOD detection. For example, if the generative model hallucinates details or smooths out important features, the method's ability to detect subtle anomalies will be compromised.
2. The need for extensive image generation and comparison could lead to high resource consumption. The process of generating class-conditioned inpainted images for each detected object, followed by a comparison with the original object, is computationally expensive. This is especially true when dealing with high-resolution images or complex scenes containing multiple objects. The computational cost could limit the practical applicability of the method, particularly in resource-constrained environments or real-time applications. The number of inpainting steps and the size of the generative model will directly impact the processing time and memory requirements.
3. Further validation on a variety of datasets is needed to ensure broad applicability and robustness. The current evaluation might not fully capture the method's performance across diverse real-world scenarios. The method's effectiveness could vary significantly depending on the dataset's characteristics, such as image quality, object diversity, and the presence of domain shifts. For example, a method that performs well on datasets with well-defined objects might struggle with datasets containing cluttered scenes or objects with significant variations in appearance. Therefore, it is crucial to evaluate the method on a wider range of datasets to ensure its generalizability and robustness.

### Questions
Please refer to the Weaknesses box.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new object-level OOD detection method called RONIN, which leverages the off-the-shelf diffusion model to replace detected objects with inpainting.  RONIN adopts a context-aware class-wise inpainting method and combinations of similarity assessment methods. Experimental results show that the proposed method outperforms existing methods in three of 4 settings on Pascal-VOC and BDD-100k.

### Strengths
- S1. Using diffusion inpainting strategy for object-level OOD detection is novel. 

- S2. The proposed method outperforms existing methods in three of four settings.   

- S3. This paper is well written.

### Weaknesses
 - W1. The inference times of comparison methods are not reported. I am concerned that this method may have a longer inference time than the comparison methods. Since the actual application of object-level OOD detection is in areas that require real-time inference, such as autonomous driving, I believe it is necessary to accurately report the inference time of comparison methods.

- W2. I wonder the reason why RONIN’s performance is lower than the comparison methods in BDD-100k vs. OpenImages. It might be better to include the reason for this result. This is because BDD-100k is a driving dataset and closer to the real-world application than VOC.

- W3. The paper does not adequately address the trade-off between performance and speed. While the authors suggest that future faster diffusion models could resolve the efficiency issue, the current performance of RONIN with a reduced number of denoising steps shows a significant drop, particularly on the VOC dataset. This raises concerns about the practical applicability of the method, as it is unclear whether the performance can be maintained with faster diffusion models. Furthermore, the scalability of the method with different diffusion models is not demonstrated, which is necessary to support the claim that the method can be easily adapted with new diffusion models.

- W4. The paper claims that the method is effective in scenarios where accuracy is favored over speed, but this claim is not supported by experimental results. The paper only evaluates performance on common benchmarks like PASCAL-VOC and BDD100K. To demonstrate the applicability of the method in areas such as ecosystem conservation and manufacturing, it is necessary to conduct experiments with datasets relevant to these areas.

### Questions
I would like to know the inference time of the comparison methods.  

I also wonder the reason why RONIN’s performance is lower than the comparison methods in BDD-100k vs. OpenImages.


I am willing to raise the score, taking into account discussions with the author and the opinions of other reviewers.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses zero-shot out-of-distribution (OOD) detection in object detection. Since object detection is often overconfident, the OOD scores computed using only the confidence values of object detection are often unreliable. 

The proposed method uses text-based image inpainting with Stable Diffusion; The proposed method first input the original image in which the regions of the detected bounding box are masked and the name fo the detected object class to Stable Diffusion to get the synthesized image in which the masked regions are inpainted. OOD detection is performed based on the similarity of the embeddings between the inpainted and the original images.

Experiments using PascalVOC and BDD100k as ID datasets and MS-COCO and OpenImages as OOD datasets show the superiority of the proposed method over several existing OOD detection methods.

### Strengths
- The idea of detecting OODs by the similarity of the images before and after inpainting is general, simple and interesting.

- The method of achieving inpainting that preserves the original context associated with the OOD classes by masking the areas that are r% smaller than the bounding box is also simple and interesting.

- The experiments and analysis are generally comprehensive, although there are some serious shortcomings, as discussed below.Although somewhat artificial, the analysis to improve misclassification of ID classes is also interesting.

- The paper is generally well organized and easy to follow.

### Weaknesses
 **W1.** The idea of using image inpainting for OOD detection is novel in itself, but its technical novelty is somewhat limited because it is basically a combination of existing pre-trained image inpainting and classifiers.


**W2.** OOD detection using image inpainting, while interesting, yields several weaknesses.

*W2-1.* As the authors themselves discuss, high-quality inpainting is computationally time-consuming, as inference also takes a long time for each image. This can be a drawback since object detection has many applications where processing time is crucial.

*W2-2.* If the ID class and OOD class are close, image inpainting with clear class distinctions and precise similarity evaluation may become difficult, resulting in less accurate OOD detection. It would be good to evaluate detection performance on datasets that include fine-grained categories and attributes, for example, LVIS and FG-OVD. This would also be relevant to the discussion around Line 076. It would also be good to discuss the object categories that are difficult to inpaint and their impact on performance.

*W2-3.* The results of inpainting are dependent on the initial noise, which can lead to large variations in OOD detection performance. Discussion on this point would be appreciated.


**W3.** Comparisons with existing methods are somewhat lacking. In this paper, the problem is defined as the task of binary classification of each detected object bbox as to whether it is ID or OOD. According to the task definition, a simple baseline would be to apply a zero-shot OOD detection method to each bbox. In particular, the proposed method uses CLIP, but there are other CLIP-based zero-shot OOD detection methods (e.g., CLIPN [Wang et al., ICCV'23]) and few-shot OOD detection methods (e.g., LoCoOp [Miyai et al., NeurIPS'23] and NegPrompt [Li et al., CVPR'24]). Comparisons with these methods should be included.


**W4.** The analysis presented in Table 4 is not exhaustive and does not fully support the validity of the triplet similarity in Eq. 4. In general, adding more hyperparameters should help improve accuracy. To demonstrate the validity of Equation 4, it is necessary to show exhaustive results for sensitivity to alpha and beta, with similarity(ori, \hat{y}) and similarity(ori, inp) each showing performance improvement over a wide range of alpha and beta.


**W5.** Modern object detectors are often open-vocabulary. Demonstrating that the proposed method is effective even in open-vocabulary scenarios is preferable.


**W6.** Other minor points

- RONIN (the name of the proposed method) first appears in the caption of Fig. 1 and Line 059 in the introduction section, but without saying what it stands for. There should be the definition.

- Bold b's appear in Lines 119 and 120 should be italic.

- Fig. 1 and Fig. 2 have considerable overlap in information and could be combined into one.

### Questions
Since the use of image inpainting is the most important idea of the proposed method, its strengths and weaknesses should be fully discussed. In this regard, I would expect thorough responses on **W2**. I would also like to see answers to the lack of comparison with existing methods (**W3**) and the lack of analysis (**W4**), as these are critical issues to clarify the validity and effectiveness of the proposed method. Given the recent emphasis on open vocabulary scenarios for object detection, I would expect an answer for **W5** as well.

### Soundness
2

### Presentation
3

### Contribution
2
