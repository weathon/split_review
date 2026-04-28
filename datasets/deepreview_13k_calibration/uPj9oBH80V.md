# SELFIES-TED : A Robust Transformer Model for Molecular Representation using SELFIES

- Decision: Reject
- Avg Score: 3.50
- Scores: 6, 1, 6, 1

## Abstract
Large-scale molecular representation methods have revolutionized applications in material science, such as drug discovery, chemical modeling, and material design. With the rise of transformers, models now learn representations directly from molecular structures. In this paper, we introduce SELFIES-TED, a transformer-based model designed for molecular representation using SELFIES, a more robust, unambiguous method for encoding molecules compared to traditional SMILES strings. By leveraging the robustness of SELFIES and the power of the transformer encoder-decoder architecture, SELFIES-TED effectively captures the intricate relationships between molecular structures and their properties. Having pretrained with 1 billion molecule samples, our model demonstrates improved performance on molecular property prediction tasks across various benchmarks, showcasing its generalizability and robustness. 
Additionally, we explore the latent space of SELFIES-TED, revealing valuable insights that enhance its capabilities in both molecule property prediction and molecule generation tasks, opening new avenues for innovation in molecular design.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
SELFIES-TED, a transformer-based model for molecular representation, property prediction and generation that utilizes SELFIES, was proposed in the paper. The model uses a robust and unambiguous molecular string representation, compared to traditional SMILES. An encoder-decoder architecture inspired by BART was introduced and can capture complex molecular relationships and features. The MVR approach further enhances the quality of the learned representations. The model was evaluated on both molecular property prediction and generation tasks. The results are compared with several state-of-the-art works. SELFIES-TED is more accurate and the generated molecules have better validity and novelty.

### Strengths
1. The proposed SELFIES-TED ensures the syntactic and semantic validity representation of molecules, This significantly reduces the chances of learning invalid molecular representations and makes the model more robust compared to those relying solely on SMILES.
2. Inspired by BART, the Encoder-Decoder transformer models are valuable for generating molecules. The MVR approach also expands the latent representation and generates multiple SELFIES strings, which significantly improve the quality of proposed models.
2. The model was compared with several graph-based, geometry-based, and text-based models. It achieves state-of-the-art results in many tasks, showing its potential to advance molecular representation learning. Specifically, the proposed model outperforms related works on several molecular property prediction and generation tasks.
3. The validity, uniqueness, and novelty of the proposed molecules are significantly better than previous works. The distribution of generated molecules is also similar to reference molecules.

### Weaknesses
1. In Figure 3, there are only 10 different molecules. Some latent representations of the green mols are surrounded by red molecules. Will this limit the model if there are a lot of molecules in the dataset? And, how about if the dataset is very small but the molecules are very similar?
2. Could you please highlight the difference between Ref Mol and Gen Mol in Figure 7? The molecules have very similar 2D graphs. 
3. The platform that trains and evaluates the models is not introduced. The overhead and limitation of SELFIES-TED are not well explained.

### Questions
1. In Figure 5, why the density of logp is not as the others? Does this mean that the model not doing well for logP?
2. How many representations are needed in MVR? Does it mean that the model is n times slower if n representations are generated?
3. Why do you use the greedy selection method in the MVR? Will this lead to overfitting?
4. Do the canonical SMILES have some privilege so that they are more likely to be selected?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper trains an encoder decoder transformer on SELFIES string representations of small molcules on large unfiltered datasets. For evaluation it evaluates prediction and generation tasks. It trains predictors on top of the latent representations and checks their predictions in various benchmarks. It generates molecules unconditionally and evaluates their distributional properties.

### Strengths
1. Interesting histograms of generated and reference molecule's synthetic acessibility and QED scores.
2. Reasonable experiments on moleculenet property predictions

### Weaknesses
1. Missing information: It is not sufficiently explained how the transformer is trained. Is there always only 15% of the sequence masked? Is X_{corrupt} a 15% masked SELFIE or is Y_{<t} the 15% masked SELFIE? If X_corrupt is the 15% masked selfie and Y_{<t} experiences all masking ratios but autoregressively from left to right, then why would the loss not be minimized by just copying over the information from X_{corrupt}? The explanation of the denoising objective remains unclear, specifically regarding the masking procedure and the roles of X_corrupt and Y_{<t}. The paper does not clarify whether the masking is applied to the input sequence X_{corrupt} only, or if the target sequence Y_{<t} is also masked during the autoregressive decoding process. This ambiguity makes it difficult to understand how the model learns to generate new sequences rather than simply reconstructing the masked input. The potential for the model to learn a trivial copy mechanism is a significant concern that needs to be addressed with a more precise description of the training process.
2. Missing information: How do you compute novelty? What is the reference set and what is the similarity measure. The paper lacks a clear definition of the novelty metric. It is not specified how the reference set is constructed, nor what similarity measure is used to determine if a generated molecule is novel. Without these details, the reported novelty scores are not interpretable. A typical novelty score would be reporting the maximum tanimoto similarity where 1 is the worst possible score. In the provided table the score for novelty for SMILES-TED is 1. 
3. The fact that multiple smiles describe the same molecule is a bug not a feature. You introduce Multi View representation as a workaround, but this would not be necessary if one simply employs a representation learning model that encodes molecules instead of ambiguous representations of molecules such as SMILES or SELFIES. (Even when using selfies/Smiles, could one not use a canonicalized smiles/selfie version instead of the ambiguous one? I know this exists for SMILES and would guess that it is also possible to construct for SELFIES.) The use of multiple SMILES or SELFIES strings to represent a single molecule is presented as a feature, but it introduces unnecessary complexity. The core issue is that SMILES and SELFIES are not unique representations of molecular structures. Canonicalization of these strings would remove the need for a multi-view approach. The paper does not justify why a canonicalized representation is not used, which would simplify the model and remove the ambiguity inherent in using multiple string representations for the same molecule.



### Questions
1. How do you compute novelty?
2. What is the magnitude of the noise that is added to the embeddings for Table 6 and Figure 5 compared to the magnitude of the noise added for figure 7.
3. How do you obtain the fixed size single vector for every SELFIE when making TSNE plots - do you sum the latent representations of every token?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work introduces SELFIES-TED, a transformer-based encoder-decoder model that uses SELFIES to learn molecular representations. The model according to authors achives very high competitive performance on various benchmarks. The authors also propose a Multi-View Representation approach that leverages multiple representations of the same molecule to improve prediction accuracy. Authors have repurposed the BART model and trained it using PubChem+Zinc 22. In order to improve the prediction accuracy the authors used a method to create multiple SMILES representations for a given molecule and then generate the SELFIES from those generated strings and used it in MVR.

### Strengths
The authors introduce a Multi-View Representation (MVR) approach, which could potentially help one improve training when there are unbalanced data points, especially in chemistry. The bidirectional approach to molecular representation learning differs from traditional encoder-only models. The model looks promising when we look into the benchmark results and also shows promising results on property prediction and molecule generation. The paper looks well-written and formulated the figures are clear. Methods and architecture are well-explained. The paper also provides insights into the latent space organization of molecular features. Also, it is great to see such work is completely open-sourced. which is highly commendable.

### Weaknesses
Overall, the majority of my concerns are not addressed. What is primarily lacking is a discussion and explanation of how results are obtained and their significance. A deeper discussion of how the model was trained, how the data was curated, and why the architecture is the way it is is crucial to understanding any scientific significance beyond better benchmark scores. From reading this paper, it is impossible to tell what led to the improvement and how to replicate or build off that.

- Where are the hyperparameter tuning details? Only single values are provided.
- The provided model ablations are not meaningful and quite confusing. The small model is given 8x more data but only 2 layers? There should be at least somewhat of a scaling analysis that leads to the 358M especially due to the size increase compared to prior models. The 2-layer model seems unrealistic as all prior methods, even non-LLM models, have more than 2 layers. Also, data is not kept the same, which voids a direct comparison.
    - The small model is a 2.2M parameter model with 2 encoder-decoder layers and 4 attention heads, pretrained with 8B samples 
    - The large model is a 358M parameter model with 12 encoder-decoder layers and 16 attention heads, pretrained with 1B samples.
- Where is the discussion of how the Morgan Fingerprint results were obtained?
- If MVR is being proposed as a general framework, there needs to be evidence to substantiate that claim. Currently, there is none, and still, the paper is lacking any and all critical ablations.

Overall, the paper is still majorly unfinished. It lacks explanations of the method and experiments. It has uninformative experiments and lacks technical novelties as many prior works that were initially missed and now added are not properly ablated. 

I maintain my stance on strong rejection. I recommend that the authors do a proper ablation study and take the time to write a self-sustaining paper upon resubmission.

### Questions
Are there any limitations in the generated length of the SELFIES string?
Figure 6 should have the training dataset chemical space and be compared it with the generated molecules' chemical space. 
The MVR idea is interesting but I have a question for the authors did they try to parse the input data always through RDKit create canonical SMILES and then generate and train the model how well does the model compare to the original?
The authors should reduce the use of unnecessary words such as "state of the art", "enhancing the reliability", "enriched" and so forth, which can be seen throughout the paper.
The authors should also discuss the limitations of using this model.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
SELFIES-TED introduces a transformer trained on SELFIES strings for improved molecule property prediction. SELFIES-TED uses a BART backbone to learn a molecule representation while also being able to generate novel molecules. SELFIES-TED has 354M parameters and was trained on 1 billion molecules from zinc-22, applying smiles enumeration. The authors also introduce a multi-view representation where multiple valid selfie representations are aggregated for one improved latent vector.

### Strengths
Overall, the paper is short and succinct. The multi-view representation is an interesting approach to leveraging existing data and representations to improve property prediction results. The results show the model can improve property prediction for certain tasks.

### Weaknesses
The paper is quite sparse in its details. Outside of the model name, archetype, and size, no details are given for the model training and benchmarking, making it quite difficult to understand the scientific contributions. Optimal hyperparameters are referred to but not shared. I think there is a strong possibility for this to be a meaningful work, but a significant addition of information and experiments is needed to understand the contribution. 

There is little novelty in taking the same training data as prior methods and swapping out the transformer backbone to train a larger model, especially when the BART architecture has been explored with selfies before [1] and was not cited. 

The Multi-view representation is interesting but not specific to SELFIES or SELFIES-TED and should be properly ablated by comparing it against prior property prediction methods. To understand the comparison of SELFIES vs. SMILES and BERT vs. BART, it would be important to have training ablations, even if on a smaller scale.

There are also several claims on the improvements SELFIES yield over SMILES but no experiments are given to substantiate those claims. There have been several works exploring these claims, including [2], which argue that invalid SMILES are enriched among low-likelihood samples from chemical language models. No discussion on this area of work is provided when central to the primary contribution.

- Given the paper is focused on introducing SELFIES-TED as a novel model the training and inference details as well as ablations are necessary as can be seen in section 4 of SELFformer of a similar method. 
- Molformer -XL is at 47M params, SELFformer 87M, and UniMol 47M, yet only one size of SELFIES-TED is reported at 354M. Given the difference between SELFformer and SELFIES-TED is RoBERTa vs. BART, significant ablations are necessary to understand the resulting benefit, and it is worth a 4x increase in model size at a minimum. 
- Prior methods have also explored BART for SMILES and SELFIES and explored the issue with a variable length representation and are not cited nor compared against [3, 1]. 
- No training information is given about any hyperparameters for the LLM or the classifier and regression models trained for the benchmarks.
- The molecule generation benchmarks are quite sparse, with all baselines taken from MolGPT, which was published three years ago. Large SELFIES-based models like SAFE-GPT [4] also include several other prior SELFIES-based models for molecule generation.




[1] https://arxiv.org/pdf/2301.11259

[2] Invalid SMILES are beneficial rather than detrimental to chemical language models https://www.nature.com/articles/s42256-024-00821-x

[3] https://arxiv.org/pdf/2208.09016

[4] https://arxiv.org/abs/2310.10773

### Questions
- How was SELFIES-TED trained?
- How does the classification performance depend on the model size?
- What happens if you apply the multiview representation to similar SELFIES and SMILES models that also rely on enumeration for training?
- Given that BART uses a variable-length encoding scheme like all prior BERT and BART-based architectures, how is the input to the XGBOOST classifier obtained when a latent vector of size 1024 is produced for each token, is it a average over the sequence length?
  - Are the prior methods compared against using the same latent vector size? 
- How does SELFIES-TED compare to Morgan Fingerprints? 
- What would happen if the multi-view representation were used with ML and classical methods?

### Soundness
1

### Presentation
2

### Contribution
1
