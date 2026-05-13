# Who Leaked the Model? Tracking IP Infringers in Accountable Federated Learning

- Decision: Reject
- Scores: 5, 3, 8

## Abstract
Federated learning (FL) emerges as an effective collaborative learning framework to coordinate data and computation resources from massive and distributed clients in training.
Such collaboration results in non-trivial intellectual property (IP) represented by the model parameters that should be protected and shared by the whole party rather than an individual user.
Meanwhile, the distributed nature of FL endorses a malicious client the convenience to compromise IP through illegal model leakage to unauthorized third parties.
To block such IP leakage, it is essential to make the IP identifiable in the shared model and locate the anonymous infringer who first leaks it.
The collective challenges call for \emph{accountable federated learning}, which requires verifiable ownership of the model and is capable of revealing the infringer's identity upon leakage. 
In this paper, we propose
Decodable Unique Watermarking (DUW) for complying with the requirements of accountable FL.
Specifically, before a global model is sent to a client in an FL round, DUW encodes a client-unique key into the model by leveraging a backdoor-based watermark injection.
To identify the infringer of a leaked model, DUW examines the model and checks if the triggers can be decoded as the corresponding keys.
Extensive empirical results show that DUW is highly effective and robust, achieving over $99\%$ watermark success rate for Digits, CIFAR-10, and CIFAR-100 datasets under heterogeneous FL settings, and identifying the IP infringer with $100\%$ accuracy even after common watermark removal attempts.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a novel method to inject backdoor-based watermark to track IP infringers in the FL setting. Using an encoder-decoder framework, this paper encodes the client unique IDs into the federated model. Experimental results demonstrate the effectiveness of the approach.

### Strengths
1. This work addresses an important and timely problem, which is to not only inject watermarks to protect model IPs but also track the IP leakages in FL settings. 
2. The paper is well-written and easy to follow in general.

3. Experimental evaluations are comprehensive, covering a broad number of aspects and ablation studies.

### Weaknesses
1. The idea of using encoder-decoder framework to embed an identifiable string such as Labels is not new[1], therefore using encoder-decoder to identify client IDs, which is the main idea of this work, appears to be an straightforward extension and not very challenging. Experimental results in Table 1 also show perfect track score and high WSR_gap for all datasets, which seems to indicate that the underlining problem is not very challenging.  It is suggested that the authors provide more discussions on the unique challenges on identifying clients as compared to other identification problems. Specifically, the paper lacks a detailed analysis of why directly applying existing backdoor techniques to client identification fails, beyond a high-level mention of potential collisions. A more rigorous analysis, perhaps showing the distribution of trigger overlaps or the impact of such overlaps on identification accuracy, would strengthen this point. 

2. The proposed method is based on the assumption that the client set is known and therefore an ID string can be assigned. In reality client sets are dynamic, especially in cross-device FL settings. How will the proposed algorithm deal with dynamic increase or decrease of the client set? Also since the decoder's dimension is higher than the number of clients, will this create scalability problems when the number of clients grow very large (e.g. millions) ? The paper needs to address the practical limitations of the decoder's size, especially when the number of clients scales to realistic levels in federated learning. The authors should provide a theoretical analysis or empirical evidence on how the decoder's performance degrades with increasing client numbers, and discuss potential mitigation strategies.

3. The experimental results do not compare with other baseline methods. Are there any other backdoor watermarking approaches that worth comparing with? The paper should include a comparison with existing backdoor watermarking techniques, even if they are not directly designed for client identification. This would help to contextualize the performance of the proposed method and highlight its advantages and disadvantages compared to existing approaches. The lack of such comparison makes it difficult to assess the novelty and practical value of the proposed method.

### Questions
In Eq 6 and algorithm 1, \theta_k^f appears from nowhere without clear explanations. I suppose it is the feature exactor of \theta_k, is it correct?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The goal of this paper is to create a watermarking schema for federated learning. The watermark should not only be able to help us identify the stolen model but also indicate which client leaked the model. The essential requirements for the watermark are: (1) accurate IP tracking - identify the client who leaked the collaboratively trained model, (2) provide the confident output of the ownership verification and the identification of the client who leaked the model, (3) the injected watermark should not lower the quality of the model, (4) the watermark should not be easy to remove, e.g., by fine-tuning. The main method assumes that the central server watermarks the shared model before sending it to the clients by assigning to each client a separate dataset. The method is expensive on the server side when we consider millions or more clients.

### Strengths
1. The problem is valid. We want to find out who leaked the collaboratively trained model.
2. The usage of the encoder-decoder from Li et al. (2021b) to generate unique trigger sets for each client is an interesting solution to lower the burden put on the server (step 1 on page 4).

### Weaknesses
1.  Verification: "To achieve this goal, we first use our decoder D to replace the classifier h_s in the suspect model $M_s$, then the suspect model can be restructured as $M_s = (f_s , D)$" - this is the biggest flaw in the paper. It was claimed on page 3 that: "Shao et al. (2022) proposed a parameter-based watermarking method for FL called FedTracker. It inserts a unique parameter-based watermark into the models of each client to verify the ownership. However, all parameter-based watermarking requires an **inspection of the parameters of the suspect models, which is not applicable enough for many re-sale models**". However, this method also requires access to the parameters of the suspect model to replace h_s with D during the verification process. If this is not the case, then the authors should explain clearly how to decode the keys from the suspect model. The authors claim that their method is more applicable than parameter-based methods because the classifier h is just a linear layer without much pre-trained information. However, the core issue is not the complexity of h, but the fact that the method requires access to the internal structure of the suspect model to perform the replacement, which is a significant limitation.

1. The method is impractical for FL across devices where we can deal with millions or more clients. It assumes that "During each communication round, the server watermarks the aggregated global model using the client-wise trigger sets before dispatching the model." and it aims at a "traceable IP verification for accountable FL that can accurately identify the infringers among a **scalable** number of clients". It was remarked that the early training rounds can be skipped but only the first 20 out of a total 300 for CIFAR10 (beginning of page 7). Furthermore: " in order to avoid this pitfall, we have to ensure the uniqueness of both the triggers and target labels between different clients".  Overall, this method is excessively expensive for the server! The server needs to generate unique trigger sets for each client in every communication round, which is not scalable for a large number of clients. The authors mention that the watermark injection can be done in parallel, but the overhead of generating and managing these unique trigger sets remains a significant concern.

2. There can be a false positive if the client has some additional data from the data used for the watermarking and the potential watermark collisions between different clients. Although the authors claim 100% tracking accuracy, the possibility of collisions, especially with non-iid data distributions across clients, is not sufficiently addressed. The use of random noise or jigsaw for watermark injection does not guarantee that clients will not have data that shares similar characteristics, potentially leading to false positives.

3. The watermark is broken at the very core - if we test the ownership by sending the trigger sets produced for each client, then this requires a lot of queries. The need to test each client's trigger set against a suspect model makes the verification process inefficient and impractical, especially with a large number of clients. This approach requires a linear increase in the number of queries with the number of clients, which is a major drawback.

4. If there are many Sybils or colluding parties, they could use the same encoder from Li et al. (2021b) to embed the watermark. The method would detect the same watermark for many models, which would make the verification of the client that leaked the model impossible since it is not a single client that leaks the shared model. The authors argue that the watermark injection is done on the server side, but this does not prevent malicious clients from using the same encoder to embed their own watermarks, potentially causing confusion and making it difficult to identify the true source of a leak.

5. The authors did not release the source code so it is not possible to check the details of the method.


Minor comments:
- On page 5, Subsection 3.4 $M_s$ is used for both $(f_s , h_s )$ and $(f_s, D)$. 
- Figure 1 is too complex and difficult to understand here - what is the decoder?
- page 2 - method description - what is the pre-trained encoder?
- at the end of page 2: "our work can be summarized in four folds" - but you have only 3 contributions enumerated
- from the initial description on page 2 - it should be already explained how the watermark despite being produced per client by the server affects the aggregation of the model updates/parameters
- "distributed learning framework that enables massive and remote clients"  page 3 - what are the massive clients?
- page 2 or 3 - I would like to learn how big have to be the separate dataset/trigger sets $D_T$ for each client. How much additional data does the server have to prepare? How much different the datasets have to be for each client?
- "the server will inject a unique watermark for each client" - again, this exerts the whole work on the server - which is too big of an overhead.

### Questions
1. What is the exact setup for CIFAR10 and CIFAR100? How many clients? How many data points per client? What exact models / encoders / decoders are used?
2. How is the decoder used for the verification process?
3. Do you need to replace the classifier with the decoder for the verification?
4. Would you improve the notation? On page 5, Subsection 3.4 $M_s$ is used for both $(f_s , h_s )$ and $(f_s, D)$. 
5. Would you improve Figure 1? It it too complex but still does not explain how the method works. How does the decoder work?
6. Would you add the ablation study for the size of the key pool?
7. Why does fine-tuning increase the accuracy in Table 2 for Digits and CIFAR10? Why does accuracy drop for CIFAR100?

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
The authors present a watermarking scheme for FL that allows to clearly and reliably identify which client leaked the global model. The so-called DUW scheme follows a backdoor-based approach where, after each aggregation round, the global model is backdoored to produce a client-specific target label when using a special decoder instead of the classification head. The authors also propose an optimization that aims to preserve the utility of the actual model and works by limiting the distance between original and backdoored model. The evaluation on standard image classification tasks shows that the proposed method is incredibly reliable, robust against several watermarking removal methods, and still preserves a high accuracy compared to training without watermarking.

### Strengths
The paper is well written and accessible even for non-experts. Prior and related works are clearly described and important research gaps identified. The resulting scheme seems to be a practically viable solution without any obvious drawbacks that fulfils all desired properties. The evaluation is extensive and all questions I had in mind were answered with meaningful experiments, e.g., the robustness is properly checked against multiple watermarking removal approaches.

### Weaknesses
I cannot find serious weaknesses in this paper. A few suggestions to improve the presentations are made below.

The discussion of related work primarily mentions FedTracker as relevant prior work. However, there also exist further works such as Merkle-Sign by Li et al. (arXiv:2105.03167 / ICMEW'22) and FedCIP by Liang and Wang (arXiv:2306.01356).

The generation of the trigger sets based on the pre-trained encoder of Li et al is not really explained. It would be great to get some more details how the encoding of client keys into the dataset works.

Algorithm 1, instead of simply referring to Equations 6 and 1, should make it more explicit where some of the defined values such as the set D_T are being used.

Instead of providing only the final benchmark results after all rounds in Table 1, plots showing the evolvement over rounds would be interesting.

### Questions
- How does DUW compare to the above mentioned works?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
