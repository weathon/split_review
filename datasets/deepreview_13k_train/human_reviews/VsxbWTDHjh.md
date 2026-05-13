# Fengbo: a Clifford Neural Operator pipeline for 3D PDEs in Computational Fluid Dynamics

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
We introduce Fengbo, a pipeline entirely in Clifford Algebra to solve 3D partial differential equations (PDEs) specifically for computational fluid dynamics (CFD). Fengbo is an architecture composed of only 3D convolutional and Fourier Neural Operator (FNO) layers, all working in 3D Clifford Algebra. It models the PDE solution problem as an interpretable mapping from the geometry to the physics of the problem. Despite having just few layers, Fengbo achieves competitive accuracy, superior to 5 out of 6 proposed models reported in \cite{li2024geometry} for the $\emph{ShapeNet Car}$ dataset, and it does so with only 42 million trainable parameters, at a reduced computational complexity compared to graph-based methods, and estimating jointly pressure \emph{and} velocity fields. In addition, the output of each layer in Fengbo can be clearly visualised as objects and physical quantities in 3D space, making it a whitebox model.  
By leveraging Clifford Algebra and establishing a direct mapping from the geometry to the physics of the PDEs, Fengbo provides an efficient, geometry- and physics-aware approach to solving complex PDEs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Fengbo, a novel computational pipeline designed to solve 3D partial differential equations (PDEs) specifically for applications in computational fluid dynamics (CFD). Utilizing Clifford Algebra, Fengbo employs an architecture that consists solely of 3D convolutional and Fourier Neural Operator (FNO) layers, effectively modeling the PDE solution process as a clear mapping from geometric representations to the underlying physics of the problem. Despite its relatively simple architecture with only 42 million trainable parameters, Fengbo demonstrates competitive accuracy, outperforming five out of six models previously proposed in the literature for the same dataset. The architecture achieves this with reduced computational complexity compared to graph-based methods while estimating both pressure and velocity fields. A notable feature of Fengbo is its transparency; the output of each layer can be visualized as objects and physical quantities in 3D space, thereby classifying it as a "whitebox" model. By integrating geometry with physics, Fengbo offers an efficient, interpretable, and physics-aware solution for addressing complex PDEs in CFD applications.

### Strengths
The paper presents a novel approach to solving 3D partial differential equations (PDEs) in computational fluid dynamics (CFD) through the use of Clifford Algebra. The use of a pipeline that incorporates only 3D convolutional and Fourier Neural Operator (FNO) layers within a Clifford Algebra framework is a creative combination of mathematical structures and neural network architectures. This uniqueness not only offers a fresh perspective but also has the potential to influence future research in both machine learning and PDE solving. The ability to visualize outputs as physical quantities in 3D space transforms the model into a "whitebox" system. This enhances the interpretability of complex models, which is increasingly important in scientific computing, as it allows for better understanding and trust in the results produced by neural networks.

### Weaknesses
1. Lack of Comprehensive Benchmarking
The paper's evaluation is limited, comparing against only a small selection of existing methods. A more thorough comparison against a wider range of state-of-the-art techniques, including both traditional numerical solvers and recent machine learning approaches for PDEs, is needed to fully assess the method's performance and novelty. The current benchmark does not sufficiently demonstrate the superiority of the proposed method across diverse scenarios and complexities.

2. Absence of Generalization and Scalability Discussion
The paper lacks a detailed discussion on the generalization capabilities of the proposed method. It is unclear how well the model would perform on datasets with different characteristics or on PDEs beyond those considered in the experiments. Furthermore, the scalability of the approach to larger and more complex simulations is not adequately addressed. The computational cost and memory requirements for larger problem sizes should be analyzed and discussed.

3. Potential Overlook of Limitations
The paper does not fully explore the limitations of the proposed approach. For instance, the reliance on specific types of neural network layers (3D convolutional and FNO) might restrict the model's ability to capture certain types of complex flow physics. The potential for instability or divergence in the solution process, especially when dealing with highly nonlinear PDEs or turbulent flows, is not discussed. A more critical analysis of the method's shortcomings is needed to provide a balanced view of its applicability.

### Questions
1. Please compare with more recent developed methods
2. Please conducts more experiments on different datasets or PDEs.

### Soundness
2

### Presentation
2

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
This work is essentially the combination of "Clifford Neural Layers for PDE Modeling":

https://arxiv.org/abs/2209.04934

and FNO:

https://arxiv.org/abs/2010.08895

with the extension to computational fluid dynamics (CFD). 3D test cases are considered in this work, with the goal of prediction of the pressure and velocity fields. The complexity of the algorithm, error analysis, and visual comparison between the ground truth and prediction were conducted in this work.

### Strengths
High quality of writing and figures. Details explanations. A successful extension of Clifford Neural Layers for PDE Modeling to the Navier-Stokes equations for molding fluid dynamics.

### Weaknesses
--> The novelty is limited. This is simply just another application of the Clifford Neural Layers for PDE Modeling paper.

--> In the literature review, the classes of PointNet and PointNet++ for deep learning of CFD have been missed. I suggest that the authors take a look and search on Google Scholar to find those articles and perhaps discuss them. Note that PointNet is suitable for unstructured grids and much lighter than graph neural networks since there is no connectivity between nodes.

--> I disagree with the claim of this manuscript saying that their proposed method is appropriate for irregular grids compared to graph neural networks or PointNet because they still convert irregular grids to Cartesian grids and this definitely introduced errors no matter how much you "carefully" convert these data.

--> Following my previous comment, I believe the information listed in Table 4 is misleading. FNO can be used for irregular geometries if one uses geometric transfer. See the following paper:

https://www.jmlr.org/papers/v24/23-0064.html

On the other hand, the proposed method is not inherently designed for irregular geometries, similar to CNNs and FNOs.

--> As a minor comment, it is better to write L2 as the $L^2$ norm

### Questions
--> In Table 2, for FNO, the test error is lower than the train error, how is this possible?

--> In Eqs. 20 and 21, the loss function is a combination of the relative $L^2$ norm with the absolute $L^1$ norm. Mathematically, it does not seem reasonable. How do you justify that?

--> I had some concerns, listed in Weakness. Please address them. Thanks.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents a new deep learning pipeline to predict the velocity and pressure fields in 3D CFD simulations. The algorithm relies on the use of Clifford algebra layers, a mathematical construction which enables the processing of n-dimensional multivector fields. First, the input fields are upsampled and mixed to translate local to global features. Then, the global information is processed with a FNO-like frequency learning algorithm in a regular voxelized domain. Last, the processed information is decoded to the desired outputs: pressure and velocity fields. This pipeline is tested in the ShapeNet Car and Ahmed Body benchmark datasets and compared with other state-of-the-art architectures.

### Strengths
* The Clifford algebra architecture is an interesting inductive bias and is generalizable to more complex multidimensional fields. 
* The method has less trainable parameters compared to other techniques.
* The last blocks of the algorithm can be interpreted as velocity and pressure fields, so one can have a visual intuition of how the network learns the final  prediction stage.

### Weaknesses
 * The method is limited for steady-state simulations, and only tested for low density/viscosity fluids.
* The performance of the method is very similar in error compared to existing techniques.
* The voxelization of the space might be very inefficient with more complex geometries.
* Line 245: Why is the bivector component left blank in the case of the velocity? The surface information is specially important for the velocity field as it determines the boundary layer dynamics, crucial for drag/lift analysis in aerodynamics. 
* The method's claim of being a white-box model may be overstated. While the final layers may provide some intuitive information during the decoding stage, the true learning of the underlying physics primarily occurs in the 3D Clifford FNO block, which still operates within a latent space. Furthermore, how practical is the interpretability of the final layers beyond offering intuition about the predictions? Have the authors observed any relevant phenomena, such as different energetic modes of the pressure and velocity field across each decoding stage? Without any analysis of this regard, the interpretability claim remains largely qualitative rather than quantitative and has little practical use.
* Table 2: Why MeshGraphNets are not tested for the ShapeNet car dataset? The original paper predicts both the pressure and the momentum field of the fluid.
* Line 388: "[...] being the only architecture reported able to do so while jointly estimating the scalar pressure field and the 3D velocity field". Any of the reported architecture can be trivially modified to include an additional output (the velocity field), so I don’t see this as a specific advantage of the proposed methodology.

### Questions
* Line 245: Why is the bivector component left blank in the case of the velocity? The surface information is specially important for the velocity field as it determines the boundary layer dynamics, crucial for drag/lift analysis in aerodynamics. 
* The method's claim of being a white-box model may be overstated. While the final layers may provide some intuitive information during the decoding stage, the true learning of the underlying physics primarily occurs in the 3D Clifford FNO block, which still operates within a latent space. Furthermore, how practical is the interpretability of the final layers beyond offering intuition about the predictions? Have the authors observed any relevant phenomena, such as different energetic modes of the pressure and velocity field across each decoding stage? Without any analysis of this regard, the interpretability claim remains largely qualitative rather than quantitative and has little practical use.
* Table 2: Why MeshGraphNets are not tested for the ShapeNet car dataset? The original paper predicts both the pressure and the momentum field of the fluid.
* Line 388: "[...] being the only architecture reported able to do so while jointly estimating the scalar pressure field and the 3D velocity field". Any of the reported architecture can be trivially modified to include an additional output (the velocity field), so I don’t see this as a specific advantage of the proposed methodology.

Final comment: The presented paper proposes almost the same methodology as GINO ("Geometry-Informed Neural Operator for Large-Scale 3D PDEs" paper) but changing the GNO layers with Clifford algebra layers. From an accuracy and novelty perspective, the results offer only incremental improvements. While the interpretability of the final layers might provide some vague intuition, the paper fails to extract any substantial insights from an engineering or mathematical perspective. The only real novelty of the paper is the reduction in number of parameters, which in my view is insufficient for the standards of this venue. For these reasons, I'd rate this paper as marginally below the acceptance threshold.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Fengbo, a neural operator pipeline that uses Clifford Algebra to solve 3D PDEs in computational fluid dynamics. Fengbo leverages 3D convolutional and Fourier Neural Operator layers within a Clifford Algebra framework to map 3D geometries to physical fields, such as pressure and velocity. It demonstrates competitive accuracy on CFD datasets with fewer parameters and lower computational complexity, while offering interpretability.

### Strengths
* The paper introduces a novel approach by embedding the entire architecture in Clifford Algebra, which allows for a unified treatment of geometric and physical data, enhancing model interpretability and preserving geometric relationships.

* This model provides white-box interpretability by representing intermediate outputs as multivectors, which correlate with physical quantities in 3D space.

### Weaknesses
 * No comparison with the most advanced deep learning-based methods (e.g. transolver, etc.).

* The main results in the paper show better results with fewer parameters, but not the best performance, and it would be better if the performance could be compared with the same parameter Settings. 

* The paper was validated on a limited dataset, and it is hoped that it can be validated on more diverse datasets and tasks (e.g., point cloud, structured mesh, regular grid, etc.), which can be referred to transolver's experimental design.

Minor comments:
* L257"... were the range of the summation of l,m,n isspecified by the kernel size and cin,cout are the ..." has some grammar and typo issues in line 127.

* The definitions of metrics in lines 346 to 363 (formulas (11),(12)) are inconsistent (groud truth and estimated results are used in the denominators respectively).

### Questions
Please refer to weaknesses section for questions.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This submission targets the learning of 3D flow fields together with pressure distributions by using Clifford algebra. This approach has been proposed in previous work, and the submission at hand extends its implementation, and add geometry and physics blocks that seem to primarily aim for up- and down-sampling.

As the paper is largely extending previous work, it does not include and evaluate simpler cases, but directly focuses on 3D flows. Results are shown for flows around obstacle geometries from ShapeNet cars, and the Ahmet body. 

The results are mixed: in some cases the proposed architecture seems to perform well, but is outperformed by previous work in others. Especially the classic Unet still seems to do a fairly good job, and probably has a much lower computational workload (and simpler implementation).

Overall, I like the direction of the paper: 3D flows are definitely a challenging topic, and important for practical applications. At the same time, the proposed method does not seem overly convincing to me: it is very tailored towards 3D flows, and seems somewhat incremental given the previous work on Clifford based GNNs. With the results in the paper, I would be hesitant to try this approach, and correspondingly, I also find it difficult to really argue for accepting this paper to ICLR. I think with the current, somewhat narrow scope on 3D pressure (+velocity) the submission would be better suited for a more specialized conference or journal.

### Strengths
I think the paper has the following strong points:
- it targets non-trivial flow scenarios in three dimensions
- the ShapeNet cars and especially the Ahmet body are interesting use cases
- a nice range of baselines models is compared to
- the underlying theory is complex

### Weaknesses
At the same time, the submission has weak spots:
- the approach seems to be specialized to 3D flows, and I don't see how it would naturally extend to other problems
- the gains in terms of accuracy seem to be mild, which is a pity given the complexity of the approach
- the Clifford algebra comes from previous work, and I have to admit that I don't find it intuitive to work with
- the properties of the baselines are not fully clear (e.g., parameter counts are missing)

### Questions
What is the bottleneck that caps the model size at 42M parameters? This does not seem overly large for 3D problems.

Minor, but why are the sizes of the other models in table 2 not listed? How many parameters did they have?

(Very minor recommendation, it's a good idea to give intuition with figures like fig. 2 about the Clifford algebra setup, but figure 3, for example, did not add much information.)

### Soundness
3

### Presentation
3

### Contribution
2
