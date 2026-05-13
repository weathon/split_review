# Efficient Fine-Tuning of Single-Cell Foundation Models Enables Zero-Shot Molecular Perturbation Prediction

- Decision: Reject
- Scores: 6, 8, 6, 3, 6

## Abstract
Predicting transcriptional responses to novel drugs provides a unique opportunity to accelerate biomedical research and advance drug discovery efforts. However, the inherent complexity and high dimensionality of cellular responses, combined with the extremely limited available experimental data, makes the task challenging. In this study, we leverage single-cell foundation models (FMs) pretrained on tens of millions of single cells, encompassing multiple cell types, states, and disease annotations, to address molecular perturbation prediction. We introduce a drug-conditional adapter that allows efficient fine-tuning by training less than 1\% of the original foundation model, thus enabling molecular conditioning while preserving the rich biological representation learned during pretraining. The proposed strategy allows not only the prediction of cellular responses to novel drugs, but also the zero-shot generalization to unseen cell types.  We establish a robust evaluation framework to assess model performance across different generalization tasks, demonstrating state-of-the-art results across all settings, with significant improvements in the few-shot and zero-shot generalization to new cell types compared to existing baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors explore the challenge of predicting cellular transcriptional responses to novel molecular perturbations, a critical task in drug discovery. By leveraging pre-trained single-cell foundation models on large-scale datasets, the authors propose an efficient fine-tuning method using a drug-conditional adapter (scDCA). This approach utilizes less than 1% of the original model's parameters, allowing for efficient adaptation to novel drugs and cell types, even in zero-shot settings. The paper demonstrates that scDCA significantly outperforms existing baselines in various prediction tasks, including unseen drug-covariate combinations and zero-shot cell type generalization.

### Strengths
The introduction of drug-conditional adapters is an innovative and efficient method for fine-tuning large single-cell FMs, which is particularly impressive given the reduction in trainable parameters. This efficient approach maintains the original biological representations, allowing the model to generalize to new cell types and drugs.


The authors effectively build upon the latest advancements in transfer learning and efficient model adaptation, such as prefix tuning and hypernetworks. The use of a transformer-based single-cell FM architecture (scGPT) combined with pre-trained molecular embeddings (ChemBERTa) demonstrates a sophisticated integration of modalities.

The paper is well-structured, with a thorough explanation of the scDCA architecture and the experimental setup. The inclusion of figures and tables to illustrate model performance across various tasks aids in understanding the results.

### Weaknesses
The experiments are primarily conducted on the sciplex3 dataset, which, although extensive, focuses on a limited number of cell lines and drugs. The generalizability of scDCA to broader datasets with more diverse cell types and perturbations remains to be demonstrated. If no single-cell dataset is available, how about using the LINCS L1000 dataset? The NIH LINCS L1000 dataset provides rich gene expression profiles for thousands of chemical perturbations across diverse cell lines. Its comprehensive scope and availability would significantly enhance the evaluation of the scDCA model, particularly for zero-shot and few-shot generalization tasks. Incorporating this dataset would validate the model’s robustness and broaden its applicability in predicting transcriptional responses to novel drugs (One caution when using this dataset is that it can be somewhat noisy). While the LINCS L1000 data offers a rich resource for bulk transcriptomic studies, *it may not directly align with the single-cell focus of the paper*. However, it could still be useful for comparison studies. It could be used to compare how predictions from bulk data differ from those based on single-cell data, highlighting the added value of single-cell resolution.


While the model achieves strong predictive performance, there is limited discussion on the biological insights derived from the model's predictions. Understanding which gene-gene interactions or molecular features drive the predictions could enhance the impact of the work for biological research.

### Questions
The paper focuses on in vitro transcriptional responses using single-cell RNA sequencing data. However, translating these predictions to in vivo or clinical settings, where cellular environments are significantly more complex, remains an open challenge. How feasible do you think it is to extend this model to such real-world scenarios?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduce single-cell drug-conditional adaptor (scDCA), an approach to fine-tune existing single-cell foundation models to predict the effect of drug perturbations in various cell-types in a parameter efficient way. scDCA accomplishes this by freezing the foundation model, scGPT in this case, and incorporating a drug-conditional adaptor in each layer. In doing so the authors show scDCA can generalize to unknown drug perturbation and cell types.

### Strengths
Work is original, the idea of injecting molecular embeddings in a way that stops catastrophic forgetting in single-cell foundation models is interesting and has not, to my knowledge, been shown before. Work is easy to follow and well-explained and addresses an important problem in predicting gene expression. If we had a model that could predict the effect in gene expression of drugs, it would revolutionize drug discovery. This model is the first step towards this reality.

### Weaknesses
I have a list of concerns that I would like to be addressed before I can accept this paper. They are listed below:

1. Figure 2 needs to be improved. I understand that the icons to the left are different cell types but they should be labeled, I see the neuron in the middle but what are the other two? Also what does each square represent a data point? I understand what you are trying to show but it can be visualized better, the figure is confusing as it stands now.
2. Why not take the output of the scGPT plus the output of the molecular embedding, concatenate it to predict the effect of expression. Is this the experiment shown in section A.2?
3. "By featurizing cell types based on their initial gene expression, our framework can generalize to unseen cell types in both zero-shot and few-shot settings." Line 328. This is not really a result of the framework, it is the result of using the scGPT and doing this efficient fine-tuning. The generalization to different cell-types arises from keeping the knowledge from the pretrained foundation model, the framework does not add anything to the pretrained model from the perspective of cell-types.
4. There needs to be statistical tests for Figure 3, there is large overlap in the error-bars. A t-test to show the difference is significant is necessary to deem if there is actual improvement.
5. It does not make sense that in Table 1 few-shot cell-type prediction is an easier task than unseen drug covariate.
6. What is Figure 7? What does DEG stand for? What is it showing?
7. Arguably the most important experiment of this paper is in scDCA predictions are robust across different targets, but the authors are vague in the description of the experiment and their results. Specifically what is meant by this phrase: "We grouped R2 for each target-cluster"?
8. I believe the claim that the model generalizes to novel cell-types is a bit exaggerated. The cell-types assessed in this paper are two breast cancer cell-lines and one leukemia cell-line. Did the authors make sure that the breast cancer cell-lines did not appear in both the train and test set in the cell-type splits because even though they have different names they would be very similar in expression profile. 
9. For the unseen drugs how similar are the drugs to each other? Can there be a plot of Tanimoto similarity of the drug-similarity in the splits. If the drugs are structurally very similar then the model can overfit on that.
10. One of the biggest problems in this paper is the overlap between scGPT pertaining set and this test set. Has scGPT already seen the gene expression vectors of these perturbation experiments? Could this not make the results seem much better than they are? This could also explain why the fine-tuning did so poorly, because scGPT had forgotten information it had already seen. Even if scGPT did not see exactly the same vectors it could have seen vectors that are very similar.

### Questions
1. I am confused by the terminology "covariate"? What is a covariate? Cell-type? I have not seen this word used in single-cell literature and ask the authors to clarify its meaning. If it means cell-type why not say cell-type?

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
This work considers the molecular perturbation prediction by leveraging Foundational Models (FMs). More specifically, it introduces scDCA, which utilizes the pretrained FM, scGPT, that is trained on single cell omic data. In this design, to enforce the molecular information, an adapter layer has been introduced to the model which allows for an efficient fine tuning of the model by keeping the FM’s weights frozen, while allowing for considering an extra modality.

### Strengths
1.	Enables fine-tuning with a limited paired data by training only the drug conditional adapter layer.
2.	By using the adapter and ChemBERTa, a molecular FM, scDCA enables the utilization of different modalities information due to its design. 
3.	It seems that based on the provided results, the proposed framework leads to superior performance with respect to baselines.

### Weaknesses
1.	One of the challenges that this study considers is data scarcity. Although there are many recently proposed parameter efficient fine-tuning approaches, they are not considered in evaluations (table 1). 
2.	There is no clear explanation on canonical projection. 
3.	The diagram in figure 1 does not match with the projections in equation 5 (based on the diagram, for both $h^{down}$  and $h^{up}$  use the projection of $b_l$ ; however, in equation for $h^{up}$ only $b_l$ is in the summation). In general, it is not obvious if projection is referring to module $f$ or the canonical projection.
4.	The quality of figure 7 is very bad.

### Questions
1.	Why other FMs are not considered in this work? Comparison with other single cell FMs can provide more insights in the benefits of the proposed adapter architecture.  
2.	Why other parameter efficient fine-tuning methods are not considered in the evaluation? This could provide more insight into the capabilities of scDCA specifically in capturing the domain shift.
3.	Is it possible to do an ablation study, specifically to show the effect of Resnet more clearly?
4.	Is it possible to explain why in figure 4 for some genes the predicted expressions are out of the true expression regions? 
5.	Again, in figure 4, for many genes the predicted expressions are close to the ends of the True expression regions. Is it possible to provide an evaluation of framework’s reliability and limitations?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper's authors introduce scDCA, a fine-tuning strategy for foundation models to predict single-cell RNA-seq perturbations in a zero-shot fashion. A pre-trained transformer model (in this case, scGPT) is adapted to the task of perturbation prediction by introducing an adapter module. The authors freeze most of the foundation model and only train the adapter module downstream. Such a module inputs drug representations (different modalities) and uses them to steer average control expression to its drug-perturbed counterpart. Moreover, scDCA can deal with unseen cell types by using their average control expression as input. In this way, scDCA is flexible: It can tackle missing compounds, cell types and combinations thereof. The authors present superior performance in comparison with four perturbation models on the task of recapitulating the perturbation effects based on differentially expressed genes. Furthermore, the paper presents qualitative results of successful drug effect prediction by showing that the model induces a gene expression shift on control compatible with the real perturbation direction.

### Strengths
I think the idea at the core of the paper is really original, interesting and promising. With the increase in the size of modern single cell datasets and representation models, I believe that research should focus on how to build additional ML tasks as efficiently as possible. The paper is therefore timely and interesting in the modern context. An additional positive aspect is that the performance appears to be good and solid according to the results provided by the authors.

### Weaknesses
* In the introduction a sentence is formulated as follows “Additionally, several methods focus on predicting the effects of genetic perturbations, where the number of possible treatments is fixed (approximately 20,000 genes) (Roohani et al., 2023). These approaches are not directly applicable to explore the vast chemical space, which is estimated to encompass up to 10^60 drug-like compounds”. In the first sentence, you talk about genetic perturbations, but then the vastness of the chemical space is brought up. I found this a bit confusing. 
* In my opinion, it is a little bit unfair to define the model as “state of the art”. The proposed evaluation is not exactly the same as in e.g., chemCPA or CPA. Specifically, the model’s performance has not been tested on held-out compounds like in the aforementioned models. I believe the authors should maybe add a disclaimer on the level of superiority their model implies. 
* There is a bit of an overuse of the variable c. First, it is introduced as a cell type indicator, while later it is used as a gene-specific attribute in the description of scGPT. I think the presentation would be clearer with a different notation. 
* Line 261-262: since it is a claim, it would be nice to have some citations!
* When presenting the feature-based approach in 3.2, it is not clear what kind of model you compare the scDCA approach within Appendix A.2. Since you are doing perturbation prediction, do 
* In Eq. 4, the authors introduce a control embedder. Connecting it to what is explained in line 10, the authors take the average embeddings of the controls of a cell type c and perturb it synthetically using the model. However, if I understand correctly, the value $X^0_c$ is an average. Does it mean that only the average control is subjected to synthetic perturbation? Are you not neglecting a lot of information on potential control heterogeneity? 
* I think the paper lacks a more rigorous description of the training process that can be integrated into the extra page. I would encourage the authors to explicitly define the target of the perturbation prediction task when starting from the average control expression. Probably the presence of an algorithm would help. Currently, I struggle to understand what task is used to ensure plausible predictions by the FM. 
* In my opinion, Figure 3 is really hard to understand. I am not sure which plot refers to which task. 
* Is the benchmark against existing models performed on held-out genes? This is not mentioned in the text describing the experiments. In the negative case, I would definitely expect to see a comparison in performance against chemCPA on leave-out compound predictions, using the same splits as in the original paper. 
* Figure 4 does not convince me completely. I would find it beneficial to, for each gene, overlay the control distribution on the perturbed distribution to confirm that the model is really predicting extreme values of the control distribution.
* I think the conclusion should also contain some limitation discussion.
* In my opinion, the appendix is not well-curated and organized. Plot labels are cut too. I do understand that the may be a matter of time, but I would encourage the authors to increase the amount of detail in future iterations of the work, especially on the baseline comparison experiments. 
* To appreciate the value of Figure 5 I think I would need to see a comparison with other perturbation models like chemCPA. 

Although potentially promising, I am not sure the paper is ready for publication yet. In my opinion, the presentation of the methods should be more thorough and detailed. I am happy to discuss my doubts with the authors during rebuttals and potentially change my opinion.

### Questions
* Does the adapter fit well with other types of foundation models aside from scGPT? I think it would be great to introduce an Appendix discussion about this. 
* In Sec 3.1, lines 209-214 I struggle to understand the logic. In the first sentence, it is claimed that control profiles are aggregated as cell line representations. Then you go on saying that you do it for all cell line drug pairs. What are the drug-cell line covariate embeddings used for? I would really appreciate it if the authors could elaborate on this a bit more and clarify this point. 
* To me, it is not very clear what objective is used in 3.2. You input the (average) control expression, the condition and the identity token. Then what loss do you calculate to evaluate the correctness of the prediction? You mention the loss in Equation 3, but how is it applied here to make sure an average control expression Is correctly perturbed? To me, this aspect is a bit unclear across the whole paper. 
* Is the evaluation carried out to the 20 top DEG or also the prediction? I.e. Do you both predict and evaluate on a limited number of genes or predict on the whole transcriptome and evaluate on the subset of genes?
* Are all baselines able to perform all tasks out of the box? Or do you have to adapt them for them? I think it would be beneficial to include a description of of baseline models and how they were run for comparison in the appendix.

### Soundness
2

### Presentation
1

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
This paper introduces a parameter-efficient approach to fine-tune single-cell foundation models for predicting how cells respond to drug treatments. They develop a "drug-conditional adapter" that allows them to inject information about molecular structures (from external embeddings) into the model while keeping the original foundation model frozen. Their method enables both prediction of cellular responses to new drugs and generalization to entirely new cell types that weren't seen during training. They demonstrate their approach outperforms existing methods particularly in few-shot and zero-shot scenarios where the model must generalize to new cell types.

### Strengths
- practical approach: leveraging foundation models for drug response prediction is highly relevant for drug discovery
- Interesting approach to solving the challenge of incorporating molecular structure information into gene expression models
- Comprehensive evaluation framework testing multiple important scenarios (unseen drugs, drug-covariate pairs, zero-shot). Generally I find the results fairly convincing.
- Results on zero-shot generalization to new cell types are valuable for real-world applications

### Weaknesses
- I find the rationale for the adapter a bit unconcinving in it's current state:
	- the authors talk about parameter efficiency but the base model is only 53M parameters so can easily and quickly be finetuned on a consumer GPU. As such, I don't find the parameter efficiency a good selling point of this paper.
	- I'm surprised how poorly the full model finetune performs in some of the settings. Probably I'd find the paper even more useful if the authors managed to get full model FT working, since that's easier to replicate (less complexity).
- The rationale behind the bottleneck design isn't well explained
- Missing important experimental details that would help reproducibility (GPU requirements (compared to full finetune), training time, hyperparameter selection). Could you add these to the paper?
- Several broken citations need fixing (their venue is not listed): Chemberta, Bert and a few others.
- The statement about residual connections facilitating drug-cell type interactions lacks citation / grounding (line 331)

### Questions
1. The ResNet component in their adapter architecture is inadequately explained. When I hear ResNet, I think about ResNet the model whereas the authors  seem to be using it to mean a generic residual connection. Could you clarify exactly what's happening in the ResNet block of your adapter?
2. Why did you choose a bottleneck design for the adapter rather than a larger architecture? What were the key considerations?
3. Could you provide more details about computational requirements (GPU usage, training time, memory requirements) for both your adapter approach and the full fine-tuning baseline?
4. Figure 4 lacks labels. I assume these are the same order as table 1?

### Soundness
3

### Presentation
3

### Contribution
3
