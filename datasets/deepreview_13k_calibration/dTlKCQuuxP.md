# Neural Polynomial Gabor Fields for Macro Motion Analysis

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
We study macro motion analysis, where macro motion refers to the collection of all visually observable motions in a dynamic scene. Traditional filtering-based methods on motion analysis typically focus only on local and tiny motions, yet fail to represent large motions or 3D scenes. Recent dynamic neural representations can faithfully represent motions using correspondences, but they cannot be directly used for motion analysis. In this work, we propose Phase-based neural polynomial Gabor fields (Phase-PGF), which learns to represent scene dynamics with low-dimensional time-varying phases. We theoretically show that Phase-PGF has several properties suitable for macro motion analysis. In our experiments, we collect diverse 2D and 3D dynamic scenes and show that Phase-PGF enables dynamic scene analysis and editing tasks including motion loop detection, motion factorization, motion smoothing, and motion magnification. Project page: https://chen-geng.com/phasepgf

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper delves into the exploration of motion analysis through the use of phase-based representation, with an emphasis on large-scale, rigid-body movements, also known as macro motion. In contrast to localized and small-scale motion, macro motion operates on a broader scale, encompassing extensive spatial and temporal transitions that are easily perceptible by humans. Traditional methods often fall short in accurately capturing such features because the filter operations are primarily designed to handle low-level features.

To overcome this limitation, this paper introduces a novel approach that utilizes phase-oriented neural Gabor fields as input embedding to reconstruct the original images or 3D scenes. By a reverse optimization process, the optimized phase input can encode some useful information while keeping the periodic. As the fundamental element in the real world, some good properties of phase can be also useful in further analysis. To enhance this reconstruction and reverse optimization, various training strategies like multi-stage, deep latent, and adversarial training have been proposed. Despite the lack of extensive evaluation, these methods are expected to deliver promising results.

In the experimental section, through some examples, it shows the method can outperform some baseline methods in extracting more reliable alignment. Moreover, the properties of the phase support the smoothing and separation of motions, which can be beneficial in specific applications like magnification.

### Strengths
The story is clear, the reader can easily understand the importance of the phase and the effectiveness of the proposed method.

The idea is interesting and novel. Using the phase as the fundamental feature to describe the motion can help to understand the motion better. 

I do like the inverse optimization with the Gabor field for locating the best-aligned phase feature; the theoretical exposition is clear, straightforward, and logical; and the proofs are also clear. 

The employed coarse-to-fine generation framework and strategy effectively facilitate the learning of priors.
The results provide some evidence to support the central thesis of the paper.

### Weaknesses
While I appreciate the innovative concept presented in this paper, I believe the current version exhibits some weaknesses that need to be addressed:

Some of the exposition needs to be improved. Some details and properties are not clearly clarified. Some points need more in-depth discussion:

1. The input phase space and the details of the Phase Generator are not elaborated. As the central element in this model, it’s not clear how to initialize the number of phases, and how the current framework adapts to the diverse scene. The full phase space can be much more complex than that in those demonstrated examples. Specifically, the paper does not discuss the dimensionality of the phase space, how it relates to the complexity of the motion, and whether a fixed-size phase space can handle arbitrary motions. The paper also lacks details on the architecture of the Phase Generator, such as the type of neural network used, the number of layers, and the activation functions. This lack of clarity makes it difficult to assess the generality and scalability of the proposed method.

2. The manipulation of the phase has been mentioned a few times, but it hasn't been detailed and demonstrated further in the paper. If the phase space is manipulatable, it will be important in the model interpretability. The paper mentions manipulating the phase for motion separation and magnification, but it does not provide a clear explanation of how these manipulations are performed. For example, it is unclear what kind of operations are applied to the phase, and how these operations translate into changes in the motion. The paper also lacks a systematic exploration of the space of possible phase manipulations and their effects on the resulting motion.

3. The implementation of using Phase-PGF in the deep neural network is not described clearly enough. The paper introduces the concept of Phase-PGF but does not provide sufficient details on how it is integrated into the neural network architecture. It is unclear how the phase information is encoded and processed within the network, and how it interacts with other network components. The paper also lacks a discussion of the computational cost of using Phase-PGF and its impact on the overall efficiency of the method.

The contribution is unclear with insufficient evaluation. A more comprehensive evaluation is needed to demonstrate the boundaries of working examples, and provide more insights:
1. Quantitative evaluation: Some of the test videos are artificial. In this case, we may want to synthesize more videos that contain varying motion complexities, for a more extensive evaluation. The paper should include quantitative metrics to measure the accuracy of the motion reconstruction and the quality of the phase representation. For example, metrics such as PSNR, SSIM, or LPIPS could be used to evaluate the reconstruction quality, and metrics such as correlation or mutual information could be used to evaluate the phase representation. The paper should also include a more diverse set of test videos, including real-world videos with varying motion complexities and camera viewpoints.
2. Ablation study: An ablation study for each network module would be beneficial. The paper should include an ablation study to evaluate the contribution of each component of the proposed method. For example, the paper could evaluate the performance of the method with and without the Phase Generator, the Phase-PGF, and the adversarial training. This would help to identify the key components of the method and their impact on the overall performance.
3. Evaluation metrics: A metric to measure if the phase meets the requirements would be useful. The paper should introduce a metric to evaluate the quality of the extracted phase representation. This metric should measure how well the phase captures the underlying motion and how interpretable it is. For example, the metric could measure the smoothness of the phase, its periodicity, or its correlation with the actual motion.

Last, some existing methods use different formulations to perform similar motion analysis, it is strongly recommended to add the comparison with them. For example, some point tracking methods can also extract rigid body movements as sparse points, and using these predictions it's also possible to extract interpretable features of the motion, such as phase or other high-level descriptions. While I don't question the novelty of this paper as it employs a *unique* methodology, it would be beneficial to add more experiments and discussions on these approaches.

### Questions
Where is the boundary of the phase space this method can support? There can be highly varied frequencies in the real world, but the working range of the proposed method is unclear. It would be useful to explore these boundaries by conducting experiments with various artificial videos.

How to determine the number of phases? In some cases, there appears to be one phase, while in others there are multiple. Is it possible to use an excessive number of phases to overfit a scene? Conversely, what would be the outcome if we used a single phase for a scene with multiple objects?

The extracted phases seem to care about the frequency more compared to the amplitude variations. In the second video of Fig.2, different balls do have different spatial transitions, but they seem to share the same peak. 

There is an option to use point tracking to extract the phase from the tracking path. How does this method complement them, and in what ways does it offer unique advantages compared to other methods?

Are the extracted phases open to manipulation? For example, if we multiply the phase by a coefficient A, will the corresponding recovered image or video be amplified? It is claimed in the paper that we can manipulate, but the results seem to be missing.

### Soundness
3 good

### Presentation
3 good

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
The paper proposes to represent scene dynamics with low-dimensional time-varying phases. The representation is learned using Phase-based neural polynomial Gabor fields (Phase-PGF). The paper argues that Phase-PGF has several properties which make it suitable for motion analysis task like motion loop detection, motion factorization,  and motion magnification.

### Strengths
- The paper addresses an interesting application and is nicely written and easy to read.  
- The paper proposes a novel formulation (Phase-PGF) for scene motion.
- Phase-PGF several properties which make it suitable for motion analysis. Two properties I found interesting are :Periodicity correlation and motion separation.
- The paper show several interesting motion analysis applications like motion separation, motion factorization, motion magnifications
- The results shown seems to surpass previous work

### Weaknesses
 - Although the method is novel, I think the supporting experiments are insufficient to validate the method.
- Not enough results in the supplementary webpage. All the results, except one, are visualizing the phase. Only one result show a generated video. This is insufficient to judge the quality of the results. I would have liked to see a video of the motion separation experiment and more videos for the motion intensity adjustment. 
- Motion editing results display visual artifact
- Most of the experiments are on toy examples with simple objects or simple motion.

### Questions
- sometimes it is hard to say which phase is right. Maybe participants are just biased towards more periodic-looking signal even if it does not really match the scene motion. I wonder if there is more systematic way to evaluate this? For example, we can detect the periodicity of a given motion and then compare its frequency with the predicted frequency.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper formulates and studies a new task of macro motion analysis. To perform macro motion analysis, the authors propose to learn an implicit function with respect to point coordinate x and time t, composed of Gabor functions and phase functions, namely Phase-PGF. By studying and adjusting the phase function of the Phase-PGF, one can infer periodic motion detection, motion separation, motion smoothing and motion intensity adjustment. Additionally, in order for the Phase-PGF to be able to extrapolate to unseen motions, which is needed for motion intensity adjustment, a discriminator on decoded images is used for adversarial training. Experiments on 2D video and 3D dynamic scenes are performed. Both human preference and visual results show its effectiveness and correctness on several motion analyses tasks.

### Strengths
1. Overall, a new problem of macro motion analysis is properly formulated and approached with reasonable method, proven effective by adequate experiments.
2. Using phase functions to model dynamic scenes has advantages for motion analysis compared with other dynamic scene representations.
3. I appreciate authors experimenting with some real-captured data and the efforts of increasing image rendering quality.

### Weaknesses
1. It would be better to design some automatic metrics other than human preference. For example, trackers can be put on moving objects to obtain ground truth motions, which can be used to compare with predicted motions. For the motion intensity adjustment experiment, to evaluate the visual quality, some metrics designed for generation tasks, e.g., FID, KID, can be used. It's not clear how the phase function's parameters are optimized to match the ground truth motion, and a quantitative evaluation of this matching process is missing. Specifically, the paper lacks a clear definition of what constitutes a 'correct' phase function, making it difficult to objectively assess the quality of the learned phase. The use of trackers to establish ground truth motion would allow for a direct comparison of the predicted motion with the actual motion, providing a more robust evaluation.
2. Currently, the examples in paper and supplementary website show very simple movements, mostly periodic. I wonder how would the method apply to more complex, dynamic scenes. Not necessarily dynamic 3D scenes, more complex 2D video can also do the work. If so, can the method separate more than two motions in the scene? And can some algorithm be designed to automatically find the moving object? The paper does not address the limitations of the Gabor basis in representing highly non-periodic or chaotic motions. The reliance on a fixed set of Gabor functions might restrict the model's ability to capture complex motion patterns, and it's unclear how the method would handle scenarios where the motion is not well-represented by a combination of these basis functions. Furthermore, the paper lacks a discussion on the computational cost associated with the proposed method, particularly when dealing with complex scenes or high-resolution videos. It would be beneficial to understand the scalability of the approach and its practical limitations.

### Questions
1. Currently, the extracted motion phase is agnostic of the motion direction. Is there a way to decompose motion phases, for example, to x and y directions.
2. How, in practice, are the motion representation, e.g., Figure. 2(a), extracted from learned implicit function?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on macro motion analysis, which involves collecting all visually observable motions in dynamic scenes. The traditional filtering-based methods typically pay attention to local and tiny motions, while recent dynamic neural representations can represent motions faithfully, but cannot be directly applied to motion analysis. The authors propose Phase-based neural polynomial Gabor fields (Phase-PGF) to represent scene dynamics with low-dimensional time-varying phases. Phase-PGF has several properties suitable for macro motion analysis, and it can be used for various dynamic scene editing tasks, such as motion loop detection, motion separation, motion smoothing, and motion magnification. It further implements the Phase-PGF using an innovative neural architecture and a refined training approach to enhance the quality of dynamic scene representation and editing.

The main contributions of this paper are as follows:
1) formulate the macro motion analysis problem 
2) provides a novel phase-based neural polynomial Gabor fields (Phase-PGF) approach to tackle the motion analysis problem
3) demonstrates the effectiveness of the Phase-PGF approach on both 2D and 3D scenes

---------------------------------------------------------------------------------------------------------------------------------------
After reviewed the author's rebuttal, I have increased my score.

### Strengths
The main strengths of this paper are as follows:
1. Originality: The paper proposes a novel approach called Phase-based neural polynomial Gabor fields (Phase-PGF) for representing and analyzing dynamic scenes. This approach addresses the gap in the field of computer vision, where traditional methods focus on local and tiny motions, while recent dynamic neural representations lack direct applicability for macro motion analysis. The paper's originality lies in its focus on macro motion analysis and the introduction of Phase-PGF as a suitable representation for this purpose.
2. Quality: The paper presents a detailed analysis of the proposed approach, discussing its theoretical properties and demonstrating its ability to handle various macro motion analysis tasks such as motion separation, motion smoothing, and motion magnification. The experiments conducted showcase the effectiveness of Phase-PGF in representing and editing dynamic scenes, making the paper's contributions of high quality.
3. Clarity: The paper is well-structured and clear. The authors formulate the problem of macro motion analysis, explain the theoretical properties of Phase-PGF, and discuss the implementation and training of the approach. The experiments are described in sufficient detail, making it easy for readers to understand and replicate the proposed method.
4. Significance: The paper addresses a key challenge in the field of computer vision, motion analysis, and dynamic scene representation. By focusing on macro motion analysis, the proposed approach has the potential to impact various applications, such as motion tracking, generation, virtual reality, and other computer vision tasks. The paper's contributions are significant in providing a novel solution to representing and analyzing large motions and 3D scenes, which has been a largely underexplored area in the field.

In summary, the main strengths of the paper are its originality, quality, clarity, and significance. The paper presents a novel and effective approach to representing and analyzing macro motions in videos (both 2D and 3D), discusses its theoretical properties, and demonstrates its practical applicability through experiments, making it a valuable contribution to computer vision and related domains.

### Weaknesses
Weaknesses of the paper:
1. Slight artifacts in boldly magnifying large motions: The paper acknowledges that when magnifying large motions, there are slight artifacts in Phase-PGF. The cause of these artifacts may stem from the neural network architecture or the way motion is represented. Specifically, the Gabor basis might not be sufficiently expressive to capture the complex deformations that arise during large motion magnification, leading to visual distortions. To reduce these artifacts, additional investigation and optimization of the model, particularly the Gabor basis and its spatial support, may be necessary. 

2. Limited scalability to complex large-scale 3D dynamic scenes: The paper acknowledges that Phase-PGF might not perform well in complex large-scale 3D scenes due to computational efficiency issues. The computational cost of evaluating the Gabor fields increases significantly with scene complexity, making it challenging to apply the method to large-scale 3D scenes. As the paper's focus is on macro motion analysis, addressing this issue is crucial to improving the applicability of the proposed method, especially for complex scenes. A possible solution could be the use of a spatially adaptive Gabor basis as mentioned in the paper, but the implementation details and the effectiveness of this approach remain unclear.

3. Insufficient experimental evaluation: Although the paper presents some experimental results, it would be beneficial to include more comprehensive evaluations with various datasets and tasks. For example, additional experiments could be conducted on larger and more diverse datasets, varying scene conditions, and different motion types (e.g. human motion). The current evaluation lacks quantitative metrics that directly measure the quality of motion analysis and manipulation, making it difficult to objectively assess the performance of the proposed method. This would help establish the robustness and generalizability of the proposed method.

4. Neural network architecture: The paper uses a neural network to instantiate the Phase-PGF representation. However, the choice of the neural network architecture could be further optimized for the specific task of macro motion analysis. The paper does not provide enough details on the network architecture (e.g. number of layers, activation functions, etc.), making it difficult to reproduce the results or understand the impact of the architecture on the performance of the method. Including the details of the architecture may help to improve the reproducibility of the proposed work.

### Questions
1. In the related work section, the authors discuss concurrent works on tiny motion editing. How does Phase-PGF differ from these methods in terms of addressing macro motion analysis?

2. The authors mention that Phase-PGF may present slight artifacts when magnifying large motions. Could they provide further insights on the reasons for these artifacts and potential solutions to address this issue?

3. Are there plans to improve Phase-PGF's scalability for large-scale 3D dynamic scenes?

4. In the experimental section, it would be helpful to know more about the datasets used and the evaluation metrics employed for assessing the performance of Phase-PGF. For example, for the human preference study, how many ratings are obtained for each video, and how many videos are being used in the study? 

5. Can the authors discuss the potential applications of Phase-PGF beyond the mentioned motion analysis and editing tasks, such as object tracking, motion generation, or other real-world scenarios?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
