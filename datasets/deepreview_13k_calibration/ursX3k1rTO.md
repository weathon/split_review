# Wyckoff Transformer: Generation of Symmetric Crystals

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 6, 6, 3

## Abstract
We propose Wyckoff Transformer, a generative model for materials conditioned on space group symmetry. Most real--world inorganic materials have internal symmetry beyond lattice translation. Symmetry rules that atoms obey play a fundamental role in determining the physical, chemical, and electronic properties of crystals. These symmetries determine stability, and influence key material structural and functional properties such as electrical and thermal conductivity, optical and polarization behavior, and mechanical strength. And yet, despite the recent advancements, state--of--the--art diffusion models struggle to generate highly symmetric crystals. We use Wyckoff positions as the basis for an elegant, compressed, and discrete structure representation. To model the distribution we develop a permutation--invariant autoregressive model based on Transformer and absence of positional encoding. Our experiments demonstrate that Wyckoff Transformer has the best performance in generating novel diverse stable structures conditioned on the symmetry space group, while also having competitive metric values when compared to model not conditioned on symmetry. We also show that it is competitive in predicting formation energy, band gap, mechanical properties, and thermal conductivity.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper focuses on the tasks of de novo materials generation and materials property prediction. The main contribution is a Wyckoff representation tokenization and model training strategy. For de novo generation, once the transformer generates a Wyckoff position then PyXtal and CHGNet are used to generate/relax the structure. In particular, the model is good at generating materials with the proper space group.

### Strengths
- The application of ML to materials discovery is interesting and timely. 
- The Wyckoff representation builds in crystal symmetries in a natural way. 
- Good empirical results for template novelty, P1, and Space Group metrics.
- The paper is written well

### Weaknesses
 - Little improvement in standard de novo generation metrics. SUN actually goes down compared to DiffCSP.   
- Additionally, de novo generation metrics were computed with a ML potential instead of DFT.  
- The property prediction benchmark is not particularly compelling because there are better benchmarks out there with other more recent models as baselines (e.g. CHGNet), such as Matbench discovery. 
- If not there, it would be good to include this citation (https://arxiv.org/abs/2106.11132).

### Questions
- You found a nice way to tokenize a Wyckoff representation, would it be better to fine-tune a LLM with this representation than train a transformer from scratch? The CrystalLLM paper (https://arxiv.org/abs/2402.04379v1) had some nice results that could potentially be improved with your representation. 
- Another important axis is the inference speed or cost of de novo generation, how does WyFormer or WyForDiffCSP++ compare to DiffSCP/FlowMM? 
- Is there a way to more concretely show the benefit template novelty?
- Can you plot the distribution of space groups generated from WyFormer compared to MP-20 distribution?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a transformer-based approach that leverages Wyckoff positions to encode material symmetries efficiently. This is done by primarily encoding the discrete symmetries of space groups without using atomic coordinates. The discussion on WyFormer, including tokenization and (extensive) metrics, is detailed. Their main contribution is to represent a crystal as an unordered set of tokens and make de novo material and property predictions. Furthermore, four new metrics are proposed (P1, Template Novelty, Space Group, and S.S.U.N.) to judge the ability to reproduce symmetry properties accurately. Results indicate that WyFormer outperforms other methods in terms of template novelty, space group distribution, and fraction of asymmetric structures.

Overall I think the paper could be a good step in the direction of using symmetries for property prediction, provided certain clarifications on experimental details and broader evaluations are addressed.

### Strengths
- Crystal representation for tokenization.
- Material property prediction results are surprisingly good when compared against neural nets trained for energy prediction.
- Four new metrics provide a new way of looking at models' ability to generate symmetry properties.
- Justification in the appendix for the selected two structure generation methods.

### Weaknesses
 - The scope of material property prediction- authors focus on just two (energy and band gap). If feasible, can the authors provide some insight on which other properties could be predicted, purely from a correlation with crystal structure perspective? It is unclear if the model can be extended to predict other properties such as mechanical or electronic characteristics, which are also crucial for material design.
- The proposed method is evaluated on a single dataset, MP-20, and makes it hard to judge the generalizable nature of WyFormer from it. Are there other datasets on which performance can be evaluated? The lack of evaluation on diverse datasets limits the assessment of the model's robustness and its ability to generalize to different types of materials and crystal structures.

- In section 1.3, line 138, "...our main differences are listed in the discussion of our contributions 1.2."  where are the main differences listed in section 1.2? Or am I missing something?

- Can the authors explain why the Space Group value for WyForDiffCSP++ is high while the S.S.U.N. value is similar to WyCryst in Table 1a? The discrepancy between these two metrics raises questions about the model's ability to accurately capture the underlying symmetries of the generated structures. A more detailed explanation of this behavior is needed.

- A discussion on computational cost would be good to have, given that the authors mention that the entire dataset fits into GPU memory (training time and memory requirements). The absence of computational cost details makes it difficult to assess the practical applicability of the method, especially for large-scale material discovery.

- Are there methods apart from CHGNet that improve crystal structure generation?

- Have the authors tried other property prediction experiments besides energy and band gap?

Additional Feedback:
1. line 280: "they to be" -> "they are"?
2. line 282: percetage -> percentage?

### Questions
1. In section 1.3, line 138, "...our main differences are listed in the discussion of our contributions 1.2."  where are the main differences listed in section 1.2? Or am I missing something?

2. Can the authors explain why the Space Group value for WyForDiffCSP++ is high while the S.S.U.N. value is similar to WyCryst in Table 1a? 

3. A discussion on computational cost would be good to have, given that the authors mention that the entire dataset fits into GPU memory (training time and memory requirements)

4. Are there methods apart from CHGNet that improve crystal structure generation?

5. Have the authors tried other property prediction experiments besides energy and band gap?

Additional Feedback:
1. line 280: "they to be" -> "they are"?
2. line 282: percetage -> percentage?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper highlights the problem of generative models for crystals not generating symmetric crystals, which is an important property of these materials. This results in less realistic materials as well as inability to model some properties of crystals correctly. The authors propose to address this limitation by generating materials in a two-stage process. First, they train a Transformer model to output occupied Wyckoff positions in the crystal. Then either a method based on DiffSCP++ or PyXtal is used for atomic coordinates. The authors verify experimentally that this allows to generate more symmetric and diverse crystals.

### Strengths
- The work tackles an important limitation of generative models for crystals
- The proposed solution is simple and sound
- The experimental evaluation shows that the method addressed the limitation. The evaluation metrics for symmetry and novelty of structures based on Wyckoff templates is also valuable.

### Weaknesses
 - Just using the Wyckoff positions is not a complete representation, especially for atoms in the general position. The sentence "reducing the number of parameters by an order of magnitude without information loss" is false. I also don't think that statement that desired properties can be obtained from the discrete values alone is accurate or substantiated by enough evidence. I therefore encourage the authors to substantially nuance that section. The experiments on property prediction indicate a degradation of performance in property when discarding coordinates.
- The model is claimed to be invariant with respect to the choice of coset representative and to permutations. This formulation is too strong, since this is achieved through data augmentation. A correct statement would be that the model is encouraged to be invariant.
- The proposed representation for Wyckoff positions is universal across space groups but might not allow proper generalization since the "enumeration" variable is not grounded on physical information but on an arbitrary convention. Therefore, if a group is rare in the training data (this is indeed the case for datasets like MP20), there is no reason that the model will learn to capture that variable correctly. The authors should discuss this limitation appropriately. 
- I did not find the discussion of the related works to be sufficient. The authors should expand that discussion so that the readers understand the differences and similarities with the proposed method better.
- I find that the explanation of Wyckoff position in the third paragraph of the introduction is not easy to understand. It may be too early in the paper to go into such an explanation.
- There are some typos and mistakes that the authors should look into correcting. For example, "lattice transition -> lattice translation" or "   Cordiality -> Cardinality".

### Questions
- I don't see what the footnote 1 adds to the discussion, I find it more confusing than anything. Could the authors clarify it, or consider simply removing it?
- I don't understand the expression in the abstract "These symmetries form energy configurations". What is meant there?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a transformer-based architecture to generate symmetric crystals conditioned on space groups in a two-stage process. Initially, it generates tokens representing elements and their site symmetries, followed by lattice and coordinate predictions for these tokens with existing methods. The results include comparisons with multiple baselines, showing competitive performance across established proxy metrics. Finally, the paper also proposes metrics to assess the symmetry of the generated crystals and highlights further gains over baseline approaches.

### Strengths
- The paper emphasizes the importance of generating symmetric crystals and highlights challenges with existing methods.
- The evaluation methods, including the newly proposed methods for evaluating symmetry, form a compelling discussion section.
- The method demonstrates effective gains for the symmetry metrics and is competitive for widely-used proxy metrics.
- The paper proposes a novel representation of crystal symmetry that could facilitate learning of crystal symmetry with deep learning approaches.

### Weaknesses
 - **Presentation and writing**: Essential concepts (site symmetry, wyckoff positions, space groups) are not appropriately introduced, which would create difficulty for readers unfamiliar with the field. Several works are cited in the related works section, but neither described nor highlighted the difference from their approach. Figures for architecture and pseudo-code to describe the training and generation pipeline would greatly benefit the understanding of the work.

- **Generalization of the approach**: 
  - The paper heavily focuses on the MP-20 dataset and does not provide any experiments with other datasets. For instance, it states permutation invariance was achieved because the number of WPs in the MP-20 dataset is small. How can this method be extended (or how does it fare in terms of performance) for crystals with a very high number of WPs? It is unclear if the method can handle a significantly larger number of Wyckoff positions, which are common in more complex crystal structures. The paper should discuss the limitations of the approach in this regard.
   - There are no precise details on how many tokens were formed from the MP-20 dataset after tokenization. It would be interesting to discuss this number and other statistics about the tokens, e.g., which tokens are present more often (for some of the high symmetry space groups) and how the distribution of tokens affects training.  It is also important to add how many new tokens the method generates or if it just predicts the fixed set of tokens in different combinations (and these combinations result in more template novelty than just sampling existing templates from training data). For instance, naively thinking about it, how will your model generate tokens that are not present in its dictionary?  The paper should clarify whether the model is capable of generating novel tokens or if it is limited to combinations of existing tokens. This is crucial for assessing the method's ability to explore new chemical spaces. Finally, in Table 1a, please also provide the number of novel templates as absolute numbers instead of percentages.

- **Architecture**:  - Please provide at least a pseudo-code of the training/generation algorithm and a figure explaining the training/generation process with a sample crystal example. The central algorithm is not clear from the text.   - Please mention the size of the model and computational and memory consumption (training time, memory required during training and generation). The paper lists that it is trained for $150k$ epochs, which seems to be a very long training process compared to existing methods (~$1k$ epochs). Can you explain this behaviour along with the set of hyperparameters used? The paper should provide a detailed analysis of training time and memory requirements, including a comparison with existing methods, to assess the practical feasibility of the approach.

- **Evaluation**:  - Can WyCryst be considered a fair baseline for comparison since it supports a limited number of unique elements per structure? For instance, it wouldn't compare with other methods that generate an arbitrary number of methods because it would result in poorer metrics (as seen in Table 1). The paper should justify the choice of WyCryst as a baseline, given its limitations in handling diverse chemical compositions.  - Is CHGNet used both to relax the generated structures and determine the energy in Table 1?   - Please mention the percentage of novel but structurally invalid generations from your method.

### Questions
- **Two-stage approach**: Can you explain the benefits of a two-stage approach instead of a one-shot (such as DiffCSP) prediction of the site symmetries, elements, their positions and lattice parameters? If problems exist with a one-shot prediction, please explain and motivate the need for a two-step approach. For instance, can we (as an example) predict all the tokens (with elements, site symmetry, enumeration) followed by the lattice parameters and the fractional coordinates of the tokens or are there inherent issues with this approach? This question becomes more necessary since the generation of crystals would be slow for the proposed "sequential two-stage" approach. 
- **Crystal Structure Prediction (CSP)**: The paper focuses on generating crystals conditioned on space group. How could this method be extended to the CSP task, which is also crucial and could potentially benefit from using crystal symmetry?
- **Dataset fragmentation**: Although the tokens can be shared across different space groups, there will still be dataset fragmentation when the approach is conditioned on the space group. Is the training (and then generation) not affected by how many samples are present within each space group?

Some of the other questions are listed in the Weaknesses section. I will be happy to improve the score if the authors address the questions and weaknesses with supportive evidence during the discussion phase.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes the **Wyckoff Transformer**, a generative model designed for creating highly symmetric crystal structures by leveraging **space group symmetry**. Recognizing that most inorganic materials exhibit inherent symmetries, the authors develop a model that encodes these symmetries to influence key material properties such as stability, conductivity, and optical behavior. The Wyckoff Transformer uses **Wyckoff positions** as a discrete, permutation-invariant representation of atomic locations, eliminating the need for explicit positional encoding and improving the model’s efficiency and alignment with crystal symmetries.

Key contributions of the paper include:

1. **Tokenization of Crystals**: The authors represent crystals as an unordered set of tokens, merging information on chemical elements and their Wyckoff positions, enabling symmetry-based generation.
2. **Permutation-Invariant Encoding**: The model encodes Wyckoff positions based on symmetry-defined point groups, allowing for the generation of stable structures without positional encoding.
3. **Transformer Architecture**: The Wyckoff Transformer combines **autoregressive probability factorization** with permutation invariance, enhancing diversity and stability in generated structures.
4. **Empirical Outperformance**: The model outperforms existing methods, generating novel, stable structures that adhere to space group symmetry.
5. **Predictive Accuracy**: Despite limited input information, the model accurately predicts formation energy and band gap values comparable to DFT (Density Functional Theory) standards.

The model demonstrates superior performance in symmetry-conditioned generation, creating a diverse set of stable crystal structures that respect the underlying physical symmetries. This approach addresses limitations in prior methods, which struggled to produce symmetry-compliant structures, and shows promise for accelerating material discovery in fields requiring stable, symmetric crystals. However, the model inherits typical dataset limitations in generative models, as it learns distributions only within the scope of the training data, which may omit some stable but out-of-domain structures.

### Strengths
Strengths

1. Originality: The Wyckoff Transformer introduces a novel approach to crystal generation by utilizing Wyckoff positions to encode symmetries explicitly, making it unique among generative models. Unlike traditional methods, it avoids positional encoding and uses permutation-invariant tokenization tailored to space group symmetries, a creative and effective innovation for materials science.

2. Quality: The paper includes experimental results (although the results are not yet complete), showing the model’s success in generating symmetric crystal structures while achieving competitive accuracy in formation energy and band gap predictions. The evaluation is thorough, comparing the model’s performance to state-of-the-art methods across multiple metrics, demonstrating its robustness and effectiveness in real-world scenarios.

3. Significance: This work is impactful for both machine learning and materials science in general. By generating materials that are symmetric and physically plausible, the Wyckoff Transformer can accelerate material discovery for applications requiring stable, symmetric structures (e.g., in semiconductors and optoelectronics). The model’s potential for symmetry-conditioned generation highlights a promising direction for future research in material informatics and generative modeling.

### Weaknesses
1. > Empirically, our model outperforms baseline methods in generating novel diverse materials conditioned on space group symmetry (Line 138-139):

- The comparisons presented in various tables are not fair, do the other model condition the same way as your model does? If not then you're exposing data to the model as in the form of data-leak.

2. >  Our approach uses discrete Wyckoff space, and **fast** autoregressive sampling .. (Line 151)? 
- Are auto-regressive methods faster in general? (Any citation to support this). Nevertheless do you have any comparison result to make this claim? I do see table 6, but that doesn't include the auto-regressive generatio speed.

3. > **Fundamental problem** : 
- The inductive bias mentioned in line (178) limits the exploration space of materials. Henceforth, defeats the purpose of material generation. It will not be surprising to see this model beat coverage benchmarks of generated material.

4. > **Model architecture** :
- The model acrictectuer is still vague, inspite of asking it in my previous comment. The authors have made no effort towards this. (Line 233-235) How are you using the end neural network? Is it over the tokens? if so then how is the variable length of the token managed (Are you feeding neurons with [MASK] tokens), If so did you use any normalsiation to normalise the input of this network?
- Do you backpropogate through this network, or the loss also has an auto-regressive component? Usually the two are trained separatly , like BERT (MMLU) and followed by a top NN (trained with classical Loss function, L2 in case of supervised learning).

5. > **Conceptual error (model inference)** :
- What do you mean in line 245, I think authors have unclear understanding how language models work. It is true that the current token will e conditioned on all previous token, and one of the previous token being chemical element, site symmetry etc. But it's not the way to condition the model, it's actually being conditioned on a joint of all previous tokens rather than specifically on chemical elment token and so on. (Btw how many tokens are used to represent chemical element, site symmetry ... each)

6. > **Missing paragraph on interpretability of results**. 
- The paper doesn't seem to cover the interpretability aspect of their (a) Inductive bias, (b) Model architecture and (c) Loss function. The numbers are fine, maybe some are high some are low, but that's not just the point of writting a paper. You are expected to note why are you getting these numbers? I read lines 513-515 and 521 but that doesn't cover the result interpretibility. 

7. > **Repeated minor but unaceptable errors** : Looks like the authors did not go through the reviews. The following mistakes are unacceptable in any peer-reviewed paper, lest be it a top conference paper like ICLR.

1. Type and gramatical errors: obey play? (line 13), doesn't make sense to use multiple (5) 'and' in 1 sentence (line 15,16,17 ) , 'tother' (line 180)
2. Vague lines without citations: 
- Line 42-44 (did you discover this fact?), 
- Line 44 (230 distinct space groups) ? It's my general observation that the authors are a bit vague when they state facts, kindly read good papers and fundamentals of paper-writing, it will help a lot. 
- Line 74-76; You may get away with these lines if this was a material science journal, but unfortunately it isn't, thus you need to cite properly so that the readers get the context.
3. Figure 1 is still vague, I udnerstand that MP-20 has 98% non P1 symmetry, what does the ticks on x-axis mean? The color map seems to corrospond to symmetry groups (arange being P1) but why ticks and why does P-1 on the x-axis colored green?

### Questions
The following are my questions and suggestions for this paper:

1. The structure of the network, inputs, outputs and loss function (including tokeization, loss function computation needs to be defined properly with proper mathamtical notation and schematics). Kindly include a schematic diagram of their Wyckoff Transformer architecture, clearly showing how it differs from standard Transformer models. Additionally, kindly clarify how their model handles both de novo generation and property prediction tasks, possibly by explaining any additional layers or modifications to the base architecture.

2. How did the authors plot Figure 1? Kindly include other generated structures in Figure 2, it will be best to show how the generated structures also follow these symmetris and where do ther lie in terms of space group number. Kindly provide a clear caption explaining the source and construction of the figure. Kindly include a figure showing examples of structures generated by their model, possibly comparing them to real structures or those generated by baseline models. This would help demonstrate the model's capabilities and the effectiveness of their novel representation.

3. In section 2.2 clearly mention the assumtpions for your model, as of now the reviewer was not able to find the assumptions which the authors have taken. These need to be mentioned in a list.

4. What was the training objective, were they two different models for task of De novo genration and Property prediction? If so, then how were they both trained? (Objective funvtion, optimiser hyper-parameters, Input data, valdiation metrics, regularisers, hardware specifications etc.)

5. The algorithm explained for (i) Tokenization, (ii) De-nove generation, (iii) Structure genration and (iv) Metric computation is vaguely defined. These need to be defined propely in algorithm sections. As of now they don't make any sense and are without mathematical notation.

6. Which DFT calculation has been used in the paper? Did the authors perform DFT of their own or are using previously reported results, if yes, then it will still need to be described and also how are they reporting.

### Soundness
1

### Presentation
1

### Contribution
2
