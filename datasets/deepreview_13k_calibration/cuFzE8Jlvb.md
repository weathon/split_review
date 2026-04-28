# Continuous Autoregressive Modeling with Stochastic Monotonic Alignment for Speech Synthesis

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
We propose a novel autoregressive modeling approach for speech synthesis, combining a variational autoencoder (VAE) with a multi-modal latent space and an autoregressive model that uses Gaussian Mixture Models (GMM) as the conditional probability distribution. Unlike previous methods that rely on residual vector quantization, our model leverages continuous speech representations from the VAE's latent space, greatly simplifying the training and inference pipelines. We also introduce a stochastic monotonic alignment mechanism to enforce strict monotonic alignments. Our approach significantly outperforms the state-of-the-art autoregressive model VALL-E in both subjective and objective evaluations, achieving these results with only 10.3\% of VALL-E's parameters. This demonstrates the potential of continuous speech language models as a more efficient alternative to existing quantization-based speech language models. Sample audio can be found at \url{https://tinyurl.com/gmm-lm-tts}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel approach to autoregressive speech modeling using continuous speech features, contrast to recent trends that rely on discrete units. The method consists of two key components: (1) A feature extraction model based on VAE, which replaces quantized codebooks (as in RVQ) with a learned mixture of Gaussian priors (GMM-VAE), and (2) A text-to-speech model that employs a Gaussian Mixture Model Language Model (GMM-LM) to model these continuous features in autoregressive manner, which also incorporating a new monotonic alignment constraint. Experimental results demonstrate that this continuous speech modeling consistently outperforms previous methods using discrete codec representations like Residual Vector Quantization (RVQ) in TTS tasks.

### Strengths
- Clear comparison to previous approaches and introduces novel continuous variants for both VAE training and TTS stages
- The introduction of GMM-LM is novel, and the formulation is clear and simple. It also enables probabilistic sampling which is a plus for TTS applications
- Nice results with much less model parameters

### Weaknesses
 - Limited discussion of prior Gaussian mixture VAE work, e.g., "Deep Unsupervised Clustering with Gaussian Mixture Variational Autoencoders". (Minor: The notation, either GMM-VAE or VAE-GMM, should be consistent.)
- The counterintuitive result where increasing Gaussian mixtures in GMM-VAE leads to worse reconstruction, where a 6-mixture GMM should subsume the modeling capacity of a 3-mixture GMM
- Some modeling details are missing, e.g., GMM-VAE frame rate, which is crucial as it could affect the type of information captured

### Questions
- Does the frame rate of GMM-VAE features align with the mel spectrogram hop length (240ms) described in 5.2?
- Why does the model require relatively few Gaussian mixtures compared to VQ codes in RVQ, and any insights on what the mixture components capture?
- Could you clarify how the monotonic alignment mechanism in Figure 2 (right) works? It seems to align the encoded text and speech prompts prior to decoding. Additionally, a more comprehensive description of the GMM-LM would be nice, including how speech and text features are fed into each decoder step, and the formulation of $e_{i,j}$​.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
Authors propose a novel means of auto-regressive TTS modeling that eschews quantization units in favor of Gaussian mixtures. Model performance consistently outperforms other standard TTS models, demonstrating high quality TTS is able without traditional VQ-VAE setup.

### Strengths
Authors present provide a thorough discussion of related work and their motivation for their approach. Description of architecture is clear and easy to follow, along with pointers for reproducibility. High performance of model is significant enough for comparison with other approaches.

### Weaknesses
There is a minor question of motivation in the author's approach: they take the stance that the community views vector quantization approaches as a necessity, but there are a fair amount of approaches in the speech modeling community that have used straight reconstruction approaches. While their gaussian mixture approach is still suitably novel, this position seems to ignore other considerations that go into VQ approach. Notably that the use of discrete tokens is relatively easy to implement in parallel with text encoding, all while minimizing storage an I/O limitations from audio/image processing.

### Questions
Given the reliance of the model architecture on monte-carlo estimation, how sensitive are results to random seeding during expeirmentation?

What is the performance on more noisy datasets than LibriSpeech? Is the Gaussian approach suitably robust across evaluation sets?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper applies a VAE with GMM before extracting latent representations, and then trains an autoregressive model on the extracted continuous latent. The approach models the autoregressive conditional distribution also by GMM.

### Strengths
The idea of using GMM-VAE to regularize the latent distribution, serving a similar role as discretization is novel and interesting. The method is also easy to understand and straightforward. The paper can also inspire research on the use of continuous variational approaches in the speech synthesis domain, which has been recently dominated by discrete-based approaches.

### Weaknesses
To me, the main issue of the paper is that the contribution of monotonic alignment and GMM-VAE are not separated. Specifically, the paper claims that "Despite its smaller size, our model achieves lower WER and higher MOS than VALL-E, thanks to the continuous autoregressive modeling approach." in lines 82-83. However, in experiments of Section 5, you are comparing your method with monotonic alignment v.s. existing methods that do not enforce monotonic alignment. Some studies have shown that enforcing monotonic attention patterns can lead to much lower WER and even better naturalness. This makes me question if the lower WER and higher MOS come primarily from the use of monotonic alignment, which is not the main novelty of the paper, rather than from the use of GMM-VAE and GMM-LM. Furthermore, while the authors do provide a comparison of alignment methods in Appendix A.1, the one without monotonic alignment (Cross Att.) does result in higher WER than all the baselines. This further substantiates that the performance increase may not come from GMM-VAE and GMM-LM. I would suggest the author do an ablation study on the monotonic alignment and add it to Table 2 to interleave the contributions of the two components.

Section 3.3 is a little bit unclear. For instance, how was this energy function $e_{ij}$ calculated? Does it have something to do with the cross-attention weights acquired by the transformer?

What are the specs for the baseline methods: StyleTTS-2 and HierSpeech++? Are they of similar parameter size?

I am wondering the validity of modeling the autoregressive distribution as a GMM. In your case, even if the KL regularization loss of GMM-VAE makes $q(h|x)$ a mixture of Gaussians, does it in any sense implies that the autoregressive conditional distribution $p(h_t|h_{t-1}, \cdots)$ is also close to a Gaussian mixture?

### Questions
- Section 3.3 is a little bit unclear. For instance, how was this energy function $e_{ij}$ calculated? Does it have something to do with the cross-attention weights acquired by the transformer?
- What are the specs for the baseline methods: StyleTTS-2 and HierSpeech++? Are they of similar parameter size?
- I am wondering the validity of modeling the autoregressive distribution as a GMM. In your case, even if the KL regularization loss of GMM-VAE makes $q(h|x)$ a mixture of Gaussians, does it in any sense implies that the autoregressive conditional distribution $p(h_t|h_{t-1}, \cdots)$ is also close to a Gaussian mixture?

The paper is well-written and interesting, but I think the experiment issue mentioned in Weaknesses should be addressed before the paper is ready to be published.

### Soundness
3

### Presentation
3

### Contribution
3
