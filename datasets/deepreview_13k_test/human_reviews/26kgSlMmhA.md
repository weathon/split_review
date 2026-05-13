# Any-Property-Conditional Molecule Generation with Self-Criticism using Spanning Trees

- Decision: Reject
- Scores: 6, 6, 5, 3, 3, 5, 5

## Abstract
Generating novel molecules is challenging, with most representations leading to generative models producing many invalid molecules. Spanning Tree-based Graph Generation (STGG) \citep{ahn2021spanning} is a promising approach to ensure the generation of valid molecules, outperforming state-of-the-art SMILES \citep{weininger1988smiles} and graph diffusion \citep{song2019generative} models for unconditional generation. In the real world, we want to be able to generate molecules conditional on one or multiple desired properties rather than unconditionally. Thus, in this work, we extend STGG to multi-property-conditional generation. Our approach, \highlight{\textbf{STGG+}}, incorporates a modern Transformer architecture, random masking of properties during training (enabling conditioning on \emph{any} subset of properties and classifier-free guidance), an auxiliary property-prediction loss (allowing the model to \emph{self-criticize} molecules and select the best ones), and other improvements. We show that \highlight{\textbf{STGG+}} achieves state-of-the-art performance on in-distribution and out-of-distribution conditional generation, and reward maximization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents STGG+, a model for molecule generation with conditional property control. The model also has the ability of self-criticism to select optimal outputs. It achieves high validity and diversity in generated molecules, efficiently handling both typical and extreme properties.

### Strengths
The paper presents molecule generation models, allowing multi-property control and self-assessment of generated molecules. It’s well-designed, with detailed experiments showing strong results across different datasets. The writing is clear and structured.

### Weaknesses
The self-criticism mechanism for filtering generated molecules based on property predictions is a key feature, but there is limited evaluation of its accuracy. Detailed analysis will be necessary.

I am not an expert of this field so I will lower my confidence score.

### Questions
In the OOD setting, how the model’s performance varies under different guidance settings, especially for extreme or non-physical property values?

### Soundness
3

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
3

### Summary
The authors build upon spanning tree-based graph generation methods to produce valid molecules with desired properties. They enhance the original network architecture by adding property embeddings and incorporate a properties predictor head for joint training. Through the use of classifier-free guidance and conditioning on these properties, the authors demonstrate that STGG+ can generate molecules conditioned on specific properties or with high reward values.

### Strengths
1. To my knowledge, this manuscript is the first to thoroughly examine STGG for reward conditioning and/or optimization.
2. The work reflects a substantial effort to assess STGG+'s capabilities. Overall, the approach appears methodologically sound.
3. Molecular property optimization is an open challenge. Given its competitive performance compared to existing algorithms and its use of a (somewhat) unique molecular representation, I expect this work will attract reasonable interest.

### Weaknesses
1. The primary limitation of this paper is that generating 'valid' molecules does not guarantee synthesizability. Many molecules presented in the appendix would be very challenging, if not impossible, to synthesize. Meanwhile, some baseline methods may perform slightly worse on reward but produce molecules that are easier to synthesize, avoiding "reward hacking." A fairer comparison would involve evaluating the reward optimization performance of synthesizable molecules across different algorithms.
2. While novelty is not an ideal measure of a paper's value, this work is highly empirical, with limited theoretical insight. This puts more emphasis on competitive performance, yet the paper lacks adequate baseline comparisons for reward optimization. Previous work has shown that methods such as GraphGA, LSTM-HC, and Reinvent are effective at maximizing OOD reward, and these baselines should be included in Sections 4.3–4.5 (particularly Section 4.5, which currently lacks any baseline comparison). This is especially relevant as the random guidance approach for OOD generation resembles slightly enhanced random sampling with a reward proxy.
3. The molecular properties selected for optimization in this study are _very_ simple. For instance, molecular weight can be adjusted by adding or removing atoms, and logP by incorporating ionic groups (which the model does). Optimizing HOMO-LUMO gaps within the QM9 dataset is not useful, as these molecules contain only 9 atoms. These problems are generally considered solved.
4. Although the work is extensive, certain details are presented inconsistently or lack substantiation. Some claims are unsupported by data (e.g., statements like "other [configurations] were not beneficial/did not improve performance" lack any data references). Additional issues include appendix figure captions that are unclear and lack cross-references in the main text (e.g., molecules with QED > 1 in figures 8 and 14), and captions inappropriately implying low QED correlates with implausibility (e.g., figure 9). Many terms are undefined, including "synthe. MAE," "HOMO/LUMO," "SAS," as well as the precise definition of diversity used here. Additionally, error bars are missing in all tables.

### Questions
1. In SMILES notation, the same molecule can have multiple string representations. Based on my (limited) understanding of STGG, this ambiguity seems present as well. How are the molecules canonicalized?
2. In Tables 3 and A.10, do all methods reach peak performance only after generating 1 million molecules? Is the search space the same across methods?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed to extend Spanning Tree-based Graph Generation (STGG) to multi-property conditional generation, namely STGG+, with improvements to successfully engineer and implement the concept. STGG+ achieves SOTA on both in-distribution and OOD conditional generation, as well as reward maximization.

### Strengths
- This paper is presented with sufficiently clear descriptions.
- The authors explored a wide range of techniques that can be applied in the under-explored context of multi-property conditional generation.

### Weaknesses
- It seems to me that the authors invented complicated ad-hoc designs and specifically engineered to fix any issues that may arise, for example by masking the creation of rings when reaching max number (100), or alternating the use of CFG and ranking via a property-predictor. I'm afraid this hampers the overall generality of the proposed method.
- Ablation studies are missing. What's the effect of the improved Transformer architecture against the vanilla one? How does the auxiliary property prediction loss contribute to the results? The same applies to CFG w/ and w/o random guidance, the masking mechanism, the ring overflow treatment, the order randomization, and the automatic construction of vocabulary instead of a predefined one. Detailed ablations are needed to validate the authors' special designs, and provide more insight to the community.

### Questions
In Table 2, why not report the MAE at different percentiles, instead of only the MinMAE? It's possible that the model simply memorizes some extreme cases seen in training so as to achieve a good minimum MAE.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed the STGG+ method, an improved method of the Spanning Tree-based Graph Generation (STGG), for generating novel molecules with multi-property conditional generation. Architecture-wise, this work introduced

1. an improved Transfomer with Flash-Attention. RMDProp, etc.
1. an extended STGG model for more robust graph generation of molecules.

By randomly masking some properties at training time and using Classifier-Free Guidance (CFG), the model was shown to generate novel in- and out-of-distribution molecules with any property conditional generation.

### Strengths
### Originality
1. This work proposed an improved method of the STGG model for any property conditional molecule generation.
1. This work introduced classifier-free guidance and self-criticism into the transformer architecture.

### Quality
1. The proposed method is shown to improve the validity and diversity of generated molecules.
1. The method is also shown to better generate molecules with desired/conditioned properties.
1. The results are shown across multiple datasets and properties.

### Clarity
1. The STGG+ architecture is clearly explained.

### Significance
1. Any-property conditional generation is a challenging yet important task in technical applications. For instance, in drug discovery, it is important to generate molecules with desired curative properties and avoid molecules with toxic properties.

### Weaknesses
As a computational chemist with expertise in molecules (and SMILES), I am concerned with
1. the contribution and improvement of this work, STGG+, to the original STGG model or the original SMILES-based molecule generation methods.
2. this work's representation of chemistry and molecules in terms of correctness and novelty.

**The STGG+ representation of molecules is within the capabilities of SMILES representation.**
1. The STGG+ improvements to STGG are not significant enough
   - the proposed improvements such as masking of invalid tokens, automatic calculation of valency, etc., seem similar to adding if-else conditions to improve the original STGG model.
   - In my opinion, these improvements should be learned by the model itself during training. The model itself should learn to avoid invalid tokens and keep track of valency. These are all fundamental grammar rules that the model should learn by itself.
   - If these constraints are manually added, it limits the efficiency of the generation process. For example, valency calculation can be intricate in the generation process when rings are involved.
   - Because of these manual implementations, I am not convinced that the STGG+ representation is significantly better than the SMILES representation in terms of ensuring valid molecules.
2. The proposed benefits of STGG+ (spanning-tree representation) compared to SMILES representation are not entirely true. SMILES can also achieve the claimed benefits with similar modifications. For example,
   - In SMILES, rings are represented by two identical numbers at the beginning and end of the ring. For cyclohexene, its SMILES representation can be `C1CCCCC=1` (or `C1-C-C-C-C-C=1`) and its spanning-tree representation can be `[bos]C[bor]-C-C-C-C-C=[eor1][eos]`. In the spanning-tree representation, a `[bor]` token must be paired with a `[eor#]` token before `[eos]` to form a valid molecule. Whereas in SMILES, a ring-starting number must be paired with the same number before the end of the string.
   - Automatic calculation of valency can be done in SMILES as well in the same fashion as STGG+ since the spanning-tree representation and the SMILES representation are interchangeable during the generation process.

**This work lacks clarity on the spanning-tree representation such as explicit/implicit hydrogen atoms and canonical representation.**
1. In Figure 1, line 140, the spanning-tree representation used a combination of explicit and implicit hydrogen atoms. The nitrogen atom was shown with an explicit hydrogen atom, and all the carbon atoms were shown without hydrogen atoms (implicit). However, from Appendix A.4, it seems that the vocabulary is collected for spanning tree representations with explicit hydrogen atoms.
1. The above point leads to the question of canonical representation - The same molecule can have different SMILES representations and different spanning-tree representations. In other words, different sequences of tokens can point to the same molecule. For example, `[bos]C[bor]-C-C-C-C-C=[eor1][eos]`, `[bos]C[bor]-C-CH2-C-C-C=[eor1][eos]`, and `[bos]C[bor]-CH2-C-CH2-C-C=[eor1][eos]` can all represent the same cyclohexene molecule.
1. For the reported generative efficiency (% of valid, novel, and unique molecules), was canonicalization performed/considered? If not, the reported efficiency might be overestimated. Additionally, the authors should provide some examples of the generated sequences and their corresponding molecules to clarify the canonicalization process.
2. **Suggestions:** In Section 3.3, the authors should discuss the issue with explicit/implicit hydrogen atoms and canonical representation. Try to clarify the following points:
   - Does STGG+ generate molecules with explicit hydrogen atoms only or can it also generate molecules with implicit hydrogen atoms? The spanning-tree representation should allow both.
   - How is the canonical representation handled in the training and generation processes?
   - **What is the definition of valid, novel, and unique molecules?** Are molecules considered unique if they have different sequences of tokens but represent the same molecule?

**The reported property MAE of the conditional generation needs more explanation.**
1. For the properties of the generated molecules, were they calculated with the property predictor of the STGG+ architecture or with an external property calculator such as RDKit? The external predictor should provide the ground truth for the property values and should thus be used for the evaluation.
2. The `MinMAE` reported in Table 2 needs more clarification: is it the minimum absolute error across the 2K generated molecules? What does "minimum mean" refer to?
   - If the minimum is reported, what about the mean of the absolute errors?
   - For such a large number of generated molecules, the mean absolute error is a better metric to evaluate the performance of the conditional generation. This is related to the application of the model (line 57) - validating the properties of the generated molecules in real life can be costly. Conditional generation aims to generate a small set of potential candidates. Minimum error implies that one has to test all 2K molecules (too large) to find the best candidate, while average error better represents the overall conditional generation performance.
   - The minimum absolute error might be more convincing if reported on a small population of generated molecules such as 10x molecules with multiple batches.

### Questions
My questions are closely related to the weaknesses mentioned above. The authors are encouraged to address the points raised in the weaknesses section. Some questions include but are not limited to:
1. The STGG+ approach claims improvements over SMILES-based molecule generation methods. **What are some of the improvements that the SMILES representation fails to achieve or is difficult to achieve compared to the STGG+ representation?**
2. The spanning-tree representation allows both explicit and implicit hydrogen atoms. Are the generated molecules restricted to explicit hydrogen atoms or can they also have implicit hydrogen atoms?
3. How does the model/evaluation handle canonicalization of the generated sequences/molecules?
   - Does uniqueness consider canonicalization or does it only consider differences in the generated sequences?
4. For reporting the property MAEs, was an external property predictor used for the evaluation? How is MinMAE reported?
   - If an external property predictor was used, provide the details of the external predictor for MolWt, LogP, QED, and HOMO-LUMO gap.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes an enhanced version of Spanning Tree-based Graph Generation (STGG+), tailored for multi-property conditional molecule generation. Based on the STGG, STGG+ includes improvements in the Transformer architecture, a flexible conditioning mechanism for any subset of properties, and a self-criticism mechanism that filters generated molecules based on a property predictor.

### Strengths
This paper used a property-predictor-driven self-criticism mechanism that allows STGG+ to evaluate and select the best out of multiple generated molecules, improving fidelity to target properties.

### Weaknesses
1. The model’s effectiveness relies heavily on the internal property predictor, which may be less reliable for out-of-distribution samples. This dependence could reduce fidelity in less representative scenarios.
2. Although the model improves conditioning performance, it’s unclear how it balances molecule diversity and property, diversity is also a crucial metric in molecular generation.

### Questions
1. The authors improved the structure of the original Transformer, but the results do not seem to reflect the improvements, such as whether the generation time and the quality of the generated molecules have been improved.
2. For the self-criticise, the authors should discuss the trade-off between performance gains and computational cost. Including a comparison of computational time for different values of k would clarify the model's efficiency.
3. The authors should optimize the structure of the result table, as it is not clear what is being compared, e.g. modify the table head.
4. For property-conditional generation. The authors only compare the MinMSE and should add some property distributions to demonstrate that the generated molecules approximate the given conditions.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper considers the problem of generating (hopefully) new representations of molecules. Existing techniques either work with a 1D string representation of molecules or a 2D graph representation. This work considers the former representation and builds on a method called Spanning Tree-based Graph Generation (STGG) that was specifically created to use generative AI models. The present work differs from existing work along the following two high level aspects:

1. Previous work would generate molecules without any restrictions. However, this paper considers the problem of generating molecules that has to satisfy (some) subset of a given set of properties that the generated molecules must satisfy.
2. Unlike existing results the paper creates models that can _self-criticize_ by allowing the model to predict properties of the molecules it generates and uses that to prune out molecules that do not satisfy the required properties.

The paper lists conceptual improvements made in this work in the context of generating molecules but since I'm more familiar with Transformers and related literature, I will focus my review on those. Specific to the Transformer model used in this work (as opposed to the STGG work), the paper uses improvements made to the Transformer architecture (e.g. FlashAttention) over the last three years.

The paper presents a pretty comprehensive (at least to me) set of experiments and show that the proposed new system works better than existing systems on benchmarks that are used in this area.

### Strengths
* The problem considered in this paper (molecule generation) has clear practical importance and given that there exists standard 1D string representation of molecules, using generative AI to create new molecules is definitely a  promising avenue worth pursuing.

* The paper has a pretty comprehensive experimental results and they show the efficacy of the proposed system.

* While some of the techniques used in the paper might be `standard' for say language modeling, being able to apply these techniques in a completely new application domain and show improvement is very nice.

* The ability to impose certain properties on molecules being generated and having the model be able to self-criticize seems like really nice capabilities.

### Weaknesses
Below are some questions that I was not able to answer based on what is there in the paper. (Again, as mentioned earlier, I focused in the Transformer aspects of the paper so all of the questions below are on that axis.) Also some of these questions might be asking for intuitive answers and not necessarily something that could potentially be answered with experiments-- but having these answers might be useful for the reader to understand some of the design choices made by the paper:

* (Q1) The paper uses causal Transformer models-- is there any reason a non-causal Transformer model cannot be used? E.g. non-causal Transformer models have been used on applications other than language modeling (e.g. ViT in image processing)-- and pre-Transformer language models like BERT were non-causal. In theory non-causal models are more expressive than non-causal model (just because a causal model is trivially a non-causal model as well).

* (Q2) The idea of having the model self-criticize the molecules it generates reminded me a lot of GANs. Have GANs been tried to generate molecules? If so, have they worked or is there some intuition for why they did not work?

* (Q3) Over the last ~3 years there have been a fair amount of work on `Transformer-free' models for language generation. One such line of work is based on state space model (Mamba [see https://arxiv.org/abs/2405.21060 and https://arxiv.org/abs/2312.00752] being a model that has garnered a lot of attention in the language modeling literature). Some of these ideas have been used in genomic sequencing (e.g. Hyena DNA-- https://arxiv.org/abs/2306.15794). Where these recent models considered in this work?

* (Q4) In lines 227-228, it is mentioned that the _number_ of masked properties $t$ was picked uniformly at random between $0$ and $T$. However, which of the $\binom{T}{t}$ subset of properties were actually chosen to mask?

Below are some minor comments (that are purely related to presentation):

* Lines 354-355: Instead of saying "similar" performance-- please quantify, i.e. within what percentage of existing work?

* Table 1: Is _Distance_ in the table column name the same as FCD?

### Questions
Please address (to the extent possible) Q1-Q4 in the Weakness section. Specifically for Q1-Q3, please state if the alternate techniques were considered when designing the experiments/writing the paper. If so, please explain why those alternate ideas were not incorporated into the paper. If not, please discuss how these alternative techniques might be relevant to the problem considered in the paper.

Post-Rebuttal Comments
----------------------------

The authors have addressed pretty much all of my concerns. As of Nov 25, I'm keeping my original score since I'm curious to see how the reviewers with the two lowest scores (one of whom is an expert in the paper's area) respond to the author's responses to their questions.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 7

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper tackles the issue of generating valid molecules by extending the Spanning Tree-based Graph Generation (STGG) to support multi-property conditional generation. The proposed STGG+ integrates a Transformer architecture, property masking, and an auxiliary loss for model self-evaluation.

### Strengths
1. The paper is well written.
2. The authors suggest modifications that make sense and feel intuitive.

### Weaknesses
1. I find the changes to be intuitive but somewhat obvious, leading me to believe that the paper lacks significant novelty.
2. Please see questions.

### Questions
1. I didn't completely follow the details of best-of-k filtering described in Section 3.6. It would be good if the authors could explain how this is exactly done. 
2. Based on observations: In Table 1, STGG+ shows an improved synth MAE, but other metrics appear comparable. In Table 2, STGG+ outperforms by design. In Table 3, the settings aren't directly comparable. Does this imply that the primary novelty lies in achieving property conditioning? If so, is the novelty somewhat limited, given that the extension feels intuitive?
3. Considering the non-comparable nature of Table 3, could the experiments be repeated under consistent settings for a fair comparison?
4. It’s currently unclear which modifications specifically drive the improvements in STGG+. Conducting ablation studies based on the points listed on page 2 (points 1-5) would provide more clarity.
5. For conditional generation, online methods like GFlowNets could serve as an additional baseline. Would it be possible to include this baseline in Table 2?

**Paper suggestions:**

a) I think, including Figure 3 (suplementary) instead of Figure 1 in the main paper would better showcase the contributions.

b) For section 3.6, I found the figure a little confusing. It may help to have a better figure to explain the same.

### Soundness
3

### Presentation
4

### Contribution
2
