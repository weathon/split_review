# Split-and-Denoise: Protect large language model inference with local differential privacy

- Decision: Reject
- Scores: 5, 3, 3, 8

## Abstract
Large Language Models (LLMs) excel in natural language understanding by capturing hidden semantics in vector space. This process enriches the value of text embeddings for various downstream tasks, thereby fostering the Embedding-as-a-Service (EaaS) business model. However, the risk of privacy leakage due to direct text transmission to servers remains a critical concern. To address this, we introduce Split-N-Denoise (SnD), an private inference framework that splits the model to execute the token embedding layer on the client side at minimal computational cost. This allows the client to introduce noise prior to transmitting the embeddings to the server, and subsequently receive and denoise the perturbed output embeddings for downstream tasks. Our approach is designed for the inference stage of LLMs and requires no modifications to the model parameters. Extensive experiments demonstrate SnD's effectiveness in optimizing the privacy-utility tradeoff across various LLM architectures and diverse downstream tasks. The results reveal an improvement in performance under the same privacy budget compared to the baselines by over 10\% on average, offering clients a privacy-preserving solution for local privacy protection.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the problem of privacy-preserving LLM inference in a setting where clients input text and a server holds the model. To address the privacy risk of direct transmission of clients' text to server, this paper splits an LLM between clients and a server such that:

1) Local computation: the client performs affordable computation locally to obtain intermediate results. In particular, only the token embedding is done on the client side to keep the computational cost low for clients. 

2) Privatising clients submissions: Differential privacy is employed to mitigate privacy leakage by injecting noises into the embedding before sharing with the server. In particular, each client adds noise to their embedding prior to sending them to the server to protect the privacy of clients while doing LLM inference;

3) Server-side computation: the server receives the noisy embedding, and performs the rest of the computations of the LLM and returns the noisy output to the client.

4) Client-side denoising: Each client performs denoising to improve the utility of the output. The denoise model is pre-trained on the server side using public datasets and synthetic noises, and subsequently shared with the client.

### Strengths
1) As opposed to the server-side denoising that has been used in the existing work, this paper performs the denoising at the client side to leverage the knowledge of noise levels and raw embedding. 

2) Evaluation of the proposed method through computing similarity between the clean and privatized embeddings, and performance on downstream tasks of sentence classification, pair similarity, Recognizing Textual Entailment

3) The problem of privacy-preserving LLM inference which is studied by this paper is an important problem as clients may input sensitive information, such as names, phones, and email addresses, that needs to be kept hidden from the service provider.

### Weaknesses
1) No evidence to support the practicality of the proposed method. This paper instantiates the denoising model as an L layer transformer-based model that receives the privatised token representations, noise matrix and noisy output computed by the server. Although this denoise model is pre-trained on the server side using public datasets and synthetic noises, each client needs to do the inference of this denoising model locally. Unfortunately, this paper does not empirically evaluate the memory and computational cost of this inference for clients. Therefore, it is not clear if this overhead is any smaller than running the whole LLM on the client side. This evaluation is necessary as one main claim of this paper is that the proposed method introduces only affordable local computations for clients.

2) No evidence demonstrating the privacy benefits of the proposed method. This paper lacks an empirical evaluation of the privacy leakage of the proposed method. This is particularly important as analytical privacy guarantees chosen by this paper are very loose for example see privacy budgets of 100, 500 and 1000 in the Tables provided in the experiment section.


3) Shallow discussion of results and not considering SOTA models. 

4) Experimental choices including hyperparameters and privacy budgets are not justified/studied and they are not consistent across models. The only statement regarding the choice of the privacy budget that I can see in the paper is the following: "For the three model families, we selected three distinct eta levels for experimentation, given the varying noise tolerance of each model. Specifically, for the Bert models, we set eta to 50, 100, and 500; for the GPT models, the values were 1, 100, and 1000; and for the T5 models, we chose 0.1, 1, and 10."


5) There are many typos:
  1) Missing "." at the end of captions
  2) Consequently, As a result,: As --> as
  3) known as ”embedding as a service”: ”embedding --> ``embedding
  4) this paper represents the pioneering effort in protect user’s: protect --> protecting
  5) Fact Kotonya & Toni (2020),Daily Dialogue: ,Daily --> , Daily

### Questions
I would recommend reporting the computational costs and privacy benefits of the proposed method. Please see my first and second concerns in the weakness box.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce Split-N-Denoise (SnD), a privacy-preserving scheme for LLMs.  SnD makes use of split learning, wherein the network is chopped in two and each half is distributed to the client and server, respectively.  SnD splits at the embedding layer, where local differential privacy (LDP) is applied to user embedding vectors for obfuscation.  Along with the embedding layer, the client side also contains a trained denoiser which, after the output embedding vectors are transmitted from the server, is used to denoise the response.  Several experiments are conducted demonstrating the efficacy of this work, compared to another method designed specifically for BERT (i.e., TokEmbPriv from Qu et al, 2021), across several models (BERT/DistillBert, T5, and GPT-2) for three classification tasks.

### Strengths
The problem of how to preserve-privacy in embedding-as-a-service applications is important with the influx of interest in LLMs.  Furthermore, the authors use of LPD provides certifiable privacy and, in the case of split learning, LDP is a very nontrivial task.  The presented framework makes sense in this context, although the overall approach could be better motivated.  For instance, why split at the embedding layer?  Splitting at this particular layer is the most unsecure, even for a simple man in the middle attack (given a pretrained foundation model).  However, splitting at any other layer and transmitting gradients naturally allows for federated learning strategies and the avoidance of DP altogether.  Furthermore, multi-party computation (MPC) methods do not have the encountered problem of trying to use DP with split learning (and properly denoising transmitted data).  A contrast and discussion of these various approaches is warranted.  Please see the following for a recent privacy-preserving MPC method:
Knott, Brian, et al. "Crypten: Secure multi-party computation meets machine learning." Advances in Neural Information Processing Systems 34 (2021): 4961-4973

### Weaknesses
# Autoregressive LLM concerns regarding the (only) use of GPT-2 and evaluation

The featured classification tasks do well to test the performance of BERT and T5.  However, they do not relevantly test the performance of GPT-2; in practice, GPT-2 does not perform well on classification tasks, which would ideally be handled by more appropriate encoder (e.g., BERT) or encoder-decoder (e.g., T5) architectures.  More relevant generative metrics, such as sentence completion (e.g., via HellaSwag), next-word-completion (e.g., via the lambada dataset), or even perplexity are required to show that GPT-2 performance is maintained.  Furthermore, - GPT-2 itself is an older model and was trained in a much less complicated manner compared to recently released (instruction-tuned) models, such as LLaMa-2, Falcon, Mistral, etc..  Testing on a more recent architecture is important to show the efficacy of this approach, to show that the more sophisticated pretrained knowledge (which naturally contains many more learned modalities/instructions compared to GPT-2) still behaves as expected, and to show different architectural choices are unaffected by the introduced noise (e.g., LLaMa uses RMSNorm vs GPT-2's Layernorm, which, relevant to the presented work, directly impacts how these models deal with noise variation in the data).

# Lack of: (a) comparison to other relevant privacy-preserving methods, (b) evidence against competitors infeasibility

Beyond TokEmbPriv, comparison is lacking to other relevant benchmark competitors.  E.g., due to the similarity of both approaches, a comparison to RAPT (Li et al. (2023)) is necessary.  Furethermore, for homomorphic encryption approaches, the authors claim:
> Cryptographic typically employs homomorphic encryption (HE) to compute the inference result of the users’ encrypted input. Unfortunately, the application of cryptographic technique is constrained by the significant computation overhead of cryptographic operations, especially on large transformer models.

To assert this claim, the proposed method and reference HE methods should be compared in terms of both accuracy, privacy-preserving ability, and wall-clock time.

# Inaccurate claims
> To the best of our knowledge, this paper represents the pioneering effort in protect user’s privacy during LLM inference with strong privacy guarantee. Existing research focuses on the privacy-preserving pre-training and fine-tuning for LLM, while few studies pay attention to the privacy concerns at inference stage, especially on privatizing user’s input to guarantee DP.

The homomorphic encrpytion work by Liu & Liu (2023); Chen et al. (2022) (cited in the paper) protects user privacy during inference, please withdraw or appropriately revise this claim.

Furthermore, the description of RAPT (which itself offers LDP for privacy-preserving LLM inference) is inaccurate:
> An alternative strategy might entail input text perturbation via textto-text privatization or synthetic data generation, preserving high-dimensional features while altering human-perceivable sequences Li et al. (2023). Specifically, the text\-to-text privatization projects text into a high-dimensional vector space with a pre-determined word embedding model,adding
carefully calibrated noise to the vector representation, and then reconvert it to obtain the perturbed
text Feyisetan et al. (2019); Qu et al. (2021a). Yet, the mere application of this technique during
inference does not guarantee a satisfactory balance between privacy and utility

This is a misleading description of the RAPT method from Li et al. (2023); RAPT performs LDP to user prompts (thus establishing certifiable privacy via DP).  In order to recover performance on the noisy data, RAPT employs prompt tuning to efficiently fine-tune a server-side model capable of performing inference on the LDP data.  This approach is extremely similar to the proposed split-and-denoise framework.  Please clearly describe RAPT and contrast it to SnP, while also benchmarking against it as a relevant competitor.

> Split learning Gupta & Raskar (2018); Vepakomma et al. (2018) ... DP is employed to mitigate privacy leakage by injecting noises into the IRs before sharing with the server.

Neither of the two papers use DP to certifiably protect the data.  Please cite another multi-party computation paper (where intermediate gradients are distributed across networks) which uses DP

# Lack of demonstrated efficacy against attacks

It is necessasry to prove the privacy-preserving capabilities of the presented approach, e.g., simulate eavesdropping attacks, which collect intercepted embedding vectors (during transmission to the server) for malicious actions (e.g., embedding inversion and attribute inference attacks).  Please see Li et al. (2023) for examples and more details.

### Questions
> We design a novel denoising method deployed on user side. In this approach, a denoise
model is pre-trained on server side using public dataset and synthetic noises. Subsequently,
this trained model is deployed on the user side, where it leverages the specific noise levels
and raw IRs provided by the user to enhance the embeddings.

Can the authors comment on how this necessarily opens up a large security hole? I.e., the data has noise injected to protect it in the event of interception by a bad actor.  However, this scheme requires the transmission of the actual denoising layer, which itself may be intercepted.  Due to the need for model refreshes, this problem is non-trivial.

> Split learning is a novel privacy-preserving approach in distributed learning
 
Please remove "novel", as it not being introduced in the presented work.

The benchmarked method, "TokEmbPriv," requires significantly more discussion during the background and previous work sections.

The paper requires an editing pass.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an approach of implementing local differential privacy to protect LLM inference. Specifically, a framework, SnD, is designed to enable the client to introduce noise prior to transmitting the embeddings to the server, and then denoise the output embeddings received from server, in a Embedding-as-a-Service scenario.

### Strengths
+ The study focuses on an interesting and important topic, the privacy in LLM.
+ The Embedding-as-a-Service business model is well-defined.

### Weaknesses
 - The overhead of proposed approach is not clear

My first concern pertains to the overhead introduced by the local encoder. While a basic complexity analysis is presented in Section 3.5, I would recommend a more comprehensive evaluation involving specific experiments. Such an evaluation is crucial to assessing the feasibility of the proposed approach. Furthermore, it remains unclear how the denoise model, pre-trained on the server, can adapt to varying noise levels determined by clients.

- Lack of details on baseline description

There is a lack of detail in the baseline description. The only information provided about the benchmark method is "where the token embeddings are perturbed by the user before sending them to the server". It would be beneficial to provide more information about TokEmbPriv and explain why this method was chosen as the sole benchmark in the evaluation. Additionally, it would be helpful to clarify why other methods, such as a vanilla model, were not considered in the comparison.

- The evaluation on denoise is somehow blur

The evaluation of the denoising process is somewhat unclear. Please explicitly state and explain why a higher Cosine Similarity score between the initial and recovered embeddings is indicative of better performance. Also, please provide a clear definition of what "initial embeddings" refer to. If they pertain to the embeddings input to the denoise module, i.e., the "output noised results" in Figure 1, it currently reads as though having fewer differences between the initial and recovered embeddings is preferred, which might lead to less noise added. Additionally, the evaluation appears to focus solely on accuracy and does not provide results on privacy protection. Given that the primary motivation of the study is addressing the "unaddressed risk of privacy leakage," the privacy performance of the proposed approach is expected and should be included in the evaluation.

### Questions
1. What is the overhead of the proposed approach?
2. Why TokEmbPriv is chosen as the sole benchmark in the evaluation?
3. What is the privacy performance of the proposed method?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a framework for achieving private Large Language Model (LLM) inference. The framework combines dx-privacy-based relaxed local Differential Privacy (DP), U-shape split inference, and a client-side denoiser based on the Transformer architecture. This innovative approach delivers efficient computation, privacy guarantees, and strong utility for private LLM inference. The paper demonstrates the effectiveness of the proposed framework using four datasets and three different architectural configurations. The results illustrate that the model maintains high utility while preserving a substantial privacy budget, with minimal computational complexity overhead.

### Strengths
1. The proposed work intelligently integrates split inference, relaxed local DP, and client-side post-processing with a denoiser.
2. The location of the denoising model at the client side, which leverages knowledge of the noise level, is crucial for effective denoising.
3. The paper provides a well-analyzed discussion of complexity.
4. The potential for several extension works pointed out in this work is interesting.

### Weaknesses
1. Recent work by "Mattern et al. - The Limits of Word Level Differential Privacy" has pointed out limitations of dx-privacy. The author should address these weaknesses and concerns related to dx-privacy in the paper. Specifically, the paper should discuss the implications of the linear growth of the privacy budget with the length of the input sequence, and how this impacts the overall privacy guarantees, especially for longer text inputs. Furthermore, the paper should address the lack of syntactic changes that dx-privacy provides, and how this could potentially leak information about the original text.
2. The denoise model is pre-trained and known by the server. Could the server utilize the Denoise model to obtain less noisy user embeddings and potentially compromise privacy? This issue should be explored. The paper should provide a more detailed analysis of the potential for the server to exploit the denoising model, even if it does not have access to the specific noise matrix, to infer information about the user's input. This should include a discussion of the types of attacks that might be possible and how the proposed framework defends against them.
3. The impact of knowing the noise level or not should be more thoroughly analyzed. The paper should include a more rigorous analysis of the sensitivity of the denoising performance to the accuracy of the noise level estimation. It should also explore the implications of using an incorrect noise level, both in terms of utility and privacy.
4. The paper does not adequately demonstrate the privacy aspects regarding textual input. There is a lack of evidence that the proposed method can effectively defend against potential inversion attacks compared to an unprotected scheme. The paper should include a more thorough evaluation of the privacy guarantees, particularly against embedding inversion attacks. This should include a quantitative analysis of the success rate of such attacks under different privacy budgets.
5. The paper creates some confusion due to the mixed usage of "eta" in both its symbol and word forms.
6. There is a typographical error: "under varying η in table 4.3.1, 4.3.1 and 4.3.1."

### Questions
1. How does the Performance on selected benchmarks compare to SoTA?

2. What does eta mean for privacy? Why can it be set differently for GPT, Bert, and T5 models?

3. Can this be extended to training (finetuning)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
