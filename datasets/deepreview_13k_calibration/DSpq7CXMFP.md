# Learning Counterfactual Interventions for Self-Supervised Motion Estimation

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 6, 5, 3

## Abstract
A major challenge in self-supervised learning from visual inputs is extracting information from the learned representations to an explicit and usable form. This is most commonly done by learning readout layers with supervision or using highly specialized heuristics. This is challenging primarily because the self-supervised pretext tasks and the downstream tasks that extract information are not tightly connected in a principled manner---improving the former does not guarantee improvements in the latter. The recently proposed counterfactual world modeling paradigm aims to address this challenge through a masked next frame predictor base model which enables simple counterfactual extraction procedures for extracting optical flow, segments and depth. In this work, we take the next step and parameterize and optimize the counterfactual extraction of optical flow by solving the same simple next frame prediction task as the base model. Our approach achieves state of the art performance for estimation motion on real-world videos while requiring no labeled data. This work sets the foundation for future methods on improving the extraction of more complex visual structures like segments and depth with high accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a self-supervised estimation of optical flow by learning counterfactual interventions instead of hand-designed counterfactual interventions. Specifically, It re-formulates the motion extraction procedure to make it a parameterized differentiable function and introduces the functional form of a sum of colored Gaussians as a natural intervention class. It claims that the proposed method achieve state-of-the-art performance on TAP-Vid DAVIS—VFG and TAP-Vid DAVIS—CFG. Generally, the idea makes sense to me.

### Strengths
1. The idea of learning counterfactual Interventions instead of hand-design counterfactual interventions is interesting and novel. 
2. Jointly learning counterfactual Interventions and a counterfactual motion prediction to make the system end-to-end is a good design.

### Weaknesses
1. Related wok is quite rough and lack comparisons to the proposed method. Especially, the second paragraph of the related work is less details. 
2. The propose method lack details and further explanation:
1) In L214, it is not clear why the predicted pixel location pˆ2 can be retrieved by finding the peak in the difference image?
2) In L239, "While sometimes effective, a bright colored patch is out of domain for the base predictor." Is there any reference or analysis to support this statement?
3) In Figure 3, I did not find p1 and Ψflow which makes it difficult for me to understand.
4) Does diffFLOW : (I1 , I2 , p1 ) generate flow vector for each pixel? It processed pixel by pixel for the image? 
5) In L306, " the first frame RGB input I and predicts the next frame Iˆ , conditioned on the flow input Fˆ." Specifically, how the model utilizes the Flow F' as condition?
6) Why The final MM prediction is the peak in the average delta image? Any theory analysis?
7) Section 3.4 lack of details for how to distill it into an architecture purpose-built for optical flow estimation.

3. Experiment:
1) It claims that the performance is state-of-the-art on TAP-Vid DAVIS CFG in Table 2 but actually it does not beat SMURF for all metrics.
2) From Table 1 and Table 2, the distilled results are not good enough as MM.
3) As stated in the paper, MM-40 has good results but makes inference expensive. Any comparisons to other SOTA methods on the computation cost?

### Questions
See the weakness.

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
4

### Summary
This paper tackles a key issue in self-supervised learning from visual data: effectively extracting useful information from the representations learned during pretraining, such as motion estimation. The authors build on the counterfactual world modelling paradigm, which uses a masked next-frame predictor to facilitate the extraction of key visual features, such as optical flow, segments, and depth. They specifically target motion estimation for real-world videos, providing a promising step forward in unsupervised visual feature extraction. The key novelty of this paper lies in enhancing self-supervised motion estimation through optimized counterfactual interventions within the Counterfactual World Modeling (CWM) paradigm. Traditional CWM methods use fixed interventions, such as colored patches, which can be inconsistent and noisy in their predictions. This paper introduces a differentiable, learned counterfactual function, termed "diffFLOW," that leverages Gaussian interventions for improved optical flow extraction.

### Strengths
- The paper is easy to follow and well-presented
- The use of a learned counterfactual intervention function is unique and provides a tighter, more effective alignment between pretext tasks and motion estimation.
- The method outperforms current unsupervised motion estimation benchmarks, especially on datasets with challenging frame gaps and motion dynamics.
- By reducing reliance on labeled data, this approach has high potential for scalability across large video datasets.

### Weaknesses
- The multi-mask inference technique, while improving accuracy, increases inference time, potentially limiting real-time applications.
- The paper primarily focuses on optical flow and does not extensively demonstrate results for other visual properties like depth and segmentation, which are mentioned as future directions.


---

Typo
L083  from from

### Questions
- How does the model perform under different types of motion, such as fast-moving objects, complex rotations, or occlusions? Are there particular types of motion where diffFLOW struggles?
- How does this method compare with other state-of-the-art models, such as SMURF and SEA-RAFT, regarding accuracy and efficiency across varying frame gaps?
- L288 to L293 Have you done the ablation with solid-coloured squares?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a Counterfactual World Modeling framework that employs masked next-frame prediction to extract dynamic visual information in a counterfactual manner. A novel approach is proposed, where instead of relying on traditional fixed counterfactuals, the model learns to predict counterfactual interventions. To achieve this, the authors extend the conventional framework by parameterizing and optimizing optical flow extraction using a differentiable program called diffFLOW. By linking the outputs of diffFLOW to a flow-conditioned next-frame predictor and optimizing both jointly, the method ensures that the learned parameters of diffFLOW generate meaningful gradients for training counterfactual interventions. Extensive experiments demonstrate the effectiveness of this method in estimating optical flow.

### Strengths
1. The proposed framework enhances the generic CWM model by learning to predict counterfactual interventions, marking an advancement in the field.
2. The proposed method achieves state-of-the-art performance in motion estimation on real-world videos, demonstrating the approach's effectiveness even when applied to datasets without annotations.
3. The paper is well written, and it is easy to follow its main idea.

### Weaknesses
1. Some technique details and the motivation for the specific design are still unclear. According to Figure 3, the model requires an initial counterfactual p, which is then used to further learn the counterfactual intervention through the optimized MLP. If I understand correctly, the training process requires an initial $p$. How does the initial position of p affect the final motion estimation results? How should $p$ be chosen for different datasets? Does the initial color of p have any impact on the optimization results? These kinds of questions introduce significant uncertainty in how to obtain good results using the existing framework. It would be beneficial to include some ablation studies on this aspect.

2. In the table1 and table2, different models are optimized using different datasets. Why not standardize the datasets used across the different methods? This seems to be a more reasonable and fair setup for comparing the performance of different methods.

### Questions
1. It would be beneficial to include some ablation studies about the choice of the initial $p$.
2. It would be beneficial to provide results for different methods trained on the same dataset, whether in a supervised or unsupervised manner. Alternatively, at the very least, a reasonable justification for the current experimental setup should be given.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose to extend the counterfactual world models (CWM) by addressing the limitations in the hand-designed interventions. Specifically, hand-designed perturbations that are not found in the training distribution can cause spurious predictions and inconsistent motion estimates. To resolve this, the authors propose a paradigm to learn the interventions without using any additional supervisions. Quantitative results demonstrate superior performance against baselines.

### Strengths
[+] The work is well motivated by the limitation in hand-designed perturbation, since the model would intuitively struggle to predict something that it has never seen before.

[+] Figure 1 is clear and helps in illustrating what is CWM and how hand-designed perturbation may be limited.

[+] The proposed multi-mask inference approach is intuitive and effective according to the ablation study.

[+] Empirical evaluation shows superior performance on tracking across large temporal gaps.

### Weaknesses
[-] The contribution appears to be rather incremental. The counterfactual paradigm was established in previous works and remained mostly the same. The proposed architecture mainly served for learning a better "learned" intervention for probing motion information (tracking).

[-] Although the proposed auxiliary task for learning diffFLOW without supervision is interesting, I am not certain it is necessary and appears overly complicated. Would it be possible to use an off-the-shelf self-supervised model to produce correspondences for learning perturbations? This should improve training efficiency, reduce memory constraints, and provide a more explicit form of supervision.

[-] Figure 3 overlaps extensively with Figure 1 and Figure 2. Some separation / focus on particular parts would be more helpful.

[-] SMURF is an optical flow method and the comparison in Table 1 may not be entirely fair. As the authors acknowledged as well (L420), "this is more challenging than optical flow estimation.." Some discussion / additional baselines would be helpful.

[-] Minor errors - (L97): "showed that initially promising with this approach"

### Questions
Beyond the question that I raised in the weakness section, I am curious how well hand-crafted perturbations could work if these are not bright color patches that are obviously OOD, but something more in-distribution to the training data (e.g. randomly sampling spherical gaussians of jittered colors). High-level discussions (without experiments) would be sufficient here.

### Soundness
3

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
2

### Summary
The paper explores a method to improve motion estimation in videos using a self-supervised approach. The authors address challenges in extracting usable information from visual representations without labeled data. They build on the Counterfactual World Modeling (CWM) paradigm, which uses a masked next-frame predictor to extract scene properties like optical flow.

### Strengths
1. The paper is well written and the approach is sound.
2. The method demonstrates performance improvements compared to the previous state-of-the-art.
3. The paper includes quantitative and qualitative comparisons, illustrating the strengths of the proposed method in various scenarios and frame gaps.

### Weaknesses
1. It seems to lack novelty, using a diffusion model to predict the next frame is too common. Firstly, the method proposed by the authors closely resembles the existing Counterfactual World Model. The counterfactual interventions proposed by the authors appear to utilize an alternative predictor to generate counterfactual predictions.
2. The overall amount of work appears too minimal.

### Questions
See weaknesses above. Authors can explain their core contributions to the task in the rebuttal. In determining the final score, I will take into consideration the opinions of the other reviewers.

### Soundness
2

### Presentation
3

### Contribution
2
