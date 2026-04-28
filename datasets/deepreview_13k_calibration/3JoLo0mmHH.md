# Reverse the auditory processing pathway: Coarse-to-fine audio reconstruction from fMRI

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 3, 5, 8

## Abstract
Drawing inspiration from the hierarchical processing of the human auditory system, which transforms sound from low-level acoustic features to high-level semantic understanding, we introduce a novel coarse-to-fine audio reconstruction method. Leveraging non-invasive functional Magnetic Resonance Imaging (fMRI) data, our approach mimics the inverse pathway of auditory processing. Initially, we utilize CLAP to decode fMRI data coarsely into a low-dimensional semantic space, followed by a fine-grained decoding into the high-dimensional AudioMAE latent space guided by semantic features. 
  These fine-grained neural features serve as conditions for audio reconstruction through a Latent Diffusion Model (LDM). Validation on three public fMRI datasets—Brain2Sound, Brain2Music, and Brain2Speech—underscores the superiority of our coarse-to-fine decoding method over stand-alone fine-grained approaches, showcasing state-of-the-art performance in metrics like FD, FAD, and KL. Moreover, by employing semantic prompts during decoding, we enhance the quality of reconstructed audio when semantic features are suboptimal.
  The demonstrated versatility of our model across diverse stimuli highlights its potential as a universal brain-to-audio framework. This research contributes to the comprehension of the human auditory system, pushing boundaries in neural decoding and audio reconstruction methodologies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper aims to achieve audio reconstruction from an fMRI brain signal via a coarse-to-fine approach. The idea is to replicate the audio processing stream in the human auditory cortex. The method is threefold: first, it uses a CLIP-based approach to extract an audio representation (low-level description) from the fMRI data signal. From these initial features, a high-dimensional description of the auditory feature is obtained via a guided AudioMAE. Finally, these high-level features are used as a condition of a Latent Diffusion model for mel-spectrogram reconstruction and, thus, audio reconstruction. The method achieves high results on three publicly available datasets, demonstrating strong performance for both low-level and high-level audio metric reconstructions, showing improvement compared to the direct reconstruction of mel-spectrogram and other high-level approaches which omit low-level features.

### Strengths
- The technical contributions of the paper are strong. The methodology, with the threefold approach, is well thought out and carefully implemented. Many implementation details are provided, and the notations are clear and easy to follow. This is a great point.

- Figure 2 is clear and provides sufficient details to understand the intricate methodology

- The new method is compared against various baselines and three openly available datasets. Also, the code is made public, and additional results are provided. This is a great point for the openness of science. 

- Various ablation studies are done to confirm the contributions of specific modules (for instance the diffusion reconstruction vs using the MAE decoder).

### Weaknesses
 - One weakness of the paper is the limited neuroscientific motivations for audio reconstruction as a way to understand auditory mechanisms (first paragraph of the introduction). It is not clear from the introduction or the conclusion how solving this task could help to understand better the auditory processes (line 28  "This research contributes to the comprehension of the human auditory
system" ). Are these models generalisable between subjects? can a model trained on a single subject be used for another subject? can they be used to identify specific features related to language disorders? 

- Another major weakness in this study is the lack of clarity in the writing, which prevents us from understanding some of the motivations and results/discussion. The characterisation of "high-level/low-level" features and "coarse/fine-grained" features throughout the paper is very unclear. Some of these terms seem interchangeable in how they are employed; the paper would greatly benefit from a clear definition (see more related questions in the next section).

- Some points of the methodology lack details and/or seem to diminish the results (see questions in the next section). For instance, the modelling of the brain signal with ridge regression, which overlooks the spatial autocorrelation of the brain signal and structure of the auditory cortices, is not motivated. Sections 3.3 and 3.4 lack clarity, it is not clear what they aim to achieve with respect to the general motivation of the paper, and the conclusion are not clear and even seem to diminish previous results (for instance Figure 5 and  line 457 to 460) - see more questions below. 

- There are some important missing descriptions regarding the dataset and the training procedure. How is the data split between training and testing? is it subject-wise or dataset-wise? Are the same subjects used both for training and testing? functional alignment between subjects if direct comparison between them?

### Questions
**Improving clarity and motivations**

- The distinction between low-level (coarse) and high-level (fine-grained) features is confusing, lacks clarity and contributes negatively to the overall appreciation of the paper. Could the authors precise what they refer to as high-level or fine-grained features and as coarse or low-level features? It is confusing to refer to "semantics" as coarse, as they are supposed to provide very precise and high-level descriptive information. Similarly, the spectrogram is often referred to as high-level, although it describes low-level features similar to the features extracted by the cochlea (line 86).

- The description of the CLAP training (with aligned textual descriptions and audio) (line 147) and the use of prompts for incorporating music genres and phenotype information  (line 117), are considered as coarse features, why? 

- The paper refers to as "inverse pathway of auditory processing" (line 17). If it is inverse; shouldn't it go from high-level to low-level? seems that the method goes from coarse-to-fine ... "AudioMAE latent feature as the fine-grained acoustic embedding of audio" (line 182) isn't it coarse information?

- Typo line 466 ->"it's better"

- In line 52, what are the DNN features referred to? could the authors provide more explanations?


**Methodology/Results:**

-  It is unclear how the Semantic Decoder extracts semantically rich information (line 137); is it validated somehow? 

- One of the baseline modes is a Transformer that goes from voxel space to mel-spectrogram space. Could the authors provide more information about this implementation, as it does not seem straightforward?

- Could the authors provide some motivations for using ridge regression to model brain signals (referred to as $x$ in the paper)? does this consider the autocorrelation of brain cortical activation and using the structure and spatial organisation of the auditory cortex?

- Regarding the generation process and the use of the latent diffusion model, how much do the authors consider providing the ground truth as input to help the model (figure 3)? Isn't the conditioning should be enough?

- In tables 1, 2, and 3, are the results averaged across subjects? if yes could you provide the std? 

- In Table 1, why is C2F-LDM low for PCC and PSNR?

- The objective of section 3.3. and 3.4 are not very clear, for instance, lines 457 to 460. More importantly, the results do not seem to go in the direction of the conclusion of the paper, e.g. in Figure 5. b. why does the fine-grained decoding perform better for almost all experiments? The hypothesis made in section 3.3, e.g. "This could be attributed to participants being more focused on the content of the stories during fMRI signal collection, potentially disregarding the speaking style of the speaker." (line 453) is used to motivate the next section 3.4 but is relatively weak and unclear. In section 3.4, The Brain2Music dataset performs better without prompts, although the prompts are supposed to incorporate important information such as the music genre. Why use prompts, then? seems somehow superficial. 

**Data**:

- what about variation in performance across subjects? are the models trained per sujects? or models are used across subjects?

- how are the voxels in Table 4 extracted? Is it from a template? subject-based parcellation?

- Are the datasets aligned functionally (on top of anatomical registration) so that similar voxels and auditory regions across subjects can be compared?

- For all datasets, the audio clips seem to be between 1.5 and 4 seconds. Is it enough to aim at reconstructing audio from a very short fMRI temporal window? What about using larger windows?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work designs a system to reconstruct audio signals from human fMRI data collected while listening to natural sounds. The system separately handles fine-grained information (i.e., the precise timing and frequencies of the sounds) and course-grained information (semantic information such as the class of sound) by using different neural network features for each branch of the architecture. The authors evaluate their method on three different fMRI datasets and multiple different evaluation methods capturing the fine-grained and semantic nature of the sounds.

### Strengths
The paper tackles an interesting and challenging problem of trying to decode auditory fMRI activity. I like how it ties back into classic ideas of course-to-fine reconstruction. It also takes advantage of many recently proposed auditory models, similarity metrics, and auditory datasets.

### Weaknesses
 * The paper combines many different pre-trained systems. This makes the methods used difficult to understand, but also makes it hard to evaluate where things might be going wrong, and which pieces are critical. Due to the unknown inherit biases of each system, it is difficult to see how the work could actually be useful for understanding the human auditory system.

* As currently written, the presentation of results is confusing. The text should point to each set of results when they are discussed, rather than stating (line 357-359) that qualitative results are displayed in Tables 1 and 2. Additionally, it would be helpful if the columns were in some way separated or labeled for the “fine grained” vs. “semantic” measures.



### Questions
1)	For each of the metrics, it would be helpful to understand what a good value is, and if these are getting at all close to that value. Currently, it is difficult to interpret whether the observed differences are at all significant. For instance, for the semantic representations one could use a baseline score that is two different samples in time from the same audio clip.  And maybe a PCC and PSNR score could be referenced to samples with additive Gaussian noise of various SNR levels at the waveform?  

2)	Listening to the supplement audio files, I am not so sure that the proposed method is actually doing something reasonable. The samples “sound” more natural (which is expected from including a diffusion model in the pipeline), but they are often completely different sounds than the initialized audio, essentially hallucinations. PSNR levels of ~15-18 seem like they might be noise, relative to the original sound.  

3)	In the decoding section, one of the experiments is on male/female decoding which is called a “semantic” task. However, I believe a decent amount of male/female decoding can be achieved from simply looking at the overall power spectrum of the sound (male voices are generally lower than female voices). Thus, this doesn’t seem particularly “semantic”.  

4)	The metrics are not defined enough in the main text (Lines 311-319). At a minimum, the acronyms need to be defined. For instance, what is “PCC” and “PSNR”? Although some audio researchers may be familiar with these measurements, a more general ICLR attendee may not. 

5)	How many repetitions of each sound are present in each dataset and are these averaged for the analysis? More generally, how is fMRI measurement noise taken into account for the analysis? I.e., is there a sort of “noise ceiling” defined on the reconstruction? 

Somewhat minor suggestions for specific lines: 
* Line 075-077: This sentence doesn’t make sense to me. How does the “high-dimensionality” play a role here? The main challenge of fine-grained decoding is the lack of resolution in time and the inherently noisy signal of the fMRI response.  
* Lines 086-088: These references seem out of place, as the decomposition of sound into difference frequencies in the cochlea dates much further back than these papers. Some good references might be work by Shihab Shamma (maybe https://ieeexplore.ieee.org/abstract/document/119739, or https://pubmed.ncbi.nlm.nih.gov/16158645/) , but I would encourage the authors to perhaps cite classic textbooks or review articles on auditory processing 
* Lines 147-152: Which features are used in CLAP? The final output features or an intermediate stage? This should be mentioned in this section.  
* Line 231: “unpatchify” is not defined.

### Soundness
2

### Presentation
1

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
This paper presents a new method for reconstructing audio signals from fMRI responses to sounds. Specifically, it proposes a course-to-fine decoding strategy in which  fMRI responses from auditory cortex are decoded in a course-grained fashion into the semantic space of CLAP (which is not defined until page 3), and decoded in a fine-grained fashion into acoustic space.

I would not recommend this paper for acceptance. While the high-level approach seems interesting, the purpose of integrating neural data seems lacking in motivation, and the use of pre-trained representations in both training and evaluation seem to present a major confound. 



Figure 5 is confusing. What are the ‘features’ that are input into the SVM? And given the results and discussion that there is ‘little semantic content in the semantic features’ (line 449) the initial claim that semantic prompts during decoding ‘[enhances] the quality of reconstructed audio’ seems perhaps exaggerated (lines 25-26). 

A lot of the text is pushed to the appendix, making the official 10 pages lacking in sufficient detail and discussion. 

A lot of the writeup feels pretty inside baseball to this reviewer (or perhaps this reviewer is just too far outside this particular game). e.g. CLAP is not explained (though there is a reference) until page 3.

### Strengths
Technically, the method introduced here is interesting and seems sophisticated. 

The paper is well-written and makes use of highly relevant contemporary work—including studies done in machine learning and neuroscience—and uses this grasp of the literature to provide interpretations on different steps in their method. 

The paper does a nice job of comparing many different methods in addition to their own.

### Weaknesses
1. Lack of Clear Motivation: This reviewer got stuck at square one: what is the goal of this work? The authors don't tell us. If the goal were to understand brain function this work would proceed differently, for example separately analyzing primary versus non primary auditory cortex, asking which brain regions are best modeled by each component of the model, comparing decoded signals to human behavioral data, etc. Alternatively, perhaps it could be intended for BCI applications. But what would those applications be? If you have access to a person's auditory cortex then you would already have access to the sound they were hearing, so there would be no point trying to decode that information from the brain. A paragraph in the appendix (A.7) attempts to provide a motivation, but it doesn't make sense to me. For example it mentions that this work could  "aid individuals with voice disorders". But if an individual had a voice disorder, one would want to generate the intended spoken information, not the heard information from auditory cortex.

It’s unclear how the findings here contribute to the ‘comprehension of the human auditory system’ as stated in the abstract (lines 27-29). While the coarse-to-fine method is inspired by the human auditory system, it is not quite a model of ‘each physiological structure of the auditory processing pathway’ (lines 96-97)

2. Possible confound.
The results on many of the metrics suggest that the direct decoding methods better reconstruct audio than the C2F-LDM proposed here (Table 1, 2). The novel C2F-LDM method does improve on measures of FD, FAD, KL, and CLAP, but these results seem to present a confound. The reconstruction makes use of many model features from pre-trained models and are subsequently evaluated on their similarity to pre-trained model features. Thus would higher scores not be unsurprising?

3. Is the fMRI data even relevant?
The paper should address the role of fMRI data and how it improves the methods described here. The majority of steps requires pre-trained models and predicting their ‘ground truth’ representations, but the optimal value of P=0.25 seems to suggest that using these ground truth representations without the neural data may improve reconstruction.

### Questions
Figure 5 is confusing. What are the ‘features’ that are input into the SVM? And given the results and discussion that there is ‘little semantic content in the semantic features’ (line 449) the initial claim that semantic prompts during decoding ‘[enhances] the quality of reconstructed audio’ seems perhaps exaggerated (lines 25-26). 

A lot of the text is pushed to the appendix, making the official 10 pages lacking in sufficient detail and discussion. 

A lot of the writeup feels pretty inside baseball to this reviewer (or perhaps this reviewer is just too far outside this particular game). e.g. CLAP is not explained (though there is a reference) until page 3.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes a coarse-to-fine framework for audio reconstruction from fMRI brain recordings that outperforms the leading solely fine-grained approaches. This approach draws inspiration from the hierarchical processing found in the human auditory system. It first projects the audio and fMRI into a coarse-grained semantic embedding in the CLAP (Wu et al, 2023) space before paring that embedding again with the fMRI signal for fine-grained decoding, generating features in the space of AudioMAE (Huang et al, 2022). Lastly, an LDM is used to reconstruct the mel-spectrogram of the stimulus audio with the fine-grained embedding, before it is converted to the waveform using a pretrained HiFiGAN (Kong et al, 2020) vocoder.

The authors evaluate the performance of this framework over three different datasets encompassing three different classes of audio / reconstruction task (sound, music, and speech). The quality of the reconstructed audio is assessed by FD, FAD, KL, and CLAP score and the mel-spectrograms are evaluated using PCC and PSNR. Performance is benchmarked against direct decoding approaches and fine-grained only approaches. The authors also offer an investigation into the quality of the semantic information captured through these approaches.

### Strengths
Overall, this paper represents a novel improvement for brain-to-audio decoding and its acknowledgement would benefit the advancement of the field. The approach introduced is novel, performance state-of-the-art, and the presentation clean.

### Weaknesses
There are a few places where choices are made without explanation and parts of the discussion on the semantic analysis are unclear. For example, in the discussion of the semantic analysis it is stated that there is less semantic richness in the brain-to-speech case because listeners might be more focused on content. However, this effect does not necessarily seem to hold for the fine-grained only decoding (which is not addressed). It seems more likely that coarse-grained decoding may just be ill-suited to capturing semantic quality from speech as the signal clearly exists given the performance of the solely fine-grained approach. This represents a potential limitation of this framework for brain-to-speech. The choice of sex as the semantic class for the brain-to-speech case is not well justified. While it is acknowledged that speech semantics are complex, the selection of sex as a proxy seems arbitrary without a clear rationale beyond its presence in the CLAP model's training data. The link between sex and the broader semantic content of speech is tenuous, and it's unclear why other, potentially more relevant, semantic features were not considered. Furthermore, the claim that sex serves as an effective semantic prompt for guiding fMRI-based speech decoding requires more substantial evidence, as the improvement in reconstruction accuracy could be attributed to other factors.

### Questions
Questions:
- Why was sex selected as the semantic class for the brain-to-speech case?
- Just confirming that: semantic features of guidance = course-grained features in the CLAP space? (might be helpful to state this more explicitly)

### Soundness
3

### Presentation
4

### Contribution
3
