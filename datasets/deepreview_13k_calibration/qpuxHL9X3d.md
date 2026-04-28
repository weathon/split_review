# Efficient Diversified Attack: Multiple Diversification Strategies Lead to the Efficient Adversarial Attacks

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Deep learning models are vulnerable to adversarial examples (AEs). Recently, adversarial attacks that generate AEs by optimizing a multimodal function with many local optimums have attracted considerable research attention.
Quick convergence to a nearby local optimum (intensification) and fast enumeration of multiple different local optima (diversification) are important to construct strong attacks. Most existing white-box attacks that use the model's gradient enumerate multiple local optima based on multi-restart; however, our experiments suggest that the ability to diversify based on multi-restart is limited.
Therefore, we propose the multi-directions/objectives (MDO) strategy, which uses multiple search directions and objective functions for diversification.
The MDO strategy showed higher diversification performance and promising attack performance.
Efficient Diversified Attack (EDA), a combination of MDO and multi-target strategies, showed further diversification performance, resulting in state-of-the-art attack performance against more than 90% of 41 robust models compared to Adaptive Auto Attack (A$^3$).
EDA particularly outperformed A$^3$ in attack performance and runtime for models trained on ImageNet, where the MDO strategy showed higher diversification performance.
These results suggest a relationship between attack and diversification performances, which is beneficial to constructing more potent attacks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose techniques to enhance the adversarial attack suite in terms of effectiveness and efficiency against robust models. Specifically, they start with a given search space containing possible gradient directions $\delta$ and losses $L$, and identify the top combinations of search direction $\delta$ and objective functions $L through Automated diversification search (ADS). They then proceed with a two-stage approach, 1 initial coarse-grained attack (GS) followed by a  2. localized attack within the region found by the best point in stage 1.  Furthermore, they combine the proposed approach with MultiTarget (MT) to obtain an Efficient diversified Attack.

### Strengths
- The authors present a unified formulation of an adversarial attack, encompassing aspects such as initialization, step size updates, search directions, and loss functions. This lets us to study each factor in a fine-grained manner and ultimately improve the attack performance

- The empirical evaluation is conducted on 41 models, which unquestionably provides a clear and comprehensive perspective and establishes robust baselines for future research endeavors.

### Weaknesses
 **Presentation:**

- In my initial reading, I found the paper's notation to be confusing. Moreover, all the crucial algorithms (ADS, GS, LS, EDA) are deferred to the Appendix, making for a less-than-smooth reading experience. Within the Appendix itself, these algorithms are distributed at different places in the 38-page paper, further complicating the reading process. I would request to consider moving a few of them (ADS, GS, LS, EDA, Target selection) to the main draft

- As also suggested by Reviewer pdmN, this paper had many abbreviations and particularly difficult to follow sometimes. I request the authors to simplify the paper presentation and notations.

**Technical:**

- In my view, the proposed ADS for selecting the most effective search direction ($\delta$) and loss function ($L$) based on the diversity measures at both input and output, appears quite straightforward. Additionally, the Diversity Index (DI) has been widely studied in Yamamura et al. 2021, thereby paper's technical contribution may be somewhat limited as it just picks the combinations based on this measure and $P_i^e$.

- The GS and LS techniques introduced within the search framework are, to some extent, heuristic in nature. Although ablation studies have been carried out with respect to N1, N2, and N3, the current framework's configuration, comprising GS with N1 and N2 iterations, followed by LS with N3 iterations, strikes me as somewhat heuristic.

- Upon closer examination, the differences in performance between ADS and Random appear negligible in Table 1, and the variation between GS+LS (ADS) and GS+LS (Random) seems relatively small. On average, across nine models, this difference stands at less than approximately 0.05% (please correct me if I'm wrong).

- Notably, there exists a substantial number of hyperparameters tied to ADS, GS, LS, and the target selection schemes. While the paper presents ablation studies, I anticipate that the widespread adoption of the proposed method as a robust alternative to the AutoAttack suite might pose a considerable challenge. 

- ADS requires access to the dataset. The authors perform ADS on 1% of the data, while AutoAttack and other baseline attacks operate on a per-datapoint basis without depending on additional datapoints.

### Questions
- Why are the step sizes set to 2*$\epsilon$ for $N_1$ iterations, $N_2$ iterations with $\epsilon$, and $N_3$ iterations with $\epsilon/2$?

- What is the individual influence of the two terms $P_i^e$ and DI(.) in the overall ADS search performance?

- What combinations were discovered by ADS for the different models? Are there any insights into the top $n_a$ combinations found by ADS for different models?

- Why is ADS performed in the LS stage? What are the benefits of conducting it before LS? While I understand that the initial points are different at these two stages, could the authors provide an empirical analysis of employing ADS in the LS stage?

- Are top combinations {$\delta_{a_j^*}, L_{a_j^*}$} found at GS, LS stages correlated? 

- Can you report the average performance over  9 models in Table 1 for all methods 

- In the absence of a dataset to perform ADS, is the combinations found by ADS transferable in the cross-domain setting?

### Soundness
2 fair

### Presentation
1 poor

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
This paper contributes a white-box adversarial attack framework of Efficient Diversified Attack (EDA) with a new multi-directions/objectives (MDO) strategy. This method focuses on the diversification of adversarial examples (AE) by utilizing multiple attack methods and objective or loss function. The effectiveness of MDO depends on appropriate search directions (δ) and objective functions (L). Thus, the authors propose an Automated Diversified Selection (ADS) algorithm to select the combinations of δ and L. The MDO strategy consists of two phases: the diversification phase (global search, GS) and the intensification phase (local search, LS). The authors conduct experiments to demonstrate the effectiveness of ADS and the GS+LS, and the efficiency of MDO in comparison to baselines.

### Strengths
1.	The paper is demonstrated well. The procedure figure and most diagrams are easy to understand. The presentation is easy to follow.

2.	The authors test their methods on 41 models and 21 different defenses, covering typical datasets of CIFAR-10/100 and ImageNet.

3.	The method reduces the number of queries and time spent to 86.9% on average, according to Table 2.

### Weaknesses
1. Even though this method saves time, the increase in attack success rate is little.
In Table 2, the delta of accuracy is very small. In Table 6 in the appendix, the delta of accuracy is less than 0.1% in most cases.

2. The diversification of EDA is not good enough.
In Figure 5, the Diversity Index (DI) of MT_cos exceeds that of the authors' methods. 

3. The authors’ methods are not consistently effective.
In Table 6, there are some cases that the authors’ method even takes longer time than the baseline. Considering the weakness in lack of improvement in diversification and effectiveness, could the authors discuss the tradeoff between efficiency and diversification?

4. This paper does not evaluate the effectiveness of combining these methods with their method.
There are many existing methods for improving the success rate of adversarial attacks, such as [1] and [2]. Can EDA and MDO be combined with them? If so, what will the diversification and effectiveness of the authors’ method and baselines be?

5. There is a contradiction between the text and the figure.
In section 4.1, the paper claims that “Figure 6 indicates that GS+LS found AEs in fewer queries than MT_cos”. However, in Figure 6, it seems GS+LS and MT_cos have similar numbers of queries, and there are more cases in which MT_cos takes fewer queries. Could the authors explain the reason? What do the average lines represent?

### Questions
1.	Can EDA and MDO be combined with other augmentation methods mentioned above? If so, what will the diversification and effectiveness of the authors’ method and baselines be?

2.	Could the authors explain the data in Figure 6? What do the average lines represent?

3.	Considering the weakness in lack of improvement in diversification and effectiveness, could the authors discuss the tradeoff between efficiency and diversification?

### Soundness
2 fair

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
The paper shows the ability to diversify the adversarial attck based on multi-restart is limited. The authors propose the multi-directions/objectives (MDO) strategy which shows higher diversification performance and attack performance. A combination of MDO and multi-target strategies is also provided. The experimental results show a relationship between attack and diversification performances.

### Strengths
- The idea is neat.
- The experimental results are plentiful.

### Weaknesses
 - The proposed approach is a white-box attack.
- Comparison with ACG attack (Yamamura et al., 2022) is not provided in Table 1.
- From Table 1 and 6, EDA is not better than GS+LS (ADS). The authors should give more analysis on that.
- Too much mathematics.
- It is hard to follow the paper. What is PAS? What does the graph $G(X,\Theta)$ mean?

### Questions
- What does the total distortion of the proposed method under $l_\infty$ attack.
- What is the motivation of generalized-DLR (G-DLR) loss, $L_{G-DLR, q}$.
- Does the initial point selection method $\phi$ and the step size update rule $\psi$ matter? The authors do not provide details on these.
- What does "the highest objective values found by an attack $a$ from $R$ initial points" mean?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an approach to improving adversarial attacks on deep learning models. The paper emphasizes the importance of diversification and intensification in constructing strong attacks. It introduces the multi-directions/objectives (MDO) strategy, employing multiple search directions and objective functions for diversification. The strategy results in more diverse and potent attacks. Furthermore, the Efficient Diversified Attack (EDA), combining the MDO and multi-target strategies, outperforms existing attacks in terms of diversification and efficiency.

### Strengths
- Research on adversarial examples is an important research topic. 
- The paper is overall well-written and provides extensive supplementary material. 
- While relatively intuitive, the discoveries in this work are novel to the best of my knowledge. 
	- Diversification Strategy: Introduces the multi-directions/objectives (MDO) strategy, a unique approach using multiple search directions and objective functions to enhance diversification in adversarial attacks.
	- Efficient Diversified Attack (EDA), combines the MDO and multi-target strategies resulting in a fast and potent attack

### Weaknesses
 - Overall the performance improvements are only marginal compared to previous results. 
- Previous works are concerned with the transferability of adversarial attacks. A transferability evaluation is missing. 
- The work mainly evaluates ResNet architectures. These days, the trend moves to the usage of transformer architectures. Hence an evaluation against transformer architectures would be beneficial and more timely. 
- The paper uses many abbreviations, making it difficult to comprehend at times.

### Questions
Please address the points in my weaknesses section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
