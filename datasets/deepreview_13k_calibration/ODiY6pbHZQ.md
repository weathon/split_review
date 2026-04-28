# Oryx MLLM: On-Demand Spatial-Temporal Understanding at Arbitrary Resolution

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Visual data comes in various forms, ranging from small icons of just a few pixels to long videos spanning hours. Existing multi-modal LLMs usually standardize these diverse visual inputs to fixed-resolution images or patches for visual encoders and yield similar numbers of tokens for LLMs. This approach is non-optimal for multimodal understanding and inefficient for processing inputs with long and short visual contents. To solve the problem, we propose Oryx, a unified multimodal architecture for the spatial-temporal understanding of images, videos, and multi-view 3D scenes. Oryx offers an on-demand solution to seamlessly and efficiently process visual inputs with arbitrary spatial sizes and temporal lengths through two core innovations: 1) a pre-trained OryxViT model that can encode images at any resolution into LLM-friendly visual representations; 2) a dynamic compressor module that supports 1x to 16x compression on visual tokens by request. These designs enable Oryx to accommodate extremely long visual contexts, such as videos, with lower resolution and high compression while maintaining high recognition precision for tasks like document understanding with native resolution and no compression. Beyond the architectural improvements, enhanced data curation and specialized training on long-context retrieval and spatial-aware data help Oryx achieve strong capabilities in image, video, and 3D multimodal understanding simultaneously.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Oryx MLLM paper proposes unified solution to process images, spatio-temporal videos and multi-view 3D input. It introduces a dynamic compressor module that performs token compression and adaptive positional embedding enables native resolution input / video length.

### Strengths
- The one-fit all solution that unifies solution to video of any length and image of varying resolution, 3D input makes is a significant contribution in it's usability especially in real world deployment. 
-The code/ training details have been elaborated and released which enables reproducibility and usage.
- Exhaustive benchmarks provided for the long video understanding and the 3D correspondance understanding.

### Weaknesses
 - The effect of ORyxViT and the compressor module on the inference throughput needs to be provided.
- Need clarity on what is short and long video to decide the downsample layers: Line 223
- It would be great to see apple-apple comparison of SOTA VLM/ Video-LLM outputs for the qualitative examples that were added.

### Questions
- Covered above in weakness.

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
This paper introduces Oryx, a unified multimodal large language model (MLLM) designed for comprehensive spatial-temporal understanding across diverse visual inputs, including images, videos, and multi-view 3D scenes. 

Key innovations include the OryxViT encoder, which processes inputs with variable aspect ratios and resolutions, and a dynamic compressor that supports on-demand compression ratios from 1x to 16x based on task requirements. It allows the model to handle extended temporal lengths while maintaining performance.

The paper also highlights enhanced data curation and specialized training strategies that bolster Oryx’s capabilities in image, video, and 3D multimodal understanding. Comprehensive evaluations across multiple benchmarks demonstrate Oryx’s competitive performance, often surpassing larger models in specific tasks.

### Strengths
1. **Innovative Architecture**:   
The paper introduce OryxViT and the Dynamic Compressor to handle various visual inputs with arbitrary resolutions and temporal lengths, which address a critical limitation in current MLLMs.

2. **Support for Native Resolution**:   
The OryxViT encoder preserves the integrity of visual content by processing inputs at their original resolution, which is essential for detailed tasks.

3. **Efficiency and Scalability**:   
By supporting on-demand compression, Oryx can effectively manages computational resources. It’s suitable for processing both high-resolution images and long-duration videos without compromising performance.

4. **Comprehensive Evaluation**:   
The model is extensively tested across a wide range of benchmarks, including NextQA, Perception Test, MMBench-Video, and ScanQA. Demonstrate its robust performance and state-of-the-art results among open-source models.

5. **Advanced Training Strategies**:   
The paper also introduce an effective data curation and training pipelines, including long-form temporal training and spatial-aware knowledge acquisition through coarse correspondences to boost MLLM training.

### Weaknesses
 1. **Writing Issues**:
    - **Lack of Focus:** The first part of the paper mainly focus on addressing the varying resolutions of visual inputs, while the second part shifts to enhanced data curation for supporting different modalities (e.g. 3D scene understanding) in MLLMs, which create a sense of discontinuity. The transition between the architectural innovations and the data curation strategies is abrupt, making it difficult to see how these two components work together to achieve the stated goal of a unified MLLM. The paper would benefit from a clearer articulation of how the specific data curation methods are designed to complement the proposed architectural changes, especially in the context of 3D understanding. 
    - **Excessive Technical Detail**: While the technical innovations are commendable, the method part contains too much technical details that can disrupt the flow and make it difficult to read. The paper delves into the specifics of the OryxViT encoder and dynamic compressor without first providing a high-level overview of how these components fit into the overall architecture. This makes it challenging for the reader to grasp the significance of each technical detail and how it contributes to the model's performance.
2. **Ambiguity in Performance Gain:**
    - It also remains unknown whether the observed performance improvements on Long-form temporal/3D understanding mainly come from the model design or from the introduction of the new long-form videos dataset and the Coarse Correspondences dataset. A more detailed analysis is required. The paper lacks a thorough ablation study to isolate the impact of the architectural changes from the data enhancements. It is unclear how much of the performance gain is attributable to the OryxViT encoder and dynamic compressor versus the new datasets. A more granular analysis is needed to determine the individual contributions of each component.
3. **More experiment to justify design choice:**
    - There are too many manual design choices within this paper that haven’t been justified by exp.
        
        1. A more detailed analysis of the computational complexity of the Variable-Length Self-Attention approach compared to traditional methods would be helpful. How does the memory footprint scale with varying sequence lengths, and what optimization strategies are in place to handle potential memory bottlenecks? The paper does not provide a clear comparison of the computational cost of the proposed variable-length self-attention mechanism with standard self-attention. It is essential to understand how the memory footprint scales with increasing sequence lengths and what optimization techniques are used to mitigate potential memory bottlenecks. Without this analysis, it is difficult to assess the practicality of the approach for long-form video processing.
        
        2. How does the significant reduction in token length for long videos (downsampling by a factor of 16) affect the model's ability to capture fine-grained visual details essential for understanding complex scenes or actions? Why downsample (1x, 4x, 16x) is a reasonable choice? How would other downsample strategy affect performance? The paper lacks a detailed analysis of the impact of the downsampling strategy on the model's ability to capture fine-grained visual details. The choice of downsampling factors (1x, 4x, 16x) is not sufficiently justified, and there is no discussion of how different downsampling rates affect the model's performance on tasks requiring detailed visual understanding. The paper should explore alternative downsampling strategies and provide empirical evidence to support the chosen approach.
        
        3. Does using a shared MLP for projecting features from different downsampling ratios adequately capture the unique characteristics of images, short videos, and long videos, or could specialized expert projection layers yield better performance? The paper does not explore the possibility of using specialized projection layers for different modalities. It is unclear whether a shared MLP can effectively capture the unique characteristics of images, short videos, and long videos. The paper should investigate whether specialized expert projection layers could improve performance by better capturing the specific features of each modality.
4. **Failure cases analysis**
    - Including analysis of failure cases would be appreciated. This analysis could provide valuable insights into the limitations of the Oryx model and offer transparency on how it performs under various challenging scenarios.

### Questions
Given the current weaknesses of this paper, I am unable to provide a positive score. However, addressing the issues above could prompt me to reconsider the rating.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a series of improvement on the vision encoder design for multi-modal large language models, enabling better understanding of images, videos, and 3D multi-view inputs. The core contribution is a ViT-based vision encoder that supports native resolution inputs, accommodating varying resolutions and aspect ratios. Additionally, the authors introduce a dynamic compression technique with a cross-attention design to reduce the information loss caused by the pooling operations. The results demonstrate the model's effectiveness across video, 3D, and image understanding tasks.

### Strengths
1. This paper implements and open-sources a powerful ViT-based encoder that supports native input resolution. This can benefits the community since it offers a more flexible and effective alternative to dynamic partitioning or fixed resolution approaches.
2. The reported results are very promising, especially on tasks requires high-resolution details or long context understanding.

### Weaknesses
1. The main concern is the lack of detailed implementation regarding the pretraining of the Oyrx ViT. It would be valuable to understand whether the Oyrx ViT remains effective without pretraining—for instance, by modifying the ViT architecture as Oyrx ViT and directly fine-tuning it on multi-modal conversation data. Additionally, more specifics about the pretraining process, such as the dataset size, batch size, and training objectives, should be provided.
2. The cross-attention downsampling module is similar to prior work [1]. The authors should discuss how their approach differs from the cross-attention architecture proposed by mini-Gemini[1].  It seems that the only apparent difference is that mini-Gemini uses a CLIP encoder for low-resolution features.

### Questions
1. What is the performance of Oyrx ViT without pretraining? If pretraining is essential, could the authors provide details on the amount of data used and the specific task mixture involved in the pretraining process?
2. In section 3.1.3, how to utilize the correspondence information provided by TrackingAnything?

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
The primary goal of this work is to address the limitations of current multi-modal LLMs in processing visual inputs of varying lengths. To tackle this issue, the paper proposes two key improvements based on existing architectures: First, it enhances the current visual encoder to accept arbitrary inputs by enlarging and rescaling the positional encoding. Second, it implements input downsampling based on the type of visual input, supplemented by additional attention mechanisms to compensate for information loss. To ensure broader applicability, this work also carefully curates diverse datasets to enhance the model's capabilities. The results demonstrate that the proposed approach shows significant advantages over similarly sized models across various benchmarks.

### Strengths
1. The writing is clear, engaging, and easy to understand.
2. The two proposed improvements to the existing architecture are concise, straightforward, and easily implementable.
3. The approach further enhances the performance ceiling of similarly sized models across various benchmarks, contributing positively to the advancement of the community.

### Weaknesses
1. The title and introduction seems somewhat overclaiming. Initially, I interpreted "ON-DEMAND" in the title as implying a dynamic adjustment of spatiotemporal compression based on input; however, the method only implements fixed downsampling based on input type, which was disappointing after reviewing the methodology.
2. The proposed improvements appear somewhat rudimentary. Both the adjustments to positional encoding and the downsampling with attention seem like baseline approaches, lacking deep exploration or inspiration for future work. While I appreciate the complexity of the experiments and the contributions to the community, there are notable deficiencies in novelty.
3. There is a lack of comparison regarding processing times for different methods when handling long videos or mixed data. Although the paper emphasizes the method's efficacy for compressing long videos, I did not find any specific comparisons regarding processing times.

### Questions
A discussion and comparison of existing methods for compressing visual signals would significantly enhance the paper.

### Soundness
2

### Presentation
3

### Contribution
2
