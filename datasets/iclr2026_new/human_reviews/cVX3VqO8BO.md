## Human Reviewer 1

### Summary
This paper explores the use of multimodal large models for cross-embodiment dexterous manipulation. The main contributions are as follows:
1. Constructed a dexterous manipulation dataset encompassing multiple heterogeneous dexterous hands, based on human manipulation datasets.
2. Proposed a language-guided, multimodal large model-based framework for cross-embodiment dexterous manipulation.

### Strengths
1.	The proposed dataset features highly aligned grasp poses with semantic annotations for cross-embodiment manipulation, which is quite a contribution to the community.
2.	Proposes and validates a viable methodology for applying Multimodal Large Language Models (MLLMs) to the challenging problem of high-DoF dexterous manipulation generation.
3.	Achieving promising results in real-world deployment on high-DoF dexterous embodiments using only human demonstration videos, providing a positive signal for addressing the issue of expensive data collection.

### Weaknesses
1.	The selected tasks are relatively simple. On one hand, many demonstrated actions (e.g., opening a drawer) can be performed by simpler, lower-cost two-fingered grippers, failing to highlight the advantage of dexterous hands. On the other hand, the tasks designed for dexterous hands (e.g., picking and placing objects) involve overly simplistic semantics, lacking part-level manipulation or interactions with clear subsequent intent (e.g., "handing the scissor handles to the user" or "grasping the teapot lid", which are feasible in OakInk). We expect to see complex manipulation sequences that are hard to do for non-dexterous hands and feature richer semantic hierarchies.
2.	The evaluations in simulation are primarily analytical metrics. I believe success rates for the manipulations are essential.

### Questions
1.	In real-world deployment in open-world scenarios, high-fidelity 3D assets of the objects being manipulated are unavailable. Could this affect the performance of the physics-guided dynamic refinement?
2.	The experiments just include comparisons with several human motion generation models. What about the performance of language-guided Hand-Object Interaction models [1] or language-guided grasp models [2, 3] (which can extend to the setting of this paper) on the current dataset.

[1] Cha, Junuk, et al. "Text2hoi: Text-guided 3d motion generation for hand-object interaction." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.

[2] Wei, Yi-Lin, et al. "Grasp as you say: Language-guided dexterous grasp generation." Advances in Neural Information Processing Systems 37 (2024): 46881-46907.

[3] Zhong Y, Huang X, Li R, et al. Dexgraspvla: A vision-language-action framework towards general dexterous grasping[J]. arXiv preprint arXiv:2502.20900, 2025.

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 2

### Summary
The paper proposes a unified pipeline for language-conditioned, sequential dexterous-hand manipulation. The method comprises: (i) a Unified Dexterous-Hand Tokenizer (VQ-VAE) that maps heterogeneous hand morphologies into a shared discrete codebook and decodes back to hand-specific joint trajectories; (ii) a VLM-based generator that, given RGB-D input, an instruction, object point clouds, and tokenized history, autoregressively produces manipulation tokens; and (iii) a physics-guided dynamic refinement that enforces contact and temporal smoothness while adhering to the generator’s intent, yielding physically feasible, executable trajectories. Experiments on DexYCB and OakInk show consistent improvements over strong motion-generation baselines (TM2T, MDM, FlowMDM, MotionGPT3) and higher real-robot success rates; ablations demonstrate each module’s contribution.

### Strengths
The paper proposes a strong framework that incorporates a cross-dexterous-hand representation, language-conditioned sequence generation, and a physics-guided dynamic trajectory refinement module.

The authors perform extensive experiments across multiple datasets, covering both seen and unseen settings, with comprehensive evaluations and ablations.

### Weaknesses
Tokenizer evaluation limited to a single hand. Although a unified dexterous-hand tokenizer is proposed, both the HOI and real-world experiments appear to use only one hand type. A broader evaluation across multiple robot hands would more convincingly validate the tokenizer’s generality and cross-hand transfer.

Underspecified sequence-generation metrics. The paper introduces a manipulation sequence generator, but the evaluation protocol for sequences is insufficiently detailed. Please clearly define the quantitative metrics and how they are computed.

Missing text–motion alignment evaluation. Given the language-conditioned setup, include explicit Text–Motion Alignment assessments is necessary. Please provide both quantitative measures and qualitative analyses (e.g., human judgments of instruction adherence).

Minor issues.

Line 075: “Language -guided” → “Language-guided”.

Line 115: missing space before “introduces”.

Line 377: only five metrics are listed

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 3

### Summary
In this work, the authors propose a novel framework for manipulation that generalizes across different dexterous-hand morphologies. Furthermore, the proposed method can generalize over unseen objects. The method consists of three main stages: first, the motion is tokenized in a morphology-independent way. Second, a token sequence is generated based on combined text, perception, and token history. Finally, the motion is generated by using physics-aware decoding. The authors report results that show that their method is superior to baselines on existing datasets, as well as in real-world evaluations.

### Strengths
The paper is considering a relevant problem of generalization to different hand morphologies. The authors proposed a comprehensive framework that shows good results across multiple metrics and in real-world robot setups. They successfully manage to combine and benefit from existing models, such as PointSam and CLIPort, and integrate them into their framework. Overall, the approach is well-defined, and evaluation supports the claims.

### Weaknesses
The main weakness of the approach is the complexity of the method. Currently, the approach consists of multiple parts and many different pre-trained models that need to be finetuned.  

The authors do not provide code. It is unclear which simulation environment they have used.

The authors mention some terms without providing sufficient explanation in their context or a reference to related work. Such terms are MANO poses (line 153), vector-quantization operator (line 187), knowledge distillation (line 203).

Smaller writing comments and typos:
- In the introduction, the authors listed 4 core capabilities, and 4 contributions. However, they almost identically, and their repetition is not well motivated. Therefore, the authors should either differentiate them better, or combine them in order to improve legibility.
- Line 045: No space before AffordDexGrasp
- Line 272: No space between sentences (generation.A practical)
- Table 1, 2, and 4: The arrow pointing to right next to Diversity is unintuitive, and its meaning might confuse readers, who did not read the evaluations section in detail.

### Questions
Have you tried different VLMs?  

Have you tried others pretrained models instead of PointSam and CLIPort? 

Have you tried different capacities of the Codebook?

Which simulation engine have you used? In the Appendix D it is mentioned that Sapien is used for visualization.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
2

---

## Human Reviewer 4

### Summary
The paper presents a VLM approach for unified dexterous manipulation. Their approach consists of multiple components. First, a unified tokenizer is learned for multiple hand morphologies using a VQ-VAE codebook. The tokenizer is learned in such a way that all morphologies share the same codebook but different encoder and decoders. For the VLM training, qwen 0.6B is used as base modell. The VLM is trained to ouptut the hand configurations given the object target trajectory and the point cloud of the object. For inference, the point cloud is inferred using PointSAM and the target trajectory using CLIPort. Finally, the hand poses are refined via optimization using a cost function that aligns contact normals with surface normals of the point cloud as well as produces smooth motions. The approach is tested on several benchmark datasets as well as real robot tasks.

### Strengths
- First VLM for unified (multi-embodiment) dexterous manipulation
- The VLM can be trained purely from human data
- Performance seems to be competitive
- Real robot experiments are convincing

### Weaknesses
- Some sections are unclear and missing detail (see questions)
- The paper would benefit from further ablations. E.g. the different parts of the cost function. Or the benefits of using a unified latent space. Here, the (maybe naive) alternative would be to learn everything in a single space (e.g. MANO) and retarget the output of the VLM afterwards. Such a comparison would be insightful. 
- There is no further information on the costs of the optimization of the grasp. How long does it take? Is it real-time capable?

However, I think the approach is interesting and shows a promising performance. The strengths do outweight the weaknesses.

### Questions
- I got confused in section 3.3 as its unclear how the mathematical objects in Eq. 7 and 8 look like. Could you please add more information here and clarify what T_tar and P_obj is (also formally, what is the dimensionality)?
- Is the target trajectory the 6D pose trajectory of an object or the 3D positions of a keypoint?

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
4