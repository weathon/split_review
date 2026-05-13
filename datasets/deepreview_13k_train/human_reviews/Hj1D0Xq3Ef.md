# Underestimated Privacy Risks for Minority Populations in Large Language Model Unlearning

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
Large Language Models (LLMs) are trained on extensive datasets that often contain sensitive, human-generated information, raising significant concerns about privacy breaches. While certified unlearning approaches offer strong privacy guarantees, they rely on restrictive model assumptions that are not applicable to LLMs. As a result, various unlearning heuristics have been proposed, with the associated privacy risks assessed only empirically. The standard evaluation pipelines typically randomly select data for removal from the training set, apply unlearning techniques, and use membership inference attacks (MIAs) to compare the unlearned models against models retrained without the to-be-unlearned data. However, since every data point is subject to the right to be forgotten, unlearning should be considered in the worst-case scenario from the privacy perspective. Prior work shows that data outliers may exhibit higher memorization effects. Intuitively, they are harder to be unlearn and thus the privacy risk of unlearning them is overlooked and underestimated in the current evaluation. In this paper, we leverage minority data to identify such a critical flaw in previously widely adopted evaluations. We substantiate this claim through carefully designed experiments, including unlearning canaries related to minority groups, inspired by privacy auditing literature. Using personally identifiable information (PII) as a representative minority identifier, we demonstrate that minority groups experience at least 20\% more privacy leakage in most cases across six unlearning approaches, three MIAs, three benchmark datasets, and two LLMs of different scales. Given that the right to be forgotten should be upheld for every individual, we advocate for a more rigorous evaluation of LLM unlearning methods. Our minority-aware evaluation framework represents an initial step toward ensuring more equitable and thorough assessments of LLM unlearning efficacy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The common method of evaluating the privacy leakage of unlearning in large language models is based on a chosen dataset $D_{forget}$ to unlearn from that model, say, $M^{(1)}$. The paper argues that a current method of using a random $D_{forget}$ significantly underestimates the real privacy leakage of the unlearned model. To do this, the paper proposes the method of analyzing the privacy leak of a synthetic dataset $D_{canary}$ created by replacing personally identifying information from $D_{forget}$ with the most unlikely personally identifying information from the whole training set $D_{train} = D_{keep} \cup D_{forget}$. The paper compares the privacy leakage of the $M^{(1)}$ and $M^{(2)}$ that were trained on $D_{forget} \cup D_{keep}$ and $D_{canary} \cup D_{keep}$ respectively and then un-trained on $D_{forget}$ and $D_{canary}$ respectively. Differences in audits in the unlearned models and a model retrained on $D_{keep}$ from scratch shows privacy leakage. Since a synthetic dataset might not represent real world scenarios, the paper does a similar analysis where $D_{forget}$ is taken from the most unlikely data in $D_{train}$.

### Strengths
* The paper highlights some weakness in current privacy evaluations for algorithm-agnostic unlearning techniques in LLMs and provides methods for improving privacy audits for these LLMs.

* The paper covers multiple unlearning algorithms and multiple membership inference attacks.
  
* The paper overall is clearly written, for example it has clear explanations of the background such as model unlearning.  Figure 1 is a clear overview of the pipeline proposed in the paper.

### Weaknesses
 * The paper seeks to explain that their evaluations of MIAs based on how *Canaries* and *Minorities* gives higher *PrivLeak* scores compared to *Random*. However, there is no justification for why the *PrivLeak* score is used to begin with. This seems important particularly given that the subsequent analysis in the paper hinges on this choice.
  
* The paper analyses the privacy-utility trade-off of models after unlearning by comparing the *PrivLeak* score and LLM perplexity. The analysis could benefit from other utility measures (for example it doesn't capture semantic meaning, and LLMs could be very confident about an incorrect prediction).

### Questions
* Why is it useful to study the *Canaries* set if synthetic data does not reflect real world scenarios?
  
* What is the justification for 10 unlearning units? How does the large underestimation in PL compare to *random* under different unlearning budgets? 
  * For an LLM would it be practical to allow for longer unlearning times especially considering the retraining cost is much larger in comparison?
* The paper highlights limitations in the typical evaluation pipeline (*random*). Are there limitations in this new pipeline?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper conducts a benchmark evaluation of different machine unlearning approaches, and computes membership inference metrics on the unlearned models.  They find that prior work underestimates the privacy risk on minority groups by about 20% in the settings they studied.  Their findings are fairly robust across a variety of different unlearning methods, MIA metrics, base models, datasets, and other experimental settings.   Based on this finding, the authors advocate for a minority-aware evaluation, and discuss which methods perform best under this evaluation.

### Strengths
* Paper introduces a solid benchmark and a carefully crafted set of experiments.
* This main findings are interesting, and could help shape future research in this space.

### Weaknesses
 * The main finding that MIA attacks have different success rates on different subsets of the population is not surprising, and is in line with other work in the privacy + fairness space.  
* A good number of experiments were done, but only two main findings came out from them: (1) that MIA metrics differ based on { Random, Canary /Minority } and (2) that  Langevin Unlearning provided the best balance between privacy and utility.  Are there more findings or observations you can make based on the data you collected?  You should target at least one key takeaway for each Figure/Table you have.

### Questions
* What are the limitations of your methodology?
* Can you offer any insight into why Langevin Unlearning does better under a minority-aware evaluation?
* Table 4 and 5 are pretty busy, and there is no reference to Table 4 in the text.  If you can help the reader by telling them what they should look at in the table and how to interpret the full results, that would be nice.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the evaluation pipeline of LLM unlearning (i.e., efficient LLM modification so that it becomes statistically indistinguishable from a model retrained from scratch, without the data subject to removal), and identifies a flaw in the existing evaluation approaches.

### Strengths
1. This paper highlights an issue with LLM unlearning evaluation, being data dependent. The current evaluation chooses to forget the dataset uniformly at random. 
2. This paper shows that minority groups experience at least 20% more privacy leakage in most cases across combinations of six unlearning approaches.
3. This paper calls for a more careful LLM unlearning efficacy evaluation.

### Weaknesses
Given the "right to be forgotten" and too expensive cost of re-training LLMs from scratch without the data subject to removal, machine unlearning techniques have been proposed.


As there is no formal unlearning guarantee for deep neural networks and LLMs, evaluation of LLM unlearning uses membership inference attacks as follows:
- Randomly select data for removal from the training set to create a "forget" dataset,
- Apply unlearning techniques to the LLM
- Use membership inference attacks to compare the unlearned models against models retrained without the removed data.

This paper identified a flaw in this evaluation pipeline (mainly in the first step): "the unlearning privacy risk of minority populations within the training set is severely underestimated since the minority data are less likely to be selected in the unlearning evaluation pipeline."
 

This paper proposes the need of using worst-case data for creating forget dataset in the evaluation pipeline. However, the suggested choice of worst-case scenario suffers from multiple issues:

1. This paper assumes that the worst case data corresponds to minority data. 
2. This paper defines minority data based on only personally identifiable information.
3. This paper creates canaries by replacing personally identifiable information in randomly chosen data within forget dataset with least frequent ones. 



This paper proposes a minority-aware LLM unlearning evaluation protocol to address the limitation of existing evaluation pipelines. However, the proposal depends heavily on the above choices: worst-case data, minority definition and canary creations. In addition, the broader motivation is unclear- for example if the data subject to removal does not blog to least frequent data, it is not clear what the applicability of the proposal would be.

The main finding of this paper (privacy risks of minority groups in the training data are usually underestimated) seems related to several existing works studying disparate vulnerability against MIAs.


Minors:
- All text in lines 197-215 + a table + a figure aim to say that frequencies of items vary in a dataset, or I am missing something non-trivial?

- "In the provided example,  Dforget unlikely contains the least frequent email with the 484 area code. As a result, the corresponding unlearning privacy evaluation may underestimate the privacy risk of minorities if unlearning minority data is inherently more challenging." --> Not clear how the latter got concluded just because of being least frequent? 

- bold claims without supports: 
	- 237-238: "albeit a similar idea extends beyond PIIs"
	- 139-140: "albeit our methodology extends to other cases whenever the indistinguishability to the retrained model is an appropriate metric"



- 93-94: "the right to be forgotten should be respected for all individuals" --> how to define individual? each individual has one record or multiple records? This is not discussed later on in the paper. 

- 40-41: missing refs for GDPR and right to be forgotten 

- 262: "it cannot quantify underestimate the privacy risk for minorities in the real-world setting" --> grammar issue


- 377: "Enron(Klimt & Yang, 2004) and ECHR(Chalkidis et al., 2019)." --> missing space

### Questions
1. Why minority data should be considered as worst-case data for LLM unlearning evaluations?
2. Why minority data should be defined based on personally identifiable information? How generalisable the results/findings are when using alternative minority definitions? 
3. Why is the suggested way of creating canaries relevant?
4. Why do the chosen minorities suffer from at least 20% more privacy leakage in studied cases? Is it due to being least frequent or their context/semantics?
5. How are these results compared to those works analyzing disparate vulnerability against MIAs such as Kulynych et. al., Disparate Vulnerability to Membership Inference Aacks (https://arxiv.org/pdf/1906.00389).

### Soundness
3

### Presentation
3

### Contribution
2
