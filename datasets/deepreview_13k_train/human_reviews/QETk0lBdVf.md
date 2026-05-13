# Long Context Transfer from Language to Vision

- Decision: Reject
- Scores: 6, 5, 8, 5, 5

## Abstract
Video sequences offer valuable temporal information, but existing large multimodal models (LMMs) fall short in understanding extremely long videos. Many works address this by reducing the number of visual tokens using visual resamplers. Alternatively, in this paper, we approach this problem from the perspective of the language model. By simply extrapolating the context length of the language backbone, we enable LMMs to comprehend orders of magnitude more visual tokens without any video training. We call this phenomenon \textit{long context transfer} and carefully ablate its properties. To effectively measure LMMs' ability to generalize to long contexts in the vision modality, we develop V-NIAH (Visual Needle-In-A-Haystack), a purely synthetic long vision benchmark inspired by the language model'
s NIAH test. Our proposed Long Video Assistant (LongVA) can process 2000 frames or over 200K visual tokens without additional complexities. With its extended context length, LongVA achieves state-of-the-art performance on Video-MME and MLVU among 7B-scale models by densely sampling more input frames.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Current LLMs struggle to understand very long videos because of the context length limitation. This paper addresses this issue by proposing a new method that extends the input context length of LLMs. The method includes three key ingredients: 1) continuous pretraining the LLM with a large context window on text-only dataset, 2) aligning the long-context LLM with image data, 3). tokenizing images (or videos) with the so called UniRes that divides images into grids and flatten the visual tokens in each grid. To evaluate the effectiveness of the method on long video understanding, they introduce a new benchmark called V-NIAH where the task is to retrieve one frame that is randomly inserted into a long video. They also evaluate the method on other video question answering benchmarks. On all the benchmarks, their model "LongVA" demonstrates state-of-the-art performance.

### Strengths
1. The proposed method achieves the state of the art on multiple video understand benchmarks. 

2. The proposed method is simple and effective. The continuous pretraining on large context window only needs text data, while the multimodal alignment stage only requires image-text data. The uniRes encoding is straightforward extension of AnyRes to videos. Nevertheless, the model seems to generalize surprisingly well to videos. 

3. The Needle-in-a-Haystack test seems to be novel in the context of long video understanding. This new task could be an interesting testbed for long video understanding in the future.

### Weaknesses
1. Despite the impressive empirical results, there are not much explanations. In particular, I am interested in understanding why the long-context pretraining on text-only data could transfer to long video understanding.

2. It is not clear on how the image-text alignment is done e.g., training data and losses. Most of the content in the Sec. 3.2 is about the UniRes which is relatively straightforward. 

3. The number of grids during training is limited to 49 (Line 205), which is effectively equivalent to 49 frames. Why does the model could generalize to handle more than 2K frames give that it is trained with only 49 frame inputs?

4. The results in Table 4 show that LongVA outperforms the methods that are much larger and trained on videos e.g., LLaVA-NeXT-Video-34B. Meanwhile, VILA-1.5 achieves the best results with only 8 frames. Those results seem to imply that the input frames and video-specific training are not that important for video understanding. I found this phenomenon counter intuitive. But this might be caused by the different LLM backbones. One interesting experiment I would suggest is to ablate context length and video specific training with the same LLM. 

5. Temporal understanding is arguably an important aspect in video understanding. Being able to process a large number of video frames does not indicate a strong capability in temporal understanding. Most of the experiments shown in the paper can be solved by "selecting" one frame or very few frames. The model might not be able to understand fine-grained motions/actions, for example Something-Something V2 dataset.

### Questions
What would be the performance of VILA-1.5 on the V-NIAH benchmark?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a novel way to implement long-context Video MLLM, which only requires long context training of plain text and image-text alignment training.
- The trained long-context LLM is used for image-text training. Through the designed UniRes visual information encoding method, the long-context LLM can be extended to the long-context video MLLM without video-text training.
- A Visual Needle-In-A-Haystavk (V-NIAH) benchmark is proposed to test the capabilities of long-context video MLLM.
- By inputting more frames for reasoning, the proposed LongVA achieves SOTA performance on Video-MME and MLVU.

### Strengths
(1) Explored a method to implement long-context video MLLM from the perspective of long-context text training. The idea is very interesting.  
 
(2) The evaluation of long-context text retrieval (NIAH) and video retrieval (V-NIAH) is very complete and well presented.   

(3) The experimental results are rich. LongVA was evaluated on different multi-modal benchmarks and achieved SOTA performance on Video-MME and MLVU.

### Weaknesses
 (1) The results of LongVA on some benchmarks are not ideal, such as ActivityNetQA and VideoChatGPT, which is reflected in the fact that more frames do not show better video understanding ability. This makes people suspect that LongVA only has the ability to retrieve long-context video information, but lacks the ability to understand long-context videos.

(2) The paper does not give detailed training details, such as the training details of the long-context LLM of pure text, the training details of image-text, and the datasets used in these two training processes. It is unclear how the long-context LLM is trained on text data, specifically regarding the context length and the data sources. Similarly, the image-text training lacks specifics on image resolution, text length, and the number of training samples. This lack of detail makes it difficult to assess the validity and reproducibility of the results.

(3) Some experimental results in the article do not show that a long-context MLLM with good video understanding ability has been achieved. And the proposed UniRes has not been proven to be better than the previous AnyRes. The performance of LongVA on Video-MME plateaus after a certain number of input frames, and even decreases with more frames in some cases. This suggests a limitation in the model's ability to effectively utilize long-range temporal information, raising questions about its true long-context video understanding capabilities. Furthermore, the experimental results do not conclusively demonstrate the superiority of UniRes over AnyRes, particularly in tasks that require detailed image understanding.

### Questions
(1) Can training only be performed on a single image? How is the long text obtained in image-text training? Because the trained LLM backbone has a context length of 224K. The training details are not provided.

(2) According to the display of Figure 2, the author treats each frame of the video as a grid of the image during testing, so 576 tokens are formed for inference. In order to input more frames during inference, my understanding is that during image-text training, the image here needs to have a very high resolution? In order to segment more grids, so as to adapt to more frames during inference. How are high-resolution images obtained? For the collection process of the training set, this seems to be a method of exchanging spatial information annotation for temporal information annotation.

(3) Unless the details of the training are given, including the amount of data, image resolution, and text length, it is difficult to understand why simple image-text training can be transferred to the reasoning of videos with very long frames?

(4) Why can image training achieve long-context video MLLM? The author did not discuss and analyze the principle.

(5) The experimental results in Table 4 show that inputting more frames into LongVA does not continuously enhance the performance of Video-MME? Especially in long duration videos, why is this? And as the number of frames continues to increase, it gets worse in short, medium and long. Although other experiments show that LongVA performs well in VNIAH, demonstrating the ability of information retrieval, it does not show the advantage of this model in long video understanding.

(6) In the experimental results of Table 7, in 6 benchmarks, UniRes is better than AnyRes in 4 tasks, which does not prove that UniRes is a better visual encoding method. Why use UniRes instead of AnyRes?

### Soundness
2

### Presentation
2

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
This paper focuses on the challenge of processing long video sequences in Large Multimodal Models (LMMs). Instead of focusing on reducing visual tokens, the authors identify the language model's context length as the key limitation and propose a novel approach called "long context transfer." The method first extends the context length of the language model through training on longer text data, then performs modality alignment without requiring long video-text pairs. They introduce UniRes, a unified encoding scheme representing videos as extended images. They propose V-NIAH, a synthetic benchmark based on the Needle-in-a-haystack test, to evaluate visual context length capabilities. Their resulting model, Long Video Assistant (LongVA), can effectively process over 200K visual tokens (approximately 2000 frames) and achieves state-of-the-art performance on Video-MME and MLVU datasets among 7B-parameter models, demonstrating that increased frame input during inference leads to improved performance on long video question-answering tasks.

### Strengths
1. Novel Perspective: The paper presents a fresh perspective on handling long video sequences in LMMs by identifying the language model's context length as the primary bottleneck rather than following the conventional approach of reducing visual tokens. This reframing of the problem leads to a novel solution pathway.

2. Technical Innovation: The discovery of the "long context transfer" phenomenon represents a significant contribution to the field. The ability to transfer extended context capabilities from language to vision without explicit long video-text pair training is both elegant and practical, potentially influencing future research directions in multimodal learning.

3. Benchmark Contribution: The introduction of V-NIAH provides the community with a much-needed evaluation framework for assessing visual context length capabilities in LMMs. This standardized benchmark addresses a gap in existing evaluation metrics and will facilitate future research in long-form video understanding.

4. Practical Impact: The achieved results are impressive, with LongVA demonstrating the ability to process over 200K visual tokens and showing state-of-the-art performance on established benchmarks. The scalability of the approach (showing improved performance with more input frames) suggests real-world applicability.

5. Methodological Clarity: The proposed UniRes encoding scheme offers a unified approach to handling both images and videos, promoting better integration of these modalities and potentially simplifying the architecture of multimodal systems.

### Weaknesses
1. Visual Encoding Ablations: The paper lacks comprehensive analysis of different visual encoding schemes' impact on performance. Specifically:
   - The comparison between UniRes, AnyRes, and Higher-AnyRes is not thoroughly explored. The paper presents a comparison in Figure 4, but it is insufficient to understand the nuanced trade-offs between these methods. A more detailed analysis, including quantitative results on various benchmarks, is needed to justify the choice of UniRes.
   - The effect of including or excluding base image encoding is not clearly demonstrated. The paper does not provide a clear ablation study on the impact of the base image encoding on the overall performance. It is unclear how much the base image encoding contributes to the final results, and whether it is necessary for all tasks.
   - The impact of different layout configurations for extended images (1 x N, N x 1, etc.) is not investigated. The paper does not explore how the arrangement of the extended image affects the model's performance. Different layouts might lead to different contextual understanding, and this aspect needs to be investigated.
   These ablation studies would provide valuable insights into the robustness and generalizability of the proposed approach.

2. Limited Context Analysis: Given that the paper's core contribution is the long context transfer phenomenon, a more detailed analysis of how different context lengths in the language model correlate with visual understanding capabilities would strengthen the claims. The paper should include a more granular analysis of the performance with varying context lengths, specifically focusing on the point at which performance plateaus or degrades. Furthermore, the mechanism behind this transfer phenomenon could be better explained. The paper does not provide a clear explanation of why and how the language model's context length extension directly benefits visual understanding. This explanation should be supported by empirical evidence and theoretical analysis.

3. Typos: The paper contains several typographical errors, specifically in the references on lines 123 and 125, where parentheses and spaces are missing. While minor, such oversights affect the paper's professional presentation and should be addressed in the final version.

### Questions
See "Weakness" 1 & 2.

### Soundness
4

### Presentation
4

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
The paper addresses a significant limitation in large multimodal models (LMMs) concerning their ability to process extremely long video sequences. The existing approaches primarily focused on reducing the number of visual tokens using visual resamplers, this work proposes a novel perspective by extending the context length of the language model backbone, which allows LMMs to interpret a substantially larger number of visual tokens—up to 2000 frames or over 200,000 visual tokens—without requiring additional video training.  The authors also introduce V-NIAH, a synthetic benchmark designed to assess LMMs' generalization capabilities in handling long visual contexts. The results indicate that the proposed method achieves state-of-the-art performance on the Video-MME task among 7B-scale models.

### Strengths
* The paper is well-written and easy to understand. The figure illustration and captions are informative.
* The authors contributed the V-NIAH benchmark, which is an effective benchmark to test LMMs' ability to locate and retrieve visual information over extremely long contexts.
*  Comprehensive evaluations on two video understanding benchmarks (Video-MME and MLVU) beat most of the baselines.

### Weaknesses
 * The technical contributions of this paper are limited. It appears that the authors' only contribution is the benchmark used to evaluate long-context understanding capabilities, which may not be sufficient for a paper presented at the main conference of ICLR.
* The authors' design to enhance the capability of video understanding in long contexts only involves using a large language model (LLM) with long-context capabilities. Such an improvement is obvious and does not provide new insights. Specifically, the method does not introduce any novel architectural components or training strategies tailored for video processing. The approach essentially leverages existing long-context LLMs and applies them to video data, which is a straightforward application of existing technology rather than a novel contribution. The core idea of processing long videos by simply increasing the context window of the language model lacks technical depth and does not address the specific challenges of long-range temporal dependencies in video.
* Where is the **transfer** mentioned in the title of the article reflected? The authors do not seem to have made any special design considerations for transfer, aside from using a long-context LLM as the base model. The paper does not explore any specific transfer learning techniques or adaptations to facilitate the transfer of knowledge from text to video. The approach relies solely on the general capabilities of the base LLM, without any explicit mechanisms to adapt or fine-tune the model for video understanding. This lack of explicit transfer mechanisms makes the claim of 'transfer' in the title misleading.

### Questions
Refer to weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper addresses the challenge of enabling Large Multimodal Models (LMMs) to process and understand extremely long videos. While previous works have focused on reducing the number of visual tokens through visual resamplers, this paper approaches the problem from the perspective of the language model. By extending the context length of the language backbone, the authors enable LMMs to process significantly more visual tokens without any additional video training. They term this phenomenon "long context transfer," where the extended context capabilities of the language model transfer to the vision modality.

To evaluate this capability, the authors introduce V-NIAH (Visual Needle-In-A-Haystack), a synthetic benchmark inspired by the NIAH test for language models, designed to test LMMs' ability to locate and retrieve information from extremely long visual contexts. They propose LongVA (Long Video Assistant), an LMM that, through context length extrapolation in the language model, can process over 200K visual tokens or 2000 frames without additional complexities or long video training. LongVA achieves state-of-the-art performance among 7B-scale models on the Video-MME and MLVU datasets by densely sampling more input frames.

### Strengths
Novel Approach: The paper introduces a novel method for enabling LMMs to process extremely long videos by extending the context length of the language model, rather than reducing the number of visual tokens. This shift in perspective is innovative and opens new avenues for research in multimodal learning.

Long Context Transfer Phenomenon: The discovery of the long context transfer phenomenon is significant. It demonstrates that the extended context capabilities of a language model can directly benefit the vision modality without additional long video training, which is a valuable insight.

V-NIAH Benchmark: The development of V-NIAH provides a useful synthetic benchmark for evaluating LMMs' ability to handle long visual contexts. This can serve as a valuable tool for the research community to assess and compare models.

Strong Experimental Results: LongVA achieves state-of-the-art performance among 7B-scale models on the Video-MME and MLVU datasets. The experimental results are comprehensive and support the claims made in the paper.

Ablation Studies: The paper includes thorough ablation studies that analyze the properties of long context transfer and the impact of different components of the model, adding depth to the evaluation.

### Weaknesses
Latest LLMs like llama3.2 already has context length up to 128k, which makes this work less valuable.

Limited Real-World Evaluation: While V-NIAH is a useful synthetic benchmark, it may not fully capture the complexities of real-world long video understanding. The reliance on synthetic data could limit the assessment of the model's practical applicability in real-world scenarios. Furthermore, the paper does not sufficiently explore the potential biases introduced by the synthetic data generation process, which could lead to skewed performance evaluations.

Potential Limitations: The paper could delve deeper into potential limitations or failure cases of the long context transfer phenomenon. Understanding scenarios where this approach might not be effective would strengthen the work. For example, it would be beneficial to investigate how the performance of LongVA degrades with increasing noise or irrelevant information in the visual input, or if there are specific types of visual content that are more challenging for the model to process within long contexts.

Clarity in Presentation: While the paper is generally well-written, some sections could benefit from clearer explanations. For example, more detailed descriptions of technical aspects and improved figures could enhance overall readability. Specifically, the paper lacks a detailed explanation of how the visual tokens are actually processed and integrated within the language model's extended context. A more thorough description of the architecture and data flow would be beneficial.

### Questions
Limitations of Long Context Transfer: Can the authors provide more insights into the limitations of the long context transfer phenomenon? Are there scenarios where this approach might not be effective?

### Soundness
4

### Presentation
3

### Contribution
3
