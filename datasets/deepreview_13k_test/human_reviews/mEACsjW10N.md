# MIO: A Foundation Model on Multimodal Tokens

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
In this paper, we introduce MIO, a novel foundation model built on multimodal tokens, capable of understanding and generating speech, text, images, and videos in an end-to-end, autoregressive manner. While the emergence of large language models (LLMs) and multimodal large language models (MM-LLMs) propels advancements in artificial general intelligence through their versatile capabilities, they still lack true any-to-any understanding and generation. Recently, the release of GPT-4o has showcased the remarkable potential of any-to-any LLMs for complex real-world tasks, enabling omnidirectional input and output across images, speech, and text. However, it is closed-source and does not support the generation of multimodal interleaved sequences. To address this gap, we present MIO, which is trained on a mixture of discrete tokens across four modalities using causal multimodal modeling. MIO undergoes a four-stage training process: (1) alignment pre-training, (2) interleaved pre-training, (3) speech-enhanced pre-training, and (4) comprehensive supervised fine-tuning on diverse textual, visual, and speech tasks. Our experimental results indicate that MIO exhibits competitive, and in some cases superior, performance compared to previous dual-modal baselines, any-to-any model baselines, and even modality-specific baselines. Moreover, MIO demonstrates advanced capabilities inherent to its any-to-any feature, such as interleaved video-text generation, chain-of-visual-thought reasoning, visual guideline generation, instructional image editing, etc.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a discrete token-based foundation model to unify understanding and generation capability in four modalities: speech, text, images, and videos with a proposed four-stage training recipe.

### Strengths
- The paper explores the potential of unifying four different modalities in a DIDO manner using existing tokenizers within a single causal MLLM.
- It also enables the generation of multimodal output in interleaved sequences.

### Weaknesses
- The paper demonstrates limited novelty in comparison to existing work within the research community.
- The overall performance of the proposed model is less competitive and lacks comprehensiveness. For example:
  - In the image understanding task, the dual-modal baselines used for comparison are relatively weak, with some considered obsolete.
  - In the image generation task, the reliance on the CLIP score metric is limiting, as it primarily focuses on text alignment and overlooks important aspects like structural integrity and aesthetics. Additionally, it has been noted to be less aligned with human preferences [1-3].
- There is a lack of both qualitative and quantitative ablation or analysis to justify key model design choices, such as the tokenizer selection, data composition, and training setup.

[1] Kirstain, Yuval, et al. "Pick-a-pic: An open dataset of user preferences for text-to-image generation." Advances in Neural Information Processing Systems 36 (2023): 36652-36663.

[2] Xu, Jiazheng, et al. "Imagereward: Learning and evaluating human preferences for text-to-image generation." Advances in Neural Information Processing Systems 36 (2024).

[3] Wu, Xiaoshi, et al. "Human preference score: Better aligning text-to-image models with human preference." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.

### Questions
Please refer to the weaknesses.

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
4

### Summary
This paper introduces a new multimodal foundation model called MIO. Multimodal foundation models are essential tools for related research, similar to the role of SD in text-to-image tasks. Although this resembles a systems engineering process rather than a novel discovery, the pipeline is clear and informative. The bottleneck, such as the token length gap between image and audio, is intriguing and has been partly resolved in this paper.

### Strengths
1. This paper systematically analyzes the limitations of current MLLM models and focuses on their critical aspect: any-to-any understanding and generation capabilities.
2. This paper examines images, videos, and speech to explore how to create a generalized model for all modalities while noting differences among them, such as variations in token length distribution.
3. This paper compares MIO with various existing MLLM models across different tasks to showcase its effectiveness.

### Weaknesses
1. This paper uses speech-enhanced pretraining to address variations in token length distribution. However, this approach is more of a patch than a well solution.
2. This paper states that "GPT-4o has showcased... However, it is closed-source." Therefore, will MIO be made publicly available? We do not require an additional closed-source copy of GPT-4o for research purposes.
3. This paper aims to address any-to-any understanding and generation. It should possess capabilities beyond existing methods. For example, can this model generate a talking-hand video in a few-shot setting that encompasses text understanding, as well as video and speech generation?

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel multimodal foundation model named "MIO" to understand and generate speech, text, images, and videos in an end-to-end, autoregressive manner. MIO is built on multimodal tokens across four modalities and undergoes a four-stage training process, including alignment pre-training, interleaved pre-training, speech-enhanced pre-training, and comprehensive supervised fine-tuning on diverse textual, visual, and speech tasks. The model demonstrates competitive performance compared to previous models and showcases advanced capabilities such as interleaved video-text generation and chain-of-visual-thought reasoning.

### Strengths
1. Similar to GPT-4o, the proposed "MIO" model is capable of understanding and generating multimodal contents across text, image, speech, and video modalities, which is a notable advancement.

2. To address the disparity of different modalities, the paper proposes a three-stage pretraining process, including alignment, interleaving, and speech ability enhancement. Experiments show that with such a design, the model can generate various modality contents in a unified model.

3. MIO exhibits advanced features such as interleaved video-text generation and visual guideline generation.

4. The authors will release the model, which has the potential to contribute to society.

### Weaknesses
1. This paper heavily relied on each modality's existing tokenizer or detokenizer, so it is restricted by their drawbacks. For example, SpeechTokenizer, although it provides a good semantic and acoustic discrete representation of a waveform, is RVQ-based and has many codebooks. So speech generation is inefficient (with 200hz).

2. As the paper claims multi-modal tokens for LLM, although it focuses on video/speech/image understanding and generation, it is necessary to evaluate the text-related benchmarks, i.e., MMLU, MMLU-Pro, GPQA etc. Please follow the practice of Llama[1] and Qwen[2] and compare your models with similar open-source models (e.g., Llama3 8B).
- [1] Dubey, Abhimanyu, et al. "The llama 3 herd of models." arXiv preprint arXiv:2407.21783 (2024).
- [2] Yang, An, et al. "Qwen2 technical report." arXiv preprint arXiv:2407.10671 (2024).

3. The authors propose a three-stage pretraining mechanism with a low ratio to a high ratio of speech tokens to tackle the disparity among different modalities.
* 3.1 Please conduct ablation experiments to demonstrate the effectiveness of the proposed method. In detail, you can compare the three-stage pretraining with one-stage pretraining. Then the one-stage pretraining's speech ratio can vary from low to high. If pretraining on the whole dataset is unaffordable, you can conduct it on a reasonable subset.
* 3.2 Usually changing the training data ratio may cause unstable results. For example, from stage 1 to stage 3, the text ratios decrease largely, thus leading to the degradation of text generation ability. Can you provide the detailed training/validation loss curve of each modality for each stage? Some evaluation results such as teacher-forcing ppl (or you can follow the practice of llama3[1] to evaluate the performance of pretrained model) are also helpful.
- [1] Dubey, Abhimanyu, et al. "The llama 3 herd of models." arXiv preprint arXiv:2407.21783 (2024).

4. For speech, the paper only conducts experiments on TTS/ASR. But as the paper claims to address the gap of GPT-4o, the most interesting and important ability, speech dialogue, is not included. In TTS/ASR tasks, the model is given textual/speech content mapping, so they can not demonstrate speech ability like GPT-4o. So I think it is an over-claim.

Furthermore, you can conduct speech-to-speech task (an example is llama-omini[1]), and evaluate it on speech-to-speech benchmarks [1]
- [1] Fang, Qingkai, et al. "Llama-omni: Seamless speech interaction with large language models." arXiv preprint arXiv:2409.06666 (2024).

5. For ASR experiments, the results are not good enough. WER 6.3 is relatively high[1]. I think the first layer of SpeechTokenizer may lose some semantic information. Why did the instructed model perform worse (6.3 --> 10.3)?

- [1] https://github.com/espnet/espnet/blob/master/egs/librispeech/asr1/RESULTS.md

6. For TTS experiments, the experiments are not convincing. I recommend following the evaluation practice of zero-shot TTS experiments[1,2,3], including 1) speaker similarity, 2) speech quality, 3) robustness (WER), and some other aspects. I also recommend evaluating on more than one benchmark.

- [1] Chen, Sanyuan, et al. "VALL-E 2: Neural Codec Language Models are Human Parity Zero-Shot Text to Speech Synthesizers." arXiv preprint arXiv:2406.05370 (2024).
- [2] Le, Matthew, et al. "Voicebox: Text-guided multilingual universal speech generation at scale." Advances in neural information processing systems 36 (2024).
- [3] Ju, Zeqian, et al. "Naturalspeech 3: Zero-shot speech synthesis with factorized codec and diffusion models." arXiv preprint arXiv:2403.03100 (2024).
- [4] Jiang, Ziyue, et al. "Mega-TTS 2: Boosting Prompting Mechanisms for Zero-Shot Speech Synthesis." The Twelfth International Conference on Learning Representations. 2024. 

7. It is difficult to understand the demonstration cases, especially for speech (i.e., I can not listen to the real samples). I recommend preparing an anonymous demo page instead of only several pictures for the case study. An example is https://aka.ms/valle2 for VALL-E 2.

### Questions
Please see the weakness.

### Soundness
2

### Presentation
3

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
The paper introduces MIO, a novel open-source, any-to-any multimodal foundation model designed for understanding and generating content across four modalities: text, images, speech, and video keyframes. Built with a Discrete-In-Discrete-Out (DIDO) approach, MIO leverages pretrained multimodal tokenization and a four-stage training pipeline to ensure robust cross-modality performance.

### Strengths
1. MIO introduces a novel approach as a foundation model tailored for interleaved cross-modality generation, advancing current capabilities in multimodal large language models.

2. By utilizing pretrained multimodal tokenizers, MIO enables scalable and efficient parallel training on interleaved multimodal data, enhancing its adaptability across diverse input types.

3. As a foundation model, MIO offers substantial potential for further research and development in multimodal large language models and related downstream tasks.

### Weaknesses
1. Qualitative comparisons with other baselines are missing. One of the main differences between MIO and Emu is the change from CICO to DIDO, and Table 4 shows that MIO performs better in image generation. The paper can be enhanced by showing the qualitative comparisons with other models, like Emu.

2. Need more clarification on multimodal inference. During the inference time, how does the model output fix-length image tokens (like one image should have 32 tokens) and speech tokens, especially for videos? Furthermore, do authors use any strategies to promise the multimodal tokens within their vocabulary?

3. Need more explanation on results. From table 3, MIO has better performance on image understanding with fewer parameters (7B vs 80B) even compared with some works that mainly focus on image understanding, like InstructBLIP and Flamingo. Can authors analyze which part led to this outperformance? Also, MIO outperforms Emu on several benchmarks. Does this indicate DIDO is better than CICO in both image generation and understanding?

4. The video generation in MIO seems more like video keyframe generation, which only maintains semantic and style consistency.

### Questions
1. One related work, NextGPT [1], is missing, which also can do text, speech, and video generation. Can authors please claim the difference between MIO and this work?

2. Why is Emu2 missing in the results?

[1] Wu, Shengqiong, et al. "Next-gpt: Any-to-any multimodal llm." arXiv preprint arXiv:2309.05519 (2023).

### Soundness
3

### Presentation
2

### Contribution
3
