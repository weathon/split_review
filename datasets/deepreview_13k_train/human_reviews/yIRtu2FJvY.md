# A Matrix Variational Auto-Encoder for Variant Effect Prediction in Pharmacogenes

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Variant effect predictors (VEPs) are designed to predict the impact of protein variants on cellular function, traditionally using data from multiple sequence alignments (MSAs). This assumes that natural variants are fit, a premise challenged by pharmacogenomics, where some pharmacogenes have low evolutionary pressure. In this context, deep mutational scanning (DMS) datasets are of particular interest since they provide quantitative fitness scores for variants. In this work, we propose a transformer-based matrix variational auto-encoder architecture and evaluate its performances on $33$ DMS datasets corresponding to $26$ drug target and absorption-distribution-metabolism-excretion (ADME) proteins available in the ProteinGym benchmark. Our model trained on MSAs (matVAE-MSA) outperforms a model similar to the widely used VEPs in pharmacogenomics, and sets a new zero-shot prediction benchmark for $2$ proteins related to the Noonan syndrome. We compare matVAE-MSA with matENC-DMS, a model with similar capacity, but trained on DMS data in a 5-fold supervised cross-validation framework. matENC-DMS outperforms matVAE-MSA for $15$ out of $33$ DMS datasets, including all ADME, and certain drug target proteins. Although our models do not outperform the best baseline models, our results help shed new light on the role of evolutionary pressure for the validity of the premise of VEP design. In turn motivating the development of DMS datasets to improve VEPs on pharmacogene-related proteins.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces two new methods for variant effect prediction: (1) matVAE-MSA which is a VAE trained on sequences from the protein family of interest and (2) matENC-DMS which is trained on DMS data from a specific protein. matVAE-MSA is similar to DeepSequence and EVE but the authors introduce architectural changes (i.e. self-attention layers) and experiment with more complex priors: mixture of diagonal Gaussians and VAMP. On pharmacogenes in ProteinGym, matVAE-ESM underperforms DeepSequence and ESM models. However, matENC-DMS, whose architecture is exactly the encoder portion of the DMS data and is trained on functional activity scores from a DMS assay, outperforms all other methods. Given that models trained on DMS data do significantly better than models solely trained on sequences from a MSA, the authors conclude that DMS data is valuable to train variant effect predictors on pharmacogenes.

### Strengths
- The authors explore novel architectural innovations to the DeepSequence/EVE family of models. In particular, they use self-attention layers where the attention map is determined from predicted contacts in AF2 structures. They also place more expressive priors on the latent space in matVAE-MSA. These are innovative ideas that have not yet been considered in the field. 

- The authors clearly benchmark their method to other state-of-the-art methods and clearly show the impact of their architectural modifications on model performance. This is one of the clearest papers I have read.

### Weaknesses
 - The primary weakness of this paper is that their VAE model does not outperform existing unsupervised variant effect predictors (like ESM or DeepSequence). They find that using a more complicated prior does not improve performance and that self-attention layers with attention maps defined using AF2 contacts does not help.
- The authors do go on to say that their encoder-only model trained on DMS data does outperform unsupervised variant effect predictors, but they do not compare to unsupervised variant effect predictors fine-tuned on DMS data. Their are many ways this fine-tuning has been proposed in the past and the authors should benchmark matENC-DMS to those methods: https://pubmed.ncbi.nlm.nih.gov/35039677/, https://www.nature.com/articles/s41467-024-51844-2, and https://arxiv.org/abs/2405.06729. 
- The authors should try pre-training a VAE on MSA data and then fine-tuning the encoder of the MSA on DMS data. 
- A central goal of the paper seems to be to identify the settings in which DMS data is useful for improving variant effect predictions. In Fig. A8, the authors are unable to find any correlations between metadata of the protein and performance difference between the DMS-trained and MSA-trained models. However, they don't consider structural features of the protein itself. Analysis along those lines would be interesting.

### Questions
- How much does performance change if attention maps in self-attention layers are learned as opposed to derived from AF2 predicted contacts?

- Based on my understanding of Fig. 1, the hyperparameter $d$ should be 20, corresponding to the number of amino acids. Why do you not embed amino acids in a higher dimensional space as you get deeper into the VAE?

- Instead of using a dimension-wise FC layer, do you think it would be valuable to have an attention pooling layer to reduce the number of parameters (# of parameters in attention pooling does not scale with the length of the sequence)? It also automatically allows you to handle sequences of different lengths.  

- For matENC-DMS, are variants at the same position either all in the training set or the testing set? Training on some varaints and testing on other variants at the same position has been shown to be a form of data leakage that inflates performance.

- Does difference in performance between matENC-DMS and matVAE-MSA depend on the number of variants assayed in the DMS? Could you include that In Fig. A8?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Here the authors propose a framework based on representation learning via VAEs for use on downstream deep mutational scanning tasks. The authors discuss their design choices and then proceed to benchmark their method against standard baseline methods for these tasks.

### Strengths
* **Novelty**: To the best of my knowledge, the authors' proposed framework is novel.
* **Impact**: The authors' motivation (i.e., assessing how well evolutionary pressure corresponds to fitness and the corresponding impact on variant effect prediction) is solid, and such studies would likely be of interest to the machine learning for proteins community.

### Weaknesses
Despite the potential impact of the authors' work, I believe that the authors' submission has significant issues that prevent me from recommending acceptance at this time. I provide details on the major issues below:

* **Unclear motivation for model design choices**: The authors spend a significant amount of time experimenting certain modeling/architecture choices (e.g. using a mixture of gaussians prior rather than a unimodal prior), which in the end don't have an impact on model performance. Indeed, this is listed as one of the authors' main contributions in the introduction. Could the authors comment on their rationale for exploring these modeling choices? Did previous results for this task find that more expressive priors led to improved performance? Or was there a more principled reason to assume that these specific priors would lead to better performance? Without more context it's hard for the reader to understand why these results are being presented. On a related note, it would be great to see an ablation study assessing the impact of training a predictor on DMS datasets using representations from previous methods (e.g. DeepSequence) compared to the same task with the authors' proposed architecture. Without this information, it's difficult for the reader to understand whether any boosts in performance for the models trained on DMS data can be attributed to the authors' proposed encoder network or if the results are solely due to training on DMS data.
* **Unclear significance of experimental results**: Perhaps most importantly, it's not clear to me that any meaningful conclusions can be drawn from the experimental results (e.g. those presented in Table 3). In particular, given the large error bars it's difficult for the reader to assess if the provided results are statistically significant. Could the authors provide results from e.g. a t test? Moreover, it's not clear to me how the authors selected their final model hyperparameters (e.g. learning rates). The authors mentioned that their choices "preserv[ed] stability and convergence", but without more details it's hard to tell if these values were cherry-picked. Were these parameters e.g. chosen via cross-validation/performance on a held-out validation set? Given these issues, it's thus unclear whether the authors' claims are supported by their experimental results.
* **Not self-contained/writing issues**: Given that ICLR is a general machine learning conference (as opposed to a more biology-focused venue), it would greatly improve the manuscript for the authors to spend more time in the introduction describing the problem setup and significance. Indeed, the introduction section to the manuscript feels extremely rushed, with little time spent on introducing the problem setting tackled by the authors. For example, providing a gentler introduction to domain-specific terms like deep mutational scanning, On the other hand, a significant amount of space is spent describing hyperparameters (e.g. sections 3.1/3.2) or details of individual datasets (e.g. section 2.3 + Table 1), which could be relegated to the Appendix. I would thus recommend that the authors restructure the manuscript so that the main text is self-contained for a general ICLR reader, with ancillary experimental details moved to the appendix to make space as needed. On a related note that could save some space, it's unclear to me why the authors spend a significant amount of time introducing certain mathematical/machine learning concepts which are subsequently not used in the method (e.g. introducing matrix decomposition before stating that transformer layers are used).

### Questions
See "Weaknesses"

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an encoder-decoder language model similar to DeepSequence for the task of mutation effect prediction and tests it on 33 drug-related DMS datasets from ProteinGym.

### Strengths
- A clear presentation on the new transformer-based module for the encoder and decoder.
- A comprehensive investigation and analysis on the impact of different designed modules to the prediction task.

### Weaknesses
 - The presentation of the motivation is unclear (Q1, 3).
- The justification for the experimental design and significance of the results is not clearly articulated (Q2, 3, 4, 6).
- The design of the prediction tasks appears to be questionable (Q3, 5, 8).
- The comparison with baseline methods is incomplete (Q7).

### Questions
1. If pharmacogenes experience low evolutionary pressure, why is MSA included? (line 18)
2. What is the significance of the statement "sets a new benchmark for 2 out of 26 proteins"? (lines 21-22)
3. Regarding the "5-fold cross-validation framework," what is the rationale for training a model to fit a DMS dataset rather than conducting zero-shot predictions? For a new protein, if a DMS dataset is already available, it is likely that users have already identified favorable mutants.
4. Are there any differences between the MSA sequences used and those provided by the ProteinGym benchmarks? If so, why not utilize ProteinGym's versions?
5. Why is there a manual selection of a threshold to binarize the DMS target scores? What are the specific criteria for this selection and what are the resulting values?
6. Could you clarify the statement "For instance ESM2 (150M), ESM2 (15B) and ESM-1v (ensemble) are all flavors of ESM"?
7. How should we interpret the statement "We compared with those models in ProteinGym which perform the best on at least one pharmacogene-related protein DMS dataset according to SpearmanR"? Does "perform the best" refer to zero-shot prediction or supervised learning tasks? What are the candidate models and their respective scores? Have all models on the ProteinGym leaderboard been considered in this comparison?
8. While the algorithm does not apply any specific designs to pharmacogene, it seems like a general framework that can be applied to any mutation effect prediction tasks. In this case, it is suggested to test the model on the complete ProteinGym benchmarks of all 217 assays.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper first proposes an unsupervised variant effect predictor (VEP), matVAE-MSA. The model is a VAE with transformer layers for the encoder and decoder with a sparse attention mask derived from the WT AlphaFold-predicted structure. Additionally the authors propose a supervised model, matENC-DMS which uses the same encoding architecture as matVAE-MSA, but maps the encoded vector to a scalar to predict the fitness label. matVAE-MSA does not consistently outperform existing unsupervised approaches, but does provide the best results for two proteins, MK01 and RAF1. matENC-DMS, which is trained on family-specific DMS data, consistently improves performance over unsupervised approaches.

### Strengths
The experimental results are cleanly laid out and the authors do a nice job of not over-selling their results.

### Weaknesses
Unfortunately I see a number of weaknesses with the current paper. First, the use of a transformer as a VAE for modeling protein families is not new and exists in ProT-VAE. Nonetheless, given that this new architecture does not outperform existing simple VAE architectures it is not clear what contribution this paper is making with this? While the matENC-DMS results are interesting, there is no benchmarking with other supervised approaches. In particular, the paper "Learning protein fitness models from evolutionary and assay-labeled data" addresses combining evolutionary data with DMS data. At a minimum the authors should compare to this approach. Overall, I wasn't able to see what contributions the authors are making. The new VAE model doesn't seem to add any new insights into how to design better unsupervised generative models and it does not outperform existing approaches. The supervised model is not benchmarked against any similar approaches and does not provide any new insights.

### Questions
Can the authors more clearly explain what they feel are the contributions of the paper?

### Soundness
3

### Presentation
2

### Contribution
1
