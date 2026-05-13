# CTBench: A Library and Benchmark for Certified Training

- Decision: Reject
- Scores: 5, 6, 3, 5

## Abstract
Training certifiably robust neural networks is an important but challenging task. While many algorithms for (deterministic) certified training have been proposed, they are often evaluated on different training schedules, certification methods, and systematically under-tuned hyperparameters, making it difficult to compare their performance. To address this challenge, we introduce CTBench, a unified library and a high-quality benchmark for certified training that evaluates all algorithms under fair settings and systematically tuned hyperparameters. We show that (1) almost all algorithms in CTBench surpass the corresponding reported performance in literature in the magnitude of algorithmic improvements, thus establishing new state-of-the-art, and (2) the claimed advantage of recent algorithms drops significantly when we enhance the outdated baselines with a fair training schedule, a fair certification method and well-tuned hyperparameters. Based on CTBench, we provide insights into the current state of certified training and suggest future research directions. We are confident that CTBench will serve as a benchmark and testbed for future research in certified training.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents CTBENCH, a standardized library and benchmark designed to fairly evaluate certified training algorithms for neural networks, addressing the inconsistency in previous evaluations due to varied training schedules, certification methods, and under-optimized hyperparameters. By testing all algorithms under consistent conditions with tuned hyperparameters, CTBENCH reveals that most certified training methods perform better than previously reported, setting new benchmarks. Through CTBENCH, authors uncover several interesting properties of models training with certified methods.

### Strengths
1. The paper proposes a new benchmark for certified robustness methods for image classifiers.
2. Authors implement several prominent certified robustness methods in a unified framework, thereby standardizing the implementations to facilitate future research.
3. Furthermore, authors correct implementation mistakes and perform systematic hyperparameter tuning to fully realize the potential of all methods.
4. Authors present several interesting findings regarding the properties of ceritified robustness methods, for example, models trained using distinct methods have a high overlap in the examples they succeed and fail on, uncovering a sample-specific inherent difficulty level that can be leveraged to improve training. And, these methods can boost OOD generalization for specific corruptions, and hurt generalization for others.

### Weaknesses
1. Authors incorrectly state that the benchmark from Li et al. is not up to date as "it reports 89% and 51% best certified accuracy for MNIST epsilon = 0.3 and CIFAR-10 epsilon = 2/255 in its evaluation, respectively, while recent methods have achieved more than 93% and 62%". However, at the time of this review, the numbers on Li et al.'s leaderboard (https://sokcertifiedrobustness.github.io/leaderboard/) are even higher than 93% and 62%, they are 94.02% and 68.2%. Furthermore, the leaderboard toppers are defenses from 2019/2021. It appears that the authors might have pulled their numbers from a stale source.
2. In order to be an improvement over the existing benchmark (of Li et.al.), one important requirement is comprable or improved comprehensiveness. Based on the results in the paper, the proposed benchmark is significantly less comprehensive than Li et. al. on two important directions: (i) number of defenses evaluated, (ii) number of diverse models used during evaluation. While I understand that the proposed work can be made more comprehensive by running more experiments, this is not the case currently and so is worth poining out.
3. Furthermore, as stated in the limitations section, the propsoed benchmark only focuses on deterministic certified robustness in the L_infinity space. Whereas, Li et. al.'s benchmark uses both determinisitc and probabilistic certified methods, and covers all the popularly used norms in literature (i.e., L_1, L_2, L_infinity). Thereby further hurting the comprehensiveness of the proposed benchmark.
4. Some of the findings presented in this paper are expected and already established by prior works (see Questions).
5. The main contribution of the paper is a unified code-based (and benchmark) for promiment certified robustness methods. Even though authors uncover several interesting findings while reproducing and tuning sota methods, the nature of the contributions of this paper are heavily empirical (not enough technical novelty). As such, this paper is much better suited for venues like TMLR that put emphasis on contributions of such nature.

### Questions
1. It is already well established by previous works that robustness training increases local smoothness. What is unique about the findings presented in this paper?
2. It is also previously established that adversarially robust trianing methods tend to have higher sample complexity, and therefore are more likely to overfit (less regularization). Other than the choice of metric, what is unique about the findings in Section 5.4.?
3. Is there an explanation for why the model performs worse for certain corruptions? How will these results be affected if we use different L_p norms? For example, I would expect a model trained to be robust in the L_2 space to be better resistant to Gaussian noise and less resistant to salt and pepper noise.

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a benchmark for certified robust training. The goal is to standardize the hyperparameters, training schedules (& other training configurations) between competing methods in certified training. The purported advantages of newer methods are lower when older baselines were given equivalent optimization and testing conditions. The work covers several popular approaches like PGD, IBP, and CROWN-IBP.

### Strengths
-- The paper is well-written and typeset well

-- Tackles an important problem in the field: the inconsistent evaluation of different certified training methods. I think the field needed this kind of paper. 

-- It's not only a benchmark paper but provides some analysis into certified model behavior in loss fragmentation (showing certified models reduce fragmentation compared to adversarial training), have shared mistake patterns, model utilization metrics, and generalization performance (showing certified training provides benefits for certain types of corruptions).

### Weaknesses
 -- The novelty of the paper is limited since it's just focused on benchmarking existing methods. Certified robustness is a relatively new field and the field needs methods as much as unifying benchmarks. I think the lack of novelty is mitigated to an extent by the analysis provided in Section 5.

-- I wonder about the sustainability of the benchmark since there are other leaderboards for adversarial training (e.g. RobustBench). Others may want to submit their work to an existing leaderboard rather than standardize to adopt your settings.

-- I'm a bit confused about the purpose of the fragmentation experiments. Robust models lead to fewer flipped neurons in the presence of noise, but why should we care? This is after all expected given they are more robust in general to input noise. I believe these experiments may be valuable but the authors should articulate why.

### Questions
Some questions I had while reading:

-- Why do methods like TAPS and MTL-IBP achieve better accuracy while deactivating more neurons?

-- Is there a theoretical framework to explain the relationship between neuron deactivation and robustness? 

-- Is there a way to understand and leverage the shared mistakes patterns to improve certified training? Or is it natural that mistakes would overlap (similar to how mistakes overlap in natural training)?

### Soundness
3

### Presentation
4

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
This paper proposes a library for benchmarking certified training methods under unified settings. It uses the best practices for certified training from (Shi et al., 2021), such as CNN7 architecture with batch normalization, IBP initialization, warm-up schedule and warm-up regularizers. To improve generalization, it uses L1 regularization and stochastic weight averaging (Izmailov et al., 2018). From the implementation perspective, the authors propose to use full batch statistics to address problems with batch normalization when gradient accumulation or PGD attack is performed. The paper claims that the improvements of recent methods in certified training drop significantly compared to older IBP training method under the same settings with proper hyperparameter tuning. Further, the authors analyze different aspects of the training methods: regularization strength, model utilization, loss fragmentation, OOD generalization and shared mistakes.

### Strengths
- The paper raises an important question of fairly assessing the algorithmic improvements of recent certified training methods compared to older IBP-based training. Since the evaluation depends on many factors and components, the paper proposes to fix some of them to the best-known ones and to properly tune the rest. 
- The writing is clear (except for the presentation of Table 1), the code for benchmarking, and the weights of pre-trained models are provided. 
- The analysis of training methods leads to interesting conclusions. Particularly, the relationship between propagation tightness and certified accuracy at larger epsilon, i.e. the absence of correlation, is surprising.

### Weaknesses
I believe the **experiments are insufficient** to support the main claims of the paper. Particularly:

1.  **Accuracy-robustness tradeoffs are not considered**. Improvements in robustness can be due to decreased natural accuracy, and vice versa [a, b, c]. For example, in Table 1 for CIFAR-10 at 2/255 the implementations of following methods choose a different point at accuracy-robustness tradeoff curve compared to the one in literature, getting higher robustness at the cost of reduced accuracy: CROWN-IBP, SABR, STAPS, MTL-IBP, making claims about technical improvements unsupported. In this regard, the baselines such as ACERT [a], and ACE [b] are missing. Accuracy-robustness tradeoff curves and metrics such as ART-score [a] can be used to capture the improvements in the tradeoff.
2.  **Error bars are missing**.  The presented improvements over the results in the literature could be statistically insignificant. For example, the experimental results for CIFAR-10 at 8/255 in paper by Shi et al. (2021) show standard deviation of $\pm0.3$ for certified accuracy and of $\pm0.4-0.7$ for natural accuracy, which makes improvements in both accuracy and robustness in Table 1 for SABR and TAPS within the error of standard deviation. 
3.  **Training costs are not considered**. Different methods require different amount of computational costs for training, which could be an important factor to consider in benchmarking.
4.  **Certification costs are not considered**. Since some certified training methods allow computing tight certified bounds using efficient "online" certification methods, such as IBP (Gowal et al., 2018, Mao et al., 2024), the IBP-based certified accuracy or IBP-based certified radius [a] could also be compared. The cost of test-time verification might be an important factor in choosing a training method.

Since this is a paper proposing a benchmark, it **lacks original** contributions. In terms of evaluation setting, most of the components were already used consistently in previous works.

Smaller comments:
- The main results in Table 1 are hard to parse and analyze due to large amount of numbers to compare. Accuracy-robustness plots could help with improving clarity.
- Due to shared mistakes, the paper claims that "_... there could be an intrinsic difficulty score for each input_". The certified radius of robustness of each point, described in [a, d], could serve as such score. The average certified radius and/or the histogram of radii [d] can be compared in the benchmark. The adaptive training methods can be discussed in this regard.

### Questions
The main concerns about the experiments are raised in the weaknesses section. If these can be addressed, I would be happy to change my opinion.

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
The The paper introduces CTBENCH, a unified library and benchmark for evaluating certified training methods for neural networks. It addresses the challenges in comparing existing certified training algorithms by standardizing training schedules, certification methods, and hyperparameter tuning. The authors demonstrate that most algorithms in CTBENCH surpass previously reported results, revealing that much of the perceived advantage of newer methods diminishes when outdated baselines are properly tuned. The benchmark provides insights into certified training methods, encouraging future research by offering a consistent framework and re-establishing state-of-the-art performance.

### Strengths
1. The paper is well presented, well written, with clear goals and objectives.

2- While this is for a non-expert is not obvious, but the amount of experiments and computation required in this paper is beyond impressive.

3- The insights of the paper are particularly helpful. I personally did not expect that current SOTA methods are under performing. However, it was not that surprising that the improvements over IBP for larger epsilons are not that big.

4- Paper sheds light on a relatively good problem.

### Weaknesses
1. The paper focuses solely on deterministic certified training, overlooking advancements in randomized certified robustness. I believe the paper should have cited works like Cohen et al., Matthias et al. (l1 certification with differential privacy -- early works from 2019), Greg Yang ("All Shapes and Sizes" paper), among many others. While the authors clearly state their focus, the lack of discussion on randomized methods limits the scope and applicability of the benchmark, especially considering the scalability advantages of randomized approaches for larger models.

2. The paper only considers infinity ball, neglecting other perturbation sets. While this is generally okay, some insights with a few experiments in other perturbation sets might be helpful. It is not clear whether the proposed tricks in the library as part of the unified certified training would work for other perturbation sets (e.g., L2). If they do not, it raises the question of whether we would need a separate library for each perturbation set. The next steps are unclear if that is the case. The absence of any discussion on the challenges and potential adaptations needed for other norms is a significant oversight.

3. Some conclusions on the impact of tuning and modifications, while valid, lack formal decomposition, making it difficult to quantify individual contributions. No clarity on the contribution of each individual component (batch norm, etc) towards the final performance. A small systematic study will be very helpful. The lack of ablation studies makes it difficult to understand the true impact of each component and limits the practical guidance that can be derived from the benchmark.

4. The evaluation is based on a single model architecture (CNN7); the paper should demonstrate that the library and recommendations hold across different architectures. The reliance on a single architecture, especially one that is relatively small and dated, raises concerns about the generalizability of the findings and the practical relevance of the benchmark for modern deep learning models.


General comment: Interest in certified models has significantly declined over the past two years. At ECCV, for example, there were notably fewer submissions and accepted papers on adversarial attacks, even though this topic was previously very popular in vision conferences. One reason for this decline could be the uncertainty around where such certifications can be practically deployed, especially given the massive scale of current models, which are thousands of times larger than the CNNs discussed here. Furthermore, as models shift towards generative architectures, it’s unclear who will find this domain relevant. While the paper makes valuable contributions, this direction feels somewhat outdated by about two years and the question of the benefit for it is very unclear and vague, at least to me. I would love to hear the authors take on this.

Minor Comments:
1. Cite "is NP-complete" line 321.
2.  Is not typical robust accuracy (adv acc) for PGD around 48% on 8/255 CIFAR10? Or is because you use CNN7.
3. adversarial accuracy is not well defined in line 135. You need to say that it is empirical and serves as an upper bound to the robust accuracy.
4. certified accuracy defined in 133 is not correct. It should be the portion of *correctly* classified samples that are certifiably robust.

### Questions
See above; I would love to hear the authors comments on each of the weakness above along with a response to the general comment.

### Soundness
4

### Presentation
4

### Contribution
2
