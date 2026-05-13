# TextSeg: Reimagining Image Segmentation as Text Generation

- Decision: Accept
- Scores: 6, 5, 8

## Abstract
Multimodal Large Language Models (MLLMs) have shown exceptional capabilities in vision-language tasks; however, effectively integrating image segmentation into these models remains a significant challenge. 
In this paper, we introduce \name, a novel \textit{text-as-mask} paradigm that casts image segmentation as a text generation problem, eliminating the need for additional decoders and significantly simplifying the segmentation process.
Our key innovation is \textit{\textmask}, a new textual representation of segmentation masks where each image patch is mapped to its corresponding text label.
This unified representation allows seamless integration into the auto-regressive training pipeline of MLLMs for easier optimization.
We demonstrate that representing an image with $16\times16$ \textmask yields competitive segmentation performance. 
To enhance efficiency, we introduce the Row-wise Run-Length Encoding (\rle), which compresses redundant text sequences, reducing the length of \textmask\ by 74\% and accelerating inference by $3\times$, without compromising performance. 
Extensive experiments across various vision tasks, such as referring expression segmentation and comprehension, show that \name achieves state-of-the-art performance on multiple datasets by fine-tuning different MLLM backbones. 
Our approach provides an efficient, scalable solution for vision-centric tasks within the MLLM framework

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces TextSeg, a novel approach that integrates image segmentation into Multimodal Large Language Models (MLLMs) by framing segmentation as a text generation task.  The key innovation is the use of semantic descriptors, where each image patch is mapped to a textual label, allowing seamless integration into the auto-regressive training pipeline of MLLMs. By representing images with 16×16 semantic descriptors, the approach achieves competitive segmentation performance. To enhance efficiency, the authors propose Row-wise Run-Length Encoding (R-RLE), which compresses redundant text sequences by 74% and speeds up inference by three times without sacrificing accuracy. Extensive experiments demonstrate that TextSeg attains state-of-the-art results on multiple datasets across various vision tasks.

### Strengths
The authors have conducted extensive experiments and ablation studies to demonstrate the effectiveness of their proposed method.

### Weaknesses
The paper presents a method that integrates image segmentation into MLLMs by introducing semantic descriptors and utilizing a SAM mask refiner. While the approach simplifies the segmentation process by treating it as a text generation task, the technical contributions appear to be more incremental and engineering-oriented. The method essentially adapts existing MLLMs with semantic descriptors to perform segmentation tasks, serving as a baseline framework that can be applied to different MLLM models.

 The authors should clearly mention about the training datasets, additional training datasets for fine-tuning (if accapable) of other methods for a fair comparison. Because we know that with more training datasets (GLaMM, Groundhog), and with fine-tuning on task-specific datasets, we can achieve a better performance.

The proposed TextSeg method incorporates a post-processing step using the SAM mask refiner. As indicated in Table 6, without SAM, the method achieves a cIoU of 73.5, which is lower than most methods in the Generalist Segmentation Models (~7B) category in Table 1. This raises concerns about the fairness of the comparison, as other methods may not use similar post-processing techniques. The authors should clarify how other methods could benefit from similar enhancements.

It would be beneficial to include the inference speed of TextSeg compared to other methods. Providing quantitative metrics on inference time would strengthen the evaluation.

The paper lacks comparisons with recent specialized segmentation models such as PolyFormer [1], UNINEXT [2], and HIPIE [3]. Including these models in the evaluation would provide a more comprehensive assessment of the proposed method's performance relative to the current state-of-the-art.

### Questions
+ Training Datasets: The authors should clearly mention about the training datasets, additional training datasets for fine-tuning (if accapable) of other methods for a fair comparison. Because we know that with more training datasets (GLaMM, Groundhog), and with fine-tuning on task-specific datasets, we can achieve a better performance. 
+ Use of SAM Mask Refiner: The proposed TextSeg method incorporates a post-processing step using the SAM mask refiner. As indicated in Table 6, without SAM, the method achieves a cIoU of 73.5, which is lower than most methods in the Generalist Segmentation Models (~7B) category in Table 1. This raises concerns about the fairness of the comparison, as other methods may not use similar post-processing techniques. The authors should clarify how other methods could benefit from similar enhancements.
+ Inference Speed: It would be beneficial to include the inference speed of TextSeg compared to other methods. Providing quantitative metrics on inference time would strengthen the evaluation.
+ Missing Recent Specialized Segmentation Models: The paper lacks comparisons with recent specialized segmentation models such as PolyFormer [1], UNINEXT [2], and HIPIE [3]. Including these models in the evaluation would provide a more comprehensive assessment of the proposed method's performance relative to the current state-of-the-art.

[1] Liu et al., PolyFormer: Referring image segmentation as sequential polygon generation, CVPR, 2023.

[2] Yan et al., Universal instance perception as object discovery and retrieval, CVPR, 2023.

[3] Wang et al., Hierarchical open-vocabulary universal image segmentation, NeurIPS, 2024.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposed TextSeg, a novel text-as-mask paradigm that casts image segmentation as a text generation problem, eliminating the need for additional decoders. It employs semantic descriptors as a new textual representation of segmentation masks where each image patch is mapped to its corresponding text label. It further compresses predicted token length by using Row-wise Run-Length Encoding to handle contiguous region of same semantic region.

### Strengths
- model pixel label as semantic text token by generalized VLLM model
- compress token length with row-wise run-length encoding
- comprehensive results on referring express segmentation and comprehension

### Weaknesses
 - idea is simple and straightforward
- relies on SAM to get the final pixel level prediction from patch level semantic text token prediction
- should compare with other VLLM approach also with SAM refinement

### Questions
- please discuss how to extend to instance level segmentation
- the name of TextSeg was already used: https://paperswithcode.com/dataset/textseg

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
This paper proposes a new scheme for adapting MLLMs to segmentation by reformulating the mask prediction as a sequence of text labels called *semantic descriptors*. Specifically, the MLLM takes as input an image and query and outputs a mask prediction, represented as a sequence of patch-wise semantic descriptors, consisting of <SEG>, 'others', and the queried target label: <SEG> is a special token that indicates the start and end of the mask, 'others' suggests a background patch, and the target label suggests a target patch. Such formulation allows the MLLM to predict the segmentation task as a sequence of text labels, instead of coordinates or special segmentation tokens, maintaining its original auto-regressive training objective and thereby facilitating easier optimization. Furthermore, the authors propose *Row-wise Run-Length Encoding (R-RLE)* that compresses adjacent repeated tokens in the mask prediction to reduce the number of tokens by 74% and triple the inference speed. The framework, names TextSeg, acheives strong performance on locating tasks like RES, gRES, and REC, showing the location ability of TextSeg, and acheives comparable performance to its MLLM backbone on VQA, suggesting that the MLLM's conversational ability is maintained.

### Strengths
Originality 
- Authors propose a new formulation of mask predictions by MLLMs. Different from previous work that represent masks as a special <SEG> token or coordinates, this work formulates the mask as a sequence of text labels (called *semantic descriptors*) of 'others' and the queried target label. Such formulation allows the MLLM to be trained for segmentation with the LLM's original autoregressive training objective, allowing easier optimization and the maintanence of the architecture. Although the idea to represent a mask as a sequence of texts itself is not unimaginable, the realization of it is original and novel. 
- Authors also propose Row-wise RLE to effectively compress the sequence of semantic descriptors and thereby eliminate any computation burden caused by their new formulation. Although, RLE is an existing technique, the authors effectively adapt it to their configuration, acquiring novelty. Instead of simply proposing a new formulation that would be computationlly heavy by itself, the authors further propose a technique that eradicates this issue, making the formulation applicable and thereby more complete. 

Quality
 - Authors carry out an extensive experiment to check whether their new formulation is generalizable to various MLLMs by using four MLLM backbones: LLaVA-1.5 (Li et al., 2024a), Qwen-VL (Bai et al., 2023), DeepseekVL (Lu et al., 2024), and InternVL2 (Chen et al., 2023b).
- Authors also experiment on various tasks (RES, gRES, REC, and Open Vocabulary Segmentation), showing that TextSeg acquires strong performance on various grounding tasks. 
- Authors also show that the conversational ability of the LLM does not diminish with the mask prediction finetuning, which is crucial for MLLMs to be useful as its their main capability. 

Clarity
 - The paper explains its method and contribution well in overall. 

Significance
 - The paper provides a new formulation of mask prediction by LLMs to the research area of adapting MLLMs to grounding tasks, which is of significant interest nowadays, and thus contributes to the community.

### Weaknesses
- Although authors stress as a main advantage of their mask formulation as not requiring a segmentation decoder throughout their paper, TextSeg uses SAM to acquire performance comparable to other generalist segmentation models. More precisely, TextSeg *does* require a segmentation decoder but *does not* require finetuning it. Thus, instead of saying that TextSeg is a decoder-free framework, authors should explain that it is a decoder-training-free framework. 
- Since the authors say that SAM is optional, the results without SAM should be included in all the main table results, not just in the ablation study. 

- Addressing the points below would make the paper clearer:
  - Is the row length in R-RLE 16? Then, is Fig. 3 a smaller version with row length 6? The discrepancy between Fig. 3 and the textual explanation is a bit confusing. 
  - Add backbone column to main results table (ie. Table 1~3), so that direct comparison between TextSeg-some-backbone and another method using that backbone is easier to do. 
  - Add references of datasets/benchmarks in tables.
  - Explain what 'mix' under 'Training Data' of LISA means in the caption of Table 4. 
  - References from the end of page 6 to halfway of page 8 seem to be missing. 
  - Explain what training scheme was used for the ablation study: was TextSeg trained on the same combined RES datasets?
  - Typo in "Notably, TextSeg with ViT-L increases the average performance on RES tasks from 70.3 to 75.4 cIoU compared to TextSeg without a mask refiner, with only a little increase in inference time." Should ViT-L be SAM-L? Also, the numbers 70.3 and 75.4 are not in Tab. 6. 
  - Performance of 79.3 cIoU of TextSeg with SAM-H in Table 6 is different from performance of 79.2 cIoU in Table 1.
  - Mark best performances in bold in Table 5 (as done in other tables).

### Questions
- In Figure 6, higher resolution patch prompts to SAM seems to result in worse segmentation results, and this is counter-intuitive as more finegrained the prompt, more finegrained the segmentation should be. Could the authors provide an explanation?

### Soundness
3

### Presentation
3

### Contribution
3
