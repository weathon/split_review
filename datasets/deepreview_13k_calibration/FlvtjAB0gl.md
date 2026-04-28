# Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 5, 6

## Abstract
Recently, the remarkable advance of the Large Language Model (LLM) has inspired researchers to transfer its extraordinary reasoning capability to both vision and language data. However, the prevailing approaches primarily regard the visual input as a prompt and focus exclusively on optimizing the text generation process conditioned upon vision content by a frozen LLM. Such an inequitable treatment of vision and language heavily constrains the model's potential. In this paper, we break through this limitation by representing both vision and language in a unified form. Specifically, we introduce a well-designed visual tokenizer to translate the non-linguistic image into a sequence of discrete tokens like a foreign language that LLM can read. The resulting visual tokens encompass high-level semantics worthy of a word and also support dynamic sequence length varying from the image. Coped with this tokenizer, the presented foundation model called \textbf{LaVIT} can handle both image and text indiscriminately under the same generative learning paradigm. This unification empowers LaVIT to serve as an impressive generalist interface to understand and generate multi-modal content simultaneously. Extensive experiments further showcase that it outperforms the existing models by a large margin on massive vision-language tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposed to unify the pre-training objectives for visual and textual tokens while adapting the LLM for vision-language tasks. To this end, they first train a visual codebook to quantize the visual embeddings and assign each visual token a discrete label. To reduce the length of visual tokens, a token selector is proposed to select important visual tokens dynamically, and the token merger is used to merge dropped tokens with selected ones. The visual tokens and text tokens are then concatenated and fed to the LLM, which is trained for classification-based language modeling tasks. The authors conduct extensive experiments to evaluate the proposed methods, and the experimental results show that the proposed methods achieve state-of-the-art performance.

### Strengths
- The experimental results demonstrate that the proposed method achieves a significant improvement compared to previous works.
- The improvements from each proposed component is well supported by the ablation study results.

### Weaknesses
 - The authors train a visual codebook to assign discrete labels to visual tokens, which can be computationally costly. In the context of efficiently adapting LLM for vision-language tasks, it would be interesting to explore whether existing codebooks [1, 2, 3] can be utilized to provide useful supervision for training LLM. Specifically, the paper should investigate the performance of using pre-trained codebooks from models like VQ-VAE [1] or BEIT [3] as initializations or alternatives to their learned codebook, analyzing the trade-offs in computational cost and downstream task performance.

- Hard to be completely fair when compared against other baselines. For instance, compared to BLIP-v2, this work adds additional English text corpus and further fine-tunes the LLM. The significant performance improvement over previous work may be attributed to the additional training data and trainable parameters. It is unclear how much of the performance gain is due to the proposed method versus the increased model capacity and training data. A more controlled experiment, perhaps by training BLIP-v2 with the same additional text data and fine-tuning strategy, would be necessary to isolate the contribution of the proposed method.

- The implementation details of the ablation studies could be clearer. It is confusing why the proposed method achieves different results in Tables 3, 6, and 7 when doing ablation studies. The paper should explicitly state the number of training steps, batch size, and other relevant hyperparameters for each ablation study to ensure reproducibility and allow for a more accurate comparison of the results across different tables. The lack of consistent training configurations makes it difficult to draw firm conclusions from the ablation studies.

- The authors claim that the learned codebook encodes high-level semantic concepts. However, the visualization results of codebooks in Figure 5 may suggest that the same code groups image patches based on low-level visual patterns, such as color and textures. It would be interesting to see additional image-level visualization results, similar to those in [4], to demonstrate that the codebook encodes high-level semantic concepts. The current visualizations are insufficient to support the claim of high-level semantic encoding, and more comprehensive visualizations are needed to validate this claim.

- Minor suggestions/typos: I noticed several typos while reading the paper: 

  - Figure 1 (a) caption: Adater -> adapter
  - The symbols X and when calculating K and V of Equation (2) should be X_d.

### Questions
Refer to the weakness.

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an image tokenization method for visual-language model (VLM) pretraining, called dynamic discrete visual tokenization. The proposed method has two key characteristics:
* Discrete: Continuous feature vectors from each image patch are mapped to a learnable codebook, resulting in discrete visual tokens compatible with text tokens. The discrete visual tokens make it possible to pre-train VLMs using the same autoregressive language modeling paradigm as text-only LMs.
* Dynamic: The number of visual tokens is dynamically adjusted depending on the image content using a token selector and token merger. The token selector chooses the most crucial patches in the image, and the token merger reacquires the visual semantics of the unimportant patches, respectively.

The proposed method is pre-trained in two steps:
1. Tokenizer learning: The tokenizer is pre-trained to reconstruct the original image from the quantized compressed visual tokens.
2. Vision-language model learning: The VLM is pre-trained to predict the next visual/text token in a sequence, using the same autoregressive language modeling paradigm as text-only LMs.
The proposed method achieves high performance on multimodal understanding and generation tasks, with the relatively small size of model parameters and training data requirements. The paper also shows that quantization and token compression are effective techniques for improving the efficiency of VLM pre-training.

Overall, this paper presents a novel and effective method for VLM pretraining. The proposed method looks simple yet effective and achieves state-of-the-art results on various multimodal tasks.

### Strengths
The paper is well-organized and easy to read, and the advantages of the proposed tokenizer are clearly described and demonstrated through various experiments and evaluations. In particular, the method for improving the inefficiency of the conventional vision-text fusion method is effective, and this study can be considered primary research for further improvement.

### Weaknesses
There are a few suggestions for the ablation study.
1. Compare the performance of text generation using merged continuous embeddings and quantized visual tokens. The loss of detailed information due to quantization is likely to affect the performance of text generation. However, it would be interesting to see how much of a difference there is.
2. Show the performance difference with and without token merger. It would help to understand the importance of the token merger module.

### Questions
1. What is the computational (speed) improvement during inference using a dynamic token length? It may be important information because training and inference efficiency may vary.

2. There are a few things that could be improved in the manuscript. Please see the following suggestions.

- Figure 1 (a): `Adater-Style` -> `Adapter-Style`
- The first line in Section 3: `the Large language model` -> `the large language model`
- The last line in `Token Selector` of Section 3.1 : `the binary decision M` -> `the binary decision mask M`
- Equation 3: $||l_{2}(\hat{x_i})-l_{2}(c_{j})||$ -> $||\hat{x_i}-c_{j}||_2$
- The 2nd line in Section 4.4: `the token predictor` -> `the token selector`

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes the idea of treating images and text equally, transforming images into a series of discrete tokens to input into LLM, and training LLM from scratch to complete understanding and generation. The experimental part of the paper yielded so-called advanced results.

### Strengths
1. The paper proposes to convert the image into a series of discrete tokens and adjust the token length according to the image content.
2. The visualization of discrete tokens is displayed in Experiments to help readers understand the semantic content carried by tokens.
3. Better results than the baseline method are achieved in the experiment.

### Weaknesses
1. The novelty of this paper is limited and the ideas of the paper have already been explored in previous work. For example, end-to-end training LLM has been explored in Emu[MR1], and the transformation of visual information into discrete tokens have been explored in [MR2, MR3, MR4, MR5].

2. The generation process relies on a stable diffusion model, which makes the verification of the visual generation capabilities of the proposed model limited. Do the image generation results rely on strong stable diffusion, or are they more attributable to the discrete labels generated by the model? It is unclear to what extent the good results achieved are due to stable diffusion.

3. Visual token merger part is not well validated. How much additional complexity does this stage bring to the model? Are different codebooks needed for data in different domains (animation, painting, natural landscape, etc.)? Why is a complex merger mechanism needed? Can a simple attention map from a pre-trained model indicate the importance of individual image patches?

3+. BTW, the processing of the decoder (using the stable diffusion model) is the same as Emu's [MR1] strategy. A reference to the corresponding location and some justifications are required.

4. In the experimental results in Table 3, using a larger number of tokens (fixed) achieves worse results, and more explanations need to be added.

### Questions
Refer to weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a vision-language framework with unified objectives for both language and image.
The crux of the proposed method is the design of a dynamic discrete visual tokenization module.
In particular, the proposed LaVIT leverages a dynamic token sparsification approach to embed the given image with fewer vision tokens.
After that, the learned tokenizer is employed to generate discrete vision tokens.
In this way, the proposed framework can achieve a unified pre-training objective.

### Strengths
- The proposed method achieves very impressive performance on several vision-language tasks such as VQA and image captioning.
- The strategy to pre-train the vision-language models with a unified objective seems interesting.
- The method can generate high-quality images based on the given textual prompt.

### Weaknesses
 - The structure of the writing, especially the method section, is very confusing to me.
In fact, the key to the proposed method is the learning of the vision token codebook.
This codebook and token selector are built on the first stage of learning.
However, the authors' description of this part makes it look like an end-to-end training framework, which confuses me a lot.
I would suggest the authors carefully revise the structure of this section.

- The authors claim their method can achieve in-context learning capability. 
However, I cannot find any experiments pertaining to this merit.

- The authors did not provide a good explanation of why inequitable treatment for language and vision harms multi-modal learning.

- More details about the language-vision pre-training part are required.

### Questions
- Is it possible that the impressive performance of the proposed method is due to more training data, especially for the vision tokenization codebook?

- Why do the authors still use the unselected tokens as keys and values? 
One intuitive approach for these tokens is simply discarding them.
Moreover, these tokens should contribute minorly to the final performance and are redundant as authors claimed.

- For the causal attention, which tokens are seen as previous ones? 
As there is actually no sequence for an image, using causal attention for image encoding is thus not convincing.

- What is the function of the second half of Eqn. 4?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
