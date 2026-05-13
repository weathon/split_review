# Novel View Acoustic Parameter Estimation

- Decision: Reject
- Scores: 6, 6, 3

## Abstract
The task of Novel View Acoustic Synthesis (NVAS) -- generating Room Impulse Responses (RIRs) for unseen source and receiver positions in a scene -- has recently gained traction, especially given its relevance to Augmented Reality (AR) and Virtual Reality (VR) development.  However, many of these efforts suffer from similar limitations: they infer RIRs in the time domain, which prove challenging to optimize; they focus on scenes with simple, single-room geometries; they infer only single-channel, directionally-independent acoustic characteristics; and they require inputs, such as 3D geometry meshes with material properties, that may be impractical to obtain for on-device applications.  On the other hand, research suggests that sample-wise accuracy of RIRs is not required for perceptual plausibility in AR and VR.  Standard acoustic parameters like Clarity Index (C50) or Reverberation Time (T60) have been shown to capably describe pertinent characteristics of the RIRs, especially late reverberation.  To address these gaps, this paper introduces a new task centered on estimating spatially distributed acoustic parameters that can be then used to condition a simple reverberator for arbitrary source and receiver positions. The approach is modelled as an image-to-image translation task, which translates 2D floormaps of a scene into 2D heatmaps of acoustic parameters. We introduce a new, large-scale dataset of 1000 scenes consisting of complex, multi-room apartment conditions, and show that our method outperforms statistical baselines significantly.  Moreover, we show that the method also works for directionally-dependent  (i.e. beamformed) parameter prediction.  Finally, the proposed method operates on very limited information, requiring only a broad outline of the scene and a single RIR at inference time.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper explores estimating room impulse response (RIR) given a spatially distributed pair of sources and receivers' positions.
In particular, the paper proposes a novel way of predicting acoustic maps in the formulation of image-to-image translation, given floor maps and acoustic parameters as input. The proposed method has been evaluated in two datasets, namely SoundSpace and MRAS, constructed to reflect realistic multi-room scenes of typical indoor apartments. Five existing methods have been compared to the proposed method.

### Strengths
I find the formulation of RIR estimation into image-to-image translation interesting and novel. The paper is well structured and clearly addresses the problem and limitations of the existing approach. The evaluation result is convincing, and the proposed dataset also seems to reflect a more realistic environment of common apartments than the existing dataset, SoundSpace.

### Weaknesses
The authors claim that the proposed method predicts acoustic parameters of 'unseen scenes'. Although I understand the context, it sounds like an overclaim. The proposed model takes a floor map as a geometric input, which requires a full 3D mesh of the scene. Given that the floor map, which requires significant work to build, is already given as input, I feel that it is not an entirely unseen scene. It would make the purpose of the paper clearer for readers by correctly addressing what the proposed aims to do in this regard. I would like to hear what the authors think about this.

### Questions
(1) Regarding the weakness that I mentioned, how costly is it to extract the full mesh of the scene to generate the floor map? 

(2) The author mentions that the floor map is constructed by slicing at certain heights. How were the certain heights modelled? What is the impact of the different slicing heights?

(3) What are the parameters of low-pass filters?

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
The paper introduces a new task, Novel View Acoustic Parameter Estimation (NVAPE), which can be then used to condition a simple reverberator for arbitrary source and receiver positions. The motivation of bringing this task out is to address existed challenges such as poor generalization to new scenes, poor handling of complex geometries, ignoring of directional dependencies, and strict constraint on the input for the previous acoustic modeling methods. As solution, the paper proposed an image-to-image translation style framework to translate floormaps into heatmaps of acoustic parameters. They claim the proposed method can outperform statistical baselines and work for directionally-dependent parameter prediction, requiring only a broad outline of the scene and a single RIR at inference time. A new, large-scale dataset of 1000 scenes consisting of complex, multi-room apartment conditions is also proposed by this paper as the benchmark.

### Strengths
+ This paper proposes an interesting task that estimating acoustic parameters given the layout and one reference impulse response. The paper proofs it's feasible to use an image-to-image way to correlate the floormap with the acoustic heatmap and is able to generalize over new rooms as well. It's insightful and potentially can help with other acoustic-visual tasks.

+ The paper introduces a challenging dataset of 1000 scenes consisting of complex, multi-room apartment conditions. The dataset can be good resource for the acoustic learning community.

+ Experiments and visualization analysis show the effectiveness of the proposed method. Details of dataset creating and method implementation are clearly described.

### Weaknesses
 - Problem Scope. Previous acoustic modeling methods usually output the impulse response wavform, so they can convolve with source sound with the impulse response to render virtual sound that matches the target environment and view pose. However, how to bridge the predicted acoustic parameter with the sound rendering is not explained in this paper. If not targeting on the sound rendering, regardless of presenting this as main application in the introduction, what can we use the parameters for? If sound rendering is indeed the final target, it will be better to include some results, conditioning on the acoustic parameter to generate IR and even target sound, comparing with baselines. The paper should clarify the connection between the predicted acoustic parameters and their practical use in sound rendering, as the current presentation leaves a gap in understanding how these parameters are utilized to achieve the stated goal of realistic acoustic environments. Without a clear demonstration of how these parameters are integrated into a sound rendering pipeline, the practical value of the proposed method remains unclear.

- Fair Comparison Concerns: In the Table 2, the paper compares the proposed method with baselines INRAS and NAF. Though it shows largely accuracy boost, the fairness seems to be an issue. It mentions the acoustic parameters are obtained from predicted IR of INRAS and NAF. However, for fair comparison, we can also compare with these methods by adapting their output from IR wavform to acoustic parameters as well (aligned with the proposed method), at least for INRAS and other baselines such as FewshotRIR [1] that support multi-scene learning. After supervised training and then compare will be more fair. Instead of using an image2image way conditioned on layout and reference IR, these methods rely on modeling the relationship between the target location and references (bounce points or reference locations). By comparing like this, we can better show the advantageous of the proposed method on learning the acoustic parameters. The comparison should involve training the baseline models to directly predict the same acoustic parameters, rather than extracting them from predicted impulse responses. This would provide a more direct and equitable assessment of the proposed method's ability to learn acoustic parameters from the given inputs, and highlight the specific advantages of the image-to-image approach over methods that model relationships between target and reference locations.

### Questions
Please check the weaknesses section for most of the concerns.
For the task, shall we call it "novel view" acoustic parameter estimation? Since it's only location based, and not condition on any target orientation.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed a novel novel view acoustic parameter estimation framework by learning a floor plan like acoustic heatmap. Instead of requiring to know full 3D geometry, this framework uses a 2D floormap and room impulse response (RIR) for inference, translating them into heatmaps representing acoustic parameters. Apart from this task, a new dataset with diverse apartment layouts was used to demonstrate that the proposed model outperforms baselines, offering efficient parameter predictions for varied source-receiver positions in complex, multi-room scenes​. The new dataset is built from SoundSpaces 1.0 simulator, requiring highly dense RIR sampling.

### Strengths
1. This paper discusses a challenging yet important task -- estimating acoustic parameters.

2. The introduced large-scale new dataset for future exploration (although I have concerns regarding this dataset)

### Weaknesses
1. **Motivation**: While it seems natural to use an image-to-image conversion to learn acoustic heatmap from 2D floorplan map, the motivation of using 2D floorplan as input to learn acoustic parameter isn't convencing. First, 2D floorplan input used in this paper is a degragated representation of the 3D room scene. Furthermore, this paper uses small-resolution (128x128) 2D floorplan as input without explicit room constructional detail. Essentially, the acoustic heatmap's goal is to predict RIR for arbitrary source and receiver position, I didn't the see the need to format it as floorplan like map. Second, obtaining 2D floorplan map is a challenging task in real-scenario, which makes the argument "learning from floorplan map" less practical in real world where the 3D mesh of the a room scene is usually missing. What is the advantage of using 2D floorplan to learn acoustic parameters?

2. **Acoustic Parameter Definition Unclear**: throughout this paper, it claims the task is to estimate the acoustic parameter for novel view, but in essense it estimates RIR. Equalizing RIR with acoustic parameter is confusing, as acoustic parameter usually indicates all relevant characteristics for a room scene that govern sound propagation behaviour, such as room layout, construction material and furniture. RIR is the overall resultant of all the acoustic parameters. To me, this work estimates the RIR, not directly the acoustic parameter. What is the concrete definition of acoustic parameter in the context of this paper? How is it related to RIR?

3. **Acoustic Heatmap**: Based on acoustic heatmap visualization in this paper, it looks like loudness map that depends on the source emitter position (Figure 1 and Figure 3 in this paper). How are all acoustic parameters encoded in the heatmap needs more clarification. The acoustic parameters should be independent on if there is any source eimitter. If so, how to understand the acoustic parameter via heatmap perspective? How does each channel of feature in the learned heatmap related to acoustic parameters?

### Questions
1. Read the weakness section.

2. L220-222: These parameters are computed from RIRs captured at a discrete set of receiver locations. **What are these parameter?**

3. Equation 4, 5: I read this paper a couple of times but still confused, the input is the stack of 5 maps (Fig. 3), what is the corresponding ground truth heatmap? **How to obtain the acoustic heatmap during training?** This echoes my confusion of the definition of acoustic parameters heatmap.

4. **MRAS dataset**: L320-323, it writes: it includes a large collection of scene geometries. What collections? It is the same dataset of SoundSpace 1.0 introduced dense RIRs on Replica or Matterport 3D room scene?

5. **Experiment**: this paper writes in L62, previous work is limited by poor generalization to new scenes. But the experiment didn't explicitly discuss the generalization capability of their framework. Moreover, experiment on real-world data is missing, which makes the framework less convencing.

6. **Missing relevant work discussion**, e.g. [1] Y. He, et al., Deep Neural Room Acoustics Primitive, ICML24. [2] Das, O. et al., Room impulse response interpolation from a sparse set of measurements using a modal architecture. ICASSP 2021.

### Soundness
2

### Presentation
2

### Contribution
2
