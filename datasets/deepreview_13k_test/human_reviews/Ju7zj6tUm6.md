# How vulnerable is my learned policy? Adversarial attacks on modern behavioral cloning policies

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Learning from Demonstration (LfD) algorithms have shown promising results in robotic manipulation tasks, but their vulnerability to adversarial attacks remains underexplored. This paper presents a comprehensive study of adversarial attacks on both classic and recently proposed algorithms, including Behavior Cloning (BC), LSTM-GMM, Implicit Behavior Cloning (IBC), Diffusion Policy (DP), and VQ-Behavior Transformer (VQ-BET). We study the vulnerability of these methods to untargeted, targeted and universal adversarial perturbations. While explicit policies, such as BC, LSTM-GMM and VQ-BET can be attacked in the same manner as standard computer vision models, we find that attacks for implicit and denoising policy models are nuanced and require developing novel attack methods.
Our experiments on several simulated robotic manipulation tasks reveal that most of the current methods are highly vulnerable to adversarial perturbations. We also investigate the transferability of attacks across algorithms, architectures, and tasks and provide insights into the generalizability of adversarial perturbations in LfD. We find that the success rate of the transfer attacks is highly dependent on the task, raising necessity for more fine-grained metrics that capture both the task difficulties and baseline performance of the algorithms. In summary, our findings highlight the vulnerabilities of modern BC algorithms, paving way for future work in addressing such limitations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper analyses the vulnerability of imitation learning policies to adversarial attacks in the visual input space. The paper also introduces a novel adversarial attack for diffusion-based policies, as it finds that these are generally harder to attack with sota attacks.
The paper evaluates on the Robomimic environments and finds that attacks dont generalise even when similar vision backbones are used, and that diffusion policies are generally more robust.

### Strengths
- relevant topic and well grounded selection of attacks and imitation learning algorithm
- solid evaluation in the given environment
- novel attack for hardest-to-attack diffusion policies

### Weaknesses
- motivation for diffusion policies attack is unclear: when is the setting of having access to the denoising process of the policy realistic?
- the empirical evaluation is limited to just one environment (Robomicic). To draw conclusions, at least 1-2 additional environments should be considered.
- A contrasting and comparing to prior works is largely missing
- e.g. the finding that denoising results in high adversarial robustness has been made before (see "(Certified!!) Adversarial Robustness for Free!")

### Questions
- Could the authors specify the threat model more clearly and motivate the setting for having access to diffusion steps

### Soundness
2

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
4

### Summary
This paper investigates the vulnerability of modern behavior cloning policies against popular adversarial attack methods. The behavior cloning methods includes original BC, LSTM-GMM, Implicit BC, Diffusion Policy and VQ behavior transformer. Adversarial attack methods includes projected gradient descent (PGD) and universal adversarial perturbation (UAP). Authors adapted these attack methods for some of the BC methods. The investigation is conducted on four manipulation tasks: Lift, Can, Square, and Push-T. The work explored a few interesting questions in addition: is perturbation learned transferable to policies learned using different BC methods? What is the impact of feature extraction backbone on adversarial attack and is the perturbation transferrable across different backbones. How does the action prediction horizon of diffusion policy affect its vulnerability?

### Strengths
1. The work provide some insights on adversarial robustness of general BC methods (DP is much more robust than other methods)
2. The work provide adaptation of classic adversarial attack methods to newer BC methods like DP, IBC, and demonstrated attack success using the adapted methods.
3. The work conducted some transferrable analysis on perturbation learned, across BC methods or across visual backbones.

### Weaknesses
1. The writing needs improvement in general. (see questions)
2. Some arguments are not well explained or supported by the result provided. (see questions)

### Questions
1. line 221: the first "maximize" should be "minimize"? 

2. line 221-223: this explanation is confusing to me, why probability of selecting the targeted action low would leads to no clear loss function?

3. line 222: what does clean mean here?

4. line 229: do you mean decrease? (same for the later "increase" used)

5. Algorithm 1: the initialization of S seems redundant?

6. line 342: Q2 is not answered.

7. line 352- 356: please consider provide concise task description if possible. (even not in main paper)

8. line 363: again, this will be more clear if some concise task/benchmark description is provided somewhere.

9. line 374: what does the perturbed observation looks like, could you provide a few examples?

10. Figure 2: why report task success rate rather than attack success rate? Also, I think normal success rate refers to task success rate? 

11. line 411-412: could you provide some task complexity related information? How is complexity measured?

12. line 426-427: can you explain this in more detail? A lot of factors should be considered here, for example, for more complex tasks, their task success rate are likely lower, so you might want to use some relative attack success rate to account for this.

13. line 426-427: Table 1 is success rate?, Table 2 is Mean IoU? how do you compare this two and reach the observation that "we noticed an increased propensity for adversarial perturbations to transfer between algorithms"?

14. Table 1: more explanation on what the columns and rows are? are attacks obtained in column methods and applied on row methods? also, what is "random", this is not explained in the paper I think?

15: line 460: "we observed high transferability for some algorithms (e.g., Diffusion Policy-C and VQ-BET)," are you referring to LSTM-GMM?

16: line 752- 754: The hyperparameter setting is not clear to me. First, please check the sentence. Second, what is perturbation if epsilon is set to 0.625 (which is pretty big compared to usual adversarial attack work.)

### Soundness
2

### Presentation
1

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
The paper studies the vulnerability of commonly used behavioral cloning algorithms. It considers well-known PGD and UVA attacks developed for supervised learning and directly applies them to compromise Behavior Cloning (BC), LSTM-GMM, and VQ-Behavior Transformer (VQ-BET) algorithms. It also shows that the PGD attack can be adapted to compromise Implicit Behavior Cloning (IBC) and Diffusion Policy (DP).

### Strengths
The paper highlights that commonly used behavioral cloning algorithms are vulnerable to PGD attacks.

### Weaknesses
The threat model is undefined. Are we considering data poisoning attacks? What can the attacker modify, states, actions, or both? What is the attacker's goal? What are the constraints to the attacker? None of them are defined in the paper. From 3.2.1, it seems that the paper considers both targeted and untargeted attacks. But the accurate definitions are missing, and it is unclear what tilde{p}_theta is. 

While undefined in the paper, a reasonable attack objective is to induce the agent to learn a bad policy. In this case, the attacker should modify multiple data points collectively. However, the simple attacks considered in the paper, such as PGD and UAP, were developed for the one-shot supervised learning setting and are ineffective for the sequential setting. The new attacks for IBC and Diffusion Policy are straightforward adaptions of PGD and also myopic.  

The reason why the simple myopic attacks can still work, as shown in the paper, is because the paper completely ignores defenses. However, there are well-known defenses for supervised learning, such as adversarial training and randomized smoothing, that can be easily adapted to the sequential setting when attacks are myopic, as considered in the paper. Simply showing that unprotected behavioral cloning algorithms are vulnerable to PGD attacks is not very interesting.

### Questions
Please see the discussion on weaknesses above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a thorough study about the adversarial vulnerability of several representative imitation learning methods (e.g., Vanilla BC, LSTM-GMM, IBC, Diffusion Policy and VQ-BeT) under two white-box attacks (PGD and UAP). The evaluation also covers the transferbility of perturbations across different policies and architectures.

### Strengths
1. The transferbility of perturbation between policies and architectures is also investigated.
2. The paper is well organized and easy to follow.

### Weaknesses
1. I concur with the authors that naive success rates may not accurately reflect the impact of adversarial attacks on robotic policies. It is essential to develop additional metrics, particularly those addressing safety concerns associated with real-robot deployments.
2. The current version seems that we have to develop tailored attacks given specific task, with privilege knowledge about the model parameters (PGD) and training samples (UAP). Thus the practical implications are limited for real-world deployments.

**[Minor:]**
1. Subscripts are not used correctly in line 752-753

### Questions
1. It is noted that the perturbations are applied uniformly throughout the trajectory during inference concerning UAP attack. Then what about PGD? Are perturbations computed for every single step during inference with updated observations?
2. How to determine the 'target action' when performing targetted attack? Does it also need to be updated during the inference process?
3. What is the precise number of iterations or steps utilized in the PGD attack? It is my belief that an extensive optimization process may diminish the practicality of the attack, as it could become less 'stealthy' for robots engaged in real-time operations.
4. As indicated in Tables 5 and 6, the IBC policy appears to be more vulnerable in the <Square> and <Can> tasks (than <Lift> and <Push-T>), while the LSTM-GMM demonstrates exceptional robustness in the <Can> task. Do these results imply that it is challenging to draw definitive conclusions regarding the relative robustness of the different policies (models), given that their performance varies across tasks?  Could the authors discuss potential factors that might contribute to the varying performance?
5. Have the authors studied about multi-task learning setting? Do you expect perturbations could be transferred across tasks?

### Soundness
2

### Presentation
3

### Contribution
2
