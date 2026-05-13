# Do You Keep an Eye on What I Ask? Mitigating Multimodal Hallucination via Attention-Guided Ensemble Decoding

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Recent advancements in Large Vision-Language Models (LVLMs) have significantly expanded their utility in tasks like image captioning and visual question answering. However, they still struggle with object hallucination, where models generate descriptions that inaccurately reflect the visual content by including nonexistent objects or misrepresenting existing ones. While previous methods, such as data augmentation and training-free approaches, strive to tackle this issue, they still encounter scalability challenges and often depend on additional external modules. In this work, we propose Ensemble Decoding (ED), a novel strategy that splits the input image into sub-images and combines logit distributions by assigning weights through the attention map. Furthermore, we introduce ED adaptive plausibility constraint to calibrate logit distribution and FastED, a variant designed for speed-critical applications. Extensive experiments across hallucination benchmarks demonstrate that our proposed method achieves state-of-the-art performance, validating the effectiveness of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a new Ensemble Decoding (ED) strategy to mitigate the object hallucination issue with Large Vision-Language Models (LVLMs). The proposed approach is motivated by the hypothesize that irrelevant objects and low object resolution in images are likely to impact performance negatively. In ED, the input image is split into sub-images and combines logit distributions by assigning weights through the attention map. ED adaptive plausibility constraint is proposed to calibrate logit distribution. The FastED, an optimized variant of ED, balances performance with speed by selecting a sub-image with the highest mean attention score from the original image. ED shows improved performance in several benchmarks

### Strengths
1. The ensemble decoding strategy proposed in this work is well-motivated and sound by zooming into local regions which is more important for decoding at each decoding step. The proposed method also does not require any training.
2. Starting from the baseline model, several optimization techniques have been proposed to improve model accuracy and running efficiency, including adaptive plausibility constraint to only keep the most plausible tokens, and a fast version ED to only focus on one particular sub-region in the image.
3. Strong performance and new state-of-the-arts have been reported on several benchmarks.

### Weaknesses
The proposed ensemble encoding strategy, fuses the logits extracted from the original image and multiple local crops. This method makes sense, but introduces much more computation burden for real-world deployment. The FastED only processes one local crop and have some accuracy drops. However, one simpler alternative is to move the ensemble to the input, and concat the multiple images in the prompt. We can imagine that this method is much faster than ED/FastED because only one feed-forward is needed. There is no discussion about where to do the ensemble.

 It is unclear how to get the $d\times d$ attention matrix in L161, Section 3.1, where d is the number of image patches. Can the author elaborate the dimension of $Q_t$ and $K_t$ in detail?

As for the logit ensemble, the generated logit should has the same of the size of LLM tokenzier? It is unclear why the proposed adaptive plausibility constraint improves performance by only keeping the elements in #p_ED# which are larger than a threshold?

Do we have any assumption that the length of the generated tokens have the same length? How should we do the logit ensemble when we have different number of generated tokens for different images.

Even though the proposed method is training-free, it also introduces a lot of hyper-parameters $\alpha$, $\beta$, $N$, $H$ and $K$. how to tune these hyper-parameters is unclear.

### Questions
1. it is unclear how to get the $d\times d$ attention matrix in L161, Section 3.1, where d is the number of image patches. Can the author elaborate the dimension of $Q_t$ and $K_t$ in detail?
2. As for the logit ensemble, the generated logit should has the same of the size of LLM tokenzier? It is unclear why the proposed adaptive plausibility constraint improves performance by only keeping the elements in #p_ED# which are larger than a threshold?
3. Do we have any assumption that the length of the generated tokens have the same length? How should we do the logit ensemble when we have different number of generated tokens for different images.
4. Even though the proposed method is training-free, it also introduces a lot of hyper-parameters $\alpha$, $\beta$, $N$, $H$ and $K$. how to tune these hyper-parameters is unclear.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the issue of object hallucination in Large Vision-Language Models (LVLMs), where models generate descriptions that include nonexistent objects or misrepresent existing ones. While previous approaches such as data augmentation and training-free methods have attempted to mitigate this problem, they face scalability issues and often rely on external modules. The authors propose a new method called Ensemble Decoding (ED), which divides input images into sub-images and combines logit distributions by weighting them through an attention map. Additionally, the paper introduces ED’s adaptive plausibility constraint to calibrate logit distributions and a variant named FastED for speed-critical applications. Extensive experiments demonstrate that this method achieves state-of-the-art performance on hallucination benchmarks, confirming its effectiveness in reducing object hallucinations.

### Strengths
- The idea of Ensemble Decoding (ED) is interesting, and well motived by evidences of model will get right answer after applying crop and resize to the image and the toy experiment of checking whether properly divided sub-images can reduce object hallucination in the outputs o LVLMs
- The authors conducted extensive ablation studies and main experiments to validate the effectiveness of the method, and the experimental results appear to be quite convincing.

### Weaknesses
 - There doesn’t seem to be a deeper explanation for why this method works. It would be better if the authors could provide more insights.
How do the degree of cropping and resizing, as well as the attention weights, affect the results? I don’t seem to see any related discussion or analysis on this.

- How do the degree of cropping and resizing, as well as the attention weights, affect the results? I don’t seem to see any related discussion or analysis on this.

### Questions
- Was there any weighting operation applied during the ensemble process?
- Can the authors discuss the relationship between this method and model uncertainty? When we perform multiple forward passes on the model and take the average, we are essentially obtaining model uncertainty. Can this method be understood as adding more logical constraints, but essentially optimizing the answer through model uncertainty?
- Besides logit ensemble, are there other levels of ensemble that could be attempted?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Large Vision-Language Models (LVLMs) excel at tasks like image captioning but face challenges with object hallucination, where they describe objects that aren't actually present in images. While existing solutions like data augmentation have attempted to address this issue, they face scalability problems and often require additional modules. This paper introduces Ensemble Decoding (ED), which works by dividing input images into smaller parts and combining their logit distributions using attention map-based weighting. It also develops ED adaptive plausibility constraint for logit distribution calibration and a faster variant called FastED for time-sensitive applications. Through extensive testing on hallucination benchmarks, the proposed method demonstrates superior performance compared to existing approaches.

### Strengths
1. It is interesting to explore the effect of the number of unnecessary objects in an image and the object resolution on the performance of LVLM.
2. The proposed method is simple and straightforward to implement, which enhances its reproducibility.
3. Experiments on multiple benchmarks demonstrate that the proposed method can achieve better performance than state-of-the-art work.

### Weaknesses
I have some concerns about this paper:

1. From Figure 3, it seems that feeding multiple sub-images into LVLM gives more correct answers than feeding the original image. I'm curious about the performance of ED without using the original image.
2. If LVLM produces the correct output for the original image, but produces the wrong output for the sub-image, does ED negatively affect the understanding of the model in this case? For example, can the split sub-image get a valid output when the target object is located at the centre of the image?
3. It is interesting that low-resolution objects may trigger the hallucination of large models. However, dividing the image into small sub-images does not improve the absolute resolution of the object but rather the percentage of the object in the image.
4. How is the metric of inference latency calculated? ED only slightly outperforms AGLA in terms of recall at the cost of more than twice the inference latency; FastED is close to AGLA in terms of efficiency but has lower recall. So what is the advantage of the method proposed in this paper over AGLA? The authors only show the performance of FastED on the CHAIR dataset, which makes its performance difficult to evaluate.
5. In this paper, there is a lack of analysis and ablation experiments on the impact of the constituent modules in ED (e.g. Attention-Guided Weight, and Adaptive Plausibility Constraint) on the performance of the method.
6.The exact number of sub-images into which the image is split (determined by the hyperparameter N) may have a strong impact on the efficiency and performance of the ED, and the impact of this factor is not analysed in this paper.
7. From Table 4, the improvement from aggregating the logits of sub-images does not seem to be significant.

### Questions
When splitting the original image into sub-images, is there no overlap at all between each sub-image?

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
This paper introduces a technique (ED) to reduce hallucination in multi-modal large language models (MLLMs) by splitting an image into N sub-images followed by using an attention guided ensemble decoding approach which ensembles the logits for the next token to be predicted by the MLLM using the attention weights of the original full-sized image and the N sub-images with the text prior. The authors conduct a systematic study which shows the two main causes of object hallucination in MLLMs as the number of objects in an image and the image resolution. They also provide systematic quantitative metrics which show improvement on hallucination benchmarks compared to existing SoTA methods and regular decoding approaches. The authors present a latency analysis of their method compared to other decoding based methods and provide a alternative baseline of FastED which balances accuracy with speed. Overall the paper is well written and conducts systematic experimental analysis.

### Strengths
1) The paper is very well written and it is easy to understand their method. 
2) The approach presented is easy to implement, is training-free and only requires inference time re-weighting of logits. 
2) The pilot study which talks about the main causes of object hallucination in MLLMs is instructive and useful to the community as a whole. 
3) It is easy to understand the motivation of their method from the conclusions of the study they present, which shows that masking irrelevant regions of an image helps reduce object hallucination, and their approach of ensembling logits from various sub-images should help with that
4) The results achieve SoTA performance on commonly used benchmarks to measure hallucination (POPE and CHAIR)

### Weaknesses
1) While the idea of splitting the original image into N sub-images is well motivated from the pilot study, the approach to utilize the attention weights to re-weight the logits lacks theoretical/empirical justification. Even intuitively, it would make sense to use attention weights for prompts such as "is there a spoon in the image" to put a higher emphasis on the sub-image which contains a spoon. However, for generic prompts such as "describe the image", the attention weights across the sub-images should be more or less equal. In such cases I am not sure of the reason why it might be useful to weight the logits by the attention scores. 
2) Adding on to 1, the paper lacks experiments/ablations which justify the use of attention weights for the decoding process. Adding ablations which vary the temperature parameter might be useful to understand the impact of attention on results. For example, a useful result to conclude the validity of the attention weights could be setting very high values of temperature parameter leading to sampling from uniform distribution across the sub-images. 
3) The paper does not include experiments on tasks other than hallucination and image captioning. For example on the MME benchmark, out of the 16 tasks, the authors only include results on the existence, count, position, and color sub-categories. It would be good to look at the results on some of the other sub-tasks such as code reasoning, OCR, common-sense reasoning, text translation etc. (as done in the VCD paper) to ensure that this method of decoding does not regress the performance on such benchmarks. 
4) The authors show results for FastED only on CHAIR and LLava-Bench, it would be good to see results of FastED on POPE and MME benchmarks as well 
5) This is already mentioned in the limitations section, but the method only works for MLLM architectures which use a linear projector and does not work with resampler and Q-former based architectures (BLIP-2, Qwen-VL). This limits the generalizability of the technique across a wide-range of model architectures.

### Questions
Please refer to the weaknesses section for questions. Additionally: 

1) Have you tried the recent Qwen-2 VL model with your technique? Given that it does not use a Q-former based technique, it would be interesting to see how this method works with a model architecture other than LLava
2) If possible, could you provide some additional examples of attention maps and final attention weights for the N sub-images for different sets of prompts and input images? It would be helpful to understand how exactly the attention weights vary.

### Soundness
3

### Presentation
4

### Contribution
2
