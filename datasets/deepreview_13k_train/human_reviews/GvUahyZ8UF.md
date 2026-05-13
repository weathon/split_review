# Improved Off-policy Reinforcement Learning in Biological Sequence Design

- Decision: Reject
- Scores: 8, 6, 3, 5

## Abstract
Designing biological sequences with desired properties is a significant challenge due to the combinatorially vast search space and the high cost of evaluating each candidate sequence.
To address these challenges, reinforcement learning (RL) methods, such as GFlowNets, utilize proxy models for rapid reward evaluation and annotated data for policy training. Although these approaches have shown promise in generating diverse and novel sequences, the limited training data relative to the vast search space often leads to the misspecification of proxy for out-of-distribution inputs. 
We introduce $\delta$-Conservative Search, a novel off-policy search method for training GFlowNets designed to improve robustness against proxy misspecification. The key idea is to incorporate conservativeness, controlled by parameter $\delta$, to constrain the search to reliable regions. Specifically, we inject noise into high-score offline sequences by randomly masking tokens with a Bernoulli distribution of parameter $\delta$ and then denoise masked tokens using the GFlowNet policy. Additionally, $\delta$ is adaptively adjusted based on the uncertainty of the proxy model for each data point. This enables the reflection of proxy uncertainty to determine the level of conservativeness. Experimental results demonstrate that our method consistently outperforms existing machine learning methods in discovering high-score sequences across diverse tasks—including DNA, RNA, protein, and peptide design—especially in large-scale scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies the problem of generative search, where we seek to generate novel and diverse particles from a large design space that yield high reward. A core practical challenge is that the proxy reward model used for the generative search is unreliable, particularly away from its supporting distribution. The paper proposes a new approach, $\delta$-conservative search, that controls "how much to trust" the proxy reward model during generative search. The approach is validated with extensive evaluation and shown to outperform other methods.

### Strengths
* The exposition of the paper is very clear.
* $\delta$-CS which works by injecting noise and learning to denoise the signal is a neat idea to constrain generative search.
* The method is evaluated against many strong baselines on relevant tasks, and shown to outperform all baselines most of the time.

Overall, this is a good contribution to the line of work on GFlowNets.

### Weaknesses
 * In the adaptive method for setting $\delta$, why does setting $\lambda \sigma \approx 1/L$ not set $\delta \approx \delta_{const} - 1/L$ to a constant that does not depend on the uncertainty $\sigma$? Given this, I find the name "adaptive" and the exposition slightly misleading. The adaptivity seems to stem from the sequence length $L$ and not the uncertainty about the reward proxy $\sigma$. How are the experimental results affected if $\lambda$ was chosen a constant?

* It would be nice to see the evaluation of various $\delta$ from Appendix B.1 extended to multiple datasets. It seems that the choice of $\delta$ is critical for the achieved performance and it would be interesting what ranges of $\delta$-values outperform the strongest baseline in each of the tasks to develop an understanding for the robustness of $\delta$-CS.

### Questions
* Can the authors elaborate how $\delta$ is chosen in the experiments? Is this a choice that can be reproduced in practice, i.e., does it require running $\delta$-CS with multiple (all?) values of $\delta$, or does it require determining $\delta$ from a (small) validation experiment, or something else?

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
3

### Summary
This paper introduces a novel method called $\delta$-Conservative Search ($\delta$-CS) for designing biological sequences with desired properties. Experiments across DNA, RNA, protein, and peptide design tasks demonstrate that δ-CS outperforms traditional methods, finding higher-scoring sequences. The approach successfully combines the advantages of evolutionary and reinforcement learning methods, offering a scalable and robust framework for biotechnological applications​.

### Strengths
This paper leverages GFlowNets for sequential generation, allowing it to efficiently generate diverse and high-reward biological sequences., and this method’s emphasis on balancing novelty with conservativeness addresses a key challenge in RL for scientific domains where exploration can easily veer into unreliable regions. This paper includes comparisons with various baselines and established benchmarks in biological sequence design.

### Weaknesses
1. Novelty: This paper draws from evolutionary search and existing GFlowNet frameworks, combining aspects of both rather than developing a unique algorithmic structure. Specifically, $\delta$-Conservative Search extends GFlowNets by adding a conservativeness parameter, δ, to manage exploration around known data. While useful, balancing exploration with reliability is a recurring theme in off-policy RL, particularly with techniques like uncertainty-based exploration in Bayesian optimization and upper confidence bounds (UCB). The paper does not adequately demonstrate how the specific implementation of the conservativeness parameter, which is based on the Hamming ball, provides a significant advantage over existing methods that achieve similar goals through different mechanisms, such as directly modeling uncertainty or using different exploration strategies.
2. Evaluating a sequence's performance is critical in the design of biological sequences. A fast, low-cost, and relatively accurate method can often significantly reduce the complexity of the problem. In this paper, the reward information provided to the model is Oracle f. Since the reward signal provided by $f$, $f$ determines the model's learning, the accuracy and generalizability of $f$ are crucial. I doubt the evaluation and experiments are testing out-of-distribution sequences, which rely on the accuracy of $f$. Specifically, the paper does not discuss the potential for the oracle function to be inaccurate or biased, especially when extrapolating to sequences far from the training data. This is a critical concern in biological sequence design, where models are often used to explore novel sequences, and the reliability of the oracle function in these regions is not guaranteed.

### Questions
1. Regarding the choice of $\delta$, although the authors reported a control experiment on $\delta$ in the appendix, are all the experiments in Table 1 based on the same $\delta$?
2. What is the initial dataset $D_0$? How is it initialized? What is the cost to acquire the reward for all sequences in $D_t$ in line 3 of Alg.1? 
3. It seems that model $f$ is fixed in training, and it provides reward information for $\delta$-CS; how can we ensure $f$ can provide safe and correct reward information?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
On-policy reinforcement learning (RL) methods for biological sequence design tasks exhibit limited search flexibility. In contrast, off-policy methods like GFlowNets provide diversity-seeking capabilities and flexible exploration strategies. However, GFlowNets struggle with long sequence tasks due to the (hypothesis (*)) poor quality of the proxy model which serves as a reward function for training the policy network.
This paper addresses the problem of GFlowNets' ineffectiveness in long biological sequence design tasks due to the proxy model misspecifications for out-of-distribution inputs and proposes $\delta$-CS, an off-policy search method for training GFlowNets to enhance robustness.
$\delta$-CS addresses this issue by incorporating a conservativeness parameter, $\delta$, which can adaptively control the search boundaries. This approach effectively restricts the search to more reliable regions, mitigating the impact of inaccurate proxy models for out-of-distribution data points.

### Strengths
- $\delta$-CS provides a balance between novelty and conservativeness.
- An adaptive variant of $\delta$-CS adjusts the level of conservativeness dynamically based on the difficulty of the search landscape, which may vary in practical applications.
- The paper provides empirical evidence by validating $\delta$-CS across various biological sequence design tasks (DNA, RNA, protein, peptide) against baseline methods.
- The paper is generally well-written, although there are some minor descriptive confusions, as listed in the weaknesses below.

### Weaknesses
1. The experiments do not convincingly demonstrate the “actual benefit” of the proposed approach relative to the related methods. I think, specifically, the paper should have presented how $\delta$-CS enhances robustness against proxy model misspecification by empirically evaluating the performance across varying proxy model initializations (e.g., from poor to high quality). Although the hard version of the task with a small search space (TF-Bind-8) is given, the hypothesis (*) is not quantitatively validated well enough when the search space is scaled up.

2. Another major concern is the lack of proxy model ablation, i.e. how does the performance of $\delta$-CS change under different proxy models used as a reward function? (See also the question below) This could demonstrate the flexibility of the proposed search approach without depending on the proxy model type specification.

3. The paper presents $\delta$-CS as a novel off-policy search method for training GFlowNets under proxy misspecification, however, how does $\delta$-CS differ from existing off-policy search methods for GFlowNets such as [7,8]? The method [7] proposes to train GFlowNet with the exploration of local neighborhoods, similar to restricting the search space via conservativeness, and [8] incorporates Thompson sampling to improve exploration. I think these should have been direct baselines of $\delta$-CS, as it would show the effectiveness of $\delta$-conservativeness against local search and sampling starting from the same initial misspecified proxy model. ( which were first published in 2023, so I think it is a fair comparison to ask). How does $\delta$-CS differ from these methods?


4. Using BO with a generative model [5,6] is a well-established approach to biological sequence design, which would provide a more competitive baseline than classical BO. Additionally, it would have provided stronger evidence to compare against existing trust region methods for biological sequence design [1,2,3,4], as the search intuition is similar and would be appropriate baselines for the proposed method-- since $\delta$-CS constraints the search space to reliable regions, similar to the trust region concept. BO is selected as a classical baseline, however, there are state-of-the-art trust region BO methods [2,3] that apply to combinatorial search spaces such as in biological sequence design space.

5. A quantitative analysis showing how the level of conservativeness/noise injection amount differs throughout the active learning rounds, which would validate the balancing capability of $\delta$-CS.

6. A part that requires a bit of clear discussion is that, if the proxy model is not of good quality then exploration helps to recover from getting stuck at local optima and collect diverse points, whereas over-exploration yields unreliable results as explained for using GFlowNets case. I think this trade-off could have been argued more clearly while motivating the method.

7. How do convergence and diversity of sampled sequences change w.r.t the batch size? It would have been better to show batch size ablations in a problem domain.

8. The paper lacks a discussion or a theoretical analysis on how $\delta$ yields better exploration, sample complexity, and/or convergence throughout the active learning process.

9. There is no clear discussion on the limitations and potential drawbacks of the method.



**Minor:**

- Line 77: The explanation regarding the search space size is unclear. Also, why it is necessary to show that the search space size is greater than 10^309? There is no explanation of what those numbers correspond to. (It is only clear to a person who is familiar with protein design literature, that 20 represents amino acids and the exponent is the length of the GPF protein sequence.)
- Regarding writing, the transition between RL and active learning terminology could be smoother. Specifically, the term "trajectories" is used without giving an explanation. Do they refer to the trajectory of sequences generated throughout the active learning/query rounds? For instance, the sentence (lines 80-81) could have been expressed more clearly, e.g. searching sequences around the neighborhood of observed (or annotated) data points. Or sampling full trajectories (in line 88).
- Appendix B.1, line 832, misspelling in "conservatives"

### Questions
1. Can we use $\delta$-Conservative Search with any other proxy model? 

2. For the baseline methods that require surrogate/proxy (e.g. BO), is the same proxy model of $\delta$-CS used, with the same initial dataset?

3. How diversity/novelty is calculated? Is it the diversity of the last top-k batches? Presenting this metric across active learning rounds would have enhanced clarity and provided a more comprehensive understanding of the diversity achieved by $\delta$-CS.

4. In Figure 5, AAV task, there is a substantial difference in diversity between the proposed method and baselines. Given that the search space is medium-sized—somewhere between RNA-A and GFP—what might be the reason for this significant disparity?

5. How does performance vary with respect to the initial dataset size, particularly in domains with large search spaces? The initial dataset sizes currently employed are very large (e.g. 50% of the whole search space for TF-Bind-8, or the value set for GFP is again too much) compared to what is used for active learning approaches in the literature.

6. How does noise injection/level of conservativeness differ throughout the active learning rounds? Have you analyzed the behavior with respect to the proxy uncertainty?

7. Line 478, Shouldn't the phrase in line 478 be "prone to generating low rewards"?

8. What is the main source of benefit of using an RL method that utilizes a proxy model (as a reward function) and trains a generative policy instead of using some other active learning frameworks that directly utilize inexpensive proxy/surrogate models that can work under very limited training data? Why train a reward model + policy network instead of directly using the proxy model for querying?

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
3

### Summary
The authors propose an off-policy search method, δ-Conservative Search (δ-CS), a novel off-policy search method for training GFlowNets designed to improve robustness against proxy misspecification. The proxy misspecification is critical in the biological sequence design problem due to its vastness of the search space and high cost of evaluating candidate sequences. 

The key of the δ-CS method is its dynamic control of search conservativeness through a parameter δ, which balances the trade-off between exploring new sequences and staying within the reliable regions of the proxy model. The method injects noise into high-scoring offline sequences by masking tokens randomly and then denoises them using a GFlowNet policy. This approach ensures that the search process is guided by the uncertainty of the proxy model, making it robust against proxy mis-specification, particularly for out-of-distribution sequences.

In summary, δ-CS offers a scalable, adaptive, and effective framework for generating novel and high-reward biological sequences, providing valuable contributions to the fields of synthetic biology and biotechnology.

### Strengths
**Novel Contribution**: A key challenge in previous active learning framework is that, the proxy model often produces
highly unreliable rewards $R(x; \phi)$ for out-of-distribution inputs. This paper mitigates this by providing off-policy trajectories denoised from noise-injected high-reward sequences. This paper uses $\delta$ to control the how "novel" the denoised sequences are compared with existing ones. For example, $\delta=1$ means the full on-policy search.  

**Comprehensive Experiments**: The experiments include a range of biological sequence design tasks, including DNA, RNA, protein, and peptide design. The comparison with several baselines, including DyNA PPO and other Bayesian optimization methods, further strengthens the claims.

### Weaknesses
 **Complexity in Implementation**: Although the proposed method shows strong performance, its implementation appears to be complex. The exploration in the active learning process is controlled by $\delta$, making its adaptation crucial. The current adaptation is controlled by the hyperparameters $\lambda, \delta_{\rm const}$. Additionally, the selection of high-score offline sequences is based on a rank-based reweighted prior, with hyperparameter ($k$). There are also potential alternatives for selecting high-reward offline sequences and adapting $\delta$. As a result, it remains unclear whether the "three steps" outlined in Lines 187-189 offer a general improvement over standard active learning methods or if the paper has cherry-picked one favorable combination.

**Uncertainty Estimate**: The method assumes that the proxy model can reliably estimate uncertainty. However, as noted in the paper, the proxy model is unreliable for out-of-distribution (OOD) inputs. This raises a concern: while the paper does not trust the proxy's output for OOD inputs during search, it still relies on the proxy to compute uncertainty for all inputs. This assumption seems questionable. I know that the experiments in Appendix B demonstrate that this adaptation is effective, but I want to hear the opinions from the authors on that.


**Choice of GFlowNets** The paper employs GFlowNets for the policy, which are equivalent to soft off-policy reinforcement learning algorithms. However, it does not explore whether the $\delta$-conservative search would be effective with other search methods. Furthermore, in Tables 1 and 2, the performance gain of GFN-AL + $\delta$-C over GFN-AL does not appear to be substantial compared to the performance gains of GFN-AL itself. This suggests that the main improvement might stem from the use of GFlowNets rather than from the search method. Many studies (to name a few, [1,2,3,4,5]) claim significant improvements over the standard GFlowNet (used in this paper), so it might be worth investigating whether replacing the GFlowNet in GFN-AL with a modified version could lead to even better performance than modifying the search.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
