# What If We Recaption Billions of Web Images with LLaMA-3?

- Decision: Reject
- Scores: 8, 3, 5, 5

## Abstract
Web-crawled image-text pairs are inherently noisy. Prior studies demonstrate that semantically aligning and enriching textual descriptions of these pairs can significantly enhance model training across various vision-language tasks, particularly text-to-image generation. However, large-scale investigations in this area remain predominantly closed-source. 
Our paper aims to bridge this community effort, leveraging the powerful and \textit{open-sourced} LLaMA-3, a GPT-4 level LLM.
Our recaptioning pipeline is simple: first, we fine-tune a LLaMA-3-8B powered LLaVA-1.5 and then employ it to recaption \app1.3 billion images from the DataComp-1B dataset. Our empirical results confirm that this enhanced dataset, Recap-DataComp-1B, offers substantial benefits in training advanced vision-language models.  For discriminative models like CLIP, we observe enhanced zero-shot performance in cross-modal retrieval tasks.  For generative models like text-to-image Diffusion Transformers, the generated images exhibit a significant improvement in alignment with users' text instructions, especially in following complex queries.
Our project page is \url{https://www.haqtu.me/Recap-Datacomp-1B/}.
\vspace{-.4em}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposes a version of DataComp-1B wherein images are re-captioned by a LLaVA fine-tune of Llama3-8B. The paper trains CLIP models on this dataset demonstrating improvements in image retrieval and regressions on classification. The authors also demonstrate applications of the dataset for text2image generation.

### Strengths
S1. Well written and clear.

S2. Well positioned in the literature.

S3. Extremely non-trivial engineering effort, which I consider a strength.

S4. Very useful dataset contribution (both in terms of quantity of data and scale), opening many future avenues in synthetic data and studying empirical phenomenon associated with training on this kind of data.

S5. Simple approach allowing the authors to study empirical phenomenon, which is the heart of the science in this paper.

S6. Further validation of the LLaVA recipe and it's usefulness for creating VLMs

### Weaknesses
W1. What is "Word distributions of our re-captions and the original captions." in Figure 1? Could you clarify this in the caption. Might also be too much information for this figure and you can consider moving that.

W2. Consider including some numerical outcomes of the dataset in the abstract/intro. e.g., training a CLIP model on [ours] shows a XX percentage point improvement when compared to training on [baseline] on [benchmark].

W3. Missing citation. MINT-1T. Awadalla, et al. 2024.

W4. More evaluation. Could be helpful to add some more evals, for example the average score from the DataComp paper for the CLIP models: https://github.com/mlfoundations/datacomp?tab=readme-ov-file#evaluation. Are there any salient trends in specific datasets and domains? For example, I imagine there could be boosts or hits in non-ImageNet tasks, which seem important to document.

W5. Can the proposed dataset be used in the LLaVA training mix, replacing the LAION fraction, to get a better LLaVA model (conceptually, as a data flywheel).

W6. Given that this is a large download, it could be good to provide statistics for the community about how many images were actually downloaded––to give the community an idea about the link rot affecting DataComp. 

W7. The method itself is not so different from that of other papers (e.g., Nguyen et al. Improving multimodal datasets with image captioning. 2023). However, given that the contributions of this paper are framed properly as a dataset and empirical results, I consider this a very minor weakness. In fact, if other reviewers complain heavily about novelty, I am willing to go to bat for this paper as I feel this criticism is misguided and overlooks the core contributions.

### Questions
Please see Weaknesses. Questions are included their with the corresponding "Weakness".

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents image recaptioning on web-crawled data empowered by LLaMA-3. The proposed LLaVA-1.5-LLaMA3-8B replaces LLM in LLaVA with LLaMA-3 and is trained following LLaVA-1.5's setting. To enhance the caption quality in DataComp-1B, it adopts LLaVA-1.5-LLaMA3-8B for recaptioning. Extensive experiments and analyses are conducted, including the features of recaptions, the mixture usage of original and recaptions, the efficacy on recognition and generation, and the impact across different sizes of architectures.

### Strengths
- The computation on LLaMA-3-powered LLaVA training and recaptioning on 1B data is tremendous. The data generation and evaluation are at scale.
- The modified and trained LLaVA-1.5-LLaMA3-8B model achieves comparable performance with the LLaVA-1.5-13B model across benchmarks for various tasks, including recognition, spatial awareness, OCR, and so on.
- Quantitative analyses regarding caption features and semantic quality are conducted. Recap-DataComp-1B has longer, more diverse, and more aligned captions than the original ones. 
- The recaptioned data helps models with different sizes of text encoders.
- The recaptioned data enhances the image generation quality.

### Weaknesses
- The main innovation lies in the recaptioning process, which has been adopted in data synthesis for better quality [1,2] and representation learning [3]. It is especially similar to [4], image captioning on DataComp, but provides fewer insights. Although the scale is at the billion level, the technical contribution is limited. 
- The prompt will impact the quality of image captioning. In particular, the paper's main contribution is image recaptioning. It would be better if they explored more than one prompt. These experiments do not have to be at the 1B scale. It could be on a reasonable-scale subset.
- Even though the proposed LLaVA-1.5-LLaMA3-8B is better than the previous LLaVA models on the MMMU and MM-Vet benchmarks (understanding/reasoning benchmarks), better image captioning ability and the necessity of LLaMA-3 are under verification. Additionally, there are no comparisons with recaptioned data from other captioning models. It is doubtful whether the data improvement comes from the captioning itself or it actually benefits from LLaMA-3. 
- It seems that the recaptioned dataset leads to much worse performance on ImageNet-1K and similar performance on the retrieval tasks. Table 3 illustrates model performance by training on different portions of original captions. Though the pure reception result (p=0) is not reported, inferring from the trend, it is likely to be worse than pure original caption-trained performance (p=1). The efficacy of recaptions is questionable. 

[1] Improving Image Generation with Better Captions.
[2] A Picture is Worth a Thousand Words: Principled Recaptioning Improves Image Generation.
[3] LLaVA-NeXT: What Else Influences Visual Instruction Tuning Beyond Data?
[4] Improving multimodal datasets with image captioning.

### Questions
- How is the current prompt chosen? How will different prompts for captioning influence the data quality?
- Compared to other captioning models on the image captioning benchmark, how much better is the LLaVA-1.5-LLaMA3-8B? Compared to the original LLaVA recaptioned (or other model recaptioned) datacomp image-text pairs, what is the advantage of LLaVA-1.5-LLaMA3-8B?
- In Table 3, what are the results when training on exclusive recaptions (p=0)? If the performance is worse than p=1, what are the possible reasons?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Web-crawled image-text pairs are noisy and usually are not descriptive enough. This paper studies recaptioning DataComp-1B to obtain detailed and descriptive for images and shows the recaptions can bring benefits to downstream vision-language tasks such as retrieval and text-to-image generation. The authors first fine-tune a LLaMA-3 based LLaVA-1.5, then use it as an image captioner to generate long, detailed captions for images in DataComp-1B. They analyze the lengths distribution before and after this recaptioning step in DataComp-1B, showing the recaptions are longer. They also use LongCLIP and GPT4V to validate the image-text alignment and caption fluency are increased by this recaptioning step. Then, they use the recaptioned DataComp-1B, named Recap-DataComp-1B, to train CLIP models (Recap-CLIP) from scratch. Specifically, they mix the original captions and recaptions in DataComp-1B to find the best way to use the recaptions. In the experimental section, they evaluate the Recap-CLIP on downstream tasks including zero-shot imagenet classification and the text-to-image/image-to-text retrieval tasks. They find the detailed captions can benefit the retrieval tasks but negatively influence the zero-shot classification task. They also conduct experiments on long-caption image-text retrieval benchmarks. To further validate the quality of the recaptions, they train T2I models using recaptions and find the detailed recaptions can help T2I generation.

### Strengths
1. The downstream tasks are comprehensive. The authors study the capabilities of recaptioning through different downstream tasks, including zero-shot classification, retrieval and text to image generation. In most of the benchmarks, recpationing procedure brings positive effects. 
2. The authors conduct experiments on different model sizes, showing the consistent improvements in retrieval tasks. 
3. The recaptioned DataComp-1B can potentially help the development of VLMs in the future.

### Weaknesses
1. Table 3 shows the ImageNet-1K zero-shot classification results and COCO/Flickr30k retrieval results. The authors should also provide the results when mixed ratio p = 0, which means the performances from the model trained using only recaptions. Obviously, the recaptions bring negative effects in the zero-shot classification task. The authors discuss the possible reason may be the missing of specific named entities. For example, in Figure 1, the example "Western Kingbird" is a valid bird class for the image, but in the detailed caption, it is described as "A small, gray and yellow bird with a black beak and black eyes...". Have the authors considered to generate the detailed captions based on the original caption as well? If the original caption can also be provided in the inputs, with a proper prompt, maybe the specific named entities can also be kept in the recaptions. 
2. In Table 6, it would be better if the authors can compare with MetaCLIP as well.

### Questions
Could the authors provide the total inference time on recaptioning the DataComp-1B?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the challenge of noisy web-crawled image-text pairs, which can undermine the performance of vision-language models. The authors propose a straightforward pipeline that uses a fine-tuned, open-source LLaMA-3-8B language model to recaption around 1.3 billion images in the DataComp-1B dataset. By improving textual descriptions, their approach, termed Recap-DataComp-1B, provides a cleaner, more semantically aligned dataset that enhances vision-language model training. Empirical results show performance improvement: for discriminative models like CLIP, zero-shot performance in cross-modal retrieval tasks improves, while for generative models such as text-to-image Diffusion Transformers, image generation aligns more closely with user instructions.

### Strengths
+ Effective recaptioning pipeline improves both discriminative and generative model performance.

+ It shows that the open-source model LLaMA-3 enables accessible advancements in dataset quality.

+ Demonstrated benefits in real-world applications, notably in zero-shot retrieval and text-to-image generation tasks.

### Weaknesses
- The work does not propose new ideas or methods and focuses on empirical verification, but it seems not provide in-depth or insightful experimental analysis, limitations (e.g., hallucination) and strengths of recaptioning, or sufficient valuable practices beneficial to the community. Most of conclusions (e.g., recaptioning is helpful for image generation in DALLE 3) have been known or have been explored in prior work. 

- Is the training with recaptioning harmful to other aspects, e.g., knowledge. Specifically, for example, “Western Kingbird” is recaptioned into a detailed appearance-oriented description. After trained with these recaptions, would the model know the concept “Western Kingbird”? Maybe some evaluations on knowledge-intensive VQA are needed. 

- Using LongCLIP-Large to evaluate semantic alignment between long captions and images may be improper since long sentences may be preferred by this model than short ones. 

- The cost of recaptioning need to be detailed. 

- The section names, e.g., CLIP in Section 5, are not informative enough. 

- Some challenging benchmarks should be considered, e.g., winoground [a] for retrieval and T2I-CompBench [b] for generation. 

[a] Thrush T, Jiang R, Bartolo M, Singh A, Williams A, Kiela D, Ross C. Winoground: Probing vision and language models for visio-linguistic compositionality. InProceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition 2022 (pp. 5238-5248).

[b] Huang K, Sun K, Xie E, Li Z, Liu X. T2i-compbench: A comprehensive benchmark for open-world compositional text-to-image generation. Advances in Neural Information Processing Systems. 2023 Dec 15;36:78723-47.

### Questions
- In Sec 6, why to use the raw CLIP text encoder instead of a encoder trained with recaptioned text? 

- Compared with retrieval, generation preferred recaptioning since the best performance happens in mixed ratio p = 0.00 in Tab 7. What is the reason? 

- Some experimental details are unclear. For instance, what does “re-caption” denote? Using re-captioned prompts for training or inference or both?

### Soundness
3

### Presentation
3

### Contribution
2
