# Beam Enumeration: Probabilistic Explainability For Sample Efficient Self-conditioned Molecular Design

- Decision: Accept
- Scores: 8, 8, 8, 3

## Abstract
Generative molecular design has moved from proof-of-concept to real-world applicability, as marked by the surge in very recent papers reporting experimental validation. Key challenges in explainability and sample efficiency present opportunities to enhance generative design to directly optimize expensive high-fidelity oracles and provide actionable insights to domain experts. Here, we propose Beam Enumeration to exhaustively enumerate the most probable sub-sequences from language-based molecular generative models and show that molecular substructures can be extracted. When coupled with reinforcement learning, extracted substructures become meaningful, providing a source of explainability and improving sample efficiency through self-conditioned generation. Beam Enumeration is generally applicable to any language-based molecular generative model and notably further improves the performance of the recently reported Augmented Memory algorithm, which achieved the new state-of-the-art on the Practical Molecular Optimization benchmark for sample efficiency. The combined algorithm generates more high reward molecules and faster, given a fixed oracle budget. Beam Enumeration shows that improvements to explainability and sample efficiency for molecular design can be made synergistic.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Generative molecular design has transitioned from theoretical validation to practical utility, evidenced by a recent surge in papers featuring experimental confirmation. In this evolving landscape, addressing challenges related to explainability and sample efficiency becomes crucial for optimizing high-fidelity oracles efficiently and providing valuable insights to domain experts. This paper introduces Beam Enumeration as a solution, aiming to exhaustively enumerate the most probable sub-sequences from language-based molecular generative models. The method demonstrates the extraction of meaningful molecular substructures. When integrated with reinforcement learning, these extracted substructures contribute to enhanced explainability and improved sample efficiency through self-conditioned generation. Notably, Beam Enumeration is adaptable to any language-based molecular generative model and significantly enhances the performance of the Augmented Memory algorithm, a recent state-of-the-art achievement in sample efficiency on the Practical Molecular Optimization benchmark. The joint focus on explainability and sample efficiency makes Beam Enumeration a pioneering method in the field of molecular design.

### Strengths
- The paper is well-written, well-organized, and easy to follow. 
- The idea is quite intuitive and straightforward. It is based on the state-of-the-art language model--augmented memory. 
- The paper also emphasizes sample efficiency, which is an essential problem in practical molecular design. It does not only require the optimization ability but also the oracle efficiency. The oracle can be computationally expensive and the bottleneck of the modern molecular design. 
- The whole setup is realistic. Novel Oracle efficiency-based metric is designed. 
- Code is easy to read and is public, guaranteeing the reproducibility. 
- The experimental results are thorough and solid. The proposed beam enumeration significantly outperforms REINVENT (the strongest baseline in the existing benchmark). It also exhibits explainability during the generation.

### Weaknesses
 - It would be great if authors could incorporate more baseline methods.
- Some minor issue, e.g., repetitive statements, like 
"To address this, Gao et al. (Gao et al. (2022) proposed the Practical Molecular Optimization (PMO) (Gao et al. (2022) benchmark." Too many "Gao et al".
- Do you use the same setup with PMO? If not, it seems unfair to compare with PMO's best baseline REINVENT.

### Questions
Is it possible to incorporate MD-based simulation as oracle? How long does it take for each oracle call? Can you provide more details?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose "Beam Enumeration", a technique that can be used to enhance any language-based molecular generation models in terms of sampling efficiency and explainability.
The key idea is to exhaustively enumerate the most probable subsequences, and the model's weights are updated such that high-reward molecules become more likely to be generated in future trajectories. 
This is achieved by "self-conditioning" the generative process by screening batches based on the presence or absence of substructures that are likely to be part of full molecules with high reward scores.

### Strengths
Overall, this is an excellent paper that is very well written.
The proposed idea is relatively simple but well-motivated, intuitive, and generally applicable to various generative molecular design models based on language models.
Beam Enumeration, proposed in this paper, has been applied to a state-of-the-art generative language model for molecular design - called Augmented Memory - and results demonstrated that the incorporation of Beam Enumeration was able to further enhance the performance of the Augmented Memory algorithm, which was already shown to outperform other existing methods.
Notably, the proposed scheme enhances the sampling efficiency significantly and the extracted top-k substructures during the generation process are shown to provide additional sources of explainability - by connecting the presence of most likely substructures in full molecules with high rewards.

Throughout the paper, the authors provide ample intuition and novel insights regarding not only "how" the proposed Beam Enumeration scheme works but also "why" they may lead to improved sample efficiency and also contribute to better explainability.

### Weaknesses
The overall paper is written very clearly and easy to follow.
Throughout the paper, the authors distill intuitive explanations and derive meaningful insights, conclusions are drawn with sufficient evidence to back them up, and hypotheses/speculations are made in a reasonable and logical manner.
As a result, I do not have any major concerns but have a number of mostly minor remarks to improve the presentation even further.

1. There are additional results in the appendix regarding the impact of the proposed Beam Enumeration scheme on reducing diversity.
While the main text briefly mentions such diversity reduction is expected, the paper would benefit from having (at least some) further discussion (in the main text) on this effect and its extent.

2. There should be further investigation of the impact of k (i.e., the number of top substructures) on the performance of Beam Enumeration.
The authors hypothesize that a low top k would be optimal, but wouldn't the use of small k potentially lead to molecules with repetitive substructures and undesirably limit the molecular diversity?

3. Similarly, the manuscript could benefit from having further discussion on the optimal choice of the "Structure Minimum Size" - currently set at 15 in the experiments - and its impact on the overall performance.
It is mentioned that "larger substructures ... improves performance" but what is the best minimum size to use?
Increasing it beyond some number would certainly degrade the performance of the molecules and also limit the diversity of the generated molecules significantly.

4. The multi-property optimization (MPO) aspects will need to be discussed in further details.
Currently, the MPO appears to completely rely on the baseline algorithm (e.g., Augmented Memory or REINVENT) to be extended with the Beamn Enumeration capability.
But since different substructures might be associated with different properties, incorporation of Beam Enumeration for MPO would have to consider the impact of self-conditioned molecular generation when used with a specific baseline algorithm and a specific number of properties for optimization.
For example, one may expect that when optimizing a large number of properties, then using a very small k may be detrimental as the selected substructures may be associated with only some of the properties of interest.

5. Finally, while the paper focuses on language models for molecular generation and uses Beam Enumeration for self-conditioning the generative process by filtering the most probable substructures, it would be great if the authors could discuss how similar ideas may be used to extend other types of popular generative molecular design models (e.g., latent space models based on VAE, JT-VAE).
Especially, models like the JT-VAE optimize molecules by sampling & assembling substructures (in the form of junction trees), which - at least at a conceptual level - *may* be related to the core "self-conditioning" idea in Beam Enumeration, to prioritize certain substructures.
While this may be beyond the scope of the current work, having at least some high-level discussion might benefit the readers.

### Questions
Please see the questions and suggestions raised in the section Weaknesses above.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The manuscript discusses the use of beam search enumeration in tandem with RNN-based reinforcement learning for molecular design. The results demonstrate that meaningful substructures can be derived, which provide insights into the properties they confer. Utilizing these substructures as filters, there is a notable increase in the sample efficiency of molecular optimization. Though there are a few flaws, the results and methods seem solid. Overall, I would recommend the paper for acceptance if authors could address my concerns.

### Strengths
## Importance of the problem
The paper delves into oracle-agnostic molecular optimization, which holds significance in the realm of AI-driven de novo drug design.

## Solid empirical performance
A marked improvement in empirical performance has been observed.

## Open-sourced code
The authors have made the code available, facilitating comparisons and further research.

### Weaknesses
## Ambiguity in Methodology
The methodology entails several phases, namely training RNN agents, beam enumeration, and resampling based on substructures. From the manuscript, it appears that only beam enumeration does not invoke the oracle while the others do. The allocation of the oracle budget across these stages is unclear. A comprehensive pseudo-code encompassing the entire algorithm, rather than just the beam enumeration, would be beneficial. Specifically, the manuscript lacks clarity on how the oracle budget is distributed between the initial training of the RNN, the reinforcement learning phase, and the substructure-based resampling. It's crucial to understand if the oracle is used to evaluate all generated molecules or if a filtering mechanism is in place before oracle evaluation, and how this impacts the overall sample efficiency.

## Exaggerated Claims
The assertion that this is the "first method to concurrently address explainability and sample efficiency" is overstated. Guo et al. [1] have put forth a concept strikingly akin to the one proposed here, where they too derive interpretable substructures and then generate novel molecules. Likewise, Fu et al. [2] have purportedly tackled both interpretability and enhanced sample efficiency. The claim of novelty should be toned down, as methods like Data-Efficient Graph Grammar (DEG) and Differentiable Scaffolding Tree (DST) also explore the relationship between interpretable substructures and efficient molecular generation. The specific differences and advantages over these existing methods need to be more clearly articulated.

## Potential nomenclature confusion
Beam search is a well-established technique within the NLP community. I would recommend revisiting the nomenclature for the proposed method. The term 'beam enumeration' is too close to 'beam search' and could cause confusion, especially since beam search is a common technique in sequence generation. A more distinct term would help avoid this ambiguity.

### Questions
- Would it be possible to exhibit the SA score, as per reference [1], for the molecules generated in the context of drug discovery (Figure 3)?
- Have the authors considered employing a more advanced language model, like the transformer, as an alternative to LSTM?
- Is there a direct comparison between the presented methods and those in PMO using the original metrics?

### Reference
[1] Ertl, P., & Schuffenhauer, A. (2009). Estimation of synthetic accessibility score of drug-like molecules based on molecular complexity and fragment contributions. Journal of cheminformatics, 1, 1-11.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Through this paper, the authors aim to increase explainability and sample efficiency in drug discovery problems. To accomplish this, the authors proposed Beam Enumeration that exhaustively enumerate the most probable sub-sequences from Augmented Memory.

### Strengths
- The authors provided the codebase.
- The writing is easy to follow. The concept figure aids the understanding.

### Weaknesses
The main weaknesses of the paper are that the contribution (both conceptual and technical) is marginal and the proposed method is heuristic rather than machine learning-based (and thus seems out of scope for ICLR) and lacks a mathematical basis. The proposed method relies primarily on Augmented Memory [1], and the methodology outside of Augmented Memory (*Beam Enumeration* ~ *Self-conditioned Generation* paragraphs in Section 3) are short and seems like an additional trick.

I will combine the *Weaknesses* section and the *Questions* section. My concerns and questions are as follows:

- What is the difference of the generation scheme in Figure 1a with that of Augmented Memory?
- The *Autoregressive Language-based Molecular Generative Model* paragraph in *Proposed Method* section should be moved to *Related Work* section as that part is not proposed by this paper.
- Are there any ablation studies that quantify the effects of Augmented Memory? Are there experiments that quantify the effects of the combination of Beam Enumeration and other generative models?
- The method description seems a bit vague. I recommend to explain the self-conditionining scheme in paragraph *Self-conditioned Generation* more concretely.

### Questions
Please see the *Weaknesses* part for my main questions.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
