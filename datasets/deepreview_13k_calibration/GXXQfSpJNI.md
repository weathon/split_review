# Fair Image Generation from Pre-trained Models by Probabilistic Modeling

- Decision: Reject
- Avg Score: 2.33
- Scores: 1, 3, 3

## Abstract
The production of high-fidelity images by generative models has been transformative to the space of artificial intelligence. Yet, while the generated images are of high quality, the images tend to mirror biases present in the dataset they are trained on. While there has been an influx of work to tackle this issue, existing works typically rely on fine-tuning an existing generative model which requires costly retraining time. In this paper, we use a family of tractable probabilistic models called probabilistic circuits (PCs), which can be equipped to a pre-trained generative model to produce fair images without fine-tuning. We show that for a given trained generative model, our method only requires a small fair reference dataset to train the PC, removing the need to retrain the generative model on a large dataset. Our experimental results show that the proposed method achieves a balance between training resources and ensuring fairness and quality of generated images.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper address the problem of fair image generation - controlling a pre-trained model to generate balanced sets of images w.r.t. certain sensitive attributes - following a reference dataset. They propose to use  probabilistic circuits (PCs) to learn the distribution of a reference fair dataset. From the learned PC, they can sample fairly the latent embeddings to generate fair distributions.

### Strengths
Ensuring fairness in generative model is critical.
The writing is easy to follow, for the most part. 
The proposed method is fairly simple.

### Weaknesses
The overall quality of the paper is quite low due to several critical issues:

- Presentation and Clarity: The paper's presentation requires significant improvement to enhance clarity. Specifically:

1) There is no clear  motivation for the use of PC and why it is particularly relevant for the task.  What advantages does it offer over existing methods that also aim to learn the distributions of fair latent codes, such as Gaussian Mixture Models (GMM)? Furthermore, it is unclear if integrating PC into this problem poses any unique challenges, or if it is merely a straightforward "plug-and-play" approach.

 2) The method lacks a concise, high-level summary, making it difficult to follow. Nowhere in the methodology section is it explicitly explained how PC is integrated with different generative models. Based on my understanding, the authors use PC to learn the distribution of latent codes to match a reference distribution. However, the description of this approach is vague, with statements like "The training algorithm is the same as the previous case" or "An overview of the proposed method can be seen in Algorithm 1," which fail to provide sufficient detail.

- Limited Contribution: The paper’s contribution appears to be minimal, as it primarily focuses on applying PC to learn a set of latent codes without introducing substantial innovation or advancement beyond this.

- Inadequate Evaluation: The experimental evaluation is limited in scope, considering only a single dataset, a single attribute, and a single model. This restricted setup weakens the generalizability and robustness of the findings. Some other models should be considered such as Stable Diffusion or StyleGAN. Some attributes for face generation should be considered such as "BlackHair Young Smiling Moustache". 

- Lack of Analysis and Ablation Study: The paper does not include any analysis or ablation study that would help elucidate the specific effects and impact of the proposed method.

### Questions
N/A. The paper requires substantial revisions before it can be considered ready for publication. There are no possible response from the authors that could change my opinion.

### Soundness
1

### Presentation
1

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
This work presents a fair image generation approach using a pre-trained model and a small fair reference dataset. Overall, the idea of using a probabilistic circuit to manipulate the latent space to make a fair representation is unique. However, the work needs to be compared with state-of-the-art models, and the writing of the whole paper needs to be improved.

### Strengths
1. The proposed method only manipulates the latent space, thus taking less computational resources.
2. A critical finding in this work is that even if fair data is used to retrain pre-trained models, the resulting model still shows biased output.
3. Using a probabilistic circuit to transform the latent space to fair representation.

### Weaknesses
1. The introduction is not well organized
	1. Need some background of probabilistic circuits in the introduction before mentioning in the contribution sections.
	2. Use reference when making some claims, i.e.
		1. On page 1, line 47, "*Rather, the users and ML practitioners for downstream tasks may be interested in the distribution of the generated samples and ensuring that it is not biased with respect to some sensitive attributes*",  - add reference. 
2. In the proposed method, as the authors tried to manipulate the latent space using both latent space and sensitive attributes, a comparison should made with [1]; they also manipulate the latent space by minimizing the correlation distance between the sensitive and non-sensitive attributes. Besides this, the authors should also compare their work with more recent work [2].
3. The overall writing should be improved
	1. In the Related Works section, some examples of probabilistic circuit-based generative models should be given
	2. The author should also mention this work's limitations and future works

### References

[1] Liu, Ji, et al. "Fair representation learning: An alternative to mutual information." _Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining_. 2022.

[2] Teo, Christopher TH, Milad Abdollahzadeh, and Ngai-Man Cheung. "Fair generative models via transfer learning." _Proceedings of the AAAI conference on artificial intelligence_. Vol. 37. No. 2. 2023.

### Questions
1. Have you tried this proposed approach for fair tabular data generation?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes a scheme to help with fair image generation. The main idea is to introduce probabilistic circuits (PCs) to guide the model in generating fair images. A critical improvement is that the sensitive attributes of the fair dataset are introduced into the training of the PCs. The advantage of the method is that it is not required to retrain the generation model. Experimental results on CelebA show that the proposed method can improve the fairness of the gender distribution.

### Strengths
1. The method is a pluggable one that does not require retraining or special network architectures, which makes the method valuable for various tasks.

2. The background of the method is described in detail. Thus, readers can follow the idea easily.

### Weaknesses
For the contributions of this work, introducing PCs and introducing the sensitive attributes in PC training are the main improvements. However, there could be shortcomings in both contributions:

1. The former one may not provide a very overwhelming improvement since there are previous methods tried to introduce other models, as described in Sec. 2, while the PCs are also an existing method.

2. The latter contribution is not detailly described. The formal definition of the sensitive attributes $S$ is not clarified. Since it is determined by the sampling algorithm, it is not clear how to ensure that the PCs can correctly learn the attributes. In the experiments, the dataset is divided by the gender attribute. But among images of one gender, the other attributes could also be not fair.

For the experiments, it can be observed that the method works well on CelebA for gender fairness. However, there could be many other cases not evaluated:

1. The performance for some other attributes is not evaluated. For CelebA, attributes such as race, age, or hair color are not considered. The performance on different datasets, such as CIFAR-10 and LSUN, which contain more attributes is not evaluated. It may be necessary because the results can demonstrate that the PCs can process different attributes' features.

2. The performance for different models is not evaluated. Since one advantage of the method is that it is easy to apply without the requirement of retraining, experiments only on VQ-GAN may not be enough to prove its effectiveness. On the one hand, widely utilized GAN models, such as StyleGAN, should be considered. On the other hand, different generative models, such as VAEs, flow-based models, and diffusion models should also be considered.

### Questions
Based on the Weaknesses, I recommend the authors provide a more comprehensive analysis of the improvements. Meanwhile, more experiments should be conducted to support the assertion of the advantage. Additionally, there are some minor issues:

1. In lines 156-157, it seems that the fair dataset is $D_{fair}$ instead of $D_{bias}$.

2. In the tables, it may be better to use XX et al. (year) to represent previous methods rather than use (XX et al., year). (Please use \citet if you are using latex)

3. In Algorithm 2, the input train set is $D_{train}$ instead of $D_{val}$.

### Soundness
2

### Presentation
3

### Contribution
2
