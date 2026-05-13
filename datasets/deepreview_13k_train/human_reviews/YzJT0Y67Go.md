# HIPODE: Enhancing Offline Reinforcement Learning with High-Quality Synthetic Data from a Policy-Decoupled Approach

- Decision: Reject
- Scores: 3, 6, 5, 6

## Abstract
Offline reinforcement learning (ORL) has gained attention as a means of training reinforcement learning models using pre-collected static data. To address the issue of limited data and improve downstream ORL performance, recent work has attempted to expand the dataset's coverage through data augmentation. However, most of these methods are tied to a specific policy (policy-dependent), where the generated data can only guarantee to support the current downstream ORL policy, limiting its usage scope on other downstream policies. Moreover, the quality of synthetic data is often not well-controlled, which limits the potential for further improving the downstream policy. To tackle these issues, we propose \textbf{HI}gh-quality \textbf{PO}licy-\textbf{DE}coupled~(HIPODE), a novel data augmentation method for ORL. On the one hand, HIPODE generates high-quality synthetic data by selecting states near the dataset distribution with potentially high value among candidate states using the negative sampling technique. On the other hand, HIPODE is policy-decoupled, thus can be used as a common plug-in method for any downstream ORL process. We conduct experiments on the widely studied TD3BC and CQL algorithms, and the results show that HIPODE outperforms the state-of-the-art policy-decoupled data augmentation method and most prevalent model-based ORL methods on D4RL benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces HIgh-return POlicy-DEcoupled (HIPODE), a novel data augmentation approach for Offline Reinforcement Learning (RL), designed to overcome the constraints of existing policy-dependent augmentation techniques. Unlike traditional methods that either add noise or rely on dynamics models yielding data of uncertain quality, HIPODE generates high-return synthetic data that is policy-agnostic, thus supporting a variety of Offline RL algorithms. The method uses negative sampling to identify and select states with high potential values from near the existing data distribution.

The paper's key contributions include the development of HIPODE as a universal plug-in capable of enhancing the performance of any Offline RL process, independent of the downstream policy. Through experiments on the D4RL benchmarks, the authors show that HIPODE improves upon several model-free offline RL baselines and policy-decoupled data augmentation methods.

### Strengths
- Clarity: The paper is clearly articulated, presenting the concepts and methodology in a manner that is easy for readers to understand.
- Empirical contribution: It presents empirical results that indicate HIPODE's potential for improvement over current data-augmentation methods and model-free offline RL baselines on D4RL benchmarks.

### Weaknesses
 - Relevance of Dataset Quality Analysis: Section 3's analysis, while potentially informative, may have limited relevance to the paper's contributions. The use of the true environment for generating synthetic data is an idealized condition not typically accessible in practical Offline RL scenarios where learned dynamics models are employed. This idealization might overstate the effectiveness of high-return data augmentation as it does not account for inaccuracies that would be present when using a learned model for data generation. Moreover, the assertion that high-value states improve policy learning is somewhat tautological and may not be particularly insightful since it is well-understood that higher-quality datasets tend to yield better-performing policies. The analysis does not sufficiently address the practical challenges of generating high-quality synthetic data in the absence of a perfect environment model, which is a core problem in offline RL.

- Strength of Empirical Results: The empirical results presented, particularly in Section 5.2, lack sufficient detail and statistical rigor to substantiate strong claims of improvement. The absence of confidence intervals or a deeper statistical analysis in Table 3 makes it difficult to discern the significance of the performance gains attributed to HIPODE. Without this, the evidence provided does not firmly establish HIPODE’s superiority over, e.g., the NoV method. The lack of statistical significance testing makes it difficult to determine if the observed improvements are due to the method or random chance. Furthermore, the performance variations across different tasks are not thoroughly analyzed, leaving open the question of HIPODE's robustness across diverse environments.

- Benchmarking Against Recent Advances: The paper does not include comparisons to some of the more recent and potentially more effective model-based methods such as RAMBO and ROMI, which are known to deliver strong performances across various data regimes. This omission raises questions about the competitiveness of HIPODE and whether the improvements it offers are indeed leading-edge when considering the full landscape of contemporary Offline RL approaches. The inclusion of these comparisons would be critical for a more comprehensive assessment of HIPODE's performance and its standing relative to the state-of-the-art. The absence of these comparisons makes it difficult to assess the true novelty and practical impact of the proposed method.

### Questions
N/A

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The impact of different types of augmented data on downstream offline reinforcement learning (ORL) algorithms is thoroughly examined by the researchers. Their findings reveal that high-quality data has a greater positive impact on the performance of downstream offline policy learning compared to noisy data with high diversity. 

To address this, the authors propose HIPODE, a policy-decoupled data augmentation method designed specifically for offline reinforcement learning (ORL). HIPODE acts as a versatile plugin capable of augmenting high-quality synthetic data for any ORL algorithm while remaining independent of the downstream offline policy learning process. HIPODE is evaluated on D4RL benchmarks, and the authors demonstrate its enhancement of multiple model-free ORL baselines. Furthermore, HIPODE surpasses other policy-decoupled data augmentation approaches for ORL.

### Strengths
- It is important to have a data augmentation approach that is policy-agnostic.
- The idea is simple yet effective
- The paper is well-written and easy to follow.

### Weaknesses
 - In the experiments, the authors only test the proposed approach in environments where the agent’s action has a cyclic pattern. For these tasks, the transition model could be relatively simple and easy to be learned. This raises concerns about the generalizability of the proposed method to more complex environments with non-cyclic action patterns or where the transition dynamics are more intricate. The evaluation should include environments with more diverse and less predictable dynamics to demonstrate the robustness of the approach.
- The experiments with only 3 random seeds are unreliable in terms of reinforcement learning. The variance in performance across different random seeds can be significant, especially in complex RL tasks. Using only 3 seeds makes it difficult to draw statistically significant conclusions about the effectiveness of the proposed method. A more robust evaluation would require at least 10 random seeds to provide a more reliable estimate of the algorithm's performance.
- It seems that there is no theoretical statement for the proposed approach. The lack of theoretical grounding makes it difficult to understand the conditions under which the proposed method is expected to work well and when it might fail. A theoretical analysis would provide insights into the convergence properties and limitations of the approach, which is crucial for the scientific rigor of the work.

### Questions
- It would be great if the authors could also provide the average return of the offline dataset in Table 1 and Table 2.
- Is the proposed approach applicable to the environment with discrete action space? It would be great if the authors could provide more experiments on different environments, such as Atari.
- It is interesting that the proposed method significantly outperforms previous methods on walker. What’s the cause of it?

------
### Post rebuttal
I appreciate the authors' provide further response and explanation. I am willing to keep my original scores.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes HIPODE, a novel data augmentation technique for offline reinforcement learning that generates high-quality (i.e. high-return) augmented data in a policy-independent fashion. At a high level, HIPODE generates augmented transitions with high value estimates near the support of the offline dataset. Empirically HIPODE is competitive with other augmentation strategies and improves performance across several offline RL algorithms.

### Strengths
1. Many prior data augmentation works have demonstrated the effectiveness of different augmentation strategies and frameworks, but the question of what augmented data *should* be generated is much less studied (I expand on this in the Weaknesses section). Thus, this paper is novel and quite timely.
    
2. Empirical analysis is thorough: a variety of tasks and baselines are considered.

3. The proposed algorithm is intuitive, indeed generates high-value augmented data (i.e. it accomplishes what the papers claims it should accomplish, shown in Figure 4)

### Weaknesses
1. My primary concern relates to the first contribution, “Our findings indicate that high-return data, as opposed to noisy data with high diversity, benefits downstream offline policy learning performance more.” I think the community implicitly understands that offline RL algorithms perform with high-quality “expert” data, though few works explicitly state this claim. I think it’s absolutely a point worth discussing, though I wouldn’t consider it a core contribution. The claim itself is also difficult to assert, since prior and current works show that the story isn't so clear-cut. For instance:

* Kumar et. al [1] discuss how offline RL algorithms benefit from noisy expert data.
* Yarats et. al [2] show that vanilla off-policy RL algorithms can outperform state-of-the-art offline RL algorithms when given highly diverse data.
* Corrado et. al [3] introduce a framework for generating expert-quality augmented data that outperforms random data augmentation frameworks. 
 * Corrado et. al [4] show that increasing an agent's state-action diversity via augmentation often yields more improvement than increasing the amount of reward signal an agent receives via augmentation.
* MoCoDA [5] is a data augmentation framework that enables users to directly control the distribution of augmented data generated. In particular, the user a can ensure task-relevant data is generated. This work also outperforms random data augmentation frameworks (including its predecessor CoDA [6])

I suggest rephrase section 3 as more of a didactic example illustrating how high-value augmented data can be more useful than diverse data. I also suggest including some or all of these works in the paper's related work section -- particularly [3] and [5], since both of these works focus on generating high-value augmented data.

2. My second concern is that the method seems to focus on generating high-value augmented data with low diversity (or low state-action coverage), but as mentioned above, data diversity is also quite important to the success of data augmentation. Thus, HIPODE may have limited applicability. I don't consider this a huge drawback though; in principle, one could use HIPODE to generate high-value augmented data along with an augmentation strategy that generates highly diverse (and potentially low-value) augmented data. It would be interesting to run experiments with "Original + Return + Diversity X" augmented data (using the naming convention of Table 1).

3. I'm skeptical about using learned model to generate rewards. Offline RL requires access to a reward function, so why not simply label augmented transitions with their true reward? Generating augmented rewards seems like an unnecessary source of variability.

4. Intuitively, I would expect HIPODE to offer the largest performance boost with random D4RL datasets (datasets which contain little to no high-value data), but its difficult to assess whether this intuition is true given the current presentation of results in Tables 2 and 3. I suggest grouping table rows by dataset type (random, medium, expert) and discussing general performance trends across dataset types.

5. The paper should include significance test for results reported in Table 1 and Table 2. (e.g. paired-t test at a 95% confidence level). For instance, in Table 1, the “Original + Return” returns for “halfcheetah-m-r” look very similar to returns for the other datasets.

6. Minor suggestion: the empirical section may flow a bit better if you first show HIPODE indeed generates high-value augmented data and *then* show that HIPODE improves performance.

### Questions
1. The notion of “policy-decoupled” data augmentation is not clearly defined. Could the authors please clarify the difference between a policy-coupled a policy-decoupled data augmentation strategy?

1. The purpose of Figure 2 is unclear to me. The core claim of section 3 is that high-quality data is better than random data, and this claim is supported by Table 1 (somewhat--see next point). Figure 2 seems to simply show that high-quality data has the highest reward (which is obvious, by definition). What’s the purpose of t-sne here?

1. HIPODE generates augmented data that remains close to the support of the offline dataset. S4RL essentially adds small random perturbations to data and thus also generates data close to dataset’s support. Would it be correct to say that HIPDOE is much more careful version of S4RL?

1. Could HIPODE in principle be used for online RL?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method, HIPODE, for generating synthetic data that can improve the performance of offline RL algorithms. HIPODE generates high-return samples by generating multiple next-state candidates from a trained CVAE and selecting the sample with the highest value estimate. An L2 penalty term is added to the critic loss to prevent overestimating OOD state values. From the sampled high-return states, actions and rewards are computed using an inverse dynamics model. Finally, the authenticity of the actions is checked using a forward dynamic model, and unreliable actions are discarded.

### Strengths
### Originality

* The authors conducted experiments that show the importance of high-return trajectories.

* They devised a clever next-state generation method based on negative sampling that enables HIPODE to generate high-valued next-states without overestimating the values too much.

### Quality

* The paper presents multiple experimental results that can show the effectiveness of HIPODE.

* The Introduction and Related Work sections provide a nice overview of existing Offline RL algorithms.

### Clarity

The paper is overall well-written and is easy to understand.

### Significance

Unlike other data-generating algorithms for offline RL, HIPODE is decoupled from the downstream offline RL policy, which allows it to be plugged into any existing offline RL algorithm.

### Weaknesses
1. In Section 3, the paper compares the results of the downstream offline RL algorithm using two types of augmented data: high-diversity data and high-return data. The high-return data was generated from a well-trained offline policy with a higher return. Since it is well-known that offline RL algorithms tend to perform better on medium-expert datasets than medium datasets, I believe it is evident that the downstream offline RL algorithm performs better with high-return augmented data. The two augmented data should have a similar maximum return value for a fair comparison.

2. The paper compares the performance of HIPODE with CABI. HIPODE and CABI share common aspects, such as using forward and inverse dynamics models. A careful analysis of how they differ from each other would be helpful for the readers to understand the novelty of HIPODE.

### Questions
Please refer to the **Weaknesses** section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
