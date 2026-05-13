# Generative modeling for RNA splicing code predictions and design

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Alternative splicing (AS) of pre-mRNA splicing is a highly regulated process with diverse phenotypic effects ranging from changes in AS across tissues to numerous diseases. The ability to predict or manipulate AS has therefore been a long time goal in the RNA field with applications ranging from identifying novel regulatory mechanisms to designing therapeutic targets. Here we take advantage of generative model architectures to address both the prediction and design of RNA splicing condition-specific outcome. First, we construct a predictive model, TrASPr, which combines multiple transformers along with side information to predict splicing in a tissue specific manner. Then, we exploit TrASPr as on Oracle to produce labeled data for a Bayesian Optimization (BO) algorithm with a costume loss function for RNA splicing outcome design. We demonstrate TrASPr significantly outperforms recently published models and that it can identify relevant regulatory features which are also captured by the BO generative process.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors proposes a transformer-based network to predict condition specific splicing event (in terms of psi). The inputs of the network are the RNA sequences near the splicing site, meta data such as sample type (tissue), exon length, intron length, etc. The labels are the psi values quantified using another method called MAJIQ. 

The goal of this manuscript is to learn the underlying regulatory mechanisms of splicing using the proposed network such that it could be used as an oracle to predict the splicing based on the sequence information and meta-data. Based on this powerful prediction capability, the authors proposes additional networks to design new RNA sequences to make them splice as expected.

In general, I think the goal is very ambitious. Unfortunately, I am not convinced by the manuscript that the goal is achieved. First, I am not sure what meta data information could be utilised to predict condition-specific splicing, assuming the input RNA sequences are from the same species thus are very similar. I feel it will be useful to give a concrete example to motivate the proposal. Second, I think it will be nice to expand the prediction part with more experiments to validate the basic assumptions. For example, if we replace the input sequences with random sequences or sequences from non-splicing genes, but with the same meta-data, we expect to see that psi is close to 0. Assuming the network has successfully captured the regulatory mechanism, we expect to see the psi will decrease to 0 if we remove the U2 elements (suppl. Fig. 7d) from the input sequences. Since the splicing mechanism is conservative between human and mouse, we expect to see that NN trained on human data should exhibit similar predictive power on mouse homolog genes. If the prediction part works with high precision, then it worth designing novel RNA sequences. It will be really helpful for me to read the ms if the authors could highlight the main ideas and assumptions and hiding unnecessary details.

Minor points:
1. Sec 3.1.1 Fig. 1b => Fig. 1a, second paragraph, "mask the surrounding k tokens", k=?
2. Sec 3.1.2 Fig. 1c => Fig. 1b
3. Explain why you want to center the sequences
4. Right on top of sec. 4, "The Levenshtein constraint is evaluated on ....", why lev(z, z') = lev(\gamma(z), \gamma(z')) hold?

### Strengths
The authors proposes a transformer-based network to predict condition specific splicing event (in terms of psi). The inputs of the network are the RNA sequences near the splicing site, meta data such as sample type (tissue), exon length, intron length, etc. The labels are the psi values quantified using another method called MAJIQ. 

The goal of this manuscript is to learn the underlying regulatory mechanisms of splicing using the proposed network such that it could be used as an oracle to predict the splicing based on the sequence information and meta-data. Based on this powerful prediction capability, the authors proposes additional networks to design new RNA sequences to make them splice as expected.

In general, I think the goal is very ambitious. Unfortunately, I am not convinced by the manuscript that the goal is achieved. First, I am not sure what meta data information could be utilised to predict condition-specific splicing, assuming the input RNA sequences are from the same species thus are very similar. I feel it will be useful to give a concrete example to motivate the proposal. Second, I think it will be nice to expand the prediction part with more experiments to validate the basic assumptions. For example, if we replace the input sequences with random sequences or sequences from non-splicing genes, but with the same meta-data, we expect to see that psi is close to 0. Assuming the network has successfully captured the regulatory mechanism, we expect to see the psi will decrease to 0 if we remove the U2 elements (suppl. Fig. 7d) from the input sequences. Since the splicing mechanism is conservative between human and mouse, we expect to see that NN trained on human data should exhibit similar predictive power on mouse homolog genes. If the prediction part works with high precision, then it worth designing novel RNA sequences. It will be really helpful for me to read the ms if the authors could highlight the main ideas and assumptions and hiding unnecessary details.

Minor points:
1. Sec 3.1.1 Fig. 1b => Fig. 1a, second paragraph, "mask the surrounding k tokens", k=?
2. Sec 3.1.2 Fig. 1c => Fig. 1b
3. Explain why you want to center the sequences
4. Right on top of sec. 4, "The Levenshtein constraint is evaluated on ....", why lev(z, z') = lev(\gamma(z), \gamma(z')) hold?

### Weaknesses
 The authors proposes a transformer-based network to predict condition specific splicing event (in terms of psi). The inputs of the network are the RNA sequences near the splicing site, meta data such as sample type (tissue), exon length, intron length, etc. The labels are the psi values quantified using another method called MAJIQ.

The goal of this manuscript is to learn the underlying regulatory mechanisms of splicing using the proposed network such that it could be used as an oracle to predict the splicing based on the sequence information and meta-data. Based on this powerful prediction capability, the authors proposes additional networks to design new RNA sequences to make them splice as expected.

In general, I think the goal is very ambitious. Unfortunately, I am not convinced by the manuscript that the goal is achieved. First, I am not sure what meta data information could be utilised to predict condition-specific splicing, assuming the input RNA sequences are from the same species thus are very similar. I feel it will be useful to give a concrete example to motivate the proposal. Specifically, what is the expected change in psi given different tissues for the same RNA sequence?  The authors should provide a clear example of how tissue-specific factors interact with the RNA sequence to alter splicing patterns. Second, I think it will be nice to expand the prediction part with more experiments to validate the basic assumptions. For example, if we replace the input sequences with random sequences or sequences from non-splicing genes, but with the same meta-data, we expect to see that psi is close to 0. Assuming the network has successfully captured the regulatory mechanism, we expect to see the psi will decrease to 0 if we remove the U2 elements (suppl. Fig. 7d) from the input sequences. Since the splicing mechanism is conservative between human and mouse, we expect to see that NN trained on human data should exhibit similar predictive power on mouse homolog genes. It is unclear if the model is learning generalizable splicing rules or simply memorizing training data. If the prediction part works with high precision, then it worth designing novel RNA sequences. It will be really helpful for me to read the ms if the authors could highlight the main ideas and assumptions and hiding unnecessary details.

Minor points:
1. Sec 3.1.1 Fig. 1b => Fig. 1a, second paragraph, "mask the surrounding k tokens", k=?
2. Sec 3.1.2 Fig. 1c => Fig. 1b
3. Explain why you want to center the sequences
4. Right on top of sec. 4, "The Levenshtein constraint is evaluated on ....", why lev(z, z') = lev(\gamma(z), \gamma(z')) hold?

### Questions
The authors proposes a transformer-based network to predict condition specific splicing event (in terms of psi). The inputs of the network are the RNA sequences near the splicing site, meta data such as sample type (tissue), exon length, intron length, etc. The labels are the psi values quantified using another method called MAJIQ. 

The goal of this manuscript is to learn the underlying regulatory mechanisms of splicing using the proposed network such that it could be used as an oracle to predict the splicing based on the sequence information and meta-data. Based on this powerful prediction capability, the authors proposes additional networks to design new RNA sequences to make them splice as expected.

In general, I think the goal is very ambitious. Unfortunately, I am not convinced by the manuscript that the goal is achieved. First, I am not sure what meta data information could be utilised to predict condition-specific splicing, assuming the input RNA sequences are from the same species thus are very similar. I feel it will be useful to give a concrete example to motivate the proposal. Second, I think it will be nice to expand the prediction part with more experiments to validate the basic assumptions. For example, if we replace the input sequences with random sequences or sequences from non-splicing genes, but with the same meta-data, we expect to see that psi is close to 0. Assuming the network has successfully captured the regulatory mechanism, we expect to see the psi will decrease to 0 if we remove the U2 elements (suppl. Fig. 7d) from the input sequences. Since the splicing mechanism is conservative between human and mouse, we expect to see that NN trained on human data should exhibit similar predictive power on mouse homolog genes. If the prediction part works with high precision, then it worth designing novel RNA sequences. It will be really helpful for me to read the ms if the authors could highlight the main ideas and assumptions and hiding unnecessary details.

Minor points:
1. Sec 3.1.1 Fig. 1b => Fig. 1a, second paragraph, "mask the surrounding k tokens", k=?
2. Sec 3.1.2 Fig. 1c => Fig. 1b
3. Explain why you want to center the sequences
4. Right on top of sec. 4, "The Levenshtein constraint is evaluated on ....", why lev(z, z') = lev(\gamma(z), \gamma(z')) hold?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes Bayesian optimization approach for designing sequence edits that modify RNA splicing in a desired way. It also proposes a transformer-based model for predicting splicing, which then serves as a surrogate source of truth for the Bayesian optimization method.

### Strengths
The main strength of the paper lies with the novel task of sequence editing aimed at altering the splicing outcome.

The proposed technical pipeline is inspired by recent work on Bayesian optimization over structured/discrete domains (cited refs. Maus et al. NeurIPS’22, Stanton et al. ICML’22) and is relatively novel: it combines top-performing current approach for predictive tasks on sequences (Transformers) with latent space Bayesian optimization (LSBO) approach for sequence design. 

Experimental results for splicing prediction show that the predictive part of the approach improves upon existing methods. Assessment of the sequence design part resulted in sequences that make biological sense.

### Weaknesses
The literature review concerning splice site prediction is phrased in a confusing way. On pg 2, when discussing DNABERT, SpliceAI, etc. authors mention sequence length limit (e.g. 10kbp for SpliceAI) as a key challenge these method face, and yet the method proposed in the paper uses short window, 400bp for each of the four Transformers. This discrepancy is not adequately justified, especially given that longer-range interactions can be crucial for splicing regulation. The review also omits recent, relevant tools such as SpliceBERT, which directly addresses some of the limitations mentioned. This omission undermines the claim of the proposed method being state-of-the-art. 

The description of the “condition-specific” nature of the method is somewhat vague, and should be described/discussed in Introduction and in the relevant Methods section in more detail. For example, it seems (pg. 3, bottom paragraph) that the method does not take condition information (RBP knockdown) on input directly, but “simulates it” via sequence modification. This approach, while potentially useful for motif analysis, is not clearly distinguished from methods that directly model RBP binding or activity. On the other hand, “condition” relating to tissue specificity seems to be used as input to the model as part of the Event features; rationale for this approach and its impact on usage of the method e.g. for splicing-altering diseases should be discussed. The lack of clarity regarding how different types of “conditions” are handled makes it difficult to assess the method's general applicability and limitations.

### Questions
See weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a model for condition-specific alternative splicing quantification, improving on existing work for this task.  They also demonstrate the utility of the model for a synthetic biology problem of modifying a genomic sequence to modify the splicing pattern in a desired way.

### Strengths
- Prediction of condition-specific alternative splicing is an important biological problem, and the proposed model performs MUCH better than the recently published Pangolin model.

- The application of the model to the problem of modifying splicing patterns in a desired way is highly novel and interesting.  While deep learning models have been used for sequence design, the particular application is new.

- An ablation study demonstrates the value of the major aspects of the architecture, and contains interesting insight on the utility of DNABERT vs an RNA counterpart trained by the authors.

- Validation of model prediction using knockdown data.

### Weaknesses
 - The ability to assess the validity of the mutated sequences is rather limited.  The authors were able to show that alternative methods for exploring sequence space to find mutated sequences are less effective at that.

- Although overall the manuscript is clear and easy to read, it contains many typos and grammatical errors - see below.

- When it comes to in-silico mutations, I am not sure the authors' experiment shows all that much.  A better approach might be to see how well the model predicts splicing QTLs as was done in the Pangolin paper (and using integrated gradients works better than mutagenesis in our experience).


Minor comments:

"For all of those target variables we use the cross-entropy loss function which performed better than regression"
Do you mean better than a regression loss function?  

"This result might be because of condition specific regulation, because the relevant sequence context is outside the 10kb fixed window used by Pangolin, or because other splicing signals in that window ‘confused’ the model with respect to quantifying the inclusion of the cassette exon. "
While the first reason seems plausible, the second is very generic and would apply to any model.

In section 4.3 it would be more friendly to the reader to spell out the first occurrence of KD since it's not a standard acronym.


typos/grammar:

curated regulatory featured --> features

constraint optimization problem --> constrained

6-mers tokens --> 6-mer tokens

and the prediction results where then averaged --> were

predictions of RBPs effects where --> RBP effects were

Daam1 gene where tested --> were tested

The foundation model for TrASPr is a 6 layer BERT model which is pretrained on human RNA splice sites (Fig. 1b).  --> 1a

The structure of TrASPr is depicted in Fig 1c. --> 1b

please improve the following sentence:
assess its ability to predict the effect of changes in trans (RBP KD) or cis (mutations in a mini-gene reporter assay) using in-silico

Figure 2 caption:
lable --> label

Pangolin model is unable --> The Pangolin model is unable

work well on most of low PSI cases --> work well on most low PSI cases.

advantage of transformers models --> transformer

 in extracting such information for the the splicing prediction task.

results on Daam1 gene --> results on the Daam1 gene

but made sure non of these randomly chosen regions hit --> none

### Questions
- When it comes to in-silico mutations, I am not sure the authors' experiment shows all that much.  A better approach might be to see how well the model predicts splicing QTLs as was done in the Pangolin paper (and using integrated gradients works better than mutagenesis in our experience).


Minor comments:

"For all of those target variables we use the cross-entropy loss function which performed better than regression"
Do you mean better than a regression loss function?  

"This result might be because of condition specific regulation, because the relevant sequence context is outside the 10kb fixed window used by Pangolin, or because other splicing signals in that window ‘confused’ the model with respect to quantifying the inclusion of the cassette exon. "
While the first reason seems plausible, the second is very generic and would apply to any model.

In section 4.3 it would be more friendly to the reader to spell out the first occurrence of KD since it's not a standard acronym.


typos/grammar:

curated regulatory featured --> features

constraint optimization problem --> constrained

6-mers tokens --> 6-mer tokens

and the prediction results where then averaged --> were

predictions of RBPs effects where --> RBP effects were

Daam1 gene where tested --> were tested

The foundation model for TrASPr is a 6 layer BERT model which is pretrained on human RNA splice sites (Fig. 1b).  --> 1a

The structure of TrASPr is depicted in Fig 1c. --> 1b

please improve the following sentence:
assess its ability to predict the effect of changes in trans (RBP KD) or cis (mutations in a mini-gene reporter assay) using in-silico

Figure 2 caption:
lable --> label

Pangolin model is unable --> The Pangolin model is unable

work well on most of low PSI cases --> work well on most low PSI cases.

advantage of transformers models --> transformer

 in extracting such information for the the splicing prediction task.

results on Daam1 gene --> results on the Daam1 gene

but made sure non of these randomly chosen regions hit --> none

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
Modeling alternative splicing (AS) and predicting the implications of _cis_-acting factors (e.g., proximal mutations) and _trans_-acting factors (e.g., RNA binding proteins; RBPs) have been studied for almost two decades. The splicing machinery and process are complicated and error-prone, which is why a significant fraction of diseases involve aberrant splicing. In this manuscript, the authors propose two major directions: using transformers for modeling alternative splicing (referred to as Traspr) and utilizing this model as an oracle to propose a Bayesian optimization (BO) method for designing sequences that achieve a desired alternative splicing level. They employ mutation and RBP knockdown data to demonstrate that their transformer-based model has learned the regulatory code of splicing. Finally, they illustrate, by example, how their Bayesian optimization method can alter alternative splicing levels.

### Strengths
While alternative splicing modeling has been extensively studied, systematic methods for designing/altering sequences are relatively new, and the authors' Bayesian optimization method appears promising.  RBP knockdown analysis is also interesting. The authors have also undertaken a significant amount of data processing and batch correction to facilitate model training and validation.

### Weaknesses
This manuscript attempts to address two major problems but, unfortunately, does not succeed in either case. Here are the main issues:

1. The authors focus on differential splicing and use splicing profiles across multiple tissues and species to train their model. However, they do not present any immediate benefits. For instance, they do not provide information on how much SpliceAI (Jaganathan et al., 2019) loses in performance, or how much Traspr gains, by having a universal (tissue-agnostic) model for splicing. In Section 4.1, the authors themselves acknowledge that "[...] predictions for tissue-specific splicing changes were not very accurate, and we, therefore, did not include them here."

2. The manuscript lacks convincing performance comparisons. It is challenging to believe that Traspr outperforms Pangolin (and subsequently SpliceAI) by such a significant margin (Spearman correlation 0.81 vs. 0.17). SpliceAI and other methods have undergone extensive testing by independent researchers. Furthermore, the approach for calculating cassette exon inclusion in Pangolin, as described in the manuscript, may not be optimal, as it ignores the upstream and downstream exon junctions. A more appropriate method can be found in the Methods section of the SpliceAI paper.

3. Traspr appears to excel at predicting constitutive and non-constitutive exons but performs poorly for exons that fall in between (the truly alternatively spliced exons). It might provide more insight if the tested exons were categorized accordingly (e.g., see Fig. 1C in the SpliceAI paper).

4. The manuscript lacks a comparison with the AE+MLP model, which is trained only on mouse data and is not considered state of the art.

5. The authors only examine Daam1 mutations published in (Barash et al., 2010), while numerous datasets have been published since then, e.g., in (Xiong et al. 2015) and (Jaganathan et al., 2019), among many others.

6. When evaluating the Bayesian optimization (BO) method for sequence design, other datasets could be considered, such as the SMA dataset in (Xiong et al. 2015).

Minor Comments:
- Not all figure panels are labeled, and some figure references are incorrect, e.g., Fig. 1b in subsection 3.1.1.
- Some tables have two values in some cells, and it is not clear what these values represent, e.g., in Tables 1 and 2.
- Fig. 1 is too small and challenging to read.

### Questions
I find the sequence design aspect of this manuscript interesting and promising. I have a couple of questions on that:

1. Is the Transformer model truly necessary here? Could the VAE be used to obtain representations and then be fed into the MLP? Essentially, could a single splice junction model be trained instead of a Transformer and a VAE?
2. On the same topic, it would be beneficial to understand how a model like SpliceAI, followed by an MLP, would perform as the oracle. I'm not convinced that the Transformer-based splice site detection (with a 400bp context) outperforms SpliceAI with a 10kb context.
3. Assuming that a tissue-specific splicing model works (which needs to be demonstrated), can the BO method be adapted to modify AS only in a specific tissue, such as the brain?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
