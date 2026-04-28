# AutoJoin: Efficient Adversarial Training against Gradient-Free Perturbations for Ro- bust Maneuvering via Denoising Autoencoder and Joint Learning

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
With the growing use of machine learning algorithms and ubiquitous sensors, many `perception-to-control' systems are being developed and deployed. To ensure their trustworthiness, improving their robustness through adversarial training is one potential approach. 
We propose a gradient-free adversarial training technique, named \model{}, to effectively and efficiently produce robust models for image-based maneuvering. 
Compared to other state-of-the-art methods with testing on over 5M images, \model{} achieves significant performance increases up to the 40\% range against perturbations while improving on clean performance up to 300\%. 
\model{} is also highly efficient, saving up to 86\% time per training epoch and 90\% training data over other state-of-the-art techniques. 
The core idea of \model{} is to use a decoder attachment to the original regression model creating a denoising autoencoder within the architecture. 
This architecture allows the tasks `maneuvering' and `denoising sensor input' to be jointly learnt and reinforce each other's performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a novel approach to enhancing the robustness of 'perception-to-control' systems, which are increasingly prevalent due to the integration of machine learning algorithms and ubiquitous sensors. The proposed method, AutoJoin, is a gradient-free adversarial training technique specifically designed for image-based maneuvering tasks. AutoJoin stands out from other state-of-the-art methods, demonstrating significant performance improvements when tested on a substantial dataset of over 5 million images. The technique showcases up to a 40% increase in performance against perturbations, while also achieving a remarkable 300% improvement in clean performance. This indicates that AutoJoin not only enhances the system's resilience against adversarial attacks but also boosts its overall effectiveness in standard operating conditions. In terms of efficiency, AutoJoin proves to be highly advantageous, saving up to 86% of the time per training epoch and requiring 90% less training data compared to other leading techniques. This efficiency makes AutoJoin a practical choice for real-world applications, where resources and time are often limited. The core innovation of AutoJoin lies in its unique architecture, which incorporates a decoder attachment to the original regression model, resulting in a denoising autoencoder integrated within the system. This design enables the simultaneous and synergistic learning of both maneuvering and denoising sensor input tasks. As a result, the performance of each task is enhanced, leading to a more robust and reliable 'perception-to-control' system. In conclusion, AutoJoin emerges as a groundbreaking technique in the field of adversarial training, offering substantial improvements in both performance and efficiency. Its unique architecture and gradient-free approach make it a promising solution for developing trustworthy 'perception-to-control' systems, capable of operating effectively in diverse and challenging environments.

### Strengths
-- AutoJoin is a gradient-free adversarial training technique.

-- AutoJoin  achieves significant performance increases up to the 40% range against perturbations while improving on clean performance up to 300%.

--AutoJoin is also quite efficient in computation cost, saving up to 86% time per training epoch and 90% training data over other state-of-the-art techniques.

-- The paper is well written and easy to follow.

### Weaknesses
Main weakness is from how the robustness is evaluated. In verifying the robustness, it would be better to explore more types of perturbations. Such perturbations could be from both common image manipulations and adversarial perturbations. Although several image corruptions are applies, they mainly focus on color perspective. What will happen if other types of image corruptions, such as image rotation, perspective warping, JPEG compression. Such robustness evaluation can be referred from [1]

[1]. Xinhua et al. Only For You: Deep Neural Anti-Forwarding Watermark Preserves Image Privacy. 2023

In addition, such evaluation can also be executed  on adversarial perturbation, such as from FGSM, PGD, Autoattack etc.  

Several minor issue:

There are some typos need to pay attention. For instance, the first sentence in introduction, "have"-->"has".

In the conclusion section, the citation is incomplete. Line 5: a full stop is missing at the end of a sentence.

### Questions
-- Adversarial training is largely dependent on how the images are perturbed, which determines how the adversarially trained model will generalize its robustness. The FID is used only minimally to determine the maximum intensity value of a perturbation. What will happen or be expected if perturbations are kept consistent with [Shen et al, 2021] and [Bengio et al 2009]?

-- Given the mentioned possible add-on evaluations, the transferability of claimed adversarial robustness can be further tested?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to improve the perception robustness of a self-driving system. Specifically, this paper propose a joint learning method, to regress the learning target and to reconstruct the clean image at the same time. With solid evaluation, the proposed method can significantly improve the robustness of the model.

### Strengths
The experiments of this paper is solid. The experiments are conducted on a number of datasets, and compared with a number of methods to improve model robustness.

This research topic is very interesting, and aligns well with the real world needs. Before this paper, I didn't see many papers working on this topic.

### Weaknesses
 There is no enough context information about the task this paper working on. Predicting steering angle from camera image seems not a very popular task, so it is worth introduce this a little bit more.

It is very interesting to see the sensitivity of the hyper-parameters. IIUC, if we set the weights of the reconstruction loss as 0, I suppose the performance will regress back to Standard (FSRI). Please correct me if my understanding is wrong.

For equation (1), I am wondering what's the reason why we times $\lambda_1$ with $l_2$, and times $\lambda_2$ with $l_1$? It seems very counter intuitive so would like to learn the reason.

Looks like the proposed method is not specifically design for the steering angle prediction task, so I am wondering why choose this task, and if the propose method can benefit other self-driving related tasks.

### Questions
See weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper is on the topic of robust maneuvering in view of autonomous driving. The authors propose to augment the training images with gradient-free perturbations. Furthermore, they propose to regularize the model training by adding a denoising task where a decoder should reconstruct the original images without the gradient-free perturbations.

### Strengths
Overall, the paper is clear. A wide range of experiments are conducted to support their claim, including experiments on several datasets, an ablation study, and experiments showing that gradient-free perturbation and denoising auto-encoder regularization are helpful in improving performance.

### Weaknesses
More analysis regarding why the proposed method works is important. For high-level tasks, adding a task of reconstructing the input image or its variant usually degrades the performance on clean data.

Besides, the limitations of this paper discussed at ICLR 2013 seem to still exist, and there seem no significant changes from the last submission.

### Questions
Please see the weakness part

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper propsoed a joint training to imporve the roboustness of image-based maneuvering models. The proposed method improve the roboustness of the two modules jointly, the decoder and steering angle prediction model.

### Strengths
The paper focuses on an interesting and important issue of deep nueral networks, especially for autnomous driving systems.

### Weaknesses
There are several issues with the paper:
1- The issue of adversarial attack is well-known in the field. However, it is not well explained how this issue might be the case for application discussed in the paper. I think it is important to provide real-world scenarios for this purpose.
2- The proposed method has not been evalauted on general benchmarks and as such it is difficulat to understand the effectivenss of the proposed method.
3- There are several new state-of-the-art adversarial defense mechanisms in the field currently, and they are missed to be included in the paper.
4- It is diffult to understand what is the main novelity of the proposed method.

### Questions
1- How deoes this problem might take palce in real-world scenarios?
2- How does the proposed method comapred with state-of-the-art adversarial training and defence mechanisms?
3- What is the main novelity of the propsoed method? new perturbation training or proposing a new roboust model for steer angle prediction?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
