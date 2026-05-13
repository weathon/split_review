# MolMiner: Transformer architecture for fragment-based autoregressive generation of molecular stories

- Decision: Reject
- Scores: 5, 3, 6, 3

## Abstract
Deep generative models for molecular discovery have become a very popular choice in new high-throughput screening paradigms. These models have been developed inheriting from the advances in natural language processing and computer vision, achieving ever greater results. However, generative molecular modelling has unique challenges that are often overlooked. Chemical validity, interpretability of the generation process and flexibility to variable molecular sizes are among some of the remaining challenges for generative models in computational materials design. In this work, we propose an autoregressive approach that decomposes molecular generation into a sequence of discrete and interpretable steps using molecular fragments as units, a `molecular story'. Enforcing chemical rules in the stories guarantees the chemical validity of the generated molecules, the discrete sequential steps of a molecular story makes the process transparent improving interpretability, and the autoregressive nature of the approach allows the size of the molecule to be a decision of the model. We demonstrate the validity of the approach in a multi-target inverse design of electroactive organic compounds, focusing on the target properties of solubility, redox potential, and synthetic accessibility. Our results show that the model can effectively bias the generation distribution according to the prompted multi-target objective.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a fragment-based generative model, MolMine, for generative molecules in an autoregressive fashion. To train MolMiner, the paper suggests using an order-agnostic way by random sampling valid molecular stories.  The experiment results demonstrate the proposed model could generate the target molecule conditioned on the given prompts.

### Strengths
1. The presentation of the paper is good. I appreciate the efforts of presenting the key steps of the proposed methods with intuitive explanations and figures，e.g. Fig1/Fig 2/Fig 4. 

2. The Molminer seems to involve a novel Transformer-based structure, which differs from the Graph Neural networks used by previous fragment-based autoregressive models. The proposed structure could hold potential for scaling. 

3. The experiments show an interesting setting and demonstrate the model could be effective in the studied scenarios.

### Weaknesses
Though I appreciate the motivation and the interesting evaluation, I believe the paper needs a major revision to get accepted by top conferences such as ICLR. 

1. The key technical contribution is not clear. I suggest the authors carefully rephrase the scoop and technical contribution of the proposed method. Specifically, I agree that the fragmentization of large molecules could be the key to enabling flexible generation.  In contrast, the five points of the introduction are not convincing to me.  For example, the paper states that the Molminer differs from the diffusion-based approach, e.g. HierDiff [1], in the fact that it could enable flexible node numbers during generation; I would consider this more as a different feature instead of the benefits. For example, HierDiff[1] also states the motivation of non-autoregressive generation over autoregressive generation in the sense of global modeling, etc. Unfortunately, I do not see any empirical evidence to compare and justify any of the proposed advantages. 


2. The evaluation parts are not comprehensive enough. Specifically, there is no baseline to compare in the experiment section which makes it very hard for me to assess the model from a systemic work perspective. From a method-oriented perspective, I am quite confused over the novelty of several important components of the proposed framework. What is the exact difference between the introduced Fragmentization procedure in Algorithm 1 and the corresponding fragmentization of previous work such as JT-VAE/HierDiff? And the training objective is a widely applied approximation for graph modeling, then I would like to consider the key novelty that originates from the network structure parts. The key components of the networks is the geometry parts which differ from previous graph transformers, however, after carefully checking the ablation in Table 1. I find that with no-geometry, the model could still perform very well, then what is the point of involving such information and increasing the complexity? 

3. Some important related works for 2D fragment-based autoregressive generation of molecules are missing [2] 

[1] Coarse-to-Fine: a Hierarchical Diffusion Model for Molecule Generation in 3D 
[2] MARS: Markov Molecular Sampling for Multi-objective Drug Discovery

### Questions
Refer to Above

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces MolMiner, an autoregressive generative model for molecules that builds them up through fragments. The authors:
* Introduce a technique for deciding on fragments (Section 2.1) -- based on dividing a molecule into its rings and other individual bonds.
* Show how to keep track of fragment attachment points (Section 2.2).
* Describe how they can model the resultant fragment sequence of a molecule (what they call a "molecular story") using an autoregressive model (the model is trained on random orders).
* Show how they can use this model to generate molecules with desirable properties by training a separate feedforward model to decide which fragment to start with. When doing so, MolMiner is able to successfully generate molecules with the desired, targeted property when that desired property is well represented in the model's training set (Figure 5).

### Update Nov 25, 2024
Have read the other reviews and authors' responses. See comment I added to their rebuttal below.

### Strengths
# S1. Paper includes detailed descriptions of the model and approach through algorithms and figures.
Figure 3 and 4, provide a detailed visual description of the MolMiner architecture and I found these helpful to understand what was happening. (A couple of very minor comments: coefficient is misspelled in Figure 3, and the box showing Figure 3 inside Figure 4 is blurry at the resolution used).

# S2. Calibration plots are clear 
Plotting the calibration curves for property optimization seems a nice way to visualize the results, and with the inclusion of the KDE show how performance depends somewhat on how "in-distribution" a property score at that value is.

# S3. Including 3D information into the 2D generation seems an interesting new idea
Including the 3D conformation information into the generation process seems interesting, and could potentially lead to better structures. While it would have been nicer to have seen better evidence for the idea's importance (e.g., via a suitable ablation study; see W1 below), this aspect of the model seems to differ from previous fragment based approaches.

### Weaknesses
# W1. Experiments do not demonstrate the approach's advantages compared to existing methods or explain design choices made (hence why low "soundness" score).
The experiments do not consider any baselines, such as the alternative fragment-based approaches discussed (such as Jin et al., 2019, 2020) or non-fragment-based approaches (such as Gómez-Bombarelli et al., 2018). It is therefore hard to gauge how useful MolMiner would be and what advantages it offers over existing, already established approaches.
Moreover, I also have a hard time distinguishing the importance of the design choices made, e.g., the incorporation of 3D information  (lines 256-258) or the semi-order agnostic serialization method proposed (line 263). (Information on 3D information is shown in Table 2 of the appendix, but it seems to only be in terms of accuracy, rather than the effect on optimization, and the effect seems fairly minor).

# W2. The method for optimizing molecules (based on picking an initial fragment according to how well it is modeled to affect a particular property score) seems like it is unlikely to scale to more interesting optimization tasks.
My current understanding of the optimization method (lines 380-386) is that it involves learning a feed forward neural network to pick the initial fragment, but that the rest of the fragment generation process happens as usual. For harder optimization tasks, I worry that other parts of the molecule will also be important and so this method is unlikely to scale.

# W3. Novelty of method (modeling molecules via generating fragments) seems low and I would have liked to have seen the differences to these approaches better studied or discussed. (hence why low "contribution"/"presentation" score).
There are several existing approaches to generating molecules that take a fragment based approach. Examples include the cited Jin et al. (2019, 2020) as well as others such as:
- Marco Podda, Davide Bacciu, Alessio Micheli (2020) 'A Deep Generative Model for Fragment-Based Molecule Generation' AISTATS 2020.
- Bengio, E., Jain, M., Korablyov, M., Precup, D. and Bengio, Y. (2021) ‘Flow network based generative models for non-iterative diverse candidate generation’, NeurIPS 2021
- Xie, Y., Shi, C., Zhou, H., Yang, Y., Zhang, W., Yu, Y. and Li, L. (2021) ‘MARS: Markov Molecular Sampling for Multi-objective Drug Discovery’, ICLR 2021. 
- Maziarz, K., Jackson-Flux, H., Cameron, P., Sirockin, F., Schneider, N., Stiefl, N., Segler, M. and Brockschmidt, M. (2022) ‘Learning to Extend Molecular Scaffolds with Structural Motifs’, ICLR 2022.
One of the main differences here seems to be the inclusion of the 3D information (see S3), but it would have been nice to have seen a comparison and discussion of these previous approaches.

### Questions
Other questions I had:
1. Lines 406-407 mentions accuracy (in the context of optimizing MolMiner’s hyperparameters). What does accuracy mean here? (Is this the fragment-level reconstruction accuracy?)
2. What is the "GetSSSR" function on line 110?
3. I'm a little confused as to the remapping procedure described in section 2.2. Why not just use atom map numbers in the SMILES to define the attachment points? (I think my main confusion is around how the symmetries are dealt with. Are all points that are symmetrically the same maintained as attachment points or is just one chosen?)
4. I just wanted to check if I understood the notation $\mathcal{U}(\mathcal{S}(\mathcal{M}))$ in Equation 1 correctly. Is this a uniform distribution over all possible stories? How important is this sampling for performance (compared to e.g. using a fixed ordering across all epochs, or restricting the number of possible orders by using a depth first search).
5. The datasets used seem quite small (~8500 molecules used for training). Does this limit the number of fragments observed and how big was the resultant fragment vocabulary?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces MolMiner, a novel generative model designed to tackle challenges in molecular generation by leveraging a fragment-based, autoregressive approach. The core idea is to generate molecules step-by-step using molecular fragments, which makes the generation process more interpretable and allows the model to decide the molecule size dynamically.

MolMiner addresses several key challenges in generative molecular modeling, including chemical validity, flexibility in molecular size, and incorporating 3D spatial information. By enforcing chemical rules during the generation process, MolMiner ensures that chemically valid molecules are produced at every step, reducing the risk of invalid outputs. Additionally, the model uses transformer-based geometry-aware mechanisms to account for the spatial arrangement of molecular fragments.

### Strengths
The paper's key strength lies in its novel approach to molecular generation, where it effectively combines concepts from natural language processing, such as autoregressive transformers, with the domain-specific requirements of chemistry. By framing molecular synthesis as a sequence of interpretable, fragment-based steps—termed "molecular stories"—the paper addresses significant challenges like chemical validity and lack of transparency in molecular generative models. This reinterpretation of the generative process not only makes the model's decisions easier to understand but also empowers domain experts to validate and interact with the process, bridging an important gap between machine learning and chemistry.

The use of geometry-aware transformers adds another layer of sophistication by ensuring that the model can capture the spatial properties of molecular structures, which are crucial for generating chemically meaningful compounds. The integration of chemical rules during generation to enforce validity is another well-executed innovation that strengthens the quality of the model. These aspects collectively offer a comprehensive and robust approach, improving upon limitations seen in previous one-shot or black-box generative models.

The empirical results are also well-supported, with extensive experiments that validate the model's ability to generate novel molecules aligned with desired properties. This showcases the model's potential for real-world applications in drug and material discovery. Overall, the originality in problem formulation, combined with a thoughtful implementation that directly addresses core limitations in prior models, makes this work a significant and valuable contribution to the field.

### Weaknesses
Limited Empirical Scope: The experimental evaluation is restricted to a narrow set of target properties (log-solubility, redox potential, synthetic accessibility). Broader validation, including additional properties (e.g., pharmacokinetics or biological activity) and diverse datasets (such as QM9 or ZINC), would substantiate the versatility of MolMiner.

Lack of Interpretability Quantification: While the model's interpretability is highlighted, the benefits are not explicitly demonstrated or quantified. User studies involving domain experts or real-world case studies would provide practical evidence of the interpretability advantages claimed by the authors.

Fragment Selection Analysis: The chosen fragment extraction method (SSSR) is not thoroughly justified or compared to alternatives. Including an ablation study to explore different fragmentation methods and their impact on model performance would enhance the robustness of the proposed approach.

### Questions
See weakness

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
4

### Summary
This paper presents MolMiner, a transformer-based autoregressive model to generate molecules by assembling fragments. This paper details on fragment pre-processing, specifically on how it assigns indices to atoms in fragments and canonicalizes indices of attach points (by using the minimum index in symmetrical cases). A decoder-only transformer network is used to generate a sequence of (fragment, attach point) tuples to build molecular graphs.

### Strengths
- Generating molecules by fragments rather than by atoms is more likely to create reasonable molecular structures and hence increases validity.
- Detailed explanation on fragment preprocessing and atom indexing.

### Weaknesses
- The core idea of this paper, generating molecules by motifs or fragments, has been practiced for very long time. There have been review articles discussing the progress in this area [1, 2]. This paper overlooked the progress in this area and in the current context the novelty of the proposed method is very limited.
- The evalution is very weak. This paper only demonstrates MolMiner's application in **only** three properties, specifically, SAScore, solubility, and redox potential. Evaluting the model solely on them is not a strong evidence of praticality of the proposed models, as these scores are somehow week and simple.
- The Introduction section mentioned "Incorporating 3D information". However, I did not notice how 3D information was significantly incorporated in both method formulation and evaluation.
- The concept of "molecular story" is weird. A "molecular story" is basically an auto-regressive generation process of a sequence of molecular fragments. There seems to be nothing else that makes the generation process unique or novel such that it needs a new name to describe itself. It seems to me that the "molecular story" name leads to confusion and ambiguity.

[1] Sergei Voloboev. A Review on Fragment-based De Novo 2D Molecule Generation (2024)

[2] Shao Jinsong et al. Molecular fragmentation as a crucial step in the AI-based drug development pathway (2024)

### Questions
See Weaknesses

### Soundness
1

### Presentation
2

### Contribution
1
