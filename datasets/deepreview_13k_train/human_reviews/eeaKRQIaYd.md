# Unsupervised Sign Language Translation and Generation

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Motivated by the success of unsupervised neural machine translation (UNMT), we
introduce an unsupervised sign language translation and generation network (USLNet), which learns from abundant single-modality (text and video) data without parallel sign language data. USLNet comprises two main components: single-modality reconstruction modules (text and video) that rebuild the input from its noisy version in the same modality and cross-modality back-translation modules (text-video-text and video-text-video) that reconstruct the input from its noisy version in the different modality using back-translation procedure.
Unlike the single-modality back-translation procedure in text-based UNMT, USLNet faces the cross-modality discrepancy in feature representation, in which the length and the feature dimension mismatch between text and video sequences.
We propose a sliding window method to address the issues of aligning variable-length text with video sequences.
To our knowledge, USLNet is the first unsupervised sign language translation and generation model capable of generating both natural language text and sign language video in a unified manner.
Experimental results on the BBC-Oxford Sign Language dataset (BOBSL) and Open-Domain American Sign Language dataset (OpenASL) reveal that USLNet achieves competitive results compared to supervised baseline models, indicating its effectiveness in sign language translation and generation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The model is proposed for cross-modal unsupervised learning. It focuses on unsupervised sign language translation and generation and it learns the task without requiring parallel sign language data. The model consists of four modules: text reconstruction,  video reconstruction, text-video-text translation, and video-text-video reconstruction.

### Strengths
The overall writing quality is good although there are some issues.

The method is unsupervised which is important in the area as it requires experts to annotate. Also, inspired by unsupervised machine translation and applying the idea to another domain is the originality of the method.

The proposed methods support the writing with detailed formulation and figures.

### Weaknesses
Discussion about existing text-to-video aligner algorithms is not sufficient. For example, although text2video[1] is a text-based talking face generation model, it uses an aligner for phoneme-to-pose.

It seems back translations are highly similar to reconstruction loss that is used in image generation, especially in unpaired I2I tasks for cycle consistency. So you might consider elaborating this in the manuscript.

There are no visual results on the manuscript and limited visual results on the supplementary materials. I think it needs to be more convincing that the model is capable of generating sign language videos with high quality.

### Questions
1. The style of equations 10-12 does not fit the manuscript. Authors can consider changing their style to make them consistent with the other equations and the rest of the paper.

2. Why there is no evaluation for the fidelity of the generated videos in terms of well-known metrics such as FID, LPIPS, etc.

3. Why there is no discussion and explanation of the methods proposed in Albanie 2021 in detail as it is the only method that you make a quantitative comparison? I think it needs to be presented more and more importantly the differences and similarities between this and the proposed methods should be highlighted more.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper develops an approach for unsupervised SL translation and generation entirely using from non-parallel datasets. The motivation is that there is not a lot of paired text and sign language video, so the authors leverage ideas in machine translation and multimodal modeling to build better (unsupervised) sign-text representations. 

The approach contains 3 parts: a masked seq2seq text reconstruction module, signing video reconstruction which uses downsampled discrete latent representations (VQ-VAE) with a GPT-style decoder, and back-translation between each modalities to go from text-to-video-to-text and video-to-text-to-video. There is a disconnect in lengths of text and video sequences, so they use a sliding window aligner to map between each. 

Results are in some cases better than a supervised baseline on the same dataset and show promise for the approach.

### Strengths
* Developing unsupervised approaches for SL generation/translation is important, especially given the many different representations used for signing. One could imagine fine-tuning this approach for any given representation (e.g., Glosses, HamNoSys). 
* There are reasonable comparisons to supervised approaches.  
* The ablations /sensitivity analysis comparing this approach with different aspects turned off is interesting. 
* Given the lack of work in this area, it was valuable to see comparisons such as Table 6 on the WMT 2022 sign language translation task

### Weaknesses
Overall the results (e.g., Table 1 & 2) are seemingly very poor. This is by no means a reason to reject a paper, but it does in my opinion require the authors to dig deep into 'why' the results are poor and to work towards building an understanding for how they can be improved significantly. It is nice to see that some results are better than the supervised baseline from Albanie et al., but in an absolute sense they are still low. Are there oracle experiments that could be run? How can the problem be made easier to better understand paths towards success?

One thing that immediately stuck out after going through the appendix is that the visual quality of the SL generations, and likely even the video reconstructions, appear to be too low fidelity to capture important hand or face information. Has there been any experimentation around using different resolution inputs for the video model? Perhaps by doubling or quadrupling the video resolution the model would be able to pick up on more nuance. An alternative approach might be to use key point or whole-body representations (e.g., SMPL) as many recent papers on SL translation have done.

One limitation of the existing approach is that (if I understand correctly) it exclusively trains on BOBSL. On the text encoder side I could imagine it being valuable to leverage existing LLMs and then fine tune. Perhaps the same could be done on the video side? Although I'm not sure what pertaining model or dataset would be the most effective for signings.

On page 5, there is a reference to Sutton-Spence & Woll stating that when signers are translating text then signs will tend to follow the English word order. While this may be true for translating text, it's unclear if it is correct for the datasets used in this paper. Have you validated this on your datasets?

### Questions
I would like to see responses to some of the line of inquiry in the weaknesses section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Inspired by the success of unsupervised NMT approaches, this paper proposes USLNet, an unsupervised SL translation and generation approach. USLNet has three main components, namely: text reconstruction module, video reconstruction module and finally cross-modality back translation module. The authors also propose a sliding window based approach to address the alignment issues that are inherent in broadcast SL datasets. The proposed approach is evaluated on BOBSL, however the reported results suggest the proposed approach does not meet the expectation of a translation system (~0.2 BLEU4 score).

### Strengths
To the best of my knowledge this is the first bi-directional (translation/generation) SL approach that is trained in an unsupervised manner. Although the results are not promising, the proposed method is sound, and further studying the unsupervised training approach might yield promising results.

### Weaknesses
Although I like the idea of using pretrained large-scale models and unsupervised learning, I'd expect quantitative results to back up the benefits of employing these ideas. Sadly, the presented results does not suggest the presented approach to be "working" (~0.2 BLEU-4 score on BOBSL, while the state of the art is above 2 https://openaccess.thecvf.com/content/ICCV2023W/ACVR/papers/Sincan_Is_Context_all_you_Need_Scaling_Neural_Sign_Language_Translation_ICCVW_2023_paper.pdf)

That being said, the reviewers and the readers should acknowledge how challenging the BOBSL dataset is, and that we still need several breakthroughs to progress in large scale SL translation/generation.

Therefore to strengthen the paper, I'd have considered/expected the following:

(1): Experiment on different datasets, such as Phoenix-2014T, or the larger OpenASL and YoutubeASL, which have more state-of-the-art results, hence more data points to gauge the performance/benefits of the proposed approach.

(2): Frame the approach as a pretraining method, and do a final supervised finetuning step (with varying amounts of data). One would expect the unsupervised pretraining on unaligned data to yield better performance than straightforward supervised translation approach, which would have strengthened the utility of the proposed method.

(3) Having some qualitative results and failure analysis for translation/generation would have helped the paper immensely. Relying solely on b1 and b4 results does not give enough insights to the reader, and possibly is not doing the proposed approach justice.

As is, I do not think the reviewer/reader has enough signals to evaluate the benefits of the proposed approach, and I'd highly recommend the authors to consider the suggestions mentioned above.

### Questions
(See Weaknesses Section for Suggestions)

--------

After Rebuttal:
I'd like to thank the authors for the rebuttal, additional experiments and considering reviewer's suggestions. As can be seen in their latest experiments, there is benefit to be gained by utilizing the approach as a pretraining step. However, I still would have liked to have more signals from other benchmarks to give the reader better understanding of the proposed approach's performance. Overall I am leaning towards improving my rating to "5: marginally below the acceptance threshold".

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies a new setting for sign language understanding: unsupervised sign language translation and generation (USLNet), which exploits information from abundant single-modality but non-parallel data. More specifically, UNMT pretrains its text encodes/decoder and video/encoder decoder by reconstruction tasks. To address the misalignment issue between video and texts, the authors further propose a sliding window based aligner.

### Strengths
1. The idea is sound. Due to the data scarcity issue in the sign language understanding systems, it is important to explore non-parallel data.
2. The text-video-text and video-text-video back-translation strategies are novel in the sign language community.
3. Detailed ablation studies.

### Weaknesses
1. The major issue is the experimental setting.

1.1. Intuitively, leveraging abundant data should be helpful to the model performance. For example, in MMTLB (Chen et al., 2022), using a translation network pretrained on large natural language corpus can boost sign language translation performance. But I didn't see similar conclusions in the experiment section. In Table 1, the authors directly compare a supervised model with the proposed USLNet, and get a worse result on BLEU-4. I understand that the unsupervised performance must be worse, but what is this comparison for? I hope to see that for example, fine-tuning USLNet on parallel corpus can give better results, i.e., similar to the conclusion in MMTLB.

1.2. The performance is **too bad**. Although it may not be the authors' fault (maybe the dataset is too difficult), the poor performance make the comparison less convincing. Experiements on other widely-adopted benchmarks, e.g., Phoenix-2014T and CSL-Daily, shall be considered.

2. It seems that there is a factual error in the sliding window based aligner. The text and video are not monotonically aligned. In fact, only video and glosses are monotonically aligned, e.g., 1-10 frames for the first gloss, and 11-20 frames for the second gloss. Thus, it is questionable for the design of the sliding window-based aligner.

3. The descriptions for the process of the aligner should be more clear. The current form is a bit difficult to understand.

4. The process of two back-translation strategies are simialr to dual learning. The authors may consider adding a subsection in related works to discuss dual learning.

### Questions
See weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
