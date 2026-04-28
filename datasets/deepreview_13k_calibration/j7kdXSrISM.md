# OpenVid-1M: A Large-Scale High-Quality Dataset for Text-to-video Generation

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
\vspace{-2.5mm}
Text-to-video (T2V) generation has recently garnered significant attention thanks to the large multi-modality model Sora. However, T2V generation still faces two important challenges: 
1) Lacking a precise open sourced high-quality dataset. 
The previous popular video datasets, \eg WebVid-10M and Panda-70M, are either with low quality or too large for most research institutions.
Therefore, it is challenging but crucial to collect a precise high-quality text-video pairs for T2V generation. 
2) {Ignoring to fully utilize textual information}. 
Recent T2V methods have focused on vision transformers, using a simple cross attention module for video generation, which falls short of thoroughly extracting semantic information from text prompt. 
To address these issues, we introduce~\datasetname, a precise high-quality dataset with expressive captions. 
This open-scenario dataset contains over 1 million text-video pairs, facilitating research on T2V generation. 
Furthermore, we curate 433K 1080p videos from~\datasetname~to create~\hddatasetname, advancing high-definition video generation.
Additionally, we propose a novel Multi-modal Video Diffusion Transformer (MVDiT) capable of {mining both structure information from visual tokens and semantic information from text tokens}. 
Extensive experiments and ablation studies verify the superiority of~\datasetname~over previous datasets and the effectiveness of our MVDiT.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a high-quality large-scale T2V dataset namely OpenVid-1M, as well as a new T2V model architecture – the MVDIT. 

As main contribution, OpenVid-1M is born out of several open sourced dataset such as Panda, CelebvHQ, etc. and filtered with carefully designed pipeline followed by recaption. 

As secondary contribution, the proposed MVDIT can be considered as a straight extension of MMDIT, where video and text token are jointly feed to 3 successive attention modules. The author(s) claim such design can mine structure information from visual feature and semantic information form text feature, and verify it through experiments.

### Strengths
1. Meticulously designed data process pipeline, which producing relatively higher quality comparing to previous datasets. There is no doubt that a publicly available million level dataset with high quality is critical for video generation task.


2. The architecture designing of MVDIT is reasonable. Text tokens are repeated by T times to fitting the frames, which makes it natural to equally treat visual and semantic information in the self-attention and temporal-attention modules. 


3. Superior generation results among popular open sourced T2V systems. BTW, is it possible to make the trained model released?

### Weaknesses
1.	As a dataset paper. The proposed OpenVid-1M is somewhat weak. First, it is in fact a downstream collection of several publicly available datasets, which doesn’t provide extra videos. (Are you considering collecting new video data?)  Second，in contrast with carefully designed filtering operations, it is too crude to directly use raw LLAVA model as captioner without any comparison, since video caption is extremely important for T2V task. It is suggested to try sophisticated commercial LMMs such as GPT 4V and Gemini, or to finetune task aware open source models.

2.	The introduced MVDIT is greatly inspired by MMDIT. It can be seen as a naturally extension to T2V task of MMDIT, which largely limit its technic novelty. It is notable in Figure 4 that this work adds Temporal-Attention and Cross-Attention layers besides Self-Attention in MMDIT,  so can you take an empirical ablation study to verify their effectiveness?

### Questions
1.	In Figure 3 Right, it is noticed that 37% clips are less than 3s. Considering mainstream T2V  systems are more than 5s, is it valuable to keep such short clips? Can you perform an ablation study showing the impact of filtering out clips shorter than 5 seconds on model performance?
2.	Is the Self-Attention Module along spatial and within the same frame? I guess so. Please make it clearer. Furthermore, have you tried full 3D attention( Open Sora Plan v1.2) with self attention module?
3.	In table 3, there are some competitive models appearing before submission DDL of ICLR, such as CogvideoX-5B and OpenSoraPlanV1.2. Can you add them in the SOTA list?
4.	In table 4, to compare model trained by OpenVidHD with the one 4x by Panda 50M is not fair. Is it possible to select 1020P from Panda 50M to form Panda 50MHD for fair comparison?

### Soundness
3

### Presentation
2

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
This paper introduce OpenVid-1M dataset, a new precise high-quality datasets for T2V generation. This dataset consists of about 1M videos, all with resolutions of at least 512x512, accompanied by detailed and long captions, facilitating the creation of visually compelling videos. An automated filtering and annotation pipeline is proposed to ensure high-quality of the dataset. Additionally, a new Multi-modal Video Diffusion Transformer (MVDiT) method is proposed to incorporate multi-modal information for better visual quality. Extensive experimental results verify the effectiveness of the proposed dataset and method.

### Strengths
1.	A dataset is proposed, comprising over 1 million high-resolution video clips paired with expressive language descriptions, this dataset aims to facilitate the creation of visually compelling videos. 
2.	An automated filtering and annotation pipeline is proposed to ensure the quality of videos. 
3.	Extensive experimental results verify the effectiveness of the proposed method.

### Weaknesses
1.	The proposed automatic data cleaning pipeline seems to be a pipeline that many previous methods have commonly used in SD-3 and SVD, lacking a certain novelty.
2.	Lack of ablation study for the proposed method, such as the effectiveness of scaling parameter α and Multi-Modal Temporal-Attention Module.
3.	The video shown in Figure 6 and Figure 8 takes up very little space, making it difficult to see the details clearly. Increasing the size of the video frames or providing higher resolution versions in an appendix would be helpful.
4.	The section on Acceleration for HD Video Generation seems redundant and is not the method proposed in this work. It can be placed in the appendix, leaving room for more qualitative text-to-video results.

### Questions
Refer to Weaknesses for more details.

### Soundness
3

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
This paper proposes a large-scale high-quality dataset for text-to-video generation, named OpenVid-1M. Compared to existing related datasets, OpenVid-1M has the edge in high-quality videos and expressive captions. OpenVid-1M is curated from ChronoMagic, CelebvHQ, Open-Sora-plan and Panda by controlling aesthetic score, temporal consistency, motion difference, clarity assessment, clip extraction and video caption. Besides, the authors follow MMDiT and design a Multi-modal Video Diffusion Transformer (MVDiT) architecture for text-to-video generation.

### Strengths
1. The authors descrive the advantages of the proposed dataset clearly.
2. There are sufficient experiments to evaluate the dataset and model.

### Weaknesses
1. Since the proposed MVDiT follows MMDiT, the authors should compare the differences between the two in detail through text descriptions or figures. For example, what modules does MVDiT retain, remove, or add from MMDiT? How do these changes more effectively cope with video data?
2. As a work on text-to-video generation, there is no project or demo webpage to showcase the dataset or model performance. It is difficult to judge the overall quality of the video from a few frames captured from the video, so I would like to know if the author has plans to make the demo website public.
3. It would be better to compare the video duration distribution between OpenVid-1M and other datasets in the form of Figure 3 Right, since the video duration can influence the quality of video generation.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses two key issues in the text-to-video field: the lack of high-quality datasets and poor textual representations, proposing the 1M high-quality dataset OpenVid-1M. MVDiT is introduced to validate the effectiveness of the dataset.

### Strengths
1. The paper resolves the critical issue of the lack of high-quality datasets in the text-to-video field, significantly impacting the fine-tuning and training of pre-trained text-to-video models, especially smaller models.

2. The article presents two datasets of different scales: 1M and 0.4M, with the 1M dataset having a resolution greater than 512.

3. The dataset’s text is highly detailed, making it suitable for future transformer or DiT-based video training models that require long text inputs.

4. The article selects high-quality data from multiple datasets and various models, demonstrating significant effort.

5. Experiments training the same model on different datasets indicate that this dataset is indeed of high quality and can enhance the model's output performance.

6. The article has a clear motivation, with writing that is clear and easy to understand.

### Weaknesses
I tend to rate the paper between 6 to 8 points, but I'm currently giving it a score of 6. Despite its rich experiments and significant contributions, there are still the following issues:

1. For the ICLR conference, this paper lacks explanatory work, such as a clear justification for each step of the dataset filtering process. Specifically, it does not adequately explain why certain models were chosen or the rationale behind the selected filtering ratios.

2. OpenVid-1M only filters and integrates existing datasets and does not include any new high-quality videos. Models trained on this dataset do not learn new knowledge.

3. Using LLaVA to generate captions for videos merely indicates that the captions are longer and does not guarantee improved accuracy or richness of the descriptions compared to the originals. Models trained with such captions primarily transfer some knowledge from LLaVA rather than gaining new knowledge to achieve performance breakthroughs.

### Questions
1. Why choose the top 20% of Panda-50M while selecting the top 90% from other datasets?

2. How is optical flow used to filter videos? Why is temporal consistency used to discard the highest and lowest, while optical flow is not?

3. In Table 3, is the comparison across different resolutions fair? Could super-resolution impact the quality of the original videos?

4. Is the dataset publicly available?

### Soundness
3

### Presentation
3

### Contribution
4
