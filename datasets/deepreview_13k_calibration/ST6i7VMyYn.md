# Unlearning Virus Knowledge Toward Safe and Responsible Mutation Effect Predictions

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 1, 5

## Abstract
Pre-trained deep protein models have become essential tools in fields such as biomedical research, enzyme engineering, and therapeutics due to their ability to predict and optimize protein properties effectively. However, the diverse and broad training data used to enhance the generalizability of these models may also inadvertently introduce ethical risks and pose biosafety concerns, such as the enhancement of harmful viral properties like transmissibility or drug resistance. To address this issue, we introduce a novel approach using knowledge unlearning to selectively remove virus-related knowledge while retaining other useful capabilities. We propose a learning scheme, PROEDIT, for editing a pre-trained protein language model toward safe and responsible mutation effect prediction. Extensive validation on open benchmarks demonstrates that PROEDIT significantly reduces the model's ability to enhance the properties of virus mutants without compromising its performance on non-virus proteins. As the first thorough exploration of safety issues in deep learning solutions for protein engineering, this study provides a foundational step toward ethical and responsible AI in biology.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a method called PROEDIT for “unlearning” virus-related knowledge in pre-trained protein language models (PLMs) to reduce ethical and biosafety risks in protein engineering tasks. This approach appears to be adapted from text LLM unlearning techniques. The authors choose a three-scope training scheme, including an unlearning scope, a retention scope, and a corruption scope, to selectively remove virus-specific data while retaining general capabilities on non-virus proteins.

### Strengths
1. The approach focuses on unlearning knowledge of the protein model, a specific verticle domain, which is novel.

2. The discussion of baselines in the experimental section appears sound.

### Weaknesses
1. I believe that prior work on unlearning knowledge in text-based LLMs, with similar designs, should be properly credited in the methods section. 
The terms designed in the method section feel **similar** [1, 2] and (maybe thus) the design of the algorithm appears to lack explanation. 
Unfortunately, I could not find any explicit citations or discussions on how you design (or analogy, or choose) the algorithm used, and I hope I missed something, as it would otherwise be**inappropriate**.

2. Compared to unlearning in text, the task of unlearning in the protein context feels somewhat artificial, with relatively limited significance.

3. Regarding the algorithm, is there a more principled way to select $D^{\text{sim}}$?

4. A minor issue: please keep the notation for  $x_M$  and $x_{/M}$  consistent.

### Questions
In the domain of safety alignment in text generation, there are methods to teach models to abstain. Is there any feasibility for this approach in protein modeling?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces PROEDIT, a framework for knowledge unlearning that enables pre-trained protein language models (PLMs) to selectively forget virus-related information while preserving predictive accuracy for non-viral proteins. Empirical validation across benchmark datasets shows that PROEDIT successfully reduces predictive capacity for viral mutations without compromising performance on beneficial proteins. However, the paper lacks clarity on the real-world necessity of selective virus knowledge unlearning, and the practical implications of this setting remain underexplored. Additionally, the evaluation pipeline does not sufficiently substantiate PROEDIT’s claims regarding safety and efficacy, as it lacks rigorous alignment with the framework's stated goals. For these reasons, I do not believe this paper meets the standards for acceptance.

### Strengths
* **Precise Knowledge Unlearning Framework**: PROEDIT’s method incorporates a carefully designed approach to model parameter adjustment by defining unlearning, retention, and corruption scopes, allowing the model to selectively forget virus protein-related knowledge. This layered optimization helps to some extent in reducing the risk of affecting non-virus protein knowledge while also providing a degree of stability and adaptability to the model.

* **Comparison of Different Edit Methods**: The paper systematically examines various edit methods, including No Edit, Gradient Ascent, Joint Gradient Ascent and Descent, Random Labels, Gradient Ascent with KL Constraint, and the proposed PROEDIT. These comparisons provide clearer insights into the impact of each method on model performance and virus knowledge unlearning.

### Weaknesses
 * **Unclear Justification of the Setting**: The paper fails to clearly explain why it is necessary to remove virus-related knowledge in protein language models, especially as this task is uniquely proposed by the authors themselves. It states, "This approach reduces ethical risks, specifically the ability of deep learning models to enhance the properties of viruses, while maintaining the model’s overall performance in designing normal, non-harmful proteins." However, the paper confuses the concept of "proteins present in viruses" with "harmful proteins." Not all "proteins present in viruses" are harmful. On the contrary, some viral proteins are beneficial for protein engineering; for example, the capsid protein in adeno-associated virus (AAV, https://en.wikipedia.org/wiki/Adeno-associated_virus) is widely used in gene therapy and vector design due to its low pathogenicity and efficient gene delivery capability. Such viral proteins play an important role in certain biomedical applications, so removing virus-related protein knowledge across the board may be inappropriate. Furthermore, in the paragraph starting with "The same concern has been raised in mutation effect prediction tasks," the paper provides no references to support why removing “virus protein” knowledge is necessary. Overall, the justification for this setting lacks persuasiveness.

* **Methodological Limitations**: The entire approach has fundamental limitations. According to the paper’s inference, protein engineering should aim to “design normal, non-harmful proteins.” However, using an unlearning approach cannot effectively achieve this goal. A more straightforward method would be to determine if a generated protein sequence is harmful (or, as the paper suggests, a “virus protein”). If a “virus protein” is designed, it could simply be rejected. In bioinformatics, this task is relatively simple. For instance, one can use BLAST or other homology search tools to compare the protein sequence with known “virus protein” databases, such as “virus protein” sequences in UniProt. High sequence similarity often suggests functional or origin-related associations. Alternatively, protein function databases like Pfam or InterPro can be used to identify functional domains. If the protein contains domains commonly found in “virus proteins,” such as reverse transcriptase or capsid proteins, it may be identified as a “virus protein.”

   Even if we insist on a machine learning approach, a binary classifier could be trained using “virus protein” data to predict whether a given protein is a “virus protein.” Using an unlearning framework forces the model to forget information about “virus proteins.” However, if the model does generate a “virus protein” (even with a lower probability), it will not recognize it as such. Thus, an additional predictor would still be needed to identify potentially harmful proteins, as outlined in the simpler approaches above.

* **Question Regarding Results on the AAV Dataset**: The PROEDIT results on the AAV dataset, shown in Table 2 and Figure 4a, appear questionable due to the negative Spearman correlation, which remains consistently negative throughout training—a common mistake when fine-tuning ESM models on supervised mutation effect datasets. Since Spearman correlation measures rank-order agreement, flipping the predictions' signs would make the correlation positive. In this context, considering the absolute value of Spearman correlation would be more meaningful, as it better reflects whether the model still retains “virus protein” information. The results suggest that PROEDIT, particularly at the 150M scale, may still retain virus-related knowledge and even outperform the pre-unlearning model, thereby casting doubt on the true effectiveness of the unlearning process.

### Questions
See **Question Regarding Results on the AAV Dataset** in weakness.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
In this paper, the authors introduce protEdit, a protein language model fine-tuned with a specialized loss function aimed at "unlearning" certain virus sequences. They utilized the pre-trained ESM2 model, fine-tuning it on a dataset consisting of 65 million non-virus proteins and 560,000 virus proteins. The model was aligned with original non-virus-like protein sequences from the dataset. Several experiments were conducted to demonstrate the capabilities of the tuned model.

### Strengths
The paper is well-structured and easy-to-follow. 

The concept of addressing safety concerns within AI applications in biology is innovative and timely. While the paper’s exploration into protein fitness prediction has debatable relevance, the attempt to integrate ethical considerations into AI model training is commendable and adds a layer of originality to the work.

### Weaknesses
The fundamental premise of what constitutes 'harmful' protein engineering is not convincingly established in the paper. While the intent to prevent harmful applications is clear, the practical implications and ethical guidelines are not thoroughly explored. For instance, engineering on adeno-associated viruses (AAVs) can be beneficial for gene therapies, contradicting the notion of universal harm. (https://www.science.org/doi/10.1126/science.adm8386) Moreover, experiments on engineering antibiotic resistance genes can help us better understand its mechanisms and lead to the discovery of novel antibiotics (https://www.cell.com/fulltext/S0092-8674(15)00078-1). The experiment design, that simply define "engineering virus is unsafe" is not valid and fundamentally flawed from this point of view.

The authors should provide a more detailed discussion of how they define "harmful" protein engineering, acknowledging potential beneficial applications of viral protein engineering, and explaining how their approach could be refined to distinguish between beneficial and harmful applications.

I noticed that the authors conducted both supervised and unsupervised learning experiments on the virus-like proteins. For the supervised learning task, without LLM, other machine learning methods, even the one-hot encoding of the sequence, may work quite good – as we have the labels and any model can learn from the dataset (https://pubmed.ncbi.nlm.nih.gov/35039677/). From Table 2 it’s surprising for me to see protEDIT does not work at all for supervised tasks, it suggests that the model embedding for these sequences are simply useless. Moreover, it’s confusing that the authors tried their best to learn an embedding that is probably worse than one-hot. If so, why do we need your model?

For the unsupervised variant effect prediction, I have to say that it's the MSA that matters. The EVE (https://www.nature.com/articles/s41586-021-04043-8), DeepSequence (https://www.nature.com/articles/s41592-018-0138-4) can performs better than language model. Even the BLOSUM62 can carry some information for the mutation effect prediction. SO I did not see what the hint was in poisoning the language model. The entire experiment design does not sound right to me.

For me the idea of this paper is like a straw man proposal. The authors try to do something that seems to be useful but totally miss the key points and lead to something useless.

### Questions
See weakness

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses mutation effect prediction. The authors proposes PROEDIT, a knowledge unlearning-based approach, which refines pre-trained models by distinguishing among three sets of training data and unlearning specific targets. The method is validated on open benchmarks, showing it can reduce the model's ability to enhance virus mutants without sacrificing performance on non-virus proteins. 

*I am not familiar with the research problem, so I am eager to see the feedback from the authors and the opinions of the other reviewers.*

### Strengths
- This paper investigates a critical problem: the safety issue in pre-trained PLM models. 
- The authors demonstrate the effectiveness of the method through experiments on various benchmarks.

### Weaknesses
 - Insufficient baseline comparisons; it is advised to add more PLM models mentioned in the related work.
- As shown in Table 3, it seems that PROEDIT only achieves the best performance in ProteinGym (Virus) on the Perplexity metric, which diminishes the contribution of PROEDIT.
- The efficiency section should include more comparisons with other methods.
- The ablation study for the different scopes (Unlearn, Retention and Corruption) is not provided.

Minor:
- It lacks a discussion of the relationship of this work in the related work section, which would help readers better understand this study.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
