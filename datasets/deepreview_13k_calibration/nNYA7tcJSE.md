# ViBiDSampler: Enhancing Video Interpolation Using Bidirectional Diffusion Sampler

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
Recent progress in large-scale text-to-video (T2V) and image-to-video (I2V) diffusion models has greatly enhanced video generation, especially in terms of keyframe interpolation.
However, current image-to-video diffusion models, while powerful in generating videos from a single conditioning frame, need adaptation for two-frame (start \& end) conditioned generation, which is essential for effective bounded interpolation. 
Unfortunately, existing approaches that fuse temporally forward and backward paths in parallel often suffer from off-manifold issues, leading to artifacts or requiring multiple iterative re-noising steps.
In this work, we introduce a novel, bidirectional sampling strategy to address these off-manifold issues without requiring extensive re-noising or fine-tuning. 
Our method employs sequential sampling along both forward and backward paths, conditioned on the start and end frames, respectively,
ensuring more coherent and on-manifold generation of intermediate frames. 
Additionally, we incorporate advanced guidance techniques, CFG++ and DDS, to further enhance the interpolation process. 
By integrating these, our method achieves state-of-the-art performance, efficiently generating high-quality, smooth videos between keyframes. 
On a single 3090 GPU, our method can interpolate 25 frames at 1024$\times$576 resolution in just 195 seconds, establishing it as a leading solution for keyframe interpolation.
Project page: \small \textsf{\url{https://vibidsampler.io/}}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work introduces a novel, bidirectional sampling strategy to address off-manifold issues without requiring extensive re-noising or fine-tuning. The proposed method employs sequential sampling along both forward and backward paths, conditioned on the start and end frames, respectively, ensuring more coherent and on-manifold generation of intermediate frames.

### Strengths
- Unlike previous fusing strategies, which compute two conditioned outputs in parallel and then fuse them, the proposed bidirectional diffusion sampling strategy samples two conditioned outputs sequentially, which mitigates the off-manifold issue.
- The proposed method can further work with advanced on-manifold guidance techniques (CFG++, DDS) to produce more reliable interpolation results that have better alignment of the input frames.
- This is a training-free method which can efficiently interpolate between two keyframes to generate a 25-frame video at 1024×576 resolution in just 195 seconds on a single 3090 GPU.

### Weaknesses
 - The experimental results presented lack PSNR scores. While accurate recovery of intermediate frames may not be the primary objective of this study, and high PSNR values might not necessarily indicate superior human preferences, it is still beneficial to include the score to provide readers with a clearer understanding of the work’s potential.
- The proposed bidirectional sampling addresses the off-manifold issue, but it comes with the potential for deviation from the start or end frame, depending on the order of sequential sampling. To mitigate this issue, the authors have incorporated previous guidance techniques. However, I would appreciate a more comprehensive video comparison in the ablation study, in addition to the provided static comparison on a single scene.

### Questions
- How to incorporate text conditioning into your framework so users can control the action in the generated frames?
- The results and presentation are sound, except for some minor issues (see weaknesses). I will increase my score once the authors address my concerns.

### Soundness
3

### Presentation
3

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
This paper presented a bidirectional sampling strategy, sequential sampling along both forward and backward paths, for video interpolation. Additional manifold guidance such as DDS and CFG++ are further introduced to enhance the interpolation results. Experiments are conducted to evaluate the proposed ViBiDSampler.

### Strengths
+ A bidirectional sampling strategy, sequential sampling along both forward and backward paths, for video interpolation. 
+ Additional manifold guidance such as DDS and CFG++ are further introduced to enhance the interpolation results. 
+ Training-free, convenient for use.
+ Experiments are conducted to evaluate the proposed ViBiDSampler.

### Weaknesses
 - The method is training-free. In general, training-based method can be more effective.
- More ablation study is suggested to assess the effect of pre-trained video generation models. Will better video generation models result in better performance?
- Discussion on the limitation and future work.

### Questions
- The method is training-free. In general, training-based method can be more effective.
- More ablation study is suggested to assess the effect of pre-trained video generation models. Will better video generation models result in better performance?
- Discussion on the limitation and future work.

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
This paper proposes a inference strategy to achieve frame interpolation w/o training. Its key idea is to use the pre-trained stable video diffusion model as a prior and complete the frame interpolation given the first and the last frame as a condition. The main improvement seems from the proposed bidirectional sampling combining with SOTA sampling approaches, i.e., DDS and CFG++.

### Strengths
+The paper is easy to follow .
+The visualization results seem impressive comparing with other baselines provided in the paper.

### Weaknesses
 The contribution of this paper seems marginal. It seems the main contribution comes from eq. (9). However, the improvement of such modification seems not that obvious comparing with using SOTA sampling approaches including DDS and CFG++ from Table. 1, i.e., only "Ours (full)" shows obvious improvement comparing with other baselines but if my understanding is correct, other baselines seem not using DDS and CFG++.

 The practical use the proposed approach seems not convincing. The proposed approach still requires 192s to generate 25 frames, which is at least two times longer than directly inferencing a video generation model with similar computational cost. Moreover, I also wonder how to keep the consistency between frames when the required length of the output video is beyond 25.

### Questions
My main concerns are mainly as follows:

1. The contribution of this paper seems marginal. It seems the main contribution comes from eq. (9). However, the improvement of such modification seems not that obvious comparing with using SOTA sampling approaches including DDS and CFG++ from Table. 1, i.e., only "Ours (full)" shows obvious improvement comparing with other baselines but if my understanding is correct, other baselines seem not using DDS and CFG++. The author should further verify the improvement of each technology used in the paper, i.e., bidirectional sampling, DDS and CFG++, e.g., providing more visualization as well as adding DDS and CFG++ to other baselines and show the improvement.

2. The practical use the proposed approach seems not convincing. The proposed approach still requires 192s to generate 25 frames, which is at least two times longer than directly inferencing a video generation model with similar computational cost. Moreover, I also wonder how to keep the consistency between frames when the required length of the output video is beyond 25.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes ViBiDSampler, a training-free method utilizing pre-trained image-to-video diffusion models for keyframe interpolation. They aim to tackle the off-manifold problem of previous studies, which leads to artifacts or costly processes. They propose bidirectional sampling, with a set of denoising-renoising-denoising with alternating conditioning on start and end frames. This way, they manage to keep the generated results stay on the original manifold. The additionally integrate advanced guidance methods like CFG++ and DDS to reach state-of-the-art performance.

### Strengths
Strengths
- Overall, the paper is easy to follow, with coherent and clear problem definition and solution.
- Simple methodology. The proposed method, Bidirectional sampling seems to be easy to use.
- Efficiency. The proposed method does not require additional training and is fast in inference.

### Weaknesses
1. Notations.
- The notations are confusing. For instance, $x_t$ seems to be used as a variable and a function. 
- The definitions could be further clarified. 
- Lines 247 - 256 was kind of confusing at first, with many similar looking notations without predefinitions, and mixed use of notations as functions and variables.


2. Limited contribution.

Although the proposed method is intuitive, simple, and quantitatively effective, some uncertainties remain.
- the 'Vanilla' setting at Table 1 and Figure 5, seems to show the effectiveness of bidirectional sampling solely, without guidance such as CFG++ and DDS. However, I am not fully convinced with its effectiveness, as Generative Inbetweening seems to outperform the vanilla version in Table 1. Also, in the qualitative results of Figure 5, the results of bidirectional sampling (vanilla) itself does not seem to be better than that of TRF.
- The concern above makes me wonder, if the superior performance of the entire framework proposed comes from the good guidance methods, CFG++ and DDS.
- In addition, CFG++ and DDS are manifold guidance methods proposed in other studies, and seems like this work simply took advantage of existing methods. I think it is hard to say that simply adoption of these guidance methods is a contribution.

In short, I am not fully convinced if the proposed bidirectional sampling itself is a powerful method compared to existing works, and suspect the superior performance could have come from the advanced manifold guidance methods, which, is hard to say to be a contribution.

### Questions
1. To my understanding, CFG++ and DDS could possibly be applied to existing methods, such as Generative Inbetweening. If so, could the authors provide experiments on this, to ablate and show the importance of bidirectional sampling?

2. In bidirectional sampling, in some aspects, I think it is possible for this to work, but in some aspects, I don't. For example, taking the example of Fig.3(b), there are three steps, (1) denoising (w/ $c_{start}$), (2) renoising, (3) denoising (w/ $c_{end}$). I am curious how the generation process goes through these steps. Maybe a visualization would be helpful, showing how the start / end conditions are really affecting in those steps. I am specifically curious of this process in that the (2) renoising step could possibly remove the information of $c_{start}$ injected from (1) denoising, and the conditioning could have possibly be injected only at (3), making the steps (1) and (2) redundant. A further analysis / clarification on this part, that the proposed method surely takes both start / end frame conditioning.

### Soundness
3

### Presentation
3

### Contribution
2
