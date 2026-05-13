# MapLearn: Indoor Mapping using Audio

- Decision: Reject
- Scores: 3, 5, 6, 5

## Abstract
Cameras and LIDARs are established methods to generate the map (or floorplan) of an indoor environment. This paper investigates the feasibility of using audio to learn the map. We aim to transmit audio beacons from a mobile device (say a smartphone) and record its reflections from the environment. Assuming known user locations, and recordings from multiple locations along walked paths, we aim to learn the 2D floorplan of the area. We use a conditional GAN (cGAN) architecture but prevent it from over-fitting using knowledge of indoor signal propagation. We pre-train our model on simulated data -- thousands of high-fidelity audio measurements on hundreds of synthetic floor plans -- and then test on 4 real environments in our home and office buildings. Results show that the generated maps are fairly accurate (in terms of precision and recall) even though no training was performed in real rooms. We have assumed clutter-free rooms; coping with clutter remains a topic for continued research.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a map construction system by using acoustic signals. The problem is interesting and useful, and can support lots of location based services.

### Strengths
An interesting problem, to support location based services. The GAN architecture to improve robustness against acoustic measurement noises.

### Weaknesses
There are some recent work using smartphone's acoustic signals to measure the environment and construct the map, e.g., BatMapper, the only difference is the mode, thus please compare with some recent work.
I'm not sure how they train the GAN network, especially how they collect the ground truth. BatMapper doesn't need any ground truth. If they need the ground truth, it will harm its application and user experimence.
Their evaluations are based on simulation, and why not implement a prototype and conduct experiment in real buildings.

### Questions
1. How to gather the ground truth, and what is the usage scenario.
2. Comparison with recent work, e.g., BatMapper.
3. Develop a prototype and test in real buildings, instead of simulation.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors aim to generate floorplans of indoor environments from audio transmitted from a mobile device. They make a few assumptions –
1.	Known locations of the multiple walking paths where recordings were made.  

2.	The rooms are devoid of clutter.

3.	The rooms are rectangular.

However, they do not assume complete coverage of the home and show results on 60% of the grid cells. The conditional GAN model (using a cGAN loss + certain audio processing priors) is pre-trained on simulated floor plans, and then tested on 4 real environments. The specific novel aspects of the architecture are –

1.	The paper suggests generating a hint_map based on the principles of signal propagation in reflective environment (an echo is a attenued time-delayed copy of the source signal). The authors use this fact to generate reflector circles corresponding to the peaks (impulse response) of the deconvolutions between the source and the echo.

2.	Instead of the raw impulse response, the paper suggests using the envelope of the response as that is less noisy.

3.	The impulse response is rotationally invariant, hence the paper inputs 4 measurements to the encoder to resolve this ambiguity.

### Strengths
1. The problem statement is novel and it appears that it has not been tackled earlier.

2. The authors propose exploiting audio and floorplan specific priors to generate floor plans. This is an interesting direction. 

3. The end-to-end evaluation is reasonable.

### Weaknesses
- I'm not convinced about the motivation and practicality of this problem.
     - While I admit there are applications wherein privacy dictates that camera or LIDARs can't be used, wouldn't the same privacy concerns persist if an audio beacon is used? 
     - What is the range of audio frequencies that this method can operate on (does it need to operate in the audible range)? I would imagine the application is expected to not operate in the audible range, please correct me on this if I'm wrong.

- Results in Section 4.1 is unclear. What does the HintMap baseline indicate? Isn't Hint map part of the MapLearn method? If so, what are the contribution of the rest of the components (ablations)?
- Question about the metrics and visualizations, the paper does not motivate why the improvement matters.
   - If an approximate floorplan suffices for downstream application(s), does the improvement in P(d) and R(d) matter? 
   - It's difficult to interpret images in Fig 10, I'm not sure if Row 2 is better than Row 3 or vice versa.

- Demonstrating an application where a more accurate floorplan from audio is needed would be useful in showing the benefit of the improvement in floorplan estimate (as the goal is anyways to obtain an approximate floorplan).

### Questions
Please answer the questions listed in Weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tries to reconstruct the floorplan of an area via audio reflections. In detail, by accepting recorded audio reflections and corresponding locations as input, a conditional GAN is used to predict the floorplan contour as output. Experiments of the model trained on synthetic dataset gives promising accuracy on real datasets.

### Strengths
1.	Interesting idea. Cameras and Lidars are generally used to reconstruct the map of an environment. In the paper, the authors propose to use audio reflections to recover the floorplan of an environment. The idea is different to previous methods and sounds very interesting.

2.	Robust solution. Predicting the indoor map from only audio reflections is very challenging due to limited and sometimes noisy information in the audio reflections. Therefore, the authors introduce the Hint map to recover a coarse geometry of an area according to the time of receiving responses. The Hint map then is used to replace original signals as the input to cGAN, making results more accurate and robust.

3.	Individual room estimation. It is really difficult to recover the whole area all at once, so recovering one room individually and stitching rooms into floorplan with known locations should give better results.

### Weaknesses
1.	Limitation. My major concern is the limitation of the idea. Audio signals contain much less information than visual or lidar signals for map reconstruction, which means the floorplan generated from audio reflections are not that accurate as also shown in the experiments. Moreover, audio reflections vary in environments with different painting materials, decorations, and objects in the area. These factors may further impair the accuracy and generalization. Specifically, the long wavelengths of audio signals inherently limit the spatial resolution achievable, making it difficult to discern fine details in the environment. This is further compounded by the fact that different materials exhibit varying acoustic properties, leading to inconsistencies in reflection patterns. For example, a room with heavy curtains will have significantly different audio reflections compared to one with bare walls, impacting the robustness of the mapping process.

2.	Pose accuracy. In the paper, the location is obtained from IMU. However, IMU is very sensitive to error accumulation especially in large rooms. Currently, as GPS is not available in indoor environments, visual information is the best to obtain location information. My concern is that if we have visual information, why don’t we just recover an accurate map with SfM techniques from images? Note that audio reflections only provide very coarse floorplan. The reliance on IMU for pose estimation is a significant limitation, as IMU drift is a well-known problem. Even with sensor fusion techniques, the accuracy of IMU-based localization degrades over time, especially in the absence of external references. This positional uncertainty directly affects the accuracy of the reconstructed floorplan, as the audio reflections are mapped to incorrect locations. Furthermore, if visual information is available, it would be more effective to use established Structure from Motion (SfM) techniques to create a detailed 3D map, rendering the audio-based approach less compelling.

3.	Applications of floorplan contour. In Section 1, the authors mention that ‘a simple floorplan contour may suffice in most cases’ but don’t provide examples. Maps reconstructed by cameras and Lidars can be used for localization which is the key technique to AR/VR and robotics navigation. It is not very clear to see how to use floorplan contour in real applications. The paper lacks a clear explanation of the practical applications of a coarse floorplan contour. While a detailed 3D map can be used for precise localization and navigation, the utility of a simple floorplan contour is not well-defined. For example, it is unclear how this type of map could be used in AR/VR applications or for robot navigation, where precise spatial understanding is essential. The authors need to provide more concrete use cases to justify the value of the proposed approach.

### Questions
Please see Weaknesses for details.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, a MapLearn method is proposed to generate indoor floorplan maps from audio signals by learning a conditional GAN. Instead of directly conditioning the GAN on the audio signals, the authors seek to derive spatial information from audio signals. Results on simulated and real-world data validate the effectiveness of MapLearn to some extent.

### Strengths
++ A spatial hint map derived from audio signals attains geometric information.

++ Using the envelope to mitigate the signal noise is insightful.

### Weaknesses
1) How is the envelope of h calculated?

2) What does "patch" mean for the patch GAN discriminator?

3) Could the authors add the precision and recall values of each estimated floor plan map to the third and fourth rows of Figure 10?

4) What if the MLP for corner prediction from the envelope is removed and directly using the envelope along with the hint map as the input?

5) Will the data and code be released for reproducibility?


Minor:
-- page 2: "it's introduction"

-- page 4: "a MLP"

-- page 5: "a MSE", "a L1"

-- Figure 5: "cGAN outpu"

### Questions
See the weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
