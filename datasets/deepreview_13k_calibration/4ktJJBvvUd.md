# Multi-objective antibody design with constrained preference optimization

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Antibody design is crucial for developing therapies against diseases such as cancer and viral infections. Recent deep generative models have significantly advanced computational antibody design, particularly in enhancing binding affinity to target antigens. However, beyond binding affinity, antibodies should exhibit other favorable biophysical properties such as non-antigen binding specificity and low self-association, which are important for antibody developability and clinical safety. To address this challenge, we propose AbNovo, a framework that leverages constrained preference optimization for multi-objective antibody design. First, we pre-train an antigen-conditioned generative model for antibody structure and sequence co-design. Then, we fine-tune the model using binding affinity as a reward while enforcing explicit constraints on other biophysical properties. Specifically, we model the physical binding energy with continuous rewards rather than pairwise preferences and explore a primal-and-dual approach for constrained optimization. Additionally, we incorporate a structure-aware protein language model to mitigate the issue of limited training data. Evaluated on independent test sets, AbNovo outperforms existing methods in metrics of binding affinity such as Rosetta binding energy and evolutionary plausibility, as well as in metrics for other biophysical properties like stability and specificity.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on some important properties, such as non-antigen binding specificity and low self-association, and optimizes the model in a DPO-like manner. What differs it from other DPO-based methods lies in two forms, the optimization targets and continuous rewards. With a two stages training framework, the proposed AbNovo is capable of capturing generalized protein information and constraining the generated results with desired properties. Experiments also support the effectiveness that generated antibodies are well designed.

### Strengths
1. Multiple objects are considered to improve the quality of generated antibodies. Although not validated in wet lab, these kinds of properties are essential.
2. This work does not simply integrate DPO only optimizing binding affinity, which broadens the horizons for similar works.

### Weaknesses
1. Rosetta energy is used as an alignment metric. It is well-known that forcefield energies have a weak correlation with measured binding affinity, typically around 0.3 [1,2]. This may lead to the totally wrong direction.
2. Limited antibody optimization experiments, which should be a major highlight of antibody design. Maybe some further experiment may alleviate this, like in [3,4].

### Questions
1. In the visualization part, I don't see why results come from dyMEAN and DiffAb do not satisfy constraints like Stability, Self-association. Can you explain this in detail?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents an antibody design method, AbNovo, achieved antibody through multi-objective optimization. By introducing a structure-aware protein language model and employing constrained preference optimization with continuous rewards, AbNovo surpasses previous methods in both reference-based metrics and reference-free metrics (i.e., biophysical properties).

### Strengths
Achieved performance on physical metrics that significantly surpasses other methods.

Introduced a structure-aware protein language model and demonstrated its usefulness for antibody design.

Provided rigorous theoretical derivation

### Weaknesses
Seems to be an updated version of AbDPO, somewhat heavier but showing better performance.

The task setting is overly simplistic. Although the structure of the antibody's FR region is relatively conserved and can be considered known, the binding pose between the antibody and antigen is typically unknown. However, given that the main goal of this work is to propose a new method for antibody optimization, this limitation is understandable.

The announcement of "The first deep generative model for multi-objective antibody design" in summarized contributions, AbDPO also supports multi-objective optimization.

In energy evaluation, if you want to assess the energy performance of the designed backbone, energy minimization is necessary for the side chains while keeping the backbone structure unchanged, and then calculate the energy. If you wish to evaluate the antibody's performance in real experiments (which implies the CDR region's structure might not maintain the designed configuration), you can use multi-chain supporting folding models like AlphaFold3 to predict the binding structure. When calculating energy, does the relaxation you used optimize only the side chain conformations, or does it also alter the main chain structure? If it's the latter, are these experiments intended to demonstrate that AbNovo can generate a better initial structure for Rosetta relaxation?

Does the optimization of these physical properties contribute to some chemical validity? For example, does the peptide bond length get closer to the actual length?

The standard deviation of the physical energy needs to be presented.

The AAR performance is excessively high, and it's necessary to check whether the training data of the protein language model contains samples similar to the test set.

I am curious about how many amino acids have mutated in those designed antibodies that outperform natural ones (at least in binding energy).

The task setting of dyMEAN is different from others, including AbNovo. dyMEAN does not provide the real FR structure, making direct comparison somewhat unfair. Additionally, how is it achieved to use dyMEAN to generate 128 antibodies for an antigen?

Calculating RMSD on the aligned structures seems somewhat unreasonable. Typically, for two rigid bodies that can freely undergo SE(3) transformations, alignment is performed first, followed by RMSD calculation. However, in the setting of this paper, the FR region is given, meaning the CDR region cannot undergo SE(3) transformations independently, thus requiring a direct RMSD calculation.

### Questions
1. The announcement of "The first deep generative model for multi-objective antibody design" in summarized contributions, AbDPO also supports multi-objective optimization.

2. In energy evaluation, if you want to assess the energy performance of the designed backbone, energy minimization is necessary for the side chains while keeping the backbone structure unchanged, and then calculate the energy. If you wish to evaluate the antibody's performance in real experiments (which implies the CDR region's structure might not maintain the designed configuration), you can use multi-chain supporting folding models like AlphaFold3 to predict the binding structure. When calculating energy, does the relaxation you used optimize only the side chain conformations, or does it also alter the main chain structure? If it's the latter, are these experiments intended to demonstrate that AbNovo can generate a better initial structure for Rosetta relaxation?

3. Does the optimization of these physical properties contribute to some chemical validity? For example, does the peptide bond length get closer to the actual length?

4. The standard deviation of the physical energy needs to be presented.

5. The AAR performance is excessively high, and it's necessary to check whether the training data of the protein language model contains samples similar to the test set.

6. I am curious about how many amino acids have mutated in those designed antibodies that outperform natural ones (at least in binding energy).

7. The task setting of dyMEAN is different from others, including AbNovo. dyMEAN does not provide the real FR structure, making direct comparison somewhat unfair. Additionally, how is it achieved to use dyMEAN to generate 128 antibodies for an antigen?

8. Calculating RMSD on the aligned structures seems somewhat unreasonable. Typically, for two rigid bodies that can freely undergo SE(3) transformations, alignment is performed first, followed by RMSD calculation. However, in the setting of this paper, the FR region is given, meaning the CDR region cannot undergo SE(3) transformations independently, thus requiring a direct RMSD calculation.

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
In this manuscript, the authors present AbNovo, a method combining constrained preference optimization with generative models for multi-objective antibody design. First, an antigen-conditioned generative model is trained to co-design antibody structure and sequence. Then this model is fine-tuned to maximize binding affinity to a target antigen while enforcing constraints on properties such as non-specific Binding, Self-association, and Stability. In their experiments, the authors compare their method to many recent works and show an improved performance.

### Strengths
•	The authors provide many theoretical derivations and analysis. 
  
•	The authors include many baselines for their experiments which shows the good performance of their proposed method.

### Weaknesses
•	I would suggest introducing a background section, as there are many things in this manuscript that would benefit from a proper introduction.

  	∘	base model, reference model, policy model could be introduced, e.g. with an intuition. These are introduced in Figure 1, but do not come with a description on how they are related. Only in Algorithm 1, the reader is shown that those are updated iterations of the very same model.

  	∘	delta and G in Equation 1 is never introduced, but instead taken from Campbell et al.

  	∘	CTMC - Continuous Time Markov Chain is never defined.

  	∘	The notion of time t in diffusion processes used in the manuscript, t in U([0, 1]) is based on the CTMC definition by Campbell et al. but differs to that used on many other publications, e.g. [1] J. Ho, A. Jain, and P. Abbeel, “Denoising Diffusion Probabilistic Models”, [2] J. Sohl-Dickstein, E. Weiss, N. Maheswaranathan, and S. Ganguli, “Deep Unsupervised Learning using Nonequilibrium Thermodynamics,”. Thus, I would recommend introducing it e.g. as being in [0, 1] in line 185. Instead, this is first done in Equation 9.

  	∘	T^(0:1) as a diffusion path is first defined in line 284 even tough being used many times before.


•	The evaluation metrics remain unclear even after reading the appendix A.3. This holds especially for “Evolutionary Plausibility”, “Stability”, “Self-association”, “Non-specific Binding”.

•	While the manuscript goes in great theoretical detail, intuition is often lacking. E.g. Equation 3 is introduced but an intuition, “first term maximizes rewards, while second term keeps the model close to the reference model.”, which could facilitate understanding for the reader is missing.

•	Many things necessary for fully understanding the paper are moved to the appendix, resulting in decreased readability. Further, this also applies to some of the most interesting results, e.g. Table 9 and especially Figure 4.

•	Some tables are hard to read, as their caption and corresponding text do not exactly describe what is in the table. E.g.

  	∘	It is unclear what “reference“ in Table 1 describes.
  	∘	In Table 3 the reader must guess that “ESM-2 based” refers to “utilizing different language models” from the text and “Multi-objective” refers to “we incorporated all constraints into the optimization objective”.

•	In the abstract and introduction, a focus is put on “alleviate overfitting issues due to the scarcity of antibody-antigen training data”, but no analysis supporting such a claim is included.

•	The analysis of the “impact of utilizing different language models in training the antibody design model” is very short and not well described.

•	Figure 4 is a very interesting figure which summarizes the capabilities of DiffAb, AbX, and AbNovo very well and highlights that AbNovo “performs best“. In there, we also observe that only a single antibody generated by DiffAb against 5NUZ does violate constraints. Therefore, it seems inadequate that the visualized antibody for DiffAb in Figure 2 is a sample which does not fulfill all constraints. Furthermore, the DiffAb sample with “Rosetta binding energy: -2.12, Evolutionary Plausibility: 2.60” violating constraints cannot be found in Figure 4.

•	Some claims appear exaggerated:

  	∘	“the first deep generative model for multi-objective antibody design, which explicitly optimizes multiple biophysical properties crucial for real-world antibody development.” There have been previous works which analyze the multi-objective setting for generating antibodies, e.g. “Pareto Front Training For Multi-Objective Symbolic Optimization" by Faris et al. which train a algorithm to optimize a pareto front of sequences regarding the objectives antibody binding quality, stability, and humanness. Perhaps the claim can be weakened or reformulated?

  	∘	AbNovo is “bridging the gap between in silico design and practical application.” seems a bit too strong given that no practical application is contained.

•	Typo “Bolocks” in Figure 3

In summary, I think this manuscript offers valuable new ideas but suffers from not being self-contained, sub-optimal readabilities and depth of analysis. I hope these issues can be addressed in the rebuttal and would love to increase my score in response.

### Questions
•	in Section 4.2 you state that when “we incorporated all constraints into the optimization objective by taking a weighted average” a “drop in performance” is observable. However, the corresponding results show an improvement wrt. the “All Constraints” metric. Could you elaborate on that? 
  
•	In Table 2, we can observe that AbNovo (base) sometimes exhibits favorable scores than AbNovo. Is there a tradeoff between fulfilling constraints and achieved AAR/RMSD? 
  
•	Is there a reason dyMEAN is not included in Figure 4 and AbX not in Figure 2 respectively?

-------
Post rebuttal:
All points were well addressed. Based on this, I am increasing my score accordingly.

### Soundness
2

### Presentation
2

### Contribution
3
