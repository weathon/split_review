# Sylber: Syllabic Embedding Representation of Speech from Raw Audio

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 8, 8, 5

## Abstract
\blfootnote{\enspace\enspace\enspace \small Correspondence to: Cheol Jun Cho \texttt{<cheoljun@berkeley.edu>}, Gopala K. Anumanchipalli \texttt{<gopala@berkeley.edu>}}
 
Syllables are compositional units of spoken language that play a crucial role in human speech perception and production. 
However, current neural speech representations lack structure, resulting in dense token sequences that are costly to process. To bridge this gap, we propose a new model, \ours, that produces speech representations with clean and robust syllabic structure. Specifically, we propose a self-supervised model that regresses features on syllabic segments distilled from a teacher model which is an exponential moving average of the model in training. This results in a highly structured representation of speech features, offering three key benefits: 1) a fast, linear-time syllable segmentation algorithm, 2) efficient syllabic tokenization with an average of 4.27 tokens per second, and 3) syllabic units better suited for lexical and syntactic understanding. We also train token-to-speech generative models with our syllabic units and show that fully intelligible speech can be reconstructed from these tokens. Lastly, we observe that categorical perception, a linguistic phenomenon of speech perception, emerges naturally in our model, making the embedding space more categorical and sparse than previous self-supervised learning approaches.
Together, we present a novel self-supervised approach for representing speech as syllables, with significant potential for efficient speech tokenization and spoken language modeling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents an innovative self-supervised learning (SSL) method that converts speech into syllable-based embeddings. The authors employ a range of evaluation metrics—such as syllable detection and discovery, speech intelligibility, coding efficiency, sWUGGY, and sBLIMP—to demonstrate the effectiveness of their approach. The approach provides a linear-time syllable segmentation algorithm and efficient speech tokenization with an average of 4.27 tokens per second.

### Strengths
The framework is well-motivated, particularly due to the efficiency of its tokenization algorithm, which helps manage the exponentially increasing compute costs associated with transformer-based models in downstream tasks.

### Weaknesses
While the approach is well-motivated as an efficient alternative for speech tokenization, achieving an average rate of 4.27 tokens per second, the evaluation metrics used don’t fully justify the applicability of these tokens for down stream tasks, as shown in Table 9. It would be beneficial for the authors to moderate some claims, such as:

	•	that syllabic units are better suited for lexical and syntactic understanding
	•	and that these units are better suited for SLU

Instead, the focus could remain on highlighting the promising initial results regarding the efficiency of the speech tokenization and interpretability of the tokens, as further work is needed before demonstrating the superiority of syllable-based tokens in downstream tasks.

I would suggest that the authors add more details in Section 3.1 and be more comprehensive. 

Also, I would strongly suggest that the authors simplify some of the very long sentences throughout the paper, e.g., 

"The target segment labels are continuous embeddings averaged across frames within each segment that are found by an unsupervised segmentation algorithm"

### Questions
- The model was trained to explicitly detect syllables. Wouldn't it perform the best using the proposed metric for syllable detection and discovery? Would metric be a biased one?

- On the author's observation that the articulatory reconstruction and intelligibility increase with finer clustering granularity,  Does that indicates that speech requires more fine-grained representation to performs well in spoken language understanding? 

- The author emphasized that other SSL tokens lack structure. Though, other SSL might not have syllable-based structure, but they have sub-phonemic structure

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
This paper studies the problem of tokenizing speech waveforms into discrete units that are suitable for tasks such as speech language modeling. Current approaches to this problem typically cluster (e.g. with K-means) the intermediate representations of a self-supervised transformer (such as HuBERT or WavLM), then run-length encode these clusterings to derive discrete tokens for training a language model over speech units. Two problems with this approach are that 1) the K-means units have been found to represent phonetic/sub-phonetic information and thus have a very high temporal rate, which makes Transformer-based speech language models difficult to scale from a computational perspective and 2) the units do not capture higher-level linguistic abstractions (e.g. words or morphemes) which could make even higher level abstractions (such as semantics) more difficult to learn, preventing current speech LMs from unlocking emergent abilities such as in-context learning.

The paper builds upon a previous approach from the literature, namely SD-HuBERT. The paper uses SD-HuBERT to extract syllable-like segmentations of speech waveforms (without the need for ground-truth annotations). It then fine-tunes an SD_HuBERT model with a teacher-student knowledge distillation objective, where the teacher is an exponential moving average of the student model whose outputs are average pooled features within each syllable-like segment.

The paper presents experimental results showing state-of-the-art performance on syllable segmentation and clustering, and demonstrates that the learned representations exhibit categorical discrimination ("lest" vs. "rest") that mirrors that of humans. It also shows the units can be used to resynthesize intelligible speech and when used to train a speech unit language model achieve strong performance on standard metrics (sWUGGY/sBLIMP)

### Strengths
-The paper investigates an important and timely topic, namely speech tokenization focused on learning linguistically-motivated large granularity units.

-The proposed method for learning the units is simple and effective.

-The experiments are broad, covering categorical perception to syllable segmentation to resynthesis to spoken language understanding tasks with speech LMs

-The experimental results are strong on all tasks evaluated.

### Weaknesses
The main weakness from my perspective is that I would have liked to see a more in-depth analysis of the resynthesis results in terms of naturalness. It is expected that when moving from low-level acoustic units to higher level syllable-like units, we may lose a lot of the low-level details that are unnecessary for higher level understanding but are needed to represent highly naturalistic speech. However, when building speech LMs we often want to re-synthesize their outputs so they may be played back to the user (e.g. when using the speech LM as a dialog agent) so it is important to understand how well the proposed units work for that scenario. Specifically, the paper does not provide any objective or subjective metrics for the quality of the resynthesized speech, making it difficult to assess the practical utility of the proposed units in downstream applications that require high-fidelity audio output. The paper should have included a perceptual evaluation of the resynthesized speech, such as a Mean Opinion Score (MOS) test, to quantify the perceived naturalness and intelligibility.

### Questions
Did the authors conduct any naturalness evaluation of the resynthesized speech from the proposed units? How did it compare to existing approaches (such as using HuBERT K-means units)?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes Sylber, a self-supervised knowledge distillation and bootstrapping method to learn syllable-level speech features. With better features, a faster segmentation algorithm with O(n) complexity can be utilized (compared to O(n^2) algorithms). Better syllable features also improve downstream performance on speech understanding and codec efficiency.

### Strengths
1. The authors presented extensive experiments to demonstrate the strengths of Sylber, covering syllable segmentation, spoken language understanding, and audio codec.
2. The propose learning approach is intuitive and having linear time segmentation algorithm would also greatly facilitate utilization of syllable level features into downstream tasks such as spoken language modeling with syllable level tokens.
3. Authors also presented interesting qualitative analysis in Section 4 connecting syllable representations to the categorical perception in rhymed syllable pairs.

### Weaknesses
1. Some details and ablation studies are missing:
    1. The proposed method regresses non-speech frames to zero. What model / method was used to determine whether a frame is speech or non-speech? It is unclear how the thresholding on the norm of the encoder layers is determined and what the effect of this threshold is on the final performance. Furthermore, the additional filtering based on waveform amplitude is not sufficiently motivated. What is the sensitivity of the method to this threshold and how does this interact with the norm threshold?
    2. The authors claim that better features motivate the design of the linear-time greedy segmentation algorithm. For SD-HuBERT and Sylber, how much does that segmentation algorithm affect the performance? It would be clear if the authors can report Table 1 results with all combinations of (SSL feature, segmentation algorithm). It is not clear if the greedy algorithm is applied directly to the features or if any additional processing is done. Also, the hyperparameter tuning for the greedy algorithm is not sufficiently described. What is the search space and how is the optimal value determined?
2. The authors should move the slightly negative results in A.3 to the main paper. It is crucial to discuss not just the advantages but also the caveats of the proposed methods.

### Questions
1. In Figure 2, does the heat map show syllable level or frame level similarity matrix for Sylber?
2. How robust is the proposed method with respect to the quality of the initial segmentation (currently segmentation from SDHuBERT) and the initial features (currently SDHuBERT) respectively? If phone segmentation instead of syllable segmentation is provided, does the model learn phone level representation instead?
3. See other questions in the Weakness section above

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes Sylber, a self-supervised learning method for extracting syllabic representations from speech. To achieve this goal, the authors propose a self-distillation framework with an unsupervised syllable segmentation algorithm. Sylber surpasses some prior speech tokenizers on multiple benchmarks, including syllable detection, speech resynthesis, and spoken language modeling (understanding). Besides, this paper introduces a discriminability index to measure whether speech embeddings align with categorical perception.

### Strengths
1) The proposed Sylber approach successfully bridges the self-distillation method in speech self-supervised learning (SSL) with syllable segmentation/discovery.
2) Sylber demonstrates strong syllable segmentation and discovery capabilities through comprehensive experimental results.
3) The discriminability index and Figure 3 clearly show Sylber's categorical perception capability, which aligns with human perception.

### Weaknesses
1) **Training effort:**  
It is not clearly stated in the main text, but according to Appendix A.1.4, Sylber requires two-stage training with 1.15M and 500k updates, respectively, even though the model was trained on the 960 hours LibriSpeech. Note that this does not include the pre-training costs of HuBERT and SDHuBERT. Moreover, the performance gain in the second stage of training is not significant (Table 6). E.g., the R-value only improved from 75.6 to 75.9. Thus, the need for the second stage of training is questioned.
2) **Model scalability:**  
The unstable training process and sensitivity to hyperparameters are known problems of EMA-based self-distillation, like data2vec. This fact might lead to challenges in scaling the model. Furthermore, larger models increase the training costs, not to mention the required 1.65M updates in the original Sylber model. The paper does not provide sufficient evidence that the proposed approach is robust to these issues, particularly given the reliance on a two-stage training process.
3) **Data scalability:**  
A commonly known fact between speech datasets is the significant domain differences. According to the experimental results, all models were optimized for LibriSpeech, a relatively clean speech corpus. However, it is unclear whether the segmentation algorithm works in noisier conditions like conversational speech (e.g., Switchboard). Additionally, the segmentation algorithm might need extra design for multilingual speech. Hence, scaling the training data might be difficult, casting doubts about Sylber's real-world applications. The paper lacks experiments demonstrating the model's performance on diverse datasets, especially those with varying noise levels and linguistic characteristics.
4) **Complicated resynthesis approach:**  
Compared to prior studies [2,3], this paper's speech resynthesis (token-to-speech) method is significantly more complicated. It involves a CFM model to generate low-level articulatory features for the Articulatory Encodec. The complicated resynthesis method might introduce more uncertainties to the evaluation results. Also, the resynthesis intelligibility and quality are not significantly better than HuBERT with K-means clustering (Table 2). The use of a CFM model adds unnecessary complexity, and the paper does not adequately justify why a simpler approach was not sufficient.
5) **Actual inference efficiency:**  
The authors only reported the complexity of syllable segmentation methods. However, a more accurate and practical evaluation method is to include the inference time required to extract syllable boundaries. E.g., latency and real-time factors (RTF). The paper should provide a more comprehensive analysis of the computational cost of the proposed method, including the actual time required for inference.
6) **Insignificant SLU improvements:**  
The SLU results in Table 4 do not show great improvements over GSLM (less than 3% relative difference). Some prior methods, like NAST [4] and SpeechTokenizer [5], are not reported for comparison. Besides, the dataset for training uLMs is not clearly stated, which is important since uLM performance highly depends on the amount of data used [6]. The paper needs to provide a more thorough comparison with existing methods, and clarify the training details of the uLM.
7) **The necessity of syllabic tokens:**  
In addition to the scalability issues previously raised, another question is whether syllabic tokens are necessary in real-world use cases. First, one of the main purposes of developing better speech tokenizers is to advance applications like ASR, TTS, and spoken LM. Nevertheless, the authors only presented a minor improvement in SLU. So, it is unclear whether Sylber helps downstream tasks. Second, because of the loss of fine-grained information (Table 9), tokens extracted from Sylber require incorporating separate speech encoders/tokenizers for more complex problems, which other SSL-based tokenizers or neural audio codecs could address. Perhaps providing convincing reasons and experimental evidence helps justify the need for syllabic tokens.

### Questions
1) Explain the differences between the discriminability index and phonetic ABX [1,2]. How are these metrics correlated?
2) How many and what kind of GPUs were used to train/fine-tune each model?
3) Why did Table 2 not consider HuBERT with 500 K-means clusters and the continuous representations? Note that 500 clusters or even 2k are commonly used in prior studies [3].
4) Because Sylber was trained with audio in 5-second segments, how does this affect the downstream performance with long utterances (syllable detection and speech resynthesis)?

[1] Schatz, Thomas. ABX-discriminability measures and applications. Diss. Université Paris 6 (UPMC), 2016.  
[2] Nguyen, Tu Anh, et al. "The zero resource speech benchmark 2021: Metrics and baselines for unsupervised spoken language modeling." arXiv preprint arXiv:2011.11588 (2020).  
[3] Maiti, Soumi, et al. "VoxtLM: Unified Decoder-Only Models for Consolidating Speech Recognition, Synthesis and Speech, Text Continuation Tasks." ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2024.

### Soundness
3

### Presentation
3

### Contribution
2
