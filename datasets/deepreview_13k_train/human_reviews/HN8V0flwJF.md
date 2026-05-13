# World Model on Million-Length Video And Language With Blockwise RingAttention

- Decision: Accept
- Scores: 8, 3, 6, 6

## Abstract
Current language models fall short in understanding aspects of the world not easily described in words, and struggle with complex, long-form tasks. Video sequences offer valuable temporal information absent in language and static images, making them attractive for joint modeling with language. Such models could develop a understanding of both human textual knowledge and the physical world, enabling broader AI capabilities for assisting humans. However, learning from millions of tokens of video and language sequences poses challenges due to memory constraints, computational complexity, and limited datasets. To address these challenges, we curate a large dataset of diverse videos and books, utilize the Blockwise RingAttention technique to scalably train on long sequences, and gradually increase context size from 4K to 1M tokens. This paper makes the following contributions: (a) Largest context size neural network: We train one of the largest context size transformers on long video and language sequences, setting new benchmarks in difficult retrieval tasks and long video understanding. (b) Solutions for overcoming vision-language training challenges, including using masked sequence packing for mixing different sequence lengths, loss weighting to balance language and vision, and model-generated QA dataset for long sequence chat. (c) A highly-optimized implementation with RingAttention, Blockwise Transformers, masked sequence packing, and other key features for training on millions-length multimodal sequences. (d) Fully open-sourced a family of 7B parameter models capable of processing long text documents (LWM-Text, LWM-Text-Chat) and videos (LWM, LWM-Chat) of over 1M tokens.
This work paves the way for training on massive datasets of long video and language to develop understanding of both human knowledge and the multimodal world, and broader capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a novel model architecture and training process that achieves significant advancements in long-context modeling for developing large language and vision-language models capable of processing sequences up to 1 million tokens in length. The authors propose a two-stage training process - in the first stage, they progressively train a base language model on increasingly longer text sequences, while in the second stage, the models incorporate vision capabilities through joint training on image and video data. The consequent Large World Model(LWM) family demonstrates impressive performance on a few challenging tasks such as long context retrieval and long video understanding.

### Strengths
1. The paper addresses an important technical challenge in building foundational AI models, which is the long sequence understanding.
2. This work achieves multiple state-of-the-art results across different training stages
3. The open-sourced implementation and pre-trained models benefit and accelerate progress in the research community.

### Weaknesses
The model's suboptimal performance on image and short video understanding tasks and the choice of visual encoding constrain the general applicability of this work.

### Questions
1. When training the models of LWM-1K and LWM-8K, there was an 16% mix of the pure text data added from OpenLLaMA in the batch, how was it determined and how sensitive is the model's performance to this parameter?
2. How did you achieve loss balancing across different tasks and contexts? Any specific strategy?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces the Large World Model (LWM), a LLaMA-based model capable of processing sequences of up to 1 million tokens, combining language and video. The paper details the training datasets, progressive training stages, and evaluation results. It incorporates techniques such as RingAttention, Blockwise Transformers, and others for efficient training on million-length multimodal sequences.

### Strengths
1. The paper provides extensive training details on scaling token sequences to 1M tokens, pushing the boundaries of context length for multimodal models.
2. Empirical results demonstrate strong performance on challenging tasks like long video understanding and retrieval across 1M token contexts.
3. The paper is well-structured and clearly written, with detailed explanations of the model architecture, training process, and evaluation results.

### Weaknesses
1. The title "Large World Model" is misleading. The paper primarily explores training multi-modal (text and video) large language models with long context windows, without adequately defining or discussing the concept of a "large world model" or its relationship to MLLMs.
2. The paper fails to address fundamental questions about the necessity of long-context multi-modal LLMs for large world models and whether such models are sufficient for this purpose.
3. The paper largely describes training datasets and stages, lacking in-depth ablation studies and analysis. It relies heavily on previously proposed components like blockwise RingAttention, making it more akin to an experimental record than a research paper.
4. There is insufficient analysis of the potential synergies or conflicts between text and video in joint training. Do text and video in joint training mutually benefit each other, or do they have a negative influence on one another?
5. The paper lacks comprehensive comparisons with recent multimodal LLM works.
6. Despite claiming contributions in areas like masked sequence packing and loss weighting, the paper lacks ablation studies on those components

### Questions
The core issue is the unclear relationship between the concept of a large world model and the multi-modal LLM with long context window presented in the paper. Additional suggestions include:
1. Provide quantitative evaluations for image and video generation, as mentioned in Section 4.3.3.
2. Explain the larger fluctuations in the purple curve compared to other curves in Fig. 9.
To improve the paper, the authors should:
● Clearly define and discuss the concept of a "large world model" and its relationship to the proposed multi-modal LLM.
● Conduct and present ablation studies to demonstrate the impact of individual components.
● Provide more in-depth analysis of the interaction between text and video modalities during training.
● Include comprehensive comparisons with other recent multimodal LLM works.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a training process that gradually extends LLMs from a limited context length of 4K tokens to an extremely long context of millions of tokens. The two-stage training process — where the first stage focuses on long-context expansion and the second stage addresses image and video understanding and generation — enables the models to support multimodal understanding and generation. The empirically feasible training process, which integrates understanding and generation capabilities into one extensive model using VQ, is quite useful. The evaluations, which involves both linguistic and multimodal tasks, are comprehensive.

### Strengths
- The empirically feasible training process that integrates understanding and generation capabilities into one extensive model using VQ is quite useful, and the evaluations encompassing both linguistic and multimodal tasks are comprehensive.
- The settings and hyperparameters for training and evaluation are presented in a meticulous manner.

### Weaknesses
 - One major contribution of this paper is extending the context length of existing LLMs to extremely long through progressive training, which is a valuable practical implementation. However, aside from the fundamental support of RingAttention, the technical improvements in this study are marginal. The progressive training, while effective, lacks significant novelty beyond the application of known techniques to a new scale.
- Building models that support both multimodal understanding and generation is interesting and meaningful. However, the simple incorporation of an off-the-shelf VQ model into the framework does not yield promising results. The VQ model integration appears to be a straightforward concatenation of existing components, without any novel adaptation or optimization for the long-context setting. I believe that more in-depth analysis and improvements are needed in this direction. The lack of fine-tuning or specific architectural modifications for the VQ model in the context of long sequences is a significant limitation.
- There is a lack of quantitative evaluation for multimodal lengthy content understanding. For example, can we evaluate understanding of image details by increasing resolutions with lengthy vision tokens? Additionally, there are long video understanding benchmarks that could be used to assess the proposed LWM-1M. The absence of such evaluations makes it difficult to assess the true capabilities of the model in handling complex multimodal data over extended contexts. Specifically, the paper does not explore how the model's performance scales with increasing visual token length or resolution, which is crucial for long-context understanding.
- Some crucial details in the main content of the paper, such as the evaluation data and the trainable parameters in each stage, are missing. The lack of clarity regarding the specific datasets used for each task and the exact parameters that are updated during each stage of training makes it difficult to reproduce the results and understand the training process fully.
- Compared to existing and up-to-date VLMs (e.g., LLaVA-NeXT, VILA, Qwen-VL, CogVLM), the performance of LWM on image understanding and video understanding benchmarks is relatively low. The model's performance on standard VLM benchmarks is not competitive, which raises concerns about the overall effectiveness of the proposed approach for multimodal tasks.

### Questions
- For the retrieval task in section 3.3.3, what is the exact evaluation benchmark used for the Multi Needle in a Haystack?
- What are the trainable parameters for each step in the stage 2?

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper scales the LLM context length up to 1M tokens by utilizing Blockwise RingAttention. They progressively increase the context length from 32K to 1M using book-length text data and video-language data. It uses discrete token representation of VQGAN to facilitate image/video generation tasks. It demonstrates competitive performance in long-context retrieval tasks. It also reports comprehensive experimental results in both image/video understanding and generation tasks.

### Strengths
+ This paper is the first to scale sequence models up to 1 million tokens, pushing the boundaries of long-context processing in both language and multimodal (text-video) tasks.
+ The model use VQGAN tokenization to enable image/video understanding as well as generation.
+ In multi-needle retrieval tasks with a 128K context, the model achieves results comparable to or better than GPT-4, demonstrating its effectiveness in long-context retrieval tasks.

### Weaknesses
 + Lack of hour-long video benchmark evaluation, please refer to questions.
+ No comparison with existing open-source LLMs in context length of 128K, for example Llama 3.1
+ The usage of VQGAN decrease the image understanding ability as Table 4 shows.
+ There is no quantitative result on image generation tasks.

### Questions
1. The three benchmarks used to report video performance is not long. It is better to show accuracy on long-video benchmarks such as VideoMME[1] and MLVU[2].
2. In Table 3, how about comparing with existing open-sourced LLM supporting context length of 128K?
3. The paper is the first to scale context length up to 1M. However, there is no baseline comparison in 1M context length. How about using linear scaling technique during inference stage to construct a naive baseline? E.g., scale 8x from a 128k model.

[1] Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis. arXiv preprint arXiv:2405.21075.
[2] MLVU: A Comprehensive Benchmark for Multi-Task Long Video Understanding. arXiv preprint arXiv:2406.04264.

### Soundness
4

### Presentation
3

### Contribution
4
