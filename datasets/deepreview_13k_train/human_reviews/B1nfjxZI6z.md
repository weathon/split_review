# Improving real-world sequence design with a simple meta-heuristic for detecting distribution shift

- Decision: Reject
- Scores: 3, 3, 3, 8

## Abstract
Biological sequence design is one of the most impactful areas where model-based optimization is applied. A common scenario involves using a fixed training set to train predictive models, with the goal of designing new sequences that outperform those present in the training data. This by definition results in a distribution shift, where the model is applied to samples that are substantially different from those in the training set (or otherwise they wouldn’t have a chance of being much better). While most MBO methods offer some balancing heuristic to control for false positives, finding the right balance of pushing the design distribution while maintaining model accuracy requires deep knowledge of the algorithm and artful application, limiting successful adoption by practitioners. To tackle this issue, we propose a straightforward meta-algorithm for design practitioners that detects distribution shifts when using any MBO. By doing a real-world sequence design experiment, we show that (1) Real world distribution shift is far more severe than observed in simulated settings, where most MBO algorithms are benchmarked (2) Our approach successfully reduces the adverse effects of distribution shift. We believe this method can significantly improve design quality for sequence design tasks and potentially other domain applications where offline optimization faces harsh distribution shifts.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a method to detect and correct for feedback covariate shift in experimental design (such as protein sequence design), where training data distribution differs from the distribution of the new data candidates generated throughout the process. The method is based on softmax regression for binary classification of the domain, which is employed to discriminate between the training data and the data generated within the feedback loop. The logit score (here OOD score) represents the intensity of the covariate shift. The authors empirically validate their approach on three use-cases: synthetic function, biological simulation, and real-world application of protein sequence design. The domain classifier equipped with the OOD score is able to identify and reduce the distribution shift in the design loop in a real-world application.

### Strengths
The paper presents an application in biology of the method for addressing feedback covariate shift. It is indeed of crucial importance to be able to correct for this shift across many fields with the strong presence of automated experimental design, biology being only of them. The method is very simple to integrate into any existing experimental pipeline, and seems to be performing well in practice.

### Weaknesses
To the best of my knowledge, I believe this way of addressing covariate shift is not novel; the novelty might lie in the aspect of applying this method to *feedback* covariate shift (see for example, https://doi.org/10.7551/mitpress/9780262170055.003.0008, or https://dl.acm.org/doi/10.5555/1577069.1755858, and references therein). Domain classification by means of logistic regression (with or without importance weighting) is one of the widely known methods, hereby just applied to the special case of feedback covariate shift in experimental design. In feedback covariate shift, it is assumed that the distribution of points generated within the feedback loop depends also on the training distribution. The paper lacks a clearer presentation of its methodological contributions, and does not fully allow one to appreciate the usefulness of the method in practice. Comparison with other baselines (e.g., other methods for unsupervised domain adaptation) would further highlight the strengths and weaknesses of the method. The running time of the method was not investigated, i.e., how much of the optimization budget needs to be dedicated to detecting and correcting for shifts in a real-world application. This could be done by comparing the computational overhead of the proposed method to the baseline optimization approach in real-world scenarios. The figures throughout the paper are not necessarily self-explanatory. Furthermore, a more rigorous technical and mathematical notation is missing.

### Questions
Could you please clarify how your approach differs from or improves upon existing methods for addressing covariate shift, particularly in the context of feedback covariate shift in experimental design? It would help to highlight your exact contributions more clearly and position with greater care your approach within related work.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes an out-of-distribution (OOD) classifier to detect distribution shifts, guiding design selection to avoid adversarial results. The authors suggest multiple ways to guide or filter sequence generation based on the predictions of the OOD classifier. The proposed method is tested on three different tasks, including AAV sequence design, using two different search methods, AdaLead and beam search. The experimental results show that the proposed OOD classifier achieves lower regret scores compared to deep ensemble-based OOD detection.

### Strengths
- I agree with the motivation that trained models can be unreliable, and handling distribution shifts is crucial in model-based optimization (MBO).
- The proposed method is straightforward and effective compared to deep ensembles
- Simplicity and ease of implementation

### Weaknesses
 - The novelty of this approach is limited: The idea of OOD classifier is not new, and the way of using the predicted OOD score is not particularly novel neither. OOD score is simply used to filtering out the sample with threshold or range.
- The claim that "the complexity of using MBO algorithms correctly... limits the adoption among practitioners. Selecting a trust region for any search algorithm can be an art rather than a science and risks wasting experimental resources" may be overstated. Several studies have focused on discovering new sequence designs while maintaining close distances to known designs (wild types). For example, proximal exploration (PEX) [1] has made significant progress by effectively balancing the enforcement of in-distribution constraints and exploration in a practical and scientific way. Though they assume multiple query rounds in their original setting, PEX gives competitive results with a single round, which is the same as MBO. Including further discussion for other MBO approaches that consider distribution shift, such as RoMA [2] and BDI [3].

#### Minor comments
- Line 65: expansive → expensive
- Line 71: In this work, propose (there is no subject)
- For me, meta-heuristic sounds improper in this context
- In Appendix E.  Fig Xa, Fig Xb, Fig Xc



### Questions
- From my understanding, the optimization process seems to be conducted iteratively. Does it means multiple query rounds like the setting in AdaLead? If not, please clearly state the difference with AdaLead setting. If yes, the motivation and approach might be improper (even though I agree with the claim that we should carefully handle the unreliable surrogate model for the adversarial samples, as mentioned above), as a key assumption in MBO is that we cannot make additional queries to the black-box function. Allowing additional queries can lead to significant differences in the methodologies used. For instance, we need to explore the unreliable region for the subsequent iterations rather than filtering out these samples.
- Regarding the AAV task, is the surrogate model the same as the one used in AdaLead? If not, I am concerned that the comparison between the OOD classifier and deep ensembles might not be entirely fair. I have checked Appendix A.2, but I am unsure whether the model capacity is sufficient to learn the fitness function of the AAV tasks and, consequently, whether deep ensemble-based OOD detection would be effective with an insufficiently trained surrogate model.
- How many models are used for the deep ensemble?
- What is the meaning of "50 bootstrap data samples" in line 472?
- Additionally, I am curious whether the proposed OOD classifier could benefit search methods that already enforce in-distribution samples, such as PEX.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a binary classification model for detecting out-of-distribution (OOD) samples in the context of offline model-based optimization (MBO). The classification model is trained on a given offline dataset (labeled 0, in-distribution) and a generated dataset (labeled 1, OOD), where the generation algorithm is task-dependent. The learned classification model is used to calculate a score indicating the intensity of the distribution shift. Experiments were conducted in a synthetic problem, a simulated protein structure design, and a real-world Adeno-Associated Virus (AAV) capsid sequence design.

### Strengths
1. The proposed algorithm is straightforward and also easy to implement.
2. The paper was generally easy to understand and follow.
3. The method achieved better results in OOD detection than the uncertainty-based method (deep-ensemble).

### Weaknesses
1. I'm not fully convinced by the proposed method. The paper says in line 921 that $1/p_{tr}(x)$ (where $p_{tr}$ is training distribution) is more suitable for detecting distribution shift. If so, there are several ways to achieve this, e.g., kernel density estimation (KDE) or neural autoregressive density estimation (NADE; [1]). A careful conceptual and experimental comparison with these density estimation methods seems crucial.
2. I'm uncertain how the proposed method "can significantly improve design quality" (line 27). Choosing the right threshold seems critical to effectively balance the exploitation of the surrogate model and the OOD robustness. Moreover, I suspect that the optimal threshold for achieving the best design, regardless of whether a score-based or percentile-based method is used, will vary depending on the specific design task and the distribution of the training dataset. However, there has been limited discussion on threshold selection.
3. Similarly, there is no experimental evidence showing that the proposed algorithm can actually improve design quality. The experiments were only about the ability to detect OOD, specifically in comparison to deep ensembles.
4. The proposed algorithm relies on the MBO algorithm to generate the OOD dataset for classifier training. However, this paper only validates it using a single MBO algorithm, AdaLead, which raises concerns about the method’s versatility and generalizability.
5. A minor point, but the writing could be improved for better readability. For instance, it might be helpful to create a separate 'Preliminaries' section for the content in Sections 2.1 (offline MBO) and 2.2 (distribution shift), allowing the 'Method' section to focus solely on the main contribution. Additionally, the paper is somewhat verbose, particularly in the experiment section. A more concise presentation that highlights the main contributions and insights would strengthen the overall readability.

### Questions
1. (Related to weakness 1) Why should one use the proposed binary classification approach for OOD detection instead of simply approximating $p_{tr}(x)$ using, e.g., KDE or NADE?
2. Similarly, I seems feasible to use the minimum distance between a sample $x$ and samples in the in-distribution dataset $D$—often referred to as "novelty" [2] and easy to compute—as an OOD score. Have you considered this approach? If so, is there a specific reason why the proposed method (the learned binary classifier) might be more effective for OOD detection?
3. Could you explain why the proposed algorithm is called a "meta-algorithm"?
4. Recent works have attempted to inject structural biases into surrogate models to improve OOD generalization in offline MBO settings [3, 4]. It would be interesting to explore how these structurally-biased surrogate models could synergize with the proposed OOD detection method, potentially opening up future research directions.

[2] Kim, Minsu, et al. "Bootstrapped training of score-conditioned generator for offline design of biological sequences." NeurIPS (2024).  
[3] Grudzien, Kuba, et al. "Functional Graphical Models: Structure Enables Offline Data-Driven Optimization." AISTATS (2024).  
[4] Grudzien, Kuba, et al. "Cliqueformer: Model-Based Optimization with Structured Transformers." arXiv:2410.13106 (2024).

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a method for detecting distribution shifts in machine learning-guided biological sequence design design, specifically addressing model-based optimization (MBO) prediction reliability when exploring regions distant from training data, identifying distribution shift when it occurs. The work introduces:

1. A binary classifier approach to detect out-of-distribution samples in MBO
2. Empirical validation through AAV capsid engineering experiments
3. Comparison between simulation benchmarks and real-world distribution shift severity
4. A framework for identifying unreliable predictions during sequence optimization

### Strengths
1. Validation through wet-lab experiments, extending beyond simulation-based evaluation (which itself was also thorough)
2. Straightforward implementation of the proposed method
3. Demonstration that simulation benchmarks may not capture real-world distribution shift challenges
4. Comprehensive ablation studies and baseline comparisons
5. Technical foundation in density ratio estimation literature
6. Direct applicability to real-world MBO applications in biological sequence design

### Weaknesses
1. Limited analysis of predictor architecture and training choices' effects on distribution shift detection. Understanding the method's robustness across different model choices would strengthen the results. Specifically, the paper does not explore how the capacity of the binary classifier, the choice of activation functions, or the optimization algorithm used during training might impact its ability to accurately estimate density ratios and thus detect OOD samples. For instance, a shallow network might underfit the density ratio, leading to missed OOD samples, while an overly complex network could overfit, resulting in false positives. The paper should include experiments that systematically vary these architectural and training parameters to assess the sensitivity of the OOD detection performance.
2. While the method effectively identifies OOD samples, the paper provides limited guidance on what to do with these flagged sequences beyond excluding them. The practical impact would be enhanced by discussing mitigation strategies such as active learning, model retraining, or ways to incorporate OOD scores into exploration. Simply discarding OOD samples may lead to inefficient exploration of the sequence space, especially if the OOD regions contain potentially valuable sequences. The paper should discuss strategies for leveraging the information gained from OOD detection to guide further optimization, such as targeted sampling in regions near the OOD boundary or using the OOD scores to weight the contribution of different sequences during model retraining.
3. The theoretical foundations could benefit from deeper analysis, particularly regarding how classifier architecture affects density ratio estimation accuracy and potential bounds on detection performance under various distribution shift scenarios. The paper does not delve into the theoretical underpinnings of how the binary classifier approximates the density ratio, nor does it explore the conditions under which this approximation is accurate. A more rigorous analysis, perhaps drawing from the literature on density ratio estimation, would be beneficial. For example, the paper could discuss how the choice of classifier architecture relates to the bias-variance tradeoff in density ratio estimation and how this affects the detection performance under different types of distribution shifts.

### Questions
1. Have you explored strategies for using the OOD scores beyond binary accept/reject decisions? Could the scores be incorporated into the optimization objective to guide exploration?
2. How sensitive is the method to surrogate model architecture and training procedure choice? Additional experiments testing robustness across architectures would be informative.
3. Could you elaborate on potential approaches to leverage the OOD scores for active learning or model refinement when significant distribution shift is detected?

### Soundness
4

### Presentation
3

### Contribution
3
