# TextEconomizer: Enhancing Lossy Text Compression with Denoising Autoencoder and Entropy Coding

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
Lossy text compression reduces data size while preserving core meaning, making it ideal for summarization, automated analysis, and digital archives where exact fidelity is less critical. While extensively used in image compression, text compression techniques, such as integrating entropy coding with autoencoder latent representations in Seq2Seq text generation, have been underexplored. A key challenge is incorporating lossless entropy coding into denoising autoencoders to improve storage efficiency while maintaining high-quality outputs, even with noisy text. Prior studies have mainly focused on near-lossless token generation with little attention to space efficiency. In this paper, we present a denoising autoencoder with a rectified latent representation that compresses variable-sized inputs into a fixed-size latent space without prior knowledge of dataset dimensions. By leveraging entropy coding, our model achieves state-of-the-art compression ratios alongside competitive text quality, as measured by diverse metrics. Its parameter count is approximately 196 times smaller than comparable models. Additionally, it achieves a compression ratio of 67× while maintaining high BLEU and ROUGE scores. This significantly outperforms existing transformer-based models in memory efficiency, marking a breakthrough in balancing lossless compression with optimal space optimization.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposed a DAE method designed for English text self-coding task is constructed by one-way bidirectional gated recursive unit (GRU) and combined with entropy coding to optimize the compression effect.

### Strengths
S1. The memory compression ratio achieves on texts are impressive.

### Weaknesses
W1. [Clarity & Writing - 1] The paper's writing could be improved to clearly outline its contributions in the introduction and abstract. Additionally, the text becomes overly verbose and includes several claims in the method section without direct references. Proper citations are needed for every claim that refers to existing literature. For instance, there is a missing reference or explanation for the "Lempel–Ziv–Markov compressor."

W2. [Clarity & Writing - 2] The paper's structure should be clearer and better organized. For example, Section 3 dedicates substantial space to details about the dataset (e.g., number of words), which is less relevant to the content of Section 4. Furthermore, the dataset attributes are repeated in Section 5.1. Additionally, Section 5 appears to be a continuation of the experimental results, and it should not be clearly separated from Section 6. Additionally, the tables should be properly positioned and the fonts should be consistent.

W3. [Experiments] There are a lot of unfair comparisons and over claims in the paper. For example, the Transformer shown in Table 1 outperforms the proposed method (97.33 vs 95.75, 99.46 vs 99.28) in terms of BLEU and BERT Score. Considering that the number of parameters of the transformer can be adjusted by reducing the number of layers or the dimension of embeddings, it is more fair to choose the transformer structure with the same number of parameters as the method in this paper.

### Questions
1. Teacher-forcing is mentioned in Figure 1, but is not described in the method section. Can you describe it briefly?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an auto encoder for text data, with the goal of lossy text compression. The goal is to preserve text semantics while minimizing rate transmitted. The method, called TextEconomizer, consumes a noisy text, transmits a fixed size latent vector, and reconstructs the text, using cross-entropy loss with partial teacher-forcing. Experiments compare TextEconomizer to several baselines, primarily lossless text compressors, and some text language models.

### Strengths
- Lossy text compression seems to be a relatively novel area of research, so the novelty of such a work is good.

### Weaknesses
 - I found the overall presentation of the work to be a bit confusing. Section 3 seems to include a lot of data creation details, which appears to explain the noise adding process, but a lot of the details I felt should have been placed in experimental setup or appendix. 
- Many of the baselines mentioned in the related work are not compared to. The only relevant baseline used in section 6 that actually does lossy text compression appears to be NUGGET, although I may be mistaken. Everything else appears to be a language model (such as T5) or lossless text compressor (Huang et al, 2023). It is difficult to judge the efficacy of TextEconomizer without a comparison to the lossy text compressors in the related work.
- Furthermore, the baselines section of 5.2 does not include all the baseline comparisons actually used in section 6. 
- In Table 1, it is hard to say that TextEconomizer is superior to NUGGET (the only other lossy text compressor). NUGGET has less memory compression ratio but superior BLEU. 
- In addition, NUGGET is missing in Table 3. It would be helpful to have a qualitative comparison for NUGGET.
- In my opinion, it may also be useful to have a metric such as Levenshtein score, in order to measure the similarity between texts in text space, rather than just BERTScore, which compares in the embedding space. This comparison would help support the qualitative results in Table 3. 
- An ablation study is missing. I think this is important because the texts shown seem to be relatively short. Since the latent variable is fixed-size, it is possible the performance may suffer if the input text lengths are longer. It would be helpful to know how the model performance changes based on (i) the fixed-size latent variable size and (ii) the input text length. In addition, the ablation study could support other design choices, such as the noise adding process.

### Questions
In addition to the questions in the weaknesses section, I have the following questions:
- Why is the fixed-size latent space necessary? I think this was motivated in the introduction, but I found the explanation there to be confusing. Presumably, a variable-size latent space could still be entropy coded or LZ-coded.
- Moreover, is the latent Z quantized before encoded with LZ? If not, this does not seem possible, as lossless compression needs a discrete input.
- Why not additionally use an entropy-model to minimize the entropy of the latent z? This would further reduce the rate, and jointly minimize the rate and cross-entropy. It can also support a variable-size latent space.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper argues that while lossy compression is widely used in image processing, its application in text compression has been less explored. Their proposed model, TextEconomizer, compresses variable-sized text inputs into a fixed-size latent space via an autoencoder-style framework and achieves relatively good compression ratios with competitive text quality, as measured by BLEU, BERT Score, ROUGE scores and PPL. The model is parameter-efficient, and it significantly outperforms existing transformer-based models in memory efficiency with the use of entropy coding on latent representations.

### Strengths
High Compression Ratio: TextEconomizer achieves a remarkable 67× compression ratio (lossy) while maintaining relatively high BLEU and ROUGE scores, indicating that it is effective at compressing text without significant loss of meaning.

Memory Efficiency: The model demonstrates significant memory efficiency with additional entropy coding on latent representations.

Parameter Efficiency: TextEconomizer shows that high performance can be achieved with a parameter count significantly smaller than comparable models.

### Weaknesses
(1) Using autoencoder and entropy coding for lossy compression is not a new idea, especially for visual signal compression like image compression [Ref1] and video compression [Ref2]. When referring to lossy image compression methods with variational autoencoders, the authors should include these representative related works in this paper (incomprehensive literature review).

[Ref1] Variational Image Compression with a Scale Hyperprior. Ballé et al., ICLR 2018.

[Ref2] DVC: An End-to-end Deep Video Compression Framework. Lu et al., CVPR2019.

(2) When applying lossy compression for text compression, it is obvious that text corpus get much high compression ratio compared with lossless compression methods, but with the sacrifice of text reconstruction precision. Different from visual signals likes images, text is a data modality with high information density. Therefore, if the authors would like to compression text in a lossy way, they should convince others that " Lossy text compression reduces data size while preserving core meaning, making ideal for some tasks". In other words, some experiments should be performed on tasks like summarization, automated analysis, and digital archives, to ensure that lossy text compression is still useful for these tasks.

(3) Different from lossless compression, lossy compression should usually be measured by different compression ratios and different distortion levels, more like a compression ratio - distortion curve. Maybe the authors can adjust the latent dimension to investigate on different compression ratios.

(4) Most of the literature referred in this paper is not correctly cited. Many references are Arxiv version. In addition, the well-known paper "Attention is All you Need" is mistaken as a paper published in 2023 (which should be a paper published in NeurIPS 2017)

### Questions
As I am not very familiar to this area, I hope the abovementioned weakness points could get some feedback from the authors.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents TextEconomizer, a lossy text compression method that combines a denoising autoencoder with entropy coding. The main claimed contributions are:
- A text noise process for training robust denoising
- A monolingual autoencoder architecture using fixed-size latent representations
- Integration of entropy coding for improved compression ratios
- Evaluation showing 67x compression while maintaining quality metrics
- Analysis of training corpus size effects on performance

### Strengths
- The reported performance is good.

### Weaknesses
 - **Lack of technical contribution**: The reviewer didn't see any technical contribution of the proposed method.
- **Lack of analysis and inspiration**: The authors didn't provide any principles, analysis, theory, or even intuitive explanations for their proposed methods. Readers are unable to understand why the proposed method outperforms others.
- **Duplicate claims of contribution**: Despite the claimed 5 contributions, most of them are duplicate and meaningless.
- **Bad presentation**: The proposed method is not presented well in the context of the paper. The authors prioritized massive details of datasets over task formulation and methodology, which makes it difficult for readers to understand the technical contribution of the paper. **LZMA** shows up in Figure 1 without any prior definition. Redundancy in this paper somehow validates the importance of text representation compression.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
