# The Challenging Growth: Evaluating the Scalability of Causal Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 3, 8

## Abstract
One of the pillars of causality is the study of causal models and understanding under which hypotheses we can guarantee their ability to grasp causal information and to leverage it for making inferences.
Real causal phenomena, however, may involve drastically different settings such as high dimensionality, causal insufficiency, and nonlinearities, which can be in stark contrast with the initial assumptions made by most models.
Additionally, providing fair benchmarks under such conditions presents challenges due to the lack of realistic data where the true data generating process is known.  
Consequently, most analyses converge towards either small and synthetic toy examples or theoretical analyses, while empirical evidence is limited.   
In this work, we present in-depth experimental results on two large datasets modeling a real manufacturing scenario. 
We show the nontrivial behavior of a well-understood manufacturing process, simulated using a physics-based simulator built and validated by domain experts. 
We demonstrate the inadequacy of many state-of-the-art models and analyze the wide differences in their performance and tractability, both in terms of runtime and memory complexity. 
We observe that a wide range of causal models are computationally prohibitive for certain tasks, whereas others lack in expressiveness. 
We release all artefacts to serve as reference for future research on real world applications of causality, including a general web-page and a leader-board for benchmarking.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a critical evaluation of the scalability and effectiveness of current causal models through extensive empirical analysis on two novel large-scale manufacturing datasets. The authors demonstrate significant limitations in both causal inference and discovery methods when applied to realistic, complex scenarios. The work provides valuable insights into the practical challenges of applying causal models to real-world problems and releases new benchmark dataset for research in high-dimensional causality.

### Strengths
The paper addresses real-world manufacturing scenarios and incorporates domain knowledge thus having high practical relevance.

There's a rigorous empirical evaluation with multiple experimental settings and ablation studies.

### Weaknesses
The dataset is very specific which while valuable there should be more domains considered (e.g. biological networks that have different DGP distributions).

Mixing two evaluations in one. I feel that this could be two papers each expanding on different sides of causal modeling. One for scalability of causal discovery methods and one for causal inference. This would have the room to expand on insights and evaluations.

Odd result regarding linear regression (check questions).

### Questions
Missing related work: 
https://arxiv.org/abs/2406.03209 studies bayesian causal discovery methods.

Why are there both logistic and linear regression as baselines? I understand that the outcome is a binary variable so why use linear regression? Also, for logistic regression, is MSE the appropriate metric?

Also, I would like to understand the linear regression performance a bit better. What is the groundtruth DGP considered? What is the non-linearity involved? I think it's possible to construct a non-linear SCM for which linear regression would fail and many applications will be more non-linear than linear. Can you provide plots of what the models learned in each case vs what's the groundtruth function (or samples)? 

Regarding CausalMan. How do the SCMs proposed here better than other simulators out there (e.g. https://gnw.sourceforge.net/dreamchallenge.html for gene regulatory networks)? I understand this is a different domain but why a different domain makes it better? How do you evaluate the quality of the SCMs you propose? I would like to understand why this is a great benchmark and the paper doesn't provide sufficient evidence.

In table 2. the MMD entry for CNF is Nan. Is this by accident?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Real-world causal phenomena often diverge significantly from common assumptions such no latent confounder. These disparities pose substantial challenges to create fair benchmarks due to the scarcity of realistic data with a known data-generating process. This paper presents an extensive experimental evaluation using two large datasets that simulate a real manufacturing scenario with a physics-based model validated by experts in the field. This findings reveal significant performance and scalability limitations in many state-of-the-art causal models, highlighting wide variability in runtime and memory demands.

### Strengths
1. This paper addresses one of the most critical challenges in causality: benchmarking different causal models with a particular focus on the scalability and applicability. 
2. Overall, the paper is well-structured and clearly written. 
3. The experiments are extensive, covering seven causal discovery algorithms and five evaluation metrics.

### Weaknesses
1. Why not consider and model the measurement error during CAUSALMAN simulation? 
2. How to obtain the ground-truth of two CAUSALMAN datasets? Simply by domain expert? Could you please provide more details on the validation process used by the domain experts or any quantitative measures used to ensure the accuracy of the ground truth?
3. According to your experiments, if you were to recommend one most reliable causal discovery method for real-world datasets, what would it be? Based on your experiments, what are the key trade-offs between the most promising causal discovery methods for real-world datasets in terms of accuracy, scalability, and robustness to different types of data?

### Questions
(See above)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a new benchmarking dataset for causal inference and discovery that is meant to mimic a manufacturing process. The simulator is “hand-tuned” by “domain experts” with the goal of obtaining a benchmarking dataset that is more realistic that existing benchmarking results.

### Strengths
The paper studies the challenge of benchmarking in the field of causality, which is an important problem that benefits from more work and proposals for datasets.

### Weaknesses
This paper is not of high quality, has no clear (scientific) contribution, is not reproducible, and is not written well. 
First, the proposed data-generating process is not described properly. There are no equations that formalize the system that is simulated, which makes the proposed benchmark not reproducible and impossible to analyze for researchers. Moreover, none of the simulation choices are justified scientifically based on any evidence beyond the claim that “domain experts” were involved in designing the data-generating process. The work provides no evidence that their released dataset is “realistic”, in whatever interpretation of “realistic” on may consider, compared to the existing benchmarking datasets referenced in Section 2. Specifically, the work does not justify what exactly is wrong with existing synthetic and semisynthetic benchmarking settings and in what we the proposed dataset resolves it (e.g., type of causal mechanisms, variance artefacts, signal to noise ratio, causal structure, etc). Independent of these points, the writing is not polished, and the font in most figures is unreadable.

### Questions
n/a

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper provides two datasets from simulators of a real-world manufacturing process. The simulators are large SCMs constructed with the support of domain experts, with different numbers of nodes (referred to as small and medium).

With the datasets, the authors provide a synthetic benchmark for different causal inference tasks, which address some shortcomings in other synthetic datasets, by providing (1) high-dimensional data (53 and 186 nodes), (2) causal insufficiency (both datasets have a large number of unobserved confounders), and (3) structural assignments, such as non-linearities, categorial variables and other artifacts, and sampling procedures (batching) which are not commonly studied in causal inference but may be realistic in manufacturing scenarios.

The authors then evaluate a cohort of causal models and causal discovery algorithms on the datasets.

### Strengths
The scarcity of meaningful benchmarks in causal inference is a serious problem. Efforts to produce new benchmarks from both real-world data or complex, well-motivated simulators are direly needed.

The authors make a valuable contribution to these efforts by providing datasets from what appears to be a complex, well-motivated simulator built together with domain experts, in an understudied field (manufacturing) that holds promise for the applications of causal inference, e.g., root cause analysis of manufacturing failures, etc. I appreciate the immense effort in building such a large simulator while integrating the feedback of domain experts.

In my opinion, the introduction and background are well-written and provide enough pointers to the relevant literature.

### Weaknesses
In my opinion, there are some weaknesses that depreciate the otherwise valuable contribution of the paper. If addressed, I would be happy to raise my score.

At a high level, these are: a limited experimental section (W1), some unsubstantiated or bold claims (W2), not releasing the simulator (W3), and a deterioration of the writing in the latter parts of the paper (W4).

- W1: The experiment section of the paper (case studies and results) felt quite limited.
  - W1.1: For the ATE case study: the two tasks, while valuable as sanity checks to show the shortcomings of causal models, seemed somewhat constructed and limited. I feel there is a missed opportunity to present an exciting task representative of the real-world manufacturing scenario that the simulator tries to capture. An example (without much knowledge of the topic), could be predicting the effect of an intervention where the parameters of some manufacturing step are modified to see if this has an effect on the quality of the end product. After downloading the dataset, I see such interventions are indeed present, but this was not clear from a first read, which initially made the benchmark and the contribution look very limited. I would recommend adding another task or at least explicitly mentioning that many further experiments are possible with the data you provide (and maybe even offering examples with your code).
  - W1.2: Linear regression outperforms models in the ATE task. This seems like an important outcome from the experiments, particularly from the perspective of a practitioner. However, no discussion is provided, and few details are given to facilitate analysis. Is the regression on all other variables in the dataset? Is the variable indicating the success of the production process a sink node in the graph? If so, this behavior is to be expected in an SCM (i.e., the only variables in its Markov blanket are its parents).
  - W1.3: The results for the causal discovery case studies in section 6.0.2 (Tables 6, 7 and Figure 5) are hidden away in the appendix. This made reading this section somewhat cumbersome and initially made me suspect you had something to hide. If this is due to a lack of space, it would help to state this explicitly.
  - W1.4: Some figures (e.g., 3,4,5) appear to have been made in a rush, e.g., Figure 3 doesn’t list the time units (I guess seconds?), and the x-label should be something like “Causal Discovery Method”; the legend could directly say “Dataset: Small / Medium” instead of “Dataset 1 / Dataset 2”. Or, figure 4 and 5 have inconsistent labels for the y axes, even though they show the same quantity (SHD).
  - W1.5: You mention how the SHD metric is not relevant from large graphs, but still use it as a metric for your results in the causal discovery section. This makes it difficult to get a clearer view of the results to motivate further research and other interesting experiments, which is the unstated goal of a benchmark paper. Showing results for additional metrics [1,2] would help, or at least mentioning that there are alternatives as you talk about the limitations of the SHD.
- W2: Some claims about the datasets are too bold or must be taken at face value. For example:
  - W2.1: In the abstract it says, “we show the nontrivial behavior of a well-known manufacturing process”. Given that there is no real-world data from the actual manufacturing process, I am not sure how you show this. Furthermore, even when it comes to the simulator, I couldn’t find support for this claim, except perhaps the single example about categorical parents in appendix B.1. You describe elements of this complexity in section 4.1 and 4.2, but from the line in the abstract I expected some sort of “evidence”, e.g., some visualization of data (the effect of batching or some non-standard structural assignments). It would also be super helpful to give the explicit expression of some of the structural assignments, e.g., in the appendix.
  - W2.2: Similarly, in line 296 you say “this complex sampling procedure gives rise to rich and heterogeneous datasets”. Since the datasets are the key contribution of the paper, I would have expected some visualization.
  - W2.3: In line 512 you write “our datasets are first of their kind [because we used expert knowledge]”. You are not the first to do this, as other synthetic datasets are also produced with ample domain-expert knowledge (e.g., the DREAM4 challenge [3], or the Neuropathic Pain simulator that you cite in the introduction). I would soften this claim as it's not necessary: you are already making a valuable contribution without it being true.
- W3: By providing two datasets instead of the simulators themselves, the authors limit the potential contribution of this work. I understand that providing user-friendly software comes with complications, and I am happy to consider doing so as out-of-scope. However, sharing at least the simulator code would greatly increase the contribution of the paper, and I would encourage the authors to do this if possible. I apologize if you do provide this and I missed the link to the codebase.
- W4: While the introduction and background are well written, the writing quality progressively deteriorates as the paper goes on. I’ve added some pointers in the “questions” section below.

### Questions
In no particular order:

1. In related work / datasets and benchmarks: in the paragraph about real-world data, I would also reference [1,2], e.g., after referencing the causal chambers, I would add “Additionally, [1,2] provide real-world datasets with a more or less justified ground-truth causal graph.”
2. In the discussion, under limitations, it would be good to remind the reader that all the usual limitations of synthetic data still apply. For example, the simulators are structural causal models, which means one cannot use this benchmark to evaluate whether these causal models are good models of reality.
3. For the complete ground-truth graphs of appendix F, would it be possible to color the nodes according to observable/hidden variables? This would greatly improve readability and make the different confounding structures visible.
4. Paragraph 412-413: The paragraph offers an explanation as to why causal models are preferable to regression-based techniques. However, the reasoning contradicts the results, since a simple regression drastically outperforms all methods despite having confounders in the data. Could you elaborate on this?
5. Wording / typos
- Line 297: “to a rich and [...] datasets” -> “to rich and [...]” or datasets in singular.
- Line 266: “obtaining” -> “obtained”
- Line 021: “well-known” -> “well-understood” as it’s not like the manufacturing process is “famous” :)
- Line 408: The sentence around “a slightly harder” seems incorrect -> “which is slightly harder” or “a slightly harder task”
- Line 332: section title “Case-Studies” should be “Case Studies” without a hyphen
- Line 394: Section number is 6.0.1 -> shouldn’t this be 6.1 instead?
- Line 1010: “way run” -> “we run?”
- Line 412: “those causal models”. Which causal models are you referring to here? Do you mean “all causal models”.
- Line 468: “Tables 6 and 7 shows” -> “show”
- Lines 258: very minor and pedantic comment: it appears you wrote “i.e.” instead of “i.e.\” in latex and you have a full space. Also, in modern American English these latinisms should be followed by a comma, e.g., “i.e.,”


[1] Mogensen, S. W., Rathsman, K., & Nilsson, P. (2023). Causal discovery in a complex industrial system: A time series benchmark. arXiv preprint arXiv:2310.18654.
[2] Mhalla, L., Chavez-Demoulin, V., & Dupuis, D. J. (2020). Causal mechanism of extreme river discharges in the upper Danube basin network. Journal of the Royal Statistical Society Series C: Applied Statistics, 69(4), 741-764.

### Soundness
2

### Presentation
2

### Contribution
3
