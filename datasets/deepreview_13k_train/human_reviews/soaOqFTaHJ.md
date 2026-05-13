# EKAN: Equivariant Kolmogorov-Arnold Networks

- Decision: Reject
- Scores: 3, 5, 3, 5

## Abstract
Kolmogorov-Arnold Networks (KANs) have seen great success in scientific domains thanks to spline activation functions, becoming an alternative to Multi-Layer Perceptrons (MLPs). However, spline functions may not respect symmetry in tasks, which is crucial prior knowledge in machine learning. Previously, equivariant networks embed symmetry into their architectures, achieving better performance in specific applications. Among these, Equivariant Multi-Layer Perceptrons (EMLP) introduce arbitrary matrix group equivariance into MLPs, providing a general framework for constructing equivariant networks layer by layer. In this paper, we propose Equivariant Kolmogorov-Arnold Networks (EKAN), a method for incorporating matrix group equivariance into KANs, aiming to broaden their applicability to more fields. First, we construct gated spline basis functions, which form the EKAN layer together with equivariant linear weights. We then define a lift layer to align the input space of EKAN with the feature space of the dataset, thereby building the entire EKAN architecture. Compared with baseline models, EKAN achieves higher accuracy with smaller datasets or fewer parameters on symmetry-related tasks, such as particle scattering and the three-body problem, often reducing test MSE by several orders of magnitude. Even in non-symbolic formula scenarios, such as top quark tagging with three jet constituents, EKAN achieves comparable results with EMLP using only $26\\%$ of the parameters, while KANs do not outperform MLPs as expected.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper extends the general framework of Finzi et al to construct equivariant matrix group MLP of Finzi to KANs.

### Strengths
- This paper is an important contribution, both theoretically and technically. The framework of Finzi et al is relatively simply, i.e., it doesn't cover steerable or regular group convolutions, yet it is applicable across a wide range of groups. An extension to KANs makes a lot of sense in many ways.

### Weaknesses
 - The paper completely neglects any literature from 2021 onwards. This is a significant oversight, as the field has progressed rapidly, particularly in areas related to equivariant neural networks and their applications. The absence of engagement with recent advancements makes it difficult to assess the novelty and relevance of the proposed method.
- Comparisons to steerable methods are missing. This is of (theoretical) interest since EMLP / EKAN operate by linear combination of scaled subspaces, whereas steerable methods, such as those based on group convolutions, offer potentially greater representational power by directly operating on feature maps transformed under group actions. The paper does not address this fundamental difference in approach and its implications for performance and expressivity. A discussion of the trade-offs between these two approaches is crucial.
- The top quark tagging problem has seen substantial progress in the last 2 years with the introduction of novel architectures and training strategies. The paper's experimental results are presented in isolation, making it hard to judge their significance relative to the state-of-the-art. The lack of comparison to these specialized methods makes it difficult to understand the practical utility of the proposed approach in this domain.

### Questions
- I would strongly advise the authors to put some effort into the paper to update it with recent works and embed it in the literature. Furthermore, the experiments need some more meat. It is scientifically not ok to report one larger experiments (top tagging) where all previous efforts are left out. 
- In the current state this paper is thus not ready for conference publication, but with mentioned changes this is a valuable contribution.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Equivariant Kolmogorov-Arnold Networks (EKAN), an extension of Kolmogorov-Arnold Networks (KANs) to integrate matrix group equivariance, enhancing their effectiveness for symmetry-related tasks. While KANs have been valuable in scientific applications due to their spline activation functions, they lack built-in symmetry awareness. EKAN addresses this limitation by incorporating equivariant linear weights and gated spline basis functions to preserve symmetry within the architecture. A lift layer is introduced to align EKAN’s input with dataset feature spaces, enabling broader applicability. Experimental results demonstrate that EKAN achieves good accuracy on symmetry-sensitive tasks with fewer parameters and smaller datasets, outperforming traditional KANs and matching or exceeding the performance of Equivariant Multi-Layer Perceptrons (EMLP) on specific applications like particle scattering and top quark tagging, where EKAN reaches comparable results with significantly reduced parameters.

### Strengths
1. The proposed EKAN framework stands out as the first of its kind to embed matrix group equivariance directly into KAN architectures, expanding their potential application range and enhancing their utility in tasks where symmetry is crucial.
2. The numerical results are promising, particularly in scientific computing tasks with symmetry-related constraints.

### Weaknesses
1. The novelty and depth of this work appear somewhat limited, as the methodology seems relatively straightforward by extending existing techniques from MLP to EMLP (Finzi et al., 2021) to construct gated basis functions and equivariant linear weights. It would strengthen the paper if the authors provided deeper insights into the intrinsic challenges or unique aspects of building EKAN from KAN, beyond the application of existing equivariant techniques. Specifically, the paper lacks a detailed discussion on how the choice of group representation impacts the performance and stability of EKAN, and whether certain representations are more suitable for specific types of symmetry. Furthermore, the paper does not explore the potential limitations of using a single lift layer, especially when dealing with complex symmetries that might require multiple stages of lifting to capture the full equivariant structure. A more thorough analysis of these aspects would significantly enhance the contribution of the paper.
2. Certain numerical tests lack fair benchmarking. For instance, more variations in the width and depth of MLP and EMLP should be considered to ensure comparability. Additionally, the results in Table 3 suggest that the performance of EMLP or EKAN may depend on balancing model size with training set size. However, model sizes for (E)MLP and (E)KAN are not equivalent across tests. It would be helpful if the authors presented results for MLP and EMLP with model sizes under 50K, as well as for KAN and EKAN with sizes over 100K, to provide a more balanced and thorough comparison. More general, the authors could test all models with 3-4 different parameter counts ranging from 30K to 150K. The current experimental setup does not adequately explore the parameter space, making it difficult to draw definitive conclusions about the relative performance of EKAN compared to EMLP and other baselines. The paper should also include a more detailed analysis of the computational cost of EKAN, particularly in terms of training time and memory usage, compared to EMLP, especially as the model size increases.

### Questions
In addition to the points noted in the "Weaknesses" section, I have the following questions:

1. It is well noticed that any KAN can be exactly represented by an MLP, for example as demonstrated in Wang et al. (2024), “On the expressiveness and spectral bias of KANs” (arXiv:2410.01803). Given this, can we assert that EKAN can be directly derived from EMLP? Alternatively, does the construction presented in this work offer new insights into achieving equivariant properties within KANs?

2. In Theorem 1, does the function $f: U_{gi} \to U_m$ ensure that the entire KAN can precisely be equivariant from original input to output, as shown in Equation (5)?

3. Regarding the singular value decomposition (SVD) of $C$ to determine the projection operator onto the kernel space, as stated in Equation (22), is this process conducted offline and can it be performed in parallel and a priori? Additionally, during the training process, how is it ensured that $W_b$ remains within the kernel space? Is a projection applied after each SGD step?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Equivariant Kolmogorov-Arnold Networks (EKAN). EKAN bases KANs and incorporates matrix group equivariance into KANs. The idea to introduce the symmetry is to incorporate a gate architecture, which is also adopted to make MLP to be equivariant to the matrix group. The networks are evaluated in some classes of scientific discovery.

### Strengths
- The motivation of this paper is somewhat clear and the contribution of the work is posited in a right area. Incorporating symmetry into machine learning models is extensively studied in the scientific discovery domain.
- Having the figures of schematic such as figures 1 or 2 seems to be a good idea to help readers easily grasp an idea of the proposed method.

### Weaknesses
 **Theoretical part:** Main drawback of this paper is the ambiguous and unclear description of theoretical parts, which makes it very hard to follow the paper. The main cause I feel is that the distinction of the definition and property is not clear and/or some mathematical terminologies are not introduced properly. The followings are the umbiguous/unclear, but not exhaustive, parts of the paper:

**Section 3**
- The sentence starting ‘In general’ in line 139 is neither trivial nor understandable. What is the assumption on "the" vector space $U$ and how is it associated with the matrix group? Specifically, is $U$ a representation space of the matrix group, and if so, what is the specific representation? The paper lacks a clear definition of the relationship between the vector space and the group action, making it difficult to understand the subsequent constructions.

**Section 4** 
- Assuming the definition of (10), for example, $T(-1, -1)$ is also allowed -- What does this notation mean? Does this imply a direct product structure, and if so, how does this relate to the group action? The notation is not standard and requires more explanation.

- As I mentioned above, how the decomposition (10) is associated to the matrix group is unclear, so I do not see how this expression helps the later discussion. The connection between the decomposition and the group representation is not explicitly stated, making it hard to see how this decomposition leads to equivariance.

- Descriptions of lines 253-256 are very vague. For example, why is the input/output feature does not lie with in $U_{I}/U_{o}$? What is the necessity of “align with gated basis functions?” Why does adding a gate scalar help to obtain the actual input/output space? The expression $U_{I}/U_{o}$ is also extremely misleading, as this could also mean the quotient space of $U_{I}$. The paper needs to clarify whether $U_I$ and $U_O$ are representation spaces, and if so, what are the specific representations. The use of the term $U_I/U_O$ is confusing and needs to be defined precisely.

- Section 4.2 is very hard to follow. For example, lines 280-284 are very difficult to understand. ‘’For the non-scalar term $v_{I, a}$, we apply the basis functions …$ I do not see any mathematical formulation for this, and it is hard to see whether this is the definition or the property derived from some equations. Line 281, “For the scalar term, …, which is equivalent to applying basis functions element-wise.” This description also does not make sense, since I do not think two mathematical terms which are supposed to be equivalent are not introduced already. The paper needs to provide the mathematical formulation for the basis function application, and clarify the equivalence between the scalar term operation and element-wise application.

- While the paper reads “$U_{m}$ can be written as …”at line 284, I do not know the original definition of $U_{m}$, and I am not sure if the equations (13, 14) hold. I could not check the validity of the proof of Theorem 1. The definition of $U_m$ needs to be stated clearly before introducing its decomposition. The proof of Theorem 1 needs to be more detailed and include the necessary steps to verify its validity.

- Unfortunately, I cannot follow the rest of the theoretical claims due to the lack of my understanding for the above questions.

Another question for the motivation of the paper is that: Why don't we use frame averaging for KAN model, but rather put hard equivariance to existing KAN model?

**Experiment part:** I also have some concerns on the setting of experiments.
- N-body simulations is a relatively small, while representative, physical system among other types of scientific simulations. The number of parameters for MLP and EMLP is relatively high compared to EKAN, and I suspect that this advantage might come from the difference in the number parameters. Would it be possible to change the number of parameters/layers of MLP/EMLP/EKAN to see how the number of parameters have an impact on the test accuracy? A more controlled experiment with varying parameter counts is needed to isolate the effect of equivariance from the effect of model size.
- I think the choice of baselines is not exhaustive. For example, Steerable E(3)-GNN [1] can be applied to N-body experiments and Top Quark Tagging. Also, Clifford Group Equivariant Neural Networks [2] could be another strong baseline. While I understand that the focus is rather on the side of comparison to (E)MLP, I still think the authors should at least mention other baselines (and hopefully include those baselines in the experiments) since all the scenarios in the experiments are in scientific domain and those models are shown to be very effective to solve tasks in (some of) those experiments.

Overall, I feel the paper needs profound revision in the writing, so the paper is more self-contained and readers could follow the main idea of the paper much more comfortably.

**Typo**
- Line 814, Adan optimizer

### Questions
See above.

### Soundness
2

### Presentation
1

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
This paper introduces a new class of equivariant KAN networks, utilizing gating mechanisms and constraining linear weights to satisfy group equivariance. Specifically, the authors apply SVD decomposition to linear weight matrices to identify their null spaces, drawing inspiration from EMLP, and use gating to scale n-rank vectors in an equivariant manner. Experimental results demonstrate that EKAN achieves superior performance over EMLP on several tasks.

### Strengths
1. The paper proposed a new class of equivariant networks based on Kolmogorov-Arnold Networks that can be applied to various scientific problems. 
2. Even though neither equivariant linear weights nor KAN or gating mechanism are new, authors managed to connect them together and provide a new set of tools in equivariance research.
3. Most of experimental results presented in the paper show that EKAN has a clear outperformance over EMLP.

### Weaknesses
1. The technical contributions presented in the paper lack novelty, as the core techniques have been previously explored in the literature. Specifically, the use of SVD for identifying null spaces in linear layers, while effective, is not a new concept, and the application of gating mechanisms for equivariant scaling has also been explored in other contexts. The paper does not sufficiently highlight what unique combination or adaptation of these existing techniques leads to a significant advancement.
2. Although EKAN is compared against MLP, KAN, and EMLP, the effectiveness of the model could be further validated by including comparisons with more recent equivariant architectures, such as those based on tensor field networks or other advanced geometric deep learning models. This is particularly important given the rapid progress in the field. Furthermore, the experiments lack a detailed analysis of the performance across different group representations, which could reveal the strengths and limitations of EKAN in various scenarios. The current comparisons do not fully establish the superiority of EKAN over state-of-the-art equivariant methods.
3. A discussion on the efficiency of the KAN-based model would be valuable, particularly for application-oriented readers. Given the current trend where researchers may prioritize data-driven approaches over constraining models with equivariant functions, such a comparison could highlight EKAN's practical utility. The paper should include a more detailed analysis of the computational cost of EKAN, including the number of parameters, training time, and inference time, and compare these metrics with other equivariant models. This analysis is crucial to understand the trade-offs between performance and efficiency.

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
2
