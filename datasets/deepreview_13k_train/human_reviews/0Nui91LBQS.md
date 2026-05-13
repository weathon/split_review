# Making LLaMA SEE and Draw with SEED Tokenizer

- Decision: Accept
- Scores: 5, 6, 8

## Abstract
\vspace{-5pt}
The great success of Large Language Models (LLMs) has expanded the potential of multimodality, contributing to the gradual evolution of General Artificial Intelligence (AGI). A true AGI agent should not only possess the capability to perform predefined multi-tasks but also exhibit emergent abilities in an open-world context. However, despite the considerable advancements made by recent multimodal LLMs, they still fall short in effectively unifying comprehension and generation tasks, let alone open-world emergent abilities. We contend that the key to overcoming the present impasse lies in enabling text and images to be represented and processed interchangeably within a unified autoregressive Transformer. To this end, we introduce \textbf{SEED}, an elaborate image tokenizer that empowers LLMs with the ability to \textbf{SEE} and \textbf{D}raw at the same time. We identify two crucial design principles:
(1) Image tokens should be independent of 2D physical patch positions and instead be produced with a \textit{1D causal dependency}, exhibiting intrinsic interdependence that aligns with the left-to-right autoregressive prediction mechanism in LLMs. (2) Image tokens should capture \textit{high-level semantics} consistent with the degree of semantic abstraction in words, and be optimized for both discriminativeness and reconstruction during the tokenizer training phase. With SEED tokens, LLM is able to perform scalable multimodal autoregression under its original training recipe, {i.e.}, next-word prediction. SEED-LLaMA\footnote{This work is a follow-up of SEED~\cite{ge2023planting}, where we update the visual tokenizer and present SEED-LLaMA.} is therefore produced by large-scale pretraining and instruction tuning on the interleaved textual and visual data, demonstrating impressive performance on a broad range of multimodal comprehension and generation tasks. More importantly, SEED-LLaMA has exhibited compositional emergent abilities such as multi-turn in-context multimodal generation, acting like your AI assistant.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Making the language model to see the words is one of the key research direction. This paper present new image tokenization on this direction. Specifically, unlike prior attempts that uses simple 2d style image tokenization (usually VQ-VAE), this paper propose SEED, which makes image embedding to be left-to-right 1d tokenization similar to the text while keeping semantic meaning of images but discarding low-level information. This paper claim that capturing too low-level information hider the performance of LLMs to effectively perform multimodal comprehension.

### Strengths
(1) Unifying vision and text representation is one of the hot research topic. 
(2) The assumption behind the proposal is reasonable. 
(3) The paper is generally well-written.

### Weaknesses
(1) The methodology is not religiously explained and is not self-contained. Especially, section 3.1 is hard to follow. There are no equation, and it is hard to track which components are trained on which objective function. The description of the Causal Q-former, VQ codebook, and de-tokenizer lacks sufficient detail, making it difficult to understand the exact training procedure and loss functions used for each component. It's unclear how the image encoder, codebook, and text encoder interact during training, and which parts are frozen or updated.

(2) In section 4.1, they compared SEED tokenization on image-text retrieval. As described in the paper, SEED generally outperform BLIP-2, in some case BLIP-2 exceed the proposed method. However, there are no explanation on this point. Similar criticism can be applied for the analysis on Table 3. The paper does not provide sufficient analysis on why the proposed method sometimes underperforms BLIP-2 in image-text retrieval, nor does it delve into the reasons for the observed trends in Table 3. The discussion lacks a deeper understanding of the trade-offs and limitations of the proposed approach.

(3) Regarding the Figure 7, I'm afraid the actual prompt is hard to imagine. The prompts used to generate the examples in Figure 7 are not clearly defined, making it difficult to understand the capabilities and limitations of the model. It is unclear how the model handles different types of prompts and how the image tokens are incorporated into the generation process.

(4) The proposed method contains several components, including image encoder, codebook, text encoder, and generation module. However, the importance of all components is less discussed, making me hard to access the importance of the specific choice of each component. The paper does not adequately discuss the role and importance of each component in the overall architecture. It is unclear how the choice of specific encoders, decoders, and codebooks affects the performance of the model. A more detailed analysis of the contribution of each component is needed.

(5) I'm afraid that I found a statement in the introduction is not fully validated. "Moreover, we empirically found that the dominant tokenizer VQ-VAE (Van Den Oord et al., 2017) in existing works captures too low-level information for LLMs to effectively perform multimodal comprehension task". Could you please clarify again which results support the above statement? The paper lacks empirical evidence to support the claim that VQ-VAE captures too low-level information, hindering multimodal comprehension. It is crucial to provide experimental results or comparisons to validate this claim.

(6) While the paper motivate to learn good 1D representation is key to incorporate visual information into pre-trained LLMs, but less discuss on why we should make the representation discrete rather than continuous. Table1 also seems to show that the continuous representation is generally better than discrete representation. The paper does not provide a clear justification for choosing discrete representations over continuous ones, especially given that the continuous representation seems to perform better in Table 1. The advantages and disadvantages of both approaches should be discussed in more detail.

### Questions
See weakness section

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work introduces an image tokenizer, which is capable of discretizing images into a series of tokens. These image tokens are transformed by Q-Former into pseudo-causal tokens that can serve as the input for Large Language Models (LLMs), most importantly, they can also act as the target. This allows the model to unify both visual understanding and generation tasks.

### Strengths
This paper is the first (at least to my knowledge) to use an image tokenizer to unify visual understanding and generation tasks in LLM, providing a feasible pipeline.

### Weaknesses
1. The authors claim that the use of q-former can establish a causal dependency, which I find questionable. This is because the attention in the visual encoder stage is bidirectional, leading to potential information leakage. Specifically, while the Q-Former itself uses a causal attention mask over its learned query tokens, the visual encoder (ViT) processes the entire image with bidirectional attention. This allows each patch to attend to all other patches, potentially leaking future information into the representation of a given patch. Even if the Q-Former queries are processed sequentially, the underlying patch representations used in cross-attention have already been exposed to the entire image context. This undermines the claim of a strict causal dependency.

2. Regarding the visual understanding task results shown in Table 3, why does SEED-LLaMA-I (14B) perform no better (or nearly the same) as SEED-LLaMA-I (8B) on some Image-Text Tasks? Does the proposed method not yield much gain on larger models, or has it already reached saturation? It is unclear whether the model's performance is limited by the proposed method or by the inherent difficulty of the tasks. It would be helpful to see results on more challenging benchmarks or with more complex visual inputs to better understand the scalability of the approach.

3. In Table 2, SEED-LLaMA-I achieves good results. However, I believe that CLIP similarity does not effectively reflect the quality of generation. While CLIP similarity can measure the semantic alignment between the generated image and the original image, it does not capture the visual fidelity and realism of the generated image. Fréchet Inception Distance (FID) is a widely accepted better evaluation method, which is more sensitive to the quality of the generated images, but unfortunately, this paper does not provide it. The lack of FID makes it difficult to compare the generation quality of this model with other generative models.

4. Regarding Section 4.3 (Causal Visual Codes vs. Bilateral Visual Codes), the authors mention that some mode collapse may occur for generation tasks, but what about understanding tasks? It's unclear if the use of causal visual codes also impacts the performance of understanding tasks, and if so, how. The paper should provide a more thorough analysis of the trade-offs between causal and bilateral visual codes in both generation and understanding tasks.

### Questions
See weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a method (SEED) to augment large language models (LLMs) with the capability of processing and generating visual data, i.e., images. The core contribution of SEED is a quantized tokenizer that learns to encode images into discrete visual tokens which can be again decoded using a pre-trained generative model. Once the tokenizer is trained, a LLM is trained and fine-tuned on interleaved image-text data such that the LLM can both process and generate the visual tokens which make it applicable to a variety of vision language tasks.

### Strengths
- SEED is well motivated in learning a 1D token representation that better aligns with the auto-regressive generative process of LLMs.
- Architectural choices are reasonable and have been validated with ablation studies to the most extend, i.e., text vs visual embedding reconstruction, embedding vs. discrete code, causal vs. bilateral visual codes, full fine-tuning after LoRA, instruction fine-tuning.
- The quantitative evaluation convinces in either surpassing or being competitive in image-text, video-text tasks as well as generative image-to-image and text-to-image tasks.
- The qualitative results showcase some interesting multi-modal capabilities of SEED, including compositional and in-context image generation.
- Publishing both code and checkpoints of large-scale models enables future research and empowers the open-source community.

### Weaknesses
 - Some architectural design choices are missing an explanation.
    - In general, it would help the clarity of the paper if all loss functions would be written out.
    - What is the reason behind using two different image encoders, one for encoding the input to the causal q-former (BLIP-2 ViT) and one for the image generation conditioning (unCLIP-SD vision encoder)? This requires loading more weights into memory during training so an explanation is needed. Can we use the unCLIP-SD vision encoder for both cases?
    - How important is the contrastive loss between the vision and text embeddings? An ablation could justify it's inclusion. It is surprising that the contrastive loss is only applied on the last token of the Causal Q-Former, as the model could potentially ignore the first 31 tokens and embed all information into the last token. This is especially concerning since BLIP-2, which inspired the use of 32 tokens, applies the loss function to all tokens.
    - Why was the original VQ codebook loss replaced by a simple reconstruction loss with cosine similarity? How are collapsing codebooks avoided? Are there any stop-gradient operation in the loss for the codes?
- The arguments and ablation for using causal vs. bilateral visual codes is not convincing. In general, previous work on VQ models have demonstrated that transformers can learn complex and even low-level dependencies of non-causal codes. Enforcing a causal mask in the q-former restricts the information flow to fully utilize the tokens efficiently and effectively. The argument made in Sec. 4.3 is that the LLM struggles with generating the correct sequence length for images which should always be 32. It is surprising that this happens because the start token for images (as in Fig. 4) should be a clear signal to the LLM that 32 image tokens follow. In practice however, it would be straightforward to enforce the generation of 32 image tokens after the start token is observed by restricting the possible output tokens. How do these two models compare when the number of image tokens is enforced to be always 32?
- It is not clear how videos are being processed. Are individual frames used to train the tokenizer or are multiple frames passed to the causal q-former? If multiple frames are passed, how do you adjust the reconstruction loss for the generative embedding (1 embedding per frame from unCLIP-SD vs. one embedding per video from your tokenizer)? Do you simply append the encoding of multiple frames when passing videos to the LLM?

### Questions
- How did you decide on using 32 tokens per image and 8192 codes? 
- Can you confirm that you are using a start and end token for images as shown in Fig. 4? Do you use the same start/end tokens for both images and videos? This information should be included in the paper.

Suggestions:
- It would help the read flow to already mention the codebook size in section 3.1.2 instead of only in 3.2.1 (i.e., 8192 visual codes).
- When Table 2 is first discussed in Sec. 4.1, it is unclear what $\text{SEED}^{\text{text}}$ refers to. A short description and reference to the ablation in Sec. 4.3. would better facilitate immediate understanding for the reader. Similarly for the "I" suffix referencing the instruction-tuned model.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
