# Neuro2Semantic: A Transfer Learning Framework for Semantic Reconstruction of Continuous Language from Human Intracranial EEG

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
Decoding continuous language from neural signals remains a significant challenge in the intersection of neuroscience and artificial intelligence. We introduce Neuro2Semantic, a novel framework that reconstructs the semantic content of perceived speech from intracranial EEG (iEEG) recordings. Our approach consists of two phases: first, an LSTM-based adapter aligns neural signals with pre-trained text embeddings; second, a corrector module generates continuous, natural text directly from these aligned embeddings. This flexible method overcomes the limitations of previous decoding approaches and enables unconstrained text generation. Neuro2Semantic achieves remarkable performance with as little as 30 minutes of neural data, significantly outperforming a recent state-of-the-art method in low-data settings. These results highlight the potential for practical applications in brain-computer interfaces and neural decoding technologies.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a novel framework called Neuro2Semantic for reconstructing semantic content from human intracranial electroencephalogram (iEEG) recordings. This study breaks through the limitations of previous methods by leveraging contras loss and triplet loss and using a pre-trained text reconstruction model in the fine-tuning stage to extract coherent text.

### Strengths
1. The transfer learning framework adopted by Neuro2Semantic can achieve efficient semantic reconstruction under the condition of a small amount of data.
2. Neuro2Semantic is able to perform zero-shot reconstruction on completely unseen semantic content, showing good generalization.

### Weaknesses
1. This paper only compares one baseline, and this baseline is very poor.
2. Model performance is highly dependent on the quality and relevance of pre-trained text embeddings, which may limit its effectiveness when dealing with domain-specific or rare vocabularies.

### Questions
1. What is the reason for the poor performance of baseline, especially much worse than the reported values?
2. Have the authors explored other more efficient sequence processing models (such as Transformers or GRUs) to improve the capture and computational efficiency of long-term dependencies?

### Soundness
3

### Presentation
2

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
The paper presents Neuro2Semantic, a new framework for decoding the semantic content of perceived speech from intracranial EEG (iEEG) recordings. The approach has two main components: an LSTM-based adapter that maps neural signals to pre-trained text embeddings, and a corrector module that produces continuous, natural language from these embeddings.  The paper claims that it could outperforms state-of-the-art models while only requiring 30 minutes of neural recordigns.

### Strengths
The performance reported in the experimental section shows good improvement over baseline models. It shows the BLEU score reached 0.1947 while the baseline method only shows 0.0315.

### Weaknesses
1. The experiment is not adequate to claim that this is a solid SOTA for brian-to-text translation, especially only given 30 minutes of training data. Considering this method has a T5 corrector over the previous method, the well-trained language model will generate multiple semantically continuous sentences containing many articles and common words will give the illusion of an artificially high bleuscore. Figure 2 generated text samples also support this phenomenon. Meanwhile, do the training set and the test set share similar sentences? If so, the training set split could also largely affect the performance rather than really learning neural patterns.

Especially, when referring to Table 1 Neuro2Semantic - Adapter Only, which emphasizes the neural patterns. This paper reaches a BLEU score of 0.0677 which is about the same as the baseline of 0.0642 and the ROUGE score is 0.1131 (baseline) and 0.00841 (this paper). It shows no clear evidence in this paper to learn a better neural representation. 

2. The experimental part lacks the cross-session and the cross-subject analysis. Only 30 minutes of data may lead to a severe over-fitting problem. 

3. The novelty is very limited, utilize an adaptor and language model to do the brain-to-text translation task. The new thing is to use iEEG rather than EEG.  However, according to the main structure part, the only difference with EEG-based models is that iEEG uses an LSTM framework vs. others using a conformer structure. Meanwhile, some of the works are not properly included and discussed, such as [1,2].

[1] Li J, Song Z, Wang J, Zhang M, Zhang Z. BrainECHO: Semantic Brain Signal Decoding through Vector-Quantized Spectrogram Reconstruction for Whisper-Enhanced Text Generation. 

[2] Yang Y, Duan Y, Zhang Q, Xu R, Xiong H. Decode neural signal as speech.

### Questions
1. What is the key difference between doing the iEEG-to-text translation rather than EEG-to-text translation?

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
3

### Summary
The submission presents an approach for decoding continuous perceived sentences using intracranial EEG recordings. This method comprises two stages: the first stage involves aligning neural signals with text in a latent space, and the second stage utilizes a Vec2Text module to map the generated latent embeddings to text. The results demonstrate that the proposed method outperforms baseline approaches in most of the cases regarding both in-domain and out-of-domain scenarios.

### Strengths
The submission is well written and clear. Authors conducted comprehensive experiments. The results demonstrates the effectivness of the methods outperforms the baseline method the scenario for in domain and out of domain cases.

### Weaknesses
Generally, the semantic meaning of the reconstructed sentences in both Neuro2Semantic and the baseline method appears to diverge significantly from the original text, as illustrated in Figures 2B and 3B. While the word error rate (WER) captures only surface-level matching between the decoded sentences and the ground truth, it is crucial to retain certain key nouns to ensure accurate semantic transmission. Current word error rate is very high, also other metrics like BERT score or BLEU score is quite low. The authors could enhance their discussion by elaborating on how the current method contributes to the field, particularly given the limited semantic alignment between the decoded sentences and the ground truth, despite improvements in the metrics.

Additionally, it would be beneficial to include a related work section that compares the proposed method with previous approaches focused on decoding continuous sentences from neural signals. The authors could also discuss related works on methods that learn the alignment of two modalities, as well as those that generate continuous vectors from text embeddings.

### Questions
1. Did authors try different architectures for phase one, instead of using LSTM?
2. How many sentences/trials are used evaluated to obtain current results?
4. What could be the upper bound of the performance, especially when more data is provided?
5. Why not include model from Wang et al., 2024 as baseline comparison?
6. What is the intuition behind using both Triplet loss and the contrastive loss since they are serving the same function?
7. It is interesting that, using phase 2 alone, without any alignment between text and neural signal, the model can still generate some outputs with comparable BLUE score to the full model, could author describe more on this? Also how the random control baseline is performed?

### Soundness
3

### Presentation
3

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
Neuro2Semantic introduces a novel approach for reconstructing semantic content from intracranial EEG (iEEG) recordings. The authors propose a two-phase framework: In the first phase, an LSTM adapter aligns neural signals with pre-trained text embeddings using a combination of contrastive and triplet loss functions. In the second phase, a pre-trained Vec2text corrector generates continuous text from the aligned embeddings. The model demonstrates the ability to decode coherent semantic content with as little as 30 minutes of neural data, significantly outperforming baseline methods in low-data scenarios.

### Strengths
The paper presents a novel approach by using the Vec2text corrector module to reconstruct sentences directly from neural embeddings, which is a fresh and innovative method in the field of iEEG-based neural decoding. The combination of pre-trained text embeddings and a correction module provides new insights and directions for generating coherent text from brain signals, offering a new perspective compared to traditional classification-based or retrieval-based approaches.

### Weaknesses
The paper demonstrates several strengths, but there are some concerns regarding the choice of methodology, data robustness, and presentation of results. Specifically, the use of LSTM instead of more modern architectures like Transformer, the potential for overfitting with such limited data, and the incomplete dataset description raise questions about the generalizability and scalability of the approach. For detailed concerns and clarifications, please refer to the Questions section.

### Questions
1） The authors have chosen an LSTM-based approach for aligning neural signals with text embeddings. While LSTMs are known for handling long-range dependencies, the current state-of-the-art models for EEG and language tasks often rely on Transformer architectures, which are more powerful in capturing contextual information. Why did the authors opt for LSTM instead of using a Transformer encoder or even more advanced architectures like xLSTM? Wouldn't these architectures better align with the pre-trained Transformer-based language models used in the later stages of the pipeline?


2） The authors used the Vec2text corrector module to reconstruct sentences from neural embeddings, so it seems that the main goal would be to make the neural embeddings as similar as possible to the text embeddings. Given this, why was a more complex loss function—combining contrastive and triplet loss—chosen over a simpler Mean Squared Error (MSE) loss? What performance advantages does this combined loss offer for aligning the neural embeddings with the text embeddings?


3）This paper achieves remarkable performance with as little as 30 minutes of neural data. It raises concerns about the robustness and overfitting of the model when applied to different subjects, which suggests that more rigorous validation methods are needed to assess the model's robustness and generalizability. Implementing more comprehensive validation strategies, such as leave-one-subject-out or similar cross-validation techniques, would provide stronger evidence of the model’s ability to generalize across diverse subjects and conditions.


4）The authors propose the use of a pre-trained T5 Corrector to reconstruct sentences from text embeddings. However, autoregressive language models, which generate text one token at a time, are the standard in most generative tasks. What are the advantages of using the Corrector compared to autoregressive generation? How does it impact the model’s performance in terms of coherence and quality?


5）The presentation of decoding results in Figure 2(B) could be clearer. There is no discussion of whether important named entities or key phrases were successfully decoded. The authors could improve the clarity by bolding successfully decoded words or phrases and italicizing words with similar meanings. This would help highlight the strengths and weaknesses of the model's semantic reconstruction capabilities.


6）The dataset description lacks important details. Key demographic information, such as the subjects' age, gender, and other relevant characteristics, is missing, which could affect the generalizability of the results. Additionally, the content of the audio stimuli is not clearly explained, making it difficult to assess the consistency or variability in what the subjects heard. More information about the stimuli is necessary to fully understand the experimental setup and ensure the results are reliable.

### Soundness
3

### Presentation
3

### Contribution
3
