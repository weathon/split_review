# Language Modeling Is Compression

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
It has long been established that predictive models can be transformed into lossless compressors and vice versa.
    Incidentally, in recent years, the machine learning community has focused on training increasingly large and powerful self-supervised (language) models.
    Since these large language models exhibit impressive predictive capabilities, they are well-positioned to be strong compressors.
    In this work, we advocate for viewing the prediction problem through the lens of compression and evaluate the compression capabilities of large (foundation) models.
    We show that large language models are powerful general-purpose predictors and that the compression viewpoint provides novel insights into scaling laws, tokenization, and in-context learning. For example, Chinchilla 70B, while trained primarily on text, compresses ImageNet patches to 43.4\% and LibriSpeech samples to 16.4\% of their raw size, beating domain-specific compressors like PNG (58.5\%) or FLAC (30.3\%), respectively. Finally, we show that the prediction-compression equivalence allows us to use any compressor (like gzip) to build a conditional generative model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper demonstrates that pre-trained large language models can be used for compressing text, image, and audio data. This is done by inputing the data to the model and relying on the model’s output probabilities across the vocabulary to perform arithmetic coding. When not considering the size of a model for computing compression ratios, the authors show that Chinchilla-70B, achieves high compression ratios surpassing well-established domain-specific compressors like PNG or FLAC. When taking into account the number of model parameters for calculating the compression ratio, the authors illustrate new empirical scaling-laws by plotting the compression ratio as a function of model size, resulting in an U-shaped curve. This scaling law suggests that depending on the size of a dataset the optimal compression ratio is achieved for one specific model size. The authors also attempt to show how compressors can be used as conditional generative models. Finally, the authors analyze how the context-length for in-context learning and different tokenizers affect a model's compression performance.

### Strengths
- The paper presents how large language models pre-trained on text data can be used for compression beyond text data 
- The authors demonstrate that this approach outperforms several well-established compression methods like gzip, PNG or FLAC in terms of raw compression ratio
- The paper provides insights on how different aspects like model size and choice of the tokenizer affects performance. For example, for model size the authors provide empirical scaling laws
- The experiments are well described, easy to follow, and kept fair for all the methods being compared. 
- Tables and figures showing the results of the experiments are also simple to understand
- The authors openly discuss limitations of using large language models as compressors (e.g. model size and context length for transformer models)

### Weaknesses
 - The motivation of this work is rather unclear to me. Is this work about advocating the use of pre-trained large language models as a potential method for compression? If so, how can they be used as such in practice considering their limitations? Or is it about using the compression framework to better understand large language models? If so, why is it interesting to study pre-trained large language models  "through the lens of compression"?
- The authors mention that they “advocate for using (lossless) compression to study foundation models”. Why and what benefits does this framework have? It is not clear to me how the results in this paper should help my understanding of large language models beyond their use as compressors? What are the further implications of the results?
- No experiments with pre-trained models other than Chinchilla-70B. Having more models could provide more evidence on the compression capabilities of pre-trained large language models and to see how compression capabilities correlate with prediction performance
- Not using publicly available pre-trained large language models for reproducibility
- The results for the generative modeling performance of compressors and Chinchilla-70B look rather poor. For example, the generated image in Figure 3 looks unconvincing since only lines are generated and not actual image content, and a quantitative analysis is also missing. Why is this section important, and why would it fit into the rest of the paper?

### Questions
Questions:
- The questions mentioned in the "Weaknesses" paragraph

Suggestions:
- To me, some findings feel somewhat scattered and it is difficult to draw a clear conclusion from this work. For example when and why is it important to distinguish between compression rates that consider and do not consider model size, and particularly the part discussing the generative capabilities feels disconnected from the rest of the story. I recommend aligning the narrative more cohesively and concluding with a clear takeaway message
- I find that the background section is more technical than needed to understand the results of the paper. For example, the authors could maybe show on a concrete example how arithmetic coding works instead being very general and introducing a lot of mathematical notations and concepts. Reducing the relatively heavy use of mathematical notation could also help with reading since most of it does not appear again after the background section. Also, in Figure 1 which illustrates arithmetic coding, there are missing explanations (e.g. arrows are not explained) to guide the reader.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper advocates viewing the prediction problem through the lens of compression and evaluates the compression capabilities of large (foundation) models, thereby providing insights into scaling laws, tokenization, and in-context learning.

### Strengths
1. Novel in the sense of applying LLM to compressed coding of images & audio.
2. Demonstration through resourceful examples.

### Weaknesses
1. The idea of deep model learning being a compression of natural data is not new, I think this is echoed by the authors too. It has, e.g., been a core and explicit theme in "High Dimensional Data Analysis with Low-Dimensional Models: Principles, Computation, and Applications". As such, shouldn't the paper's title be more specific, such as "LLMs are general-purpose image & audio compressors"?

2.  A key into understanding the algorithm is Fig. 1, but the figure contains ambiguities and confusion. E.g. Why a "?" in "b0?" only? In the last column, how to go from 4bit to 7bit? The illustration should be more tractable. The description of how the intervals are split and how the binary sequence is derived is not clearly explained, which makes it hard to verify the correctness of the compression process.

3. I have doubt about the "generative" model part, for the text examples in B.1, the good performance of Chinchilla over gzip is no surprise. But the poor performance on images & audio in Fig. 3 & B.2 indeed shows LLM can't handle these data in general. How can an LLM even be called generative in images/audio if the results make no sense? If that's the case, the last sentence in Abstract shouldn't be made. The paper does not adequately explore the limitations of applying a text-based model to non-text modalities, and the claim of general-purpose compression seems overstated given the observed poor performance on image and audio data.

4. I am also doubtful about the part on tokenization. The tokenizer being part of a Transformer is only due to its root in language modeling. In the same vein, we can easily make a claim on "A CNN stem is compression" (a CNN has a stem, body & head), and varying the stem (e.g. different strides) we get different compression rates too, so what is interesting in that? The paper does not offer a strong justification for why the tokenization process in transformers is particularly insightful for compression, beyond the fact that it reduces the input sequence length. This argument lacks depth and does not provide a novel perspective on tokenization itself.

Editorial:
The line above Sect 3.6, typo "accross"

### Questions
See weaknesses for questions.

Also, is the context length of 2048 bytes still a must given the recent work on lifting this length constraint? e.g. "Efficient Streaming Language Models with Attention Sinks".

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors argue that predictive models can be transformed into lossless compressors and vice versa, and that language models can also be powerful compressors, providing novel insights into scaling laws and in-context learning. The paper includes experimental details and additional results, including data auto-regressively generated by gzip and Chinchilla.

### Strengths
1.  The paper is well-written and clear to investigate how and why compression and prediction are equivalent. 
2. Evaluate large pretrained models used as compressors against various standard compressors and showed that they are competitive, not only on text but also on modalities they have never been trained on, such as images and audio data.

### Weaknesses
If we discuss the number of parameters in larger language models and how it reflects compression performance, it would be better to investigate the reasons behind this relationship.

### Questions
The questions are listed in the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an interesting view that connects compression and prediction of LLM. It leverages a pre-defined rule (e.g., Arithmetic coding) to compress a sequence based on the conditional probabilistic intervals of its each token. The compressed content can be losslessly restored to the original content based on the decoding rules that reverse the encoding process. The experimental results show an LLM can be very effective to compress content and works as a general-purpose compressor.

### Strengths
This paper discusses a novel perspective to connect between compression and sequence prediction. Its evaluations on the compression capabilities of LLMs are extensive and sound. The results that it can compress other modalities like images and audio are pretty interesting and its insight of the compression with the size of data and model (scaling) is inspiring.

### Weaknesses
While this paper introduces a novel perspective to understand the compression ability of Large Language Models (LLMs), its contribution or novelty is not particularly prominent from a high-level idea/conclusion standpoint.

Firstly, the concept that a language model is a form of compression is not new. As early as 2023, in an interview between Nvidia's Jensen Huang and OpenAI's Ilya Sutskever, Ilya mentioned that a language model learns through compression, and the generative model is essentially a compression of data in the world. This insight is well ingrained among most NLP/LLM professionals. Therefore, although this paper connects sequence prediction and compression from an arithmetic perspective, aside from some interesting experimental results, it doesn't provide practitioners with many new insights, such as in terms of methodology. While its LLM compressor performs well compared to gzip, it is difficult to use in practice due to the high inference cost.

Secondly, I believe a major highlight of this paper is the discussion on general-purpose (trained on text, but can work for other modalities) and scaling (the larger, the better at compression). The overall method of the paper still uses the Arithmetic coding approach. However, prior work has already presented similar observations and conclusions, albeit not from an arithmetic coding perspective. For instance, Ge et al. (2023) proposed using lora tuning to adapt the LLM for the compression ability, enabling it to compress a long context into a short span. Although Ge et al.'s (2023) work is not lossless compression, they observed similar phenomena: for example, their Table 3 comparison of normal text, patterned random text, and completely random text shows that LLMs can compress based on certain patterns (even though the model has not seen patterned random text, it performs better on patterned random text than on completely random text). Similarly, their Tables 5 and 8 also indicate that more potent LLMs are better at compression. Therefore, while I find the perspective of this paper novel and interesting, its final conclusions cannot be considered entirely novel.

Despite these weaknesses, I think this paper's contribution overweigh the weaknesses as a research paper to present in ICLR.

### Questions
See the weakness section.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
