# Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Unsupervised reinforcement learning (RL) aims at pre-training models that can solve a wide range of downstream tasks in complex environments. Despite recent advancements, existing approaches suffer from several limitations: they may require running an RL process on each task to achieve a satisfactory performance, they may need access to datasets with good coverage or well-curated task-specific samples, or they may pre-train policies with unsupervised losses that are poorly correlated with the downstream tasks of interest. In this paper, we introduce FB-CPR, which regularizes unsupervised zero-shot RL based on the forward-backward (FB) method towards imitating trajectories from unlabeled behaviors. The resulting models learn \emph{useful} policies imitating  the behaviors in the dataset, while retaining zero-shot generalization capabilities. We demonstrate the effectiveness of FB-CPR in a challenging humanoid control problem. Training FB-CPR online with observation-only motion capture datasets, we obtain the first humanoid behavioral foundation model that can be prompted to solve a variety of whole-body tasks, including motion tracking, goal reaching, and reward optimization. The resulting model is capable of expressing human-like behaviors and it achieves competitive performance with task-specific methods while outperforming state-of-the-art unsupervised RL and model-based baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes FB-CPR, a regularizer for unsupervised RL that improves its pre-training performance given a state-only trajectory dataset. FB-CPR is built on prior works of forward-backward (FB) representation in RL & successor measures of state. An FB approximation is trained with bellman update and can used to approximate successor measure, which is used as a zero-shot policy evaluator. Furthermore, using tricks from prior works, the authors further uses a latent vector z to extend the core components (FB & successor measure) to multiple policies. At pre-training time, FB-CPR is used as an regularizer, with a discrimination loss added to original unsupervised RL objective to make sure learned behavior stay close to the distribution in the dataset. FInally, the authors evaluated the merit of the proposed method with one natural application of simulated humanoid control, where mocap data (state-only trajectory dataset) is available. The resulting method outperforms baselines by some metrics, with outstanding performance in staying human-like.

### Strengths
The method is sound towards its goal. Intuitively, the discriminator encourages FB_CPR to learn policies that makes it roll out stay close to that in the dataset M, while the Q function itself is approximated by Fz.

The paper's presentation is clear considering its technical depth.

The paper is solid with extensive details for reproduction, evaluations, and sufficient mathematical details. The experiments considered sufficient baselines and there are a good amount of ablations for more insights

### Weaknesses
I think the authors explained the necessary details very well in their writing. However, given that the technical depth of FB heavily depends on prior works, I think the authors should definitely provide more intuitions along the way. When reading the prelim section, there are many times that I need to stop and ask myself why is this math transformation okay. A paper shall be relatively self-contained, and shall still allow readers to understand the high-level intuition of each equation without consulting the details of prior works. 

One core assumption of the work is that one can reparameterize the policy dependence with the introduction of a policy embedding z (Eqn 4). I wonder how grounded is this, especially when z has to live in a continuous space. I list a few questions about z in my Questions section.

It's pretty clear that the paper heavily depends on the prior line of work of FB & state measure. I skimmed the mentioned works in the prelim section, and it seems that most of these works are evaluated on relative toy datasets only e.g. maze. Therefore, it's a big step for the authors to make claims about an application like humanoid control while skipping evidence of FB & state measure methods being general enough for RL benchmarks. This makes readers wonder whether there are hidden limitations of the proposed method. It seems that standard RL benchmarks are out of scope for this project given its unique setting of having some state dataset, but alternative evidence to address my above concern would be appreciated. 

Figure 2 is very helpful to one's understanding of the method. However, I believe two simple changes could significantly enhance it: 1. link $F(\dot,z)^\top z$ back to $Q^\pi$ to remind readers of this connection back in prelim, especially because $Q^\pi=F(\dot,z)^\top z$ wasn't even highlighted with its own equation number. 2. Add a post-training / adaptation box that emphasizes all prior training is happening without reward, and is a separate part from downstream abilities.  

Algorithm 1 is very helpful too, and I believe many readers would be looking for an algorithm box like this in main paper. The authors could highlight it's in the appendix more, or put a abbreviated algo box in main paper called "Algorithm 1 (informal)", and link readers to the full version in the appendix in the caption.

I wonder whether TD3 is a competitive baseline at all for "Naturalness" - it seems like sequence-based methods like diffuser serve as a stronger baseline here, as RL methods are purely optimized for reward maximization.

### Questions
What's the dimension of z? Usually, a policy has to be represented by a neural network. I wonder whether a compact latent variable z is expressive enough to represent policies that have combinatorial complexity. In that case, you must be sacrificing something. Could you provide more intuitions and conduct more ablations on the dimension of z?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes FB-CPR, a variant of FB representations that regularize behaviors to offline trajectory data. Their main idea is to define a regularization reward with a GAN-style discriminator, and add this as a bonus to the original FB reward. Importantly, the authors condition this discriminator on an inferred $z$, making the regularization more targeted. They apply FB-CRP to Humanoid control, showing that it achieves better performance and naturality than other baselines.

### Strengths
* The paper is of high quality and well-written.
* To my knowledge, this is one of the few works that scale unsupervised RL up to Humanoid control.
* The proposed objective is clean and reasonable.
* The paper presents several ablation studies, which help understand the importance of the individual components of FB-CPR.

### Weaknesses
 * One weakness is its limited novelty. The method is largely built upon the previous FB framework, and the only difference between the original FB paper and this work is the additional discriminator term for behavioral regularization. Having a data-regularization term in data-driven RL (i.e., BC, offline RL, motion priors, etc.) is a standard, well-established technique. While FB-CPR's conditioning of the discriminator on inferred $z$ is distinct from standard offline RL regularization techniques, I believe this alone doesn't constitute significant novelty, given how other skill-based offline unsupervised RL works (e.g., HILP (Park et al., 2024), FRE (Frans et al., 2024), etc.) employ similar $z$-inference techniques when applying behavioral regularization, though they don't use explicit discriminators. The core idea of using a discriminator to match a learned policy to a dataset is not new, and the specific contribution of conditioning this discriminator on the latent variable $z$ feels like a minor modification rather than a fundamental innovation, especially given the existing literature on latent variable models for skill discovery.
* Another weakness is that the effectiveness of FB-CPR is only shown on Humanoid. While Humanoid control is indeed an important problem, it is unclear whether FB-CPR can generally be applicable to other environments, or if it is only effective for Humanoid. The paper lacks experiments demonstrating the method's performance on other benchmark tasks, such as those found in D4RL, which would help to establish the generality of the approach. Without these experiments, it is difficult to assess whether the method is truly robust or if its success is limited to the specific characteristics of the Humanoid environment.
* It seems the benefits of FB-CPR mostly come from behavioral regularization, and the contribution of the FB objective seems relatively marginal (Fig. 4, top right). While the authors show that the FB objective helps to some degree, given the significant complexity of the FB algorithm and its marginal effect on performance, I'm not entirely convinced that having the FB component is worthwhile. The ablation study suggests that the discriminator-based regularization is the primary driver of performance gains, raising questions about the necessity of the FB component, which adds significant complexity to the overall algorithm. A more thorough analysis of the individual contributions of each component is needed to justify the inclusion of the FB objective.

### Questions
I'm curious why FB-CPR is only shown on Humanoid control. For example, could the same method be applied to manipulation environments (e.g., D4RL Kitchen or similar human demonstration-based manipulation datasets)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose to augment the forward-backwards unsupervised RL framework with a policy regularization term that encourages covering the entire set of behaviors present in the training dataset. They do so by augmenting the FB loss with a discriminator that determines whether a state came from the dataset or from the policy. The authors provide extensive experiments on humanoid control problems showing that FB-CPR approaches the performance of policies trained on individual goals and outperforms other multi-task baselines.

### Strengths
- The authors present their method clearly and motivate the problem setting well.
- The proposed method is a simple addition to the standard FB framework.
- The proposed implementation allows steering the model to learn useful behaviors by modifying the latent distribution of skills used during training.

### Weaknesses
 - The majority of the evaluations are conducted only on the humanoid environment. Although the number of experiments done in this environment is diverse, higher diversity in environments would make the paper even stronger. Specifically, the method's performance on tasks requiring different control strategies, such as navigation or manipulation, remains unclear. The reliance on a single type of environment limits the generalizability of the findings.
- Although more “human like” behavior (more like the training dataset) might be desirable in a humanoid environment, could the regularization negatively affect performance where the majority of the data is very suboptimal? It is not clear how the method would perform if the demonstration data is of poor quality or contains behaviors that are not aligned with the desired task. The regularization might bias the policy towards these suboptimal behaviors, hindering the learning of effective strategies.
- It feels like something like METRA [1], which is explicitly trained to span a diverse set of behaviors, is also a relevant baseline. It tackles a similar problem that the proposed regularization intends to solve: spanning a diverse set of useful behaviors. The lack of comparison to such methods makes it difficult to assess the novelty and effectiveness of the proposed approach.

### Questions
- On the humanoid experiments, why aren’t there more direct comparisons to FB without the proposed regularization? There are a few ablations in the appendix with direct comparison to FB, but this also feels relevant to the main experiments. 
- How does the proposed regularization affect the nature of the embedding space? Could a nicely regularized latent space enable something like interpolations between skills etc.?

References:
[1] Seohong Park, Oleh Rybkin, and Sergey Levine. METRA: scalable unsupervised RL with metric-aware abstraction. In ICLR. OpenReview.net, 2024b.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes an algorithm that pre-trains behavioral foundation models (BFMs) using unlabeled motion capture data for zero-shot generalization to humanoid control tasks. It combines the Forward-Backward (FB) representation with Conditional Policy Regularization (CPR) to solve tasks like motion tracking, goal-reaching, and reward optimization. FB-CPR outperforms existing unsupervised RL algorithms and model-based methods, achieving competitive results compared to task-specific models while also producing more human-like behavior.

**Post-Rebuttal Review**

Thanks for the detailed response. I have carefully read your rebuttal and it resolved most of my concerns. I will raise my score accordingly.

### Strengths
The authors address the challenging problem of generalizing to unseen tasks in humanoid whole-body control without the need for task-specific training. The paper provides a lot of details in the appendix, a well-designed and thorough experimental section. The experiments cover a wide range of scenarios, demonstrating the method's effectiveness across various tasks.

### Weaknesses
The problem definition is not very clear, making it difficult to understand at the beginning. The theoretical explanations about FB representation might be a little complicated for readers lacking corresponding background. Some explicit examples or pictures may help.

It is unclear how the advantages and differences of this method compare to previous approaches, such as AMP[1] and ASE[2], as well as to recent work (like Omnigrasp[3], MaskedMimic[4]), when applied to the demonstration data settings discussed in this paper. Specifically, the paper does not clearly articulate how the conditional policy regularization differs from the adversarial imitation learning techniques used in AMP and ASE, and how this difference leads to the claimed improvements in tracking and reward optimization. Furthermore, the comparison with Omnigrasp and MaskedMimic is lacking, especially considering their relevance to the humanoid control tasks discussed in this paper.

I want to know if it is possible to deploy the method on real robots, just like RobotMDM[5] (I feel that this method is difficult to have this scalability). The paper does not discuss the practical challenges of deploying the proposed method on real robotic systems, such as dealing with sensor noise, model inaccuracies, and the sim-to-real gap. The assumption of direct online interaction with the environment may also pose a challenge for real-world deployment.

While the paper focuses on motion capture datasets, how would FB-CPR perform when trained on more diverse or noisy datasets, such as uncurated video footage? The paper does not address the robustness of the proposed method to variations in data quality and diversity. It is unclear how the method would perform when trained on datasets with significant noise, occlusions, or variations in viewpoint and lighting conditions, which are common in real-world video data.

### Questions
* It is unclear how the advantages and differences of this method compare to previous approaches, such as AMP[1] and ASE[2], as well as to recent work (like Omnigrasp[3], MaskedMimic[4]), when applied to the demonstration data settings discussed in this paper.
* I want to know if it is possible to deploy the method on real robots, just like RobotMDM[5] (I feel that this method is difficult to have this scalability).
* While the paper focuses on motion capture datasets, how would FB-CPR perform when trained on more diverse or noisy datasets, such as uncurated video footage?


[1]Peng, Xue Bin, et al. "Amp: Adversarial motion priors for stylized physics-based character control." ACM Transactions on Graphics (ToG) 40.4 (2021): 1-20.

[2]Peng, Xue Bin, et al. "Ase: Large-scale reusable adversarial skill embeddings for physically simulated characters." ACM Transactions On Graphics (TOG) 41.4 (2022): 1-17.

[3]Luo, Zhengyi, et al. "Grasping diverse objects with simulated humanoids." arXiv preprint arXiv:2407.11385 (2024).

[4]Tessler, Chen, et al. "MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting." arXiv preprint arXiv:2409.14393 (2024).

[5]SERIFI, AGON, and MARKUS GROSS. "Robot Motion Diffusion Model: Motion Generation for Robotic Characters." (2024).

### Soundness
3

### Presentation
2

### Contribution
3
