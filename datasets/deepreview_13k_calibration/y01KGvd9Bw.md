# DreamLLM: Synergistic Multimodal Comprehension and Creation

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
This paper presents \dreamllm, a learning framework that 
first achieves versatile Multimodal Large Language Models (MLLMs) empowered with frequently overlooked synergy between multimodal comprehension and creation.
\dreamllm operates on two fundamental principles.
The first focuses on the generative modeling of both language and image posteriors by direct sampling in the raw multimodal space. 
This approach circumvents the limitations and information loss inherent to external feature extractors like CLIP, and a more thorough multimodal understanding is obtained.
Second, \dreamllm fosters the generation of raw, interleaved documents, modeling both text and image contents, along with unstructured layouts.
This allows \dreamllm to learn all conditional, marginal, and joint multimodal distributions effectively.
As a result, \dreamllm is the first MLLM capable of generating free-form interleaved content.
Comprehensive experiments highlight \dreamllm's superior performance as a zero-shot multimodal generalist, reaping from the enhanced learning synergy. Project page: \href{https://dreamllm.io}{\texttt{dreamllm.io}}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces "DREAM LLM", a novel learning framework designed to enhance Multimodal Large Language Models (MLLMs). The model is designed to 1) The model late-fused three pretrained models, a text-LLM, an image generation model (SD), a CLIP model. Unlike conventional methods that utilize intermediate image representations, DREAM LLM leverages score distillation techniques with a diffusion image generation model inputs raw data modalities and outputs them in the same format. 2) The model is also trained on interleaved multimodal corpora sourced from the internet. 
This leads to superior performance in several benchmarks and the ability to generate free-form interleaved content.

### Strengths
1. The model late-fused three pretrained models, a text-LLM, an image generation model (SD), a CLIP model. With the designed dream query and score distillation with SD model, the model is superior than earlier models that utilize intermediate image representation. 
2. What's more, the model is trained on carefully collected various datasets, including, various text-image datasets, interleaved multimodal corpora sourced from the internet, instruction datasets. With joint-training, it also shows synergy of text and image, understanding and creation. 
3. The model shows very comprehensive experiment results in various benchmarks like MS-COCO, MMBench, and MM-Vet, in different setup zero-shot understanding, image generation, interleaved generation, etc.

### Weaknesses
1. The model is trained on very rich data, and it is not clear how does those data contribute to the zero-shot evaluation.

a. several dataset used by the model are derived from COCO datasets, e.g Laion-COCO, LLaVaInstruct, etc. How do we know if there is data leakage in the training datasets. This applies to the results in table 1, as well as in table2. Specifically, the use of Laion-COCO, which is constructed using BLIP captions on LAION images, raises concerns about potential bias towards COCO-style descriptions, which could inflate performance on COCO-related benchmarks. Furthermore, the LLaVAInstruct dataset, derived from COCO, introduces a potential for data leakage, especially if the instruction-tuning data overlaps with the evaluation sets. This is a significant concern because it could lead to an overestimation of the model's generalization capabilities.

b. Is the model in table 1 after instruction tuning?

c. if you continue training SDv2.1 with the collected dataset, what are the MS-COCO, and LN-COCO FID number? It is important to understand how much of the improvement comes from the specific architecture and training method versus simply fine-tuning a strong diffusion model on a large dataset.

2. Some model details are not clear.

a. how is the multi token dream query implemented. For decoder-only transformer training, every token needs a loss (or a score). What us the loss of each query token during training, and are they generated sequentially or altogether during inference? The exact mechanism by which the multi-token dream query interacts with the diffusion model and the language model needs clarification. Specifically, it's unclear how the gradients are backpropagated through the dream query to update the parameters of both the diffusion model and the language model.

b. in the interleaved multimodal joint training, for the second/third image generation, do they condition on both the image1 dream query and image1 visual encoder? Or just image1 visual encoder. The conditioning mechanism for subsequent image generations in interleaved multimodal training needs to be specified. Does it use the dream query of previous images, or only the visual encoder outputs? This is crucial for understanding the model's ability to maintain context across multiple modalities.

c. for the stage1, stage2, stage3, what's the final loss? Do they both have L_DM (formula 5) and L_MLLM (formula 6)? Is there a weight? The loss function used in each training stage needs to be clearly defined. Specifically, it's unclear whether both the diffusion loss and the language modeling loss are used in each stage, and if so, how they are weighted.

d. for the I-GPT training, does the visual projector, condition projector, dream embedding get updated? or only the MLLM transformer got updated? The specific components updated during I-GPT training require clarification. It is unclear whether the visual projector, condition projector, and dream embeddings are jointly trained or if only the MLLM transformer is updated.

e. in section 5.1, the L_CLIP is not clear. Which two embeddings are used to calculate the loss? The CLIP loss calculation needs to be clarified, specifically which embeddings are used to compute the loss, and how this loss is used during training.

### Questions
1. Can the model do k-shot learning for image understanding task?
2. table4 shows amazing results that the model is better at text task than the pretrained text LLM, does the author have any hypothesis why?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a framework to allow multimodal large language models combining multimodal comprehension and generation. To enable image generation, instead of fitting CLIP feature, this work directly optimizes the diffusion model's objective to achieve modeling multimodal posteriors. The training pipeline is comprised of three stages: alignment pretraining, interleaved generative pretraining, and supervised finetuning. Extensive experiments on multimodal comprehension and creation have shown the superiority of the proposed model.

### Strengths
1. This model proposed a unified framework for joint multimodal comprehension and generation which shows impressive performance on various tasks, demonstrating the benefits of synergizing these two tasks.
2. The usage of score distillation avoids the possible information loss to greatly improve the image generation ability.
3. The proposed training pipeline enables the free-form interleaved generative ability of multimodal models.
4. The experiments are comprehensive and convincing.

### Weaknesses
1. For free-form interleaved generation, it is important to ensure the consistency between related images. However, as we can view the model as replacing the CLIP text encoder of stable diffusion with a much more powerful LLM for the image generation aspect, the control of the generated image is still limited. As we can see from the Figure 3, the phones in generated samples have large discrepancy. Specifically, while the overall scene might align with the text prompts, the fine-grained details, such as the specific model or style of the phones, vary significantly across different generated images that are supposed to depict the same object, indicating a lack of precise control over object attributes during interleaved generation.
2. The paper does not demonstrate the in-context comprehension ability of the model. This is a critical aspect for evaluating the model's ability to generalize to new tasks or scenarios without explicit fine-tuning. The absence of in-context learning experiments leaves a gap in understanding the model's adaptability and potential for broader applications.
3. Ablation studies on the choices, combination ways, and the importance of filtering process of the training datasets are not shown, which might provide insights for future study. The lack of ablation studies makes it difficult to understand the contribution of each component of the training pipeline. For example, it's not clear how different data sources, or different filtering strategies, impact the model's overall performance. Without such analysis, it's hard to determine the optimal training setup or identify potential bottlenecks.

### Questions
Will including samples from training datasets as in-context examples improve the performance during evaluation?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a framework that unifies generation of text and images. Specifically, it utilizes a newly introduced <dream> token to encode the representations that will later be forwarded to the diffusion model to decode to images. The authors have conducted extensive experiments across multiple tasks and benchmarks to showcase the ability of the proposed method.

### Strengths
The paper proposes a unified and promising framework for multimodal generation, strong performances are reported. The proposed approach to integrate diffusion models with LLM seems reasonable and could inspire following works in this area.

### Weaknesses
The major concern I have is the necessity to utilize the <dream> token from LLM for image decoding. What is is going to be if you let the LLM to first output the image description, then extract it and feed it directly to the diffusion model? In this case, the original text encoder of diffusion models are leveraged. The results in Table 2 show that the specialists still outperform dreamLLM, which means the above naive alternative could potentially perform better? In addition, is it possible that directly use output text can also alleviate the loss of LLM's original power?

### Questions
See weakness .

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
