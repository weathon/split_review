# TIGER: Time-frequency Interleaved Gain Extraction and Reconstruction for Efficient Speech Separation

- Decision: Accept
- Avg Score: 5.83
- Scores: 6, 8, 6, 8, 6, 1

## Abstract
In recent years, much speech separation research has focused primarily on improving model performance. However, for low-latency speech processing systems, high efficiency is equally important. Therefore, we propose a speech separation model with significantly reduced parameters and computational costs: \textit{Time-frequency Interleaved Gain Extraction and Reconstruction network (TIGER)}. TIGER leverages prior knowledge to divide frequency bands and compresses frequency information. We employ a multi-scale selective attention module to extract contextual features, while introducing a full-frequency-frame attention module to capture both temporal and frequency contextual information. Additionally, to more realistically evaluate the performance of speech separation models in complex acoustic environments, we introduce a dataset called \textit{EchoSet}. This dataset includes noise and more realistic reverberation (e.g., considering object occlusions and material properties), with speech from two speakers overlapping at random proportions. Experimental results showed that models trained on EchoSet had better generalization ability than those trained on other datasets to the data collected in the physical world, which validated the practical value of the EchoSet. On EchoSet and real-world data, TIGER significantly reduces the number of parameters by \textbf{94.3}\% and the MACs by \textbf{95.3}\% while achieving performance surpassing state-of-the-art (SOTA) model TF-GridNet.
  This is the first speech separation model with fewer than \textbf{1 million parameters} that achieves performance comparable to the SOTA model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper developed a deep learning model for speech separation; and it not only focuses on improving model performance but model efficiency. The model is lightweight, and is constructed of a new band-split strategy and a new frequency-frame interleaved (FFI) block. Additionally, to reduce the gap between synthetic data and real-world, it introduced a dataset, named EchoSet, with different noise and realistic reverberation. Experimental results demonstrates the effectiveness and efficiency of the proposed model, and the generalization of the dataset to real-world audio.

### Strengths
Overall the paper is well-written and easy to follow. The proposed model architecture looks reasonably nice with the introduction of a new band-split strategy and a new FFI block. Experimental results show that the model not only archieves competitive performance on all datasets, but also it is very lightweight in terms of model sizes, MACs. Its efficiency in training (GPU time & memory) and inference (CPU time, GPU time & memory) looks good, too.
The motivation of creating EchoSet dataset is clear and reasonable with a complete analysis of existing dataset. Experimental results on the real-world data with different models, trained on different datasets respectively, demonstrate its generalization ability.

### Weaknesses
The FFI block follows a common design of dual-path architecture, it consists of 2 different parts: frequency path and frame path. Each path has two main modules: multi-scale selective attention (MSA) and full-frequency-frame attention (F^3A). While F^3A looks familiar with self-attention mechanism, MSA extracts features through a selective attention mechanism at multiple scales. We may need an ablation study of the MSA architecture with different scales (e.g. 1,2,3,4) to see how it affects model performance. Specifically, it's unclear how the different scales interact and if there's redundancy or interference between them. For example, do larger scales capture more global context while smaller scales focus on local details, and how does this impact the overall representation? Furthermore, the paper does not discuss the computational cost of each scale, which could be important for model efficiency.

The evalution on model efficiency is conducted with a fixed audio input length of 1 second. It would be more complete if the evaluation was with different audio input lengths (each audio in EchoSet is 6 seconds, LRS2-2Mix: 2 seconds, Libri2Mix: 3 seconds). The current evaluation may not reflect the model's behavior with longer sequences, where memory usage and latency could become more significant factors. Specifically, the paper should analyze how the model's efficiency scales with input length, which is crucial for real-world applications where audio recordings can vary significantly in duration. The reported metrics might not accurately represent performance on longer audio segments.

### Questions
The model source code is open, the description of EchoSet is reasonable, but it would be better if the configuration/code of data generation is also open.

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
4

### Summary
The paper introduces a novel model architecture that has small number of parameters and performs as well as other larger models on various separation tasks.

The model architecture is similar to bandsplit RNN in its encoder/decoder part and in its core part, it has two novel attention-based submodules called MSA and F3A which are applied in the frequency direction and time (frames) direction separately in identical fashion. These modules are repeated a fixed number of times. When repeating, the parameters are tied, so the number of parameters in the model do not increase when the repetition count is increased.

The paper also introduces a new dataset called EchoSet which includes reverberant speech mixtures which improved performance on a "real" dataset. The "real" dataset is not real in the sense of real speech conversations, but it is obtained through playback in a real acoustic environment of individual sources which are mixed later for evaluation.

The performance on real data shown in Figure 4 is much lower compared to the results with artificial mixtures even when training on EchoSet, which shows there is still a lot of room for improvement when applying these models on real data.

### Strengths
The paper is well written and the model is described in a detailed manner even though there may be room for improvement in the model description for more clarity.

The method applies to many different sampling rate data due to bandsplit RNN based encoder/decoder. The model is also used to perform cinematic audio separation at 44.1 kHz.

The ablations and various comparisons with state-of-the-art on multiple relevant datasets are all appropriate and impressive.

### Weaknesses
Loss function was not mentioned in the main text (or I missed it). Is the loss in (10) in the appendix used for all tasks, or only for cinematic sound separation?

The math in the MSA module description gets a bit hard to follow, so maybe a more detailed Figure that tracks along with mathematical equations would help. How does selective attention (SA) work? It was not described in the paper.

### Questions
1. What was the loss function?
2. How does selective attention (SA) work?
3. What is the reasoning behind repeating the same FFI block (with tied parameters)?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents an approach named TIGER for speech separation, emphasizing both efficiency and performance. The proposed approach utilizes frequency band-splitting, selective attention modules, and F3A to manage both temporal and frequency information. In addition, the authors introduced a new data set named EchoSet, that considers the realistic environmental factors such as noise, reverberation, and varied speaker overlap ratios. Experimental evaluations reveal that the proposed approach achieves competitive results across multiple benchmarks.

### Strengths
1) The authors' provision of open-source code enables researchers in the field to reproduce and build upon this work.
2) The authors have a detailed ablation study, as it clarifies the impact and effectiveness of each proposed module.

### Weaknesses
1) The proposed approach does not demonstrate clear performance advantages over the current SOTA method, with a noticeable performance gap.
2) Although the authors claimed their approach is more lightweight, the comparison is not entirely fair. A comparison with other systems that specifically employ lightweight methods would provide a more accurate assessment of the model's efficiency.

### Questions
1) The authors mentioned that the band-split module is inspired by prior knowledge of music separation. it would be helpful to clarify if the targeted speech separation task has similar prior knowledge and to highlight any key differences or similarities between the band-split module used here and that in the original paper.
2) In Figure 2, the authors mention that "Residual connections are used to retain original features and reduce learning difficulty." Could you please indicate where these residual connections are depicted in the figure?
3) In Figure 4, the authors use a line chart to present the results. This may be misleading because the results on the three datasets are independent of each other. A different visualization style, such as a bar chart, might provide a clearer comparison.
4) What are the differences between TIGER (small) and TIGER (large), why do they have the same model size?
5) In the ablation study, it looks like the proposed modules appear to involve trade-offs among various performance criteria. Could the authors discuss how to balance this tradeoff and what could be the best to consider?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents TIGER, an efficient speech separation model with significantly reduced parameters and computational costs, optimized for low-latency applications. Leveraging frequency band segmentation and attention mechanisms, TIGER captures rich contextual information. The authors introduce EchoSet, a realistic dataset for evaluating model robustness in complex environments. TIGER achieves state-of-the-art performance with 94.3% fewer parameters and 95.3% fewer MACs than existing models.

The result is very impressive and the details is rich. They also provide a high quality dataset which would be beneficial to the field.

### Strengths
1. Provide a new way of speech separation with very efficient paramater usage. It is very important to the industry and would be very influential 
2. provide a new dataset which provides different content compared to all other similar kinds before.

### Weaknesses
1. The model focused on two speaker separation which makes the task much simpler. May need to provide a way to generalize the framework.

### Questions
1. How would the model deal with the audio with background noise? 
2. Does the method still work when two people speaking in different setup? e.g. one people is much further to the speaker than another. 
3. How should the model accommodate variable number of speakers?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose a speech separation setup which relies on multi-scale selective attention and interleaved time-frequency attention modules. The design is relatively lightweight, significantly reducing the number of model parameters and consequently, computing resources in inference. They also introduced   a speech separation corpus, EchoSet, that allegedly has more realistic noise and reverberation. They conducted comprehensive empirical evaluations of several comparable models and public data sets.

### Strengths
The paper is well-written overall, following a logical organization and making sound arguments. The development of the proposed system is easy to follow. The details of the modules inside the systems are adequately presented. The evaluation results, given the nature of the paper as an empirical study, can seem a bit under-developed, but the major evaluations are made and presented. The ablation studies are important to help readers understand the importance of the MFA and F3A modules. That being said, similar ablation studies can also be performed on the EchoSet, to determine which aspect of the simulation set this new corpus apart from the former ones. 
The paper highlighted the strong performance of the proposed speech separation system and its small footprint in terms of model size.

### Weaknesses
The comparison between the various corpus is not strictly fair, given the data sets have different sizes. From the data provided by the authors, EchoSet contains 33.78 hrs, whereas LRS2-2Mix has 11.1 hours and Libri2Mix has 58 hrs. Did the authors augment/select the data to ensure that the same amount of data is used in training to evaluate the systems in Table 2?
The argument in Sect. 6.1 is not entirely clear to me. What does data collected in the real world refer to? Is there any description of this data?
To measure the model complexity, model parameters are acceptable, but MACs is inadequate. To go beyond theoretical analysis, the authors can measure the memory usage, power consumption, throughput and latency on server or edge devices. 
Related to the comments above, Sect. 6 can be beefed up with more analysis. For example, does TIGER or models trained with EchoSet perform better in lower SNR/stronger reverb compared to other models? Can we break it down? How does Tiger/EchoSet fare on male-male pair vs. male-female pair, etc.?

### Questions
In Table 4, how does LowFreqNarrowSplit compare with Mel-split?
How scalable is Tiger for multi-talker separation?
How scalable is Tiger for audio separation beyond speech, as alluded to in Table 9, where music and environmental sound is still a lot harder than speech. What's the path forward?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper has two main contributions:
1. The TIGER architecture which is a lightweight time-frequency model
focusing on reducing model size while keeping separation accuracy high.
2. The EchoSet dataset for two speaker speech separation which attempts
to resemble real world scenarios more closely than previous datasets by using
3D environments.

### Strengths
The paper proposes a novel dataset, the EchoSet, which not only includes noise
and reverberation, but also object occlusion and different materials through
3D environments. The proposed speech separation architecture achieves high
accuracy on this new dataset while having few trainable parameters.

### Weaknesses
There are many issues with the experimental part of the paper, especially the
evaluation of the proposed model architecture.

The first issue is the datasets that were chosen. The main dataset for
speech separation, the WSJ0-2Mix, was not used. Instead, three others were - the proposed EchoSet, the LRS2-2Mix and the Libri2Mix. While choosing
the LRS2-2Mix over WHAMR! is motivated, the main problem concerns the
Libri2Mix. The results of the Libri2Mix reported here do no coincide with
previous reported results. The Conv-TasNet normally reaches 14.7 dB SI-SDRi
while this paper only report 12.1 dB SI-SDRi. Since all of the results reported
in this paper disagree with previous results, I assume that this is caused by
the choice of limiting the sequence length of the Libri2Mix to 3 seconds, as is
mentioned in the appendix. It also appears that this paper only uses utterances
from train-100 and leaves out utterances from train-360 as is used in the original
Libri2Mix. Therefore, this paper significantly changed the dataset of the Libri2Mix
while still calling it Libri2Mix. Since the training set was clearly significantly
altered, the results obtained here are very difficult to interpret because the
normal Libri2Mix contains more and significantly longer training data.

If one wanted to include two speaker speech separation, why not just use the
standard WSJ0-2Mix which basically everyone uses? And how are future papers
meant to compare themselves to the results reported in this paper? Is everyone
now meant to use this altered Libri2Mix? Since the source code is included,
others could run experiments to figure out the accuracy of the TIGER model
on the normal Libri2Mix or the WSJ0-2Mix. But it simply does not make sense
to have others go through said effort instead of having the original paper contain
this basic information.

There are, however, even more aspects of the results that are unusual. The
speed and memory measurements were taken using an input sequence containing
16k elements. This does not represent any of the datasets used. The EchoSet
is reported to use 6 second inputs, meaning it should contain 96k for 16 kHz,
the LRS2-2Mix uses 2 second inputs at 16 kHz, meaning a sequence length of
32k, and the Libri2Mix uses 3 second inputs, meaning a sequence length of 48k
at 16 kHz. Choosing any (or preferably all) of the sequence lengths used in the
datasets would be logical, but showing the results of a much shorter sequence
length is not.

However, even if all results reported in the paper were correct, they would
still not make a convincing case for the TIGER architecture. The biggest
strength of it is its low model size. While the experiments concerning accuracy
as well as computational cost are flawed as described above, the results of the
TIGER architecture are still not very convincing except for its accuracy on
the EchoSet. It is neither particularly fast nor memory efficient and was only
compared to a single other recent SOTA architecture, the TF-GridNet, which
it cannot match in accuracy in 2 of the 3 datasets tested.
While the paper includes an ablation study, it doesn’t answer the most
pressing questions. What kind of performance (in terms of accuracy/speed/memory
usage) would the TF-GridNet have if it shared model weights across its blocks
and reduced some parameters to match the TIGER’s model size? If such a
comparison was made and the TIGER architecture would be more accurate/faster/used
less memory, then there would be a better argument for it. As of now, it just
looks like it sacrifices accuracy for model size.

The paper also fails to mention perhaps the most significant previous work
for speech separation models with few trainable parameters, which is Group
communication [1]. It is incorrectly claimed that the TIGER architecture is
the first speech separation model with less than 1 million parameters, when the
aforementioned paper includes models with less than 100k parameters and is
roughly 4 years old.

The paper also claims that the models trained on the EchoSet perform better
on real world signals than the Libri2Mix and LRS2-2Mix. This might be true,
but is difficult to say with certainty due to the lack of information in the paper.
The real world data that was used is described in the appendix - however,
important details like its sampling rate and duration were left out. The sampling
rate for the speech separation datasets is only specified for the LRS2-2Mix to be
16 kHz but I assume it to be the same for the Libri2Mix and the EchoSet since
the training configuration appendix talks of frequency ranges from 0-8 kHz.
The duration for these datasets, however, is very different - 2 seconds for the
LRS2-2Mix, 3 seconds for the Libri2Mix and 6 seconds for the EchoSet. If the
average duration of the real world data is also closer to 6 seconds, then it would
give the EchoSet an unfair advantage over the other datasets. Again, this might
not be the case, but without clarification of the duration and sampling rate of all
the data used the results given cannot be verified. In fact, the reported results
in Figure 4 are very unexpected. How is the LRS2-2Mix often even worse than
the Libri2Mix (despite using background noise and reverb, same as the real
world data) while the EchoSet is massively better than both? The paper never
attempts to explain this oddity.

### Questions
1. The assembly of the real world data is somewhat confusing. As I understand
it, the utterances as well as the noise was rerecorded in the real world and then
mixed together at different SDRs. Why did you not play multiple utterances
and noise from different locations in the room at the same time which would
resemble a real world mixture more closely rather than mixing them together
afterwards?
2. Computational cost was measured on a one second input at 16 kHz.
This choice is never motivated and in the context of speech separation illogical.
While there are some previous papers that have done the same [2, 3], neither
of them had any justification for this choice either. The standard for speech
separation would be an input of at least 4 seconds [4, 5]. The reasoning is
that the WSJ0-2Mix, contains utterances with an average length of about 4-5
seconds. The EchoSet, meaning the dataset the paper proposes, uses 6 second
utterances. Why choose a completely different length for the calculation of
speed and memory usage?
3. The sampling rate for the speech separation datasets is only specified
for the LRS2-2Mix as 16 kHz. Is it the same for the other two (Libri2Mix and
Echoset)? If so, why? Typically, 8 kHz is used and while there is nothing to be
said against using 16 kHz, it still makes future comparisons difficult to not also
include 8 kHz data.

References

[2] Kai Li, Runxuan Yang, and Xiaolin Hu. “An efficient encoder-decoder
architecture with top-down attention for speech separation”. In: ICLR.
2023.

[3] Chen Chen et al. “A Neural State-Space Modeling Approach to Efficient
Speech Separation”. In: Proc. INTERSPEECH 2023. 2023, pp. 3784–3788.
doi: 10.21437/Interspeech.2023-696.

[4] Zhong-Qiu Wang et al. TF-GridNet: Integrating Full- and Sub-Band Modeling
for Speech Separation. 2023. arXiv: 2211.12433 [cs.SD].

[5] Cem Subakan et al. Exploring Self-Attention Mechanisms for Speech Separation.
2023. arXiv: 2202.02884 [eess.AS].

### Soundness
1

### Presentation
3

### Contribution
1
