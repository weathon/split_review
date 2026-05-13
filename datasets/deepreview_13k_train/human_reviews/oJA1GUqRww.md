# Faceshot: Bring any Character into Life

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Portrait animation generates dynamic, realistic videos by mimicking facial expressions from a driven video.
However, existing landmark-based methods are constrained by facial landmark detection and motion transfer limitations, resulting in suboptimal performance. In this paper, we present \emph{FaceShot}, a novel training-free framework designed to animate any character from any driven video, human or non-human, with unprecedented robustness and stability.
We achieve this by offering precise and robust landmark results from an appearance-guided landmark matching module and a relative motion transfer module.
Together, these components harness the robust semantic correspondences of latent diffusion models to deliver landmarks across a wide range of character types, all without requiring fine-tuning or retraining.
With this powerful generalization capability, FaceShot can significantly extend the application of portrait animation by breaking the limitation of landmark detection for any character and driven video.
Furthermore, FaceShot is compatible with any landmark-driven animation model, enhancing the realism and consistency of animations while significantly improving overall performance.
Extensive experiments on our newly constructed character benchmark CABench confirm that FaceShot consistently surpasses state-of-the-art approaches across any character domain, setting a new standard for open-domain portrait animation. 
Our code will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
FaceShot achieves precise landmark matching and robust motion transfer by introducing an appearance-guided landmark matching module and a relative motion transfer module. The landmark matching module utilizes the semantic correspondences of a latent diffusion model to extract consistent and robust landmarks from various types of driving videos. Subsequently, the motion transfer module effectively conveys the relative motion information of these landmarks to the target character, enabling diverse and realistic character animation without needing fine-tuning or retraining.

### Strengths
1.FaceShot offers a potential solution for portrait animation in open domains. Traditional methods often fail with non-human characters, such as emojis, animals, and toys, due to their facial features significantly differing from humans. This results in landmark detection failures and compromised animation quality. FaceShot addresses this by providing accurate landmarks, making animations for non-human characters more reasonable and effective.
2.FaceShot can be integrated as a plugin into other landmark-based animation-driven models, enhancing its scalability across various animation tasks.
3.FaceShot achieves precise landmark matching by leveraging semantic correspondences within latent diffusion models.

### Weaknesses
1. I like this application scenario as it effectively utilizes the correspondence between the features and positions of diffusion for landmark detection. However, without training, the effectiveness seems limited. See Question 7.
2. The cross-domain expression driving has been effectively improved, but the pose driving remains limited. However, this is a common drawback of 2D methods. See Question 2.

### Questions
1. Is the purpose of the appearance gallery to match the target image with a composite reference image (from different images)?
2. What is the structure of the LandmarkMotionTransfer module? Can you describe the working principle of this part?
3. On the CABench benchmark proposed by the authors, Faceshot achieved SOTA performance. Is this a test benchmark for the same identity (character)? Besides qualitative experiments, how is the effect of cross-identity motion measured? What are the quantitative results for same-identity and cross-identity driving on traditional facial video datasets, such as voxceleb1 or 2, or HDTF?
4. Is the 3DMM using an iterative fitting algorithm based on LSFM? If so, it seems intuitive that it might not perform well on video sequences. Additionally, how many iterations does it take? Have algorithms like DECA, Deep3D, 3DDFAv2, etc., been tested for performance on video sequences?
5. Which algorithm is used for annotating the landmarks in the reference images?
6. How is the stability and robustness of landmarks prediction with training-free?
7. In Figure 7, is the poor driving effect of the eyes in the first row and fifth row due to the difficulty in detecting round eyes?
8. How is the time efficiency? What is the specific time for each step, and what is the frame rate for animation driving?
I am willing to improve my score after addressing any questions.

### Soundness
3

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
This paper introduces an innovative training-free framework, FaceShot, designed to animate any human or non-human character using any driven video. The FaceShot framework is built on three key components: 1) an appearance-guided landmark matching module, 2) a relative landmark motion transfer module, and 3) a character animation model. Together, these components enable precise landmark detection and stable animation generation across diverse character types. In addition, the authors present CABench, a standardized benchmark dataset specifically created to evaluate distribution-agnostic portrait animation techniques. The techniques introduced by FaceShot represent a significant advancement in the field of open-domain portrait animation, overcoming limitations in existing methods and expanding animation capabilities to a broader range of characters

### Strengths
1. Broad Character Adaptability: FaceShot incorporates an "appearance-guided landmark matching module" that enables it to handle a wide variety of characters, including non-human characters like emojis, toys, and animals, without requiring retraining. This innovation significantly extends the model's applicability, allowing it to generate stable animations across diverse domains.

2. Stability in Animation Generation: FaceShot demonstrates high stability in handling non-human characters, accurately capturing subtle expression changes like eye blinks and mouth movements to produce smooth and coherent animations. This stability is mainly due to the "relative motion transfer module," which ensures continuity of facial features in the landmark sequence generation, resulting in consistent animation effects.

3. Introduction of the CABench Dataset: FaceShot not only offers a novel animation generation method but also introduces the CABench dataset, providing a standardized tool for evaluating animation performance on non-human characters. This dataset includes various character types and emotion-driven videos, offering a more representative testing environment for future research and filling a gap in the diversity of characters in current datasets.

### Weaknesses
Many details are missing. Without specifying the experimental setup, including the device used and the details of the training parameters (such as the learning rate), it is unclear how much time overhead is introduced by incorporating the appearance-guided landmark matching module and the relative motion transfer module. Additionally, the resolution of the generated videos has not been mentioned. See questions for details.

Specifically, the paper lacks crucial information regarding the implementation of the appearance-guided landmark matching module. The method for matching the target image to the appearance gallery is not clearly defined, making it difficult to assess the robustness and accuracy of this step. Furthermore, the description of the relative motion transfer module is vague, particularly concerning the determination of local coordinate systems and how they adapt to motion, which raises concerns about the precision of motion transfer. The absence of details about the CABench dataset, such as the specific number of videos per emotion and the distribution of intensities, limits the ability to evaluate the dataset's representativeness and utility. Finally, the computational overhead of the proposed method, especially when used as a plugin, is unclear, which is critical for practical applications.

### Questions
1. How to match I_{tar} with the closest domain in the appearance gallery G, and what evaluation metric is used? This step is not indicated in the pipeline.

2. In the relative landmark motion transfer section, I have three questions. First, how to get the angle of the global rectangular coordinate system? Second, how to determine the origin and angle of the local rectangular coordinate system of each part of the face? Third, when motion occurs, the origin and angle of different local coordinate systems in the reference and target image will also change. How to deal with this? 

3. CABench is considered a significant contribution of this paper, but the dataset details are missing. It would be nice to provide a detailed list of the character types and their quantities included in CABench, specifying the specific emotions and intensity distributions of the driving videos, and the number of videos for each emotion. Additionally, what is the total number of images and video frames in the dataset, and do you need any preprocessing operations performed on the dataset, including the resolution and format of the images?

4. When FaceShot is a plugin for landmark-driven animation models, will it introduce additional computation and time overhead?

5. Can Faceshot achieve real-time interaction?

6. In the pipeline, it would be nice to give some example text prompts in the  “Appearance Guided Landmark Matching” step.

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
2

### Summary
The paper proposed a training free framework for animating any input character (human or non-human) from any human face driven video, by predicting facial landmarks for the input character. Extensive qualitative results showcase the effectiveness of the proposed method.

### Strengths
1. The proposed training-free architecture is easy to follow and and the objective as in Eq(4) is straightforward.
2. The introduced Appearance Gallery consisting of rich semantic meaningful regions benefits facial expression&motion modeling, matching and transfer. 
3. The qualitative results look good and promising, especially the comparisons in Fig.12.

### Weaknesses
It seems that the proposed method does not significantly outperform LivePortrait in terms of both qualitative and quantitative results, as shown in Table1 and videos from Anonymous website.

It's unclear how the method handles occlusions or extreme head poses in the driving video, which could lead to inaccurate landmark predictions and consequently, poor animation quality. The paper lacks a detailed analysis of failure cases, which would be beneficial for understanding the limitations of the approach. Furthermore, the method's reliance on a pre-defined set of semantic regions in the Appearance Gallery might limit its ability to generalize to characters with highly unusual or complex facial structures. The appearance gallery, while beneficial, could also introduce biases if the semantic regions are not universally applicable across diverse character designs. The paper does not discuss the computational cost of creating and maintaining the Appearance Gallery, which could be a significant overhead.

### Questions
1. Though reported in Table 2, how long does it take for generating a single frame or the same number of frames in inference compared with other methods. e.g.  LivePortrait (with the same number of inputs)?
2. In Figure 12, why the numbers of generated landmarks with the proposed method are not consistent across different figures?
3. Some black or purple texture artifacts are witnessed on the generated images of the pink figure shown in Figure 1 (on the second row and second colume), which is more severe in its corresponding video (at the very end of the website, the 5th video from left to right). Is that because of the proposed method itself cause I haven't seen such issue on other compared methods?
4. Are there any generated videos longer than five seconds?

### Soundness
3

### Presentation
3

### Contribution
3
