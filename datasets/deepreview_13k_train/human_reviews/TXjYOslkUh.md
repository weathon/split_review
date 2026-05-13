# Distribution Shift Aware Neural Feature Transformation

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
Feature transformation, as a core task of Data-centric AI (DCAI), aims to improve the original feature set to enhance AI capabilities. In dynamic real-world environments, where there exists a distribution shift, feature knowledge may not be transferable between data. This matter prompts a distribution shift feature transformation (DSFT) problem. Prior research works for feature transformation either depend on domain expertise, rely on a linear assumption, prove inefficient for large feature spaces, or demonstrate vulnerability to imperfect data. Furthermore, existing techniques for addressing the distribution shift cannot be directly applied to discrete search problems. DSFT presents two primary challenges: 1) How can we reformulate and solve feature transformation as a learning problem? and 2) What mechanisms can integrate shift awareness into such a learning paradigm? To tackle these challenges, we leverage a unique Shift-aware Representation-Generation Perspective. To formulate a learning scheme, we construct a representation-generation framework: 1) representation step: encoding transformed feature sets into embedding vectors; 2) generation step: pinpointing the best embedding and decoding as a transformed feature set. To mitigate the issue of distribution shift, we propose three mechanisms: 1) shift-resistant representation, where embedding dimension decorrelation and sample reweighing are integrated to extract the true representation that contains invariant information under distribution shift; 2) flatness-aware generation, where several suboptimal embeddings along the optimization trajectory are averaged to obtain a robust optimal embedding, proving effective for diverse distribution; and 3) shift-aligned pre and post-processing, where normalizing and denormalizing align and recover distribution gaps between training and testing data. Ultimately, extensive experiments are conducted to indicate the effectiveness, robustness, and trackability of our proposed framework.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies feature transformation problem within the context of distributional shift in real-world scenarios. It introduces a Shift-aware Representation-Generation Perspective, which involves encoding transformed features into embedding vectors and decoding the optimal embedding. To address distributional shift, the paper proposes several techniques, including shift-resistant representation, flatness-aware generation, and shift-aligned pre- and post-processing. The effectiveness of these methods is evaluated through experiments on classification and regression tasks.

### Strengths
-	This paper addresses the important problem of feature transformation under distributional shift, a crucial challenge in deploying large foundation models in practical settings nowadays.
-	The paper introduces a comprehensive pipeline for feature transformation, including data collection, feature graph embedding, transformation, and pre-/post-processing stages.
-	Extensive experimental validation is provided, covering classification and regression on multiple datasets, ablation studies, and robustness analyses

### Weaknesses
-	The contribution of this paper appears somewhat ad hoc, as it incorporates a variety of techniques such as RL-based data collection, shift-resistant feature graph embedding, flatness-aware transformation, and shift-aligned pre-/post-processing without clearly explaining the motivation behind each component. The paper lacks a cohesive narrative that justifies the necessity of each component in the overall framework. For instance, the specific type of RL algorithm used for data collection and its impact on the final feature transformation is not well-motivated. Also, the connection between shift-resistant embedding and flatness-aware transformation is not clearly established, making it difficult to assess the importance of each component.
-	Several of the techniques used, particularly flatness-aware methods for addressing distributional shift, have been widely studied. The integration of these methods offers only incremental technical contributions. While the paper combines these techniques, it does not provide a novel theoretical insight or a significant advancement in the existing methodologies. The paper should more clearly articulate the novelty of their specific combination of techniques, and why it provides a substantial improvement over existing methods.
-	The experiments are primarily conducted on small-scale datasets, raising concerns about the scalability and generalizability of the proposed approach to large-scale pretraining datasets nowadays. The paper does not provide sufficient evidence that the proposed approach can handle the complexity and scale of modern datasets. The experiments lack the scale to demonstrate the practical applicability of the proposed approach in real-world scenarios. Additionally, the computational cost of the proposed method, especially the RL-based data collection and graph embedding, is not thoroughly evaluated, which is important for scalability.
-	The selection of baseline models for comparison appears outdated, as most were published prior to 2020, potentially limiting the relevance of the comparisons. The paper needs to compare against more recent and state-of-the-art methods to demonstrate the effectiveness of their proposed approach. The current baselines do not provide a strong benchmark to assess the true performance of the proposed method in the context of recent advances in feature transformation.
-	The paper's organization and clarity could be improved; for instance, the introduction contains redundant and hard-to-follow contexts that hinder readability. The introduction needs to be more concise and focused on the core problem and the proposed solution. The current organization makes it difficult for the reader to grasp the central ideas of the paper. The logical flow of the paper needs to be improved to enhance readability and understanding.
-	The mathematical presentation is unsatisfactory; for example, providing a formal mathematical formulation for DSFT would enhance clarity over the current textual description. The provided formulation is very high-level and lacks the necessary details to understand the technical implementation. The paper should provide a more rigorous mathematical formulation, including the specific algorithms used for each component.
-	Some notations are introduced before being defined, such as $f_1$, $f_2$.

### Questions
please refer to the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Existing techniques for addressing the distribution shift cannot be directly applied to discrete search problems and present two primary challenges: (1) How can we reformulate and solve feature transformation as a learning problem? What mechanisms can integrate shift awareness into such a learning paradigm? To tackle these challenges, the authors leverage a unique Shift-aware Representation-Generation Perspective. To formulate a learning scheme, they construct a representation-generation framework: (1) representation step: encoding transformed feature sets into embedding vectors (2) generation step: pinpointing the best embedding and decoding as a transformed feature set. To mitigate the issue of distribution shift, they propose three mechanisms: (1) shift-resistant representation, where embedding dimension decorrelation and sample reweighting are integrated to extract the true representation that contains invariant information under distribution shift; (2) flatness-aware generation, where several suboptimal embeddings along the optimization trajectory are averaged to obtain a robust optimal embedding, providing effective for diverse distribution, and (3) shift-aligned pre and post-processing, where normalizing align and recover distribution gaps between training and testing data.

### Strengths
This paper addresses an interesting question: How do we transform features when there is a distribution shift?

### Weaknesses
 - The formulation of the discrete search problem into a deep learning problem is similar to [Reinforcement-enhanced autoregressive feature transformation: Gradient-steered search in continuous space for postfix expressions].
- The novelty of the methodology is limited. Is the representation step specially designed for encoding feature transformation problems?
- Although considering the feature sets as a feature-feature interaction attributed graph is novel, the motivation behind it is not well explained. Why can the feature sets be considered a graph? Is it reasonable?
- Limited empirical validation. The authors only used 16 datasets for evaluation. However, as the baseline outlined in the paper [Reinforcement-enhanced autoregressive feature transformation: Gradient-steered search in continuous space for postfix expressions], there are 23 datasets that have been evaluated.

### Questions
See Weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper deals with the Neural Feature Transformation problem in the context of distribution shift, i.e., Distribution Shift Feature Transformation (DSFT) problem.   

Specifically, it follows a representation-generation framework similar to (Wang et al., 2023), involving a representation step and a generation step. Moreover, three mechanisms are designed to deal with the DSFT problems: shift-resistant representation, flatness-awareness generation, and shift-aligned pre and post-processing.   

During training, Shift-resistant Bilevel traning is proposed, and flatness-aware gradient ascent is incorporated. 

Experiments are conducted on UCI and OpenML datasets with Kolmogorov-Smirnov to construct the distribution shifted data splits. Comparisons and ablations are conducted.

### Strengths
### Problem 
- This paper addresses the Distribution Shifted Feature Transformation (DSFT) problem, which is relatively new and overall makes sense. 
### Methodology & Ablation of Modules
- Specific techniques are designed to combat shifts in a representation-generation framework (Wang et al., 2023): bilevel training of samole weights and model parameters, flatness-aware gradien ascent.   
The ablation in Figure 4 shows the effectiveness. 
### Experiments 
- Experiments are conducted on 16 benchmark datasets from UCI and OpenML. The proposed method outperforms SOTA in most settings.

### Weaknesses
### Organization and writing
- Overall, the main idea is easy to grasp. While the technical details, modules, and work flows are not quite easy to follow. For example, Algorithm 1 use full paragraph texts instead of algorithm-style to explain the framework. 
- From line 627-632, the MOAT paper: Reinforcement-enhanced autoregressive feature transformation: Gradient-steered search in con-
tinuous space for postfix expression, appears twice. In line 294 argmin. 
### Methodology
- While distribution shift problem is relatively novel, the main framework follows MOAT (Wang et al., 2023), see Figure 2 of MOAT. This is neither stated nor discussed in the paper. This is kind of misleading or overclaiming the contributions. A better practice is to explicitly clarify how the framework differes from MOAT, and the contributions to distribution shift. 
- The RL pipeline for data preparation, $L_{rec}, L_{est}$ follow MOAT. Or any changes? 
- New modules in Eq. (1) is straightforward with several existing work such as [R1]. The utilization for distribution shift and re-weighting is reasonable, but the overall technical contribution is not significant in this point. 
- Flatness-aware gradient ascent is motivated from existing works (Izmailov et al., 2018; Garipov et al., 2018). According to Algorithm 3, it seems a simple technique. 
### Experiments
- The SOTA baseline MOAT is experimented on 23 datasets, while this paper only on 16. Can you provide a justification why only 16 datasets are experimented or include more results for comprehensive comparison.

### Questions
- What are the main differences of the proposed method and MOAT? And how these differences address the Distribution Shift? 
- MOAT experimented on 23 datasets, while this paper only 16. Why the other benchmarks are not reported?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a feature transformation technique to improve the AI capability from Shift-aware Representation-Generation perspective. And three mechanisms are proposed to address distribution shift by shift-resistant feature set representation, flatness-aware generation, and integration of normalization. Extensive experiments have been conducted on classification and regression tasks.

### Strengths
1. This paper is well presented and easy to understand.
2. This paper addresses an interesting topic, feature transformation is crucial to improve the performance of the model.

### Weaknesses
1. The contribution point 1 is not clear enough. The embedded-optimization-reconstruction framework was proposed in baseline method [1].  The distinction with baseline methods needs to be made clear in the motivation section. Specifically, the paper needs to articulate the limitations of the existing framework [1] when applied to distribution shift scenarios, and how the proposed method overcomes these limitations. It is not sufficient to simply state an improvement; the mechanism of improvement must be clearly explained.
2. The experimental results are questionable. In Table 1, some experimental results are not consistent with the results reported in [1], and are significantly lower than the reported results. For example, Higgs Boston, please give a reasonable explanation.  In addition, compared with the baseline method, there are still some results on other datasets not shown. The paper should provide a detailed analysis of why the results differ, including a discussion of any differences in data preprocessing, hyperparameter settings, or evaluation protocols. The absence of results on other datasets mentioned in [1] raises concerns about the generalizability of the proposed method.
3. Ablation experiments. Three mechanisms proposed in the method, it is suggested to provide ablation experiments of these three mechanisms in the ablation experiments section. The ablation study should not only demonstrate the effectiveness of each component but also analyze the interaction effects between them. For instance, how does the performance change when flatness-aware generation is used without shift-resistant feature representation, or when normalization is applied in isolation?

### Questions
The main questions are in weaknesses 1 to 3.

### Soundness
3

### Presentation
3

### Contribution
2
