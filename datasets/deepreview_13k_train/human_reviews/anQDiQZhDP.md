# Vevo: Controllable Zero-Shot Voice Imitation with Self-Supervised Disentanglement

- Decision: Accept
- Scores: 5, 3, 8, 6

## Abstract
The imitation of voice, targeted on specific speech attributes such as timbre and speaking style, is crucial in speech generation. However, existing methods rely heavily on annotated data, and struggle with effectively disentangling timbre and style, leading to challenges in achieving controllable generation, especially in zero-shot scenarios. To address these issues, we propose Vevo, a versatile zero-shot voice imitation framework with controllable timbre and style. Vevo operates in two core stages: (1) Content-Style Modeling: Given either text or speech's content tokens as input, we utilize an autoregressive transformer to generate the content-style tokens, which is prompted by a style reference; (2) Acoustic Modeling: Given the content-style tokens as input, we employ a flow-matching transformer to produce acoustic representations, which is prompted by a timbre reference. To obtain the content and content-style tokens of speech, we design a fully self-supervised approach that progressively decouples the timbre, style, and linguistic content of speech. Specifically, we adopt VQ-VAE as the tokenizer for the continuous hidden features of HuBERT. We treat the vocabulary size of the VQ-VAE codebook as the information bottleneck, and adjust it carefully to obtain the disentangled speech representations. Solely self-supervised trained on 60K hours of audiobook speech data, without any fine-tuning on style-specific corpora, Vevo matches or surpasses existing methods in accent and emotion conversion tasks. Additionally, Vevo’s effectiveness in zero-shot voice conversion and text-to-speech tasks further demonstrates its strong generalization and versatility. Audio samples are available at https://versavoice.github.io/.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Vevo, a zero-shot voice imitation framework with controllable timbre and style, featuring a fully self-supervised approach that progressively decouples timbre, style, and linguistic content of speech using VQ-VAE tokenizers with an information bottleneck technique. Vevo outperforms existing models in accent and emotion conversion, particularly excelling in zero-shot tasks, demonstrating its versatility and robustness.

### Strengths
1. This paper introduces a unified speech synthesis framework, Vevo, capable of handling zero-shot timbre, style, and voice imitation tasks. It provides clear and precise definitions of timbre and style and achieves its objectives through a two-stage modeling strategy: Content-Style Modeling and Acoustic Modeling.

2. By experimenting with the codebook size of self-supervised speech representations quantized via VQ-VAE, the paper follows the theory of information bottleneck and implements a progressive information filtering approach. This results in a simple yet efficient self-supervised method to gradually decouple timbre, style, and linguistic content.

3. Experiments indicate that Vevo matches or exceeds the performance of comparable state-of-the-art speech generation models across various zero-shot scenarios, showcasing its strong generalization and versatility.

### Weaknesses
1. The self-supervised VQ-VAE tokenizer for content and content-style information requires meticulous parameter tuning, such as continually adjusting the codebook size. Balancing the performance between the content and content-style tokenizers involves trade-offs, making it a suboptimal choice with potential risks. It might be beneficial to compare this with supervised tokenizer models, such as extracting content and content-style tokens directly using open-source models like FACodec [1], to evaluate the impact on model performance and make more informed decisions.

2. In the Content-Style to Acoustic stage, the paper utilizes a conditional flow matching model with a masking strategy, relying on unmasked portions of mel spectrograms to guide the modeling of masked timbre, linguistic content, and acoustic style. This stage may encounter issues of information leakage, where the model might learn the speaker's context from the provided unmasked mel portions during training, aiding in better generation of masked mel segments. During inference, while aiming to replicate the timbre reference, the model might inadvertently also learn consistent style information.

### Questions
1. The paper notes that "both the content and content-style tokenizers are trained on a 100-hour subset randomly sampled from the full 60K-hour dataset." Training on such a small subset raises questions about the model's generalization and robustness. How are these ensured given the limited training data?

2. Has the model been tested on datasets beyond audiobooks to evaluate its zero-shot voice generation capabilities, including timbre imitation, style imitation, and voice imitation?

3. Regarding the parameters in the conditional flow matching model, how is the "randomly mask ratio" determined, especially given that the paper reports a range of "70%-100%"?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper builds upon the foundational HuBERT representation model and explores the disentanglement of content tokens and content-style tokens by analyzing VQ codebook spaces of varying sizes. Based on this disentanglement, the authors propose a cascaded generation framework called Vevo (AR Transformer combined with Flow Matching), which successfully performs zero-shot timbre, style, and voice imitation tasks.

### Strengths
1. Exploring the unified approach to zero-shot timbre, style, and voice imitation tasks through disentangled representations is a meaningful attempt, although similar efforts have been made previously.
2. The novel approach of disentangling timbre, style, and content by analyzing different sizes of VQ codebook spaces is interesting, although it is difficult to provide strict evidence of its effectiveness.

### Weaknesses
1. It is challenging to guarantee strictly disentangled results when analyzing different sizes of VQ codebook spaces for timbre, style, and content.

 &nbsp; &nbsp; 1.1. The results may be biased by hyperparameter tuning in downstream tasks.

 &nbsp; &nbsp; 1.2. The authors should include comparisons with other disentanglement methods in Table 2, such as label-based    disentanglement techniques.

 &nbsp; &nbsp; 1.3. The differences in evaluation metrics between various codebook sizes, such as a SIM score improvement from 40 to 44, are minimal and insufficient to claim successful disentanglement. Specifically, the speaker similarity (S-SIM) to the reference speaker increases from 0.398 to 0.441 when reducing vocabulary size, which is not a substantial improvement. The authors also claim that timbre imitation improves with smaller vocabulary size, but this is not strongly supported by the results in Table 2.

 &nbsp; &nbsp; 1.4. The performance metrics in Table 2 for different codebook sizes show substantial gaps compared to the ground truth (GT).

2. The overall cascaded generation framework of Vevo is not highly innovative, as similar frameworks have already been proposed, such as SeedTTS and CosyVoice.

3. The unified definition of zero-shot timbre, style, and voice imitation tasks is not new, as seen in prior works like ControlSpeech and StyleFusion TTS.

4. The experimental results do not demonstrate significant performance gains. Furthermore, the baselines are relatively weak. At least, comparisons with open-source models like CosyVoice should be included. Additionally, comparing to FaCodec is unfair; a comparison with NaturalSpeech3 would be more appropriate

### Questions
1. I am unclear about the specific implementation details of the Vevo-Timbre and Vevo-Style versions. 

2. Will you be releasing the complete training and inference code, as well as the model weights?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a voice imitation approach supporting style information transfer at different granularities, including global timbre, accent, and emotion. The authors create varying sizes of information bottlenecks by VQ-VAE with different codebook sizes on self-supervised speech representations, obtaining speech representations with different levels of information. Upon these representations, the authors build a two-stage speech generation model composed of autoregressive and flow matching modules. Experiments demonstrate the effectiveness of this approach in voice imitation.

### Strengths
1. The idea of using codebooks of varying sizes to control the width of the information bottleneck is impressive, and the study on the order that information are filtered out with the shrinking codebook sizes are highly meaningful.

2. The experimental results are promising, and the demo sounds impressive.

### Weaknesses
I do not see any significant flaws in the paper for now. I may raise new questions based on the feedback from other reviewers.

### Questions
Did the authors validated their theory regarding the relationship between VQ-VAE codebook size and the information contained in representations on other self-supervised speech representations (such as wav2vec2, w2vbert)? Are their conclusions consistent?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses challenges in voice imitation for speech generation, proposing Vevo—a zero-shot framework with controllable timbre and style. It operates in two stages and uses a self-supervised dicoupling approach with VQ-VAE tokenizer. Trained on 60K hours of audiobook data, Vevo outperforms existing methods and shows effectiveness in zero-shot conversion and text-to-speech, demonstrating generalization and versatility.

### Strengths
1. Vevo can do both VC and TTS tasks and can simultaneously control both timbre and style.
2. The experiments are very detailed and the conclusions prove the effectiveness of the proposed model.
3. This paper is well structured and easy to read, and the demo sounds good.

### Weaknesses
Although the paper has done a lot of research on the comparison and selection of representations, it seems that there is relatively little innovation.

### Questions
1. The content and content-style tokenizers are trained only on 100-hour data. Is the amount of data sufficient? Has a comparison of different amounts of data been made?
2. In section 4.1, "When K reduces further to 32, in addition to timbre, most style information is also filtered out", FPC drops from 0.764 to 0.706, that's not a big difference. How can it be proved that the style has been removed?

### Soundness
3

### Presentation
3

### Contribution
2
