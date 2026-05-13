# Prompt-Aware Adapter: Towards Learning Adaptive Visual Tokens for Multimodal Large Language Models

- Decision: Reject
- Scores: 6, 3, 5, 5

## Abstract
To bridge the gap between vision and language modalities, Multimodal Large Language Models (MLLMs) usually learn an adapter that converts visual inputs to understandable tokens for Large Language Models (LLMs). 
However, most adapters generate consistent visual tokens, regardless of the specific objects of interest mentioned in the prompt. 
Since these adapters distribute equal attention to every detail in the image and focus on the entire scene, they may increase the cognitive load for LLMs, particularly when processing complex scenes. 
To alleviate this problem, we propose prompt-aware adapters. 
These adapters are designed with the capability to dynamically embed visual inputs based on the specific focus of the prompt.
Specifically, prompt-aware adapters utilize both global and local textual features to capture the most relevant visual clues from the prompt at both coarse and fine granularity levels.
This approach significantly enhances the ability of LLMs to understand and interpret visual content. 
Experiments on various visual question answering tasks, such as counting and position reasoning, demonstrate the effectiveness of prompt-aware adapters.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies the impact of prompts on adapters, revealing that prompt-independent adapters still have deficiencies in visual understanding. To this end, this paper proposes a new adapter that dynamically injects visual input into LLM through prompts. The proposed global attention mechanism and local attention mechanism can utilize the overall content or local content of textual information for visual guidance at different granularities. The experiments are conducted on a large number of complex scene understanding datasets.

### Strengths
- The experiments are sufficient and demonstrate that the proposed method performs well across multiple visual perception and cognitive tasks, indicating good generalizability suitable for a wide range of applications. 
- The paper is well-written with a clear structure, making it easy to follow.
- The proposed new adapter and dual attention mechanism appears to be an innovative approach to processing visual inputs.

### Weaknesses
- The motivation of dual attention is not clear. The visual clues can be captured by cross-attention at token level from prompt. Why do we need to split it into global attention and local attention? And the visual clues are typically given at a word/token level. Why do we need a global attention?
- The differences in the metrics in the "Calculate" column of Table 3 are quite substantial and require further explanation. The Q-Former∗ + Linear model achieves a score of 78.07, while the proposed method only scores 50.
- There are two bolded numbers in the "Position" column of Table 3. Please correct this issue.
- The results in Table 1 indicate that the proposed method performs poorly on the color recognition task (99.99 vs. 165.00). What factors might contribute to this discrepancy? Could you provide an appropriate analysis or evidence to support this observation?

### Questions
Please refer to Weaknesses.

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
4

### Summary
This paper proposes a text-guided feature transformation for the vision encoder. Similar to InstructBLIP, it enhances the correlation between visual representations and text instructions by introducing a global text token and a local attention mechanism.

### Strengths
1.	The paper is well-written, logically structured, and easy to follow.
2.	The motivation and the proposed prompt-aware global and local attention are generally reasonable.
3.	The ablation studies are extensive, and the selection of comparison methods is appropriate.

### Weaknesses
1.	The major weakness is the lack of novelty. Multimodal fusion for vision encoders has already been extensively explored and validated. Compared to VisionLLM and InstructBLIP, the proposed prompt-aware global and local attention is merely a combination of existing techniques, offering minimal contribution.
2.	The experimental comparison in Table 1 is not fair. This paper uses LLaMA2-7B as the large language model, while its main counterparts, such as InstructBLIP, use the weaker Vicuna-7B model. Since the choice of vision encoder and LLM directly impacts multimodal performance, the performance improvements in the experiments can not reflect the advantages of the proposed method.
3.	As shown in Eq. 5, compared to cross-attention, the proposed prompt-aware local attention uses global softmax to create a single association between text tokens and vision tokens. This implicitly assumes that each text token will have a high correlation with only one visual token. However, this assumption does not hold in many cases, especially when visual patches are densely divided.

### Questions
Please refer to the Weaknesses section.

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
4

### Summary
The paper proposed a prompt-aware adapter method that matches both global and local texture features in the prompt to the relevant image contents. Therefore, the adapter can adaptively inject the visual tokens to the semantic space of an LLM according to individual textual prompts. Specifically, the proposed method extracts the CLIP features of the entire prompt which are mapped and appended to the visual features extracted by ViT. Next, the similarity matrix between individual words in the prompt and the features of all visual patches is calculated to derive the weights of the visual patches. The proposed method has been evaluated on COCO-QA and MME datasets and outperforms some recent methods noticeably.

### Strengths
The paper proposes a simple and effective way to improve the adapter between a visual encoder and an LLM. The mapping of CLIP features of a prompt to visual features and the adaptive weights of visual patches w.r.t. individual words in the prompt are easy to reproduce.

The experiments show that the proposed method is effective to improve the VQA task on COCO-QA and MME datasets.

### Weaknesses
The contributions of this work may not be as significant as the paper claimed.

First of all, given the recent efforts on the native multi-modal foundation model, such as EMU3, the adapter approach may be a temporary solution for MLLM. 

The motivation to come up different ways to inject visual tokens to an LLM according to different prompts may not be that strong. The fundamental way to improve VQA shall be on how to generate detailed and accurate description and representation of image. Using the case in Fig.1 as an example, if MLLM can describe the image as “Along the pool in the backyard of a house, there is a table with 5 drinks on it and 4 chairs”, surely an LLM can conduct VQA and answer “Is there a pool in this image?” and “How may drinks are on the table?” without an adaptive adapter. Please send this photo to OpenAI o1 and check if it can generate a detailed description of the image. So it is arguable that do we really need to change the way to encode visual patches according to each textual prompt.  

The technical contributions are a bit thin which are from line 253 to line 284 and Fig.3, while, most of the paper discusses the background and difference to previous works. The length of the paper could be trimmed, e.g., like Fig.1, the specific image is not informative, perhaps only keeping the same color tokens and different color tokens is enough. 

The experiments verified the proposed schemes are useful to the VQA tasks on two datasets. What about its performance on more complicated tasks such as multi-round conversation w.r.t. images or video understanding.

Regarding to the writing, the paper tends to use some generic and vague expressions, like “understands information”, “to extract the most informative clues”. Btw: if your goal “aims to extract the most informative visual clues”, it does not mean you did “extract the most informative visual clues”, you still need to justify why you achieve this, in what sense it is “informative” (which is a very vague term), in what sense it is the “most” informative, etc.

### Questions
Please discuss given the recent progress of Open o1/4o and Gemini which can describe the image contents in details, why it is important to use different way to transform the visual tokens in the adapter. 

Please discuss how to extend the proposed method to more complicated multi-modal recognition tasks.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces a novel approach to enhance the visual understanding capabilities of Multimodal Large Language Models (MLLMs). The authors propose a prompt-aware adapter that dynamically embeds visual inputs based on the specific focus of the textual prompt. This adapter utilizes both global and local textual features to capture relevant visual cues at different granularity levels, reducing the cognitive load on the Large Language Model (LLM) and improving its ability to interpret visual content. The method is evaluated on various visual question answering tasks, including counting and positional reasoning, demonstrating significant improvements over prompt-unaware baselines.

### Strengths
1. The paper introduces a prompt-aware adapter that adapts visual inputs based on the textual prompt, which is a novel approach compared to traditional, prompt-unaware adapters.
2.  By focusing on the specific visual elements mentioned in the prompt, the proposed adapter reduces the cognitive load on the LLM, leading to more efficient and accurate processing of visual information.

### Weaknesses
1.  The paper presents a method for enhancing visual understanding in MLLMs by focusing on visual details relevant to the textual prompt. While the concept of improving model performance through prompt-related visual cues is not entirely new, with prior works like API[1], AGLA[2], MAVEN[3], and ConrtolMLLM[4] exploring similar ideas. Despite some innovation in the design, the contributions do not seem to offer substantial new value or advancements in the field.
2. There is an inconsistency in the choice of baseline models. Line 353 mentions initializing parameters with MiniGPT-V2, yet Tables 2 and 3 use MiniGPT-4 as the baseline. 
3. Ablation studies, particularly those involving parameter tuning (as shown in Table 7), should ideally be conducted on a validation set to ensure the generalizability of the findings. Although most researchers have currently overlooked this point.
4. Since Table 1 compares earlier models that utilize different visual encoders and language decoders, it would be beneficial to include comparisons with the latest methods that are not contemporaneous, such as LLaVA-Next. Additionally, it would be insightful to see if the authors' proposed method could be applied to other state-of-the-art models like LLaVA-Next or others.
5. It would be valuable to see comparisons with models that possess referring and grounding capabilities, such as Qwen-VL[5], Ferret[6], and ViP-LLaVA[7].
6. Figure 1 could be further refined to make it more concise and intuitive. Improving the figure to be more straightforward would enhance the reader's understanding of the concepts presented in the paper.

[1] Attention Prompting on Image for Large Vision-Language Models.

[2] AGLA: Mitigating Object Hallucinations in Large Vision-Language Models with Assembly of Global and Local Attention.

[3] MaVEn: An Effective Multi-granularity Hybrid Visual Encoding Framework for Multimodal Large Language Model.

[4] ControlMLLM: Training-Free Visual Prompt Learning for Multimodal Large Language Models.

[5] Qwen-vl: A frontier large vision-language model with versatile abilities.

[6] Ferret: Refer and Ground Anything Anywhere at Any Granularity.

[7] ViP-LLaVA: Making Large Multimodal Models Understand Arbitrary Visual Prompts.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
