# SoundMorpher: Perceptually-Uniform Sound Morphing with Diffusion Model

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 3, 5

## Abstract
We present SoundMorpher, a sound morphing method that generates perceptually uniform morphing trajectories using a diffusion model. Traditional sound morphing methods models the intractable relationship between morph factor and perception of the stimuli for resulting sounds under a linear assumption, which oversimplifies the complex nature of sound perception and limits their morph quality. In contrast, SoundMorpher explores an explicit proportional mapping between the morph factor and the perceptual stimuli of morphed sounds based on Mel-spectrogram. This approach enables smoother transitions between intermediate sounds and ensures perceptually consistent transformations, which can be easily extended to diverse sound morphing tasks. Furthermore, we present a set of quantitative metrics to comprehensively assess sound morphing systems based on three objective criteria, namely, correspondence, perceptual intermediateness, and smoothness. We provide extensive experiments to demonstrate the effectiveness and versatility of SoundMorpher in real-world scenarios, highlighting its potential impact on various applications such as creative music composition, film post-production and interactive audio technologies. See \href{https://xinleiniu.io/SoundMorpher-demo/}{SoundMorpher-demo} for the listening demonstration.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new method for sound morphing, defined as the generation of a sequence of perceptually intermediate sound samples for a given pair of source and target audio. As this problem is not very common in the audio processing community, the authors introduce different formulations of the problem (e.g., static vs. dynamic morphing) and discuss the criteria for a good morphing path, including correspondence, intermediateness, and smoothness. The authors propose an original method of sound morphing based on interpolating latents within AudioLDM2, demonstrating impressive results compared to the baseline. They also introduce several heuristics to make the transitions between consecutive samples along the morphing path more uniform and stable, including LoRA fine-tuning of AudioLDM2 and finding an optimal sequence of interpolation coefficients using binary search. Finally, the authors describe various experiments that demonstrate the strong performance of their model across different scenarios and audio domains.

### Strengths
- The proposed method is very reasonable and has already shown good results in image processing;
- Mostly, the quantitative comparisons are solid and show the effectiveness of the method in various audio domains;
- The paper proposes metrics to measure the morphing quality in terms of correspondence, intermediateness and smoothness which is important for further development of this research topic.

### Weaknesses
 - The contribution of the paper is relatively incremental as the paper borrows most of its ideas from (Yang et al. 2023). All essential features of the proposed method such as latents interpolation inside a Latent Diffusion Model, LoRA adaptation, finding the optimal trajectory with binary search on a sequence of values of an auxiliary metric, and even the introduction of 3 metrics for model evaluation, were proposed in (Yang et al. 2023). The paper is basically an attempt to adapt the approach introduced in (Yang et al. 2023) to audio domain. The main challenge the authors face in this study is related to tuning AudioLDM 2 and designing perceptual metrics as in (Yang et al. 2023).
- Comparison with only one baseline on a music domain given in Table 1 seems insufficient to provide full understanding of the performance of the method. Although objective metrics and the recordings given in the supplementary material demonstrate huge improvement over the baseline, it more likely suggests that the baseline may be too weak or poorly tuned. 
- The MOS scores given in Table 4 don’t have any grounding such as GT intermediate samples or a baseline which makes them uninterpretable. Moreover, because of a small number of assessors, the variance of the score is too large.
- Table 5 shows no improvement over the baseline in 2 metrics of 3. Intuition of the qualitative difference corresponding to the improvement of 0.04 in the first metric is not provided. Some illustrations of spectra and/or audio samples in the supplementary material corresponding to different levels of CDPAM may help here.
- Metric MFCC_Se introduced in Appendix 8 doesn’t evaluate the portion of the content from x_{source} and x_{target} but similarity of the spectra. The metric is easily minimized when we average x_s and x_t. 
- Minor issues: “Spectral contras” p.9:450; “Mean opinion socre” p.20:1034

### Questions
The recordings given in the supplementary material are either midi or short isolated environmental sounds which raises concerns about applicability of the method to real data. Did you try to apply your method to real music recordings?

### Soundness
2

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
5

### Summary
The authors present a method to morph sounds in an intended way.

They rely on a pretrained AudioLDM2 model (a latent diffusion model for sounds and music) and propose to generate morphed sounds by interpolating between two sounds. 

"Textual inversion" is performed in the condition embedding level for each sound to obtain embeddings $E$.
Latent representations $z_T$ are obtained using the probability flow ODE.
Morphed sounds are obtained by generating using the probability flow ODE from $(z_T^\alpha, E^\alpha)$ where the $z_T^\alpha$ is a slerp interpolation of the $z_T$'s and $E^\alpha$ a linear interpolation of the $E$'s.

Binary search is then performed on this trajectory parameterized by $\alpha$ to obtain samples equally-spaced according to some perceptual measure, relative L2 norm over mel spectrograms in the present case.

### Strengths
The paper is well-written and easy to follow, with examples provided in the supplementary material.
There is an extensive experimental part with a user study, but mainly compares with SMT.

### Weaknesses
 - The paper lacks novelty. Most of the elements presented in the paper do come from 
Yang et al.2023 IMPUS: IMAGE MORPHING WITH PERCEPTUALLYUNIFORM SAMPLING USING DIFFUSION MODELS.
The present paper can thus be seen as a straightforward adaptation of IMPUS to the audio domain.
- If LPIPS was chosen in IMPUS as the perceptual metric, here the choice of L2 over mel-spectrograms may be less appropriate. The use of L2 distance on mel-spectrograms, while computationally simple, may not accurately capture the perceptual nuances of audio morphing. This is because mel-spectrograms, while representing frequency content, do not fully account for temporal dynamics and phase information, which are crucial for human auditory perception. A more perceptually relevant metric, such as those based on auditory models, might be more suitable.
- Concatenating audio segments in Eq. 8 in x-space seems to produce abrupt transitions. Please not that with most of the architectures used for diffusion models, it would be possible to have this chunk-based generation done directly in z-space.

- There are some missing references concerning controlled interpolations using audio diffusion models.
- Provided audio examples are not particularly convincing and transitions sound abrupt, especially with as few points as five.



### Questions
- Where do the "Static morphing; Cyclostationary morphing & Dynamic morphing" terms come from?
- Why not using CDPAM as the perceptual metric? 
- The choice of the interpolating path is pretty arbitrary, and the presented technique could be applied over any path. Is the perceptual metric always monotonic over these trajectories?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a MusicLDM2-based inference-time method (requiring no model training or fine-tuning) for morphing various types of music and sounds across scenarios such as timbral morphing of musical instruments, environmental sound morphing, and music morphing. The authors claim their approach differs from traditional sound morphing methods, which assume a straightforward, linear relationship between the morph factor and perceived sound qualities. Traditional methods oversimplify the complexity of sound perception and limits morph quality. In contrast, they propose SoundMorpher, which establishes a more accurate, proportional mapping between the morph factor and the perceived characteristics of morphed sounds using Mel-spectrograms. SoundMorpher employs the Sound Perceptual Distance Proportion (SPDP) ensuring that changes in the morph factor correspond uniformly to perceptual changes. This approach enables smoother sound transitions and maintains consistent quality across different sound-morphing tasks.

The paper also introduces metrics to evaluate sound morphing systems based on three key criteria: correspondence, perceptual intermediateness, and smoothness. Extensive tests demonstrate SoundMorpher's effectiveness and adaptability, with potential applications in music creation, film post-production, and interactive audio technologies. 

Demo audio files are provided in the supplementary material.

### Strengths
This is a fairly well-written paper. I found it interesting and a pleasure to read. Even though the method it presents is not a groundbreaking novelty and is only an inference-time "trick" to achieve good sound morphing, I found it a clever way of handling and extracting desired results from a pre-trained generative model. The related work section is quite comprehensive (at least, I couldn’t recall any paper that hasn't been mentioned here), the objectives of the work are clear, and the method is fairly well explained. The proposed metrics do make sense (I’ll come back to this in the weaknesses section), and the algorithms (show in the appendix) and descriptions of the methodology are quite comprehensive and help understanding.

### Weaknesses
Here is the list of my concerns following the order of the sections.

Sound morphing preliminary:

In the paragraph of line – 141 -149, authors define 3 criterias Correspondence, Intermediateness, and Smoothness. I think there are lots of critiques one can brung up to these criterias.

1.	Correspondence: This criterion requires that the morph captures semantic-level transitions. However, perception of “semantic” qualities in sound can be subjective and context-dependent. If listeners interpret these qualities differently, then it may be difficult to ensure correspondence consistently across diverse types of sounds, especially if the morphing involves highly variable sources, like environmental sounds versus musical instruments. The paper does not address how the method handles the inherent ambiguity in semantic interpretation of sounds, which is a significant limitation.

2.	Intermediateness: This criterion expects listeners to perceive intermediate morphs as “between” the source and target sounds. However, the perceptual “in-betweenness” may not always be straightforward in audio and can be (again) subjective. If sounds have distinct timbral qualities, they might not blend smoothly. In such cases, perception could be binary or categorical(?), with certain morphing points perceived as “closer” to one sound or the other rather than as true intermediates. For example, in the audio demo files, there is a cat-to-dog morph. Sometimes, the cat's meow gradually changes into a dog’s bark, but at other times, there is an intermediate sound containing both the cat and dog sounds (like an audio scene where both animals are present, which is quite realistic and could be perceived as intermediate). So, which of these is truly intermediate? Or are both? I don’t see a clear description addressing this. Please correct me if I’m missing something. The paper lacks a discussion on how the method distinguishes between a true intermediate sound and a composite sound containing elements of both source and target, which is crucial for evaluating the effectiveness of the morphing process.

3.	Smoothness: This criterion assumes that a linear change in the morph factor will correspond to a consistent, linear perceptual transition. I have a major question here: why is a linear change necessarily good? As we know, sound perception does not always follow linear increments; auditory characteristics like volume and pitch are often perceived on logarithmic or exponential scales. This means that, depending on where we are in the spectrum, even small changes in the morph factor might lead to abrupt perceptual shifts, while large changes may go unnoticed by human listeners. This would violate the criterion of smoothness, correct? For example, if a bass instrument is morphing into a high-pitched violin and pitch is increasing by a fixed step (say 100 Hz), that change at a low frequency would be perceived as quite large, while at higher frequencies (around 2000 Hz), the same 100 Hz step wouldn’t be perceived as a significant change. So, what exactly do the authors mean by "linear change"? when they say linear in context of perceptual doe this mean logarithmic in metrics? I didn’t find a clear explanation on this in the paper but this is a major question, I think, and need to be mentioned and clearly explained. The paper does not clarify whether the linear change in the morph factor is intended to correspond to a linear change in the Mel spectrogram domain or in the perceptual domain, and this ambiguity significantly undermines the validity of the smoothness criterion.

Evaluation:

My main concern with this paper lies in the experiments and evaluation section. The issue I see is that the work develops its own metrics and then uses these motly for just reporting the number of the model. For the comparison with baseline(s) same metrics are used, rather than relying on established metrics (at least thiose used in the prevous work for fair comarison). This approach makes comparisons with existing work somewhat shaky.

Here are the details.

1.	Evaluation metrics

Lines 1021 and 1023-1024: Did you mean “consecutive” instead of “consentive”? The calculation of FAD and FD is unclear. Are these values averaged? The paragraph starting at line 1019 is not entirely clear. I see there are instrument groups, but it’s not fully explained how FAD and FD are calculated along the morphed path. Sounds in the middle of this path would presumably be intermediate between the two instruments. Are we calculating FAD and FD across the entire sequence and then averaging, or only at the midpoint? If it's the midpoint, what are we comparing it to—the source or the target? I’m unsure what FAD and FD are meant to reveal in this context. Could you provide a more detailed explanation, maybe including a formula for how final FAD is calculated in the tables (lines 270, 380, and 447)? The paper lacks a clear explanation of how FAD and FD are computed across the morphing sequence, making it difficult to interpret the reported values. The description is ambiguous, and it is unclear whether the metrics are calculated at each step of the morphing sequence or only at specific points, and how these values are aggregated.

Lines 316-320: use of CDMAP seems not fully justified.  CDMAP is typically used for speech. Is it suitable for measuring instrument and environmental sounds? Could you provide some justification for why this metric is relevant here? The paper does not provide sufficient justification for using CDMAP for evaluating instrument and environmental sounds, given that it is primarily designed for speech. The paper needs to explain why the features extracted by CDMAP are relevant for non-speech audio and how they capture the perceptual qualities of interest in this context.

2.	TIMBRAL MORPHING

The baseline model chose here is weird the Sound Morphing Toolbox (SMT) from Caetano, 2019. This is very old and not a ML model. Why don’t authors use some more recent work for the comparison. In the demo files the files generated by SMT sound terrible! I don’t think SMT is even worth considering as a baseline. I’m sure much better quality of audios can be achived by usieng any other concurent ML based baseline. The choice of the Sound Morphing Toolbox (SMT) as a baseline is inadequate, as it is an outdated signal processing method and not representative of current machine learning-based approaches. This makes the comparison unfair and does not provide a meaningful benchmark for the proposed method.

3.	ENVIRONMENTAL SOUND MORPHING

No baseline, Just showing the numbers for their own metrics.

4.	MUSIC MORPHING

Same concern here, no baseline! I don't undestand what are are these numbers say without a baseline...

5.	Subjective Evaluation:

Again, for some reason, the subjective (human) evaluation does not compare the proposed method with other methods. 

Generally, in the paper, baseline models are not used in the evaluation. The paper only presents results for the proposed model, with the only comparison being in timbral morphing for musical instruments—and even that is with an older signal processing method, the Sound Morphing Toolbox (SMT) from Caetano, 2019. The related work section references numerous concurrent works in the field, so I don’t understand why the authors did not adopt any of these as baselines. The lack of baseline comparisons across all scenarios significantly limits the evaluation's validity and makes it difficult to assess the true performance of the proposed method relative to existing techniques.

6.	Model comparison

In the "Model Comparison" subsection at line 472, the authors compare their method to a concurrent work, MorphFader (Kamath et al., 2024), but they only use the 7 examples provided on the demonstration page of that work. I don’t believe that 7 examples are sufficient for a robust comparison. I would have liked to see a comparison with this model (or other concurrent models) across all scenarios with all metrics and bigger test dataset, including those used by the baseline models, for a fair assessment. Additionally, they report only CDPAMT, CDPAMmean±std, and MFCCsE—why limit the metrics? The comparison with MorphFader is inadequate due to the limited number of examples and the restricted set of metrics used. This does not provide a comprehensive evaluation of the proposed method against a state-of-the-art approach.

There are some small typos and grammatical errors that I spoted:

In the line 013: if I understand what authors say correctly, "models" should be "model" to match the plural subject "methods."

Line 243 there is a typo: adaption->adaptation.

It would be nice to have table 1 on the page where it is dsuicussed.

Line 444-445, in the table 3 N is number of components of PCA? This is misleading because N was used for N a number of sounds in morphed sequence between sores and target lines (190—193).

The experiment section is structured a little weird. I don’t understand why in experiments (where we also have results presented by scenarios) we have subsection “discussion”. And this subsection presents Mean opinion score, which, in my opinion, is the most valuable part of results section.

Line 1207 – instead of “achieves” must be “be achieved”, I suppose.

### Questions
Questions and Suggestions for Improvement

From the comments above here are some questions/suggestions for the authors:

Sound Morphing Preliminary:

o	Correspondence: few words about subjectivness of the semantic meaning would help here I think.

o	Intermediateness: The example I gave in the comments above, the cat-to-dog morph in the demo files sometimes produces an "in-between" sound that contains both the cat and dog sounds, which might be realistic but isn’t necessarily an intermediate. Could the authors clarify what qualifies as intermediate? Are both interpretations valid?

o	Smoothness: Could the authors explain what they mean by "linear change"? Although numbers are used (Mel spectrograms in this case), it’s still not fully clear. For elements like pitch and loudness, does this “linear change” involve logarithmic scaling in metrics? Is it based on human perceptual linearity, and if so, what exactly does that mean, and how does it translate to audio metrics? A more explicit explanation would be helpful. In lines 258–265, the authors state that the Mel spectrogram is a good approximation of human perception, but I think a few more words on the logarithmic nature of audio perception and how the Mel scale assists here would strengthen the explanation.

________________________________________
Evaluation Concerns:

2.	Evaluation Metrics:

o	Please provide exact formula of how FAD and FD are calculated or please direct me to where it is presented.

o	Could you provide justification for why CDPAM is relevant metric?

3.	Timbral Morphing:

o	The choice of baseline model (Sound Morphing Toolbox from Caetano, 2019) seems outdated and not representative of current ML methods. Could the authors consider more recent ML-based baselines? This would provide a fairer comparison, especially as the SMT-generated audio files seem quite low quality.

4.	Environmental Sound Morphing:

o	No baseline model is used here, and the results are presented only with the authors' own metrics. Could the authors incorporate a baseline to add context to their results?

5.	Music Morphing:

o	Similarly, no baseline model is used here. Without a baseline, it is difficult to interpret the significance of the reported results. Could the authors add a comparison baseline to strengthen the evaluation?

6.	Subjective Evaluation:

o	In the subjective (human) evaluation, no comparison is made with other methods. Why did the authors choose to evaluate only the proposed model, especially considering the number of concurrent works mentioned in the related work section? Adding more baseline comparisons would enhance the evaluation's rigor.

7.	Model Comparison:

o	In the "Model Comparison" section (line 472), would it be possible to expand this comparison across all scenarios, including metrics from MorphFader or other models, for a fairer and more comprehensive comparison? Additionally, the authors report only CDPAMT, CDPAMmean±std, and MFCCsE. Why were these metrics chosen, and why were other metrics not included?

### Soundness
3

### Presentation
2

### Contribution
3
