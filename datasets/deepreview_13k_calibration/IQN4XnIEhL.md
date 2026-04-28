# A Variational Approach for Generative Speech Language Modeling

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 8, 3, 6

## Abstract
The success of large language models in text processing has inspired their adaptation to speech modeling. However, because speech is continuous and complex, it is often discretized into tokens derived from self-supervised speech models. These speech tokens typically focus on the linguistic aspects of speech and neglect its paralinguistic content. As a result, autoregressive models trained on these tokens may generate speech with suboptimal naturalness. Previous methods attempted to address this limitation by adding pitch features to speech tokens prior to autoregressive modeling. However, pitch alone cannot fully represent the range of paralinguistic attributes, and selecting the right features requires careful hand-engineering. To tackle this issue, we propose a variational approach that automatically learns to encode these continuous speech attributes to enhance the speech tokens. Our proposed approach eliminates the need for manual paralinguistic feature selection and extraction. Moreover, we demonstrate that our proposed approach maintains or improves speech language modeling performance and enhances the naturalness of generated speech compared to baseline approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a variational approach that automatically learns to encode these continuous speech attributes to enhance the speech tokens, and eliminates the need for manual paralinguistic feature selection and extraction, such as pitch features.

### Strengths
1. Employing an encoder to derive continuous features instead of manually crafted paralinguistic features endows the features with greater flexibility and potency.
2. The symbols and formulas within the paper are clearly defined, and comprehensive details, encompassing mathematical derivations and experimental setups, are thoroughly documented in the Appendix.
3. Various advanced technologies are used to enhance the model, such as time-wise normalizing flow, and diffusion decoder (However, the ablation studies are not reported in the paper).

### Weaknesses
1. In section 3.2, it is mentioned that "By using these tokens, the model no longer needs to encode as much phonetic information in Z^c, allowing Z^c to focus on other continuous speech attributes. ". To strengthen this argument, it would be more convincing to include some analytical experiments. For instance, demonstrating that Z^c excels in speaker verification or emotion recognition, but performs less effectively in speech recognition, would provide a more nuanced understanding of its capabilities.
2. The descriptions of the evaluation are unclear. The authors should provide a clear explanation of whether the AR model is utilized for each metric, possibly by referring to section 3.1 of the GSLM paper.
3. In the main results, the conclusion, "Speech generated from our proposed approach does not sacrifice meaningfulness compared to speech generated from the baselines.", is not strongly supported by the experiments, particularly when considering the observed declines in sWUGGY and sBLIMP. Despite the authors' speculations, the empirical data does not robustly corroborate this claim. The subjective M-MOS scores are not sufficiently strong to overcome the objective sWUGGY and sBLIMP score decreases.
4. it is very weird that the sWUGGY of (Token + continues features) is worse than that of both Token-LM or continues features-LM. (Proposed vs. Token-LM, Proposed vs. Proposed - tokens, in Table 3). This suggests a potential issue with how the combined features are being utilized or that the model is not effectively leveraging the additional information.

### Questions
1. What is the CER of the ground-truth, which serves as the upper bound for the ASR model?
2. When utilizing discrete tokens enriched with acoustic information, such as Encodec, can the proposed method yield enhancements?
3. Why does the Token-LM trained on the LibriSpeech dataset exhibit significantly better CER compared to the Token-LM trained on the Libri-light dataset (5.40 vs. 10.19), yet this improvement is not obtained in the proposed method (5.06 vs. 4.35)?
4. why the numbers of γ=0.5 in Table 4 can not be found in Table 3?
5. why the β is set to 0.04 instead of 0.03 in Table 4?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper describes an approach to improve speech LM modeling in a speech sequence completion task.  The central idea is to augment the speech tokens with an additional autoregressive variational input.  This results in improved naturalness and meaningfulness of the responses compared to a baseline and a speech-token + pitch representation.

### Strengths
The proposal is well motivated, and builds on prior work on speech representation and variational modeling speech generation.

The results are generally quite strong.  The subjective evals show clear improvements to both meaningfulness and naturalness.  The only regressions are to sWUGGY and sBLIMP objective measures.

While the approach adds overall complexity to the inference call, the number of parameters added appear to be quite low -- only 2M additional params.

### Weaknesses
It would be useful to have some confidence measure for the sWUGGY, sBLIMP and Perplexity values.  It is unclear how much the 61.75 -> 60.48 sWUGGY regression means.  Is this statistical noise, or an issue that should be addressed.

While the variational augmentation adds fewer than 1% of parameters, it would be useful to know if this meaningfully adds to inference latency.

### Questions
See above -- it would help understand the approach more completely to have an understanding of any latency implications to this model adjustment.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes learning para-linguistic information within a VAE framework by incorporating semantic information from a speech language model. However, there are issues with both the learning objective formulation and the experimental results.

1. The core idea is to learn an autoregressive prior through VAE training. This approach differs from VQ-VAE, where the prior is learned separately after training. However, the authors use the intermediate features directly to train \(\phi\) and then expect \(\phi\) to generate \(z_t^{c}\) for computing divergence. This does not achieve the traditional effect of KL divergence in regularizing the latent space. Furthermore, it diverges from standard approaches where the prior is parameterized independently from the latent features. Effectively, this approach is equivalent to learning the prior after training, which undermines the formulation's purpose.

2. Conditioning on semantic information to learn para-linguistic features is not new and has already been investigated in works like [1]. Additionally, the audio samples presented by the authors are audibly poor and notably worse than those produced by speech synthesis methods that directly utilize pitch features, as demonstrated in [2]. Furthermore, unlike most recent studies, the authors did not provide a web interface for easy access to samples, which makes evaluation cumbersome. If MOS evaluations were already conducted, it would be beneficial for reviewers to have a similar interface for sample evaluation.

References:  
[1] Zhang, Xin, et al. "Speechtokenizer: Unified speech tokenizer for speech large language models." arXiv preprint arXiv:2308.16692 (2023).  
[2] Polyak, Adam, et al. "Speech resynthesis from discrete disentangled self-supervised representations." arXiv preprint arXiv:2104.00355 (2021).

### Strengths
Nothing particularly strong.

### Weaknesses
1. The core idea is to learn an autoregressive prior through VAE training. This approach differs from VQ-VAE, where the prior is learned separately after training. However, the authors use the intermediate features directly to train \(\phi\) and then expect \(\phi\) to generate \(z_t^{c}\) for computing divergence. This does not achieve the traditional effect of KL divergence in regularizing the latent space. Furthermore, it diverges from standard approaches where the prior is parameterized independently from the latent features. Effectively, this approach is equivalent to learning the prior after training, which undermines the formulation's purpose. The core issue is that the prior is conditioned on the latent features themselves, creating a circular dependency. The KL divergence, in this case, does not enforce a meaningful prior distribution independent of the encoder's output. This fundamentally alters the role of the KL divergence from a regularizer to a fitting term, which is not the intended use in a VAE framework.

2. Conditioning on semantic information to learn para-linguistic features is not new and has already been investigated in works like [1]. Additionally, the audio samples presented by the authors are audibly poor and notably worse than those produced by speech synthesis methods that directly utilize pitch features, as demonstrated in [2]. Furthermore, unlike most recent studies, the authors did not provide a web interface for easy access to samples, which makes evaluation cumbersome. If MOS evaluations were already conducted, it would be beneficial for reviewers to have a similar interface for sample evaluation.

### Questions
Why no demo page? Have you try train the AR prior post training?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a variational approach to speech-language modelling in contrast to traditional auto-regressive models. The aim is to capture information other than semantics.

### Strengths
1. Using the variational method for speech-language modelling is novel and useful. The exploration is very interesting and I like the idea.
2. The paper is well-written with adequate derivations for key loss functions.

### Weaknesses
1. My main concern is how this method is useful for more practical downstream tasks such as ASR, emotion or speaker recognition, to reflect that capturing the additional (mainly paralinguistic) information is useful. I strongly encourage the authors to conduct at least 2 of the above practical tasks using the variational speech LM and compare it to token-based speech LM to see if there are any potential benefits of using variational methods.
2. Experimental is conducted using LibriSpeech and Libri-light, which are datasets with quite small variabilities other than semantic information. I believe the variability remains in the speaker representation space, which is not explicitly reflected in the experimental design.

Together with the question below, I am not convinced that this paper has acceptance quality at the moment. However, given the idea is interesting, I would like to see how the authors would improve the paper during the rebuttal period, and promise to raise my score if my concerns are addressed.

### Questions
1. Why do we need to separate z^c and z^d? Are they really independent? I believe knowing z^c will tell you a lot about z^d, right? The authors are encouraged to explain this design choice further.

### Soundness
3

### Presentation
3

### Contribution
2
