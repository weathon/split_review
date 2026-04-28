# Distilling an End-to-End Voice Assistant Without Instruction Training Data

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 5, 3

## Abstract
Voice assistants, such as Siri and Google Assistant, typically model audio and text separately, resulting in lost speech information and increased complexity. Recent efforts to address this with end-to-end Speech Large Language Models (LLMs) trained with supervised finetuning (SFT) 
 have led to models ``forgetting" capabilities from text-only LLMs. Our work proposes an alternative paradigm for training Speech LLMs without instruction data, using the response of a text-only LLM to transcripts as self-supervision. Importantly, this process can be performed without annotated responses. We show that our Distilled Voice Assistant (DiVA) generalizes to Spoken Question Answering, Classification, and Translation. Furthermore, we show that DiVA better meets user preferences, achieving a 72\% win rate compared with state-of-the-art models like Qwen 2 Audio, despite using $>$100x less training compute.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes DiVA, a voice assistant model that is able to follow both spoken and written instructions. It is trained via a dual distillation and alignment loss and shows relatively strong results on various benchmarks including head to head comparison with Qwen 2 Audio. The authors propose a "q-former" style injection of audio into the model, which is initialized from a Whiper model, and a text model initialized with Llama weights and left frozen which consumes the audio input. This model is then trained for relatively small amount of steps on CommonVoice data to learn input alignment as well as output alignment (as compared to text labels).

### Strengths
- Interesting approach which takes several pre-trained models (Llama, Whisper), connects them via a q-former based adapter and trains a small portion of the combined model to respond to audio inputs.
- Scores relatively well on various benchmarks compared to some well known models.
- The main contribution is showing that it is sufficient to teach an existing instruction-tuned model to understand audio through relatively light weight techniques which then allows the model to follow instructions via audio queries.

### Weaknesses
There is not a lot of novelty in this method besides choosing which data to train on. Q-former or in general attention based pooling (e.g. as in perceiver) is well known; L2 loss as a replacement for KLD has also been around for awhile (e.g. in Soundnet: Learning sound representations from unlabeled video.). Putting some of these pieces together to allow Llama models to process audio input has also been explored, for example in Nvidia's SpeechLLM or SALMONN (which is cited in this paper and apparently does not use Llama). In my opinion demonstrating that full SFT is not required to obtain an audio understanding model is interesting but not sufficient. The use of a pre-trained model to initialize the q-former is a useful technique but not particularly novel in itself. While the authors propose a feature-regression style loss, this is not a significant departure from existing feature distillation techniques, which have been explored in various contexts, including image classification and other modalities. The core idea of using a L2 loss to align hidden states is similar to existing approaches that minimize the difference between student and teacher representations, and the theoretical justification provided, while useful, does not introduce a fundamentally new concept. Furthermore, the comparison to other models is not complete, as it does not include other adapter-based approaches on top of Llama3, which the authors' own ablations show to be a significant factor in performance.

### Questions
- Have you compared your approach with an ASR -> LLM based pipeline? One would imagine it would score poorly on the emotion recognition tasks, but probably very high on others.
- Have you considered diving deeper into what kind of data is requires to achieve specific results? For example, you could ablate the amount of commonvoice data required to achieve specific results; explore other datasets and/or languages and measure their impact on downstream tasks. This would provide a valuable contribution to the community.

### Soundness
3

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
4

### Summary
This paper proposes a method named DiVA for training a speechLLM without using any instruction data in the speech modality. To perform this, an LLM is adapted to enable speech input and output by first combining it with a Whisper based speech encoder, and then using two Novel loss term to train the new modules. The two losses are a cross-model alignment loss which aims to alight the speech and text modalities, and a (simplified) KL divergence loss on the distribution of text and speech outputs. The authors evaluate the paper on 3 groups of tasks, which are spoken question answering, speech classification and speech to speech translation. In all 3 task groups the method reaches state of the art results and surpassed the baseline methods. 

Overall, this paper shows a significant contribution and I recommend to accept it.

### Strengths
1. The proposed method is novel and easy to reproduce.
2. Evaluations show strong results on a wide variety of tasks. 
3. The paper is clearly written. 
4. Authors use publicly available datasets and fine-tuned models.

### Weaknesses
1.  **Limited Novelty:** Although the authors suggest an "alternative paradigm" for aligning speech inputs to text-based LLMs, similar approaches involving distillation text responses for cross-modal alignment have already been explored in works like BLSP [1] and AudioChatLlama [2]. A more detailed discussion and comparison with these works would help clarify the unique contributions. Specifically, the claim of retaining instruction-following abilities through self-knowledge distillation is not novel, as BLSP also employs a similar approach. The distinction between token-level distillation in BLSP and representation-level distillation in the current work needs further elaboration to justify the novelty of the proposed method.
2.  **Potential Limitations of Q-Former as Modality Adapter:** DiVA employs a Q-Former as the modality adapter to convert Whisper outputs into tokens. However, recent research in Vision-Language Models suggests that Q-Former can introduce semantic deficiency and "redundant double abstraction," making it less effective than simpler alternatives like MLP with average pooling [3]. Furthermore, the fixed number of query tokens restricts the model’s ability to process speech of varying lengths, potentially limiting its adaptability. The paper does not adequately address the potential information bottleneck introduced by the fixed number of query tokens, especially for longer speech inputs. The authors should provide a more detailed analysis of how the Q-Former handles variable-length speech inputs and justify their choice over simpler alternatives.
3.  **Unclear Basis for Performance Gains:** The claim that DiVA outperforms SOTA models like Qwen2-Audio may be misleading, given that DiVA builds on Llama-3—a stronger backbone than Qwen2-Audio’s Qwen-7B. This discrepancy makes it difficult to attribute performance gains solely to the proposed training method. Including the text-only performance of the backbone models (Llama-3 / Qwen-7B) or training DiVA on the same backbone as Qwen2-Audio could clarify the source of the observed improvements. The performance gains could be primarily attributed to the stronger backbone model rather than the proposed training method. A more rigorous comparison is needed to isolate the impact of the proposed approach.

### Questions
1. How is speech generated from the model output?
2. How is the quality of the output speech compared with the ground truth speech? 
3. it is stated that without the KL-divergence loss the speech output is incoherent, how was this measured?
4. Are there any audio samples from the model?
5. In what voices is the model able to generate speech?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel approach for training Speech LLMs in the absence of explicit instruction-following data. The authors introduce a method to transfer the instruction-following and conversational capabilities of text-based LLMs to speech-based models by leveraging only ASR data. Specifically, the proposed approach aligns input tokens using a cross-modal token alignment loss and output representations via embedding distillation loss, effectively bridging the modality gap between speech and text. Experimental results demonstrate that this method generalizes well to downstream tasks, including spoken QA and speech translation.

### Strengths
1.  The cross-modal alignment approach effectively retains general instruction-following abilities, addressing the common issue of forgetting in supervised fine-tuning (SFT).
2.  The Distilled Voice Assistant (DiVA) surpasses previous SOTA models, such as Qwen2-Audio, with significantly lower resource requirements.
3.  A qualitative user study shows DiVA’s strong alignment with human preferences in conversational quality.
4.  Ablation analysis confirms the distinct contributions of cross-modal token alignment and embedding distillation loss to DiVA’s performance.

### Weaknesses
 - Lack of Novelty: The paper’s distillation approach lacks originality and does not go beyond established self-supervised and cross-modal transfer methods. Its reliance on prior distillation techniques without meaningful innovation limits the work's impact.
- Missing Comparisons to Key Similar Work: The paper does not compare DiVA to highly relevant models, such as those using cross-entropy on target sequences or alternative distillation methods, failing to clarify any advantages over standard methods in the field [1, 2, 3].
- Insufficient Literature Survey: The paper omits numerous relevant works, resulting in a limited survey that neglects essential context for DiVA’s approach within the broader Speech LLM and instruction-following literature.
- Paralinguistic Claims: Assertions about capturing paralinguistic features (e.g., sarcasm, emotion) are questionable given that DiVA’s speech embeddings are mapped to text-like embeddings, likely relying more on text semantics than true paralinguistic cues.

### Questions
Questions:
1. In Section 3.1, the authors state that they use the decoder weights of Whisper to initialize the Q-Former’s _cross attention_. However, in Section 3.2.1, it’s mentioned that the speech tokens are processed with _causal attention_ in Whisper's decoder. This seems contradictory and is confusing. Could the author clarify the architecture of the Q-Former adapter? 
2. In Section 3.2.1, the cross-modal token alignment loss is applied only to the last $N$ tokens. However, this choice is unclear since Q-Former’s output tokens lack causal relationships. Additionally, the number of speech tokens $Q$ is defined as a hyperparameter, so the assumption that $Q>N$ may not hold for all inputs during inference. Could the author provide further justification for these design choices and proofs for the assumption about token counts?
3. In Section 3.2.1, the author claim that the additional $Q-N$ token provide information bandwidth for other information. However, I see no evidence to support this claim. Is there any statistic on the number of tokens that did not undergo alignment during training? If so, how does dropping these tokens affect the model's performance? 
4. In Section 3.2.2, the authors claim that the proposed $L_2$ loss can be computed more efficiently than KL divergence. Could additional evidence on training costs (e.g., computation time or resource usage) be provided to support this claim?
5. The ablation study indicates that the token alignment loss aids the model in adhering to text instructions. However, this difficulty in following text instructions might stem from DiVA being trained solely on speech inputs without accompanying text instructions. Could incorporating text instructions before speech tokens during training improve performance? Furthermore, if this modification were implemented, would the token alignment loss still be necessary, or could it be reduced or omitted?

Typos and minor mistakes:
1. In Table 1, the base LLM for Qwen 2 Audio Instruct is listed as Qwen2 Instruct. However, according to the technical report, the correct base model should be Qwen-7B. 
2. In Equation (1), the subscripts in the summation notation should start from 1.
3. In Section 3.2 line 247, "L2" should be $L_2$

[1] Chu Y, Xu J, Yang Q, et al. Qwen2-audio technical report[J]. arXiv preprint arXiv:2407.10759, 2024.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes the Distilled Voice Assistant (DiVA), a Speech Large Language Model (LLM) trained on ASR data alone to enhance instruction-following abilities through self-supervised distillation. The authors align DiVA’s responses with those of a text-only LLM to enable cross-modal transfer of instruction adherence. However, the approach does not present substantive methodological innovation, as it closely mirrors existing distillation and instruction-following techniques. Furthermore, the work critically lacks comparisons to similar method in this domain, failing to substantiate its claimed improvements over key baseline methods.

### Strengths
- The use of ASR data alone to improve instruction-following behavior could offer cost benefits by reducing dependence on annotated instruction data.
- DiVA’s evaluation across diverse benchmarks provides a quantitative assessment of the model’s instruction-following performance.

### Weaknesses
- Lack of Novelty: The paper’s distillation approach lacks originality and does not go beyond established self-supervised and cross-modal transfer methods. Its reliance on prior distillation techniques without meaningful innovation limits the work's impact.
- Missing Comparisons to Key Similar Work: The paper does not compare DiVA to highly relevant models, such as those using cross-entropy on target sequences or alternative distillation methods, failing to clarify any advantages over standard methods in the field [1, 2, 3].
- Insufficient Literature Survey: The paper omits numerous relevant works, resulting in a limited survey that neglects essential context for DiVA’s approach within the broader Speech LLM and instruction-following literature.
- Paralinguistic Claims: Assertions about capturing paralinguistic features (e.g., sarcasm, emotion) are questionable given that DiVA’s speech embeddings are mapped to text-like embeddings, likely relying more on text semantics than true paralinguistic cues.



1. Fathullah, Yassir, et al. "AudioChatLlama: Towards General-Purpose Speech Abilities for LLMs." Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers). 2024.
2.  Wang, Chen, et al. "Blsp: Bootstrapping language-speech pre-training via behavior alignment of continuation writing." arXiv preprint arXiv:2309.00916 (2023).
3. Wang, Chen, et al. "BLSP-KD: Bootstrapping Language-Speech Pre-training via Knowledge Distillation." arXiv preprint arXiv:2405.19041 (2024).

### Questions
- The authors should clarify the differences between this model and an ASR-LLM cascade, as mapping speech to text-like tokens questions both novelty and latency gains.
- Single-token predictions seem insufficient to capture temporal dynamics, potentially reducing DiVA’s effectiveness for tasks that require detailed temporal context.

### Soundness
2

### Presentation
3

### Contribution
2
