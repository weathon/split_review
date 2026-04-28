# A Recipe for Improved Certifiable Robustness

- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 6, 8

## Abstract
Recent studies have highlighted the potential of Lipschitz-based methods for training certifiably robust neural networks against adversarial attacks.
A key challenge, supported both theoretically and empirically, is that robustness demands greater network capacity and more data than standard training. 
However, effectively adding capacity under stringent Lipschitz constraints has proven more difficult than it may seem, evident by the fact that state-of-the-art approach tend more towards \emph{underfitting} than overfitting.
Moreover, we posit that a lack of careful exploration of the design space for Lipshitz-based approaches has left potential performance gains on the table.
In this work, we provide a more comprehensive evaluation to better uncover the potential of Lipschitz-based certification methods.
Using a combination of novel techniques, design optimizations, and synthesis of prior work, we are able to significantly improve the state-of-the-art VRA for deterministic certification on a variety of benchmark datasets, and over a range of perturbation sizes.
Of particular note, we discover that the addition of large ``Cholesky-orthogonalized residual dense'' layers to the end of existing state-of-the-art Lipschitz-controlled ResNet architectures is especially effective for increasing network capacity and performance.
Combined with filtered generative data augmentation, our final results further the state of the art deterministic VRA by up to 8.5 percentage points.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper improves L2 deterministic certifiably robust training from three aspects: 1) adding additional layers; 2) using Cholesky-based orthogonal layers in the neck; 3) data augmentation with a newer diffusion model.

### Strengths
* By combining technical improvements on three aspects as mentioned in the summary, the paper shows a significant empirical improvement over previous works across all the datasets (e.g., +8% on CIFAR-10). 
* This work provides suggestions on better settings for the robust training, in terms of model architecture with additional layers, building orthogonal layers with Cholesky decomposition, and data augmentation with a newer diffusion model.

### Weaknesses
 * The paper looks like manually searching for settings (model architecture, orthogonal layers, diffusion model). It has engineering merits. But it does not have much novel contribution by adding more dense layers and replacing the diffusion model already used in Hu et al,, 2023 with a newer diffusion model.
* The benefits of the best choices found by the paper are not well explained. For example, the paper only explains that the Cholesky-base orthogonalization is more numerically stable and faster, but it does not explain why it can improve VRA. Therefore, the paper provides limited insights, in its current form.
* I think adding additional dense layers to improve the capacity is very straightforward. The authors mentioned that "Using orthogonalized dense layers turns out to be non trivial in our experiments". But there are many existing works on orthogonalized layers. By looking at the comparison with the existing methods in Table 3, the newly proposed Cholesky-based Orthogonal Layer doesn't seem to be much better than the existing methods. Therefore, I think the empirical improvement of this paper mainly comes from relatively trivial parts (especially adding additional layers), not others such as how to use orthogonalized dense layers in a new way.

### Questions
* How does the Cholesky-base orthogonalization help on VRA?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The work proposed some new architectures to enhance the certified robustness of neural network by reducing the Lipschitz constant. Empirical experiments showed some improvement.

### Strengths
1. This work studies the limitation for Lipschitz-based certification and proposed new architectures to mitigate the issue.
2. Strong empirical result: experiments showed noticeable improvement over the baseline models.

### Weaknesses
The authors need to include some intuitions when designing the layers.

### Questions
Can the authors include training time and inference time for the new architecuture?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
It provides a more comprehensive evaluation to better uncover the potential of Lipschitz-based certification methods. Using a combination of novel techniques, design optimizations, and synthesis of prior work, it is able to improve the state-of-the-art VRA for deterministic certification on a variety of benchmark datasets, and over a range of perturbation sizes.

### Strengths
It finds that an apparent limitation preventing prior work from discovering the full potential of Lipschitz-based certification stems from the framing and evaluation setup. Specifically, most prior work is framed around a particular novel technique intended to supersede the state-of-the-art, necessitating evaluations centered on standardized benchmark hyperparameter design spaces, rather than exploring more
general methods for improving performance (e.g., architecture choice, data pipeline, etc.).


It discovers that the addition of large “Cholesky-orthogonalized residual dense” layers to the end of existing state-of-the-art Lipschitz-controlled ResNet architectures is especially effective for increasing network capacity and performance. 

This work provides a more comprehensive evaluation to illuminate the potential of Lipschitz-based certification methods. It finds that by delving more thoroughly into the design space of Lipschitz-based approaches, it can improve the state-of-the-art VRA for deterministic certification significantly on a variety of benchmark datasets, and over a range of perturbation sizes. Combined with filtered generative data augmentation, the final results further the state of the art deterministic VRA by up to 8.5 percentage points.

It provides an overview of the existing methods used for controlling the Lipschitz constant during training, and propose its own method that can be combined with other approaches.

It discusses the role data augmentation plays in training high-capacity models. It covers DDPM, which prior work has found helpful for certified training, and proposes an alteration to the typical augmentation strategy that further boosts performance.

### Weaknesses
In section 4.3, it seems to mainly discuss the comparison with RS based methods. But Table 5 shows several other works which can achieve better performance. It is better to also discuss the comparison with these works. Currently it seems that table 5 only shows the results without detailed discussions for these works.

### Questions
see the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
