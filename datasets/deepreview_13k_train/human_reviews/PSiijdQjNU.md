# Steering Protein Family Design through Profile Bayesian Flow

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Protein family design emerges as a promising alternative by combining the advantages of de novo protein design and mutation-based directed evolution.In this paper, we propose ProfileBFN, the Profile Bayesian Flow Networks, for specifically generative modeling of protein families. ProfileBFN extends the discrete Bayesian Flow Network from an MSA profile perspective, which can be trained on single protein sequences by regarding it as a degenerate profile, thereby achieving efficient protein family design by avoiding large-scale MSA data construction and training. Empirical results show that ProfileBFN has a profound understanding of proteins. When generating diverse and novel family proteins, it can accurately capture the structural characteristics of the family. The enzyme produced by this method is more likely than the previous approach to have the corresponding function, offering better odds of generating diverse proteins with the desired functionality.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors build a generative model of protein sequences based on the Bayesian Flow Network model, which they adapt to categorical data. They show that, conditioned on a protein family, their model better predicts structure and generates more realistic proteins than previous models as measured by activity and structure predictors.

### Strengths
They use a new architecture to model protein data.
They have many different sources of validation which have the potential to be convincing.

### Weaknesses
I strongly suggest the authors write their introduction more carefully. 1) de novo design, even if it has a low success rate, can be useful for library design. It is not necessarily to be contrasted with directed evolution as an alternative; in practice, libraries designed with these methods are used to find a hit which is then optimized by directed evolution. 2) The statement "However, it tends to produce proteins too similar to the original wild type, limiting the exploration of protein space and hindering the discovery of globally optimal proteins with desired functions." seems intuitively sound but is not backed up by empirical data in the literature. Given these comments as well, it makes little sense to position their "protein family design" as a third way (this paragraph should also compare their method with PoET and EvoDiff); I would appreciate them putting it in context in a library -> optimization pipeline. The related works section has a similar issue.

The paper understates the methods that previously have modeled protein families. I would like the authors to make it very clear that PoET, and ProtMamba (https://www.biorxiv.org/content/10.1101/2024.05.24.595730v1, which was not cited), did something like this previously; the authors mention some of these works in the experimental section, but they should be clearly mentioned in the introduction and related works section. I appreciate that the authors take an alternative approach to these models (which train on protein families); I would therefore also like an argument for why the authors expect their method to outperform these methods in principle given that one might expect their method to perform worse since they didn't train on protein family data.

The introduction of their model is too colloquial. It would strengthen the paper for the authors to introduce BFNs by describing the generative process and likelihood normally ("VLB stands for variational lower bound" for example). This lack of rigour is manifest in many of the ways the authors use the model (see questions).

"Consequently, we can bypass the need to construct an MSA profile training set, offering a more efficient and practical solution." This solution is more "efficient and practical" for the authors not the practitioners or those who wish to use the model; the authors should simply curate a training dataset as other model developers have done many times.

Important aspects of all of the evaluations are in the appendix, including the definition of nearly every metric. Any detail needed to understand the soundness of the evaluation (how you predict the enzymatic activity) should be in the main text.

In terms of soundness, conditioned on a protein family, one wishes to sample more sequences from that family. "diversity" and "novelty" are not the goal -- these statistics should be compared to those of the real family.

### Questions
What does the sampling process have to do with the generative process described by a BFN? It seems you're "denoising" a profile, but your claim is that the generative model itself outputs profiles. Please be as rigorous in your answer as possible.

In "Sampling Process Reflects Protein Conservation" the authors show a correlation between conservation at a site and transition rate. Is this something we expect? Is this something we should be interested in?

In Table 3 the authors show that the representations of their model can be used to predict downstream tasks (by the way, it is misleading to bold their results when they do not beat the baselines). Conspicuously missing is mutation effect prediction on ProteinGym. Is there a reason your model was not benchmarked on this when arguing for "understanding"?

Could you release representative sequences suggested by all models for table 2? Were their diversity or similarity to the conditioned family significantly different? How mush of the protein family did you pass to PoET to do this evaluation -- could you be clearer on how the baselines were run?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a new method for family-based protein generation, as a cross between mutation-based (where a single sequence is mutated one residue at a time) and de novo methods (where the design is entirely structure- or function-driven and the sequence is inferred from scratch). It does by adopting Bayesian Flow Networks. It operates in sequence space and is thus most analogous to a handful of recent methods on sequence-based diffusion, which is in general an underexplored space for protein design.

### Strengths
* The method is novel and explores a region of algorithm space that is generally underexplored for proteins, namely sequence-based design and in particular MSA-based design.
* Results are competitive if not necessarily state of the art. I consider the paper more about new ideas and approaches as opposed to necessarily achieving the best results.
* The method essentially finds a niche between quality and novelty of generated structures, sitting in between existing methods on the Pareto frontier.
* Experiments are well done and the algorithm itself appears clever.

### Weaknesses
 * Biggest weakness (see question) is that how the evaluations are precisely done is not well described at all.

### Questions
* In Table 1, structural metrics are described (LR P@L) but how structures are predicted is actually never described. The paper repeatedly refers to CAMEO but CAMEO is not a method, it’s an evaluation set. Are actual structures being predicted using AlphaFold or similar method and then assessed? Or are only contacts being predicted using e.g., Potts models and then assessed? This is never stated in the main text or the appendix as far as I can tell.
* Similarly in Table 2, percentages are provided for what fractions of enzymes are considered functional, but the method of assessment is never mentioned! How is an enzyme being assessed as being functional? Is this based on a prediction tool? If so which tool?
* Similarly in Table 3, the focus is no longer on just enzymes but function prediction in general, but again how any of the accuracies are computed is never mentioned.

If these ambiguities are properly addressed I would increase my score.

### Soundness
3

### Presentation
3

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
Introduces a novel modification to the pre-existing Bayesian Flow Networks (BFN) learning scheme to create the ProfileBFN. It then applies this new ProfileBFN to the protein generation task. Like AlphaFold (and many other works) they use MSA, however, they use the the distribution statistics of MSA rather than the actual MSA data directly. They show that they technique performs well across most metrics, and produces state of the art results in some.

### Strengths
The results are overall quite impressive. Despite being outperformed in some metrics, ProfileBSN still achieves decent results in those metrics while achieving state of the art results in other measurements. 

Additionally, I like the use of Bayesian Flow Networks, which are not entirely in the mainstream techniques in protein modeling. This gives this paper a high degree of novelty

I appreciate the introduction to BFNs provided in Section 2.2. This greatly helped the readability.

### Weaknesses
The mathematics is not presented in the easiest way to understand. It is not so problematic that I reject the submission, but it is not written in an easy manner for the reader to follow. Reuse of variable names (see Questions) is an issue, but the largest issues are:

A - In line 170: dimensions are given for the summation symbol. This does not make sense, as summation is an operator, not a data type. Please explain what this means. I have held off on lowering the score too much for it in hopes there is a good explanation, but I definitely would like to see an answer for this. 

B - Explanation for many of the results feels quite rushed, and I had to put a lot of effort into parsing it out.

### Questions
1 - Why do you use sigma for both the Kronecker delta and the Dirac delta functions? This is confusing.

2 - You do not define PMF. What does it stand for?

3 - You do not define phi, it just appears in equation 3 (and in the line above). What does phi represent?

4 - Why do you not cite the paper (Z Lin’s or another) that introduces ESM-2?

5 - How did you choose the hyper parameters in lines 266-267?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors introduce Profile Bayesian Flow Networks (ProfileBFN), an adaptation of the Bayesian Flow Networks from Graves et al. (2023), designed specifically for aligned protein sequences in multiple sequence alignments (MSAs) and their frequency profiles. They derive a simplified loss function measuring the squared difference between the predicted latent embedding p_phi and the encoded representation e_x, effectively capturing how well the model’s predictions align with encoded information in the data.  Furthermore, the authors present techniques to efficiently sample from the model.
Arguing that training directly on MSA profiles rather than raw MSAs offers key advantages, the authors highlight that MSAs can be large, computationally intensive, and challenging to generate. By relying on sequence profiles instead, their method reduces computation and even enables training on single sequences rather than full MSAs. Furthermore, the approach does not require additional profile data construction, but instead leverages existing sequence profile data for training.
Their results show that the generated sequences better capture protein contacts than standard MSA-based methods. Additionally, in-silico refolding of these generated sequences predicts structures that closely resemble native structures. Despite these advances, the generated sequences remain highly similar to native sequences in terms of sequence identity.

### Strengths
The papers' emphasis is focused on the mathematical derivation and has clear explanations of key theoretical components. The authors benchmark ProfileBFN against multiple SOTA methods, demonstrating that it performs on par with or surpasses existing approaches.

### Weaknesses
While the paper is strong on the mathematical side, it lacks some depth in application.

### Questions
To better showcase the strength and applicability of ProfileBFN, I’d suggest the following points:
* The authors claim that their method is suitable for de-novo design, potentially enabling the creation of novel sequences, structures, or even entirely new functions. However, it appears that the sequences generated by ProfileBFN are optimized variants closely resembling native sequences in terms of similarity and identity. Could the authors elaborate on this point and clarify how ProfileBFN supports de-novo design?
* Could the authors specify which protein families were used to evaluate their method? In particular, is there a dependency between the depth of the MSA and the quality of the generated sequences? Certain regions, such as antibody loops (and loops in general), are challenging to model and generate due to the complexity of viable variations. Have the authors considered testing ProfileBFN in these difficult sequence spaces?

### Soundness
3

### Presentation
3

### Contribution
4
