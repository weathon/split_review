# DEL-Ranking: Ranking-Correction Denoising Framework for Elucidating Molecular Affinities in DNA-Encoded Libraries

- Decision: Reject
- Scores: 6, 3, 3

## Abstract
DNA-encoded library (DEL) screening has revolutionized protein-ligand binding detection, enabling rapid exploration of vast chemical spaces through read count analysis. However, two critical challenges limit its effectiveness: distribution noise in low copy number regimes and systematic shifts between read counts and true binding affinities. We present DEL-Ranking, a comprehensive framework that simultaneously addresses both challenges through innovative ranking-based denoising and activity-referenced correction. Our approach introduces a dual-perspective ranking strategy combining Pair-wise Soft Rank (PSR) and List-wise Global Rank (LGR) constraints to preserve both local and global count relationships. Additionally, we develop an Activity-Referenced Correction (ARC) module that bridges the gap between read counts and binding affinities through iterative refinement and biological consistency enforcement. Another key contribution of this work is the curation and release of three comprehensive DEL datasets that uniquely combine ligand 2D sequences, 3D conformational information, and experimentally validated activity labels. We validate our framework on five diverse DEL datasets and introduce three new comprehensive datasets featuring 2D sequences, 3D structures, and activity labels. DEL-Ranking achieves state-of-the-art performance across multiple correlation metrics and demonstrates strong generalization ability across different protein targets. Importantly, our approach successfully identifies key functional groups associated with binding affinity, providing actionable insights for drug discovery. This work advances both the accuracy and interpretability of DEL screening, while contributing valuable datasets for future research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors define a novel objective function for finding hits from a DEL screening campaign. They then compare their approach across a number of different DEL datasets of carbonic anhydrase.

### Strengths
The description of the field is helpful.

I think the deep dive into the biochemical and technical sources of variation are helpful.

The number of datasets in which evaluation was done is impressive.

The ablation experiments are very helpful and surely a lot of work, so I appreciate them described in detail here.

Generally, I think the authors are quite well versed in the field and problem domain.

### Weaknesses
Generally, I’m a bit confused about the discussion of “Distribution Noise”. Is this variance? Others in the sequencing space has parameterized this as either a negative binomial or a zero-inflated negative binomial–is this what you’re referring to? If so, it’s just the variance of the observations.

Are the acronyms ARDC, AGR, and CDEC necessary? Is there a one-word description of these that you could propose to summarize their function? For example:

ARDC - Reference Correction
AGR - Refinement
CDEC - Consistency

This will help the reader follow how each of these components contribute to the model. This is in addition to new acronyms PSR, and LGR.

More care needs to be given to defining the Pairwise Soft Ranking Loss. There are a number of variables that either aren’t defined or aren’t used consistently. It’d also be great to have more intuition for design decisions on the objective function. What happens when certain components become large or small? Why multiply or subtract things? As a reader that’s worked with DEL data, this isn’t clear.

The same is true for the Listwise Global Ranking Loss. What is s_i? How does it differ from s_{\pi(i)}? Then \sigma is recycled from PSR as the weight for L_con?

“a novel ranking loss that rectifies relative magnitude relationships between read counts enabling the learning of causal features determining activity levels”. The use of ‘causal’ is particularly strong here. How do you disentangle correlation from causation? What aspects are explicitly causal?

In section 3.1, where is the “Activity Label” derived? Is it used in any equation? (This is y_i). The variable y is then also used in line 250–is this the same?

Again in section 3.3, what is Activity? Also “...where Apred and Atrue denote the predicted and ground-truth activity”: Do you actually ever know “ground-truth” activity, or is it just ‘observed’? Typically there is just some biochemical proxy for ‘ground-truth’.

Where are \Delta G_ij and \Delta D_ij defined? I see the non \Delta versions defined in lines 254 and 255.

How do you know the docked poses described in part 4 are actually real, or correspond to where the molecule is binding? Have these docking poses been shown to correspond to read counts in these molecules?

“Traditional methods based on binding poses and fingerprints inculde[sic]...Benzene Sulfonamide…” What is Benzene Sulfonamide? This is just a carbonic anhydrase-specific thing?

Is the “zero-shot” predictions just also on carbonic anhydrase? That seems disingenuous. I would anticipate zero-shot to be on another target entirely, not just a different dataset on the same target.

Were the pyrimidine sulfonamide groups identified by any other method presented here?

Was the pose encoder necessary? It seems superfluous to the other components added here, and quite complex.

### Questions
“a novel ranking loss that rectifies relative magnitude relationships between read counts enabling the learning of causal features determining activity levels”. The use of ‘causal’ is particularly strong here. How do you disentangle correlation from causation? What aspects are explicitly causal?

In section 3.1, where is the “Activity Label” derived? Is it used in any equation? (This is y_i). The variable y is then also used in line 250–is this the same?

Again in section 3.3, what is Activity? Also “...where Apred and Atrue denote the predicted and ground-truth activity”: Do you actually ever know “ground-truth” activity, or is it just ‘observed’? Typically there is just some biochemical proxy for ‘ground-truth’.

Where are \Delta G_ij and \Delta D_ij defined? I see the non \Delta versions defined in lines 254 and 255.

How do you know the docked poses described in part 4 are actually real, or correspond to where the molecule is binding? Have these docking poses been shown to correspond to read counts in these molecules?

“Traditional methods based on binding poses and fingerprints inculde[sic]...Benzene Sulfonamide…” What is Benzene Sulfonamide? This is just a carbonic anhydrase-specific thing?

Is the “zero-shot” predictions just also on carbonic anhydrase? That seems disingenuous. I would anticipate zero-shot to be on another target entirely, not just a different dataset on the same target.

Were the pyrimidine sulfonamide groups identified by any other method presented here?

Was the pose encoder necessary? It seems superfluous to the other components added here, and quite complex.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
DNA-encoded library (DEL) screening has been an instrumental technique in accelerating the pace of drug development. By attaching a unique DNA “barcode” to each compound, thousands of compounds can be screened against a protein target in a single experiment. The number of copies of each barcode indicates how many of those compounds are bound to the target protein. However, the barcode count data is noisy, is not directly correlated with the dissociation constant, and contains systematic biases. Therefore, the problem is reduced to generating a ranking of compounds based on observed barcode read counts. The authors address the main issues in DEL screening by proposing a new ranking loss, rectifying some inherent issues in read counts, and implementing a self-training method to align activity labels with barcode read counts.

### Strengths
Unfortunately, I am not able to gauge the strengths of this paper due to presentation issues (see “Questions”).

### Weaknesses
Unfortunately, I am not able to gauge the strengths of this paper due to presentation issues (see “Questions”).


**Minor points**
- In Fig. 1, the middle panel incorrectly depicts DNA barcodes binding to the target protein; it should show “building blocks” instead. A correct version can be found in (Shmilovich et al., 2023).
- In line 104, ZIP loss has not been defined.
- In line 147, the statement “While existing methods offer improved scalability and the ability to capture complex molecular interactions, they still face challenges in interpretability” is vague and needs further elaboration.


I had difficulty following the problem formulation. Here are some of my questions:

- Why are M_i and R_i \in \mathbb R+? Can’t these counts be zeros?
- M_i​ is control counts and R_i is the target counts. But in line 197, it states: “modeling read counts r_i as (M_i,R_i), where M_i accounts for excess zeros and R_i represents non-zero counts.” I am confused. Is r_i two-dimensional? Moreover, what does the (M_i, R_i) tuple mean?
- In Eq. (2), why does each compound have a different \pi (\pi_i)?
- Why do control and target counts not have different \pi values, as in Shmilovich et al. (2023)? These \pi values should differ by orders of magnitude.
- In the Problem Definition, y_i​ \in {0,1} is the activity level, but in line 250, “\hat y_i​ represents the predicted read count value for compound i.” Then, what are \hat M​_i and \hat R_i introduced in Eq. (1)?
- In Eq. (4), L_PSR does not seem to be a function of i or j, as the sum goes over all values of i and does not depend on j either.
- In the same equation, why does it depend on y_i and y_j? Should it have been \hat y_i and \hat y_j? Although, the authors also mention in line 254 that G_i = softplus(y_i).
- What is “K” in Eq. (5)?
- In Eq. (6), L_GSR, the first term on the right-hand side does not depend on i or j, while the second term depends on both i and j. Should there be a double sum over i and j for the second term?
- On the same note, what is “s_i​”? Is it the same as r_i​?

### Questions
I had difficulty following the problem formulation. Here are some of my questions:

- Why are M_i and R_i \in \mathbb R+? Can’t these counts be zeros?
- M_i​ is control counts and R_i is the target counts. But in line 197, it states: “modeling read counts r_i as (M_i,R_i), where M_i accounts for excess zeros and R_i represents non-zero counts.” I am confused. Is r_i two-dimensional? Moreover, what does the (M_i, R_i) tuple mean?
- In Eq. (2), why does each compound have a different \pi (\pi_i)?
- Why do control and target counts not have different \pi values, as in Shmilovich et al. (2023)? These \pi values should differ by orders of magnitude.
- In the Problem Definition, y_i​ \in {0,1} is the activity level, but in line 250, “\hat y_i​ represents the predicted read count value for compound i.” Then, what are \hat M​_i and \hat R_i introduced in Eq. (1)?
- In Eq. (4), L_PSR does not seem to be a function of i or j, as the sum goes over all values of i and does not depend on j either.
- In the same equation, why does it depend on y_i and y_j? Should it have been \hat y_i and \hat y_j? Although, the authors also mention in line 254 that G_i = softplus(y_i).
- What is “K” in Eq. (5)?
- In Eq. (6), L_GSR, the first term on the right-hand side does not depend on i or j, while the second term depends on both i and j. Should there be a double sum over i and j for the second term?
- On the same note, what is “s_i​”? Is it the same as r_i​?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper tackles the problem of how to build a good machine learning model of ligand binding activity based on DEL screens. The two primary challenges with modeling DEL-based data is the noise in the data and the mismatch between the true log-enrichment of a compound in the DEL assay and the actual binding affinity of the compound. The authors propose a number of new modeling approaches to tackle these issues. First, a new ranking-loss is proposed. In addition the authors introduce an iterative training approach that promotes the matching of read-based predictions to true activity values as well as a consistency loss.

### Strengths
The paper addresses a number of relevant challenges to an important problem of predicting binding affinity from DEL data.

### Weaknesses
1) I found it really hard to understand the details of the specific losses and approaches. For example, Equation 4 seems to depict a function that takes in two element, y_i and y_j, but the right-hand side is written using a sum of 'i' and 'j', suggesting it is over the entire dataset?

I was unable to understand at all what the activity-guided refinement is based on the written text. Similarly, there is no clear motivation for the specific choices of many of the loss functions. For example, Equation 8 is just presented but there is no explanation for why the particular terms are included over a simpler loss such as ||A_true - A_pred||_2.

2) The largest weakness for me is that the paper seems reads as a "bag-of-tricks". Each individual loss may be reasonably motivated, but each loss term also introduces its own set of hyperparameters. This paper introduces at least 6 new hyperparameters. Importantly, there was no discription of how these hyperparameters were chosen and no demonstration that they can be robustly chosen using a validation set. Thus, I do not believe the authors have demonstrated that they have actually produced a more useful method. So far, they have only shown that with a carefully chosen set of hyperparameters and the introduction of a much much more complicated modeling scheme that they can slightly improve the spearman correlations.

3) Nowhere in this paper is the ZIP loss actually defined. It first shows up in the paper with just the acronym and no description of what ZIP means.

### Questions
1) How were the hyperparameters chosen?

2) Can they be chosen robustly with a validation set? Please provide experiments demonstrating this, if so.

3) Using molecular docking structures seems potentially problematic as these poses are often wrong and therefore add noise to your model. Please discuss this further.

4) The authors claim that DEL data is inherently ranking in nature, but this is not obvious to me. The relative magnitude of the log-enrichments may provide useful information about the binding affinity. Throwing away this information and only ranking loses information.

5) What is ZIP? 

6) Please provide further discussion of the iterative algorithm.

### Soundness
2

### Presentation
1

### Contribution
2
