# BounDr.E: Predicting Drug-likeness through knowledge alignment and EM-like one-class boundary optimization

- Decision: Reject
- Avg Score: 4.40
- Scores: 5, 5, 3, 3, 6

## Abstract
The advent of generative AI models is revolutionizing drug discovery, generating de novo molecules at unprecedented speed. However, accurately identifying and rescuing drug candidates among countless generated molecules remains an open problem.
The essence of this drug-likeness prediction task lies in constructing a compact subspace that encompasses majority of approved drugs with only a small number of unknown compounds (drug candidates) inside.
Computational challenges arises in constructing a decision boundary on an unbound chemical space that lacks definite negatives, i.e, non drug-likeness.
Approved drugs exist highly dispersed across structural space, making it more harsh to effectively separate drugs from non-drugs through existing classifiers. 
Addressing such challenges, we introduce BounDr.E: a novel approach for learning a compact boundary of drug-likeness through an Expectation-Maximization (EM)-like iterative optimization process. 
Specifically, we refine both the boundary and the distribution of the embedding space via metric learning, allowing the model to iteratively tighten the drug-like boundary while pushing non-drug-like compounds outside.
Augmented by integration of biomedical context within knowledge graphs via multi-modal alignment, our model demonstrates 10% increase in F1 score over the previous state-of-the-art, along with strongest robustness to cross-dataset validation.
Zero-shot toxic compound filtering and comprehensive drug discovery pipeline case studies further showcases its utility in large-scale screening of AI-generated compounds. 
To facilitate in silico drug discovery, we provide the code and benchmark data under various splitting schemes at: https://anonymous.4open.science/r/boundr_e.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper's central contribution lies in its attempt to merge biomedical knowledge with structural information for drug-likeness prediction. However, the approach reveals several concerning technical limitations that significantly impact its potential impact and practical utility.
The authors' adaptation of the CLIP loss for knowledge alignment (Equations 2 and 3) appears superficially innovative, but closer examination reveals concerning oversimplifications. The assumption that ATC classification similarities can be directly translated into embedding space relationships is problematic and insufficiently justified. The authors fail to address the inherent hierarchical nature of ATC classifications and how this hierarchy affects similarity computations. This oversimplification potentially introduces systematic biases in the learned representations. The EM-like optimization process, while mathematically presented with apparent rigor, suffers from serious theoretical gaps. The proof of Theorem 1 relies heavily on assumptions that are neither fully justified nor empirically validated. Most concerningly, the authors claim convergence properties without adequately addressing the potential for local optima or the impact of initialization conditions.

### Strengths
1.The paper introduces a novel technical framework integrating biomedical knowledge with molecular structure representation. The use of multi-modal alignment through softened CLIP loss represents an interesting attempt to bridge the gap between chemical structure and biological function.

2.The theoretical foundation, particularly the EM-like boundary optimization process, is mathematically formulated. The authors provide formal proofs for boundary convergence (Theorem 1) and establish conditions for reducing in-boundary non-drugs.

3.The experimental framework appears comprehensive, employing both scaffold-based and time-based splits to evaluate generalization capability. The integration of zero-shot toxic compound filtering demonstrates potential practical utility.

### Weaknesses
The paper introduces a novel technical framework integrating biomedical knowledge with molecular structure representation. The use of multi-modal alignment through softened CLIP loss represents an interesting attempt to bridge the gap between chemical structure and biological function.

The theoretical foundation, particularly the EM-like boundary optimization process, is mathematically formulated. The authors provide formal proofs for boundary convergence (Theorem 1) and establish conditions for reducing in-boundary non-drugs.

The experimental framework appears comprehensive, employing both scaffold-based and time-based splits to evaluate generalization capability. The integration of zero-shot toxic compound filtering demonstrates potential practical utility.

The softened CLIP loss formulation (Equations 2,3) oversimplifies the complex hierarchical nature of ATC classifications. The geodesic mixup strategy lacks proper ablation studies to justify its effectiveness. The boundary optimization process shows concerning sensitivity to initialization conditions, which is inadequately addressed.

The reported "five orders of magnitude improvement" raises serious concerns about potential data leakage or experimental design flaws
Baseline comparisons appear biased, with competing methods using suboptimal default parameters. The scaffold distribution (1.97 molecules per scaffold) indicates extreme sparsity, yet its impact on model generalization is not properly analyzed. Statistical significance testing is notably absent from all experimental results.

Neural architecture choices (2-layer MLP, 512-dimensional hidden layers) lack proper justification. Training protocol shows concerning arbitrariness in hyperparameter selection. The convergence criterion based on in-boundary compound ratio is potentially unstable. Computational complexity analysis is entirely missing.

Zero-shot toxicity prediction results lack proper error analysis and statistical validation. The time-based split evaluation inadequately addresses temporal evolution in drug discovery practices. External validation sets are limited and potentially biased. The relationship between model predictions and actual experimental outcomes is not explored

### Questions
1.What theoretical guarantees exist for avoiding local optima in the EM-like optimization process?
2.How does the method handle conflicting or inconsistent information between structural and knowledge-based representations?
3.How could the method be adapted for specific therapeutic area focusing?

### Soundness
3

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
3

### Summary
The authors present a method to predict drug-likeness. Precisely, they a) use a contrastive learning scheme to learn a joint embedding space for molecular structure and biomedical context, and b) learn a decision boundary by an EM algorithm. The authors show that their approach outperforms compared methods on the task of distinguishing DrugBank molecules from ZINC molecules. Also they showed that their method is capable of filtering toxic compounds.

### Strengths
- **Clarity**:  The paper is generally well-written. The scope of the work and the research question are clearly presented. The proposed method, including the multi-modal alignment and the EM-algorithm-based decision boundary, is well described.
- **Significance**: The presented method clearly outperforms compared methods. Results are presented with error bars (standard deviation across cv).
- **Relevance**: Drug likeness is an important property to consider in drug discovery projects. Therefore, improved methods to detect drug likeness are desirable.

### Weaknesses
 - **Little Novelty**:  There is a lot of work wrt aligning two modalities with contrastive learning methods. E.g. the presented idea of softening the CLIP matching has been done before [1].
- **Clarity**: The presented method is provided with enriched information about biomedical context. The authors missed to explain whether baseline method did get a fair chance to operate on this enriched data base as well. Could have performance gains just have arisen because the presented method is provided with more information (biomedical context)?
- **Experiments**: The ablation study is informative. However it would have been interesting to train a MLP (i.e. a universal function approximator) on top of the embeddings from the contrastive learning space to estimate the effectiveness of the EM-based algorithm. What is the intuition why a MLP should not be capable of learning a proper boundary? Is it that not only the boundary but also the encoder is iteratively updated in the EM algorithm? If so, can it be shown that this is the critical point?

Comment about hard negatives: Also the proposed method is trained in a way strictly treating non drug-like molecules as negatives while the EM algorithm adjusts the decision boundary. (Compare l72ff - related work: supervised models treat unlabeled compounds as hard negatives.)

### Questions
- Could have performance gains just have arisen because the presented method is provided with more information (biomedical context)?
- What is the intuition why a MLP should not be capable of learning a proper boundary? Is it that not only the boundary but also the encoder is iteratively updated in the EM algorithm? If so, can this be somehow shown?
- What if the structural and biomedical representations are naively concatenated and fed into an MLP? Shouldn't this approach be able to get  similar performance values compared to the presented one without the need of the two-stage training procedure?

Comment about hard negatives: Also the proposed method is trained in a way strictly treating non drug-like molecules as negatives while the EM algorithm adjusts the decision boundary. (Compare l72ff - related work: supervised models treat unlabeled compounds as hard negatives.)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper poses the main challenges for the drug-compound identification task: the absence of a clear negative class and the vastness of chemical space. This paper proposes a targeted solution, using an EM-like optimization process to avoid strict decision boundaries. In addition, a contribution is to propose a novel multimodal alignment module to more effectively capture drug-like related features. Experiments have demonstrated the effectiveness of the proposed method.

### Strengths
1.  Sound motivation and clear writing. I can clearly understand the problem that this article focuses on. I also agree that this is the main challenges of this task. I can quickly and easily get the technical details (method part) of this article.

2. The author provides detailed introduction to the various technologies and designs used, which is very reader-friendly.

3. Experimental results show obvious advantages from proposed method. Code is provided and is (at least) runnable.

### Weaknesses
1. By reading the setting and challenges of the task, I would like to question whether this is a standard PU learning setting. If so, the author could have directly introduced this common scenario (if I am wrong, please correct me). In addition, line106 points out that the existing PU learning methods rely on negative samples, which is confusing. As far as I know, the **training process** of PU learning does not provide negative samples.

2. This point is associated with weakness 1. I do not quite understand the problem setting. This paper claims that most existing methods rely on defined negative samples. So is there any difference in problem setting from BounDr.E and others? To my understand, this task suggest training with positive and unlabeled samples and testing with defined positive and negative ones. If the settings among papers are consistent, you can directly say that something like "The drug-compound identification task are commonly formulated as a PU learning setting. However, existing methods xxxxxx". If not, perhaps you should first introduce the difference.

3. Question about the experiment setup. Drugbank and Zinc datasets are used, but it seems like there is still no defined negative samples. If yes, how do you get them? I personally think that it is not difficult to create some real negative samples for the test set. The simplest way is to predict or query whether a molecule is toxic. We can regard toxic molecules as absolutely non-drug (for training and testing). If your test set does not have absolute negative samples, you should not consider metrics such as F1, but should refer to the ones such as recall in the recommendation system task. If the test set has negative samples, the metric you use is reasonable.

### Questions
N.A.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses the challenge of accurately identifying drug candidates, an essential task in the drug discovery process. The authors introduce BounDr.E, a novel method designed to construct a compact boundary of drug-likeness within the chemical space. The approach utilizes an Expectation-Maximization (EM)-like iterative optimization process combined with metric learning to refine both the drug-like boundary and the embedding space distribution. By incorporating biomedical context through multi-modal alignment with knowledge graphs, BOUNDR.E achieves significant improvements in drug-likeness prediction, reportedly up to five orders of magnitude in performance metrics. The model's effectiveness is further demonstrated through zero-shot toxic compound filtering and detailed case studies, showcasing its value in large-scale screening of AI-generated compounds.

### Strengths
The paper is thorough, offering extensive details on the algorithm, experimental settings, and data used, making it self-contained and easy to follow. 

The proposed method builds upon a foundation of established works, such as DREAMwalk and Geodesic Mixup, which contributes to its enhanced performance. 

Additionally, the authors have provided theoretical justification for the M-step of the EM-like algorithm, adding further depth to their approach.

The code is provided, ensuring the reproducibility of this work.

### Weaknesses
Relying solely on a fully data-driven approach to estimate drug-likeness might be risky and may deviate from a more rational pathway for drug discovery. A more effective strategy for screening drug candidates involves predicting specific properties—such as toxicity and the binding affinity of a drug to specific targets—and leveraging these properties to filter molecule databases, thereby identifying promising drug candidates more reliably. This may indicate the limitation of the proposed framework in real-world practice of drug discovery.

The experiments can be more extensive. One limitation noted is the demonstration, using only one specific example, where the average probability density function (pdf) of Imatinib increased after filtering with the proposed methods. Relying on a single example may not comprehensively illustrate the method’s effectiveness or generalizability.

The authors claim that no attempts have been made to align the biomedical knowledge graph embedding space with the molecular structural embedding space for downstream tasks. However, to my knowledge, several studies have already explored unifying molecular structures with knowledge graphs for tasks like property prediction [1,2,3]. Additionally, multi-modal alignment with contrastive learning is not a novel approach.

Drug discovery is fundamentally a multi-objective optimization problem. In its early stages, the goal is not to minimize the number of molecules screened, but to ensure that the selected molecules meet the property requirements for further drug development. The results in Table R4-1 only compare the number of remaining molecules after filtering, which cannot demonstrate the effectiveness of BounDr.E.

As a data-driven virtual screening method, BounDr.E lacks the interpretability for the predicted results compared with property-driven approaches [4].  This creates significant challenges for subsequent drug development; merely being close to known drugs in the "latent space" does not provide meaningful insights for drug discovery on a specific target, as drug targets are highly specific.

What advantage does BoundDr.E offer when used alongside other property-driven approaches, beyond simply yielding fewer filtered samples? Can BoundDr.E enhance screening outcomes by selecting molecules with better drug-like properties? The presented results (e.g., in Table 5) do not seem convincing enough to demonstrate the superiority of this model.

Defining "drug-like" molecules is inherently challenging, and I question the approach of setting a boundary to filter candidate molecules rather than using distance-based measurements. How do we truly measure "likeness" and what makes one molecule more "drug-like" than another? Property-based methods may address this issue more effectively, providing a clearer rationale for why a given molecule may not qualify as a potential drug. This work also doesn't provide structural analysis (e.g. scaffold, functional motif, non-covelant interactions) of filtered molecules to support the drug-likeness results. As I have mentioned, relying solely on a fully data-driven approach to estimate drug-likeness may be risky and insufficiently convincing. The authors should consider analyzing the results using domain knowledge or comparing them with traditional methods to demonstrate the effectiveness of their approach [5,6].

To evaluate the properties of filtered molecules, the authors only tested QED, Ro5, and toxicity. However, I believe these metrics alone are insufficient to demonstrate a molecule's drug-likeness. Binding affinity, for example, is a crucial evaluation metric and would provide a more comprehensive assessment of the molecules' potential.

### Questions
See the weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors address two main challenges:

1. The accuracy of identifying drug candidates is still challenging.
2. The distribution of existing approaved drugs is wide-spread, make the one-class classification more challenging. 

The authors address the problem by proposing:

1. a novel multi-modal mixup framework for aligning knowledge between knowlwdge graph and structural embedding space. 
2. a improved EM-like algorithm to optimize the decision boundary for one-class classification between drug and non-drug compounds.

Through experiments, the proposed method achieves State-Of-The-Art around all metrics. Also, extensive experiments such as zero-shot prediction, embeeding visualization, and distance distribution demonstrates the robustness and effectiveness of the method. Finally, the method is applied to filter generated drug candidates, making it potential applicable to wider field of drug filtering.

### Strengths
1. The method improvement is well-designed and very closely related to the existing challenges. 
2. The experiment validation from different perspectives are comprehensive and sound. 
3. Mathmatical proof is well-written and supportive to the approach enhancement.

### Weaknesses
1. Some evaluation metrics are not well-designed, and some conlusion drawn from experiments are not reasonable. 
2. Somehow, KS-mix lacks novelty.

### Questions
1. Regarding Section4.1, the training data is chosen from DrugBank and ZINC. I can understand the proposed two split methods, but is it possible selecting compounds from other datasets to construct the dataset? It is because in your proposed setting, there should be an intersection between the distribution of drug and compunds. Moreover, the larger the intersection is, the more challenging the task would be. In the paper, only one compound dataset is employed without initial distribution analysis, which makes the validation of model's performance to the real-world dataset questionable. Would you please provide a more detailed introduction to the dataset construction and distribution analysis?

2. Regarding Section4.2, three metrics are proposed, including ICR, IDR, and IDR/ICR. I have two doubts. The first one is the proposed EM improvement would benefit identifying identifying the boundary. But w.r.t. ICR, the performance is lower than existing methods like DeepDL and D-GCAN. Does it mean that the drug decision boundary is relative poor? The second question is that in line 357, "IDR/ICR ratio to report the models’ capability in balancing the trade-off between inclusion of drug-like compounds with exclusion of non-drugs.". But, the detection of drug and compounds is not correlated, which means that is it not a binary classification senario like MCC and F1. Also, the ratio of two metric cannot refect the tradeoff. Instead, the sum would be a better one. Would you please provide a detailed explanation on this metric?

3. In Figure6, there is performance comparsion between F1 score according to Drug/Compound Ratio. We can see that higher ratio leads to higher difficulty. Futhermore, the proposed method achieves SOTA only when the ratio is over 1:50. Thus, a natural question is that what is the corresponding ratio in your training and testing sets. 

4. In Figure8, the caption states that "BOUNDR.E-filtered set shows more distinct distribution of molecular propertirs from the original 10k molecules." But, in the plot results, the above conclusion seems not able to be easily drawn. May you provide a detailed analysis?

### Soundness
3

### Presentation
3

### Contribution
3
