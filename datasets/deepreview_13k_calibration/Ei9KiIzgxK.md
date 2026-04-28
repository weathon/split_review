# Synthetic Data is Sufficient for Zero-Shot Visual Generalization from Offline Data

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Offline reinforcement learning (RL) offers a promising framework for training agents using pre-collected datasets without the need for further environment interaction. However, policies trained on offline data often struggle to generalise
due to limited exposure to diverse states. The complexity of visual data introduces additional challenges such as noise, distractions, and spurious correlations, which can misguide the policy and increase the risk of overfitting if the training data is not sufficiently diverse. Indeed, this makes it challenging to leverage vision-based offline data in training robust agents that can generalize to unseen environments. To solve this problem, we propose a simple approach—generating additional synthetic data. We propose a two-step process, first $augmenting$ the originally collected offline data to improve zero-shot generalization by introducing diversity, then using a diffusion model to $generate$ additional data in latent space. We test our method across both continuous action spaces (Visual D4RL) and discrete action spaces (Procgen), demonstrating that it significantly improves generalization without requiring any algorithmic changes to existing model-free offline RL methods. We show that our method not only increases the diversity of the training data but also significantly reduces the generalization gap at test time while maintaining computational efficiency. We believe this approach could fuel additional progress in generating synthetic data to train more general agents in the future.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel two-stage method to improve generalization in offline visual RL. The method first introduces data augmentations, then trains a latent-space diffusion model to generate new transitions. 

The method is tested on V-D4RL and Offline ProcGen. The experiments show that augmentation and upsampling together greatly improve generalization performance.

### Strengths
- The method is simple and easy to understand;
- The proposed method improves generalization performance of offline visual RL methods;
- The method also yields an additional improvement when given a small subset of data with distractions;
- The method only changes the dataset and therefore does not depend on the particular RL algorithm, so in theory it can be used to improve any offline RL algorithm;

### Weaknesses
 - As authors listed, the method requires tuning of the data augmentation parameters, which limits it's applicability.
- The experiments only include DrQ and CQL. Since this paper deals with extending the data and can be applied to many different methods, it would make the method more compelling if there were more methods like in [SynthER](https://arxiv.org/abs/2303.06614), e.g. IQL, TD3+BC, EDAC.

###### Writing 
- Figures 4, 5, 6 are too large
- JS divergence heatmaps in the figures throughout the paper are not very informative. In figure 1 b and 6b, I think it should just be a bar plot, heatmaps with just 4 values seem unnecessary. In figures, 4 and 5, to make it more informative, I'd put the exact values on top of the squares;
- 361 tecnic -- technique? Although it's incorrect, I like this spelling.

### Questions
- Do I understand correctly that your 'Upsampled' method is akin to [SynthER](https://arxiv.org/abs/2303.06614)? If that's so, I would put that in parenthesis. If not, could you provide that comparison?

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
The paper discusses a novel approach to enhance zero-shot visual generalization in offline reinforcement learning (RL) by integrating data augmentation and diffusion models. The proposed two-step method first augments the original dataset to increase diversity, then employs a diffusion model to generate additional synthetic data in latent space. This approach significantly reduces the generalization gap in both continuous (V-D4RL) and discrete (Procgen) control tasks without altering existing model-free RL algorithms. The results demonstrate improved performance in unseen environments, suggesting that this method could advance the training of more robust agents in offline RL settings.

### Strengths
1. The two-step approach effectively combines data augmentation and diffusion model-based upsampling, significantly reducing the generalization gap in both continuous (V-D4RL) and discrete (Procgen) control tasks. This leads to improved performance in unseen environments without requiring modifications to existing model-free offline RL algorithms.

2. By augmenting the original dataset and generating synthetic data in the latent space, the method broadens the distribution of training data. This increased diversity helps mitigate overfitting to spurious correlations in visual inputs, making the trained agents more robust to variations in unseen scenarios.

3. The approach maintains computational efficiency by operating in the latent space rather than the pixel space, allowing for the generation of diverse synthetic data without incurring significant computational costs. This scalability makes it practical for real-world applications in various domains, such as healthcare and robotics.

### Weaknesses
Although the method shows promising results in benchmarks like V-D4RL and Procgen, these are controlled environments. It’s unclear how the method would perform in more complex, real-world scenarios where the variety of unseen situations is vastly greater than in benchmark tests.

The effectiveness of the approach depends heavily on specific augmentation techniques like rotation, color jittering, and color cutout. The results may vary significantly if the distribution of unseen environments does not align well with these augmentations.

While the authors claim the diffusion-based data generation is computationally efficient, training and running diffusion models can be resource-intensive. This could be a bottleneck for scaling up the approach to larger datasets or high-resolution visual inputs.

The paper focuses on a two-step process (data augmentation and diffusion model-based upsampling) but does not explore or compare with other generative models (e.g., GANs, VAEs) that could also potentially increase diversity and improve generalization.

While augmentation and synthetic data help generalization, there is a risk that the model may overfit to artificially generated diversity, especially if this data diverges from real-world test distributions.

### Questions
How does the proposed approach handle significantly different visual distributions in real-world applications (e.g., new lighting conditions or object appearances)?

What are the specific computational costs associated with diffusion model-based upsampling, especially when scaled to larger datasets or higher-resolution visual inputs?

Has the performance of the approach been tested against other generative methods, such as GANs or VAEs, to assess if they could offer similar improvements with potentially lower computational overhead?

How does the choice of augmentation techniques affect generalization across different types of environments? Would different augmentations be needed for different application domains?

Could there be an overfitting risk associated with heavy reliance on synthetic data? How does the method mitigate this, if at all?

### Soundness
2

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
3

### Summary
This paper proposes a two-step approach to improve generalization in offline reinforcement learning with visual inputs. By combining data augmentation with diffusion model-based synthetic data generation in latent space, the method enhances training data diversity without modifying existing algorithms. The authors evaluate their approach on both continuous (Visual D4RL) and discrete (Procgen) action spaces, demonstrating significant reduction in generalization gaps while maintaining computational efficiency. Notably, their method is the first to effectively address visual generalization challenges across both continuous and discrete control tasks in offline RL.

### Strengths
1. The paper presents an innovative approach by combining two complementary data augmentation strategies: classic transformations and generative model-based data synthesis. This integration effectively leverages both the reliability of traditional augmentation methods and the diversity potential of generative modeling, providing a more comprehensive solution to the data diversity challenge in offline RL.

2. The implementation of diffusion model-based data synthesis in latent space, rather than in high-dimensional observation space, demonstrates significant computational efficiency. This design choice makes the approach more practical and scalable while maintaining effectiveness in generating diverse synthetic data.

3. The paper includes insightful analysis using metrics like Jensen-Shannon divergence to quantify the alignment between training and testing distributions

### Weaknesses
 **Weaknesses**

1. The discussion and analysis of chosen data augmentation techniques in Section 3.2 lacks sufficient depth. The authors should provide empirical evidence for their augmentation choices and properly reference established techniques from online RL literature, such as DrAC[1], SVEA[2], and the comprehensive survey[3]. The current treatment of augmentation strategies is superficial and fails to leverage valuable insights from prior work. Specifically, the paper does not discuss the specific parameters used for each augmentation (e.g., the magnitude of random shifts, the probability of color jitter, the kernel size for blurring), nor does it justify why these specific augmentations were chosen over others. A more thorough analysis would include a discussion of the potential impact of each augmentation on the learning process and how they contribute to improved generalization. Furthermore, the paper should discuss the interaction between different augmentations and how they are combined to maximize the diversity of the training data. The lack of such analysis makes it difficult to assess the effectiveness of the proposed augmentation strategy.

2. The proposed Generalization Performance metric $G_{\text {perf }}=\frac{T_{\text {test }}-B_{\text {test }}}{B_{\text {train }}-B_{\text {test }}}$ needs better justification. A more straightforward approach would be using $T_{\text {train }}/B_{\text {train }}$ to evaluate training effectiveness, while comparing $B_{\text {test }}/B_{\text {train }}$ with $T_{\text {test }}/T_{\text {train }}$ would provide a more natural measure of generalization capabilities. The current metric obscures the individual contributions of training and testing performance, making it difficult to understand the true impact of the proposed method on generalization. For instance, a high $G_{perf}$ could be achieved by a large increase in training performance with a small increase in test performance, or vice versa. A more transparent metric would allow for a clearer understanding of the method's strengths and weaknesses.

3. The experimental results reveal a critical misalignment with the paper's claimed contribution to "Zero-Shot Visual Generalization." The performance improvements predominantly stem from enhanced training performance rather than improved generalization ability, as evidenced by the persistent generalization gap between training and testing environments. This fundamental disconnect between the empirical results and the paper's main thesis requires substantial clarification and resolution for the work to be considered acceptable. The paper should provide a more detailed analysis of the generalization gap, including a discussion of the factors that contribute to it and how the proposed method addresses these factors. It is not sufficient to simply show that the method improves performance; the paper must also demonstrate that it improves generalization specifically.

4. The paper provides insufficient exploration of diffusion model design choices and their impact on performance, lacking crucial ablation studies on model architecture, hyperparameters, and the relationship between latent space dimensionality and generation effectiveness. The paper should include a discussion of the specific architecture of the diffusion model, including the number of layers, the size of the latent space, and the choice of activation functions. Furthermore, the paper should provide a detailed analysis of the impact of different hyperparameters on the performance of the model, such as the learning rate, the number of diffusion steps, and the noise schedule. The lack of such analysis makes it difficult to understand the sensitivity of the method to different design choices and limits the reproducibility of the results.

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors propose a novel data augmentation method to enhance generalization in an offline RL setting.
By training a diffusion model on a set of augmented latent features, the model can subsequently generate additional latent data for offline RL training.
The paper demonstrates that the distribution of the augmented data more closely aligns with the evaluation data distribution, resulting in improved generalization performance.

### Strengths
1) The paper proposes a novel approach to using diffusion models to generate new data for image-based RL.
Augmenting in the latent space helps avoid the overwhelming computational costs associated with both training and inference when using a diffusion model directly on image level.
2) A comprehensive experimental analysis is provided.
3) The paper is clearly written and easy to follow.

### Weaknesses
1) On line 246, I noticed that the _Augmented_ dataset has the same size as the _Baseline_ dataset, whereas the _Augmented Upsampled_ dataset is larger than the _Baseline_ dataset.
This raises the question of whether the performance gain of the _Augmented Upsampled_ dataset over the _Augmented_ dataset is primarily due to the increased amount of augmented data used in training. Given that the diffusion model is trained on the augmented data, the data it generates may follow a similar distribution to the augmented data. So, is there a significant difference between using data augmentation to increase the dataset size versus using a diffusion model to generate additional data? Conducting an additional experiment where the size of the Augmented dataset is increased to match the Augmented Upsampled dataset would help isolate the potential benefits of the diffusion model's data generation.
2) Following the discussion above, the performance of this method might highly depend on the data augmentation used in the first phase. The types of the data augmentation actually decide the data distribution generated by the trained diffusion model. Have you run any ablation study on this?
3) minor: typo on line 137 (invrease).
typo on line 361 (tecnic)

### Questions
1) On line 150, the types of data augmentation used are listed.
Could you please explain why random shift, a common data augmentation used in image-based RL, is not included here?
2) On line 169, both the state $s$ and state $s'$ are augmented by a function called Augment.
Are they augmented by the same image transformation or a randomly sampled image transformation?
3) If I understand correctly, FDD in section 5.5.1 (line 361) refers to including 5% of data that is close to the evaluation distracting dataset.
Is it possible that, by incorporating a small amount of data from the Fixed Distraction Dataset along with the diffusion upsampling process, we could achieve relatively good performance even without the initial data augmentation phase?
Because this small amount of data could be enlarged by the diffusion model.
It will beinteresting to test this hypothesis by comparing the performance of the models trained with different percentages of FDD and diffusion upsampling against the full method.

### Soundness
3

### Presentation
3

### Contribution
3
