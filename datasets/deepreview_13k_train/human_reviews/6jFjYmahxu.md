# DiffSound: Differentiable Modal Sound Simulation for Inverse Reasoning

- Decision: Reject
- Scores: 3, 5, 5, 3

## Abstract
Accurately estimating and simulating the physical properties of objects from real-world audio observations is of great practical importance in the field of vision and embodied AI. However, previous differentiable rigid or soft body simulations cannot be directly applied to modal sound synthesis due to the high sampling rate of sound, and previous audio synthesizers do not fully model the physical properties of objects behind the modal analysis.
We propose DiffSound, a differentiable sound simulation framework for physically based modal sound synthesis.
Our framework is capable of solving a range of inverse problems, including object shape, material parameter, and impact position reasoning.
Experimental results demonstrate the effectiveness of our approach, highlighting its ability to accurately estimate physical parameters and reproduce the target sound. Our DiffSound differentiable sound simulator serves as a valuable tool for applications requiring sound synthesis and analysis.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper describes a differential simulation framework for sound synthesis of physical objects impacts. The framework is a pipeline that employs a NeRF-like MLP to reconstruct the Signed Distance Function and translate it into the shape of the object. These are then being used by Finite Elements Method to recover object shape and an Additive Synthesizer to generate sound which is optimized by minimizing loss between the expected and groundtruth spectrograms. Experiments are performed on ObjectFolder-Real dataset for sounds from 100 objects.

### Strengths
1. The work proposes an additional step of recovery of Signed Distance Function done by MLP to assist with object shape recovery and synthesis of impact sound of the object.

2. Synthesized results appear to be corresponding to objects and their expected sounds.

3. The paper is well written.

### Weaknesses
1. The choice of baselines and whether these are strongest possible baselines is unclear. It is not clear if the baselines are the most relevant for the task of impact sound synthesis from object shapes. For example, are there other methods that directly synthesize sound from 3D shapes or SDF representations that could be used as a comparison? The paper does not discuss why the chosen baselines were selected and if they are the most appropriate.

2. The experiments are done on 100 objects only. This is a relatively small dataset for training a neural network, especially considering the complexity of the task. It is unclear how well the method would generalize to unseen objects with different shapes and material properties. The paper should provide a more thorough analysis of the generalization capabilities of the proposed method.

3. Train/validation/test split is not specified and thorough quantitive accuracy of these is not presented. The lack of a clear description of the data split makes it difficult to evaluate the validity of the experimental results. Furthermore, the paper does not present detailed quantitative results, such as specific metrics for sound similarity or shape reconstruction accuracy, making it hard to assess the performance of the method beyond qualitative observations.

4. Technical contribution is limited since the components of the pipeline are standard. Ablations with extensions of the components are needed to examine whether these are optimal for sound synthesis. The paper does not explore alternative architectures for the MLP or different methods for the FEM simulation. It is unclear if the current choices are optimal for the task or if other combinations of components could lead to better results. The lack of ablation studies makes it difficult to understand the contribution of each component to the overall performance.

### Questions
1. The current pipeline is split between a neural network approach and FEM simulator. Could both steps be modeled with a neural networks?

2. How would the work compare with impact sound generation from videos through diffusion model?
Su, Kun, et al. "Physics-Driven Diffusion Models for Impact Sound Synthesis from Videos." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.

3. What is the computational complexity of the pipeline?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a differentiable sound simulation framework called DIFFSOUND, containing three components. The first component is a differentiable tetrahedral representation, which uses implicit neural representation to encode SDF values and convert the encoded SDF into an explicit tetrahedral mesh. The second component uses a high-order finite element method to optimize material properties and shape parameters. In the end, an additive audio synthesizer synthesizes the sound.

### Strengths
1) The idea of building a differentiable sound simulation pipeline is very interesting. While the task is challenging, I am glad that the authors come up with a solution that will definitely be useful for various applications.
2) The component introduced in this work is highly interpretable. To my best knowledge, physical properties such as Young's modulus and Poisson's ratio were not modeled in the previous audio synthesizers.
3) Three inverse problems are conducted, and the results look reasonable.
4) The supplementary includes the code, which will be useful for reproduction.

### Weaknesses
1) One main concern is that the paper writing is very rough. For example, in 3.1 Differentiable tetrahedral representation, there is no formal mathematical definition for the input-output of the implicit neural representation (INR), how the encoded SDF values are converted into an explicit tetrahedral mesh, and the specifics of the transformation function applied to the mesh. The description in 3.1 lacks the necessary mathematical rigor and detail to be fully understood and reproduced. In 3.3, the loss equations 7 and 10 use the same annotation, but the $i$ means totally different things; this is a major source of confusion. Section 4 is a problematic combination of ablation studies and experiments on three inverse problems. The inverse problems, being a core contribution, should be presented in a separate section with a clear description of the experimental setup and evaluation metrics. In tables and figures, annotations like baselines 1, 2, and 3 are confusing since there is no corresponding description in captions, making it difficult to understand the differences between these baselines. The lack of clarity in writing and organization significantly hinders the overall reading experience.
2) I am interested in the computational cost of the optimization process for each object, but there is no information in the paper. While it is acceptable that the current approach may not be real-time, the paper should include an analysis of the optimization time, including the number of iterations, the time per iteration, and how these scale with the complexity of the object. This is important for assessing the practical applicability of the method.
3) A critical point of concern is the source of the ground truth eigenvalues. The paper does not explain how these eigenvalues are obtained, especially for real-world objects. Without a clear explanation of how these values are acquired, the optimization problem becomes less convincing. It is unclear if the optimization can be performed using only the audio loss, which would be a more realistic scenario.
4) The use of the Wasserstein distance to bridge the ground truth and predicted spectrograms is a good idea. However, the paper does not clearly define the criteria for switching between the Wasserstein loss and the L1/L2 spectrogram loss. The term 'sufficient convergence' is vague and lacks a precise definition. The lack of a clear switching criterion makes it difficult to understand and reproduce the optimization process.

### Questions
See my questions in the weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents DiffSound framework that connects material parameters of a solid body and acoustic features from the body in a differentiable manner. 
Using this model, we can construct a neural network that simulates audio signals when impacting the object or inferres the object shape from the audtory information.

### Strengths
The differentiable simulation is carefully derived from relevant literatures such as tetrahedral mesh, generalized eigenvalue decomposition and superimposed sinusoidal signals.

### Weaknesses
My major concern is that the reviewer is not convinced with the importance of shape geometry reasoning from audio signals. 
I think audio modality is not as informative to recover the shape of objects. Indeed, Figure 6 gives smoothed mesh surface. The shape may be distorted without sufficient voxel constraints. 

Is there any application scenario?
Perhaps this model may be applied to non-invasive examination of solid structures like impacting the surface and observing the responding signals. 
However, we cannot see such usages from the current set of experimental results.

### Questions
1. Eq. (5) to (6)

I could follow the derivation of Eq. (6) from (5). Do you use $\partial {\bf u}_i=0$ or some transformation of ${\bf u}_i ^T {\bf M} {\bf u}_i$?

2. What do you mean by *hybrid loss*?

Is it hybrid because linear and logarithm error is combined as in Eq. (10)? 
Or does this mean the use of $\ell_1$ loss and OT-based loss?

3. Using ground truth $\nu$

In the result of Table 1, how is estimation of $\nu$ critical to reduce the error in the spectrogram? 
Does the error reduce if ground truth Poisson's ratio $\nu$ is given?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an end-to-end framework for inferring the geometry and material properties of objects based on the frequency domain representation of the sound that they make.  To overcome some of the challenges, e.g., a sparse spectrogram representation, the authors propose a hybrid loss that first uses optimal transport to compute an approximate solution, and then the L1 loss to refine the solution.  Experiments are run to test material, geometry, impact positioning, independently.

### Strengths
+ The paper is tackling an important and challenging problem, which is especially of interest with increasing interest in AR/VR applications.
+ The writing is good, and the problem and solution are easy to follow, even for a non-expert.

### Weaknesses
 - I accept that the problem being tackled here is challenging, but the experimentation seems very limited.  The paper more shows anecdotal examples rather than present summary statistics for a larger test set with examples for illustration.  
- I am wondering how does the method fare in terms of accuracy for different materials?  Different object sizes?  and so on.

### Questions
How sensitive is the approach in terms of placement of the sensor?  If the microphone is too far away, does environmental effects influence the results (e.g., reverberation or other material properties that might affect reflectance, etc.?).  

How much does the complexity of the shape influence reconstruction?  For example, an intricate and non-convex shape that impedes direct path to the sensor? 

For Equation (10), why are both terms required?  One is just a compressed form of the other?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
