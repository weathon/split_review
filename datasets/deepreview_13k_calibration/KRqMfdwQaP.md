# SEAL-Pose: Enhancing Pose Estimation through Trainable Loss Function

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
Accurately predicting 3D human pose is a challenging task in computer vision due to the need to capture complex spatial structures and anatomical constraints. We propose SEAL-Pose, an adaptation of the Structured Energy As Loss (SEAL) framework for deterministic models, specifically designed to enhance 3D human pose estimation from 2D keypoints. 
Although the original SEAL was limited to probabilistic models, our approach employs the model's predictions as negative examples to train a structured energy network, which functions as a dynamic and trainable loss function. 
Our approach enables a pose estimation model to learn joint dependencies via learning signals from a structured energy network that automatically captures body structure during training without explicit prior structural knowledge, resulting in more accurate and plausible 3D poses .
We introduce new evaluation metrics to assess the structural consistency of predicted poses, demonstrating that SEAL-Pose produces more realistic, anatomically plausible results.
Experimental results on the Human3.6M and Human3.6M WholeBody datasets show that SEAL-Pose not only reduces pose estimation errors such as Mean Per Joint Position Error (MPJPE) but also outperforms existing baselines.
This work highlights the potential of applying structured energy networks to tasks requiring complex output structures, offering a promising direction for future research.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents SEAL-Pose, a Structured Energy As Loss framework to improve the 3D pose estimation from 2D keypoints. The SEAL loss is previously applied in probabilistic models whereas the paper modifies it to deterministic models. This loss improves the dependencies among the keypoints which produces more plausible poses empirically.

### Strengths
1. This paper addresses an interesting problem of improving the plausibility of output pose. The SEAL loss is new and effective.
2. This paper is easy to understand.

### Weaknesses
1. The writing of this paper can be improved, e.g., the names of task-net and loss-net are confusing since the task here is only pose estimation and loss-net only refers to energy loss. Also, it would be clearer if authors can give an overview of what each net functions in the beginning of Sec.3.1.
2. The motivation is not clearly explained and verified. It’s not clear why SEAL-Pose can improve the plausibility of estimated poses and why it can perform better in the proposed metrics, i.e., LSE, BSLE, and LLE. The paper lacks a clear explanation of how the structured energy loss specifically enforces the desired structural constraints on the pose. It's unclear how the loss-net learns to represent plausible poses and how this representation is then used to guide the task-net. The connection between the energy landscape learned by the loss-net and the resulting pose plausibility is not sufficiently established.
3. The method should be evaluated on more advanced frameworks. It’s necessary for this method to compete against state-of-the-art methods and on more challenging benchmarks, for example, 3DPW, MPI-INF-3DHP. In Table 2, the performance is very similar to the baseline method VideoPose. The evaluation is limited to a single baseline and does not demonstrate a clear advantage over existing methods on more complex datasets. The paper would benefit from a more comprehensive comparison against a wider range of state-of-the-art techniques.
4. Minor issues:
    1. Inconsistency between P-MPJPE and PA-MPJPE in H36M and H3WB
    2. The quality of figures can be improved

### Questions
The contributions do not reach the bar of ICLR therefore I recommend rejection. The further improvement can be better presentation of paper and more experimental validation of the proposed loss.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work addresses 2D-to-3D human pose lifting, by applying the "Structured Energy as Loss" (SEAL) framework. That is, besides training a regressor for the task (here called task-net), a second network (loss-net) is also trained that scores prediction-input pairs for their plausibility. At inference time, the output can be taken as is, or gradient-based inference (GBI) can be applied to modify the prediction towards driving down the loss-net output (to make the prediction seem more plausible to the loss-net). This GBI can be applied by tuning either the prediction itself or the model weights.
The motivation is to better take into account dependencies in the output variables, such as bone lengths in the case of human pose estimation.
The model is evaluated on Human3.6M and its whole-body extension and is shown to improve the scores.

### Strengths
* The problem of human pose lifting is of interest to the research community.
* Applying the SEAL framework to this task is novel.
* The method, when applied to SimpleBaseline and VideoPose3D, improves results on Human3.6M, both in terms of the standard metrics and in terms of bone symmetry and bone length error.
* The ablation model (Section 3.2) is useful in demonstrating the value in training the loss-net together with the task-net.

### Weaknesses
 * The most serious problem I see is using a hyperparameter sweep tool (from WandB) to tune hyperparameters directly for the Human3.6M/H3WB test set. If this was indeed done so, it invalidates the seen improvements, as the gap is not so large and tuning hyperparameters for a particular test set can aways achieve significantly stronger results.
* While the method is motivated from the prior SEAL method, I am not convinced that the terminology of structured energy is helpful for understanding rather than obscuring what actually happens in the approach. In essence, the final model is a fairly standard conditional GAN. The terminology of "structured" learning/energy/outputs comes from the pre-deep-learning era when multi-output model were generally less standard and more difficult to train. Today, talking about a learned loss function or indeed simply a discriminator may be much better understood by the community, since models that make "structured" predictions are commonplace today. GANs have been used in a similar fashion for 2D-to-3D lifting (e.g. [3]), diminishing the novelty of the proposed paper.

* The work only uses Human3.6M (and its wholebody extension). While Human3.6M has been very valuable for research over the last decade, today we now have many more datasets and it is now possible to give stronger evidence for a method than improvements on two specific subjects. The particular bone-length structures of subject 9 and subject 11 of H36M may not generalize. Other possible training datasets would include the following (of course I do not expect using all of these, it is just to give some ideas): MPI-INF-3DHP, CMU-Panoptic, AMASS, HuMMan, AIST-dance++, AGORA, BEDLAM, GeneBody, DNA-Rendering, RICH etc. And other evaluation datasets include 3DPW and EMDB. Again, I do not expect using all, but using at least something further beyond the Human3.6M data would make the evidence much stronger.
* The baseline methods (SimpleBaseline, VideoPose) are fairly old by the standards of this field (2017 and 2019). It would be important to try newer lifting methods as well. The results are also not compared to the current SOTA methods or those from the last five years.
* The writing is quite verbose, for example an full page (page 5) is spent on describing limb length losses, which could be expressed in a briefer way. Such bone-based losses and metrics have been used in many prior works, for example [2,3]
* It is not clear why the SemGCN model has spikes in the training curve (Fig. 3). These spikes can appear for many practical reasons in a particular implementation and do not generally mean a fundamental problem.

### Questions
* Is GBI used in combination with SEAL? Fig. 2 (left) seems to indicate so but the text does not make this clear.
* As far as I understand, the method is only tested with ground-truth 2D keypoints (L200). This is not a realistic setup, and 2D keypoints from 2D pose estimators would yield a more realistic evaluation. Is this correct?
* Are the hyperparameters tuned for the test set?

### Soundness
2

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
4

### Summary
This paper presents SEAL-pose to handle 2D-to-3D lifting problem in human pose estimation. The core is training a learnable loss function to encode the structure of output body limbs. To evaluate the performance, the authors propose two new metrics: Limb symmetry error (LSE) and Body segment length error (BSLE). Experiments are performed on H36M and H3WB.

### Strengths
The incorporation of SEAL framework for 3D human pose lifting is a novel idea. The experiments could support the effectiveness of SEAL-psoe to some degree.

### Weaknesses
Description of methods should be improved. Experiments are not enough. See Questions below.

1. The technical part is not clearly stated, thus making the readers hard to follow. For example, in eqn(1),(3), how is B_t defined? How is \eta_{\phi} defined? Is “x” the input image or 2D pose for lifting? Is L the joint number?

2. There are many previous methods that estimate a probabilistic distribution of output 3D skeleton from 2D input (e.g. Diffusion-based 3d human pose estimation with multi-hypothesis aggregation, ICCV 2023). It may be better for SEAL pose to combine with such framework instead of a deterministic model.

3. Why not use MPI-INF-3DHP for evaluation? The experiments have been limited to the camera settings of H36M, which may not convince the readers for the generalization ability of SEAL-pose.

4. The authors propose LSE and BSLE. However, they only report these two metrics on H3WB in Table.3. Why not report on H36M for body only poses?

5. Is there any visualized comparison to demonstrate the 3d lifting quality of SEAL-pose? Without visualized results, I could not fully understand the improvement brought by lower LSE and BSLE. As H3WB contains 133 keypoints with distinct scale, which part is  improved the most (face, or hand, or body)?

### Questions
1. The technical part is not clearly stated, thus making the readers hard to follow. For example, 
in eqn(1),(3), how is B_t defined? How is \eta_{\phi} defined? Is “x” the input image or 2D pose for lifting? Is L the joint number? 

2. There are many previous methods that estimate a probabilistic distribution of output 3D skeleton from 2D input (e.g. Diffusion-based 3d human pose estimation with multi-hypothesis aggregation, ICCV 2023). It may be better for SEAL pose to combine with such framework instead of a deterministic model. 

3. Why not use MPI-INF-3DHP for evaluation? The experiments have been limited to the camera settings of H36M, which may not convince the readers for the generalization ability of SEAL-pose. 

4. The authors propose LSE and BSLE. However, they only report these two metrics on H3WB in Table.3. Why not report on H36M for body only poses? 

5. Is there any visualized comparison to demonstrate the 3d lifting quality of SEAL-pose? Without visualized results, I could not fully understand the improvement brought by lower LSE and BSLE. As H3WB contains 133 keypoints with distinct scale, which part is  improved the most (face, or hand, or body)?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces a Structured Energy As Loss (SEAL) framework aimed at improving 3D human pose estimation. However, the paper is incomplete (less than eight pages) and lacks a description of the method’s motivation, a comparison with prior approaches, and an evaluation against state-of-the-art methods.

### Strengths
The proposed method is simple but effective.

### Weaknesses
1. The diagram in Figure 1 is overly simplistic and does not effectively convey the motivation behind the proposed method.
2. The paper is incomplete (less than eight pages), lacks a thorough description of the method’s motivation, a discussion on advantages over prior methods, and comparisons with state-of-the-art approaches.

### Questions
Please see the Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
