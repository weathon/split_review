# DAWN: Dynamic Frame Avatar with Non-autoregressive Diffusion Framework for Talking head Video Generation

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 5, 6, 5

## Abstract
Talking head generation intends to produce vivid and realistic talking head videos from a single portrait and speech audio clip. Although significant progress has been made in diffusion-based talking head generation, almost all methods rely on autoregressive strategies, which suffer from limited context utilization beyond the current generation step, error accumulation, and slower generation speed. To address these challenges, we present DAWN (\textbf{D}ynamic frame \textbf{A}vatar \textbf{W}ith \textbf{N}on-autoregressive diffusion), a framework that enables all-at-once generation of dynamic-length video sequences. Specifically, it consists of two main components:  (1) audio-driven holistic facial dynamics generation in the latent motion space, and (2) audio-driven head pose and blink generation. Extensive experiments demonstrate that our method generates authentic and vivid videos with precise lip motions, and natural pose/blink movements. Additionally, with a high generation speed, DAWN possesses strong extrapolation capabilities, ensuring the stable production of high-quality long videos. These results highlight the considerable promise and potential impact of DAWN in the field of talking head video generation. Furthermore, we hope that DAWN sparks further exploration of non-autoregressive approaches in diffusion models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work presents a non-autoreregrssive diffusion based approach for talking head generation. This allows the generation of videos with non-fixed length. To enhance the performance the authors also decouple the motion of lips, head, and blinks and also introduce a two stage curriculum learning strategy. The proposed model is evaluated on the CREMA and HTDF datasets achieving state-of-the-art results.

### Strengths
The paper is well written and easy to follow

First non-autoregressive diffusion-based approach for talking head generation

### Weaknesses
Why is the proposed approach compared against wav2lip? Wav2lip only generates the mouth region, therefore the comparison is not really fair. The authors are encouraged to explain in the paper this decision and clearly acknowledge this limitation.

The authors use the syncnet model for measuring the quality of the generated lip movements. Why not using a lipreading model? It would be a more accurate measure of the lip movement quality. An explanation why syncnet is preferred over lipreading models would be very useful. Alternatively, the authors could use some public lipreading models to evaluate the performance (e.g., AutoAVSR, Raven, AV-Hubert).

The authors use several quantitative metrics to evaluate the model's performance and this is good. However, a user study is missing. There are no quantitative metrics which correlate highly with human perception, therefore evaluating the performance of generative models via user studies is highly desirable. The paper would be much stronger if a user study is included. Otherwise, the authors should explain why it's not included.

Table 1, why are some results underlined? This should be explained in the captions.

On which dataset is the LFG trained? Is it trained on each dataset separately? Also, what's the impact of pre-training? Has the option of training the LFG component jointly with the rest of the model been considered (and if yes can some results be presented)? The paper would be stronger if the author provide additional details regarding the above questions.

### Questions
Please see above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a diffusion-based non-autoregressive talking head synthesis method that operates with input from only a source portrait and an audio sequence. The method is performed in a two-stage manner: a Latent Flow Generator (LFG) serves as the video reenactment model, and a diffusion model together with PBNet serve as the motion generation models. To achieve non-autoregressive synthesis (NAR), PBNet generates the entire blink and pose sequence at once. The authors also propose a two-stage curriculum learning strategy to enhance the efficiency and performance of the diffusion model's learning process.

### Strengths
1. The paper is well written and easy to read. 
2. The proposed method can performed nearly in real time on a single V100 16G GPU.

### Weaknesses
1. I believe the proposed method lacks novelty. The overall architecture and the two-stage approach, which involves training a reenactment model first and then generating motion latents, have already been proposed in many existing works, such as TH-PAD[1], GAIA[2], VASA-1[3], AniTalker[4], and so on.. Although the authors attempted to innovate from a non-autoregressive perspective, I believe that their discussion and argumentation regarding the advantages of NAR are not sufficiently robust, and I will state my reasons below.
2. I don't think the proposed NAR method and experiments conducted demonstrate the authors' claim:  
a) Generating only blinks and poses through PBNet is not sufficient; the expression-related motion is still generated from the diffusion branch with audio input as a condition.  
b) The authors claim that there is error accumulation in long video sequences of existing AR and SAR models, but no comparative experiments have been conducted between the proposed NAR method and existing methods to prove this claim.  
c) Given that the authors consider NAR as the main contribution of this paper, the paper does not adequately discuss the advantages of NAR over AR and SAR, nor does it provide reasonable comparative metrics to substantiate these claims. Merely comparing general metrics such as image quality, lip sync, identity, and motion matching is not sufficient to demonstrate that the performance improvements are due to the adoption of NAR.  
3. Methods like Anitalker[4], TH-PAD[1], and VASA-1[3], etc., have similar overall architectures with the proposed one, but the authors did not illustrate the differences between the proposed method and these methods.
4. Recently, many diffusion-based talking head synthesis methods have been proposed, such as AniPortrait[5], Anitalker[4], Hallo[6], EchoMimic[7], FollowYourEmoji[8], and so on. Most of them operate in an auto-regressive manner. The authors did not compare the overall performance with these methods; therefore, there is no adequate evidence to prove the performance superiority of the proposed method.

Generally, I think the authors should conduct more experiments and propose more reasonable metrics to prove the effectiveness of the proposed method. And considering the main contribution is the non-autoregressive approach, the authors need to adequately discuss its advantages over AR and SAR. Based on the above reasons, I have doubts that this submission meets the bar for publication.

If the authors could discuss the advantages of NAR more thoroughly and supplement with sufficient experiments to prove that the proposed method has better effects compared to existing diffusion methods, I would raise my rating.

### Questions
1. I have a question regarding the ablation study on the TCL strategy: when the model was trained only with stage 1 and only with stage 2, did you maintain the same number of training epochs and steps as in the proposed method? I am curious to know whether the effectiveness of the two-stage curriculum learning is due to the training time or the strategy itself.

New after rebuttal: I raised the soundness score from 1 to 2 and the rating from 3 to 5.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents a new method for talking head generation called DAWN. This networks contains three main parts: a latent flow generator to drive a source image using latent flows, an "audio to latent flow" diffusion network and a pose and blink generation network. The network first predict latent flows from an audio sequence and pose and blink parameters. Those latent flows are then used by the latent flow generator to project the motion to RGB space using a source image containing the new identity. The pose and blink parameters are generated by the pose and blink generation network. DAWN outperforms the method used in the comparison on most metrics quantitatively and also qualitatively. The generated head pose and blink can be replaced by real one extracted from video for better control on the generation. Extensive ablation study is provided.

### Strengths
- The method works directly on the image by using its own latent flow generator. This is good because the network doesn't need to rely on other intermediate representations (e.g. 3dmm extracted from the video) which can already contain errors leading to bad generation.

- DAWN is able to generate pose and blink directly from the audio which is something not many methods do.

- By generating the head pose and blinking parameters outside the diffusion network and using them as condition instead the authors make their method more controllable.

- Qualitative results look good even if in low resolution.

- The authors provided video results for qualitative evaluation.

- The ablation study is extensive.

### Weaknesses
 - The main issue I have with the paper is that the method used as baseline for the comparison are not state of the art: Wav2Lip, MakeItTalk and Audio2Head are from 2020-2021 while SadTalker and DiffusedHeads are from 2023. There are more recent method that could have been used for the quantitative comparison [1,2], there also exist diffusion based method that perform much better than DiffusedHeads [3]. Additionally several recent methods, for which the code is not available, could have been considered only for the qualitative results due to their impressive performances [4,5,6].

- On the same subject DiffusedHeads is known to perform badly on out of distribution data. It was trained on the MEAD dataset and tend to fail if the background is not green.

- The method is able to generate head pose but both datasets used for experiments exhibit limited head poses. It would have been better to use the VoxCeleb or CelebV-HQ datasets to evaluate the quality of the generated head poses.

- Most experiments are performed with a resolution of 128*128 when state of the art usually use 256X256 or higher (notably for HDTF that is often used at 512X512).

- In table 1 the LSEc and LSEd of wav2lips are not in bold/underlined when they should, they are often the best.

- For the video results provided the authors should make it clear whether the head pose was generated or taken from the ground truth. In some examples (e.g. driven_by_music.mp4) it look really impressive but I suspect it come from the ground truth since the results in the comparison video, while good, are not as impressive.

- It is still not clear how the non-autoregressive part is used during inference. Are the sequences generated only at a chosen size (e.g 200 for HDTF)? Or are several sequence generated then put back to back to make long videos (like the ones from the supplementary material). If it is the latter, since the method is non-autoregressive how do the authors avoid discontinuity between sequences with respect to the head pose?

- In table 4 the authors show that PBNET improve lips synchronization (LSEd and LSEc) by a lot but do not explain in details why this is happening. While it's true that the training become more difficult as a result there is still a loss focusing on lips so the lip motion should stay about as good in my opinion.

- I understand why the authors perform two training with different sequence length and the ablation shows that it improves results. However I don't see why they set X_src=X_1 for the first training instead of using a random starting frame like they do in the second training. Could the authors clarify their choice on this?

- The paper mention that a GAN loss is used inside PBNET but does not say how it is applied. Is there a discriminator? This part need to be clarified.

- The paper state that AR and SAR "leads to constrained performance and potential error accumulation, especially in long video sequences" but only cite one paper to support that claim. Most other methods mentioned in the paper or the one I proposed seem fine in that regard. The authors should develop this part with more examples.

### Questions
- The latent flow generator is effectively a video-driven talking head generation method. It would have been interesting to see how it perform against similar methods, e.g. [7].

- Notation issue: in eq .6 the input are x_src,y_1N and p_1N. in the conditioning paragraph and in the figure it is stated that instead the inputs are in fact Z_src,a_1N and p_1N. Also p_1N is not defined when it's used in eq.6. Both of these things need to be corrected.

[7]: Y. Wang, D. Yang, F. Bremond and A. Dantcheva, "LIA: Latent Image Animator," in IEEE Transactions on Pattern Analysis and Machine Intelligence, doi: 10.1109/TPAMI.2024.3449075.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces DAWN, a system that uses non-autoregressive (NAR) diffusion models to generate talking head videos of varying lengths from portrait images and audio. This method achieves faster processing speeds and high-quality outputs. To overcome limitations in NAR approaches and improve the modeling of longer videos, the system separately controls the movements of the lips, head, and blinking. This provides more precise control over these individual movements. The paper proposes PBNet, a network that generates realistic head poses and blinking sequences directly from audio clips using an NAR approach. The Two-stage Curriculum Learning (TCL) strategy is introduced to train the model effectively in generating lip movements and controlling head poses and blinks accurately, which helps in achieving robust convergence and better extrapolation capabilities.

### Strengths
1. The performance is decent
2. Talking head generation is a research field with practical value.

### Weaknesses
1. The motivation for introducing NAR is relatively weak. VASA[1], which uses SAR, already achieves real-time performance with good results. The motivation to use NAR to improve inference speed is weak, as the paper is only faster than diffused head, but the slower speed of diffused head is due to it generating images directly rather than intermediate representations.
2. The novelty of this paper is limited, as many modules are similar to previous methods. For example, the LFG is similar to the FOMM[2] series of work, and pose prediction is similar to SadTalker[3]. Although the paper introduces some novel training techniques like TCL, previous methods have already achieved good results without relying on such fancy techniques. Therefore, the significance of these fancy techniques is questionable.

### Questions
Did the paper conduct a user study? I don’t seem to have seen one. User studies are very important in this field.

### Soundness
3

### Presentation
3

### Contribution
2
