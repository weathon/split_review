# Federated Generative Learning with Foundation Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Existing approaches in Federated Learning (FL) mainly focus on sending model parameters or gradients from clients to a server. 
However, these methods are plagued by significant inefficiency, privacy, and security concerns. Thanks to the emerging foundation generative models, we propose a novel federated learning framework, namely \emph{Federated Generative Learning}. 
In this framework, each client can create \emb{} that are tailored to their local data, and send embeddings to the server. Then the informative training data can be synthesized remotely on the server using foundation generative models with these embeddings, which can benefit FL tasks.
Our proposed framework offers several advantages, including \textbf{increased communication efficiency}, \textbf{robustness to data heterogeneity}, \textbf{substantial performance improvements}, and \textbf{enhanced privacy protection}. We validate these benefits through extensive experiments conducted on 12 datasets. For example, on the ImageNet100 dataset with a highly skewed data distribution, our method outperforms FedAvg by 12\% in a single communication round, compared to FedAvg's performance over 200 communication rounds.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work introduces a novel federated learning framework called Federated Generative Learning, which addresses the inefficiency and privacy issues of existing solutions that transmit features, parameters, or gradients between clients and servers. In this framework, clients generate text prompts tailored to their local data and send them to the server, where informative training data is synthesized using stable diffusion. This approach offers enhanced communication efficiency, significant performance gains, and improved privacy protection, as demonstrated through extensive experiments on ImageNet and DomainNet datasets.

### Strengths
- This work proposes a novel learning framework to train local data without accessing the raw data directly.

- communication of prompts instead of model parameters addresses several issues of existing federated learning frameworks; high communication cost and potential privacy threats by attackers.

### Weaknesses
 - The proposed method may be highly dependent on the performance of both diffusion models and visual-captioning models.
  - An ablation study of varying the foundation models is needed.

- In a similar vein, the local training dataset should be unseen for pertaining foundation models and should be more difficult than ImageNet which is a standard image classification dataset. As mentioned in the Introduction section, the local training data are more likely to be privacy sensitive, so they are more likely to be unseen or not contained for pre-training foundation models such as BLIPv2 and Stable Diffusion. Evaluation on ImageNet or DomainNet implicitly uses the assumption that local data have a similar or subset domain to the pretraining dataset of foundation models, which are publically accessible or have no privacy issue.

- Clients in federated learning are often assumed to have limited capacity in memory or computation. Generating prompts using a large visual captioning model in each client is impractical.

### Questions
- The quality of synthetic data could be highly different according to domain discrepancy between the local training data and the pretraining data for the foundation model. Instead of using standard image classification datasets, does the proposed method work for federated learning on fine-grained classification such as CUB-200, Cars, and medical image datasets?

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- The main idea of the paper is to use prompts to “summarize” the client-side data in federated learning. These prompts are then sent to the central server and fed to a foundation generative model, with the hope that the generated data distribution is close to the client data distribution.
- With this idea, federated learning can be made one-round or few-round to drastically reduce communication costs, where clients can just send over the prompts one-shot to the server as the prompts and labels require very little communication.
- The paper then evaluates on several natural image datasets (subsets from ImageNet) and show that the proposed technique can match FedAvg in performance.
- The paper also performs some privacy analysis and shows that by transmitting prompts instead gradients/model updates/data, the membership inference attack success drops significantly.

### Strengths
- The proposed approach is interesting and novel to my understanding. Assuming the client data distributions can be well captured by the foundation generative model, the proposed technique can clear benefits in simplicity and reducing communication costs.
- Putting aside the underlying assumptions of the proposed techniques (see weaknesses), the paper is overall well-executed in terms of the diversity of the experiments and visualizations.
- The paper is generally well-written and easy-to-follow.

### Weaknesses
[W1] The main weakness of the proposed method is the underlying assumption that client data can, in fact, be generated by foundational models. This sound obvious but is key to the applicability of the proposed approach in practice. To put it bluntly, is the proposed solution searching for a problem?

1. Settings where FL is helpful—such as medical images across hospitals [1], user-generated text across mobile phones [2]—are often where the data distributions aren’t covered by the pre-training data of foundational models. The datasets used by the experiments are all natural image datasets (ImageNette, ImageFruit, etc.), which can be well-represented in the pre-training dataset of foundation generative models. I would appreciate results on non-natural image datasets. Specifically, the fine-grained nature of datasets like CUB-200 (birds) and Cars, while challenging, still fall within the scope of typical pre-training data for generative vision models. The paper should include more diverse datasets, such as those found in medical imaging or remote sensing, where the generative model's ability to capture the underlying data distribution is less certain.
2. In particular, if we consider horizontal FL settings (as with the paper), the server may even know about the possible classes / labels (e.g. federating binary classifiers) without communicating to the clients, in which case the “class-level prompts” may not be needed at all since the server can just generate images by itself. The paper overstates the necessity of class-level prompts, especially given that the server often has prior knowledge of the task's label space. The experimental section primarily uses class-level prompts, and the paper should more clearly discuss the limitations of this approach and the scenarios where it is less beneficial.

[W2]  More broadly, the threat model of the paper may need to be defined more clearly.

- What exactly is client privacy in this case? Can the client data be still considered “private” if you could already generate them with public foundation models (see also [3])? Does the privacy of the data lie in the pixels, or simply the description of the pixels? The paper's definition of client privacy is unclear. If the goal is to protect the pixel values of the training images, the proposed method may not be sufficient, as the prompts themselves could reveal significant information about the underlying data distribution. The paper should clarify whether the privacy concern is about the pixel values or the high-level information contained within the images.
- In many cases, the descriptions of the images can already be leaking privacy. If we apply the proposed method to cross-device federated learning on user’s photo data, the server could already learn a lot about the user data distribution and preferences. For example, following Sec 5.4 and Figure 6, knowing that a user have lots of golf photos (without knowing the pixels of the photos) already allows the FL service provider (e.g. Google) to sell targeted ads. The paper needs to address the potential for side-channel attacks, where even high-level descriptions of the data can reveal sensitive information. The paper should acknowledge that the prompts, even without pixel data, can leak user preferences and potentially enable targeted advertising or other privacy violations.

### Questions
- [Intro section] Why exactly does the proposed method provide robustness to data heterogeneity? Heterogeneity can still surface in the (instance-level) client prompts and subsequently the generated images.
- Minor comment: consider using different citation commands `\citet` , `\cite`, etc. in LaTeX to make the formatting of the in-text references consistent.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses efficiency and client-shift issues in federated learning by harnessing generative foundation models. Unlike traditional approaches that communicate model parameters, this work exploits clients to send instance-level or class-level prompts, generated by a pre-trained captioning model, to the server. The server aggregates these prompts to produce a proxy dataset via a pre-trained generative model, enabling standard federated learning on this dataset. The server then dispatches the refined weights back to the clients. Empirical evaluations underscore the efficacy of the proposed approach.

### Strengths
1. The proposed approach significantly reduces communication costs compared to traditional parameter transmission.
2. By leveraging foundation models to synthesize proxy data, the authors effectively mitigate the client-shift problem.
3. A variety of experimental settings across four datasets demonstrate the robustness and effectiveness of the proposed method.

### Weaknesses
1. The training framework is predominantly tailored for image datasets, limiting its applicability. The reliance on image captioning and generative models makes it unclear how this approach would generalize to other data modalities such as time-series data, or tabular data, where the concept of 'captioning' is not directly applicable. The method's dependence on specific pre-trained models also introduces a potential bottleneck, as the performance is highly contingent on the quality and availability of these models for different data types.
2. The method heavily depends on the congruence between the captioning and generative models, making it challenging to ensure the proxy dataset's distribution aligns with the private data. The quality of the generated proxy data is directly tied to the ability of the captioning model to accurately represent the client's data and the generative model to faithfully reconstruct it. Any bias or limitation in either of these models could lead to a significant discrepancy between the proxy data and the actual private data, potentially hindering the performance of the federated learning process. This is especially concerning in scenarios with highly heterogeneous client data distributions.
3. The experimental setup, with only five clients, may not adequately represent real-world scenarios; expanding the evaluation to include 50 or 100 clients could provide more insightful results. The limited number of clients does not fully capture the challenges associated with large-scale federated learning deployments, such as increased communication overhead, higher data heterogeneity, and potential client dropout. The performance of the proposed method might degrade significantly when scaled to a more realistic number of clients.
4. The comparison to a single baseline, FedAvg, falls short; including comparisons to advanced Federated Learning frameworks could better highlight the proposed method's effectiveness. While FedAvg is a common baseline, it is a relatively simple algorithm. Comparing against more sophisticated federated learning methods, such as those addressing client drift or incorporating personalized models, would provide a more comprehensive evaluation of the proposed method's advantages and limitations. The current comparison does not sufficiently demonstrate the superiority of the proposed method over state-of-the-art techniques.
5. Table 2 shows the proposed method outperforming centralized learning significantly; a thorough explanation of this phenomenon is warranted. The fact that a federated learning approach outperforms centralized training is counterintuitive and requires a detailed analysis. It is crucial to understand the specific factors contributing to this result, such as the nature of the proxy data, the initialization of the model, or any other aspect of the proposed method that might lead to such an outcome. Without a clear explanation, this result raises concerns about the validity of the experimental setup or the interpretation of results.

### Questions
1. I wonder if the approach cam be applied to other types of datasets, besides the image datasets.
2. What the experimental results would be when the number of clients becomes bigger, e.g., 100.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The Federated Generative Learning (FGL) framework offers a novel approach to federated learning, leveraging foundational generative models like Stable Diffusion to generate training data from prompts shared by clients. Clients contribute class-level or instance-level prompts, encapsulating key features of their local data. The server, in turn, amalgamates these prompts and synthesizes corresponding training data for global model training. This approach trims down communication costs since only concise prompts, and not bulky gradients or models, are transferred. This system also boasts robustness to data diversity and has demonstrated superior performance – with just one communication round, it outdid FedAvg's 200 rounds in accuracy. When trialed on skewed ImageNet100 distributions, FGL exceeded FedAvg's performance by 30% in just five communication rounds. Apart from being efficient, FGL also enhances privacy, as prompts reveal lesser private data than traditional methods. Evaluations confirmed no private data memorization in the synthetic images and an enhanced resilience against membership inference attacks. However, challenges persist with non-IID data, intricate domains, and the potential risks associated with prompts.

### Strengths
1.	Novel idea of using foundation models to synthesize training data for federated learning, enabling low communication costs and better privacy.
2.	Compelling experimental results demonstrating accuracy improvements over traditional FedAvg, especially with skewed data distributions.
3.	Thorough analysis and quantification of privacy benefits, showing reduced memorization and vulnerability to membership inference attacks.

### Weaknesses
1.	The evaluation of the Federated Generative Learning (FGL) framework is limited to simpler domains like ImageNet and doesn't extend to other areas, casting doubt on whether prompts can encapsulate complexity.
2.	While FGL aids in data generation for non-IID data, achieving congruence with a global distribution is yet to be addressed. 
3.	Security risks of prompts require more analysis. Could prompts be reverse-engineered to obtain private data?
4.	The framework hasn't been benchmarked against other federated learning methods that employ generative models.

### Questions
please refer to the weakness

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
