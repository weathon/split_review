# Single Motion Diffusion

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Synthesizing realistic animations of humans, animals, and even imaginary creatures, has long been a goal for artists and computer graphics professionals. 
Compared to the imaging domain, which is rich with large available datasets, the number of data instances for the motion domain is limited, particularly for the animation of animals and exotic creatures (\eg, dragons), which have unique skeletons and motion patterns.
In this work, we present a Single Motion Diffusion Model, dubbed \algoname{}, a model designed to 
learn the internal motifs of a single motion sequence with arbitrary topology and synthesize motions of arbitrary length that are faithful to them.
We harness the power of diffusion models and present a denoising network explicitly designed for the task of learning from a single input motion. 
\algoname{} is designed to be a lightweight architecture, which avoids overfitting by using a shallow network with local attention layers that narrow the receptive field and encourage motion diversity.
\algoname{} can be applied in various contexts, including spatial and temporal in-betweening, motion expansion, style transfer, and crowd animation. 
Our results show that \algoname{} outperforms existing methods both in quality and time-space efficiency.
Moreover, while current approaches require additional training for different applications, our work facilitates these applications at inference time.
Our code and trained models \ifanonymous{will be made available.}\else{are available at \url{https://sinmdm.io/SinMDM-page}.}\fi

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a motion diffusion model (SinMDM) that utilizes a QnA-based UNet architecture in the motion domain. The model incorporates QnA layers, which enable local attention with a temporally narrow receptive field, resulting in improved efficiency in space and time. The use of QnA layers allows for fast and efficient implementation, enhancing the model's performance compared to global attention layers. The paper validates the design choices through experiments and provides a comprehensive list of hyperparameters for reproducibility. The paper demonstrates various applications of single-motion learning using diffusion models. These applications include motion composition, motion harmonization, and straightforward use for long motion generation and crowd animation. The authors showcase the effectiveness of the proposed model in these applications, highlighting its ability to handle complex tasks like harmonization and style transfer.

### Strengths
The proposed method is the first work that applies diffusion to single motion learning. The paper is well-written and details are clearly presented. The methodology is well-designed in the way to reduce the range of receptive field to prevent acquiring global context and overfitting. The results in the paper and the supp video are of high quality. Applications are interesting and making use of the diffusion framework. The authors also presents a user study that demonstrates the superiority of the proposed model in terms of diversity, fidelity, and quality.

### Weaknesses
 - As restricted by the source of data, the results of some editing applications are somehow not that impressive. Similar results can be achieved by simple manipulations without resorting to a powerful diffusion model. E.g. the spatial composition looks no more than cutting-and-pasting the upper/lower body motion, and the style transfer application is like temporally synchronising the pace of the steps of the happy/crouched style video to the content.

- Although a solid work, most techniques used in the methodology are from existing papers, including diffusion for motion, and single motion generation, and the contribution to the community is limited.

### Questions
- Are there motion representations other than the adopted one from HumanML3D tested for the proposed method? How do you expect the motion representation could affect the generation performance?
 
- In what circumstances does the method fail?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces SinMDM, a Single Motion Diffusion Model based on the motivation that the number of data for the motion domain is limited. SinMDM learns from a single motion sequence, generating motions true to original motifs, while avoiding overfitting through a lightweight, attention-focused architecture (narrow respective field). It demonstrates various motion tasks, including spatial and temporal composition, as well as Harmonization (style transfer). SinMDM shows high efficiency and good performance.

### Strengths
1. The usage of the Diffusion model in the single-motion generation is interesting. 

2. Also, this paper demonstrates various interesting applications of motion synthesis with efficiency and good quality. 

3. In order to overcome overfitting and promote diversity, SinMDM proposes to use the shallow QnA module to limit the receptive field and relative temporal positional embeddings.

### Weaknesses
1. Single-motion generation task and using Diffusion to do single-instance generation is not new. Some concepts have been explored in previous papers. For example, Sinfusion[1] has pointed out that the receptive field needs to be reduced for single-instance generation task. The only difference is that they use ConvNext while SinMDM uses QnA module. 

2. Also, for the Harmonization, the way of using guidance injection is from ILVR [2]. 

Maybe, could you elaborate on this, and emphasize the contribution of this work?

### Questions
1. As the receptive field is narrowed, how to guarantee temporal smoothness? As shown in Table 3, using a wide receptive field gives better FID.   

2. Comparison with Ganimator in HumanML3D?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Paper introduces a generative diffusion model for motion synthesis. The model is a UNet that operates on motion data with a specialized efficient local attention layer (QnA) in place of global attention. The key intuition of this work is restricting the capacity (receptive field) of the underlying UNet to improve generalization and avoid mode collapse. Results are provided on several tasks, including motion composition, harmonization and generation, and seem to be state-of-the-art.

### Strengths
- Paper is well-written and is easy to follow. Supplementary material is of high quality.
- The key technical novelty - to reduce receptive field - is simple and is easy to implement, and makes sense in the limited data regime.
- Qualitatively results look impressive. User study and benchmarks also confirm performance of the method is state-of-the-art.

### Weaknesses
 - Authors propose a solution that fixes a specialized version of UNet (presumably similar to the one used for image generation) - by introducing local attention mechanism. I understand that it might be a way to repurpose an existing architecture developed for a different task, but it does seem like there are exist a wide range of existing architectures (1d convnets / wavenets), which exhibit the same property by construction. It is a bit unclear why is the vanilla UNet considered in the first place? Specifically, the paper lacks a clear justification for choosing a UNet architecture, which is inherently designed for spatial data, over architectures more naturally suited for sequential data like motion capture sequences. The use of a UNet, even with modifications, requires reshaping the 1D motion data into a 2D representation, which introduces an artificial spatial structure that might not be optimal for capturing the temporal dependencies inherent in motion data. This reshaping process and its potential impact on performance are not adequately discussed.
- (Novelty, minor): diffusion models have been used for motion synthesis, the QnA has been used before, although in different context.
Misc:
- afaik vanilla UNet [Ronneberger'2015] does not have attention layers, do you imply the unet similar to that used in stable diffusion implementation?

### Questions
- What exactly is meant by "single input UNet" in 4.? 
- Why is the UNet the default option here? Wouldn't LSTMs / WaveNet / TCNN would be a better option?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes "Single Motion Diffusion" to learn a generative model of skeletal motions from small training data. The key architectural ideas are 1. shallow U-Net and 2. QnA attention model for local receptive fields. The paper demonstrates applications in the temporal composition (temporal in-painting for in-betweening and motion expansion), spatial composition (spatial in-painting by constraining a part of the skeletal tree with an unseen motion), harmonization (mix low-frequency unseen motion during denoising), and style transfer using harmonization. The method is compared numerically against Ganimator [Li et al. 2022] and GenMM [Li et al. 2023] for the coverage (the rate of generated motions reproducing the input), global diversity, local diversity, inter-diversity, intra-diversity difference, and computational efficiency metrics (number of parameters and total running time). The method is also compared against MDM trained on a single clip and MDM trained on a cropped clip to simulate the narrow receptive field regarding SiFID, inter-diversity, and intra-diversity differences. The numerical evaluations are backed up by the user studies.

### Strengths
The core takeaway is reducing the temporal receptive field by tweaking existing architectures (reducing the U-Net depth and using the QnA transformer) allows the training of generative motion models with a very small amount of data. While the idea is simple, the technique shows promising results on important animation tasks.

Thorough numerical evaluations and user studies support the claim. The visual quality is also fine but with some caveats (see Weakness).

The technique is reproducible with the provided code, data, and pretrained models.

### Weaknesses
The flip side of the simplicity of the technique is that the technical novelty may not be so significant.

It seems like there is a trade-off to reducing the temporal receptive field. The generated results often show abrupt transitions, such as unnaturally fast turns. I believe this is due to the limited receptive field not seeing the full segment of some longer actions. Can authors discuss this? This may indicate that we need more metrics to measure the visual quality of motions.

### Questions
(Minor comment)
From the abstract:
> learn the internal motifs of a single motion sequence with arbitrary topology

I initially thought "arbitrary topology" meant cases like generating the dragon motions from the model trained on human skeletons. I now know that this just means that the architecture itself is agnostic to the skeletal structure but the trained model must be applied to the same skeletal structure. I hope there is a way to phrase this better to reduce the confusion.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
