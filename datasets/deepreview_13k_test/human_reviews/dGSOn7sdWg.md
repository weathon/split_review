# SyllableLM: Learning Coarse Semantic Units for Speech Language Models

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Language models require tokenized inputs. However, tokenization strategies for continuous data like audio and vision are often based on simple heuristics such as fixed sized convolutions or discrete clustering, which do not necessarily align with the semantic structure of the data. For speech in particular, the high resolution of waveforms (16,000 samples/second or more) presents a significant challenge as speech-based language models have had to use several times more tokens per word than text-based language models. In this work, we introduce a controllable self-supervised technique to merge speech representations into coarser syllable-like units while still preserving semantic information. We do this by 1) extracting noisy boundaries through analyzing correlations in pretrained encoder losses and 2) iteratively improving model representations with a novel distillation technique. Our method produces controllable-rate semantic units at as low as 5Hz and 60bps and achieves SotA in syllabic segmentation and clustering. Using these coarse tokens, we successfully train SyllableLM, a Speech Language Model (SpeechLM) that matches or outperforms current SotA SpeechLMs on a range of spoken language modeling tasks. SyllableLM also achieves significant improvements in efficiency with a 30x reduction in training compute and a 4x wall-clock inference speedup.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a method to extract speech units from existing pre-trained models such as HuBERT or Data2vec2 at syllable boundaries. They show that they are able to significantly lower the number of units used to encode a particular utterance while maintaining and improving on the quality of re-synthesized speech, or continuation of the speech if used with a language model trained on these new speech units. The method is relatively straight forward and, if it works, allows significant savings in the number of tokens needed to accurately model speech data.

### Strengths
- the paper describes the method in sufficient detail to reproduce it
- this appears to be a novel way (although based on much prior work) to discover unit boundaries in speech data, which turn out to be syllables.
- the results are compelling in light of much concurrent work on speech-unit language models, especially as they allow to significantly reduce the cost of training such models due to higher compression ratio

### Weaknesses
- while using speech units from HuBERT and other models has been widely explored, one downside of such units is that they tend to mostly capture only the semantic content. Presumably, TWIST units may capture some of the prosodic information, but it is not clear how the authors measure the prosody and expressiveness of this method. An alternative for generative tasks is to simply model speech as text (e.g. via an ASR model) and add additional style vectors. Speech understanding tasks may simply use the pre-trained models which this work bootstraps on directly. It would be very interesting to see some quantitative and qualitative comparisons on this topic.
- "Language models require tokenized inputs" - this is not strictly true depending on how one defines "tokens". While discrete tokens are a popular choice, one can certainly build a language model that uses continuous inputs ("tokenized" by splitting it into distinct representations on the time axis or through methods like what is described in this paper) with discrete or continuous targets on the output.

### Questions
see weaknesses section for suggestions on what to add to the paper

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
5

### Summary
The authors propose a novel method to extract rough syllabic segment boundaries utilizing loss patterns in HuBERT induced by different input mask spans. With those rough segments, a learning method, SylBoost, is proposed to learn a segmented representation by fine-tuning pretrained SSL models. By controlling the granularity of the initial segments, the authors train multiple models with different frequency of speech segments, ranging from phoneme to word level. Syllables are more accurately and efficiently detected than the previous model, SD-HuBERT. By training LM on those syllable-like units from clustering, the authors suggest SyllableLM and demonstrate that spoken LMs at syllabic granularity can outperform or on par with previous SOTA spoken LMs using smaller model and training data.

### Strengths
LossPred and Sylboost are well-motivated, novel ways to learn speech representation beyond phonemes, allowing different model training with different frequency units. The method is meticulously explained. Authors depict real speed up in using these units compared to TWIST. Furthermore, results shown achieve near SOTA results on syllable boundary detection and discovery. Table 5 well ablates their design choices and results shown in Table 6 show clear improvements over existing baselines. In particular, the gain in length of tokens and bitrate is outstanding compared to previous speech unit LMs, which is an important factor in LM.

### Weaknesses
There are several concerns regarding some claims/analysis, as detailed below.

1. Lack of verification of syllabic correspondence of higher frequency models: The higher frequency models (6.25 HZ or 8.33 Hz) seem sub-syllabic or representing di- or tri-phones based on Figure 2 and Table 3. For example, there is a huge gain in phoneme boundaries correspondence (F1-P) by changing from 5Hz to 6.25Hz. Though, F1-S is still higher than F1-P, but this would be due to the usage of monophones in evaluation. This evokes a question whether the 6.25Hz GSLM – the best one beating SOTA, is a “syllable” LM. The 5Hz version seems the most syllable-like (and the only evaluated frequency in Table 1), but it is the worst among different frequency versions according to Table 5 and 6, showing high WER and no outstanding performance in LM.  Detailed analysis of the linguistic characteristics of the units at different frequencies, perhaps including examples and a discussion of how they relate to syllables, phonemes, or other linguistic units will make this clear.

2. Overclaiming controllability: The controllability of the segment frequency is given during training not at inference. However, the statement in the abstract, ”Our method produces controllable-rate semantic units” is misleading as it strongly implies that the controllability is given at the inference time. It requires rephrasing or a significant improvement in clarity. Besides, the authors claim a lack of controllability of previous studies, but the mincut approach cited by the authors has knobs that can control the frequency of resulting segments. The previous method may have a controllability though the prior works didn’t leverage the functionality. If true, the claimed novelty on controllability should be reassessed, may be provide additional experiments as evidence; and the manuscript must be accordingly updated.

3. Adaptability on different speaking rate at inference: The audiobook datasets have relatively consistent speaking rate as the speech is very carefully delivered. However, in the real world, people may use very different speaking rates based on contexts or based on accents or dialects. Can a model work on speech with a different speaking rate? For example, if we put speech elongated by two times, would the model output the same number of syllables or doubled? The authors explain that the k is determined by optimizing timestep losses but not clear how this loss is calculated at the inference time. 

4. Lack of validation of semantic unit discovery: As the authors are citing Choi et al. (2024), I assume semantics here means concepts, e.g., “dog” is similar to “puppy” though they are phonetically distant. However, syllables by definition are not conveying such conceptual meaning, rather structured phonetic information. While the authors are frequently claiming semantic unit discovery, the paper has no supporting evidence that the discovered units or embeddings are semantics. The low error rates in resynthesis cannot verify whether the feature encodes semantic information. The approach suggested by Choi et al. (2024) may be useful to verify the claims.

5. Lack of valid comparison/evaluation of LossPred: The proposed method for initial boundary extraction, LossPred, is novel and makes a lot of sense. Table 2 shows comparisons using Feat-Sim, but why not VG-HuBERT or SD-HuBERT? Those prior works already showed that the Feat-Sim on the original HuBERT is not accurate in terms of syllabic segmentation. As Feat-Sim works best with VG-HuBERT or SD-HuBERT, a fair comparison should involve Feat-Sim on them, not on HuBERT.

6. Absence of audio quality evaluation of generated speech: The paper severely lacks evaluation of the quality of generated audio which is a very crucial aspect of generative model or codec language model of speech. Though it is not claimed to be the main focus, some quality metrics like Mean Opinion Score (MOS) should be reported.  The WER/CER metrics are not sufficient to show the audio quality.

7. Erroneous calculation of RTF: As defined by sources like https://www.openvoice-tech.net/index.php/Real-time-factor and https://link.springer.com/article/10.1007/s11042-020-10073-7, real time factor is defined as the ratio between the time to process an input over the duration of the input. However, it seems like here, the authors chose to report the reciprocal, which is inadequate. The scores should be corrected to comply with the RTF definition. Also, the RTF comparison over TWIST should be calculated end-to-end, not from cached speech units. This is because RTF is aimed to measure efficiency in “real-world” scenarios, so the calculation should start from raw waveform, simulating real-world inference as much as possible. Moreover, this correction is critical as SyllableLM has an additional layer of segmentation in comparison to TWIST, which is not reflected.

### Questions
In the intro, what is evidence for “language models on spoken language still struggle to output semantically meaningful speech.”? 

In method, “We apply the SylBoost loss (Equation 4) to model features at layer L, which we select based on syllabic correlation as explored in detail in Pasad et al. (2024).” The cited paper is about words not syllables, where I couldn’t locate a particular mention of syllabic correlation. Please let me know in which part of the reference paper demonstrates it.

1. Provide motivations/reasons for some design choices: Why 75% of timesteps in Section 5.2? Why 8.33, 6.25, and 5.00Hz?

2. On the statement "training a resynthesis model provides a stronger description of the semantic information contained in units than purity metrics”, please provide the rationale for this. It is counter intuitive since resynthesis will be better if the input embedding is closer to low-level, like acoustics. For example, VQ-VAE based models like EnCodec show great performance in resynthesis but are claimed to lack higher-level information like semantics.

3. Typo in Table 2: Boundary detaction —> detection.

4. In Table 6, sBLIMP is designed for evaluating syntax (or grammar), which should not be categorized under “semantics”. Also, sWUGGY-all and tSC are the best in Moshi but bold annotations are erroneously given. Please fix them if the numbers are correct.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper suggests a discrete unit extraction method for speech, where each unit has a variable length, unlike most discrete audio units with a fixed rate (often 25/50 Hz).
To segment variable length units, they use a pre-trained self-supervised audio model trained on masked language modeling.
They first run the SSL model on the raw sequence to obtain the GT discrete units (teacher predictions).
They then mask a fixed-sized segment and use the SSL model again to measure the likelihood of every teacher token. They repeat this over sliding windows throughout the input, resulting in a square asymmetric “similarity” matrix.
As in previous work, they apply a min-cut algorithm to segment the audio into variable-length units.
They then train a neural model for feature matching, which leverages the produced boundaries in its loss function (average feature teacher feature across the segment). 
This is done to make the unit extraction more efficient (resolve the computational-heavy sliding windows) and hopefully generalize better.
To finally derive discrete units, they extract features from the boosted neural model and use a more efficient cut algorithm to segment the sequence. 
They then calculate the mean feature over each segment, and cluster using K-means and agglomerative clustering to discretize the units. 
Using their novel variable-length discrete units, they train speechLMs and see benefits in several metrics (e.g. sWUGGY, sBLIMP, and tSC).

Edit: I increased my score from 5 to 6 (weak-accept) and the contribution from 2 to 3 (good).

### Strengths
- The problem of extracting variable-length representations for audio is important, as the amount of information within different audio segments changes. 
- The approach reduces the token rate by x2-3 and SpeechLMs trained on these units obtain better results compared to the fixed-rate VQ/K-means discrete unit extraction.
- The idea of segmenting the audio before clustering is interesting, and seems to be quite efficient.

### Weaknesses
Weaknesses:
- The approach for variable-length unit extraction is quite complicated, with a wide range of hyperparameters to control (span size, number of segments, different ways to combine two clustering algorithms, etc). 
I’m a bit concerned that this method is overfitted to boost the specific metrics evaluated.  I find the core idea to be grouping before clustering - would you agree? 
A simpler algorithm can be: (1) compute a similarity matrix with SSL embeddings (maybe K-band matrix as you did to reduce complexity) (2) segment the audio using the similarity matrix (3) run K-means on the average representation per segment. (no training, no sliding windows)  .

- The metrics calculated to evaluate speechLMs mostly include likelihood ranking and perplexity calculations. However, generative models are mostly used to generate content. 
A sample page with audio continuations would help qualitatively check the differences in the generative capabilities of the models. ([1] may be useful to quantify those generative capabilities).  
I admit that likelihood ranking is the common practice for evaluating speechLMs, but IMO they don’t measure the thing we’re interested in (I’ll use the model mainly to generate, not to measure likelihood), so evaluating generated outputs is also important and should be added.  

- One reason to have variable-rate units is to dynamically distinguish between high-info segments and low-info segments. 
In your approach, the number of semantic regions is proportional to the length. In that case, 10 seconds of silence and 10 seconds of high-speed speech would result in the same number of tokens. 
The units have a variable length, but each sample has a fixed sample rate. With BPE, in contrast, we might get fewer tokens for 10 seconds of silence compared to 10 seconds of fast speech.  

- Table 6: What is the reason for the gray shade on several TWIST? In several metrics, the bolded result is not the best (in contrast to what is stated in the caption). I assume you want to state it is unfair to compare 7/13B models with 300M models (and I agree). In that case, it should be clear from the caption. 

- The tokenizer is trained on 960 hours of audio, which got me concerned about scalability in the unit extraction process. Can your algorithm scale so we can compute the units based on (e.g.) 55K hours of data? Can you elaborate on the sample complexity of the process (w.r.t. the length of each sample and the number of samples) 

- Table 6: The results suggest BPE (an alternative approach to producing a variable-length representation) degrades the results. This contradicts the findings of other several papers reporting benefits from BPE (additional references attached): 
[1] Exploring the Benefits of Tokenization of Discrete Acoustic Units (Interspeech 2024) 
[2] On the Effectiveness of Acoustic BPE in Decoder-Only TTS (Interspeech 2024) 

- Section 5.2: The explanations on the final unit extraction using clustering are vague. How did you combine K-means and Agglomerative clustering? 

- I find the task of unsupervised syllable segmentation is more suitable for speech-oriented venues such as ICASSP and Interspeech.

### Questions
Comments:
- It would be interesting to develop a joint algorithm for segmenting and clustering together. 
- Table 5: When training your tokenizer on smaller datasets with a single language and low input variability, it is easier to compress them and reduce the bitrate, as you have less information to distill into the discrete units.  

Writing/Typos:
Lines 14-17 (abstract) can be simpler and more concise

Line 172: Can you clarify: “C models the raw probabilities of the losses”

Line 158: “Two frozen Hubert models” - you used the same single model, right? (otherwise, their token space wouldn’t match..) 

Line 280: TWIST citet->citep

Table 2: Detaction->Detection

line 462: Regarding “the E2E GSLM pipeline is deep” — how about rephrasing it to “consists of several independently trained components”?

### Soundness
3

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
3

### Summary
This work introduces a controllable self-supervised technique to merge speech representations into coarser syllable-like units while still preserving semantic information. The propsed method produces controllable-rate semantic units at as low as 5Hz and 60bps and
achieves SotA in syllabic segmentation and clustering. Using these coarse tokens, authors successfully train SyllableLM, a Speech Language Model that matches or outperforms current SotA SpeechLMs on a range of spoken language modeling tasks.

### Strengths
Overall, I believe this is a valuable work, featuring a clear motivation, good technical contributions, and impressive experimental results. The use of semantic units as low as 5Hz undoubtedly holds significant value for training SpeechLLMs. Additionally, with under 90 hours of training, SyllableLM outperforms both the 13B parameter TWIST and the 7B Moshi on sBLIMP, indicating that this paper contributes meaningfully to both the speech and multimodal research communities.

### Weaknesses
The reason I gave a "boadline rej" is that I still have several concerns due to the somewhat unclear presentation of this paper. If my main questions can be adequately addressed during the rebuttal phase, I would be willing to raise my score.

1) If I understand correctly, SylBoost tokens are extracted from the waveform and include not only a sequence of tokens but also the start and end timestamps for each token. However, it’s unclear how SpeechLLM decodes these tokens when performing speech continuation, particularly in terms of predicting timestamps. Specifically, how exactly are timestamps handled during decoding? Is there a step-by-step process the authors could provide to clarify this? Additionally, the frequent mention of TWIST in Section 4.2 is somewhat confusing. My personal suggestion would be to focus more on the proposed method itself in the methods section, and simply add appropriate citations for references to other works where relevant.

2) I noticed that the authors used a cold-init approach for the 90M model. What are the potential advantages and disadvantages of using a larger text pre-trained model compared to the cold-init approach? How might this affect performance on specific downstream tasks?

3) In addition to semantic information, can SylBoost tokens also model acoustic information? Furthermore, regarding SyllableLM, what specific modifications to SyllableLM might be needed to improve its zero-shot TTS voice cloning capabilities?


Question (3) is intended solely for discussion and does not require corresponding experiments to demonstrate these capabilities.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
1

### Contribution
3
