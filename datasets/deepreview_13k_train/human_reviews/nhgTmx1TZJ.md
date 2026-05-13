# UniAudio: An  Audio Foundation Model Toward Universal Audio Generation

- Decision: Reject
- Scores: 5, 1, 5, 1

## Abstract
\vspace{-10pt}

Large Language models (LLM) have demonstrated the capability to handle a variety of generative tasks. This paper presents the UniAudio system, which, unlike prior task-specific approaches, leverages LLM techniques to generate multiple types of audio (including speech, sounds, music, and singing) with given input conditions. 
UniAudio 1) first tokenizes all types of target audio along with other condition modalities, 2) concatenates source-target pair as a single sequence, and 3) performs next-token prediction using LLM. Also, a multi-scale Transformer model is proposed to handle the overly long sequences caused by the residual vector quantization-based neural codec in tokenization. Training of UniAudio is scaled up to 165K hours of audio and 1B parameters, based on all generative tasks, aiming to obtain sufficient prior knowledge not only in the intrinsic properties of audio but also the inter-relationship between audio and other modalities. Therefore, the trained UniAudio model has the potential to become a foundation model for universal audio generation: it shows strong capability in all trained tasks and can seamlessly support new audio generation tasks after simple fine-tuning. Experiments demonstrate that UniAudio achieves state-of-the-art or at least competitive results on most of the 11 audio generation tasks. Demo and code are released.\footnote{\url{https://uniaudio666.io/demo_UniAudio/}}
\blfootnote{* Equal contribution; $\dagger$ Corresponding author}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a foundation model for audio generation capable of handling a number of different tasks, all of which output audio (including speech, environmental sounds, and music) conditioned on input from multiple modalities including text, audio, and MIDI.  

The paper also introduces a two-level Transformer architecture where the top-level attention operates across audio *frames* (where each frame consists of multiple discrete tokens) and the bottom-level attention operates on the tokens within a frame.

### Strengths
I am very much in favor of the goal of the paper: to introduce a multitask foundation model for audio generation.  I am also totally on board with the proposed architecture; decomposing the quadratic attention into frame-level and token-level is an excellent idea for handling the longer sequence lengths that are necessary for freeform audio generation.

### Weaknesses
Two main areas of weakness:

1) Most of the evaluation tasks do not seem ideal for demonstrating the effectiveness of an architecture designed to enable long sequence lengths; other than text-to-music, the tasks are all quite local, with no real dependencies longer than a few seconds.  For example, tasks like speech enhancement and voice conversion are inherently local, focusing on frame-by-frame transformations rather than capturing long-range temporal dependencies.  Notably, text-to-music is the task on which the model in the paper performs worst compared to baseline. And the experimental evaluation of the architecture vs others consumes only a small section of the paper and is fairly inconclusive. The paper does not adequately explore the potential of the proposed architecture for tasks that require modeling of longer temporal contexts, such as generating extended musical pieces with coherent structure or creating soundscapes with evolving environmental sounds. Essentially, the architecture seems overkill for most of these tasks, and for the task for which one might expect it to help most (text-to-music), possibly the smaller training data size prevents the model from taking advantage of its capability.

2) The paper does not convincingly demonstrate that training a single model on speech-, music-, and sound-generating tasks exhibits synergy across domains.  While for most of the evaluation tasks the multitask model outperforms the single task model, a) the difference in performance is small and b) it's not clear that the model really benefits from training on all of speech, music, and sound compared to a separate speech model, music model, and sound model as this experiment was not performed.  It's also not clear how much of the benefit depends on specifics of the datasets and tasks used here vs a more general principle; e.g. the overall amount of speech data here is much larger than the other domains and so a music task might benefit from training jointly with speech more than would be the case if the amount of music data were larger. The paper lacks a rigorous ablation study that isolates the contribution of each domain to the overall performance, making it difficult to ascertain the true benefits of multi-domain training. For example, it would be useful to see results from models trained on all combinations of domains (speech only, music only, sound only, speech+music, speech+sound, music+sound, and all three) to understand the interaction effects. Overall, I'm just not satisfied that the main hypothesis of the paper -- training a model on all audio generation domains at once is better than training separate models for each domain -- is sufficiently backed up with experimental evidence.  The fact that the joint model outperforms state of the art on about half the tasks (and *not* the music tasks) corroborates my dissatisfaction here.

One other possible reason for training on multiple domains could be: only a small quantity of training data exists for certain domains.  However, for the case of foundation models this is certainly not true; it is usually *labels* that are in short supply, and raw audio -- speech, music, and sound -- exists in enormous quantity.

### Questions
1) Basically, convince me that training on speech helps with music, even if one has access to enormous unlabeled music datasets.  I'm totally willing to believe that training on all the speech tasks at once is helpful.

2) I do believe that the architecture proposed is going to outperform the comparison architectures for audio generation.  But the experiment demonstrating this isn't especially compelling; did you perform other experiments on the different architectures?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a LM-like audio model, that is able to conduct multiple (11) audio generation tasks. Audio is tokenized with a EnCodec-like quantizer to fit for LM. Multi-scale Transformer is used for handling multiple tokens per audio frames. Experiment was conducted by training on 165K hours audio data.

### Strengths
The overall approach is sound. It's great to see a single model can handle so many different audio generation tasks.

### Weaknesses
1. The novelty of this paper is very limited. All the components used in the paper are previously existing. The main contribution of this paper is to train a multi-task model with a mixture of multiple datasets.
2. The overall contribution to the research community seems very limited. There is no much insights can be drawn from this paper to benefit the community. There is no ablation study conducted. It looks more of an engineering work than a research work.
3. The presentation of this paper needs improvement. It seems presented in an eye-catching, but misleading way. For example, it's improper to put Table 1 as the first thing in the content of this paper, because it lacks context and is confusing. Even worse, it's not a fair comparison -- the cited papers didn't include experiments on specific tasks doesn't mean that the methods presented in those papers are incapable of those tasks.

### Questions
None.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- The authors present a foundation model for audio generation and editing which encompasses 11 tasks spanning multiple modalities of audio such as speech, music, and general sounds. 
- The paper proposes a different approach to modeling audio tokenized into discrete codes using audio codecs. The proposed architecture is a single multi-scale transformer which involves a global transformer which operates on a summarized form of each audio frame, and a local transformer which performs autoregressive generation of codes within an audio frame. The design is proposed as a way to alleviate training transformers on very long sequences of flattened audio codes (SPEAR-TTS), or having train an autoregressive transformer on one level of codes and another non-autoregressive transformer on the remaining level of audio codes (VALL-E).
- The training process involves 7 different tasks with various task indicator tokens being used. The remaining tasks are incorporated in a fine-tuning phase post training of the base model.
- The authors perform evaluation using subjective and objective metrics and compare against various other models which may be specialized for each task. The results indicate that UniAudio is competitive against all the baselines.

### Strengths
- As the authors show in the first table, this system is the first to tackle so many tasks in audio generation using a single backbone with only additional fine-tuning.
- The proposed model architecture is different from those used in other audio generation models and shows some gains. The comparison is not necessarily fair because of differences in training data, but it does give the community a new option to consider while building audio generation models.
- Results for speech data and denoising are decent.

### Weaknesses
 - The paper is a very dense read with some details relegated to the appendix while some details difficult to glean from the text. For example, the details about the audio tokenizer is moved to the appendix and no specifics are mentioned in the main text. Also, the text and the figure in the model architecture section are a little difficult to understand. I think I got it after reading through a few times, but adding some annotations to the figure and its caption will greatly improve readability.
- While the results for speech are decent, I found some issues w.r.t words being skipped. Also, the results on text to music/audio are pretty poor. The authors have not discussed any of the limitations in terms of quality of the generated audio despite the model being competitive with current state-of-the-art. 
- The paper does not offer too much in terms of insights. Not to take away from the effort it takes to setup such a large scale experiment, but my main takeaways from the paper are as follows:
  1. Existing audio codecs are not suitable for wide range of tasks, so one needs to train them on more diverse data.
  2. As long as we collect 100k+ hours of audio data we can achieve such performance using the multi-scale transformer. 

  The multi-scale transformer architecture is definitely interesting to the community but the architecture contribution is not well ablated, and in my opinion, that is the most important part of the paper.
- Minor correction: In Table 3, subjective and objective metrics column headers should be interchanged.

### Questions
- Wonder if the authors can add any ablations that answer questions related to the effect of data quantity?
- Did the authors consider using DAC as the audio codec? Those models are trained on a more diverse dataset and also have other improvements over EnCodec.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors train a single multi-scale transformer to perform multiple different audio tasks. They demonstrate that, by learning these tasks together, they get a performance boost for this model, and achieve state of the art results on multiple tasks (against specialist models). They show that the existing model can be fine tuned to perform well on novel tasks. In addition, they describe how to translate multiple input modalities into a universal data space with a neural codec to allow this to happen, and discuss the merits and detriments of this system against other approaches.

### Strengths
* All data used is public, so results can be reproduced
* Compute required is not out of the realms of most academic institutions (16 x MI200-64G GPUs ~ $64k) - particularly if, as is suggested, this model is taken and simply fine tuned upon
* I am not aware of another model which has covered all of these tasks nor comprehensively demonstrated that combining different input modalities benefits each task; the authors show the benefit of training on multiple modalities by training their model on just the one task, and then again on all task, and by comparison with the current sota (generally single-task) model
* Care and attention has been taken to compare with recent sota models in each domain, and to perform both objective and subjective evaluations. In addition, an anonymised website of audio generations was provided

### Weaknesses
* Reliant on the input representation - any losses incurred by input representation cannot be modelled, and if a new representation were to be used, a new model must be trained. This is particularly concerning as the input representations (T5, mHuBERT, and the neural codec) each have their own limitations and biases. For example, the T5 model may not capture all nuances of text, mHuBERT may not be optimal for all audio types, and the neural codec introduces quantization errors. These limitations are compounded when combined, and the model is fundamentally limited by the weakest link in this chain. Furthermore, the necessity to retrain the entire model when changing any of the input representations presents a significant practical drawback.
* As noted in the limitation section, there's no demonstration of fine tuning to an unknown modality (which would require a new special modality token to be included in the vocabulary). This greatly limits the model's ability to generalize to new, unforeseen tasks or data types without substantial retraining and modification of the model architecture. The inability to simply add a new modality token and fine-tune the model is a significant hurdle for practical applications where new modalities might be encountered frequently.
* The evaluation is so wide ranging it's difficult to parse in tables. Perhaps a bar chart or plot could improve the interpretation of relative performance with sota benchmarks? The current tabular format makes it challenging to quickly assess the model's performance across all tasks and compare it to existing state-of-the-art models. A more visual representation would greatly enhance the clarity and impact of the results.
* Only amazon turk was used for evaluation - a broader human evaluation with subject experts would be very interesting. While Amazon Turk provides a convenient way to gather human evaluations, it is not ideal for all tasks, particularly those that require specialized knowledge or expertise. Subject matter experts, such as musicians, speech therapists, or audio engineers, could provide more nuanced and reliable judgments on the quality of the generated audio.

### Questions
* It is not explained exactly why the 4 tasks were selected for the fine tuning study, was there any reason?
* Is there any reason that the process could not be end to end (i.e. must the neural codec be learned prior and fixed)?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
