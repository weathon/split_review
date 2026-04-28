# Adversarial Self Flow Matching: Few-steps Image Generation with Straight Flows

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 3, 5

## Abstract
Flow Matching provides a method to train Ordinary Differential Equation (ODE)-based generative models and facilitates various probability path designs between initial and target distributions. Among these designs, straight flows are particularly interesting for reducing sampling steps. While some works have successfully straightened flows and achieved image generation in a few steps, they often suffer from cumulative errors or provide only piecewise or minibatch-level straightness. We propose Adversarial Self Flow Matching (ASFM), which can straighten flows and align the generated data distribution with the real data distribution. ASFM consists of two complementary components. Online Self Training straightens flows by constructing a conditional vector field using paired data, enabling one-step image generation during training. Adversarial Training aligns the one-step generated data with real data, thereby reducing cumulative errors when straightening flows. Experiments demonstrate that ASFM can build straight flows across the entire time span between two complete distributions and achieve highly competitive results across multiple datasets among Flow Matching-based methods. For instance, ASFM achieves 8.15 and 14.9 FID scores with NFE=6 on CelebA-HQ (256) and AFHQ-Cat (256), respectively.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Adversarial Self Flow Matching (ASFM), a method for few-step image generation using straight flows in Ordinary Differential Equation (ODE)-based generative models. ASFM includes two components: Online Self Training, which straightens flows by constructing a conditional vector field with paired data, and Adversarial Training, which aligns generated data with real data to reduce cumulative errors.

### Strengths
Few-Step Generation: ASFM enables high-quality image generation in just a few steps, which is more efficient compared to traditional methods that require a large number of steps.

Improved Efficiency: By leveraging straight flows, ASFM reduces the number of function evaluations (NFE) needed, significantly decreasing the computational cost and time.

Zero-Shot Capabilities: ASFM retains the zero-shot capabilities of ODE-based generative models, allowing for tasks such as image editing without the need for paired data.

### Weaknesses
Complexity in Training: ASFM's two-component training methodology, including Online Self Training and Adversarial Training, may introduce additional complexity in the training process compared to simpler generative models. Specifically, the interplay between the self-training and adversarial components needs further clarification. The self-training process, which involves constructing a conditional vector field, may be sensitive to the choice of the paired data and the method used for vector field construction. The adversarial training, while aiming to align generated data with real data, may introduce instability or mode collapse if not carefully tuned. The paper lacks a detailed analysis of the sensitivity of these components to hyperparameter settings and the potential for these issues.

Generalization to Other Tasks: While ASFM shows promise for image generation, its extension to more complex tasks like text-to-image generation or large-scale datasets may require further enhancements and research. The current formulation of ASFM is primarily designed for unconditional image generation. Extending it to conditional generation tasks, such as text-to-image synthesis, would require significant modifications to the model architecture and training procedure. The paper does not provide any concrete discussion or preliminary experiments on how ASFM could be adapted for such tasks, leaving a gap in the assessment of its broader applicability. Furthermore, the performance of ASFM on large-scale datasets is not evaluated, which is a crucial factor in determining its practical utility.

### Questions
1. How does ASFM balance the trade-off between the quality of generated images and the number of function evaluations (NFE)?

2. Can ASFM be extended to conditional generation tasks, such as text-to-image synthesis, and if so, what challenges might arise?

### Soundness
3

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
This paper improves flow matching-based models by integrating two training schemes: (1) Online Self-training and (2) Adversarial Training, which are combined and called Adversarial Self Flow Matching (ASFM). (1) is an upgraded version of the original reflow (from Rectified Flow paper) by converting it into an online learning strategy, where the synthetic data is generated on the fly, instead of generated after each rectified flow process. (2) is a way to better align the synthetic data distribution with the real data distribution by using GAN loss. The author validates ASFM's effectiveness through multiple datasets such as CIFAR-10, CelebA-HQ, and AFHQ-Cat showing competitive scores using few denoising steps (NFE=1 to 6). Furthermore, the authors show downstream task applications such as image editing are also applicable upon the trained models.

### Strengths
Presentation:
The paper is well-structured and provides clear explanations of both the conceptual foundation and technical implementations of ASFM. Key technical components, such as the loss functions and training algorithm, are detailed sufficiently to allow reproducibility and insight into the model’s design choices.

The paper introduces a new method that integrates GAN loss into flow-matching, along with new strategy to implement reflow. The method is also experimented quite extensively through multiple datasets and the trained models have good quality only using a few denoising steps.

### Weaknesses
1. nit: L213-215: "Given that the sum of two sides ..." I don't really see this as a strong explanation, since the data is actually in a higher dimension space rather than 2D?
2. L238-239: "where only the newly generated data is use ... causing the model’s training to fail to converge" and Model A in the experiment section show that generating new image every batch makes the model couldn't converge. It would be nice if the authors can dive in more in this phenomenon and explain why this would happen. Suppose that the author claimed that GAN-loss would help the generated distribution more aligned with the real image distribution, I don't understand why having new samples every batch would harm it (ignore the computational expense).

-> If possible, authors should provide a more detailed analysis of this phenomenon, perhaps including visualizations of the training dynamics or theoretical justifications for why this occurs despite having GAN loss.

3. It seems like the model needs to be initialized with good weights beforehand, would the method still work if it is randomly initialized? If not, what would be the root cause?

-> If possible, authors should provide an ablation study comparing performance with random initialization versus pretrained initialization, and a discussion of the implications for the method's robustness and generalizability.

4. The `freq` param to update new data seems to be quite important in my opinion, does it need to be tuned properly for this training scheme to work? An ablation study for this would be more convincing.
5. GAN loss is known to be unstable while training, was the training for ASFM affected by it, it yes, how did the authors fix it?
6. Both GAN-loss and reflow is also known for making the model has the property of mode collapse. Do models trained with ASFM have this problem? Authors should also use metrics such as "recall" (https://arxiv.org/abs/1904.06991) to evaluate the model.
7. Is there any reason for the fact that there's no output metrics for ASFM using NFE=6 same as in AFHQ and CelebA-HQ?

### Questions
Author should address the Weakness section.

### Soundness
3

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
5

### Summary
The paper introduce adversarial training for flow matching framework that better aligns the one-step generated solution and real data. The method is shown to reduce the cumulative errors of solution trajectories of flow rectification.

### Strengths
- Leverage adversarial objective to align one-step prediction with real data distribution
- The idea is simple and intuitive while showcasing their strong performance on different datasets.

### Weaknesses
 - The method has limited novelty as the usage of adversarial training in one-step generation is introduced in several works like ASM [1], CTM [2], ADD [3]. The method is solely the combination between flow-rectification and adversarial training.
- The effectiveness of the methods appears limited to low-resolution data like CIFAR-10, as shown in Table 2, where the FID scores for 1 and 2 NFE remain quite high. Additionally, the table omits the results for 2-rectified-flow and 3-rectified-flow, which is shown to achieve better FID scores under few-steps sampling (similar to the observation in Table 1). The authors should ensure fairness in their reporting so please include the results of 2-rectified-flow and its distillation in the table.
- Need to update table 2 with some few-steps works like CTM & CD as well.
- Table 1: the authors should report results of RectifiedFlow in combination with their distilled versions for 1-NFE generation as they give best FID scores of 6.18 vs 378 for 1-rectified-flow, 4.85 vs 12.21 for 2-rectified-flow, and 5.21 vs 8.15 for 3-rectified-low. Again, the authors should be integrity in their reports.
- The adversarial training is supposed to improve the gap between data distribution and one-step prediction. However, for high-resolution dataset as in table 2, the method still need more than one-step to produce better FID score under 10.0.
- Meanwhile, the authors should report the FID and NFE of the original flow matching model that they build upon for better exposition. In L332, it showed that the method uses the pretrained 1-rectified-flow. However, the 1-rectified-flow is shown to have straighter solution strajectories than the original flow model. It is reasonable for the authors to test their method starting with the original flow model.
- The method requires online-sampling of new samples to put in the queue. Does it add cost to the training progress in terms of speed and computation? Besides, the method requires two-separate model forward passes for flow matching loss and adversarial loss as shown in Algorithm 1. What if both objectives using the same random t1, how is the model performance?
- Is the size of training memory associating with model performance? The paper is only test with a size of 128 batches.
- The ablation of number of generated samples in Table 3 should include the case where 2-rectified-flow-online use the same amout of data size to compare with ASFM.
- Ablation of $\lambda_1, \lambda_2$ in Eq. 13 is missing.
- Zeroshot editing task should be moved to the main manuscript.

### Questions
Please address my concern above.

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
This paper introduces ASFM as a novel Flow Matching model to straighten the trajectory of samples and generates high-quality images in a few steps. In contrast to previous approaches in the literature, such as the Reflow procedure and non-trivial pairing, ASFM learns flows using Adversarial Training and Online Self Training to straighten flows and generates high-quality images in a few steps. Experiments are conducted on CIFAR-10, CelebA-HQ (256) and AFHQ-Cat (256) dataset.

### Strengths
The paper is clear and easy to follow.

The core idea of ASFM that introduces adversarial training after online self training is interesting.

### Weaknesses
ASFM can achieve good FID scores on CIFAR-10, but the generated images in Fig.4 are not good enough. More generated images from other baselines are needed to support the experiment. Specifically, the visual quality of the generated samples appears to lack fine-grained details and exhibits some artifacts, which raises concerns about the practical applicability of the method. A more thorough comparison with existing methods, including both quantitative metrics and qualitative visual analysis, is necessary to fully assess the performance of ASFM.

While the authors assert that their research exhibits the one-step generation capability in the abstract, the existing experimental results do not sufficiently validate this claim: No high- resolution sample with fewer-steps (NFE<6) is displayed. The absence of high-resolution results with very few steps makes it difficult to evaluate the true potential of the method for fast generation. The claim of one-step generation requires more compelling evidence, especially at higher resolutions where the challenges of generating coherent images are more pronounced.

The authors also assert that ASFM is a straight flow, but the visual results do not sufficiently validate this claim. I encourage the authors to show the flow is straight over the entire time span, i.e., generated samples with different sampling steps and the same initial noise. The current results only show the final generated images, which do not provide direct evidence of the flow's straightness. To validate this claim, it is essential to visualize the intermediate steps of the generation process and demonstrate that the flow trajectories are indeed straight.

### Questions
The clarity of Fig.2 is insufficient. The transparent red dashed line is some what confusing. It would benefit from additional labels or a more detailed legend to help readers better understand its significance.

The image mixture described in Appendix.C.1 is not clear and the results in Fig.7-8 are not convincing , making it difficult for me to understand the purpose. Providing more detailed explanations or context would greatly improve comprehension.

### Soundness
2

### Presentation
2

### Contribution
2
