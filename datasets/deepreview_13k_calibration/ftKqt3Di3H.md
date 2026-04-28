# Text-Free Federated Transformers Knowledge Distillation Without GAN

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
Federated Learning (FL) is a distributed learning process designed to protect user privacy by avoiding the transmission of user data during communication while training a model. Many techniques aim to enhance the performance of models through knowledge distillation but lack data on the server side. To address this issue, Generative Adversarial Networks (GANs) are commonly employed to generate data for model distillation. The GANs approach faces numerous challenges in recent popular large-scale Transformer-based NLP tasks, such as structural mismatches in models, high computational complexity, and concerns regarding the privacy of client-generated text. Prior research has sought to enhance the process using auxiliary data to avoid the above issues, however, the selection of suitable data tailored to diverse tasks remains a challenging endeavor. To address the challenges posed by GANs and auxiliary data, this work proposes a lightweight approach that samples from the embedding structure of Transformers and learns a set of pseudo data for the distillation process, which draws inspiration from the concept of soft prompts. This lightweight approach does not require GANs or auxiliary data, incurs no communication overhead, and yields improved model performance with relatively lower computational costs on the server side. Our experiments yield superior results compared to methods that rely on auxiliary data on complex NLP tasks such as the SuperGLUE Benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the author propose a method to sample the embedding layer of transformer models and use for knowledge distillation in Federated Learning. The paper provides a good motivation to come-up with privacy preserving methods for knowledge distillation and identifies the gaps in GAN based methods.

### Strengths
This paper provides an interesting method to sample the embeddings of the transformer models for knowledge distillation in federated learning and thereby reducing the communication overhead and improving the accuracy.

### Weaknesses
The paper lacks crucial details regarding the proposed method, making it difficult to fully understand and reproduce. The abstract claims "This lightweight approach does not require GANs or auxiliary data, incurs no communication overhead, and yields improved model performance with relatively lower computational costs on the server side." However, the paper does not provide a clear explanation or empirical evidence of the claimed communication overhead savings. The comparison to FedAVG is not explicitly discussed, and the reader is left to assume the communication cost is similar, which is a significant oversight. The accuracy gains, while present, are moderate compared to FedAUX across different values of \alpha in the Dirichlet distribution. Therefore, a detailed analysis of the trade-off between communication cost savings and the additional computational cost at the server is needed to justify the method's practical value.

Furthermore, the ablation study is confusing. It is unclear how the numbers in Table 1 should be compared with the accuracy numbers in Table 3. The paper does not clarify the relationship between these tables, making it difficult to interpret the ablation study results. The observed decaying performance difference between FedDRS and other techniques in Table 1 with increasing \alpha is not adequately explained. The paper should provide a more thorough analysis of why this occurs and what it implies about the method's behavior under different data distributions.

### Questions
please see above.

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
This paper proposes a lightweight approach for knowledge distillation in federated learning without using GANs or auxiliary data. The approach samples from the embedding structure of Transformers and learns a set of pseudo data for the distillation process, resulting in improved model performance with relatively lower computational cost. The paper suggests that this approach can be applied to other large-scale NLP tasks beyond Transformers.

### Strengths
* The approach does not require GANs or auxiliary data, incurs no communication overhead, and yields improved model performance with relatively lower computational costs on the server side.
* The experiments conducted in the paper show that the proposed approach yields superior results compared to methods that rely on auxiliary data on complex NLP tasks such as the SuperGLUE Benchmark.

### Weaknesses
 * The challenge addressed in this paper may not be comprehensive. Although some papers utilize GANs to generate data for model distillation, it's important to note that GANs are not the sole method for data generation. Therefore, the scope of this paper appears to be limited.
* The assertion that "The GANs approach faces numerous challenges in recent popular large-scale Transformer-based NLP tasks" prompts the question: Were the models employed in the experiments considered large-scale?
* This paper does not specifically address the challenges associated with GAN-based methods for Federated Learning (FL) in its experimental section.
* Is this method applicable to other NLP tasks aside from text classification?

### Questions
See Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

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
This paper proposes a lightweight approach for knowledge distillation in federated learning (FL), particularly in the context of Transformer models. The authors address the challenges posed by Generative Adversarial Networks (GANs) and auxiliary data in FL by sampling from the embedding structure of Transformers and learning a set of pseudo data for the distillation process. This approach, called FedDRS, draws inspiration from the concept of soft prompts and does not require GANs or auxiliary data. It incurs no communication overhead and yields improved model performance with relatively lower computational costs on the server side.

The authors propose three methods for sampling from embeddings: random sampling, target sampling, and adversary sampling. They demonstrate that their approach outperforms methods relying on auxiliary data on complex NLP tasks such as the SuperGLUE Benchmark. The paper also presents ablation experiments that elucidate the unique advantages of models equipped with embeddings over those without embeddings, showcasing the efficiency and quality of sampling in embedding-enhanced models.

In summary, the paper introduces a novel text-free approach for knowledge distillation in federated learning, specifically for Transformer models. The proposed FedDRS method addresses the challenges posed by GANs and auxiliary data and yields improved model performance with lower computational costs.

### Strengths
### **Originality:**

The paper presents a novel approach for knowledge distillation in federated learning, particularly focusing on Transformer models. The proposed FedDRS method is unique in its text-free approach, which samples from the embedding structure of Transformers and learns pseudo data for the distillation process. This approach addresses the challenges posed by GANs and auxiliary data in FL, offering a creative combination of existing ideas.

### **Quality:**

The paper is well-written and provides a clear explanation of the proposed method. The authors demonstrate the effectiveness of FedDRS through experiments on the SuperGLUE benchmark, showing improved performance compared to methods relying on auxiliary data. The paper also includes ablation studies that elucidate the advantages of models equipped with embeddings.

### **Clarity:**

The paper is well-organized and presents its ideas in a clear and coherent manner. The authors provide a thorough explanation of the proposed method, its components, and the experimental setup. The results are presented in a clear and concise manner, making it easy for readers to understand the contributions of the paper.

### **Significance:**

The proposed FedDRS method addresses an important problem in federated learning, particularly in the context of Transformer models. By offering a lightweight approach that does not require GANs or auxiliary data, the method has the potential to advance the field of federated learning and improve the performance of Transformer models in FL settings. The paper also contributes to the understanding of the challenges posed by GANs and auxiliary data in FL, providing valuable insights for future research.

Overall, the paper presents a novel and creative approach to knowledge distillation in federated learning, focusing on Transformer models. The proposed FedDRS method demonstrates improved performance compared to existing methods and addresses the challenges posed by GANs and auxiliary data. The paper is well-written clear, and significantly contributes to the field of federated learning.

### Weaknesses
1. Privacy concerns (important): The paper does not address the potential privacy concerns arising from sampling from the model. The method involves extracting embedding information, which, while not directly text, could still be vulnerable to reconstruction attacks, potentially leaking sensitive information from the training data. The paper should explore and incorporate privacy-preserving measures, such as differential privacy or federated learning specific privacy techniques, to quantify and mitigate this risk. This is crucial for the practical deployment of the proposed method in privacy-sensitive scenarios.

2. Limited exploration of sampling methods: The paper focuses on three sampling methods (random, target, and adversary sampling) but does not explore other potential sampling strategies. The current sampling methods may not fully capture the diversity of the embedding space, and exploring techniques such as importance sampling, or methods that leverage the geometry of the embedding space could lead to further improvements in the performance of the proposed method. It's unclear if the current methods are optimal or if there are other more effective ways to generate pseudo-data.

3. Limited exploration of model architectures: The paper focuses on two Transformer models (RoBERTa and T5) but does not explore other popular Transformer architectures, such as BERT or GPT. The performance of the proposed method may vary across different architectures due to variations in their embedding spaces and training objectives. The paper should investigate the applicability of the proposed method to a broader range of Transformer models, including encoder-only, decoder-only, and encoder-decoder models, to demonstrate its generalizability. This would also help identify potential limitations or specific adaptations required for different architectures.

4. The illustration of Figure 1 seems chaotic.

### Questions
1. Although the authors mentioned about this weakness in the conclusion, it still requires some interpretation of how likely a generative model could leak private data. Therefore, I suggest authors add text inference attack experiments to show this risk. 
2. In Table 3, I am curious about the performance of Fedavg + random sample + adv. sample. I suspect that the improvement of including a target sample in MixSample is negelactble.

### Soundness
3 good

### Presentation
3 good

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
The paper addresses the challenges in Federated Learning (FL) for NLP tasks, specifically the complications arising from using GANs and auxiliary data. By leveraging the embedding structure of Transformers, the authors propose a novel method to generate pseudo data inspired by soft prompts. This approach sidesteps the need for GANs, reduces computational overhead, and outperforms auxiliary data methods on the SuperGLUE Benchmark.

### Strengths
This paper has a clear presentation.

### Weaknesses
* **Motivation.** The motivation of this paper did not convince me. It seems that the target problem is ambiguous and meaningless. The authors seem to just make a minor modification to replace GAN in FL's knowledge distillation for NLP tasks and it lacks motivations and scenarios. GAN is actually rarely used in NLP and NLP is also less studied in FL before. Not using GAN in NLP is trivial and common, which cannot be the main motivation. An appropriate motivation is the problems raised in actual scenarios and previous works, not the "a + b" pattern. Also, the authors think GAN will leak privacy and the proposed method can protect privacy, but the authors didn't provide evidence to support that point.
* **Novelty.** I think the proposed method is not novel. First, knowledge distillation is not a novel thing in FL. Second, such a design in Transformers is also not novel. 
* **Baselines.** The authors missed some important baselines in the experimental part, which weakens the validity of the proposed method. Specifically, the authors should compare the following methods in the experiments: [1] [2] [3].

### Questions
See the weakness above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
