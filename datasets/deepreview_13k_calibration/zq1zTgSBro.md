# SPEAR: Receiver-to-Receiver Acoustic Neural Warping Field

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3

## Abstract
We present \emph{SPEAR}, a continuous receiver-to-receiver acoustic neural warping field for spatial acoustic effects prediction in an acoustic 3D space with a single stationary audio source. Unlike traditional source-to-receiver modelling methods that require prior space acoustic properties knowledge to rigorously model audio propagation from source to receiver, we propose to predict by warping the spatial acoustic effects from one reference receiver position to another target receiver position, so that the warped audio essentially accommodates all spatial acoustic effects belonging to the target position. \emph{SPEAR} can be trained in a data much more readily accessible manner, in which we simply ask two robots to independently record spatial audio at different positions. We further theoretically prove the universal existence of the warping field if and only if one audio source presents. Three physical principles are incorporated to guide \emph{SPEAR} network design, leading to the learned warping field physically meaningful. We demonstrate \emph{SPEAR} superiority on both synthetic, photo-realistic and real-world dataset, showing the huge potential of \emph{SPEAR} to various down-stream robotic tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces SPEAR, a novel neural warping field model designed to predict spatial acoustic effects in a 3D environment with a single stationary audio source. Unlike traditional source-to-receiver models requiring prior knowledge of room acoustics, SPEAR operates from a receiver-to-receiver perspective, allowing it to predict how audio would sound at different spatial positions using only discrete audio recordings at various receiver positions. This framework is trained using synthetic, photo-realistic, and real-world datasets, demonstrating significant flexibility and generalizability across different environments. The paper's contributions include a new problem formulation, a theoretically supported neural architecture guided by three physical principles, and comprehensive experimentation showing SPEAR's accuracy and efficiency over baseline methods.

### Strengths
1. The receiver-to-receiver formulation of spatial acoustics is innovative, providing a new paradigm in spatial audio modeling that does not rely on prior knowledge of acoustic properties.
2. Methodologically rigorous, supported by a blend of theoretical analysis and robust experimental results across diverse datasets (synthetic, photo-realistic, real-world).
3. The overall flow and structure of the paper are clear, with detailed explanations of each stage in the model’s development, including physical principles and architecture specifics.
4. SPEAR’s method addresses a gap in the field, making spatial acoustics modeling more accessible for real-world applications in complex environments.

### Weaknesses
1. Sampling Density Requirement: A dense sampling of receiver positions is currently required for SPEAR to achieve optimal accuracy. This requirement may limit its scalability in highly variable environments. The paper does not adequately address the computational cost associated with this dense sampling, particularly in terms of memory usage and processing time, which could be a significant bottleneck for real-world applications. Furthermore, the method's sensitivity to the density of sampling is not fully explored, leaving questions about the minimum sampling rate required to maintain acceptable performance.

2. Positioning Constraint: SPEAR assumes all receiver positions lie on the same horizontal plane, which could restrict applications in multi-level or irregular environments. The paper lacks a detailed analysis of how the model's performance degrades when this constraint is violated. It is unclear how the model would handle scenarios where receivers are placed at varying heights, which is a common occurrence in many real-world acoustic environments. The limitation to a single horizontal plane significantly reduces the model's applicability in complex, multi-story spaces.

### Questions
1. Could the authors elaborate on potential methods to reduce the dense sampling requirement? Would techniques like data augmentation be feasible for this purpose?

2. Are there specific changes or enhancements that could allow SPEAR to handle multi-level environments with varying elevations?

3. For real-time applications, what optimizations could be implemented to further reduce inference time without sacrificing accuracy?

4. Could the authors provide a comparison with conventional RIR-based approaches, detailing the trade-offs in accuracy, efficiency, and data requirements?

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
The authors propose a novel method for estimating the warping field that corresponds to sound propagation between two points inside a fixed environment. The method applies for a stationary source and two moving receivers (microphones). The receivers are synchronized, and thus the transfer function between the reference to the target receiver can be estimated from recordings in the frequency domain.

### Strengths
* The method can be applied relatively easily since it does not require a lot of knowledge about the environment
  * It is relatively original since most other methods require more information about the environment or a more complex recording setup
  * Quality is somewhat unclear (see comments below)
  * Clarity and significance could be improved (see comments below)

### Weaknesses
 * The method estimates the ratio between two transfer functions and this is prone to ill conditioning - however, it is not fully addressed. In the experiments they simply use clipping and zeroing to handle such cases, but how this affects performance is not clear. Specifically, the method does not address the fundamental issue of estimating the warping field at frequencies where one of the transfer functions, H1 or H2, is zero. This leads to undefined ratios and requires a more robust regularization approach, which is not discussed. The frequency of occurrence of such ill-conditioned cases and their impact on the final result should be quantified.
* The strengths and weaknesses of the method are not sufficiently clear. Furthermore, the constraints on receiver locations relative to one another are not discussed. If the receiver locations are not carefully controlled, how prone is the method to producing inaccurate warping field estimations? This is a critical practical consideration that needs to be addressed.
* I’m finding some difficulties in understanding exactly what SPEAR is trying to learn. In line 304: “...we can obtain the ground truth warping field…” - if you can calculate it analytically and then train the model to predict it, what exactly does the model learn? Some kind of generalization to other frequencies? Interpolation to grid points that are not measured? In any case, this is not discussed in the experiments. Moreover, the ability of the method to extrapolate to new room positions is unclear. If the method only interpolates between very close measured locations, its practical use is limited. How well does the method perform when only a fraction of the room positions are sampled, and how can one determine if the room has been sufficiently sampled?
* Experiments section (section 4.6)
  * There is too much emphasis on visual analysis of the warping field signal in the frequency domain (Figures 4, 6, 7, 8). It is very difficult 
to understand actual performance from these graphs. In all cases it looks like the estimated warping field is very different from the ground truth. Furthermore, the evaluation relies heavily on visual inspection of the time-domain signal, which is not a robust evaluation method.
  * Fig 5 - what is the meaning of the MSE values? Again, difficult to understand something about performance from reading absolute MSE values (i.e., how bad/good is an MSE of 1.06?). The MSE values are not normalized, making it difficult to assess the quality of the estimation. A normalized MSE, such as in dB, would provide a more meaningful measure of performance.
  * Table 3 - was the metric measured for the same signal? It should be noted that depending on the frequency content of the signal, estimating the warping field is limited. It is also important to note that there are RIR-based methods that are also source agnostic.
* It is not clear how to use the method given some very important parameters:
  * How close should the receiver be? Is this frequency dependent?
  * What source signal to use? 
  *How many grid points should be sampled in the environment in order to estimate the warping field of the entire environment? Is this even possible?

**Minor comments**
* Introduction → contribution 3: “We demonstrate SPEAR superiority…” - superiority compared to what?
* Lines 132-139: the relation to “Time-series Prediction” is not very clear. Please explain more clearly what is the relation between SPEAR and the type of networks you mentioned.
* Equation (2) - is p_1 and p_2 the same as p_r and p_t ? if so, please be consistent with notation
* Lines 308-309: “For ground truth warping field supervision, we combine both L1 and L2 loss.” - can you please provide an explicit equation for the loss? Is there a weighting parameter between the L1 and L2 losses? Why did you incorporate both L1 and L2?

### Questions
* SPEAR learns the propagation of sound from one receiver (reference) to the second receiver (target). So to map all potential (reference, target) positions in the room is also combinatorically complex (as in the RIR case). Thus:
  * How much more efficient this method is to the previous ones (RIR-based / NAF)?
  * Please explain more clearly the benefits (or tradeoffs) between SPEAR and source-to-receiver modeling methods. In other words, why does the latter require prior space acoustic properties knowledge and SPEAR does not? (this is not clear in both the introduction and not in “related work” section)
  * How dependent is the method on the specific source signal? If the signal is narrowband (single frequency), then the method would not be able to estimate other frequencies.
* There are two very significant claims in lines 162-165:
  * Warping transform is multiplicative in the frequency domain
  * The acoustic neural warping field is independent on audio content
While you refer to the appendix for proof and discussion, I would suggest adding some coarse and intuitive explanation to why that is the case.
* Equation (5) - there are cases where the transfer function H may be zero for some frequencies. Then the relations in equation (5) would not hold. How do you handle these cases? (in the experiments you mention that you use a Sine Sweep signal but this is not clear at this stage of the paper)
* Equation (7) is a generalization of eq. (5): thus the determinant condition applies to equation (5) as well, but it is not mentioned.
* In your SPEAR training you fix the position of the source. If we would like to use SPEAR with a source that is located in a different position (and in a different room), we would have to train it again in the new setting, correct? If so, this should be mentioned clearly
* What applications could benefit from this method (especially compared to alternatives)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a method for estimating the wrapping field in an enclosed acoustic environment, which is the relative transfer function between two receivers, when given the position of the two receivers. This method is meant to replace direct room impulse response estimation which relies on prior space acoustic properties and complex computations or requires massive amount of RIRs as a supervision. The method is shown to outperform baselines on both simulated and real-world data.

### Strengths
The paper presents a novel viewpoint that learns the wrapping field that connects two receivers using a new transfomer-based model. A comprehensive experimental study is conducted with both simulated and real-world data, and different aspects of the proposed method are examined. The paper is clearly written and contains meaningful illustrations that clarify its core ideas.

### Weaknesses
The usefulness of the proposed method is not well motivated. On the one hand, the wrapping field corresponds to a fixed source position, but in reality it is more informative to consider a source that can change locations. On the other hand, the space of all possible wrapping fields seems to be unnecessarily large, since it is defined by two receiver locations, whereas for RIR estimation the mapping is a function a single receiver only (and a source position). This is also evident from the vast amount of training samples that are required for training the model. Note that from these same measurements one can extract the RIR if the emitted source signal is known (which should be the case since the training recordings are performed in a controlled manner).
Note that this idea of utilizing the wrapping field already exists in the literature for two decades. It is known as the Relative Transfer Function (RTF). A plethora of methods have been proposed to robustly estimate the RTF from measured signals (see a summary on [1] Section IV. C. 3). More close to the current paper, it was already proposed in previous works to generate RTFs based on source-receiver locations [2,3,4]. This relevant literature should be referred to in the paper, and it should be made clear what is the difference between these works and the current contribution.
In addition, the paper is very similar to [5], where it seems that the main difference is that the current paper deals with RTF estimation instead of RIR estimation, thus requiring an additional emitting sound at a fixed position. It should be clarified what is the main contribution of the current work compared to [5].

[1]  Gannot, S., Vincent, E., Markovich-Golan, S., & Ozerov, A. (2017). A consolidated perspective on multimicrophone speech enhancement and source separation. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 25(4), 692-730.

[2] Wang, Z., Vincent, E., & Yan, Y. (2017). Relative transfer function inverse regression from low dimensional manifold. arXiv preprint arXiv:1710.09091.‏

[3] Wang, Z., Li, J., Yan, Y., & Vincent, E. (2018, April). Semi-supervised learning with deep neural networks for relative transfer function inverse regression. In 2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 191-195). IEEE.‏

[4] Bianco, M. J., Gannot, S., Fernandez-Grande, E., & Gerstoft, P. (2021). Semi-supervised source localization in reverberant environments with deep generative modeling. IEEE Access, 9, 84956-84970.‏

[5] He, Y., Cherian, A., Wichern, G., & Markham, A. (2024, January). Deep Neural Room Acoustics Primitive. In Forty-first International Conference on Machine Learning

### Questions
Several questions related to the weaknesses mentioned above:

1.	What is the motivation for learning the RTF where both receivers can change positions while source position is fixed (in test time maybe we would like the source to change places)?
2.	What is the relation to previous works on RTF estimation [2-4]?
3.	What is the key contribution over [5]?

Additional minor questions: 

4.	Why is the Fourier transform used instead of STFT representation?
5.	Line 151 - the meaning of this notation $\mathcal{F}\leftarrow(\mathcal{A},\mathcal{P})$ is unclear.
6.	There is inconsistency in the notation, switching from $p_1,p_2$ to $p_r,p_t$ and the same for the wrapping field.
7.	Proposition 2 contains an over-general statement (“existence is not guaranteed”) and the proof is vague. In general, the identifiability of the mixing matrix in (7) was investigated under the field of independent component analysis (ICA), and there are certain conditions for which the matrix is identifiable (full rank matrix and at most one Gaussian source).  The wrapping field can be defined as a vector of length K that contains the wrapping field for each individual source. 
8. Line 294: "The two input positions’ features are extracted from the grid feature by bilinear interpolation" - please clarify how the bilinear interpolation is performed. 
9. What is the motivation for using a transformer? What does the attention between patches is expected to learn? 	
10. The proposed method is not necessarily more realistic compared to baselines. The required data is similar to collecting massive RIR data, since RIR can be extracted when the source signal is known. 
11.	Fig 4., why NN baseline is not presented?
12.	The figures order does not follow the order they appear in the text -  Fig. 6 should come before Fig. 5.
13.	Warping Field Sensitivity to Noise - is the noise added during training?   What happens in higher noise levels?
14.	Missing details regarding experiments – what is the reverberation time? What is the signals length? 
15.	Why Fig. 5.a. does not contain comparison to NN? 
16.	Appendix D is empty
17.	Are there any insights regarding the characteristics of the failure cases?
18.	Table 3 – It is unclear why the feature dimension is 384, and what is 43 in the initial token representation. Why is there a pruning step at the output?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors point out that the problem of acoustic field estimation is characterized by the high cost of collecting prior information (about the physical properties such as geometries), and propose a relatively simple way to solve the problem: to estimate the receiver signal at another location from the receiver signal. They present their theoretical assumptions and backgrounds for their methodology and demonstrate its effectiveness on simulated and real recorded datasets.

### Strengths
One of the strengths of this paper is its value as an attempt to alleviate the difficulty of data acquisition for sound field synthesis. It also deserves recognition for achieving large computational efficiency gains within moderate memory efficiency.

### Weaknesses
For me, the justification for the main contribution of this study remains unclear. To point out my thoughts on the main contributions listed by the authors at the end of Section 1:

1. Please clarify the reasoning behind the claim that the receiver-to-receiver framework requires less prior information than source-to-receiver (e.g. NAF). 

    - At the end of the second paragraph of Section 1, the authors explain their motivation as collecting RIR data is exceedingly difficult in real scenarios, and their receiver-recorded audio is more readily accessible. What I don't understand about this argument is that they ended up using a sine sweep source for training, so in what way is this more efficient than training with RIR? Specifically, how does the use of a sine sweep signal, which inherently contains frequency information across a broad spectrum, reduce the need for prior information about the acoustic environment compared to using RIR data, which directly captures the room's response?

    - Let's say that the training data is not necessarily a sine sweep. One of the cases where a receiver-to-receiver framework can be beneficial, as the paper suggests, is when we don't know about the source signal. I'm curious to hear your thoughts on whether cases like this are prevalent in real-world scenarios. In my understanding, as there should be a receiver recording to train SPEAR in a certain room, one should first play the source signal to acquire the responses at each receiver point, meaning that we already know the source signal. Furthermore, if the source signal is unknown, how does the model ensure accurate generalization across different types of source signals, given that the acoustic properties of a room can interact differently with different signal types?

2. The statements and proofs of the propositions in Section 3.2 seem to lack the rigor to be presented as major contributions.

    - What the authors describe as the claim and proof in the text for Proposition 1 is a direct consequence of Rayleigh's reciprocity theorem. Aside from the rigors in the proof of the “unique existence of warping given any pair of receivers”, there is something I don't understand about what the authors conclude in the last sentence of the proof: what does the claim “independent of the audio source” mean? Considering diffraction, the warping field should be variant depending on the source frequencies, isn’t it? Could you elaborate on the mathematical space in which the warping field is defined and how its uniqueness and existence are assured within that space?

    - Similarly, there are several technical misleading statements throughout the paper that could be used to claim theoretical contributions, and the explanation of acoustic propagation is still underdeveloped. One example of this is the claim in Principle 1 in Section 3.3 that 'the entire 3D space is involved in the receiver recording', which could be misleading to those unfamiliar with audio. It would be better to claim instead that 'because the sound is generally more reflective than light, even signals reflected from occluded areas can be affected, and because of their lower velocity, the effect is more pronounced'.

3. To claim to have revealed the superiority of SPEAR, the baseline selection is weak, and the ablation study did not sufficiently reveal the strengths and weaknesses of the proposed methodology.

    - At the very least, INRAS [1] should be included, and it would be nice to see other baselines such as AV-NeRF [2], DiffRIR [3], etc. These models provide alternative approaches to modeling room acoustics and could offer a more comprehensive comparison.

    - In the context of synthesizing acoustic warping fields for moving sources with a fixed receiver (which shares systematic similarities with this paper’s problem statement), WaveNet-based architectures are often used [4,5], or even MLPs [6] to estimate the frequency domain warping fields. How does the Transformer architecture bring advantages over these other architectures? Specifically, what aspects of the Transformer's architecture, such as its self-attention mechanism, make it more suitable for this task compared to the sequential processing of WaveNet or the simpler feedforward nature of MLPs?

    - I wonder if re-training is essential for comparing performance with RIR-based source-to-receiver methodologies (including NAF). Even with keeping those source-to-receiver models as-is, we can estimate $H_{p_r}$ and $H_{p_t}$ directly, and it seems natural to be able to obtain $\mathcal W_{p_r \to p_t}=H_{p_t}/H_{p_r}$. Is there a reason to retrain the NAF nonetheless? Given such commutative nature of LTI systems, how is receiver-to-receiver learning systematically different from source-to-receiver learning, as one could readily get the impulse response for each of the receivers and then deconvolve one into the other? If the source position is fixed, as implied in the experimental setup, does this not simplify the problem to a set of linear equations that can be solved without iterative training?

### Questions
A few minor comments based on the weaknesses mentioned above.

- For the claim “to be more favorable to real-world scenarios” to be convincing, the method would need to be validated in cases where the source signal is not a sine sweep, but a more readily accessible sound like clapping (which is easy to generate and record at the receivers but difficult to acquire the original source). Furthermore, the performance under different receiver position sampling policies would need to be more rigorously validated to see how much space is covered by the receiver positions for training. In this respect, the choice of dataset in this paper could benefit from further diversification:

    - Pyroomacoustics was synthesized based on the image-source method in a shoebox room as stated in the paper

    - Sound Spaces 2.0 is also based on ray-based simulation and the office subset of Replica used by the authors is a single-room

    - MeshRIR is a real measurement, but the structure of the room is also a shoebox

    A dataset that can verify performance for non-trivial cases may be a multi-room dataset (where there could be no direct acoustic path, e.g., 'line of sight'), such as Replica's Apartment subset. In this case, other factors than the Reference-Target Distance reported in this paper may be important for sampling receiver positions. For example, if the source is in the living room of an apartment, how much detail should the training receiver be sampled to ensure performance?

- Typos/misleading phrases
    - L182, L205: The part where the author expresses "according to room acoustics (Savioja & Svensson, 2015)" seems to assume an LTI system, but since not all room acoustics assume LTI, the expressions seem to need clarification.
    - L370 PSESQ $\to$ PESQ
    - Figure 8 comes before Figure 6 and 7.
    - Wrong references to "Fig. B" (L456) and "Fig. C" (L464)

### Soundness
2

### Presentation
2

### Contribution
1
