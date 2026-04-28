# Mitigating Spurious Bias with Last-Layer Selective Activation Retraining

- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 3, 6, 6, 3

## Abstract
Deep neural networks trained with standard empirical risk minimization (ERM)
tend to exploit the spurious correlations between non-essential features and classes
for predictions. For example, models might identify an object using its frequently
co-occurring background, leading to poor performance on data lacking the correlation. Last-layer retraining approaches the problem of over-reliance on spurious correlations by adjusting the weights of the final classification layer. The success
of this technique provides an appealing alternative to the problem by focusing on
the improper weighting on neuron activations developed during training. However,
annotations on spurious correlations are needed to guide the weight adjustment. In
this paper, for the first time, we demonstrate theoretically that neuron activations,
coupled with their final prediction outcomes, provide self-identifying information
on whether the neurons are affected by spurious bias. Using this information,
we propose last-layer selective activation retraining (LaSAR), which retrains the
last classification layer while selectively blocking neurons that are identified as
spurious. In this way, we promote the model to discover robust decision rules
beyond spurious correlations. Our method works in a classic ERM training set-
ting where no additional annotations beyond class labels are available, making
it a practical and efficient post-hoc tool for improving a model’s robustness to
spurious correlations. We theoretically show that LaSAR brings a model closer to
the unbiased one and empirically demonstrate that our method is effective with
different model architectures and can effectively mitigate spurious bias on different
data modalities without requiring annotations of spurious correlations in data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the issue of spurious correlations in deep neural networks trained with empirical risk minimization (ERM). The authors propose an approach called Last-Layer Selective Activation Retraining (LaSAR), which aims to mitigate spurious bias without requiring group labels or external annotations. The method selectively blocks neurons identified as spurious during the retraining of the last classification layer, thus promoting the model to learn robust decision rules. The authors demonstrate that LaSAR is effective across multiple data modalities, such as vision and text, and improves worst-group accuracy in benchmark datasets.

### Strengths
The proposed LaSAR method aims to achieve robust learning without group information by proposing metrics to evaluate whether a neuron is spurious or core related. This approach makes LaSAR a practical and fully unsupervised solution to mitigating spurious bias.

### Weaknesses
 - Limited Theoretical Analysis: While the empirical results are promising, the theoretical foundation for why the proposed spuriousness score works effectively in all cases is very limited. Including more rigorous analysis or theoretical guarantees would strengthen the paper's claims about the effectiveness of LaSAR.
- Limited Heuristic Exploration: There is limited heuristic exploration of the distribution of the proposed spuriousness score. Figure 4 appears to be cherry-picked, and it would be more persuasive if the authors could provide the distribution of the proposed spuriousness score across neurons in different datasets.
- Incremental Contribution: The phenomenon that spurious neurons and core neurons can be separated has been demonstrated in prior work [1][2]. Moreover, the proposed spuriousness score is calculated as the median among misclassified samples and the median among correctly classified samples, which appears equivalent to retraining the last layer while up-weighting the incorrect samples. This limits the novelty of the contribution. Furthermore, the neuron masking algorithm assumes that a neuron can represent part of the spurious features, which is a strong assumption that may not always hold true. Additionally, it is unclear why masking the last layer is necessarily better than masking a middle layer.
- JTT Algorithm Classification: JTT is listed as a semi-supervised algorithm at line 362, but it appears to work without group information. This classification should be corrected.

### Questions
Distribution of Spuriousness Scores: Could the authors show the distribution of the proposed spuriousness scores across neurons in different datasets? This would help validate the claim that the spurious and core neurons can be effectively separated.

Difference from Retraining with Up-Weighting: What is the difference between the proposed algorithm and retraining the last layer while up-weighting the misclassified samples? Clarifying this would help in understanding the distinct contribution of the proposed method.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Last-layer Selective Activation Retraining (LaSAR), which identifies and mitigates spurious bias without requiring external supervision or group labels. The key point lies in observing that neuron activations combined with prediction outcomes can self-identify spurious features, and then using this information to selectively block spurious neurons during last-layer retraining. The method works as a practical post-hoc tool in standard ERM training settings, and requires no additional annotations beyond class labels. Authors compare their method with competitive baselines such as JTT, and DFR and show some improvement in worst group accuracy on a benchmark with 4 datasets.

### Strengths
Key Strengths:

1. Spurious neuron identification: The proposed LaSAR framework introduces an interesting approach to identify spurious neurons using activation patterns and prediction outcomes, providing a self-guided mechanism for bias detection.

2. Practical Utility: The method works as a post-hoc tool in standard ERM training settings, making it highly practical for real-world applications.

### Weaknesses
1. The contribution of this paper is severely limited. Indeed, the core intuition that using (i) misclassified examples of validation data, (ii) and retraining all layers or the linear head to reduce reliance on spurious features has been demonstrated previously with methods such as JTT and AFR. How is LaSAR fundamentally different from AFR? 

2. Lack of fair comparison. Although JTT and AFR need group information on the validation data only to tune hyper-parameters. They can be tuned using the worst-class accuracy. Authors should therefore compare their method with JTT and AFR when tuned on worst-class accuracy.

3. No theoretical guarantees are provided about the convergence and stability of the selective activation retraining process, even on synthetic data.

### Questions
1. How does the method ensure that it doesn't accidentally block neurons representing valid but complex feature combinations rather than truly spurious correlations?
2.  How does the method handle cases where features might be spurious in some contexts but valid in others?
3. (Also related to 1.) There has been evidence that neurons may learn polysemantic features. What is the impact of LaSAR in case neurons may learn linear combinations of spurious and core features?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, the authors propose a novel method to self-identify spurious features and mitigate the spurious bias by retraining the last classification layer. In general, the idea of using neuron activations before the last classification layer, coupled with their final prediction outcomes, to provide self-identifying information on whether the neurons represent spurious features seems interesting.

### Strengths
The authors did extensive experiments.

### Weaknesses
The writing in some places is unclear, in particular, they did not clearly explain the behind reasoning of the proposed method to identify the spurious features. The did not use some theoretical results to support the proposed method.

The authors defined the spuriousness score as (5), but the rationale behind this definition is not clearly explained. It is not immediately obvious why the difference between $\mu_{\text{mis}}$ and $\mu_{\text{cor}}$ would indicate a spurious feature. The connection between this score and the actual identification of spurious features needs more justification. In line 157, the authors mentioned that WGA is the accuracy on the worst performing data group in the test set $\mathcal{D}_{test}$. However, they used argmax in the formula of WGA, which is problematic since argmax will output a group label rather than the value of accuracy, and the argmax will output the best performing data group in terms of accuracy rather than the worst performing data group.

In Section 3.2, they used a synthetic motivating example. It may be better to use a real motivating example to demonstrate the practical relevance of the problem. Additionally, in line 321, the authors may want to say "equation (6) and equation (7)" rather than equation 6 and equation 7.

I think the study objective in this paper is quite similar to variable selection in statistics. We can use many penalties such as L1 penalty to remove those spurious features. I do not see the advantages of the proposed method compared with those variable selection methods in statistics. The authors may need to discuss this point.

### Questions
1, why did you define the spuriousness score as (5)? To help readers understand the behind rationale, I think the authors may need to add more explanation.

2, In line 157, the authors mentioned that WGA is the accuracy on the worst performing data group in the test set $\mathcal{D}_{test}$. However, they used argmax in the formula of WGA, it seems problematic since argmax will output a group label rather than the value of accuracy and the argmax will output the best performing data group in terms of accuracy rather than the worst performing data group. 

3, In Section 3.2, they used a synthetic motivating example. It may be better to use a real motivating example.

4, In line 321, the authors may want to say "equation (6) and equation (7)" rather than equation 6 and equation 7.

5, I think the study objective in this paper is quite similar to variable selection in statistics. We can use many penalties such as L1 penalty to remove those spurious features. I do not see the advantages of the proposed method compared with those variable selection methods in statistics. The authors may need to discuss this point.

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
4

### Summary
In this work, authors propose a debiasing method that works by retraining only the last layer (classification layer) in order to re-weight different factors in the latent representation. The assumption is that latent factors carry different information (source, spurious, noise) which can be effectively filtered out from the classification layer by reweighting. They test their method on standard debiasing benchmarks such as celeba, waterbirds, multinli and civil comments.

### Strengths
- The paper tackles a very important issue, which is learning unbiased models from biased data. 
- The proposed method does not need any kind of annotation on the bias, and it just leverages the class label (unsupervised debiasing)
- The reported results show improvement w.r.t other methods

### Weaknesses
Here are my main concerns about the work:

- The authors' assumption is that latent representation can be factorized in source, spurious and noise components. This is clearly shown in the toy example; however it is not clear why this should also happen in representations extracted from deep neural networks on complex data. It might not be so simple to factor out single components in the learned representations, as they might be intertwined and correlated. Can you provide some more theoretical backing of this method?

- I think that validation on more difficult datasets such as 9-Class ImageNet / ImageNet-A (https://openreview.net/forum?id=2OqZZAqxnn) should be added to the experimental validation.

- The related work section should be updated a bit with relevant works in the area (e.g. [1-6])

[1] Bahng, Hyojin, et al. "Learning de-biased representations with biased representations." International Conference on Machine Learning. PMLR, 2020.

[2] Tartaglione, Enzo, et al. "End: Entangling and disentangling deep representations for bias correction." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2021.

[3] Y.-K. Zhang, Q.-W. Wang, D.-C. Zhan, and H.-J. Ye, “Learning debiased representations via conditional attribute interpolation” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2023.

[4] Barbano, Carlo Alberto, et al. "Unbiased Supervised Contrastive Learning." ICLR. 2023.

[5] Zhang, Yi, et al. "Poisoning for Debiasing: Fair Recognition via Eliminating Bias Uncovered in Data Poisoning." ACM Multimedia 2024. 2024.

[6] Wang, Yining, et al. "Navigate Beyond Shortcuts: Debiased Learning through the Lens of Neural Collapse." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.


### Questions
- Could also provide results in terms of balanced accuracy (other than accuracy and WGA)? 
- I think that retraining on a part of the validation set may lead to "unfair" comparison with baseline methods that are not trained also on validation data
- Reweighting the classification layer essentially does not "remove" the bias from the whole model, but it is just a correction. Do you think this might be an issue in certain cases?
- I do not see a clear difference between core activation maps and spurious activations maps for CelebA in Fig. 4., the spurious heatmaps even seem a bit more focused on the hair (which is the target task). 
- Using your method do you think it would be possible to provide pseudo-labels for the training data in order to use a supervised debiasing method?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a new method for mitigating spurious bias in an unsupervised fashion. 

It tries to detect non-essential features based on the pattern of errors, mask them away, and retrain the last layers. The method is compared against other methods in image and text datasets.

### Strengths
The paper deals with a relevant problem. It proposes a new method that is, to the best of my knowledge original. And presents an evaluation in relevant benchmarks.

### Weaknesses
My main concern is that I find the motivation for the method not very strong. I believe the authors don't provide strong evidence for the main assumptions that motivate the methods.

Particularly, core assumptions for the method are that
1.  some features in the latent embedding that are responsible for encoding the *spurious correlation are confined to single neurons*, and can be masked away. It is a bit unclear to me whether this is true. For instance, maybe some component that is not entirely aligned with any specific neuron could be responsible for encoding this spurious feature.
2. spurious features can be distinguished from core features by looking at the error density. And while the toy example motivates this, It seems the pattern we see in Fig2(b) for spurious vs core features is very different from what we see in Fig 4.
Overall, I think these are two very important assumptions of the method that should be more clearly demonstrated

### Questions
Some minor concerns.
- I don't understand, why not provide visualizations using linear dimensionality reduction for the motivating example (section 3.2), since you are using a linear model. Using T-SNE somehow confuses the example
- How were the baselines implemented? are they openly available (it could make sense to provide the links) or did you re-implemented them
- How many spurious features were masked away in each of the examples

### Soundness
2

### Presentation
3

### Contribution
2
