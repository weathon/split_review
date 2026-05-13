# SummaryMixing: A Linear-Complexity Alternative to Self-Attention for Speech Recognition and Understanding

- Decision: Reject
- Scores: 3, 8, 6, 5

## Abstract
Modern speech processing systems rely on self-attention.
Unfortunately, token mixing with self-attention takes quadratic time in the length of the speech utterance, slowing down inference and training and increasing memory consumption.
Cheaper alternatives to self-attention for ASR have been developed, but they fail to consistently reach the same level of accuracy.
This paper, therefore, proposes a novel linear-time alternative to self-attention.
It summarises an utterance with the mean over vectors for all time steps.
This single summary is then combined with time-specific information.
We call this method ``SummaryMixing''.
Introducing SummaryMixing in state-of-the-art ASR models makes it feasible to preserve or exceed previous speech recognition performance while making training and inference up to 28\,\% faster and reducing memory use by half.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a novel neural network architecture called SummaryMixing for speech recognition. The motivation of this work is to replace the heavy computational cost yielded by transformer self-attention blocks with a SummaryMixing block on top of the branchformer architecture. SummaryMixing shows effectiveness by offering a competitive performance from the original branchformer architecture, especially with the low computational cost, mainly within the CTC framework.

### Strengths
- Simple and yet another neural network architecture by extending the branchformer architecture to capture global characteristics via SummaryMixing and local characteristics via cgMLP.
- Showing the low computational cost compared with the original branchformer
- Good reproducibility (open source implementation and the use of public data).

### Weaknesses
 - The survey of the efficient transformer (conformed) is not sufficient. There are a lot of efficient transformers in the NLP and ML field (e.g., https://arxiv.org/pdf/2009.06732.pdf). Even if we limit the discussions to speech applications, there are a lot of methods (e.g., squeezeformer, efficient conformer, emformer, etc.). Specifically, the paper lacks a detailed comparison with methods that explicitly aim to reduce computational cost while maintaining performance, such as those employing low-rank approximations or kernel methods within the attention mechanism. The current survey does not adequately cover the breadth of techniques available for efficient sequence modeling.
- The performance improvement from the conventional method (e.g., fastformer) is marginal. While the paper demonstrates improvements over Fastformer, the gains are relatively small, especially considering the added complexity of the SummaryMixing block. The improvements need to be more substantial to justify the introduction of a new architecture. It is unclear if the observed gains are statistically significant, and the paper does not provide a detailed analysis of variance or confidence intervals.
- The method is on top of branchformer, which already uses Fastformer, and its technical novelty is weak. The core idea of using a summary mixing block is not entirely novel, and the application on top of branchformer does not represent a significant leap in terms of architectural innovation. The paper does not clearly articulate how SummaryMixing differs fundamentally from other similar approaches, such as those based on global pooling or other forms of feature aggregation.
- Several descriptions (e.g., the surveys, distinction from HyperMixer/MLP Mixer, and detailed architectures) are unclear.
  - Frankly, I could not understand the distinction of the SummaryMixing block from HyperMixer/MLP Mixer only from Section 2.1, mainly due to the lack of an explanation of what HyperMixer/MLP Mixer is. The paper needs to provide a clear explanation of the HyperMixer/MLP Mixer architectures, including their key components and operational mechanisms, to allow for a meaningful comparison with the proposed SummaryMixing approach. Without this, the reader cannot fully assess the novelty of the proposed method.
  - It is difficult to understand the detailed architectures only from this description: "In particular, the transformation (f), summary (s), and combiner (c) functions are all implemented as a dense linear layer followed by a GeLU activation function." Similarly, how the model size of the proposed and other methods is adjusted was unclear. The paper should provide a more detailed description of the specific parameters used in the linear layers, the number of hidden units, and how these parameters are adjusted to maintain a comparable model size across different architectures. A clear explanation of the model size adjustment is crucial for a fair comparison.

### Questions
- Can you expand the discussion of how this novel architecture and findings would attract the general AI and ML researchers in ICLR? This paper specializes in speech recognition (and spoken language understanding, which is a very similar task to speech recognition), and it is a narrow scope for me.
- Besides the above expansion, can you explain why you selected Fastformermer and ContextNet?
- Can you apply this to RNN-T?

Other minor comments
- Abstract: ASR --> automatic speech recognition (ASR), speech understanding --> spoken language understanding
- Page 3, last paragraph "Hence, $X \in \mathbb{R}$ becomes $X \in \mathbb{R} ^{T \times D/n}$": Is $X \in \mathbb{R}$ scalar? I think you missed adding some domains.

### Soundness
3 good

### Presentation
2 fair

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
The paper proposed a global summarization layer as a replacement for MHSA in several ASR architectures such as branchformer and Conformer. This layer or module is introduced and compared with several parallel implementation in an open source project SpeechBrain. 
The newly proposed component dubbed summaryMixing has a linear computation cost on the encoder ASR components.
Expectation is that this will close the gap with MHSA but actually authors found this surpasses it in their tests.

### Strengths
The paper proposes a generalization of hyperMixer and apply it to Speech tasks. 
The generalization is simple but its effectiveness is surprising. 
The proposed architecture works very well in comparison with many baselines and architectures (Conformer, Branchformer, ContextNet, Branchformer +fastattention, Branchformer w/o attention, ...)
The obtained and reported results are very competitive with various ASR benchmarks and setups.
It is worth noting the surprisingly good performance of one of the simplest baseline, the branchformer w/o attention, which authors acknowledge and highlight.
They consider encoder architecture only to show the unnecessary MHSA complexity for ASR tasks is not coming exclusively from the top decoder..

### Weaknesses
There is a couple of points where the newly proposed component experimentation could have been improved.
The authors should clarify the ASR architecture in the final version since the current description of the ASR architecture is vague and prone to confusions-- see  questions below --.  I think this is something that authors might be aware of but prefer refer readers to the SpeechBrain recipes and experimentation.  This might leave a shallow reader without immediate interest in reproducing or delving into the code and recipes with a confusing architecture.

The approach has some limitations, so it would be intriguing to examine the performance of the proposed encoder in long-context ASR. 
Since this is a leaning representation conference, some experiments on NLP tasks, as in the original HyperMixer paper, would have attracted more readers.

Given the nature of speed optimization and comparison with MHSA, it would be interesting for the readers to know the specifics of the MHSA implementation as there are many very efficient implementations available nowadays.

Finally, it would have been nice to compare the proposed approach in both batch and online ASR.

### Questions
The following questions might need some attention into the manuscript:
* which is the global architecture and loss ? It is clear that it is a encoder decoder based architecture with CTC loss, but this is an important detail mentioned in 1 line. How many encoder layers each arch has ? which are the details of the decoder ? 
* Could the MHSA improve as the context becomes larger ? 
* which is the MSHA implementation have you used ?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel method to replace self-attentions with a more computationally efficient summary mixing model for speech recognition and spoken language understanding. Rather than computing an NxN attention matrix, the authors propose to first compute the temporal mean of the sequence and combine that with local information extracted using a cgMLP branch. Experiments on multiple corpora show that the proposed approach can match the performance of standard self-attention and Branchformer.

### Strengths
1. The paper uses a very simple approach to substitute self-attention with attention between a temporal summary and the original vector that appears to work well in practice.

2. Experiments are performed on multiple corpora for ASR (CommonVoice-Dutch, Italian, French), Librispeech, AISHELL, TED-LIUM 2, GSC and SLURP for SLU.

### Weaknesses
1. The paper makes the assumption that MHSA in the encoder is not necessary based on Zhang et. al. and Peng. et. al. However, I believe the assumption may not be well supported because (a) Zhang et al point out that you don't need self-attentions in higher layers, not that you don't need self-attentions at all, and (b) Peng. et. al which uses self-attentions to model global context while using cgMLP to model local context. Therefore, the rationale behind this fundamental assumption made in the paper seems unclear. Specifically, the paper does not adequately address the potential for self-attention to capture long-range dependencies, which could be crucial for certain speech phenomena. The argument that uniform attention weights justify a simple average is not sufficiently rigorous; while a uniform distribution might suggest that all tokens contribute equally, it does not account for the complex, non-linear interactions that self-attention can model, even when the attention weights are not sharply peaked. The paper needs to provide a more detailed analysis of the attention weight distributions and their implications for information flow.

2. SLURP uses read speech - the impact of temporal averaging here may be minimal, but may be very harmful in spontaneous conversational speech. Such explorations in my view are important in this work to claim that SummaryMixing can reach top-of-the-line in speech understanding. The paper lacks experiments on more challenging datasets with spontaneous speech, which is a significant limitation. The temporal averaging operation, while computationally efficient, could potentially smooth out important temporal variations in spontaneous speech, leading to a loss of crucial information for accurate speech understanding. The authors should investigate how the performance of SummaryMixing degrades with increasing levels of spontaneity and noise, and compare it to the performance of self-attention under the same conditions.

3. Writing could be more self-contained and clear in certain places - for example, HyperMixer is not well described which makes it hard to assess the relationship between the methods. The lack of a clear explanation of HyperMixer makes it difficult to understand the novelty and contribution of the proposed method. The paper should provide a more detailed description of HyperMixer, including its architecture, parameters, and how it relates to the proposed SummaryMixing approach. This would help the reader to better understand the context and significance of the proposed method.

### Questions
1. The authors claim that a score of 0.5 diagonality implies a uniform distribution and therefore, a simple average could achieve a similar token mixing. However, this is not obvious or clear to me. Could the authors explain?

2. I was interested to know how the performance of summary mixing is impacted during inference by temporal averaging. As the sequence length increases, the sum vector becomes a mixture of more frames, degrading the ability to discriminate individual frames/tokens. Do the authors have any numbers showing ASR performance (WER) as a function of sequence length across models with self-attention and the proposed SummaryMixing ?

3. As SLURP uses read speech, I was wondering if the authors had performed experiments on other corpora with spontaneous speech, for example, SLUE-VoxPopuli [1] for Named Entity Recognition (NER)?

4. The paper mentions KWS results, but I don't see any in the results section.

5. There are some papers [2,3,4] that show linear transformers can obtain comparable performance to MHSA for ASR contrary to what the authors claim. These works are also relevant and must be acknowledged in the paper. 

[1] "SLUE Phase-2: A Benchmark Suite of Diverse Spoken Language Understanding Tasks",
Suwon Shon, Siddhant Arora, Chyi-Jiunn Lin, Ankita Pasad, Felix Wu, Roshan S Sharma, Wei-Lun Wu, Hung-yi Lee, Karen Livescu, Shinji Watanabe

[2] Jingyu Sun, Guiping Zhong, Dinghao Zhou, Baoxiang Li, Yiran Zhong, "Locality Matters: A Locality-Biased Linear Attention for Automatic Speech Recognition"

[3] "Conformer-Based Speech Recognition with Linear Nyström Attention and Rotary Position Embedding", 
Lahiru Samarakoon, Tsun-Yat Leung

[4] "Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition", Dima Rekesh et. al.

### Soundness
3 good

### Presentation
2 fair

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
This paper proposes a linear-complexity based architecture as a replacement of self-attention for speech recognition to improve the efficiency. The proposed block has a local branch and a global branch to take both information into account. The local branch is based on a MLP, and the global branch has a MLP and then an average pooling among all the fram

### Strengths
* Paper fits ICLR scope well.
* The idea of reducing model complexity through replacing self-attention with linear layers is interesting.
* The proposed method is solid.

### Weaknesses
 * Presentations need improvement. See question sections for details.
* Literature reviews on ASR are very limited. Please have an individual paragraph in Section 1.1 to describe those.
* Novelty is a concern. The proposed work is an incremental work on the top of BranchFormer and HyperMixer. Although there is a paragraph describing the relationship to HyperMixer, the difference seems to be more on the choice of linear functions. Please explain more on this.
* The improvements from the proposed method seems to depend on the use of a transformer decoder (with self-attention). Need more experiments to verify the parity of the proposed method to self-attention in other conditions. See question sections for details.

### Questions
Abstract: “However, attention layers in trained speech recognizers tend to not capture fine-grained pair-wise information.” Please explain what “fine-grained pair-wise information” is and why it is important (although they are explained in the following sections, abstract should be self-explanatory).

Figure 1: The diagrams are a bit confusing. I understand that “T” refers to the total number of frames. However, audiences may likely think of them as different attention heads. Please consider a better way for the diagrams.

Section 2.1 - Multi-head SummaryMixing. Please better explain the heads in SummaryMixing. In self-attention, heads are operating in parallel with different sets of parameters. However, here heads help to reduce the number of parameters. Please consider adding a diagram on this if it helps. In addition, by dividing x_t into n chunks, is it similar to chuck-wise attention or attentions with a limited context window? If that’s the case, please avoid using “head” here.

Section 3.3.1: The results shown in this section have a transformer decoder of 6-blocks-MHSA paired with each system. In this setup, the decoder will capture the global context, even if the encoder doesn’t. However, we can only conclude that self-attention is redundant when self-attention based decoders are used.
The authors also conducted experiments without a transformer decoder (i.e., CTC only) on Branchformer in the supplemental materials. However, there are two more problems to figure out. 1. How does vanilla Conformer/Transformer with CTC performance in this setup? They are the most common architectures for productions than Branchformer. 2. These results are obtained with LM shallow fusion, which can be expensive for deployment. How would the proposed approach perform without shallow fusion? If the language information is needed, please also consider RNN-T decoder.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
