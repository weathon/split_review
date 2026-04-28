# Learning with Preserving for Continual Multitask Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 5, 6

## Abstract
Artificial Intelligence (AI) drives advancements across fields, enabling capabilities previously unattainable. Modern intelligent systems integrate increasingly specialized tasks, such as improving tumor classification with tissue recognition or advancing driving assistance with lane detection. Typically, new tasks are addressed by training single-task models or re-training multitask models, which becomes impractical when prior data is unavailable or new data is limited. This paper introduces Continual Multitask Learning (CMTL), a novel problem category critical for future intelligent systems yet overlooked in current research. CMTL presents unique challenges beyond the scope of traditional Continual Learning (CL) and Multitask Learning (MTL). To address these challenges, we propose Learning with Preserving (LwP), a novel approach for CMTL that retains previously learned knowledge while supporting diverse tasks. LwP employs a Dynamically Weighted Distance Preservation loss function to maintain representation integrity, enabling learning across tasks without a replay buffer. We extensively evaluate LwP on three benchmark datasets across two modalities—inertial measurement units of multivariate time series data for quality of exercises assessment and image datasets. Results demonstrate that LwP outperforms existing continual learning baselines, effectively mitigates catastrophic forgetting, and highlights its robustness and generalizability in CMTL scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a new problem setting called Continual Multitask Learning (CMTL) and proposes a novel method called Learning with Preserving (LwP) to address it. CMTL is defined as a scenario where a model needs to learn multiple different tasks sequentially, with input data coming from the same distribution but each task having distinct label spaces. The proposed LwP method aims to preserve previously learned knowledge in the shared representation space without requiring a replay buffer of old data. It uses a novel Dynamically Weighted Distance Preservation (DWDP) loss to maintain the integrity of representations. Extensive experiments demonstrate LwP's strong performance and generalization abilities in CMTL scenarios.

### Strengths
1. A new continual learning setting is introduced.
2. A method tailored to the new setting is designed.

### Weaknesses
1. Compared to general CL scenarios, such as CIL, DIL (domainincremental learning), TIL (task incremental learning), the proposed CMTL setting can indeed be seen as an idealized simplified version. CMTL lets the input data come from the same distribution, which means that all tasks are performed on the same data domain, without considering the case where the data distribution drifts over time. In real-world applications, the data distribution of subsequent tasks may differ from the previous ones. This simplification limits the practical applicability of the proposed method in scenarios where domain shift is a significant factor. The assumption of a shared input distribution across tasks is a strong one, and the paper does not adequately address how the method would perform when this assumption is violated, which is common in real-world continual learning problems.
2. It is difficult to imagine how this setting could be implemented in reality. In actual scenarios, it might only be achievable by repeatedly labeling the same set of data with new labels. Even updating the data slightly would likely change its domain distribution. The paper does not provide a compelling real-world use case where the same data is repeatedly labeled for different tasks without any change in the underlying data distribution. This raises questions about the practical relevance of the proposed CMTL setting and whether it addresses a genuine need in the field.
3. The methods used for comparison are somehow out of date. The baselines used in the experiments, such as DER and DER++, while relevant, do not represent the current state-of-the-art in continual learning. There are more recent and advanced methods that could have been included to provide a more comprehensive evaluation of the proposed method's performance. The lack of comparison with these newer methods makes it difficult to assess the true contribution of the proposed approach.
4.The performance of LwP likely depends on careful tuning of the loss weights (λc, λo, λd). The paper does not provide sufficient detail on how these hyperparameters were chosen, and whether the reported results are robust to changes in these values. The sensitivity of the method to these hyperparameters is a potential weakness, as it may require significant effort to tune them for new tasks or datasets.

### Questions
Please refer to my comments in the 'Weakness' session.

### Soundness
3

### Presentation
3

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
This paper introduces Learning with Preserving (LwP), a novel framework designed for Continual Multitask Learning (CMTL), which involves learning different tasks sequentially while preserving shared representations. The paper evaluates LwP on three benchmark datasets across two modalities, demonstrating its competitive performance compared to existing continual learning methods.

### Strengths
1.	The paper proposes a new scenario of continual learning, CMTL, highlighting its unique challenges and significance in practical applications.
2.	The LwP framework is innovative in preserving previously learned knowledge in a way that remains applicable and beneficial across diverse tasks.
3.	The experimental results suggest that LwP demonstrates competitive performance compared to existing continual learning methods.

### Weaknesses
1.	How does the proposed method address the fundamental challenges in continual learning, such as catastrophic forgetting or the stability-plasticity dilemma?
2.	The Dynamically Weighted Distance Preservation (DWDP) loss is an innovative contribution. However, it would be valuable to delve deeper into the theoretical foundations of DWDP, exploring its relationship to other distance-preserving techniques and providing additional insights into why it is effective for preserving implicit knowledge.
3.	A point of concern is that, continuous learning methods in the comparison experiment are not state-of-the-art, and therefore may not effectively substantiate the validity of the method proposed in this paper.
4.	Further exploration is needed for more experimental settings, such as investigating the performance of a model when continuously learning five tasks in the presence of five base tasks.
5.	The section on the extension to learning problems (pages 19-20) provides a valuable insight into the theoretical underpinnings of LwP, but it could be integrated more seamlessly into the main body of the paper to enhance its readability and coherence.

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper aims to address the continual multi task problem. The paper proposes a LwP loss in addiction to current loss and loss to preserve old preditions. LwP tries to preserve the knowledge in the implicit knowlege space. The paper also propose to masks the loss on LwP if the labels are different and in that case it is not nessory to have this preserving loss. 

The paper then goes to evaulate this approch on various small scale benchmarks, and specilay on image datasets, it shows a clear gains over previous approches. The paper also shows the BWT metric for all the continual learning methods, and t-sne plots for the latent space.

### Strengths
Performance on all the benchmarks are impressive. Figure 5 clearly shows the minimal loss in performance in the previous tasks as the learning progress. 

the benifits of Learning with Preserving (LwP) loss as a regulaization is very solid, and can be seen on the figure 5 and table 1, and compared to other appoches LwP performs considerably well. 

the evaulation is done with a good coverage, with 3 vision benchmarks, and show the distributions of these latents in t-sne plots. the paper also measures the backward transfer values of the continual learning methods.

### Weaknesses
It is not clear, how this CMTL problem is novel, it is same as in early LwF papers, and the paper claims this is one of the contibutions. please adress this in the rebuttal. 

while the results are impressive, i am bit scaptical on the scale of the datasets, all have been trained on smaller scale and low resolution. would be nice to show some results on larger resolution images and models. Also would be nice to show that this approch can work for other archituctres like vit. I belive it should work without any problems. I still think resnet 18 is too small model in the current landscape to validate anything concretely.

Also there is not enough ablations to varify the contibutions of dynamic weighting, that would be helpful to validate this claim.

### Questions
please look at my strengths and weakness sections, and if you can adress the weakness section, i am happy to change my ratings.

### Soundness
1

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
This paper introduces Learning with Preserving (LwP), a novel approach to continual multitask learning (CMTL) that addresses limitations in traditional continual and multitask learning methods by preserving previously learned knowledge across diverse tasks. LwP employs a Dynamically Weighted Distance Preservation (DWDP) loss function, which maintains representation integrity for both prior and future tasks without relying on a replay buffer.

### Strengths
1. The idea is good - multi-task continual learning and is an essential problem in the space of continual learning.
2. The dynamic weighting is an interesting method, but a little ensure if pair-wise comparison is optimal when the dataset is big.
3. Adequate sets of experiments across various metrics.

### Weaknesses
1. Why does the authors consider three separate datasets and not a combination of them? The latter would be more representative of real-world scenarios.
Eg: first 3 tasks CelebA, next 3 tasks PhysiQ and so on, which is more representative of a realistic scenario.
2. How is Fig 2 visualized? what exactly it is meant to represent? Is this is a conceptual diagram, a visualization of actual data?

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
2

### Contribution
2
