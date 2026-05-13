# Data Distillation for extrapolative protein design through exact preference optimization

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
The goal of protein design typically involves increasing fitness (extrapolating) beyond what is seen during training (e.g., towards higher stability, stronger binding affinity, etc.). State-of-the-art methods assume that one can safely steer proteins towards such extrapolated regions by learning from pairs alone. We hypothesize that noisy training pairs are not sufficiently informative to capture the fitness gradient and that models learned from pairs specifically may fail to capture three-way relations important for search, e.g., how two alternatives fair relative to a seed. Building on the success of preference alignment models in large language models, we introduce a progressive search method for extrapolative protein design by directly distilling into the model relevant triplet relations. We evaluated our model's performance in designing AAV and GFP proteins and demonstrated that the proposed framework significantly improves effectiveness in extrapolation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this work, preference learning on triplets of sequences has been proposed to improve the performance of prior edit-based methods for the task of protein design. In prior edit-based method(s), the conditional generative model is only trained on pairs of sequences where the likelihood is maximized for generating the sequence with higher property conditioned on the sequence with lower property. However, faced with three (or higher)-way relationships, the conditional generation is not guaranteed to move the optimization towards the sequence with the highest property. To mitigate this issue, the set(s) of sequence triplets are designed to further optimize the conditional generative model through preference learning losses.

Protein optimization tasks (four in total) with varying degree of extrapolation difficulty (designed by prior work) have been used to demonstrate the effectiveness of preference learning on sequential design of proteins. The proposed method works better than prior protein design approaches in terms of extrapolation and finding higher fitness samples in three out of the four design tasks.

### Strengths
1. Demonstrating the impact of preference learning in extrapolative generative protein design.

2. Nice ablation study on the impact of a) the strategies/criteria to create dataset of triplet sequences for preference learning, b) the type of preference learning approach adopted.

### Weaknesses
1. The authors have specified a separate category of methods for extrapolation, whereas by the definition of the paper in section 3.1, almost all the methods for protein optimization are doing extrapolation. They are all searching for sequences not existing in the train set that have properties beyond the range of training samples. The extent of extrapolation may differ from one work to another as discussed by  [1] and [2] that introduces the concept of “separation”, which can be seen as the extent of extrapolation, and the challenges associated with that in protein optimization tasks.

2. Given that this work is for protein optimization, the related work section should contain a category for methods that perform optimization in the latent space which could be guided by property values as well. The famous work of [3] is one of these methods which has been included and discussed in many protein optimization benchmarks. Also, the recent method of [2] (published at ICLR 2024), encodes the _preference_ of sample generation into the continuous latent space of the generative model. This makes the optimization robust to the extent of “separation", i.e., extrapolation, in the design tasks.

### Questions
1. How were the pairs with true scores generated? Has the same binning of fitness been used to generate pairs as well as the triplets? Were the pairs taken from two consecutive bins?
In section 3.3 there is no mention of using the training pairs with their original scores, while it is mentioned in section 4.3 (first paragraph). Make the two consistent to avoid confusion.

2. Why are the triplets generated from consecutive bins? Is there an underlying assumption that the sequences coming from two adjacent bins are more similar than the ones further apart? The fitness landscape of protein does not necessarily behave like this. The fitness can have sharp variations in a local neighborhood of sequence space.

3. How is a small meaningful improvement of score determined for the perturbed seed sequence (section 3.3, line 163). I am assuming that having a small improvement is the requirement of the conditional modelling used. How is a meaningful improvement identified? Also, how different can a perturbed sequence look from the seed sequence? Is there any restriction on the dissimilarity between the perturbed and seed sequence in the sequence space?

4. In the main text you should clarify what $r_\phi$ (reward) stands for.

5. Please explain top-k and top-p sampling and the role of temperature in the inference.

6. Is the default operating mode of EXO with the “All” triplet creation (Table 2)?

7. (Minor). Change 2023 to 2024 in the citation for,
Improving protein optimization with smoothed fitness landscapes. In The Twelfth International Conference on Learning Representations, 2023.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In order to optimize a certain protein of interest, some preliminary source of supervised data is collected around the property of interest and some mutational landscape of that protein. In the effort to achieve a higher functional capability than those derived from the supervised set, protein designers will propose, express, and assay new designs in hopes that they can achieve more fit proteins than their initial candidate pool. To that end, this work uses some of the reward modeling techniques from preference optimization literature to improve a conditional protein generation model’s ability to extrapolate to unseen fitness values. It argues to use the exact preference optimization (EXO) framework with a mixture of hard negatives to improve the generative model’s capability to sample fit sequences.

To assess the contribution of different components, it ablates the choice of preference optimization method and triplet generation techniques. In addition, it studies the performance of methods that explicitly use and do not use the scorer during sampling.

### Strengths
The model’s intervention is well motivated and deserves recognition for its simplicity. Preference optimization is easy to implement, and the results against non-scoring guided samplers make this an intervention that’s likely to be adopted. I can see this becoming a well adopted strategy for these reasons.

In introducing the intervention, the work does a good job in beginning to analyze what alterations are causal in increased performance. The experiments with respect to triplet curation and reward methods are well thought out and thorough. Each study is run with 5 replicates to ensure that performance is not a result of randomness. In addition, Figure 2 is quite compelling towards understanding EXO’s performance compared to other alternatives, while also illuminating the core goal of the project.

### Weaknesses
As the paper notes, all experiments are derived from a blending of wet-lab data and estimated wet-lab experimental outcomes. As such, there might be a mismatch between the benchmark outcomes and real world outcomes. This should not be counted against the work too much, but kept in the back of readers minds.

The two major areas for improvement in this work lie in elements of clarity and the derivation of baselines. Overall, the work asks the right questions, but the exposition in how the answers are derived leaves out critical details that makes it hard to have conviction in the whole outcomes.

On the note of clarity, the work finds certain key components unexplained. In particular, while dedicating an entire subsection to the role of sampling with a scorer, the details of how this performs are left unstated. Specifically, what is the mechanism for incorporating the scorer's output into the sampling process? Is it a direct probability adjustment, or is there a more complex iterative refinement? Furthermore, the exact reasoning behind certain choices is left unsaid: why does sampling with a scorer have a different temperature and what is the maxim used to select this? As a minor nitpick, on line 284, the mentioning of $\beta=0.1$ should clarify a preference loss $\beta$ as it’s confusable with AdamW’s two separate $\beta$s.

My largest source of concern in the work centers around how baselines are evaluated and the steps leading to a hyperparameter selection. Looking at Table 11, hyperparameter choice can mean the difference between a SoTA performance  and unusable model. With this in mind, and the explanations towards those chosen for the preference models, the leading question then becomes how sensitive are the baseline models to hyperparameter selection? The text does not explain how they were optimized. It is crucial to understand if the reported baseline performance is the result of a thorough search or if it reflects a suboptimal configuration. The lack of detail makes it difficult to assess the fairness of the comparison.

Even for certain choices in the paper, the statements: “[b]ased on the results shown in Figure 21 and Table 10, $\beta = 0.1$ is performing well” and “[s]imilarly, based on Figure 22 and Table 11, $\tau=0.7$ is performing well” led to confusion amongst what “performing well” means. Additionally, in what order were $\beta$ and $\tau$ chosen? Even if not a hard and fast rule it would aid the reader to understand which metrics were being balanced to make this decision. It is unclear if these values were chosen based on a single metric or a combination, and what the trade-offs were.

Lastly, a more minor comment, the claims around Figure 3 should be hedged to take into account the stochastic nature of t-SNE and the relationships that they may imply. Both panels of the figure are challenging to read from the choice in symbols due to small size. It’s challenging to draw the same conclusion as the paper about the “supports by unseen ground truth extrapolation sequences.” This feedback seems more splitting hairs about a qualitative study so I don’t think it’s a strong critique, rather room for the wording to get a little qualification.

### Questions
* How is the sampling with scorer guidance performed?
* In what order were $\beta$ and $\tau$ determined?
* What choices went into the selection of hyperparameters for the baseline models?
* How does performance of the baseline models change when benchmarked with the same attention as the proposed model?

Because of the simplicity, this algorithm seems like an attractive solution for protein designers, but still has room to grow towards evaluation. To clarify, it does not need uniformly SoTA results to merit publication, rather reproducible experimental parameters to give confidence in performance differences. If work evolves to address the above questions, I’d happily raise my score.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a data distillation method focused on extrapolative protein design by applying triplet-based preference optimization. The approach, termed Exact Preference Optimization (EXO), aims to improve the generation of protein sequences with fitness values that exceed those observed during training. By aligning model training with structured triplet preferences, the authors seek to direct the model toward higher-fitness extrapolation regions. Performance is evaluated on Green Fluorescent Proteins (GFP) and Adeno-Associated Virus (AAV) datasets, with results suggesting improvements over existing methods in metrics such as extrapolation rate and top-100 fitness.

### Strengths
1. The method provides a unique approach to data distillation for extrapolative tasks, using triplet preferences instead of traditional pairwise comparisons. This formulation may better approximate the gradient direction toward higher fitness values, which is often challenging in extrapolative settings.

2. The paper includes benchmark results against several existing methods, both scorer-based and non-scorer-based, which helps to establish a comparative baseline for their approach. The presented improvements in extrapolation metrics provide an indication that the model is capturing some aspects of fitness not fully addressed by baseline methods.

3. Evaluation across multiple dimensions, including extrapolation rate and diversity among top sequences, gives a broader perspective on how the model navigates the trade-off between exploration and exploitation. This helps to contextualize the method’s potential in extrapolative design, though the gains remain somewhat dataset-specific.

4. Ablation studies on different strategies for preference data construction are included, offering insights into the model’s sensitivity to triplet selection and shedding light on the specific design choices that contribute to observed performance improvements.

### Weaknesses
1. Generating triplet preferences, particularly when using scorer-based distillation, is computationally intensive and may limit the scalability of this method in practice. The reliance on costly preference data creation steps could hinder its application to larger datasets or more varied protein types. Specifically, the computational cost of generating a single triplet using scorer-based distillation is a significant bottleneck, requiring substantial resources and time, which makes the method impractical for large-scale protein design projects. This limitation is further exacerbated by the need to generate a large number of triplets to effectively train the model, making the overall process very resource-intensive.

2. The paper’s evaluation is confined to GFP and AAV datasets. While they are common in the field, they may not fully represent the diversity of protein design challenges. The extent to which the method generalizes across other types of proteins remains unclear, and additional benchmark results would strengthen claims. The fitness landscapes of GFP and AAV are relatively well-studied, and the method's performance on these datasets may not be indicative of its performance on proteins with more complex or rugged fitness landscapes. The lack of evaluation on diverse protein families limits the generalizability of the findings.

3. The approach relies heavily on in-silico evaluators that are trained on subsets of the data, which could contain biases and limit the evaluator’s ability to accurately assess extrapolative performance. The model’s extrapolative capability, therefore, may not fully translate to real-world scenarios without further validation, such as wet-lab testing. This dependence on in-silico metrics calls into question the practical value of the observed improvements. The in-silico evaluators, trained on a subset of the data, may not accurately reflect the true fitness landscape, especially in extrapolative regions. This discrepancy between in-silico and in-vivo fitness could lead to over-optimistic results that do not translate to real-world applications. The lack of wet-lab validation further compounds this issue, as the true performance of the designed proteins remains uncertain.

### Questions
1. The triplet generation process, especially when involving scorer-based distillation, appears computationally intensive. Could the authors provide more detail on the computational requirements for this step? Additionally, how would the method scale to larger datasets or to proteins with significantly different characteristics?

2. The results are presented for GFP and AAV datasets. To what extent do authors believe the method could generalize to other proteins, especially those with less predictable fitness landscapes? Have the authors considered additional datasets, or are there plans to test the model on other types of proteins?

3. The ablation studies show some performance sensitivity to triplet dataset construction. Could the authors elaborate on the specific criteria used to select the triplets, and whether the approach is robust to different triplet selection methods? Additionally, how dependent is the performance on the accuracy of the scorer used in the distillation process?

4. The diversity metric suggests some degree of balance between exploration and exploitation, but it’s unclear how this affects overall model performance. Could the author clarify how the model’s exploration-exploitation balance was tuned or controlled, and how this may impact its ability to generalize in truly extrapolative regions?

### Soundness
3

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
3

### Summary
This paper addresses the problem of designing novel protein sequences with fitness values beyond those training ones. The paper distills triplet relationships into a generative model using preference alignment to better capture the fitness gradient than alternative pair-based approaches. This model is validated on AAV and GFP and outperforms state-of-the-art scorer-based and non-scorer-based baselines in extrapolation tasks.

### Strengths
Overall this paper is a valuable contribution to the field.
* The problem of designing proteins with fitness value beyond the training range is an important problem and challenging in protein design e.g. lead optimization; the proposed work has high practical value.
* The proposed approach is well-motivated; the use of triplet-information with preference optimization for protein design makes a lot of sense and is (to my knowledge) new. The analysis of the importance of using difficult triplets is insightful. The experimental validation is thorough (including ablation studies) and shows that the proposed model outperforms alternatives in the extrapolation regime.

### Weaknesses
 * The preference optimization relies on a scorer function to define the triplets; in real-world setting, training such scorers is difficult and the scorer is often used in out-of-distribution settings where it does not generalize well. Adding some discussion on this topic would be valuable to the paper as it is not discussed to avoid settings where the proposed preference optimization would degrade the base pairwise model. In particular, could the authors explain how robust is the preference fine tuning model to noisy labels? How to avoid pathological cases where difficult triplets are defined by an imperfect scorer ? 
* The presentation is at times confusing and difficult to understand (c.f. clarifying question).

### Questions
* Some parts of this paper are dense and difficult to read; in particular the definition of triplets (defined in different parts of the paper in sections 3.4; 4.3 and 6.1). W.r.t. scorer distillation, what is defined as a hard triplet ranking wise (for the vanilla version, hardness is defined by the local editor) ? The term "scorer distillation" is confusing (if I understood correctly the vanilla version also uses a scorer).
* How important is the mask infilling step ? How frequently are the mask infilled samples represented in the challenging triplets (where the editor does not capture the right fitness ordering) ?


====Post rebuttal====
I thank the authors for the rebuttal; I recommend acceptance.

### Soundness
3

### Presentation
3

### Contribution
3
