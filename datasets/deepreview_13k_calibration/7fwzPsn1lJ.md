# LLark: A Multimodal Foundation Model for Music

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Music has a unique and complex structure which is challenging for both expert humans and existing AI systems to understand, and presents unique challenges relative to other forms of audio. 
We present LLark, an instruction-tuned multimodal model for music understanding. We detail our process for dataset creation, which involves augmenting the annotations of diverse open-source music datasets and converting them to a unified instruction-tuning format. We propose a multimodal architecture for LLark, integrating a pretrained generative model for music with a pretrained language model. 
In evaluations on three types of tasks (music understanding, captioning, and reasoning), we show that our model outperforms existing baselines in zero-shot generalization for music understanding, and that humans show a high degree of agreement with the model's responses in captioning and reasoning tasks. LLark is trained entirely from open-source music data and models, and we make our training code available along with the release of this paper.
Additional results and audio examples are at https://bit.ly/3ZyzbGG .

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This project uses a pretrained audio encoder, and a pretrained language encoder. A learned mapping of the audio encoder output to the embedding space of the language encoder is introduced. A learned output language decoder is also learned. All of this is trained by optimising a loss on (audio in, text in, text out) triples. These training triples are constructed with an LLM + some ad hoc filtering steps, and are basically q & a "what sort of song is this" etc.

The pieces are well known and this is largely an empirical study. The results are promising and the paper is easy to read.

### Strengths
The paper is easy to read, and the results look pretty good. Although it merely rehashes existing datasets and models, it seems like a nice combination and well thought out.

### Weaknesses
It's largely an empirical study / engineering type of project. The authors seem to say they will give code and data but no checkpoint.

### Questions
Have you included the latest results on the benchmarking tasks? I am not a specialist in this area and I am curious if other reviewers find missing comparisons.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents LLark, a multimodal foundation model for music understanding. It's trained using instruction-based tuning and metadata augmentation on open-source music datasets. LLark combines a pretrained audio encoder with a large language model, effectively merging language capabilities with traditional music information retrieval models for improved music understanding. LLark excels in various music tasks, showing impressive generalization capabilities. Human evaluators also show strong agreement with LLark's performance in captioning and reasoning tasks.

### Strengths
1.	This work blends the knowledge from audio understanding models with a touch of ChatGPT for LLaMA, addressing high annotation costs in the music domain by leveraging language models and pretrained MIR models.

2.	The model attains impressive results, particularly in reasoning tasks, showcasing its potential for practical applications.

3.	The incorporation of instruction tuning and metadata augmentation provides reusable insights within the realm of music information retrieval.

4.	The paper leverages publicly accessible, open-source, and permissively licensed music datasets for training, which ensures data accessibility and reproducibility.

### Weaknesses
1.	Section 1 mentions LLark's architecture as a contribution, but the integration of large language models (LLM) and domain-specific models has been previously explored in the literature [1-4], as properly cited in the paper. To strengthen the paper, consider providing a more detailed explanation of what sets LLark's architectural design apart from existing implementations, particularly concerning the specific fusion mechanisms between the audio encoder and the LLM, and how these differ from prior work.

2.	Limiting the audio encoder to 25-second clips (mentioned in Sections 4.1 and 7) is a notable drawback, as it lacks the understanding of important contextual information in real-world scenarios (most music audio is longer than 25 seconds), leading to potential misinterpretations and missed insights in audio content analysis. This limitation needs further discussion, including the impact on tasks requiring long-range temporal dependencies, such as understanding musical form or narrative.

3.	Section 4.2.1 should investigate how LLark's performance is affected by the features extracted from traditional MIR models [5], especially regarding temporal-related music properties like timestamped chords and beat grids. Additional ablation studies should be included to confirm the performance gain of metadata augmentation, focusing on the specific contribution of each type of metadata (e.g., key, tempo, and instrument labels) to the overall performance.

4.	In Sections 6.3 and 6.4, it’s ok to rely on human evaluation as we don't have holistic objective metrics to assess captioning and reasoning tasks. But leaning entirely on non-experts for this might not be the best call. It might be better to balance this out with some expert raters rather than going all-in on non-experts. The potential for bias and lack of musical expertise in the raters should be explicitly addressed, including the potential impact on the validity of the results.

5.	In Figure 4, the matching rates are quite low across all models (around the random guessing level), leading to questions about whether LLark's performance on certain tasks is only marginally better than random guessing. Section 6.4 attributes this result to “limitations in the musical expertise of the (non-expert) raters in our study," further emphasizing my previous concerns about relying solely on non-experts for human evaluation. This raises concerns about the reliability of the matching rates as a measure of performance.

6.	With no clear indication of randomness in option order (or maybe I missed?), such as whether LLark is consistently presented as the first option, this raises concerns about potential biases [6] in the evaluation results of GPT-4 in Sections 6.3 and 6.4. The paper should clarify the randomization procedure for the presentation of options during human and GPT-4 evaluations to ensure the validity of the results.

7.	Wrong citation in Appendix F: the ablation study used the CLAP developed by LAION [7], but wrongly cited the Microsoft one [8]. This made me confused for a while. Please correct the citation.

8.	In Appendix F, ablation studies may not offer a fair comparison due to the significant model size differences between CLAP [7] and Jukebox [9]. To assess temporal information's significance, please consider an additional ablation study where Jukebox's weights are still frozen but average pooling is applied to its output embeddings without preserving temporal information. This would more clearly isolate the impact of temporal modeling on the model's performance.

### Questions
1.	Why does the dataset contain 1.2M text samples and only 164K audio clips, despite there being only three types of tasks?

2.	Is LLark limited by the upper bounds of the MIR model's performance used for metadata augmentation, and if so, how does this limitation impact its performance?

3.	In Figure 4, all models seem to have low performance. Is it possible that the performance of baselines is lower than random guessing?

4.	Section 6.2 suggests that the improved genre performance of ImageBind-LLM [10] is attributed to genre tags used in pre-training. However, according to my knowledge, ImageBind [11] is trained on image-related pairs only, and there are no audio-text pairs used during pre-training. Why are genre tags relevant in this context?

5.	How many raters were involved in the human evaluations for captioning and reasoning tasks?

[10] Jiaming Han, Renrui Zhang, Wenqi Shao, Peng Gao, Peng Xu, Han Xiao, Kaipeng Zhang, Chris Liu, Song Wen, Ziyu Guo, et al. Imagebind-llm: Multi-modality instruction tuning. arXiv preprint arXiv:2309.03905, 2023.

[11] Rohit Girdhar, Alaaeldin El-Nouby, Zhuang Liu, Mannat Singh, Kalyan Vasudev Alwala, Armand Joulin, and Ishan Misra. Imagebind: One embedding space to bind them all. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 15180–15190, 2023.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper collects several common MIR tasks (captioning, tagging, tempo estimation, etc) under a common text-based formulation that allows them to be trained and evaluated via instruction-tuning a single LLM with audio conditioning. It presents a new model called LLark along with a number of experimental evaluations.

### Strengths
- modelling improvements on several MIR tasks
- presents a clear and compelling path for future MIR work in this direction
- comprehensive details on the data processing choices and implementation provided in the supplements
- technical details are clearly communicated with an emphasis on making things easy to reproduce

### Weaknesses
 - Some of the most impressive results in the paper are regarding the long-form text outputs - but this is also where the non-expert evaluations are limited, and where the negative side effects of LLM’s come into play. I think that lumping these together under the term “model hallucinations” loses important nuance about how this will play out when LLark gets deployed into products, etc. When I look at the outputs in the online supplement, I see really impressive text with lots of musical terms thrown in that are related to the track - but I think more focused evaluations with experts would immediately reveal that much of this captioning output is nonsense - and isn’t it creating a problem to have such nicely packaged up nonsense that to non-experts it looks right? That sense of authority and confusion is less of a problem with the pre-LLM baseline models. I understand that this kind of evaluation may be out of scope for this paper, and there’s room for critical follow-up work once the model is made open-source - But I can examples of this happening immediately in the online supplement, and I think it’s worth at least highlighting these kinds of things in the paper.  For example:

 -   under “How could a music producer recreate the sounds in this track? —> they would likely use a variety of synthesizers, both digital and analog” - that’s typical LLM word-salad stuff that in some cases seems harmless, but it’s super misleading! You definitely don’t need to go out and buy a bunch of analog synthesizers to produce that kind of track. 

- “What are some characteristics that potentially differentiate the song from other similar songs —> the use of the synthesizer as the main instrument…Additionally, the song's tempo of 120 BPM and the use of the E minor key… gives the song its own unique identity within the electronic genre” This is all nonsense - pretty much every song in the electronic genre features the synthesiser, 120 bpm is the least distinctive tempo you can choose, and E minor is a very typical key!

### Questions
Given the time to do it, how would you design an evaluation to address the kinds of issues raised under "weaknesses" above? How much of that can be communicated within this paper rather than left to future work?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a language-based music understanding model designed to excel in various music comprehension and retrieval tasks. The model's architecture is constructed by harnessing the power of the jukebox audio encoder and the Llama 2 text encoder. To create the training data, ChatGPT (or GPT-4) is employed to generate instructional texts based on music track metadata, encompassing information such as BPM, genre, chord progression, and key signature. This comprehensive model offers thorough analysis and understanding of music inputs. The authors showcase the impressive capabilities of their model, named 'Llark,' by demonstrating its high performance across a wide range of music-related tasks, including music genre classification, key signature classification, tempo estimation, and music captioning. Furthermore, the authors have dedicated a substantial portion of the appendix to provide in-depth insights into their experimental results and the data generation process.

### Strengths
The proposed LLark model stands out as a tool for tackling a wide array of music understanding and retrieval tasks. Notably, the realm of cross-modality models, particularly those bridging language and music, has remained relatively under-explored. The majority of existing models have primarily concentrated on text-image and general audio-text associations, leaving a gap in the field. This paper marks an initialization in the direction of language-based music understanding, utilizing LLM. The selection of music-related tasks employed to evaluate the capabilities of the LLark model is logical and well-founded.

### Weaknesses
However, there are several notable shortcomings in this paper concerning its overall motivation, technical novelty, and experimental design, which diminish its quality and hinder its acceptance at the ICLR conference.

First, the assertion that LLark serves as a foundational music model is overstated. Upon closer examination, LLark emerges as a language-based audio understanding model, enriched with music instruction-based data. It lacks significant technical novelty for the following reasons:

(1) The audio encoder (Jukebox) and text encoder (Llama 2) employed in LLark were introduced in previous works, and their training primarily relied on large-scale data pre-training. Consequently, the paper doesn't place substantial emphasis on advancing the early-stage representation learning of both audio and language models. The choice of these specific encoders, while leveraging their pre-trained capabilities, does not introduce any novel architectural modifications or training strategies tailored for music understanding. The paper does not explore alternative encoder architectures or modifications that could potentially improve performance in the music domain.

(2) The model architecture itself, present in both encoders, exhibits no novel adaptations to better suit the domains of music understanding or language comprehension. The paper uses a standard cross-modal architecture without any specific modifications to handle the unique characteristics of music, such as its temporal structure, harmonic relationships, or rhythmic patterns. This lack of domain-specific architectural innovation is a significant limitation.

(3) The instruction-based data generation process, while employed effectively, has been previously explored in various machine learning domains, including audio, as demonstrated by works such as LAION-CLAP [1] and WavCaps [2]. The method used for prompt creation in this paper does not introduce particularly novel design elements, potentially falling short of the requisite technical novelty standards for ICLR. The prompts used for data generation appear to be relatively straightforward and do not explore more sophisticated methods for eliciting complex musical understanding from the model.

Consequently, apart from LLark's exploration of LLM's potential applications in the context of music as a sub-category of the audio modality, both the audio and text encoders, as well as the data creation approach, lack substantial innovation. It appears to be more of a fusion of pre-existing works rather than a meticulously designed contribution to the field of music understanding.

Additionally, LLark's design, which is more of a combination of existing components than a novel creation, results in a limitation. It primarily excels at simple classification-based and language-generation tasks, thus falling short of being a comprehensive music foundation model capable of addressing diverse aspects of music content, such as music source separation and music generation. Consequently, labeling LLark as a music foundation model appears somewhat overambitious, as a language-output-only model does not meet the criteria for such a designation. The model's architecture, which is primarily focused on mapping audio to text, does not inherently support tasks like music generation or source separation, which require different output modalities and architectures.

This limitation exposes a second weakness. If LLark were indeed a potent model capable of unifying various music understanding tasks, it would represent a significant breakthrough, offering a one-stop solution for music classification, understanding, and captioning. However, LLark does not meet these expectations. Based on my extensive knowledge of Music Information Retrieval (MIR) development, LLark lags behind state-of-the-art models in several MIR subtasks, and even falls short of other music understanding models, such as MERT [3]. Here are some pertinent statistics:

(1) In genre classification on GTZAN, the current state-of-the-art [4] achieves an accuracy of 83.5%, while MERT, a music understanding model without a language component, achieves around 79.3%. In contrast, LLark only achieves 56%, which falls significantly short of practical usability standards. The large performance gap between LLark and existing models on this task raises concerns about the model's ability to capture the nuances of musical genre.

(2) For key-signature classification on GiantStep, the current state-of-the-art model [3] achieves 74.3% accuracy, whereas LLark attains 70%. While the performance difference is smaller than in genre classification, it still indicates that LLark is not competitive with specialized models.

(3) In tempo estimation on GiantStep, the current state-of-the-art model [5] reaches an accuracy of 88.6%, while LLark achieves 86%. This further demonstrates that LLark's performance is not state-of-the-art in core MIR tasks. The paper does not provide a detailed analysis of why LLark underperforms in these tasks compared to specialized models.

Remarkably, LLark does not exhibit superior performance despite leveraging two large models, Jukebox-5b and Llama2-7B. It's worth noting that these state-of-the-art models often have parameter sizes of less than 100 million or even 1-5 million. MERT, a Hubert-based music understanding model, effectively achieves equal or superior performance with a parameter size ranging from 95 million to 330 million, employing straightforward linear modules. Furthermore, models like MERT, CLAP, and others can extend their capabilities to encompass broader applications, such as music separation and text-to-music generation tasks. Thus, introducing a language model with billions of parameters that delivers fewer tasks and less performance seems counterintuitive. Moreover, comparing LLark with language-audio (LU-AST) or language-image (IB-LLM) models is not comprehensive, as they are trained on different datasets and do not primarily focus on music data. Additionally, these models, in my view, are also far from achieving state-of-the-art performance to demonstrate practical usability

It is important to highlight that LLark's inference setting may not be as rigorously defined as proposed. The instruction-based data generation method provides the model with pre-structured slots for various music elements, such as genre, tempo, instrument, and chord. In this setup, it is expected that LLark can generate outputs corresponding to these slots when prompted with questions. Consequently, it may not truly qualify as a zero-shot setting. The model's performance may be heavily reliant on the specific structure of the instruction prompts, rather than a genuine understanding of the underlying musical content.

Regarding music captioning, while LLark's performance in this aspect demonstrates the power of language models, it is arguable whether this achievement is solely attributed to LLark or whether it mainly leverages the adaptation learned within Llama 2. Furthermore, when it comes to evaluation metrics, such as BLEU scores, LLark does not consistently outperform previous state-of-the-art approaches. The paper does not provide a detailed analysis of the model's performance on music captioning, particularly in comparison to other models specifically designed for this task.

Third, the motivation behind incorporating a language model within a music foundation model remains somewhat unclear. While LLM represents a remarkable advance in AI, the necessity of using a language model to answer questions about music attributes like tempo, key signature, chord estimation, or genre is a matter of debate. Such an interface may be more welcome when provided with labels or temporal markers, rather than a language-based query. Although music captioning demonstrates the potential, it is not fully explored in this paper. To harness the full potential of LLM in music understanding, it is crucial to either prove that language can serve as an effective tool or instruction for new music tasks (e.g., text-to-music generation, text-guided separation) or show that LLark can learn more from limited instruction-based data. However, this aspect remains unaddressed in the paper, as it is evident that LLark's performance relies heavily on specific instruction texts, and it may struggle to comprehend music without those explicit cues.

In summary, LLark appears to lack the necessary level of technical novelty in designing new architectures for a music foundation model, does not provide comprehensive evidence to establish itself as a complete music foundation model, and fails to demonstrate superior performance or conduct exhaustive comparisons against established Music Information Retrieval (MIR) state-of-the-art models or other music understanding approaches. As such, it may not meet the standards expected for acceptance at the ICLR conference, and more substantial evidence is required to demonstrate its functionality and efficiency

### Questions
1. Regarding CLAP, you mentioned in the appendix that it lacks sufficient music data and temporal-related embeddings to serve as the audio encoder. However, it's worth noting that their official GitHub repository provides a checkpoint trained on more than 630K data, including music, speech, and general audio. Have you explored this checkpoint? Additionally, there seems to be a reference error related to LAION-CLAP; it should refer to [1] instead of [2].

2. Do you have any experimental results for LLark on tasks related to temporal aspects, such as chord estimation or beat tracking? Including such results could enhance the paper's overall demonstration of LLark's performance and its ability to adapt to a wider range of Music Information Retrieval (MIR) tasks.

3. On the demo page, there appears to be an issue with the music captioning demo. Specifically, I observed that Beethoven's captioning has three identical captions. Is this a posting error that needs to be addressed?

[1] Large-scale Contrastive Language-Audio Pretraining with Feature Fusion and Keyword-to-Caption Augmentation, ICASSP 2023

[2] CLAP: Learning Audio Concepts From Natural Language Supervision, ICASSP 2023

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
