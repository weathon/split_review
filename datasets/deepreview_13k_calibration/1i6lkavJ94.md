# Conformal Generative Modeling with Improved Sample Efficiency through Sequential Greedy Filtering

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 5, 6, 6

## Abstract
Generative models lack rigorous statistical guarantees for their outputs and are therefore unreliable in safety-critical applications. In this work, we propose \textit{\underline{S}equential \underline{Co}nformal \underline{P}r\underline{e}diction for \underline{Gen}erative Models} (\textit{\ourmethod}), a sequential conformal prediction method producing prediction sets that satisfy a rigorous statistical guarantee called conformal admissibility control. This guarantee states that with high probability, the prediction sets contain at least one admissible (or valid) example. To this end, our method first samples an initial set of i.i.d.\ examples from a black box generative model. Then, this set is iteratively pruned via so-called greedy filters. As a consequence of the iterative generation procedure, admissibility of the final prediction set factorizes as a Markov chain. This factorization is crucial, because it allows to control each factor separately, using conformal prediction. In comparison to prior work, our method demonstrates a large reduction in the number of admissibility evaluations during calibration. This reduction is important in safety-critical applications, where these evaluations must be conducted manually by domain experts and are therefore costly and time consuming. We highlight the advantages of our method in terms of admissibility evaluations and cardinality of the prediction sets through experiments in natural language generation and molecular graph extension tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This fairly well-explicated paper considers the following question of much recent interest: how could we obtain some semblance of guarantees for generative models' outputs i.e. in terms of factuality. This is related to the problem of hallucination control directly, since a method involving calibration for correctness could reduce hallucination if a suitable domain-specific calibration set were available. The approach of the paper is simple yet innovative. In a basic sense it does the following: In the first step, the method samples from the generative model conditioned on a fixed input. There is a calibration parameter that controls, based on a suitable non-conformity measure, that the generations contain at least one correct generation. Then, the generated set is pruned further using separate calibration parameters based on diversity and factuality considerations. Unlike some previous works, the sequential nature of the process permits the overall admissibility to be easily factorizable, permitting a direct application of conformal prediction proper. An interesting connection is also made to the pareto methods since there are multiple calibration parameters to be handled. The experiments report a general improvement datasets and are sufficient to demonstrate the applicability of the proposed method.

### Strengths
-- The paper is quite well-written and clear. Each of the steps are well-described and easy to follow. 

-- The method is novel along multiple axes: Wrappers generally make far more simplifying assumptions due to the intractability of conformal prediction directly in such settings; the admissibility control criteria and the connections to pareto methods are interesting and could provide straightforward avenues for future work.

-- While still compute intensive (since multiple generations are required), it could be tuned based on available data for some domain.

### Weaknesses
 -- There are now a bunch of papers on using conformal wrappers for filtering long form generations by dividing them into segments and then scoring. I think it would have been great to evaluate on such tasks as well, as generally QA type tasks are a bit too easy.

-- Sampling multiple times and expecting a correct response can be quite compute-intensive.

### Questions
-- I might have missed it, but do at least a fraction of the experiments report some kind of human evaluation? I think to validate the method, at least some of it might be reasonable. While using another generative model (as a judge or to generate a calibration set) is popular, it still presents an incomplete analysis. 

-- The authors might also want to discuss the works on conditional language validity by Cherian https://arxiv.org/abs/2406.09714 and also the earlier work by Mohri and Hashimoto https://arxiv.org/abs/2402.10978. Further, there is also a literature on confidence scoring which is often used for fine-tuning and reducing hallucinations. e.g. Kuhn et al. https://arxiv.org/abs/2302.09664, Lin et al. https://arxiv.org/abs/2305.19187, Wang and Holmes https://web3.arxiv.org/abs/2406.05213. It would be useful to include a brief discussion of these and how conformal methods might be used to calibrate such scores. It would help to bridge the two somewhat separate lines of enquiry together.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents SCOPE-Gen, a sequential conformal prediction method designed to generate prediction sets that satisfy admissibility guarantees with high probability. The method operates in two main stages: a generation stage and a filtering stage. In the generation stage, i.i.d. samples are drawn from the generative model until a specified non-conformity measure (related to sample count or quality) surpasses a threshold set by calibration with ground-truth samples. In the filtering stage, the prediction set is refined in a greedy manner, optimizing for diversity and quality based on another threshold derived from calibration. To ensure admissibility, the approach leverages a Markov chain factorization for admissibility control, and calibration is conducted on independent, non-overlapping data subsets to enable this factorization. Experimental results demonstrate that SCOPE-Gen reduces both the number of queries to the admission function during calibration and the size of the prediction set needed to meet admissibility requirements, outperforming baseline methods like CLM.

### Strengths
* This paper presents an efficient approach for generating prediction sets with admissibility guarantees by using a sequential generation and greedy filtering strategy.
* It reduces the number of admissibility checks during calibration compared to previous baselines, improving computational efficiency.
* Experimental results support the method’s effectiveness in reducing both query counts and prediction set sizes to meet admissibility criteria.

### Weaknesses
 * The paper lacks a theoretical analysis detailing how effectively the proposed method reduces the required admissibility checks and prediction set size. Specifically, while the method aims to reduce admissibility checks, there is no formal proof or analysis of the conditions under which this reduction is guaranteed or how the reduction scales with problem complexity or dataset size. The absence of such an analysis makes it difficult to assess the practical advantages of the method in different scenarios.
* The sequential generation and filtering process may introduce additional computational costs by generating a large number of samples before the filtering stage. The paper does not provide a detailed analysis of the computational overhead introduced by this process. It is unclear how the number of generated samples scales with the desired level of admissibility or the complexity of the generative model. This lack of analysis makes it difficult to assess the overall efficiency of the method, especially when compared to methods that directly generate admissible sets.
* The calibration process, which involves sample splitting for generation and each filtering stage, may require extra ground-truth samples to determine accurate threshold (lambda) values. The paper does not discuss the sensitivity of the method to the size of the calibration sets or the impact of this splitting on the overall performance. The choice of the size of the calibration sets and the splitting strategy could significantly affect the accuracy of the threshold values and, consequently, the performance of the method. A more detailed analysis of the impact of calibration set size and splitting strategy is needed.

### Questions
* The paper defines admissibility as including at least one (semantically) correct answer in the prediction set and aims to minimize the prediction set size while ensuring this inclusion. This is achieved by a “sub-sampling” technique, sampling answers based on a quality score ranking. Can the proposed method generalize to a broader admissibility definition, such as including multiple correct answers (e.g., 5 out of 10) or maximizing the fraction of correct answers? How would this method perform compared to baselines if the goal were to optimize the fraction of acceptable answers within a fixed prediction set size?
* How does the sequence of filtering stages (diversity vs. quality) impact performance? Why is diversity filtering prioritized in the proposed method?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a heuristic algorithm to filter predictions of generative model to achieve conformal admissability. It argues that previous techniques need to evaluate the admissability multiple times per instance during the calibration phase, which is impractical when the admissability is evaluated by a human oracle. In their setup, the admissability factorizes into Markov chain and thus es requires fewer queries to the admission function (e.g. human oracle). The paper presents the algorithm for the filtering heuristic as well as the necessary calibration algorithms using two filters based on diversity and quality functions of the generated examples. The experiments over natural language generative tasks and molecular generation reporting favorable metrics in particular in terms of reduction in number of queries and runtime.

### Strengths
The paper addresses an important problem of current stochastic generative models hallucinating non-factual responses. Formulating this problem within the risk-control framework can provide the mathematical means for addressing it. The experimental evaluation over the natural langauge tasks seems relevant.

### Weaknesses
I find the empirical evaluation very difficult to asses both, on its own as well as in comparison to previous methods. To understand the effects of various parts of the proposed algorithms, it would be beneficial to perform ablation studies that could provide more insights into the effects of its individual components (e.g. the update function, the coverage level $\alpha$, etc.). 
I am not convinced about the benefits of the molecular example - when there is only one valid/admissable example, it seems to me that simple checking of the validity at the generation time for each generated specimen should be enough. I do not see the benefit of the proposed method in this setup. This also applies to the TriviaQA experiment.
The algorithm requires an independent calibration set which seems to be very difficult to obtain in practice. In the presented experiments either boils down to something very trivial (single example being the valid one) or relying on another model which itself may be of uncertain quality. Further, I see similar issue with the update and filter functions which seem difficult to formulate reasonable in realistic scenarios. For me these are major limitations of the method which shall be discussed. 

The main text of the paper (section 9) spills over to page 11. As per the call for papers, there is a strict 10 page limit on the main text and the call suggests a desk reject in case of violations of this limit.

### Questions
1. One of the motivations for the method is the possible reliance on human oracle and expenses related to querying it. In the end the experiment use a non-human validation function. Related questions:
- Would not the human oracle make some of the assumptions invalid (e.g. the need for increasing update function)?
- As some point you mention that multiple queries over the same example need to be executed - wouldn't the human validation bring even more noise into the whole process and invalidate some of your probabilistic conclusions?
2. I do not understand equation (6). What level of quantile is this? What is the interpretation of the n-fracion in the right-hand side?
3. Is there a way to independently post-evaluate that the experimental results are really conformal with the $\alpha$ level you were trying to achieve. Or would you need to use your own calibration parameters? If it were possible, this would provide additional useful insight.
4. Please address the concerns mentioned under Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This manuscript introduces a sequential conformal prediction method called SCOPE-Gen. SCOPE-Gen uses a sequential pruning approach to iteratively refine the prediction set, allowing for separate control over each factor in the Markov chain, and demonstrates a significant reduction in the number of admissibility evaluations required during calibration. The method has been experimentally validated in natural language generation and molecular graph extension tasks.

### Strengths
Generally well-written; it’s clear that the manuscript is largely inspired (and adopted) from the setup in Quach et al 2024. Nevertheless, the authors detailed differences to Quach et al 2024 and highlight the efficiency of their method by leveraging sequential factorization.

### Weaknesses
 - (minor) Fig 1 is slightly unclear — the caption should at least include some explanation of \nu, which is not specified until Sec 3

 - Can the author clarify the results in Table 2 of the appendix? It appears that the performance gap between SCOPE and CLM is narrowing - can the authors explain why this might be happening?

### Questions
- Can the author clarify the results in Table 2 of the appendix? It appears that the performance gap between SCOPE and CLM is narrowing - can the authors explain why this might be happening?

### Soundness
2

### Presentation
3

### Contribution
2
