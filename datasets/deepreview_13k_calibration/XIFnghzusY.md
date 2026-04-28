# OccSora: 4D Occupancy Generation Models as World Simulators for Autonomous Driving

- Decision: Reject
- Avg Score: 5.40
- Scores: 5, 6, 5, 6, 5

## Abstract
Understanding the evolution of 3D scenes is important for effective autonomous driving.
While conventional methods model scene development with the motion of individual instances, world models emerge as a generative framework to describe the general scene dynamics.
However, most existing methods adopt an autoregressive framework to perform next-token prediction, which suffer from inefficiency in modeling long-term temporal evolutions.
To address this, we propose a diffusion-based 4D occupancy generation model, OccSora, to simulate the development of the 3D world for autonomous driving.
We employ a 4D scene tokenizer to obtain compact discrete spatial-temporal representations for 4D occupancy input and achieve high-quality reconstruction for long-sequence occupancy videos.
We then learn a diffusion transformer on the spatial-temporal representations and generate 4D occupancy conditioned on a trajectory prompt. 
We conduct extensive experiments on the widely used nuScenes dataset with Occ3D occupancy annotations.
OccSora can generate 16s-videos with authentic 3D layout and temporal consistency, demonstrating its ability to understand the spatial and temporal distributions of driving scenes.
With trajectory-aware 4D generation, OccSora has the potential to serve as a world simulator for the decision-making of autonomous driving.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a 4D occupancy generation model called OccSora, designed to simulate the evolution of environments in autonomous driving scenarios. It proposes a 4D scene encoder to produce a compact spatiotemporal representation and uses a diffusion model to generate 4D occupancy sequences based on given trajectory prompts. OccSora addresses the inefficiency of existing autoregressive models in long-term temporal simulation, providing more physically consistent simulation support for decision-making in autonomous driving through trajectory-aware 4D generation. OccSora achieves good results on nuScenes dataset.

### Strengths
1.The paper is well written and organized. It’s easy to understand.
2.The authors provide abundant visualization results to show the effectiveness.

### Weaknesses
1. The novelty is limited. Using diffusion to generate occupancy is widely studied. And the contribution seems incremental compared to previous works in the field of occupancy prediction.
2.  It might be beneficial to conduct experiments on additional datasets, such as Waymo, to enhance the persuasiveness of the paper. 
3. The text in Figure 3 is too small and unclear.

### Questions
See the weaknesses above

### Soundness
3

### Presentation
3

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
This paper introduces OccSora, a diffusion-based model for 4D occupancy generation in autonomous driving. Using a 4D scene tokenizer, OccSora captures compact and discrete spatiotemporal representations, allowing for the high-quality reconstruction of long-sequence occupancy videos. A diffusion transformer is subsequently trained on these representations to generate 4D occupancy, conditioned on a trajectory prompt. Experimental results on the nuScenes dataset with Occ3D occupancy annotations show that OccSora can produce 16-second videos with realistic 3D layouts and temporal coherence, demonstrating its understanding of spatial and temporal patterns in driving scenes. This method shows potential as a world simulator for decision-making in autonomous driving, addressing the inefficiencies in modeling long-term temporal evolution found in autoregressive approaches.

### Strengths
This paper presents OccSora, a pioneering diffusion-based 4D occupancy generation model that utilizes a 4D scene tokenizer to capture compact spatiotemporal representations, improving the modeling of long-term temporal dynamics in autonomous driving. The research is comprehensive, featuring extensive experiments on the nuScenes dataset that showcase OccSora's ability to generate realistic 16-second videos with stable 3D layouts.  The paper is clearly structured and well-written, offering thorough explanations of the model architecture, training procedure, and evaluation metrics. OccSora’s capability to generate trajectory-aware 4D occupancy scenes makes it a valuable asset for decision-making in autonomous driving, with the potential to enhance safety and efficiency.

### Weaknesses
The writing of this paper should be enhanced. For example,

1）Some details in the methods section (Section 3) could be presented with greater clarity. For ‘Category embedding and Tokenizer’, occupancy is represented by Rin in the text, while in Figure 3, occupancy is represented by Ro.

2）If Figures 2, Figure 3 and Figure 4 contain elements corresponding to Rin, Rmi, Ro, and Rtr, please ensure these are labeled directly within the figures.

3）Please clearly indicate the dimensional changes between features within the figure to enhance reader comprehension.

### Questions
Refer to Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces a trajectory-aware 4D occupancy generation model capable of understanding ego car trajectories and enabling trajectory-controllable scene generation.

### Strengths
This paper proposes a trajectory-aware 4D occupancy generation model, which can comprehend the trajectories of ego car and realize trajectory-controllable scene generation. The model uses a 4D scene tokenizer to create compact, discrete spatial-temporal representations of 4D occupancy inputs, achieving high-quality reconstructions for long-sequence occupancy videos. The proposed OccSora can generate long-term occupancy videos up to 16 seconds.

### Weaknesses
1. This paper claims in the abstract and introduction that existing autoregressive methods "suffer from inefficiency to model long-term temporal evolutions". It is unclear how the authors address this, as the multiple denoising steps of the diffusion model can also be time-consuming. I suggest that the authors provide some **evidences to demonstrate that the proposed architecture is more efficient**, such as runtime comparisons or theoretical complexity analyses between the proposed approach and existing autoregressive methods.
2. The experiment on the 4D occupancy prediction is not convincing. The metrics indicate that OccSora significantly outperforms OccWorld; however, the **generation quality** in qualitative results is not good enough. It is beneficial to provide side-by-side visual comparisons between OccSora and baseline methods, highlighting specific areas where the generation quality differs.
3. It is unclear **how 4D occupancy prediction is conducted** in Fig. 5 and Tab. 10, as there appears to be no frame condition in the proposed architecture. I suggest that the authors provide a more detailed explanation of how the model handles frame conditioning for 4D occupancy prediction in the proposed architecture.
4. As shown in Fig.12, the model can generate different scenes with different motion conditions. However, their first frames are different. As far as the reviewer knows, if the authors want to **claim the model is controllable**, the model should be able to generate different future predictions with the same initial frame(s) using different trajectories. I recommend that the authors provide additional experiments or qualitative results to demonstrate this .
5. Why are the IoU and mIoU values at 0s in Table 5 different from the reconstruction results in Table 1? Both seem to measure reconstruction performance.

### Questions
The reviewer has identified five major concerns and would like the authors' responses to these points. Please answer each concern in the rebuttal stage. The reviewer will respond according to the authors' rebuttal in the discussion phase.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes OccSora, a diffusion-based 4D occupancy generation model designed for autonomous driving. It utilizes a 4D scene tokenizer to get spatial-temporal representations, allowing for high-quality reconstruction of long-term occupancy videos. The model generates 4D occupancy data based on trajectory prompts, generating videos with 3D layouts and temporal consistency. Experiments demonstrate OccSora's potential as a world simulator for autonomous driving.

### Strengths
1. This paper is well-organized, presenting a clear flow making it easy to read.
2. This paper proposes a generative 4D occupancy world model designed for autonomous driving, along with a novel generation task for occupancy data.
3. The experiments provide an evaluation of the model's capabilities and performance across various scenarios.

### Weaknesses
1. The quality of the turning cases shown in Figure 8 and Figure 13 appears to be quite poor. The motion trend is barely visible, and the scene structure beside the road becomes corrupted in the later frames. This undermines the claim of trajectory awareness. I suspect this issue is related to the imbalanced data distribution in the nuScenes dataset, which could present an interesting challenge. Unfortunately, the paper offers no further analysis or solution regarding this problem.

2. The authors spent a lot of space discussing the diffusion transformer (lines 269–290). However, much of this appears to replicate the contribution of the original DIT paper. This section could be shortened or moved to a preliminary section instead.

3. The mathematical notation throughout the paper is quite disorganized. Some of the symbols are unusual, and the authors should consider using more standard notation (e.g., what is "mi" in $ R_{mi} $?). The excessive use of superscripts and subscripts makes it difficult to follow. Additionally, the authors should avoid using unnecessary symbols for unimportant variables (e.g., $ x $ in line 246). There are also several instances of misused symbols. For example:
  1. The symbol $ N $ is used multiple times for different meanings, such as a label (line 176), nearest code operation (line 205), and Gaussian noise (line 271).
  2. In line 254, the positional encoding notation is inconsistent with Equation (2).
  3. In Equation (3), the $ t $ in $ v(t) $ should represent the diffusion timestep, but it is confused with the occupancy timestep $ t $.
  4. In line 265, $ v $ is referred to as the waypoint timestep embedding, but it is suddenly called the denoising timestep in line 269.

4. There are several grammar issues and typos:
  1. In line 181, "represents" should be "representing."
  2. In line 197, "model ability" should be "model's ability."
  3. In line 253, "model understanding" should be "model's understanding."
  4. In line 266, it should read: " $ g $ is then embedded into the input sequence ..."
  5. In line 280, "occuancy" should be "occupancy."
  6. In line 525, "reprort" should be "report."

### Questions
1. In Table 2, it's unclear why increasing the resolution (from $ 128 \times 4 \times 25 \times 25 $ to $ 128 \times 8 \times 50 \times 50 $) improves the reconstruction IoU and mIoU, but results in a decrease in generation FID. This discrepancy needs further explanation.
2. The figures showing occupancy data throughout the paper are quite small, and the resolution is low, making it difficult to see details. The authors should consider placing fewer samples in each row and enlarging the figures for better visibility.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces **OccSora**, a 4D occupancy generation model designed to capture the evolution of 3D scenes. Notably, it is **the first generative 4D occupancy world model for autonomous driving**. The model employs a 4D scene tokenizer to create compact spatiotemporal representations from 4D occupancy inputs, facilitating the high-quality reconstruction of long-sequence occupancy videos. Additionally, OccSora incorporates a diffusion transformer to generate 4D occupancy conditioned on trajectory prompts. Extensive experiments on the nuScenes dataset demonstrate OccSora's ability to generate 16-second videos with realistic 3D layouts and temporal consistency, highlighting its capacity to comprehend dynamic driving scenes. As a result, OccSora holds promise as a simulation tool for autonomous driving decision-making.

### Strengths
1. The paper is well-organized, making it easy to follow.
2. This paper introduces the first generative 4D occupancy world model for autonomous driving and proposes a new generation task for occupancy data, which is a contribution to the community.
3. The design of the 4D tokenizer (Section 3.2) is particularly novel. The experiments demonstrate its effectiveness in preserving 3D occupancy geometry with temporal consistency, even under high compression rates.
4. The ablation study is thorough and comprehensive.

### Weaknesses
1. I don't see the necessity of using quantizers and a codebook in the tokenizer (line 200). Since the authors employ a diffusion-based model, typically paired with a continuous compression model (e.g., VAE), this differs from the auto-regressive models (e.g., OccWorld) where such techniques might be more fitting. Could the author clarify their reasoning or provide supporting empirical results? Specifically, the benefit of discrete latent space for a diffusion model is not clear, and the added complexity of training a codebook seems unnecessary when a VAE could provide a continuous latent space more naturally suited for diffusion.
2. The idea of compressing the latent spatiotemporal dimensions together is interesting. However, in the diffusion model, simply flattening the tokens results in temporal modeling inefficient. Why not adopt an additional temporal layer, as is common in video-based diffusion models? Some references that might be helpful include:
  - Align Your Latents: High-Resolution Video Synthesis with Latent Diffusion Models
  - Scaling Latent Video Diffusion Models to Large Datasets
  - VDT: General-purpose Video Diffusion Transformers via Mask Modeling
  - Latte: Latent Diffusion Transformer for Video Generation
 The lack of explicit temporal modeling within the diffusion process is a significant concern, as it could limit the model's ability to capture complex temporal dynamics present in the 4D occupancy data. The current approach seems to treat the temporal dimension as just another spatial dimension, which is unlikely to be optimal.
3. The generation metric is not described in sufficient detail. Firstly, FID is designed to evaluate images, yet this paper generates occupancy videos. At the very least, the authors should consider using FVD. Additionally, no details or references explain how FID is adapted for occupancy data or how occupancy features are extracted from pre-trained networks, given that this is the first work to generate 4D occupancy. The absence of a clear explanation of how FID is applied to 4D occupancy data raises serious questions about the validity of the reported results. It is unclear what features are being compared and how this relates to the quality of the generated occupancy videos.
4. I am confused by the two experimental setups in Section 4.3. For the "Trajectory Video Generation" experiment (line 406), I expected to see how the generation would vary with different trajectory inputs. However, Figure 7 presents three entirely different scenes, even in the first frame. In the "Scene Video Generation" experiment (line 413), the authors claim they use the same trajectory for each motion case (line 417), but what causes the differences in the left and right parts of Figure 8? Is it the random seed or the input latents? The inference process is not explained at all. The lack of clarity regarding the experimental setup and the role of trajectory inputs makes it difficult to interpret the results. The authors need to provide a more detailed description of the inference process and how different inputs affect the generated scenes.
5. I have concerns about the 4D occupancy prediction experiment described in line 484. The task is to forecast future frames based on historical frames. However, the authors use a 3D encoder with no masking strategy, which means the encoder can "see" the future frames, making the prediction task unfair. This could be proved by the results in Table 8 of the appendix, where the reconstruction IoU is higher for the 1-9s but lower at 0s, since there is no historical information for the 0s frame. Furthermore, the paper only demonstrates the process starting from pure noise. How is historical occupancy input into the DIT model? The use of a 3D encoder without masking for a temporal prediction task is a major flaw. The encoder should only have access to past information, and the current setup introduces a significant information leak, invalidating the results of the prediction task.

### Questions
1. **The main text of the paper exceeds the maximum page limit of 10 pages**, as per the ICLR 2025 guidelines. Please check the details at ICLR Call for Papers.
2. The authors should consider using `\citep{}` in the paper for better formatting. Refer to the ICLR LaTeX template for the appropriate usage and differences between citation commands.
3. In the caption of Table 1, the output dimension for the "512x" setting should be listed as $ 25 \times 25 \times 4 $.
4. In Figure 6, the model name should be updated to **OccSora-base**.

### Soundness
3

### Presentation
1

### Contribution
3
