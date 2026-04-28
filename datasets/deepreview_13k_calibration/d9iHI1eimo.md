# TAPE3D: Tracking All Pixels Efficiently in 3D

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Tracking dense 3D motion from monocular video remains challenging, particularly when aiming for pixel-level precision over long sequences. We introduce TAPE3D, a novel method that efficiently tracks every pixel in 3D space, enabling accurate motion estimation across entire videos. Our approach leverages a joint global-local attention mechanism for reduced-resolution tracking, followed by a transformer-based upsampler to achieve high-resolution predictions. Unlike existing methods, which are limited by computational inefficiency or sparse tracking, TAPE3D delivers dense 3D tracking at scale, running over 8x faster than previous methods while achieving state-of-the-art accuracy. Furthermore, we explore the impact of depth representation on tracking performance and identify log-depth as the optimal choice. Extensive experiments demonstrate the superiority of TAPE3D on multiple benchmarks, achieving new state-of-the-art results in both 2D and 3D dense tracking tasks. Our method provides a robust solution for applications requiring fine-grained, long-term motion tracking in 3D space.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel method for dense 3D tracking in monocular video. By introducing the anchor tracks and attention based upsampling methods, the proposed method significantly improves the inference speed by ~10x. By modifying the depth representation and supervision signal, the method significantluy improves the performance.

### Strengths
1. The proposed method indeed remedy the efficiency issue of previous SOTA methods significantly.
2. The experiments are comprehensive and convincing.

### Weaknesses
Some key concepts and design choices are not well explained. 
 
1. Why do we need certain anchor tracks? What if we sample some certain points in the dense tracks?
2. The difference of sparse tracks and dense tracks are not well explained. For the comparisons in subfigure 2 and 3 in Fig.3, the dimension of sparse tracks and dense tracks are both T x N, then why it is called dense tracks? What is N' and L, the meaning of these two parameters are not well defined and explained.  
3. If the depth is predicted from monocular video, the scale is not specified. How can we ensure their consistency across different frames?
4. The attention upsampling method is quite related to the well known guided filter work. It is better to discuss the relationship with it.

### Questions
1. Why the 2D version consistently better than 2D version in Table2? Is there any analysis on this unexpected results?
2. How the key parameters such as M, r, N' and L are chosen?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a model for tracking points in 3D densely, whose architecture is inspired by 2D sparse tracking CoTracker model, but with a number of modifications to 1) lift the tracks to 3D and 2) improve the model efficiency to allow for dense tracking with reasonable computational cost. 

For lifting the tracks to 3D, the authors propose that the model takes RGB-D frames as input, and add depth tokens to the model's transformer framework (eq 1) to refine the depth predictions jointly with the 2D tracking predictions. This seems to be similar to the approach proposed in SceneTracker.

For tracking densely with reasonable computational cost, the authors adopt two different strategies. First, they perform most of the tracking prediction at a downsampled resolution (H/r, W/r) and propose a learnt cross-attention based upsampler to upsample the predictions to (H, W) resolution. Second, authors introduce some modifications to the spatial attention module proposed in CoTracker to increase efficiency. As in CoTracker, they perform cross-attention between virtual tracks and sparse tracks (here sampled on a uniform grid on the first frame and called "anchor tracks"), and then perform most of the computation by self-attention layers on the virtual tracks. However, they introduce a third tensor of "dense tracks", which they process by local attention and then fuse with the anchor tracks before decoding back the final refined dense tracks predictions by performing cross-attention with the virtual tracks.

The model is trained using a fully supervised setting by using synthetic videos generated with the Kubric simulator. The model is first pre-trained on the 2D tracking setting for 100k iterations, and then further trained on the 3D setting for an additional 100k iterations.

Their model is evaluated both for the 2D and 3D tracking tasks using standard benchmarks such as CVO, LSFOdyssey and TAPVid-3D. The results show the model obtains SOTA results on the CVO benchmark as well as in the TAPVid-3D benchmark. On the LSFOdyssey benchmark, the model trained on Kubric does not attain SOTA performance, but the one finetuned on LSFOdyseey does.

The authors conduct a series of ablation studies to show the impact of the design decisions regarding the depth respresentation, spatial attention module and upsampler.

### Strengths
This is one of the first papers addressing the TAP-3D problem with a feedforward model (not requiring test-time optimization), along with SceneTracker and SpatialTracker, which makes it a valuable contribution in this newly developing field.

In addition, the authors present quantitative results on both 2D tracking and 3D tracking which demonstrate the good performance of the model. The proposed model obtains SOTA results on the CVO benchmark as well as in the TAPVid-3D benchmark.

The visualizations included in the supplementary material help to further assess the quality of the 3D tracks produced by the model and compare it to the SceneTracker and SpatialTracker baselines. The results show a cleary superiority of TAPE3D over SceneTracker, and  slightly superior results compared to SpatialTracker. These observations are roughly in line to the reported quantitative results on TAPVid-3d.

The design choices proposed by the paper are thoroughly ablated in section 4.3 and Table 6, demonstrating the value of each of these design decisions.

Finally, Fig. 1 shows that in the dense-tracking scenario, TAPE3D is at least 8x faster than the baselines, while obtaining superior performance on TAPVid-3d.

### Weaknesses
While the paper is a valuable contribution with good results, the model design seems to be mainly a combination of ideas from SceneTracker and CoTracker. The paper does not clearly state which ideas are novel, and which are borrowed from these previous methods. 

Furthermore, the experimental section only presents 2D tracking results on CVO, which is not the most widespread 2D tracking benchmark. Results on TAPVid-DAVIS would help in demonstrating the SOTA status of this model for 2D tracking. 

However, the main weakness of the method lies in that some of technical contributions are not presented with sufficient clarity or mathematical rigor. First, it is not clear how the dense tracks from Fig. 3, (3), are computed and how they connect to the tokens G^i_t of eq (1). In addition, the eq. (3) seems mathematically incorrect or at least too vague in notation and lacking explanation. It is not explained whether the functions q and k are linear layers and on what they are applied. Also, it's not clear what the softmax function is applied over. Finally, this is referred to a as cross-attention, but the values seems to be missing from the equation. While Figure 4 helps in understanding the general idea of the proposed attention-based upsampling, it is not exactly clear how to connect it to eq. (3) and therefore to fully understand the proposed module. 

Regarding the training procedure, it's not clear why the authors train on such small number of videos (5.6K) if these are synthetic videos that can be generated at a larger scale at ease. It's also not clear adding other data sources, such as PointOddysey would improve performance on the  TAPVid-3D benchmark.

### Questions
Could you please describe which elements in the model design are novel and which are borrowed from prior work?

Have you tried evaluating your method on TAPVid-DAVIS (first)? Does it obtain SOTA results on 2D tracking compared to CoTracker and BootsTAPIR?

Please clarify how the dense tracks in Fig. 3 (3) relate to the explanations in Sec. 3 and in particular to the tokens G^i_t of eq. (1).

Please clarify how the proposed attention-based upsampling works and provide a corrected eq. (3) if possible. Please explain how the \tau cross attention blocks from Fig. 4 operate. Are these multiple heads in parallel?

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
This paper presented a method, TAPE3D, that efficiently tracks every pixel of a frame throughout a video, demonstrating state-of-the-art accuracy in dense 2D/3D tracking while running significantly faster than existing 3D tracking methods.

### Strengths
1. TAPE3D introduces the spatial-temporal transformer to extract more visual features and uses the Upsampler module to obtain high-resolution results. 
2. TAPE3D delivers dense 3D tracking at scale, running over 8x faster than previous methods while achieving state-of-the-art accuracy.

### Weaknesses
1. The idea of using the spatial-temporal transformer is not new, such as [1][2][3].
2. The authors are suggested to provide the compilation cost of each module to verify the efficiency of TAPE3D.
3. Are all inference experiments testing on a same machine? The information of the machine including GPU and CPU are suggested to provide.

### Questions
See weakness. If questions addressd, I will increase the rating.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a method for dense 3D motion prediction, named TAPE3D. This paper finds that there is a redundant design in the CoTracker's global attention, and proposes their local-global attention, which reduces calculation costs to both accelerate the speed and reduce the resource requirement. After that, the paper proposes a transformer-based upsampler, which shows better performance than previous upsamplers, such as the ConvNet-based used in optical flow methods. This paper also finds that using log-depth as the depth representation is an optimal choice. Finally, TAPE3D achieves SoTA performance on both 2D/3D point tracking with the fastest speed.

Overall, TAPE3D is an interesting work that contributes some insights to the field, and this must be acknowledged. However, these contributions are a little lack depth, and feel somewhat scattered, like a collection of bundled findings. Considering that there are some parts not clearly written and are difficult to understand, I'm giving 'marginally below the acceptance threshold' for now.

### Strengths
1. This paper proposes a method, named TAPE3D, which not only obtains SoTA performance but also achieves the fastest speed.
2. This paper proposes the local-global cross-attenton, which reduces the calculation consumption while achieving better performance.
3. This paper proposes a transformer-based upsampler to upsample the sparse predictions to dense ones, achieving better performance than the ConvNet-based ones in previous optical flow methods.
4. This paper finds that using log-depth as the depth representation can obtain better performance.

### Weaknesses
1. Although many contributions are provided, they are a little lack depth, and feel somewhat scattered, like a collection of bundled findings. (but we have to acknowledge the contributions' value)
2. There are some parts that are not clearly written. In local-global attention, what N' (Fig 3) means, and why N' is different between training and evaluation? And it seems that there is no description of what M means (number of anchors if I understand correctly).
3. It seems that the differences between the proposed Local-Global attention and the global one in CoTracker are
    a) use anchor tracks to attend virtual tracks.
    b) add local attention.
Although a) can reduce the calculation consumption, b) needs additional calculation consumption. During evaluation, local-global even requires O(TKM + TLN^2) more calculation.
4. In L290-L295, I'm confused why the virtual tracks should "cross-attent to a local random patch of tracks". What is "local random patch of tracks"? In Fig.3, it seems that the virtual points only attend to anchor tracks in cross-attention and themselves in self-attention.
5. In Table.5, why BootsTAPIR+ZoeDepth is worse than CoTracker+ZoeDepth? As far as I know, BootsTAPTIR have much better performance than CoTracker in 2D point tracking, maybe more comparisons are required to show the reasonability (LocoTrack and TAPTRv2 for example).

### Questions
For the questions, please refer to the Weaknesses part. If the author can address my concerns, I will raise my score.

### Soundness
2

### Presentation
2

### Contribution
3
