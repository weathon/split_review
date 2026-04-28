# TopoGaussian: Inferring Internal Topology Structures from Visual Clues

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
We present TopoGaussian, a holistic, particle-based pipeline for inferring the interior structure of an opaque object from easily accessible photos and videos as input. Traditional mesh-based approaches require tedious and error-prone mesh filling and fixing process, while typically output rough boundary surface. Our pipeline combines Gaussian Splatting with a novel, versatile particle-based differentiable simulator that simultaneously accommodates constitutive model, actuator, and collision, without interference with mesh. Based on the gradients from this simulator, we provide flexible choice of topology representation for optimization, including particle, neural implicit surface, and quadratic surface. The resultant pipeline takes easily accessible photos and videos as input and outputs the topology that matches the physical characteristics of the input. We demonstrate the efficacy of our pipeline on a synthetic dataset and four real-world tasks with 3D-printed prototypes. Compared with existing mesh-based method, our pipeline is 5.26x faster on average with improved shape quality. These results highlight the potential of our pipeline in 3D vision, soft robotics, and manufacturing applications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors present a holistic approach to estimating the internal topology of objects from images. The work relies on the use of a particle-based differentiable simulator to estimate probable internal topology directly from the seen motion of an object. By this approach, the author is able to generate even real-world 3D printed versions with reasonable structure directly from a small video sequence.

### Strengths
The author works on a novel approach to solving a relatively novel problem for modern 3D Computer Vision. While the idea of reconstruction of internal topologies is not novel to the best of my knowledge, I have not seen much work trying to solve this for 3D Gaussian Splatting or NeRF-based approaches.
The work itself is decently written and shows a great evaluation to validate the quality of their methodology.
The authors can propose a holistic pipeline that should make their work easily usable for users, with the authors giving a significant amount of design possibilities.
In general, I am more than in favor of this work's results and core concept being interesting.

### Weaknesses
A large issue in this work is the convoluted writing. While still quite understandable, this work packs a significant amount of results, ideas, and concepts from many different fields.
As such, while many parts of the simulation (core contribution) have been well explained, much information regarding the volumetric representation is missing. Specifically, the details of how the particle-based simulation is coupled with the volumetric representation are unclear. For example, how exactly are the particle positions and velocities translated into a density field or occupancy grid? What kind of interpolation or smoothing techniques are used? Without these specifics, it's difficult to fully assess the technical novelty and reproducibility of the method. As such, to improve the work (and make it complete), I would suggest the author add more information in the appendix.
Another larger issue is the motivation. While in Computer Graphics/Computer Vision, the challenge of estimating internal topologies is quite interesting, the estimation part might be a larger issue for practical, real-world use cases. In many real-world applications that rely on internal topologies, it is quite important that exact information is given, as this cannot assured by your model. The lack of guarantees about the accuracy of the internal topology makes it difficult to see how this method could be used in applications where precise internal structures are critical, such as in engineering or medical contexts. I am still quite unsure when this work will be usable in real-world applications.

### Questions
- The authors claim one of the applications is in 3D printing; since I lack any knowledge of 3D printing, I am unsure about its weaknesses. But to enhance my understanding, why do we require the internal topology to be known for this? Shouldn't having the surface not be enough?
- Please fix the typo in line 175 "point clout"
- Please keep writing style consistent for example, line 234, "point-cloud"
- Would it be possible again to summarize for me what actually is the main goal and main application of this work?
- Not so much a question but rather a comment regarding Abstract Style (improvement/suggestion): Having this kind of structure usually improves understandability and readability: 1. What is the problem and why is it important? 2. What are the limitations of existing solutions? 3. What are the advantages of the proposed approach? 4. How does it work? 5. Summary of results

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
4

### Summary
The paper presents TopoGaussian, a pipeline for inferring the internal structure of opaque objects using only photos and videos as input. The pipeline works by first using Gaussian splatting on multi-view images to obtain a point cloud, then optimizing the internal topology structure through a differentiable physics simulator to match observed motion patterns.

The key contributions include a particle-based, mesh-free pipeline that combines Gaussian splatting with a differentiable physics simulator; three flexible topology representation options: particle-based, neural implicit surface, and quadratic surface; a particle-based differentiable simulator supporting both rigid and soft objects with different topology structures.

### Strengths
1. Novel combination of Gaussian splatting with physics-based optimization for internal structure inference.
2. Uses a mesh-free approach that avoids common issues with mesh processing; presents particle-based differentiable simulations that are compatible with three flexible topology representations, including particle, neural implicit surface, and quadratic surface.
3. Well-structured presentation with a clear pipeline overview.

### Weaknesses
The reviewer appreciates the authors' effort in building a particle-based pipeline to find a physically plausible internal topology structure. As the authors have also mentioned in the paper, this task is relatively new, and there are fewer baselines to compare with (at least other baselines do not use point-based representation). I have several concerns about the measuring metrics and their validation to support the claims from the authors:

1. Optimization Loss: This measures the difference between simulated motion and reference motion, and it directly indicates whether the internal topology structure is physically plausible. However, in Figure 3, the current method does not achieve the lowest loss among baselines in multiple test samples.
2. Comparison Implementation: When exporting the mesh from other baselines and chaining it into the rest of the pipeline in this paper, how can the mesh-based representation be made compatible with the rest of the system that is particle-based?
3. Time / Smoothness: It is unclear whether this improvement comes from the GS representation itself or from the authors' method. The reviewer encourages the authors to elaborate more on this or provide ablation studies to explain that the improvement comes from the proposed method itself.
4. Inner Structure: Can the authors provide the reference ground truth for the inner structures when making comparisons with other baselines? The reviewer understands that, in practice, the inner structures are hard to acquire, but in synthetic data, it is practical to obtain the ground truth of inner structures.

Other question:

How is the decision variable applied to the point cloud representation to obtain a continuous indicator function from the point cloud? (Line. 193)

### Questions
Please see my questions in the previous weakness section.

### Soundness
2

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
The paper introduces TopoGaussian, a particle-based approach that uses visual clues from photos and videos to infer internal topology structures of opaque objects. Key contributions include:
1. Mesh-Free Topology Inference: TopoGaussian combines Gaussian splatting and a particle-based differentiable simulator to infer interior topology without requiring mesh-based representations, which traditionally entail extensive fixing and filling processes.
2. Flexible Topology Representations: The pipeline supports different topology representations (particle, neural implicit surface, and quadratic surface), allowing for optimization and simulation within a unified framework.
3. Experimental Validation: TopoGaussian is evaluated on synthetic and real-world tasks, showcasing its capability to generate 3D-printable reconstructions that exhibit high fidelity and reduced processing time compared to existing mesh-based methods.

### Strengths
1. Efficient and High-Quality Reconstruction: The particle-based approach of TopoGaussian achieves efficient reconstructions, with the authors reporting a significant speedup (5.26x faster) and superior boundary reconstruction quality (2.33x improvement) compared to mesh-based methods like PGSR and Gaussian Surfels.
2. Annotation-Free and Flexible: The pipeline’s independence from intrusive sensors or annotation requirements makes it practical and applicable in fields like robotics and manufacturing. Additionally, the three topology representation options offer flexibility based on application needs, from rigid to soft-body simulation.
3. Simplicity and Smoothness of Output: By eliminating the need for mesh processing, TopoGaussian produces smoother outputs conducive to 3D printing and manufacturing.

### Weaknesses
1. Evaluation Limitation: The method optimizes the interior structure based on a single motion, which may lead to overfitting and an inaccurate reconstruction of the true internal structure. Since ground truth data for internal topology is unavailable, it is difficult to verify if the inferred structure is correct or merely adapted to the given motion. Although the authors acknowledge this limitation and propose alternative metrics, these may not fully reflect the true structure. To strengthen the evaluation, the authors could consider obtaining ground truth through simulation (maybe with physics simulation) or testing the inferred structure on new motion videos as a test set. If the predicted structure is accurate, it should exhibit consistent behavior across these unseen motions, providing stronger validation.
2. Potential Overfitting to Single Motion: The current approach optimizes the internal structure based on a single motion video, which may lead to overfitting and limit the model’s generalization capability. To improve the robustness and accuracy of the inferred structure, the authors could consider optimizing based on multiple motion videos. By incorporating a variety of motions, the resulting model may better capture the true internal structure and provide more reliable and generalizable results.
3. Limitation to Simple Material Compositions: The current framework supports only single-object, dual-material compositions, which may limit applications involving complex, heterogeneous materials or multi-object interactions. Future work could focus on extending support to more intricate material compositions.

### Questions
See weakness

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
3

### Summary
This paper proposed a particle-based pipeline for motion reconstruction with physically corrected internal topology based on visual inputs. Specifically, they used a vision-based reconstruction method to construct the point cloud and optimize the physical properties of each particle through a differentiable simulation. Through several rigid-body and soft-body motion tasks, they verified the validity of the approach.

### Strengths
● Extracting an object's internal topology through a visual solution sounds interesting and is a novel task. The feasibility of the solution is also demonstrated.

● The article constructs multiple synthetic data to validate the effectiveness of its scheme, and more importantly, it accomplishes multiple sets of validation experiments in real-world scenarios.

### Weaknesses
● The main goal of the article is to build the internal structure of the object by visual motion, but there is no proper metric or GT comparison to measure the correctness of the internal structure recovery, it only compares the rendering results

● The comparative experiments are insufficient; the paper only compares optimization loss, reconstruction quality, and time with two mesh-based approaches. This fails to highlight the main contribution of the paper, which is the recovery of internal structures. Additionally, the visual comparison of internal structures does not fully reflect the accuracy of the internal structure recovery.

● The proposed method involves multiple steps, such as Gaussian Splatting, Volumetric Shape Generation, and Topology Optimization, etc., but lacks thorough validation for these steps. For example, there is no detailed analysis of the impact of filling quality on topology optimization or the robustness of the entire system to the visual input quality and movement amplitude.

### Questions
● Is there a unique solution for recovering the internal structure of an object based solely on visual observation? How can we determine if the recovered internal structure is reasonable?

● The article mentions that the volumetric shape generation stage is faster than mesh-based methods. Is this stage entirely consistent with the PhyGaussian?

● What is the relationship between the metrics used in the article—reconstruction quality and optimization loss? How is reconstruction quality defined? Does the "Smoothness" mentioned in Section 8.1 Metrics represent reconstruction quality? Why does the proposed method achieve similar optimization loss to the baseline, yet show significantly better reconstruction quality than the baseline?

### Soundness
3

### Presentation
3

### Contribution
3
