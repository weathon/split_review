# Advancing Text-to-3D Generation with Linearized Lookahead Variational Score Distillation

- Decision: Reject
- Avg Score: 4.40
- Scores: 6, 3, 3, 5, 5

## Abstract
Text-to-3D generation based on score distillation of pre-trained 2D diffusion models has gained increasing interest, with variational score distillation (VSD) as a remarkable example. 
VSD proves that vanilla score distillation can be improved by introducing an extra score-based model, which characterizes the distribution of images rendered from 3D models, to correct the distillation gradient. 
Despite the theoretical foundations, VSD, in practice, is likely to suffer from slow and sometimes ill-posed convergence.
In this paper, we perform an in-depth investigation of the interplay between the introduced score model and the 3D model, and find that we can simply adjust their optimization order to improve the generation quality. 
By doing so, the score model looks ahead to the current 3D state and hence yields more reasonable corrections. 
Nevertheless, naive lookahead VSD may suffer from unstable training in practice due to the potential over-fitting. 
To address this, we propose to use a linearized variant of the model for score distillation, giving rise to the Linearized Lookahead Variational Score Distillation ($L^2$-VSD). 
$L^2$-VSD can be realized efficiently with forward-mode autodiff functionalities of existing deep learning libraries. 
Extensive experiments validate the efficacy of $L^2$-VSD, revealing its clear superiority over prior score distillation-based methods. 
We also show that our method can be seamlessly incorporated into any other VSD-based text-to-3D framework.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the text-to-3D generation problem using the variational score distillation (VSD) method. The authors identify issues in the practical implementation of VSD, specifically a mismatching problem between the LoRA and 3D distributions. They propose the Linearized Lookahead Variational Score Distillation ($L^2$-VSD) method to improve the generation quality. The paper conducts in-depth analyses and experiments, comparing $L^2$-VSD with other baseline methods and demonstrating its superiority in terms of generation quality and compatibility with other techniques.

### Strengths
+ The paper is well-structured. The writing is clear. The methodology section presents a detailed comparison between VSD and L-VSD, followed by a clear derivation of $L^2$-VSD. 
+ The proposed $L^2$-VSD method addresses the mismatching problem in VSD by adjusting the optimization order and using a linearized variant for score distillation.

### Weaknesses
- The proposed $L^2$-VSD method seems to be highly dependent on the specific settings and assumptions of the VSD framework. It is not clear how well it would generalize to other text-to-3D generation methods like Gaussian Dreamer or LucidDreamer, which are recent SOTA, or different types of 3D representations such as Gaussian Splatting. As the original VSD takes 8 hours to generate one 3D model, while Gaussian Dreamer takes only 15 mins. The reviewer is afraid the proposed method does not give significant contribution to the current literature.
- The definition of the mismatching problem between LoRA and 3D distributions could be more precise. Besides, is there any metric to estimate the degree of mismatching? A more rigorous mathematical formulation of this problem would strengthen the paper's theoretical foundation.
- Figure 2a: In the original VSD results, as γ increases, the "hamburger" depicted in the figure appears smaller. However, the manuscript states that "the shape of the hamburger becomes more reasonable and clearer as γ rises," which is confusing and requires clarification. It is unclear what criteria are being used to define "reasonable" and "clearer" in this context.
- Figure 2b: Although γ is increased, the learning rate is decreased. These two adjustments seem to counteract each other. Initially, the LoRA learning rate is relatively high, allowing more to be learned in a single update step. With the reduced learning rate, the amount updated in each step decreases, but the number of update steps (γ) increases. This appears to result in a balancing effect, and the manuscript should address this interaction and explain why this particular combination is optimal.
- Figure 3: I am particularly interested in the loss variations during the initial few dozen steps for the four curves presented. Could the authors provide the relevant data to illustrate the loss behavior in the early training stages? This would provide insights into the initial convergence properties of the different methods.
- Figure 4: Would it be possible to include the curve for the VSD method in this figure for comparative purposes? This would allow for a direct comparison of the proposed method's performance against the original VSD.
- Last-Layer Approximation: The manuscript mentions that using the last-layer approximation can eliminate floaters but leads to a reduction in quality. Could the authors elaborate on why this trade-off occurs? A more detailed explanation of the underlying mechanism would be helpful.
- Final Methodology: In the proposed final approach, is it still necessary to use γ to increase the number of LoRA training iterations? Clarification on the necessity and impact of γ in the final method would be beneficial. Specifically, does increasing γ still provide benefits in the context of the other modifications made in $L^2$-VSD?
- Effectiveness of Quality Improvement: Based on the current set of result images, it is challenging to ascertain whether the quality has been effectively enhanced. Could the authors provide additional result images, perhaps with a more diverse set of prompts and under more challenging conditions, to better demonstrate the improvements?
- Scope of VSD Improvements: The paper appears to implement improvements only in the first phase of VSD. Is this the final outcome, or are there plans to apply similar geometry and texture improvements in the second and third phases of VSD? Clarification on whether subsequent phases will also be addressed is needed.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work empirically analyzes the two theory-implementation gaps of Variational Score Distillation (VSD): (1) Convergence of the LoRA model; (2) Misalignment of LoRA model with current 3D model. Based on the analysis, this work further introduces L-VSD and L$^2$-VSD, both of which are lookahead variants of VSD and enable the LoRA model to be aligned with the current 3D model to match theoretical derivations. In particular, L$^2$-VSD is an interpolation of VSD and L-VSD, obtained by discarding the high-order Taylor expansion terms of L-VSD. For evaluation, this work provides qualitative and quantitative comparisons of L-VSD and previous methods: SDS, VSD, ESD, and HiFA.

### Strengths
1. Variational Score Distillation (VSD) is a representative score distillation method for diffusion-guided 3D generation. The defect analysis and improvement of VSD may provide inspiration for subsequent research. To the best of my knowledge, the analysis of LoRA training for VSD is original and somewhat interesting.

2. The paper is well-written and clearly structured.

### Weaknesses
1. This work primarily focuses on the potential issues of LoRA training within the context of VSD, which narrows the scope of the research. While VSD is a significant method, it is worth noting that other score distillation methods, such as ISM, do not rely on a LoRA model. Furthermore, even within VSD, the use of LoRA is arguably an implementation choice. Although the authors' exploration of the theory-implementation gaps is valuable, the practical implications seem limited, especially considering the marginal improvements shown in Figure 7 and the increased training time for L$^2$-VSD, as indicated in Table 2. The 43% additional training time reported for L$^2$-VSD compared to VSD raises concerns about the practical applicability of the proposed method.

2. The analysis presented in Figures 2, 3, and 4 appears to be based predominantly on a single example, "a delicious hamburger." This raises concerns about the generalizability of the findings. To ensure robustness and reduce potential noise, it would be beneficial to conduct experiments on a more diverse set of samples, particularly for quantitative analyses like those presented in Figures 3 and 4.

3. There appears to be a contradiction in the authors' arguments regarding LoRA optimization. In Section 3.1, they suggest that LoRA's finite step optimization leads to under-convergence and deviates from VSD's theoretical derivation. However, in Sections 3.3 and 4, they claim that the lookahead mechanism can cause over-convergence, and a linear lookahead mechanism is needed to prevent overfitting. It is unclear why LoRA overfitting is considered detrimental, as it seems to align with the VSD theory. A more detailed explanation of the potential negative effects of LoRA overfitting on the overall generation process would strengthen the argument.

4. The claim in Line 230 regarding "the necessity for the LoRA model to look ahead" is not fully supported by the results presented in Figure 2. Specifically, L-VSD does not appear to offer a clear advantage over VSD when $\gamma$ = 1, 2, and 5. Further clarification and evidence are needed to justify this claim.

5. Figure 1 is somewhat unclear and could benefit from further explanation. While it suggests that L-VSD provides a better fit than VSD, the specific role and influence of the LoRA distribution r(x) in this context remain ambiguous.

### Questions
1. For L-VSD, in a certain iteration step $i$, are the input $x_{t'}$ used for LoRA training (Eq.(6)) and the input $x_t$ used for NeRF training (Eq.(5)) sampled from the same camera view? Do they use different timesteps?

2. In Figure 2(b), it seems that lowering the learning rate of LoRA is quite effective for L-VSD. So why do we need to use the computationally expensive L$^2$-VSD?

### Soundness
2

### Presentation
2

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
The paper introduces Linearized Lookahead Variational Score Distillation (L2-VSD) to improve the convergence of VSD for improved text-to-3D generation with text-to-image diffusion models. The paper aims to improve the NeRF optimization using VSD, by first analyzing the convergence behavior of LoRA layer, and suggest a Lookahead score distillation which can reduce the gradient norm. The author states that this method can better adjust the gradient information based on current 3D model and can improve the stability of 3D optimization as well as the quality of 3D generation. The provided experiments compare with VSD with its variant, and show improvements.

### Strengths
1. L2-VSD provides more stable convergence by utilizing a linearized lookahead correction.
2. L2-VSD can be incorporated into other VSD-based frameworks, such as HiFA.

### Weaknesses
The visual results presented for L2-VSD do not clearly demonstrate an improvement over those generated by VSD. Specifically, Figure 7 does not convincingly address known issues with VSD, such as saturated colors and visual artifacts in 3D assets. Additionally, the quantitative results in Table 1 are somewhat misleading. In most contexts, a higher CLIP similarity score indicates a better match with the prompt, yet L2-VSD, which has a lower CLIP similarity than other methods, is highlighted in bold. The evaluation is also based on 20 prompts with 120 views, which could lead to a saturated distribution, raising concerns about the reliability of FID as a measure of the proposed method’s quality.

Regarding Figure 3, the observed reduction in loss is likely expected, given that the random timestep selection during optimization naturally reduces variance. The authors attempt to correlate this reduction in loss with improved 3D generation quality by showing a single example in Figure 2. However, given the inherent randomness in generative models, drawing meaningful conclusions from a single example is not advisable and may not support a causal relationship.

The paper’s clarity could also benefit from further refinement, as the core argument is challenging to follow. The main points seem to be: 1) fitting the LoRA model in VSD with additional optimization steps can improve 3D generation quality; 2) however, a naive application of this approach did not yield satisfactory results; and 3) therefore, the authors propose a linearized VSD with a second-order approximation to improve convergence. This reasoning is presented in a somewhat disjointed manner, making it difficult to follow the logic and understand the proposed method’s effectiveness over existing approaches. Additionally, the results presented do not appear to fully support the claims made.

### Questions
1. Could the author justify the quantitative results in Table 1?
2. Does the proposed method can be applied to mesh fine-tuning (e.g., stage 2 of Prolific dreamer)?

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
4

### Summary
This paper studies the issues of Variational Score Distillation (VSD) and proposes solutions to these problems. Specifically, the study identifies a gap between the theories and practical implementation of VSD. To bridge this gap, the first suggested approach is to repeat the LoRA training multiple times. The second approach is to run the LoRA training before the 3D model learning. However, the authors observe that simply combining these two methods does not lead to good performance. Furthermore, they find that the "training LoRA first" approach results in an unstable high-order term that negatively impacts generation quality. As a solution, they propose removing the high-order term from the update equation.

### Strengths
Strength:
1. The paper offers a solid analysis of VSD and proposes improvements based on this analysis.
2. The L2-VSD reduces computational overhead in the proposed methods.

### Weaknesses
Weaknesses:
1. The representation and organization of the paper in its current form are very confusing, especially in Section 3.1. This section discusses the importance of repeating the LoRA training multiple times, yet concludes that it is "somehow important but not sufficient." Additionally, this method is NOT included in the final equations (Eq 9 and Eq 11), raising questions about the section's relevance.

2. An important ablation study is missing: method with the high-order term vs. the proposed method vs. standard VSD. This makes it difficult to assess the importance of removing the high-order term for practical use cases.

3. The generated results using the proposed method still show over-saturated colors. This is visible in Fig. 7 (burger, fox, robot) and Fig. 8 (cake), indicating that the over-saturation issue has not been fully addressed.

4. VSD is known as one of the slowest SDS-like methods due to the optimization of LoRA. There are multiple methods that improve VSD's efficiency and achieve better results, such as CSD[1] and LODS[2], the proposed method is even slower than standard VSD, significantly limiting its practical utility.

5. Presentation inconsistency. In Fig. 7, the label unexpectedly changes to "L2-VSD".

### Questions
Questions:

1. In addition to the weaknesses listed above, I feel that the proposed method still does not fully address the problems of VSD. Section 3.1 emphasizes the importance of "making the Lora model better converged", but I don't see how the lora model's convergence can be improved by the final Eq. 11.

2. Furthermore, if we consider an extreme case where the Lora model is perfectly trained, it would generate Gaussian noise identical to the noise added to the input. In this case, VSD would be reduced to standard SDS, which contradicts the intuition behind the proposed methods.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors analyzed VSD by identifying critical gaps between its theory and implementation, and introduced L^2-VSD, an efficient and easily implemented variant to mitigate the mismatching issues. The author also showed that L^2-VSD integrates seamlessly with other VSD-based techniques, enhancing its practical utility.

### Strengths
This paper introduces a VSD variant addressing its practical training instability due to potential overfitting. The authors propose a lookahead scheme by updating LoRA before NeRF, contrary to VSD's approach. Additionally, they present a linearized strategy to mitigate the collapse caused by lookahead. The linearized strategy's formulation is clearly presented.

### Weaknesses
Figure placement is problematic. Figure 1, illustrating VSD's distribution alignment drawback, appears in Section 1 on page 2 but is explained in Section 3 on page 5. This forces readers to navigate back and forth to understand the figure's content.

The claim that few efforts focus on improving VSD is inaccurate. Besides ESD, which is examined in the paper, several other studies [1,2,3] have explored VSD variants, contradicting the authors' assertion. Specifically, these works have investigated alternative distillation strategies and loss functions that directly address the limitations of VSD, such as its instability and mode collapse issues. The authors' claim that their method is novel in addressing these issues is therefore not entirely accurate.
The study is limited to NeRF+DmTet 3D representations. Score distillation is independent of 3D representation types. The authors should extend their experiments to include 3DGS-based methods, as demonstrated in works [4,5]. The lack of experimentation with other 3D representations limits the generalizability of the proposed method. For instance, Gaussian Splatting, with its explicit representation, may reveal different challenges and benefits when combined with the proposed L^2-VSD approach, which are not explored in the current study.

### Questions
Why lookahead is important? In lines 227-229, the authors claimed that Lookahead-VSD optimizes NeRF faster than VSD for geometries and textures. However, Fig. 2b shows that Lookahead-VSD produces oversaturated textures compared to VSD (Fig. 2a), worsening as $\gamma$ increases from 1 to 5. This contradicts the authors' assertion that Lookahead is an effective strategy. The authors acknowledged this issue in lines 231-232 but do not explain the apparent contradiction.

The necessity of more LoRA steps. In Section 3, the authors extensively discussed the need for more LoRA steps (measured by $\gamma$) to better align with rendered image distributions. However, they neither incorporate $\gamma$ variation in the proposed methods nor include it in the ablation study, merely stating it is unnecessary. This raises questions: Is $\gamma$ not suitable for 3D generation? If so, why dedicate so much discussion to it?
Wrong CLIP similarity. The biggest puzzle for me is that lower CLIP similarity scores are considered better. Given that CLIP measures cosine similarity between text and image embeddings, higher scores should indicate better performance. While it is expected for VSD to have higher similarity than SDS, it is counterintuitive that L^2-VSD yields lower values.

### Soundness
2

### Presentation
2

### Contribution
2
