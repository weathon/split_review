# Efficient-vDiT: Efficient Video Diffusion Transformers With Attention Tile

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
Despite the promise of synthesizing high-fidelity videos, Diffusion Transformers (DiTs) with 3D full attention suffer from expensive inference due to the complexity of attention computation and numerous sampling steps. For example, the popular Open-Sora-Plan model consumes more than 9 minutes for generating a single video of 29 frames. This paper addresses the inefficiency issue from two aspects: 1) Prune the 3D full attention based on the redundancy within video data; We identify a prevalent tile-style repetitive pattern in the 3D attention maps for video data, and advocate a new family of sparse 3D attention that holds a linear complexity w.r.t. the number of video frames. 2) Shorten the sampling process based on multi-step consistency distillation; We split the entire sampling trajectory into several segments and perform consistency distillation within each one to activate few-step generation capacities. We further devise a three-stage training pipeline to conjoin the low-complexity attention and few-step generation capacities. Notably, with 0.1% pretraining data, we turn the Open-Sora-Plan-1.2 model into an efficient one that is 7.4x −7.8x faster for 29 and 93 frames 720p video generation with a marginal performance trade-off in VBench. In addition, we demonstrate that our approach is amenable to distributed inference, achieving an additional 3.91x speedup when running on 4 GPUs with sequence parallelism.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the acceleration of 3D full attention video generation models, focusing on sparsifying 3D attention and reducing sampling steps. The authors propose an algorithm for searching optimal sparse attention masks based on the observed Attention Tile phenomenon and combine this with a consistency distillation method to reduce the number of steps, resulting in an accelerated version of DiT while striving to maintain generation quality.

### Strengths
The paper effectively optimizes DiT using sparse attention and MCD, and the proposed framework demonstrates commendable speed results alongside assured generation quality. Specific strengths include:

- The identification of the Attention Tile phenomenon, accompanied by a detailed analysis, provides a background for the design of sparse attention masks and proposes an algorithm for searching optimal mask sets. Comprehensive evaluation experiments validate the effectiveness of this method.
- The integration of the consistency distillation method leads to a complete acceleration framework, with rigorous ablation studies confirming the framework's soundness and ensuring generation quality. The FVD metric significantly outperforms the use of the MLCD method alone.

### Weaknesses
While the paper is rich in content, there are still potential issues to consider: According to Table 7, the acceleration benefits from sparse attention masks are not substantial, with noticeable quality degradation occurring beyond a 1.45× acceleration. Although there is some improvement when combined with MLCD (compared to a 5× acceleration), the effectiveness of the design based on the Attention Tile, which is a core contribution of the paper, appears insufficient here.

### Questions
- The changes in Dynamic Degree seem to exhibit a certain trend; are there any related experimental analyses available?
- There is a discrepancy between the acceleration results in Table 1 and Table 7. Could you please provide the specific experimental parameter differences (as they seem to be absent in the paper)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper tackles the inefficiency of DiTs used in video diffusion model. The speedup of the presented method comes from two sources: 1) pruning the large full 3D attention of VDM DiTs and 2) distilling the model into a multi-step consistency model.
The authors identify a repetitive tile-like pattern, termed "Attention Tile," in the 3D attention maps of video data. Leveraging this pattern, they propose a new family of sparse 3D attention mechanisms that reduce the computational complexity from quadratic to linear with respect to the number of video frames.
To further accelerate the inference process, the paper introduces a multi-step consistency distillation (MCD) technique. By dividing the sampling trajectory into segments and performing consistency distillation within each, the number of sampling steps required for video generation is significantly reduced.
Results show that the method achieves good speedup without suffer much performance, using limited training data.

### Strengths
1. The paper makes a significant contribution by discovering the "Attention Tile" phenomenon in 3D full attention Diffusion Transformers (DiTs) for video data. This insight into the redundancy and repetitive patterns within attention maps is a valuable addition to the understanding of how attention mechanisms function in video generation models.
2. Building on the Attention Tile observation, the authors propose a new family of sparse 3D attention mechanisms that reduce computational complexity from quadratic to linear concerning the number of video frames. This is a substantial improvement that directly addresses the inefficiency issues in existing models.
3. The introduction of the EFFICIENT-VDIT framework is a well-thought-out approach that combines multi-step consistency distillation, layer-wise sparse attention mask searching, and knowledge distillation. This pipeline effectively accelerates inference while maintaining high metrics.
4. Achieving these results using only 0.1% of the pretraining data is notable. It indicates that the method is not only computationally efficient but also data-efficient, which is advantageous when large datasets are not readily available.

### Weaknesses
1. The paper could benefit from a more in-depth discussion of the trade-offs involved, such as the balance between sparsity level and video quality or the impact on different types of video content (e.g., fast-moving vs. static scenes). For instance, why don't you directly use the demo videos on OpenSORA's websites and compare the qualitative results? They provided both static scenes with only relative camera poses and more dynamic scenes, e.g. filming of an explosion scene.
2. The method relies on the observation that the Attention Tile pattern is data-independent. If this assumption does not hold for certain types of video data (e.g., highly dynamic scenes), the efficiency gains might not translate, potentially limiting the method's applicability.
3. The use of only 0.1% of the pretraining data raises concerns about the generalization capabilities of the accelerated model. While performance loss is minimal on tested datasets, the model may underperform on unseen data or less common video scenarios.
4. While the paper uses VBench and FVD for evaluation, these metrics may not capture all aspects of video quality, such as temporal coherence in more complex scenes or perceptual quality under different conditions. Including additional metrics or user studies could provide a more comprehensive assessment. This is especially concerning combined with weakness #2, since FVD is commonly known as a weak metric that focuses strongly on independent frames rather than overall video coherence. Overall, the evaluation seems to favor more static videos rather than highly dynamic videos, and I suspect the attention pruning would encourage such results too. A metric that takes motion into account is Content-Debiased FVD [1], but ideally, this is more suitable via a user study (even though I do not think this is necessary for the rebuttal stage, but better prepare it for another iteration of the paper).
5. Inherit my point in #2 and #4, the paper does not provide any video data, making it challenging to assess the actual quality of the generated contents. From my point of view, a VDM paper should always be accompanied with as many videos as possible within the supplemental material size limit. Again, a good set would be the demo videos on OpenSORA's websites. They provided a wide range of descriptions and all the corresponding text prompts --- supposedly those prompts would work well on OpenSORA.

[1] Ge et al., On the Content Bias in Fréchet Video Distance, in CVPR 2024.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposed an efficient method for DiT based text-to-video generation. They found a unique pattern in the attention map of DiT based video generation diffusion models and proposed a method to exploit this pattern to ignore the computation of attention between many query/key pairs and hence speed up the generation.

### Strengths
- The finding (attention tile) is quite interesting and could be useful for future research in the community in this area.
 - the proposed layer-wise optimal search for sparse attention masks is somewhere novel in the paper.

### Weaknesses
- This work over-claimed the contribution of the proposed method. Actually, the efficiency improvement is mostly coming from MLCD, which is proposed by another work. The real improvement from the main finding or the proposed 'new' method in this paper is much less than MLCD.
 - Experiment is not thorough. This paper only experimented their method on one DiT based text-to-video generation model.
 - Comparison with other methods is missing. This paper only compared the results from different hyper parameters of the proposed method. Many existing methods that accelerate diffusion models are missing in the paper.
 - The larger diagonal attention is not something new or surprising as the each query token is computing the `correlation` with itself.

### Questions
please refer to the weakness section

### Soundness
2

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
4

### Summary
The authors propose a framework to speed up video generation using Video Diffusion Transformers by optimizing attention computation and reducing sampling steps. A repetitive attention tile pattern in 3D attention maps is identified which allows for sparse attention that lowers complexity. The framework uses a three-stage training pipeline: multi-step consistency distillation to reduce sampling steps, a layer-wise search for optimal sparse attention masks, and knowledge distillation to retain performance. This approach claims to achieve up to a 7.8× speedup in video generation with minimal quality loss.

### Strengths
The paper is well-written.

The computational complexity of video diffusion models presents a significant challenge, and the authors effectively highlight this issue and provide a good motivation for addressing it.

To tackle this, the solution provided by the authors of using a sparse attention map is interesting. Although thinking in this direction is not new, the way the authors motivate the solution and compute the attention maps is scientifically sound and has some novelty.

The computational speed-up achieved by the method looks impressive.

### Weaknesses
In the video generation literature, there are models that generate frames sequentially or follow an auto-regressive approach [1,2]. These models may be less computationally expensive than those using full 3D attention heads, yet there is no empirical or theoretical comparison with such models in the paper.

There should be an ablation study with the separate effects of sparse attention (without the MLCD) to understand each component in more detail.

The sampling distillation stage (Stage 1) is not really new, either technically or conceptually. There has been a line of work that provides a similar methodology [3,4], etc. It is not clear how different the proposed distillation is from the existing literature. The same can be said for the knowledge distillation in the final stage (Stage 3).

The paper has only two qualitative video generation results (or at least what I have found), of which only four frames are shown. There should be a lot more generated videos shown side by side to compare the method qualitatively.

[1] Diffusion forcing: Next-token prediction meets full-sequence diffusion. Chen et al. 2024.

[2] Diffusion models are real-time game engines. Valevski et al. 2024.

[3] MLCM: Multistep Consistency Distillation of Latent Diffusion Model. Xie et al. 2024.

[4] SCott: Accelerating Diffusion Models with Stochastic Consistency Distillation. Liu et al. 2024.

### Questions
What happens if the stages are switched, i.e., first obtain T_{sparse}, then T_{MCM}​ from T_{sparse}, and finally apply the knowledge distillation step?

Table 4 needs additional quantitative metrics like aesthetic quality, subject consistency, imaging quality, and FVD to provide a complete understanding of the effect of parallelization.

When comparing speed-up performance for parallelization, are the baseline models also trained with parallelization (Table 4)?

How does the proposed model achieve a lower FVD (Table 5) than the main base model, given that the proposed model is ultimately a distilled version of the main model?

How is the claim (lines 424 to 430) that model performance is within 1% of the base model accurate? It is evident that the numbers for imaging quality and subject class are significantly lower than those of the base model.

Ablation studies in Table 6 show that only MLCD can speed up the process by 5 to 8 times compared to the base model without significantly compromising quality. What is the justification, then, for the need for sparse attention maps on top of that?

It seems the main contribution is the sparse attention part. However, some doubts remain. Therefore, I can increase my rating if my questions and concerns in the weakness section and questions section are answered satisfactorily.

### Soundness
3

### Presentation
3

### Contribution
2
