# Large Language Models Are Stronger Entropy Models for Transform Coding

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 5, 6

## Abstract
Large language models (LLMs) have shown promising advancements in lossless compression due to their excellent next-token prediction capabilities. However, there is a gap between LLM-based compressors and classical transform-based codecs. Existing LLM-based compressors function solely as entropy coders, focusing on compressing redundant data in the raw domain. In contrast, classical codecs typically transform raw data into more compact features in the latent domain before applying entropy coding. But LLM-based compressors have not discussed this case. To our knowledge, this is the first work to introduce an LLM-based entropy model for transform coding. Specifically, we propose a simple yet effective fine-tuning strategy, tested across various codecs for both images and speeches. With less than 2% parameters are fine-tuned, the LLMs can serve as highly effective entropy models for well-established transform-based compression codecs. For instance, LLaMA3-8B paired with arithmetic coding compresses latent image codes on Kodak to 4.62% and speech codes on LibriTTS to 42.53% of their transformed sizes after fine-tuning. Our proposed methods achieve notable BD-rate improvements of 54.07% over JPEG, 17.61% over VQGAN, and 34.61% over SpeechTokenizer. These findings highlight the great potential of integrating LLMs into codecs to significantly improve coding efficiency. Source codes will be released upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper studies using LLMs in the compression of transformed data in lossy compression. It is not about using LLMs to improve the transformations, but only about improving probability estimation for the arithmetic coding stages. It uses the power and computational complexity of LLM to generate better probabilities for transform data, which are coded using arithmetic coding.

In the paper most of the work is about ad hoc modifications to adapt the data to format most suitable for LLMs, and related training and adjustments.

### Strengths
The idea of using LLMs for estimating symbol probabilities in entropy coding is not new. In fact, since it represents a more complex prediction structure, it is not surprising that it could be used in applications like lossless compression of text and somewhat improve results. There are several papers on the subject (including in the citations of this paper).

The main contribution of this paper is to extend this approach to compressing data after linear or nonlinear transformations. Since the purpose of those transformations is exactly to reduce source redundancies, they by definition are meant to use simpler entropy models. Thus, compression results are better, but it is not surprising that a very complex method will enable better compression.

### Weaknesses
While the results do so show some improvement, they are mostly when compared to much simpler methods. For example, for image coding the results may seem significant when compared to the 40+-year-old coding techniques of JPEG, but much less when compared to the hyper-prior prediction, which is much simpler neural-based approach and not sufficiently discussed.

It is important to consider that the most fundamental practical problem is if the improvement in compression justifies such very expensive LLM computations. Comparisons with methods that are orders of magnitude more efficient are not fair, and do not provide real insight on the contribution.

Complexity is partially shown by running times in Table 4, but this table is not even commented anywhere in the text. The caption refers to 64x64 images, but that size is completely unrealistic. This needs to be more carefully analyzed and explained.

In summary, paper claims to be the first to apply LLMs to help entropy coding of transformed data, and as expected it gives some improvement due to the better prediction capabilities of LLMs, but with enormously larger complexity, and the results are not significantly better than other simpler neural-network-based prediction like hyperprior networks, or entropy coding methods more modern and more powerful than JPEG’s.

From a theoretical perspective, it is not clear if there is enough novelty in showing that LLM-based compression, which has been shown to work on other data, also works with transform coefficients.

### Questions
It would be interesting to see more comparisons with the hyper-prior approaches (including complex recursive version), and computational complexity.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a method to leverage the strength of LLMs for predictive coding in the transform-coding setting. Specifically, the paper proposes a latent code arrangement technique that is shown to work with three different codecs (JPEG, VQGAN, and SpeechTokenizer). The latent code arrangement is used to align the dimensions of the LLMs and the latent codes. The input and output layers of the LLM are trained while the rest of the LLM backbone is frozen. The proposed approach delivers significant improvements with JPEG and consistent improvements with VQGAN and SpeechTokenizer.

### Strengths
1. The proposed approach delivers impressive gains with JPEG and consistent gains with VQGAN and SpeechTokenizer.

2. The latent code arrangement approach is flexible, which makes it well-suited to the transform-coding framework.

### Weaknesses
1. Lack of novelty. The key idea of leveraging the strong predictive capabilities of LLMs for compression has been proposed and explored in the literature (Deletang et al. 2024, Valmeekam et al. 2023). Given this, the main contribution in this work (of latent code arrangement) is incremental as far as novelty is concerned.

2. There is no qualitative evaluation of the proposed approach. It would be interesting to see how the coding efficiency manifests in terms of perceptual image/speech quality.

3. There is no comparison with Deletang et al.’s work. Given the same underlying philosophy, such a comparison is warranted. 

4. There is no discussion on the choice and size of the training dataset on performance. Also, the ImageNet dataset is not particularly suited for evaluating codec performance.

5. The quality of the writing needs improvement. For example, there are missing references and grammatical errors.

### Questions
1. What is the impact of the coding gains on perceptual quality? Can you please provide image examples?

2. Have you considered other perceptual quality metrics for evaluating performance? 

3, Why is a comparison with related methods not presented? Such a comparison would help place the proposed work on a strong footing.

4. What is the impact of the training dataset on performance? What is the impact of using the Kodak dataset for testing instead of ImageNet?

5. Why was the ImageNet dataset used for training the model? ImageNet data is not particularly suited for testing codec performance. Questions 4 and 5 apply to the speech codec as well.

6. What is the impact of the inference time on scaling the proposed method to large data?

7. Why are smaller image sizes considered for running time measurements? These sizes are not representative of standard image resolutions such as full-HD or higher.

### Soundness
2

### Presentation
2

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
In this paper, the authors proposed to use LLM + transform coding for the compression tasks. Unlike previous work which use LLM for performing compression in the raw signal (e.g. pixel) domain, the authods proposed to use LLM for performing compression in the latent domain, where the latent codes are obtained by transform like DCT or neural networks. The authors have demonstrated by simply finetuning LLM, it can be used for enhancing the compression performance of the latent code.

### Strengths
- In this paper, the authors propose using LLM + transform coding for compression tasks. I think this is a novel idea and worth studying.
- The authors demonstrated that, with simple fine-tuning, LLMs can be adapted for compressing the latent code generated by different transformations.

### Weaknesses
 - In my opinion, the main contribution of the work is exploring the use of LLMs for compression in the latent domain. However, the techniques proposed for adapting LLMs for compressing different signals are straightforward.

- From this work, I can't see the potential for integrating LLMs into codecs (which the authors suggested) due to the model's size, complexity, and performance. The performance of the proposed method is clearly not comparable with SOTA codecs, requiring a large model with a significant amount of computation/parameters and a slow inference speed.
    - For example, it’s not comparable with the classical Hyperprior model in learned image compression, where the SOTA image codecs are far better than the Hyperprior model.
    - In the case with VQGAN, the number of required fine-tuning parameters is up to 134.2M, which is larger than most existing codecs. When the fine-tuning parameters exceed those of a neural codec (which also outperforms the proposed method), I can't agree that fine-tuning an LLM for compression is a practical approach.
    - While the use of an LLM within a codec for entropy coding may not be practical, I believe the study of LLMs for latent domain compression is still interesting.
- Although the authors suggested that the raster order preserves spatial correlations, I think this is not correct for the JPEG case, where the DCT converts the inputs into the frequency domain.
- As VQGAN was not originally proposed for the compression task, it may not be suitable as an anchor for evaluating compression performance.

### Questions
- Why is there no comparison to VQGAN in the RD plots?
- For the VQGAN anchor, how is entropy coding being performed?
- How are the rate points generated for Figure 5? (The authors only mentioned using QF 20/50/80, but there are more rate points in Figure 5.)
- Are only two rate points being used to calculate BD-rate for VQ-GAN+LLM?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel image and audio compression method that leverages large language models (LLMs) as entropy encoders, significantly enhancing the efficiency of traditional compression approaches. Unlike entropy encoding methods that rely on static probability distributions, LLMs can dynamically predict the conditional probability of each symbol by utilizing contextual information, resulting in more efficient encoding. By applying minimal fine-tuning to the LLM model, this method successfully adapts to data across different modalities.

### Strengths
1. The authors conducted multimodal testing of the method, covering various data types including images and audio, which validated the method's effectiveness across multiple data modalities. Experiments included a range of encoding baselines, such as JPEG, VQGAN, and SpeechTokenizer, demonstrating the method’s versatility, showing that LLMs can adapt to diverse data modalities and compression requirements.

2. Through dynamic probability prediction, the use of LLMs as entropy encoders significantly enhances compression efficiency, achieving notable improvements over baseline methods, particularly for image and audio data. Experimental results demonstrate that the model achieves strong compression performance across various datasets.

3. The paper presents a computationally resource-efficient approach that requires fine-tuning only a minimal portion of the LLM’s input and output layers to adapt to inputs of different dimensions.

### Weaknesses
1. This paper should provide experiments applying the LLM-based entropy encoding scheme to VAE-based models, such as HyperPrior, and conduct a comparative analysis with the results of the original entropy encoding scheme. This would yield more comprehensive results.

2. Table 4 is missing the inference time for the original VQGAN.

### Questions
The metrics section of the paper mentions the use of FID; however, it seems that this metric is not included in the comparative analysis of the experimental results.

### Soundness
3

### Presentation
3

### Contribution
3
