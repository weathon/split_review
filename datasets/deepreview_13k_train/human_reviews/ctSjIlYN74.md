# Balanced conic rectified flow

- Decision: Reject
- Scores: 5, 3, 6, 6

## Abstract
Rectified flow is a generative model that learns smooth transport mappings between two distributions through an ordinary differential equation (ODE). Unlike diffusion-based generative models, which require costly numerical integration of a generative ODE to sample images with state-of-the-art quality, rectified flow uses an iterative process called reflow to learn smooth and straight ODE paths. This allows for relatively simple and efficient generation of high-quality images. However, rectified flow still faces several challenges. 1) The reflow process requires a large number of generative pairs to preserve the target distribution, leading to significant computational costs. 2) Since the model is typically trained using only generated image pairs, its performance heavily depends on the 1-rectified flow model, causing it to become biased towards the generated data.

In this work, we experimentally expose the limitations of the original rectified flow and propose a novel approach that incorporates real images into the training process. By preserving the ODE paths for real images, our method effectively reduces reliance on large amounts of generated data. Instead, we demonstrate that the reflow process can be conducted efficiently using a much smaller set of generated and real images. In CIFAR-10, we achieved significantly better FID scores, not only in one-step generation but also in full-step simulations, while using only $7.2\%$ of the generative pairs compared to the original method. Furthermore, our approach induces straighter paths and avoids saturation on generated images during reflow, leading to more robust ODE learning while preserving the distribution of real images.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents Balanced conic rectified flow, an improved version of "reflow" in rectified flow. The main idea is to use a real sample and its reverse Gaussian random noise pair based on inverse flow rather than using noise and corresponding generated samples using PF ODE. To mitigate the error from the inverse flow, the paper presents a "conic" reflow that considers a neighbor of the inverse point with a small noise. The paper argues the proposed method shows better $k$-rectified flow for $k>1$, especially for 1-step generation.

### Strengths
- To the best of my knowledge, using real data and its reverse Gaussian random noise is an interesting and under-explored direction.
- The performance improvement on CIFAR-10 is promising.
- The observations (Figures 2 and 3) that motivate the method are interesting.

### Weaknesses
I am slightly negative to the paper due to the clarity/readability problem. Specifically:

- The writing of the paper can be improved. For instance, since the primary focus of the paper is the transport from Gaussian distribution to the target data distribution, explicitly mentioning it (like $X_1$ or $X_0$ becomes the real data and the Gaussian noise, respectively), can help the readers to understand the contents better, especially for the people who are not very familiar with the concept of Rectified Flow. Moreover, some captions are overlapped with other figures, such as in Figures 2 and 3. Other figures are really problematic; for instance, in Figure 9 and 10, legends and labels are almost impossible to read. 
-  The paper compares the performance only with the original rectified flow and does not provide a comparison with relevant work [1]. Although it may be understandable because the primary focus of this paper is in revisiting the "reflow" process, I think the quantitative comparison should exist because this work also deals with the same problem. Otherwise, could authors try conic reflow upon this paper? 
- As mentioned in the paper, the paper lacks theoretical analysis when choosing slerp or conic hyperparameters. In this respect I expect more empirical results (like imagenet or various higher-resolution datasets) should be provided, but the in the current form the paper only provides retuls on CIFAR-10 and (qualitative) evaluation on LSUN. Does a similar trend hold for AFHQ or other datasets? I think the paper should include the results at least on all datasets used in the original rectified flow datasets, given that the original paper provides all of the checkpoints for those datasets and this paper does not have theoretical insights (meaning that the validation should be done in empirical manner). 
- The values in Table 2 are difficult to understand. What do they mean?
- Suggestion: do we need to write the reverse ODE as $v^{-1}$? Isn't it just $-v$?
- Minor: curvature -> Curvature in L410.

### Questions
- In Table 3, why does NFE between the original rectified flow and the proposed method differ (like 110 vs. 104)? 
- Did authors try using only real pairs for reflow (without fake pairs)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper claimed that rewiring the flow starting from the source distribution (e.g. the Gaussian distribution) to the real data distribution in rectified flow generates the drifted distribution. To remedy this, the authors proposed to start from the real data distribution for rewiring. After obtaining the inversion of each real data, the authors use the spherical linear interpolation (slerp) between the reverse noise and a randomly sampled noise. The training objective involves data from both inversion directions.

### Strengths
The authors did analysis investigating the rewiring directions in the original rectified flow. There might be a distribution drifting phenomenon that we should pay attention to.

### Weaknesses
The authors make some claims without strong evidence:
- The authors mentioned in line 124: "Interestingly, the k-rectified flow underperforms the (k − 1)-rectified flow in terms of image quality. This is obvious because the fake samples have lower quality than the real samples". This sounds too strong. Won't there be other reasons? Specifically, the claim that the lower quality of fake samples is the *obvious* reason for performance degradation lacks rigorous justification. There could be other factors, such as the accumulation of errors in the iterative flow process or the model's inability to generalize to unseen distributions as the number of rectification steps increases. A more thorough investigation into the root cause is needed.
- The authors mentioned that "Since the reflow process uses only fake pairs, discrepancies occur between the reconstruction errors of real and generated images." However, it is still not obvious why reflow process uses only fake pairs is a reason for "discrepancies occur between the reconstruction errors of real and generated images". This statement lacks a clear mechanistic explanation. Why does using only fake pairs inherently lead to discrepancies in reconstruction errors between real and generated images? A more detailed analysis of how the training process using fake pairs affects the reconstruction of real images is required.
- Why "$L^{recon}_2$ is lower at the fake samples than the real samples" indicates "the 2-rectified flow drifts away from the real samples" (line 151)? The connection between lower reconstruction error on fake samples and drift from real samples is not clearly established. It is necessary to explain why the model prioritizing reconstruction of fake samples implies a drift away from the real data manifold. A more detailed analysis of the error landscape and its relationship to the data distribution is needed.
- Why "Lp-recon is lower near the fake samples than the real samples" indicates "the 2-rectified flow suffer from crossing between real samples"  (line 152)? The link between lower perturbed reconstruction error near fake samples and crossing between real samples is not clearly justified. It is crucial to explain the underlying mechanism that connects the perturbed reconstruction error to the potential for sample manifold crossing. A more rigorous explanation of this phenomenon is required.
- The authors mentioned that the original Rectified Flow algorithm (Liu et al. 2022) uses the fake pairs, but I have to mention that the original Rectified Flow algorithm provided an option to use the real data pairs $(v^{-1}(X_1), X_1)$. The authors should acknowledge that the original work did propose the use of real data pairs, and clarify the novelty of their approach in this context.

Experimental results contradict with the claims:
- From the experiments in Fig. 3(b), the perturbed reconstruction error for real samples are higher than the reconstruction error for real samples. This is not faithful. This contradicts with the perturbation proposed in the method in Sec. 3.3. The results in Figure 3(b) seem to contradict the claims made about the behavior of the perturbed reconstruction error. The authors need to reconcile these conflicting observations.
- This paper discussed that in the original rectified flow, more number of rectified flow lowers the image quality. Therefore, the authors proposed to use real pairs. However the proposed method also suffers from more number of rectified flows being worse (Figure 7). The fact that the proposed method also suffers from performance degradation with an increasing number of rectification steps undermines the motivation for using real pairs. The authors should discuss this limitation and its implications for their method.

Many parts in this paper is not clear and confusing:
- The generated pair or fake pair in this paper seems confusing. Please have formal definitions of the generated pair, fake pair, real pair. The lack of clear definitions for key terms like "generated pair," "fake pair," and "real pair" makes it difficult to understand the method. Formal definitions are needed to clarify the different data pairs used in the method.
- What are fake samples? Are those data generated from the source distribution (e.g., Gaussian distribution) via a trained $v$? The definition of "fake samples" is unclear. It is essential to explicitly state how these samples are generated and their role in the training process.
- In line 141 the authors wrote: "Lower reconstruction error on the real samples $_2^{recon}(X_1)$ indicates that a rectified flow is more faithful to the real samples as shown in Figure 3b." However, in Fig. 3(b), real samples have higher reconstruction error. I got confused about what the authors want to express. The statement in line 141 directly contradicts the evidence presented in Figure 3(b). The authors must correct this error and provide a consistent interpretation of the results.
- Definition of exp() in Eq. (10) and (12). Is it an exponential function? I understand $t$ is generally between 0 and 1. The definition of the `exp()` function in equations (10) and (12) is ambiguous. The authors should clarify whether it refers to the exponential function and explain how it is used within the given context, especially given that `t` is typically between 0 and 1.
- In line 295, this method needs to define a slerp schedule with respect to time t. How is the time t in line 295 related to training steps in Fig. 5? How to set the proportional coefficient for the slerp noise schedule? The relationship between the time parameter `t` in the slerp schedule and the training steps shown in Figure 5 is unclear. The authors should provide a detailed explanation of how the slerp schedule is implemented and how its parameters are determined.
- What does the "single real pair" in "reflow using just a single real pair" in Sec. 4.6 Ablation study refer to? The meaning of "single real pair" in the ablation study is ambiguous. A precise definition is needed to understand the experimental setup and results.
- Table 1's results are not explained. The results presented in Table 1 lack sufficient explanation. The authors should provide a detailed analysis of the results and their implications for the proposed method.

Experimental results are not strong:
- From the ablation study, the method without slerp noise performance is similar to the proposed method, in terms of Inception Score, 8.79 vs 8.57. The authors should do experiments on more datasets to evaluate the effectiveness of the proposed real pair and slerp noise. The marginal improvement in Inception Score with the slerp noise suggests that the proposed method may not be significantly better than the baseline, and further experiments on diverse datasets are needed to validate its effectiveness.
- No quantitative comparison between the proposed method and the baseline method on the LSUN bedroom dataset. In terms of the qualitative results, when the number of steps is 2 (Fig. A27) or higher (Fig. A28), the results of the proposed method and the baseline method appear close. The lack of quantitative comparisons on the LSUN bedroom dataset and the qualitative similarity between the proposed method and the baseline in the provided figures raise concerns about the practical advantages of the proposed method.

### Questions
See Weakness

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper begins by identifying two key issues with current rectified flow models: (1) high computational costs due to the large synthetic datasets required for the reflow process, and (2) degradation in image quality with k-rectified flow, where generated images drift from the real data distribution, potentially leading to potential mode collapse. To address these challenges, the authors propose incorporating real images into the k-rectified flow process. This integration significantly reduces computational costs, as fewer samples are needed when using real images (by their experiments). The authors construct noise-image pairs by inverting real images and stabilize the process by blending the inverted and Gaussian noise through spherical interpolation.

Additionally, the paper introduces several enhancements, including balancing between traditional (synthetic-only) and real image-based rectified flows and implementing a Slerp noise schedule. They also propose a new metric, Initial Velocity Delta (IVD), to analyze model performance in one-step denoising. The proposed method demonstrates improvements over traditional k-rectified flow models, as shown through evaluations on CIFAR-10.

### Strengths
The authors begin with a thoughtful analysis of the limitations in existing rectified flow models, which effectively motivates their proposed approach. Their decision to incorporate real images into the reflow process is both intuitive and straightforward to implement. Additionally, they smartly apply spherical interpolation to blend Gaussian and inverted noise, promoting stable training, and introduce balancing techniques to integrate synthetic-only and real-data flows for greater consistency. The introduction of the IVD metric further enhances the paper’s novelty by offering an innovative tool for in-depth analysis of one-step denoising, providing valuable insights into model behavior and effectiveness, especially in assessing the initial accuracy of generative paths.

### Weaknesses
Although the paper presents substantial improvements to the k-rectified flow process, a more in-depth theoretical foundation could enhance the rigor and clarity of the contributions. Some key points to consider:
1. The use of real images in reflow may seem to contradict the original purpose of the rectified flow method. Since reflow is based on the fact that it used the new synthesized data which was rewired, making it easier to straighten the path. Real data does not carry that property, so integrating real images might theoretically undermine the reflow process. While experimental results indicate positive outcomes, a theoretical examination of why real images enhance rather than disrupt the reflow process would strengthen the study and clarify this counterintuitive result. Specifically, it's unclear how the distribution of inverted real images aligns with the desired properties of the reflow process, which typically relies on a continuous transformation between noise and data distributions. The paper lacks a discussion on the potential impact of using real data on the learned vector field, and whether the vector field remains smooth and well-behaved when real images are introduced.
2. The choice of spherical interpolation (Slerp) lacks adequate justification. It would be helpful to understand why Slerp was selected over simpler alternatives like linear interpolation. Is there a theoretical or empirical reason why Slerp provides a significant advantage for stability or image quality in this context? A comparison with other interpolation methods could demonstrate whether Slerp offers unique benefits. The paper should provide a more detailed analysis of how Slerp affects the geometry of the noise space and why this specific geometry is beneficial for the training process. Without this, the choice of Slerp appears somewhat arbitrary.
3. Similarly, the noise scheduler’s reliance on spherical interpolation, with a gradual increase and then decrease in Gaussian noise, is not fully explained. An explanation for this scheduling pattern, ideally supported by theoretical or experimental evidence, would clarify its role in enhancing training or image quality and differentiate it from simpler approaches. The paper should explore the impact of different noise schedules on the training dynamics and final image quality. For example, how does this specific schedule compare to a monotonically increasing or decreasing schedule, and what are the trade-offs in terms of convergence speed and sample quality?
4. Since the method stated that it should helps the model avoiding mode collapse, it would be nice to see even more extreme k (papers examined till k=3) to see the effectiveness of the method.

### Questions
Authors should address the questions raised in Weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes to introduce real samples and their inverted noises (real sample -> noise) instead of commonly used Gaussian noises and generated samples (noise -> generated samples) for rectification (reflow). This operation alleviates the target distribution drift and improve the performance and efficiency of rectification.

### Strengths
Overall I think the paper is good and reading this paper inspire me to some extent,
1. The motivation is clear (as indicated in the abstracts and introductions) and the overall storytelling is smooth for me.
2. The demonstration is good (good figures and tables).
3. The method is straightforward and easy to understand and implement. 
4. The performance seems to improve a lot compared to the baseline method.

### Weaknesses
1. **Performance**: Although the improvements from vanilla rectified flow, the performance still seems to be  not competitive with advanced distillation and acceleration techniques like iCT [1] and  SiD [2]. For example, in table 1, we can see that the proposed method with rf-3 achieves FID 5.48 (4.68), while in iCT achieves 1-step FID 2.83, 2.51 on CIFAR-10.

2. **Comparison**: For all tables, I would like the authors to add the performance of the original pretrained diffusion models. This will give the readers a clear understanding what is the upper-bound of reflow. Otherwise, readers might find it struggle to understand gap between a pretrained diffusion model  and a trained rectified model. 

3. **Metrics**: I would like to see more metrics like recall and precision to better understand the gap of real data distribution and the generated data distribution. 

4. **Typos**:  In line 746-747,  there is a `??` ; From line 753 to line 768, the words are horizontally centred in a strange way.


5. **Theoretical Analysis**: Though soundness, no critical theoretical analysis or bounds are provided. I'm not implying that there necessarily is one, but I am suggesting that adopting a rational analytical perspective can significantly enrich the substance of the article.

### Questions
If the pretrained diffusion model will generate a data samples whose distribution has a drift from real data distribution, it will probably fail to reconstruct the noise with real  samples? That is to say, you can never really achieve a perfect coupling noise and sample with a spoiled pretrained diffusion model. How to handle these situations?

### Soundness
3

### Presentation
3

### Contribution
2
