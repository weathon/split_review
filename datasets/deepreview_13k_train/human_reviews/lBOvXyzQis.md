# Measuring Diversity: Axioms and Challenges

- Decision: Reject
- Scores: 5, 8, 5, 5, 5, 5

## Abstract
The concept of diversity is widely used in various applications: from image or molecule generation to recommender systems. Thus, being able to properly measure diversity is important. This paper addresses the problem of quantifying diversity for a set of objects. First, we make a systematic review of existing diversity measures and explore their undesirable behavior in some cases. Based on this review, we formulate three desirable properties (axioms) of a reliable diversity measure: monotonicity, uniqueness, and continuity. We show that none of the existing measures has all three properties and thus these measures are not suitable for quantifying diversity. Then, we construct two examples of measures that have all the desirable properties, thus proving that the list of axioms is not self-contradicting. Unfortunately, the constructed examples are too computationally complex for practical use, thus we pose an open problem of constructing a diversity measure that has all the listed properties and can be computed in practice.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper discusses some theoretical aspects of various diversity measures. It suggests that common diversity measures, such as Vendi Score and Determinantal Point Process scores are optimized for computational simplicity rather than axiomatic optimality. They have potential drawbacks breaking some intuitive properties, such as monotonicity and uniqueness. The paper then proposes two measures: MultiDimVolume and IntegralMaxClique, which preserve all properties, despite being NP-hard to compute.

### Strengths
Originality: The paper provides a systematic overview of commonly used diversity measures and gives concrete examples where these measures fail. The overview lays good foundation for the proposed methods.

Clarity: The proposed ideas are clearly presented and their connections to prior limitations are straightforward.

### Weaknesses
While I appreciate the unique angles that the paper takes to introduce the new NP-hard diversity measures, the measures themselves do not appear totally novel to me. They appear closely related to hypervolume-based multiobjective optimization, dating back to 2012. Additional discussions are needed to clarify the connections to existing work and to refresh the claims of contributions.

Another weakness is a lack of experiments. Contrary to the author's conclusion, an NP-hard objective can be practical if the number of candidates are few. For example, it is possible to compute the MultiDimVolume of Top-K recommended items from a recommender system, provided that K is in the range of 100-1000. For an ICLR contribution, I would expect to see some empirical validation of the proposed methods.

Lastly, the discussion of DPP objective can be strengthened. It is unclear to me whether the violation of the monotonicity property can be a result of improper normalization or is it a fundamental flaw of the DPP objective. More discussions about the construction of the K-matrices (Line 210) would be helpful.

### Questions
Regarding the comparison with hypervolume-based multiobjective optimization. Can the authors:
1. Clarify connections to existing work
2. Revise claim of novelty with respect to prior work

Regarding empirical evaluation. Can the authors validate an empirical comparison between the proposed methods and DPP or Vendi Scores. Here are some examples of empirical papers on the topic of diversity:
* Diverse Beam Search: Decoding Diverse Solutions from Neural Sequence Models . https://arxiv.org/abs/1610.02424
* Maximal Marginal Relevance: https://www.cs.cmu.edu/~jgc/publication/The_Use_MMR_Diversity_Based_LTMIR_1998.pdf

Regarding DPP discussion, please provide the sample points that are used to create the K matrices on Line 210.
* Are the sample points themselves violating monotonicity?
* What normalization steps are commonly used for DPP calculation?
* Would diagonal regularization (adding an lambda x Identity matrix) alleviate some of the drawbacks?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a systematic examination of diversity quantification across different use cases and fields. The authors identify that existing diversity metrics fail to simultaneously satisfy three fundamental axioms: monotonicity, uniqueness and continuity. The authors then propose two theoretical measures, MultiDimVolume and IntegralMaxClique, which satisfy these axioms. This work makes a contribution by establishing formal axioms for diversity measurement and framing a crucial open problem: developing computationally efficient diversity measures that satisfy all three fundamental axioms.

### Strengths
The theoretical rigor of this paper is commendable.

### Weaknesses
The main weakness is that both measures which are proposed in the paper prove computationally intractable due to their NP-hard nature.

### Questions
The paper might benefit from more rigor in addressing computational concerns earlier, particularly in a section discussing the limitations of applying these measures at scale. A discussion around the theoretical complexity of diversity measurement or potential computational techniques to approximate them would have provided a more balanced contribution.

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
**Summary**:

This paper focuses on the concept of diversity and how to quantify diversity for a set of objects. The authors first systematically review prior studies in measuring diversity, showcasing that these diversity measures behave undesirably in some cases.
Then, the paper proposes three desirable axioms of a reliable diversity measure: monotonicity, uniqueness, and continuity, followed by two examples of diversity measure having the desirable properties. However, the proposed measures are computationally expensive, preventing a practical use case.

### Strengths
1. The paper studies an interesting problem, measuring diversity of a set of objects, which can be broadly applied in various problems, e.g., image or molecule generation, recommender systems.

2. A thorough analysis of existing diversity measures is provided, offering insights into the behavior of each measure.

3. The three proposed diversity measuring axioms are easy to understand.

### Weaknesses
While the paper has some merits, it suffers from a key limitation in the method itself. The proposed diversity measures, MultiDimVolume and IntegralMaxClique, are NP-hard, making them computationally expensive as the authors acknowledge. This computational intractability severely limits the practical applicability of the proposed measures, rendering them unsuitable for real-world datasets where efficiency is crucial. Additionally, the lack of experimental results comparing the proposed method with prior studies raises questions about the effectiveness of the proposed method. The absence of empirical validation makes it difficult to assess the practical benefits of the proposed axioms and whether they lead to diversity measures that outperform existing ones. Making the proposed method computationally tractable and including comparative experiments, therefore, would significantly strengthen the proposed approach.

### Questions
Please see the weaknesses.

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
The paper focuses on diversity evaluation, i.e, how to quantify diversity in a collection of objects. The authors first criticize existing diversity measures by claiming that they may either lead to unexpected evaluation results or degenerate solution when being optimized. To bridge the gap, they define three properties associated with a good diversity measure: monotonicity, uniqueness, and continuity.  

Lastly, by analyzing two diversity measures that satisfy all three properties, but being NP-Hard, the authors pose the challenge of developing diversity measures that satisfy all three properties while being computationally manageable.

### Strengths
1. The proposed ideas are well justified. For example, the authors use a concrete counter-example in Appendix A to argue the necessity for the diversity function to be continuous. 

2. The paper is presented in a systematic manner and it is easy to follow the claims and analysis conducted by the authors.

### Weaknesses
1. Analysis of existing diversity measures is limited to simple cases. It would be better to examine whether such analysis holds for more practical scenarios, such as diversity metrics in the recommendation task or NLG generations. 

2. No explanation provided to "why a measure satisfying all three axioms can effectively evaluate diversity or lead to good performance while being optimized."

3. The contribution of the paper is somewhat limited, as it primarily critiques existing measures and introduces a new problem without offering concrete solutions to address it.

### Questions
1. How do you concretely define "our intuitive perception of diversity"? I think you should discuss in the context of several specific tasks. For example, how do you define diversity in the context of generations from LLMs? What are the intuitions regarding diversity in such a context?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper studies quantifying the diversity of a set of objects, such as samples in a dataset. The authors first give a thorough literature review of prior diversity measurement methods. Then, the authors propose three axioms for a reliable diversity measurement according to the literature review and find that existing methods are struggling to satisfy these three axioms. Finally, the paper shows two examples that satisfy all three axioms to prove the non-self-contradicting of these axioms.

### Strengths
- The paper suggests the requirement for better diversity measurement, which is a valuable problem and indicates strong motivation.
- The paper is well-structured and easy to follow.

### Weaknesses
 - The paper would benefit from more extensive experiments that highlight the drawbacks of existing methods and demonstrate the necessity of the three proposed axioms. Such experiments would make the work more convincing.
- Similar axioms have already been proposed in Leinster's work [1]. It would be helpful to clarify the differences between the axioms in Leinster's work and those presented in this paper.
- Section 3 includes some overly intuitive descriptions, and the prerequisites for the drawbacks of existing methods are too strict, e.g.,  
1) In Lines 126-128, the situation where a dataset appears more diverse from a human perspective but is less diverse in actual measurements may be strongly related to the embedding used for computing distances or similarities. This could indicate an issue with the embedding rather than the diversity measurement method. Additionally, such a case seems relatively rare, and it might be reasonable to conduct experiments to verify its occurrence. 2) The description of the limitations of the existing method includes very stringent prerequisites (e.g., requiring 16 points to be located at the four corners of a unit square, as mentioned on line 142), which are difficult to justify as generally applicable. Additionally, the positions of these points in the feature space are closely related to the embedding computation.


### Questions
It appears that the Vendi Score satisfies the second axiom (Uniqueness), as it meets the property of identical elements [2]. The underlying logic of identical elements seems to be similar to that of the second axiom in this paper. 

Reference:
[2] Friedman D, Dieng A B. The vendi score: A diversity evaluation metric for machine learning[J]. arXiv preprint arXiv:2210.02410, 2022.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper critiques existing diversity measures, illustrating their unreliability through examples. It introduces three axioms: monotonicity, uniqueness, and continuity which are essential for a reliable measure. None of the known measures satisfy all three properties. The authors propose two new measures that meet these criteria but are computationally complex. Future research is needed to develop a practical diversity measure that adheres to all three axioms.

### Strengths
+ The research problem in the paper is meaningful.
+ The paper is well-organized and easy to follow.
+ The examples and analysis are detailed.

### Weaknesses
 - Some writing needs to be more clear.
- Some undefined notations make part of the paper hard to understand.
- Typos and grammar issues.



### Questions
1. The authors claim that, "we formulate three desirable properties (axioms) of a reliable diversity measure: monotonicity, uniqueness, and continuity." And it is mentioned several times in the text that a reliable diversity metric should satisfy these three properties. To confirm, do the authors believe that it is a reliable metric as long as these three properties are satisfied? My question is, how is a reliable diversity metric defined? Do related studies support it? Does a reliable diversity metric only need to satisfy these three properties, and are there no other properties that need to be satisfied?

2. Some undefined notations make the paper hard to understand.
- On line 78 of page 2, what is the range of $i$ and $j$, and is there a size relationship?
- On line 90 of page 2, what is the meaning of $t$? There is no explanation and no reference for it.
- On line 364 of page 7, what is the Equation (7)?
- Etc.

3. Some writing needs to be more clear. For example, on lines 78-79 of page 2, the authors say that, "For generality purposes, we do not require the triangle inequality to be satisfied by $d_{ij}$." No more explanations. I do not know why.

4. Diversity is a scientific topic that has been studied for a long time, but the paper has only just a few references. It is recommended that the authors add references when introducing each comparative metric. Moreover, compare more diversity metrics, such as the Gini index, Coverage, etc.

5. Typos and grammar issues: 
- On line 87 of page 3, "(often referred to as Bottleneck and Diameter, respectfully)." 
- On lines 108-110 of page 3, "Some previous works on measuring diversity analyze and compare measures based on properties they do or do not satisfy. We review these works in Section 4.2." While on lines 251-252 of page 5, "Several papers analyzed and compared diversity measures in terms of properties they do or do not satisfy." 
- On line 252 of page 5, "For instance, Xie et al. (2023) formulates three axioms."
- Etc.

### Soundness
3

### Presentation
2

### Contribution
2
