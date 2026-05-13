# Speeding Up Image Classifiers with Little Companions

- Decision: Reject
- Scores: 5, 3, 3, 6

## Abstract
Scaling up neural networks has been a key recipe to the success of large language and vision models. However, in practice, up-scaled models can be disproportionately costly in terms of computations, providing only marginal improvements in performance; for example, EfficientViT-L3-384 achieves <2\% improvement on ImageNet-1K accuracy over the base L1-224 model, while requiring $14\times$ more multiply–accumulate operations (MACs). In this paper, we investigate scaling properties of popular families of neural networks for image classification, and find that scaled-up models mostly help with ``difficult'' samples. Decomposing the samples by difficulty, we develop a simple model-agnostic \textbf{two-pass} \OurMethod algorithm that first uses a light-weight ``little'' model to make predictions of all samples, and only passes the difficult ones for the ``big'' model to solve. Good little companions achieve drastic MACs reduction for a wide variety of model families and scales. Without loss of accuracy or modification of existing models, our \OurMethod models achieve MACs reductions of 76\% for EfficientViT-L3-384, 81\% for EfficientNet-B7-600, 71\% for DeiT3-L-384 on ImageNet-1K. \OurMethod also speeds up the InternImage-G-512 model by 62\% while achieving 90\% ImageNet-1K top-1 accuracy, serving both as a strong baseline and as a simple practical method for large model compression.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a method named Little-Big to accelerate image classification with neural networks. Little-Big uses a light-weight model to quickly classify all of the samples and selects the "hard" samples which get low confidence behind the threshold. Then, it uses a large model to update the prediction for each hard sample. Little-Big can significantly reduce the inference cost and latency for many advanced large classification models without sacrificing the accuracy. The authors provide many experiments with different pairs of large and small models to validate the effectiveness of Little-Big.

### Strengths
(1) The motivation and method of Little-Big is very simple and straightforward. 

(2) It seems that Little-Big is very easy to implement. In addition, Little-Big is model-agnostic which can be applied to models with different scales and architectures.

(3) Little-Big can accelerate a pre-trained model without introducing additional training cost.

### Weaknesses
 (1) Lack of novelty. As the authors say, Little-Big is an embarrassingly simple method, which adopts a large model and a light-weight model for image classification. It's the major advantage but also the major disadvantage of Little-Big. Many previous works share the similar motivation with Little-Big which uses different networks for accelerating, such as early existing and speculative decoding as you mentioned in the paper. While these works mostly include specific and delicate designs. I understand that Little-Big is very simple, but i don't think it's novel.

(2) The proposed method only focuses on the classification tasks. While the authors provide the example about how to extend it to video classification, it's hard to directly apply the method for other popular tasks (e.g., object detection and segmentation), which limits its use.

(3) The authors could include more classification tasks to further prove the generation ability of Little-Big, such as multi-label classification, binary classification.

### Questions
(1) The authors could also plot a figure for top-1 accuracy vs. latency.

(2) How long does it take to load and unload models compared with the inference latency for each batch? I'm wondering whether the method can be used for online inference.

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
3

### Summary
This paper proposes a simple yet effective two-pass algorithm called "Little-Big" to speed up image classifiers.  The core idea is to leverage a smaller, less computationally expensive "Little" model to pre-screen input samples. Only samples for which the Little model exhibits low confidence are then passed to a larger, more accurate "Big" model.  The paper claims that this approach significantly reduces the computational cost (measured by Multiply-Accumulate operations or MACs) for a variety of model architectures and scales, without sacrificing accuracy on ImageNet-1K and other datasets. The authors demonstrate MACs reductions of up to 80% while maintaining or even improving accuracy compared to the single Big model baseline. They also argue that this approach is more effective than existing model compression and adaptive computation methods.

### Strengths
- The proposed Little-Big algorithm is conceptually straightforward and easy to implement. It requires minimal modifications to existing models and training pipelines.
- The paper demonstrates significant MACs reduction across a range of model architectures (CNNs, transformers, hybrids) and scales, suggesting broad applicability.
- Experiments are conducted on multiple datasets (ImageNet-1K, ImageNet-ReaL, ImageNet-V2) to evaluate the robustness and generalizability of the method.
- The Little-Big approach addresses a critical issue in deploying large vision models: their high computational cost. The proposed method offers a practical solution for model compression without retraining or complex modifications.

### Weaknesses
# Major
- The method seems to rely on finding an optimal threshold T on the test set (Imagenet validation set) to determine which samples are passed to the Big model. This raises concerns about potential overfitting to the validation set and its impact on generalization performance. Results should be provided using a threshold determined on the training or a held-out portion of the validation set to address this concern. The current approach of optimizing the threshold on the validation set could lead to an overly optimistic performance estimate, as the threshold is effectively tuned to the specific characteristics of the validation data. This could mask potential issues with the method's ability to generalize to unseen data distributions.
- The paper could benefit from a more comprehensive discussion of related work, particularly in areas like cascade models and dynamic inference methods. Specifically, work on early-exit models [1] and confidence-based dynamic routing [2] appears closely related and should be discussed. This would help to better contextualize the novelty and contributions of the proposed approach. The lack of a thorough comparison with these existing methods makes it difficult to assess the true advantages and limitations of the Little-Big algorithm. The paper should also discuss how the proposed method compares to other techniques that aim to reduce computational cost, such as knowledge distillation, which also leverage smaller models.
- Experiments solely focuses on ImageNet dataset. More experiments needed to understand the robustness of the proposed method. The reliance on a single dataset, even one as large as ImageNet, limits the generalizability of the conclusions. It is unclear how the Little-Big approach would perform on datasets with different characteristics, such as those with different levels of image complexity, object variability, or noise. The paper should include evaluations on a more diverse set of datasets to demonstrate the robustness of the method.
- I also find it difficult to parse the results presented in huge tables: specifically Table 3: there are multiple baselines for DeiT models. Are you comparing results with different baseline accuracies? The presentation of results in Table 3 is confusing due to the multiple baselines for the DeiT models. This makes it difficult to understand the actual performance gains achieved by the Little-Big approach. The paper should clarify the choice of baselines and ensure that comparisons are made against a consistent and well-defined baseline.

# Minor
- [L132] I can't see the definition of "w and l".
- [Section 2.3] Quantization is a key method for compression and not mentioned here. Also Mixture of Depths (https://arxiv.org/abs/2404.02258)
- The paper's use of "hardness" and its relationship to model confidence is not always clear. In some sections, low confidence is equated with hardness, while in others, the opposite is implied. This needs clarification. For example [L199] "which allows us to approximate a "hardness" axis with prediction confidence." hardness means low confidence, no?

### Questions
- Please clarify the relationship between "hardness" and model confidence. Is low confidence always indicative of a hard sample, or are there cases where this assumption does not hold?
- Can you provide results where the threshold T is determined using only the training set or a held-out portion of the validation set? This would help to assess the potential for overfitting to the validation set and the generalizability of the method.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a technique called the Little-Big algorithm. It combines a small and large pre-trained model to improve the trade-off between cost and accuracy. It first applies the small model to a given sample. When the confidence is high, the prediction is returned. Otherwise, the large model is applied, and its prediction is used.

In experiments, the authors focused on the ImageNet-1K image classification task. They demonstrated that the proposed method boosts efficiency for various pairs of models.

### Strengths
S1) The proposed method is practical. It is easy to implement and does not require any modification or additional training of existing models. 

S2) It is widely applicable. For any classification problem, it’s readily available. We could apply it to other tasks as well if we could come up with confidence estimation methods for them.

S3) Extensive experimental results show that the proposed method is robustly performing well in the ImageNet classification task.

### Weaknesses
W1) The proposed approach lacks novelty. The idea of using multiple models with different cost-accuracy tradeoffs is highly common, to name a few, such as speculative decoding for language models and cascade ranking systems for recommendation and information retrieval. 

W2) The experiments are weak. All the experiments are about ImageNet-1k image classification task, so it is quite uncertain whether this method works well for other tasks as well.

### Questions
Q1) Can you develop better ways to explain your idea’s novelty, or do you have any ideas to further enhance the novelty?

Q2) Can this idea be applied to language models as well? Particularly, I'm interested to see how it compares with speculative decoding.

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
4

### Summary
The paper discusses improving the speed of visual recognition systems using a "Little-Big" model setup. The Little model is a smaller architecture that processes examples first. If the confidence is below a predefined threshold, the sample is reprocessed by a "Big" model. This simple setup improves the speed of visual recognition systems on ImageNet, ImageNetv2, and ImageNetReal significantly (without loss in accuracy). The authors experiment with both CNNs and Transformer models. They also study the fraction of examples processed by the Little and the Big network, showing the accuracy as a function of threshold.

### Strengths
- The paper studies an important topic - efficiency of visual recognition models.
- The speedup claimed by the paper is substantial. At a fixed accuracy, their method improves speed by 30%-80% (Figure 1).
- The paper is written clearly and is easily understandable. The investigation presented studies the natural questions that arise with threshold tuning for the Little model's confidence. Figure 3 clearly demonstrates how the accuracy and efficiency change as a function of the threshold.
- The paper accounts for generalization across different datasets by fixing the threshold on ImageNet and analyzing results on ImageNetv2 and ImageNetReal. This is an important aspect of the investigation, as choosing the threshold based on the validation set can create bias.

### Weaknesses
My main concern is the comparison with prior art. As line 437-439 states, "even with tricks that effectively retrained models, many pruning methods are not competitive... with modern baselines... which in essence are better trained ViTs". It seems that the Little-Big method is evaluated using modern architectures and training recipes, whereas other baselines (pruning, etc.) are using older architectures or training recipes. I'm worried that the gains of this method are primarily attributable to the use of newer architectures or training recipes. A fair comparison would use the same architectures as previous works.
- For example, Table 3 shows a datapoint with T=0, meaning the Big architecture is never used.
- Additionally, the baseline architecture in Table 3 ("Our Baseline") is significantly more accurate than previous work's baseline (Yin et al.).

The choice of "Little" network seems arbitrary in some cases. In Table 2, EfficientNet-B2-288 uses EfficientViT as a little network, but most other EfficientNet variants do not. And EfficientNet-B2-288 is not used with EfficientNet-B1, but most other variants are. I have similar thoughts on most of the rows in Table 2. Can you please justify the choice of Little architecture?

Line 132: Equation 2 should have a reference, and there should be some more specific qualifications as to what types of models this equation applies to. Similarly, the characteristic width w_j is not well defined and doesn't have a reference.

Line 150: I recommend also discussing quantization briefly here.

Line 172-173: "ingest gigabits/s of raw visual information and compress it to tens of bits/s" <- this needs a reference

In Table 3, it would help the reader if you mark the baselines by their general approach (e.g. which ones are pruning, etc.).

Line 202: "confidence > 0.5-0.7" <- what does this mean? How can a confidence be greater than a range? Did you instead mean "0.5 < confidence < 0.7"?

### Questions
My main suggestion is regarding the fairness of comparisons with baselines (mentioned above).

I also would like to understand the justification for the choice of Little model (mentioned above).

### Soundness
2

### Presentation
4

### Contribution
2
