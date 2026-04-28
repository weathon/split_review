# Articulate Anything: Open-vocabulary 3D Articulated Object Generation

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 8, 5

## Abstract
3D articulated objects modeling has long been a challenging problem, since it requires to capture both accurate surface geometries and semantically meaningful and spatially precise structures, parts, and joints. Existing methods heavily depend on training data from a limited set of handcrafted articulated object categories (\textit{e.g.}, cabinets and drawers), which restricts their ability to model a wide range of articulated objects in an open-vocabulary context.
To address these limitations, we propose \model, an automated framework that is able to convert any rigid 3D mesh into its articulated counterpart in an open-vocabulary manner. Given a 3D mesh, our framework utilizes advanced Vision-Language Models and visual prompting techniques to extract semantic information, allowing for both the segmentation of object parts and the construction of functional joints.
Our experiments show that \model~can generate large-scale, high-quality 3D articulated objects, including tools, toys, mechanical devices, and vehicles, significantly expanding the coverage of existing 3D articulated object datasets. Additionally, we show that these generated assets can facilitate the acquisition of new articulated object manipulation skills in simulation, which can then be transferred to a real robotic system.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents a pipeline for part segmentation, motion prediction, part completion with re-texturing. The authors leverage vision foundation models and LLM to lift the 2D part segmentation to 3D. The authors further design the heuristic-based motion prediction and leverage LLM to pick the keypoint for the predefined joint categories. For the incomplete geometry, they use diffusion priors to optimize the geometry and texture with text prompts. They compare their results with some articulated model generative work.

### Strengths
1. The task to convert static 3D mesh into interactable articulated objects is valuable and interesting.
2. The final demos that show that it can guide the real-to-sim-to-real demonstrate the usefulness of the pipeline.

### Weaknesses
1. This paper is not an articulated object generation work. But focus on the part segmentation, motion prediction and part completion. It’s more on the analyzing on the shape side instead of generating the shape. Therefore, the whole comparison is a bit weird. There are a number of works focusing on part segmentation, and motion prediction. There needs to be comparisons with them on the segmentation and motion prediction performance (e.g. Category-Level Articulated Object Pose Estimation, PartSLIP). The authors can consider comparing with some work listed in the survey (Survey on Modeling of Human-made Articulated Objects).
2. A known issue of lifting 2D SAM masks into 3D is the consistency of different viewpoints, the granularity of the segmentation, and how to predefine the part labels. There lacks such discussion in the paper. Please provide more discussions on such details and show more quantative results on this part.
3. The writing and experiments are confusing to mention generated objects from the pipeline. When compared with other generative work, it’s unclear if you start from an existing 3D mesh. If yes, then why compare the raw mesh with them, even if there can be some geometry change in the part completion step. Please provide a more detailed explanation on the input of different methods of the comparison and explain why the comparison is fair if the proposed method uses an existing 3D mesh. Please also discuss how to fetch the 3D mesh to compare with other methods.

### Questions
For the shape in the teaser image and in the website, do they go through the refinement step? Seems that their geometry is much better than the results after the refinement step in the paper. Please give more clarification on the process to generate the demos of the objects shown in the teaser image on how do they keep the original texture, if they go through the whole pipeline of the proposed method?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses an interesting problem that aims to convert 3D meshes into articulated objects. This challenge is quite important and has the potential to greatly benefit the fields of 3D vision and robotics.

### Strengths
- The challenge discussed in this paper is important, and the proposed algorithm is reasonable.
- The 3D demos presented in this paper are interesting.

### Weaknesses
 - Novelty: This paper introduces an interesting method called "Articulated Anything" to address the problem of articulated object generation. While the method is reasonable, it essentially relies on the power of various large models and diffusion models, which may limit the novelty of the proposed framework.

- Writing: Some parts of this paper are difficult to follow. For example, in Section 3.4, the process of refinement in the proposed architecture is hard to follow. When describing the method, it would be helpful to include some mathematical expressions or pseudocode to assist in explaining the approach.

- Experiments: In the ablation study, it is recommended to add more quantitative experiments to evaluate the performance of different components of the proposed framework. For instance, for the ablations of refinement and transformation presented in Figure 6, could the authors provide detailed quantitative comparisons for these experiments?

- Performance: The performance of the proposed method is not particularly impressive. It is difficult to observe a significant improvement compared to existing methods, such as CAGE.

### Questions
Please see the weaknesses part.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors propose an automated framework, that converts rigid 3D surface meshes into articulated meshes. It first uses VLM to segment the object into parts, then uses geometric cluses and visual prompting to estimate joint parameters. Finally it refines the parts through SDS optimization. It improves existing optimization method by randomly transform the parts during the optimization process.

The method can be applied on AIGC（Artificial Intelligence Generated Content） mehes and hand-crafted 3D models. Experimental results show that it can generate high-quality meshes. Experiments on PartNet-Mobility show that it can estimate the joint parameters accurately.

### Strengths
This paper designs an effective pipeline for open-vocabulary 3D articulated object generation. It leverages the advanced VLM and visual promptiing techniques to segment parts and estimate the joint parameters.

The integration of all three modules to achieve high performance and successfully connect them is impressive. To the best of my knowledge, this is the first work on open-vocabulary 3D articulated object generation.

The application of the proposed method on Real-to-Sim-to-Real is interesting.

### Weaknesses
My main concern is the Part C （Geometry & Texture Refinement）.

The manuscript in Part C is too rough. To my understanding, it is an improvement to existing SDS optimization method Qiu et al. (2024). If so, the baseline method should first be desribed, making the paper self-contained. Further detailed description of the improvement is lacking. The authors should add some figures to illustate the optimization pipeline and some math equations should be added.

As claimed, the refinement process should be able to generate and optimize the inner structure of each part, but it is difficult to see and evaluate the performance based on the figures in the submission or the webpage. 
I suggest providing cross-sectional views of refined objects, including before-and-after comparisons of internal geometries,quantitative metrics to evaluate the quality of inner structures

Provide examples of cases where the pipeline fails or produces suboptimal results.
Analyze the root causes of these failures.
Discuss potential solutions or future work to address these limitations.

### Questions
Combine Figures 4, 5, and 6 into a single, more comprehensive figure
Add labels or annotations to highlight key features or differences between examples
Include a diverse set of objects to better showcase the method's capabilities

Comparision between the improvement in Part C and baseline method is missing.

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
4

### Summary
This paper works on the task of converting a 3D mesh into its articulated counterpart, and there are two scenarios: 
1) if the input mesh comes with part geometries, this work can segment the articulated parts and estimate the articulation parameters for each part so that the mesh can be articulated; 
2) if the input mesh is a single surface, this work takes an additional refinement step to generate an articulated object which takes the input mesh as initialization and a text as additional input.

This work proposes a three-stage pipeline to work with arbitrary input, which is stated as open-vocabulary in the paper.
- In the first stage, it proposes to leverage VLM to segment the part in 3D from multi-view images rendered from the input mesh.
- In the second stage, it first proposes several candidate 3D points where the joint might appear based on several heuristic rules. Then the VLM is prompted to select the points on the image to infer the joint parameters in 3D.
- In the third stage, it first reconstructs DMTet for each part and then uses SDS loss to refine the incomplete regions.

The main contribution is this pipeline that enables the generation of diverse articulated objects by taking arbitrary 3D mesh as input.

### Strengths
- This paper identifies a critical research gap in 3D generation for articulated objects and contributes to an increasingly important area. 
- This paper proposes a novel pipeline that enables the creation of articulated objects from arbitrary input mesh.
- The paper shows promising preliminary results to demonstrate the effectiveness of the method.

### Weaknesses
 - **Somewhat misleading presentation**: I believe the paper would benefit from reorganization to better clarify the main goal or task that this work addresses, and the downstream applications that the proposed method enables. The way the paper currently presents its goal and teaser figure seems somewhat misleading. Based on my understanding, there are essential two tasks enabled by the pipeline proposed in the paper. The high-quality output shown in Figure 1 is produced using an input mesh that already contains part geometries, which aligns with the stated goal of "converting a rigid mesh into its articulated counterpart” as the first task. 
The second task involves input meshes without any part geometries, requiring an additional reconstruction and optimization step. Based on my understanding, this process cannot fully preserve the original input in terms of geometry and appearance. This feels more like a text-to-3D generation task, where a 3D mesh serves as an initialization and a text input provides conditional guidance, rather than a straightforward conversion.
- **No quantitative evaluation of the reconstruction quality**: The paper lacks a quantitative evaluation of the reconstruction accuracy, in terms of geometry and appearance. I believe this is one of the most critical experiments needed to validate the approach. Specifically, taking a mesh surface (without part geometry) of the object in PartNet-Mobility as input, once it is reconstructed using the proposed pipeline, the Chamfer Distance of the part meshes with respect to the ground truth object can be reported. To consider the different states of the articulated objects, the ID and AID metrics (proposed by NAP and CAGE) can also be reported. For appearance, the PNSR/SSIM/LPIPS can be reported by rendering multi-view images.
- **Missing Technical and Experimental Details**: While the overall idea of the paper is easy to follow, many critical technical and experimental details are omitted. This lack of detail significantly weakens the paper’s reproducibility. Also,  it is unclear whether the comparison experiments presented are conducted in a fair manner. Please refer to the `question` section for specific requests for clarification.
- **Low resolution of Qualitative Results**: The resolution of most qualitative results, particularly those in Figures 3, 4, 5, and 6, is relatively low. I strongly recommend replacing these with higher-resolution images that better showcase the output quality. Based on the current results, it seems to me that the reconstructed objects shown in Figure 8 are of much higher geometry quality compared to other results. This inconsistency raises concerns about the overall quality of the generated outputs. I am not fully convinced by the quality of the generated objects as currently presented.

### Questions
There are **several details that need clarification**. Providing these details would help clarify the evaluation process and ensure the results are reproducible.
- How is the GPT4o exactly prompted for the task of part segmentation and joint point selection?
Once the joint point is selected, how are the joint limit and the direction of rotation/translation determined?
- How is the SDF of each part computed in section 3.3?
- How is the optimization process implemented? Where is the text prompt from? How many iterations are required to optimize each object? How long does it take?
- For unconditional generation, how is the experiment conducted? What are the input to this method and other baselines (NAP, CAGE, URDFormer)? Did you retrain URDFormer on the same split as CAGE?
- What do the red and blue boxes mean in Figure 5? Is the object shown at the left-most the input?
- For the comparison of articulation parameter estimation, what is the input to NAP and CAGE? How are they implemented to be compared? 

**Other questions about the experiment results**:
- In Table 2, the "Ours" score in the last column is significantly higher than that of PartNet-Mobility, which I assume serves as a ground-truth reference. Could you clarify why this is the case?
- In Table 2, the VQA score for NAP is also higher than “PartNet w/o texture”. What is it implied? It would be helpful to understand the reasoning behind this discrepancy and how the scores are being interpreted. 
- In Figure 3, what is the input to each method and how are the examples selected for comparison?


**Missing comparison points**:

On the side of articulation estimation, it is possible to compare it with other methods beyond just NAP and CAGE, such as Shape2Motion and Real2Code.

**Missing references**:

[1] Hu, Ruizhen, et al. "Learning to predict part mobility from a single static snapshot." ACM Transactions On Graphics (TOG) 36.6 (2017): 1-13.

[2] Sharf, Andrei, et al. "Mobility‐trees for indoor scenes manipulation." Computer Graphics Forum. Vol. 33. No. 1. 2014.

[3] Weng, Yijia, et al. "Neural Implicit Representation for Building Digital Twins of Unknown Articulated Objects." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.

[4] Wei, Fangyin, et al. "Self-supervised neural articulated shape and appearance models." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.

[5] Liu, Jiayi, Manolis Savva, and Ali Mahdavi-Amiri. "Survey on Modeling of Articulated Objects." arXiv preprint arXiv:2403.14937 (2024).

### Soundness
2

### Presentation
2

### Contribution
3
