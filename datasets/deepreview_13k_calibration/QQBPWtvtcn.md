# LVSM: A Large View Synthesis Model with Minimal 3D Inductive Bias

- Decision: Accept
- Avg Score: 7.67
- Scores: 8, 8, 6, 8, 8, 8

## Abstract
We propose the Large View Synthesis Model (LVSM), a novel transformer-based approach for scalable and generalizable novel view synthesis from sparse-view inputs. We introduce two architectures: (1) an encoder-decoder LVSM, which encodes input image tokens into a fixed number of 1D latent tokens, functioning as a fully learned scene representation, and decodes novel-view images from them; and (2) a decoder-only LVSM, which directly maps input images to novel-view outputs, completely eliminating intermediate scene representations. Both models bypass the 3D inductive biases used in previous methods---from 3D representations (e.g., NeRF, 3DGS) to network designs (e.g., epipolar projections, plane sweeps)---addressing novel view synthesis with a fully data-driven approach. 
While the encoder-decoder model offers faster inference due to its independent latent representation, the decoder-only LVSM achieves superior quality, scalability, and zero-shot generalization, outperforming previous state-of-the-art methods by 1.5 to 3.5 dB PSNR. Comprehensive evaluations across multiple datasets demonstrate that both LVSM variants achieve state-of-the-art novel view synthesis quality. Notably, our models surpass all previous methods even with reduced computational resources (1-2 GPUs). Please see our website for more details: \textcolor{red}{\tt\small\url{https://haian-jin.io/projects/LVSM/}}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work presented the Large View Synthesis Model (LVSM), which aims to achieve novel view synthesis (NVS) via a pure transformer architecture, bypassing the need for additional 3D inductive bias. In particular, LVSM explored an encoder-decoder model design and a decoder-only one, where the former is more efficient in inference with a more compact learned latent space, and the latter is more effective and scalable regarding visual quality. Experiments of object-level datasets and scene-level datasets demonstrate the superiority of the introduced LVSM.

### Strengths
* The idea of achieving high-quality photorealistic NVS with minimal 3D inductive bias is brave. It is also impressive that LVSM implements this brave idea with a straightforward yet effective pure Transformer-based architecture.
* Experiments on several benchmarks demonstrate the effectiveness of the introduced LVSM
* The paper is well structured, and it is easy to follow.

### Weaknesses
 * More discussion with Scene Representation Transformer (SRT) [Sajjadi et. al, CVPR 22]. LVSM seems to be a ‘reimplementation’ of SRT with more recent modules, which significantly limits the novelty of LVSM. The discussions in L141-L146 cannot convince me about the key contribution of LVSM. A more thorough analysis is suggested below.
  * The introduction should clearly reveal the similarities and differences between SRT and LVSM. The motivation (minimal 3D inductive bias) and architecture (encoder-decoder) of LVSM are similar to SRT, and it seems that the key difference is that LVSM adopts more advanced modules from LRM. Specifically, the tokenizer, the progressive compression of latent tokens, and the joint updating of latent and target patch tokens in the decoder need more detailed comparison with SRT's corresponding modules. It's not clear how these specific changes contribute to the performance gains over SRT.
  * Different observations of ‘decoder-only’ architecture between LVSM and SRT.  SRT also explores the ‘decoder-only’ designs (see Sec. 4.3 “No Encoder Transformer” in SRT), which shows that ‘decoder-only’ performs worse than its ‘encoder-decoder’ counterparts. This observation happens to be contradicted to that of LVSM. It would be interesting to provide further analysis about what leads to this different conclusion despite similar settings. The differences in decoder architecture, specifically the use of self-attention in LVSM versus cross-attention in SRT, should be highlighted and analyzed to explain the performance discrepancy.
  * More analysis is needed to understand why LVSM achieves good quality on NVS.  It is hard to understand why LVSM gets much cleaner images while SRT gets only blurry ones. Is it because LVSM is trained with more data? Besides, it would be beneficial to visualise the attention of LVSM (similar to Fig. 5 in SRT). The analysis should include a comparison of training data size and a visualization of attention maps to understand the model's focus during rendering.
  * Noisy poses or unknown poses settings on LVSM. SRT achieves reasonably good results when the camera poses are noisy or even unknown (Fig. 4 in SRT). How does LVSM perform under similar noisy pose or pose-free settings? The paper should include experiments or at least discussion on the robustness of LVSM to pose noise and its performance in pose-free settings.


* Assessing the geometrical accuracy. For the object-level data, it would be better to reconstruct the 3D mesh using the rendered novel views, similar to Fig. 5 in latentSplat [Wewer et al., ECCV 24]. For the scene-level data, e.g., the single-view case in Fig. 1, it would be better to show the error map between the rendered and ground truth views (similar to Fig.6 in MVSplat [Chen et al. ECCV 24]), which makes it easier to understand how well the rendered views align with the given camera poses.


* Performance on more complex datasets. L527 claims that LVSM is not simply doing view interpolation. Since the results are mainly shown on simple data, e.g., RealEstate10K with zoom-in / zoom-out trajectories, it cannot justify this claim. It would be better to show some results on more complex datasets, e.g., MipNeRF360, Tanks and Temples.

### Questions
Kindly refer to [Weaknesses]

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces two view synthesis models: one with an encoder-decoder architecture and another with a decoder-only design. Both models treat view synthesis as a predictive sequence-to-sequence task, using Plucker embeddings for camera position encoding. Without relying on intermediate 3D structures, the models achieve impressive results across object-level and scene-level view synthesis.

### Strengths
The paper is well-motivated and and very well-written, though certain technical details could benefit from additional clarity (outlined below). The visual results are striking, as shown on the authors’ website, and I appreciate the authors provide additional results with limited GPU-hours, making reproduction more feasible for academic labs. Overall, this work is a valuable contribution to view synthesis research.

### Weaknesses
1. Related Works. While the paper covers key prior work on 3D representation and few-shot view synthesis, it would benefit from a discussion of generative multi-view methods, especially recent works like Free3D (CVPR 2024, also uses Plucker embedding to encode camera poses) and EscherNet (CVPR 2024, also can be inferenced with varying number of reference/target views). These methods also do not rely on intermediate 3D representations, treating view synthesis as a sequence-to-sequence problem. Adding some proper discussions on how the proposed methods differ from these could provide valuable context for readers, and strength the community focussing on sequence-to-sequence learning type view synthesis.

2. Architecture Design Details.
- Encoder-Decoder Architecture: Could the authors clarify the choice of compressing input tokens into a fixed-length representation with latent tokens? What are the benefits over using uncompressed reference tokens (only with linear complexity)?
- Decoder-Only Architecture: Are attention masks fully bi-directional? It would be interesting to see if introducing asymmetric masking strategies (e.g., limiting specific views to certain tokens) could enhance generalization to different numbers of reference views. Additionally, if attention is fully bi-directional, the distinction between reference and target views seems blurred, as the loss can be computed from all views, (conditioned on all other views)?

3. Experiments

- Unified Model Training: Could the model be trained jointly on both object- and scene-level data instead of using separate models? Demonstrating this capability would advance the model’s utility toward a more general-purpose view synthesis framework.
- Varying Reference Images: The authors suggest the model performs well with varying numbers of reference images. To strengthen this claim, I recommend evaluating on a NeRF-Synthetic dataset instead of GSO in Fig. 5 (similarly as shown in EscherNet), which includes more complex objects in terms of textures and lighting. This would also enable clearer comparisons to other state-of-the-art, scene-specific methods like InstantNGP and 3D Gaussian Splatting that leverage 3D representations.
- Single-Image View Synthesis: Single-image view synthesis is a common use case, so it would be valuable to include a comparison to methods specifically designed for single-image scenarios to showcase the model’s adaptability and strong generalization.
- Plucker Embedding Generalization: Could the authors explore how well the Plucker embeddings generalize to different spatial coordinates? For instance, in scene-level experiments, would generation quality remain consistent if reference/target camera poses are applied with the same camera transformation, such as a 30-degree elevation or a 1-meter translation?

4. Limitations
A dedicated limitations section would help readers identify areas for improvement. Potential limitations include:

- Predictive Modeling: The predictive approach in LVSM may restrict outputs to interpolation, limiting extrapolation capabilities, especially in scene-level tasks (as shown in the website). Maybe a generative model variant trained on larger datasets address this? Can the authors provide some extrapolation results?
- Extreme Reference View Limits: How well does LVSM handle extremes in reference view numbers (e.g., only one view or over 100 views)? This could be an insightful addition, especially if single-view predictions are inconsistent or if performance degrades with many reference views.

### Questions
See limitations.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper studies the task of synthesizing novel views from a set of views without explicit 3D representation.
The key idea is to use a transformer architecture to bypass the 3D inductive biases.
To achieve this goal, an encoder-decoder and a decoder-only architectures are proposed to conditional on image and camera pose for novel view synthesis. 
Experiments are trained on object-level Objaverse dataset, and scene-level RealEstate10K dataset, and tested on object-level Google Scanned Objects and Amazon Berkeley Objects and scene-level RealEstate10K dataset.
They demonstrate reasonable results on novel view synthesis, outperforming the existing state-of-the-art approaches.

### Strengths
### S1 -- Good results on an interesting task
- The task of synthesizing novel views from a set of input views is interesting and very challenging. The proposed method seems to work well on both object-level dataset and scene-level dataset.
- Base on the visual results shown in Figure 3 and 4, the proposed deterministic pipeline also can imagine the new content which is invisible from the input views.

### S2 -- Simple ideas and careful implementations
- There are two main transformer-based architectures. 
    - One is an encoder-decoder architecture, which used the transformer encoder to encode all input views into latent space, and then use a query camera pose to get the target view images. This architecture is very similar to SRT, except here the encoder is transformer architecture.
    - The second idea is to design a decoder-only architecture. This reduces the necessary of the one representation from the encoder.
- These two ideas are carefully implemented and validated through ablation studies. In particular, the decoder-only architecture seems quite effective in achieving a set of input views, from 1-10.

### S3 -- Good writing
- The paper is very well written, with clear motivations, sufficient technical explanations and illustrative visualization.

### Weaknesses
### W1 --- Significant is not well demonstrated
- The proposed idea is a very specific, minor change to SRT -- basically using a slightly different transformer encoder or decoder to replace the original CNN. Fundamentally, I am not fully convinced that it is even crucial to use only transformer architecture than the CNN-based feature extraction and then do the transform.
- This small change seems to lead to a large improvement on both object-level and scene-level datasets. However, if we train the original SRT on the same dataset with the same computational GPUs, what's the performance? 
- A fair comparison to the highly related work (SRT) should be provided. The discussion in L140-145 is also not a very strong claim. 
- The decoder-only architecture is very interesting and useful, but some related work like 3DIM, Free3D, CAT3D also used it in the diffusion for a set of views with the Plücker Rays embedding as conditional. Why this architecture is better than these difussion-based methods, which also used the transformer in pixel or latent space?

### W2 --- More results should have been expected
- I expected more visual results on scene-level cross-domain datasets. Figure 4 shows only result on RelEstate10k, which is a relative easy dataset. How about the performance on the scene-level datasets, such as DL3DV, Mip-NeRF 360, or other traditional NeRF Datasets?
- This deterministic model can also provide sharp results for invisible regions, which is quite interesting. However, the authors only highlight them in the object-level results, how about the scene-level results? 
- Does the scene-level model perform good for the extrapolation, instead of interpolation?
- In 3DIM, Free3D, SV3D, CAT3D, they used some temporal attention to ensure the consistency of generated images. How do the authors active the 3D consistency in the design? Besides, the multi-view rendered results as in 3DIM and Free3D or reconstructed 3D as in SV3D and CAT3D will make the paper stronger to show 3D consistency and structure, while they want to bypass the 3D representation.
- It will be helpful to provide some visual examples of the failure cases.
- The ablations studies are only related to the different layers of the transformer, and the attention architecture. If the authors argue the large contribution of transformer compared to CNN, a fair ablation should be made to use SRT-related architecture under the same experimental settings.


### Questions
- Why this simple architecture performs so good compared to SRT? What's the key contribution, only transformer vs. CNN? 
- What's the performance on other scene-level datasets?
- How about the 3D consistency?
- The decoder-only transformer also be used for CAT3D, while they are in latent space for diffusion. If we train the similar architecture, but on diffusion-based architecture, what's the performance? In particular, could we use it to build a large foundational 3D model upon the pre-trained 2D diffusion models? The model not only works well on a special trained dataset, but can be generalised well to arbitrary images.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose to train a generalizable novel view synthesis model with minimal 3D inductive biases, training on posed multi-view data to map images and camera rays to novel views, with target rays as queries.  This is supervised by a simple photometric and perceptual novel view loss.  
The architecture uses ViT-like image tokenization to embed images and corresponding Plucker rays, and the target views are decoded by Plucker ray queries.  Two Transformer architectures are considered – decoder-only, and encoder-decoder.
These are compared to prior work, and differences in performance between the two choices are compared and contrasted.

### Strengths
The model variants introduced compare well to prior work; the large improvements compared to baselines for the decoder-only variant are impressive.  The investigation of both encoder-decoder and decoder-only as modeling choices (with the discussed tradeoffs) is also interesting and seems novel.  The discussion of the effects of compute (model size, compute available) on performance, while disorganized, is quite interesting.

### Weaknesses
There is limited novelty in the approach of removing handcrafted 3D representations – as the authors point out this was done in SRT [1], with a less effective and scalable architecture, as well as in the stereo case [2], which proposes a similar philosophy of input-level inductive biases, and in the multi-view case [3], where the view synthesis branch closely resembles LVSM.  Clarification of the novel elements of this architecture compared to prior work would be great, beyond the discussion of encoder-decoder vs decoder-only.

The presentation is somewhat messy.  The discussion of encoder vs encoder-decover in Section 3.2 takes up a lot of room, but much of it is standard Transformer information; this could be condensed to describe specifically how these concepts relate to the architecture rather than be a general introduction.  Also, there is information about model scale and compute scattered throughout the document, and the model sizes are not in terms of #params but layers.

### Questions
Suggestions - clarifying the scaling (model size, compute) discussion (with model parameter counts), and comparison to prior work.
Also if possible it would be good to have the encoder-decoder vs decoder-only comparisons for both scene- and object-level (i.e. Table 2).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a novel transformer-based approach for scalable and generalizable novel view synthesis from sparse-view inputs. Two models are proposed. both of which bypass the 3D inductive biases used in previous methods and address novel view synthesis with a fully data-driven approach. Comprehensive evaluations across multiple datasets demonstrate that the work achieve state-of-the-art novel view synthesis quality.

### Strengths
1. this paper minimizes 3D inductive biases for scalable and generalizable novel view synthesis;
2. Two LVSM architectures—encoder-decoder and decoder-only—are designed to minimize 3D inductive biases;
3. Both of the two models achieve impressive sparse novel view synthesis performance. 
4. The impressive result might provide a potential new representation for generalizable NVS task.

### Weaknesses
The architecture level is not well explained and might cause a bit confusing, I will elaborate it in questions part.

### Questions
The architecture of decoder model is elaborated from L303-308, the attention layer in the transformer block seems to be self-attention. During both training and inference stage, I wonder how many input and target views are used for each batch sample, will the self-attention between target views affect the result? If I want to get the target view at P1 and P2, will inferencing them at the same feedforward pass be different from inferencing one by one?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes LVSM, a general novel view synthesis (NVS) model for sparse-view inputs. It aims to improve the quality, efficiency, and scalability of NVS by minimizing 3D inductive bias. Different from previous works, LVSM directly utilizes transformer-based backbone to synthesize novel views without intermediate 3D representations and corresponding rendering equations. The author(s) introduce two versions of LVSM. The first model, encoder-decoder LVSM, encodes inputs into a scene representation token and decodes it into novel views. The second model, decoder-only LVSM, further removes the need for intermediate representation by adopting a single-stream transformer. Both models patchify the posed input view and use Plucker ray embeddings to tokenize the target view. Experiments show that LVSM trained on 2-4 input views has generalizability to an unseen number of views, and it outperforms the SOTA GS-LRM by 1.5 to 3.5dB PSNR.

### Strengths
1.	The proposed models achieve impressive reconstruction results in terms of PSNR, SSIM, LPIPS, and qualitative evaluation.
2.	The proposed models can be trained with a single A100 80G GPU. In contrast, existing general reconstruction models, like LRM, LGM, and GS-LRM, usually require a large number of computational resources.
3.	The proposed model is generalizable to an unseen number of input views, from single view to more than 10 views.
4.	Ablation studies show the scalability of LVSM, where transformers with more layers generally perform better in terms of the quantitative reconstruction results.

### Weaknesses
1.	The qualitative results are not consistent with the quantitative results. In specific, Table 1 shows that the encoder-decoder LVSM achieves similar quantitative results as GS-LRM, and sometimes worse in object-level datasets. However, Figure 3 and Figure 7 substantially outperform GS-LRM. I am worried about potential cherry picks in the qualitative results. It will help evaluation by showing more examples as well as some failure cases of LVSM.
2.	Missing experiments for efficiency comparison. Specifically, the paper claims the higher efficiency of LVSM than previous methods, while there is no comparison between LVSM and other NVS models.
3.	Generalizable models are proposed to increase the efficiency of novel view synthesis and 3D reconstruction. In the 075 line, the author(s) also mentions how they contribute to a scalable and efficient novel view synthesis model. However, I cannot see an obvious motivation about removing 3D inductive bias, if the model increases much computational complexity with comparison to other reconstruction-based large models, e.g. LRM, GS-LRM. Specifically, I'm asking what the largest advantage of removing 3D inductive bias is. This includes but is not limited to:
    - Is LVSM easier to be trained than GS-LRM? (more stable or faster)
    - Does LVSM supports faster rendering than other LRMs?
If the efficiency is not you major claim, it's better to fix the over-claim in 075 line. Also, how much speed sacrifice is needed, compared to reconstruction-based generalizable models? Does LVSM still support real-time rendering?

### Questions
1.	It is commonly believed that 3D reconstruction improves view consistency for novel view synthesis. By removing 3D inductive bias, how does LVSM ensure consistency across novel views? Is this knowledge simply learned using attention mechanism? To demonstrate view consistency, you may want to provide some 3D-aware metrices for comparison, such as reprojection error or depth estimation, which will help my evaluation a lot.
2.	Could you please provide a more detailed diagram for the LVSM architecture? Specifically, such a diagram will help readers understand the methodology more easily. In the submission, only Figure 2 is available with very brief design.
3.	Refer to weakness.
4. Will you release your codes and pretrained models after possible acceptance?

### Soundness
4

### Presentation
3

### Contribution
3
