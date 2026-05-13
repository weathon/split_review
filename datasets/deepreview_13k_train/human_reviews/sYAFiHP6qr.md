# Implicit Neural Surface Deformation with Explicit Velocity Fields

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
In this work, we introduce the first unsupervised method that simultaneously predicts time-varying neural implicit surfaces and deformations between pairs of point clouds. We propose to model the point movement using an explicit velocity field and directly deform a time-varying implicit field using the modified level-set equation. This equation utilizes an iso-surface evolution with Eikonal constraints in a compact formulation, ensuring the integrity of the signed distance field. By applying a smooth, volume-preserving constraint to the velocity field, our method successfully recovers physically plausible intermediate shapes. Our method is able to handle both rigid and non-rigid deformations without any intermediate shape supervision. Our experimental results demonstrate that our method significantly outperforms existing works, delivering superior results in both quality and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a method to simultaneously recover the implicit neural representation of two given point cloud inputs, together with time-varying intermediate shapes between them. The point movement is modeled using an explicit velocity field regularized with smoothness and divergence-free constraints, and the shape is implicitly deformed using the modified level-set equation. The method is evaluated on four datasets, demonstrating its ability to model both pose and non-rigid deformation, as well as its robustness to incomplete and sparse input.

### Strengths
- **The modified level-set equation**: The paper modifies the Level-set equation by introducing an additional term (Equ.12). This modification ensures both the velocity field and implicit function are supervised to enforce the Eikonal constraint at each step. This approach is novel and effective in this context.
- **Performance**: The method demonstrates a better capability to recover physically plausible intermediate shapes compared to the given baselines.
- **Robustness to Incomplete and Sparse Input**: The proposed method is robust to the size of the target input point cloud. Unlike other methods, it can accurately recover the target shape and generate plausible intermediate shapes, even when the input is ten times sparser.

### Weaknesses
 - **Motivation**: Please clarify the motivation for this setting. Why is it important to recover physically plausible intermediate shapes? Why is it reasonable to assume that correspondances are available?
- **Correspondances**: While an ablation of the sparsity of the correspondences is available in the supplementary materiel, it’s not clear what happens when correspondances are not available i.e without the last term of Equ.15. On the other hand, can other methods rely on the correspondance information? For example, could this constraint be embedded in NISE and how does it perform in this case ?
On the other hand, one numerical result that can strenghten the paper is the average error of the method using correspondences from Cao et al. (2024a) . This should be added to table (a). In addition, it would be helpfull to also show the result with GT correspondences  in Fig.11 to better see the difference. 
- **Ablation of the modified level-set equation ablation**: Figure 8 is a bit surprising. Why is the OLSE baseline not able to recover the final shape while this constraint is explicitly enforced in the loss function ? Is the volume preserving term used in this experiment ?

### Questions
- What is the main motivation for this setting ?
- How  robust is the method to the failures of point-registration techniques, when ground-truth correspondences are not available ?

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
5

### Summary
This paper proposed a self supervised method for frame interpolation between two given point clouds. Technically, the proposed method models the point movement using an explicit velocity field and transform the time-varying implicit field through modified level-set equation. Experiments on various datasets show its effectiveness.

### Strengths
* The writing is easy to read and follow.
* The problem modeling is clear and the formula derivations are also correct.
* The proposed method achieves better performance than baseline methods at different datasets.

### Weaknesses
 * As shown in Fig. 4, the trajectory of each point is assumed as a line segment, making the shape different than the tow given shapes.
* The datasets used in the experiment do not consists of complex diformation. Can the proposed method deal with these conditions?
* There is no efficiency analysis about the proposed methods and baseline methods, which is important in practice.
* There is no experiment about reconstruction accuracy under different network sizes.

### Questions
* Can the proposed method be used to process non-watertight surfaces, such as clothes, by replacing the SDF with UDF?
* Should Eq. 4 consist of $\phi(x,t)=x^1$, where $x^1$ is the endpoint of the trajectory.
* Why not include Eq. 3 in the loss function?
* Given two shapes, there are many methods to calculate the flow of each vertices/points. Once the flow calculated, the frames between them are easy to interpolate. What is the advantages over these methods?
* Can the proposed method be used for triangle mesh directly?
* If replace the marching cubes with dual countouring, would the reconstruction increase?

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
This paper focuses on the task of learning continuous intermediate surface deformations between two given 3D point clouds. An end-to-end framework built upon fluid mechanics and physical constraints is designed to learn the time-varying implicit field via an explicit velocity field. Various comparison experiments and ablation studies are conducted to show the effectiveness and characteristics of the proposed learning approach.

### Strengths
- The theoretical formulations are well-motivated and technically sound, and the learned deformation results look smooth and reasonable.
- The method is able to handle rigid and non-rigid deformations without intermediate shape supervision.

### Weaknesses
 - One critical issue is the setting that a certain ratio of ground-truth point-to-point correspondences must be provided (although might be partially noisy). In fact, this is a very strong prior, especially when the points that are given GT correspondences are scattered around the whole shape surface. For example, during training 20,000 points are sampled from the surface, 5%-20% of them (1000-4000 points) are corresponded. This prior information makes the task itself much easier. From this perspective, I do not agree with the claim that the proposed learning framework is fully “unsupervised”.

- The experimental results suggest that the input shapes have similar geometries or poses and the method cannot handle very large deformations.

- As for the divergence-free velocity field, is it reasonable to constrain that the total mass inside surface always stay the same, especially when we deform two objects of distinct types and/or categories?

- Figure 6 presents an interesting example of handling incomplete inputs. What would happen if the input model becomes "broken," for example, if one paw is separated from the dog's leg? Is your method robust enough to handle such scenarios?

- Since the method is SDF-driven, it cannot handle surfaces with large boundaries, such as the clothes models in the DeepFashion3D dataset. Nevertheless, it would be beneficial to discuss this issue.

- Can your method handle inputs of different topologies? For example, a standing man with genus 0 and another person with hands on the waist, which is of genus 2.

- The authors claim that the intermediate shapes are physically plausible; however, all evaluation metrics provided are geometric. Additionally, the velocity loss, which includes a smoothness term and a divergence-free term, is not directly related to physical principles. Therefore, this claim requires better justification using quantitative physical measures.

### Questions
As for the divergence-free velocity field, is it reasonable to constrain that the total mass inside surface always stay the same, especially when we deform two objects of distinct types and/or categories?

Figure 6 presents an interesting example of handling incomplete inputs. What would happen if the input model becomes "broken," for example, if one paw is separated from the dog's leg? Is your method robust enough to handle such scenarios?

I suggest adding visulizations of the learned velocity fields.

Since the method is SDF-driven, it cannot handle surfaces with large boundaries, such as the clothes models in the DeepFashion3D dataset. Nevertheless, it would be beneficial to discuss this issue.

Can your method handle inputs of different topologies? For example, a standing man with genus 0 and another person with hands on the waist, which is of genus 2.

The authors claim that the intermediate shapes are physically plausible; however, all evaluation metrics provided are geometric. Additionally, the velocity loss, which includes a smoothness term and a divergence-free term, is not directly related to physical principles. Therefore, this claim requires better justification using quantitative physical measures.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Leveraging the Lagrangian approach in fluid mechanics, the authors introduce a novel method for implicit surface deformation. It models point trajectories during surface deformation using explicit velocity fields, enabling the recovery of physically plausible intermediate shapes through a modified level-set function. Unlike previous implicit methods, this approach requires only a sparse set of correspondences between the source and target point clouds in the unsupervised loss computation, eliminating the need for inefficient supervision from intermediate shapes. Experiments cover both intra- and inter-category shape deformations, as well as point clouds of different quality (sparse/incomplete).

### Strengths
- The paper is well-written, clear, and easy to follow.

- The authors provide detailed derivations for formulating the Modified Level-Set Equation from the ordinary differential equation of the velocity field.  

- The proposed method deforms source and target surfaces using a loss function that effectively avoids dependence on intermediate shapes, and requires only a sparse set of correspondences between the source and target point clouds.

- The method demonstrates efficiency in handling pose deformation within the same category and non-rigid deformation across different categories, and is flexible to incomplete and sparse point cloud inputs. 

- Ablation studies are provided to validate robustness of the method to different correspondence qualities.

- Multiple visualizations are provided for qualitative evaluations of the method.

### Weaknesses
 - Correspondences between the source and target shape have to be provided, which are not always available. Establishing correspondences between cross-category shapes might be challenging. 

- It is more informative if the correspondences utilized in deforming each surface pair can be visualized as well in some figures. 

- The readability of Figure 2 and Figure 7 should be improved.

### Questions
- How are the sparse correspondences selected for each deformation? Do they have to cover the entire shape, or is the method still effective if the correspondences are nested in certain regions of the surface?

### Soundness
3

### Presentation
3

### Contribution
3
