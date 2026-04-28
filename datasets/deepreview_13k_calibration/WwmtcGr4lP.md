# GANDALF: Generative AttentioN based Data Augmentation and predictive modeLing Framework for personalized cancer treatment

- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 6, 8, 6, 8

## Abstract
Effective treatment of cancer is a major challenge faced by healthcare providers, due to the highly individualized nature of patient responses to treatment. This is caused by the heterogeneity seen in cancer-causing alterations (mutations) across patient genomes. Limited availability of response data in patients makes it difficult to train personalized treatment recommendation models on mutations from clinical genomic sequencing reports. Prior methods tackle this by utilising larger, labelled pre-clinical laboratory datasets (‘cell lines’), via transfer learning. These methods augment patient data by learning a shared, domain-invariant representation, between the cell line and patient domains, which is then used to train a downstream drug response prediction (DRP) model. This approach augments data in the shared space but fails to model patient-specific characteristics, which have a strong influence on their drug response. We propose a novel generative attention-based data augmentation and predictive modeling framework, GANDALF, to tackle this crucial shortcoming of prior methods. GANDALF not only augments patient genomic data directly, but also accounts for its domain-specific characteristics. GANDALF outperforms state-of-the-art DRP models on publicly available patient datasets and emerges as the front-runner amongst SOTA cancer DRP models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose GANDALF, a framework that leverages attention-based generative models to augment patient genomic data, addressing limitations in data availability and patient-specific characteristics within existing models. GANDALF demonstrates superior performance over state-of-the-art models in predicting drug responses for cancer treatments.

### Strengths
- The studied problem is important and practical. 

- The idea of incorporating patient-specific characteristics with drug response prediction models is novel. 

- The code is provided for reproducibility.

### Weaknesses
 - The comparative performance analysis in Table 1 focuses on only 5 drugs, which is a small subset of the 56 drugs mentioned in the dataset. The paper does not justify why these specific drugs were chosen or demonstrate that the performance advantages generalize across the broader drug set. This limited evaluation makes it difficult to assess the method's robustness across different drug classes.  The paper needs to demonstrate results across a more diverse set of drug classes and provide statistical tests showing whether performance advantages hold across the full drug set.

- The authors state "we do drug-specific model tuning in GANDALF, by only augmenting with sample, drug pairs for the drug considered." This approach may cause extensive computational burden, as it requires fine-tuning for each new drug, potentially limiting its practical deployment. The computational cost of this approach, especially with a large number of drugs, is not discussed. Furthermore, the paper does not specify the exact fine-tuning procedure, such as the number of epochs, learning rate, or other hyperparameters, making it difficult to assess the practical feasibility and resource requirements of this drug-specific tuning.

- The paper does not address how well GANDALF generalizes to novel drugs in out-of-domain scenarios—a critical consideration given that new drugs are regularly introduced into clinical practice. The model's ability to handle drugs with different mechanisms of action or chemical structures is not explored, which is a significant limitation for real-world applicability.

- Though the paper deals with the challenge of limited patient data, it doesn't systematically analyze how performance varies with different amounts of training data. There's no exploration of learning curves showing how model performance changes with increasing patient samples, or minimum data requirements for reliable predictions. The paper should investigate the sensitivity of the model to varying amounts of real and synthetic data, and determine the minimum amount of real patient data required to achieve a certain level of performance.

### Questions
See weaknesses above.

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
This study presents GANDALF, a generative, semi-supervised framework addressing the challenge of limited labeled data in sparse patient genomic datasets by leveraging cell line data and augmenting patient samples with their clinical information. However, key concerns include the need for clearer model justification, additional technical details, and further clarity in experimental results.

### Strengths
- This study introduces GANDALF, a novel generative and semi-supervised data augmentation framework designed to overcome sparse labeled patient genomic data. 
- GANDALF leverages labeled samples from the cell line to augment patient data with critical information.
- By incorporating attention mechanisms and generating augmented samples, GANDALF significantly enhances classifier performance in predicting patient drug response.

### Weaknesses
 - The manuscript proposes a model with three distinct encoders, but the reasoning behind selecting this multi-encoder structure lacks clarity and strong justification. Specifically, the rationale for using a variational autoencoder (VAE) prior to the denoising diffusion probabilistic model (DDPM) is not well-established. The authors state, "to ease training, we reduce the dimensionality … using variational autoencoders (VAEs)," but it is unclear why a VAE is required rather than a simpler embedding without a decoder and what specific role the VAE’s decoder serves. While VAEs are known for capturing latent features and supporting generative tasks, considering that DDPM is an autoencoder-structured generative model, the need for a secondary, nested autoencoder is not well justified. This makes the model more complicated. The authors need to address the following points; 1. why a simpler embedding without a decoder is insufficient in this context; 2. what the specific function of the VAE's decoder plays in the model's architecture; 3. how the combination of VAEs and DDPM provides benefits that DDPM alone does not.

- How is the time step $t$ defined? Does it mean the time after treatment? This should be clarified in the problem formulation section. Additionally, how is $\beta_t$ set?

- How are the ground truth noise distributions $e_c, e_p$ defined, and how does the DDPM decoder remove domain-specific noise?

- In the results section, only five drugs are reported out of about 100 test drugs. The criteria for selecting these specific drugs should be clarified, especially given that all drugs were included in the ablation study.

- The study should assess the model’s ability to accurately label mutation-drug pairs when the drug in question is absent from the labeled training dataset (X_p, y_p, d_p). Were these five drugs excluded from the training and validation sets? If they were, a comparative analysis of model performance on drugs within and outside the training set would enhance the understanding of the model’s generalizability; if not, this experiment does not adequately validate the model’s intended benefits.

- There are typos in Equation (6), specifically where L_MSE is indicated as L_R and L_KLDV as L_KLD?

### Questions
- The manuscript introduces a model with three distinct encoders, yet the rationale behind this multi-encoder structure lacks clarity and a convincing explanation. For example, the authors state, "to ease training, we reduce the dimensionality … using variational autoencoders (VAEs),” but it is unclear why a VAE is required rather than a simpler embedding without a decoder and what specific role the VAE’s decoder serves. While VAEs are known for capturing latent features and supporting generative tasks, considering that DDPM is an autoencoder-structured generative model, the need for a secondary, nested autoencoder is not well justified. This makes the model more complicated. The authors are needed to address the following points; 1. why a simpler embedding without a decoder is insufficient in this context; 2. what the specific function of the VAE's decoder plays in the model's architecture; 3. how the combination of VAEs and DDPM provides benefits that DDPM alone does not.

- How is the time step $t$ defined? Does it mean the time after treatment? This should be clarified in the problem formulation section. Additionally, how is $\beta_t$ set?

- How are the ground truth noise distributions $e_c, e_p$ defined, and how does the DDPM decoder remove domain-specific noise?

- In the results section, only five drugs are reported out of about 100 test drugs. The criteria for selecting these specific drugs should be clarified, especially given that all drugs were included in the ablation study.

- The study should assess the model’s ability to accurately label mutation-drug pairs when the drug in question is absent from the labeled training dataset (X_p, y_p, d_p). Were these five drugs excluded from the training and validation sets? If they were, a comparative analysis of model performance on drugs within and outside the training set would enhance the understanding of the model’s generalizability; if not, this experiment does not adequately validate the model’s intended benefits.

- There are typos in Equation (6), specifically where L_MSE is indicated as L_R and L_KLDV as L_KLD?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Edit: Updated my score to 8 after the authors addressed my most major concerns

This paper proposes a method, GANDALF, for improving domain transfer for machine learning models, explicitly focusing on the cancer domain where we want to train chemo response models on cell line data, but apply them to patients. GANDALF works by creating artificial examples that are more similar to the target domain that can then be used for model training. The authors find that this data augmentation strategy significantly improves the performance of chemo response models on patients.

### Strengths
Strengths:
- Very well written paper, I really enjoy the step by step breakdown.
- Very strong empirical improvement over prior art
- Novel combination of techniques, incorporating a wide variety of tricks to improve performance
- Very significant topic, as domain adaptation is critical for many important problems where in-domain data is hard to obtain

### Weaknesses
Major:
- This paper is sorta a mix of two contributions, a very good “pseudo-labeler” MTL model and the data augmentation. However, it’s unclear which of those two contributions is important as it’s missing a simple, but important baseline: simply using the “pseudo-labeler” MTL model as a final classifier. It is insufficient to compare against DruID, as the architectures are quite different, making it difficult to isolate the impact of the data augmentation strategy. The paper needs an ablation study that evaluates the performance of the MTL model alone, without any data augmentation, to properly assess the contribution of the proposed augmentation method.

- I don't see any discussion of hyperparmeters for both models and baselines. How were they selected and how did you ensure that equal hyperparameter search time was dedicated to your model and baselines? It's not clear if the baselines were tuned on the same data, or if the authors used the hyperparameters from the original papers. This is especially important since the datasets used in this paper appear to be different from those used in the baseline papers, which could lead to unfair comparisons if the baselines are not properly tuned for the new data.

- It’s very hard to compare the ablation results in table 2 to table 1. Can you create an alternative table 2 that is side-by-side comparable with table 1?

Minor:
- There are some typos (for example the first row in table 2)
- I think some of the analysis in 3.4 is incorrect. For example, looking at only the top 2 principal components in high dimensional data to compare variance does not seem correct as you might be ignoring a ton of the signal. However, section 3.4 doesn’t matter for the central hypothesis of the paper so it’s not that important. I would actually just remove section 3.4

### Questions
Can you explain in more detail the differences between table 2 and 1 and why you chose a vastly different format between them?

How were standard deviations calculated?

### Soundness
4

### Presentation
4

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
Authors proposed GANDALF a method for data augmentation that takes labeled cell line and patients mutation data as input and makes drug response prediction via generating patient-driven samples in a 5 step process:
- pretraining diffusion models on cell lines and patients
- generating augmented samples 
- training a multitask predictor using labeled cell lines and patients 
- making predictions for augmented samples and selecting confident ones 
- training a final predictor on confident augmented samples and patients

GANDALF was compared with state-of-the-art of drug response prediction across 5 chemotherapy drugs in terms of AUROC and AUPR and was able to outperform the majority of them.

### Strengths
- The introduction of biological aspects was gentle and informative enough for those not familiar with the motivating application of the work. 
- While the separate components of GANDALF are not novel per se, components are linked together in a novel way for data augmentation - based on patient data for precision oncology. 
- The experimental results show improvements compared to baselines across multiple drugs

### Weaknesses
 - The input patient data is itself coming from 3 different resources i.e, P(Xp1) != P(Xp2)!=P(Xp3) similarly, the cell line data is also coming from two resources (input from CCLE, output from GDSC) but there is no indication of that in neither the assumptions nor the setup or the method. What makes GANDALF capable of handling shifts like that?

- Although authors have provided the source code, critical information is missing with respect to reproducibility of this work. For example, it is unclear if the reported numbers are from how many independent runs or hyper-parameters and the procedure for tuning them are not reported in the paper for any of the components e.g., DDPA, transformers, VAE, MTL, etc. 

- Citations of the utilized data are inaccurate and incomplete. For example, for CCLE and GDSC the seminal work like 
“Barretina et al., The Cancer Cell Line Encyclopedia enables predictive modelling of anticancer drug sensitivity 2012” or “Iorio et al. A Landscape of Pharmacogenomic Interactions in Cancer 2016” are not cited. Moreover, Although authors claimed that they’ve used GDSCv2, the citation is for 2012 which is more correlated with GDSCv1 timeline. Is this a citation error or GDSCv1 was used? 

- Authors used genomic data from CCLE and response data from GDSC, there is no justification for why the response profiles of these datasets are interchangeable. How many cell lines were in common between CCLE and GDSC, was the drug screening assay comparable between the two? this is important because GDSCv1 used Syto60 assay while CCLE and GDSCv2 used CellTiter-Glo (going back to the previous point on which GDSC was used).  

- There are parts of the paper that is challenging to follow for example, “We had a total of 156441 train, 17371 validation and 21589 test cell line, drug pairs. We also had 488/488/487 train, 53/54/56 validation and 115/114/113 test patient, drug pairs over the 3 folds.” Is unclear to me. Is this a reference to different patient data sources? 

- W/o MTL in ablation seems misleading as it only removes the cell line part but the proper way of doing this is to replace it with a drug specific single task model train on both cell lines and patients. 

- Another missing ablation is w/o diffusion what happens if you apply VAE directly to the input data?

- GANDALF learning curve is missing in Figure 7

### Questions
- There is no information regarding the applicability domain of GANDAL including what types of cancers was this method train/evaluated on? What was the performance per cancer type? similarly for cell lines, was the data from only solid tumours or both solid and non-solid tumours? 

- While somatic mutations can be predictive of drug response, other available data types such as RNA-Seq make more accurate predictions. To my knowledge, CCLE/GDSCv2 and TCGA/CbioPortal also have gene expression data, if the ultimate goal is to assist clinicians with choice of therapy why did you choose not to use other data types? 

- Why is GANDALF only applicable to chemotherapy drugs? Mutation data is also predictive of targeted therapeutics I can imagine it could be due to lack of labeled data for targeted drugs if so, isn’t this a huge disadvantage for the proposed method that requires labeled patient data as input? For targeted drugs like Erlotinib (Byers et al. An Epithelial-Mesenchymal Transition Gene Signature Predicts Resistance to EGFR and PI3K Inhibitors and Identifies Axl as a Therapeutic Target for Overcoming EGFR Inhibitor Resistance 2013) there are many labeled cell lines and smaller labeled patient data. Do you have any sense on the minimum required number of cell lines and patient samples for your method? I believe an experiment of percentage of labeled samples would be highly beneficial.  

- The reported performance for WISER and Code-AE in this work are substantially lower than those reported in the original papers for similar drugs and datasets. It seems WISER and Code-AE had a similar setup so what’s the difference between your setup and their’s? 

I'd be happy to revise my score if authors answer all questions/concerns thoroughly particularly:
- potential data issue
- applicability domain
- reproducibility 
- missing ablations

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The study shows an AI4Science application. It majorly focuses on using related cell line data and patients' clinical data to do drug and dosage response. The major contributions of this paper are: 1. proposing a composite framework (diffusion $+$ transformer) architecture to use cell line data to enrich limited patient clinical data. 2. the proposed framework also include a prediction module for the drug response prediction task and it beats SOTA models on the task.

### Strengths
- The study introduces a complete framework to do the DRP task. The framework uses a smart way to use the cell-line data to augment the patient data in order to improve model's performance on the target task.
- I like the idea that projects the patient embedding and cell-line data embedding data on the shared latent space and uses the cross attention strategy to keep the shared information. 
- The step 3 is also a smart move that addresss the limited drug issue in patients' clinical dataset.
- I can see from Table 1 that the proposed framework achieves general improvement on the datasets compared with baselines. 
- The authors provided comprehensive ablation studies. Table 2 demonstrates the importance of each component of the framework.

### Weaknesses
 - In figure 4, the aim is to show distribution similarity between generated patient data. But the PCA visualization is a linear projection method, and I cannot tell any difference between the distributions. Can you use some non-linear methods UMAP/t-SNE to show the distributions, and mark the labels using different colors? It would be better to see the distribution characteristics and differences.
- Why you put related works at last? It is hard for a reader not in this field to follow the work. It would be better put the section right after the introduction. And unsupervised models has been introduced well in the paper, can you elaborate a little bit more on the brief definitions or examples of inductive and transductive approaches in the context of drug response prediction, and how their method differs from yours.
- One key step is data augmentation. The author does provide the sample size for train/test/val in the appendix, but I didn't find the details about the sample size, i.e. how many psedo-patient data were added before training the final model. I think it is a key information for your experiments. And, I like your experiments in the appendix A.2, but the quantity there confused me. It would be better to provide the sample size directly rather than the thresholds.

### Questions
As I am not an expert in this application, I want to left the decision to the other reviewers and chairs that whether it deserves a highlight. But I think it is a very interesting application of diffusion models to this two modalities. 
Good work!

### Soundness
4

### Presentation
3

### Contribution
3
