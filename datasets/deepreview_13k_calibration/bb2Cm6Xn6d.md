# Intriguing Properties of Large Language and Vision Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
Recently, large language and vision models (LLVMs) have received significant attention and development efforts due to their remarkable generalization performance across a wide range of tasks requiring perception and cognitive abilities. A key factor behind their success is their simple architecture, which consists of a vision encoder, a projector, and a large language model (LLM). Despite their achievements in advanced reasoning tasks, their performance on fundamental perception-related tasks (\eg MMVP) remains surprisingly low. This discrepancy raises the question of how LLVMs truly perceive images and exploit the advantages of the vision encoder. To address this, we systematically investigate this question regarding several aspects: \textit{permutation invariance}, \textit{robustness}, \textit{math reasoning}, \textit{alignment preserving} and \textit{importance}, by evaluating the most common LLVM's families (\ie LLaVA) across 10 evaluation benchmarks. Our extensive experiments reveal several intriguing properties of current LLVMs: (1) they internally process the image in a global manner, even when the order of visual patch sequences is randomly permuted; (2) they are sometimes able to solve math problems without fully perceiving detailed numerical information; (3) the cross-modal alignment is overfitted to complex reasoning tasks, thereby, causing them to lose some of the original perceptual capabilities of their vision encoder; (4) the representation space in the lower layers ($<25\%$) plays a crucial role in determining performance and enhancing visual understanding. Lastly, based on the above observations, we suggest potential future directions for building better LLVMs and constructing more challenging evaluation benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper looks at how Large Language and Vision Models (LLVMs) like LLaVA handle different tasks. It finds that LLVMs don’t rely much on image order, sometimes solve math without exact details, and lose some visual skills when fine-tuned for language tasks. The study also notes that the first layers process visuals best. The authors suggest building tougher benchmarks to better test and improve these models.

### Strengths
This paper is useful because it digs into how large language and vision models (LLVMs) really work with visual information. It shows that LLVMs are flexible, able to handle scrambled image pieces and solve math problems without all the visual details. It also highlights that when LLVMs are tuned for complex reasoning, they lose some basic visual skills. These findings can help make LLVMs better by balancing complex reasoning with simpler perception tasks, potentially guiding the creation of new, stronger models.

### Weaknesses
The paper would benefit from more precise and carefully scoped conclusions. While the experiments provide interesting observations, the claims drawn from them are often overly broad. For example: 1) The claim about permutation invariance is based on VQA tasks, but this alone cannot support a general conclusion about LLVMs' visual processing capabilities.
2) The benchmarks used don't adequately test basic visual skills to support such sweeping statements about visual understanding

Specificity Needed:
Each conclusion needs clear boundaries about when it applies and when it doesn't.
The paper makes approximately 10 major claims, but lacks sufficient context about their limitations and specific application scenarios.
More precise scoping of these findings would make them more actionable for future research.
Currently, the broad generalizations make it difficult for other researchers to build upon these results effectively.

Minor points:
Figure 5's text is too small to read effectively, hampering understanding of key results.

### Questions
Besides the weakness, to improve, I suggest the authors:

1. Clearly specify the conditions under which each conclusion holds
2. Acknowledge the limitations of their experimental setup
3. Provide more nuanced interpretations of their results
4. Consider additional experiments to support broader claims

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper analyzes some properties of LLVMs with respect to permutation invariance, mathematical reasoning, robustness to perturbations, and other aspects. The problem tackled is interesting and relevant to the VLM community. The authors analyze a wide variety of VLMs properties by focusing on the LLAVA family and a diverse set of classification/instruction following benchmarks.

### Strengths
* The paper addresses an important and timely problem that is of interest to the VLM community.
* Some observations made by the authors are insightful and have the potential to contribute to the understanding of VLMs.
* The set of analysis is diverse and has the potential to inform the  development of a new set of architectures/benchmark.
* Detailed set of benchmark datasets in the Appendix.

### Weaknesses
 * Many conclusions are not clearly backed up by evidence or rigorous analysis, which undermines their validity (I've given some examples in the questions section)
* Some observations appear to be cherry-picked (by dataset or sample?), which raises concerns about the representativeness and generalizability of the results. For instance, the authors want to evaluate the LLaVA family of models but some results are given on a single model and data sample while the conclusion is general (Figure 1 and Section 3.7 for instance, i've given more specific questions in the next section)
* The choice of datasets, metrics, and evaluation methods for different parts of the analysis is often unclear or unjustified, making it difficult to assess the generalizability of the findings.

### Questions
* The article focus on the LLaVA family. Could the authors  explain their rationale for focusing on the LLaVA family and discuss potential limitations in generalizing these results to other LVLM architectures?
* In Section 3.3, how is the grouping done to quantify local information in patches? How are neighbours defined, and what is the impact of this definition on the results?
* The explanation of backpropagation and loss signal coming from the assistant in line 234 is unclear. Can the authors provide more details or clarify the average performance drop, which seems to be benchmark-dependent?
* In Table 2, what setting is used to measure the frequency of outputting 1 (synthetic or original)? Is there a difference between these cases? Can the authors also report the frequency of outputting "no" and precision/recall for yes/no questions?
* Evaluating the loss of  cross-modal alignment is interesting. However the evaluation method used in Table 3 is unclear and may not be fair compared to a contrastive approach. Could the authors give more details about their evaluation setup (prompt used?) as it is known that prompt optimization impacts even zero-shot CLIP models classification performance.  Can the authors consider alternative approaches, such as log-likelihood comparison of description prompts (e.g., "Describe the image: This is an image of a [class label]")? As it is done in captioning models evaluation for instance?
* How is the 1k subset obtained in Table 3?
* The section on shared world concepts is hard to follow. What metric is used to measure alignment, and why was the DOCCI dataset chosen? How is alignment measured with long captions given CLIP's 77-tokens context?
* Are the local scores in Figure 8 averaged over the whole dataset or just one example? Same question for Figure 1 ? 
* Can the authors comment on the choices of datasets for different parts of the analysis (e.g., MMVet for localization of information, MMStar for layers importance)? Are these results model-, dataset-, or sample-specific, and how do they impact the generalizability of the findings? I know this question is quite general but the justification is not clear to me and the drawn conclusions seem to be a general so I would except such visualizations to be performed on a subset of the different datasets.
* The conclusion drawn from Figure 9 lacks a clear explanation of how the importance score is obtained. Can the authors provide more details on the method used (e.g., noised input or weights, which proportion)?

* In general it would help if the authors could : 
1. Provide explicit justifications for their dataset choices in each analysis section
2. Discuss potential limitations in generalizing results from specific datasets to broader conclusions
3. Consider extending their analysis to multiple datasets where feasible, or explain why this might not be possible or necessary

### Soundness
2

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
3

### Summary
This paper presents an empirical study of large vision language models with a focus on the llava model families using perception and reasoning tasks across various benchmarks. The authors revealed several findings of LVMs including image patch permutation invariance, overfitted cross-modal alignment, importance of lower block layers, etc..

### Strengths
The paper comprehensively evaluated several VLMs across various perception and reasoning benchmark to better understand their behavior and performance. These empirical findings could be valuable providing insights for model developments.

### Weaknesses
1. While the paper shows some good empirical studies of the LVM performance, they are loosely connected to the suggested future directions. This makes the contribution of the paper less clear. For example, the authors suggested "deeply consider innovative model architectures" in Sec 4 for enhancing cross modal alignment, yet it's not clear how this related to the empirical findings discussed in the previous sections and what necessary enhancements are entailed from their analysis.

2. The authors should consider toning down the rhetoric of the study from general LVMs to llava model families. Reported results do not show whether these findings would generalize to other LVMs as they are not evaluated yet.

3. Some of the findings are more or less expected, e.g., some degree of robustness to occlusion due to the robustness from image encoder. The conclusion from these findings are not clear. I suggest the authors append more focused discussions on a few key findings and tie them to any future directions or proposed improvements.

### Questions
Please see weaknesses above.

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
4

### Summary
This paper presents a detailed investigation of how vision is perceived in large language and vision models. Comprehensive experiments reveal the properties of LLVMs from multiple aspects including permutation invariance, robustness, math reasoning, alignment preserving and importance.

### Strengths
This paper elaborates on a critical problem in multimodal LLMs that how vision is perceived. It is a profound question which could benefit the future development of MLLMs.

### Weaknesses
The examples to be investigated in this paper are mainly from the LLaVA family whose vision representation is continuous. An analysis on discrete vision representation would be interesting.

### Questions
Please see weakness.

### Soundness
3

### Presentation
3

### Contribution
3
