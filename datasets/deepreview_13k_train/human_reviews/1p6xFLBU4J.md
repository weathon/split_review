# GenSE: Generative Speech Enhancement via Language Models using Hierarchical Modeling

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Semantic information refers to the meaning conveyed through words, phrases, and contextual relationships within a given linguistic structure. Humans can leverage semantic information, such as familiar linguistic patterns and contextual cues, to reconstruct incomplete or masked speech signals in noisy environments. However, existing speech enhancement (SE) approaches often overlook the rich semantic information embedded in speech, which is crucial for improving intelligibility, speaker consistency, and overall quality of enhanced speech signals. To enrich the SE model with semantic information, we employ language models as an efficient semantic learner and propose a comprehensive framework tailored for language model-based speech enhancement, called GenSE. Specifically, we approach SE as a conditional language modeling task rather than a continuous signal regression problem defined in existing works. This is achieved by tokenizing speech signals into semantic tokens using a pre-trained self-supervised model and into acoustic tokens using a custom-designed single-quantizer neural codec model. To improve the stability of language model predictions, we propose a hierarchical modeling method that decouples the generation of clean semantic tokens and clean acoustic tokens into two distinct stages. Moreover, we introduce a token chain prompting mechanism during the acoustic token generation stage to ensure timbre consistency throughout the speech enhancement process. Experimental results on benchmark datasets demonstrate that our proposed approach outperforms state-of-the-art SE systems in terms of speech quality and generalization capability. Codes and demos are publicly available at https://anonymous.4open.science/w/gen-se-7F52/.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
- This paper introduces a language model-based generative speech enhancement system, termed GenSE.
- The system comprises two primary components: a decoder-only model that enhances noisy tokens into clean tokens, and a neural speech codec, SimCodec, which reconstructs waveforms from the enhanced clean tokens.

### Strengths
- The paper is clearly written and easy to follow.
- The proposed approach demonstrates the effectiveness of the decoder-only architecture for conventional signal processing tasks, such as speech enhancement (SE).

### Weaknesses
 - The proposed approach lacks significant novelty, which is the primary reason for my decision to reject the paper. However, please correct me if I am mistaken, as I am open to revisiting my assessment.

- Concerning speech enhancement (SE) using language models (or the decoder-only architecture), similar approaches have already been introduced in:

[1] Wang, X., Thakker, M., Chen, Z., Kanda, N., Eskimez, S. E., Chen, S., ... & Yoshioka, T. (2024). Speechx: Neural codec language model as a versatile speech transformer. IEEE/ACM Transactions on Audio, Speech, and Language Processing.  
[2] Yang, D., Tian, J., Tan, X., Huang, R., Liu, S., Chang, X., ... & Meng, H. (2023). Uniaudio: An audio foundation model toward universal audio generation. arXiv preprint arXiv:2310.00704.

Neither of these references are cited.

- Similarly, with regard to the neural speech codec, an analogous method was proposed in:

[3] Li, H., Xue, L., Guo, H., Zhu, X., Lv, Y., Xie, L., ... & Li, Z. (2024). Single-Codec: Single-Codebook Speech Codec towards High-Performance Speech Generation. arXiv preprint arXiv:2406.07422.

This work is also not referenced. Given these omissions, I judge the paper as lacking sufficient originality for acceptance. I believe all referenced works were available prior to the ICLR submission.

### Questions
- The lack of novelty mentioned in the weaknesses section diminishes the overall contribution of this paper. Without a substantially innovative approach, I am inclined to recommend rejection.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents GenSE, a novel generative framework for speech enhancement that leverages language models (LMs) and discrete speech tokens. GenSE employs a single-quantizer neural codec model called SimCodec to extract acoustic tokens from speech, reducing the complexity compared to previous multi-quantizer codecs. It also introduces a hierarchical modeling approach that separates the denoising and generation stages, with a noise-to-semantic (N2S) module transforming noisy speech into clean semantic tokens, and a semantic-to-speech (S2S) module generating clean acoustic tokens.

### Strengths
1. The proposed generative framework leverages language models and discrete speech tokens to outperform state-of-the-art speech enhancement systems in terms of speech quality and generalization capability.
2. The paper introduces a hierarchical modeling approach that separates the denoising and generation stages, improving the stability and performance of the LM-based generation process.
3. The paper is clearly written and easy to follow.

### Weaknesses
The ablation studies are relatively insufficient. For example, it would be helpful to provide detailed analysis on what information are contained in noisy/clean semantic tokens and noisy/clean acoustic tokens, respectively.

### Questions
Could you provide a comparison between SimCodec and Vocos (Siuzdak, 2023) and WavTokenizer(Ji, 2024)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces GenSE, a generative speech enhancement (SE) framework that integrates language models (LM) to leverage semantic information for enhancing speech signals. Unlike traditional SE methods that focus on signal mapping, GenSE treats SE as a conditional language modeling task. By tokenizing speech into semantic and acoustic tokens using a novel codec (SimCodec) and employing a hierarchical approach, GenSE aims to maintain speaker consistency and improve speech quality under noisy conditions. Experiments demonstrate GenSE’s significant improvements over state-of-the-art SE systems in both quality and robustness to noise.

### Strengths
1. GenSE offers a unique perspective by reframing SE as a language modeling task, using semantic information to enhance robustness. This represents a notable departure from conventional deterministic mapping in SE.
2. The hierarchical modeling method, separating semantic and acoustic token generation, improves both quality and intelligibility of enhanced speech, as evidenced by superior metrics across DNSMOS and SECS.
3. The authors present a detailed breakdown of the methodology and technical architecture, providing clear diagrams and tables that make complex processes accessible.
4. By addressing the limitations of traditional SE approaches in handling complex noise environments, GenSE has the potential to impact real-world applications in noisy and challenging acoustic settings.

### Weaknesses
1. The hierarchical design and multiple components in GenSE, while effective, may pose a challenge in real-time applications. The sequential nature of semantic and acoustic token generation, where semantic tokens are generated first, followed by acoustic tokens, introduces latency. This two-stage process, especially with the complex models involved, could limit its applicability in scenarios requiring immediate feedback. Simplifying or optimizing these processes further could improve usability.

2. Although SimCodec effectively reduces token count, further exploration into balancing token complexity and quality in low-bandwidth scenarios could enhance GenSE’s adaptability. The current implementation focuses on a specific trade-off between token rate and reconstruction quality, but a more detailed analysis of how different compression levels affect the performance of the downstream speech enhancement task is needed. This includes investigating the impact of varying codebook sizes and token generation frequencies on both the quality and intelligibility of the enhanced speech, especially in very low-bandwidth conditions.

3. The two-stage quantizer reorganization might benefit from more empirical comparisons with other single-quantizer methods such as WavTokenizer, as these details are relatively underexplored. While the paper presents results using SimCodec, a more comprehensive comparison with other established tokenization methods is necessary to fully validate its effectiveness. This comparison should include a detailed analysis of the trade-offs between token rate, reconstruction quality, and computational cost for different quantization strategies.

### Questions
1. Could the authors provide more insight into how SimCodec might perform under different network conditions, especially with low latency or limited bandwidth?
2. How does the system handle speaker identity in cases of domain shifts, such as across different languages, accents, and ages, and would an alternative to XLSR affect GenSE’s generalization capability?
3. For practical implementation, are there considerations for reducing the computational overhead of the hierarchical modeling method, perhaps through model pruning or compression techniques?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a novel approach to speech enhancement (SE) called GenSE, which integrates semantic information into the enhancement process using language models (LMs). Traditional SE methods often ignore the semantic context, focusing solely on mapping noisy to clean speech, which can lead to performance issues in challenging environments. GenSE redefines SE as a conditional language modeling task by leveraging LMs to predict discrete acoustic tokens based on semantic information. It also separates the denoising and generation stages, improving prediction stability and incorporating a token chain prompting mechanism to maintain timbre consistency. The proposed SimCodec Model achieves remarkable reconstruction quality at a lower bit rate. Experimental results show that GenSE outperforms existing SE systems, demonstrating improved intelligibility and robustness in noisy conditions.

### Strengths
1. The proposed hierarchical modeling method that separates the denoising and generation stages is effective.
2. The proposed SimCodec reduces the number of tokens in the generation process, which would benefit all speech generation tasks.
3. The experimental results and demo audios are promising.

### Weaknesses
 **The main issues with this paper lie in the design of SimCodec and the lack of some experimental details:**   
*SimCodec*:
1. The issue of low codebook usage with a large codebook size has been identified in the field of computer vision for a long time, and there are already many solutions available [1, 2]. Although this work proposes the codebook reorganization strategy to solve this issue, there are no ablation comparisons between this strategy and baselines like CVQ [2] and FSQ [3]. These comparisons are important for validating the effectiveness of the reorganization strategy proposed in this paper.  
2. The codebook reorganization strategy employs two quantizers at the first stage and concat the two quantizers at the second stage. This process is slightly similar to the GRVQ technique of Hifi-Codec [4] and the multichannel quantization of MoVQ [5]. I think the comparative experimental results of these two techniques should be added to Table 3. And the authors should discuss how their approach differs from or improves upon GRVQ and MoVQ.  
3. I think Figure 6 looks extremely similar to Figure 1 in WavTokenizer [8], even the colors of the baselines are the same. However, this paper does not compare with WavTokenizer. An explanation why WavTokenizer was not included in the comparison and how their work differs from or builds upon WavTokenizer is required, or 2) Include WavTokenizer as a relevant baseline.  

*Some experimental details*:
1. Real-time generation is crucial for speech enhancement models, but the experiments of this paper do not mention the real-time factor (RTF) of the GenSE model. While Table 4 demonstrates that token chain prompting and hierarchical modeling are highly effective, it also does not indicate how much delay these methods introduce.
2. In Section 3.3.2, the prefix token of GenSE at the S2S stage contains noisy acoustic tokens, clean semantic tokens, and noisy semantic tokens, which significantly increase the sequence length in training and inference. This paper lacks a specific analysis of the trade-offs between performance gains and computational costs of the introduced prefix sequence.  
3. Mapping from semantic to acoustic using a flow-matching model has proven to be highly effective in many previous studies [6, 7].  The authors could explain why they chose their current approach instead of a flow-matching model for the S2S module, discussing potential advantages and disadvantages. Alternatively, they might consider implementing a flow-matching model as an additional baseline in their experiments to compare its performance with their current method.  

**Minor questions that would not influence the scores:**
1. Do you use greedy decoding for decoder LM? Will beam search improve the performance of the model?  

**Minor clarity issues**:
1. In Section 3.2.3, Line 264, ``we reinitialize the encoder and decoder parameters to fit the new codebook dimension, while copying the parameters from the first stage``, the use of "reinitialize" in the first half of the sentence introduces clarity issues;
2. In Section 3.3.1, Line 293, ``Meanwhile, the self-supervised model is also noise-robust to some extent.`` Some citations can be added here to demonstrate that this phenomenon actually exists.

**Minor typos**:  
1. In Section 1, Line 052, the quotes of ``textless NLP``;
2. In Figure 6, `Our` -> `Ours`.

**Conclusion**:  
The SimCodec and hierarchical modeling method proposed in this paper are not particularly novel, as there have been related studies in fields such as Computer Vision and Speech Generation. However, the experimental results are still quite impressive. If the authors could address my concerns, I would increase the score.

### Questions
My questions are included in the weaknesses part.

### Soundness
2

### Presentation
3

### Contribution
3
