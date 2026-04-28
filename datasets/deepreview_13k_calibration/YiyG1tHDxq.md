# Bayesian Active Learning By Distribution Disagreement

- Decision: Reject
- Avg Score: 3.40
- Scores: 5, 3, 3, 3, 3

## Abstract
Active Learning (AL) for regression has been systematically under-researched due to the increased difficulty of measuring uncertainty in regression models.
Since normalizing flows offer a full predictive distribution instead of a point forecast, they facilitate direct usage of known heuristics for AL like Entropy or Least-Confident sampling.
However, we show that most of these heuristics do not work well for normalizing flows in pool-based AL and we need more sophisticated algorithms to distinguish between aleatoric and epistemic uncertainty.
In this work we propose BALSA, an adaptation of the BALD algorithm, tailored for regression with normalizing flows.
With this work we extend current research on uncertainty quantification with normalizing flows to real world data and pool-based AL with multiple acquisition functions and query sizes.
We report SOTA results for BALSA across 4 different datasets and 2 different architectures.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper addresses the challenges of active learning (AL) research in regression tasks, specifically when using normalizing flow models in pool-based AL settings. The authors propose two novel extensions of BALD algorithm, named BALSA, which approximate the BALD acquisition function by calculating distance between pairs of predictive distributions from different parameter samples. They evaluate BALSA's  performance across four datasets and two model architectures, demonstrating its effectiveness and robustness in real-world applications.

### Strengths
The paper is original in its focus on developing active learning strategies specifically for regression with normalizing flows, while much of the AL research traditionally focuses on classification tasks. 

The paper offers a comprehensive benchmark for AL in regression with predictive distributions. The experiments are robust, testing BALSA across four diverse regression datasets and two model architectures. This extensive comparison proves BALSA's effectiveness and generalizability.

### Weaknesses
The presentation of this paper could be improved.

For example, Figure 1 is presented without reference or explanation in the text, which reduces clarity for the reader.

In Pair Comparison, the paper introduces a pairwise approach to approximate Eq. 2, which is one of the core components of BALSA. However, the paper does not adequately explain why this approach is effective, nor does it discuss any potential trade-offs or advantages that led to this specific choice. The lack of justification for using consecutive pairs, as opposed to other pairing strategies, weakens the argument for this specific implementation.

The paper claims that  BALSA is specifically designed for use with Normalizing Flow models, but figure 1 suggests that the method might also be applicable to Gaussian Neural Network. This raises questions about what unique properties of normalizing flows motivated the development of BALSA.  A deeper discussion on this point would clarify the applicability of the method.

### Questions
In line 255, did you consider any alternative pairing strategies beyond consecutive pairs, such as randomly selected pairs or stratified pairing? If so, what were the findings or reasons for not using these alternatives?

in lines 278-280,  Why was the mathematical analysis omitted for BALSAKL Pair and BALSAEMD? Given their differences, might an appendix providing an overview of the theoretical differences still be valuable for readers?

In Figure 3, the results suggest potential overfitting, as performance decrease with an increasing number of labeled data points.

### Soundness
2

### Presentation
2

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
The paper studies active learning for regression tasks. It recognizes that this is harder than classification tasks and that current methods are suboptimal. The paper proposes 'BALSA' algorithms which are an extension of 'BALD' algorithm. A number of experiments are carried out to suggest the proposed algorithms compare favorably to previous ones.

### Strengths
The authors report strong results on the chosen datasets.

### Weaknesses
The writing is very poor and hard to follow. The notation exhibits a lack of rigor and mathematical expressions are not properly introduced. For example, it is unclear what each \theta_i in eq. (1) refers to. It's unclear how these quantities are measured.  'BALD' is also mentioned many times and never properly described.

While the authors claim that the datasets were selected to 'provide maximal intersection with other literature for AL with regression', they are quite small by modern standards.

I find the use of 'critical difference diagrams' quite strange, instead of reporting the actual performance of the methods.

I'm not necessarily interested in seeing the code at this stage but the link does not work for me.

### Questions
What *exactly* is your algorithm? How do you choose which points to label? Do you compute BASLA(x) for each of the unlabeled points?

How can you tell if your method better captures 'aleatoric' or 'epistemic' uncertainty?

236 - why is there no sound way of doing this?
246 - I don't understand; averaging k distributions still leads to a distribution
260 - how exactly are the 'parameter samples \theta_i' drawn? Why is this pairwise approximation sound?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes BALSA, a novel AL method that addresses challenges in regression models with uncertainty quantification, specifically for pool-based AL. While traditional uncertainty measures like entropy and least confidence are less effective here, BALSA adapts the BALD algorithm to handle predictive distributions, distinguishing between aleatoric and epistemic uncertainty. BALSA demonstrates state-of-the-art results across four datasets and two architectures by leveraging Bayesian techniques like MC Dropout.

### Strengths
1. The paper addresses an under-researched area of the literature.
2. The broader approach to the BALD acquisition criterion is interesting and appears to have strong potential.

### Weaknesses
1. Formatting issues:
   - Ensure paragraphs are indented throughout the document.
   - Correct the initial quotation marks by using `` for opening quotes in LaTeX.
   - In Figure 3, the abundance of methods makes the lines difficult to differentiate. Consider moving some of these methods to the appendix to enhance readability.

2. Results presentation: The results lack standard deviation and confidence intervals, making it challenging to fully trust the conclusions. Including these would provide clearer insight into the variability and reliability of the findings.

3. Missing baselines and experimental settings: Essential settings from Berry and Meger (2023a, b), such as the 1D and multi-D configurations, are absent, as well as Nflows Base and PaiDEs. These settings serve as crucial baselines and should be included to enable comprehensive comparisons.

4. Terminology clarification: The term MC dropout is used incorrectly in the context of Nflows Out, which is trained using a fixed set of dropout masks rather than MC dropout. This distinction should be clearly communicated to avoid confusion.

5. Acquisition function clarification: Berry and Meger (2023a, b) use differential entropy in their derivation of BALD as the acquisition function. What is meant by line 172 point (i)?

### Questions
Is the use of an encoder justified for this problem? It seems potentially excessive; was it essential for achieving strong performance, or could a simpler model have sufficed?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors developed an active learning (AL) algorithm for regression, introducing BALSA, an adaptation of the BALD algorithm specifically designed for regression tasks. They extended the Shannon Entropy used in BALD by incorporating additional distance measures, including KL-Divergence and Earth Mover’s Distance (EMD). The proposed method was evaluated on four datasets.

### Strengths
The authors gave a clear explanation of their proposed methods.

### Weaknesses
(1) The baseline models used in this paper are limited. Several active learning models capable of handling regression problems, such as BADGE [1], SIMILAR [2], and BAIT [3], are not included or compared in the experiments. Furthermore, the baselines that are included lack sufficient detail regarding their implementation and hyperparameter tuning, making it difficult to assess the true performance gains of the proposed method. The absence of established regression-focused active learning baselines makes it challenging to contextualize the contribution of BALSA.

(2) Many other Bayesian models are not considered. The use of Bayesian neural networks (BNNs) is restricted, with key methods such as SGHMC [4], SG-MCMC [5], and cSG-MCMC [6] missing. The paper does not explore the impact of different approximate inference techniques within the Bayesian framework, which could significantly affect the performance and uncertainty estimates used by the active learning algorithm. This limits the scope of the investigation and the generalizability of the findings.

(3) Regarding data modality, only tabular data are included, while image-based datasets, such as IMDB-WIKI [7], could have been explored. The experiments are limited to a single data modality, which does not demonstrate the versatility of the proposed method. The absence of experiments on image data, which is commonly used in active learning research, raises concerns about the applicability of BALSA to other domains.

(4) There is also limited discussion and experimentation on key factors such as query batch size and the differences between low-data and high-data domains. The paper does not explore how the performance of BALSA varies with different batch sizes, which is a critical hyperparameter in active learning. Furthermore, the experiments do not investigate the performance of BALSA in both low-data and high-data regimes, which is important for understanding the practical applicability of the method.

(5) No theoretical analysis or insights are provided to explain the performance improvements or offer any guarantees. The lack of theoretical justification makes it difficult to understand why BALSA performs better than other methods. The absence of theoretical guarantees also raises concerns about the robustness and reliability of the method.

### Questions
Various strategies can be employed to effectively select a batch of queries, such as greedy selection in BatchBALD [1] and stochastic batch acquisition [2]. Could the authors clarify why these extensions to a batch setting were not explored?

References:

[1] Kirsch, Andreas, Joost Van Amersfoort, and Yarin Gal. "Batchbald: Efficient and diverse batch acquisition for deep bayesian active learning." Advances in neural information processing systems 32 (2019).

[2] Kirsch, Andreas, Sebastian Farquhar, Parmida Atighehchian, Andrew Jesson, Frederic Branchaud-Charron, and Yarin Gal. "Stochastic batch acquisition: A simple baseline for deep active learning." arXiv preprint arXiv:2106.12059 (2021).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper focuses on active learning for regression, studying two model classes: normalizing flows and Gaussian Neural Networks (GNNs). Authors show that standard active learning acquisition functions (like entropy minimization) do not work well when applied to these models. Instead, authors apply approximate Bayesian inference in form of MC-dropout, and propose several adaptations of the previously proposed BALD acquisition function. Authors evaluate the baselines and proposed methods on 4 regression datasets.

### Strengths
- Originality: while I am not an expert in active learning, to the best of my knowledge the grid and pair-wise versions of the BALD acquisition function are novel.
- Reproducibility: comprehensive experimental details provided in the paper, code is publicly available. 
- Authors use critical difference diagrams to report results, which allows to compare methods across all datasets at once.

### Weaknesses
 - Lack of focus and motivation: the paper in its current form lacks focus, and does not present a compelling story. It proposes several methods and baselines, but the narrative did not make it clear what problems (with existing methods) the proposed methods are supposed to solve. The paper makes several observations, but the overall message/recommendation of the paper is not clear to me. Specifically, the introduction does not clearly articulate the limitations of existing active learning methods when applied to normalizing flows and GNNs, which are the core models explored in the paper. The motivation for the specific adaptations of BALD is also not well-established, leaving the reader wondering why these particular modifications were chosen.
- Clarity: it took me multiple re-reads to fully grasp the proposed methods and baselines. For example, Eq. (2) assumes a deterministic label, while section 5 suddenly jumps to predictive distributions. The "baselines" part of Section 5 is very dense, making it difficult to follow the experimental setup and the rationale behind each baseline choice. Section 3 does not cite important work (e.g. SVGD). Figure 1 is never mentioned in the main text, which is a missed opportunity to visually introduce the core concepts. Finally, authors have tweaked the style to remove paragraph spacing (presumably to fit more content), which further degrades readability. The sudden shift from deterministic labels in equation 2 to predictive distributions in section 5 is jarring and lacks proper explanation. The description of baselines in section 5 is too condensed, making it hard to understand the differences between them and their relevance to the proposed methods. The lack of paragraph spacing makes it difficult to parse the text and follow the logical flow of ideas.
- Significance: results suggest that BALD H and BALD Std are more or less competitive with BALSA KL variants, both on NLL and MAE. It is not clear to me from the results that BALSA strongly outperforms BALD. Combined with the lack of clear motivation for the method, this does not convince me that I should choose BALSA over BALD. The observation that baselines that don't estimate epistemic uncertainty don't do well in active learning is not surprising to me: I believe it's known that epistemic uncertainty is much more important for active learning. While the paper prods in multiple interesting directions in active learning, I did not find a significant-enough contribution to recommend acceptance. The fact that BALSA does not show a clear and consistent improvement over BALD across all metrics and datasets weakens the impact of the proposed method. The paper does not sufficiently demonstrate the practical advantages of using BALSA over simpler, well-established methods like BALD.

### Questions
- If authors were to pick the most significant/surprising finding in the paper, what would they pick?
- Why are authors only comparing _subsequent_ pairs in pairwise methods? Have authors considered performing comparisons across all pairs of posterior samples? Could this improve performance? (Appreciating this might have an impact on computational complexity)
- Is the 200 grid size fixed across all experiments? Have authors tried to perturb this value, and does it have any measurable impact on performance?
- What are the computational complexities (or empirical runtimes) of the evaluated methods/baselines?

### Soundness
2

### Presentation
1

### Contribution
1
