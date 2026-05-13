# Contextual Molecule Representation Learning from Chemical Reaction Knowledge

- Decision: Reject
- Scores: 3, 5, 8, 5

## Abstract
In recent years, self-supervised learning has emerged as a powerful tool to harness abundant unlabelled data for representation learning and has been broadly adopted in diverse areas. However, when applied to molecular representation learning (MRL), prevailing techniques such as masked sub-unit reconstruction often fall short, due to the high degree of freedom in the possible combinations of atoms within molecules, which brings insurmountable complexity to the masking-reconstruction paradigm. To tackle this challenge, we introduce \textit{REMO}, a self-supervised learning framework that takes advantage of well-defined atom-combination rules in common chemistry.  Specifically, \textit{REMO} pre-trains graph/Transformer encoders on 1.7 million known chemical reactions in the literature. We propose two pre-training objectives: Masked Reaction Centre Reconstruction (MRCR) and Reaction Centre Identification (RCI). \textit{REMO} offers a novel solution to MRL by exploiting the underlying shared patterns in chemical reactions as \textit{context} for pre-training, which effectively infers meaningful representations of common chemistry knowledge. Such contextual representations can then be utilized to support diverse downstream molecular tasks with minimum finetuning, such as affinity prediction and drug-drug interaction prediction. Extensive experimental results on MoleculeACE, ACNet, drug-drug interaction (DDI), and reaction type classification show that across all tested downstream tasks, \textit{REMO} outperforms the standard baseline of single-molecule masked modeling used in current MRL. Remarkably, REMO is the pioneering deep learning model surpassing fingerprint-based methods in activity cliff benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces REMO, a self-supervised learning framework for MRL, which leverages well-defined rules of atom combinations in chemical reactions. REMO pre-trains graphformer encoders on a large dataset of chemical reactions and proposes two pre-training objectives: masked reaction centre reconstruction and reaction centre identification. REMO supports diverse downstream molecular tasks with minimal finetuning and outperforms traditional masked modeling approaches in various experiments.

### Strengths
1.	The paper is well-written and easy to follow.
2.	The experiment results are comprehensive.

### Weaknesses
1. My main concern revolves around the masking strategies employed and the performance of the proposed method. I find it is hard to comprehend the additional information gained from the two pre-training strategies, as they appear similar in their tasks. Specifically, both masked reaction center reconstruction and reaction center identification seem to focus on the same core problem: understanding which atoms are involved in a reaction. The distinction between predicting the location of the reaction center and reconstructing it given its location is not clearly justified, and it's unclear how this provides complementary information. Besides, the inclusion of a conditional molecule as a constraint during pre-training seems necessary, yet this information is absent during the actual execution of the downstream task. This discrepancy causes a disconnect between the pre-training and downstream tasks, potentially limiting the transferability of the learned representations. The pre-training objective appears to be learning reaction-specific information, but the downstream tasks are often molecule-specific, which creates a mismatch.

2. Additionally, in Table 1, the authors conclude that their approach is inferior to ECFP+SVM. It is unclear how this supports the claim of superiority for their own method. The lack of comparative advantage raises questions about the effectiveness of their approach in relation to existing methods. The fact that a simple fingerprint-based method outperforms the proposed approach on a key benchmark undermines the motivation for using a more complex pre-training strategy.

### Questions
1. What is the rationale behind conducting pretraining for the same task?
2. Is there a way to evaluate the significance of conditional molecule generation?
3. In Table 2, why is the prediction of reaction centers useful for cliff? Especially considering that ECFP performs better than most other pretraining methods, could we explore if other methods incorporating chemical reactions for pretraining also provide information gain?
4. Why does REMO-IM outperform REMO-IM Attrmask in Table 3?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes two novel masking approaches to pretraining on molecular data using reaction data: 
(1) predict the reaction center's atom type and adjacent bonds, 
(2) predict whether an atom belongs to a reaction centre. 
The experiments contain different tasks, benchmarks, and focus on comparing to other masking approaches

### Strengths
- I agree that reaction data is a promising source which should be considered in pre-training.
- The proposed approaches are straightforward / relatively simple, but make sense.
- The experiments are nice in that they also include transformers as baselines, not just GIN, and they cover different tasks.

### Weaknesses
 - The related work is missing all references to masking approaches in SSL beyond graphs. ICLR is a more general ML conference and graph SSL has clearly been inspired by those.
- The writing contains many statements I do not think there is clear consensus about
    - "in molecule graphs the relationships between adjacent sub-units are mostly irrelevant." - would at least need references. This statement is too strong, as the specific arrangement of atoms and bonds directly dictates molecular properties and reactivity. While the variety of possible combinations is large, the relationships are far from irrelevant.
    - "while changing one word in a long sentence might have a relatively low impact on the semantic meaning of the full sentence," - adding "not" does not. This analogy is flawed, as a single word change can drastically alter meaning, especially in contexts like negation. The comparison to molecular changes is not well-justified.
    - "In such cases, traditional masked reconstruction loss is far from being sufficient as a learning objective." - The Molformer paper shows that simple masking can recover structure quite well if enough pre-training data is available. The claim that masked reconstruction is insufficient needs more rigorous justification, especially given recent successes with this approach.
    - "most biochemical or physiological properties of a molecule are determined and demonstrated by its reaction relations to other substances" - also needs references, esp. for ML readers. While reactions are important, many properties are also determined by the molecule's intrinsic structure and electronic properties, not solely by reactions. This statement oversimplifies the relationship between structure, reactions, and properties.
    - "ACNet (Zhang et al., 2023) demonstrate that existing pre-trained models are incomparable to SVM based on fingerprint on activity cliff." - I doubt that activity cliffs should be a goal / considered in pre-training. This is a particularly challenging fine-tuning scenario, I agree on that. However, in pre-training the goal is to learn a generally good embedding space which can be easily adapted in various fine-tuning scenarios. In fact, in unsupervised learning more generally (i.e., not transfer learning), a uniform space is considered as goal in many papers. It is not clear to me how an embedding space needs to look like so that it is particularly beneficial also in AC scenarios. If the authors consider those, a more detailed investigation might be useful.
- Table 1: I think the baselines are too basic and thus unrealistic, the SOTA is more advanced, e.g.
    - ECFP: might be a concatenation of ECFP+MAACs or even additional, helpful descriptors rdkit provides. Using a simple ECFP is not representative of current best practices.
    - GAT, GCN, etc. are all models from the GNN literature. There are others, e.g., D-MPNN (chemprop), which target chemical tasks. The choice of baselines is not comprehensive enough to make a strong claim about the proposed method's performance.
- My current main concern is the experiment design, which is not fully clear to me.
The Table 3 comparison may be lacking. Since there are no ablation results in terms of masking, I assume the authors intended to compare this in this table as well (i.e., beyond just comparing to SOTA works in general). The baselines from related works seem to be trained on other data. However, even if these are larger datasets, they do not necessarily have to be better. In fact, USPTO contains highly diverse, special data from patents. So it is not directly clear to me that this dataset is comparable to the pre-training data the other models use. Therefore, it is not at all clear how the proposed masking actually compares to related works. It is also not clear from the table if the REMO_x models are based on GIN or Graphormer. Only if the former is the case, the comparison to most of the baselines makes sense to me, in terms of masking.

### Questions
see above

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new self-supervised method for learning molecule representation. They propose to use masked reaction center reconstruction instead of conventional masked sub-unit reconstruction. The argument for that is in this way, the model can exploit underlying shared patterns in chemical reactions as context and can infer meaningful representations of common chemistry knowledge.

The main motivation for the paper was that  the traditional masked reconstruction loss is not enough for molecules due to:
1)  the "activity cliff" property of molecules, where a single molecular change could lead to a big difference in the molecule property, the standard self-supervised learning techniques fall short when applied to molecules.
2) BERT-like masked reconstruction loss omits the high complexity of atom combinations within molecules in nature that are quite unique compared to a simple sentence comprised of a few words.

Therefore, instead of sub-units,  they proposed to reconstruct the reaction center from the given reactants as context. 
This is due to the fact that molecule biochemical or physicochemical properties are determined and demonstrated by its reaction relations to other substances.

### Strengths
1. The motivation/intention of the method is very clear and well-justified.
2. The paper is well-written and easy to follow.
3. The results looks good

### Weaknesses
The paper overall is easy to follow and easy to understand, but in terms of the baselines and experimental set up some parts could be improved. For details please reach the questions section. It would be nice if the authors add a discussion around the limitation of the proposed method.



### Questions
1. The graph formed part of the explanation is a bit confusing, would it be possible to make it more clear so one does not need to go back to the original paper to understand? 

2. In table 1, I was wondering why REMO_IM model is not presented but only REMO_I and REMO_M? This also extended to Table 2, here the REMO represents the model trained to do the reaction center reconstruction task, the identification task, or both.

3. From Table 3, it seems often the model trained for reaction center reconstruction does not have as good performance as the one trained to predict the reaction center, any insights on this?

4. Regarding the baselines for the drug-drug interaction task, I was wondering what happens if one uses simply the graph formed without self-supervised learning, what would be the result? I think one main baseline missing from the paper here is, what happens if we do not use self-supervised learning, but directly use the proposed graph network structures to do the task, would the result be a lot worse than having the self-supervised learning setup? 

5. Regarding the reaction center identification task, as the output is softmax over all the atoms, you will have a vector of [p_1, p_2,,, p_N] where 0<=p_i<=1,  what happens when you have multiple reaction center, maybe the answer to this question is very obvious but I am somehow failing to see it clearly.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This study focuses on understanding molecular representation by anticipating the context of hidden atoms. 
While numerous prior research has delved into graph representation by reconstructing the masked components in the graph, this study seeks to reconstruct the "reaction center," believed to be vital in grasping the context of chemical reactions. 
The authors start by pinpointing reaction centers as previous works - by recognizing atom pairs with differing bond types between the reactant and product graphs. 
They then introduce two unique training strategies: the masked reaction center reconstruction and reaction center identification. 
The former targets the prediction of the specific type of concealed atoms, while the latter determines if the atoms in a molecule belong to the reaction center.

### Strengths
1) Learning the representations of molecules is important for various downstream tasks.
2) Idea of identifying the reaction center is novel and the approach will definitely help the model to understand underlying chemical knowledge.
3) Extensive experiments on various downstream tasks demonstrate the superiority of REMO.

### Weaknesses
1) In paragraph 2 of the Introduction, the authors mentioned that "in molecule graphs the relationships between adjacent sub-units are mostly irrelevant". Is there any reference for this? I don't agree because the sub-units of the molecules are relevant to each other, and therefore, it will be helpful in reconstructing the molecule structure from the given molecule.

2) Weak experimental results.
- The most important baseline [1] is missing. It should be compared to demonstrate the effectiveness of reconstructing reaction centers instead of just learning from chemical formulas.
- In Table 1, it would be more convincing why fingerprint-based methods outperform deep models [2].
- In Table 2, comparing Mole-BERT and GraphLoG will be helpful since those methods outperform GraphMVP in Table 3.
- In Table 4, why many baseline models in previous tables are missing? Overall, various self-supervised learning methods should be compared in all tasks since they can be applied to all tasks.
- Moreover, in MolR [1], they have a task for chemical reaction classification, which aims to predict the reaction class that a chemical reaction belongs to. It would be great if REMO outperforms MolR in the task, thereby demonstrating the superiority of MolR in understanding underlying chemical reaction knowledge.

[1] CHEMICAL-REACTION-AWARE MOLECULE REPRESENTATION LEARNING, ICLR 2022.

[2] Why Deep Models Often cannot Beat Non-deep Counterparts on Molecular Property Prediction?, arxiv 2023.

3) No codes are available.

### Questions
Provided above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
