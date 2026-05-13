# Online Reward-Weighted Fine-Tuning of Flow Matching with Wasserstein Regularization

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Recent advancements in reinforcement learning (RL) have achieved great success in fine-tuning diffusion-based generative models. However, fine-tuning continuous flow-based generative models to align with arbitrary user-defined reward functions remains challenging, particularly due to issues such as policy collapse from overoptimization and the prohibitively high computational cost of likelihoods in continuous-time flows. In this paper, we propose an easy-to-use and theoretically sound RL fine-tuning method, which we term Online Reward-Weighted Conditional Flow Matching with Wasserstein-2 Regularization (ORW-CFM-W2). Our method integrates RL into the flow matching framework to fine-tune generative models with arbitrary reward functions, without relying on gradients of rewards or filtered datasets. By introducing an online reward-weighting mechanism, our approach guides the model to prioritize high-reward regions in the data manifold. To prevent policy collapse and maintain diversity, we incorporate Wasserstein-2 (W2) distance regularization into our method and derive a tractable upper bound for it in flow matching, effectively balancing exploration and exploitation of policy optimization. We provide theoretical analyses to demonstrate the convergence properties and induced data distributions of our method, establishing connections with traditional RL algorithms featuring Kullback-Leibler (KL) regularization and offering a more comprehensive understanding of the underlying mechanisms and learning behavior of our approach. Extensive experiments on tasks including target image generation, image compression, and text-image alignment demonstrate the effectiveness of our method, where our method achieves optimal policy convergence while allowing controllable trade-offs between reward maximization and diversity preservation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work introduces a way to finetune conditional flow matching models to maximize some user-defined reward function. Specifically, the paper combines two techniques: (1) reward-weighted conditional flow matching; and (2) a constraint that bounds the pretrained model and the finetuned model. The work gives some theoretical analyses to justify the proposed method is grounded and some experiments also show its effectiveness.

### Strengths
- The problem of finetuning conditional flow matching models is of general interest to the community. How to preserve the generation diversity and avoid model collapse is a challenging problem.

- Combining the reward-weighted matching loss and the Wasserstein distance regulatization seems to be empirically effective. The experimental results look good.

- There are quite a few theoretical justifications for the proposed method. Although I didn't check carefully, I find them to be quite reasonable claims.

### Weaknesses
 - The contribution of the paper seems ad-hoc to me. There is quite little connection between the reward-weighted matching loss and the Wasserstein regularization. I find both techniques independent of each other, so I find the motivation of the work quite weak. Could the author elaborate more on why these two techniques should be used together (other than empirically well-performing)?

- Given that the reward-weighted matching loss and the Wasserstein regularization are unrelated contributions, I will be interested to see how much gain each individual component contribute to the performance gain? Could the authors conduct some ablation study?

- I find it less convincing for the performance gain, since there is no compelling baselines for comparison. For example, the paper claims that the Wasserstein regularization performs well. How about other discrepancy measure? How is the Wasserstein distance a good choice here? I think more discussion on the motivatiojn will help the reader gain more insights. 

- Whlle I am no expert in this domain, I am wondering whether there are other stronger baselines to compare to. The problem this paper studies doesn't seem to be new, so I think there will be some other finetuning methods for comparison, say [Imagereward: Learning and evaluating human preferences for text-to-image generation, NeurIPS 2023].

- The experiments are relatively small-scaled. I don't know how the proposed method scales with the size of the model/dataset. Could the authors conduct some experiments to study the scaling performance of this finetuning technique?

### Questions
See the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a method to perform reward finetuning of flow-based models. The idea starts with the reward-weighted version of the standard flow matching loss (i.e., doing simple importance sampling) and, to remove the dependency on pretraining datasets and to perform online training, changes the sampling distribution from the original data distribution to the finetuned sampling policy. Such a strategy proves very prone to overfitting, as the finetuned distribution collapses into a single mode if it is trained for too many epochs. Therefore, the authors further proposes to regularize the sampling policy to be not too far away from the pretrained one (using a Wasserstein distance). The paper discusses some theoretical results like the asymptotic behaviors of the proposed methods and empirically show that the proposed method can be applied to finetuning of flow matching models pretrained on MNIST and CIFAR-10.

### Strengths
The paper theoretically analyzes probably one of the most intuitive methods of reward reweighting, and by introducing a regularization loss on the finetuned distribution, shows that this naive method can be extended to the online setting. To support the claims, the paper does sufficient amount of experiments on different small-scale image datasets and different reward functions. Especially, the paper shows that their online variant is better than the offline one.

Compared to baselines like DDPO that requires one specify the number of sampling steps for finetuning, the proposed method finetunes a model in the way very similar to flow matching -- to sample images from a "data" distribution and some random t in [0,1], and to compute the matching loss.

### Weaknesses
The paper does not compare the proposed method against any other methods, for instance DDPO (running PPO for diffusion finetuning). While one may argue that DDPO is not designed for continuous flow models, one eventually samples from CNFs with some discretization and can therefore construct an MDP for DDPO finetuning, and not to mention some more recent methods. On flow matching, there is a very recent paper [1] that does reward finetuning for flow matching (though this paper should be considered as a concurrent one). There also exist some more recent papers for reward finetuning to compare with, and I feel that showing at least one of them will be great.

The proposed method seems to be a bit sensitive (in theory) to hyperparameter tuning due to its online nature. It is a bit unsatisfactory that the resulted distribution (Eqn 12 in the paper) is dependent on the number of epochs. While in practice it is not a super big concern, an objective that guarantees convergence to a specific distribution (e.g. P_pretrained(x) * exp(lambda * r(x)) / Z) is generally considered better.

Many of the baselines are tested on large-scale models like StableDiffusion, and many of them can converge in a reasonably fast speed on simple reward functions like Aesthetic Score used in DDPO. The paper fails to show results in these more realistic settings (though it probably requires some compute, but one might be able to find a smaller model to do experiments).



### Questions
Besides the points raised in the weakness section:

1. It is probably better to also show quantitative metrics like diversity scores (e.g., feature pairwise distances) and FID scores.
2. In Eqn 10, it is probably more aesthetic to write \theta_\text{ft} and \theta_\text{ref} (for the subscripts), instead of \theta_{ft} and \theta_{ref}.
3. W2 distance is great, but I wonder if it makes a big difference if one instead uses KL divergence (both theoretically and empirically).

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
4

### Summary
The paper introduces a new online reinforcement learning (RL) fine-tuning method for continuous flow-based generative models, named Online Reward-Weighted Conditional Flow Matching with Wasserstein-2 Regularization (ORW-CFM-W2). It addresses the challenges of policy collapse and high computational costs associated with traditional fine-tuning methods. The authors propose integrating RL within the flow matching framework, utilizing an online reward-weighting mechanism to focus on high-reward regions and a Wasserstein-2 distance regularization to balance exploration and exploitation. The paper provides theoretical analyses and empirical results across various tasks, demonstrating the effectiveness of the proposed method in achieving optimal policy convergence with controlled trade-offs between reward maximization and the generation capacity.

### Strengths
1.The paper effectively identifies and addresses some key issues in fine-tuning continuous flow-based generative models, such as policy collapse and computational inefficiency.
2. The introduction of the online reward-weighting mechanism and Wasserstein-2 distance regularization is well-suited for flow matching models that balances exploration and exploitation, mitigating the policy collapse problem.
3. The theoretical analyses are rigorous and provide a solid foundation for the proposed method. The empirical results across various tasks are convincing and demonstrate the method's effectiveness.

### Weaknesses
Potential Overemphasis on Theoretical Analysis:
While the theoretical underpinnings are robust, the paper might overly focus on the theoretical aspects at the expense of practical considerations. Balancing the presentation (e.g.section 4.6 to the appendix) to include more  case studies could make the findings more relatable to a broader audience. Specifically, the paper could benefit from a more detailed exploration of how the method performs across different types of reward functions, and how sensitive the performance is to the choice of hyperparameters in the W2 regularization. The current presentation leaves the reader wondering about the practical trade-offs and limitations of the proposed approach in real-world scenarios.
Lack of Comparative Analysis with Other Regularization Techniques:
The paper introduces W_2 distance regularization but does not compare its effectiveness with other potential regularization methods. Including such comparisons could strengthen the paper's contribution by positioning it within the broader landscape of regularization strategies. For example, a comparison with KL divergence regularization, if feasible, or other distance metrics like W1, would provide valuable insights into the unique benefits of the chosen W2 regularization. The paper should also discuss the computational cost and implementation complexity of W2 regularization compared to alternatives.
Narrow Empirical Validation:
The empirical validation is commendable, but the paper could benefit from testing the method across a wider range of datasets (e.g. CeleA face dataset) and tasks to further establish the generalizability and robustness of the approach. The current set of experiments, while demonstrating the method's potential, does not fully explore its limitations and applicability across diverse data distributions and task complexities. More extensive experiments, including those with higher dimensional data and more complex reward functions, would be beneficial.

### Questions
1. What kind of reward functions can be fine-tuned without collapsing by the proposed W_2 regularization method?  
2. Is this method capable of performing fine-grained fine-tuning tasks, such as controlling specific semantic parts of images?
3. Why not use W_1 distance for regularizing?

### Soundness
3

### Presentation
2

### Contribution
2
