# MERT: Acoustic Music Understanding Model with Large-Scale Self-supervised Training

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
Self-supervised learning (SSL) has recently emerged as a promising paradigm for training generalisable models on large-scale data in the fields of vision, text, and speech. 
Although SSL has been proven effective in speech and audio, its application to music audio has yet to be thoroughly explored. This is partially due to the distinctive challenges associated with modelling musical knowledge, particularly tonal and pitched characteristics of music.
To address this research gap, we propose an acoustic \textbf{M}usic und\textbf{ER}standing model with large-scale self-supervised \textbf{T}raining (\textbf{MERT}), which incorporates teacher models to provide pseudo labels in the masked language modelling (MLM) style acoustic pre-training.
In our exploration, we identified an effective combination of teacher models, which outperforms conventional speech and audio approaches in terms of performance. 
This combination includes an acoustic teacher based on Residual Vector Quantisation - Variational AutoEncoder (RVQ-VAE) and a musical teacher based on the Constant-Q Transform (CQT). 
Furthermore, we explore a wide range of settings to overcome the instability in acoustic language model pre-training, which allows our designed paradigm to scale from 95M to 330M parameters.
Experimental results indicate that our model can generalise and perform well on 14 music understanding tasks and attain state-of-the-art (SOTA) overall scores.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed MERT, an SSL  model for music representation. The model is based on MLM training such as Hubert, and utilizes multiple pseudo targets during the pretraining stage such as k-means, constant-Q Transformation, and neural codec codes. By combining different self-supervised targets, experiments on 14 diverse downstream MIR tasks show that MERT is able to extract good representation for MIR tasks and attains SOTA overall scores. The checkpoints and code are open-source.

### Strengths
1. The method is simple but effective. The paper demonstrates the importance of choosing appropriate pseudo targets.
2. Considers a diverse set of MIR tasks for evaluation, providing a good standard that can be followed by future works.
3. Unlike many previous closed-source works, this paper has made the checkpoints publicly available, which is a significant contribution to the research community.

Overall, the paper is well-written with a clear goal and provides sufficient experiment results to support the claims. Although the conclusions are not surprising, the work is still significant for the related research community from a practical perspective due to its reproducibility and accessibility.

### Weaknesses
There are 2 minor concerns.
1. Since RVQ-VAE is pre-trained on a larger dataset, comparing MERT with CQT/k-means and MERT with RVQ-VAE is somewhat unfair.
2. The experiment should verify how RVQ-VAE code performs on downstream tasks to prove that the proposed MLM training phase with RVQ-VAE code as the target is required. Otherwise, one can directly utilize codes and codebook vectors from RVQ-VAE as upstream representations instead of MERT.

### Questions
1. How do you calculate "Previous SOTA average score" in Table 2? The number did not match any baselines listed in the table, is it referenced from another work?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a self-supervised model for acoustic music understanding based on similar self-supervised learning paradigms in speech processing. The authors provide extensive comparison on 10 different MIR tasks some of which require understanding the local characteristics (such as pitch and beat), whereas some require a track-level understanding (such as genre, or emotion).

The authors experiment with two different teacher paradigms. They work with one 95M parameter model that is trained on publicly available music, and another larger model with 330M parameters that they train on 160k hours of music mined from internet. They compare their variants against the state of the art, and show that the model achieves similar or better results compared to the current state-of-the-art.

### Strengths
- Extensive comparison between different models, conditions and # parameters on various MIR tasks. 
- The results indicate the strengths of the proposed model (e.g. efficacy on tasks that require local-level musical information) as well as the limitations (e.g. 5 second excerpts)
- Provide a strong baseline for future research on self-supervised learning on acoustic music that is comparable to the current state of the art.
- Extensive literature review, which facilitates to convey the basis of the work as well as the motivations
- The authors explain issues they have faced while training the model, and also how they mitigated these issues, which is invaluable for future research. See the Training Stability part in Section 4.3. as an example.
- Open source code, experiments and dataset (where shareable)
- The language is appropriate for an engineering work, and the paper is easy to follow.

### Weaknesses
- Works on short excerpts. The authors argue that this limitation could be overcome in future work.

### Questions
- We mined 160K hours of music recordings from the Internet ... 

What are the typical sources for mining? Youtube, streaming services, Freesound, or something else? What is the typical audio quality? Are they copyrighted, or not? Do you keep the audio or only the relevant features (MFCC, CQT?)

- Some references are not well formatted and/or they miss key information (in particular the conference). Examples:

Alonso-Jimenez, P., Serra, X., and Bogdanov, D. (2022).
Bogdanov, D., Won, M., Tovstogan, P., Porter, A., and Serra, X. (2019)
Chen, W., Keast, J., Moody, J., Moriarty, C., Villalobos, F., Winter, V., Zhang, X., Lyu, X., Freeman,
E., Wang, J., et al.

- While Table 1-2 are compact and informative, it's impossible to track the references apart from following the hyperlinks as the Reference formatting do not include the number. 

- Although they should be known in general, I would suggest the authors to mention the full name of all the metrics such as R2 or ROC used in the experiments.

In addition, some of the "previous SOTA" (e.g. 26, 36) are still the best. Wouldn't it mean that they are still the state-of-the-art?

- Appendix D - Ethics. I think there should be a mention of music copyrights here, in particular the implications about mining music from the Internet.

Below are minor suggestions and nitpicks that I'd like to provide for the sake of completeness. They do not contribute to my decision on the paper.

- The writing switches between British and American spelling, e.g. "masked language modeling" vs. "masked language modelling."
- Nitpick: Page 4 "data sample in a speech or language dataset..." -> the dataset doesn't have to be speech or language, e.g. it can contain instrumental music. 
- "Additionally, we present the advanced SOTA for each task including" -> This phrase could be read as the proposed model advances the state of the art for all tasks, which is not necessarily the case. If I understand correctly, "the current SOTA" is a better wording.
- "... longer contexts if required" ->  longer contexts, if required (missing comma)
- Page 17 is almost fully empty.
- Figures 2 - 6 are very useful, however, they are not suitable for color-blind readers. I would suggest to change the line/marker styles for each  element in the legends.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper describes self-supervised learning technique for music audio. The most relevant previous work is HuBERT in speech domain which uses masked prediction learning using codeword of audio features. The authors applied this method to music audio and developed several techniques on top of the reference model. Basically, the most contributions lie on how they build codewords specifically dedicated to music audio. To do that, they mainly compared three ways which are MFCC-based codeword (K-Means), LogMel+Chroma-based codeword (K-Means), and EnCodec. MFCC and Log-Mel-spectrogram mainly captures timbre information from audio, so they utilized Chroma to compensate tonal information of music. Also, there has been a previous work called EnCodec which is a pre-trained codec encoder designed for music audio, so that this model already has some ability to capture both timbre and tonal information. Also, they added CQT loss to further enhance pitch and chord level information. In the end, the authors verified the models on 14 Music Information Retrieval tasks (mostly segment-level tasks, not note-level or frame-level). The results showed that EnCodec-based approach was the best performing model.

### Strengths
The strengths of the paper comes from how the authors tailored the previously proposed method to music audio domain. To do that, they tested various music audio specific techniques such as Chroma, CQT, and EnCodec. The results showed that these additional method improved the model performance on several downstream tasks that are more related to pitch, chord, tonal information of music. For the tasks where timbre information is important, the effect of using these tonal features is marginal.

### Weaknesses
The weaknesses of the paper is on novelty. If we see the results in Table 1 and 2, the trends are quite predictable even though the proposed method achieved SOTA performance on 3 tasks out of 14 tasks. For the models that doesn't utilize chord information, still those models achieve good performance on tasks where timbre is important (such as tagging, genre, mood, theme), however, if any methods includes to use this kind of information, then it shows good performance on both timbral and pitch related tasks. Also, it seems many performance boosts are made through the EnCodec, I think the novelty of the approach itself is a bit weak.

### Questions
If the used split of each downstream tasks can be written more in detail in Appendix, it would be better.
In Section 4.1, where GTZAN and MTG-Genre downstream task's metric is explained, only ROC and AP is mentioned, I think accuracy can be added.
In Section 4.3, "1.5 and 5.5 hours" is not a batch.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents MERT - large scale self-supervised models for music tasks. The approach is built primarily on top of the speech SSL approach (Hubert). Aside from K-means, MERT proposes to use Encodec to get targets for SSL pre-training. Reconstruction loss on Constant-Q transform is also used for training. The pre-training is done on 1K hours of music data and then a 160K hour of music data. In terms of model size MERT offers two flavors: a 95M parameter model and a 330M parameter model. The MERT model is evaluated on a wide range of music tasks - Music tagging, music genre classification, instrument classification and so on.

### Strengths
– The paper presents self-supervised learned models for music audio. Better large scale SSL models for music are definitely desirable and the paper is a fair attempt at building such models. Moreover, the paper aims to make the model open-source which can definitely help in future development of SSL models for music. 

– The paper describes the approach clearly. The datasets, downstreams tasks etc. are also well described. 

– Discussions on challenges in scalability and training stabilities are also discussed. I think that’s a good topic to touch upon. 

– The paper also does downstream evaluation on a variety of music datasets. This creates a really good benchmark for evaluations.

---- 
Increased score after rebuttal.

### Weaknesses
– The presented approach is primarily minor modifications of existing SSL models and the significance of the MERT training approach itself  is limited. It’s not fully established that the modifications over Hubert are really adding substantive improvements in performance. 

–  “Computationally affordable”, “cost-effective”, “lightweight sizes”  etc. are frequently used for the proposed MERT but it is not really clear how all of these are attained for MERT. How is MERT more computationally efficient or lightweight  than say Hubert-Base. Aren’t the models similar ? What efficiencies are we expecting here? Is it just about K-Means vs uses of codebook from Encodec ? This aspect has been highlighted several times in the paper so it would be good properly establish (quantitatively ??) how MERT is better than others.  

— Is it necessary to use all 8 layers of codebooks ? perhaps some additional experiments to better show how results vary with codebooks from different layers would be good. 

— Related to the previous point, how about using Encodec itself as SSL representation. Codec is used in MERT as a teacher - can codec itself be used as a SSL model for music. Isn’t that a baseline one can have ? 

— The “AVG” column in Table 2. What is it avg of ? of all the other columns ? I am not sure looking at avg of different types of metrics over different datasets is a good way to look at overall results. 

– Comparing “HuBERT base” and MERT-95M^{K-Means} it seems that they are pretty similar. 

– For all of the downstream experiments, is the full training set for each dataset used in the experiments ? I think some experiments on “limited training data” would be useful. Otherwise, these models are not really outperforming the supervised baselines – which does not full justify the SSL pre-training. 

– In Sec 5.1, the paper describes that the model is doing better on local-level music tasks compared to global level tasks. Some more discussion and perhaps illustration of why this is happening would be super helpful.

### Questions
Please respond to the points in the weakness section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
