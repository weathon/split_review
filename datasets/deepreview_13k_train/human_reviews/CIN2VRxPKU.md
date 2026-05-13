# Evaluating Deep Unlearning in Large Language Models

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
Machine unlearning is a key requirement of many data protection regulations such as GDPR. Prior work on unlearning has mostly considered superficial unlearning tasks where a single or a few related pieces of information are required to be removed. 
However, the task of unlearning a fact is much more challenging in recent large language models (LLMs), 
because the facts in LLMs can be deduced from each other. 
In this work, we investigate whether current unlearning methods for LLMs succeed beyond superficial unlearning of facts. 
Specifically, we formally propose a new setting of unlearning, \textit{\problemname}, which considers the logical deductions between facts. 
Moreover, we design the metric, \textit{recall}, to quantify the extent of \problemname.
To systematically evaluate \problemname, we construct a synthetic dataset \dataname, which consists of a synthetic knowledge base of family relationships and biographies, together with a realistic logical rule set that connects them. 
We use this dataset to test four unlearning methods in four LLMs at different sizes. 
Our findings reveal that in the task of \problemname\ only a single fact, they either fail to properly unlearn with high recall, or end up unlearning many other irrelevant facts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a critique of current unlearning methods through the lens of fact unlearning - it shows that while current unlearning methods can unlearn the target fact in isolation, they often fail to unlearn other related facts through which the target fact can be logically deduced, thus negating the effect of unlearning. The authors refer to the task of unlearning additional facts which are logically related to the target fact, as "deep unlearning". They introduce 2 metrics based on set overlap: recall and accuracy, which quantify the extent of "deep unlearning". All experiments are conducted on a small, synthetic dataset derived from a synthetic knowledge base and a set of logical rules.

### Strengths
This paper extends the discussion on the "illusion of machine unlearning" vis-à-vis current unlearning methods, to the relatively simple yet seemingly hard task of unlearning a single fact from the LLM's parametric memory, given that logically related facts are also present in the LLM. This work shows, somewhat surprisingly, that when current unlearning methods are tasked with erasing a single fact from the LLMs parametric knowledge, they do not erase related facts which also share entities/objects with the target fact, for e.g. erasing the target fact **F1**: Y is child of X, may fail to erase logically related facts such as: **F2**: Z is husband of X, and **F3**: Z is father of Y, even though Y as an entity appears in F3, and this would allow the erased fact to re-surface via logical deduction. On a synthetic toy dataset, they provide a reasonable set overlap based metric for quantifying the degree of such unlearning. While it is already known that most knowledge that is supposedly deleted by current unlearning methods can be re-surfaced via adversarial/jailbreak prompting and probing, this work highlights limitations of current methods at the atomic level of single-fact deletion, hinting at a tension between an LLM's reasoning capabilities and the effectiveness of unlearning techniques.

### Weaknesses
- Firstly, I find it a bit counter-intuitive that even an unlearning method such as WHP (Who's Harry Potter) would not suppress the effect of other facts which share entities with the target fact, such as in the case of facts related to familial connections where a target entity appears verbatim in other facts. This leads me to wonder if the failure to "deeply unlearn" a target fact is simply an artifact of the way in which the unlearning methods are applied e.g. WHP requires finetuning a reinforced model on a corpus that is much larger than just a handful of facts, in order for the logit difference with the baseline to be significant. The paper does not really discuss how each of the unlearning methods are actually applied, and whether any of the tested unlearning methods are even compatible with the setting of single fact unlearning - in my view, methods such as NPO, TV, and WHP are clearly more suited for a setting where the unlearning target is defined around a *concept* or *topic*, rather than single **fact**. A discussion around the compatibility of the evaluated unlearning methods with the single fact unlearning setting, and what role the small size of the synthetic dataset plays in limiting the effectiveness of unlearning methods, would be a useful addition. For example, if the WHP method is properly applied as it is designed i.e. for concept unlearning rather than fact unlearning, I imagine that it would successfully suppress the fact that "Harry is child of Lily" even if it was fine-tuned on other facts that mentioned that "James is father of Harry" and "James is husband of Lily". To help readers better understand the experimental setup and interpret the results, I recommend that the authors discuss the adaptations they made to apply WHP, NPO, TV etc., to the fact unlearning task.

- The synthetic dataset appears to be biased towards highly deducible relationships (e.g., familial connections) which is not really representative of real-world knowledge structures where logical connections are typically more complex and less *deducible*. In my view, the authors should have included an evaluation on a dataset extracted from a real-world knowledge base with partial/noisy/incomplete logical connections between facts - my guess is that since most real facts require more than just simple deductive reasoning e.g. may require multi-hop reasoning, this problem of knowledge deductibility or fact reconstruction would be less of an issue even with current unlearning methods. While the authors claim that it is hard to conduct prompt based evaluations for determining if a fact is in the LM (false negatives), I'd like to point out that alternatives to the simple prompts used by the authors (as shown in Table 1) do exist (see [1]), such as MCQ-based binary choice Q&A or latent supervised/unsupervised probing. It would also useful have been to see how the "approximate" recall and accuracy metrics will scale to real KBs where many of the logical connections between facts are unknown.

- The authors should discuss the limitations of their current dataset and how these might affect the generalizability of the results.

- Minor typos: typo in appendix C, should be “algorithm 3” instead of “Algorithm 9”.  Caption of Figure 7 should also say “algorithm 3” instead of “algorithm 1”.  Typos in each caption of subfigures in figure 8: should say “Minimal Deep Unlearning” sets.

### Questions
Q1: How would the accuracy and recall metrics change w.r.t. to the # of minimal deep learning sets discovered when applied on a KB with incomplete/partial logical dependencies? Would recall increase since the minimal deep unlearning set is smaller and closer in size to the actual set unlearned by the algorithm, thus having higher overlap? What about accuracy?

Q2: Given the small size of the target facts to be unlearnt, how do you satisfy the fine-tuning data requirements of methods such as NPO & WHP?

Q3: What motivated 0.8 as threshold value for comparing recall/accuracy (Figures 3 and 6)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces "deep unlearning" as a novel approach in the domain of large language models (LLMs), emphasizing its importance in effectively erasing certain facts. As the target fact can be deduced from logical rules, superficial unlearning methods, which solely unlearn the target fact, cannot unlearn it successfully. The authors also present new metrics, including Accuracy and Recall, to evaluate this process, backed by experiments across various LLMs and unlearning methods.

### Strengths
1. Novel Contribution: The introduction of deep unlearning and a curated dataset highlights a significant gap in current research, drawing attention to an important and underexplored issue. 
2. Innovative Metrics: The proposal of Recall as a new evaluation metric, accompanied by a detailed algorithm for addressing the NP-hard nature of the problem, demonstrates thoughtful consideration of the challenges involved in deep unlearning. 
3. Comprehensive Experiments: The thorough experimental setup across four LLMs and unlearning methods strengthens the paper's credibility and provides valuable insights into the effectiveness of the proposed approach.

### Weaknesses
1. Code Availability: The lack of code and dataset release until after acceptance may hinder reproducibility and limit the community's ability to validate the findings. If possible, we encourage the author to give an anonymous link to the git repo. If it is forbidden in rebuttal process, you can include more raw samples in Appendix with explanation. More importantly, as you proposed a benchmark, the statistics of the datasets are of vital importance, which should be discussed in the main part, rather than appendix.
2. Missing Results: The author did not report the accuracy on the dataset of the models fine-tuned but not subjected to unlearning, which makes it difficult to gauge the impact of the unlearning methods accurately. Please include the baseline accuracy results for the fine-tuned models before unlearning.
3. Poor Presentation: The author should improve the writing and figure for better illustration, especially the figures. For instance, Figure 3 and 6 are not clear to the analyzed conclusions. Maybe a organized table will be better. From my perspective, for this work, the related work is crucial for the understanding of the benchmark, which can be moved to Sec 2.

### Questions
Refer to peaknesses, I hope that you can solve these concerns.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces the concept of "deep unlearning", which studies the unlearning tasks in large language models where logical relationships between facts need to be considered. The authors constructed a synthetic dataset EDU-RELAT, containing family relationships and biographical information, to evaluate four unlearning methods across four different-sized LLMs.

### Strengths
1. Presents an important and novel problem - deep unlearning that considers logical reasoning between facts
2. Constructs a structured evaluation dataset with reasonable logical rules and relationships
3. Proposes reasonable evaluation metrics (recall and accuracy) and designs approximate algorithms to compute these metrics
4. Comprehensive experiments that reveal the limitations of current methods in deep unlearning

### Weaknesses
1. While deep unlearning sounds reasonable overall, the paper's setting may not align with practical scenarios. In real machine unlearning cases, related knowledge is typically forgotten together (e.g., forgetting all content related to Harry Potter) rather than just forgetting a single relationship. Under this setting, is it still important to forget all knowledge that could potentially derive the current relationship?

2. Given that real-world relationships can be far more complex than the R defined in this paper's dataset, could there be situations where forgetting one piece of knowledge requires forgetting an excessive amount of content? In multi-hop reasoning scenarios, a large amount of knowledge might need to be forgotten, which raises another question: is deep unlearning always necessary in unlearning scenarios? If unlearning is applied for copyright protection, can knowledge derived through multi-hop reasoning constitute infringement?

3. The paper only focuses on logical rules in the specific domain of family relationships, which is rather narrow in scope.

4. No new solutions are proposed to improve deep unlearning effectiveness, remaining only at the problem analysis level.

### Questions
Please refer to the weakness part.

### Soundness
3

### Presentation
3

### Contribution
2
