# Disentangling Time Series Representations via Contrastive Independence-of-Support on l-Variational Inference

- Decision: Accept
- Avg Score: 5.67
- Scores: 1, 8, 8

## Abstract
Learning disentangled representations for time series is a promising path to facilitate reliable generalization to in- and out-of distribution (OOD), offering benefits like feature derivation and improved interpretability and fairness, thereby enhancing downstream tasks. We focus on disentangled representation learning for home appliance electricity usage, enabling users to understand and optimize their consumption for a reduced carbon footprint. Our approach frames the problem as disentangling each attribute's role in total consumption. Unlike existing methods assuming attribute independence which leads to non-identiability, we acknowledge real-world time series attribute correlations, learned up to a smooth bijection using contrastive learning and a single autoencoder. To address this, we propose a Disentanglement under Independence-Of-Support via Contrastive Learning (DIOSC), facilitating representation generalization across diverse correlated scenarios. Our method utilizes innovative \textit{l}-variational inference layers with self-attention, effectively addressing temporal dependencies across bottom-up and top-down networks. We find that DIOSC can enhance the task of representation of time series electricity consumption. We introduce TDS (Time Disentangling Score) to gauge disentanglement quality. TDS reliably reflects disentanglement performance, making it a valuable metric for evaluating time series representations disentanglement. Code available at https://institut-polytechnique-de-paris.github.io/time-disentanglement-lib.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper seems to be an application of disentangled representation learning for home appliance electricity usage. The authors propose to combine contrastive and variational losses. Unfortunately, the paper falls somewhere between methodological novelty and application, making it difficult to understand where the main contributions of the paper will lie. In general, I found the paper very hard to read.

### Strengths
The main strength of the paper is its approach to tackling the important problem of disentangled representation learning, which may contribute to reducing carbon footprint.

### Weaknesses
The paper seems to be an application of disentangled representation learning for home appliance electricity usage. The authors propose to combine contrastive and variational losses. Unfortunately, the paper falls somewhere between methodological novelty and application, making it difficult to understand where the main contributions of the paper will lie. In general, I found the paper very hard to read.

The paper lacks proper organization and has a tendency to include some unproven (or wrong) claims. For instance, in the introduction, the authors mention that "Disentanglement via VAE **can be achieved** by a regularization term of the Kullback-Leibler divergence[]," which is not necessarily true without certain strong assumptions and underlying conditions. The Beta-VAE paper has some qualitative evidence showing how the images are more disentangled compared to VAE. The authors also claim, "Rather than training separate auto-encoders for individual appliances," which requires empirical validation with proper citations. This claim is particularly problematic as it is not clear how the proposed method handles the multi-appliance scenario, especially when appliances have different activation patterns and power consumption profiles. Without a clear explanation of how the model distinguishes and disentangles these diverse signals, the claim lacks credibility.

In addition to these issues, the notations used are very confusing and are not defined before they are referenced. For example, in the proposed method section, the notation $z_m^+$ is used without description it. It is also unclear how it differs from $\bf{z}$ or $z$. The lack of clear definitions for these variables makes it difficult to follow the mathematical arguments and understand the proposed method's mechanics. The paper would benefit significantly from a dedicated notation section and a more rigorous definition of each variable before it is used.

The main goal of this paper remains unclear to me. For example, the authors mentioned, "The primary goals of this work are twofold: to effectively address the NILM problem and to obtain a disentangled representation of input data." However, it is unclear what the NILM problem is, what the nature of the input data is, and how the authors plan to achieve a disentangled representation that distinguishes itself from previous works. One issue might be that the problem statement and preliminaries are somewhat intertwined. The authors need to clearly define the NILM problem within the context of their work, specifying the exact nature of the input data (e.g., time series of aggregate power consumption) and how their approach builds upon existing methods. The current presentation leaves the reader unsure of the specific problem being addressed and the novelty of the proposed solution.

The color meaning used in the tables of result section is not clear. Even it is not clear how TDS (as a metric) has been compared with VAE and Beta-VAE in Table 1.

### Questions
- I strongly suggest the authors make their main contributions clear at the end of the introduction. 

- There is no related work section.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study explores disentangled representations for time series data, with a primary emphasis on achieving representation generalization across diverse, interrelated scenarios. They focused on a specific application of electric load monitoring application where computing different household appliances contribution in a total load is the task. 
In the context of Variational Autoencoders (VAE), this study draws inspiration from Roth et al., 2023, who addressed correlated attributes in an image processing context by replacing the independence constraint over attributes in the latent space (by a regularization term of the Kullback-Leibler divergence between the posterior of the latent attributes and a standard Guassian distribution), with the Hausdorff Factorized Support (HFS) assumption. The authors have adapted this idea for time series data and introduced the use of cosine similarity instead. Consequently, this approach no longer necessitates independent latent activations for different appliances. 
The main idea is to address appliance correlations with weakly supervised contrastive disentanglement, promoting similarity for the same appliances and dissimilarity for absent appliances in latent representations. This is achieved through a loss function composed of two terms, one for alignment based on correlation and another to minimize redundancy between latent variables.
In addition, the authors proposed l-variational inference layers with self-attention mechanism to address temporal dependencies. Additionally they propose a metric of  Time Disentangling Score (TDS) to evaluate the  disentanglement performance in time series data.

### Strengths
The paper presents several intriguing novelties.
1) Using pairwise similarity rather than independence assumption in VAE, to consider the correlated representations. 
2) l-variational inference layers with self-attention mechanism
3) A metric of  Time Disentangling Score (TDS) to evaluate the  disentanglement performance in time series data

 The authors have tackled a captivating problem, successfully adapting image processing techniques to the more complex domain of time series data.

### Weaknesses
The paper needs some modifications to make it easier to read (some suggestions given in the Questions).
The experimental results are very abstract (some suggestions in Questions part)
The application worth more explanation, the description lacks either an illustration or it is abstract.

### Questions
-Using cosine similarity instead of HFS needs more elaboration.

-Section 3.2 would benefit from a dedicated illustration demonstrating ATTENTIVE l-VARIATIONAL AUTO-ENCODERS, along with the corresponding notations used in the text.

-The authors have effectively presented the formulation for the usecase; however, in the experimental results, which I find somewhat abstract, there's a lack of a specific example illustrating how X and Y values for a time window are displayed, along with different rows of Y, etc.

-In section 4.1, should be included how exactly augmentation is performed and how many, it is very abstract now. 

-In Section 2, specifically concerning contrastive learning, the evaluation of appliance dissimilarity in "x" and "x-" is not explicitly clarified. Is labeling used for this purpose? What if the appliances are not the exact same but should exhibit similar behavior? How are such cases addressed? Additionally, the preparation of negative and positive samples is not detailed. Have you considered ensuring that there are no common or similar appliances in these two sets, and if so, how was this determined? Providing further explanation or an illustration could enhance the clarity of data preparation, which is a crucial aspect of the methodology.
-How many training examples did you use for linking?
“We link the learned latent representation to ground-truth attributes using a limited number of pair labels”
-After equation 2, In this test, the latent variable is represented as "z," which is defined as a matrix of dimensions (M + K) × dz, where "K" and "dz" should be introduced and define.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper discusses the importance of learning disentangled representations for Time Series data, specifically in the context of home appliance electricity usage. The goal is to enable users to better understand and optimize their energy consumption, thereby reducing their carbon footprint. The authors frame the problem as one of disentangling the role of each appliance (e.g., dishwashers, fridges) in total electricity usage.

Unlike existing methods that assume attributes (appliances in this case) operate independently, this work acknowledges that real-world time series data often show correlations between attributes. For instance, dishwashers and washing machines might be more likely to operate simultaneously during the winter season.

To address these challenges, the authors propose a method called DisCo (Disentangling via Contrastive), which employs weakly supervised contrastive disentanglement. This approach allows the model to generalize its representations across various correlated scenarios and even to new households. The method incorporates novel VAE layers equipped with self-attention mechanisms to effectively tackle temporal dependencies in the data.

To evaluate the quality of disentanglement, the authors introduce a new metric called TDS (Time Disentangling Score). The TDS proves to be a reliable measure for gauging the effectiveness of time series representation disentanglement, thereby making it a valuable tool for evaluation in this domain.

Overall, the paper argues that disentangled representations, particularly those achieved using their DisCo method, can enhance the performance in tasks like reconstructing individual appliance electricity consumption.

### Strengths
The method is very sound with mathmaticaly correct derivations. 
The addressed problem of disentagling latent factors in VAE type of models is very important.
Specifically, he paper addresses the unrealistic assumption of independence among generative attributes that is often present in traditional untangling methods. In contrast to these traditional approaches, DisCo focuses on recovering correlated data by encoding a wide range of possible combinations of generative attributes in the learned latent space.

The authors assert that simply encouraging pairwise factorized support in the latent space is sufficient for achieving effective disentanglement, even when data attributes are correlated. This is an important finding. 

In terms of performance, DisCo is shown to be competitive with downstream task methods, exhibiting significant improvements of over +60% across a variety of benchmarks in three different datasets undergoing correlation shifts (Finding 5.1). This is a strong aspect of the work.

Additionally, the capability of DisCo to adapt across correlation shifts leads to better out-of-distribution generalization, especially when these shifts are more severe. This fulfills one of the key promises of learning disentangled representations, which is to improve the model's robustness and generalizability.

### Weaknesses
I enjoyed the paper and did not find important weaknesses.

### Questions
Please discuss how sensitive the method is to hyperparameter selection.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
