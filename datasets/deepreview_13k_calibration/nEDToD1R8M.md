# Rectified Diffusion: Straightness Is Not Your Need in Rectified Flow

- Decision: Accept
- Avg Score: 5.75
- Scores: 8, 6, 1, 8

## Abstract
Diffusion models have greatly improved visual generation but are hindered by slow generation speed due to the computationally intensive nature of solving generative ODEs. Rectified flow, a widely recognized solution, improves generation speed by straightening the ODE path. Its 
key components include: 1) using the diffusion form of flow-matching, 2) employing $\boldsymbol v$-prediction, and 3) performing rectification (a.k.a. reflow). In this paper, we argue that the success of rectification primarily lies in using a pretrained diffusion model to obtain matched pairs of noise and samples, followed by retraining with these matched noise-sample pairs. Based on this, components 1) and 2) are unnecessary. Furthermore, we highlight that straightness is not an essential training target for rectification; rather, it is a specific case of flow-matching models. The more critical training target is to achieve a first-order approximate ODE path, which is inherently curved for models like DDPM and Sub-VP. Building on this insight, we propose Rectified Diffusion, which generalizes the design space and application scope of rectification to encompass the broader category of diffusion models, rather than being restricted to flow-matching models. We validate our method on Stable Diffusion v1-5 and Stable Diffusion XL. Our method not only greatly simplifies the training procedure of rectified flow-based previous works~(e.g., InstaFlow) but also achieves superior performance with even lower training cost.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes Rectified Diffusion that generalizes rectified flow to broader categories of diffusion models, improving image generation efficiency by removing the need for flow-matching and v-prediction. Key components of the proposed method include pre-computed noise-sample pairs, consistency distillation, and phased ODE segmentation, allowing the model to achieve comparable or superior quality with fewer training steps.

### Strengths
1. The authors  generalized rectified flow to a wider array of diffusion models by focusing on paired noise-sample training, making the approach compatible with different prediction types and diffusion models.
2. The paper demonstrates that Rectified Diffusion performs better than prior methods like InstaFlow and Rectified Flow in terms of FID and CLIP scores, particularly when generating images in low-step regimes.
3. By dividing the ODE path into phases with enforced linearity in each phase, the model maintains a balance between quality and computational efficiency without altering the fundamental diffusion trajectory.

### Weaknesses
1.  While the approach seems efficient, the paper builds on existing methods, particularly using paired noise-sample training, phased ODE segmentation and consistency distillation. The lack of entirely new techniques could limit its novelty in diffusion model research.
2. While this method employs distillation techniques that improve inference speed, achieving single-step image generation without pre-trained models could introduce a novel advancement.
3. The performance metrics on FID shows only marginal improvements over Rectified Flow. The FID metric for Rectified Flow shown in Table 2 corresponding to step2 (62.81) is higher than step1 (13.67). Are these values correct? Generally step2 value should be lower.
4. Although the method is compared against multiple models, all experiments are limited to a single dataset (COCO). Additional experiments on other benchmark datasets, such as ImageNet, would help validate the generalizability of the results.

### Questions
1. The performance metrics on FID shows only marginal improvements over Rectified Flow. The FID metric for Rectified Flow shown in Table 2 corresponding to step2 (62.81) is higher than step1 (13.67). Are these values correct? Generally step2 value should be lower.
2. Could the authors validated the performance of their method on more datasets?

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
This paper presents two findings, one is that straightness as required in rectified flow is not necessary, and second is that it proposed Rectified Diffusion, which generalizes the design space and application scope of rectification to diffusion models.

### Strengths
First strength is that the paper shows that straightness is necessary as required in rectified flow. It shows that rectified flow is a special case of rectified diffusion, which is what the paper proposed as a better generative model. 
Second strength is the better quantitative results and favorable comparison with other methods.

### Weaknesses
Maybe I am missing something, it seems the paper argues that straightness of the ODE trajectory is not necessary, but its results appear to show a straight path, such as Figure 4 and Figure 5. 
Other weaknesses include that from visual evaluation, it seems that though the rectified diffusion gave better images than rectified flow in most cases, the improvement is not always clear. For example, in Figure 10, the result of rectified diffusion on the sneakers seem that the string missed a buttonhole. Also, in the pajama example, figure patterns on the pajama in the rectified diffusion result are not as sharp as those on the result of rectified flow. In Figure 10, the huskie images generated by both ReFlow and Rec Diffusion seem to have an extra leg, though it is more evident in the image generated by ReFlow.

### Questions
From eq 13 to eq 14, it asserts that d\lambda_t/dt is not zero, what is that? Or as \lambda_t = ln \alpha_t / \sigma_t, is it always true that this partial derivative is non-zero? 
Table 1, second block, it seems for example Rectified Flow's FID had great improvement from 1 step to 2 steps then to 25 steps, the Rectified Diffusion's FID did not show a great improvement from 1 step to 2 steps then to 25 steps, while the Rectified Diffusion's FID at 25 steps is slightly better than the FID of Rectified Flow at 25 steps. Can authors elaborate on why Rectified Diffusion does not experience a much-improved performance from 1 step to 25 steps? 
Figure 2 is somehow difficult to understand. Why did the FID and CLIP score of Rectified Flow not change with iterations?
Figure 6, the two rightmost plots, why did the curves of Rectified Diffusion go up at 4 and 8 steps? Does it mean the method need to stop at some optimal points before its performance decreases? And if so, how does one determine the proper steps to stop? 
In Figure 7, it seems the biggest difference in preference given by human evaluation is the Phased 4-step results. Does it imply that Phased implementation, which features multiple straight trajectories rather than one single straight trajectory generally, generally gives better results? Also, in Phased implementation, how many phases were used? It seems this information is not given in the paper.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper proposed to study the essence of rectified flow and proposed Rectified Diffusion.

### Strengths
They tried to highlight that straightness is not an essential training target for rectification.

### Weaknesses
It was not stated clearly why it is necessary to study whether straightness is not an essential training target for rectification. To me, it was the straightness used in the ode of the rectified flow algorithm that causes the usage of rectified flow, thus it seems trivial that there is no need to use the rectified flow in a ode that does not follow a straight line. 

The diffusion that follows the curve form that the authors proposed is mentioned in some papers including the original rectified flow paper with the formula listed as well. It can return back to DDPM or DDIM; therefore, to me, it seems like recirculating the algorithm.  The authors might want to look into the following references mentioned in the original rectified flow paper in Lu et al., 2022 (Lipman et al., 2022; Albergo & Vanden-Eijnden, 2022; Heitz et al., 2023).Neklyudov et al. (2022).
While the authors meant to straighten the paths that originally were curves, they can be viewed as approximately meanwhile they can also be viewed as the original straight flows.
Although one can choose any ode path, the paper did not prove (or it is not clear) that their choice gains advantage over existing algorithms. As a matter of fact, the authors used 200000 runs to train the algorithm as shown in figure 2. 

Also, Theorem 1 proved in Appendix seems like a similar version of one in (Lu et al., 2022), there is no need to repeat.

As a result of the weaknesses stated here, the title of this paper seems like questionable itself ( seems like a logic flaw?).

### Questions
1. Please correct the typo "obeserve" in Page 5 line 265 and if there is any more.
 2. In Page 5 around line 265, the authors stated that the trajectory of y_t is a straight line from the initial point ϵ towards the direction of x0 (as shown in Figure 3 (e). This is not clearly explained. Also, It seems like a very special case  when they only used X0 = [0, 1]. It would make more sense if the authors generate the trajectories over time for each elements of X_0 to \epsilon.
3. In Page 4, line 205, the authors mentioned that there exists an exact ODE solution form from Lu et al., 2022, but they omitted the solution was  for  what first order ODE. That will easily confuse the readers.
4. Eqn (2)  in Page 4 should be just an linear approximation of curves. You can use a straight line to approximate the curve, but then you can say this linear line is the result of a straight flow ode.
5. Some descriptions seem like claims that need to be further elaborated, for example those in line 250-line 261.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes rectified diffusion, a generalization of rectified flow to first-order ODEs. During training, rectified diffusion aims to correct the learned ODE of the pretrained diffusion model to be closer to a first-order ODE, using precomputed noise-data pairs. Thus the authors argue that using paired noise-data examples is the essential component of both rectified flow and rectified diffusion. The authors further propose phased rectified diffusion and consistency distillation on top of rectified diffusion. In their experiments, they demonstrate superior quantitative and qualitative performance over rectified flow and a previous phased ODE segmentation method (PeRFlow).

### Strengths
* The quantitative and qualitative results (Figs. 8-10) are quite convincing. The authors provide the essential baselines of rectified flow and PeRFlow, as well as additional Stable Diffusion XL-based baselines in Table 2.
* The idea is original yet simple (a strength not a weakness). It is well-backed by a brief theoretical discussion in Section 2.2.
* Besides a few grammatical errors and too-short figure captions, the presentation is good. The text is easy to follow, and the figures are intuitive.

### Weaknesses
 * It would have been nice to compare to Consistency Models (Song et al. 2023) for one-step generation.
* In Table 1, is there a typo for 25-step Rectified Diffusion (Ours)? It says the time is only 0.09s, which is the same as 1-step Rectified Diffusion (Ours).

Nitpick:
* Figure 4 should have axis labels. 
* Fonts too small to read in Figure 7.
* Figure 6 caption too short and could use more description.

### Questions
* In lines 357-358, the authors claim that the first-order ODE objective is a stronger constraint than self-consistency. If it’s the case that first-order ODE => self-consistency, then why would consistency distillation be necessary after rectified flow?

### Soundness
3

### Presentation
3

### Contribution
3
