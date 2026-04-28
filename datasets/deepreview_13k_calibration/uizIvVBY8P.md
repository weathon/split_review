# Continual Supervised Anomaly Detection

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
This paper proposes a continual-learning method for anomaly detection when a few labeled anomalies are available for training in addition to normal instances. Although several continual-learning methods have been proposed for anomaly detection, they have been dedicated to unsupervised anomaly detection, in which we can use only normal instances for training. However, few anomalies, which are valuable for constructing anomaly detectors, are often available in practice. In our continual-learning method, we use a hybrid model of a Variational AutoEncoder (VAE) and a binary classifier, and compute the anomaly score from the outputs of both models. The VAE is trained by minimizing the reconstruction errors of training data to detect unseen anomalous instances, and the binary classifier is trained to identify whether the input is a seen anomaly. Combining these two models enables us to efficiently detect both seen and unseen anomalies. Furthermore, the proposed method generates anomalous instances in addition to normal instances for generative replay to reduce the negative effects of catastrophic forgetting. In generative replay, anomalous instances are more difficult to generate than normal instances because few anomalous instances are available for training in anomaly detection. To overcome this problem, we formulate the generation of anomalous instances as an optimization problem, in which we find a latent vector of the VAE corresponding to anomalous instances, and generate anomalies by solving it using gradient descent. Our experimental results show that the proposed method is superior to anomaly detection methods using conventional continual learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a method for semi-supervised anomaly detection in the setting of continuous learning. They combine a binary classifier for the labeled anomalies together with a VAE reconstruction score for the anomaly detection part. The continuous learning is addressed by, one, using the latent space of the VAE to sample data from past tasks, and, two, using the gradient of the binary classifier to sample labeled anomalies in the same latent space via iteration from a starting point.

### Strengths
The paper is easily readable.
They perform experiments on various types of datasets. 
They perform an ablation study.

### Weaknesses
It represents a straightforward combination of ideas.
The argument that one cannot keep data due to privacy reasons also applies for resampling data from an autoencoder. If it is a very good reconstruction, it would equally cause privacy issues.
The important and relevant case of slow distribution shift is only partially addressed, via the credit data. Doing so in more and more controllable settings would be of interest.
A comparison against reusing past training data would be of interest - in particular from tasks a few epochs ago. Reason being that a slow shift of parameters would also affect sampling of data from not so recent past tasks.
MNIST and FMNIST might be too simple as problem. A more complex image dataset is missing.

### Questions
NA

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new approach to the task of continual supervised anomaly detection. This paper designs a pipeline with three specific components: a variational autoencoder, a binary classifier, and an anomaly generation mechanism. This paper conducts experiments on five datasets to validate performance.

### Strengths
•	This paper proposes a new pipeline for continual supervised anomaly detection that aligns well with the practical application needs.
•	 The performance gains for AUC on five datasets look good, especially on the FMNIST and MNIST datasets.

### Weaknesses
•	The novelty of the proposed framework is limited. The overall network architecture consists of a VAE and a classifier without any particularly unique components.

•	This paper does not include a comparison with some of the latest supervised anomaly detection methods such as DRA[1], PRN[2], BGAD[3], which might be relevant for a more comprehensive evaluation.

### Questions
Is there a more detailed explanation regarding the impact of the number of seen anomalous samples on the experimental results?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Many anomaly detection papers assume that only normal instances are present in the training, and train the model unsupervised.
However, in the real world, there are situations where even a few labeled abnormal instances are available.
In this case, studies have shown that even a very small number of anomalies can significantly improve the performance of the detector.
In addition, anomaly detectors are often trained under the assumption that the data distribution is stationary, but in real-world deployments, the distribution changes over time.
Therefore, the authors propose a supervised anomaly detection method using continual learning.
The method consists of a Variational AutoEncoder (VAE) and a binary classifier.
The VAE uses the reconstruction error to determine whether the input data is an unseen anomaly, and the binary classifier determines whether the input data is a seen anomaly, and calculates the anomaly score by aggregating the results of both models.
In addition, the VAE's decoder is used to generate data, which is then used for generative replay to prevent catastrophic forgetting in continual learning.

### Strengths
- The paper is well organized and the notation is easy to follow.
- The structure of the model and the organization of the methods (such as loss) are theoretically clean and natural. The authors naturally integrated supervised anomaly detection with continual learning.
- The proposed method works with various types of input data, such as images and tabular data.
- It is impressive that the method utilizes CVAE and a binary classifier to learn the process of generating rare abnormal instances by gradient descent, which is then used for generative replay.

### Weaknesses
The main weakness is that experimental results do not sufficiently support the superiority of this method.

- On tabular datasets such as UNSW, bank, and credit, the model does not significantly outperform the other baselines. In many cases, the performance is similar to that of the binary classifier, suggesting that the performance is due to the binary classifier included in the method rather than the proposed method. It is unclear if the VAE component contributes meaningfully to the overall performance on these datasets. The reported results lack a detailed ablation study that would isolate the impact of the VAE and the continual learning aspects from the binary classifier.
- The experimental baselines are too simple. BC and VAE are components of the proposed method, and there are many methods that might outperform DevNet and Deep SAD, at least in the image domain (Liu et al., 2023). Many anomaly detection methods in the image domain are not designed for continual learning, but since EWC and A-GEM can be applied, it would be meaningful if the proposed method outperforms in this setting. The choice of baselines does not adequately challenge the proposed method, especially in the image domain, where more sophisticated anomaly detection techniques exist. The comparison should include methods that also incorporate generative models or contrastive learning techniques.
- In the image domain, the proposed method shows better performance than other baselines, but it seems that experiments on larger datasets are needed to show the practicality of the proposed method. The method was only tested on FMNIST and MNIST with MLP structure, but it would be useful to test it on larger datasets such as CIFAR10 and CelebA. The use of simple datasets and architectures limits the generalizability of the findings. The experiments should be extended to more complex image datasets and convolutional neural network architectures to demonstrate the method's effectiveness in more realistic scenarios.

### Questions
- Similar to other continuous-learning papers, it would be nice to be able to see how performance changes with additional training on each task.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
