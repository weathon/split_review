# NExT-GPT: Any-to-Any Multimodal LLM

- Decision: Reject
- Scores: 6, 5, 5, 8

## Abstract
While recently Multimodal Large Language Models (MM-LLMs) have made exciting strides, they mostly fall prey to the limitation of only input-side multimodal understanding, without the ability to produce content in multiple modalities. 
As we humans always perceive the world and communicate with people through various modalities, developing any-to-any MM-LLMs capable of accepting and delivering content in any modality becomes essential to human-level AI.
To fill the gap, we present an end-to-end general-purpose any-to-any MM-LLM system, \textbf{NExT-GPT}.
We connect an LLM with multimodal adaptors and different diffusion decoders, enabling NExT-GPT to perceive inputs and generate outputs in arbitrary combinations of text, image, video, and audio. 
By leveraging the existing well-trained high-performing encoders and decoders, NExT-GPT is tuned with only a small amount of parameter (1\%) of certain projection layers, which not only benefits low-cost training but also facilitates convenient expansion to more potential modalities.
Moreover, we introduce a modality-switching instruction tuning (MosIT) and manually curate a high-quality dataset for MosIT, based on which NExT-GPT is empowered with complex cross-modal semantic understanding and content generation.
Overall, our research showcases the promising possibility of building a unified AI agent capable of modeling universal modalities, paving the way for more human-like AI research in the community. 
Project website: \url{https://next-gpt.io/}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a multi-modal LLM, called any-to-any MM-LLM, to extend the multi-modality of LLM to a state where there is no limitation on the input and output modality combinations. To achieve this goal, the authors (1) propose a lightweight alignment learning technique to achieve en effective semantic alignment across different modalities with limited trainable parameters and (2) annotate a modality-switching instruction tuning dataset. The displayed results and visualizations suggest the promising performance of the tuned any-to-any MM-LLM.

### Strengths
- Extending the multi-modal LLMs free of limitation on the input/output modalities is an important research question that can facilitate a wider range of applications. 
- The introduced dataset, if made publically available, would be a good contribution to the community.
- Various evaluation benchmarks are used to benchmark the proposed model with existing solutions. 
- The writing is clean and easy to follow

### Weaknesses
 - The proposed alignment learning technique is a bit naive and does not consider much about the challenge introduced by the any-to-any modality, such as how to balance the performance across different modalities. 
- Although introducing contents from different modalities during tuning is considered to improve the overall performance of the model, in the experiment section, it seems introducing these additional modalities actually leads to worse performance on benchmarking datasets. Does this indicate the alignment technique is not effective enough as expected?

### Questions
Will the pretrained model and dataset be released to the public?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces NExT-GPT, an end-to-end, multi-purpose, multi-modal Language Learning Model (MM-LLM) capable of generating text, images, audio, and video. The system is designed to be efficient, utilizing a small quantity of parameters. Furthermore, a multimodal instruction dataset named MosIT is presented, which facilitates cross-modal understanding and content generation.

### Strengths
1. The system architecture is compact and includes multiple decoders for text, video, audio, and image generation, making it straightforward to implement.
2. The generation process is end-to-end and does not require initial text generation.

### Weaknesses
1. The quality of the generation output is primarily dependent on the pre-trained generation modules. If these modules are flawed or produce errors, the system cannot rectify these issues. For instance, if in image generation, stable diffusion struggles with accurately rendering certain elements (e.g., the number of human fingers), NExT-GPT would not be able to produce an accurate output, irrespective of its understanding of the instruction. This reliance on pre-trained models introduces a significant limitation, as the system's performance is capped by the capabilities of these external components. The lack of an internal mechanism to correct or refine outputs from these modules means that any inherent biases or limitations in the pre-trained models will directly propagate to the final output of NExT-GPT.
2. The evaluation strategy appears questionable. It seems that the NExT-GPT model used in the evaluation was fine-tuned on individual datasets, which may not accurately reflect the effectiveness of the proposed method. This fine-tuning on specific datasets raises concerns about the generalizability of the results. The reported performance might be inflated due to overfitting to the evaluation datasets, and it remains unclear how the model would perform on unseen data or tasks. The lack of a unified evaluation protocol across all tasks makes it difficult to assess the true capabilities of the proposed method.
3. What would be the results if the model was trained on a mixture of the proposed MosIT dataset and benchmark datasets, and then evaluated on the benchmarks? Additionally, in a multimodal language model, text generation is crucial. It would be interesting to know how the system performs on recent benchmarks such as MME [1], MMBench [2], and SEEDBench [3].
4. The qualitative comparison provided lacks thoroughness. The paper only presents a few demonstrations and fails to provide comparisons with other MLLMs, including InstructBLIP [4], LLaVA [5], mPLUG-Owl [6] for text generation, and DreamLLM [7] and EMU [8] for conditioned image generation. The absence of a comprehensive qualitative analysis makes it difficult to assess the practical performance of the model. The lack of comparisons with existing state-of-the-art models further limits the ability to contextualize the contributions of the proposed method.

### Questions
see weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a unified framework that enables any-to-any generation. Specifically, it receives inputs from multiple modalities, such as text, audio and video. Furthermore, it leverages off-the-shelf LLMs and diffusion models, which enables efficient training. They propose to leverage special tokens that encodes the semantics, and then feed this to the diffusion model to act as the conditional input. The paper shows promising results on the evaluated benchmarks.

### Strengths
This paper proposes a novel approach to enable any-to-any generation by integrating off-the-shelf diffusion models with LLMs. The proposed approach to align the semantic tokens with outputs from text encoders of diffusion models seems efficient. The results look promising.

### Weaknesses
The major concern I have regarding this paper is the training object during alignment, which is to align the semantic tokens with outputs from text encoders of diffusion models. This seems reasonable at first, but if the objective is to "match the semantics token with textual captions' representations from the text encoders of diffusion models", why not just directly use the diffusion model's text encoder to encode the textual captions? More specifically, why not just let the LLM output a caption according to some fixed format, and extract the caption, then feed it to the diffusion model for generation? I think it would be a more direct approach and probably will enable better performance. Unfortunately, I do not find comparison with this simple alternative in the paper.

### Questions
Please see weakness.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed an end-to-end general-purpose any-to-any MM-LLM system, NExT-GPT, by connecting an LLM with multimodal adaptors and different diffusion decoders.

### Strengths
(1) The paper formulation is good and clear.  
(2) Introduced lightweight alignment learning techniques.  
(3) Annotated a high-quality modality-switching instruction tuning dataset.

### Weaknesses
(1) The model relies on different pretrained models to understand different types of information, like text, images, and audio. The quality of pretraining may directly impact how well the model performs its tasks.  
(2) What is the size of parameters when tuning the model for each modality?

### Questions
(1) Please see the comments above.  
(2) The work in [1] may be related, can the authors provide a comparison? (not included in rating) 

[1] Moon, S., Madotto, A., Lin, Z., Nagarajan, T., Smith, M., Jain, S., Yeh, C., Murugesan, P., Heidari, P., Liu, Y., Srinet, K., Damavandi, B., & Kumar, A. (2023). AnyMAL: An Efficient and Scalable Any-Modality Augmented Language Model. ArXiv, abs/2309.16058.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
