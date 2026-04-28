# Conditional Enzyme Generation Using Protein Language Models with Adapters

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 5, 8

## Abstract
The conditional generation of proteins with desired functions and/or properties is a key goal for generative models. Existing methods based on prompting of language models can generate proteins conditioned on a target functionality, such as a desired enzyme family. However, these methods are limited to simple, tokenized conditioning and have not been shown to generalize to unseen functions. In this study, we propose ProCALM (\textbf{Pro}tein \textbf{C}onditionally \textbf{A}dapted \textbf{L}anguage \textbf{M}odel), an approach for the conditional generation of proteins using adapters to protein language models. Our specific implementation of ProCALM involves finetuning ProGen2 to incorporate conditioning representations of enzyme function and taxonomy. ProCALM matches existing methods at conditionally generating sequences from target enzyme families. Impressively, it can also generate within the joint distribution of enzymatic function and taxonomy, and it can generalize to rare and unseen enzyme families and taxonomies. Overall, ProCALM is a flexible and computationally efficient approach, and we expect that it can be extended to a wide range of generative language models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces ProCALM (Protein Conditionally Adapted Language Model), an approach for the conditional generation of proteins, specifically enzyme in this paper, using adapter tuning with protein language models.
In silico experiments show that matches existing methods (ie, ZymCTRL) in generating sequences from target enzyme families while offering several advantages, such as being parameter-efficient to train, allowing multiple conditionings (by adding more adapter and re-train accordingly(, and can generalize to rare and unseen enzyme families and taxonomies. 
ProCALM demonstrates potential in generating sequences for unseen functions, although there is room for improvement and future research.

### Strengths
The use of adapters allows for parameter-efficient training, and easy accommodates various types of conditioning information, such as enzyme function and taxonomy for different applications.

ProCALM shows capabilities to generalize to rare and unseen enzyme families and taxonomies, which is an unique advantage over existing methods.

### Weaknesses
Despite the promise of ProCALM in generating functional protein sequences, the current form of the manuscript can be significantly improved if the following concerns are addressed in the future.

**Lack of technical novelty in the machine learning side:**
This paper appears to be a simple adaptation of adapter tuning for PLMs for one specific application scenario. Neither a new ML method nor new insights into how to properly tailor existing ML methods to protein problems are presented. Protein LMs (ProGen) are existing models, and adapter tuning is widely used in LMs, including protein LMs [1, 2, 3, 4]. The integration method seems fairly straightforward, with the only difference being the task (enzyme design).

**The performance is not strong and the evaluation is not sufficient**.
Compared to existing methods, ProCALM's performance is comparable and not impressive. 
More efforts need to be put in providing clear evidence of ProCALM's superiority over existing methods.
Despite the promise in generating sequences for unseen functions, this paper only studies enzyme generation. Given the mild contributions from the ML aspect, the authors should provide more evaluations on various conditional protein sequence design applications using PLMs and conditional adapters to demonstrate ProCALM's generality and versatility for functional design.

### Questions
see weaknesses.

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
4

### Summary
This paper proposes a novel approach, ProCALM (Protein Conditionally Adapted Language Model), for the conditional generation of proteins using adapters in protein language models. They leverage a seperate encoder to capture information of given condition into latent representation. The conditional adapter layer, presented within each transformer layer, integrates this latent representation with the language model's embeddings to ensure conditional generation. Experimental results demonstrate that ProCALM can successfully generate protein sequences conditioning on enzyme function and taxonomy, and it shows significant generalization capabilities to unseen enzyme families and taxonomies.

### Strengths
1. The proposed method ProCALM is parameter-efficient and computationally inexpensive to finetune protein language models for conditional generation tasks.
2. ProCALM can handle multiple types of conditioning information, such as enzyme function and taxonomy, and different representations of the same condition.
3. The paper shows that ProCALM can successfully generalize to out-of-distribution conditions.

### Weaknesses
1. This paper does not cite LM-Design [1], which introduces a lightweight adapter into protein language models to perform structure-conditioned sequence generation and is very related to this work.
2. The method proposed in this paper is similar to LM-Design, and the experimental results, such as generalization to OOD distribution, have already been demonstrated by LM-Design. Therefore, I believe this paper lacks sufficient novelty.
3. The current results still lag behind existing methods (such as ZymCTRL) in terms of generation quality, diversity and perplexity, and only shows advantage in training costs, which may not be sufficiently strong to prove the effectiveness of this method.
4. The evaluation metrics are not comprehensive enough. For sequence quality, the pLDDT metric has widely been used in sequence generation evaluation [2,3]. And for sequence diversity, comparing generated sequences among themselves, rather than against a reference database, can more directly reflect diversity. For example, this can be evaluated from both sequence and structure dimensions: by calculating pair-wise sequence identity and by using a structure prediction model (such as ESMFold) to first obtain the structure of the sequence and then calculating the pair-wise structural similarity.

### Questions
1. Previous work [1] has validated the effectiveness of scaling. Considering that ProGen2 also has 2.7B and 6.4B versions, can scaling to bigger protein language model further improve the generation performance of the method proposed in this paper?

### Soundness
3

### Presentation
3

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
The paper proposes ProCALM, a method for the conditional generation of proteins using protein language models enhanced with conditional adapters. This approach aims to generate protein sequences tailored to meet specific types or molecular functions.
The authors conduct several experiments and demonstrate that, for seen enzyme families, ProCALM achieves comparable to previous methods like ZymCTRL. Additionally, it shows the ability to generalize to rare and novel enzyme families and taxonomies.

### Strengths
1. Adapter is indeed a parameter-efficient method that enables controllable generation at a relatively low cost and effectively mitigates overfitting.
2. The authors conducted extensive experiments to demonstrate the effectiveness of the proposed method, such as generating unseen families, and some necessary ablation studies like the performance in different function representations.

### Weaknesses
1. Compared to previous fine-tuning models designed to generate protein sequences with specific functions, the approach tries to learn the mapping of functional distribution, and indeed holds some potential to generate sequence with functions not encountered during training. However, it seems to rely on the quality of the functional representation, and there seems to be a risk of “data leakage” during the stage of function representation learning. Specifically, if the functional representations are derived from data that overlaps with the training set for the protein language model, the model might be learning spurious correlations rather than genuine functional relationships. This is especially concerning if the functional representations are learned using methods that are not strictly held out from the protein sequence data used to train the language model, potentially leading to inflated performance metrics.
2. Although ProCALM has a lower training cost than previous methods, its ability to generate sequences with both seen and unseen protein families is limited. For seen functions, its performance is slightly inferior to existing methods, and for unseen families, its capabilities remain quite limited. The reported performance on unseen families, while a valuable contribution, highlights a significant gap in the model's generalization capabilities. The model's inability to generate high-quality sequences for novel families raises questions about the robustness of the learned functional mapping and the limitations of the adapter-based approach when dealing with out-of-distribution data.

### Questions
I have listed my concerns and questions in 'Weaknesses'.

### Soundness
3

### Presentation
3

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
The authors propose ProCALM, an adapter-based method to allow for conditional generation of proteins from pre-trained protein language models, and demonstrate the performance of ProCALM on conditional enzyme generation. Their main contributions are 1) demonstrating that conditional adapters, while being parameter efficient and inexpensive to train in both time and memory, yield comparable performance to existing methods and 2) creating a flexible framework for conditional generation -- ProCALM is not limited to any one particular class of condition, and the authors demonstrate individual and joint conditioning across enzyme class and taxonomy. Lastly, the authors assess the ability of ProCALM to generalize to rare and completely held-out/out-of-distribution enzymes (this includes unseen combinations of taxonomy and enzyme class). The authors also evaluate across a broad range of metrics and perform several ablation experiments.

### Strengths
1. The paper is written very clearly and does a good job of contextualizing the contributions of ProCALM against prior work.
2. While this paper does not represent the first use of conditional adapters for protein generation, the authors explore conditioning on information other than structure (like taxonomy and enzyme class)
3. The evaluation metrics are well-chosen and reasonable for sequence-level similarity and diversity, though it may be worthwhile to perform more fine-grained evaluation on generated sequences (i.e. domain-level)
4. Based off the evaluations provided, ProCALM is clearly performant and compares well to the existing method tested, ZymCTRL
5. The authors perform an ablation study to test the benefits of parallel adapters vs. a shared adapter in the case of conditioning both taxonomy and enzyme class,

### Weaknesses
My main concern is about the out-of-distribution (OOD) generalization claims, which I believe are currently unsupported by the evaluations/data-splitting:
1. The 70% and 90% sequence identity thresholds used for clustering to get held-out clusters for evaluation (Table 2) are really high thresholds. 
- It seems like it would be totally feasible for a sequence in train and a sequence in one of these evaluation sets to be very closely related homologs (~40% shared sequence similarity and higher). 
- In such a case, it seems like ProCALM could simply generate, for a given enzyme commission (EC) class, a sequence very similar to one seen with the same EC class in training. 
- I believe that adding evaluations for held-out clusters at other thresholds will strengthen the overall results of this work.

2. The Heldout ECs for generation evaluation are randomly sampled ECs, which doesn't account for the hierarchy of EC numbers. 
- While it would not be reasonable to hold out say all sequences where the first digit of the EC number starts with a 7, there should be some standardizing of what level of EC number gets held out. For example, maybe if all sub-subclasses are held out for a specific subclass, that would be an informative evaluation to see. 
- In light of the random sampling of ECs for the heldout group, the mean accuracy level in Figure 4.D seems a little underwhelming. If the mean accuracy level is below 1, then the accuracy level is more about the ability of ProCALM to generate examples of the same overall class, which probably relies more on overall sequence similarity between examples of the target class and the training data, which comes back to the point about high percent identity clustering thresholds.

### Questions
I think that the authors make a convincing case that ProCALM is broadly applicable and useful given that it is 1) parameter efficient and inexpensive to train while matching ZymCTRL and 2) flexible to allow multiple types of conditioning. I also think that the paper would benefit from addressing the concerns about the OOD generalization claims.

I may have misunderstood the data-splitting, evaluations, or something else entirely, and I am willing to increase my score if this is the case and/or the authors address my concerns listed in the weaknesses section.

I'm also curious if the authors have examined the properties of the subsequences in the ProCALM-generated enzymes. For example, a histidine kinase will contain a histidine kinase domain (which may be as short as 70 amino acids), and this is probably the region of the protein to which it is most important to generate something similar in order to yield a working histidine kinase. I think it would be valuable to see if the generated sequences for a specific EC class contain the domain(s) that the target sequences contain and in what order (for multi-domain enzymes)

**Note:** raised rating to an 8 in light of authors' responses and revisions

### Soundness
3

### Presentation
3

### Contribution
3
