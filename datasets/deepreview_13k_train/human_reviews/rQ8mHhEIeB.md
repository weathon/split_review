# Towards Understanding Link Predictor Generalizability Under Distribution Shifts

- Decision: Reject
- Scores: 5, 6, 6, 6, 5

## Abstract
State-of-the-art link prediction (LP) models demonstrate impressive benchmark
results. However, popular benchmark datasets often assume that training, validation, and testing samples are representative of the overall dataset distribution. In
real-world situations, this assumption is often incorrect; since uncontrolled factors
lead to the problem where new dataset samples come from different distributions
than training samples. The vast majority of recent work focuses on dataset shift
affecting node- and graph-level tasks, largely ignoring link-level tasks. To bridge
this gap, we introduce a novel splitting strategy, known as LPShift, which utilizes
structural properties to induce a controlled distribution shift. We verify the effect of LPShift through empirical evaluation of SOTA LP methods on 16 LPShift
generated splits of Open Graph Benchmark (OGB) datasets. When benchmarked
with LPShift datasets, GNN4LP methods frequently generalize worse than heuristics or basic GNNs. Furthermore, LP-specific generalization techniques do little
to improve performance under LPShift. Finally, further analysis provides insight
on why LP models lose much of their architectural advantages under LPShift.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper investigates the generalizability of link prediction models under distribution shifts, a crucial problem given the structural differences often encountered between training and real-world data. To address this, the authors introduce LPShift, a dataset-splitting strategy that induces distribution shifts based on structural properties, allowing for a controlled study of model performance under these conditions. They evaluate several state-of-the-art Graph Neural Network for Link Prediction models and generalization methods across multiple split scenarios.

### Strengths
1. The focus on distribution shifts in link prediction is valuable, as models often fail to generalize well when such shifts occur in real-world settings, like social networks or recommender systems. This paper directly addresses this issue by benchmarking models in varied shift scenarios.

2. The paper provides comprehensive baseline comparisons under the distribution shift setting.

### Weaknesses
1. The motivation behind distribution shifts in link prediction is not effectively illustrated in the introduction. A clearer example is needed to demonstrate why link prediction models might struggle with distribution shifts:  
Figure 1 is confusing. Models should easily predict links with more common neighbors (blue and green links) compared to red links, aligning with typical link prediction assumptions. However, this is not explained well, which weakens the introductory motivation.

2. The definition of distribution shift, based solely on heuristics, feels arbitrary. It would strengthen the study if the importance of these heuristics in link prediction were demonstrated upfront, clarifying their role in creating meaningful shifts.  
a) Previous studies (e.g., [1]) emphasize the significance of global structure information, which seems not fully considered in the LPShift splitting strategy.
b)  The use of temporal datasets like Collab may not suit this split strategy, as it is sensitive to time. As a benchmark paper, two datasets seem limited.

3. The paper’s terminology needs refinement for clarity. For example, using consistent names for terms like “inverse”/“backward” splits would reduce confusion. “’repair’” should be replaced with “repair” for consistency and correctness.

4. As a benchmark study, the insights provided are minimal. It would be more valuable to include a deeper analysis, such as how different splitting strategies impact performance or specific guidance on choosing GNN4LP models based on observed patterns in the results.

### Questions
Why is it important to focus on distribution shifts in link prediction? While distribution shifts can impact GNN performance, is it useful to have a benchmark dedicated to evaluating these shifts independently? In many cases, performance on the original dataset splits remains a key concern. For instance, using the time-based splits in OGB-Collab might offer a more practical perspective. I would consider raising the score if the authors provide a promising rebuttal for my questions and concerns.

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
The paper introduces a dataset-splitting strategy to assess the generalizability of the link prediction models under distribution shifts. LPShift utilizes three structural metrics—Common Neighbors, Shortest Path, and Preferential Attachment—to induce shifts, creating training, validation, and testing sets with distinctive structural properties. The empirical results reveal that GNN4LP models perform poorly under LPShift, with simple heuristics sometimes outperforming complex models. The paper posits LPShift as a framework for studying distribution shifts in LP tasks and highlights the need for generalization methods.

### Strengths
1. This paper tackles a compelling and timely research problem: handling complex distribution shifts in graph data for link prediction tasks, a topic of significant recent interest.
2. The splitting strategy is straightforward and well-explained, which is easy to understand.
3. The observations are inspiring to show the author’s motivations.

### Weaknesses
1. The novelty is somewhat concerning to me since there is no comprehensive approach proposed. The paper introduces a dataset splitting strategy, but it does not offer a novel model or algorithm to address the identified distribution shift problem. The contribution is limited to the creation of a benchmark, which, while useful, does not constitute a significant theoretical or methodological advancement. The lack of a proposed solution makes the work feel incomplete from a research perspective.

2. The paper lacks detailed theoretical analyses to support their main claims. While the empirical results are presented, there is no formal analysis of why the observed distribution shifts cause the performance degradation. The paper does not delve into the mathematical properties of the graph metrics used for splitting, nor does it provide a theoretical framework to understand the generalization challenges. This absence of theoretical grounding weakens the conclusions and limits the generalizability of the findings.

3. I think this paper seems to be a technical report/benchmark paper instead of a research paper. The authors might address this concern by presenting a formal method rather than intuitive explanations to answer the presented questions. The paper focuses on empirical observations and lacks a deeper theoretical contribution. The analysis is primarily descriptive, and there is no attempt to develop a formal model or framework to explain the observed phenomena. The paper would benefit from a more rigorous approach, such as developing a theoretical model that explains the impact of structural shifts on link prediction performance.

### Questions
I am curious what is the main difference among node-level graph OOD method and link-level graph OOD method?

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
3

### Summary
This paper proposes a new problem related to data distribution shift in link prediction. To address this, this paper introduces a novel splitting strategy called LPShift to create benchmark data for distribution shift in link prediction. The proposed dataset is used to evaluate current link prediction methods and analyze why these models exhibit weaknesses.

### Strengths
The paper proposes a method to introduce distribution shift in link prediction.

By evaluating various methods across multiple benchmarks, it demonstrates that existing models are vulnerable to distribution shifts in link prediction.

Through several analyses, the authors aim to show the effectiveness of the proposed method for inducing distribution shift and to explain why there is a drop in model performance.

### Weaknesses
1. The most critical issue is the lack of clarity on why distribution shift is necessary in link prediction and what realistic scenarios justify this need. Can’t we consider changes in edge connections as changes at the graph level? How does graph-level distribution shift differ from this? It would be beneficial to provide specific scenarios that demonstrate the importance of this problem. Without this, it might seem like the issue is being created without a clear purpose.

2. It’s unclear whether this problem is genuinely challenging. In Table 2 for DropEdge and TC (ogbl-ppa), the mean change in performance is marginal, ranging from -1% to +4%. Additionally, in Tables 1 and 7, simple RA and GCN show strong performance. 
While these results may highlight limitations of LP methods, could you further explain why this new problem is challenging and why there is a need to advance methods to address it?

3. As a minor suggestion, placing citations within parentheses would enhance readability.

### Questions
Please refer to W1 and W2.

1. The most critical issue is the lack of clarity on why distribution shift is necessary in link prediction and what realistic scenarios justify this need. --> Regarding this, please refer to following questions to better justify the importance and novelty of the proposed work:
(1) Provide concrete examples of real-world scenarios where link prediction models face distribution shifts.
(2) Clarify how the proposed distribution shift differs from or relates to graph-level changes.
(3) Explain more explicitly why existing graph-level distribution shift benchmarks are insufficient for link prediction tasks.

2. It’s unclear whether this problem is genuinely challenging. In Table 2 for DropEdge and TC (ogbl-ppa), the mean change in performance is marginal, ranging from -1% to +4%. Additionally, in Tables 1 and 7, both Simple RA and GCN show strong performance. 
While these results may highlight limitations of LP methods, could you further explain why this new problem is challenging and why there is a need to advance methods to address it?

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
This paper benchmarks the generalizability of LP models under distribution shifts, which is often neglected in link-level tasks. It introduces a dataset splitting strategy called LPShift, which uses structural properties to induce distribution shifts, enabling the study of LP model performance under such conditions. The authors evaluate various LP models and generalization techniques on 16 LPShift-generated dataset splits. The paper concludes that structural shifts significantly impact LP model performance, advocating for further exploration of generalization techniques.

### Strengths
1. The problem of link prediction under distribution shifts is not fully explored, and the paper has the potential to bridge the important gap.
2. The proposed LPShift strategy can be applied to real-world datasets, offering a practical tool for researchers to evaluate the generalization of LP models in realistic scenarios.
3. Many experimental results are provided showing the limitations of current LP-specific generalization methods.

### Weaknesses
1. The writing is problematic with many grammar errors and confusing sentences. For example, the CN example in the introduction confuses me without a specific source node and target node context. What is a "red" graph? Line 52: requires $\rightarrow$ require.
2. All splits are based on statistical heuristics without any real-world shift splits, e.g., temporal shift, which produces not enough the significance. The lack of real-world shifts limits the practical relevance of the benchmark, as it's unclear if the observed performance drops on these synthetic splits would translate to actual OOD scenarios. The structural shifts induced by LPShift, while interesting, need to be more convincingly linked to real-world distribution shifts to justify their significance.
3. Traditional generalization baselines are missing, e.g., IRM, VREx, etc. It is not sure whether not LP specific methods can already solve the LP OOD problem. The absence of these baselines makes it difficult to assess the difficulty of the proposed benchmark and whether existing OOD techniques can address the observed performance degradation. The paper should include a more comprehensive comparison with established domain generalization methods.
4. The hyper-parameter sweeping space is not large enough to produce significant experimental conclusions. The limited hyperparameter tuning could lead to suboptimal performance for some models, making it difficult to draw robust conclusions about the effectiveness of the proposed benchmark and the generalization capabilities of the tested models. A more thorough hyperparameter search is needed to ensure fair comparisons.
5. As a benchmark, no code is provided. The lack of publicly available code hinders reproducibility and makes it difficult for other researchers to utilize the proposed benchmark and build upon the findings of this work. The absence of code significantly reduces the impact of the benchmark.

### Questions
1. Why are the proposed splits significant? For example, if a generalization method works well on your split, which real OOD problem can the method solve? Can you provide experiments and discussions to validate that?

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
4

### Summary
This paper investigates the distribution shift issues on LP tasks on the graph, where the links in training, validation, and testing sets may be drawn from different distributions. The authors introduce a graph edge splitting method LPShift, which can artificially create a split with distribution shift. Three traditional LP methods are selected as the metrics to perform the LPShift: CN, Shortest-Path, and Preferential Attachment. LPShift is applied to OGB datasets: Collab and PPA to generate a set of new splits. By evaluating the LP methods' performance on these new splits, the authors conclude that current LP methods are sensitive to the distribution shift problem, and advocate for further exploration on this issue.

### Strengths
[S1] The paper is easy to read. It has a clear demonstration of the problem setup, methods, experiments, and conclusions.

[S2] Different from previous distribution shift studies, this paper identifies the issue of LP tasks, which is novel.

[S3] The experiment shows that LPShift can effectively cause a distribution shift problem for current SOTA LP methods.

### Weaknesses
[W1] My major concern is whether the study has any practical merit. It is unknown if the distribution shift problem for LP tasks (widely) exists in the existing benchmarks. Instead, in this paper, the problem is artificially created and identified by manually creating such a dataset. There is Collab that has such an issue, but it is already reported in [1], with a very similar plot. It would be more convincing if the authors could show and identify more existing datasets that suffer from such an issue. The presented analysis of the Collab dataset largely replicates the findings of the NCNC paper, which already demonstrated a common neighbor distribution shift between training and testing sets. The addition of a validation set distribution does not substantially alter the core finding, thus limiting the novelty of this aspect of the study. The artificial nature of the introduced distribution shift, while providing a controlled environment, raises questions about its relevance to real-world scenarios where such shifts may manifest differently.

[W2] The experimental results are confusing. Table 1 uses Hits@20 as the metrics to rank models, but Table 7/8 uses MRR for actual performance. If both metrics have to be applied here, then they should both have the same set of tables (ranking table as of table 1, actual performance table as of table 7) for a clear demonstration.

[W3] The relative comparison among LP methods in Table 1 can be misleading. The authors attempt to conclude that simpler methods with Collab can perform better because GNN4LP struggles to generalize due to the structural shift induced by LPShift. However, the LPShift also uses HeaRT[2] to generate negative samples. And under the HeaRT setting alone, simpler methods like RA can already perform better than GNN4LP. This leads to confusion about whether it is the HeaRT or LPShift that causes GNN4LP to fail to generalize. The experimental design makes it difficult to isolate the impact of LPShift from the influence of the HeaRT negative sampling strategy, particularly since HeaRT itself introduces a structural bias by selecting negative samples with higher common neighbor counts. This makes it unclear if the observed performance differences are due to the distribution shift induced by LPShift or simply an artifact of the HeaRT sampling method. The claim that GNN4LP methods generalize worse than heuristics on LPShift datasets is not fully supported, as the performance differences could be attributed to the interaction between HeaRT and the specific graph structures created by LPShift.

Minor issues:

* Authors use "inverse split" and "backward split" interchangeably, which causes confusion.

### Questions
[Q1] Link-MoE [3] uses a set of link predictors as experts to perform LP tasks and achieves SOTA performance. Given that the authors show that different methods have different capabilities to handle distribution shift, will a mixture of experts model help with the issue by integrating strengths of different models together?

[Q2] Since CN, SP, and PA are selected as the metrics for LPShift, it would be interesting to include SP and PA and see how they work under the shifting, similar to RA.

[Q3] Follow up on W1, if Collab already shows a distribution shift issue, is it necessary to further manually corrupt the dataset?

[3] Mixture of Link Predictors.

### Soundness
3

### Presentation
3

### Contribution
2
