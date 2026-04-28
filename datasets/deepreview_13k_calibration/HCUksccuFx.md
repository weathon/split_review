# PuppetMaster: Scaling Interactive Video Generation as a Motion Prior for Part-Level Dynamics

- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
We present \method,
  an interactive video generative model that can serve as a motion prior for \emph{part-level} dynamics.
  At test time, given a single image and a sparse set of motion trajectories (\ie, \emph{drags}),
  \method can synthesize a video depicting realistic part-level motion faithful to
  the given drag interactions.
  This is achieved by fine-tuning a large-scale pre-trained video diffusion model, for which we propose a new conditioning architecture to inject the dragging control effectively.
  More importantly, we introduce the \emph{all-to-first} attention mechanism,
  a drop-in replacement for the widely adopted spatial attention modules,
  which significantly improves generation quality by addressing the appearance and background issues in existing models.
  Unlike other motion-conditioned video generators that are trained on in-the-wild videos and mostly move an entire object, 
  \method is learned from \datasetF, a new dataset of curated \emph{part-level} motion clips.
  We propose a strategy to automatically filter out sub-optimal animations and augment the synthetic renderings with meaningful motion trajectories.
  \method generalizes well to real images across various categories and outperforms existing methods in a \emph{zero-shot} manner on a real-world benchmark.
  See our project page for more results: \href{https://vgg-puppetmaster.io/}{\texttt{vgg-puppetmaster.io}}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors present a framework called PuppetMaster for generating videos with part level object motion from a single image. The approach uses "drag" inputs to control fine grained parts of the generated video. This approach is trained on the Objaverse-Animation-HQ dataset that contains videos with part level motion annotation. State of the art quantitative performance is demonstrated on the videos generated for various classes (animals, humans, objects).

### Strengths
1. **Clarity**: The paper is well written with adequate attention to detail. All the design components are explained in detail to aid in reproducibility. 
2. **Result Quality**: The generated videos show improved quality over baselines with similar drag controls. 
3. **Comparison**: Both quantitative and qualitative performance is provided against a number of baselines. Additionally, out-of-domain performance on the Human3.6 datasets shows the efficacy of the approach.
4. **Ablations**: The provided ablations highlight the need for the all-to-first attention and the right parameterization needed to represent the drag constraints.

### Weaknesses
 1. **Claims of Novelty**: The authors claim the "all-to-first" attention. Although not previously demonstrated in its exact form. The mechanism is essentially a variant of cross attention looking at KV pair from just the first frame. To that the claim that authors present a "novel all-to-first attention can be softened. For instance, one can highlight the finding of all-to-first attention while emphasizing that the variant of cross-attention that always looks at first frames is better than no attention at generating videos with fine grained part control.

### Questions
1. What is maximum number of frames that can be generated ? Can the all-to-first attention be replaced with a full 3D attention for better performance?
2. How is the performance of the framework on non articulated objects? In particular, providing a video example of a non articulated object along with arbitrary drags is helpful to demonstrate the framework's default behavior. 
3. What happens when the drag condition input to the framework is zero? Does the network generate a video with arbitrary motion or just a static image? Showing an example of this setting would be helpful to understand "unconditional" synthesis  from the network.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents PuppetMaster, a conditional 2D video generation model that takes an reference object image and some conditional input drags then synthesizes a video with part-level object dynamics. The authors finetunes an off-the-shelf video diffusion model and extend it to encode input conditional drags. Additionally, they propose all-to-first attention method to remove the artifacts when generating out-of-domain video and improve the quality. They also made their own dataset, Objaverse-Animation-HQ, with data curation from Objaverse dataset. The authors argued that the proposed method generalizes well on real images and outperforms in real-world benchmarks in a zero-shot manner.

### Strengths
1. The motivation of the paper to generate object animation given a reference object image and user-controllable drag condition seems practical. Compared to the existing methods that generate a static image of the final-state of objects, the proposed method can produce fine-grained object motion as a video.

2. The numerical experiments are conducted in rigorous validation by retraining the comparable method (DragAPart) with an identical data setting as the proposed method. To validate the accuracy of part-level dynamics, the authors introduce the 'flow error' metric by computing errors between predicted and ground-truth point trajectories.

### Weaknesses
1. Insufficient generation quality: Although the authors leverage and finetune the video foundational model (Stable Video Diffusion), the generated video quality is not sufficient to determine that the learned model well-captures object dynamics. In the video results provided by the authors in supplementary materials, the generated results do not preserve the ground-truth object's appearance details, e.g., the generated object colors are changed in every frame (flickering effect). The reviewer wonders if the authors consider these low temporal smoothness problems and make any solution in the proposed method.

2. Limited qualitative result: The reviewer thinks that the authors should provide more qualitative results compared with DragAPart. Although DragAPart is a method that generates a static image, the video results can be obtained by dense sampling on the trajectory and defining fine-grained drag conditions. The reviewer found two samples in the supplementary document, but the reviewer thinks that more diverse object samples should be reported in the main paper.

### Questions
1. In Sec. 5.1, the authors argue that the proposed model obtains smaller errors when averaging all foreground points (L412). However, the reviewer thinks that the flow error is smaller with the averaged conditioning points. It would be helpful if the authors could provide more explanation and analysis of the results.

2. In Table 2, the authors report the ablation study results. In models A and B, the reviewer wonders why the authors do experiments without an end location of the drags. Is it possible to encode input drags without an end point? It would be great if the authors give more explanation of baseline models in ablation studies. 

3. Impact of drag modulation with scale: The authors argue that utilizing the adaptive normalization layer helps to improve the generation quality. The reviewer needs more explanations about the authors' design choices.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the problem of generating videos controlled by drag. The key idea is to take the pre-trained stable video diffusion and fine-tune it by conditioning it on drag control. They used all-to-first attention to improve the consistency between the reference images and video frames. A dataset with paired drag input and output videos is collected while building upon the Objaverse animation dataset.

### Strengths
First, the collected dataset could be helpful for further study in this direction. 
Second, compared with previous works such as DragAPart, which used an image generation model, it makes more sense to use pre-trained video diffusion to generate temporal consistent videos.

### Weaknesses
First, some descriptions might be confusing to understand, making it difficult to follow. For example, in line 113, "The resulting datasets, Objaverse- Animation and Objaverse-Animation-HQ, contain progressively fewer animations of higher quality." what does it mean by progressively fewer animations?  
From Lines 197-205, they mentioned there are two main challenges. However, it seems that both challenges are about injecting drag control into the pre-trained video diffusion.

Second, to my understanding, the problem itself is not quite properly defined. Given the drag input in the image space only, the input control itself is ambiguous. For example, whether the drag is supposed to zoom-in the object or manipulate part of the object is ambiguous. From my understanding, it also depends on the training set. In this case, the training is severely overfitted to the training set.

Third, the technical contributions are not clear here. Except for collecting a dataset, the technical novelty is limited. For example, the drag encoder seems to be very similar to that proposed in DragAPart. The all-to-first attention(replacing K, V in the attention) is also not new in the context of video generation or image generation, such as Consistent123.

### Questions
1) What is the difference between the drag encoder and that in the DragAPart paper?
2) Why not demonstrate the generated videos of DragAPart? 
3) What are the failure cases?

### Soundness
2

### Presentation
2

### Contribution
2
