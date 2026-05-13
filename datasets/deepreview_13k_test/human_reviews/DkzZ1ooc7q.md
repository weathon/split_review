# OmniSep: Unified Omni-Modality Sound Separation with Query-Mixup

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
The scaling up has brought tremendous success in the fields of vision and language in recent years. When it comes to audio, however, researchers encounter a major challenge in scaling up the training data, as most natural audio contains diverse interfering signals. To address this limitation, we introduce \textbf{Omni}-modal Sound \textbf{Sep}aration (\textbf{OmniSep}), a novel framework capable of isolating clean soundtracks based on omni-modal queries, encompassing both single-modal and multi-modal composed queries. Specifically, we introduce the \texttt{Query-Mixup} strategy, which blends query features from different modalities during training. This enables OmniSep to optimize multiple modalities concurrently, effectively bringing all modalities under a unified framework for sound separation. We further enhance this flexibility by allowing queries to influence sound separation positively or negatively, facilitating the retention or removal of specific sounds as desired. Finally, OmniSep employs a retrieval-augmented approach known as \texttt{Query-Aug}, which enables open-vocabulary sound separation. Experimental evaluations on MUSIC, VGGSOUND-CLEAN+, and MUSIC-CLEAN+ datasets demonstrate effectiveness of OmniSep, achieving state-of-the-art performance in text-, image-, and audio-queried sound separation tasks. For samples and further information, please visit the demo page at \url{https://omnisep.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents OmniSep, a framework for omni-modal sound separation, which supports sound isolation using queries from multiple modalities, such as text, image, and audio, either independently or in combination. The key method of omni-modal source separation is the introduction of Query-Mixup, a strategy that mixes query features from different modalities, using a pre-trained ImageBind. OmniSep further enables open-vocabulary sound separation with Query-Aug, a retrieval-augmented method that enhances adaptability, particularly for text-based queries. Experimental evaluations on MUSIC, VGGSOUND-CLEAN+, and MUSIC-CLEAN+ datasets showcase OmniSep’s SOTA performance across various modality-based separation tasks.

### Strengths
The paper presents an omni-modal sound separation approach, allowing users to conduct sound separation tasks using queries across various modalities, including text, image, and audio, both independently and jointly. Additionally, the authors conducted a comprehensive evaluation across several benchmarks. Further, the inclusion of extensive ablation studies provides insight into the contributions of each component: impact of Query-Mixup, negative query weighting, long text description-queried separation, and analysis on query embeddings.

### Weaknesses
While the paper presents a solid framework, there are some details missing that make it difficult to give a firm acceptance (please answer Questions). 

The use of full-length video as a query, which includes the target segment, raises questions about the potential for information leakage. It’s unclear if the QueryNet architecture ensures a bottleneck to prevent the model from “cheating” by directly accessing target audio features. To better demonstrate the model’s robustness, an alternative setup might involve using a different video as the query that shares the same class identity as the input audio.

Additionally, the comparison in Section 4.3 between the proposed weighting and a naive weighting approach on $Q_N$ may not be particularly insightful, as both methods use the same model. The proposed approach always has a weight difference of 1 ($1+\alpha$ vs. $\alpha$), while the comparison (naive) approach reduces the weight gap between $Q$ and $Q_N$, hence the results in Figure 2 are somewhat predictable. However, the insights provided by varying $\alpha$ are valuable.

### Questions
- What happens when the query is some class that’s not present inside the input mixture audio?
- Table 2: why no results on AQSS?
- Query-Aug Adaptability:
    - Is the Query-Aug method adaptable only to text queries $Q_T$, or does it extend to other modalities as well?
    - Additionally, how will the model handle text prompts containing multiple sound sources (e.g., “the sound of a baby with her parent’s soothing voice”)? Is the model trained to handle multi-source separation?
- Number of Audio Sources in Mixtures: For AQSS VGGSOUND, does $\mathcal{S}=5$ mean $A_\text{mix}=\sum_{n=1}^6A_n$? then for all other setups, is $A_\text{mix}=A_1+A_2$?
- Did the authors use the pre-trained ImageBind weights from the official repository (https://github.com/facebookresearch/ImageBind), or did they train ImageBind from scratch? They should mention the repository if pre-trained weights were used. If trained from scratch, they should include the details of the pre-training specifications.
- How does OmniSep respond when a query references a class that is not present within the input audio mixture?
- Why are there no AQSS results reported in Table 2?

Minor comments
- typo @Figure 1: “…, donated as $\text{Q}_T$, …”
- Figure 1: inside the Query-Mixup block, the weight factors are denoted as $W$, where it should be $w$
- grammar @line 217: “The training …”
- Table 1: should note the source of VGGSOUND-CLEAN+ and MUSIC-CLEAN+ subsets. Also provide a couple of sentences for details of these subsets.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents OmniSep, a novel unified framework for query-based sound separation that accommodates multiple query modalities (text, image, and audio) within a single model. The authors introduce three key technical contributions: Query-Mixup for simultaneous multi-modal query processing, a negative query mechanism for unwanted sound suppression, and Query-Aug for handling natural language descriptions beyond predefined class labels. The model's architecture represents an advance over previous approaches, which were typically constrained to single-modality queries.

Experimental validation on several datasets demonstrates OmniSep's performance compared to existing methods across all query modalities. The model exhibits robust separation capabilities in complex, multi-source scenarios and achieves state-of-the-art results on MUSIC, VGGSOUND-CLEAN+, and MUSIC-CLEAN+ benchmarks. OmniSep's multi-modal query capability enables enhanced separation performance through the simultaneous application of different query types, such as combining textual and visual queries.

### Strengths
The paper presents a clear and well-motivated problem statement, addressing three fundamental limitations in current sound separation approaches: the absence of unified multi-modal query handling, insufficient flexibility in sound manipulation (particularly for unwanted sound removal), and restricted vocabulary constraints that preclude natural language descriptions. The authors construct a compelling narrative throughout the introduction and literature review, effectively contextualizing their contributions within the field through comprehensive citations and thorough analysis of related work.

The methodology is generally well-documented to begin with. The experimental validation is particularly robust, encompassing diverse tasks and datasets that demonstrate the method's versatility. The authors provide extensive ablation studies that illuminate the model's internal mechanisms and justify some of the architectural choices. Their commitment to reproducibility through code release further strengthens the paper's contribution to the field.

### Weaknesses
There are several issues with the paper, which can broadly be classified into two areas.  Most of these issues can be fixed with better, scientific writing, and more explanation, rigour and experimentation. 

Technical Clarity Issues: 
1. Significant documentation gaps in core variables and operations in Separate-Net: 
   - q_i and q_ij are poorly explained or completely undefined in Separate-Net 
   - Many variables are undefined and or with no dimensions specified. All variables should be clearly defined with dimensions given.  
   - M(hat) is defined but never used. 
   - Mechanism of how masks are used/applied is not explained.
   - Audio U-Net lacks both citation and architectural explanation.
2. Query-Aug undefined components: 
   - Q_des: completely undefined without dimensions and no explanation of how these features are obtained (T5/Bert?).
   - Query-Set: is undefined and dimensions not specified.
   - Q_aug defined as argmax but its integration into model never explained.
   - sim(.,.) is not a standard operator, it should be properly defined (cosine similarity?).

Experimental Validation Problems: 
1. Table 1 uses a 2017 model called PIT for non-queried sound separation. State-of-the-art audio-only separation methods (i.e. TDANet, TF-GridNet) would serve stronger baselines (while these models are for speech separation, so is PIT. Additionally, PIT was proposed so solve the permutation problem, not as a strong speech separation model).  
2. Table 2 does not show that the query-mixup method works, only that it scales across different modalities. Validating its effectiveness would mean comparing to other methods and/or different strategies. 

However, there are some other issues. While the method is interesting, the paper's novel work can be summarised as a weighted average of modalities, a linear layer and (1+alpha)Q-alphaQ_N for negative queries.

### Questions
1. Separate-Net only converts to magnitude spectrum X, ignoring phase. Modern time-frequency methods (RTFS-Net, TF-GridNet) use retain both magnitude and phase information via concatenated real/imaginary STFT outputs. Some methods additionally concatenate the magnitude to create a three channel representation. Have you tried these approaches? 

2. Why keep ImageBind parameters frozen? What if it was trained from scratch with the model? What if it was initialized and fine tuned with the model using a lower learning rate? 

3. For the Negative Query, why (1+alpha)Q-alphaQ_N instead of (1-alpha)Q+alphaQ_N, Q-alphaQ_N or a scale-and-shift approach such as in stable diffusion - please add some justification in this section or some experimental evidence. 

4. And the problems raised in the weaknesses section.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes an audio source separation model that can be queried via audio, language and image. To construct such model, this paper proposes query mixup which blends query from different modalities during training and ensure queries from different modalities reside in the same semantic space. This paper also propose a negative query mechanism to enhance the flexibility of query in inference stage. Last, to enable open-vocabulary text query input to the model which trained on close-set class name, this paper propose a query-augmentation method at inference time which retrieves nearest class name. Experiment result shows the model outperforms existing model in all modalities on MUSIC, VGGSOUND-CLEAN+, and MUSIC-CLEAN+ datasets.

### Strengths
1. A novel model for source separation queried by audio, text and image. Propose a novel query-mixup method to enable such model.
2. Propose novel negative query and query-aug method to improve performance and flexibility at inference time.
3. State-of-the-art performance on separation tasks queried by all modalities

### Weaknesses
1. Presentation: Certain aspects of the paper’s presentation feel oversimplified, particularly in explaining key contributions and technical details. Please refer to the questions section for specific areas needing clarification.

2. Contribution of Query-Aug: The significance of the query-augmentation (query-aug) contribution seems overstated. For example, lines 054–056 suggest that current systems cannot handle open-vocabulary queries. However, Liu et al. (2023) ("Separate Anything You Describe") demonstrates that open-vocabulary language queries are achievable using audio-text datasets, such as Clotho or AudioCaps. Furthermore, the model proposed in this paper should be capable of training on these audio-text datasets and potentially on datasets lacking complete audio, text, or image pairs. An expanded discussion comparing this work to Liu et al. (2023), along with a rationale for the choice of datasets, would strengthen the contribution.

3. Experimental Results: The presentation of experimental results lacks some necessary detail:
 - What training settings were used for the models in Table 2, and how do these models (particularly model #5) correspond to those in Table 1?
 - For Table 4, a comparison of results from querying the same audio mixture across different modalities would provide valuable insights.

4. Metrics for Comparison: In prior works cited in the paper, metrics such as SI-SDR and SDRi are commonly used for source separation tasks, as they better reflect model performance in recent studies. Including these metrics or providing justification for the metrics chosen would enhance the comparative analysis.

### Questions
The introduction of the Separate-Net is missing some details:
1. Line 210: what is k and what does k corresponds to? 
2. Does the query conditioned to the U-Net? If not, why query is not conditioned to UNet? If possible, it would be helpful to visualize the qi in some examples. It feels odd to me that the query only results in a channel-wise weight.

### Soundness
3

### Presentation
2

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
This paper attempts to cover text-, image- and audio-queried sound separation all at once with one model by exploiting ImageBind as its encoder. Several training techniques are introduced and verified its effectiveness in terms of signal-to-noise ratio as well as spectral similarity, which demonstrates the superiority of OminiSep to other existing query-based sound separation methods

### Strengths
- Three novel training techniques, Query-mixup, NQ, Query-Aug, are proposed and evaluated in the standardized experimental settings
- Consistent improvements of median SDR in Table 2, which demonstrates the SOTA performance of OmniSep in the query-based sound separation field
- Good visualization of ImageBind embeddings to show the clear motivation of the Query-mixup

### Weaknesses
- Inappropriate motivation: I felt puzzled when I was reading the introduction part because the original motivation of the paper was how we could increase the number of high-quality training dataset although this motivation was never addressed anywhere in the other sections of the paper. If the objective is like the above, why don't we simply compare your scheme to other data augmentation methods or artificial data creation methods other than sound separation? I agree that denoising with sound separation would serve as one of many methods to achieve the same goal. Then, I believe the author should prove that OmniSep is the one of the best methods to increase the number of data. That being said, while assessing the paper, I somehow felt that this was not your intention. Since the technical contributions of the paper are fair enough, I suggest rewriting the introduction part in a way like your motivation is to improve the quality or coverage of text-, image-, or audio-queried sound separation and NOT to use sound separation to increase the number of training datasets for other purposes. 
- As an expert in this field, I don't agree relying only on SDR to measure the performance of any sound separation methods. Rather than showing pairs of spectrums, I suggest conducting a listening test to doublecheck if the performance of OmniSep really dominates others and the difference is recognizable. If the goal of the paper is not to make separated data available to human, as you originally stated in the introduction part, i.e., data increase is the objective, I don't think having a subjective listening test enriches the content. Otherwise, I strongly recommend this because this is a common practice in the sound separation community.

### Questions
The motivation of Query-mixup is clear. On the other hand, its effectiveness compared to finetuning of ImageBind is not clear. Why don't you simply finetune your encoder so that all the modalities align well each other to the inputs of your interests. It is also unclear if the performance improvement really comes from the proposed three methods because the encoders in CLIPSep and OmniSep are different. Table 3 is a nice way to prove Query-Aug is actually important to increase SDR. Not sure about other two. You could have tried the rest of two methods on CLIPSep and see the performance improvements of CLIPSep?

### Soundness
3

### Presentation
3

### Contribution
3
