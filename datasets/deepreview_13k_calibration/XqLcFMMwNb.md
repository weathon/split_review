# MM-LDM: Multi-Modal Latent Diffusion Model for Sounding Video Generation

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 8, 5, 5

## Abstract
Sounding Video Generation (SVG) is an audio-video joint generation task challenged by high-dimensional signal spaces, distinct data formats, and different patterns of content information.} for the SVG task.
We first unify the representation of audio and video data by converting them into a single or a couple of images. 
Then, we introduce a hierarchical multi-modal autoencoder that constructs a low-level perceptual latent space for each modality and a shared high-level semantic feature space. 
The former space is perceptually equivalent to the raw signal space of each modality but drastically reduces signal dimensions. 
The latter space serves to bridge the information gap between modalities and provides more insightful cross-modal guidance.
Our proposed method achieves new state-of-the-art results with significant quality and efficiency gains.
Specifically, our method achieves a comprehensive improvement on all evaluation metrics and a faster training and sampling speed on Landscape and AIST++ datasets.
Moreover, we explore its performance on open-domain sounding video generation, long sounding video generation, audio continuation, video continuation, and conditional single-modal generation tasks for a comprehensive evaluation, where our MM-LDM demonstrates exciting adaptability and generalization ability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The present paper proposes a framework based on the latent diffusion model to address the challenge of audio-visual joint generation. In comparison to the baseline (MM-Diffusion), the generation scheme proposed in this article, which operates in the latent space, offers significantly enhanced accuracy and reduces the computational burden. Moreover, the application of contrastive loss is also more judicious than in previous methods.
However, the author's writing exhibits some instances of ambiguity, which may suggest a lack of thorough understanding of the latent diffusion model. While the article's motivation and approach are commendable, I suggest that the author consider further revision and refinement of the manuscript before submitting it to the next conference.

### Strengths
1. The application of diffusion in latent space has been demonstrated in the fields of image and video generation, thereby warranting its extension to multi-modal generation. This approach to model generation is highly relevant in the current context of machine learning and artificial intelligence, where multi-modal data is increasingly prevalent. By leveraging the power of diffusion in latent space, multi-modal models can be developed that can generate diverse outputs across various modalities. This approach offers significant benefits in terms of model robustness, scalability, and generalization, making it an attractive choice for businesses and academic researchers alike.

2. The present study's results exhibit substantial enhancements from both qualitative and quantitative perspectives. The research outcomes demonstrate a significant improvement in both the quality and quantity of the study's output.

3. The proposed module in this article has been validated through extensive ablation experiments. The results of these experiments indicate the module's efficacy in addressing the intended objectives.

### Weaknesses
1. I think the author's understanding of latent diffusion is not deep enough, and there are many unprofessional and unscientific descriptions in the writing process. For details, see Questions 1, 2 and 4.

2. The sign of equation (7) is confusing. According to the paper, $(n_a^t,n_v^t)$ are predicted noise features. But obviously this variable is not a predicted value, but a variable that satisfies the N(0,1) distribution.

3. The Implementation Details only give the training details of the multi-modal autoencoder, but not the training details of the diffusion model. Or is it that the model in this paper does not need to first train an autoencoder and then perform diffusion training, like [1]?

### Questions
1. "we can leverage pre-trained image diffusion models to be our signal decoders". How is this step implemented? Are the "signal decoders" used here the diffusion unet in the image diffusion model? I don't understand how image diffusion model can act as decoder in autoencoder.

2. What is the relationship between the content drawn in Figure 3(b) and T? Why does the multi-modal autoencoder perform a denoising process?

3. In contrastive loss, how are positive and negative samples constructed, and how to define "matched pairs" during the implementation process?

4. "we utilize the ϵ-prediction to optimize our signal decoder, which involves the noise mean square error loss". What is the relationship between the process of training autoencoder and the method of noise prediction?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the author studies the problem of sounding video generation (SVG) and proposes a novel multi-modality video generation model in latent space named MM-LDM. The idea of incorporating the latent diffusion model and SVG task is interesting and the overall result is promising.

### Strengths
1. The idea of modeling audio and video in latent space for sounding video generation is interesting and promising.
2. The writing is good and the results further demonstrate the effectiveness of the proposed method.

### Weaknesses
1. Similar ideas to the conditional generation section have been proposed in many papers which seems too weak to list as a technical contribution in the paper. I would like the author to claim this point as a "bonus" of the proposed model in the paper.
2. The visual quality of MM-Diffusion results in Fig. 4 seems quite different from their original paper even considering the result has been super-resolved by the SR model. Is there any explanation for that? The visual quality of the results seems to be in low resolution or processed by some simple SR methods like nearest-neighbor.

### Questions
Please refer to the weakness part.

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
This paper introduces the Multi-Modal Latent Diffusion Model (MM-LDM) for Sounding Video Generation (SVG). The main contributions of this paper are two-fold:
1. MM-LDM establishes audio and video latent spaces for SVG, which significantly reduces computational complexity.
2. MM-LDM proposes a multi-modal autoencoder to compress video and audio signals from pixel space to a semantically shared latent space.
The proposed method achieves state-of-the-art results, demonstrating its effectiveness.

### Strengths
1. The authors attempt to solve a novel and valuable problem and design a reasonable framework for this purpose.
2. The multimodal VAE designed by the author is interesting, establishing semantic latent spaces for audio and video modalities. Further, the authors use a shared multimodal decoder introduced in cross-modal alignment, which can inspire future multimodal generation.
3. The experimental results are promising in metrics, demonstrating the effectiveness of the proposed method. In particular, the MM-LDM achieves state-of-the-art results.

### Weaknesses
1. The designing of a multimodal VAE is innovative, but it may not be as effective as that of two separate VAEs. The authors should compare their multimodal VAE with most direct audio and video VAEs, which would better demonstrate the effectiveness of multimodal VAE. Specifically, a comparison should be made against independently trained VAEs for each modality, ensuring that the latent space dimensionality and decoder architectures are consistent across all compared models to isolate the effect of the shared latent space. It's also important to analyze the reconstruction quality of each modality separately when using the multimodal VAE to understand if one modality is being favored over the other in the shared latent space.

2. I have viewed the generated results provided by the author, and only some results from the AIST++ dataset are available (MM-LDM: Multi-Modal Latent Diffusion Model for Sounding Video Generation (anonymouss765.github.io). However, the movements of the video characters are not natural, and due to the similarity of the generated audio, it is not clear whether the two modalities are in temporal alignment. Although the author has demonstrated significant success in metrics for their proposed method, it is necessary to supplement a human evaluation with MM-Diffusion to enhance credibility. This evaluation should include metrics for both visual quality and audio-visual synchrony, perhaps using a Likert scale to assess the naturalness of the motion and the perceived alignment of audio and video.

3. The paper only does experiments on small datasets, and there may be serious overfitting problems for diffusion-based methods. The author should discuss the generalization of their method on larger datasets. It is crucial to evaluate the model's performance on datasets with greater diversity in terms of content and style. For example, testing on datasets with more varied actions, environments, and audio characteristics would provide a more robust assessment of the method's generalization capabilities. The authors should also consider reporting the performance on a held-out test set to demonstrate the model's ability to generalize beyond the training data.

### Questions
1. In Table 2, parts “Multi-Modal Generative Models on Audio-to-Video Generation” and “Multi-Modal Generative Models on Video-to-Audio Generation”, the results of MM-Diffusion don’t take the other modality as a condition input.
2. There is a typo in the heading of Table 3. “Latent Average Poolong” should be “Latent Average Pooling”.
3. On page 5, in the section “Signal Decoding”, the authors state that they initialize their signal decoder with parameters of a pre-trained image diffusion model to reduce training time and enhance the quality of reconstruction. It is confusing to initialize the decoder with a diffusion model as they are for different objectives. I wonder if this initialization has positive benefits.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a multi-modal latent diffusion model named SVG for audio and video generation. Both audio and video signals are into latent spaces and then learn joint semantic features via classification and contrastive loss. The resulting semantic features can be used as conditional signals to improve audio-to-video and video-to-audio generation. The experiments were conducted on two sounding video datasets and the quantitative results are better than the baselines.

### Strengths
1) Audio-visual cross-modal generation is a challenging task. The authors proposed a promising approach to bridge the gap between audio and video efficiently.
2) The quality of the generated samples looks good to me.
3) The paper is easy to understand.

### Weaknesses
1) The paper is more like a straightforward follow-up on MM-Diffusion. The major difference is changing the diffusion targets from the raw signal domains to the latent spaces. However, based on the literature, it is almost trivial or obvious that transferring to latent space could achieve better results and improve training efficiency in any diffusion generation. From this perspective, the technical novelty of this paper is limited.
2) The datasets used in the paper are pretty limited. The AIST and Landscape are small-size datasets. The proposed method could overfit the dataset, and indeed, diffusion is really good at overfitting. While the authors mentioned that they have not yet extended the method to open-domain sounding video datasets, I believe that is actually the critical research problem required to solve.
3) While the quality of the generated samples on the webpage is nice for 1 second, I believe it is quite limited and probably hard to generalize for a longer time.
4) In addition to quantitative metrics, I believe it is quite important to have a subjective evaluation of the generated samples, especially for audio.

### Questions
1) Have you tried doing applications on audio-visual continuation? For example, the model is conditioned on the first 1s audio, and then you can generate the next 1s audio and visual together. Based on your approach, it seems like these applications are also feasible.
2) There exist so many losses and learnable embeddings within the audio-visual autoencoder. How do you search those weights of different losses? While there are ablation studies, it is only in one direction. I am interested in how you eventually could find the best combinations of all terms.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
