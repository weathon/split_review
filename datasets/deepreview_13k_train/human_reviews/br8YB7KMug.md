# ImDy: Human Inverse Dynamics from Imitated Observations

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
Inverse dynamics (ID), which aims at reproducing the driven torques from human kinematic observations, has been a critical tool for human motion analysis. 
However, it is hindered from wider application to general motion due to its limited scalability. 
Conventional optimization-based ID requires expensive laboratory setups, restricting its availability. 
To alleviate this problem, we propose to exploit the recently progressive human motion imitation algorithms to learn human inverse dynamics in a \textit{data-driven} manner.
The key insight is that the human ID knowledge is implicitly possessed by motion imitators, though not directly applicable.
In light of this, we devise an efficient data collection pipeline with state-of-the-art motion imitation algorithms and physics simulators, resulting in a large-scale human inverse dynamics benchmark as \textbf{Imitated Dynamics} (\textbf{ImDy}). 
ImDy contains over \textbf{150 hours} of motion with joint torque and full-body ground reaction force data.
With ImDy, we train a data-driven human inverse dynamics solver \textbf{ImDyS(olver)} in a fully supervised manner, which conducts ID and ground reaction force estimation simultaneously.
Experiments on ImDy and real-world data demonstrate the impressive competency of ImDyS in human inverse dynamics and ground reaction force estimation.
Moreover, the potential of ImDy(-S) as a fundamental motion analysis tool is exhibited with downstream applications.
The project page is \href{https://foruck.io/ImDy}{https://foruck.io/ImDy}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper focuses on human inverse dynamics, aiming to estimate the driving torques of body joints from motion observations. While previous methods have primarily targeted lab settings, this paper employs imitation learning within physics simulators. Building on this approach, the authors created a dataset by importing the AMASS and KIT datasets into Isaac Gym, obtaining contact forces and joint torques based on the previous PHC method. Experimental results also demonstrate improved performance compared to the AddBiomechanics benchmark after fine-tuning.

### Strengths
1. Estimating human dynamics from motion observation is an interesting and meaningful direction.

2. The paper is well-written and easy to follow.

3. The proposed strategy is to make human dynamics look effective.

4. Experiments show better performance than previous methods.

### Weaknesses
While the proposed method looks promising, I am concerned that its technical contributions may be limited for an ICLR paper. Numerous previous works on physics-aware pose estimation have utilized human dynamics through either non-differentiable physics simulators with reinforcement learning or differentiable dynamics solvers, both of which seem to be more challenging approaches. In these prior works, dynamics estimation often served as an intermediate task, either implicitly or explicitly. In this paper, it seems that only part of the previous methods were adopted, with an increased focus on dynamics estimation. Furthermore, the method employed is also similar to as that of PHC. The core issue is that the paper appears to re-purpose existing techniques for a slightly different objective without introducing substantial methodological novelty. The use of imitation learning within a physics simulator, while effective, does not represent a significant leap from prior work that has used similar techniques for related problems. The paper lacks a detailed comparison to these methods, particularly in terms of the specific challenges addressed and the novel solutions proposed. The focus on large-scale data collection, while valuable, does not compensate for the incremental nature of the methodological contribution.

### Questions
1. KIT is also part of the AMASS dataset, but the paper mentions using the AMAS and KIT datasets. Is there any difference?

2. ImDyS is tuned on AddBiomechanics for 10 epochs. How is the performance without fintuning?  

3. I am also curious about whether a better-estimated dynamics is helpful for downstream tasks like human pose estimation.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a dataset ImDy (Imitaed Dynamics) with 150 hours of physically simulated humanoid characters imitating kinematic human motions with joint torques and full-body ground reaction forces. The paper claims that ImDy data is unique in its scale (100x more than previous ones), includes more general physics parameters such as the ground reaction forces (GRFs) for the entire body, and is represented in SMPL. Using this ImDy, the paper proposes ImDyS (Imitaed Dynamics Solver), a data-driven humanoid inverse dynamics solver. ImDyS is a simple encoder-head design where a transformer encoder maps the pose state to the ID (inverse dynamics) feature, which is used to predict the dynamics using linear heads. The notable loss designs are the use of the FD (forward dynamics) cycle consistency loss with an FD model trained together to predict the pose state from the dynamics, and a discriminator loss on the ID features, similar to AMP [Peng et al. 2021]. To overcome the sim2real issues, the model is trained in two stages, first with the ImDy data, and then with the data from AddBiomechanics while freezing the encoder and training only the linear head for joint torques.

### Strengths
The proposal is a great data and baseline model to advance the data-driven approach to understanding dynamics in human motions. While the baseline model ImDyS is simple, I see enough novel, especially in the loss design with the cycle consistency using the learned FD model and a discriminator loss on the ID features.

### Weaknesses
The paper is straightforward and looks good. I appreciate some clarifications in the questions

Have the authors studied the error in the learned FD model? Is it possible to replace this with a differentiable FD simulation?

I would appreciate it if authors could share visual ablations with various motions, with and without the AddBiomechanics so I can confirm the effect of the sim2real, especially for motions out of distribution from the AddBiomechanics data. It is hard to tell how much jittering still exists just by looking at the mPJE.

### Questions
Have the authors studied the error in the learned FD model? Is it possible to replace this with a differentiable FD simulation?

I would appreciate it if authors could share visual ablations with various motions, with and without the AddBiomechanics so I can confirm the effect of the sim2real, especially for motions out of distribution from the AddBiomechanics data. It is hard to tell how much jittering still exists just by looking at the mPJE.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, authors introduce data-driven inverse dynamics solver (ImDyS) that could estimate dynamic states of the person (including joints torque and ground reaction forces) from the observed kinematics. To train ImDyS in a fully-supervised manner, they first propose the data acquisition to collect scalable human dynamics data following the recently proposed imitation learning methods. 

They benchmarked their method on both the imitated data (ImDy) and real-world data, AddBiomechanics, which has the measured ground reaction forces and 3D kinematics labels. The results showed that the proposed method is more accurate to estimate human dynamics from both the imitated and real datasets. 

Since the authors borrow the concept of imitation learning from the previous work (PHC), I do not see significant novelty in their data acquisition pipeline. However, given their contribution to processing and sharing of the dataset, and the performance of the supervised inverse dynamics module, I think the paper can contribute to the community.

### Strengths
The paper's strengths can be summarized as follows:

1) They train an imitation policy that can imitate the large-scale human motion capture dataset (AMASS and KIT) which provides the pairs of human kinematics and dynamics with the larger scale than any other publicly available datasets.

2) They train an inverse dynamics solver on the processed data, resulting in the state-of-the-art performance in estimating ground reaction force and dynamics state of the human (on both imitated and real data).

3) Good visual presentation is appreciated

### Weaknesses
Data acquisition part of this paper does not seem to include significant novelty since most of the part were borrowed from the previous work (PHC, Luo et al.,). I would like authors to elaborate what their imitation learning can offer other than PHC. Can we run PHC to collect kinetic/kinematics pairs of AMASS and KIT data? If so, why do we need to use the proposed method for the dynamics data acquisitions?



### Questions
1) Connected to the weakness that I pointed above, why does authors' imitation on AMASS have lower success rate than PHC? I would suggest the authors to provide quantitative/qualitative comparisons of two imitation learning schemes (their and PHC), and justify their purpose of the proposed method.

2) It is not clear what can ImDyS bring over the imitation learning. Let's assume we collect kinematics data and want to extract dynamics from it. We can either run ImDyS to estimate dynamics or ImDy policy to imitate the kinematics (where the dynamics will come together). What is the major benefit of using ImDyS in this case? I guess the inference speed but wonder authors' perspective. I would suggest authors to provide comparisons between the proposed IL and ImDyS to highlight the unique values of ImDyS.

### Soundness
3

### Presentation
4

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
This paper proposes ImDy, a human inverse dynamics benchmark & dataset that contains 150 hours of motion with joint torque and full-body ground reaction forces obtained from humanoid motion tracking. ImDy provides a scalable approach to obtain more joint-level actuation for human motion as well as ground reaction force grounded in physics simulation. Experiments show that data obtained from ImDy could support learning an inverse dynamics model that has competitive performance on real-world data, showcasing the advantage of having large-scale synthetic dynamics data obtained from simulation.

### Strengths
- The proposed ImDy and ImDyS, as far as I know, is a novel attempt at using simulation and humanoid motion tracking to obtain large datasets for inverse dynamics analysis. The results show that the large-scale dynamics data obtained from simulation could be of use in learning models (ImDyS) that perform well on real human performance data.
- A comprehensive analysis of the proposed ImDyS and the baselines is provided. Since this is a relatively new topic, not many prior arts exist. Nonetheless, ImDyS outperforms the baselines and generalizes to real-world data with competitive performance.
- I appreciate the analysis of failure cases, which analyzed the advantages of ImDyS and plausible causes for failure in predicting the joint torques on the jumping motion.

### Weaknesses
 - Since a dataset is proposed, an analysis of the data composition (like in Figure 12) would be beneficial. Since AMASS also contains many locomotion data, and the PHC with a naive PD controller has a lower success rate, it would be good to see what motions are tracked and included in the dataset. Specifically, a breakdown of the types of activities (e.g., walking, running, jumping, manipulation) and their respective proportions within the dataset would be valuable. Furthermore, it would be helpful to understand the distribution of motion speeds and complexities, as these factors can significantly impact the performance of inverse dynamics models. This analysis should also include the range of joint angles and velocities observed in the dataset, as this information is crucial for assessing the generalizability of the learned models.
- ImDys has many details that seem to be omitted. A data flow chart that includes the different losses in the appendix would be helpful. It is unclear how the different loss terms (e.g., reconstruction loss, discriminator loss, and any other regularization terms) are weighted and combined during training. The specific architectures of the networks used for inverse dynamics prediction and the discriminator are not clearly specified. What is the motivation for including the discriminator loss if it does not contribute much to accuracy (as shown in Table 5)? The lack of clarity on these implementation details makes it difficult to reproduce the results and fully understand the method's behavior.


Minor:

- I would recommend changing the term "imitation learning" to "motion tracking" as "imitation learning" is quite overloaded nowadays.

### Questions
Figure 11 visualizes a failed joint prediction case; the plot shows that ground truth torques are quite smooth while the predicted are jittery (before both the ground truth and predicted are jittery). Based on the provided analysis, it is possible the data quality of AddBioMechanics could be the cause here?

### Soundness
3

### Presentation
3

### Contribution
3
