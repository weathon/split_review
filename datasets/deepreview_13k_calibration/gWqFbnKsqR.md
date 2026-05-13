# Depth Any Video with Scalable Synthetic Data

- Decision: Accept
- Avg Score: 6.67
- Scores: 5, 10, 5

## Abstract
Video depth estimation has long been hindered by the scarcity of consistent and scalable ground truth data, leading to inconsistent and unreliable results. In this paper, we introduce \textbf{Depth Any Video}, a model that tackles the challenge through two key innovations. First, we develop a scalable synthetic data pipeline, capturing real-time video depth data from diverse synthetic environments, yielding 40,000 video clips of 5-second duration, each with precise depth annotations.
Second, we leverage the powerful priors of generative video diffusion models to handle real-world videos effectively, integrating advanced techniques such as rotary position encoding and flow matching to further enhance flexibility and efficiency.
Unlike previous models, which are limited to fixed-length video sequences, our approach introduces a novel mixed-duration training strategy that handles videos of varying lengths and performs robustly across different frame rates—even on single frames. At inference, we propose a depth interpolation method that enables our model to infer high-resolution video depth across sequences of up to 150 frames. 
Our model outperforms all previous generative depth models in terms of spatial accuracy and temporal consistency.
\blfootnote{$^*$Equal contribution.}
\blfootnote{$^\dag$Corresponding author.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a video-depth method that is trained on synthetic datasets only. The results show consistent video depth, generalizing diverse real-world scenes across diverse benchmarks. The paper provides practical engineering strategies, e.g., a batching strategy for better usage of RAM, temporal interpolation module, frame dropout, etc.

---

I rate the paper marginally below the acceptance threshold. The empirical results are very strong, but the paper mostly focuses on engineering solutions without scientifically interesting ideas. Also, there might be a license concern on the synthetic depth dataset. I am happy to improve the rating if the questions in the Weakness and Question sections are properly addressed.

### Strengths
* Good empirical results

  The method shows very good empirical results compared with the previous methods. The model outputs consistent depth estimates without temporal flickering, and good accuracy on public benchmarks. The ablation study in Table 3 validates the technical design choices of the method. 

* Clarity

   It's easy to follow the paper. The paper provides sufficient technical details on the datasets, training, architecture, etc.

### Weaknesses
 * A bit of engineering work

   The paper is mostly about engineering. It adopts conditional flow matching, uses large-scale synthetic datasets to boost accuracy, and introduces mixed-duration training to improve memory usage. All these aspects attribute better accuracy and performance, but it doesn't necessarily provide novel findings. If wanting to emphasize, what would be the most interesting, novel findings of the paper?

* Dataset licence and reproducibility

   It's curious if the collected synthetic dataset can be released or made public. What is the license condition of each game in DA-V? Are there any concerns about using the commercial game engine for research? Is there any plan to release the data? It can affect the reproducibility of the method.


* The effect of the DA-V dataset

   The ablations study in Table 5 shows that the synthetic game data improves the depth accuracy but quite marginally although the dataset size is around 6M. Why doesn't it improve the accuracy significantly? Is there any qualitative improvement that the metrics or numbers don't show?

### Questions
* Insights on why 2D VAE variants surpasses 3D VAE variants? I am wondering why 2D VAE variants outperform. Or asking differently, where do the artifacts of the 3D VAE variant come from? A good video depth model may have a good 3D prior, so 3D VAE might be a more natural choice to encode 3D information, but why does it underperform? Is it more difficult to train 3D VAE properly? Providing any insights or discussion is appreciated.

* In Fig. 7 (a) why do more denoising steps hurt accuracy?

* (nit) When looking at the qualitative examples, there are thin depth boundaries along the person's boundaries (the 5th example, woman, in Fig. 6), probably it's a kind of an average of depth of the person and the background. Why it's the case? What would be the source of this error?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
Depth Any Video is proposed for video depth estimation. It has a scalable synthetic data pipeline from game environments. A novel framework uses generative video diffusion models’ priors. It has a mixed-duration training strategy and a depth interpolation method. The model outperforms previous generative depth models, achieving good spatial accuracy and temporal consistency.

### Strengths
- The paper constructs a large-scale synthetic dataset of 40,000 video depth clips from 12 diverse modern video games.This dataset provides a scalable and cost-effective way to gather ground-truth video depth data and helps the model generalize to real-world scenarios.
- A mixed-duration training strategy is proposed. It includes frame dropout augmentation with rotary position encoding and a video packing technique.
- Effective Model Design
- The method achieves state-of-the-art performance among generative depth models.

### Weaknesses
The work in the article is very solid, with good model performance and efficiency, and comprehensive evaluation. The only concern for the reviewer is how the author ensures that the dataset, which is a major contribution, will be open-sourced as promised. This is very important for the community, but there are many difficulties regarding copyright and other aspects. In addition, it is necessary to evaluate and compare the diversity of the dataset.

### Questions
See Weaknesses

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper works on video depth estimation with diffusion models. First, considering the lack of video depth data, they collect 40,000 videos with depth annotation from video games. With the collected data, this paper fine-tunes the video diffusion model to achieve depth estimation. In addition, rotary position encoding and flow matching are introduced to further enhance the performance. With the proposed techniques, this paper achieves good spatial and temporal consistency on long video depth estimation.

### Strengths
1. The motivation for the framework is clear and reasonable, considering the limited data, inference speed and the long video in the applications.

2. Collecting and annotating high-quality data can improve the model and also inspire the community. It would be more beneficial if the data or collection pipeline can be open-sourced

3. Extensive experiments and ablation studies demonstrate the effectiveness of the proposed method.

### Weaknesses
1. **The representation is more image depth estimation rather than video depth estimation.** If I understand correctly, although the paper focuses on video depth estimation, the predicted relative depth maps are independent for each frame, which is demonstrated in the input normalization and alignment during evaluation. Specifically, each frame is normalized based on the depth range of itself and the scale and shift are also aligned for each frame during inference. In my view, this is incorrect for video depth estimation. To use the accurate relative depth of a video, the scale and shift should be the shared values aligned to the whole video, like DepthCrafter (Hu et al.). The current approach effectively treats each frame as an independent image, losing the temporal coherence that video depth estimation should capture. This is a critical flaw as it undermines the core concept of video depth, where depth relationships should be consistent across frames. The lack of a shared scale and shift means that the depth values between frames are not directly comparable, making it difficult to interpret the scene's 3D structure over time.

2. **Shift from EDM to Flow Matching.** The SVD model was pre-trained with the EDM denoising scheduler, which has a different optimization objective with flow matching. However, this paper directly fine-tunes the SVD model with conditional flow matching. As far as I know, InstaFlow (Liu et al, ICLR2024) optimized rectified flow for stable diffusion with velocity distillation instead of directly fine-tuning. I hope the authors could provide more explanation about the shift from EDM to Flow Matching. The direct fine-tuning approach raises concerns about potential conflicts between the pre-trained EDM weights and the flow matching objective. The optimization landscapes of these two methods are different, and directly applying flow matching to an EDM-trained model might lead to suboptimal results or even instability. It would be beneficial to understand the theoretical justification for this shift and how the authors addressed potential issues.

3.  A follow-up question about the shift. The ablation study of removing the pre-trained SVD model is required to demonstrate if the EDM pre-trained weights benefit or not. Without this ablation, it's difficult to ascertain whether the performance gains are due to the pre-trained weights or simply the flow matching fine-tuning process. This is crucial for understanding the contribution of the pre-trained model and the effectiveness of the proposed approach.

4. **More explanation about the video interpolation model.** As illustrated in Sec. 3.3, video interpolation model takes the key frames as input and interpolate other frames. Do the key frames replace the original noise? Or are they concatenated on the channels of latent? In addition, why are the mask maps replicated 4 times? The lack of clarity on how the key frames are integrated into the diffusion process makes it difficult to assess the effectiveness of the interpolation model. Specifically, it's unclear how the key frames influence the generation of intermediate frames and why the mask maps are replicated four times, which seems arbitrary without a clear explanation. A more detailed description of the input process and the rationale behind the mask replication is necessary.

### Questions
My main concern is the representation of video depth data. I feel it is not hard to use a shared scale and shift following DepthCrafter, which would be more reasonable for video depth estimation. In addition, I am also curious about the shift from EDM to Flow Matching.

**Post Rebuttal:** My previous questions are mainly addressed. However, the copyright issue remains severe after discussing with authors and other reviewers.

### Soundness
3

### Presentation
3

### Contribution
2
