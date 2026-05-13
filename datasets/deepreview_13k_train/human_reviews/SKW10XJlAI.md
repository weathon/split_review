# Towards Understanding Text Hallucination of Diffusion Models via Local Generation Bias

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
Score-based diffusion models have achieved incredible performance in generating realistic images, audio, and video data. While these models produce high-quality samples with impressive details, they often introduce unrealistic artifacts, such as distorted fingers or hallucinated texts with no meaning. This paper focuses on textual hallucinations, where diffusion models correctly generate individual symbols but assemble them in a nonsensical manner. Through experimental probing, we consistently observe that such phenomenon is attributed it to the network's local generation bias. Denoising networks tend to produce outputs that rely heavily on highly correlated local regions, particularly when different dimensions of the data distribution are nearly pairwise independent. This behavior leads to a generation process that decomposes the global distribution into separate, independent distributions for each symbol, ultimately failing to capture the global structure, including underlying grammar. Intriguingly, this bias persists across various denoising network architectures including MLP and transformers which have the structure to model global dependency. These findings also provide insights into understanding other types of hallucinations, extending beyond text, as a result of implicit biases in the denoising models. Additionally, we theoretically analyze the training dynamics for a specific case involving a two-layer MLP learning parity points on a hypercube, offering an explanation of its underlying mechanism.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the local generation bias phenomenon in diffusion models and its relationship to text hallucination. The authors propose the Local Dependency Ratio (LDR) metric to provide empirical insights into this bias and present theoretical analysis attempting to explain the underlying causes of hallucinations.

### Strengths
The paper offers a novel perspective on diffusion model hallucinations through the lens of local dependency analysis.
The introduction of the Local Dependency Ratio (LDR) metric, along with the Quarter MNIST dataset, provides a useful probe for evaluating models' ability to consider global information versus local information.

### Weaknesses
- The central claim about hallucinations stemming from training dynamics rather than architectural limitations lacks substantial support:
  - No proposed training paradigm to demonstrate improvement.
  - Recent work (Stable Diffusion 3 [1]) achieves significant typography improvements through architectural changes (MMDiT)
- Regarding the experiments in section 4.2, it is possible that the network capacity might be insufficient to learn global relations. There should be more details on the model architecture. (It is claimed that the details of the model architecture are in the appendix, but they don't.) Specifically, the number of parameters and the depth of the network are not provided, making it difficult to assess if the model is capable of capturing the necessary long-range dependencies.
- In addition to the previous point, the DiT model seems to be able to memorize the training samples very well. The model does not need to learn the true latent relation ($s_1 + s_2 = s_3 + s_4$) if it can simply memorize all training samples. This mitigates the validity of the claim that diffusion models cannot learn the global relation. The authors should provide evidence that the model is not simply memorizing the training data, perhaps by testing on held-out examples that require generalization beyond the training set.
- The description "both have even numbers" about the Parity Parenthesis dataset seems incorrect. The claim "random guess has 50% chance of satisfying parity requirement" seems questionable. The parity condition as described is not clear, and the authors should provide a more precise definition of the parity constraint and a justification for the 50% random guess claim. It is unclear if the parity is defined over the sum or product of the tokens, and this ambiguity undermines the analysis.
- The authors attempt to theoretically prove that neural networks are prone to learning the marginal distributions instead of the global correlations by analyzing a two-layer MLP. However, the analysis may not generalize to U-Net or Transformer-based diffusion models. The DiT model is able to memorize Quarter MNIST training samples, demonstrating its capability of learning more than the marginal distributions. The theoretical analysis should be extended to architectures more relevant to diffusion models, or at least acknowledge the limitations of the current analysis.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper examines the issue of textual hallucinations in score-based diffusion models. The authors identify this phenomenon as stemming from a local generation bias, where the denoising networks rely heavily on highly correlated local regions of input data, leading to a failure in capturing the global structure. The paper proposes the Local Dependency Ratio (LDR) as a new metric to quantify this bias, demonstrating its persistence throughout training and across various network architectures. The findings suggest that the hallucinations are a result of the training dynamics rather than limitations in the model's architecture

### Strengths
1.This paper proposes a new metric for measuring text hallucinations.The introduction of Local Generation Bias and the Local Dependency Ratio (LDR) provides a new perspective on understanding hallucinations in diffusion models.
2.The paper features a rigorous derivation process, and its logic is sound and clearly structured.

### Weaknesses
1. Some of the core arguments are not well articulated:
The paper suggests that the causes of hallucinations stem from fundamental training dynamics rather than architectural limitations. However, the comparative experiments in Figure 4 only demonstrate that different model architectures exhibit hallucinations, it does not completely decouple architectural influences
2. Insufficient experiments: The article conducts comparative experiments under two different experimental settings on only two datasets. Including more validation experiments would enhance the reliability of the paper.

### Questions
1. I am trying to find some arguments to support the thesis in the paper that 'the causes of hallucinations stem from fundamental training dynamics rather than architectural limitations' , But I haven't found any direct relevant evidence. Could you please provide stronger evidence to support this point? Perhaps I miss some key information.
2. The experimental content included in the paper is still somewhat lacking. Could you provide experiments on more datasets (or more models) to demonstrate the generalizability of the method?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper performs a structured and theoretically motivated investigation of hallucination in text generation with diffusion models.
The authors construct two toy problems, parity parenthese and quarter MNIST, to investigate the phenomenon. The empirical evaluation along training steps and different generative architectures reveals that DMs fail to learn complex rules governing symbol distributions without access to strong priors. Using the proposed Local Dependency Ration (LDR) the authors demonstrate that symbols are generated with mainly localized attention, despite architecture design allowing for the capture of global structure. 
The authors further underpin these empirical observations by providing theoretical proof that the DM training paradigm can get stuck at a local saddle set, which forces the model to learn marginal, localized distributions.

### Strengths
- **Key problem from a new perspective.** In investigating text generation with diffusion models, the authors work on a core problem in the field with high relevance. The more theoretical approach chosen by the paper offers a novel perspective and interesting insights. 
- **Solid evaluation**. The authors construct two suitable proxy tasks for their analysis on which they perform compelling evaluations across training steps and architectures. 
- **Novel probing tool.** The proposed LDR metric is an interesting approach that could potentially benefit other fields and aid future interpretability research

### Weaknesses
 - **Generalization to current models**. While the paper does perform valuable evaluations and theoretical analysis on a constrained problem set, it fails to analyze strong, general-purpose models. Recent models like SD3, Flux, Playgroundv3, SD3.5, or Recraftv3 have become progressively better at text generation. At least if the text to be generated is supplied in the model prompt. Since many of these models' weights are openly accessible, it would be key for the paper's evaluation to investigate them using the proposed LDR metric. Specifically, insights into whether these models leverage more global structure or if improvements are tied to the strong priors of text conditioning 
- **Readability.** In the same vein, the theoretical sections of the paper may be hard to follow for some readers, although the actual problems, like the proposed Quarter MNIST, are intuitive and easy to understand. The paper would benefit from interleaving some more plastic examples into the methodological definitions and theoretical analyses to appeal to a broader audience. 
- **Lack of derived recommendations/future work.** The authors outline multiple issues in DMs that lead to hallucinations in text generation. Despite numerous insights, the paper does not come up with approaches or recommendations that would allow future work to address the same issues. 



### Questions
- **Q1** When comparing UNet and DiT architectures, do the authors ensure equal parameter count? Otherwise, the difference in performance could be attributed to an increased capacity in favor of the DiT.
- **Q2** Could the authors further elaborate on the difference across timesteps in Fig. 5. First, could the authors clarify if in their notation the generative/reverse diffusion process goes from $T \rightarrow 0$. I.e. higher values of $t$ correspond to earlier/more noise steps in the denoising process. If that is the case, the results are somewhat counter-indicative to prior observations of diffusion models. It seems to be the current consensus that earlier steps generate larger/global image aspects with later steps refining localized features. 
- **Q3** Following up on Q2, do the authors have an intuition/explanation why the UNet seems to have a clear progression over timesteps from between more global and local attention, whereas the DiT does not exhibit such a seperation?
- **Q4** Is the x-axis in Figure 5 the same as in Figure 4 as is implied in the main body? If so, why are the axes over the 2 Figures not aligned? It would make it easier for the reader to identify correlations in LDR with downstream performance.

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
This paper explores the score-based diffusion models' text hallucination, where each generated symbol is accurate but arranged nonsensically. Through the experiments on various settings of toy datasets, the authors observed that this phenomenon is related to the local generation bias of the score model, which is the tendency of the score model to not regard the entire input region and their correlation. 
In the process, a metric called Local Dependency Ratio(LDR) was newly suggested to quantify how the diffusion model relies on specific local region of the input for denoising.

The authors also found that this bias emerges across various architectures, including CNN, MLP, and transformers.
Lastly, they examined training dynamics on specifically designed data to propose a theoretical perspective on the emergence of local generation bias.

### Strengths
-The paper newly identifies the possible cause of the text hallucination, with extensive experiments over various dataset settings of symbols and their correlation.

-The suggested metric of LDR is intuitive and shows good explainability of the score model behavior.

### Weaknesses
 -Since most of the results are obtained from the simple controlled data, there's still some gap to fill to extend the results into the real-world language data. The experiments, while thorough on toy datasets, do not fully address the complexities of natural language. For example, the symbol correlation in real text is far more intricate than simple pairwise dependencies, involving long-range dependencies and hierarchical structures.

-The proposed theoretical analysis on local generation bias with training dynamic is limited for the used problem setting(e.g. most conclusions in Section 5.1 require Assumption 5.1). The theoretical analysis relies heavily on a specific assumption about the data distribution, which may not hold in more complex scenarios. The analysis, while insightful, lacks the generality needed to apply to diverse real-world datasets. The conclusions drawn from this analysis are therefore somewhat restricted in scope.

-The paper does not sufficiently explore the impact of model size and training data size on the observed local generation bias. It is unclear whether the bias is an inherent property of the diffusion model or a result of insufficient training or model capacity. The experiments do not provide a clear picture of how these factors interact with the local dependency ratio.

### Questions
-In the dyck parenthesis experiment in Section A.4.2, it seems like the diffusion model correctly figures out the grammar beneath valid dyck sequences.  Does this suggest the denoising network can overcome the local generation bias and avoid hallucination, contrary to the paper's conclusion? If not, what is the difference between this experiment and other results?

-In Figure 5(right), how does the figure contain the LDR plot with t=121 and t=168 if the total timestep is 100?

-It would be better if there's an LDR comparison on the sampling of pre-trained models, between generating hallucinated samples and generating correct samples.

-In the overall results, the authors distinguished the 'extrapolated' samples and 'in-dataset memorized' samples. However, in terms of resolving hallucinations, is there a meaningful difference between the generation of extrapolated data and memorized data? Memorized output is also valid, and memorization by overfitting may not be due to the intrinsic symbol correlation itself, but to other factors such as training data preparation, model size, etc. Also, for some datasets, especially real-world texts, the correct extrapolation from the training dataset is almost impossible, and being contained in the database becomes the only way to be valid.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates textual hallucinations, where diffusion models generate locally accurate but globally nonsensical symbols. The authors introduce the local dependency ratio (LDR) as a probe to quantitatively measure the model's dependency on local regions when conducting denoising. With LDR, the authors observe that the textual hallucinations are caused by the local generation bias, And this phenomenon exists across various denoising network architectures including MLP and transformers. The authors also provide a theoretical analysis of its underlying mechanism.

### Strengths
1. The authors explore textual hallucination in generative models, addressing a crucial yet often overlooked research problem. 

2. They introduce the local dependency ratio (LDR) to examine how diffusion models depend on localized regions of input noise during denoising and generation. The analysis is both robust and engaging. 

3. They present a sound theoretical examination of the mechanism underlying textual hallucination.

### Weaknesses
1. Labeling this issue as "textual hallucination" might cause confusion with hallucination problems in large language models (LLMs). It’s advisable to adjust the task description or add a notice at the start of the main paper for clarity.

2. Following up on the previous question, would this issue also occur in Vision Language Models (MLLMs)?

3. The experimental setup appears less practical and somewhat limited in scope. Most experiments were conducted on small, toy datasets and within narrow domains, such as digit generation. Could larger datasets and real-world applications, like image generation on ImageNet, be explored? Additionally, would textual hallucination issues appear in other real-world contexts?

4. The theoretical analysis is constrained to two-layer MLP learning parity points on a hypercube, creating a significant gap between MLPs and more complex models like UNet and DiT. The relevance of the proposed theory to real-world models is therefore uncertain and requires further investigation.

5 It is suggested to include potential strategies to address textual hallucination issues. Although fully solving this problem may be challenging, proposing ways to partially mitigate this limitation in generative diffusion models would be valuable.

### Questions
Please refer to the weaknesses section.

### Soundness
4

### Presentation
2

### Contribution
3
