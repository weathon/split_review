# PDED: Revitalize physics laws submerged in data information for Traffic State Estimation

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
Traditional physics-informed deep learning combines the data-driven methods with the model-based methods by incorporating physics loss as a constraint in total loss function in general, which aims to enforce the neural network to behave according to the physics property. However, this simple integration makes physical knowledge submerged in data information since data loss and physics loss could have large magnitude differences, conflicting directions of the gradients, and varying convergence rates so that the physics law may not work as expected and inhibits the model from working effectively furthermore, especially for traffic state estimation (TSE). To alleviate these issues, we propose a Physical knowledge combined Data information neural network with Ensemble Distillation framework (PDED) to first disentangle the data-driven model and physics-based model, and then reassemble them to take advantages of label information and physics property. Practically, we separately train data-driven model based on true labels and physics-based model according to physics laws. Then, we introduce the ensemble learning and knowledge distillation to assemble their representations of these two models for constructing a more competitive learnable online teacher model, which in turn distills knowledge to guide the update of them for learning richer knowledge to improve the performance of student models. Through extensive experiments on both synthetic dataset and real-world datasets, our model demonstrates better performance than the existing state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript elucidates inherent limitations in conventional physics-informed deep learning, notably the diminution of physics insights due to disparate magnitudes, antithetical gradient orientations, and inconsistent convergence tempos between distinct loss functions. To address these challenges, the authors propose the Physical knowledge combined Data information neural network with Ensemble Distillation framework (PDED). This approach disentangles the data-driven and physics-based models, then reassembles them using ensemble learning and knowledge distillation. By incorporating Bayesian Neural Networks, they also manage data uncertainty.

### Strengths
1.The manuscript highlights the inherent limitations of the physics-informed deep learning approach. Especially, there are discrepancies in magnitude between the Loss_PDE and Loss_MSE, along with distinct convergence speeds and conflicting gradient orientations. Appendix A and Figure 1 provide a lucid exposition of these issues, serving as the major highlights of this paper. 
2.PDED uses knowledge distillation, especially the ensemble distillation framework, to solve the conflict between Physics-Based model and Data-Driven model.  
3. The manuscript provides a very thorough and comprehensive ablation study. Comprehensive mathematical demonstration is contained with details

### Weaknesses
1. This paper identifies a valuable research question, but its proposed solution looks a stack of existing ensemble distillation, traffic state relation, and anomaly detection via BNN into two models, stacking sufficient external strategies to boost performance.  
2. Using Traffic State Relation Distillation, Ensemble Distillation, and anomaly detection via BNN lacks motivation. The author's approach seems to amalgamate all available techniques into the model to ascertain if performance can be improved, resembling a combination of existing strategies. At least within this paper, the author fails to provide a rationale for choosing this particular strategy, thereby giving readers an impression of a brute-force stacking of various established methods. 
3. Experiment 3.4 Noise Robustness Analysis 
The PDED has better noise robustness compared to the baselines since it utilizes the BNN to measure data uncertainty and adopts uncertainty to guide the fusion process. However, the comparison with the other two models is not rigorous enough. While a significant part of the robustness improvement in your model can be attributed to the integration of the BNN, it's inconclusive whether the NN and PIDL models, if augmented with uncertainty quantification, would demonstrate weaker noise robustness than PDED.

### Questions
1.	Could you elaborate on the difference/superiority between the proposed method and existing works on combining physical losses and standard ML losses (e.g., MSE)?

2.	See other comments in weaknesses above

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an ensemble (teacher-student) based physics-informed and data-driven model for traffic state estimation. Specifically, due to the well-known complexity of coupled modeling of physics information (in the form of PDE based conservation conditions) and data-driven (e.g., Mean-squared error) losses, the paper proposes a de-coupled method of modeling these two steps by first employing a physics-informed neural network to model the PDE based losses and a Bayesian Neural Network to model the data-driven losses. Further, a feed-forward neural network is employed to ensemble the predictions of the physics-informed and data-driven components by employing the latent representations from each of the two (I.e., physics-informed and data-driven) models. The ensemble model (infused with both data-driven and physics-driven knowledge) is trained in a data-driven manner and knowledge from the ensemble (teacher) model is distilled into each individual physics-driven, data-driven (student) models. In this manner, employing a combination of ensemble modeling, physics informed neural networks and knowledge distillation, the paper proposes a Physics-Informed Deep Learning (PIDL) solution for traffic state estimation.

### Strengths
1. Two interesting parts about the paper are (i) the alternating teacher / student training (ii) the uncertainty fusion employing the BNN covariance matrix.  However, not enough is discussed about either of these aspects in the main paper. 
  

2. Overall the paper is cohesive and well-written.  The quantitative and qualitative results (although incomplete) demonstrate that the proposed framework yields good performance relative to baselines in addition to highlighting the importance of each component (ablation analysis).

### Weaknesses
- **[Limited Novelty].** The proposed model is a combination of a physics informed neural network (PINN) employed with a relatively simple PDE, in addition to another standard Bayesian Neural Network (BNN) paradigm combined with knowledge distillation (KD). These three paradigms (PINN, BNN, KD) are all extremely well studied, well-understood and the current paper doesn’t propose any novel extensions of the actual paradigms or increase the characteristic understanding of any of the aforementioned paradigms. It is simply an exercise in the application (specifically, the combination) of these paradigms in a (somewhat) creative way to address the problem of traffic state estimation.  
    - Further, the knowledge that the physics losses and data-driven loss don’t always play well together (mentioned in contribution 1) isn’t new and has been well researched in the context of physics-informed neural networks applied to PDEs [3, 4, 5]	 
 

- **[Important Related Work Missing].** The paper completely misses mentioning operator learning paradigms which are more recent updates to traditional PINNs which learn families of PDEs as opposed to single instances of PDEs (albeit in a slightly different manner) however the reviewer believes that a brief description of operators like [1, 2] would contextualize the current work in the physics informed deep learning space.  
 

- **[Incomplete Performance comparison].** A related paper Trafficflowgan [6] that employs physics information, uncertainty aware GAN for traffic state estimation has not been compared against. 

### References:

1. Lu, Lu, Pengzhan Jin, and George Em Karniadakis. "Deeponet: Learning nonlinear operators for identifying differential equations based on the universal approximation theorem of operators." arXiv preprint arXiv:1910.03193 (2019). 
 

2. Li, Zongyi, et al. "Fourier neural operator for parametric partial differential equations." arXiv preprint arXiv:2010.08895 (2020). 
 

3. Krishnapriyan, Aditi, et al. "Characterizing possible failure modes in physics-informed neural networks." Advances in Neural Information Processing Systems 34 (2021): 26548-26560. 
 

4. Wang, Sifan, Yujun Teng, and Paris Perdikaris. "Understanding and mitigating gradient flow pathologies in physics-informed neural networks." SIAM Journal on Scientific Computing 43.5 (2021): A3055-A3081. 
 

5. Kim, Jungeun, et al. "DPM: A novel training method for physics-informed neural networks in extrapolation." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 35. No. 9. 2021. 
 

6. Mo, Zhaobin, et al. "Trafficflowgan: Physics-informed flow based generative adversarial network for uncertainty quantification." Joint European Conference on Machine Learning and Knowledge Discovery in Databases. Cham: Springer Nature Switzerland, 2022.

### Questions
1. Why has TrafficflowGAN [6] not been compared despite being a related / physics-informed + uncertainty aware model for traffic state estimation?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new knowledge-guided ML method, called PDED. PDED disentangles the data-based and physics-based modules, which are trained with labeled data and physics laws respectively. Ensembling learning and knowledge distillation are used to assemble those two representations. Superior performance has been shown to validate the effectiveness of the proposed method.

### Strengths
- This paper proposes a new framework for combining physics laws and data, which aims to avoid the optimization issue in common physics-informed learning tasks. 

- This paper is well-written and well-structured.

### Weaknesses
- It seems that this method still has many hyperparameters to tune as shown in Eq. (14) and (15), though the goal of this paper is to mitigate the optimization issue in physics-informed learning. I am not sure of the magnitude differences between those loss terms in physics loss and data loss in  Eq. (14) and (15).

- As shown in **Experiments settings** on Page 6, all of the hyper-parameters are set to 1. It seems they don’t have large variances in magnitudes. However, the test datasets focus on $x, t$ dimensions, which can be regarded as 1D PDEs in physics-informed learning. 1D PDEs are relatively easy to learn, and the optimization issues are not severe. I am wondering if the authors could test on more challenging 2D datasets in traffic modeling.

### Questions
- On Page 2, the authors claim that they discovered the optimization issue of physics-informed learning, where many existing research works have identified this problem [1-2]. I don’t think that is one of the contributions of this paper. 

- On Page 5, “As mentioned by Theorem 2.1, the effectiveness of ensemble teacher model is also determined by the the accuracy of individual student model.” There is a double “the” in this sentence. 

- This paper considers relative L2 errors, as commonly seen in physics-informed learning research. However, in the domain of traffic prediction, researchers also consider RMSE and MAPE to measure the errors from different perspectives. Is it possible to add more evaluation metrics since the traffic data has some rush hour phenomena, where extreme statistics are needed? 

- Regarding the noise setting in Section 3.4, is it common to set the noise ratio by using a small covariance of 0.01/0.04 in the Gaussian distribution? Can the authors add some references here?

---
**Refs:**

[1] Krishnapriyan, Aditi, et al. "Characterizing possible failure modes in physics-informed neural networks." Advances in Neural Information Processing Systems 34 (2021): 26548-26560.

[2] Wang, Sifan, Yujun Teng, and Paris Perdikaris. "Understanding and mitigating gradient flow pathologies in physics-informed neural networks." SIAM Journal on Scientific Computing 43.5 (2021): A3055-A3081.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
