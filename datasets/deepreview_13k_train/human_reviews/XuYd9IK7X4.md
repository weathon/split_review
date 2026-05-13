# COMAL: A Convergent Meta-Algorithm for Aligning LLMs with General Preferences

- Decision: Reject
- Scores: 6, 3, 3

## Abstract
Many alignment methods, including reinforcement learning from human feedback (RLHF), rely on the Bradley-Terry reward assumption, which is insufficient to capture the full range of general human preferences. To achieve robust alignment with general preferences, we model the alignment problem as a two-player zero-sum game, where the Nash equilibrium policy guarantees a 50\% win rate against any competing policy. However, previous algorithms for finding the Nash policy either diverge or converge to a Nash policy in a modified game, even in a simple synthetic setting, thereby failing to maintain the 50\% win rate guarantee against all other policies. We propose a meta-algorithm, \textbf{Co}nvergent \textbf{M}eta \textbf{Al}ignment Algorithm (\LPO), for language model alignment with general preferences, inspired by convergent algorithms in game theory. Theoretically, we prove that our meta-algorithm converges to an exact Nash policy in the last iterate. Additionally, our meta-algorithm is simple and can be integrated with many existing methods designed for RLHF and preference optimization with minimal changes. Experimental results demonstrate the effectiveness of the proposed framework when combined with existing preference policy optimization methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose to generalize the intrinsic assumptions behind the Bradley-Terry preference model to make the alignment objective more robust to general preference. They propose to formulate the robust alignment problem as a Nash equilibrium solving problem for a two-player zero-sum game. Strong last-iterate convergence results are established. In practice, authors suggest that such an objective can be combined with many existing alignment algorithms.

### Strengths
The robust alignment objective, when reduced to prox operator, builds connection with various existing alignment algorithms. The benefit of modifying those algorithms to the proposed COMAL is that it enjoys theoretical last-iterative guarantee while the original algorithms do not. On common alignment benchmark, COMAL shows promising results.

### Weaknesses
The weakness mainly lies in the experiment section. According to the formulation of COMAL objective, an equilibrium is found mean the resulting policy wins against any other policy. The presented experiment results testify this. However, my concern is that such an objective may result in heavier alignment tax, which is commonly observed from other alignment algorithm literature.

- To make the meta-algorithm more appealing to real applications, I suggest the authors to also include the evaluation results on academic benchmarks such as logical reasoning, maths, and coding.

### Questions
- How is the regularization parameter searched?

- How sensitive is the result to any of the hyperparameters? Did you find any recommended hyperparameter defaults that work well across different base models and training datasets?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes COMAL, which is designed to address the limitations of existing alignment methods for Large Language Models (LLMs), such as Reinforcement Learning from Human Feedback (RLHF). While methods like RLHF assume human preferences can be modeled with the Bradley-Terry (BT) approach, the authors argue that this simplification does not capture the full complexity of general human preferences. To overcome this, the authors frame the alignment as a two-player zero-sum game, with the goal of finding a Nash equilibrium policy that achieves robust alignment.

### Strengths
- The paper is written very well and easy to follow.

### Weaknesses
 - For motivation, the authors have argued that transitivity may not hold in practice, while in theory, it makes sense. However, it would be nice to provide some evidence of such behavior in the real-world preference datasets available in practice. 

- Further, to deal with this issue, a general preference optimization framework is utilized, as proposed in existing literature, but this has some issues. While collecting the preferences offline from humans makes sense, it is extremely hard to realize the assumption of having access to preference oracle. Are there any real-world examples of such oracles? For the experiments in this work, an LLM is used for preferences, which are AI-generated only then. Does it mean the framework of general preferences is only realistic with AI feedback not human? 

- The contributions are incremental because the authors have just utilized the prox operator, which is well-defined and developed in the optimization theory. Are there any additional challenges in applying that to the alignment context? 

- Why iterative averaging is cumbersome: we can easily maintain a running average of the model; this way, we don't need to store all the LLMs generated during the training. 

- Why does the alignment objective in (3) make sense because there is no KL regularized term in the objective? The authors have mentioned that the objective without KL can no longer achieve robust alignment. We note that straying closer to the based model via KL is one of the most important properties of any alignment method. It does not makes sense to solve a problem without it. 

- The proposed algorithm again solves a regularized problem only in the algorithm; it is confusing and hard to follow what is the exact approach. I see the authors have proposed to change the reference model to new pi^{t+1}, but this is weird because the final optimal model can be too far from the based model SFT, which is not required at all. Note that the alignment problem is just not only to maximize the preference provided by the preference oracle, but it is also important to stay closer to the base SFT model. 

- How win rate is calculated? Is it via GPT-4 ? 

- Also, the win rate plot without showing KL divergence to the SFT model is an incomplete description of the alignment performance of the approach. See the following alignment papers for that: 

 Mudgal S, Lee J, Ganapathy H, Li Y, Wang T, Huang Y, Chen Z, Cheng HT, Collins M, Strohman T, Chen J. Controlled decoding from language models. arXiv preprint arXiv:2310.17022. 2023 Oct 25.

Chakraborty S, Ghosal SS, Yin M, Manocha D, Wang M, Bedi AS, Huang F. Transfer Q Star: Principled Decoding for LLM Alignment. arXiv preprint arXiv:2405.20495. 2024 May 30.

### Questions
Please see the weakness.

### Soundness
2

### Presentation
2

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
This paper proposes a new algorithm, Convergent Meta Alignment Algorithm (COMAL), aimed at aligning language models with general preferences. The authors frame the alignment promblem as a two-player zero-sum game and demonstrate that COMAL can converge to a "exact" Nash equilibrium strategy using prox operaters, ensuring a minimum 50% win rate under any competing strategy, which they refer to as "robust alignment". The paper provides theoretical guarantees for the algorithm’s convergence and demonstrates its advantages over existing methods through synthetic and real-world LLM fine-tuning experiments.

### Strengths
The main strengths of this paper are: 

1. introduces a new concept called robust alignment and provides a theoretical gurantee that COMAL can achieve robust alignment, whereas existing methods cannot.

2. COMAL can be easily integrated into existing algorithms, such as INPO, to achieve robust alignment.

### Weaknesses
 1. The paper introduces a novel concept called "robust alignment". However, the motivation behind this concept is unclear and lacks a rigorous mathematical definition. The authors state that robust alignment aims to ensure a minimum 50% win rate under any competing strategy, yet the connection between this concept and alignment is not well-established. Furthermore, it is not evident how the "robust" aspect is manifested in this context. The significance of achieving robust alignment in the broader context of alignment research remains ambiguous. From my perspective, this concept appears to be more of a repackaging of existing game theory results [1] rather than a substantive contribution. 

 2. The main idea of this paper stems from [1] and [2], which established the result of last-iterate convergence to the exact Nash equilibrium in monotone games. However, this paper lacks proper citation of these two works. Even in the section on last-iterate convergence in the related work, [1] is not cited, and no comparison or discussion is provided. This oversight fails to acknowledge the foundational contributions of these prior works.

 3. The authors’ emphasis on the prox operator as the primary mechanism for achieving last-iterate convergence is confusing and misleading. It appears that the authors may not fully understand the theoretical foundations of the results in [1] and [2]. In fact, last-iterate convergence is achieved through the introduction of an additional convex regularizer in the payoff, rather than by the prox operator itself. While Mirror Descent (MD) is a proximal algorithm, MD alone does not ensure last-iterate convergence.  This means than COMAL actually does not apply to Iterative DPO, Iterative IPO, SPPO.  

 4. This paper builds on the perspective introduced by SPIN [3], which views DPO as the first iteration of MD. However, according to [1], for last-iterate convergence to the exact NE, it is necessary to first converge to the stationary point of the regularized game. Thus, as highlighted in [1], it is crucial to run the iterations for a sufficiently large number of iterations before updating the slingshot strategy. However, COMAL replaces the reference strategy after just a single iteration, which I believe is insufficient for convergence to the NE of the regularized game. Even from a practical standpoint, this falls significantly short. Given that this is the only modification COMAL makes to existing algorithms, I consider it a significant flaw in the framework.

 5. The experiments in this paper are extremely limited. The first experiment is overly simplistic and does not address real-world issues. The authors merely tested MD on a simple matrix game, but the results are already well-known and are far different from alignment scenarios, providing little insight into how COMAL addresses alignment challenges. The second experiment has two major issues: first, the model used, Qwen2-1.5B, is too small to be meaningful—at least an 7B parameter model should have been used to demonstrate the effectiveness. Second, while the authors used the AlpacaEval dataset, the evaluation relied on Llama-3-OffsetBias-8B, which fails to convincingly show that COMAL can meaningfully improve LLM performance. To truly demonstrate COMAL’s effectiveness, results showing consistent improvements across iterations are necessary ( since the authors claims last-iterate convergence).  Besides, the model's performance should be evaluated in at least two widely used benchmarks to demonstrate its effectiveness. Without such evidence, the results presented are insufficient to support the claims.

### Questions
How is COMAL’s performance on the standard AlpacaEval benchmark? Since the responses have already been generated in the second part of the experiment, it should only require following the standard AlpacaEval pipeline and using GPT-4 for evaluation to assess the performance.

### Soundness
2

### Presentation
2

### Contribution
1
