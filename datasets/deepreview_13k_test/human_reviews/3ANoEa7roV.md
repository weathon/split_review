# Systematic Assessment of Tabular Data Synthesis

- Decision: Reject
- Scores: 8, 3, 6, 6, 6, 3, 6

## Abstract
Data synthesis has been advocated as an important approach for utilizing data while protecting data privacy. A large number of tabular data synthesis algorithms (which we call synthesizers) have been proposed.  Some synthesizers satisfy Differential Privacy, while others aim to provide privacy in a heuristic fashion. A comprehensive understanding of the strengths and weaknesses of these synthesizers remains elusive due to drawbacks in evaluation metrics and missing head-to-head comparisons of newly developed synthesizers that take advantage of diffusion models and large language models with state-of-the-art marginal-based synthesizers.  

In this paper, we present a systematic evaluation framework for assessing tabular data synthesis algorithms.  Specifically, we examine and critique existing evaluation metrics, and introduce a set of new metrics in terms of fidelity, privacy, and utility to address their limitations.  Based on the proposed metrics, we also devise a unified objective for tuning, which can consistently improve the quality of synthetic data for all methods. We conducted extensive evaluations of 8 different types of synthesizers on 12 real-world datasets and identified some interesting findings, which offer new directions for privacy-preserving data synthesis.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper reviews the current state of tabular data synthesis, an approach that balances data utility with privacy. Despite numerous proposed algorithms, a comprehensive comparison of their performance is lacking due to the absence of standardized evaluation metrics. The authors critique existing metrics and propose new ones focusing on fidelity, privacy, and utility. They also introduce a unified tuning objective that enhances the quality of synthetic data across different methods. Extensive evaluations on eight synthesizers and twelve datasets reveal insights that guide future research on privacy-preserving data synthesis.

### Strengths
+. The authors introduced a new fidelity metric based on Wasserstein distance to evaluate diverse data types, addressing the heterogeneity and high dimensionality of tabular data.
+. The authors introduced the membership disclosure score as a novel privacy metric effectively addresses the limitations of existing privacy metrics and enhances the understanding of privacy risks in data synthesis.

### Weaknesses
-. The related work section of the paper is relatively weak and should be systematically organized to provide a more comprehensive introduction of relevant studies.
-. My major concern is whether the synthesized tabular data can maintain usability for more complex downstream applications. In other words, is this usability specific to certain downstream tasks, or can it apply to any downstream task?

### Questions
How can we evaluate whether the synthesized tabular data has general applicability for downstream tasks?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates the performance of tabular data synthesizers w.r.t. three metrics, fidelity, privacy, and utility. The authors conduct extensive experiments to compare SOTA tabular data synthesizers.

### Strengths
S1. Extensive experiments are conducted to examine the performance of each tabular data synthesizer w.r.t. the three metrics adopted in this paper.

### Weaknesses
W1. The technical depth of this paper is limited. All the metrics are already proposed by existing work and the authors mainly conduct an empirical comparison among tabular data synthesizers. The novelty of this paper is not clear.

W2. This paper discusses tabular data synthesizers. However, it seems to me that the three metrics also fit general data synthesizers. What is the unique feature of tabular data that requires the adoption of the three metrics in model evaluation? If the authors cannot elaborate on the connection between the three metrics and tabular data, the motivation for adopting the three metrics will be unclear.

W3. Since the authors adopt three metrics, the tabular data synthesis task becomes a multi-objective optimization problem. What are the relationships among the three objectives? Do they contradict each other? Is it possible to maximize the model performance w.r.t. all three metrics? The authors should provide an in-depth analysis of these issues.

W4. For fidelity, why only consider the marginal distribution (definition 1)? If we only consider marginal distributions, the complex relationships among columns in a table may be ignored. Note that for tabular data, we may have some (approximate) functional dependencies among columns, which are very important for data integrity and challenging to capture for tabular data synthesizers.

### Questions
W1-W4

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper offers an opinionated selection of methods to evaluate synthetic data generation methods for tabular data. In particular, they select metrics to evaluate fidelity (Wasserstein distance), empirical privacy (they introduce the Membership Disclosure Score), and utility (via Machine Learning Affinity and QueryError). The paper goes through a very extensive set of experiments, where it compares synthesizers based on these metrics.

### Strengths
- Well-written, and evaluates many methods against many datasets
- Wasserstein distance seems like an appropriate choice for measuring fidelity, and it is adequately justified; similarly, MLA and QueryError seem good measures for utility.
- The paper offers some interesting takeaways: statistical methods work best for privacy applications, while diffusion models offer good fidelity.

### Weaknesses
- The proposed privacy metric, MDS, has critical flaws that make it unsuitable (and, potentially, misleading) for evaluating privacy. [See below]
- The use of Wasserstein distance for synthesizer isn't exactly new; for example, Singh et al. [1] used it in their optimization objective. Similarly, as argued below, MLA is incremental.
- Besides evaluating synthesizers with an opinionated (and well-justified, in some cases) approach, this paper feels quite redundant and it's unclear what is the "delta" from prior work. From a quick search, there's dozens of synthetic data evaluation frameworks [2-6], and it's unclear why a new one is needed. I appreciated your comparisons between metrics, provided in the appendix, but the main question is: can you empirically demonstrate that one would be wrong in using one of the prior frameworks, and that they should use yours instead?

[1] Singh Walia, Manhar. "Synthetic Data Generation Using Wasserstein Conditional Gans With Gradient Penalty (WCGANS-GP)." (2020).

[2] https://github.com/schneiderkamplab/syntheval

[3] https://github.com/Vicomtech/STDG-evaluation-metrics?tab=readme-ov-file

[4] Qian, Zhaozhi, Rob Davis, and Mihaela van der Schaar. "Synthcity: a benchmark framework for diverse use cases of tabular synthetic data." _Advances in Neural Information Processing Systems_ 36 (2024).

[5] Livieris, Ioannis E., et al. "An evaluation framework for synthetic data generation models." _IFIP International Conference on Artificial Intelligence Applications and Innovations_. Cham: Springer Nature Switzerland, 2024.

[6] McLachlan, Scott, et al. "Realistic synthetic data generation: The ATEN framework." _Biomedical Engineering Systems and Technologies: 11th International Joint Conference, BIOSTEC 2018, Funchal, Madeira, Portugal, January 19–21, 2018, Revised Selected Papers 11_. Springer International Publishing, 2019.

### Questions
**MDS**

1) Def 2 isn't well defined:
- H is supposedly sampled "at random" from the dataset, but the distribution of this sampling isn't defined.
- please replace the expectation's subscript with $H \subset D \setminus \{x\}$, or clarify that the expression $x\in H$ is an additional requirement to $H \subset D$.
- what is $\mathcal{M}$ in this definition? Can it be _any_ distance? Any particular property it should have?

2) I have several reasons to think that the membership disclosure score (MDS), as defined in Eq. 8, is a very poor choice:
- It's important to note that MDS, as defined in Eq. 8, is just an estimate, and it gives no formal guarantees. For a privacy metric, this is troublesome, and I highlight one counterexample to its reliability below.
- Here's an example where MDS suggests high privacy, but where an attack is trivial. Consider a synthesizer $s(\cdot)$ that maps a point as follows $s: x \mapsto -x$ . It's trivial to see how an attacker can achieve 100% accuracy. Yet, suppose the nearest neighbor to $x$ in the real dataset is $x+\varepsilon$. Then MDS would be proportional to $|d(x, s(x)) - d(x, s(x+\varepsilon))|$, which can be made arbitrarily small with $\varepsilon$. Hence MDS is a metric which can be tricked, and this makes it unsuitable for any serious privacy application. NOTE: I noted that in Appendix C you acknowledge possible drawbacks, but seem to dismiss them. Unfortunately, these are _critical_ issues even for less contrived synthesizers: for example, privacy metrics are routinely used to ensure that synthesizer implementations are bug-free, and this is certainly something that MDS cannot be trusted to do. 
- MDS' value is (potentially) unbounded, and it's unclear how its value can be matched to the risk of successful attack. Note that the two main ways of measuring privacy in this context both offer this: 1) DP (its parameters can be mathematically matched to the risk of MIA) and of course 2) running a (potentially worst-case) MIA attack directly tells us this.
- Finally, an important drawback is that MDS doesn't really capture the worst-case: it takes the average (expectation) across multiple runs of the generator. This may be fine, but it should be carefully motivated.

I strongly recommend using a conventional metric (e.g., risk against state of the art MIA attack), which is empirical (similarly to MDS), but provides a better interpretation and it is well-understood by the security community.
Together with this MIA metric, I recommend also including a metric with theoretical guarantees; DP parameters $(\varepsilon, \delta)$ would be the most standard choice for this.

**Utility**

The authors introduce "Machine Learning Affinity" (MLA) as a metric, which is defined as the average difference across various models of the performance of a model that uses training or synthetic data. This feels incremental: most works on synthetic data generation already look at the difference between the performance (e.g., (Jordon et al., 2021)), and looking at the average across models looks like the natural next-step. I would recommend downtuning the claim that this metric is novel.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors present an evaluation framework called SynMeter to evaluate generative modeling approaches for tabular data across 3 different dimensions: i) fidelity, ii) utility, and iii) privacy. The authors introduce reasonable metrics to evaluate algorithms/datasets along these 3 dimensions. The authors then evaluate several SOTA tabular data generation algorithms using SynMeter.

### Strengths
1) The paper is very thorough. Given the extensive appendix, I imagine it has gone through one or more review cycles before. Nevertheless, the authors clearly have discussed in details a lot of very reasonable concerns about their approach, which I quite appreciate. 
2) The paper is quite topical and there aren't that many similar papers out there.

### Weaknesses
1) Presentation: 
a) The authors try to cram in too many things into the paper. All figures are too tiny. I recommend moving some of the figures to the appendix if make the remaining ones bigger. 
b) The appendix needs better structure. I'd recommend moving the experiment details ahead of discussion of limitations. 
2) Technical points: 
a) The MDS metric is designed for the synthesis algorithm whereas others are for a specific synthetic dataset. This is a major inconsistency. 
b) MDS only captures privacy against MIA attacks. This is not  unreasonable but please spend a few lines explaining why you chose to only focus on MIAs?
c) One of the references [1] is quite similar to this paper in scope but uses slightly different metrics. Given the similarity, I would love to see the authors discuss the key differences between the papers and areas of novelty. 



[1] Qian, Zhaozhi, Rob Davis, and Mihaela van der Schaar. "Synthcity: a benchmark framework for diverse use cases of tabular synthetic data." Advances in Neural Information Processing Systems 36 (2024).

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper critically examines the limitations of existing evaluation metrics and introduces new metrics for fidelity, privacy, and utility, establishing a comprehensive framework for assessing tabular data synthesis. Additionally, it proposes an integrated tuning objective that consistently optimizes data quality across different synthesizers. The study demonstrates that recent advancements in generative models significantly enhance tabular data synthesis performance while also highlighting key challenges, such as privacy risks and performance disparities among synthesizers.

### Strengths
1. The paper effectively identifies and addresses the limitations of existing metrics for fidelity, privacy, and utility, highlighting the need for the proposed metrics.
2. By introducing fidelity, privacy, and utility as core evaluation dimensions, the paper offers a well-rounded framework for assessing synthetic data quality.
3. The proposed metrics are thoroughly validated through extensive experiments on a large number of datasets, demonstrating their robustness and applicability in various contexts.

### Weaknesses
1. There is a lack of experimental comparison between the proposed fidelity and utility metrics and existing metrics. For example, including case studies where the proposed metrics and existing ones yield different evaluations on the same model could have strengthened the paper's claim of improved fidelity and utility assessments. 
2. While the proposed privacy metric is an innovative approach, its reliance on numerous shadow models and synthetic datasets could lead to high computational costs. This complexity might render the metric impractical for large datasets, as the evaluation process could require substantial time and resources, limiting its usability in real-world applications.

### Questions
Since the tuning objective includes the same metrics used for evaluation, isn’t the observed performance improvement in Table 1 simply an expected result? Can this performance improvement truly be considered a reflection of the tuning objective’s effectiveness?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a new framework, called SynMeter, to assess (tabular) synthetic data generators. They focus on three dimensions: 

- Fidelity: 
	- Authors argue the need for a faithful and universal metric
	- They propose a Wasserstein distance-based metric to evaluate complex, high-dimensional tabular data distributions
- Privacy
	- Authors argue syntactic privacy scores to not be adequate
	- Authors argue that existing MIAs are ineffective, as they are not well understood and no MIA is effective against all synthesizers. 
	- They propose a new metric called membership disclosure. 
- Utility
	- Authors state that the traditionally used ML efficacy is not adequate, as they argue that there is no consensus on which evaluator should be used. 
		○ They propose two new metrics: ML affinity and query error. 

The paper then includes a holistic tuning objective as a combination of all metrics, to be used for hyperparameter selection. 

Finally, the paper includes comprehensive experiments evaluating all metric across datasets and generators.

### Strengths
1. Comprehensively evaluating synthetic data generators is an important problem, and the paper provides a systematic, multi-dimensional evaluation framework to do so. 
2. The paper includes considers many datasets and synthetic data generators, and comparing them across metrics is valuable for the research domain as a whole.
3. Proposes a way to pick hyperparameters across a multiple dimensions. 
4. Authors make the framework publicly available as a tool for people generating synthetic data

### Weaknesses
While I understand the need for a holistic and widely agreed upon evaluation framework for synthetic data  generators, as a reader, I am not convinced that the metrics proposed by the authors are novel, or particularly better than previously proposed ones. I elaborate on each of the dimensions: 

**1. Fidelity.**

While I find the notion of using Wasserstein distance to compute fidelity interesting, I remain to be convinced why this would be better than existing methods. 
- Could you come up with an experimental setup and results which would compellingly show why the Wasserstein-based fidelity metric is strictly better than other deployed methods?

**2. Privacy.**

 I agree with the authors on the shortcomings of syntactic metrics, and like the example given for DCR. However:
- I do not follow the arguments made for why MIAs are not sufficient. 
	- Why are MIAs against tabular data synthesis not well understood? 
	- There indeed does not exist one MIA effective across all synthesizers, but this does not seem like a justification why MIAs are not useful? The ineffectiveness of the MIA might also just reflect limited privacy leakage?  
- I do not understand what the difference is between the MDS metric and an MIA. If I understand it correctly, you are building a shadow model setup to then compute an MIA scoring function (which you then not evaluate as an MIA). You then pick the record for which you get the best distinction for this scoring function.  To me this basically comes down to compute MIA performance for all records, and use the highest MIA performance as the privacy metric.  
	- How does this resolve your previously raised concerns regarding MIAs? 
	- Moreover, with this, it is not clear whether this is the state-of-the-art MIA. 
- Finally, in this entire discussion, I believe authors fail to mention (and implement) important related work. Houssiau et al [1] propose a new MIA which beats the one proposed by Stadler et al, and Meeus et al [2] propose a principled way to identify most at-risk records. 

**3. Utility.**

I agree with the authors that there is no consensus in the literature on which metric should be used to evaluate the utility of the synthetic data. My thoughts:
	- While the exact formulation of the MLA score is, at least to my knowledge, new, I believe its novelty to be very limited. For instance, Stadler et al (in Sec. 6.3) measure utility as a decrease in ML accuracy of a model trained on real compared to a model trained on synthetic data. The only difference with the MLA metric would be the averaging across ML models and the normalization. 
	- Similarly, the query error seems very similar to the k-way marginals fidelity approach, which has also been studied in for instance Annamalai et al. [3] 
	- Could authors clarify why the query error should be part of the utility and not part of the fidelity evaluation? 

**References**

[1] Houssiau, F., Jordon, J., Cohen, S. N., Daniel, O., Elliott, A., Geddes, J., ... & Szpruch, L. (2022). Tapas: a toolbox for adversarial privacy auditing of synthetic data. arXiv preprint arXiv:2211.06550.

[2] Meeus, M., Guepin, F., Creţu, A. M., & de Montjoye, Y. A. (2023, September). Achilles’ heels: vulnerable record identification in synthetic data publishing. In European Symposium on Research in Computer Security (pp. 380-399). Cham: Springer Nature Switzerland.

[3] Annamalai, M. S. M. S., Gadotti, A., & Rocher, L. (2024). A linear reconstruction approach for attribute inference attacks against synthetic data.

### Questions
(also see weaknesses)

- Could you come up with an experimental setup and results which would compellingly show why the Wasserstein-based fidelity metric is strictly better than other deployed methods?
- Why are MIAs against tabular data synthesis not well understood? 
- There indeed does not exist one MIA effective across all synthesizers, but this does not seem like a justification why MIAs are not useful? The ineffectiveness of the MIA might also just reflect little privacy leakage?  
- How does the MDS metric resolve your previously raised concerns regarding MIAs? To my understanding, you are in fact proposing a new MIA, but not evaluating it as such. 
- Could you implement the MIA developed by Houssiau et al, and explain why the MDS metric is superior to compute the MIA performance for records identified by Meeus et al? 
- Could authors clarify why the query error should be part of the utility and not part of the fidelity evaluation?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 7

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the problem of evaluating tabular synthetic data generation techniques. To this end, it critiques existing metrics for fidelity, privacy, and utility, and proposes new ones. Then, it evaluates these metrics on a set of 12 datasets. The authors find that diffusion models generally outperform other model types in terms of utility and fidelity, whereas statistical methods are better suited for privacy. They also evaluate differentially-private synthesizers and evaluate the effect of DP budget.

### Strengths
This paper is interesting, I think these kinds of benchmarking studies can be very useful. 

The paper tackles an important problem, there is a lot of interest in generating synthetic tabular data right now. I thought some of the metrics were interesting, particularly query error, which seems to address a common use case for synthetic data. I appreciated that the MDS score was taken as a maximum over x in D, in line with best practices in the membership inference literature. 

The head-to-head comparison between models is very practically useful, and could have real-world impact.

### Weaknesses
I’m a little worried that the level of the technical contribution and the findings may not rise to the level of a top-tier conference. This is particularly true given that there exist other surveys on the quality of synthetic data generators. 

1)	I don’t understand why the Wasserstein metric makes sense as a fidelity metric for categorical variables. You have defined the cost matrix as infinite between classes. So how can you find a meaningful transport map? This doesn’t seem like the right metric for categorical variables. By the way, Wasserstein distance has already been used as a fidelity metric for synthetic data over a metric space (e.g., CTAB-GAN+ (Zhao et al), DoppelGANger (Lin et al)), with total variation distance being used for categorial variables. 

2)	The paper seems not to mention a number of related works, including:

-	On the Inadequacy of Similarity-based Privacy Metrics: Reconstruction Attacks against Truly Anonymous Synthetic Data (Ganev and De Cristofaro)
-	On the Quality of Synthetic Generated Tabular Data (Espinosa and Figueira)
-	A universal metric for the evaluation of synthetic tabular data (Chundawat et al)

For a survey paper, these omissions worried me--I’m concerned that there may be others I’m not aware of. I would definitely want to see a more in-depth literature review. How does your work relate to these, particularly the surveys on synthetic tabular data? What does your survey add to the discussion? 

3)	The evaluation seems incomplete in terms of baselines. I thought there should at least be a tabular transformer (e.g., RealTabFormer or a successor) in the mix. GReaT is a transformer, but the tokenization is not really tailored to tabular data, and RealTabFormer is (a) more widely used in practice, and (b) not compared against in the GReaT paper. Also, the tables in the evaluation are illegible—it would be nice to make them bigger.

### Questions
1) How does your work relate to existing surveys on tabular synthetic data?

2) Why is Wasserstein distance an appropriate metric for categorical fields? 

3) How do tabular transformers like RealTabFormer compare to the baselines you have evaluated?

### Soundness
2

### Presentation
3

### Contribution
2
