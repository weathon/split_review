# Large Language Model-driven Large Neighborhood Search for Large-Scale MILP Problems

- Decision: Reject
- Avg Score: 5.25
- Scores: 8, 5, 5, 3

## Abstract
Large Neighborhood Search (LNS) is a widely used method for solving large-scale Mixed Integer Linear Programming (MILP) problems. The effectiveness of LNS crucially depends on the choice of the search neighborhood. However, existing strategies either rely on expert knowledge or computationally expensive Machine Learning (ML) approaches, both of which struggle to scale effectively for large problems. To address this, we propose LLM-LNS, a novel Large Language Model (LLM)-driven LNS framework for large-scale MILP problems. Our approach introduces a dual-layer self-evolutionary LLM agent to automate neighborhood selection, discovering effective strategies with scant small-scale training data that generalize well to large-scale MILPs. The inner layer evolves heuristic strategies to ensure convergence, while the outer layer evolves evolutionary prompt strategies to maintain diversity.  Experimental results demonstrate that the proposed dual-layer agent outperforms state-of-the-art agents such as FunSearch and EOH. Furthermore, the full LLM-LNS framework surpasses manually designed LNS algorithms like ACP, ML-based LNS methods like CL-LNS, and large-scale solvers such as Gurobi and SCIP. It also achieves superior performance compared to advanced ML-based MILP optimization frameworks like GNN\&GBDT and Light-MILPopt, further validating the effectiveness of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a new dual-level heuristic design method based on LLMs and applies it to the development of large neighborhood search (LNS) heuristics for MILP. The proposed method shows promising results in packing problems and TSP, when compared to existing methods such as FunSearch and EoH. It successfully generates new heuristics that surpass traditional hand-crafted approaches in LNS.

### Strengths
1. The dual-level framework incorporates both prompt evolution and directional evolution, enhancing heuristic design.
2. It introduces effective new heuristics specifically tailored for large neighbourhood searches in MILP. The results show good scalarization.

### Weaknesses
 1. The specific contributions of the newly introduced components in the dual-level framework remain unclear. Specifically, the roles of the outer and inner loops, and how they interact to achieve the reported performance gains, are not well-defined. It's unclear how the differential evolution in the outer loop influences the prompts and how these prompts subsequently affect the heuristic generation in the inner loop. A more detailed explanation of the information flow and the specific mechanisms at play is needed.
2. Additional experimental results are needed to further validate the effectiveness of the proposed method. The current results, while promising, lack sufficient depth to fully assess the robustness and generalizability of the approach. For example, the method's performance across a wider range of problem instances and parameter settings needs to be evaluated. Furthermore, the consistency of the results, given the use of LLMs, requires more rigorous investigation.

### Questions
1. How do the individual components of the dual-level framework contribute to its overall performance? An ablation study is recommended.
2. How many repeated trials were conducted using the proposed method, EoH, and FunSearch on the tasks compared? How consistent are the results of the proposed method, considering that the initial seed heuristics appear to be hand-crafted?
3. What are the detailed settings for the Differential Memory in Directional Evolution? Are both thought directions and code directions utilized? Could you provide an illustrative example and discuss how these mechanisms impact the results?
4. Why are the settings for population size different between LNS tasks and combinatorial optimization tasks? How does changing the population size affect the outcomes within your framework?
5. What performance levels do FunSearch and EoH achieve on the LNS tasks? Are their results comparable to those of the proposed method?
6. What new insights have been gained from the application of LLM-designed heuristics in LNS for MILP, and how might these contribute to the field?

### Soundness
3

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
4

### Summary
This paper proposes to use LLMs to guide adaptive large neighborhood search, with the following three components (1) prompt evolution (2) heuristics evolution (3) differential memory that feeds back the fitness score from past generations. The authors evaluate the performance on online bin packing, traveling salesman and large scale MILP and show the performance improvement from a variety of baseline methods.

### Strengths
- To my knowledge, there has not been works that combine LLMs with large neighborhood search based heuristics. So this can be regarded as a new task (although I have concern about the novelty given there has been works that combine LLMs with a lot of other heuristics and search algorithms for CO).
- The authors evaluate the performance of the algorithm on three sets of CO problems (online bin packing, traveling salesman, and large-scale MILP). The scope of evaluation (in terms of three different problem classes) seems to be satisfactory.
- I find using prompt evolution to prevent the search process from getting trapped in local optima interesting.

### Weaknesses
 - I find Figure 1 confusing. There are too many components in the illustration, and it’s hard to parse the relationship of the arrows from one component to another. I suggest the authors to improve the visualization of the pipeline (e.g. emphasize the important components, remove less important ones) to make it more clear.
- I find the paper lacking baseline comparisons. For example, I would like to see the performance of adaptive large neighborhood search (ALNS) with different heuristic scoring functions (not LLM designed). I also would like to see how each component of the LLM pipeline (prompt evolution, heuristic evolution, and differential memory) contributes to the final performance.
- For traveling salesman, the performance seems to be evaluated only on a small set of instances (5 instances). How is this set selected? I believe the authors need to evaluate on a larger set of instances to claim the performance improvement.
- I have slight concerns about the novelty of the proposed method. The three components used by the authors have all been proposed in previous works. While it is interesting to combine them together and show effectiveness, I’m concerned that the proposed methodology may not be novel enough.

### Questions
- How large is the training set for each task? I may miss it, but it doesn’t seem to clear from reading the main paper.
- Why do the authors train on small-scale problems and generalize to larger problems? What would happen if the authors directly train on larger problems?
- Is the proposed method sensitive to what algorithm backbone the authors are using? e.g. instead of ALNS, would the proposed method perform well when combined with other search / decomposition methods, or LNS without the adaptive size?

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
This article presents 1. Dual-layer Self-evolutionary LLM Agent and 2. Differential Memory for Directional Evolution to implement LLM as Hyper-heuristic on MILP.

### Strengths
1. The results of the proposed method shown in the article is leading.
2. The proposed Dual-layer Self-evolutionary LLM Agent is novel and reasonable

### Weaknesses
I have doubts mainly about the contribution of this paper. I cannot determine whether there is some over-claim in this paper.
1. This paper claims that the introduction of LLM-driven heuristic on LNS is an innovation at the application level. I wonder whether other comparative algorithms such as EoH cannot be similarly introduced to LNS.
2. This paper lacks ablation experiments. I have some doubts about the effectiveness of Differential Memory for Directional Evolution intuitively. I would like the authors to add ablation experiments to validate the contribution of the two components of this paper.

### Questions
1. This paper lacks some clear experiments setting descripsion on Online Bin Packing and Travelling Salesman Problem (e.g. seemingly you use GLS for TSP), which can be very misleading.
2. As my biggest question: on LNS, why does the algorithm SCIP, which is considered to generate labels in [1], perform so poorly?
3. The authors should elaborate on whether they introduced a seed function (initial code for experts) thus introducing possible unfair comparisons. (I observe that the method proposed in this paper has an initial advantage in Figure 3).
4. As the proposed Differential Memory for Directional Evolution will increase the input length (token numbers), can you analyze the relationship between the number of input tokens or API cost and the optimization effect？
5. Please discuss the limitations of this paper.
[1]Huang, Taoan, et al. "Contrastive Predict-and-Search for Mixed Integer Linear Programs." Forty-first International Conference on Machine Learning.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This manuscript proposes a Dual-layer Self-evolutionary LLM-based method for heuristic generation. The experimental results demonstrate that LLM-based heuristic generation methods show promise compared to traditional heuristic generation methods.

### Strengths
S1: This manuscript proposes an innovative approach by introducing a dual-layer structure for heuristic generation.

S2: This manuscript proposes an LLM-based method for ranking decision variables of MILP problems.

### Weaknesses
W1: The proposed LLM-LNS lacks clarity in certain technical details, making it difficult to fully comprehend. For example, on Page 5, the authors say “These parents are then combined with evolutionary strategies, selected from the Outer Layer’s population of prompt strategies”. However, the criteria for selecting evolutionary strategies are not explained. Furthermore, on Page 6, the authors state that “underperforming strategies are pruned”. However, this manuscript fails to clearly define what is a poorly performing strategy. This manuscript relies heavily on textual explanations with insufficient mathematical formalization, making it difficult for readers to fully comprehend and reproduce the proposed LLM-LNS method. Including mathematical definitions, formulas, and pseudocode would greatly enhance clarity. Furthermore, the absence of open-source code compounds this issue, limiting both comprehensibility and reproducibility.

W2: The concept of using LLMs to evolve strategies resembles the approach in the prior study [1], while the notion of differential memory seems to align with another method from [2]. However, this manuscript does not clearly delineate the distinctions between the proposed LLM-LNS method and these prior studies. In addition, it would be more convincing to include experimental comparisons with these prior studies. 

W3: In Section 3.2, the authors state that “Initially trained on small-scale MILP problems, the agent learns effective strategies for selecting promising decision variables.” However, the manuscript lacks details regarding the training process of the LLM agent. For example, how many parameters does it contain? Is it fine-tuned on an existing open-source LLM (e.g., Llama) using MILP data?

W4: In Section 4.1, the experiments are conducted using only a single LLM (GPT-4o-mini), which raises concerns about the robustness of the proposed LLM-LNS method when applied to different LLMs. It is recommended to reference prior studies [3] and conduct experiments across multiple LLMs. In addition, in Section 4.2, can existing LLMs (e.g., Llama) be used to rank decision variables without requiring pretraining using MILP data? If so, why are they not included in comparisons with LLM-LNS?

W5: The lack of ablation studies further raises concerns about the effectiveness of certain submodules within LLM-LNS, such as Differential Memory. Conducting ablation studies would provide valuable insights into the contribution of each submodule.

W6: This manuscript is missing important details in some areas and contains grammatical errors. For example, in Table 1, the terms "Evolutionary Prompt," "Strategic Evolution," and "Directional Evolution" are not explained. Additionally, on Page 8, there is a grammatical error: “In the Appendix A B C D”.

### Questions
Please refer to the weakness section.

### Soundness
2

### Presentation
1

### Contribution
2
