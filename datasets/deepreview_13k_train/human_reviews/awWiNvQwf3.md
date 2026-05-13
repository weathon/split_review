# Efficient Evolutionary Search Over Chemical Space with Large Language Models

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
Molecular discovery, when formulated as an optimization problem, presents significant computational challenges because optimization objectives can be non-differentiable. 
Evolutionary Algorithms (EAs), often used to optimize black-box objectives in molecular discovery, traverse chemical space by performing random mutations and crossovers, leading to a large number of expensive objective evaluations.
In this work, we ameliorate this shortcoming by incorporating chemistry-aware Large Language Models (LLMs) into EAs.
Namely, we redesign crossover and mutation operations in EAs using LLMs trained on large corpora of chemical information. We perform extensive empirical studies on both commercial and open-source models on multiple tasks involving property optimization, molecular rediscovery, and structure-based drug design, demonstrating that the joint usage of LLMs with EAs yields superior performance over all baseline models across single- and multi-objective settings. 
We demonstrate that our algorithm improves both the quality of the final solution and convergence speed, thereby reducing the number of required objective evaluations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces MOLLEO (Molecular Language-Enhanced Evolutionary Optimization), which is a framework that combines Large Language Models (LLMs) with evolutionary algorithms for molecular discovery. The study integrates three LLMs - GPT-4, BioT5, and MoleculeSTM - into genetic operators such as mutations and crossover operations for molecular generation. The experimental results span multiple tasks, including property optimization, molecular rediscovery, and structure-based drug design, where MOLLEO demonstrates superior performance over its baseline models. Among the tested models, MOLLEO with GPT-4 achieves the best results in 15 out of 23 tasks. Furthermore, this study tackles more challenging scenarios such as protein-ligand docking tasks, which better represent real-world molecular generation conditions.

### Strengths
The primary strength of this paper is its straightforward implementation of integrating LLMs into evolutionary algorithms for molecular optimization. This makes it easy to follow and understand the core mechanism of the proposed framework. Another strength is the framework's flexibility in incorporating different types of LLMs, from commercial (GPT-4) to open-source models (BioT5 and MoleculeSTM), making it adaptable to different resource constraints and use cases. This study also demonstrates practical applicability by showing how MOLLEO can improve upon existing molecules in existing chemical datasets like ZINC 250K, indicating its potential value for real-world drug discovery pipeline.

### Weaknesses
The weakness of this paper is particularly regarding the novelty of the methodology. The core idea of MOLLEO is essentially a straightforward substitution, where genetic operators in the existing evolutionary algorithm framework (Graph-GA) are replaced with LLMs. Fundamentally, this method mainly involves leveraging LLMs to perform mutation and crossover operations, which could be seen as a relatively simple extension of existing approaches.

Furthermore, the paper lacks a detailed explanation of how the authors address multi-objective optimization settings. While they acknowledge that determining the weight for each objective function in a sum-aggregate objective could be challenging, they do not specify how these weights are assigned in their experiments. 

Additionally, the authors propose handling multi-objective settings using Pareto set selection, where only the Pareto frontier of the current population is retained. However, this approach is a standard practice in evolutionary algorithms, as seen in well-established methods like NSGA [1] and MOEA/D [2], which leverage Pareto ranking. The authors might assume that Pareto set selection is less frequently applied in molecular optimization, this concept has already been widely applied in molecular optimization problems in previous studies [3-5]. Though the authors do not claim a novel contribution in using Pareto set selection, the paper would benefit from a more thorough discussion of their approach to multi-objective optimization and clearer positioning within the broader landscape of Pareto-based optimization approaches.

### Questions
1) The authors propose using LLMs for genetic operators (mutation and crossover), but how does this approach fundamentally differ from existing methods that use deep neural networks for learning genetic operators? What unique capabilities do LLMs bring to molecular generation that cannot be achieved through existing deep learning-based mutation and crossover operations? The authors may consider that LLMs do not require additional training for genetic operator learning, as they can be adapted simply by modifying prompts. However, I believe that the inference process for LLMs could introduce a computational cost comparable to training deep neural networks for genetic operators. Furthermore, while the authors may suggest that LLMs can facilitate the generation of molecules aligned with objective fitness functions through descriptive prompts, deep neural networks trained specifically for genetic operations can offer distinct advantages. By learning from a dataset of molecules, they can capture meaningful molecular representations and generate novel combinations that are data-driven rather than randomly assembled.

2) The authors state that in Graph-GA, the default crossover and mutation operators are pre-defined by domain experts based on chemical knowledge. How can we be confident that LLMs naturally incorporate this domain-specific knowledge and execute these crossover and mutation operations accurately, rather than merely presenting empirical results? What evidence supports the notion that LLMs inherently understand and replicate these chemically-informed operations?

3) The authors state that they examined whether the open-source models generated molecules previously seen during training and found no overlap between generated molecules and the datasets. However, given that LLMs are trained on extensive chemical literature, including popular molecular objectives like JNK3, GSK, QED, and DRD2, could there still be a risk of data leakage? Specifically, if LLMs have learned about these well-known objectives, they may inherently recognize and prioritize molecular structures that are known to perform well for these targets. If the LLM’s prior knowledge is being leveraged intentionally, how does this approach handle genuinely novel molecular objectives that the LLM has never encountered? In cases where the LLM lacks specific training for unfamiliar objectives, how can it be expected to perform effective genetic operations without relying on prior knowledge, especially when such knowledge may be absent or limited?

4) Building on the previous question, methods like REINVENT and Augmented Memory can optimize molecules from scratch, allowing them to adapt effectively to entirely new and unseen objectives. Given that MOLLEO relies on LLMs with pre-existing chemical knowledge, can it perform better when optimizing for novel molecular targets with limited or no prior information? How does MOLLEO address this challenge to ensure effective adaptation and optimization for objectives that the model has never encountered?

5) The authors employ GraphGA as the backbone model, but why was this specific choice made? Other genetic algorithm-based methods, such as GPBO, or even other generative models like Augmented Memory, could also be suitable. For instance, in molecular generation, LLM-based genetic operations could be implemented and integrated into a replay buffer to iteratively refine results. This approach seems feasible, so why did the authors choose to rely solely on GraphGA as the backbone model?

6) In their multi-objective experiments (shown in Table 2), where mixed objectives are used (e.g., maximizing QED while minimizing SAscore), the authors do not explicitly explain how they handle the differences between minimization and maximization objectives. Do they simply flip the sign of the minimization objectives to treat them as maximization objectives? If so, is this approach sufficient for effectively balancing objectives with inherently different goals?

7) In Figure 2, there appears to be a typo where "LLM editting" is used. Should this perhaps be corrected to "LLM editing"?

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
4

### Summary
This work discusses an approach to molecular discovery, an optimization problem that faces challenges due to non-differentiable objectives. Evolutionary Algorithms (EAs) typically explore chemical space through random mutations and crossovers, which requires numerous costly evaluations. This work integrates chemistry-aware Large Language Models (LLMs) into EAs, redesigning crossover and mutation operations based on chemical knowledge from LLMs.

### Strengths
The strength of the proposed Molecular Language-Enhanced Evolutionary Optimization (MoLLEO) framework lies in its innovative integration of chemistry-aware LLMs (GPT-4, BioT5, MolSTM) into Evolutionary Algorithms (EAs) to improve molecular discovery. By using LLMs as genetic operators in crossover and mutation, MoLLEO enhances proposal quality and accelerates the optimization process. The framework’s effectiveness is demonstrated across multiple black-box optimization tasks, including complex ones like protein-ligand docking, outperforming baseline EAs and other optimization methods.

### Weaknesses
1. The diagram lacks clarity. Based on the description, this work employs LLMs designed solely for text, but Figure 1 appears to suggest the use of an MLLM.

2. The presentation of the proposed method should be improved. For instance, there is no justification provided for using different prompts for LLMs like GPT-4, BIOT5, and MOLSTM. Introducing these LLMs could be moved to the appendix, and the comparison of the designed strategies would benefit from a clearer presentation, such as in a table format.

More concerns can be found in the "Questions".

### Questions
1. My main concerns is the correctness of this method. How to ensure LLMs can produce better offerspring based on the description and fitness value? I believe the molecular is so complex that it is very difficult to figure out which component contributes to the high fitness.

2. The abstract states that the proposed method addressed problem of expensive evaluation. However, I didn't see any relevatnt discussion on it. It is solved by surrogate model normally in evolutionary computation.

3. I am uncertain about the evaluation function. Could you clarify what is meant by 'black-box'? In my experience, fitness is typically determined either through practical experimentation or by calculation using a specific function.

4. How to turn molecule into text description so that it can be processed by LLMs?

5. I am curious the scale of the molecule and its text description. If the scale is too big, will LLMs suffers the risk of correctness? I mean, the generated molecule is probably infeasible?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces MOLLEO, an algorithm that combines chemistry-aware large language models (LLMs) with evolutionary algorithms to optimize molecular properties efficiently. The LLMs guide crossover and mutation operations, reducing evaluations needed in black-box optimization for molecular discovery.

### Strengths
MOLLEO showcases a novel application of LLMs within evolutionary processes, yielding superior performance across 26 molecular design tasks and showcasing promise in early drug discovery.

### Weaknesses
MOLLEO’s reliance on proprietary LLMs may limit reproducibility, and the diversity of the chemical space explored could be improved for broader molecular applications.

### Questions
Question 1: Could the authors provide a computational cost comparison between MOLLEO and traditional methods, given the LLM integration?

Question 2: How does MOLLEO balance chemical space exploration with optimization, and could additional mechanisms for diversity be beneficial?

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
4

### Summary
This paper presents a novel approach to molecular optimization by replacing the crossover and mutation operations in GraphGA with Large Language Models (LLMs) to enhance sample efficiency. Instead of employing LLMs for end-to-end molecule generation, the study uniquely integrates LLM capabilities into specific genetic algorithm operations (crossover, mutation), effectively combining the strengths of LLMs with those of GAs. I really enjoyed reading this paper and think it is a good one. However, the method seems too simple, and I believe that if the methodology is reinforced, it could become an excellent paper.

### Strengths
1.	Unlike conventional end-to-end LLM methods, the paper strategically replaces only the GA operations where LLMs can be effective. This selective substitution leverages the advantages of LLM and genetic algorithm.
2.	It proposes a prompting method that utilizes LLMs to improve performance in molecular optimization tasks. This approach opens avenues for further advancements if combined with additional methods.

### Weaknesses
1.	While the main contribution appears to be the replacement of evolutionary algorithm (EA) components, the paper lacks a comprehensive analysis of existing EA methods. Particularly in multi-objective optimization, evolutionary algorithms like MOEA/D and NSGA-III [1, 2]. The study introduces Pareto Optimality (PO) using the Pareto Front but does not compare it with these established multi-objective optimization EAs. Additionally, the paper DyMol [3] has proposed a Pareto Sampling method similar to the PO in this study, which should be acknowledged.

2.	The MolLEO framework is applied only to GraphGA, which limits its demonstrated versatility. Recent works like Genetic GFN [4] and Saturn [5] have enhanced performance by incorporating crossover and mutation into methods like Augmented Memory and GRU-based GFlowNet. Applying MolLEO to these methods could further validate its effectiveness.

3.	The paper could better articulate why specific objectives were chosen, such as maximizing JNK3 and minimizing GSK3β in objective selectivity tasks. Providing rationale for these choices would strengthen the study's context and applicability.

### Questions
1.	In replacing the crossover and mutation operations within GraphGA, did the LLM genuinely perform these operations, or did it retrieve known SMILES strings based on the provided inputs? For mutation, does the LLM modify only certain tokens in the existing SMILES, similar to the actual mutation operation, or does it reconstruct the entire sequence? Regarding crossover, how closely does the LLM's output resemble true crossover? Given the prompt used—You can either make crossover and mutations based on the given molecules or “just propose a new molecule based on your knowledge”—it's important to understand the ratio of outputs resulting from crossover, mutation, and LLM retrieval.
2.	The objectives in the PMO benchmark are well-known objectives, with extensive experimental data available. Consequently, the LLM might already be familiar with molecules that perform well for these objectives, especially for targets like JNK3 mentioned in the introduction. Is there a possibility that the LLM is retrieving and outputting known high-performing molecules rather than generating novel ones? Verifying this would be crucial to assess the true innovative capacity of the approach.
3.	Building on the previous question, did you intentionally leverage the LLM's existing knowledge to rapidly improve performance, perhaps aiming for a zero-shot learning scenario? If so, this strategy has merit. However, it raises concerns about the method's applicability to entirely new objectives where the LLM lacks prior knowledge. How do you address this potential limitation?
4.	As highlighted in Weakness 2, the evaluation of MolLEO is confined to GraphGA. To demonstrate its generalizability and robustness, it would be beneficial to apply the MolLEO framework to other models like Genetic GFN and Saturn.
5.	All the score curves in the paper compare GraphGA and MolLEO. Including Augmented Memory in these comparisons would provide a more comprehensive evaluation of MolLEO's performance relative to other established methods.
6.	In Table 2, the "Sum" appears to represent the sum of AUC top-10 scores. To prevent confusion—since row “sum“ and column “sum“ are denoted same—please clarify this in the caption or relabel it as "Sum(AUC)." Alternatively, consider using a term like "Scalarization" to more accurately reflect the data presented.
7.	Since the objectives involve both maximization and minimization, summing their scores may not straightforwardly reflect overall performance. Maybe you applied simple (e.g., using 1−score) score for minimization objectives for scalarization. It's important to explicitly detail these methods to ensure the validity and reproducibility of your results.

### Soundness
3

### Presentation
3

### Contribution
2
