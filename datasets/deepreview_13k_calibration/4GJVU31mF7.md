# Unified Music-Language Model for Symbolic and Waveform Integration

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 6, 3, 3

## Abstract
Music is a unique and essential modality constituting human life, presenting challenges for multimodal advances due to its complex structure and intricate details. Recent Music Language Models (MuLMs) facilitate music understanding and generation by leveraging the inherent knowledge and reasoning capabilities of pre-trained Language Models (LMs), yet they overlook the complementary benefits of different music representations. To this end, we propose a unified music language model, named UniMuLM, form the existing approach of using a single representation to multiple music representations. Concerning the unification, we address the challenges of missing modalities and unstable training to adapt different scenarios. Specifically, we integrate symbolic, waveform music, and textual instructions into an LM and design a bar-level tokenizer to explore the fine-grained correlations between different modalities. Moreover, we propose a multi-stage training strategy to progressively enhance this synergy. Trained on open-source datasets, UniMuLM demonstrates superior performance compared to SOTA methods across five music tasks, evaluated on nine benchmark datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents UniMuLM, a Unified Music-Language Model designed to integrate symbolic music, waveform music, and textual instructions into a cohesive framework. The model addresses the challenges posed by the distinct representations of music (symbolic notation vs. audio waveforms), aiming to leverage their complementary strengths. Key contributions include:

Unified Tokenization: Introduction of a bar-level tokenizer that aligns symbolic and waveform music representations to enable fine-grained, mutually reinforced understanding.

Multi-Stage Training Strategy: The model is trained in three stages to inject knowledge, align music representations, and fine-tune the system for various music-related tasks.

Comprehensive Evaluation: Demonstrates state-of-the-art (SOTA) performance across different music tasks, validating the effectiveness of integrating multiple music modalities.

### Strengths
Comprehensive Multimodal Integration: The model successfully combines symbolic and waveform music representations, addressing a major limitation in existing models and enabling better music understanding and generation.

Innovative Bar-Level Alignment: The bar-level tokenizer offers a novel approach to synchronizing symbolic and audio representations, improving the model’s ability to process and generate music in a contextually relevant manner.

### Weaknesses
1. Inconsistency and Misalignment in Title, Problem Formulation, and Paper Focus

The title, "Unified Music Language Model," suggests a comprehensive system capable of generating audio, which is misleading since the model does not generate audio directly. Instead, it is an "audio-informed, text-based music language model" that can handle both music description and symbolic music generation.
The problem formulation further contributes to the confusion, as it mainly addresses a music description problem. However, the actual contributions focus more on using audio information to enhance symbolic music generation and music understanding, indicating a disconnect between the proposed problem, the title, and the work's real impact.


2. Suboptimal Baselines and Limited Impact of SOTA Claims

The choice of baselines for music generation, such as ChatMusician and MUPT, undermines the significance of the model's claimed state-of-the-art performance. Both baselines are first-of-its-kind general-purpose multimodal music models, but with subpar generation quality compared to dedicated symbolic generation models like Music Transformer or the more advanced whole-song generation via hierarchical diffusion models.

A similar issue exists in the music understanding benchmarks. Using Mu-LLaMa as a baseline, while suitable for demonstrating language model integration, fails to compare favorably against specialized Music Information Retrieval (MIR) tools, which excel in task-specific performance. The broader question remains whether integrating music information into a text-based language model leads to genuinely superior performance.

Ultimately, the novelty of integrating music data into language models has become less groundbreaking. The field has matured, and the critical evaluation should focus on whether this integration yields better performance. Based on the provided demos, the symbolic music generation quality lags behind specialized models, and in music QA tasks, errors were evident, as seen in 2nd and 3rd showcased examples.

### Questions
1. one main weakness of existing text-based music LM (e.g. chatmusician) is that they can only answer the type of questions that they have been trained on (either in the pertaining stage or instruction fine-tuning state) and fail to generalize on new types of questions. Have you looked into this problem? (I am assuming that you use one fine-tuned model to handle all kinds of  text-based queries rather than applying one LoRA per type of query)

2. the bar-level alignment is interesting. How is the aligned data prepared -- synthesizing the ABC into audio or applying MIR tools to audio? Could you handle audio whose tempo is unstable, both in the training and inference stages?

### Soundness
3

### Presentation
2

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
This paper introduces a Unified Music-Language Model that integrates symbolic music and waveforms through bar-level tokenization inspired by bar-patching [1], addressing the issue that current music language models struggle to handle both notation and performance due to temporal scale inconsistencies. 
The proposed approach follows a three-stage training strategy. First, it incorporates music knowledge to warm up Llama-3 with foundational music theory concepts. Second, a bar-level tokenizer is trained on paired symbolic and waveform data using contrastive and reconstruction losses. Finally, LoRA-tuning is applied to adapt the model for various downstream tasks involving diverse music representations.
By uniting these two modalities, the model enhances both music understanding and generation capabilities, showing advantages over single-modality models in three downstream tasks: music theory injection, waveform-based music understanding, and symbolic music generation.

[1] Shangda Wu, Dingyao Yu, Xu Tan, and Maosong Sun. Clamp: Contrastive language-music pre-training for cross-modal symbolic music information retrieval. In ISMIR, pp. 157–165, 2023.

### Strengths
This paper introduces a music-language model capable of encoding cross-modality data for symbolic music and waveforms. It addresses the challenge of temporal consistency by using a bar-level tokenizer to align music waveforms with notation, employing contrastive and reconstruction losses to enhance alignment between symbolic and waveform information. 

The paper is well-written, with a clear and well-defined problem statement that makes the methodology and contributions straightforward and easy to understand. This work offers a valuable approach to unifying multiple input modalities in music through a unified tokenizer, paving the way for enhanced music understanding and more controllable music generation.

### Weaknesses
1. Limited Novelty in Modality Alignment: This paper is not the first to align audio waveforms with symbolic representations. For example, JASCO employs ‘nearest’ interpolation for chords and ‘linear’ interpolation for melody, resampling them to match EnCodec’s frame rate. To strengthen the paper’s contribution, it would be helpful to emphasize the specific advantages offered by your alignment strategy. For example, how your bar-level tokenization differs from or improves upon interpolation-based approaches in terms of preserving musical structure or handling different types of musical elements. Specifically, the paper should include experiments that demonstrate the ability of the proposed method to preserve musical structure, such as through transcription tasks that evaluate the accuracy of the recovered symbolic representation after encoding and decoding the waveform. 

2. Marginal Improvement on Waveform Music Understanding Tasks: The model demonstrates limited improvement over Mu-LLaMA on 3 out of 4 datasets for waveform music understanding tasks. This raises questions about the actual benefit of incorporating symbolic information to enhance waveform audio understanding. Providing further exploration or justification of the advantages of symbolic data for audio understanding would strengthen the paper. For example, you can provide a more detailed analysis of where and why your model shows improvements or limitations compared to Mu-LLaMA  and discuss specific examples or task types where symbolic information seems to help or hinder performance. It would be beneficial to analyze the types of questions where the model performs well and poorly, and whether these patterns correlate with the presence or absence of symbolic information.

3. Ignorance of Difference between Real-world Waveform and Synthesized Waveform: the alignment stage does not train on the real-world waveform, which might perform different from the synthesized waveform. I understand large-scale pair data lacks, but you can still use some data augmentation strategies such as using different soundbanks to render the symbolic music, or applying some transcription tools (e.g. MT3) to get the coarse symbolic representation and fine-grain them to ensure valid format via GPT-4. I think it would be better to discuss in your paper the potential impact of using synthesized vs. real-world waveforms on their model's performance. The paper should also include a discussion of the limitations of using synthesized data and how this might affect the generalizability of the model to real-world audio.

4. Minor Typos: There are minor typos in the description of Figure 3, such as “constrastive loss” and “corss-reconstruction losse.” In Section 4.3, symbols in formula (4) do not correspond with the symbols in the textual explanations above.

### Questions
1.	Dataset Construction Process: Could you clarify the dataset construction process, particularly regarding any differences in cleaning and downsampling strategies across datasets? A detailed explanation of the sampling methods used for each dataset would enhance transparency.

2.	Multi-Track Music Processing Details: While the paper discusses bar-level tokenization for single-track music, it lacks details on aligning multi-track waveforms with ABC notation. Could you provide more information on how alignment is managed for multi-track music?

3.	Exploration of General Model’s Music Knowledge: Given that models like GPT-4 and GLM-4 are noted for their in-context learning capabilities, have you explored prompt engineering with these models to assess their music theory knowledge? This could offer a fairer basis for comparison.

4.	Music Understanding Performance Analysis: The UniMuLM model performs better on shorter-text datasets compared to longer-text ones. Could you elaborate on this performance variation? Additional analysis would provide valuable insights into the underlying factors.

5.	More Details about the Subjective Evaluation: how many participants joined the subjective test? What are their music backgrounds? What’s more, your demo page only provides single-track samples and what about the multitrack generation results? How do you ensure consistency across different raters.

6.	About the Waveform Music Generation: intuitively, when seeing your paper’s title, I expect to see the comparison between text-waveform and text-symbolic generation. From my perspectives, that’s the main challenge and concern of symbolic-waveform music alignment work, to support the controllable waveform generation and more diverse symbolic generation simultaneously by getting the embeddings from two domains closer. Therefore, if possible, please discuss what are your initial findings, results or the challenges you've encountered within the text-waveform task, as mentioned in your future work part. It really benefits the whole AI music community.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a fine-tuned language model for music understanding and generation. The music representations used in this paper are text-like ABC format, audio format, and a representation jointly learned from symbolic and audio domain music data. The input to the model is text and music, and the output is text or music in ABC format. The model demonstrates superior performance in some tasks in generation and understanding.

### Strengths
The proposed model incorporates data from multiple modalities and provides a general interface for generation and understanding. Music features from the audio domain and the symbolic domain are considered and proved helpful for the task.

### Weaknesses
1. The title is misleading, as it suggests the language model itself integrates multiple modalities, whereas the actual integration occurs primarily at the tokenization level.
2. The paper's writing lacks clarity and rigor. Figure 3 is confusing because there are no distinctions between inputs and outputs and no explanation of color coding for adapters and tokens. The notation is sloppy; symbols like L_c appear in the figure but are not defined in anywhere else in the paper. In the main text, terms like LM(), Adapter(), and Symbolic-Encoder() are presented as informal expressions rather than proper mathematical functions.
3. The integration of audio and symbolic data is bounded by the fact that paired audios are synthesized. The quality in the demo page is not convincing.
4. Figure 1 feels promotional, yet it's hard to tell what are the nine tasks after finish reading (e.g., what is MCQ-inpainting). Additionally, the experiments only assess performance at a superficial level. The paper would benefit from deeper analysis to demonstrate what the model actually gains from modality integration. Providing additional demos, case studies, and comparisons either in the appendices or on the demo page would strengthen the evaluation.

### Questions
Questions are mentioned in the weaknesses.

### Soundness
2

### Presentation
1

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
The paper presents UniMuLM, a unified music language model designed to address the limitations of existing music language models (MuLMs) that typically rely on a single representation type. UniMuLM integrates symbolic music, waveform audio, and textual instructions through a novel bar-level tokenizer to facilitate fine-grained, multi-modal music understanding. To handle the complexities of multimodal alignment and stabilize training across these varied representations, the authors implement a multi-stage training strategy. Their empirical evaluation on nine music-related tasks indicates UniMuLM’s performance improvements over current state-of-the-art methods, underscoring the benefits of unified, multi-representational learning for advancing MuLMs.

### Strengths
The authors introduce a novel and well-motivated approach that leverages multiple music representations for a unified model, which is an important advancement for multimodal music understanding. The proposed method and experimental design appear to be robust, addressing significant challenges within the field and offering promising results on music theory, acoustic music understanding and symbolic music generation tasks.

### Weaknesses
The paper’s primary claims highly overstate the experimental outcomes due to the following reasons.
* The claim of 9 music tasks might be miscounting. Or maybe the author (over)claims the four music captioning datasets as four tasks (theory, caption, QA and generation). According to my understanding, it should be a music theory benchmark, three music caption/description datasets, 1 musical, and 2 types of music generation with 2 different types of evaluation methods. Please clarify what are the nine different tasks.
* as the evaluation lacks comparisons with recently released in the past 9 months, advanced baselines, such as SALMONN, GPT-4o and Qwen2-audio, are relevant to benchmark improvements, which may provide much better results on music theory and music captioning. For example, Qwen-audio and SALMONN tech reports include the sota performance on music captioning and GPT-40 is well-known for its audio instruction following capability
* Additionally, several tasks are missing comprehensive evaluation metrics (e.g., BERT-score and METEOR for music captioning, which are widely used and much more persuasive compared to the BELU score reported in this paper).
* The paper claims the alignment of 3 modalities, but it does not explore the direct alignment of symbolic and audio modalities without intermediate text, e.g. audio transcription to ABC notation, which limits insights into tasks. 
* Further, ablation studies are absent for the loss functions introduced in stage two of training, leaving uncertainty around the necessity and optimal weighting of each component. This does not make the methodology proposed in stage 2 solid. You can run the experiments on changing the loss weights or delete part of the loss
* The author claims the impact of bar-level tokenization. However, there is no ablation study on not using such tokenization. Besides, the author does not clarify which dataset requires bar-level information for the model to evaluate. Please clarify why the 4 or 9 tasks are contributed by the bar-level information you provided and show the experimental results if the bar-level tokens indeed help. Maybe it does not align well or screw up the performance by increasing the length of tokens

### Questions
Typographic and Formatting Issues:
* The numbering in the paper is inconsistent (e.g., Section 3 contains only one paragraph, Section 4.1 includes only 4.1.1).
* Figure 1’s color distinctions are difficult to discern, and Figure 3(a) is complex, potentially making it harder to interpret than the accompanying text.
* Formulae could benefit from simplification. Besides, some notation feels excessive or potentially confusing. For instance, is “Zbar” intended to be “Z_{bar}”?
* In Table 1, could the authors clarify the meanings of "Quantity" and "Sampled"? Do these refer to token count and instruction-answer pairs?
* Many typo errors

Experimental & Dataset Details:
* Please clarify the precision during training. Is the 4-bit training precision sufficient? Half-precision training is typically float16 (16-bit), and 4-bit precision may impact training stability or gradient calculations. Did the authors consider gradient overflow or stability issues, or was 4-bit precision specifically chosen for other reasons? (Or maybe 4B=32bit, which is the common training precision)
* How was MIDI data transformed into ABC notation, and how was bar/beat-level annotation achieved? Transcribing MIDI to bar-level music sheet is not trivial. The quality of this annotation could significantly impact bar-level information integrity.

### Soundness
2

### Presentation
2

### Contribution
3
