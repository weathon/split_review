# DreamFuser: Value-guided Diffusion Policy for Offline Reinforcement Learning

- Decision: Reject
- Scores: 3, 3, 6

## Abstract
Recent advances in reinforcement learning have underscored the potential of diffusion models, particularly in the context of policy learning. While earlier applications were predominantly focused on single-timestep settings, trajectory-based diffusion policy learning promises significant superiority, especially for low-level control tasks. In this context, we introduce DreamFuser, a trajectory-based value optimization approach that seamlessly blends the merits of diffusion-based trajectory learning and efficient Q function learning over state and noisy action. To address the computational challenges associated with action sampling of diffusion policy during the training phase, we design the DreamFuser based on the Generalized Noisy Action Markov Decision Process (GNMDP), which views the diffusion denoising process as part of the MDP transition. Empirical tests reveal DreamFuser's advantages over existing diffusion policy algorithms, notably in low-level control tasks. When benchmarked against the standard benchmark of offline reinforcement learning D4RL, DreamFuser matches or even outperforms contemporary methods. This work also elucidates the parallels between the optimization process of DreamFuser over GNMDP and Diffusion Policy over MDP, demonstrating its computational and memory advantages.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper develops a learning protocol that integrates reinforcement learning (RL) with diffusion models, jointly training the underlying diffusion with a Q-function. The results are compared against five baselines.

### Strengths
Strengths
* The concept of integrating diffusion models with RL is interesting.
* The paper compares the method against five baselines.
* The paper claims that the method outperforms baselines on most of the considered tasks.

### Weaknesses
Summary of weaknesses (for details, see below):
* It is not clear how the "inference" of the method works (i.e., having everything trained: how do we execute actions? is $Q$-value used? do we only sample from the diffusion policy? etc.). There is no pseudo-code provided.
* It is not clear what the components of the method are.
* The loss formulas seem not to reconcile with the formalism of GNMD introduced in the paper.
* The experimental section is lacking.

The method:
* Figure 1, the main visual help to understand what is happening, seems to be attached to Section 4.1. However, it is being explained in  Section 4.2, an unfortunate layout choice, which extends the time needed to understand the approach.
* Section 4.2 is confusing
	* It seems that the dynamics works like this:
		* for $k>0$, sampling an action $A_t^{k-1}\sim \pi(\cdot|\hat{s})$, with $\hat{s}=(O_t, A_t^k)$ transitions to $\hat{s}'=(O_t, A_t^{k-1})$.
			* This suggests that the correct formula for the "consistency" loss should be: $$\mathcal L_{consistency}=\left(\gamma_2\mathbb E_{A_t^{k-2}\sim \pi(\cdot|\hat{s}')} [Q_\phi(\hat{s}', A_{t}^{k-2})] - Q_\phi(\hat{s}, A_t^{k-1}) \right)^2.$$

		* for $k=0$, $\hat{s}=(O_t,A_t^0)$, the action is always $\epsilon\sim N(0,I)$, and the resulting the new state is $\hat{s}'=(O_{t+l}, \epsilon)$,
			* This suggests that the correct formula for the MSBE loss should be: 
		$$\mathcal L_{MSBE}=\left((\mathcal R_t + \gamma Q_\phi(\hat{s}', A_{t+l}^{K-1})) -Q_\phi(\hat{s}, \epsilon) \right)^2.$$
	* The last term in equation (9) is unclear.
	* $\epsilon_{t,k}$ in equation (10) is not defined.
	* TD3 is mentioned, but the losses do not reflect this (details are mentioned in passing in Appendix B.1, but no formula is provided).
	* There is no pseudo-code for the training protocol in the main paper (it can only be found in the Appendix).
* In the Introduction, it is written that "DreamFuser integrates a learned dynamic model". It is only briefly mentioned in Section 5, paragraph "effectiveness of the learned model". However, Appendices B.2-3 unexpectedly describe GRU, stating that the diffusion policy now inputs history states $O_t$, noisy sequence $A_t^k$, and predicted future states $O_t'^{k}$ (which is not defined). This seems like an important piece of information, and its omission from the main body of the paper creates confusion as to how the method works. Additionally, transformers make their appearance. What also adds to the confusion is the introduction of $K_{inference}=4$ in B.2. which seems to be used as $K$, but it is not (it is chosen "independently of chosen value for K").

Experiments:
* Results are computed for a low number of seeds (equal to 3, information which can only be found in the Appendix). Additionally, no confidence intervals for the reported numbers are reported, which makes it hard to infer the relative performance of the methods (however, for three seeds, CIs might be too noisy to be informative).
* In Section 5.2, it is mentioned that DreamFuser converges to optimal actions. Why?
* In Section 5.2, it is written that the "proposed trajectory learning optimization technique for Q values proves effective notably excelling in tasks labeled as 'umaze'". What is the reason for that? How is it connected with the diffusion process?
* Figures 2(a) and (c) show strange behavior in learning curves, which is not discussed. 
* The results in Figure 2(a-b) are only presented for length 1 or 7. What about other values?

Other:
* It would be interesting to investigate whether the method's success is related to specific features of the chosen environments (and if so, what features).
* In equation (15), there should be $\epsilon \sim N(0, I)$.

### Questions
See above.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes DreamFuser, an algorithm that synergistically combines diffusion models and Q-learning for offline reinforcement learning. It models action sequences using a conditional diffusion model and incorporates the diffusion process into the MDP as hidden transitions, enabling efficient Q-function optimization. Experiments on D4RL and robot control tasks demonstrate significant improvements over strong baselines.

### Strengths
1. The idea of incorporating the diffusion process into the MDP as hidden transitions is creative, and enables more efficient policy learning and optimization.
2. DreamFuser elegantly combines diffusion modeling and Q-learning in a mutually beneficial way. The sequence modeling handles multimodality while Q-learning enables optimization.
3. The empirical results are quite strong, with DreamFuser outperforming state-of-the-art methods on both D4RL and robotic manipulation tasks. The consistent gains are impressive.The ablation studies clearly demonstrate the value addition from Q-learning, sequence modeling, and dynamics modeling in DreamFuser

### Weaknesses
1. The paper does not sufficiently analyze the increased computational costs and inference times resulting from modeling longer action sequences. Using longer sequences increases training and memory requirements, as well as inference latency. A quantification of these costs compared to shorter sequence models would be useful to characterize the trade-offs.
2. The optimal sequence length likely varies across different tasks and environments. More ablation studies on a diverse set of tasks could help identify the best sequence lengths for different problem settings. This could make the method more adaptable and provide more concrete recommendations on sequence length selection.The sequence length is a difficult hyperparameter to tune. The paper could explore adaptive methods to automatically adjust sequence lengths during training to reduce the burden of manual tuning for each task.
3. The paper does not provide an in-depth analysis comparing DreamFuser to prior diffusion model methods like DD and Diffuser using similar length action sequences. Clarifying the key differences and improvements would strengthen the claims.
4. The paper lacks results comparing DreamFuser against Diffusion Policy on the D4RL benchmarks for mujoco and antmaze tasks. This is an essential control experiment to demonstrate the effectiveness of DreamFuser over diffusion modeling alone.
5. From my perspective, this work combines elements from prior work like Q-values guide diffusion policy from diffusion policy, and trajectory generation from diffuser. While the approach is technically sound, the fundamental conceptual advance appears incremental. The novelty may be limited and no insight for me without deeper analysis and comparison.

### Questions
Please see the weakness above and address my concerns.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents Dreamfuser, a diffusion model based offline RL algorithm. Dreamfuser works by jointly optimizing actions for multiple states in parallel, with the diffusion refinement steps integrated into the MDP as "hidden transitions" in the state-action space to make Q-learning tractable in parallel with behavioral cloning.

### Strengths
The method presented is algorithmically sound and supported by a good set of comparisons to multiple prior methods to validate its performance. The topic is important and the algorithm novel, to my knowledge.

While I found the writing a little jargon/notation dense at times, overall the paper does a good job of presenting the method.

### Weaknesses
While it's a bit of a dirty word, I can't help but feel that this paper is a bit Incremental.

To be clear, I'm of the opinion that that shouldn't be an obstacle to publication- I'm recommending marginal acceptance as I do think the method is novel and sound and the improvement on prior work seems credible, which should be the bar for research to be considered worth sharing.

My general criticism is that this paper doesn't do a lot to justify that the presented algorithm is radically better than prior ones. The motivation makes sense as an extension of previous work, and the experimental results substantiate that Dreamfuser is comparable or better in several benchmarks, but as someone not working in offline RL specifically it's not clear to me how this work has moved the field forward beyond taking that incremental step. Is there an extension or new ground that could be broken to build off of this work?

I've got a few specific questions and suggestions below, but my main concern is that the paper doesn't do a good job explaining its own significance. If there's something I'm missing here I am open to revising my score, for what it's worth.

-There's a number of grammatical errors scattered throughout the paper, particularly after section 1. I'd suggest another editing pass, though this doesn't significantly impede understanding the paper.

-How does the MDP formulation in Section 4.1 differ from a POMDP (with the action history as part of the observation)? Is there a reason it is not described as a particular subtype of POMDP? The hindsight framing M' seems to suggest that it can be treated as one.

-What is the downside to the GNMDP formulation here? It seems like it should make action/Q-value gradients much more noisy and slow learning due to the temporal extension/noisy credit assignment. Are there drawbacks to this approach?

-I understand the concept, but counting down from K to 0 in the forward direction of time for diffusion steps is confusing when present alongside typical "0 to T" timestep notation. I imagine this counting down notation is standard in the diffusion model literature, but from an RL perspective it would improve readability to have both incrementing in the same direction.

-How does multi-action prediction affect the Gym tasks, similar to Figure 2a and 2b? The results in those figures are compelling, but intuitively I'd expect the importance of temporally extended action planning to vary significantly depending on the task, and this ablation seems to be the main motivation for a major element of the algorithm as presented, as I don't see a clear motivation for predicting a whole trajectory at once in the introduction. Perhaps there's some intuition from previous work I'm unfamiliar with, but it's not obvious to me why joint prediction of actions would improve forward action prediction accuracy at test time (outside a fully model-based method with forward dynamics). Does it benefit supervised training stability in some way?

-In figure 2c, how does this overfitting issue without the dynamics model compare to other methods? I had gotten the sense that methods like CQL generally avoid/minimize overfitting (albeit perhaps at a cost in theoretical performance), am I mistaken and most offline RL methods still suffer overfitting late in training? 

-Where does the name "Dreamfuser" come from, out of curiosity?

### Questions
-There's a number of grammatical errors scattered throughout the paper, particularly after section 1. I'd suggest another editing pass, though this doesn't significantly impede understanding the paper.

-How does the MDP formulation in Section 4.1 differ from a POMDP (with the action history as part of the observation)? Is there a reason it is not described as a particular subtype of POMDP? The hindsight framing M' seems to suggest that it can be treated as one.

-What is the downside to the GNMDP formulation here? It seems like it should make action/Q-value gradients much more noisy and slow learning due to the temporal extension/noisy credit assignment. Are there drawbacks to this approach?

-I understand the concept, but counting down from K to 0 in the forward direction of time for diffusion steps is confusing when present alongside typical "0 to T" timestep notation. I imagine this counting down notation is standard in the diffusion model literature, but from an RL perspective it would improve readability to have both incrementing in the same direction.

-How does multi-action prediction affect the Gym tasks, similar to Figure 2a and 2b? The results in those figures are compelling, but intuitively I'd expect the importance of temporally extended action planning to vary significantly depending on the task, and this ablation seems to be the main motivation for a major element of the algorithm as presented, as I don't see a clear motivation for predicting a whole trajectory at once in the introduction. Perhaps there's some intuition from previous work I'm unfamiliar with, but it's not obvious to me why joint prediction of actions would improve forward action prediction accuracy at test time (outside a fully model-based method with forward dynamics). Does it benefit supervised training stability in some way?

-In figure 2c, how does this overfitting issue without the dynamics model compare to other methods? I had gotten the sense that methods like CQL generally avoid/minimize overfitting (albeit perhaps at a cost in theoretical performance), am I mistaken and most offline RL methods still suffer overfitting late in training? 

-Where does the name "Dreamfuser" come from, out of curiosity? I understand the [dif]fuser part, but what about "dream?"

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
