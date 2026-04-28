# Towards Holistic Multimodal Interaction: An Information-Theoretic Perspective

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
Multimodal interaction, which assesses whether information originates from individual modalities or their integration, is a critical property of multimodal data. The type of interaction varies across different tasks and subtly influences the effectiveness of multimodal learning, but it remains an underexplored topic.
In this paper, we present an information-theoretic analysis to examine how interactions affect multimodal learning. We formulate specific types of information-theoretical interactions and provide theoretical evidence that an effective multimodal model necessity comprehensive learning across all interaction types. Moreover, we analyze two typical multimodal learning paradigms—joint learning and modality ensemble—and demonstrate that they both exhibit generalization gaps when faced with certain types of interactions. This observation underscores the need for a new paradigm that can isolate and enhance each type of interaction.
To address this challenge, we propose the Decomposition-based Multimodal Interaction learning (DMI) paradigm. Our approach utilizes variation-based decomposition modules to segregate multimodal information into distinct types of disentangled interactions. Then, a new training strategy is developed to holistically enhance learning efficacy across various interaction types. 
Comprehensive empirical results indicate our DMI paradigm enhances multimodal learning by effectively decomposing and targeted improving the learning of interactions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates multimodal interaction through the lens of decomposition. The authors argue that the existing learning paradigms, such as joint learning and modality ensemble, struggle to handle all types of interaction effectively, leading to generalization issues. To address this, the authors propose a new paradigm called decomposition-based multimodal interaction (DMI) learning. DMI decomposes multimodal interaction into separate interaction types and applies a new training strategy to enhance learning across these interactions.

### Strengths
* The authors tackle the important problem of multimodal learning through mutual information decomposition.
* Improvements over state-of-the-art.
* The design of the Interaction Decomposition Module is very creative and aims to completely break down mutual information through learning. Figure 3, which shows the Interaction Decomposition Module, is very informative.

### Weaknesses
 * I'm confused by the results in Table 1 and the associated section 3.3. Reading through the proof for Lemma 3.3 from Appendix A.3, it looks like the N = 2n relationship comes from how the authors constructed the new dataset by separating X(1) and X(2): S(1) = {X(1), Φ(2), Y}, S(2) = {Φ(1), X(2), Y}. However, these are the **same** data, just arranged differently to emulate the unimodal MI instead of multimodal MI to create the bounds in Eqs (25) and (26); as a side effect, there are now twice as many samples. But the underlying data stays exactly the same -- we don't need more data to train each model paradigm. What does this result mean in practice?
* The model architecture seems unclear. There isn't much information available beyond Figure 3, and it would be difficult to understand or reproduce this work with the information given.
* Table 1 uses this form of big-O notation $O(1/\sqrt{N})|_{N=2n}$. Does $N=2n$ simply mean "set N to 2n" (I've not seen this condition before)? Since big-O notation is asymptotic, what difference does it make between $N=n$ vs. $N=2n$?

### Questions
* Table 1 uses this form of big-O notation $O(1/\sqrt{N})|_{N=2n}$. Does $N=2n$ simply mean "set N to 2n" (I've not seen this condition before)? Since big-O notation is asymptotic, what difference does it make between $N=n$ vs. $N=2n$?
* My takeaway from this paper is "interaction decomposition improves multimodal interaction learning". Is this what the paper is trying to convey?
* Are joint learning and ensemble learning the only paradigms available? Are there other paradigms that address the proposed problem?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a method to explicitly decouple the redundancy (R), synergy (S), and uniqueness (U) of the information in a pair of modalities when doing multimodal learning. The proposed method first breaks down the information from each modality into task-specific (T) and task-irrelevant (V) information, followed by aligning the redundant parts of the information in T1 and T2 (R) while keeping the unique parts separate (U1 and U2), while trying to learn the synergy between V1 and V2. To improve the quality of the decomposition, the method first trains the modality encoders, following by freezing them and only training the decomposition module, and finally training the whole model end-to-end.

The paper presents results on audiovisual datasets like CREMA-D (for emotion recognition in an acted setting), AV-MNIST, Kinetics Sounds (for sound event detection), amd CMU MOSEI (for multimodal sentiment) and compares against baselines based on joint/ensemble learning, and those based on unimodal regulation and multimodal interaction.

### Strengths
I thank the authors for sharing their ideas.I think that some of the contributions of the paper are interesting, well thought out, and clearly presented:
- I found the clear breakdown and explanation of the R, U, and S type of multimodal interactions and how they can be explicitly optimized as part of a loss function while doing multimodal learning to be a strength of the paper. Intuitively, this idea makes sense, and has been illustrated well to the reader in the equations and the figures.
- The chosen baselines make sense.
- The presented results on the chosen datasets are strong when compared to the chosen baselines.
- The technical details of the experiments are clearly presented, and the setup is understandable.

### Weaknesses
While I think that the core motivation of the paper is solid, and the proposed approach makes sense, I believe where the paper in its current state falls short is the rigor and comprehensiveness of the experiments. The same method (along with the baselines), when demonstrated with more convincing technical choices/design would make for a much stronger paper.

- The paper presents itself as a general contribution to multimodal learning, however the demonstrated experiments are only on 3 limited audio-visual datasets (and CMU MOSEI in a limited way for audio-text and visual-text). I believe that only using these datasets is not as strong a result as, for example, also showing strong and comprehensive results on vision+text, audio+vision+text, or other sensory modalities like LIDAR, ultrasonic sensors, physiological sensors (EEG / eye tracking / EMG etc). The presented results are fine if the claim of the paper was slightly more focused to the audiovisual setting (or to only CMU MOSEI for multimodal sentiment analysis). However, I do not think the experiments are "Comprehensive" and "holistic" like the authors have claimed.
- Even within the audiovisual datasets, I have significant concerns about the methodology used to extract information from each modality. For example, in the Kinetics sound dataset (which itself is dominated by the audio modality), using 1 frame per second (and a total of 10 frames per video) is not ideal (as opposed to using every frame at 25 or 30 FPS).
For the CREMA-D datasets, the authors take 1 single frame from the entire video. This is incredibly limiting for affect recognition (especially on this specific dataset), due to not capturing the temporal dynamics of emotion (such as the onset-apex-offset (see https://www.researchgate.net/figure/Typical-development-of-a-facial-expression-with-onset-apex-and-offset-from-the-survey_fig1_326023674) dynamics). Using the temporal information from the video is critical here in my opinion (it just happens to be that in an acted dataset like CREMA-D the *acted* facial expression usually coincides with the center timestep of the video) to have a method that is more generally applicable.
- I also think that the scale of the chosen datasets was limited. For example, to demonstrate the approach on solely audiovisual interactions, there are alternative datasets like AVSpeech, LRS, LRW, Audioset, along with any of the datasets in https://openaccess.thecvf.com/content/CVPR2024/papers/Singh_Looking_Similar_Sounding_Different_Leveraging_Counterfactual_Cross-Modal_Pairs_for_Audiovisual_CVPR_2024_paper.pdf
- In my opinion, the choices of the backbones (ResNet18 and LeNet) are also sufficient for basic experiments, but not to draw holistic conclusions.

### Questions
- Are there any direct comparisons to the numbers presented in the baselines? E.g. Wu et al (2024) in MMML do an extensive set of results on CMU MOSI and CMU MOSEI, whereas their method’s baseline results in this paper are quite a bit lower. What specific differences exist in these two experimental settings?
- CMU MOSEI is by far the most appropriate dataset to demonstrate the method out of the chosen datasets, since it allows for multiple different modality pairs. Why did the authors choose to do the ablations on the smaller CREMA dataset and (larger) Kinetics sounds, which are both audiovisual only, instead of on MOSEI?
- Could the method be easily extended to interactions between additional modalities than just 2? For example, multiple visual streams (along with depth, LIDAR etc) in robotics, or just audio + vision + text in MOSEI etc. Why or why not?
- Certain typos (CRAME instead of CREMA) and broken links (e.g. hyperref link in Figure 1, citations in the tables) were broken

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces an information-theoretic framework that shows the importance of learning from different interactions and the shortcomings of the traditional multimodal methods. To solve the issue, the paper proposed a decomposition-based multimodal interaction learning model that disentangles the interactions within the multi-modal data. Experiments on the various datasets and straightforward visualizations show the effectiveness of the proposed method.

### Strengths
1. The visualizations are clear and straightforward. The figures are well-designed.
2. Theoretic analysis demonstrates the importance of learning from different interactions and the shortcomings of traditional multimodal methods.
3. The proposed method shows promising performance on most of the datasets and tasks against competitive SOTA baselines.

### Weaknesses
1. The method section lacks sufficient detail and thus is a bit confusing to me. Please refer to Questions 1-6.
2. DMI’s improvements over the best baseline on AV-MNIST and CMU-MOSEI (V+T) are not statistically significant.

3. Line 322, why does synergy only contain task-irrelevant information? My understanding is that the integration of synergy has additional information to unimodal data which is task-relevant.
4. Equation 13, V and M are symmetric, which implies they can be interchanged without affecting the outcome. Given that, how do you control the learning to make one vector task-relevant and the other task-irrelevant? (which is mentioned in Line 352)
5. Line 368, training stage 1 lacks sufficient detail. Can you explain how you warm-up the encoder? Specifically, what are the input, output, and objective during this phase? Additionally, Figure 3 shows two encoders within distinct decomposition components. Are both encoders warmed up in this stage?
6. Line 371, training stage 2, “we freeze the encoder and focus solely on training the decomposition module…” Could you clarify if this means that all encoders are frozen, with only the decoders being fine-tuned in this stage?
7. In Figure 3, the decomposition modules include decoders. Does the learning objective (Equations 13 and 14) have a reconstruction loss to guide the decoders during training?
8. After decomposition is complete, how is the pre-trained model utilized for downstream tasks? Specifically, is there any further fine-tuning involved, or do you directly apply the representations learned from the decomposition modules to the downstream tasks?
9. Line 416,  can you explain the several modifications specific to each modality in ResNet18?
10. For MOSEI, are you working on sentiment analysis or emotion recognition?
11. Tables 2 and 3, performance of the uni-modal method is missing.
12. Section 4.4 ablation study, the study shows that using a single decomposition method (DMI-TC and DMI-CD) yields worse performance than the approach without any decomposition at all (DMI-FC). Can you explain the reason?

### Questions
1. Line 322, why does synergy only contain task-irrelevant information? My understanding is that the integration of synergy has additional information to unimodal data which is task-relevant.
2. Equation 13, V and M are symmetric, which implies they can be interchanged without affecting the outcome. Given that, how do you control the learning to make one vector task-relevant and the other task-irrelevant? (which is mentioned in Line 352)
3. Line 368, training stage 1 lacks sufficient detail. Can you explain how you warm-up the encoder? Specifically, what are the input, output, and objective during this phase? Additionally, Figure 3 shows two encoders within distinct decomposition components. Are both encoders warmed up in this stage?
4. Line 371, training stage 2, “we freeze the encoder and focus solely on training the decomposition module…” Could you clarify if this means that all encoders are frozen, with only the decoders being fine-tuned in this stage?
5. In Figure 3, the decomposition modules include decoders. Does the learning objective (Equations 13 and 14) have a reconstruction loss to guide the decoders during training?
6. After decomposition is complete, how is the pre-trained model utilized for downstream tasks? Specifically, is there any further fine-tuning involved, or do you directly apply the representations learned from the decomposition modules to the downstream tasks?
7. Line 416,  can you explain the several modifications specific to each modality in ResNet18?
8. For MOSEI, are you working on sentiment analysis or emotion recognition?
9. Tables 2 and 3, performance of the uni-modal method is missing.
10. Section 4.4 ablation study, the study shows that using a single decomposition method (DMI-TC and DMI-CD) yields worse performance than the approach without any decomposition at all (DMI-FC). Can you explain the reason?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper investigates the role of multimodal interaction in multimodal learning. It provides information-theoretical evidence that learning all types of interactions (redundancy, uniqueness, synergy) is necessary for good performance and shows that naive joint and ensemble learning cannot learn all types of interactions equally well. Motivated by this finding, the paper proposed the Decomposition-based Multimodal Interaction learning (DMI) paradigm that uses variation-based approach to decompose multimodal information into different types of interactions learned via a three-phase training.

### Strengths
1. **Novel theoretical analysis**: the paper presents an original theoretical analysis on the role of multimodal interaction in multimodal learning, being the first to establish a theoretical connection between multimodal interaction and multimodal learning performance. The analysis is clear, well-written, accompanied by sound proofs, which provides theoretical insights to understanding the importance of multimodal interaction in addition to prior works. The paper also proves that naive joint and ensemble learning are not able to capture all types of necessary interactions, resulting in suboptimal performance and generalization gap. 
2. **New learning paradigm for interaction learning**: the paper proposes a new learning paradigm, DMI, designed to explicitly disentangle and capture the three types of interactions and corresponding training strategy for DMI learning. Evaluation on real-world datasets corroborate some claims of effectiveness of this learning paradigm.

### Weaknesses
 1. **Generally weaker experiment section**: the paper perform a relatively comprehensive evaluation of relevant methods that also target at capturing interactions in multimodal learning; however, the analysis on the results is generally very limited.
- There is no comparison/analysis between the proposed DMI and regulation methods and other interaction methods (the paper only mentions that the improvement attributes to the effective decomposition and holistic learning of different interactions, which is weakly supported by ablations, further analysis, or the additional experiment details in appendix). Meanwhile, the reviewer is not sure whether it could be a fair comparison (e.g. are modality-specific encoders and model size standardized?) 
- The improvement from existing best-performing methods / baselines seems marginal ($\le$ 2% in accuracy), which could undermine the claims about importance of learning interactions in multimodal learning. 
- The choice of evaluation datasets / benchmarks are not justified and are also limited in terms of scope, given a wide range of multimodal datasets / benchmarks exist.

2. **Documentation of the synthetic setup needs more details**: the section on validating DMI on synthetic data and Figure 1 are interesting, but the documentation of data generation and experimental setup need more details. For example, the following aspects need more clarifications:
- How do the informative dimensions "maintain statistical relationships with the label" specifically? What are the statistical relationships that represent the three types of interactions respectively?
- How is different interaction combination (e.g. $\frac14 U+\frac34 R$, Figure 1) achieved in the data generation?
- How many synthetic data are used in this validation setting? What is the DMI architecture evaluated in this setting?
- Comparing to CVX, DMI indeed show better approximation but the evaluation is limited to one complex setting AND+XOR. Maybe adding a few evaluations on other complex logical relations (e.g. OR+XOR, AND+XOR+OR) could strengthen the claim.

In general, the reviewer agrees that if the paper is primarily a theoretical contribution, it does not need to incorporate evaluations on real-world benchmarks as comprehensively as other empirical studies, but the reviewer also believes it is necessary to document the details of data generation and experimental setup of the presented results in the appendix, which is currently missing. The reviewer believes that increasing the completion and soundness of the experiments and analysis section (compared to the theoretical section) will make this submission much stronger.

### Questions
General questions / Clarifications:
- Major questions mentioned in the Weaknesses section, including more details on experimental setup for fair comparison across methods, justification / limitation in the choice of evaluation datasets, more details on synthetic data generation and more validation settings
- Can the author clarify why synergistic information are considered as task-irrelevant features? Synergy can be very important for pure-synergy tasks such as XOR.
- **Concerns about DMI assumption**: DMI assumes a complete separation of synergistic features and features of other interactions (redundancy, uniqueness). However, can overlaps in features exist? For example, in detecting sarcasm, if a person is criticizing with a smiley face, the positive sentiment in facial expression can be unique in the visual modality, while the negative sentiment in speech is only available in the text modality, but both these features are also necessary for the inconsistency, i.e. the synergistic information, which is essential for sarcasm detection. Is DMI able to handle such cases, and how does it perform on sarcasm detection?

Notations:
- A.1 Proof for Proposition 3.1: the first term should be $\log\frac{\mathbb{E}_\boldsymbol{c}p(z,y|\boldsymbol{c})}{p(z,y|\boldsymbol{c})}$ instead of $\frac{\log\mathbb{E}_cp(z,y|\boldsymbol{c})}{\log p(z,y|\boldsymbol{c})}$ in equation 17, 18
- A.5 Explanation of decomposition: inconsistent notation $u,v$ for the first independent features

### Soundness
3

### Presentation
3

### Contribution
2
