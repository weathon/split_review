# ILLUSION: Unveiling Truth with a Comprehensive Multi-Modal, Multi-Lingual Deepfake Dataset

- Decision: Accept
- Scores: 6, 6, 8, 5, 5

## Abstract
The proliferation of deepfakes and AI-generated content has led to a significant increase in media forgeries and misinformation, necessitating development of more robust detection systems. Current datasets, however, lack comprehensive diversity across modalities, languages, and real-world scenarios. To address this gap, we present ILLUSION (Integration of Life-Like Unique Synthetic Identities and Objects from Neural Networks), a large-scale multi-modal deepfake dataset comprising over 1.3 million samples. ILLUSION encompasses (i) audio-visual forgeries, (ii) diverse linguistic content with over 26 languages, (iii) challenging noisy environments, and (iv) various manipulation protocols. Generated using state-of-the-art generative models, ILLUSION includes face swaps, audio spoofing, synchronized audio-video manipulations, and synthetic images, faces, and videos. The proposed dataset has balanced representation of gender and skin tone, supports multilingual experiments, and is designed to facilitate development of robust multi-modal detection systems. We benchmarked state-of-the-art algorithms across multiple modalities including image-based, audio-based, video-based, and multi-modal detection. The results highlight critical challenges such as (a) performance degradation in multi-lingual and multi-modal contexts, (b) accuracy reduction in noisy environments, and (c) limited generalization to real-world scenarios and zero-day attacks. It is our assertion that the comprehensive nature of the proposed dataset enables researchers to develop and evaluate more resilient deepfake detection methods, addressing the evolving landscape of synthetic media threats.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Glad to review the work.

This work proposes a large-scale multi-modal deepfake dataset that encompasses samples from multiple aspects. 

In general, I consider the constructed dataset could be helpful to related researchers.

### Strengths
In addition to constructing a large dataset, the authors evaluate many deepfake detectors from five aspects, summarize their findings, and discuss potential implications, the design of the work is complete.

The constructed dataset is comprehensive, covering different modalities, languages, and generation approaches.

### Weaknesses
Some of my concerns are listed as follows.

(1) Regarding the dataset, although it is generated using different aspects of algorithms, I doubt whether the samples in each set are with certain relationship (rather than randomly combining data), e.g., the voices generated using different algorithms are from the same source "voice" or "text", e.g.,  the pipeline in Set A are from the same "source" in the beginning of Figure 3 (similar in other sets).
In this case, it will be useful to evaluate and compare the performance of deepfake detectors.

(2) Regarding baseline detectors, although it mentions they are state-of-the-art, more categories or reviews on them are necessary to support why they are selected, whether they are type-complete or typical. The selection of baseline detectors may result in different findings or implications.

(3) Finally, I believe the work could provide potential reference to related researchers, however, I doubt whether the contribution of this work is enough for ICLR.
Although this work proposes a large dataset and conducts multiple evaluations, I am afraid it lacks some technical contributions, e.g., new generation approaches, or the dataset could help to improve deepfake detectors. 
On the other hand, the empirical evaluations could also be explored through other datasets.

### Questions
My main concerns are listed in the weakness part, where the weaknesses (1) and (2) are expected to be responded.

I will consider changing my score based on responses and other reviews.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper adopts various forgery generation algorithms to create a large-scale dataset containing four subsets, and raises five questions from three aspects: multimodal identity exchange, detection system generalization and detection of forgery or generation methods, and conducts related experiments.

### Strengths
The authors propose a large-scale forgery dataset, which includes a variety of face-changing forgery, generation methods and speech forgery methods, and includes languages of many countries, which has certain originality.

### Weaknesses
The problems studied in this paper are the focus of current research, not the author's new definition. The object of this paper is to put forward a large-scale and organized data set to explore the problem and support relevant research, which I think has certain value. However, it seems that the existing data sets can also be used to explore the five questions raised, and the author only gave the relevant experiments on four questions, the exploration and analysis of the experimental results are not deep enough, and the proposal of innovative solutions is not innovative enough for a top conference, and there is still room for further improvement in the writing logic of this paper.

In the data set of video generation, image generation, audio generation did not separate the clear description, the combination of a very poor look, video 100,000 magnitude, image million magnitude, in the scale is not small, only the million magnitude is not rigorous, there is still room for improvement in the logic of the discussion. In addition, the problems discussed in this paper can also be realized by using existing data sets, so I think the innovation of this paper is not enough, although this data set has certain value.
It is suggested that the results of the experiment should be further explored and analyzed, and it would be better to put forward some innovative solutions.

### Questions
In the data set of video generation, image generation, audio generation did not separate the clear description, the combination of a very poor look, video 100,000 magnitude, image million magnitude, in the scale is not small, only the million magnitude is not rigorous, there is still room for improvement in the logic of the discussion. In addition, the problems discussed in this paper can also be realized by using existing data sets, so I think the innovation of this paper is not enough, although this data set has certain value.
It is suggested that the results of the experiment should be further explored and analyzed, and it would be better to put forward some innovative solutions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces ILLUSION, a comprehensive multi-modal and multi-lingual deepfake dataset containing over 1.3 million samples. The dataset uniquely combines identity manipulations, synthetic content across multiple modalities (image, audio, video), and real-world test samples spanning 26 languages, generated using 28 different generation techniques. Through extensive benchmarking experiments with state-of-the-art detection methods, the authors demonstrate critical challenges in deepfake detection, including poor generalization to unseen generation methods, performance degradation in multi-lingual contexts, and limited effectiveness on real-world samples. The work provides valuable insights into the current limitations of deepfake detection systems and establishes a foundation for developing more robust detection approaches.
The main contributions include: (1) the first large-scale dataset combining multi-modal and multi-lingual deepfakes, (2) balanced representation across demographic attributes, and (3) comprehensive evaluation across various challenging scenarios revealing current detection limitations.

### Strengths
1. The paper presents a new dataset with impressive scale, content diversity, and multi-modal richness, demonstrating substantial effort in data collection and curation.

2. The incorporation of multi-lingual samples fills a significant research gap in the field of deepfake detection.

3. The authors propose a diverse evaluation strategy with four different protocols, including the consideration of real-world applications like Midjourney, which enhances the practical value of their work.

### Weaknesses
1. The performance evaluation is somewhat limited with only four detection methods. While this isn't the paper's main contribution, including more methods would provide a more comprehensive assessment of the dataset's quality. The authors should consider adding classical general face forgery detection methods (like LTW[1], DCL[2], SBI[3], SLADD[4] e.t.c.), AIGC detection methods for Set B (like NPR[5]), and standard baselines (EfficientNet-b4[6] and VIT series).

[1]. Domain general face forgery detection by learning to weight

[2]. Dual contrastive learning for general face forgery detection

[3]. Detecting Deepfakes with Self-Blended Images

[4].Self-supervised Learning of Adversarial Example: Towards Good Generalizations for Deepfake Detection

[5].Rethinking the Up-Sampling Operations in CNN-based Generative Network for Generalizable Deepfake Detection

[6]. Rethinking Model Scaling for Convolutional Neural Networks

2. The authors should provide a deeper analysis of Table 4's results, particularly explaining the substantial performance variations between different methods on Set B and Set C.

3. The audio forgery aspect presents an interesting dimension that deserves more thorough analysis, specifically examining how different types of audio manipulation affect overall deepfake detection performance.

4. The robustness evaluation could be more comprehensive. While c23 and c40 compressions are considered, additional real-world noise simulations like JPEG compression and resolution variations would better assess the dataset's practical utility.

5. The quality assessment is primarily statistical, lacking detailed analysis through visualizations of different methods' outputs or quality evaluations for each category.

### Questions
1. What is the purpose of including "This Person Does Not Exist" samples in Set B? The relationship between these synthetic faces and the natural images in Set B needs clarification.

2. The authors should explain the unusually high accuracy of MesoInceptionNet on Set C while other methods perform poorly (Table 4). This significant performance disparity requires investigation and explanation.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This manuscript presents ILLUSION, which is a large-scale multi-modal deepfake dataset. The author(s) believe(s) the comprehensive nature of the proposed dataset enables researchers to develop and evaluate more resilient deepfake detection methods, addressing the evolving landscape of synthetic media threats.

As the current popularity of generative artificial intelligence, it is inevitable to propose a complete data set, especially considering multimodal data. However, for the forgery identification algorithm, whether the generalization ability is achieved is an important indicator to solve today's identity forgery. Many forgery identification algorithms are based on deep learning, which generalizes the concept of differentiation from real images by extracting depth or potential features. This has to mention the importance of data sets. Based on my experience, the following advantages, disadvantages and questions I hope the author can reply to are summarized for this manuscript.

### Strengths
- The author aims at the current hot issues of generative AI, and the contribution of this manuscript is expected to be called solving the ethical problems of generative AI.

- This paper collates the information of the current dataset and embodies the advantages of ILLUSION.

- Many datasets tend to pursue a huge number. The datasets proposed in this paper enrich the current research from the perspective of multimodality.

### Weaknesses
Some major comments:

- As other methods of generalized image forgery, such as digital watermarking, PS, image optimization, etc. Whether the author considers to include it in the falsification data set, or how the author thinks about the falsification hazards brought by this kind of data.

- The author provides a large-scale data set, which is essential in today's research direction focusing on large models. However, does the author consider that the larger the data size, the better? Some studies have shown that data validity (such as reducing samples with similar features, reducing samples with overlapping features, etc.) often takes precedence over data size. The author also mentioned the disadvantages brought by the large data scale in the BROADER impact. The author is requested to analyze from the perspective of data validity whether the gain brought by this dataset on the large model can make up for the defects brought by invalid data.

Some other minor comments:

- The font of Figure 1 and Figure 2 is too small, please adjust according to the requirements.

- The author used a large number of face images in the dataset. Are these images exempted?

### Questions
- The author(s) take(s) into account the multi generative model to enrich the diversity of forged data. Generative models often have digital fingerprints [1]. How do(es) the author(s) consider the differences between the data set proposed in this paper and the existing data set at the level of digital fingerprints?

- According to Q1, the author is requested to provide the degree of overlap between the digital fingerprints of the data set proposed in this paper and the existing data set, and to elaborate the advantages and disadvantages.

- In order to verify the validity of the proposed dataset, the authors used the detection model such as SSLModel for verification (Table 7). As we all know, deep learning models have data specificity. Whether these models have some improvement in generalization. If not, this part of the experiment is not very convincing.

- The data set formed in this paper is based on the training of generated samples. However, whether these fake samples can represent forgery in the real world. I mean, when the detection model trained based on this dataset encounters real-world samples, does it recognize forged features or synthetic data?

**Refs:**

    [1] Yu, N., Skripniuk, V., Abdelnabi, S., & Fritz, M. (2021). Artificial fingerprinting for generative models: Rooting deepfake attribution in training data. In Proceedings of the IEEE/CVF International conference on computer vision (pp. 14448-14457).

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this paper, the authors introduce a large-scale, comprehensive deepfake dataset containing nearly 30 different forgery methods, divided into four subsets. The dataset includes multi-modal and multi-lingual fake videos, with a balanced distribution across gender and age groups. The authors also conducted exploratory benchmarking on their dataset and highlighted the challenges that existing detectors face when identifying deepfakes in real-world scenarios.

### Strengths
- A large-scale dataset containing various forgery methods is proposed.

- A benchmark for the proposed dataset is constructed.

### Weaknesses
 - Uniqueness of the dataset. As a large-scale multimodal dataset, ILLUSION does not exhibit particularly distinctive features. Previous datasets, such as ForgeryNet [A] and KoDF [B], have already focused on large-scale video and image forgeries. Additionally, many recent datasets have been proposed for the detection of AIGC content [C][D][E][F][G]. While the integration of various forgery methods is certainly commendable and meaningful, further discussion is needed on how this integration can contribute to advancing research.

- The comparison with related datasets is insufficient. The authors should enhance Figure 1 by including, but not limited to, datasets in [A]-[G].

- The authors are advised to include more state-of-the-art deepfake detectors to create a more comprehensive benchmark.

Regarding multi-modal forgery, datasets such as AV-Deepfake1M have already addressed audio-video forgeries, which might be a particular aspect that this dataset needs to carefully consider.

The reviewer appreciates the “continuity” of the website constructed by the authors, but this aspect is not reflected in the main manuscript.

### Questions
Please see Weaknesses

### Soundness
2

### Presentation
3

### Contribution
2
