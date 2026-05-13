# Disentangling data distribution for Federated Learning

- Decision: Reject
- Scores: 3, 5, 3, 6

## Abstract
\noindent Federated Learning (FL) facilitates collaborative training of a global model whose performance is boosted by private data owned by distributed clients, without compromising data privacy. Yet the wide applicability of FL is hindered by entanglement of data distributions across different clients. 
This paper demonstrates for the first time that by disentangling data distributions FL can in principle achieve efficiencies comparable to those of distributed systems, requiring only one round of communication. 
To this end, we propose a novel FedDistr algorithm, which employs stable diffusion models to decouple and recover data distributions. Empirical results on the CIFAR100 and DomainNet datasets show that FedDistr significantly enhances model utility and efficiency in both disentangled and near-disentangled scenarios while ensuring privacy, outperforming traditional federated learning methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this work, authors claim that a major challenge of federated learning is due to the entanglement of data distribution across clients. As a result, authors proposed a communication-efficient algorithm named FedDistr which decouples client data distributions into the different base distributions, and then the server merges the base distributions, finally a model trained over synthetic data generated following the base distributions. Authors perform numerical experiments to compare with several baseline federated learning algorithms and demonstrate FedDistr obtains better utility, communication, privacy trade-off.

### Strengths
1. Both communication cost and heterogeneity are important challenges in federated learning;
2. Authors verify the efficacy of the proposed algorithm through numerical experiments;
3. The proposed algorithm saves communication cost compared to baseline federated learning algorithms with little utility loss.

### Weaknesses
1. The paper is not well-motivated. In federated learning, heterogeneity is a more common term compared to the so-call disentanglement. Furthermore, in the first paragraph, authors claims 'There is a consensus that this inefficiency stems from the entanglement of data distribution across clients', can you provide references to this claim of 'consensus'. In fact, in the later part of the introduction, authors show that it is the disentanglement where classical FL algorithms like FedAvg does not perform well. The authors need to clarify the distinction between heterogeneity and their notion of 'entanglement' and provide stronger motivation for why disentanglement is the key challenge, rather than simply a manifestation of heterogeneity. The claim of consensus needs to be backed by specific references to the federated learning literature.
2. The proposed algorithm is not clearly introduced. Both Algorithm 1 and Section 4 only covers the parts until 'Activate Distribution Alignment', it seems there are steps after this in Figure 3 where clients generate data locally and train locally? Please explain more. The description of the algorithm is incomplete, lacking crucial details about how the synthetic data generation and local training are performed. The paper needs to provide a complete algorithmic description, including the data generation process using the diffusion model and the local training procedure, with clear mathematical formulations.
3. The claim of privacy preserving lacks rigorous discussion. How do you guarantee that the proposed algorithm does not leak user privacy. Roughly, the propose algorithm transfer cluster center of local datasets (in latent space) to the server, will this leak sensitive user information? The paper needs a more detailed privacy analysis. Transferring cluster centers, even in a latent space, could potentially reveal information about the client's data distribution. A rigorous privacy analysis, possibly using differential privacy or similar frameworks, is needed to support the privacy claims. The paper should discuss the potential privacy risks and provide a theoretical or empirical analysis of the privacy guarantees.

### Questions
Please see the weakness above and also the questions below:

1. How to do you plot figure 5? do you add noise somewhere to guarantee DP?
2. It seems the final training is performed over the so-called base distributions, in case of classification, is the learned model useful for the original client dataset?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel FedDistr algorithm, which employs stable diffusion models to transfer data distributions instead of model parameters between clients and the server. The theoretical and experimental results demonstrate the effectiveness of the proposed method. Overall, the paper is easy to understand, but I still have some concerns regarding the fundamental settings in federated learning and the risks of privacy leakage.

### Strengths
1. The paper is easy to follow.
2. The experiment results look good.

### Weaknesses
1. The proposed method may have the potential to leak privacy.
2. Some related work on methods that transmit knowledge instead of models between clients and the server may need to be reviewed and discussed.
3. There are some minor spelling and grammatical errors.

4. There are some grammatical errors.
   - “FL is hindered by entanglement of data distributions across different clients” —> “FL is hindered by **the** entanglement of data distributions across different clients”
   - “both disentangled base distribution” —>  “both disentangled base distributions”
   - “…for achieving ideal efficiency of federated learning…” –> “…for achieving **the** ideal efficiency of federated learning…” 
   - ”extract data distributions via stable diffusion model, and then upload these decoupled distributions to the server” —>  ”extract data distributions via **a** stable diffusion model and then upload these decoupled distributions to the server”
   - “The server actively identifies the orthogonal or parallel between the base distributions uploaded by clients and aggregate the orthogonal distribution once.” —> “The server actively identifies the orthogonal or parallel between the base distributions uploaded by clients and **aggregates** the orthogonal distribution once.”

5. In the reference “Numerous studies (… Li et al..),” the year is missing; it’s recommended to update the references.

6. It is better to adjust the formatting of the references. For example, ...
   - Use**\citet**: “Latent Diffusion Model (LDM) Ho & Salimans (2022)” —>“Latent Diffusion Model (LDM, Ho & Salimans, 2022) ” 
   - Use**\citep**“: The autoencoder Van Den Oord et al. (2017); Agustsson et al. (2017) “ —>  “The autoencoder (Van Den Oord et al., 2017; Agustsson et al., 2017) “
   - Use**\citep**“: LDM Ho & Salimans (2022); Liang et al. (2024)” –> “LDM (Ho & Salimans, 2022; Liang et al., 2024)” 

7. Some equations lack punctuation at the end, such as Eqs. (8), (9), (10) … 

8. Some minor spelling issues ：
   - “consisting solely of ’cat’ images, … ’dog’ images” —> “consisting solely of **\`cat\`** images, … **\`dog\`** images”. 
   - “Theorem 2. When the distributions of across K clients satisfy” —> “Theorem 2. When the distributions across K clients satisfy”
   - “We conduct experiments on two datasets: x‘CIFAR100 has the 20…” —> “We conduct experiments on two datasets: CIFAR100 has the 20…” 
   - “For DomainNet and CIFAR10, we regard…” —> “For DomainNet and CIFAR100, we …” 
   - “the era of large language models (LLMs) (), the time” —> “the era of large language models (LLMs) , the time” 

9. It is recommended to present Algorithm 1 in a single-line format to avoid confusing indentations and spacing.

10. In Section 4.3, each client $ k$ uploads the distribution parameters to the server, but the paper states that “the server does not have access to the sequence of the distribution parameters.” This seems contradictory.

11. The idea of transferring information contained in data rather than the data itself has been reflected in some previous works, such as methods based on distillation and those using data Mixup. It is recommended to include a review and discussion of similar methods in the paper, and ideally, to add these baselines in the experiments.

12. If clients and the server have information about the base distributions, can they infer the distribution information of other clients? Would this potentially lead to privacy leakage? It would be beneficial to include a discussion in the paper regarding the privacy and security implications of the proposed method.

### Questions
1. There are some grammatical errors.
   - “FL is hindered by entanglement of data distributions across different clients” —> “FL is hindered by **the** entanglement of data distributions across different clients”
   - “both disentangled base distribution” —>  “both disentangled base distributions”
   - “…for achieving ideal efficiency of federated learning…” –> “…for achieving **the** ideal efficiency of federated learning…” 
   - ”extract data distributions via stable diffusion model, and then upload these decoupled distributions to the server” —>  ”extract data distributions via **a** stable diffusion model and then upload these decoupled distributions to the server”
   - “The server actively identifies the orthogonal or parallel between the base distributions uploaded by clients and aggregate the orthogonal distribution once.” —> “The server actively identifies the orthogonal or parallel between the base distributions uploaded by clients and **aggregates** the orthogonal distribution once.”

2. In the reference “Numerous studies (… Li et al..),” the year is missing; it’s recommended to update the references.

3. It is better to adjust the formatting of the references. For example, ...
   - Use**\citet**: “Latent Diffusion Model (LDM) Ho & Salimans (2022)” —>“Latent Diffusion Model (LDM, Ho & Salimans, 2022) ” 
   - Use**\citep**“: The autoencoder Van Den Oord et al. (2017); Agustsson et al. (2017) “ —>  “The autoencoder (Van Den Oord et al., 2017; Agustsson et al., 2017) “
   - Use**\citep**“: LDM Ho & Salimans (2022); Liang et al. (2024)” –> “LDM (Ho & Salimans, 2022; Liang et al., 2024)” 

4. Some equations lack punctuation at the end, such as Eqs. (8), (9), (10) … 

5. Some minor spelling issues ：
   - “consisting solely of ’cat’ images, … ’dog’ images” —> “consisting solely of **\``cat‘’ **images, … **\``dog’’** images”. 
   - “Theorem 2. When the distributions of across K clients satisfy” —> “Theorem 2. When the distributions across K clients satisfy”
   - “We conduct experiments on two datasets: x‘CIFAR100 has the 20…” —> “We conduct experiments on two datasets: CIFAR100 has the 20…” 
   - “For DomainNet and CIFAR10, we regard…” —> “For DomainNet and CIFAR100, we …” 
   - “the era of large language models (LLMs) (), the time” —> “the era of large language models (LLMs) , the time” 

6. It is recommended to present Algorithm 1 in a single-line format to avoid confusing indentations and spacing.

7. In Section 4.3, each client $ k$ uploads the distribution parameters to the server, but the paper states that “the server does not have access to the sequence of the distribution parameters.” This seems contradictory.

8. The idea of transferring information contained in data rather than the data itself has been reflected in some previous works, such as methods based on distillation and those using data Mixup. It is recommended to include a review and discussion of similar methods in the paper, and ideally, to add these baselines in the experiments.

9. If clients and the server have information about the base distributions, can they infer the distribution information of other clients? Would this potentially lead to privacy leakage? It would be beneficial to include a discussion in the paper regarding the privacy and security implications of the proposed method.

### Soundness
3

### Presentation
3

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
The paper tackles the problem of heterogeneous federated learning by estimating the data distribution in a federated way. Specifically, it assumes that the global data distribution can be represented as a mixture of a set of base distributions, with local distributions varying from the global one in their mixture coefficients. The proposed approach uses diffusion models to disentangle data into base distributions and communicates these distributions using only a single round of communication.

### Strengths
- Novel application of diffusion models to disentangle and aggregate data distributions in federated learning.
- Demonstrates some improvements in communication efficiency and utility for specific datasets.

### Weaknesses
 - The approach is similar to previous approaches [1, 2] but does not discuss them.
- The theoretical results are questionable and assumptions are not clearly stated.
- The results seem to contradict previous theoretical results [1].
- The description of the approach omits important details, in particular, how the local models are trained and if local models can differ.
- The approach does not clearly address the impossibility result of federated learning under a mixture of distributions, as shown in [1].
- The paper does not adequately discuss the implications of one-shot distributed learning results [3] on their approach.
- The paper does not discuss the connection with one-shot federated learning for convex problems with robust aggregation [4].
- Lemma 2 appears to be incorrect, as the bound does not hold without further assumptions on the distributions $S$ and $\widehat{S}$. Specifically, the counterexample provided demonstrates that the expected loss cannot be bounded as stated.
- Theorem 1 relies heavily on the flawed Lemma 2, and its conclusion seems to contradict both the impossibility result in Marfoq et al. [1] and classical transfer learning results. If local tasks are independent, it is unclear how learning from each other is possible.
- The paper does not explicitly state that the theoretical results require finding the global risk minimizer, which is infeasible for non-convex problems like deep learning, thus limiting the practical applicability of the theory.
- The paper does not clearly explain how the model is trained on the estimated global distribution $\widehat{S}$, particularly how generating examples from $\widehat{S}$ leads to a good model if local distributions are disentangled.
- SCAFFOLD underperforms in the experiments, which is unexpected given its typical performance on heterogeneous FL tasks. The paper does not provide sufficient explanation for this discrepancy.

### Questions
- Marfoq et al. [1] provide an impossibility result that shows that federated learning under a mixture of distributions is impossible without further assumptions on the distributions. It seems that this result is applicable to your case. How can this be reconciled with your paper?
- Shamir and Srebro [3] show that one-shot distributed stochastic learning via averaging of parameters can be arbitrarily bad. How does this result relate to your work?
- It can be shown that one-shot federated learning is provably efficient for convex learning problems when using robust aggregation [4]. How does this relate to your approach?
- I have troubles understanding why Lemma 2 should be correct. It seems that without further assumptions on $S$ and $\widehat{S}$ we cannot bound the expected loss. Assume that under $S$ only $z$ has probability 1 and all others have probability 0 and that under $\widehat{S}$ some $z'$ has probability 1 and all others have probability 0. Now we can assume that $f(w,z)=0$ for all $w$ and for any number $C>2L\epsilon$, we can assume $f(w,z')=C$. Then the bound in Lemma 2 should not work. Did I understand an assumption wrongly? 
- The proof of Thm 1 heavily relies on Lemma 2. It basically says: if local distributions have nothing to do with each other, then we can estimate the global distribution from local distributions. Now with Lemma 2 this would imply that one can learn a good model on that. This not only seems to contradict the impossibility result in Marfoq et al., it also seems to contradict classical transfer learning results - if local tasks have nothing to do with each other, how can we learn from each other? 
- The paper does not state in the main text that for the theoretical results to hold, one has to find the global risk minimizer (as stated in the assumptions of Lemma 2). Since this is in practice infeasible for non-convex problems, such as deep learning, the paper should address the limitations of their theory.
- How is the model trained? Is it trained on the estimate of the global distribution $\widehat{S}$ by generating examples and training on them? How can such a model be good if local distributions are disentangled? 
- SCAFFOLD generally performs well on heterogeneous FL tasks; however, your results show it underperforms. Could you elaborate on potential reasons for this discrepancy and clarify whether experimental settings or parameters might have affected SCAFFOLD's performance?


References:

[1] Marfoq, Othmane, et al. "Federated multi-task learning under a mixture of distributions." Advances in Neural Information Processing Systems 34 (2021): 15434-15447.

[2] Wu, Yue, et al. "Personalized federated learning under mixture of distributions." International Conference on Machine Learning. PMLR, 2023.

[3] Shamir, Ohad, and Nathan Srebro. "Distributed stochastic optimization and learning." 2014 52nd Annual Allerton Conference on Communication, Control, and Computing (Allerton). IEEE, 2014.

[4] Kamp, Michael, et al. "Effective parallelisation for machine learning." Advances in Neural Information Processing Systems 30 (2017).

### Soundness
1

### Presentation
3

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
The paper proposes an one-shot method approach to federated learning by introducing the concept of “disentangling” distributions. The authors determine two distributions to be disentangled if given the same mixed distributions, the stochastic weight vector has a cosine similarity of 0. The authors theoretically support their approach via Theorems 1 and 2. The proposed algorithm, FedDistr, trains a Latent Diffusion Model which learns to generate distributions which are aligned in a central server. The alignment process uses the distribution parameters to determine orthogonal and parallel distributions for different clients; this is accomplished by solving an optimization problem on a weighted bipartite graph. The consolidated distribution parameters are broadcasted to all clients.

The work provides a good, singularly novel, idea, that of entangled/disentangled distributions and the creation of parallel/orthogonal sets of parameters. The body of the work relies heavily on the work of Liang et al. (2024), "Diffusion-Driven Data Replay: A Novel Approach to Combat Forgetting in Federated Class Continual Learning." Unlike in Liang et al., which thoroughly explains each step of their algorithm, the authors sweep factors underneath the rug. For example, Liang et al. state that the Latent Diffusion Model (LDM) is used to generate images at the edge which are used to train a classifier. The classifier, trained locally, is aggregated through the use of the traditional FedAvg algorithm. The authors of this paper do not clarify if they do or do not do this. It must be assumed by the reader that they do not, but one who reads the related work I have referenced will wonder if that is truly the case. In fact, I believe a re-organization and further clarifications would strengthen the paper significantly.  The authors did not reference Liang et al. and break down their work in the Related Works section; this is an obvious mistake as the two are without a doubt built on the same core with a minor, although interesting and significant, improvement. I believe it would be beneficial to the paper if the authors added a flow chart or table comparing/contrasting the work of Liang et al. and their work.

If the authors had more clearly explained how a final classifier is made, if one was even trained, I would be willing to increase the score. It would be prudent to add a subsection on how classification works, if a model is trained or not, and how one achieves a singular classification model used by all agents. I believe the paper has good merit but with further clarifications and much clear writing and flow, the paper would be much stronger than it currently is. A key problem with the writing is the authors are relying on too much prior knowledge rather than opting in for clarity and verbosity, both of which would make it a much better read with much clearer communication of ideas. Furthermore, I believe the experiments section needs to be clearer with regard to what was done. The additional, but few, comments in the Appendix mention the authors used subsets of the classes of the datasets; what does this mean and how is the data distributed to the agents? If 20 classes are used and 5 clients exist in your network, are you forcing each agent to have a different subset of the 20 classes to force heterogeneity? This further speaks to the overall lack of clarity in the writing and explanation provided by the authors. I would ask the authors to better explain their experimental setup and the associated variables. I would also ask the following: How many classes of each dataset were used in total? How were these classes distributed among the clients? Was heterogeneity artificially induced, and if so, how?

Overall, independently of the lack of clarity, I believe the paper is relevant to readers in the field of Federated Learning, as it proposes an interesting one-shot approach to heterogeneous federated learning. If possible, I would prefer to see the paper rewritten for clarity but the results and ideas are important enough to warrant acceptance.

### Strengths
The primary, and possibly only, strength of the paper is the ability to achieve high accuracy scores with only one communication round in a heterogeneous federated learning scenario; this, followed by theoretical support proved in the appendix, the authors proposed a unique solution to a commonly known problem in federated learning. The idea of disentangling the local data is original and significant.

### Weaknesses
The weaknesses of the paper are all indirectly related to their contribution. The writing lacks extreme amounts of clarity all around. The authors are not clearly explaining concepts and do not mention how extremely similar the core of their work is to Liang et al. (2024). They cited the paper in a small section of the paper, but it is much more significant than they lead the readers to believe and because of this it needs to be introduced in the related works section with a proper break down. The authors further fail to clarify if the ResNet classifier is trained and fused or if the one-communication step is only to learn to generate images and labels through the Latent Diffusion Model. These are important questions. Furthermore, there are several things to cover that I will double-up and put in the "Questions" section because I believe the authors need to answer them. Here they are:
1) In the experiments section, the authors did not explain the exact precisely enough what the federated architecture looks like. While stating that K=5,10,20, does this mean there are a total of K clients in the network and all K are used when training? It is typical to show results with a subset of the agents as the contributing agents in the learning step. For example, in the work that introduced FedAvg, the authors design a network with 100 agents and use subsets as the contributing agents when fusing models, such as 10 of the 100 are used to average their models together.
2) The authors also don’t clearly state what the distribution of the data looks like at the edge. While their proposed algorithm aim to disentangle the distributions, one wonders what the underlying initial distribution of data does to the result of the model. Perhaps the authors’ goal was to limit to cases of disentangled and nearly-disentangled, but it would be better to make this clear. Furthermore, of the subclasses of the datasets selected, how are those samples distributed? This is also not clearly defined.
3) The paragraph between eq 2 and 3 contains the unsubstantiated claim, other than their own claim on the matter via the presented “Theorem 1”: “Both theoretical analysis and empirical studies show that data heterogeneity is a blessing rather than a curse, as long as data distributions among different clients can be completely disentangled.” This claim needs to be supported by citations such that readers can confirm such a bold claim, which is commonly known to be a difficult hurdle for FL-algorithms to overcome.
4) In the paragraph between equation 10 and 11, the authors state the following: “To disentangle the data distribution for client k, the data is segregated based on these latent feature embeddings.” What exactly does this mean and how is this accomplished?
5) The second paragraph of section 4.3, “Active Distribution Alignment,” needs clarification on what it meant by “the server does not have access to the sequence of the distribution parameters.” Further, when the authors state “orthogonal and parallel data base distributions,” what does this mean?
6) The proofs in the appendix need more clarifications to be more clear and need grammatical cleaning (e.g., the proof of Theorem 1 has a "}" in the "exp( . )" above equation 7).

### Questions
I have a singular, but deep question that I need answered, because it is not at all clarified in the paper: Could you please clarify how a singular, global, classification model is obtained? In the referenced work of Liang et al., a clearly important reference as the authors have a very similar structure to the one presented, the authors learn to generate datasets and labels via the LDM, but further train a classifier in a FedAvg fashion. It seems to me that this work fixes the multiple-communication rounds used to learn the distribution parameters used to generate samples/labels at the edge, but speaks nothing about the classifier model itself.

The answer to this question is at the heart of the paper itself and needs to be answered. If a classifier is trained, how is it done? How does it perform on a test set that includes labels outside of the local training distribution? Does it require aggregation, as is typically done in federated learning?

### Soundness
2

### Presentation
2

### Contribution
2
