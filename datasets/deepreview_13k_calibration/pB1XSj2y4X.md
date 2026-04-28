# Generative Flows on Synthetic Pathway for Drug Design

- Decision: Accept
- Avg Score: 5.60
- Scores: 6, 5, 6, 6, 5

## Abstract
Generative models in drug discovery have recently gained attention as efficient alternatives to brute-force virtual screening. However, most existing models do not account for synthesizability, limiting their practical use in real-world scenarios. In this paper, we propose \modelname, which sequentially assembles molecules using predefined molecular building blocks and chemical reaction templates to constrain the synthetic chemical pathway. We then train on this sequential generating process with the objective of generative flow networks (GFlowNets) to generate both highly rewarded and diverse molecules. To mitigate the large action space of synthetic pathways in GFlowNets, we implement a novel action space subsampling method. This enables \modelname to learn generative flows over extensive action spaces comprising combinations of 1.2 million building blocks and 71 reaction templates without significant computational overhead. Additionally, \modelname can employ modified or expanded action spaces for generation without retraining, allowing for the introduction of additional objectives or the incorporation of newly discovered building blocks. We experimentally demonstrate that \modelname outperforms existing reaction-based and fragment-based models in pocket-specific optimization across various target pockets. Furthermore, \modelname achieves state-of-the-art performance on CrossDocked2020 for pocket-conditional generation, with an average Vina score of –8.85 kcal/mol and 34.8\% synthesizability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces RXNFLOW, a generative framework that integrates synthesizability considerations into molecular generation for drug design. Following previous work, RXNFLOW addresses synthesizability by generating molecules using molecular building blocks, chemical reaction templates and a GFlowNet model. RXNFLOW aims to efficiently learn to sample from a large and complex action space, employing an action space subsampling technique to handle the combinatorial explosion of possible synthetic pathways. The authors claim that RXNFLOW achieves strong performance in pocket-specific and pocket-conditional generation tasks, with high synthesizability and diversity scores compared to previous models.

### Strengths
- RxnFlow performs well across all tasks/targets and the comparison of a reaction-based GFlowNet to SBDD models is welcome.
- The subspace sampling technique substantially reduces memory and computational complexity.
- The use of non-hierarchical action base combining reactions and build blocks is novel and well motivated.
- Article is generally very well written and the quality of figures is high.

### Weaknesses
 **Weakness/points to be worked on:**

- The main contribution of the works is the non-hierarchical and continuous action space. There are many theoretical benefits to this, but the benefit of their method is not concretely controlled with respect to the building block data used and compute budgets.
    - I would recommend Figure 6 be amended with scaling laws for the SynFlowNet [1], RGFN [2] and SyntheMol [3] methods. Specifically, the computational cost (time and memory) of training and sampling should be explicitly compared across these methods as a function of the building block library size. This should include not just the final performance, but also the convergence rate.
- Another fundamental claim is that the model can generalise to ‘’unseen” building blocks. While in theory their method should allow this, it has not been justified with experimental evidence.
    - As far as I can tell, this is only benchmarked in Figure 5 which looks at QED. This is a highly uninformative metric given how well generative models do on QED. Benchmarking the seen and unseen molecules on one of the targets for instance would be a better example. Furthermore, the Tanimoto similarity between seen and unseen building blocks should be reported to quantify the novelty of the unseen set.
    - Furthermore, a random split of the building blocks are used, given the high degree of redundancy in the Enamine Building Block set it is not surprising that performance does not change as these sets are highly similar. How does the model do on highly novel building blocks? A more rigorous evaluation would involve using building blocks with significantly different structural features, perhaps by clustering the building blocks and selecting clusters with low inter-cluster similarity for the unseen set.
- While technically impressive, I see no practical utility gained in the case on not retraining on new building block sets as (i) these libraries at not updated regularly and (ii) the costs of training these models are so small one would prefer to retrain a model anyways.
    - The y-axis scales in Figure 6 are extremely narrow for many metrics and does not represent a meaningful change in values for Vina and Structural Diversity. For Figure 6b there is only a meaningful reduction in scaffold diversity when number of available building blocks is 10^2, an extremely smaller number and other works do not use. The practical relevance of these small changes needs to be better justified.
    - Furthermore, RGFN [2] introduces a similar method to scale to large build block spaces and a proper comparison is not conducted. A direct comparison of memory usage and computational cost at different building block sizes is needed.
- Some aspects of the evaluation could be improved:
    - What is the with per run variance for the docking scores for molecules in Tables 1-4? Is there really a significant difference between the methods? I would recommend including per run box plots of Vina scores in the appendix. The statistical significance of the reported differences should be explicitly tested and reported.
    - There is next to no discussion on the limitations of their model and possible future work. The manuscript should discuss the limitations of the current approach, such as the potential for bias in the building block selection or the limitations of the reaction templates used, and suggest avenues for future research.
    - L458: The authors do not include statistical tests or error bars/standard deviation values in Table 5 yet claim ”RXNFLow achieves significant improvements in drug-related properties” in the CrossDocked experiments. The lack of statistical rigor undermines the claims made.
    - No effort is made to disentangle the technical changes of the authors model v.s. building block library size when comparing to baselines. The performance gains should be attributed to specific technical contributions rather than simply increasing the building block library size.
- The article is generally very well written but parts are not clear, for instance:
    - The fact that the continuous embedding space is based on chemical fingerprints is not mentioned in the main text. This detail is crucial for understanding the method and should be included in the main text.
    - Table 6:  No legend/keys are provided to indicate what the symbols mean. The table is difficult to interpret without a clear legend.
- L429: “Since RXNFLOW explicitly considers synthesiz- ability, we exclude the SA score from the TacoGFN’s reward function as described in Sec. C.2.”.  I Could not find reference to SA score in Section C.2. Am I right in thinking the authors removed the SA reward from TacoGFN? In which case they ablated another model they are comparing to. Or have they removed it when training their model? Please clarify.
- No code is provided.

**Minor points:**
- L122: “...trained models with the GFlowNet objective”, is it not more accurate to say these works propose reaction-based GFlowNet models?
- I struggle to see the added value in Algorithm 1 in the main text. It does not aid in understanding the method. I recommend removing.
- Table 6 seems wrong?
- In Table 3, calling this metric “Percentage of Synthesizable Molecules” is misleading, as these are predicted not ground truth. I would prefer AIZynFinder success as done in the previous literature [1].
- I appreciate the use of the LIT-PCBA targets, but is there a reason the SEH Proxy used in the rest of the GFlowNet literature [1,2] was not used?
- Section B.1: The formulation sees to be highly inspired by SynFlowNet, if so please cite accordingly.

### Questions
- Table 5: Values in time column have ‘a’ and ‘b’ superscripts. What do these mean?
- Section 4.2: Can the authors clarify what is ‘zero-shot’ about this method?
- Do you use the same reward functions for methods when comparing to previous GFlowNets?

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
4

### Summary
This paper introduces a new gflownets-based method RxnFlow for conducting the synthesizability-aware generation. To this end, the authors proposed to redefine the action space with Reaction templates and building blocks. To make the training procedure flexible, the authors involve a subsampling method for training RxnFlow in huge spaces.  The experiments over the SBDD benchmark have demonstrated the effectiveness of the RxnFlow for generating molecules with both good binding affinity and synthesizability.

### Strengths
1. The motivation of the paper is clear. I believe that apart from the generative approaches that formulate the problem as a constraint generation/projection, the proposed methods focus on an alternative perspective, i,e,  explicitly limiting the action space of gflownets, which should also be explored.

2. The paper introduces a simple yet effective approach, which is referred to as subspace sampling. The method takes a very simple formulation while it enables the reduction of complexity and enables feasible training of the algorithm. 

3. The empirical study of the proposed framework is extensive, with both pocket conditioned/ specific ligand generation being considered.

### Weaknesses
1. Though I appreciate the methods with simplicity and effectiveness, I believe that a more systematic investigation and overview of the proposed methods is needed.  Based on the bias/variance discussion in the appendix, does the proposed approach conduct a variance/efficiency tradeoff, i.e. large variance for high efficiency? This is a little counterintuitive for me, could the authors discuss this further. From the ablation in Fig. 6, with sufficient steps, a larger subspace shows better performance. Does the key benefit of the proposed method is accelerating the optimization?

2. Some important baselines are suggested to be included in Table 5, for example [1] for atom-level SBDD. And the paper mentioned the recent relevant work [2], so why not include it? 

3. I would like to suggest the author include the SA score as another metric for evaluating the synthesizability. I am curious to see whether SA is aligned with the used metrics in the paper.

### Questions
Refer to above

### Soundness
3

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
4

### Summary
This paper proposes  a GFlowNets based method 'RXNFLOW' for drug discovery. By employing space subsampling technique, RXNFLOW can expand the search space and handle massive action spaces. This method can be adopted for pocket-specific optimization task as well as pocket-conditional generation task.

### Strengths
1. The method enables the generation of synthetic pathways for molecules, allowing for the sampling of highly synthesizable compounds while maintaining a significant level of diversity, which is meaningful for drug discovery.
2. With the enhancement of building blocks, the method demonstrates good scalability.
3. The experiments were conducted thoroughly, and the presentation is relatively clear.

### Weaknesses
1. Regarding the pocket-conditional generation task, to my knowledge, the more advanced methods [1] have not been compared.  This has somewhat affected the persuasive power of the experiments.
2. Compared to other SBDD methods, it seems that direct generation of conformations combined with the pocket is not achievable.
3. Regarding the pocket-specific optimization task, I notice that the reward function consits of Vina Score which is also used for evaluation. I have concerns about whether the method may be overfitting to Vina, which could result in inflated evaluation metrics.

### Questions
1. What limitations do you perceive in the current method, and how might it be improved in the future?
2. Regarding the pocket-conditional generation task, I am curious about the method's ability to synthesize molecules with specific binding characteristics, such as calculating the 'delta score' metric propsed in Paper [1].


[1]. Gao, Bowen, et al. "Rethinking Specificity in SBDD: Leveraging Delta Score and Energy-Guided Diffusion." ICML 2024.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this manuscript, the authors adopted the GFlowNet to generate synthesizable molecules based on the protein pocket. They were able to demonstrate that RXNFLOW outperforms existing reaction-based and fragment-based models in pocket-specific synthetic pathways, and their method achieves state-of-the-art performance on CrossDocked2020 for pocket-conditional generation.

### Strengths
Overall, this paper is interesting. The GFlowNet model is suitable to be adopted to solve the synthesizability problem of small molecules. The problem with GFlowNet is that it lacks a method to construct a graph that covers the entire space of small molecules. This paper cleverly utilizes chemical synthesis reactions to construct this graph, while also adopting a down-sampling approach to enhance the effectiveness of the method.

### Weaknesses
The main issue is the insufficient characterization of 3D interactions; the model does not explicitly model the interactions between atoms in 3D space and only uses the generated molecule's vina score with the pocket as the reward. This approach neglects crucial geometric information that dictates binding affinity and specificity. In addition, a careful discussion of the differences from SynFlowNet is needed. Currently, the authors have avoided mentioning SynFlowNet in the introduction. According to my understanding, the method proposed in this paper has no structural difference from SynFlowNet in terms of the model framework, with some improvements in sampling techniques. I hope the authors can discuss the differences from SynFlowNet in detail from the perspectives of graph construction for the flow, reward settings, and the sampling algorithm.

### Questions
1. For conventional SBDD methods, they are generally trained on molecules that can bind to protein pockets, resulting in generated small molecules with a specific distribution. I am curious about how the molecules generated in this space of synthesizable reaction-based small molecules differ from those generated by SBDD methods, such as pocket2mol. Because drug-likeness is not solely determined by synthesizability and vina score alone. For instance, the bond angle, number of rings. These facts are hard to encode into the reward function.
2. Please compare the speed of different methods. 					
3. Why use 3 reaction steps for your method and 4 steps for SynFlowNet and RGFN?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The author proposed a GFlowNet for on synthetic pathway, aiming to leverage the large action space for drug synthesis while retaining computational efficiency. The author proposed an action embedding which embeds the template and building blocks to parameterize the policy network. They further reduces the computational complexity by introducing a subsampling technique on the action space via importance sampling. The author validate their approach on LIT-PCBA, CrossDocked2020 dataset and outperformed baselines.

### Strengths
1. The proposed methods outperforms baseline in standard benchmark.
2. The methods exhibit nice scaling behavior on unseen blocks.

### Weaknesses
1. **Conceptual Novelty:** Utilizing reinforcement learning (RL) to determine reaction pathways is not a novel approach. The authors have simply applied this existing methodology to GFlowNets, which does not represent a significant conceptual advancement.

2. **Technical Novelty:** The proposed action embedding and importance sampling techniques do not appear to introduce new concepts. Essentially, the authors are reparameterizing the policy network with template and building block embeddings— a standard practice in RL when addressing large action spaces. The specific implementation of these embeddings, and how they interact with the GFlowNet framework, lacks detailed explanation, making it difficult to assess their true contribution beyond standard practice.

3. **Figure Clarity:** Figure 2 is currently confusing and requires further refinement. The use of diamonds to represent templates and squares for reactions may initially cause some misunderstanding. In contrast, Figure 7 is clearer and more effectively conveys the intended information.

4. **Efficiency Discussion:** The paper's main claim centers on reducing the action space to enhance computational tractability. However, there is a need for a more in-depth discussion and comparison of the training and inference times between the proposed network and existing baselines to substantiate this claim. The paper should include a detailed analysis of the computational complexity of the proposed method, especially in comparison to other GFlowNet approaches for reaction pathway generation. It is not clear how the subsampling method affects the convergence rate and the overall training time.

5. **Ablation Study:** The manuscript lacks an ablation study comparing Hierarchical Markov Decision Processes (MDPs) with non-hierarchical MDPs. Such a study is essential to evaluate the effectiveness and advantages of the non-hierarchical approach presented. The authors should provide a justification for choosing a non-hierarchical approach over a hierarchical one, given that hierarchical methods are often used to handle complex decision-making problems.

### Questions
1. Table 5, what is a and b?
2. line 45, what does it mean by 'chemical modification can degrade in the optimized propeties', can you give some examples?
3. It's unclear to me how you introduce the additional objective without retraining, can you clarity that?

### Soundness
2

### Presentation
2

### Contribution
2
