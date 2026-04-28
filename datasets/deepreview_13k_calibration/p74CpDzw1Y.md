# Varying Shades of Wrong: Aligning LLMs with Wrong Answers Only

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
In the absence of abundant reliable annotations for challenging tasks and contexts, how can we expand the frontier of LLM capabilities with potentially wrong answers? We focus on two research questions: (1) \emph{Can LLMs generate reliable preferences among wrong options?} And if so, (2) \emph{Would alignment with such wrong-over-wrong preferences be helpful?} We employ methods based on self-consistency, token probabilities, and LLM-as-a-judge to elicit wrong-over-wrong preferences, and fine-tune language models with preference optimization approaches using these synthesized preferences. Extensive experiments with seven LLMs and eight datasets demonstrate that (1) LLMs \emph{do} have preliminary capability in distinguishing various shades of wrong, achieving up to 20.9\% higher performance than random guess; (2) Alignment with wrong-over-wrong preferences helps LLMs to produce less wrong and sometimes even outright correct answers, while overall improving model calibration.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a creative approach to solving alignment problem in large language models (LLMs) especially in resource constraint settings by proposing a methodology called "wrong-over-wrong alignment." The core idea is for LLMs to learn by differentiating varying degrees of wrongness in responses, enabling alignment without the need for correct, ground-truth answers. This approach addresses a common challenge in real-world applications where human-verified data is often scarce. By relying on wrongness comparisons, the authors demonstrate that this alignment can enhance model calibration and improve response accuracy even in resource-limited settings.

### Strengths
This paper introduces quite a novel approach to doing alignment in the absence of ground truth. The paper proposes an alignment methodology called wrong-over-wrong alignment. Such an alignment allows any LLM to learn the correctness of an answer (for the domain it is trained/aligned on), by simply distinguishing between varying shades of wrong. This is quite a valuable approach to solve alignment especially when human vetted groudth truth is missing, which is more often than not in any practical situation. This idea has the potential to push the capabilities of LLMs in resource constrained settings. 

Authors have done a good job in presenting a very comprehensive, clear and rigorous experimentation methodology to test the hypothesis. I was quite satisfied to read about various methods that the authors proposed to elicit wrong over wrong preferences. I also came out quite impressed with the experimentation rigor presented in the paper. From various preference elicitation methods to various LLMs, authors have ensured sufficient dimensions are explored in depth. 

Lastly, various insights such as task utility, effectiveness of wrong over wrong preferences, innate capabilities of LLMs, model confidences etc strengthened the paper further.

### Weaknesses
The biggest weakness in my opinion of the method presented in tihs paper is its reliance on proxy functions. While the main objective of the paper is to explore alignment without dependence on correct answers, the paper however relies on proxy functions to elicit wrongness of answers. The proxy methods come with their own limitations and I worry that in real world practice, they may inadvertently introduce biases or even inaccuracies. Authors themselves have called out a possible introduction of biases in domains where the proxies are not well represented. Having said this, its not clear what unbiased alternative proxy methods one could use or even do away with proxies. 
As an ML practioner in an industrial setting, I would have liked to see experiments on real world use cases where implicit signals such as lack of clicks (normalized according to position) act as proxies for assigning wrongness score. The paper has an opportunity to test this idea in wild and use real world implicit signals to elicit wrongness. There is more wrongness signal than correctness signal in any real world application and thus this idea has huge potential.

### Questions
My main question to author is how confident they are in proxies' ability to accurately represent wrongness across different tasks. Have authors been thinking about doing proxy weighting to further improve their reliability. 

 On the insights, another question that I would like to get answers on is if authors observe any patterns in failure cases ? I am looking for cases where wrong over wrong alignment did not produce reliable preferences. What were those patterns ? 

I mentioned this in above section too. I am curious to learn how well does wrong over wrong alignment generalize to out of distribution tasks. Have the authors tested whether the model's calibration is preserved across tasks ? 

How do the authors plan to use this method in more subjective domains ? We get into the ethical contexts where defining what is less wrong could be culturally vary. This, in some sense, could be tied back to domain specific proxy definitions ? What are authors' thoughts and what guidance they want to provide to the community wanting to use this method in practice.

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
3

### Summary
The paper explores aligning LLMs with "wrong-over-wrong" preferences, a novel approach to distinguishing varying degrees of incorrectness rather than simply selecting between correct and incorrect answers. This technique aims to enhance not only the probability assigned to "less wrong" responses but also improves model accuracy and calibration.

### Strengths
* Creative approach that addresses alignment without needing correct answers.
* Solid, methodologically rigorous results across diverse datasets, validated with multiple LLMs.

### Weaknesses
 * The results and analysis sections are presented in a "bullet point" format without logical transitions, making it feel like a collection of findings rather than a cohesive story.
* Most tables, especially Table 1, are dense and challenging to interpret. Consider breaking them down, or move detailed tables to an appendix and keep summary statistics or visualizations. 
* In the experimental settings section, more context around the overall setup would help; for instance, the mention of multiple-choice questions jumps in without prior explanation.
* Why not average over evaluators? The paper doesn't focus on LLM-as-a-judge, so differentiating evaluators doesn’t seem essential in this context.
* The claim that "knowledge-based tasks are easier while commonsense is most challenging" feels overstated given the relatively modest performance gap.

**Minor Comments:**
* I would appreciate a clearer motivation, especially in the abstract and introduction; perhaps clarify how this method could address practical limitations in LLMs.

### Questions
* Why not average over evaluators? The paper doesn't focus on LLM-as-a-judge, so differentiating evaluators doesn’t seem essential in this context.
* The claim that "knowledge-based tasks are easier while commonsense is most challenging" feels overstated given the relatively modest performance gap.

**Minor Comments:**
* I would appreciate a clearer motivation, especially in the abstract and introduction; perhaps clarify how this method could address practical limitations in LLMs.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper explores utilizing LLMs to discern between incorrect answers i.e. wrong-over-wrong preferences and aligning LLMs using these preferences in situations where correct answers are unavailable or annotations are scarce.

### Strengths
- The paper explores a novel concept of "wrong-over-wrong" alignment, presenting an approach that diverges from traditional correct-answer evaluations, especially in contexts where correct answers may be absent.
- It raises important questions about how incorrect answers can still provide value in training and evaluation processes, potentially paving the way for further research in this area.

### Weaknesses
1. The framing of the concept could be improved to clearly communicate the utility of wrong-over-wrong alignment. The lack of explicit applications or contexts weakens the paper's stance. For instance, theorem-proving and low-resource languages are mentioned but the paper does not carry out any experiments on the same. Authors mentioned in the results that knowledge-based tasks had better performance but these tasks inherently contain correct answers which diverge from the proposed applications. Moreover, dataset curation inherently requires the ground truth to be present, which contradicts the motivation of the paper, which is that it can be deployed on tasks with scarce or no ground truths. The method performs poorly on SciBench which can be considered as a task close to theorem proving. Overall, the framing of concepts and applications can be improved.
2. The assessment of wrongness lacks rigorous criteria, leading to potential ambiguity in what constitutes "less wrong." More robust evaluation metrics are needed to substantiate claims. The subjectivity of wrongness varies drastically from task to task. The complexity of evaluating incorrect responses and their subjective interpretations requires more detailed explanations and examples to improve reader comprehension.
3. Currently the paper presents evaluations on different tasks and various parameters of its own method. But, it lacks sufficient comparison with existing models which are not aligned to wrong over wrong tasks.
4. The paper uses Logit-based methods to evaluate the correctness of a sample. They justify it by mentioning high token probability “probably” implies correct. However, models may assign high logits to incorrect answers due to biases in training data, leading to misleading assessments of accuracy[1].
5. The heuristic that longer answers equate to higher quality can lead to misjudgments, as verbosity may obscure clarity and accuracy, making it difficult to evaluate the substance of the response.  In [3], the authors evaluate the factuality of long-form responses, showing that simply increasing the length of an answer does not guarantee that it will contain accurate or relevant information. [4] emphasizes that longer outputs can often be less reliable due to various factors, including how models memorize factual knowledge.
6. Weak evaluation metrics: Given the small number of options in certain tasks, accuracy is a weak metric to fairly assess the performance, methods such as f1, precision, and recall provide more reliable results in such scenarios. ECE has limitations due to its reliance on binning, sensitivity to data distribution, and focus on average calibration. The choice of bins can introduce arbitrariness, affecting ECE values and leading to varying conclusions about a model’s calibration quality. Furthermore, ECE may be disproportionately impacted by bins with few data points, skewing results. As a summary statistic, it lacks detailed insights into calibration across specific confidence levels or types of inputs, making it less informative for models that need to distinguish varying degrees of incorrectness.

### Questions
1. Context of Application: Can the specific types of tasks that are most suitable for the wrong-over-wrong alignment approach be elaborated? This will help clarify the method's applicability and relevance.

2. The dataset creation process excludes correct answers and hence requires correct answers to be available. How does the paper reconcile this with the assertion that the method can be applied in contexts where ground truth is absent? A more detailed explanation is necessary.

3. Evaluation of Wrongness: What criteria were used to quantify the degree of wrongness in responses? Given the subjectivity involved, a detailed framework or methodology would enhance the validity of your evaluations.

4. The paper suggests that the model generates 4.5% more correct answers despite only aligning on wrong answers. What specific mechanisms can be hypothesized to contribute to this improvement? Further analysis could provide critical insights as it is noteworthy how without using correct answer information the model was able to perform better. 

5. The paper evaluated the method on ScieBench which can be considered a task close to theorem proving. But, it does not perform up to the mark on the task. Can the paper discuss the implications of your findings for other datasets or tasks and as to why the method lacked generalizability to the task?

6. Evaluation Metrics: Can the paper focus why accuracy was chosen as the primary evaluation metric? Given the small number of options in certain tasks, would it be more appropriate to use additional metrics such as F1, precision, and recall to better capture model performance?

7. The paper mentions potential benefits for low-resource languages. Can specific examples or preliminary results demonstrate how the method could be applied effectively in this context?

8. While LLM as a judge holds promise, to use LLMs to judge themselves for something as subjective as wrongness with lack of ground truth should be justified with empirical results demonstrating the robustness of the evaluation. Can further experiments be performed to address this considering the paper compares different models as judges as part of their evaluations. Additionally, to use LLM as a judge, previous examples have to be given to align the LLM for evaluations. Can the paper mention how the examples have to be chosen for a given task and calibration of the LLM judges and how were they selected?

9. Pairwise evaluations - The evaluation results are mostly in the range of random answers even with filtering. Can the paper have a deeper analysis that justifies these results not being random?

10. There is a huge variance in metric performance with 1 out of 22 overall scores being above 70 which is mentioned as 20 points better than random guessing while 12 of these reported overall scores are within 5 points of random guessing. Can the paper delve further into this as there is no consistent pattern that can help users choose the appropriate metrics, evaluators and method in general for their applications.

### Soundness
2

### Presentation
2

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
This article introduces an approach based on wrong-over-wrong preference for aligning Large Language Models to address the issue of high costs associated with obtaining ground truth in this field.

### Strengths
This idea is interesting and beneficial for the entire field.

The authors conducted experiments using several popular LLMs across multiple datasets. The results indicate that utilizing wrong-over-wrong preferences can lead to LLMs generating fewer incorrect answers.

### Weaknesses
In the experiments, the authors initially employed a proxy function to compute correctness scores based on ground truth, and then derived wrong-over-wrong preferences from these scores. I believe this process contradicts the motivation behind this work, as the resulting wrong-over-wrong preferences do not significantly differ from traditional right-over-wrong preferences obtained through similar methods.

The authors primarily relied on accuracy metrics. However, due to the lack of calibration mitigation in the baselines, these metrics are influenced by label distribution.

The baselines were limited to the original models, without comparison against some state-of-the-art (SOTA) alignment methods.

### Questions
see Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
