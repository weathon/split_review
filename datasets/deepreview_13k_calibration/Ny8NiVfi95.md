# Masked Audio Generation using a Single Non-Autoregressive Transformer

- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 8, 8

## Abstract
We introduce \method, a masked generative sequence modeling method that operates directly over several streams of audio tokens. Unlike prior work, \method is comprised of a single-stage, non-autoregressive transformer. During training, we predict spans of masked tokens obtained from a masking scheduler, while during inference we gradually construct the output sequence using several decoding steps. To further enhance the quality of the generated audio, we introduce a novel rescoring method in which, we leverage an external pre-trained model to rescore and rank predictions from \method, which will be then used for later decoding steps. Lastly, we explore a hybrid version of \method, in which we fuse between autoregressive and non-autoregressive models to generate the first few seconds in an autoregressive manner while the rest of the sequence is being decoded in parallel. We demonstrate the efficiency of \method for the task of text-to-music and text-to-audio generation and conduct an extensive empirical evaluation, considering both objective metrics and human studies. The proposed approach is comparable to the evaluated baselines, while being significantly faster (x$7$ faster than the autoregressive baseline). Through ablation studies and analysis, we shed light on the importance of each of the components comprising \method, together with pointing to the trade-offs between autoregressive and non-autoregressive modeling, considering latency, throughput, and generation quality. Samples are available on our demo page \url{https://pages.cs.huji.ac.il/adiyoss-lab/MAGNeT}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the author proposed MAGNET, a masked discrete generative model on top of RQV representations (EnCodec), able to perform audio generation at a faster inference speed than other baselines while reaching the same generation quality. To improve their model, the authors propose a list of techniques: 1. a masking strategy where instead of masking tokens, spans of tokens are masked, given that neighboring tokens are inter-dependent temporally paired with a restricted context on the self-attention for codes greater than one (given the convolutional nature of EnCodec and the limited receptive field of its LSTM in practice) 2. a re-scoring strategy at inference time, where the probability to mask a span is given by an external audio model (e.g., MUSICGEN and AudioGen) 3. an annealer for the classifier free guidance embedding strength. Additionally, the authors experiment with a hybrid model trained both with autoregression and masking. The resulting model results 10 times faster than the autoregressive baseline when using low batch sizes.

### Strengths
- The proposed masking strategy, which uses token spans instead of individual tokens, is an important methodological contribution of the paper since it greatly impacts the performance of the proposed model.
- The 10x speedup in latency is remarkable, especially in a setting like music, where it is required to sample many tokens, given the long context.

### Weaknesses
 - A problem with the work is related to the title and the overall tone, in which the authors claim proposing a new type of audio/music model. In a paper titled "Masked Audio Generative Modeling," it is supposed that the authors proposed for the first time a masked model for audio. Nonetheless, the papers introducing such an idea in audio are SoundStorm (which the authors cite correctly) and VampNet https://arxiv.org/abs/2307.04686 (which the authors should cite as concurrent work). The authors could change the title of the article to better delineate the paper as a set of improvements of such models (providing at least one of the two as baselines).
- Except for the masking strategy, which I find important, the other introduced techniques seem relatively not critical or novel, especially the rescorer model, given that it improves the FAD only marginally.
- The scheduler $\gamma(i; s) = \cos( \pi(i−1)/ 2s )$ is badly defined because computed on $i=1$ returns still $1$.
- I do not understand why the new CFG anneal performs better.
- Can the authors explain why the small 300M model performs better than the 1.5B model? I find this counterintuitive.
- Additionally, can the authors explain better why the restricted context improves the metrics? Intuitively, the only advantage should be training/inference time improvement.

### Questions
- The scheduler $\gamma(i; s) = \cos( \pi(i−1)/ 2s )$ is badly defined because computed on $i=1$ returns still $1$.
- I do not understand why the new CFG anneal performs better.
- Can the authors explain why the small 300M model performs better than the 1.5B model? I find this counterintuitive.
- Additionally, can the authors explain better why the restricted context improves the metrics? Intuitively, the only advantage should be training/inference time improvement.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
MAGNeT constitutes a mask generative modeling approach for conditional audio synthesis, leveraging the neural audio codec (EnCodec) to transform audio waveforms into compressed and discrete sequences. The main contribution lies in transfering the masked generative modeling, as exemplified by MaskGIT in the image domain, to the audio domain. In my opinion, the fact that the methods are shown to be effective in other domains (image, for example) does not necessarily undermine the findings in this work. My assessment therefore is based on completeness and rigor in justification of design choices and experimental details.

### Strengths
The choice of spanned mask prediction training with restricted context for RVQ is well justified both intuitively and through ablation studies. The use of a shifted impulse function for analyzing EnCodec's latent vector is a welcomed addition, especially to better understand the dependency between multi-level RVQ tokens, which will inspire the community to improve the methods to train the codec model and/or the generative model alike.

The accuracy-latency tradeoff analysis for the first-level RVQ token versus the rest is also helpful in designing a better decoding strategy for the RVQ tokens. It is worth mentioning that such dynamics can potentially change when an improved codec model is developed. The analysis methods in MAGNet are generalizable to assess future-generation codec models as well, and will likely become useful tools to design an optimal generative model for the target codec model.

### Weaknesses
The ablation study is satisfactory overall, but I would also like to see quantitative analysis on the proposed annealed classifier-free guidance scale, which seems to be missing in the current manuscript. While intuitive, documenting the performance gain obtained by the method would make the paper more convincing and complete. Specifically, the manuscript should include a table showing the performance of the model with different starting and ending values for the classifier-free guidance scale, and how these values impact the final generation quality. This would provide a more rigorous understanding of the method's sensitivity to this hyperparameter.

Although the manuscript states that the training dataset is the same for several baseline models (Mousai and MusicGen), others (MusicLM and AudioLDM2) are trained on different data. Understanding the challenge in matching the music dataset (and open sourcing the data due to copyright concerns), further clarification on the training dataset for all baseline models via a complete paragraph and/or the table will be beneficial to gain a complete picture in the field of audio/music generative models. The current description lacks the necessary detail to fully assess the comparability of the different models, and a more thorough description of the datasets, including size, composition, and preprocessing steps, is needed to ensure a fair comparison.

### Questions
There have been several concurrent works using a similar approach, including SoundStorm, which is adequately mentioned in the manuscript. I would like to mention another concurrent work, VampNet[1], which applied MaskGIT-like training and a neural audio codec for music generation. While the comparison is not strictly necessary, it would be beneficial for the audience to have a summary of the differences between the models, such as highlighting the spanned mask prediction training and rescoring method of MAGNeT.

[1] Garcia, Hugo Flores, et al. "Vampnet: Music generation via masked acoustic token modeling." arXiv preprint arXiv:2307.04686 (2023).

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The proposed model (MAGNET) is a generative sequence modeling method for discrete audio tokens. It uses a single-stage, non-autoregressive transformer encoder during training to predict masked token spans and gradually constructs the output sequence during inference. The authors further introduce a model rescorer that leverages another pretrained model to rank predictions. A hybrid version combines autoregressive and non-autoregressive models, generating the initial part autoregressively and the rest in parallel. MAGNET operates on a multi-stream audio representation (EnCodec) and uses a single transformer model trained to predict spans of masked input tokens. During inference, it constructs the output audio sequence through multiple decoding steps. The method achieves competitive results in text-to-music and text-to-audio generation, with seven times faster latency compared to autoregressive methods, and offers insights through ablation studies.

### Strengths
The authors of this research paper address the challenging problem of generating long audio and music sequences, a task that has garnered significant attention due to its relevance in various applications, such as text-to-music and text-to-audio generation. Their proposed solution, known as MAGNET (Masked Audio Generation using Non-autoregressive Transformer), introduces several innovative techniques to tackle this problem effectively.

One key feature of MAGNET is its use of a training via masking strategy, a popular approach in contemporary self-supervised learning. This approach is particularly well-suited for the task of audio generation as it helps the model to learn dependencies and patterns in the data by predicting masked segments. In the case of MAGNET, the authors employ span masking, a technique rooted in speech and audio processing, which proves to be more effective than traditional token based masking. Span masking mitigates the issue of information leakage and results in more coherent and high-quality audio generation.

MAGNET's underlying representation is based on EnCodec, which combines full self-attention with smaller attention spans derived from the impulse response characteristics of LSTM blocks. This hybrid approach allows the model to efficiently capture long-range dependencies while preserving local details, contributing to the generation of realistic audio sequences.

A notable innovation in this work is the introduction of model rescoring through MusicGen and AudioGen. This technique enhances the robustness of the model during the sampling process, ensuring that the generated audio maintains high quality and coherence. Additionally, the authors incorporate annealing in the classifier-free guidance parameter, a strategy previously demonstrated to be useful in 3-D shape generation. This further contributes to the model's performance.

The authors conduct a comprehensive evaluation of MAGNET on both text-to-music and text-to-audio generation tasks. They use objective metrics such as FAD, KL Divergence, and CLAP scores to quantitatively assess the model's performance. Subjective metrics, derived from crowd-sourced evaluations and including Mean Opinion Score (MOS) and audio-text relevance assessments, provide a more human-centered perspective on the quality of the generated audio.

To further validate their approach and elucidate the rationale behind their design choices, the authors conduct ablation studies. These studies help in understanding the individual contributions of different components to the overall performance of MAGNET.

Finally, the authors perform a comparison of MAGNET with existing methods, including MusicGen, Mousai, and AudioLDM2, providing a clear understanding of its strengths and weaknesses in comparison to state-of-the-art approaches.

### Weaknesses
The main weakness of this paper is that there is a heavy amount of engineering involved in the development of this model. While, it is definitely commendable, it makes reproducing the result extremely difficult for the rest of research community. Further, authors have not referred to this work titled "Masked Autoencoders that Listen" which has a very similar idea of span masking. It  would have been interesting to see the contrast and comparison against something that is designed with similar idea. Another issue I have with the paper is that the authors do not provide any details about the dataset used for training.

### Questions
NA

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
