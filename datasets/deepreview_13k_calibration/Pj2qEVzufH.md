# Efficient Structure-Aware 3D Gaussians via Lightweight Information Shaping

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
3D Gaussians, 
as an explicit scene representation, 
typically involve 
thousands to millions of elements per scene. 
This makes it 
challenging to control 
the scene in ways 
that reflect the underlying semantics, 
where the number of independent entities 
is typically much smaller. 
Especially, 
if one wants to animate or edit objects in the scene, 
as this requires coordination among the many Gaussians
involved in representing each object. 
To address this issue, 
we develop a mutual information shaping technique 
that enforces resonance and coordination
between correlated Gaussians 
via a Gaussian attribute decoding network. 
Such correlations can be learned 
from putative 2D object masks in different views. 
By approximating the 
mutual information with 
the gradients concerning the network parameters, 
our method ensures consistency 
between scene elements 
and enables efficient scene editing 
by operating on network parameters rather than massive Gaussians.
In particular, 
we develop an effective contrastive learning pipeline
with lightweight optimization to shape the attribute decoding network,
while ensuring that the shaping (consistency) is maintained during continuous edits, 
avoiding re-shaping after parameter changes. 
Notably, 
our training only touches 
a small fraction of all Gaussians in the scene 
yet attains the desired correlated behavior 
according to the underlying scene structure. 
The proposed technique 
is evaluated on challenging scenes and demonstrates significant performance improvements 
in 3D object segmentation and promoting scene interactions, 
while inducing 
low computation and memory requirements. 
Our code and trained models 
will be made available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a method for correlating Gaussians that belong to the same semantic group. It leverages a network to decode feature Gaussians into attributes and approximates mutual information via gradients with respect to network parameters. This approach enables editing operations through adjustments to the network parameters rather than direct manipulation of numerous Gaussians. The mutual information between Gaussians is approximated by shaping activations from perturbed network weights.

### Strengths
Previous approaches embed semantic features directly within each Gaussian primitive, requiring extensive manipulation of individual Gaussians to edit scenes. This paper instead proposes encoding mutual information within an attribute decoding network, allowing scene edits to be made by directly adjusting the network parameters.

### Weaknesses
The paper is generally challenging to follow, with many points lacking clear explanations. For example, Equation 7 and Line 304 state that "we find that ∂h corresponds to repeated activations σ(h(l−1))." However, this lacks sufficient context, specifically regarding how the partial derivative relates to the activation function and the preceding layer's output. The explanation does not clarify the mechanism by which this relationship is derived or why it is crucial for the method's success. Similarly, Line 317, which mentions that "shaping activations ∂h within the attribute decoding network Φa supports a sequence of editing operations," is vague. It does not explain how manipulating these activations translates to specific editing operations on the 3D scene, nor does it detail the nature of these 'shaping' operations. 

The proposed method uses an MLP network to model mutual information between Gaussians, where the Gaussians primarily serve to splat features onto images used as inputs for the MLP. The primary contribution appears to be an enhancement to the JacobiNeRF framework, rather than a significant innovation in the context of 3D Gaussian Splatting (3DGS). The method seems to leverage the existing 3DGS framework primarily for feature extraction, then applies a network-based approach similar to JacobiNeRF for editing, which raises questions about the novelty of the approach within the 3DGS domain itself.

The contributions of Section 3.5 on coarse mask guidance and Section 3.6 on smoothness regularization seem minor, primarily focused on refining supervision masks. These sections could potentially be merged, as similar techniques have been explored in prior work. The techniques described for mask refinement appear to be standard practices in the field, and the paper does not adequately demonstrate a significant advancement or novel application of these techniques. The discussion lacks a detailed analysis of how these refinements specifically contribute to the overall performance gains.

The method depends on a 2D video mask tracker for grouping Gaussians. Based on the experimental results, it is difficult to determine if performance improvements arise from the mask tracker or the proposed approach. For instance, in Figure 4, the poor mask quality generated by Gaussian Grouping may stem from suboptimal 2D masks. The reliance on an external mask tracker introduces a potential confound, making it difficult to isolate the impact of the proposed method from the quality of the input masks. The paper does not provide sufficient analysis to disentangle these effects.

### Questions
Please refer to the weaknesses section.

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
This paper proposes information shaping for the 3D Gaussian field, following NeRF-based work JacobiNeRF. By contrastive learning between Gaussian primitives, the resulting Gaussian primitives on the same entities have a strong correlation while primitives on different entities have a weak correlation. The technical part follows the basic idea of JacobiNeRF and is tailored to 3D Gaussian with a attributes decoding network.  The learned Gaussian field is easier to edit, such as object removal and object movement.

### Strengths
- This paper adapts the basic idea of JacobiNeRF to 3DGS and makes it work in terms of scene editing.
- The method achieves good performance in the open vocabulary segmentation task.
- The application of object removal seems have good qualitative performance.

### Weaknesses
 - The technical novelty is limited. The Jacobian-based mutual information learning is the core part of this paper, which mainly follows JacobiNeRF. The authors are suggested to emphasize the unique designs that are different from the JacobiNeRF and demonstrate the effectiveness of the unique designs. The mask guidance and smoothness regularization differ from the DINO adopted in JacobiNeRF. However, these components seem to be incremental techniques, and their effectiveness is not well validated in the experiments.
- The writing should be improved. Many concepts lack a clear definition. For example, what are the exact definitions of perturbation and the sequential of perturbations (e.g., 1st/2nd/3rd perturbation). What are the exact parameters perturbated and how are they perturbated (i.e., perturbation direction and norm).
- The demonstration is weak. The object movement in Figure 6 is not impressive and it seems to be a sample handpicked with effort. It would be better to present more object movement demonstrations, using the main components of a 3D scene, such as the earthmover toy in the kitchen scene. Can you move the earthmover to anywhere else on the desk? Furthermore, the demonstrations have low diversity, mainly adopting the scene of kitchen and bear.
- The method outperforms JacobiNeRF and JacobiGS. However, the authors do not show the reasons via an apple-to-apple comparison with JacobiNeRF and JacobiGS. As I suggested in the first item, the authors are encouraged to show the performance roadmap from the JacobiGS baseline (or other reasonable baseline) and add the unique components one by one, offering a better understanding of the inner workings to readers.

### Questions
Does the decoding network reduce the rendering efficiency?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a mutual information technique based on 3D Gaussian splatting. Building upon JacobiNeRF, the authors present a more efficient training pipeline that optimizes activations instead of Jacobians. This approach ensures that the correlations between Gaussians are correctly shaped and remain consistent through successive parameter changes. Experiments on open-vocabulary segmentation and scene editing demonstrate the efficiency and significant capabilities of the proposed method.

### Strengths
1. The paper is well-written and organized, the authors provide a thorough theoretical analysis of the proposed method.
2. Experiments demonstrate that the proposed method outperforms other baselines while maintaining robustness to incorrect masks.

### Weaknesses
1. Compared to methods that edit the scene after obtaining the labels for each Gaussian, such as Gaussian Grouping, the direct manipulation of network parameters appears less flexible. For instance, while Gaussian Grouping can achieve style transfer, the proposed method seems limited to modifying the colors of selected Gaussians to be uniform.

2. The authors conduct open-vocabulary segmentation in only three scenes, evaluating just one object per scene if I understand correctly. Including more experiments would enhance the robustness and credibility of the results.

### Questions
1. Aside from JacobiGS in the paper, which utilizes the same mutual information shaping loss as JacobiNeRF, why was the original JacobiNeRF not included as a baseline for comparison?


2. Regarding weakness 2, is it possible for the proposed method to edit the color of an object to a textured color? Additionally, for the object movement task, can the method modify the trajectory of a selected object to follow a position-related trajectory, such as rotation?


3. Besides open-vocabulary segmentation tasks, would it be feasible to conduct experiments on semantic or instance segmentation tasks to further enhance the credibility of the findings?

### Soundness
3

### Presentation
3

### Contribution
3
