# ProtComposer: Compositional Protein Structure Generation with 3D Ellipsoids

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
We develop ProtComposer to generate protein structures conditioned on spatial protein layouts that are specified via a set of 3D ellipsoids capturing substructure shapes and semantics. At inference time, we condition on ellipsoids that are hand-constructed, extracted from existing proteins, or from a statistical model, with each option unlocking new capabilities. Hand-specifying ellipsoids enables users to control the location, size, orientation, secondary structure, and approximate shape of protein substructures. Conditioning on ellipsoids of existing proteins enables redesigning their substructure's connectivity or editing substructure properties. By conditioning on novel and diverse ellipsoid layouts from a simple statistical model, we improve protein generation with expanded Pareto frontiers between designability, novelty, and diversity. Further, this enables sampling designable proteins with a helix-fraction that matches PDB proteins, unlike existing generative models that commonly oversample conceptually simple helix bundles.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a framework to generate protein structures by conditioning on layouts specified through 3D ellipsoids. The conditions include location, size, orientation and secondary structure. These conditions are injected to flow-base protein generative models via proposed cross-attention and update modules. It shows greatly improved controllability and designability over baselines.

### Strengths
This paper is well motivated, formulated, written, and evaluated. 

1. The injection of ellipsoid information is achieved through cross attention. This allows the ellipsoids to be unordered set. i.e. user doesn’t have to specify the order or ellipsoids; model also decides the order of ellipsoids. 
2. The formulation of ellipsoid token is effective and is easy to be extended to different conditions other than secondary structure. (such as hydrophobicity)
3. Thorough analysis of ellipsoid consistency, including both geometric and probabilistic metrics.
4. Fig4: The comparison on designability/diversity with baseline methods are done as comparing Pareto frontiers with varying sampling temperatures/guidances. This clearly shows the tradeoff between the methods and the performance improvement from baselines.  I found this analysis insightful and believe other papers arguing increased performance could benefit from a similar evaluation scheme.
5. The practical use-case of the method is shown in Section4.3 flexible conditioning.
6. The controllability is greatly improved from Chroma (Table1). Accuracy and coverage is very impressive.

### Weaknesses
How is sequence design performance? What I understand is that the designability is solely based on the generated structure (i.e. generated sequence is discarded). Can you also present co-design designability value as in MultiFlow paper?

Other than that, I did not find any major weaknesses from the paper. However, the ablation study can be improved. Most of the model ablations are based on guidance strength, but I am also curious about ablation study on (i) ellipsoid segementation cutoff (5A currently), (ii) allow residue token to update ellipsoid token or not. For (ii), explaining the reasoning behind the design choice may suffice.

### Questions
Is it possible to set the order of ellipsoids? Or how complicated would it be to extend this framework to allow user to set the order of ellipsoids?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work extends Multiflow to accept spatial conditioning of secondary structures via 3D ellipsoids, aiming to improve control in protein generation and reduce the overrepresentation of alpha-helices in current generative models. Building on Multiflow’s architecture, the authors address two main challenges:

1. Integrating and updating ellipsoid conditioning with structure embeddings with minimal modifications: they introduced an *Invariant Cross Attention* module to update residue embeddings while preserving local SE3 invariance.
2. Implementing an effective conditioning approach for flow-matching models: they used classifier-free guidance to interpolate flow vectors across translation, rotation, and amino acid spaces, and employ self-conditioning to refine predicted structures
    
Extensive experiments show that the proposed model can faithfully follow spatial conditioning, resulting in greater diversity, novelty, and improved secondary structure composition. This improves Multiflow by generating proteins with secondary structures more similar to natural proteins. 
Overall, this work presents a straightforward approach to control protein generation, enhancing Multiflow's diversity, novelty, and secondary structure accuracy.

### Strengths
**[Clarity & Quality]**
- The manuscript is well-written, with a thorough introduction and background information on protein structure generation, spatial conditioning, and flow matching for data generation. Overall, it provides a smooth reading experience.
- The paper is of good quality, presenting clear mathematical foundations grounded in current techniques for protein modeling, diffusion-based generation, and guided sampling.
- The problem is well-defined, and the authors designed several experiments to evaluate model performance in 1) following conditioning, 2) improving general performance, and 3) demonstrating practical use in flexible conditioning, with both quantitative and qualitative comparisons.

**[Significance]**
- The spatial conditioning approach using ellipsoids is intuitive for practical applications and has potential implications for the utility of protein generation models.
- The proposed methods appear generalizable to various spatial conditioning scenarios. (*However, this paper focuses solely on secondary-structure conditioning.*)

**[Originality]**
- The authors introduce a novel conditioning modality using spatial ellipsoids for protein generation, along with a new layer, "invariant cross-attention," to integrate this information.

### Weaknesses
 **[Clarity]**
- Some design choices and model details lack clear explanations or in-depth examination (see Q1, 2, and 4).

**[Soundness]**
- Performance on Natural Proteins: While the authors demonstrate high designability at fixed helicity levels on synthetic data, it isn't as clear if these benefits hold for natural proteins (see Q3).

**[Significance]**
- Scope: The current methods are examined only on Multiflow and for secondary structure guidance. Their practical impact on other protein generation models and types of spatial conditioning (e.g., domains, hydrophobic cores) is not extensively explored.

### Questions
1. **Ellipsoid Representation**

    a. Choosing the Number of Ellipsoids (k):
    - *Training:* Is k determined by the structure of the training protein? If so, what is the distribution of k in natural proteins?
    - *Evaluation based on the statistical model:* The authors appear to have used a fixed k=5 in the experiments. How was this number chosen? Have the authors tested other k values?

    b. Number of Residues per Ellipsoid:
    - The current representation specifies the number of residues in each ellipsoid, but the authors show that this number directly depends on ellipsoid volume. Could specifying the number of residues be redundant, and might removing this constraint provide the model more flexibility in generation? Have the authors examined the impact of residue count on amino acid (AA) prediction?

2. **Invariance Cross-Attention (ICA) Layer Design**

    a. The authors separately model the SE3 features (E_k) and scalar features (e_k) of ellipsoids using the proposed ICA and transformer to achieve SE3 invariance in the local frame. Has the team considered alternative approaches, such as modeling ellipsoids as “pseudo frames” with SE3 and scalar features and simply using IPA to update ellipsoid and residue features together?

    b. In Algorithm 1:
    - Could the authors clarify the *PosEmbed* used in line 223? Does it include distance, angles, or local coordinates?
    - Could they also explain why the query uses un-updated $s$, while the key and value use $a$, which incorporates current ellipsoid information?

3. **Results in Table 2 (natural proteins):** The model, even with the strongest guidance, tends to overestimate helices in proteins. Additionally, the authors did not present designability results, which, based on Figure 16, may be compromised with strong guidance. Could the authors elaborate on the model's performance in addressing the “overrepresented helix problem,” the trade-offs with other metrics, and its overall comparison to models like *RFDiffusion*?

4. In self-conditioning (line 290), they propose supplying interpolated conditions to both conditional and unconditional models, suggesting this improves “designability and ellipsoid adherence for all $\lambda$ values.” However, no ablation studies were provided to verify this claim.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents ProtComposer, which is a fine-tuned model from MultiFlow to support conditional generation based on 3D ellipsoids, showing success at controllable design and achieving SOTA on the Pareto frontier of designability and diversity.

### Strengths
The paper is well written with clean visualizations demonstrating methods and results. The concept of utilizing ellipsoids as conditions for protein generation is interesting and novel, providing a bridge between protein-level conditioning and atom-level conditioning. In addition, the authors propose an effective Invariant Cross Attention module for integrating ellipsoid conditioning and demonstrate success at achieving SOTA performance on the Pareto frontier of designability and diversity.

### Weaknesses
I have no major concerns about this paper. However, it would be helpful if the authors could elaborate on the applicability of the ellipsoid-based conditioning approach on practical protein design tasks. How would it help with or facilitate the protein design process?

### Questions
- Line 355: How is the length between ellipsoids determined/sampled? Also, consider an ellipsoid with beta strand annotation, how is the length between each stranded segment determined (particularly if a strand ellipsoid is formed by segments that are distant in sequence but close in structure)? 
- It would be helpful if the authors could provide ablation study results on the effect of self-conditioning, particularly the two self-conditioning schemes described in line 290.
- Figure 9: What is the linear fit and statistical significance in both cases?
- During training, is the ellipsoid conditioning information always provided, or only provided for a percentage of time?
- Line 367: Why is a structured residue considered as “covered” if it is inside at least one ellipsoid instead of inside the ellipsoid it is assigned? 
- Table 1: Could the authors provide some intuition on why over-guidance (\lambda > 1) performs better than the conditional model itself (\lambda = 1)?
- Table 2: Does “PDB proteins” correspond to the validation dataset or does it include the training dataset?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Introduces ProtComposer, a generative model for proteins. ProtComposer seeks better control over the shape of generated proteins, as well as allow for greater novelty in the generation of proteins. Notably, the user has to choose between control or novelty, ProtComposer does not achieve both simultaneously. These tasks are accomplished by the introduction of 3D ellipsoid frames to guide the generation of proteins by the pre-existing Multiflow algorithm. 

Without a pre-existing metric the authors feel sufficiently quantifies compositionality, they introduce their own metric. It is shown that ProtComposer outperforms existing methods in this metric.

### Strengths
It addresses an important and relevant area. The results are overall quite impressive as well. Additionally, showing the ability to work with handcrafted ellipsoid frames or the more easily scalable ML generated frames shows the practicality of ProtComposer.

I really like the point about using simple ML models for ellipsoid sampling as compared to NNs. I would like to see some stronger analytical or experimental justification of the claim though.

### Weaknesses
Since a custom metric is introduced in this paper and then used as justification for the performance of the model, a section (either in the main paper or the appendix) justifying this metric would be nice. Showing comparisons to other pre-existing metrics, performance of many other algorithms under this metric, or stronger domain justification would strengthen the meaning of the results. I did not reject over this since the metric intuitively looks good, but further empirical or analytical support would be nice.

The formatting of the extra results in the appendices results in very odd page layouts, where some pages are blank, others have odd whitespace gaps, etc. Adjustment to make these pages more presentable would be nice.

### Questions
I am assuming that the user can redefine K during each trial as they see fit, though studies on guidelines in choosing K would be helpful. In situations where the user has only a vague idea of what they are looking for (an unfortunately common occurrence), having a guide on where to start would be beneficial.

### Soundness
3

### Presentation
3

### Contribution
3
