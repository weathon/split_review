# Geometric Algebra Planes: Convex Implicit Neural Volumes

- Decision: Reject
- Scores: 6, 5, 8, 5

## Abstract
Volume parameterizations abound in recent literature, from the classic voxel grid to the implicit neural representation and everything in between.
While implicit representations have shown impressive capacity and better memory efficiency compared to voxel grids, to date they require training via nonconvex optimization. 
This nonconvex training process can be slow to converge and sensitive to initialization and hyperparameter choices that affect the final converged result.
We introduce a family of models, \modelname{}, that is the first class of implicit neural volume representations that can be trained by \emph{convex} optimization. 
\modelname{} models include any combination of features stored in tensor basis elements, followed by a neural feature decoder. 
They generalize many existing representations and can be adapted for convex, semiconvex, or nonconvex training as needed for different inverse problems.
In the 2D setting, we prove that \modelname{} is equivalent to a low-rank plus low-resolution matrix factorization; we show that this approximation outperforms the classic low-rank plus sparse decomposition for fitting a natural image.
In 3D, we demonstrate \modelname{}' competitive performance in terms of expressiveness, model size, and optimizability across three volume fitting tasks: radiance field reconstruction, 3D segmentation, and video segmentation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a family of discretized implicit representations designed to enhance optimizability, memory efficiency, and expressiveness. The approach combines multiple discretizations of the 3D volume at different dimensions (1D, 2D, 3D) and resolutions to learn volume features. These features are then combined and input into a shared decoder, implemented as either an MLP or a convex MLP. Additionally, it is shown that with a linear decoder, the problem can be framed as a low-rank plus low-resolution matrix factorization.

### Strengths
Analyzing the properties of discrete implicit representations in terms of optimizability, memory usage, and expressiveness is highly valuable.

Several variants of the proposed method are tested across a diverse set of tasks, including both 2D and 3D problems.

The equivalence between one-dimensional grid representation and low-rank plus low-resolution matrix factorization appears intriguing.

### Weaknesses
Unclear method formulation

The method section is hard to read and follow. Some missing elements:
*  Functions and vectors are not introduced with dimensions
* Not all elements of the models are formulated (such as the multi-resolution copies) 
* Some concepts are introduced before their definition, such as the feature grids, following eq (4). What is the quantity c enumerating on, in eq (5)?
* The definition in equation (5) is challenging to interpret. What does  $f$  represent, and why are both  $f$  and  $\psi$  needed? What are their dimensions? The separation between equations (5) and (6) adds to the confusion and may frustrate the reader.
* Certain terms are not properly defined. For instance, what exactly does ‘semi-convex’ mean, and why exactly (proof) is the proposed model considered semi-convex?”

Unclear claim regarding generalizing existing models

It is unclear in what way the method generalizes previous work. The proposed factorizations appear to have been introduced in earlier studies, and this method seems to focus more on feature engineering in combining these factorizations. I may be mistaken, but the text would benefit from a clearer explanation of how it offers generalization.
 
Unclear relation between the introduction of the GAPlanes model and advocating for convex formulations.

The relationship between the introduction of the GAPlanes model and the emphasis on convex formulations is unclear. Specifically, the connection between the integration of convex MLP (in cases where the loss is convex) and its relevance to the GAPlanes model is not well established. This approach appears more like an application of convex MLP rather than a novel contribution. Additionally, the empirical benefits of convex formulations seem uncertain. How does this relate to the goals of this work?

### Questions
I would appreciate any feedback on the weaknesses and questions outlined above.

### Soundness
3

### Presentation
2

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
This paper proposes GA-Planes, a new family of models for representing volumes.
GA-Planes include features stored in a tensor basis and a neural decoder. This setup is flexible, and can be adapted to convex, semiconvex, or nonconvex training.

For 2D setting with a linear decoder, the authors show that GA-Planes can be reduced to a low-rank plus low-resolution matrix factorization.
For 3D tasks, GA-Planes are tested on radiance field reconstruction, 3D segmentation, and video segmentation, showing competitive results in terms of expressiveness, model size, and ease of optimization.

### Strengths
The motivation of the work is clear to me. The idea of GA-Planes seems interesting and is indeed quite flexible. The numerical experiments show competitiveness of the proposed method, particularly in 3D applications.

### Weaknesses
1. My main concern of this paper is on the theoretical part. I am not convinced that the authors have indeed proved the equivalence to matrix completion in 2D. See questions for more parts that are unclear to me.
2. Convexity/Semiconvexity seems to be of interest to the author, and is mentioned throughout the paper. It is exciting to see that GA-Planes can be adapted to convex optimization-based training. However, I am not sure if the numerics have provided any evident that this might be good to the GA-Planes family.
3. The presentation can be improved. For example, I am not quite sure what other dots (those not connected) in Figure 1a means.

### Questions
1. In the proof provided, I can see that the GA-Planes model can indeed be written in the form of (15), but I don't see how the training problem is equivalent to problem (9). Is this correct for more general 'true' representation y (e.g. higher rank)? Can we relate the optimal solutions of the two problems? 
2. In most experiments, the non-convex GA-Planes give the best result. Are there any advantage of using convex GA-Planes? For example, the authors mention optimizing globally regardless of initialization. Have you encountered any difficulties while adopting the non-convex setting, such as the choice of initialization?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work introduces a family of volumetric representations combining ideas from geometric algebra and convex optimization. First, features are learned on a predefined tensor basis represented by line, plane and volume elements. Using (bi/tri)linear interpolation and different elementary operations (concatenation, addition, multiplication), these are combined into multivectors. Second, these are then processed by a decoder MLP. This construction generalizes many previous volumetric representations, both classical and neural. Under additional restrictions on the multivectors, the decoder, and the objective, the entire optimization can be made convex or semi-convex.

After the theoretical discussion, different realizations of these GA-Planes models are tested empirically on three different tasks - radiance fields, 3D segmentation, and video segmentation. The results indicate good performance, especially for smaller models.

### Strengths
- The proposed representation family helps put many previous and potential future methods in a unifying framework. This is also done in a mathematically precise manner. I believe such efforts are important in the fast-paced ML research. 
- Similarly, the discussed trade-off between model size, expressivity, and optimizability makes for a good and easy to follow story. The paper is well-written overall.
- The empirical results suggest good potential of the method.

### Weaknesses
 - While different types of experiments are considered, each contains only a single problem instance (lego scene and skateboarding video). This makes it hard to draw strong conclusions about the empirical performance. The lack of diversity in the datasets limits the assessment of the method's robustness and generalizability. For instance, the lego scene is relatively simple and might not expose potential weaknesses of the approach when dealing with more complex geometries or textures. Similarly, the skateboarding video might not be representative of other types of motion or occlusions.
- While the method generalizes neatly and offers a lot of flexibility, it is not entirely clear how to make these design choices. There is a good discussion on the elementary operations and also on lines vs. planes vs. volumes, but the multi-resolution aspect of each seems to be overlooked, simply stating "we use multi-resolution copies [..]". The paper lacks a detailed explanation of how the different resolutions are chosen, and how they interact with each other. The authors should provide more insights into the impact of different resolution choices on the final performance and computational cost. The absence of a clear methodology for selecting these parameters makes it difficult to reproduce the results and adapt the method to new tasks.
- Limitations are not discussed. The paper does not address potential failure cases or scenarios where the method might not perform well. For example, it would be beneficial to discuss the limitations of the convex formulation in terms of expressiveness or the potential for overfitting in the non-convex case. Furthermore, the computational cost of the method, especially for high-resolution inputs, should be discussed. The lack of a discussion on limitations makes it difficult to assess the practical applicability of the method.
- Even though there is great value in considering the representation of a single signal, the authors overlook the opportunity to also discuss the generative setting, which would reach a broader audience. The paper focuses solely on reconstruction tasks, neglecting the potential of the proposed representation for generative modeling. This limits the scope of the paper and might not fully exploit the capabilities of the proposed method. Exploring the generative setting could reveal new insights and applications of the GA-Planes representation.

### Questions
- Could you please explain how you chose the different resolutions as mentioned in W2?
- Similarly, in the last sentence of section 5.1 you make it sound like the model can allocate parameters to different dimensional features adaptively, i.e. automatically. However, my understanding is that you need to predefine all the feature grid sizes. Could you please clarify this and potentially adjust the wording?
- To compare the (non-/semi-) convex formulations, you report the final performance metrics, and in addition you discuss the convergence guarantees. Are there other relevant practical aspects, in particular the number of training iterations or time?
- Can you comment on using GA-Planes in the generative setting?

**Suggestions**
- Please include a discussion of the limitations.
- The presentation could potentially benefit from some schematic representations of the method and especially GA concepts.
- During the submission process, please use the appropriate template which includes the line numbers. This is helpful for the review process.

### Soundness
3

### Presentation
4

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
This paper provides a generic strategy for grid-based representation of volumetric features, for use in applications like NeRF where the task involves computing a spatial quantity in 3D.  The basic idea, inspired by geometric algebra, is to include features that are constant along planes/lines in addition to a feature per grid cell.  This approach in some sense generalizes past approaches, as articulated in the appendix.

Although the title/discussion claims a link to geometric algebra, it seems the connection here is somewhat superficial.  As far as I can tell, the paper does not make use of any *algebra* from geometric algebra (e.g., assorted products and geometric operations) and could be described more simply without this language.  It seems like the basic idea here is simply to drop indices from a grid-based volume representation --- e.g., rather than having all features be f_ijk we can have some features with fewer indices f_ij/f_jk/f_ik (“plane feature grids” in parlance of the paper) and f_i/f_jf_k (“line feature grids”).  Invoking geometric algebra adds complexity to the text without benefit.

I appreciated the theoretical analysis in the paper, but the results do not seem reflective of the typical use cases.  In particular the theorems require piecewise-constant interpolation between grid elements as well as a convex objective, neither of which are common practice and are quite restrictive assumptions (indeed many of the experiments in section 5 are unable to use convex objective functions).

I appreciate the ‘framework’ for understanding assorted approaches to parameterizing volumes of features, and appendix A.1 helped me translate the discussion in the paper to something more concrete.  Given the zoo of prior models articulated in past work (see page 15), however, it seems the current paper is a variation on a fairly common theme in the literature.

The experiments here begin to validate that the proposed strategy is relatively effective, although they are far from comprehensive (just a few examples drawn from standard datasets in computer vision).  

For the reasons above, I am unable to suggest publication of the work at this time.  To improve the paper, I might suggest more deeply applying geometric algebra or removing it altogether in favor of simpler language, ensuring that the model and assorted objective functions can reasonably be implemented/reproduced from the text of the paper alone (or including code), and testing the proposed representations more thoroughly.

****

The paper claims to be the “first class of implicit neural volume representations that can be trained by convex optimization.”  I might argue that the approach outlined here is far from a typical “neural” representation, to the point that one could equally argue the same point for a grid or kernel method (if I understand sec 3.1 properly, this method relies on a grid rather than a generic neural parameterization).

Page 2:  “At the same time, any GA-Planes model can be trained by nonconvex optimization towards any objective.” --- This claim seems empty relative to any other alternative in the literature.  I would suggest removing this sentence altogether.

The introduction to geometric algebra and its notation on page 3 is rather terse.  I doubt this is a tool that a typical ICLR reader is likely to know, even if they’re working on 3D problems.  I would suggest making a more intuitive (but still compact) introduction to the relevant notions in the paper.

The notation at the beginning of section 3.1 was hard for me to conceptualize.  Perhaps an illustration would help.  Has the term “feature grid” been defined anywhere?  Concretely, how are the variables g_{i(jk)} stored/represented?  What is a “basis element” in this context?  Alternatively, it might be useful to simply give an equation that maps a 3D coordinate to the value of its feature as predicted by the proposed architecture.

In eq(4), what is the order of operations relating * to \odot?

“Full implementation details are available in our code, which will be released upon publication” --- in this case, I can’t actually see the implementation details during the review process.

Should I understand (3) as having some features per x/y/z coordinate independently, some features per xz/yz/xy pair, and and some features per xyz grid point?  So it’s just a grid with some features repeated along different axes?

Theorem 1 and 2 rely on nearest-neighbor interpolation, which seems to contradict how people would typically implement such models. What goes wrong in the general case?  Do the experiments show examples with this interpolant?

I appreciate the theoretical analysis in Theorems 1-3.  The statements of these theorems are quite long and can definitely be streamlined (for example, the statement of Theorem 2 takes half a page alone).  But, I appreciated that section 4.2 gave some intuitive discussion of the impact/interpretation of these results in terms of upsampling.

In Figure 1, why not use the GA-Planes model instead of something “similar to the structure” of GA-Planes?

The NeRF experiments here seem to involve only a single ‘lego’ scene.  This seems below the standard of experimentation in the field.  I would suggest experimenting on several examples to make sure we can be confident in the reported results.  

In general, I would have a hard time translating the high-level approaches described in this paper into equations I could implement.  For example, the experiments described in sec5 lack unambiguous descriptions of the architectures and loss functions (the sections contain only text without equations, architecture parameters, and so on), and I would struggle to articulate the difference between the convex, semiconvex, and nonconvex cases mentioned in Tables 1-2.

### Strengths
See above.

### Weaknesses
This paper provides a generic strategy for grid-based representation of volumetric features, for use in applications like NeRF where the task involves computing a spatial quantity in 3D.  The basic idea, inspired by geometric algebra, is to include features that are constant along planes/lines in addition to a feature per grid cell.  This approach in some sense generalizes past approaches, as articulated in the appendix.

Although the title/discussion claims a link to geometric algebra, it seems the connection here is somewhat superficial.  As far as I can tell, the paper does not make use of any *algebra* from geometric algebra (e.g., assorted products and geometric operations) and could be described more simply without this language.  It seems like the basic idea here is simply to drop indices from a grid-based volume representation --- e.g., rather than having all features be f_ijk we can have some features with fewer indices f_ij/f_jk/f_ik (“plane feature grids” in parlance of the paper) and f_i/f_jf_k (“line feature grids”).  Invoking geometric algebra adds complexity to the text without benefit.

I appreciated the theoretical analysis in the paper, but the results do not seem reflective of the typical use cases.  In particular the theorems require piecewise-constant interpolation between grid elements as well as a convex objective, neither of which are common practice and are quite restrictive assumptions (indeed many of the experiments in section 5 are unable to use convex objective functions).

I appreciate the ‘framework’ for understanding assorted approaches to parameterizing volumes of features, and appendix A.1 helped me translate the discussion in the paper to something more concrete.  Given the zoo of prior models articulated in past work (see page 15), however, it seems the current paper is a variation on a fairly common theme in the literature.

The experiments here begin to validate that the proposed strategy is relatively effective, although they are far from comprehensive (just a few examples drawn from standard datasets in computer vision).

For the reasons above, I am unable to suggest publication of the work at this time.  To improve the paper, I might suggest more deeply applying geometric algebra or removing it altogether in favor of simpler language, ensuring that the model and assorted objective functions can reasonably be implemented/reproduced from the text of the paper alone (or including code), and testing the proposed representations more thoroughly.

The paper claims to be the “first class of implicit neural volume representations that can be trained by convex optimization.”  I might argue that the approach outlined here is far from a typical “neural” representation, to the point that one could equally argue the same point for a grid or kernel method (if I understand sec 3.1 properly, this method relies on a grid rather than a generic neural parameterization).

Page 2:  “At the same time, any GA-Planes model can be trained by nonconvex optimization towards any objective.” --- This claim seems empty relative to any other alternative in the literature.  I would suggest removing this sentence altogether.

The introduction to geometric algebra and its notation on page 3 is rather terse.  I doubt this is a tool that a typical ICLR reader is likely to know, even if they’re working on 3D problems.  I would suggest making a more intuitive (but still compact) introduction to the relevant notions in the paper.

The notation at the beginning of section 3.1 was hard for me to conceptualize.  Perhaps an illustration would help.  Has the term “feature grid” been defined anywhere?  Concretely, how are the variables g_{i(jk)} stored/represented?  What is a “basis element” in this context?  Alternatively, it might be useful to simply give an equation that maps a 3D coordinate to the value of its feature as predicted by the proposed architecture.

In eq(4), what is the order of operations relating * to \odot?

“Full implementation details are available in our code, which will be released upon publication” --- in this case, I can’t actually see the implementation details during the review process.

Should I understand (3) as having some features per x/y/z coordinate independently, some features per xz/yz/xy pair, and and some features per xyz grid point?  So it’s just a grid with some features repeated along different axes?

Theorem 1 and 2 rely on nearest-neighbor interpolation, which seems to contradict how people would typically implement such models. What goes wrong in the general case?  Do the experiments show examples with this interpolant?

I appreciate the theoretical analysis in Theorems 1-3.  The statements of these theorems are quite long and can definitely be streamlined (for example, the statement of Theorem 2 takes half a page alone).  But, I appreciated that section 4.2 gave some intuitive discussion of the impact/interpretation of these results in terms of upsampling.

In Figure 1, why not use the GA-Planes model instead of something “similar to the structure” of GA-Planes?

The NeRF experiments here seem to involve only a single ‘lego’ scene.  This seems below the standard of experimentation in the field.  I would suggest experimenting on several examples to make sure we can be confident in the reported results.  

In general, I would have a hard time translating the high-level approaches described in this paper into equations I could implement.  For example, the experiments described in sec5 lack unambiguous descriptions of the architectures and loss functions (the sections contain only text without equations, architecture parameters, and so on), and I would struggle to articulate the difference between the convex, semiconvex, and nonconvex cases mentioned in Tables 1-2.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
2
