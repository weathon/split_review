# Flat Reward in Policy Parameter Space Implies Robust Reinforcement Learning

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8

## Abstract
Investigating flat minima on loss surfaces in parameter space is well-documented in the supervised learning context, highlighting its advantages for model generalization. However, limited attention has been paid to the reinforcement learning (RL) context, where the impact of flatter reward landscapes in policy parameter space remains largely unexplored. Beyond merely extrapolating from supervised learning, which suggests a link between flat reward landscapes and enhanced generalization, we aim to formally connect the flatness of the reward surface to the robustness of RL models. In policy models where a deep neural network determines actions, flatter reward landscapes in response to parameter perturbations lead to consistent rewards even when actions are perturbed. Moreover, robustness to actions further contributes to robustness against other variations, such as changes in state transition probabilities and reward functions. We extensively simulate various RL environments, confirming the consistent benefits of flatter reward landscapes in enhancing the robustness of RL under diverse conditions, including action selection, transition dynamics, and reward functions.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper investigates the relationship between flat reward maxima in policy parameter space and the robustness of reinforcement learning (RL) agents. It claims that flatter reward maxima lead to more robust policies, particularly against action perturbations. The paper presents a theoretical proposition linking flat reward to action robustness and supports this claim through empirical experiments in MuJoCo environments (e.g., Hopper-v3, Walker2d-v3, HalfCheetah-v3). The authors demonstrate that an RL algorithm enhanced with Sharpness-Aware Minimization (SAM), called SAM+PPO, consistently outperforms standard PPO and a recent robust RL baseline (RNAC) in various robustness tests, including action noise, transition probability changes, and reward function variations. The paper also provides visualizations and quantitative measurements of reward surfaces, further confirming the link between flatness and robustness.

### Strengths
- This paper provides a formal link between flat reward surfaces and robustness in policy space. Proposition 1 establishes a clear theoretical foundation for the paper's main claim.
- The authors comprehensively test SAM+PPO across multiple challenging environments and scenarios, including noisy actions and varying transition probabilities, to demonstrate robustness.
- The authors compare SAM+PPO with RNAC, PPO, and RARL, which shows both performance and computational efficiency, which strengthens their findings.
- The use of reward surface visualizations and flatness metrics strengthens the paper's argument by providing visual and quantitative evidence for the flatness achieved by SAM+PPO.

### Weaknesses
 - While SAM is shown to be effective, the paper lacks a discussion of its potential limitations, such as computational overhead or sensitivity to hyperparameter tuning.
- The justification for reward noise being added during training for reward function robustness evaluation could be clearer: The paper mentions this difference in methodology but could expand on why this is necessary for a valid evaluation.
- I don't know if the preliminary experiment is best placed in the introduction, it feels a bit out of place for me.
- typos 234 "objeective", 249 " funciton"

### Questions
- Do you have an intuition on why SAM doesn't perform better on Walker2d-v3 for high friction factor?
- Have you tested SAM+PPO on non-MuJoCo environments to assess robustness in discrete action spaces or varying reward structures?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a study on using sharpness-aware regularization to obtain robust reinforcement learning policies. Drawing a theoretical connection between flatness in the reward, action and parameter space to action-robust RL, the authors present both a theoretical justification and experiments to show that the proposed method achieves good robustness properties.

### Strengths
The authors propose a simple yet intuitive approach for robust RL. I was somewhat surprised that this combination has apparently not been tried in the literature, but a brief literature survey has not brought up any similar algorithms. I actually think the authors are somewhat underselling their contributions here! While SAM has been used to train PPO before, the authors appropriately cite prior work here, previous papers have not drawn any connections to robust RL at all and the authors should feel entitled to proudly claim this connection as their connection! They do not merely provide theoretical backing, as far as I can tell, they make a connection that was wholly absent in cited work.

The theoretical statements are mostly correct as far as I can tell. See questions below however.

### Weaknesses
The main problem with the paper as it stands are writing problems and baseline comparisons.

Especially the beginning of the paper, abstract and introduction, suffer from very frequent grammar mistakes which make the paper much harder to read. I strongly encourage the author to revise the paper wrt to the writing.

In definition 1, I'm unsure if $\epsilon$ is added to the policy, parameters or action? From the proof it seems this is a parameter perturbation, this should be stated directly. I think adding parentheses in the equation would already make this much clearer, as we have two nested subscripts here.
In addition, the state is sampled from the policy, which seems strange?

As the theoretical statement depends on the Jacobian of the policy network, which is not bounded anywhere, I'm slightly skeptical that the theoretical results are sufficient to practically guarantee robust RL. Does the SAM objective guarantee or incentivize a flat Jacobian?

Given the surprisingly (?) bad results of RNAC - it barely seems to outperform PPO - I think it would be appropriate to apply SAM+PPO in the same environments as used in the RNAC paper. As far as I can tell, the code is available, so this should be feasible within the rebuttal timeline? If not, I will not hold this against the authors. I think it is important to verify that used examples are not cherry-picked to make the presented algorithm look stronger. This is the higher priority comment in terms of baseline comparisons.

I would encourage the authors to present some additional baselines. I acknowledge that more baselines is a somewhat lazy comment. However, given that there are several different formulations of robust RL, I believe it would be helpful to pick a variety of environments and algorithms presented with different robust formulations for comparison to understand how well the algorithm does in comparison to others. This doesn't have to be many or complex environments, just a larger variety of formalisms. This is a soft concern and not a large barrier to acceptance for me.
Both safe-control-gym and Safety Gymnasium provide a variety of tasks and implemented baselines to speed up experimentation.

### Questions
Is there a specific advantage to using PPO with SAM, or could any PG or even AC algorithm be used? It might be that the clipping approximation to the trust region synergizes well with the SAM objective? I think this is an optional extension to the paper.

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
3

### Summary
This paper explores the impact of flat minima in reinforcement learning (RL), linking flatter reward surfaces to improved model robustness. The authors show that flatter rewards lead to more consistent actions despite parameter changes, enhancing robustness against variations in state transitions and reward functions. The authors show through extensive experiments to confirm that flatter rewards significantly bolster RL model performance across diverse scenarios.

-------------------
After the rebuttal: The authors have addressed some of my concerns. I raised the score.

### Strengths
- Provide a link of flat reward to action robustness. The authors show this through both theoretical results in section 4, and various experiment results. The motivation of having a robust objective is good. The theoretical result seems correct.

- Positive experiment results showing the benefit of optimizing for a flat reward maxima. The authors show this through different experiment settings: variation to physics properties of the underlying MDP, and visualization of the reward surface.

### Weaknesses
 - The performance of SAM + PPO is mixed in comparisons to the baselines, e.g. some visible ones at Fig 5.c, 4.b.

- Ablations are not provided to understand how such an objective can bring benefits in comparisons to similar approaches, e.g. RNAC or robust RL.

- The proof of proposition 1 is a bit not standard. The policy is sometimes referred as a distribution, but sometime used as a deterministic mapping. It needs revised.

### Questions
- Is the perturbation domain $\rho$ in Eq.8 known to the agent? Probably the optimization of the objective in Eq.8 needs elaboration, and with pseudo-code.

- Why in "Nominal"  SMA+PPO still has a higher reward, e.g. Table 1+2, Fig. 3,4. Similarly,  experiment in 5.2, why when action noise is small, i.e. even equal to 0, SAM+PPO still performs better than the others, because the objectives of PPO and SAM+PPO would converge to the same one? And in 5.3, SAM+PPO has a higher return, while with variation in Friction Coefficient shows mixed results. 

- Joint variation of friction and mass shows quite clear that SAM+PPO is performing better than baselines, except on Walker2d-v3 with a mixed result. Can the authors elaborate on why or provide ablation to explain the mixed performance of SAM+PPO?


- The proof of proposition 1 is a bit not standard. The policy is sometimes referred as a distribution, but sometime used as a deterministic mapping. It needs revised.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work proposes a new method to ensure robustness in RL based on variations in the loss landscape: "SAM": Sharpness-Aware Minimization. By posing the policy optimization as a min/max objective with respect to perturbations in the parameter space, the authors show robustness to changes in reward and dynamics. A theoretical result is given, linking parameter and reward robustness, and a diverse set of experiments on 3 MuJoCo environments is provided.

### Strengths
- This use of robustness in policy parameter space seems to be fairly new
- The experiments demonstrate a strong performance boost across a range of perturbations 
- The visualizations in Figure 6 offer an interesting insight into the optimizations produced by PPO vs SAM+PPO. The Hopper example is quite striking. Could you elaborate on the distinction and sharp dropoffs seen there?
- Theory provides a potential link between flatness in parameter space and action robustness
- Provided a solid comparison wrt computational overhead / sample complexity and wall time versus other algorithms
- Figure 5 is quite nice, I think it should be emphasized

Overall, the paper seems like a nice first step in the direction of understanding the relationship between robustness in reward, policy parameter, and dynamics spaces. The notion of "flat rewards" is an interesting one.

### Weaknesses
 **Writing:**

- Overall, I think the clarity of the paper can be enhanced with a re-write fixing grammar and overall structure:
- It would be helpful for example, to also include some visualizations of the definitions 1 & 2.
- Also, Proposition 1 and the following remarks are not very clear. As an example, for Prop1, if I understand correctly, the result would be better phrased as "if $\mathcal{E}$-flat, then $\Delta$-robust, with $\Delta \leq ...$ otherwise the current phrasing is a bit confusing.


**Discussion:**

- The discussion of the main idea, "SAM" is lacking:
- After it is introduced in Sec 3.3, the authors give a way to solve the optimization problem in Eq (3) by their steps (i)-(iv). However, (to me at least), it is not clear why this method is used. Is there prior work demonstrating the efficacy of this method? Are there experiments or maybe some minimal example illustrating the utility of this setup? E.g. why is $\epsilon$ chosen to be in the direction of the previously computed gradient, if theoretically it should represent an arbitrary direction in the ball. 
- At the very least, can the authors provide some visual demonstration as to what is happening here in the loss landscape? Getting a better intuition would help to understand the core method of the paper. 
- Remark 1.1 seems to be a restatement of Prop 1 unless I am missing something. Could you please explain?
- Remark 1.2 can be improved by using more technically accurate statements (i.e. what is meant by "when a reward function slightly changes")? What is meant by the "direct [correspondence] to the changes of loss function in the supervised learning case"? I think the latter is very unclear, and maybe even misleading.


**Experiments:**
- My only issue with the experiments (minor) is that you are missing RNAC in Table 2 (why?). Also why not compare against RARL? Missing explanation of the shaded regions in each figure caption.


### Questions
I'm really curious about "flat rewards" in general. Definitions 1 and 2 seem too strict at first glance (the equalities therein), so it is actually a bit surprising to me that they are even possible at all; however IIUC, Fig 6 does give evidence of this. I think that these definitions can be further elaborated on (do you have a toy example where it is easy to see in parameter or action space?) Realistically, what values of $\epsilon$ do you think are reasonable? Something like $10^{-11}$ or $10^{-2}$? (I might've missed it somewhere, sorry.) If these are novel definitions not previously given in the literature, that can be stated as a contribution of the paper. I think it can spark future work in both theory and experimental directions.

Here are some follow up questions/comments:

- In Sec 5, how long are those agents trained for? Equal number of env steps for each? How were hparams tuned for each algo?
- What is the agent's action scale for these environments (cf L337)? What do you do if the noise added is outside the action range?
- Do you have any ideas about the sharp dropoff in Fig 3b for SAM PPO? it looks interesting, but I'm not sure what to make of it... is there some "critical" mass ratio? I.e., if we zoom in, how sharp is that transition, and have you averaged over enough random seeds?
- you mention "flatter reward maxima" in L70. I think a formal definition or good visualization of this phenomenon early on would really improve the paper.
- How does this work relate at all to other trust region methods like TRPO? How about e.g. [1]

[1]: https://arxiv.org/abs/2103.06257

Typos/minor

- Fig 3 caption "nomial"
- some missing +/- signs in Table 1 (in parens)
- citations in sec 2 often have a missing leading space.
- can you improve the visual in Fig 1? I think it's important but not quite capturing the essence. Maybe just to remove axes and grid and zoom in a bit: is there indeed a channel for the agent? It's hard to see
- The introduction paragraphs have some grammatical issues. A cleanup/re-write here can help to crystallize the main message early on

With a rewrite to clean up the presentation, deeper explanation for SAM (i)-(iv), and perhaps a few more visualizations, this could be a really strong paper; but unfortunately I don't think it's quite there yet.

### Soundness
3

### Presentation
3

### Contribution
3
