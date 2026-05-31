## Human Reviewer 1

### Summary
This paper proposes Ano, a first-order adaptive optimizer designed for robustness in noisy and non-stationary optimization settings, particularly relevant to reinforcement learning problems. The algorithm synthesizes ideas from both traditional adaptive methods like Adam and sign-based optimizers like SignSGD.
The key design choice decouples update direction from magnitude. The momentum term's sign provides directional information—leveraging its stability under noise—while the instantaneous gradient magnitude determines the step size, which responds better to non-stationary conditions. This approach contrasts with Adam's entangled treatment of both signals and represents a complementary design to Grams, which uses gradient sign for direction and momentum magnitude for scaling.

The paper establishes theoretical convergence guarantees under standard assumptions (smoothness, unbiased gradients, bounded variance), achieving a convergence rate of $$\tilde{O}(K^{-1/4})$$, consistent with other sign-based optimizers. The theoretical analysis employs a sign-mismatch probability bound to track how often momentum and gradient directions disagree, which decays as the algorithm progresses.

Empirically, the authors validate Ano across three domains. In controlled noise robustness experiments on CIFAR-10 with injected Gaussian noise, Ano consistently outperforms adaptive and sign-based baselines across all noise levels ($$\sigma \in {0, 0.01, 0.05, 0.10, 0.20}$$). On standard supervised learning tasks, Ano achieves competitive or superior results—outperforming comparisons on CIFAR-100 and excelling on high-variance GLUE tasks (MRPC, CoLA, RTE). In deep reinforcement learning, evaluated via Soft Actor-Critic on MuJoCo environments and PPO on Atari, Ano achieves the best or near-best performance across 3 of the 5 benchmarks, for both environments.

An ablation study isolates each component's contribution across four representative benchmarks (deep RL, computer vision, and NLP tasks). Results demonstrate that the momentum sign provides critical benefits in non-stationary RL settings, while both gradient normalization and gradient magnitude scaling are important—removing either substantially degrades performance.

### Strengths
The algorithm is well motivated as a principled response to limitations in existing approaches. The complementary relationship to Grams—where Ano swaps the roles of momentum and gradient information for direction versus magnitude—provides clear intuition: momentum sign captures stable directional signals robust to noise, while instantaneous gradient magnitude enables responsive adaptation to non-stationarity. 
The convergence analysis is technically sound, establishing an Õ(K^{-1/4}) rate. The proof structure adapts well-established techniques from sign-based optimizer analysis while extending to this new decoupling scheme under relatively mild assumptions. Very nice proof overall!

The reinforcement learning experiments are well designed and appropriately scoped. The authors recognize RL as the natural testbed for their method given the high variance and non-stationary nature of these problems, and they evaluate across both continuous (MuJoCo with SAC) and discrete (Atari with PPO) action spaces, strengthening claims about generality.

Anolog is a practical contribution that removes the $\beta_1$ hyperparameter through a logarithmic schedule. The ablation results show this variant maintains competitive performance—generally within or near the confidence intervals of the base algorithm—making it a valuable option when tuning budget is limited.

### Weaknesses
The paper lacks thorough comparative analysis explaining why Ano outperforms Grams despite their symmetric designs. Since both methods decouple direction and magnitude but swap which component comes from momentum versus gradients, this core difference deserves deeper investigation. Section 5.2 on noise robustness would be the natural venue for this analysis. The anomalous behavior in Table 1—where Grams improves from σ=0 to σ=0.01 before degrading at higher noise levels warrants explanation. The noise robustness section itself feels underdeveloped; given that noisy gradient adaptation is central to Ano's motivation, additional experiments demonstrating robustness in synthetic noisy settings would substantially strengthen the claims.

On the experimental side, Ano and Anolog often achieve leading performance but frequently exhibit higher variance than competitors across Tables 2, 3, 4, and 5. This higher variance partly offsets the improvements in point estimates, and confidence intervals often overlap with strong baselines. In the NLP task, Grams maintains competitive performance on GLUE despite its opposite design choice, which raises questions about whether the direction-magnitude assignment is truly the critical factor or whether other aspects of the algorithm matter more.

The RL experiments, while well motivated, suffer from a methodological limitation. Using only 100k-step HalfCheetah proxy runs for hyperparameter tuning biases the grid search toward larger learning rates, which may favor more aggressive optimizers like Ano while disadvantageing methods that stabilize with conservative settings. Since RL is where Ano's advantages are most compelling, extending these experiments to longer horizons with tuning conducted on representative scales would better justify the claimed benefits and limit concerns about unfair comparison.

### Questions
A technical issue in Table 3: the default configuration results appear systematically higher than tuned results in the top half of the table, which seems counterintuitive and may indicate a data entry or labeling error.

### Soundness
4

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes a new random optimizer named Ano, which improves training stability in noisy and non-stationary environments by decoupling the direction and magnitude of updates. It also provides a theoretical analysis of its convergence. Experiments on three tasks, CV, NLP, and RL, show that Ano either achieves improvements or remains competitive with baseline optimizers in noisy environments. However, Ano lacks detailed parameter analysis and validation on larger networks and more complex tasks.

### Strengths
1. Clear Motivation: The approach of decoupling optimization directions and magnitudes is interesting, and convergence analysis under certain assumptions provides theoretical guarantees.
2. Clear Writing: The paper is well-written and easy to follow.

### Weaknesses
1. Limited Experiment Scale: The experiments mainly focus on small-scale networks. The effectiveness of Ano on larger networks and more complex tasks is unknown. E.g., This paper should amplify the experiments on ImageNet for CV tasks, GPT-2 serious models on NLPs. 
2. Limited Practical Gains: In stable environments and with longer training times, Adam sometimes outperforms Ano. In more unstable RL settings, such as in the MuJoCo environment, the convergence curve of Ano is sometimes comparable to, or even worse than baseline.
3. Other: See questions below.

### Questions
1. Sensitivity to Hyperparameters: How sensitive is Ano to hyperparameters, such as batch_size and buffer_size in RL? Can it maintain robustness?
2. Combination with Regularization Methods: Can Ano be combined with regularization methods like Batch Normalization or Layer Normalization to provide additional gains?
3. Validation in More Non-Stationary Environments: In non-stationary RL tasks, when using actor-critic algorithms with different learning rates for the actor and critic, can Ano adapt? In more complex MARL tasks, where the environment becomes more non-stationary due to other agents' training, can Ano provide greater advantages?
4. Training Stability: Ano updates using $|g_k|$. Could this make training more unstable, especially when gradients are noisy or subject to common problems like gradient explosion or vanishing gradients? Does this makes training more difficult?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
3

---

## Human Reviewer 3

### Summary
This manuscript challenges gradient descent optimization techniques. Decoupling magnitude and direction for momentum and gradient, the authors propose Ano, which enables robust optimization for noisy landscapes. Experiments on CIFAR, GLUE, and reinforcement learning demonstrate these improvements.

### Strengths
- Indeed, training a large model sometimes exhibits instability in training, which requires a rerun and wastes time and effort. The study on robustness to noise is expected to contribute to this direction.
- Theoretical analysis, especially for the convergence ratio of the Ano, is provided with proof. I think the proof itself is solid enough.
- Source code is available, which eases deployment of Ano in practice.

### Weaknesses
- The results were reported with final performance, such as test accuracy. It would be nice to quantify noise robustness analysis in Section 5.2 with proper indices. Also, I encourage the authors to add more qualitative results on noise robustness; the current analysis with final test accuracy looks not convincing.
- How can we expect or say that the loss landscape for the target task would be noisy and we should use a robust optimizer for the noisy landscape? Is it possible to quantify noisiness in a landscape, such as in a reinforcement learning setting? The authors inject noise into the gradient for training, but I think it is still an artificial setup and far from a practical scenario. Furthermore, the failure of existing methods such as Adam should be clearly demonstrated, not by final accuracy.
- Experimental results are not solid enough. CIFAR-100 with ResNet-34, with 70% accuracy, is a weak baseline; I encourage performing ViT training with ImageNet. Similarly, GLUE with BERT is a standard but weak baseline for now.
- Specifically, the convergence rate of O(k^{-1/4}) for the proposed method is slower than O(k^{-1/2}) of Adam, despite the gain in noise robustness. This limitation should be verified in large-scale experiments such as ImageNet or LLM, targeting long iterations for training.
- Please check the following mathematics.
    - At Line 107, the authors use $v_k$ in the denominator, whereas Eq. 2 at Appendix C applies $v_{k-1}$ in the denominator, which is inconsistent.
    - \lambda_k in Algorithm 1 should be explicitly specified.
- Writing should be improved.
    - “Lanscapes” → “Landscapes” in OpenReview title.
    - “G^2” → “\tilde G^2” at Line 775.
    - “Equation equation 5” → “Equation 5” at Line 1060.
    - Ensure consistency for the choice of “optimiser” or “optimizer” as well as “optimisation” or “optimization”
    - “non-stationnary” → “non-stationary”
    - “environments. which” → “environments, which”
    - “litterature” → “literature”
    - Line 423-426: duplicate.
- For the source code, the authors apply v_hat correction for ano.py, whereas others such as anolog.py, anosqrt.py, and anoall.py do not apply v_hat correction. This practice requires explanation.

### Questions
Please see the weaknesses above. My score is based on the assumption that all typos are corrected in the revised manuscript.

### Soundness
2

### Presentation
2

### Contribution
3

### Rating
4

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper presents a new variant on adam/sign sgd updates that rescales the sign sgd update via a variance-like estimator.

### Strengths
The idea is new to me, and the attempt to decouple the direction and magnitude in this way seems interesting.

There is a convergence guarantee for finding critical points.

### Weaknesses
The theory is conducted in the standard smooth optimization analysis. This framework is known to very poorly describe practical neural network optimization - even convex theory has better agreement.

Moreover, the theorem is actually much worse than would achieved by standard SGD. The statement that sign-based methods fundamentally cannot achieve this rate is highly suspicious. It is well-known that normalized gradient descent (even in many different norms) achieves the same convergence rate as SGD when combined with momentum (see e.g. https://arxiv.org/abs/2002.03305, https://arxiv.org/pdf/2502.02900). sign-sgd is simply normalized SGD in the Linf norm, it should converge as well.

The authors claim many benefits of the algorithm in terms of difficult noise distributions in the gradients. It would be better if the theory actually illustrated these points.

The experiments look very detailed, but in almost all cases it seems like the final performance of Ano is within the error bars of the baseline.

### Questions
Please address the weaknesses above. Happy to reconsider my analysis.

### Soundness
4

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 5

### Summary
The paper introduces Ano, a first-order optimizer designed for noisy or non-stationary training. Its core idea is to decouple update direction and magnitude: the direction follows the momentum sign while the step size scales with the instantaneous gradient magnitude and a Yogi-style second-moment term; weight decay follows AdamW. The paper also proposes Anolog, which removes tuning of $\beta_1$ by growing the momentum window via a logarithmic schedule $\beta_{1,k}=1-1/\log(k+2)$. Theoretically, under standard smoothness/unbiased-noise assumptions and a decaying stepsize $\eta_k=\Theta(k^{-3/4})$ with $\beta_{1,k}=1-1/\sqrt{k}$, Ano achieves a non-convex convergence rate $\min_{k<K}\mathbb{E}\|\nabla f(x_k)\|^2=\tilde{O}(K^{-1/4})$. Empirically, Ano is competitive on CIFAR-100/GLUE and shows clear gains and faster learning on MuJoCo and Atari-5 benchmarks; it is also more robust under synthetic gradient noise on CIFAR-10.

### Strengths
The paper’s central idea, explicitly decoupling update direction and magnitude, is simple and well-motivated. In Algorithm 1 and Sec. 3, the direction is taken from the sign of the momentum, while the magnitude scales with the instantaneous gradient and a Yogi-style second-moment term. This design clearly differentiates Ano from Adam/Lion/Grams and aligns with the intuition that signs can be stable even when magnitudes are noisy. The companion variant, Anolog, further reduces tuning by growing the momentum window with a principled logarithmic schedule (Sec. 4), which is a practical touch that lowers the optimizer’s cognitive load. 

On the theory side (Sec. 5 and App. C), the analysis leverages a sign-mismatch bound and smoothness-based descent to deliver a non-convex convergence rate, with assumptions and constants made explicit. 

Empirically, the evidence is broad and convincing: classification on CIFAR-100 and GLUE shows Ano is competitive with strong baselines; in RL/non-stationary regimes (MuJoCo/SAC and Atari-5/PPO), Ano consistently learns faster and often to higher returns, with plots and tables that include multiple seeds and confidence intervals. 

The paper is generally clear and easy to follow; the motivation for the direction–magnitude split is intuitive, and the update is straightforward to implement from the provided pseudocode.

To sum up:
1. The paper has adequate mathematical analysis with clear assumptions, statements and proofs.
2. The work includes experimental work that compares the proposed method with other works.
3. The writing is generally clear with nice flow.

### Weaknesses
There is a noticeable theory-practice gap: the proof requires specific schedules (e.g., $\eta_k\propto k^{-3/4}$ and $\beta_{1,k}=1-1/\sqrt{k}$, whereas the practical defaults use a fixed $\beta_1$ (Ano) or the logarithmic Anolog schedule, with limited analysis of how far these choices deviate from the theoretical ones. Furthermore, from a theoretical standpoint, Sec. C.2 imposes a lengthy list of assumptions: a lower-bounded objective, unbiased gradient estimators with bounded variance, and, on top of that, both smoothness and bounded gradients. This feels overly restrictive; once the first three conditions are in place, it is more typical to assume either smoothness or bounded gradients, not both.

In terms of experiments, while results span CV/NLP/RL, the largest experiments remain moderate scale (e.g., CIFAR-level vision, GLUE-level language), so claims about large-scale pretraining or very long-horizon stability are untested, acknowledged in the Limitations.

### Questions
See weaknesses. To sum up:

1. Can you quantify the theory–practice gap by evaluating the theoretical schedules against the practical defaults (constant $\beta_1$ for Ano and Anolog’s logarithmic schedule)? How closely do their outcomes match in practice?
2. Can you reduce the number of assumptions in the theoretical analysis? 
3. Regarding experimental scope, do you have results beyond CIFAR-level vision and GLUE-level language, e.g., large-scale pretraining or very long-horizon runs, to support the broader claims?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3