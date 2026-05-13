# Discrimination-free Pricing with Privatized Sensitive Attributes

- Decision: Reject
- Scores: 5, 6, 6

## Abstract
Fairness has emerged as a critical consideration in the landscape of machine learning algorithms, particularly as AI continue to transform decision-making across societal domains. To ensure that these algorithms are free from bias and do not discriminate against individuals based on sensitive attributes such as gender and race,  the field of algorithmic biasness has introduced various fairness concepts, including demographic parity and equalized odds, along with methodologies to achieve these notions in different contexts. Despite the rapid advancement in this field, not all sectors have embraced these fairness principles to the same extent. One specific sector that merits attention in this regard is insurance. Within the realm of insurance pricing, fairness is defined through a distinct and specialized framework. Consequently, achieving fairness according to established notions does not automatically ensure fair pricing. In particular, the regulatory bodies are increasingly emphasizing transparency in pricing algorithms and imposing constraints for insurance companies on the collection and utilization of sensitive consumer attributes.  These factors present additional challenges in the implementation of fairness in pricing algorithms. To address these complexities and comply with regulatory demands, we propose a straightforward method for constructing fair models that align with the specific fairness criteria unique to the insurance pricing domain. Notably, our approach only relies on privatized sensitive attributes and offers statistical guarantees. Further, it does not require insurers to have direct access to sensitive attributes, and it can be tailored to accommodate varying levels of transparency as required. This methodology seeks to meet the growing demands for privacy and transparency set forth by regulators while ensuring fairness in insurance pricing practices.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper discusses a practical method to produce 'discrimination-free prices' for a regression task with a finite number of sensitive attributes. The method essentially consists on training a separate regression model for each sensitive task, then aggregate the predictions according to some predefined (sensitive) group marginal. To introduce some measure of privacy into the model, the sensitive attributes of each sample are shared using randomized response.

### Strengths
The method itself is exceedingly simple to implement.

### Weaknesses
One major concern for me is the novelty of the algorithm, since it amounts to learning a per-sensitive-group regression model and  (weighted) averaging.

The other large concern relies on the claims that the proposed algorithm is differentially private. I think the authors should specify this claim more precisely, maybe by stating that its assumed x, y are public knowledge and that the model is therefore private wrt only the sensitive attribute.

### Questions
What are the formal privacy guarantees for the trained model, given that the private release mechanism is applied only on the sensitive attributes and not on the entire sample.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of fair pricing in insurance. The insurance industry pursues actuarial fairness, a concept distinctive from the more commonly studied algorithmic fairness, and there lacks effective methods for designing pricing models that are actuarial fair. Motivated by this research gap, this paper proposed a method to train actuarial fair models for the practical scenario where an insurer has access to non-sensitive attributes, and a trusted third-party (TTP) partner has access to the corresponding privatized sensitive attributes. The proposed training method only requires access to privatized sensitive attributes via the TTP. The authors demonstrated the validity of their method by deriving relevant statistical guarantees and showing empirical effectiveness on an income prediction task.

### Strengths
This paper studied an important practical challenge of training fair ML model when the protected attributes are not readily available. The research problem has practical potentials as it is directly motivated by real-world insurance pricing. Along with the proposed algorithms, the authors provided solid theoretical results about the statistical guarantees for their performance.

### Weaknesses
This paper focused on ‘actuarial fairness’ definition formulated in an earlier paper. It is unclear whether this formulation is practical, and whether it is a broadly accepted formulation. Further literature review on its usage and potentials in practice will be helpful. On a related note, the term ‘actuarial fairness’ was used in the introduction paragraph without defining what it is. While I understand it was formulated later in the mathematical definition, it will be helpful to see how the insurance industry defines ‘actuarial fairness’ on the conceptual level first. 

I also found it difficult to pinpoint what is novel in the paper. One motivation mentioned in the beginning of the paper is that the difference between actuarial fairness and other conventional algorithmic fairness notions calls for new fair algorithms, but it is unclear why a fair algorithm designed under privacy considerations for a conventional fairness concept would not work. It seems that the difficult comes from the unavailable sensitive attribute, but this is not an issue unique to the insurance pricing application. In addition, for the derivation of theoretical results, it would be useful to know whether and how the fairness or the noise or the multi-party training flow leads to challenges.

### Questions
1.	In insurance pricing, are there any popular fairness definitions that are already used in pricing mechanisms? 

2.	How restrictive are Assumptions A and B in Section 4.3?

3.	What is the interpretation of noise in this context?

4.	The algorithms consider that only the protected attributes are sensitive, hence are stored with the third party. Is it reasonable to also consider non-protected attributes (in terms of fairness) are also not readily accessible to the insurer, but need to be obtained via a third party? If so, can the algorithms be generalized?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Due to difficulty learning fair insurance prices because of inaccessible/privatized sensitive attribute data, the authors propose a multi-party training framework to achieve discrimination-free insurance pricing. In their proposed model, the insurer has access to all data except the sensitive attributes and the third party uses the transformed data from the insurer plus the sensitive information to make fair pricing predictions. The authors test their method on the Adult income dataset and compare accuracy for varied values of privacy budget.

### Strengths
- I like the problem the authors investigate. The authors tackle a real challenge faced during fair predictive decision-making. 

- The write-up is precise and consistent, and the ideas are well presented. 

- I like that authors theoretically and empirically investigated cases of known and unknown pi and showed results for varied privacy budgets.

### Weaknesses
While I think the authors did a great job laying down the proposed model, I observed some shortcomings that influenced my score. 
Below are the observed weaknesses (and respective suggestions) and some questions. 

- Specific versus general models. Although the authors mention that the biggest strength of their work (especially in comparison to previous works -relatedworks) is their model working under any given loss function, in their theory and empirical work, the focus is on logistic regression. The authors (reasonably) defend this choice as a tradeoff between transparency and complexity, which makes it hard to appreciate author contributions.

- Since noise levels have a significant effect on risk-LDP, I am curious about the effect of overestimating and underestimating noise on fairness and the impact on different sensitive groups, especially in the case of unevenly distributed groups.

- Several challenges are associated with a multi-party framework, for example, information leakage, computation overhead, etc..  I am curious how the proposed method would be comparatively better than those settings where fairness is computed on (single-party) fully differentially private data (X,D) or where causal inference (and other methods) is used to perform fairness in the absence of sensitive attributes. 

- Experimental setup and results. There are other (single-party) fair decision-making with private data methods and noisy sensitive attributes that the authors could have compared their work with. Although authors show different error rates with varied privacy budgets, it would have been informative to see how the method compares to other (similar) methods. Additionally, authors say they couldn't find insurance-like data, but there are at least 50 insurance datasets on Data World (and other platforms).

### Questions
Although generally, I think the authors did a great job with outlining the problem and proposed solution, I found a couple of shortcomings (questions) raised in the weakness section that influenced my score.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
