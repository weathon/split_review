# EqNIO: Subequivariant Neural Inertial Odometry

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 5, 8, 8

## Abstract
Neural network-based odometry using accelerometer and gyroscope readings from a single IMU can achieve robust, and low-drift localization capabilities, through the use of \emph{neural displacement priors}. These priors learn to produce denoised displacement measurements but need to ignore data variations due to specific IMU mount orientation and motion directions, hindering generalization.
This work introduces EqNIO, which addresses this challenge with \emph{canonical displacement priors}. We train an off-the-shelf architecture with IMU measurements that are mapped into a canonical gravity-aligned frame with learnable yaw. The outputs (displacement and covariance) are mapped back to the original frame.
To maximize generalization, we find that these learnable yaw frames must transform equivariantly with global trajectory rotations and reflections across the gravity direction, \emph{i.e.} action by the roto-reflection group $O_g(3)$ which preserves gravity (a subgroup of $O(3)$). This renders the displacement prior $O(3)$ \emph{subequivariant}.
We tailor specific linear, convolutional and non-linear layers that commute with the actions of the group. 
Moreover, we introduce a bijective decomposition of angular rates into vectors that transform similarly to accelerations, allowing us to leverage both measurements types. Natively, angular rates would need to be inverted upon reflection, unlike acceleration, which hinders their joint processing.
We highlight EqNIO's flexibility and generalization capabilities by applying it to both filter-based (TLIO), and end-to-end (RONIN) architectures, and outperforming existing methods that use \emph{soft} equivariance from auxiliary losses or data augmentation on the TLIO, Aria, RONIN, RIDI and OxIOD datasets. We believe this work paves the way to low-drift, and generalizable neural inertial odometry on edge-devices. 
\iffalse
Neural networks are seeing rapid adoption in purely intertial odometry, where accelerometer and gyroscope measurements  from commodity inertial measurement units (IMU) are used to regress displacements and associated uncertainties. They can learn informative displacement priors, which can be directly fused with the raw data with off-the-shelf non-linear filters. 
Nevertheless, these networks do not consider the physical roto-reflective symmetries inherent in IMU data, leading to the need to memorize the same priors for every possible motion direction, which hinders generalization.
In this work, we characterize these symmetries and show that the IMU data and the resulting displacement and covariance transform equivariantly, when rotated around the gravity vector and reflected with respect to arbitrary planes parallel to gravity. 
We design a neural network that respects these symmetries \emph{by design} through equivariant processing in three steps: First, it estimates an equivariant gravity-aligned frame from vectors and scalars derived from IMU data, leveraging expressive linear, convolutional and non-linear layers tailored to commute with the underlying symmetry transformation.
We then map the IMU data into this frame, thereby achieving an invariant \emph{canonicalization} that can be directly used with off-the-shelf neural inertial odometry architectures. Finally, we map these network outputs back into the original frame, thereby obtaining equivariant covariances and displacements.
We demonstrate the generality of our framework by applying it to the filter-based approach based on TLIO, and the end-to-end RONIN architecture, and show better performance on the TLIO, Aria, RONIN, RIDI and OxIOD datasets than existing methods.
\fi
\iffalse

Presently, neural networks are widely employed to accurately estimate 2D displacements and associated uncertainties from Inertial Measurement Unit (IMU) data that can be integrated into stochastic filter networks like the Extended Kalman Filter (EKF) as measurements and uncertainties for the update step in the filter.
However, such neural approaches overlook symmetry which is a crucial inductive bias for model generalization. This oversight is notable because (i) physical laws adhere to symmetry principles when considering the gravity axis, meaning there exists the same transformation for both the physical entity and the resulting trajectory, and  (ii) displacements should remain equivariant to frame transformations when the inertial frame changes.
To address this, we propose a subequivariant framework by:
(i) deriving fundamental layers such as linear and nonlinear layers for a subequivariant network, designed to handle sequences of vectors and scalars,
(ii) employing the subequivariant network to predict an equivariant frame for the sequence of inertial measurements. This predicted frame can then be utilized for extracting invariant features through projection, which are integrated with arbitrary network architectures,
(iii) transforming the invariant output by frame transformation to obtain equivariant displacements and covariances. 
We demonstrate the effectiveness and generalization of our Equivariant Framework on a filter-based approach with TLIO architecture for TLIO and  Aria datasets, 
and an end-to-end deep learning approach with RONIN architecture for RONIN, RIDI and OxIOD datasets.
\fi

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a method to adapt existing inertial odometry (IO) architectures to be invariant to the IMU orientation. This is done by making use of an $O_g(3)$/$SO_g(3)$ equivariant network that transforms the gravity-aligned IMU measurements to a canonical frame as a pre-processing step for non-equivariant IO. The predicted displacement and covariance from IO for these canonicalized measurements are then transformed back to the source frame using the inverse canonical frame. The proposed method leads to improved accuracy while maintaining comparable runtime and can in principle be applied to any IO method.

### Strengths
- This is an interesting and novel application of equivariant networks to an under-explored but useful problem. The canonicalization approach is a good choice for this problem as it adapts existing sota IO architectures and keeps the pipeline interpretable.
- The symmetry of the problem in terms of $O_g(3)$ equivariance (which is $O(3)$ subequivariant) is well presented. Care has been taken to consistently process the IMU measurements and specialized $O(2)$/$SO(2)$ architectures based on vector neurons have been developed, while more architectures are possible.
- The approach was tested on two IO architectures which showed accuracy improvements on many datasets, with comprehensive ablation studies, while keeping the inference times comparable.

### Weaknesses
 - The general canonicalization scheme has been proposed before by Kaba, Sékou-Oumar, et al. "Equivariance with learned canonicalization functions." ICML 2023, and cannot not be presented as a contribution. The original work must be cited.
- While there is a reduction in drift compared to the baselines, the remaining drift is still significant (>2m) which suggests that the main problem in IO is not in exact equivariance but elsewhere (most likely sensor noise).



### Questions
- Why is this canonical. equiv. scheme chosen over other equiv. choices? e.g. frame averaging (Puny et al. ICLR '22) also allows adapting existing non-equiv. architectures.
- I'm confused about the choice of metrics, especially for the TLIO experiments. From the definitions in A.5 (I believe squared norm is missing), it seems that MSE is just sqrt(ATE)? But the numbers don't reflect this. And I also think ATE, RTE, AYE would be sufficient. Do you do SE3 alignment with the GT trajectories?

Minor non-critical comments:
- Could you elaborate on the yaw augmentation procedure used for TLIO / RoNIN?
- It is surprising to me that despite requiring 10x more FLOPs than the non-equiv. architectures, there is barely any increase in runtime (<1 ms). Since there is no code release, can you comment more on the reasons for this efficiency?
- Writing: In Fig. 3b it is not clear what 'rot. sense' means; explain how the frame is constructed from the network outputs with gs-orth. for sake of clarity; Typo in conclusion: "respects eliminates"; Would be helpful to indicate that * means no-EKF in the table 2,3 captions or simply remove the * since it is not applicable to RoNIN.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work introduces EqNIO, a neural network-based odometry system that enhances localization accuracy using accelerometer and gyroscope data from a single IMU. Traditional neural odometry methods face challenges with generalization, as variations in IMU orientation and motion direction can disrupt displacement predictions. EqNIO overcomes this by training a model with canonical displacement priors, aligning IMU data to a gravity-aligned frame with learnable yaw. This approach ensures that the system’s outputs are invariant to rotations and reflections in the gravity direction, supporting robust generalization. Through carefully designed layers and an innovative angular rate decomposition, EqNIO can effectively integrate both acceleration and angular data. Tested on TLIO, Aria, RONIN, RIDI, and OxIOD datasets, EqNIO demonstrates superior performance and adaptability over existing methods, marking a step forward in low-drift neural inertial odometry suitable for edge devices.

### Strengths
I think the method itself looks novel and interesting.  It introduces a canonicalization scheme that leverages gravity and an estimated sub-equivariant frame to map IMU measurements into a canonical orientation. This procedure can be flexibly applied to arbitrary off-the-shelf network architectures by mapping the inputs into the canonical space and mapping the outputs back into the original space.

### Weaknesses
The primary weakness of this paper is the clarity of its writing. I’m unable to fully understand the major differences between this work and RIO: Rotation-equivariance Supervised Learning of Robust Inertial Odometry.

While the key idea of this paper is clear, it’s difficult to discern how it specifically diverges from the previous work. I strongly recommend that the authors begin by clearly outlining the main concepts, followed by a detailed description of the methodology. This structure would greatly help readers in understanding the unique contributions of this work.

### Questions
What is the roto-reflection group, and why is it important? A more detailed explanation of this concept and its relevance would be helpful.

What is the PCA(handcrafted equivariant frame)? A more detailed explanation of this concept and its relevance would be helpful.

Clarity in distinguishing from RIO: It appears that the figure is intended to convey the core idea of this work. However, the differences between this approach and RIO are unclear—elaborating on this distinction would strengthen the presentation.

Data specification in figure captions: It would be beneficial if each figure caption specified which data is seen and which is unseen to enhance the reader's understanding. Note, the performance of different method highly depends on how much data is seen or trained. 

Supplementary material vs. main paper clarity: The supplementary material provides much better clarity than the main paper. Including some of this contextual information directly in the main paper would make it easier for reviewers to follow your method.

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
2

### Summary
This paper presents a new method for inertial odometry, which predicts the poses given IMU measurements. The method is called EqNIO, which brings the idea of the so-called canonical displacement priors. How it works, is (1) that IMU measurements are mapped into a gravity aligned, canonical frame with neural networks, and (2) mapping the outputs back to the original frame. Several contributions are presented. A canonicalization scheme is presented, that maps IMU measurements into a canonical orientation. A processing step is devised, which map both accelerometer and gyro readings into a space where gravity direction is preserved. Finally, a neural network designed is presented to perform regression tasks. Several experiments are presented, demonstrating advancements to the state of the art and ablation studies that motivate the overall approach.

### Strengths
Pros:

-	The paper is written well with clear figures, and many intuitive explanations of complex concepts.

-	The paper presents several technical contributions, which overall leads to more generalizable framework for inertial odometry. Mixing the physical properties with learning based regression module makes sense, which can boost generalization performance.

-	Experimental results are presented to a large extent, demonstrating advancements to the state of the art. Ablation studies presented are useful to better comprehend the research done.

### Weaknesses
Cons:

- It is not clear if ICLR is the best venue for such research, since learning components here is rather limited to a regression module.

- Uncertainty modelling assumes diagonal covariance. Validity of these assumptions are tested by looking at the final performance that it helps. Perhaps an in-depth analysis on this step could help, despite not the core focus of the paper. For example, there has been many evaluation tools from uncertainty quantification literature, and can be presented here.

### Questions
I wonder for sensor fusion in the form of visual-inertial odometry, it could be helpful to have a good uncertainty estimates from the inertial odometry module. Uncertainty estimates could consider the modelling errors of neural networks, and propagated to the final module. Here, priors can also be defined using physical properties of the system. Would it be a consideration to use Bayesian modelling tools?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper  presents a method to enhance inertial odometry by applying group equivariance to canonicalize IMU data and targeting yaw ambiguity in gravity-aligned frames through a subequivariant framework. 

The authors design a neural network architecture that maintains equivariance under roto-reflections around the gravity axis, allowing integration with existing systems like RONIN and TLIO. By predicting canonical yaw frames and equivariant covariance matrices, EqNIO improves generalization across diverse motion patterns and reduces drift caused by sensor noise and biases. Experiments on publicly available datasets demonstrate that this method achieves reductions in Mean Squared Error and Absolute Translation Error compared to baseline models, while also exhibiting faster convergence and maintaining computational efficiency suitable for deployment on edge devices.

### Strengths
The paper introduces an approach by applying strict subequivariance in neural inertial odometry, addressing yaw ambiguity and gravity alignment limitations directly within the network architecture, an aspect that prior methods often handled indirectly. Its originality lies in developing a canonicalization scheme using the roto-reflection group to simplify IMU data processing. The authors integrate and extend existing methods by adapting the framework to both end-to-end and filter-based neural inertial odometry systems, which demonstrates its flexibility and scalability. 

In terms of quality, the paper provides detailed, reproducible implementation notes and thorough ablation studies in the appendix that clarify design decisions and evaluate parameterization choices. It emphasizes empirical rigor by testing the model across multiple datasets with varied sensor placements and motion patterns, supporting claims of robustness and broad applicability. Clarity is maintained through structured explanations of complex mathematical formulations, specifically around group theory and its relevance to sensor data processing, while the significant computational efficiency results underscore the practical utility for edge-device applications. The combination of technical insights and comprehensive empirical validation underlines the paper's contribution to advancing neural inertial odometry, particularly in settings with challenging orientations and device constraints.

### Weaknesses
The abstract describes EqNIO as leveraging "canonical displacement priors" to generalize across arbitrary IMU orientations, but it lacks a clear technical explanation of how these priors work in practice. Generalization is claimed to stem from "canonical gravity-aligned frames" and "equivariant yaw frames," but the abstract could benefit from a more precise explanation of these transformations and their operationalization in the model.

The learnable yaw orientation in canonical frames is a promising feature but lacks clarity on how it resolves yaw drift or improves orientation estimation, given that yaw is typically the most challenging to estimate accurately in inertial odometry due to the absence of an absolute reference.

The introduction highlights EqNIO’s generalization and robustness but does not discuss potential limitations or scenarios where the approach may struggle (e.g., handling different sampling rates, extreme motions where IMU biases may not be fully mitigated, or contexts with poor gravity alignment).

While EqNIO is compared to existing neural odometry methods like TLIO and RONIN, the introduction does not delve into specific weaknesses in these prior approaches and how EqNIO addresses these limitations.

The paper covers a broad range of related works but may omit some recent or seminal papers in the domain of learning-based inertial odometry and equivariant neural networks. Ensure a comprehensive literature review by including all relevant and recent works that contribute to the field. This includes verifying that seminal papers and the latest advancements are adequately cited to position EqNIO within the current research landscape. Due to the inherent relationship between odometry and inertial attitude estimation, as well as the similar methods applied to both, I highly encourage you to explore these areas further, including learning-based approaches to inertial attitude estimation.

The descriptions of related methods (e.g., TLIO, RONIN) are somewhat high-level and lack technical depth.  Providing only superficial descriptions may not adequately highlight the nuances that differentiate EqNIO from these methods.

### Questions
Could you provide a technical explanation of how the canonical displacement priors are implemented in practice?
How exactly do the gravity-aligned frames and equivariant yaw frames work in your model architecture?
What specific mechanisms in your learnable yaw orientation approach help address the yaw drift problem?
Could you provide experimental evidence demonstrating how your method improves yaw estimation compared to existing approaches?
How does your model perform under varying IMU sampling rates?
What are the performance characteristics under extreme motion scenarios where IMU biases may be significant?
How does the system behave in situations with poor gravity alignment?
How does your work relate to recent developments in learning-based inertial attitude estimation?
Could you elaborate on the connections between EqNIO and current research in equivariant neural networks specifically applied to inertial navigation?

### Soundness
3

### Presentation
3

### Contribution
3
