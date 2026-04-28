# MONICA: Benchmarking on Long-tailed Medical Image Classification

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 5, 8

## Abstract
Long-tailed learning is considered to be an extremely challenging problem in data imbalance learning. It aims to train well-generalized models from a large number of images that follow a long-tailed class distribution. In the medical field, many diagnostic imaging exams such as dermoscopy and chest radiography yield a long-tailed distribution of complex clinical findings. Recently, long-tailed learning in medical image analysis has garnered significant attention. However, the field currently lacks a unified, strictly formulated, and comprehensive benchmark, which often leads to unfair comparisons and inconclusive results. To help the community improve the evaluation and advance, we build a unified, well-structured codebase called \textbf{M}edical \textbf{O}pe\textbf{N}-source Long-ta\textbf{I}led Classifi\textbf{CA}tion (\textbf{MONICA}), which implements over \textbf{30} methods developed in relevant fields and evaluated on \textbf{12} long-tailed medical datasets covering \textbf{6} medical domains. Our work provides valuable practical guidance and insights for the field, offering detailed analysis and discussion on the effectiveness of individual components within the inbuilt state-of-the-art methodologies. We hope this codebase serves as a comprehensive and reproducible benchmark, encouraging further advancements in long-tailed medical image learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors introduce the problem of long-tailed medical image classification and challenges in the field. Then they develop MONICA which is a package to benchmark various methods ranging from different loss functions, augmentations, etc on the benchmark datasets across medical image classification tasks. They provide an overview of datasets and methods and experiment results on the datasets. The authors additionally share learnings and observations.

### Strengths
- A good overview of the datasets curated for this work
- important contribution of decoupling the codebase
- A good overview of the method approaches
- practically useful to AI researchers in medical imaging

### Weaknesses
 - It would help to expand the benchmark datasets and bring in a canonical set for a field such as Camlyon for Pathology, etc. WILDS (medical subset) is a great example of a dataset to bring in to this benchmarking codebase
- Resnet-50 is used as a backbone but the community has generally moved on to more complex backbones such as ConvNext / Swin or foundation model backbones for different datasets. 
- Generally the community uses pretrained backbones rather than training the backbones from the scratch.
- The same backbone is used for every task for fairness but generally a sweep over backbones would help since different modalities and tasks require different approaches
- Top-1 accuracy is an in appropriate metric for model selection in imbalances settings and AUROC, AUPRC, F1 should be used
- error bars are missing in experiments
- More thorough error analysis
- Clearer articulation of novel insights
- Better connection to clinical relevance
- More detailed ablation studies

### Questions
- Are their any key trends that you'll observed across the board to narrow down the design space for the future across the general task space? The results are not convincing in any one direction across the board on tasks and methods
- Do you'll think stronger backbones can help learn better features?
- Did you'll consider trying complex augmentation techniques such as AugMix or even learned augmentations?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a unified benchmark for long-tailed learning in the medical domain by integrating several existing datasets and implementing a complete pipeline from data loading to model training and evaluation. The authors claim that the benchmark supports over 30 methods for comparison and provides an analysis of their performances.

- Update after the discussion phase:

Thank you for the detailed responses! I've raised my score. While my concerns are not entirely resolved, I believe with careful revisions, its future version has the potential to be accepted.

### Strengths
The paper attempts to provide a comprehensive benchmark for long-tailed medical image classification. The idea of integrating multiple existing methods and datasets into a unified platform could potentially be useful for researchers who want to compare various methodologies under a standardized framework.

### Weaknesses
1. Motivation. The paper lacks sufficient justification for evaluating long-tailed problems specifically in medical imaging tasks. While the authors mention some motivations at the beginning, these arguments are not convincing. Is there a fundamental difference between long-tailed problems in medical imaging and those in conventional tasks? Would this difference necessitate different methodologies? Even if the data modalities and evaluation methods are distinct (e.g., balanced vs. imbalanced test sets), would this lead to fundamentally different approaches? The paper analyzes multiple methods based on this premise but fails to provide insightful conclusions, which further deepens my skepticism about the motivation.

2. Dataset Contribution. Although the paper claims to use 12 datasets, 7 of these come from MedMNIST, and several of them are derived from previous work. This reduces the originality of the dataset contribution. Furthermore, the split between multi-class and multi-label datasets is 9/3, respectively. It is worth noting that many existing studies have already utilized MedMNIST for long-tailed learning (https://scholar.google.com/scholar?cites=11226954386823169312&scipsc=1&q=long+tail). Given that 7 out of the 12 datasets in this paper are from MedMNIST, why should users choose MONICA over MedMNIST, which already has extensive use and coverage in the medical imaging field? Additionally, the experimental methods used for multi-class and multi-label datasets are almost entirely different, and the analysis of multi-label results is limited to a single vague statement that multi-label classification is more challenging. This gives the impression that multi-label datasets were included just for the sake of completeness, rather than being a key focus.

3. Code Contribution. The code is not provided in the appendix, nor is there an anonymous GitHub link, which means the authors' claims about the code cannot be verified. By comparison, the NeurIPS D&B track (single-blind review) usually includes dataset or code links, along with information about author affiliations, licenses, and ethics. Although such links may be added after acceptance, this suggests that such work may not be well-suited for ICLR's double-blind review process.

    Additionally, the description of the code structure in Section 3.1 is not particularly informative. The modular design described is basic and lacks novel insights. A more impactful modular design, like in mmdetection, which breaks down components into backbone, neck, and bbox head, would have been more meaningful. As it stands, the description feels unnecessary.

4. Experimental Analysis Lacks of Insights. Comments below:

    - Despite using multiple datasets, the authors only provide a generic / systematic comparison of the methods without analyzing differences across domains. For example, there is no discussion about which methods are better suited for dermatology versus ophthalmology. Almost all discussion is very general, without any specific insights related to medical applications. This diminishes the value of using 12 datasets, as the conclusions drawn are not substantially different from what could be obtained from a single dataset.

    - The analysis in Section 4.2 is poorly organized. There is no clear structure, with the discussion jumping from evaluation metrics (e.g., "Curse of shot-based group evaluation") to re-sampling methods, MixUp, two-stage training, and even self-supervised learning in a seemingly random fashion. Many claims are also not supported by data. The overall takeaway from the experimental section is unclear, and I did not gain any insights on how to design better models.

    - In Section 4.1, there is inconsistency in the training strategies used: some methods use a unified training strategy, while others use the one specified in the original paper (e.g., SAM, Line 306), with no explanation for this discrepancy.

    - There are issues with the tables, such as Table 2, where it is unclear what methods like ERM, cRT, and LWS represent, as they are not referenced properly. Additionally, Section 3.2.3 does not fully align with the table.

    - The categorization of methods is confusing. The authors categorize methods into three types—class re-sampling, information augmentation, and module improvement—but later mention that re-sampling and MixUp are used in many methods, making the classification in Tables 2/3 somewhat meaningless.

    - The discussion on self-supervised learning (Line 398) appears out of place, as it is not introduced earlier.

    - Similarly, the mention of OOD detection (Line 421) is abrupt and lacks context.

    - The section on using an imbalanced validation dataset for checkpoint selection is unclear about its purpose. The conclusion seems to be that GCL exhibits lower fluctuations, but the reasoning and implications are not well explained. Additionally, Figure 4 lacks labels for the x and y axes, making interpretation difficult.

    - Line 475 suddenly states that multi-label classification is more challenging without providing adequate context or analysis.

    - Line 504 claims that "the most advanced long-tailed learning methods no longer focus on improving a single strategy," but this claim is not well-supported by the preceding analysis.

### Questions
See weakness sections. Some more questions below:

Could you elaborate on why the results of self-supervised learning and OOD detection are relevant in this paper? They seem out of place given the main focus on long-tailed classification.

Why did the authors not include a domain-specific analysis (e.g., which methods work better for certain medical fields)? It seems like an important missed opportunity.

### Soundness
2

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
5

### Summary
This work introduced Medical OpeN-source Long-taIled ClassifiCAtion (MONICA), a comprehensive benchmark for long-tailed medical image classification (LTMIC). It includes a unified, well-structured codebase integrating over 30 methods developed in relevant
fields and 12 long-tailed medical datasets covering 6 medical domains.

### Strengths
Long-tailed learning is an extremely challenging problem, this work can serves as a comprehensive and reproducible benchmark, encouraging further advancements in long-tailed medical image learning.

It covers most of the strategies that deal with long-tailed problems, and also include 12 datasets from different application domains.

### Weaknesses
This work doesn't introduce any new datasets or methods. It is a collection of datasets (multi class or multi label) that are already publicly available without justifications as they are many other such kind of long tail datasets available. Also, they have changed some of the original datasets, it would not be useful if they don't share the modified datasets.

They only tried ResNet for the tasks, would be nicer to make comparisons with other models. Also the discussions on SSL models seem not supported by any data.

### Questions
Some of the datasets have been changes in terms of distributions, would you share the modified datasets or the code on making the changes?

What are the performance of the SSL models?

There are some typos such as quotation markers etc, please correct.

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
4

### Summary
This paper presents a framework and codebase for structured benchmarking of long-tailed (LT) learning methods on various medical image classification tasks. The benchmark, MONICA, implements over 30 LT learning methods, with comprehensive experiments assessing performance across 12 LT medical image classification datasets spanning 6 different modalities. The experiments analyze which methods, and categories of methods, provide the most benefit to LT medical image classification across tasks in a controlled environment.

### Strengths
- This work addresses an important problem, namely the variability in dataset/hyperparameters/etc. when evaluating LT learning methods for medical image classification tasks. These variations in setting make head-to-head comparisons difficult, so MONICA serves to provide a “fair playing ground” for these LT learning methods.
- The framework will become publicly available and should serve as an extensible resource going forward for LT medical image classification research.
- The organization and presentation quality of the paper is strong, with helpful use of formatting (typesetting, color, etc.) and high-quality figures.
- Experiments are very thorough, spanning many relevant methods, datasets, and tasks.
- Discussion is thoughtful, going beyond simply displaying all benchmark results. The authors try to synthesize takeaways, provide caveats/limitations, assess out-of-distribution performance, and more.

### Weaknesses
 - Writing can be improved throughout. See specific comments below for examples of awkward wording, inconsistent naming, grammatical errors, etc.
- It is possible that choosing a fixed set of hyperparameters across methods unintentionally advantages certain methods. Ideally, one could argue that each method should be individually tuned on each task; however, I am aware that this would require a vast amount of resources and time, so I do not consider this a major limitation. More practical solutions to enhance the benchmark would be the following: (i) uncertainty estimates should be provided (e.g., bootstrapped confidence intervals or standard deviations over multiple runs), and (ii) multiple performance metrics should be provided (e.g., AUROC).
- The two paragraphs “LTMIC improves out-of-distribution detection” and “Using imbalanced validation dataset for checkpoint selection” are not properly set up. For the former, what does it mean to use “ImageNet as OOD samples, with 1,000 randomly selected images”? What exactly is the task, how is it formulated, and how are experiments conducted? Further, why do we care about this model behavior? For the former, Figure 4 and its findings are confusing – why exactly does this demonstrate “stable convergence”? My general advice: **Use the methods section to describe and prepare the reader to understand everything that appears in the results**. When I come to these results sections, I should already have an idea of what experiments you have performed.

**Minor comments/questions:**
- Avoid editorializing with value judgments: “benchmark is **meticulously** designed”; “we… develop a… **well-structured** codebase”; “our work provides **valuable** practical guidance”. Simply present your work and let the reader make these judgments!
- “data imbalance learning” is not a phrase I have heard. Perhaps “imbalanced learning”?
- “unified, strictly formulated, and comprehensive benchmark”. Unsure what “strictly formulated” means. Could simply say “unified, comprehensive benchmark”
- “we build a… codebase…, which implements over 30 methods… and evaluated on 12… datasets”. It seems that “evaluated on” is the wrong tense; also, what is being evaluated?
- This does not belong in an abstract: “We hope this codebase serves as a comprehensive and reproducible benchmark, encouraging further advancements in long-tailed medical image learning.”
- Often unnecessary inclusion of “the” before concepts: “The deep learning techniques”; “the collected image datasets”; “the long-tailed imbalance”
- “The deep learning techniques have proven effective for most computer vision tasks benefiting from the grown-up dataset scale.” Remove “The”; what does “grown-up dataset scale” mean? “Grown-up” is not the right adjective – be more concrete.
- Refrain from claims like “always result” (line 57) – soften to “usually” or similar
- Confused by this justification: “it is vital to recognize these rare diseases in real-world practice, as they are relatively rare for doctors and may also lack diagnostic capacity.” This reads as “it is vital to recognize rare diseases because they are rare”.
- Line 65: can change “contributions, i.e.,” -> “contributions:”
- Be consistent with capitalization/presentation of terms: “Re-sampling” vs “re-sampling”; “Module improvement” vs. “Module Improvement”; “mnist” vs. “MNIST”; “mixup” vs. “MixUp”; etc.
- Line 82: “we are still curious to explore”. Perhaps just “we aim to explore”?
- “The partition schemes are vita important”. What does “vita” mean?
- The last two paragraphs of the introduction are probably better off being formatted as bulleted or numbered lists. Also, it is unclear why these numbered lists are formatted differently: **1) xxx.** vs. (1) xxx.
- “of class $k$ where $ho$ denoted as imbalance ratio”. The phrase “denoted as” is awkward + need a comma after $k$
- “a common assumption in long-tailed learning is when the classes are sorted by cardinality in decreasing order” I’m not sure what this means or why this represents an “assumption”. I would just remove this sentence since it does not seem to be used later.
- Line 144: “is a long-tailed version constructed from”. Need to say it is a version “of” something; alternatively, use a word other than “version” like “dataset”
- Inconsistent spacing/use of commas in numbers. “10, 015” -> “10,015”; “3200 fundus images” -> “3,200 fundus images”
- Inconsistent spacing around commas and colons: “training/off-site testing / on-site testin”; “7 : 1: 2”; etc.
- “Liver Tumor Segmentation Benchmark” -> “the Liver Tumor Segmentation Benchmark”
- I realize it is hard to categorize some methods into one bin but GCL loss going in Information Augmentation is interesting, particularly since all other losses fall under re-sampling. It seems to also have module improvement as well.
- “Causal classifier (Tang et al., 2020) resorted to causal inference for keeping the good and removing the bad momentum causal effects in long-tailed learning.” The phrase “resorted to” is strange and has a negative connotation; also, what do “good” and “bad” mean?
- “All these designs are for the fairness and the practicality of the comparison on the benchmark.” Too vague – in what specific way do these support fairness?
- Table 3: Inconsistent “Avg” vs “Avg.” vs “avg”
- Table 4: Consider using a line break occasionally (so one loss function occupies two rows). This would allow you to use a larger font size. Also, be consistent “CrossEntropy” vs “CE”?
- “assessing MixUp based solely on performance is not fair”. Soften to “may not be fair”
- “led to a significant performance decline, e.g,”. Refrain from saying “significant” without statistical significance test + change “e.g,” -> “e.g.,”
- “Use two-stage training as a general paradigm” sounds like a command. Perhaps “Using”?
- Define “SSL” acronym at first use
- “Modify classifier to reduce prediction bias” -> “Classifier modification to reduce prediction bias”
- “In Fig. 2, We visualize” -> “In Fig. 2, we visualize”
- Table 5 indicates the meaning of asterisk, which is never used in the table.
- “models with larger parameters”. The parameters are not “larger” – could say “more parameters” or “a larger parameter count” perhaps.

### Questions
- Is it possible that the chosen hyperparameters used across all methods happen to be more advantageous for certain methods and suboptimal for others? In one sense, using the same set of hyperparameters across methods appears “fair”; however, it may actually be more fair to individually tune each method on each task. I recognize the difficulty of conducting fair comparisons in such a large-scale experimental setting, where it is costly to, e.g., run multiple trials of all experiments. I am not asking the authors to necessarily perform such experiments, but rather to consider this point and perhaps comment on it as a limitation/consideration.
- Can the authors provide a summary of practical suggestions for which methods to use in a few sentences near the Conclusion?
- I might suggest including the **rank** of each method on a given task in all tables. This would also enable you to *quantitatively* assess method performance across tasks (which method has the lowest average/median rank overall?). To make this work logistically (fit all columns in the table), you may need to reduce the precision to one decimal place, e.g.
- The two paragraphs “LTMIC improves out-of-distribution detection” and “Using imbalanced validation dataset for checkpoint selection” are not properly set up. For the former, what does it mean to use “ImageNet as OOD samples, with 1,000 randomly selected images”? What exactly is the task, how is it formulated, and how are experiments conducted? Further, why do we care about this model behavior? For the former, Figure 4 and its findings are confusing – why exactly does this demonstrate “stable convergence”? My general advice: **Use the methods section to describe and prepare the reader to understand everything that appears in the results**. When I come to these results sections, I should already have an idea of what experiments you have performed.

**Minor comments/questions:**
- Avoid editorializing with value judgments: “benchmark is **meticulously** designed”; “we… develop a… **well-structured** codebase”; “our work provides **valuable** practical guidance”. Simply present your work and let the reader make these judgments!
- “data imbalance learning” is not a phrase I have heard. Perhaps “imbalanced learning”?
- “unified, strictly formulated, and comprehensive benchmark”. Unsure what “strictly formulated” means. Could simply say “unified, comprehensive benchmark”
- “we build a… codebase…, which implements over 30 methods… and evaluated on 12… datasets”. It seems that “evaluated on” is the wrong tense; also, what is being evaluated?
- This does not belong in an abstract: “We hope this codebase serves as a comprehensive and reproducible benchmark, encouraging further advancements in long-tailed medical image learning.”
- Often unnecessary inclusion of “the” before concepts: “The deep learning techniques”; “the collected image datasets”; “the long-tailed imbalance”
- “The deep learning techniques have proven effective for most computer vision tasks benefiting from the grown-up dataset scale.” Remove “The”; what does “grown-up dataset scale” mean? “Grown-up” is not the right adjective – be more concrete.
- Refrain from claims like “always result” (line 57) – soften to “usually” or similar
- Confused by this justification: “it is vital to recognize these rare diseases in real-world practice, as they are relatively rare for doctors and may also lack diagnostic capacity.” This reads as “it is vital to recognize rare diseases because they are rare”.
- Line 65: can change “contributions, i.e.,” -> “contributions:”
- Be consistent with capitalization/presentation of terms: “Re-sampling” vs “re-sampling”; “Module improvement” vs. “Module Improvement”; “mnist” vs. “MNIST”; “mixup” vs. “MixUp”; etc.
- Line 82: “we are still curious to explore”. Perhaps just “we aim to explore”?
- “The partition schemes are vita important”. What does “vita” mean?
- The last two paragraphs of the introduction are probably better off being formatted as bulleted or numbered lists. Also, it is unclear why these numbered lists are formatted differently: **1) xxx.** vs. (1) xxx.
- “of class $k$ where $\rho$ denoted as imbalance ratio”. The phrase “denoted as” is awkward + need a comma after $k$
- “a common assumption in long-tailed learning is when the classes are sorted by cardinality in decreasing order” I’m not sure what this means or why this represents an “assumption”. I would just remove this sentence since it does not seem to be used later.
- Line 144: “is a long-tailed version constructed from”. Need to say it is a version “of” something; alternatively, use a word other than “version” like “dataset”
- Inconsistent spacing/use of commas in numbers. “10, 015” -> “10,015”; “3200 fundus images” -> “3,200 fundus images”
- Inconsistent spacing around commas and colons: “training/off-site testing / on-site testin”; “7 : 1: 2”; etc.
- “Liver Tumor Segmentation Benchmark” -> “the Liver Tumor Segmentation Benchmark”
- I realize it is hard to categorize some methods into one bin but GCL loss going in Information Augmentation is interesting, particularly since all other losses fall under re-sampling. It seems to also have module improvement as well.
- “Causal classifier (Tang et al., 2020) resorted to causal inference for keeping the good and removing the bad momentum causal effects in long-tailed learning.” The phrase “resorted to” is strange and has a negative connotation; also, what do “good” and “bad” mean?
- “All these designs are for the fairness and the practicality of the comparison on the benchmark.” Too vague – in what specific way do these support fairness?
- Table 3: Inconsistent “Avg” vs “Avg.” vs “avg”
- Table 4: Consider using a line break occasionally (so one loss function occupies two rows). This would allow you to use a larger font size. Also, be consistent “CrossEntropy” vs “CE”?
- “assessing MixUp based solely on performance is not fair”. Soften to “may not be fair”
- “led to a significant performance decline, e.g,”. Refrain from saying “significant” without statistical significance test + change “e.g,” -> “e.g.,”
- “Use two-stage training as a general paradigm” sounds like a command. Perhaps “Using”?
- Define “SSL” acronym at first use
- “Modify classifier to reduce prediction bias” -> “Classifier modification to reduce prediction bias”
- “In Fig. 2, We visualize” -> “In Fig. 2, we visualize”
- Table 5 indicates the meaning of asterisk, which is never used in the table.
- “models with larger parameters”. The parameters are not “larger” – could say “more parameters” or “a larger parameter count” perhaps.

### Soundness
4

### Presentation
3

### Contribution
3
