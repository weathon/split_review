# MOGIC: METADATA-INFUSED ORACLE GUIDANCE FOR IMPROVED EXTREME CLASSIFICATION

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Retrieval-augmented classification and generation  models significantly benefit from the *early-stage fusion* of high-quality text-based auxiliary metadata, often called memory, but they suffer from high inference latency and poor robustness to noise. In classifications tasks, particularly the extreme classification (XC) setting, where low latency is critical, existing methods incorporate metadata for context enrichment via an XC-based retriever and obtain the representations of the relevant memory items to perform *late-stage fusion* to achieve low latency. With an aim of achieving higher accuracy while meeting the low latency constraints, in this paper, we propose MOGIC, an approach for metadata-infused Oracle guidance for XC tasks. In particular, we train an early-fusion Oracle classifier with access to both query-side and label-side ground-truth metadata in the textual form. The Oracle is subsequently used to guide the training of any existing memory-based XC Disciple model via regularization. The MOGIC algorithm, when applied to memory-based XC Disciple models such as OAK, improves precision@1 and propensity-scored precision@1 by ~2% on four standard datasets, at no additional inference-time costs to the Disciple model. We also show the feasibility of applying the MOGIC algorithm to improve the performance of state-of-the-art memory-free XC approaches such as NGAME or DEXA, demonstrating that the MOGIC algorithm can be used atop any existing XC-based approach in a *plug-and-play* manner. Finally, we also show the robustness of the MOGIC method to missing and noisy metadata settings. We will release code on acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
In this paper, the authors propose MOGIC to leverage an additional oracle model and metadata for extreme classification. In the first phase, an oracle model for early fusion is trained with metadata. Then a smaller encoder with the same architecture as OAK is trained by distilling the oracle model with auxiliary losses in the second stage. The experiments are conducted on some benchmark datasets based on Wiki. The experimental results show that the MOGIC framework can improve OAK across all datasets. The authors also conducted several studies to demonstrate the effectiveness of each component. Besides, there is also a theoretical analysis of the loss used in the distillation.

### Strengths
* Great improvements over different base models.
* Both alignment and matching to approach the Oracle model are helpful.
* Good theoretical analysis for the framework and optimization losses.

### Weaknesses
 * The experiments only use the Wiki datasets, so the framework is unproven for other domains, such as e-commerce like Amazon datasets.
* Performance gaps between baselines and MOGIC are unclear about whether they are from the framework, pre-trained oracle model, or ground-truth metadata in training. It's hard to isolate the contribution of each component.
* Lack of reports and analysis on training and inference time when the authors emphasize the efficiency. The practical feasibility of the approach is not fully established.
* Writing and organization can be improved. The paper would benefit from a clearer explanation of key concepts, such as predicted and ground-truth metadata, earlier in the text.

### Questions
* I wonder whether the two-stage framework is needed when it could be feasible to train models directly with "ground-truth" metadata (and, of course, use the predicted metadata during inference). It would be great to patch an experiment to demonstrate the benefit of this two-stage design.
* I guess PCA is one of the main reasons why Phi-2 and LLaMA-2-7b underperform DistiBERT as oracle models, especially the authors do not provide more details. I would suggest also reporting the performance without PCA, even if it would take a longer time.
* It would be great to patch an efficiency analysis for both training and inference.
* I would also suggest polishing the writing and organization to ease the reading. For instance, the concept of predicted and ground-truth metadata are not explained until the experiment section, but the term ground-truth metadata is used throughout the whole paper.

### Soundness
3

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
2

### Summary
This work proposes MOGIC, a method for achieving high accuracy, low latency extreme classification (XC). In MOGIC, the authors first train an expensive early-fusion oracle classifier that can access metadata as text. Subsequently, this oracle is used to regularize the training of existing XC methods like OAK. This consistently improves quality by a couple of percentage points when applied over a variety of XC methods, including OAK, DEXA, and NGAME, on a few XC datasets.

### Strengths
1. The authors conduct evaluation on several benchmarks and by applying MOGIC over three different XC baselines, and show consistent gains across the board. This suggests the method has some fundamental additive capacity to add to the field of XC.

2. The proposed method balances quality and cost, while boosting quality over baselines. This type of improvement is encouraging to see.

### Weaknesses
1. The paper is not particularly easy to follow. In particular, while I appreciate the potential generality of the proposed framework, the current presentation comes at the cost of concreteness. For one, the paper needs an end-to-end example of how different components interact with a given query at training and inference time, e.g. how OAK works and how OAK via MOGIC works. In general, the descriptions of the task and the oracle are a lot more complicated than I think they need to be. The lack of a concrete example makes it difficult to understand the flow of information, particularly how the query, metadata, and labels are processed and used in the different stages of training and inference. For instance, it's unclear how the metadata is selected and incorporated into the query representation, and how this process differs between the oracle and the disciple model.

2. Building on #1, the discussion of the oracle, saying things like "Oracle leads to very high accuracy on the downstream XC task but is computationally expensive to deploy. It entails too high inference times for any real world application, due to the large context length" is quite perplexing. An "oracle" suggests to me access to privileged information, generally not available at test time; if so, the computational cost is the least of anyone's concerns for deploying the oracle. (I imagine I simply do not fully understand this section!) When the authors discuss presenting the "Labels" to the oracle, I'm left unsure if they mean concatenating all 312,000 labels (is this why the context is so long?) or the ground truth labels (why is that long, in that case?). Overall, the discussion of the oracle and the overall pipeline is fairly opaque. It is not clear what information is available to the oracle that is not available to the disciple, and how this privileged information is used during training. The paper needs to clarify the exact nature of the oracle's inputs and outputs, and how they differ from the disciple's.

2. Given the increased training-time cost, and the complexity of the method (at least as currently presented notationally, see weakness #1), gains of 1-2 percentage points with a fairly standard intuition (i.e., distilling an expensive oracle) may not be the most rewarding tradeoff, in a way that weakness the core contribution of this work. The paper needs to provide a more detailed analysis of the computational cost of MOGIC, including both training and inference time, and compare it to the baselines. The marginal gains need to be justified in light of the added complexity and computational burden, especially considering that the core idea of distilling an expensive oracle is not novel.

### Questions
1. The authors write "XC tasks involve sparse query representation, and are short-text in nature". Is this key to the contribution here? It just seems like an inaccurate/overly general statement, e.g. see BioDEX as a fairly standard XC task where the queries are anything but short.

2. The paper says "discipline" 3 times. Is this a typo? Is it supposed to be "disciple"?

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
3

### Summary
The paper's focus is Extreme Classification (XC) tasks, in which the goal is to achieve high-accuracy within low-latency constraints. To address these challenges, the authors introduce MOGIC, which is a novel approach for metadata-infused oracle guidance for XC tasks. MOGIC is a 2-step process: first, it trains an early-fusion oracle classifier with access to both query- and label- side ground-truth textual metadata; then this oracle is used to guide the training of any existing memory-based XC student model via regularization.

### Strengths
The motivating problem (XC) has clear practical applicability, and the proposed approach (MOGIC) appears to be novel. Due to the paper's barely-fair organization and poor writing (including many non-grammatical and/or ambiguous statements that are difficult & time-consuming to parse), it is difficult to judge the paper's likely significance and impact.

### Weaknesses
The paper has two main weakness: (1) it lacks any latency numbers for a problem (XC) in which latency is critical, and (2) it is extremely difficult to read and comprehend due to its poor writing (e.g., long, ambiguous sentences, and dozens of missing articles) and a no-better-than-fair organization. All of this makes it extremely challenging to judge the paper's contributions and expected significance/impact.  

1. ABSTRACT
- given the centrality of latency in XC, please add a sentence that summarizes MOGIC's latency and how it compares to existing approaches
- whenever you make claims on accuracy gains (eg, line 24), please quantify the claim as follows: "MOGIC improves P@1 by X%, from Y% to Z%". To be informative, the X% value must be judged in the context of Y% and Z%

2. Introduction
- please intuitively define/introduce, ideally with an illustrative example, all the key concepts of the paper: early/late-stage fusion, metadata-infused oracle, memory-based/free models, query-/label-side ground-truth, etc
- please restructure and re-write this section along the lines of the one in [Mohan et al, 2024]. That paper's introduction is easy to read and assimilate, and, as such, a great example to emulate. After I read Mohan's intro, it became much easier to understand yours.
- due to the odd formatting of the first column in Table 1, you should improve its readability by drawing the horizontal lines for each row. You should also (i) add the relevant query- and label- side meta-data [see lines 88-89], (ii) intuitively explain (for a general audience) the entire process, rather then relying  on the abstract row-names for rows 2-4, and (iii) explain the reason behind the mistakes of the the four approaches, with an emphasis on OAK, Oracle, and MOGIC (in particular, why the errors of MOGIC are disjoint from those of the Oracle?)
- ideally, Table 1 please should have an additional row for MOGIC( NGAME ), which is listed in the abstract as a major contribution.  
- ideally, there should be an additional table (similar to Table 1) that intuitively explain the differences between the results with early- vs late- fusion
- lines 93-102 are just "tuning Table 1 into prose," without adding any insides or intuitions. As such they should be replaced insights/intuitions (or simply removed)
- lines 139-144: to increase the readability of this long, reference-rich sentence, you should replace the comma before "text-based" with a semi-column; then re-write the second part by bringing tabular data first, as it only was two references (vs 1+ lines of them)
- the caption of Table 2 is too long and too in-depth; move most of it the main narrative
- please replace the Low/High/VeryHigh labels in the last column by actual numbers; eg, O( ms ). 
- Figure 1 is hard to read and interpret: (i) if the green box is "the architecture of the OAK disciple" then why does the horizontal-bracket labeled "Disciple" also covers the Encorder fed by the "Label: Jellybean" rectangle?, (ii)overall, you should spend a new paragraph that provides an intuitive, step-by-step explanation of what takes place in Fig 1.   

3. Experimental Results
- in all tables, please use BOLD for the best result and UNDERLINED-ITALIC for the runner-up
- all tables/figures should include the results on all four datasets (not only a subset of them); at the very least, they should be added to the APPENDICES 
- lines 338-342: provide references for both "the plethora of papers" and "the few of them that offer ground-truth data"
- Table 3: please provide the details on how EXACTLY you computed all values in the last four columns; for example, you have an "Avg Q/L" of 2.11, but 693K/312K = 2.22; similarly, in the first row "the nmb of memory items is smaller than the nmb of training queries", but it is larger in the second row; please explain why?
- for each of the four datasets, please select-and-justify a reasonably-ambitious target-latency (eg, answering N queries per second); then create a table (similar to Table 4) in which you compute the actual latencies for all the various approaches
- Table 4: please discuss the results where MOGIC is outperformed, especially when it loses to ANCE by 7.4% (50.99% vs 43.60); similarly, why does OAK outperform MOGIC on the same metric/dataset?
- Table 5: how comes that, by itself, DistilBERT heavily outperforms the other two oracles, but within MOGIC the differences are minimal?
- line 460: please quantify "more powerful and larger oracles;" the reader should have immediate access to this info in your paper
- the entire 4.2 section reads like "a bag of tables and results;" please re-organize it to emphasize the main results (eg, as 4..2.1, 4.2.2, etc)  


- last but not least, in the robustness analysis
  (i) please show numbers for MOGIC's competing approaches, too
  (ii) please discuss in depth the sources/hypotheses for this robustness: is there any redundancy in the data sources? it is highly-counterintuitive that using only 40% of the data barely impacts MOGIC, while significantly impacting the Oracle (Table 9)
  (iii) same fore noise: how could be MOGIC barely impacted if 60% of the data is incorrect? also, when the impact on the oracle is greater than 50%, what factors contribute to "fading the impact of noise" on MOGIC by about an order of magnitude?

### Questions
- please section above

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces an oracle guidance framework for enhancing extreme classification tasks by integrating metadata through early-fusion techniques. By distilling from the oracle model, the disciple model can generate high-quality embeddings while maintaining low inference latency. Experimental results on benchmark datasets show that MOGIC consistently enhances performance on XC task, surpassing state-of-the-art methods.

### Strengths
1.The proposed method finds an efficient way to distill the oracle model, enhancing the disciple model’s ability to embed extreme classification data while maintaining low inference latency. 
2.The authors conducted thorough experiments to validate the effectiveness of the proposed method.
3.Comprehensive implementation and experiment details underscore the soundness and practical viability of the proposed method.

### Weaknesses
1.In robustness analysis section, the author mentioned the MOGIC framework is more robust to Oracle models. Further analysis should be conducted on this phenomenon to verify that the robustness stems from the proposed MOGIC framework rather than from the OAK method itself.
2.The theoretical analysis on the oracle-guided losses is unaligned with the experiment implementation. Please see question 2 for details.
3.The presentation of the paper could be improved. There are many writing errors in the paper that hinder understanding, e.g. the unfinished caption of table 10.

### Questions
1.Why did you only present results on the LF-WikiSeeAlsoTitles-320K dataset when discussing MOGIC's generalizability across different disciple models? Does MOGIC still demonstrate generalizability on other datasets?
2.In the theoretical proofs in Appendix A, the loss function is assumed to be a decomposable binary loss rather than the non-decomposable triplet loss. Does the conclusion hold under triplet loss circumstances? Additionally, the alignment loss defined in line 797 has an asymmetric form. If that is not a typographical error, why is the binary loss of (xi*, zi, yi) calculated inner the binary loss of (xi, zi*, yi)?

### Soundness
3

### Presentation
2

### Contribution
2
