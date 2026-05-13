# Policy Gradient without Boostrapping via Truncated Value Learning

- Decision: Reject
- Scores: 6, 5, 5, 3

## Abstract
Reinforcement learning algorithms have typically used discounting to reduce the variance of return estimates. However, this reward transformation causes the agent to optimize an objective other than what is specified by the designer. We present a novel deep policy gradient algorithm, \textit{Truncated Value Learning} (TVL), which can learn rewards \textit{discount free} while simultaneously learning value estimates for \textit{all} summable discount functions. Moreover, unlike many other algorithms, TVL learns values without bootstrapping. We hypothesize that bootstrap-free learning improves performance in high-noise environments due to reduced error propagation. We tested TVL empirically on the challenging high-noise \textit{Procgen} benchmark and found it outperformed the previous best algorithm, Phasic Policy Gradient. We also show that our method produces state-of-the-art performance on the challenging long-horizon Atari game \env{Skiing} while using less than 1\% of the training data of the previous best result.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose an algorithm for handling large horizons and undiscounted MDPs. They argue that discounting is for the purpose of reducing error propagation when bootstrapping. They claim that the proposed algorithm may work better in environments with high noise and high variance of returns.

### Strengths
The introduction is well-motivated and has a logical flow.

Proposed an algorithm that can learn discount-free rewards even for large horizons.

### Weaknesses
In the listed contributions what is the difference between points 1 vs 4 and 2 vs 3?
I think the authors should argue with the applications about the relevance of the study.

### Questions
Typo fig 3 caption, X-axis
Which step in the TVL algorithm is dampening the error propagation similar to discounting?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a novel deep policy gradient algorithm, Truncated Value Learning (TVL), that can learn rewards discount-free while simultaneously learning value estimates for all summable discount functions. The main contribution of TVL is scaling the fixed-horizon long-horizon tasks with three ingredients: geometrically spaced value heads, sample-based return estimator, and fixed-horizon update rule.  The algorithm is tested empirically on the challenging high-noise Procgen benchmark and the long-horizon Atari game Skiing, showing state-of-the-art performance.

### Strengths
1. Effectively motivated to extend the learning horizon in fixed-horizon tasks.
2. The algorithm is rigorously evaluated on challenging benchmarks, specifically, noisy tasks where TD methods falter, and it surpasses previous state-of-the-art algorithms.

### Weaknesses
1. The novelty is under the bar for ICLR where this paper involves almost heuristic designs. The core of the algorithm relies on a specific geometric spacing of value heads and a sample-based return estimator, which, while effective, lack a strong theoretical foundation or justification beyond empirical success. The design choices, such as the specific form of the geometric spacing and the fixed-horizon update rule, appear somewhat arbitrary without a clear explanation of why these particular choices are optimal or even necessary.
2. Long-horizon brings the higher sample inefficient for online algorithms. The training time is 3x higher than the PPO algorithm. This significant increase in training time raises concerns about the practical applicability of the algorithm, especially in scenarios where computational resources are limited. The paper does not adequately address this trade-off between performance and computational cost, nor does it explore potential optimization strategies to mitigate the increased training time.
3. This paper involves multiple hyperparameters, e.g., $k, c_{vh}$, without sufficient ablation study. The lack of a thorough ablation study for these hyperparameters makes it difficult to assess the robustness and generalizability of the proposed method. It is unclear how sensitive the algorithm's performance is to variations in these parameters and whether the reported results are specific to a narrow range of hyperparameter settings.

### Questions
It is hard for me to follow to distillation part. For example, what is $c_{vh}$, and why we should use distillation? What is actually doing in Eq. 14?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a deep PG method, called Truncated Value Learning (TVL), to learn rewards without discounting. In addition, this paper claimed bootstrap learning may degrade the performance in high-noise environments and introduced a bootstrap-free learning method. Some experimental results in  Procgen and Atari-5 seem to show an improved performance.

### Strengths
1. The paper is written concisely, clearly, and easily understandable.
2. The proposed method is relatively novel, and some experimental results show improved performance.

### Weaknesses
1. This paper lacks enough ablation experiments, making it difficult to see the role of each component clearly. For example, the author should have shown the benefits of TVL not using traditional discounting while learning rewards. Specifically, it is unclear how the performance changes with different truncation lengths in TVL, and whether the truncated value learning is actually contributing to the performance gain or if it is simply a result of other implementation details. A comparison with a standard discounted return approach, with and without the other proposed modifications, is essential to isolate the impact of the truncation mechanism.
2. In addition, TVL has yet to be significantly proposed compared with the baseline algorithm on the long-horizon task, so it is difficult to judge whether the TVL method is effective on the long-horizon task. In addition, the author may be able to test it on more long-horizon tasks. Increase persuasiveness, such as pitfall, etc. The choice of Skiing as a long-horizon task is questionable, as it primarily features deferred rewards rather than the sparse rewards that are characteristic of many challenging long-horizon environments. The paper needs to demonstrate the effectiveness of TVL in environments with sparse rewards and long time dependencies, such as Montezuma's Revenge or Pitfall, to make a stronger case for its applicability to long-horizon problems. The current results do not sufficiently demonstrate that TVL is a significant improvement over existing methods for long-horizon tasks.

### Questions
1. Can the authors add some ablation experiments to supplement the paper?
2. There are many other long-horizon tasks in Atari, such as pitfall. Skiing alone is not convincing enough (and the performance in skiing does not seem to be significantly improved). Can the author add some results of other tasks? This might increase the convince of the proposed method.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a method that learns the value function with truncated horizon. This estimator is further combined with the PPO algorithm and is empirically tested on several Atari tasks. The experiment results show the advantage of the proposed algorithm.

### Strengths
The paper studies an important problem. The arguments are supported with sufficient examples and experiments. And the paper is presented in sufficient details and illustrations.

### Weaknesses
1. The motivation need to be further addressed. The authors demonstrate the advantage of horizon truncation in section 3, showing that untruncated TD update can lead to divergence. However, one weakness of this demonstration is the authors set h_max to be 1000, which is the effective horizon of $\gamma=0.999$. With this hard constraint, further increasing $\gamma$ has very little effect on the convergence result because they are "cut off" back to $0.999$ due to the constraint (as one can see from the figure, the slope is much smaller when $\gamma$ exceeds 0.999). In this case, the comparison for $\gamma > 0.999$ is not fair. On the other hand, when one looks the part of $\gamma < 0.999$, both curves show good convergence results, which makes the authors' claim less convincing. 

The authors might strengthen their argument by adding the following results: 1. One would like to see what happens for a larger h_max value when testing the convergence result for a larger $\gamma$ value, for example, one can set h_max=10000 for $\gamma=0.9999$ so that no long term signals are killed. 2. Another concern is the introduction of h_max is exploiting the prior knowledge that there is no signal in the long term (because the reward is always 0 in this toy example.). If this is true, then setting an even smaller h_max values like 100 or 10 can lead to even better convergence result. The authors could also show the experiments for smaller h_max values to prove that this concern is wrong. 

2. While the algorithm learns the h-horizon values for several horizons, when combined the value function with PPO, one only finds the appearance of the value function for h_max (for example, equation 12). This is somehow disappointing. It could be possible that the value estimations for various horizons are hidden somewhere in this expression like the TD updater. But if that is the case, the authors should address it in the main context as this is crucial for showing why their formulation is useful. 

3. The use of notation is messy. In equation 3, while it's said to be n-step update, the corresponding notation is replaced by k in the equation. I never see a formal definition of NSTEP_h^n in the main article. The most similar notation is NSTEP_h^(k) in the appendix. The authors should clarify if they are pointing to the same thing, and why the bracket sometimes disappears, and why sometimes there is an additional $\gamma$ in the bracket but sometimes it also disappears. In the algorithm, the authors introduced another new notation NSTEP_x(s, h), I'm not sure if it has the same meaning of NSTEP_h^x(s). Overall, it could be much better if the authors could use consistent notations. 

4. Part of the experiments didn't show convincing results. For both General Performance and Long Horizon, the algorithm doesn't significantly outperforms the baseline.

### Questions
1. What is the justification for using linear interpolation to estimate the value function of an unknown horizon $h$? 

2. How did the authors choose the number of horizons K? If one uses a larger K, will one always expect a better performance so that the only constraint is computation resource? Or there is already some trade-off over the statistical performance so that increasing K can actually decrease the estimation accuracy / cumulative reward at some time point?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
