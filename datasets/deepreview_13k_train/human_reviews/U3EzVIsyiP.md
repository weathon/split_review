# Dog-IQA: Standard-guided Zero-shot MLLM for Mix-grained Image Quality Assessment

- Decision: Reject
- Scores: 5, 3, 8, 3

## Abstract
\vspace{-3mm}
Image quality assessment (IQA) serves as the golden standard for all models' performance in nearly all computer vision fields.
However, it still suffers from poor out-of-distribution generalization ability and expensive training costs.
To address these problems, we propose \textbf{Dog-IQA}, a stan\textbf{D}ard-guided zer\textbf{o}-shot mix-\textbf{g}rained IQA method, which is training-free and utilizes the exceptional prior knowledge of multimodal large language models (MLLMs).
To obtain accurate IQA scores, namely scores consistent with humans, we design an MLLM-based inference pipeline that imitates human experts.
In detail, Dog-IQA applies two techniques.
\textbf{First}, Dog-IQA objectively scores with specific standards that utilize MLLM's behavior pattern and minimize the influence of subjective factors.
\textbf{Second}, Dog-IQA comprehensively takes local semantic objects and the whole image as input and aggregates their scores, leveraging local and global information.
Our proposed Dog-IQA achieves state-of-the-art (SOTA) performance compared with training-free methods, and competitive performance compared with training-based methods in cross-dataset scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This submission proposes a standard-guided zero-shot mix-grained image quality assessment method, named Dog-IQA. To deal with the problem of poor out-of-distribution generalization ability and expensive training costs, Dog-IQA proposes two techniques: 1) developing a standard-guided scoring system that aims to establish a clear mapping between quality levels and scores and restrict the MLLM to scoring within a predefined range; 2) Utilizing segmentation models to provide MLLM with the whole image and object-centered sub-images. Although the experiments show the better performance of the proposed method, there are still some concerns about its acceptance.

### Strengths
The experiments show the better performance of the proposed method. The method provides a train-free IQA model benefiting from the powerful foundation models.

### Weaknesses
1)	The mapping between the specific quality levers and annotated quality scores has been proposed and demonstrated as effective in [1]. Thus the idea of “standard-guided” is not novel. For the second technique of introducing pre-trained segmentation models (SAM2) to provide the local quality scores, it is a common and maybe computing expensive tool in IQA.
2)	For the better performance of IQA, it may be largely contributed to the better performance of the used foundation model (mPLUG-Owl3). As shown in Table 6, the performance on SPAQ of the raw mPLUG-Owl3 model reaches 0.858 in SRCC, much better than the 0.347 of mPLUG-Owl2. The performance gains are much worse than the SOTA Q-align, considering that its pretrained model employed the mPLUG-Owl2.
3)	For the validation of the second technique, I would like to know the inner analysis of the mask mechanism for different data or datasets, such as how to get the (quality-sensitive) segmented patches and how to determine their number. At least, from Table 4, s_seg seems to be ineffective.

### Questions
Please refer to the above comments.

### Soundness
2

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
This paper introduces Dog-IQA, a stanDard-guided zero-shot mix-grained image quality assessment (IQA) method exploiting multimodal large language models (MLLMs).
The Dog-IQA objectively scores entire input image and local patches segmented from it, within pre-defined 7-level discrete range.
Those scores are aggregated, specifically the local scores are weighted in proportion to the area of it.
In experiments, Dog-IQA outperforms previous methods even without training.

### Strengths
- Insight2 is a good way to exploit the knowledge of MLLMs.
- Table1 shows a reason 7-level grading is enough.
- Detailed ablation study for each component of Dog-IQA makes it easier for readers to understand it.

### Weaknesses
- Insight 1 seems just hypothesis and not verified, need some citations at least.
- $s_{local}$ has not bounded and its maximum value varies depending on each benchmark. In addition, the score may be affected by the number of objects (segmentation). Then, can we use Dog-IQA as a consistent IQA metric for general use-cases? For example, how should we determine $c_{max}$ for real-world images? Image A has 6.10 and image B has 6.20 but they have a large different number of segmentations then which one is better? I don't think the proposed method guarantees fairness.
- The performance is largely from underlying backbone MLLM, mPLUG-Owl3. For a fair comparison, how about CLIP-IQA with mPLUG-Owl3, or how about Dog-IQA with CLIP?

### Questions
- It seems "remain mask" contains unsegmented areas then those may not important region of interest for IQA. I'm not sure if it's good to use those information. Could the authors provide some examples of the remain masks and some analysis?
- Could the authors compare with the following methods?
> - Re-iqa: Unsupervised learning for image quality assessment in the wild
> - Quality-aware pre-trained models for blind image quality assessment
> - Blind image quality assessment via vision-language correspondence: A multitask learning perspective

### Soundness
2

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
4

### Summary
The authors propose a standard guided zero-shot mix-grained image quality analysis (Dog-IQA). This method takes advantage of pre-trained multimodal large language models (MLLMs), resulting in a training-free style. To better align with human evaluation, they design an inference pipeline with MLLMs. In the experiments part, they show that Dog-IQA achieves SOTA results under the training-free setting. Such a training-free pipeline performs pretty well and contributes to IQA development largely.

### Strengths
The idea is simple yet working. As there are more and more powerful MLLMs being released, how to make better use of them and introduce them into IQA attracts increasing attention. The authors propose a training-free method Dog-IQA without finetuning, which is a clever practice.  

The authors propose the standard-guided scoring mechanism and provide several insights with some results (i.e., Tab. 1). Such a mechanism helps keep the scores consistent and aligned with the standard. As a result, the method could perform robustly in terms of different cases.

Another key component is the mixed-grained aggregation mechanism, which helps refine the final score by aggregating global and local assessments. These global and local views are similar to the pipeline of a human quality analysis system.

The experiments, like the ablation study, are very extensive and demonstrate the effectiveness of each proposed component. Furthermore, the main comparisons on several datasets and metrics show the superior performance of Dog-IQA.

The authors also discuss the limitations of Dog-IQA and give detailed analyses, which provide clues for future works and can further motivate the development of MLLM-based IQA.

The supplementary file provides more details like the segmentation settings, visualization, and prompt. Those materials allow readers to understand and reimplement this work better. Plus, the authors promise to make the code public, which makes this work more solid.

The writing and organization are pretty good. The authors provide extensive different forms of presentation, such as figures (e.g., overall comparison in Fig. 1, pipeline in Fig. 3), tables, algorithms, visualization (e.g., Figs. 4 and 5), and prompts in the supplementary file. Such a good presentation also makes this work more convincing.

### Weaknesses
The authors claim that the standard-guided mechanism helps ensure consistent quality evaluation. How to show or support the consistency with some more specific results? Some metrics, like variance, could be used to show consistency.

As an MLLM-based IQA method, Dog-IQA could take much longer time to process the inputs, especially when the image resolution is large, like 2K, 4K, or 8K. Also, the GPU memory usage can also become larger. Such a resource consumption may hinder the practical usage of Dog-IQA.

In Tab. 3, Dog-IQA performs the third best on KADID-10k with training set KonIQ or SPAQ. The authors did not give sufficient analyses.

It could be better to provide parameter comparisons between the proposed Dog-IQA and others. I am wondering if the superior performance comes from a larger number of parameters.

### Questions
By using MLLMs, how does the method process high-resolution images efficiently？

Can we also train Dog-IQA under the same settings as other related works, like Q-Align? If so, it is better to provide the results of Dog-IQA?

In Tab. 3, under the training-based IQA case, Dog-IQA still performs well on SPAQ and AGIQA-3k datasets and ranks third on KADID-10k. What are the possible reasons behind this?

In Tab. 6, mPLUG-Owl3 outperforms other MLLMs largely. Can we assume that the excellent performance of Dog-IQA mainly comes from the strong base model, mPLUG-Owl3?

How about using multiple MLLMs to process IQA? Will this combination obtain better results?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, the authors propose Dog-IQA, a training-free image quality assessment (IQA) method designed to address limitations in out-of-distribution generalization and high training costs. By leveraging the advanced prior knowledge of multimodal large language models (MLLMs), Dog-IQA aligns IQA scores more closely with human evaluations. Specifically, two main improvements are introduced: 1) discrete scoring rather than continuous value inference, and 2) a segmentation-based mixed-grain aggregation mechanism to refine final quality scores. Competitive results across cross-dataset scenarios validate the method's advantages.

### Strengths
1. Enhances MLLM capabilities for image quality inference in a training-free manner, effectively reducing training costs.
2. Proposes a human rating-inspired quality inference approach, incorporating discrete scoring and local-global quality aggregation.

### Weaknesses
1. The authors use SAM for segmentation in quality inference, but using a complex model as a preprocessing step adds computational cost. If a secondary model is used before MLLM for image preprocessing, one might consider integrating an IQA-specific model to improve performance.
2. Ablation studies were conducted only on SPAQ and AGIQA-3k datasets. However, testing mPLUG-Owl3 on other datasets with a similar approach as Q-bench achieves comparable performance without the proposed strategy, suggesting its limited effectiveness across datasets.
3. Generalization to other MLLMs should be verified, as the method should apply across diverse MLLMs for practical use; broader testing would confirm the proposed strategy's robustness.
4. Segmentation may be less effective in cases of severe distortion, which is common in IQA tasks. In such cases, segmentation failures could potentially negatively impact quality inference.

### Questions
1. Ablation studies on additional existing datasets are recommended to further validate the effectiveness of each design component.
2. Verifying generalization across other MLLMs is also suggested to ensure robustness.

### Soundness
2

### Presentation
3

### Contribution
2
