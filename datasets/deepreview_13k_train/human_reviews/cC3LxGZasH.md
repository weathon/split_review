# Beyond FVD: Enhanced Evaluation Metrics for Video Generation Quality

- Decision: Accept
- Scores: 3, 8, 6, 8, 6

## Abstract
The Fr\'echet Video Distance (FVD) is a widely adopted metric for evaluating video generation distribution quality. However, its effectiveness relies on critical assumptions. Our analysis reveals three significant limitations: (1) the non-Gaussianity of the Inflated 3D Convnet (I3D) feature space; (2) the insensitivity of I3D features to temporal distortions; (3) the impractical sample sizes required for reliable estimation. These findings undermine FVD's reliability and show that FVD falls short as a standalone metric for video generation evaluation. After extensive analysis of a wide range of metrics and backbone architectures, we propose \textbf{JEDi}, the \textbf{J}EPA \textbf{E}mbedding \textbf{Di}stance, 
based on features derived from a Joint Embedding Predictive Architecture, measured using Maximum Mean Discrepancy with polynomial kernel.  Our experiments on multiple open-source datasets show clear evidence that it is a superior alternative to the widely used FVD metric, requiring only 16\% of the samples to reach its steady value, while increasing alignment with human evaluation by 34\%, on average.\footnote{\textbf{Project page:} \url{https://oooolga.io/JEDi.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the issues present in currently popular evaluation metrics in the field of video generation by proposing a new evaluation metric. It points out the assumptions underlying existing evaluation methods and the problems associated with these assumptions. The newly proposed metric shows better performance in terms of cosine similarity with human evaluations and demonstrates significant improvement in the number of samples needed to converge.

### Strengths
The paper comprehensively considers the strengths and limitations of existing metrics and systematically reviews the assumptions underlying these metrics, along with the problems associated with these assumptions. It delves into the accuracy of The Fréchet distance (FD) and its consequences when these assumptions do not hold. Building on this foundation, the paper addresses some of the issues present in current evaluation strategies. The new evaluation strategy proposed shows a significant improvement in consistency with Cosine Similarity with Human Evaluation.

### Weaknesses
The paper emphasizes that JEDi, as a video generation evaluation metric, has an advantage in the number of samples required for convergence, achieving faster convergence. However, the number of samples required for convergence should not be considered the primary concern of an evaluation strategy, as not all datasets face the issue of insufficient samples affecting precision; there are still many datasets that meet the necessary conditions. While JEDi performs well in consistency with human evaluations, further experimental validation is needed to assess its performance in other aspects as an evaluation metric.
Although the author said in the experiment that the resolution can be arbitrary, since this work relies on the representation capability of SreamDiffusion[3] based on SD-Turbo or LCM, many "high-resolution" images are not included in the training set of SD-Turbo or LCM. Can Promptus effectively transmit videos with various resolutions and high resolutions that it has not seen during SD training?

### Questions
Please refer to the Weakness section. 
Additionally, the paper provides limited explanation of the proposed evaluation metric, JEDi. It might be beneficial to reduce the amount of reiteration about other evaluation metrics and instead increase the logical exposition of JEDi to provide a more comprehensive understanding of its strengths and limitations.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper reveals that FVD falls short as a standalone metric for video generation evaluation, then analyzes a wide range of metrics and backbone architectures, and proposes JEDi, the JEPA Embedding Distance, based on features derived from a Joint Embedding Predictive Architecture, measured using Maximum Mean Discrepancy with polynomial kernel.

### Strengths
The proposed JEDi eliminates the need for parametric assumptions about the underlying video distribution, unlike FVD which relies on the Gaussianity assumption to make its metric feasible.
JEDi significantly reduces the number of samples needed to make an accurate estimate.
JEDi has better alignment with human evaluations compared to FVD.

### Weaknesses
1.	The tile of the paper is relatively too broad, as video generation quality as well as its evaluation cover many aspects, however JEDi can only cover an aspect of quality.
2.	The proposed JEDi is a distribution-based evaluation metric, which can not work for a single case, for example to evaluate the quality of a single generated video.
3.	The single video AIGC video quality assessment should also be discussed and compared, including the state-of-the-arts and its differences and similarities with the distribution metrics.
4.	The authors conduct a subjective evaluation which is a very small scale study. More evaluations on existing large-scale AIGC video quality databases should be conducted.
5.	More comparisons with the single AIGC video quality assessment metrics are suggested to be included.

### Questions
Following the above weaknesses, some questions are suggested to be answered.
1.	As we known, video generation quality covers many aspects, thus the authors are suggested to specify which aspect of quality this paper focuses on.
2.	The possibility of applications on single video quality evaluation should be discussed.
3.	The are many studies for single generated image or video quality assessment studies in the image/video quality assessment communities.
4.	In some open AIGC video quality assessment databases, both generated videos and human labels are given, for example the Text-to-Video Quality Assessment DataBase (T2VQA-DB), Large-scale Generated Vdeo Quality assessment (LGVQ) dataset, Generic AI-generated Action (GAIA) dataset. The alignment with human ratings on these databases are suggested to be tested.
5.	Following the above comment, the performance comparisons with these AIGC video quality models are suggested to be given.

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
3

### Summary
This work analyzes the limitations of FVD and proposes the JEPA Embedding Distance based on features derived from a Joint Embedding Predictive Architecture. The authors commit to develop effective, robust metrics with small sampling size for guiding the current surge in video generation research. The experiments on open-source datasets show that compared to the widely used FVD metric, the proposed method requiring only 16% of the samples to reach its steady value, while increasing alignment with human evaluation by 34%, on average.

### Strengths
1. The authors note three key hurdles in video generation: (1) Data size, (2) Computational resources, and (3) Metric convergence speed, and commence by developing metrics with higher sample efficiency with fast convergence.
2. The authors investigate the correlation between metric with distortion level and training duration and gain valuable observations to further improve the FVD metric.

### Weaknesses
1. The content arrangement is not sufficiently appropriate. For example, Section 2.1 and 2.2 introduce a lot of consensus information about Inflated 3D ConvNet, video masked autoencoder, and the definition of Fr ́echet Distance, which should be moved to Appendix. In contrast, more related work about the evaluation metrics for video generation should be reviewed [1, 2]. 
2. The organization of Section 1 should be improved to enhance its readability. Line53: a video generation model …… produce ….. with diverse features? The two examples in Line53-57 are limited in scenarios. Line 59 - 60 only mentioned some full-reference video quality metrics,  however, lack of the introduction of no-reference video quality assessment (VQA) metrics ([1, 2]), which are more practical in real-world applications.
3. Fig. 3 is difficult to interpret without zooming in. Improving the resolution, providing clearer annotations or changing the scale could make the results more convincing.
4. What is the meaning of the items in red font in Table 1? Lack of explanation. And what is the meaning of blur (low, mid, high)? Are they mean the distortion Level? These should be noted in the Table caption.
5. The experiment is not comprehensive enough. Only two I2V models and three noise distortion types are included. I recommend that the authors add more image-to-video models for evaluation, both proprietary and open source, to support your findings. Since there are low-level distortion (blur, noise, artifacts) and high-level distortion (semantic, composition) in generated videos, it is necessary to evaluate the proposed JEDi in these scenarios.
6. The details of human evaluation in Section5.4 are vague. Since the normativity of the subjective study largely affect the reliability of these results. The content in App. E.3 is empty.
7. Line378: I3D and VideoMAEPT are not ideal feature spaces for building video quality metrics, as they do not capture blur distortion well. How about other distortions?
8. The equations in App. B should be better arranged to increase their readability.

### Questions
see weaknesses.

### Soundness
2

### Presentation
2

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
This paper provides critical analysis about FVD, which is the commonly used quality evaluation metric for generated videos. Three major limitations of FVD are discussed: 1) over-reliance on Gaussianity assumptions, 2) high-dimensional feature spaces, and 3) low sample efficiency. Furthermore, this paper proposes a new metric named JEDi, which computes Maximum Mean Discrepancy (MMD) in a V-JEPA feature space. Extensive experiments are conducted and the results demonstrate its robustness and effectiveness in terms of distortion-sensitivity, high sample efficiency, and high correlation with human ratings.

### Strengths
1.	The limitations of FVD are systematically identified and analyzed, especially regarding the non-Gaussianity of the I3D feature space and the low sample efficiency. 
2.	Findings and insights derived from comprehensive comparison experiments are interesting and convincing, such as the importance comparison of feature space and distance metrics, and the distortion-aware feature space selection.
3.	A well-justified metric name JEDi is proposed that addresses the main issues in FVD. The methodology is clearly explained, and the effectiveness of JEDi is well verified through extensive experiments.

### Weaknesses
1. Due to the limitations of the small-scale human evaluation, it would be better to evaluate the quality evaluation performance on large-scale video quality assessment datasets of generated content. In the human evaluation, only comparison ratings as the human preference are provided, lacking the overall quality ratings which can be obtained by single stimulus. Since JEDi is targeting quality evaluation for generated videos where the quality is practically measured without reference, i.e., no-reference quality assessment, it would be more comprehensive to evaluate JEDi on large-scale open-source video quality databases of AI-generated content, such as T2VQA-DB and GAIA.  
2. Lacking of reviewing and analyzing relevant literatures. Similar to FID ant its variants, NIQE evaluates the quality by measuring distribution distance in the feature space. Targeting measure quality of non-generated images, NIQE extracts neurostatistical features, fit the features with Multivariate Gaussian Model, and compute distribution distance by Mahalanobis Distance. It would be very insightful to include the Mahalanobis Distance into the discussion of the effective distance metrics, and to analyze the difference of algorithm design among FID/FVD, NIQE, and JEDi. Quantitive experiments are expected to provide holistic analysis.

### Questions
Can the monotonicity with training iterations in Fig. 5 imply the accuracy as well? Fig.5 only demonstrate the better monotonicity of JEDi during training over that of FVD and other metrics, yet it can not tell the superiority of quality evaluation accuracy of JEDi. Refer to the commonly used index, SROCC, PLCC, and RMSE, for measuring the performance of quality assessment metrics.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper makes a strong empirical case for the JEDi metric, which is based on features derived from a Joint Embedding Predictive Architecture, measured using Maximum Mean Discrepancy with polynomial kernel, as a superior alternative to FVD in evaluating video generation models.

### Strengths
1. Interesting metric. The paper introduces the JEDi , a new metric for evaluating video generation quality, addressing several limitations of the existing FVD. JEDi is shown to improve alignment with human evaluations by 34%, which is a significant improvement.

2. Clear Identification of FVD’s Limitations. The authors thoroughly analyze the shortcomings of FVD, including:
    a.Non-Gaussianity in feature space.
    b. Insensitivity to temporal distortions.
    c.The impractically large sample sizes required for reliable metric estimation.

These are important challenges in the field of video generation, and addressing them demonstrates the paper's relevance.

3. Good Efficiency. One of the key claims is that JEDi requires only 16% of the samples compared to FVD to reach its steady value, which could make it a more practical metric for real-world applications.

### Weaknesses
First I want to declare that I am not very familiar with this area and I am going to summarize some weaknesses that matter to me.
1. Missing Analysis on Long-Term Temporal Distortions. Although the paper mentions the insensitivity of FVD to temporal distortions, the experiments primarily focus on shorter-term consistency and aesthetics. It would be beneficial to see deeper analysis on how JEDi handles long-term temporal coherence in video. Specifically, the paper lacks experiments that explicitly evaluate the metric's sensitivity to long-range dependencies and temporal drifts that might occur over longer video sequences. For instance, do subtle but consistent changes in motion or object appearance over several seconds affect the JEDi score, and how does this compare to FVD's behavior in similar scenarios?

2. Issues About Human Evaluation.  Are these human subjects trained and qualified to evaluate video quality? Do the randomly selected videos adequately represent the entire set, and is there sufficient diversity? Has there been consideration of increasing the number of evaluation videos and including more subjects to ensure the reliability of the conclusions? The paper should provide more details on the demographic background of the human evaluators and their expertise in video quality assessment. Furthermore, it is unclear how the video samples were selected for human evaluation. Were they chosen randomly, or was there a specific sampling strategy to ensure a representative set of videos covering a wide range of quality and distortions? The lack of these details makes it difficult to assess the reliability and generalizability of the human evaluation results.

3.  In 5.1 section, how is the degree of blur determined, and are there any objective metrics for it? For the detection and assessment of noise and blur, many no-reference quality evaluation algorithms can perform this task. It is recommended to include some quality evaluation metrics for comparison, such as NIQE and Q-Align. The paper should clarify the specific parameters used to control the degree of blur applied to the videos, such as the kernel size and standard deviation of the Gaussian blur. Additionally, the paper should justify why no-reference image quality metrics like NIQE and Q-Align were not used to quantify the blur, especially since these metrics are designed to capture spatial distortions, which are a component of the blur applied in the experiments. It is important to understand if the temporal aspect of the blur is the only factor being evaluated, or if the spatial blur itself is also a contributing factor.

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
