# DynaVol: Unsupervised Learning for Dynamic Scenes through Object-Centric Voxelization

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
Unsupervised learning of object-centric representations in dynamic visual scenes is challenging. Unlike most previous approaches that learn to decompose 2D images, we present DynaVol, a 3D scene generative model that unifies geometric structures and object-centric learning in a differentiable volume rendering framework. The key idea is to perform \textit{object-centric voxelization} to capture the 3D nature of the scene, which infers the probability distribution over objects at individual spatial locations. These voxel features evolve through a canonical-space deformation function, forming the basis for global representation learning via slot attention. The voxel and global features are complementary and leveraged by a compositional NeRF decoder for volume rendering. DynaVol remarkably outperforms existing approaches for unsupervised dynamic scene decomposition. Once trained, the explicitly meaningful voxel features enable additional capabilities that 2D scene decomposition methods cannot achieve: it is possible to freely edit the geometric shapes or manipulate the motion trajectories of the objects.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an optimization-based method for taking a monocular video as input and producing an object-centric 3D dynamic representation as output. The idea is to optimize a 3D voxel grid to learn the 3D occupancy/density field at each timestep, along with the warp that links each timestep to the zeroth timestep. Then, these occupancies are divided into a set of object representations using connected components, and then slot-based optimization proceeds, where  features associated with objects are averaged across the time axis, and per-timestep features are assigned to the objects via iterated slot attention. The representation is trained by rendering to the given views with a nerf-style setup, using a color loss, an entropy loss aiming to separate foreground/background, and a cycle-consistency objective on the scene flow fields. The results are impressive, both in simulation and in the two real videos.

### Strengths
I like this paper. It is well written, it is interesting, the method seems sensible (thought I have a few questions), and the results look good.

### Weaknesses
I have a variety of fairly low-level questions, which I hope the authors can address.

Overall I think the method would be easier to understand if the stages were presented in a more central way, instead of at the very end. After reading everything I am still a bit unclear on the meaning of an "episode".

Section 2 emphasizes that "we also consider scenarios where only one camera pose is available at the first timestamp". What does it mean for only one camera pose to be available? Camera poses are relative to something. A single pose might as well be the identity matrix.

The beginning of Section 3.1 says the method will be trained "without any further supervision", without defining any initial supervision. So I suppose the question is: further to what?

Section 3.1 introduces the number of objects N, as "the assumed number of objects". Is this manually chosen? Later on there is a connected components step, so I wonder if connected components could choose N instead.

It is unclear to me what exactly is happening in the warmup stage vs. the dynamics stage. From the names I might guess that the warmup stage does not involve any dynamics, but this is wrong, because it uses all timesteps and it also trains the forward and backward dynamics modules. The section also says "To obtain the dynamics information, we train an additional module f′ξ" -- but dynamics information is already obtained by f_ψ, so there is some mixup here, unless the authors do not see f_ψ as obtaining dynamics information. Finally, it's unclear how exactly the connected components and the "feature graph" connect with the rest of the method.

L_point seems like it is never defined, and only a citation is given. It would be great to describe in English what is happening there.

Section 3.3 seems to complain that prior compositional nerfs used an MLP to learn a mapping from position+direction+feature to color+density, and then proposes to do the exact same thing. Have I missed something here?

Overall I like the paper and I hope it can be cleaned up. The video results show that the segmentations are a little messy, and it seems like only 2 real videos are used, but still I think the paper is interesting and useful to build on.

### Questions
This is more of a personal curiosity, but: instead of learning two deformation networks (one forward, one backward) and then asking them to be cycle-consistent, would it work to learn an invertible mapping here instead? (Like with Real NVP.)

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces DynaVol, an attempt at unsupervised learning for object-centric representations in dynamic scenes. While most existing solutions focus on 2D image decomposition, DynaVol aims to offer a 3D perspective by leveraging object-centric voxelization within a volume rendering framework. It has a few steps to achieve this, including but not limited to canonical-space deformation optimization, and global representation learning with slo attention. The approach combines both local voxel and global features as conditions for a NeRF decoder. The proposed method achieves good results in a simulation environment and demonstrates its applicability in one real-world dataset.

### Strengths
1. Good attempt. The proposed DynaVol approach introduces a shift from 2D image decomposition by bringing in a 3D perspective (via NeRF). NeRF as a 3D representation beyond view synthesis is an underexplored region and I think this work makes a good effort towards this direction by doing object-centric voxelization within a volume rendering framework. Although the canonical-space deformation operation is widely seen in dynamic NeRF works, it still brings value to object-centric learning.

2. The paper is well articulated in the introduction section. I do capture the underlying motivation for the whole work, but I found a hard time understanding the two-stage training at the beginning. The authors are suggested to make the overview section and the overview figure flow better.

### Weaknesses
Dataset Limitations: My primary concern is the robustness of DynaVol when applied to intricate real-world scenes. The paper predominantly employs what can be described as a 'toy' dataset to validate its model. The observations made from this kind of dataset often fail to generalize to real-world applications. The mention of the HyperNeRF dataset application does lend some credence to its real-world viability. However, a more thorough exploration, perhaps using more diverse and challenging datasets (one or two demos would be enough), would provide stronger evidence of the model's capability.

Also, I wonder how important the background loss is in the pipeline. Will this method work without this loss? Will the slot decompose the background?

### Questions
1. Based on the results presented in Table 1, it seems that models utilizing 5 views (V=5) don't consistently surpass the performance of those with just a single view. Could the authors shed light on the underlying reason for this unexpected behavior?

2. Significance of the Warmup Stage: The paper doesn't delve deeply into the role of the warmup stage in the ablation studies. How crucial is this phase to the overall performance and efficiency of DynaVol?

3. Performance of Warmup-Stage-Only: It's intriguing to observe that the 'warmup-stage-only' variant appears to perform quite competently even though it's restricted to initial timestep observations. It's even better than other baselines reported in Table 1. Could the authors explain the factors or mechanisms behind this seemingly robust performance?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The manuscript proposes a method, DynaVol, that learns to represent dynamic scenes as decomposed into the different moving parts (objects). The input to the method is a sequence of frames and their pose.
This decomposition is learned in 3D by learning to deform a canonical volume into the 3d states at the different observation points. Slot attention on 3d voxel grids is used to learn time-invariant object representations that are deformed by the deformation field. A NERF rendering loss guides allows learning this from just the input image sequence.

### Strengths
The research direction of learning to decompose and represent a dynamic scene in terms of the motion of individual constituent parts (objects / slots) is important. 

The results on simulated data are encouraging (although there are only a few scenes shown) and show cases where the model is indeed able to nicely separate out the different moving parts of the scene.
Figure 4 exactly captures the advantage of the proposed dynamic object-centric scene representation in comparison to 2d methods (SAM): being able to represent unobservable parts of an image.

The proposed approach to dynamic scene representation has fundamental advantages as demonstrated by the qualitative results on scene editing (removing objects; modifying dynamics).

The visuals and writing in the manuscript are of high quality (the clarity could be improved - see weaknesses).

### Weaknesses
The proposed model DynaVol is complex. The text and the architecture figures were not easy to follow. Especially the parts about the slot updating and training are a bit opaque to me still. There are various unexplained variables in Fig. 1 which means the figure doesnt really add much to explaining the concepts and architecture to me.

One weakness is that DynaVol has to be overfited to each individual single scene. As such this is similar to NERF and okay. But when comparing such an overfit model to a fully generalizing model like SAM caution has to be use to clarify very precisely. 

The experiments do suggest to me that DynaVol works well on easily segmented objects (from the simulation) but on real sequences DynaVol does not much outperform other methods. The small set of sequences evaluated in sim and real weakens the claims.

### Questions
Do I understand correctly that there is only one occupancy grid at t=0 and the other ts are reconstructed using the deformation field? A query at time t is warped back to t=0 and then interpolated into the feature volume?

Where is the GRU in Fig 2?

For the NERF rendering is it correct that the occupancy comes from the occupancy grid and the color comes from the slot features? Why this choice and not push occupancy into the slot features too?

I couldnt find the per-point color loss in the DVGO paper? What am I missing?

What happens without the warmup phase? 

How are the occupancy grid and the deformation function represented? Just dense values on a grid? what resolution?

How is the feature graph computed after warmup?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an unsupervised learning method for 3D dynamic scene capture and decomposition. The presented method, DynaVol, utilizes a canonical NeRF as well as a time-conditioned implicit warping field for modeling a 3D dynamic scene. Learning such a representation uses a monocular video together with multi-view observation of a static frame, and several other objectives designed for retrieving better geometry and enforcing temporal consistency. Comparisons with previous state-of-the-arts are shown on the tasks of novel view synthesis and 3D scene decomposition, and improved results are reported.

### Strengths
* Experiment

 Extensive experimental results are shown on tasks like novel view synthesis and 3D scene decomposition. Improved results are achieved compared to many existing baselines and state-of-the-arts.

### Weaknesses
 * More insights from ablation study?

It is really good to see that the authors conduct a lot of ablation study on the work. However, some of them only consist of a chart with statistics, while lacking some insight analysis on them. It would further improve the quality of this work if more insights are discussed there.

* Novelty?

The method proposed in the manuscript is pretty interesting, although it would be great to highlight the novelty and difference between the proposed method and previous literature. For example, on the dynamic modeling side, what is the relationship with [1, 2]. On the representation side, the design of volume slot attention is also not very well justified. It would be great if more insights and ablations are provided for the that part of design.

* Introduction

In the introduction part, I feel the importance of the problem that the paper is working on is not well explained. Instead, the author directly starts to focus on what method is proposed and what experiments are conducted. It would better enhance the quality of the paper if more background and impact of solving this problem are provided and discussed.

### Questions
* Supervision?

Although not a very big concern, the number of objects N seems to serve as input to the pipeline. This semantic could serve as additional supervision with strong prior, especially to the task of scene decomposition. It would be interesting to see how to address the problem of automatically determining the number of objects in the scene.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
