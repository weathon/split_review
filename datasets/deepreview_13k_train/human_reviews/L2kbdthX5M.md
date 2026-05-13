# SignAvatars: A Large-scale 3D Sign Language Holistic Motion Dataset and Benchmark

- Decision: Reject
- Scores: 6, 6, 5, 8

## Abstract
We present SignAvatars\footnote{\url{https://signavatars.io/}}, the first large-scale, multi-prompt 3D sign language (SL) motion dataset designed to bridge the communication gap for Deaf and hard-of-hearing individuals. 
While there has been an exponentially growing number of research regarding digital communication, the majority of existing communication technologies primarily cater to spoken or written languages, instead of SL, the essential communication method for Deaf and hard-of-hearing communities. 
Existing SL datasets, dictionaries, and sign language production (SLP) methods are typically limited to 2D as annotating 3D models and avatars for SL is usually an entirely manual and labor-intensive process conducted by SL experts, often resulting in unnatural avatars. 
In response to these challenges, we compile and curate the SignAvatars dataset, which comprises 70,000 videos from 153 signers, totaling 8.34 million frames, covering both isolated signs and continuous, co-articulated signs, with multiple prompts including HamNoSys, spoken language, and words.  
To yield 3D holistic annotations, including meshes and biomechanically-valid poses of body, hands, and face, as well as 2D and 3D keypoints, we introduce an automated annotation pipeline operating on our large corpus of SL videos.
SignAvatars facilitates various tasks such as 3D sign language recognition (SLR) and the novel 3D SL production (SLP) from diverse inputs like text scripts, individual words, and HamNoSys notation. 
Hence, to evaluate the potential of SignAvatars, we further propose a unified benchmark of 3D SL holistic motion production. We believe that this work is a significant step forward towards bringing the digital world to the Deaf and hard-of-hearing communities as well as people interacting with them.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a large-scale 3D sign language motion dataset. This dataset is organized with video-mesh-prompt. For accurate mesh annotation, it designs multiple loss terms and leverages 2D pose detectors to provide supervision signal. For prompt, it collects multiple types, i.e., HamNoSys, spoken language, and words. Besides, it also provides a baseline for sign language production.

### Strengths
- To my best knowledge, this paper proposes the largest SL motion dataset. It promotes the research in sign language production.
- The designed baseline is sound.
- The whole paper is well-organized and well-written.

### Weaknesses
 - One of the main concerns is the evaluation metrics. It is important to evaluate the semantics of the produced motion. Although the authors claim that the metric of back-translation is not generic for each text prompt, we can divide the dataset into multiple groups, i.e., word-level and sentence-level. Word-level and sentence-level videos should be divided, as they have different co-articulated characteristic.
- For the proposed baseline method, how does the semantics input act as a condition in the autoregressive Transformer? Specifically, is the semantic input directly concatenated to the input of the transformer, or is it used to modulate the attention mechanism, or is it used in another way? The paper should clarify this point.
- What is PLFG? I cannot find this module in Figure 4. The description of the architecture is not clear enough. It is important to clearly define each component and its role in the overall framework.
- The core design of the baseline is the utilization of VQ-VAE for both motion and semantics tokenization. Could the authors perform ablation on it? Specifically, what is the impact of the codebook size, the number of layers, and the quantization method on the final performance?
- Some typos, divrse in Page 4; the ASL data volume is not consistent in Table 2 and the text description (34K, 35K).
- Some other relevant works should be discussed in the part of 3D holistic mesh reconstruction (for SL), such as 
Hu H, Zhao W, Zhou W, et al. SignBERT+: Hand-model-aware Self-supervised Pre-training for Sign Language Understanding. IEEE TPAMI, 2023.

### Questions
Please refer to the weakness part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a large-scale multi-cue 3D sign language (SL) action dataset, aiming to build a communication bridge for hearing-impaired individuals.

### Strengths
- Well-written.
- A practical dataset is proposed.

### Weaknesses
 - Why did the author use the annotation method in Figure 3? Are there other labeling methods that can be compared?
- It is expected that the author can describe the specific structure of the "Autoregressive Transformer" in Figure 4.
- What is the specific meaning of "code index vector" in Figure 4? Please clarify.

### Questions
Please see "Weaknesses".

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors apply a parametric body model based 3D pose estimation framework to estimate signer poses from monocular videos. They apply their framework on publicly available SL datasets. The extracted poses are noted to be publicly available upon publication of the manuscript to set up a new benchmark for SLP. In addition to the avatar generation framework, the authors propose an VQ-VAE based SLP approach, which can be prompted by spoken language sentences, words, sign glosses or HamNoSys sequences. This approach is evaluated on the presented benchmark, and the presented qualitative results look promising.

### Strengths
- It's an interesting idea to have multi-source prompting as SLP input. 

- The qualitative samples the authors share seem to yield compelling SLP performance.

- Although VQ-VEAs have been explored for SLP (https://arxiv.org/abs/2208.09141), it has not been utilized in combination with multi-source prompting and 3D mesh generation to the best of my knowledge. Hence, this approach and the results might be useful to the other researchers.

### Weaknesses
General:
- Supplementary video could have been better. There is no narration in the video. Failure analysis and having SLP with different prompts that are corresponding to the same meaning would have strengthened the submission.

- Overall the presentation quality of the paper can improve significantly. As is it does not meet the expectation of being publication ready (See Questions).

About Dataset:
- This manuscript is framed as a dataset paper, however there is no new data that is collected or will be released. What the paper actually presents is derivative data, i.e. 3D pose estimates from existing datasets, which is disappointing as a reader who was hoping to find a new,  potentially useful data source.

- Although the authors present this dataset as "large scale", it still lacks the scale to be considered as one. 70,000 videos is hardly large scale, even considering the contemporary SL alternatives, such as BOBSL or Youtube-ASL.

About Pose Estimation Framework:
- Given one of the main proposed contributions of this paper is the pose estimation framework, I would have expected more qualitative and quantitative results against the state-of-the-art approaches from the model based pose estimation domain. If this is just an application of previously existing approaches, such as (Spurr et al., 2020), then this needs to be clearly stated.

About VQ-VAE SLP-based Approach:
- The proposed VQ-VAE based SLP approach is only evaluated on the presented benchmark dataset, which does not give the reader any anchor points to compare against the state-of-the-art on other benchmarks. Also the authors compare their approach only against the Ham2Pose-3D approach on the new benchmark.

### Questions
- "We compile SignAvatars by synergizing various data sources from public datasets to online videos and form seven
subsets, whose distribution is reported in Fig. 2". - As it was used multiple times in the manuscript, what does "synergizing" mean in the context of this paper? 

- Figure 2 is not clear. What is "word", which is the "ASL" dataset? It would have been better to have a clear introduction of the terminology and the source dataset that are utilized just after or before Figure 2. 

- "Moreover, there are over 300 different sign languages across the world, with hearing-impaired people who do not know any SL." Can the authors elaborate what they mean here?

- "Our SL annotations can be categorized into four common types: HamNoSys, spoken language, word, and gloss, which can be used for a variety of downstream applications such as SLP and SLR". What is the difference between word and gloss in this context? 

- "Overall, we provide 117 hours of 70K video clips with 8.34M frames of motion data with accurate expressive holistic 3D mesh as motion annotations" - Will the authors provide the original video clips? Did you ask the original authors permission? As you shared in your appendix not all the datasets have "Share alike" permission in their licenses. 

- "To demonstrate our dedication, we have submitted all source code as part of the appendix." - I was unable to find the source code either in the appendix or the supplementary material.

- "RELATED WORK (REUSING THE PREVIOUS ANSWERS...)"- What do the authors mean by "Reusing the previous answers"?

----------------------
**After Rebuttal Comments:**

Authors provided a great rebuttal and updated their website, which addressed most of my concerns, and I thank them for that.

I am still adamant about my standing of this not being a dataset paper, as I categorically do not consider automatic pose estimations as annotations.

There is a lot in this paper, and I do think it will be useful to the field, but as is, it is spread thin over many components of a sign language production pipeline. As I mentioned in my initial review, if the novelty comes from the pose estimations, then we need more experiments and comparisons against other pose estimation methods. If the novelty is the SLP network, then we need more comparisons against sota and a user study to understand its performance. Thankfully, the authors provided additional experiments in the discussion period, so some of these concerns are partially addressed.

Given all these, I am learning towards improving my recommendation to a borderline rating, and I do not feel strongly for either acceptance or rejection of this manuscript.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper looks at the problems of Sign Language (SL) production and translation. They introduce a significant new dataset of annotated sign language data. While many of the videos used are curated from other datasets (e.g., How2Sign), a core contribution is their optimized 3D body (SMPL-X) and hand (MANO) representations for each frame in these datasets. Sign Language transcription forms can vary (e.g., text/gloss/HamNoSys), so one benefit of this work is the inclusion of multiple forms and across languages (English, German SL, French SL, Polish SL, Greek SL). The authors also introduce benchmarks and metrics to facilitate future modeling work. 

On top of this, the authors describe development of an SL production baseline based on VQ-VAE models which shows promise. The videos are compelling and the results are significantly better than Ham2Pose on various metrics.

### Strengths
This is an exceptional paper that will be important for the sign language modeling community from dataset, benchmarking, and modeling perspectives.  

Some things that I found are really well done / investigated. 
* The human pose representations build on SOTA avatar representations (SMPL+X, MANO) as opposed to the more common keypoint-based solutions. 
* For computing human pose annotations, the authors do an especially nice job with novel system engineering and iteration to compute the highest quality annotations. For example, adding biomechanics constraints on top of the SMPL and MANO computations. 
* The use of multiple SL annotation types (HymNoSys, text, gloss) makes this work useful for working on SL modeling from multiple perspectives. 
* The SL production work is a really nice advanced development of discrete variable model approaches for complex motion synthesis. 
* Related work is well represented and contextualized (although some additional work from the HCI and Accessibility communities could be added)
* The paper is well written and generally easy to follow (but may be hard to reproduce given the complexities of each model involved).

### Weaknesses
 * The number of metrics is a little overwhelming. Some of them seem very useful but others may dilute the findings? For example, I'm not convinced that metrics like FID are useful here. Can the authors demonstrate that improved results on each metric do correlate with a model's ability to generate correct/accurate signs?

### Questions
Perhaps I missed it, but how important are the biomechanics constraints or other regularizations on the annotation quality? Are there metrics for this or is it mostly perceptual.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
