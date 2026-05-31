## Human Reviewer 1

### Summary
The paper hypothesizes that effective time-series forecasting requires models that can learn underlying time series dynamics and introduces the PRO-DYN framework to analyze this.

### Strengths
- This paper tackles an interesting and important question: whether time-series models can effectively learn temporal dynamics and presents a novel framework to try to analyze this.
- The authors’ decision to open-source their code in the supplemental material is commendable.

### Weaknesses
Overall, the paper is convoluted and difficult to parse, with sections that could benefit from improved organization and figure clarity. The arguments supporting the main hypothesis are not entirely convincing and could be strengthened with more formal theoretical formulations. Specific points are detailed below.
- Lines 122–125: The discussion of dynamical systems is very brief, limited to just two sentences, and the treatment of time-series dynamics is insufficient. A more thorough discussion is warranted, given that dynamics are central to the paper’s focus.
- Lines 56–57: The statement, “We thus hypothesize that TSF models should be able to learn time-series dynamics,” is insufficiently supported by the preceding text. The authors should clarify whether they mean that a “good” TSF model should learn time-series dynamics and explicitly define what is meant by this term before stating the hypothesis.
- Line 72: The paper references iTransformer, PatchTST, and Crossformer as “SOTA foundation models,” but these are not true TSFMs. TSFMs are typically pretrained on large-scale, cross-domain time-series datasets (e.g., Moment, Chronos, TinyTimeMixers, Moirai, LagLlama). While PatchTST is reasonable as a strong baseline, other cited models are not representative of SOTA time-series forecasting. It is also worth noting that simpler models, such as DLinear, have outperformed some transformer variants in long-term forecasting.
- Lines 72 and 97: References to a “linear dynamics layer” or “linear functions” are too broad. For instance, PatchTST uses a linear layer to project patched time-series tokens. The authors should clarify how their proposed linear layer differs from such projection layers.
- Line 72: The placement of the dynamic linear layer seems inconsistent across architectures (e.g., after the encoder in Informer versus first in FiLM, according to Fig. 2). The rationale behind these placement choices should be explicitly explained.
- Line 203: The claim that “LSTF-Linear models do have learnable dynamics modeling capabilities” is not well-supported with evidence.
- Figure 1: The meaning of the pink and white rectangular boxes is unclear, as are the outputs from the functions $f_\theta$., which are represented as non-annotated empty boxes. If the final output represents a forecast, it should be denoted as $\hat{y}$ instead of $y$.
- Table 1: It is unclear what “better than NLinear” refers to and why NLinear was chosen as the reference. The rationale should be explicitly stated, particularly if the claim relates to the LSTF-Linear models’ learnable dynamics.
- Evaluation (lines 353–355): The evaluation method is unconventional and non-intuitive: “We count the number of cases where the modified models are better, equal (iso), worse by at most 1% (low degradation), or worse by at least 1%, than their vanilla version.” A more standard and interpretable approach would be to report percent changes in error metrics across datasets between the original (vanilla) and modified models, ideally in a table.

Other:
- The abbreviation “LSTF” is not defined. It appears to refer to long-term time-series forecasting, but this should be explicitly stated.

### Questions
1. Have the experiments been repeated across multiple random seeds with metric results reported as averages?

### Soundness
1

### Presentation
1

### Contribution
1

### Rating
0

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper analyzes existing time-series forecasting (TSF) models, aiming to address why simple linear models often outperform complex deep learning models in this domain. The authors posit that TSF tasks necessitate models capable of learning the underlying dynamics of the data. To investigate this, a "PRO-DYN" nomenclature is introduced, decomposing models into processing (PRO) and dynamics (DYN) units . Two primary insights emerge from this analysis: 1) Models underperforming relative to linear counterparts often lack a DYN module or possess only a partially learnable one; 2) The positioning of the DYN module within the model architecture is crucial, with placement at the terminal end generally yielding optimal performance. Extensive experiments are conducted to substantiate these claims .

### Strengths
1. The paper introduces an original and insightful PRO-DYN nomenclature for deconstructing TSF models. This framework is effectively utilized to rationalize the "anomalous" effectiveness of current LSTF-Linear models and formulate two key observations regarding the role and placement of dynamics modules.
2. The authors provide substantial empirical evidence through extensive experiments to validate the proposed insights concerning the importance of the DYN module and its architectural positioning for model performance .

### Weaknesses
1. The paper's analysis of dynamics relies almost exclusively on adding or relocating a linear DYN layer to represent the temporal space transformation. While sufficient to demonstrate that incorporating some dynamics is superior to its absence (e.g., 0-padding in Informer ), it lacks the evidence to generalize this finding to the claim that "dynamics," specifically linear dynamics, is the optimal or necessary form.
2. The work primarily focuses on evaluating the importance of the dynamics module, offering valuable guidance, but the actual technical innovation presented is limited .
3. The exposition suffers from clarity issues. The formal definition of the TSF task is arguably over-complicated , yet the explanation of core concepts and arguments lacks sufficient mathematical formalization, relying instead on potentially ambiguous verbal descriptions, thereby increasing the difficulty of comprehension .

### Questions
1. The paper fails to provide a detailed explication of the crucial concept of "dynamics." While lines 343-344 draw an analogy to physics ("dynamics matrix," "external force"), the correspondence is not elaborated upon . How exactly these terms map to physical dynamics and why this analogy explains the performance of LSTF-Linear models remains unclear.
2. The primary empirical support rests on Figures 4 and 5. However, in the upper panel of Figure 5, the advantage of DYN added models over PRO added models is not consistently evident, particularly for the FiLM model. This suggests that the performance gains observed for FiLM in Figure 4 might stem largely from increased parameter count rather than the dynamics aspect itself , thus providing insufficient support for RQ1.
3. Figure 2 illustrates varied designs for implementing the DYN added modifications across different models (e.g., replacing 0-padding vs. adding at the entry) . Does a unified principle or rationale underpin these differing design choices, or are they ad-hoc modifications?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper bring in a nomenclature for time series forecasting (TSF) methods and comes up with interesting hypothesis such as "under-performing architectures learn dynamics at most partially" and "the location of the dynamics block at the model end matters", thus justifying the importance of the title, dynamics is very important for TSF. Their experiments show that adding dynamics learning blocks to a normal model enhances it's performance on TSF.

### Strengths
- The idea of bringing in nomenclature to TSF methods is good. As noted by the authors, TSF methods are somehow a bit different compared with mainstream LLMs but they might not be, and such discussion will help researchers understand if any differences exist.
- The research questions are well motivated and the experiments have answered them to good detail.

### Weaknesses
**Expanding nomenclature**: The nomenclature inclusion of TSF methods which incorporate some sort of dynamical systems is missing in Table 1. I’ve seen the authors cite Attraos [1], but they didn’t include it in Table 1. In addition to that, please add other latest dynamical-based TSF methods such as DeepEDM [2], Koopa [3], KNF [4] to your Table 1. In case a method can’t be nomenclature using PRO-DYN, the authors should explicitly mention the limitations associated with it on why it's not possible.

**Inclusion of dynamical-based TSF methods in experiments**: Following previous point on nomenclature expansion, pick one/few dynamical-based TSF methods and supplement the experiments. A potential RQ3 that I am interested is something like the following — Whether Informer-DYN will be better than already built-in dynamical-based TSF method i.e if adding DYN block to a normal baseline will make the model better compared with already built-in dynamical-based TSF methods. This sort of expands RQ1. Specifically, it's interesting to know the tradeoffs associated. Feel free to make certain choices to speed up experimentation and compute limitations. Eg: Picking up latest models might be enough to compare against. 

1. Attraos (NeurIPS 2024) - https://openreview.net/forum?id=fEYHZzN7kX  
2. DeepEDM (ICML 2025) - https://openreview.net/forum?id=LLk1qYQatJ
3. Koopa (NeurIPS 2023) - https://openreview.net/forum?id=A4zzxu82a7 
4. KNF (ICLR 2023) - https://openreview.net/forum?id=kUmdmHxK5N

### Questions
I personally felt the presentation can be made much better.

- Figure 1 can be made much better. I had a hard time understanding the flow of information.
- The mathematical notations can be simplified further. Consider adding a Glossary of notations. 
- Table 13, 14, 15 - The presentation can be much better. Use sub columns/subrows to represent complex tables.

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Summary
The paper “Dynamics Is What You Need for Time-Series Forecasting!” argues that the key to improving time-series forecasting (TSF) is not architectural complexity but explicitly learning underlying dynamics. The paper introduces the PRO-DYN framework, which decomposes models into processing (PRO) functions that operate within the same time interval and dynamics (DYN) functions that map past to future. Analyzing many TSF architectures, they find that top-performing models share two traits: a fully learnable dynamics block and its placement at the model’s end.

### Strengths
The paper offers an interesting and conceptually unifying perspective on time-series forecasting (TSF) by reframing existing architectures through the lens of dynamics learning. The proposed PRO-DYN framework provides a clear and intuitive decomposition of model components into processing and dynamics functions, which helps explain why certain architectures perform better. The empirical results are broad and consistent across multiple benchmarks. The work is well-organized, and its emphasis on the role of dynamics could inspire future studies that bridge traditional dynamical systems theory with modern deep learning approaches.

### Weaknesses
While the conceptual framing is novel, the paper lacks depth in both theoretical and empirical validation of what it calls “dynamics.” The introduced DYN block is essentially a simple temporal linear or MLP layer, and no evidence is provided that it actually learns or represents true system dynamics. The analysis remains largely phenomenological rather than mechanistic. Moreover, the paper does not evaluate or compare against existing dynamics-based models such as Koopman, Neural ODEs, PINNs, or state-space models, that explicitly learn or approximate underlying temporal evolution laws.  Dynamics is the main focus of the paper, so naturally, one would expect a more detailed discussion on work in that domain as well as some baselines in the main results. Some representative works include:

- Lusch, B., Deep learning for universal linear embeddings of nonlinear dynamics. Nat Commun 9, 4950 (2018). 
- Liu, Y., et al. Koopa: Learning non-stationary time series dynamics with Koopman predictors. NeurIPS 2023.
- Hu, Jiaxi, et al. Attractor memory for long-term time series forecasting: A chaos perspective. NeurIPS  2024: 20786-20818.
- Majeedi, A., et al. LETS Forecast: Learning embedology for time series forecasting. ICML 2025. 

Finally, to convincingly support the claim that “dynamics is what you need,” the paper should have included experiments on synthetic or controlled dynamical systems, where the true underlying evolution laws are known. Such settings would allow testing whether the proposed DYN block can actually learn or approximate genuine system dynamics, rather than merely fitting temporal statistical correlations in real-world data. Instead, the experiments are limited to standard benchmark datasets, which, while diverse, do not provide ground truth about underlying dynamics, making it difficult to validate the central hypothesis in a rigorous way.

Furthermore some of the claims are confusing, for instance, iTransformer, by inverting the inputs, essentially applies a temporal MLP which is equivalent to the DYN layer. Further more, DLinear also relies on a temporal linear layer, does that mean DLinear learns all the dynamics? More clarification on these would greatly strengthen the support for the claims in the paper.

### Questions
1) How do we know that the DYN block is learning any dynamics? 
2) Why are none of the Dynamics based models compared in the experiments? For instance to test if adding the DYN block helps in those cases or not.
3) More discussion on the related work in the dynamics space would greatly improve the context of this work.
4) Some more clarity on the scope and claims would be helpful.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
5