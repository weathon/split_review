# Mini-Monkey: Alleviating the Semantic Sawtooth Effect for Lightweight MLLMs via Complementary Image Pyramid

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Recently, scaling images to high resolution has received much attention in multimodal large language models (MLLMs). Most existing practices adopt a sliding-window-style cropping strategy to adapt to resolution increase. Such a cropping strategy, however, can easily cut off objects and connected regions, which introduces semantic discontinuity and therefore impedes MLLMs from recognizing small or irregularly shaped objects or text, leading to a phenomenon we call the semantic sawtooth effect. This effect is particularly evident in lightweight MLLMs. To address this issue, we introduce a Complementary Image Pyramid (CIP), a simple, effective, and plug-and-play solution designed to mitigate semantic discontinuity during high-resolution image processing. In particular, CIP dynamically constructs an image pyramid to provide complementary semantic information for the cropping-based MLLMs, enabling them to richly acquire semantics at all levels. Furthermore, we introduce a Scale Compression Mechanism (SCM) to reduce the additional computational overhead by compressing the redundant visual tokens. Our experiments demonstrate that CIP can consistently enhance the performance across diverse architectures (e.g., MiniCPM-V-2, InternVL2, and LLaVA-OneVision), various model capacity (1B$\rightarrow$8B), and different usage configurations (training-free and fine-tuning). Leveraging the proposed CIP and SCM, we introduce a lightweight MLLM, Mini-Monkey, which achieves remarkable performance in both general multimodal understanding and document understanding. On the OCRBench, the 2B-version Mini-Monkey even surpasses the 8B model InternVL2-8B by $12$ score. Additionally, training Mini-Monkey is cheap, requiring only eight RTX $3090$ GPUs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces the "semantic sawtooth effect" caused by common cropping strategies in high-resolution image scaling for MLLMs. To tackle this issue, they propose a Complementary Image Pyramid (CIP), a flexible and easy-to-integrate approach aimed at reducing semantic discontinuity by providing rich semantic information across different scales. Alongside CIP, they also introduce a Scale Compression Mechanism (SCM) to minimize computational overhead by compressing unnecessary visual tokens. These enhancements improve performance across various MLLM architectures and capacities, leading to the development of a lightweight model called Mini-Monkey, which shows notable improvements in multimodal and document understanding tasks.

### Strengths
1. The proposed CIP is logically clear and reasonable. Experiments show that CIP outperforms other cropping methods.
2. The experiments are comprehensive, showing significant improvements across various model families and sizes, as well as multiple datasets, which demonstrates the effectiveness of the proposed CIP.
3. The paper is well-written and clear.

### Weaknesses
1. The insight and inspiration of proposed Adaptive Group is not clear.

2. Lack ablation studies on proposed CIP and SCM

See below for details.



### Questions
1. There is a lack of explanation for the setting of the Adaptive Group. While both detail and global are easy to understand, the paper does not explicitly state the benefits of detail group or provide experimental evidence to support it.
2. The experiments lack ablation studies, such as removing the detail, adaptive, or global components. What would be the impact if one of these were removed? Which component is most critical? Secondly, what impact does the number of tiles in CIP have? How does the performance of CIP change with the number of tiles in the detail component? Also, what aspect ratios are set by default for CIP?
3. The motivation behind SCM does not align well with the experiments. The paper mentions that "certain scenarios may restrict the level of computational resources available," but the experimental part does not provide experiments on how different compression rates of SCM affect model acceleration and computational cost.

If the authors could supplement their experiments, I would be willing to raise the score to above borderline.

### Soundness
3

### Presentation
2

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
This paper proposes Mini-Monkey, a lightweight multimodal large language model that effectively mitigates the semantic sawtooth effect in high-resolution image processing through a Complementary Image Pyramid (CIP) and a Scale Compression Mechanism(SCM), achieving superior performance across various benchmarks.

### Strengths
1、The paper describes CIP for dynamic segmentation of images and SCM for compression of visual tokens to address the semantic sawtooth effect in MLLM high-resolution image processing, demonstrating innovations in addressing specific challenges.
2、In the CIP module, the model focuses on the feature interactions of different sub-images
3、In the SCM module, the model selectively compresses visual tokens. The interaction information of different types of visual tokens is also considered.

### Weaknesses
1、In Figure 2a, the pixel shuffle operation appears, but the paper does not reflect the transformation of the image features before and after this operation. Specifically, it is unclear how the channel dimension changes and what kind of feature re-arrangement occurs during the pixel shuffle. This lack of detail makes it difficult to understand the exact mechanism and its impact on the subsequent processing.
2、According to the formula in line 241, the aspect ratios of the adaptive and detailed groups are not integer multiples. But for Figure 2b, the final selection of Ah is 1 and Dh is 3, which seems to be a contradiction. The paper needs to clarify the relationship between the adaptive and detailed groups in the case where Ah is 1, and how this affects the non-overlapping cropping strategy. The current explanation is insufficient to ensure the reader understands the cropping logic.
3、In the CIP module, the paper does not present a clear picture of how the predefined slice ratios appropriate to the size of the image are selected, i.e., what principle is it based on. It is necessary to provide a more detailed explanation of the selection process, including the specific criteria used to determine the optimal slice ratio for different image aspect ratios. Without this information, it is hard to assess the robustness of the approach.

### Questions
1、I would like to inquire why the paper does not mention the maximum resolution of the images that the model supports, as well as the corresponding comparative experiments.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Existing multimodal large language models (MLLMs) often use cropping when processing high-resolution images (divides the high-res image into multiple lower-resolution as the input). However, Non-Overlapping Cropping can lead to semantic discontinuity and semantic damage, referred to by the authors as the "semantic sawtooth effect." On the other hand, Overlapping Cropping results in redundant visual information.

To address this, the paper proposes a complementary image pyramid, which aims to alleviate the semantic sawtooth effect in the context of Non-Overlapping Cropping. To mitigate the additional computational burden introduced by this module, the authors propose a Scale Compression Mechanism. This mechanism leverages the attention weights of the LLM and the proposed multi-scale image semantics in a training-free and parameter-free manner to compress redundant tokens.

The proposed approach achieves promising results on 8 general multimodal understanding benchmarks and 9 document understanding benchmarks.

### Strengths
1. The use of the complementary image pyramid (CIP) to replace high-resolution input images with sub-images of various scales is an excellent idea. Compared to existing methods that introduce multi-scale visual signals through models, this approach is simpler and more effective, without requiring additional parameters or training.

2. The Scale Compression Mechanism (SCM) reasonably and interestingly reduces the extra computational load brought by multi-scale input sub-images by compressing visual tokens.

3. Both the proposed CIP and SCM do not require the introduction of additional parameters or training, making them applicable to different MLLMs.

4. The method proposed in this paper achieves promising results in various general multimodal understanding and document understanding benchmarks.

### Weaknesses
1. The authors claim in lines 265-266 that "a well-trained LLM from MLLM can effectively select the necessary visual features based on the input question," which seems to differ from the conclusions of existing MLLM works [1,2]. This discrepancy makes me question the effectiveness of the proposed method. If MLLMs cannot truly understand images, how can their attention weights be used here to compress visual tokens? It is unclear how the attention mechanism, which may not be truly grounded in visual understanding, can reliably identify the most salient visual features for compression. This is particularly concerning if the LLM is primarily relying on textual cues to answer questions, rather than genuine visual understanding.

2. The rationale for selecting only the first and second layers of the LLM to choose visual tokens is not sufficiently explained, and no ablation studies have been conducted. How would the results differ if more LLM layers were selected, only one LLM layer was chosen, or the selection was done randomly without using LLM attention priors? In conclusion, ablation studies have only been conducted on the Resolution Strategy, lacking ablation experiments on the compression of visual tokens. The lack of ablation studies on the number of LLM layers used for visual token selection makes it difficult to assess the robustness and generalizability of the proposed approach. Without these experiments, it's hard to determine if the choice of two layers is optimal or simply an arbitrary selection.

3. For the complementary image pyramid, the authors need to manually preset a set of predefined aspect ratios, which seems somewhat tricky. How these aspect ratios are set and why these specific values are chosen remains unclear. A better solution might be to perform K-means clustering on the resolution ratios of images and use the clustering results as the predefined aspect ratios. The manual selection of aspect ratios introduces a potential source of bias and limits the adaptability of the method to different datasets with varying image characteristics. The lack of a systematic approach for determining these ratios is a significant weakness.

4. When comparing with other methods and conducting ablation studies, only the number of parameters and performance are shown, lacking comparisons on FLOPs. Although your proposed multi-scale input does not introduce new parameters, it does increase actual computational load. Therefore, in the ablation studies of Table 4, the actual computational load and inference overhead should also be compared. The absence of FLOPs comparisons makes it difficult to assess the practical efficiency of the proposed method, especially given that the multi-scale input inherently increases computational costs. A thorough evaluation should include both parameter counts and computational complexity.

### Questions
Please refer to the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper focuses on the issue of semantic discontinuity in MLLM when scaling images to high resolution, particularly through a sliding-window cropping strategy that can misidentify small or irregularly shaped objects. To tackle this problem, the paper proposes the Complementary Image Pyramid (CIP), which dynamically constructs an image pyramid to enhance semantic information. Besides, the authors introduce a Scale Compression Mechanism (SCM) to minimize computational overhead by compressing redundant visual tokens. Experimental results show the proposed method achieves the best performance across diverse benchmarks.

### Strengths
1. Mini-Monkey tackles an important problem in MLLM: scaling images to high resolution. The Complementary Image Pyramid (CIP) introduces the pyramid structure, which is an interesting idea. Besides, CIP and SCM are plug-and-play, which can be easily integrated into different MLLMs.
2. The experiments are sufficient.

### Weaknesses
1. Implications of this research. Whether the semantic sawtooth effect mentioned in the paper is a necessary issue to investigate, common Crop-based methods (such as LLaVA-UHD [1] and InternVL [2]) put all cropped regions into a sequence, which does not affect semantic continuity.
2. The work is incremental. The core crop strategy has been widely used in other approaches. CIP is an incremental improvement and doesn't mean much to the community.
3. The architecture is highly sophisticated. The global group is enough to solve the loss of fine-grained features caused by the detailed group. This brings the question of whether the proposed adaptive group is necessary for CIP.
4. The writing needs further improvement. Authors are suggested to improve the readability of the paper. For example, it is hard to understand "For the detailed group, we calculate the aspect ratio of the input image and then compare it with the aspect ratios within the detailed group by calculating the absolute differences." in L231-L233. How to compare? Another example: L270 "We reuse the layer of the LLM as this LLM's Layer". What's the difference between two LLMs?
5. Incomplete experimental analysis. Experimental analysis should include analysis of reasons and not just a list of indicators.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
