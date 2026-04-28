# Jigsaw++: Imagining Complete Shape Priors for Object Reassembly

- Decision: Reject
- Avg Score: 5.25
- Scores: 3, 6, 6, 6

## Abstract
The automatic assembly problem has attracted increasing interest due to its complex challenges that involve 3D representation. This paper introduces Jigsaw++, a novel generative method designed to tackle the multifaceted challenges of reconstruction for the reassembly problem. Existing approach focusing primarily on piecewise information for both part and fracture assembly, often overlooking the integration of complete object prior. Jigsaw++ distinguishes itself by learning a category-agnostic shape prior of complete objects.  It employs the proposed ``retargeting'' strategy that effectively leverages the output of any existing assembly method to generate complete shape reconstructions. This capability allows it to function orthogonally to the current methods. Through extensive evaluations on Breaking Bad dataset and PartNet, Jigsaw++ has demonstrated its effectiveness, reducing reconstruction errors and enhancing the precision of shape reconstruction, which sets a new direction for future reassembly model developments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces Jigsaw++, a generative method to improve automatic assembly tasks involving complex 3D reconstruction challenges. Unlike existing methods that focus on assembling individual pieces or fractures, often neglecting the overall object structure, Jigsaw++ learns a category-agnostic shape prior for complete objects. A key innovation is its "retargeting" strategy, which utilizes the output of any existing assembly method to generate more accurate complete shape reconstructions. This makes Jigsaw++ complementary to current approaches. The authors provide evaluations on the Breaking Bad dataset and PartNet demonstrates its effectiveness in reducing reconstruction errors and improving shape precision, offering a promising new direction for future reassembly models.

### Strengths
- Jigsaw++ learns a shape prior that is not limited to specific object categories, making it more versatile and adaptable to a wide range of objects.
- The proposed retargeting makes the method complementary to other approaches.

### Weaknesses
 - Initial guidance may harm the performance of the proposed method, though this is a strength claimed by the authors' proposed "retargeting" tech.
- Although category-agnostic, the performance on highly intricate or unconventional objects is not extensively discussed. Only simple results are shown in the paper. 
- Utilizing the generative models is a good idea, but how to ensure the generated results comply with the topic of "fractured assembly"? In the shown results, the shape may change, and the SE(3) transformation is also difficult to obtain, making the proposed method hard to use in real-life applications, for example, providing a few scanned point clouds and then understanding how to assemble them to form a complete shape.

### Questions
- The first contribution, the authors claim the proposed Jigsaw++ is a novel method for addressing the object reassembly problem. At the end of Sec. 3.1, the authors say the purpose of the proposed method is not to design a reassembly algorithm, but rather an additional layer of information to improve the reassembly algorithm. They are very different concepts, and the contribution summarized in the Intro section is very misleading.
- The shape before and after "retargeting" may vary, and probably the worst case, it diverges to a totally different shape. It would be necessary to quantify how much shape change occurs between input and output.
- Would the proposed method generate parts that were not originally from the fractured pieces since it is based on a 3D generation model?
- Explain how the proposed approach could be adapted or extended to provide actionable assembly instructions from scanned point clouds.
- It would be greatly appreciated if the authors could provide several real-life examples, instead of simple samples from datasets, to prove the proposed method is useful for assembly purposes as the title suggested.

I suggest the authors could detailedly address the concerns and I will provide a final rating based on the feedback and other reviewers' opinions.

### Soundness
2

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
This paper aims to provide a category-agnostic global shape prior for shape assembly (part/fracture assembly) methods, improving upon the shortcomings of existing approaches that rely solely on local feature information. In modeling the generative model, to learn robust feature encoders and decoders based on limited initial assembly results (both intact and damaged), the proposed method maps 3D point clouds to multi-view images. This allows the use of robust pre-trained encoders and decoders trained on large-scale data. Based on this, the authors designed a training process based on rectified flow to implement a generative model that encodes damaged initial assembly results into latent representations and generate the intact ones. The effectiveness of the proposed pipeline across different assembly models has been validated on part and fracture assembly tasks.

### Strengths
- Learning robust latent representations and generative models based on limited intact geometry and initial assemble results is a challenging problem. The authors use multi-view images as a bridge, employing a pre-trained images-to-3D sparse-view reconstruction model to provide robust encoders and decoders. By mapping point clouds to multi-view images and utilizing these pre-trained robust encoders and decoders, they cleverly overcome this issue.
- Experimental results show that the generative model proposed by the authors can effectively enhance the initial assembly results of multiple models in both fracture assembly and part assembly tasks.

### Weaknesses
My primary concern is the necessity of the model design. In the problem setting, paired data is available, and paired data is directly used for fine-tuning the rectified flow model in the final stage, which makes the necessity of the entire pipeline uncertain. Unlike methods by Song et al., 2021a; Mokady et al., 2022; Meng et al., 2022; Liu et al., 2023, which perform distribution transformations like image editing, restoration, or image-to-image translation based on inversion, the process proposed in this paper requires fine-tuning based on paired data (L-355~L-359). This makes the overall process more complex compared to training-free approaches and directly training conditional generation models either from scratch or fine-tuning a pre-trained conditional model for example with ControlNet on paired data, without demonstrating advantage of the proposed method over these two types of approaches in the experiments. More specifically, the necessity of the pipeline lacks the following experimental clarifications:
- Given the problem formulation in the paper, paired data is available, which allows for directly training a conditional rectified flow. Compared to this naive solution, does performing inversion and “retargeting” before training the rectified flow on paired data offer advantage, like better robustness or generalization?
- Regarding the rectified flow model trained in Sec-4, how effective is the inversion-then-generate process without the “retargeting” step? Alternatively, what is the effect of skipping fine-tuning on the rectified flow model? Although the paper mentions that the results are suboptimal, there is no quantitative or qualitative evidence provided to support this claim.

Moreover, the proposed method can only serve as a shape prior and cannot yet be directly combined with existing assembly algorithms for the actual assembly task. The inability to directly optimize the final assembly result indeed represents a weakness (as mentioned by Reviewer kWoJ & r9Py).

### Questions
- How many shape pairs were used for training during the fine-tuning (or retargeting) of the rectified model? Was the model trained on the assembly results of one model directly applied to others? (e.g., Jigsaw → SE(3))
- The discussion of existing works in L207-L211 is somewhat inaccurate:
    - Regarding category-agnostic models and geometric details: many existing geometric generation models can produce detailed geometry (such as CLAY, X-Cube, etc., whose generated results can also be converted to point clouds). Whether training a category-agnostic model is essential might be more a matter of training and experimental details.
- Referring to works like (Song et al., 2021a; Mokady et al., 2022; Meng et al., 2022; Liu et al., 2023) as “conditional generation” in L219-L223 could be misleading. Alternative terms like “inversion-based methods” might be more accurate.
- It is necessary to discuss the relationship between mapping point clouds to images and NOCS[1] as well as X-NOCS[2].

[1] Normalized Object Coordinate Space for Category-Level 6D Object Pose and Size Estimation

[2] Multiview Aggregation for Learning Category-Specific Shape Reconstruction

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper studies the problem of object reassembly. the paper proposes a method called Jigsaw++, which learns a category agnostic prior of complete objects. The proposed method is able to generate complete shape reconstructions and can be used in conjunction with existing methods. Results on Breaking Bad and PartNet show the effectiveness of the proposed method.

### Strengths
1. A method that is able to "imagine" the complete shape prior which can be useful for the object reassembly problem.

2. The proposed retargeting method is able to facilitate the reconstruction of complete objects from partially assembled input. 

3. The proposed method can be used with other existing methods to further improve performance.

### Weaknesses
1. the first two columns of figure 6a are very difficult to see what they are trying to show (they look all black). maybe consider changing the style of presentation.

2. if other researchers want to apply this method to assemble a set of fractures from an unseen object, how confident can they be? should they expect the proposed method to give reasonably good assembly results? if not, why is that and how could they make improvements?

### Questions
good paper, but i still have questions. please see the weaknesses above

### Soundness
4

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
The authors propose an algorithm to fine-tune a partially reassembled object into a fully reassembled one, potentially with missing pieces or imperfections. They represent the objects as point clouds, which can be rendered into images via differentiable rasterization. A point cloud of a partially reassembled object is then rendered and encoded using a pre-trained diffusion model. The algorithm relies on the fact that partially reassembled shapes are likely underrepresented in the pre-trained training data; thus, they propose flowing the encoding to a higher probability region and decoding it to obtain the reassembled shape. The authors test their algorithm exhaustively on existing baselines.

### Strengths
I congratulate the authors for their work and thank them for their submission. As far as I know (I could be wrong though), this is the only work that proposes separating the “global” first-attempt-at-reassembly problem from the “local” fine-tuning-the-placement-of-the-pieces problem and proposes to solve the reassembly problem in two stages. Given the struggles of existing reassembly works, I believe this may very well be a strategy worth pursuing. The work seems technically sound and exhaustively evaluated, enough to convince me that the combination of this work and DGL/Jigsaw is the new state of the art for the reassembly task.

### Weaknesses
From a technical perspective, this work is fundamentally reliant on the completed object being given higher likelihood by the diffusion model than the partially reassembled one, which probably translates to similar objects being present in the data that was used to train said models. This is in opposition to purely geometric or feature-matching-type works like the ones mentioned in Sec. 2.1 that assemble pieces based on geometric features in the fracture faults. This reliance is never mentioned explicitly as a weakness, nor explored experimentally, which I found disappointing. For example, what happens if one tests the proposed method on procedurally generated shapes with procedurally generated fractures?  

From a less technical perspective, I believe the authors could scope the proposed method better and quicker in the introduction. By reading the abstract and the first four paragraph, a reader will believe that they are being presented with a full reassembly method, not just one to fine-tune an already-good, partial reassembly. As said above (see “Strengths”), this is a perfectly valid problem to tackle, but it should be very clear immediately.

The presentation of the qualitative results could also be improved, and I would really appreciate if the authors did so in their revision. While the authors use a point cloud in their network, both datasets they are using are actually meshes, and it is really hard to visually distingush the geometric matching of two shapes by looking at unstructured points. Could the authors use the learned transformations of the points to obtain a per-part mesh transformation, apply it to the input and show that as the result? At the very least, show that in addition to the point cloud. Now that I think of it, how would one extract a per-part transformation (i.e., in the form of T_i) from the existing pipeline, not just an output point cloud? Isn’t this transformation what one needs for the suggested applications in robotics, archeology and medicine?

### Questions
Please see the parts of “Weaknesses” that end in a question mark for questions addressed at the authors. On top of those,

- What exactly is the function “f” in L248? Are the point cloud visualizations throughout the paper actual rasterizations as described in these lines?
- What do these two sentences mean? “Likely, given a colored image under the same color encoding scheme, we obtain a corresponding partial colored point cloud that corresponds to the 2D pixels. The computed point cloud will be further refined through a camera-pixel alignment operation that projects the decoded 3D point onto the ray that connects the pixel and the camera center.” Could the authors elaborate, or explain this in a different way? Unfortunately, I cannot follow this reasoning or understand what I should take from it.
- In figure 3, which parts of this are didactic and which parts aren’t? For example, the voxel grid shows geometric information which then converges to the bottle shape. Is this what the latent r looks like? Or is a decoding of r what is being displayed?

### Soundness
3

### Presentation
2

### Contribution
3
