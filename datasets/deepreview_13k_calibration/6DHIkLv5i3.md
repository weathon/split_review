# Curriculum-aware Training for Discriminating Molecular Property Prediction Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 3, 8, 8

## Abstract
Despite their wide application across various fields, current molecular property prediction models struggle with the challenge of activity cliff, which refers to the situation where molecules with similar chemical structures display remarkable different properties. This phenomenon hinders existing models' ability to learn distinctive representations for molecules with similar chemical structures, and results in inaccurate predictions on molecules with activity cliff. To address this limitation, we first present empirical evidence demonstrating the ineffectiveness of standard training pipelines on molecules with activity cliff. We propose a novel approach that reformulates molecular property prediction as a node classification problem, introducing two innovative tasks at both the node and edge levels to improve learning outcomes for these challenging molecules with activity cliff. Our method is versatile, allowing seamless integration with a variety of base models, whether pre-trained or randomly initialized. Extensive evaluation across different molecular property prediction datasets validate the effectiveness of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes to use curriculum training to address the activity cliff (AC) problem in molecular property prediction. The proposed method re-formulates property prediction task as node classification where the molecules are considered as nodes, and the edges are constructed based on whether the molecules are AC pairs. The edge-level task also helps curriculum training. Extensive experiments are conducted on MoleculeNet dataset by adding the proposed method to various baselines to evaluate the model performance.

### Strengths
- The paper tackles a very important task in molecular property prediction, and is from the training perspective. 
- The adaptation of curriculum training here is rational. 
- The paper has performed a series of analyses to show the findings.

### Weaknesses
 - Activity cliff is a critical concept in chemistry, primarily based on differences in molecular structure. Any method addressing this task should be motivated by chemical intuition related to these structural variations somehow. However, the proposed method lacks insights that would specifically address activity cliffs. It is more like tackling a hard sample problem rather than focusing explicitly on the activity cliff challenge.

- How is the "training loss for the top 10%-loss molecules with and without AC" calculated? Are the molecules involved in the matched pairs removed from this calculation? If the training involves only AC vs. non-AC molecules, the results seem fairly intuitive. Additional clarifications would help make these experiments easier to understand.

- In Fig. 4, are the dashed and solid edges used to denote different labels or categories, like being used differntly? Or are they simply shown to illustrate how AC pairs vary?

- The selection of molecules is based on loss differences, but this approach does not necessarily correlate with AC performance. For instance, an AC might result in high loss, but a high loss does not necessarily indicate an activity cliff.

- Each task seems to require a separate graph, as molecules can behave differently depending on the properties being evaluated. This approach might incur significant computational costs. Table 9 shows the results of AC pairs obtained in each dataset, which helps clarify the data size. However, the number of pairs seems quite large, making the computational complexity and scalability other concerns.

- The backbone models seem not very new. There are many recent SOTA models and the authors should evaluate the performance of adding the proposed component to these models.

- For some datasets, the method shows only marginal improvement. Have the authors explored the underlying reasons for this?

- The experiments seem only run once, which might not robust. The authors could try cross validation or run several times to report the standard deviation. 

- There are already proposed AC datasets [1, 2], why the authors do not evaluate the proposed method on them?

### Questions
See weaknesses.

### Soundness
2

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
4

### Summary
This paper focused on the molecular property prediction task, in particular accounting for properties exhibiting activity cliffs, which are defined as minor structural changes conferring significant changes in activity.  A new method based on curriculum learning is proposed, where property prediction is formulated as a node classification problem on a graph where nodes are molecules and edges encode molecular similarity. The proposed approach is evaluated using several classification and regression datasets and different molecular encoders.

### Strengths
- Except for a few points, the method is clearly described and the paper is relatively easy to follow.
- Figures help understand the intuition for the method and the method itself.
- The initial analyses are well-conducted and help familiarize with the challenge tackled in this paper.

### Weaknesses
 - The main claims of this work appear to be not well supported by results. In particular
    - Line 70: "We are the first to investigate why...". I could not see results indicating why molecular property prediction models struggle in these casese. Instead, the work include some empirical evidence that only reinforces the (known) observation that generalizing to AC is challenging. The analysis presented does not provide a mechanistic explanation for why activity cliffs are difficult for models, but rather shows that molecules with activity cliffs have higher loss values, which is an expected outcome. Additionally, many works investigated activity cliff in the context of property prediction. See for example "Zhang et al., Activity Cliff Prediction: Dataset and Benchmark, 2023", or "Wu et al., A Semi-Supervised Molecular Learning Framework for Activity Cliff Estimation, 2024". These works are not cited or compared.
    - Line 75: "We propose to re-formulate molecular property prediction as a node classification problem.". This does not appear completely novel, see for example "Zhuang et al., Graph Sampling-based Meta-Learning for Molecular Property Prediction, 2023" or "Zhao et al., Molecular Property Prediction Based on Graph Structure Learning, 2023", which are not cited. In general, previous works on this direction are not accounted for. The graph formulation, while presented as a core contribution, is not sufficiently differentiated from existing approaches that also leverage graph structures for molecular property prediction. The authors need to clearly articulate the differences and novel aspects of their graph construction.
- Novelty. The novelty of the work appears limited. As stated in line 324, the methodological novelty is the extension from node to node+edge curriculum learning. However, the definition of the edge-level loss (Eq. 2) is based on the same node-level loss. This work largely appears as an application of standard curriculum learning. The edge-level loss, while intended to capture activity cliff information, is ultimately derived from the same loss function used at the node level. This raises concerns about whether the edge-level loss truly introduces a novel learning signal or if it is simply a re-weighted version of the node-level loss. The authors should clarify how the edge-level loss provides a unique learning signal beyond the node-level loss.
- Lack of baselines. The authors only compare the proposed method to the baseline network, i.e., no other methods of any kind are taken into account. The authors should compare the proposed method to existing methods. These include works focused on AC prediction (see points above for some examples), but also methods broadly focused on representation robustness (e.g., based on adversarial perturbations or mixup) and domain generalization. The lack of comparison to existing methods, particularly those focused on activity cliff prediction or representation robustness, makes it difficult to assess the true performance and contribution of the proposed method. The authors should include a more comprehensive set of baselines to properly contextualize their results.

### Questions
See weaknesses. In particular, The authors should 1) better clarify the claims, 2) reference previous work focused on AC prediction 3) better clarify the novelty of the proposed approach, 4) include more baselines.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
------- Update -------

Thank you to the authors for addressing the comments and questions I had on the paper, I'd like to say again what a pleasure it was to read and that I really appreciate both the content clarifications and updates to the presentation. 

On reviewing your answers to my questions and reading the paper again, I'm very happy to raise my score to an 8. 
Well done on the paper, and thank you again for all of your hard work. 



-----------
Thank you for a really interesting read. I found both the analysis of model performance on the molecules with activity cliffs a strong addition to the literature, to take something commonly acknowledged and quantify it is vital work, and the novel exploration of the problem very good to see. 

Summary:
* The authors present a novel approach to tackling the problem of molecules exhibiting an activity cliff. This problem plagues computational chemists as many molecules share large portions of their structure, differing only for a small percentage of the molecule, and still have very different properties. Such properties are intuitive to human experts, but hard to handle using many deep learning methods. 
* The authors take this anecdotal knowledge and make strong baseline measurements of the discrepancy found in many SOTA models in cases where activity cliffs are present. 
* The authors then reformulate the problem of molecular property prediction into a node classification problem as part of a graph structure representing molecules with similar structures.
* They present this worm as Learning with Activity Cliff (LAC) - and use the concept of curriculum learning to slowly introduce harder to separate AC molecules - this work shows improvements across a range of benchmark datasets and conduct extensive ablation studies to investigate which properties are contributing.

### Strengths
* The analysis of the well known but poorly quantified impact  of molecules with activity cliffs is a really valuable contribution to the field 
* The novel problem construction looks like a genuinely different way to approach training models for molecular property prediction. 
* The extensive ablation study is really strong showing which components of the restructuring are contributing to the improvements in score - this means as a reader I have the ability to start replicating / incorporating this method into new work. 
* The combination of new reformatting of the problem with the curriculum learning approach to slowly introduce more complex examples seems like a very promising path.

### Weaknesses
 * The degree of improvement over the baselines in each case was perhaps hard to quantify - I really appreciate the comparison (Table 2, 3) with the baseline models and + LAC - but felt these tables perhaps lacked context. From the tables alone it’s hard to evaluate if the degree of improvement is significant or not. If a couple of reference models could be added to these tables to show other work that would help calibrate my perception of the improvement of the LAC method. 
* The comment about the lack of baseline against which to judge the contributions applies to tables 4 and 5 and 6 as well. (However I recognise that adding / evaluating baseline models for all cases can be expensive / difficult to conduct.) 
* The way the initial node features are generated feels unclear to me - on line 228 “In this graph, each molecule corresponds to a node, and the molecule’s chemical structure can be stored as node features” - How exactly are these features chosen? Are these features the readout from the baseline models (GraphGPS, UniMol ?) or are these simply generated from something like RDKit. My interpretation from the text is the former, but some more clarity here in the text would be good. 
* I find it slightly unclear what the exact message is - my take away is the LAC is a really good way to improve the abilities of an already performed model - but I'm left concluding the paper a bit unsure exactly how strong the case is.
* The loss distributions in Fig 6 are very hard to read, please use the same binning scheme for both histograms and show them either with low alpha or as lines only so I can see how they change. Also the text is too small, try adjusting figure sizes for these results?

### Questions
Questions / Suggestions:
* What is the impact of the batch size on training here? In line 3 of the algorithm (line 312) the mini batch is chosen, then pairs with the activity cliff found. This means the second term in the loss L_e is dependant on how many samples are found, did you study the impact of the batch size on the training? As a reader I would want to know - my dataset has X% of possible activity cliff molecules, what batch size Y do I need to see an improvement of magnitude Z using this method? Otherwise I would suspect the impact to only be a small reguarlising term? Is this a correct analysis - and could some more detail be given on this point? 
* Do you have any analysis at how effectively the LAC process picks out the molecules which have an activity cliff? It selects the ones with high loss and then forms edges based on the relative labels - but do you know how much of the time these pairs do form AC pairs? 


Formatting - lower priority but would be good to aesthetically improve
* Figure text sizes - the text on many of the figures is unreadable at a normal zoom level, try adjusting the matplotlib params to make these more readable. You can always move some into the appendix and leave one or two examples from each figure in the main text. Specially Fig 2, 3 and 6
* Caption of Fig 7 is a bit unwieldy 
* Line 194 has a typo “even they” -> “even though they” ? 


Thank you again for the work, I found the paper really enjoyable to read and showed strong scientific process. 
Some clarifying on a few points and tidying up of some of the figures are my main concerns, otherwise I find the work very solid.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a curriculum learning-based training method (LAC) for molecular graph learning on property prediction tasks. Empirical evidences are provided to expose the limitation of current molecular graph learning is the insufficient learning for activity cliff molecules. Further, an elaborate definition is designed to convert the general graph learning to node-level and edge-level tasks with activity cliff being considered, followed by a designed integrated loss function. The experiments on several general molecular property prediction tasks show improvements of LAC than ordinary training method.

### Strengths
- The empirical analysis results effectively highlight the current limitations in molecular property prediction, especially concerning the activity cliff issue.

- The definitions of node-level and edge-level tasks, considering activity cliffs, are clearly elaborated.

### Weaknesses
 - It’s unclear why only an MLP model was applied for regression tasks but other models (GraphGPS, GraphMVP, etc.) were excluded. Additionally, the choice of specific ChEMBL assay data (please include the ChEMBL ID) over commonly used molecular property regression benchmarks (e.g., FreeSolv, ESOL) is not explained. The lack of justification for the model selection and dataset choice weakens the experimental design and makes it difficult to assess the generalizability of the findings.

- A study on curriculum learning for molecular graph learning and property prediction should be referenced to strengthen the related works section:

Ref:
Gu Y, Zheng S, Xu Z, et al. An efficient curriculum learning-based strategy for molecular graph learning[J]. Briefings in Bioinformatics, 2022, 23(3): bbac099.

- A comparison of computation times with standard random-sampling training would provide additional context for performance evaluation regarding the time cost issue. The absence of this comparison makes it difficult to assess the practical efficiency of the proposed method, especially when considering the potential overhead of curriculum learning.

- LAC demonstrates performance improvements, it would be helpful to clarify how these gains are achieved—does LAC contribute more to activity cliff (AC) data, non-AC data, or both? A table or figure result may be helpful to understand that. Without this analysis, it is difficult to pinpoint the specific advantages of the proposed method.

- Since the loss functions for standard training and curriculum learning differ in equations and terms, directly comparing their values may be misleading. An alternative approach would be to show the proportions of large-loss instances for AC data across each training strategy throughout the process (e.g., similar to Figure 3). The direct comparison of loss values between different training strategies is problematic and may not provide a clear picture of the method's effectiveness.

### Questions
- What are the criteria used for the detection of activity cliffs? Since it is a concept mainly for binding affinity, people may be more interested about how the authors transfer and expand such concept to molecular property tasks (especially regression tasks and some non-affinity property tasks such as BBBP) with rationales behind. Please provide more details about the clear criteria and other necessary descriptions about this. It could be the most important experimental setting and basis of the study to ensure accurate definition for AC is applied.

- How is the alpha ratio for pairwise loss determined?

- Some typos exist. Such as "ChemBL" should be "ChEMBL".

### Soundness
3

### Presentation
3

### Contribution
3
