# STREAM: Spatio-TempoRal Evaluation and  Analysis Metric for Video Generative Models

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 3, 6

## Abstract
Image generative models have made significant progress in generating realistic and diverse images, supported by comprehensive guidance from various evaluation metrics. However, current video generative models struggle to generate even short video clips, with limited tools that provide insights for improvements. Current video evaluation metrics are simple adaptations of image metrics by switching the embeddings with video embedding networks, which may underestimate the unique characteristics of video. Our analysis reveals that the widely used Fr{\'e}chet Video Distance (FVD) has a stronger emphasis on the spatial aspect than the temporal naturalness of video and is inherently constrained by the input size of the embedding networks used, limiting it to 16 frames. Additionally, it demonstrates considerable instability and diverges from human evaluations. To address the limitations, we propose STREAM, a new video evaluation metric uniquely designed to independently evaluate spatial and temporal aspects. This feature allows comprehensive analysis and evaluation of video generative models from various perspectives, unconstrained by video length. We provide analytical and experimental evidence demonstrating that STREAM provides an effective evaluation tool for both visual and temporal quality of videos, offering insights into area of improvement for video generative models.  To the best of our knowledge, STREAM is the first evaluation metric that can separately assess the temporal and spatial aspects of videos.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
While evaluation metrics for image generative models are relatively comprehensive, those for video are limited. This paper addresses the drawbacks of existing metrics, proposing a new metric, STREAM, which comprehensively evaluates the temporal and spatial aspects of videos. Experimental validation was conducted on several baseline video generative models.

### Strengths
- The writing is clear and easy to follow.
- The paper's motivation is strong. Given the rapid development in the field of video generation, traditional metric FVD falls short in representing performance comprehensively. This paper bridges this gap.
- The proposed metric allows independent evaluation of spatial and temporal domains, making it applicable for assessing the quality of long videos.

### Weaknesses
 - The experimental section of the paper is relatively weak, being limited to a few older baseline models. Authors should focus more on current open-source Text-to-video models, which would provide more convincing results.
- Although UCF-101 is a common benchmark dataset, as a contribution paper introducing a new evaluation metric, testing on a wider range of datasets and tasks, including T2V, video prediction, and the latest works in unconditional generation, would enhance the paper's credibility.

### Questions
Despite some experimental limitations, the paper makes substantial theoretical contributions. The problem it addresses holds significant value. Currently, I am providing a borderline accept score, hoping the authors will address the experimental aspects mentioned in my review in their future research.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a novel method to evaluate the quality of generated videos. Specifically, it proposed STREAM-T and STREAM-S to assess temporal and spatial aspects of the videos respectively. STREAM-T is designed to measure temporal quality. It evaluates the continuity and consistence of videos by calculating the FFT of real and fake videos and comparing the difference of the frequences. STREAM-S evaluates the spatial quality by classifying the amplitude at frequency of 0 using KNN. Experiments show that the proposed method is able to measure video quality better than current methods such as FVD.

### Strengths
1. The paper is well-written and easy to follow.
2. The proposed method proposed a novel method targeting a challenging task, video generation evaluation. 
3. Experiments show the effectiveness of proposed method in evaluating temporal quality in video generation.
4. STREAM-T is a reasonable metric since it applies statistical method rather than simple l2 or l1 distance to compute loss of video frequency.

### Weaknesses
1. How will the performance be if most of the generated videos are still? Can they be correctly evaluated?
2. Using P&R to compute fidelity and diversity of fake videos is reasonable, but why to use amplitude at frequency of 0 as sample points? I would like to see more explanations from the authors.
3. As video quality is very subjective, a systematic evaluation by human raters is required to compare with current method FVD.
4. The difference in the style of real and fake video datasets may have a huge effect on the result. For example, if real videos tend to have fast changes, the frequency may be concentrated on the high frequency, and the curve fitted may have a higher skewness. In such case, if the curve fitted by fake videos is less steep (fake videos change slowly), skewness may be small, and even if the fake video is of high quality, STREAM-T may be small.

### Questions
see weaknessess

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a new metric to evaluate the generated videos. The authors present three new metrics to assess video quality namely 1) spatial fidelity 2) diversity and 3) temporal coherence. Authors construct various kind of perturbation and evaluate the videos.

### Strengths
* Paper is easy to follow
* The most important contribution of the paper is the newly proposed metric is bounded between 0-1 as opposed to FVD, which is an unbounded metric.

### Weaknesses
 * FVD is a single metric used to evaluate a video. With STREAM as a metric, you would have 3 sub-metrics to evaluate generated videos. This would result in $2^3$ scenarios when comparing two baselines, making it tedious to evaluate a new method.



### Questions
I would like to see how this metric performs in three scenarios.
* When the generated video consists of only one frame repeating throughout the video segment
* One of the main selling points of the FVD metric was it penalizes blur phenomena significantly higher than noise phenomena. This was a useful property because it correlates well with human vision. Additionally, the video generation methods tend to produce blurry samples which would score higher on traditional metrics like SSIM and PSNR. I would want to see how it performs on blurry videos (apply Gaussian blur). 
* What would be the results if the video is reversed temporally and evaluated? please do the same for flipping the videos spatially(take mirror images of the frames) and lastly, run the evaluation for both spatially and temporally flipped video sequences.
I would like to see an evaluation of all these three scenarios before making my final decision.

How is the metric affected by the length and resolution of videos, and if it is affected, please provide the standardization of metric because people can game the metric utilizing this loophole.

### Soundness
2 fair

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
The authors propose a set of metrics to evaluate generative models for video. The propose STREAM-T to assess temporal naturalness as well as STREAM-F for fidelity of videos and STREAM-D for the diversity of videos. They compare to the Frechet Video Distance (FVD) on both synthetic data and using a number of generative models.

STREAM-T is based on the idea of looking at FFT features of the video to assess temporal "naturalness", while STREAM-F and STREAM-D are based on Precision & Recall metrics, but include tweaks to make them work better for video data.

### Strengths
**Originality:** The Authors argue that STREAM can separately assess temporal and spatial aspects of video, and works regardless of video length (unlike FVD). To the best of my knowledge this is true. I like their idea of using FFT to look at spectral features to identify temporal consistency.

**Quality:** The motivation for their method makes sense, and I think their empirical valuation is sensible. The authors only compare to FVD.

**Clarity:** I was able to follow along nicely

**Significance:** I think it is certainly nice to be able to have several dimensions upon which to evaluate generative methods.  However, it is unclear to me how useful that is in practice. Having these metrics can certainly help "debug" generative methods, but I would imagine that they will not be as useful as a "one metric to judge overall quality" that FVD provides. Especially since the human evaluation shows that FVD actually does fairly well (especially given that in contrast to the three measurements of STREAM it  is only a single number).


**UPDATE AFTER READING THE REBUTTAL**
Overall, my judgment is that the authors have convinced me that in principle this manuscript deserves publication: they attack a meaningful problem and their empirical work is solid. So I think this work scores high enough in Originality,  Quality, and Clarity to be publication. As far as signficance goes: I'm not 100% conviced ICLR is the best venue for this work (I'd imagine you find a more interested audience in conferences that are more focused on computer vision), which is why I still think the manuscript is only marginally above the acceptance threshold for ICLR.

### Weaknesses
 * While I think it is useful to have metrics that focus on different aspects of the generation, I would imagine that while developing a method, most of the time it is more helpful to have a single metric to look at to judge progress (if I'm developing a new method and my newest change to the method improves STREAM-F but hurts STREAM-T, is it a good modification or not. Thus, I think the proposed STREAM metrics will be helpful, but will fail to actually replace FVD.  If the authors could find a good way to combine their measurements into a single number (e.g. akin to the F1-score to combine P&R), I think the paper would have more impact. 
* The paper mentions the Video Inception Score (VIS) several times as go-to metric for this task, but does not compare to it. The authors should motivate why they did not use this metric at all, despite it being an obvious competitor.
* I find it confusing that the authors introduce the term "STREAM-S": Its name implies that it's one of the metrics that is being introduced (it follows the same naming convention), but it actually isn't. I'm absolutely unclear what that term actually denots.. I think the paper would improve in clarity if that term would be removed and instead clearly state that there are 3 new metrics that are being introduced (STREAM-T, STREAM-F, STREAM-D).

### Questions
* I would like to know how well FVD correlates with the various STREAM measures. Figures 3, 4 and 6 seem to indicate that the spearman correlation between STREAM-T and FVD is actually fairly high, which is completely contrary to the main text, which several times claims that FVD is not good at picking up temporal details.

* What is the reason for not comparing against VIS?

* STREAM-T uses a histogram comparison. How do binning sizes affect the outcome?

* Will the authors provide source code for implementing STREAM? It seems nontrivial to implement.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
